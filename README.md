# Strategize Globally, Adapt Locally: A Multi-Turn Red Teaming Agent with Dual-Level Learning

This is the official implementation of the paper ["Strategize Globally, Adapt Locally: A Multi-Turn Red Teaming Agent with Dual-Level Learning"](https://arxiv.org/pdf/2504.01278).

## Abstract

The exploitation of large language models (LLMs) for malicious purposes poses significant security
risks as these models become more powerful and widespread. While most existing red-teaming
frameworks focus on single-turn attacks, real-world adversaries typically operate in multi-turn
scenarios, iteratively probing for vulnerabilities and adapting their prompts based on threat model
responses. In this paper, we propose GALA, a novel multi-turn red-teaming agent that emulates
sophisticated human attackers through complementary learning dimensions: global tactic-wise
learning that accumulates knowledge over time and generalizes to new attack goals, and local promptwise learning that refines implementations for specific goals when initial attempts fail. Unlike
previous multi-turn approaches that rely on fixed strategy sets, GALA enables the agent to identify
new jailbreak tactics, develop a goal-based tactic selection framework, and refine prompt formulations
for selected tactics. Empirical evaluations on JailbreakBench demonstrate our framework’s superior
performance, achieving over 90% attack success rates against GPT-3.5-Turbo and Llama-3.1-70B
within 5 conversation turns, outperforming state-of-the-art baselines. These results highlight the
effectiveness of dynamic learning in identifying and exploiting model vulnerabilities in realistic
multi-turn scenarios.

## Usage

1.  **Set up your API keys and endpoints:**
    *   In `gala_qwen.py`, configure the `openai_key` and the `base_url` for your attacker model (e.g., Qwen) and target models (e.g., Llama). You can use `vllm` to host the model.
    *   In `gpt_judge_binary_qi.py`, set your `openai_key` for the GPT-4 judge model.

2.  **Run the GALA agent:**
    *   Modify the `TARGET_MODEL` variable in `gala_qwen.py` to specify the model you want to attack.
    *   Run the script:
    ```bash
    python gala_qwen.py
    ```
    *   Results, including conversation logs, will be saved in the `results_{TARGET_MODEL}` directory.

3.  **Evaluate the results:**
    *   After running the attacks, you will have a `.csv` file with the conversation histories.
    *   In `gpt_judge_binary_qi.py`, set `eval_file_path` to the path of the results file.
    *   Run the evaluation script:
    ```bash
    python gpt_judge_binary_qi.py
    ```
    *   This will generate a new CSV file in the `./evaluation/` directory containing the jailbreak scores and the judge's reasoning.

## Script Descriptions

*   `gala_qwen.py`: This is the main script for running the GALA red-teaming agent. It implements the core logic of the multi-turn attack, including the planning, belief update, and learning modules. The agent interacts with a specified target LLM to achieve harmful goals read from the [JailbreakBench](https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors) dataset.

*   `constant_agent.py`: This file contains the prompt templates and the initial knowledge base (memory) for the GALA agent. The memory includes a `Tactic Pool` of known adversarial techniques and examples of successful past attacks (`Success Trials`).

*   `utils.py`: This file contains helper functions used across the project, such as a function to make API calls to LLMs with retry logic (`generate_response`), a utility to extract JSON objects from model outputs (`extract_dict`), and a function to shorten conversation histories (`shorten_conversation`).

*   `gpt_judge_binary_qi.py`: This script is used to evaluate the success of the jailbreaking attempts. It takes the conversation history from an attack and uses a powerful judge model (GPT-4) to determine if the target model's responses violated safety policies, assigning a binary success score.

## Citation

If you find this work useful, please consider citing the original paper.

```bibtex
@misc{chen2025strategize,
      title={Strategize Globally, Adapt Locally: A Multi-Turn Red Teaming Agent with Dual-Level Learning}, 
      author={Si Chen and Xiao Yu and Ninareh Mehrabi and Rahul Gupta and Zhou Yu and Ruoxi Jia},
      year={2025},
      eprint={2504.01278},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```
