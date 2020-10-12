# -*- coding: utf-8 -*-
"""
Bulk files decoding in directory and subdirectories with specified encoding,
extension and confidence using chardet and tempfile
"""
import os
import sys
import chardet
import tempfile
import argparse


def bulk_decode(dir_path, target_encoding, extensions, confidence_threshold):
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            temp_name = ''
            filename = os.path.join(root, file)
            if extensions != '*':
                file_extension = os.path.splitext(filename)[1]
                if file_extension not in extensions:
                    continue
            with open(filename, 'rb') as f:
                content_bytes = f.read()
                detected = chardet.detect(content_bytes)
                encoding = detected['encoding']
                confidence = detected['confidence']
                print("{}: detected as {} with confidence {}.".format(filename, encoding, confidence))
                if confidence < float(confidence_threshold) or encoding == target_encoding:
                    print("{} skipped.".format(filename))
                else:
                    content_text = content_bytes.decode(encoding)
                    with tempfile.NamedTemporaryFile(mode='w', dir=os.path.dirname(filename),
                                                     encoding=target_encoding, delete=False, newline='\n') as f:
                        f.write(content_text)
                        temp_name = f.name
            if temp_name != '':
                os.replace(temp_name, filename)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir_path', help='directory to be decoded', default='./')
    parser.add_argument('--target_encoding', help='target encoding after decoding', default='utf-8')
    parser.add_argument('--extensions',
                        help='extensions of files in directory to be decoded,' +
                             'can be specified with a comma, e.g. - .cpp, .h' +
                             'all files will be decoded by default',
                        default='*')
    parser.add_argument('--confidence', help='confidence of encoding treshold', default='0.7')
    args = parser.parse_args()
    bulk_decode(args.dir_path, args.target_encoding, args.extensions, args.confidence)
    return 0


if __name__ == '__main__':
    sys.exit(main())
