import re
import warnings

def extract_c_code_block(text):
    if "assistant" in text.lower():
        assistant_idx = text.lower().find("assistant")
        text = text[assistant_idx + len("assistant"):].strip()
    
    c_code_pattern = r'```c\s*(.*?)\s*```'
    match = re.search(c_code_pattern, text, re.DOTALL)
    if match:
        # Remove free() statements from C code
        c_code = match.group(1).strip()
        c_code = re.sub(r'\s*free\s*\([^)]*\)\s*;?\s*', '\n', c_code, flags=re.MULTILINE)
        
        # Check if assert.h is included, if not add it at the beginning
        if '#include <assert.h>' not in c_code and re.search(r'\bassert\s*\(', c_code):
            c_code = '#include <assert.h>\n' + c_code
        
        return c_code
    else:
        warnings.warn("No C code block found in the generated text. Returning empty string.")
        return None
    
if __name__ == "__main__":
    # Example usage
    example_text = """
    Here is some C code:
    ```c
    #include <stdio.h>
    void foo() {
        int *ptr = malloc(10 * sizeof(int));
        // Some operations
        assert(ptr != NULL);
        free(ptr);
    }
    ```
    """
    print(extract_c_code_block(example_text))