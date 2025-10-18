# Flask Prompt Matching API

This is a simple Flask-based API built using the **MVC architecture** (View and Service layers).  
It was developed as part of a **Software Engineer Internship task**.

---

## Overview

The API receives a JSON payload containing:
- `situation`
- `level`
- `file_type`
- `data`

and returns the corresponding **Prompt (1–5)** based on matching criteria.

If the input doesn’t match any prompt, the API returns an **“Invalid Prompt”** error.  
If any field is missing, it returns a **“Missing Data”** error.

---

## Example Request

```json
{
  "situation": "Commercial Auto",
  "level": "Structure",
  "file_type": "Summary Report",
  "data": "Sample input data"
}
```

## Successful Response

```json
{
  "prompt": "Prompt 1"
}
```
