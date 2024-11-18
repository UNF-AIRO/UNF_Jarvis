def Get_Function_Details() -> list[dict[str, any]]:
    functions: list[dict[str, any]] = [{
        "type": "function",
        "function": {
            "name": "Open_Webpage",
            "description": "This function opens a browser window to the given URL. Returns 'Success' if successful, 'Failed' if not.",
            "parameters": {
                "type": "object",
                "properties": {
                    "url": {
                        "type": "string",
                        "description": "The URL to open.",
                    }
                },
                "required": ["url"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "Write_Code_Snippet",
            "description": "This function writes the given code snippet to a file named 'Code_Snippet.py'. Returns 'Success' if successful, 'Failed' if not.",
            "parameters": {
                "type": "object",
                "properties": {
                    "codeSnippet": {
                        "type": "string",
                        "description": "The code snippet to write.",
                    }
                },
                "required": ["codeSnippet"]
            }
        }
    }]

    return functions

def Open_Webpage(url: str) -> str:
    import webbrowser
    return 'Success' if webbrowser.open(url, new=1) else 'Failed'

def Write_Code_Snippet(codeSnippet: str) -> str:
    try:
        with open('Code_Snippet.py', 'w') as file:
            file.write(codeSnippet)
        return 'Success'
    except Exception as e:
        return f'Failed: {e}'