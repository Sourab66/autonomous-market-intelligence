import time
import json


def estimate_tokens(text):

    if not text:
        return 0

    return max(1, len(str(text)) // 4)


def invoke_with_metrics(llm, prompt):

    start = time.time()

    response = llm.invoke(prompt)

    end = time.time()

    execution_time = round(end - start, 2)

    usage = {}

    if hasattr(response, "usage_metadata"):

        usage = response.usage_metadata or {}

    elif hasattr(response, "response_metadata"):

        usage = response.response_metadata.get(
            "usage_metadata",
            {}
        )

    input_tokens = usage.get(
        "input_tokens",
        usage.get("prompt_token_count", 0)
    )

    output_tokens = usage.get(
        "output_tokens",
        usage.get("candidates_token_count", 0)
    )

    total_tokens = usage.get(
        "total_tokens",
        usage.get(
            "total_token_count",
            input_tokens + output_tokens
        )
    )

    # --------------------------------------------------
    # Fallback estimation when Gemini metadata is missing
    # --------------------------------------------------

    if total_tokens == 0:

        input_tokens = estimate_tokens(prompt)

        try:

            if hasattr(response, "content"):

                output_text = response.content

            elif hasattr(response, "model_dump"):

                output_text = json.dumps(
                    response.model_dump()
                )

            else:

                output_text = str(response)

        except Exception:

            output_text = str(response)

        output_tokens = estimate_tokens(
            output_text
        )

        total_tokens = (
            input_tokens +
            output_tokens
        )

    # --------------------------------------------------
    # Gemini Pricing Estimate
    # --------------------------------------------------

    INPUT_PRICE_PER_1M = 0.30
    OUTPUT_PRICE_PER_1M = 2.50

    estimated_cost = round(

        (
            input_tokens / 1_000_000
        ) * INPUT_PRICE_PER_1M

        +

        (
            output_tokens / 1_000_000
        ) * OUTPUT_PRICE_PER_1M,

        6

    )

    return {

        "response": response,

        "execution_time": execution_time,

        "tokens": {

            "input_tokens": input_tokens,

            "output_tokens": output_tokens,

            "total_tokens": total_tokens

        },

        "cost": estimated_cost

    }