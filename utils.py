# --- Prompt Engineering ---

def prettify(results):
    global_output=""
    for result in results:
        output = f"Source: {result[0].metadata['source']}\n"
        output += f"Page: {result[0].metadata['page']}\n"
        output += "Content:\n"
        output += str({result[0].metadata['chunk_content']})
        output += "\n"
        output += "=" * 80
        output += "\n"
        global_output += output
    return global_output