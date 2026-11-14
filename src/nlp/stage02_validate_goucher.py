"""stage02_validate.py.

(EDIT YOUR VERSION OF THIS FILE)

Author: Britany Goucher

Date: 2026-11

Source: raw JSON object
Sink: validated JSON object

Purpose

  Inspect JSON structure and validate that the data is usable.

Analytical Questions

- What is the top-level structure of the JSON data?
- What keys are present in each record?
- What data types are associated with each field?
- Does the data meet expectations for transformation?

Edit your Python file to:
- inspect the JSON structure for your API,
- validate required keys and types,
- confirm the data is usable for your analysis.
"""

# ============================================================
# Section 1. Setup and Imports
# ============================================================

import logging
from typing import Any

# ============================================================
# Section 2. Define Run Validate Function
# ============================================================


def run_validate(
    json_data: Any,
    LOG: logging.Logger,
) -> list[dict]:
    """Inspect and validate JSON structure.

    Args:
        json_data (Any): The raw JSON data from the Extract stage.
        LOG (logging.Logger): The logger instance.

    Returns:
        list[dict]: The validated JSON data.
    """
    LOG.info("========================")
    LOG.info("STAGE 02: VALIDATE starting...")
    LOG.info("========================")

    # ============================================================
    # INSPECT JSON STRUCTURE
    # ============================================================

    LOG.info("JSON STRUCTURE INSPECTION:")

    # Log the type of the top-level JSON structure.
    # Use the built-in type() function to get the type
    # and built-in variable __name__ to log just the type name.
    LOG.info(f"Top-level type: {type(json_data).__name__}")

    if isinstance(json_data, dict) and "quotes" in json_data:
        quotes = json_data["quotes"]

        LOG.info(msg=f"Total quotes retrieved: {len(quotes)}")

        first_record = quotes[0]

        LOG.info(msg=f"Keys in first record: {list(first_record.keys())}")

        LOG.info(msg="Field types:")

        for key, value in first_record.items():
            LOG.info(msg=f"{key}: {type(value).__name__}")

    # ============================================================
    # VALIDATE EXPECTATIONS
    # ============================================================

    if not isinstance(json_data, dict):
        raise TypeError("Expected JSON data to be a dictionary.")

    if "quotes" not in json_data:
        raise KeyError("Expected 'quotes' key in JSON response.")

    quotes = json_data["quotes"]

    if len(quotes) == 0:
        raise ValueError("Expected at least one quote.")

    if not all(isinstance(record, dict) for record in quotes):
        raise ValueError("Expected each quote record to be a dictionary.")

    required_fields = {"id", "quote", "author"}

    if not required_fields.issubset(quotes[0].keys()):
        raise ValueError(f"Expected fields: {required_fields}")

    LOG.info("Validation passed.")
    LOG.info("Sink: validated JSON object")

    # Return the validated JSON data for use in the next stage.
    return json_data["quotes"]
