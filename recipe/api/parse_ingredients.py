#!/usr/bin/env python3

import argparse
import json
import sys
import subprocess
import tempfile
import os

from ingredient_phrase_tagger.training import utils
MODEL_PATH = 'recipe/api/20200720_2006-nyt-ingredients-snapshot-2015-461547e.crfmodel'


def _exec_crf_test(input_text, model_path):
    with tempfile.NamedTemporaryFile(mode="w+") as processed_file:
        processed_file.write(utils.export_data(input_text))
        processed_file.flush()
        return subprocess.check_output(
            ['crf_test', '--verbose=1', '--model', model_path,
             processed_file.name]).decode('utf-8')


def _convert_crf_output_to_json(crf_output):
    # return json.dumps(utils.import_data(crf_output), indent=2, sort_keys=True)
    return utils.import_data(crf_output)


def parse(input_arr):
    # raw_ingredient_lines = [x for x in sys.stdin.readlines() if x]
    crf_output = _exec_crf_test(input_arr, MODEL_PATH)
    return _convert_crf_output_to_json(crf_output.split('\n'))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='Ingredient Phrase Tagger',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-m', '--model-file', required=True)
    parser.add_argument('-f', '--input-file', required=True)
    main(parser.parse_args())
