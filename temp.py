import re

decode_text = '"""\nhello world\n"""\nhello\nif'

# Find the last occurrence of \n and remove everything after it
last_newline_index = decode_text.rfind('\n')
if last_newline_index != -1:
    processed_texts = decode_text[:last_newline_index]
    type = decode_text[last_newline_index + 1:]
else:
    processed_texts = decode_text

print("原始处理结果:")
print(processed_texts)

# Extract content inside and outside triple quotes
docstring_pattern = r'"""\n(.*?)\n"""\n'
docstring_matches = re.search(docstring_pattern, decode_text, re.DOTALL)

# Extract content outside triple quotes
content_outside = re.sub(docstring_pattern, '', decode_text, flags=re.DOTALL).strip()

# 也可以分别处理处理后的文本
print("\n处理后文本的分离结果:")
docstring_matches_processed = re.findall(docstring_pattern, processed_texts, re.DOTALL)[0].strip()
content_outside_processed = re.sub(docstring_pattern, '', processed_texts, flags=re.DOTALL).strip()

print(docstring_matches_processed)
print(content_outside_processed)
print(type)