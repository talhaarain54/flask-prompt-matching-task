def match_prompt(situation, level, file_type):
    prompts = {
        ("Commercial Auto", "Structure", "Summary Report"): "Prompt 1",
        ("General Liability", "Summarize", "Deposition"): "Prompt 2",
        ("Commercial Auto", "Summarize", "Summons"): "Prompt 3",
        ("Workers Compensation", "Structure", "Medical Records"): "Prompt 4",
        ("Workers Compensation", "Summarize", "Summons"): "Prompt 5"
    }

    return prompts.get((situation, level, file_type))
