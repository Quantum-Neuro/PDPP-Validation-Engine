# Localization & i18n Language Boundaries
When generating, modifying, or copy-pasting content across multi-language documentation files (e.g., `README.md` and `README_zh-CN.md`), you must strictly enforce absolute language boundaries:
1. **Never** include Chinese characters (or any non-English text) in the English documentation, even when linking to Chinese resources. Always localize the link text to English (e.g., `[Read Whitepaper (Simplified Chinese)](...)` instead of `[阅读白皮书]`).
2. Do not blindly copy-paste user prompt text into a localized file if the prompt's language does not match the file's target language. Always proactively translate and adapt the content to maintain a pure, professional language interface.
