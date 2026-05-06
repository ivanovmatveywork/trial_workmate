import argparse

from app import start


parser = argparse.ArgumentParser()
parser.add_argument('--files', type=str, nargs='+', required=True)  # Переменная с директориями файлов
parser.add_argument('--report', type=str, required=True)            # Переменная с названием отчета
args = parser.parse_args()

files_path = args.files
report_name = args.report

start(files_path=files_path, report_name=report_name)
