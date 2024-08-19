# vim: set ts=4 sts=0 sw=4 si fenc=utf-8 et:
# vim: set fdm=marker fmr={{{,}}} fdl=0 foldcolumn=4:

import argparse
import logging
import pandas as pd

from functools import partial
from sys import stdout
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain


def getargs():
    parser = argparse.ArgumentParser()
    parser.add_argument('--narrs')
    parser.add_argument('--template')
    parser.add_argument('--question')
    parser.add_argument('--output')
    return parser.parse_args()


def get_logger(sname, file_name=None):
    logger = logging.getLogger(sname)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s " +
                                  "- %(message)s", datefmt='%Y-%m-%d %H:%M:%S')
    handler = logging.StreamHandler(stdout)
    if file_name:
        handler = logging.FileHandler(file_name)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


def getcreds():
    with open('creds/creds.txt', 'r') as f:
        out = f.readline().strip()
    return out


def read(filename):
    with open(filename, 'r') as f:
        out = f.readlines()
    return ''.join(out).strip()


class QuestionAnswerer():

    """Query individual documents with yes or no questions."""

    def __init__(self, model, prompt, logger):
        self.chain = prompt | model

    def ask(self, document, query):
        try:
            ans = self.chain.invoke({'narrative': document, 'question': query})
            return ans.content
        except Exception as e:
            return 'API error'


def import_narratives(filename):
    km0 = pd.read_parquet(filename,
                          columns=['caseno', 'incident_id',
                                   'fileids', 'narrativa'])
    return km0[km0.narrativa.notna()]


if __name__ == '__main__':
    args = getargs()
    logger = get_logger(__name__)
    logger.setLevel(logging.DEBUG)


    model    = ChatOpenAI(openai_api_key=getcreds(), temperature=.5)
    prompt   = ChatPromptTemplate.from_template(read(args.template))
    db       = QuestionAnswerer(model, prompt, logger)
    question = read(args.question)
    narrs    = import_narratives(args.narrs)

    narr2ind = partial(db.ask, query=question)
    logger.info(f"question: {question}")

    logger.info("starting round 1")
    narrs['answer1'] = narrs.narrativa.apply(narr2ind)
    logger.info("starting round 2")
    narrs['answer2'] = narrs.narrativa.apply(narr2ind)
    logger.info("starting round 3")
    narrs['answer3'] = narrs.narrativa.apply(narr2ind)

    narrs.to_parquet(args.output, index=False)


# done.
