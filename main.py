# import textwrap
# from llama_cpp import Llama
#
# llm = Llama(
#     model_path="./codellama-7b-instruct.Q4_K_M.gguf",
#     n_ctx=2048,
#     n_gpu_layers=-1,
#     verbose=False,
# )
#
#
# def full_prompt(sys: str, prompt: str) -> str:
#     return textwrap.dedent(
#         f"""
#         [INST] <<SYS>>
#         {sys}
#         <</SYS>>
#
#         {prompt} [/INST]
#
#         ```python
#         """
#     ).strip()
#
#
# def llama_output(full_prompt):
#     return llm(
#         full_prompt,
#         max_tokens=256,
#         stop=["</s>", "```"],
#         echo=False,
#     )
#
#
# def main():
#     system_message = "You are an expert Python programmer. Your sole task is to generate a single, complete, runnable Python script that satisfies the user's request. Output ONLY the code, with no explanations, comments, or markdown formatting outside of the code block itself."
#
#     user_prompt = input("Prompt: ")
#     output_file = input("Output file: ")
#
#     output = llama_output(full_prompt(system_message, user_prompt))
#
#     code: str = output["choices"][0]["text"]
#
#     with open(output_file, "w") as f:
#         f.write(code)
#
#
# if __name__ == "__main__":
#     main()

import argparse
import sys
import textwrap
from llama_cpp import Llama

try:
    llm = Llama(
        model_path="./codellama-7b-instruct.Q4_K_M.gguf",
        n_gpu_layers=-1,
        n_ctx=2048,
        verbose=False,
    )
except Exception as e:
    print(f"Error: Failed to load the LLM model. {e}", file=sys.stderr)
    sys.exit(1)


def create_full_prompt(sys_msg: str, user_prompt: str) -> str:
    return textwrap.dedent(
        f"""
        [INST] <<SYS>>
        {sys_msg}
        <</SYS>>

        {user_prompt} [/INST]
        
        ```python
        """
    ).strip()


def main():
    parser = argparse.ArgumentParser(
        description="~local~ vibe coder: Generate a complete Python script from a natural language prompt.",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument(
        "prompt", type=str, help="The user prompt describing the code to generate."
    )
    parser.add_argument(
        "-o", "--output", type=str, help="The output file name.", default="output.py"
    )
    args = parser.parse_args()

    system_message = (
        "You are an expert Python programmer. Your sole task is to generate a single, complete, "
        "runnable Python script that satisfies the user's request. Output ONLY the code, with no "
        "explanations or text outside of the code block. The script must be ready to run as-is."
    )

    full_prompt_str = create_full_prompt(system_message, args.prompt)

    print(f"Vibe received. Generating code for '{args.output}'...", file=sys.stderr)

    try:
        output = llm(
            full_prompt_str,
            max_tokens=1536,  # Increased for larger scripts
            stop=["</s>", "```"],
            echo=False,
        )
        code = output["choices"][0]["text"].strip()
    except Exception as e:
        print(f"Error: Failed during model inference. {e}", file=sys.stderr)
        sys.exit(1)

    try:
        with open(args.output, "w") as f:
            f.write(code)
        print(f"Success! Code saved to {args.output}", file=sys.stderr)
    except IOError as e:
        print(f"Error: Failed to write to file {args.output}. {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
