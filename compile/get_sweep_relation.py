import os
import re

def extract_clock_relationship_summary(input_dir, output_file):
  """
  指定したフォルダ (サブフォルダも含む) の *.timing.rpt を探して開き、

  ---------- 2. Clock Relationship Summary (begin) ----------
  ---------- Clock Relationship Summary (end) ---------------

  で囲まれたテキストを抜粋し、output.rpt に出力します。
  *.timing.rpt が複数見つかった場合は、すべての *.timing.rpt から上記ブロックを抜粋し、ひとつの output.rpt に結合します。

  Args:
    input_dir: 入力フォルダ
    output_file: 出力ファイル
  """

  with open(output_file, 'w') as output:
    for root, dirs, files in os.walk(input_dir):
      for filename in files:
        if filename.endswith('.timing.rpt'):
          filepath = os.path.join(root, filename)
          with open(filepath, 'r') as input:
            text = input.read()
            match = re.findall(r'Clock Relationship Summary \(begin\)(.*?)Clock Relationship Summary \(end\)', text, re.DOTALL)
            if match:
              output.write(f'## {filepath}\n')
              output.write('\n'.join(match))
              output.write('\n\n')

if __name__ == '__main__':
  input_dir = './'
  output_file = './output.rpt'
  extract_clock_relationship_summary(input_dir, output_file)

