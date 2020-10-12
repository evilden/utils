# bulk-files-decoder
Bulk files decoding in directory and subdirectories with specified encoding,  extension and confidence
### Requirements
 - Python 3
 - Installed chardet, tempfile for Python 3
### Usage
You can just specify directory and target encoding(utf-8 by default)
```
python bulk_files_decoder.py --dir_path=my_src_dir --target_encoding=utf-8
```
You can specify file extensions separated by comma
```
python bulk_files_decoder.py --dir_path=my_src_dir --target_encoding=utf-8 --extensions=.cpp,.h
```
For more details
```
python bulk_files_decoder.py -h
```
