# Localization & i18n Language Boundaries
When generating, modifying, or copy-pasting content across multi-language documentation files (e.g., `README.md` and `README_zh-CN.md`), you must strictly enforce absolute language boundaries:
1. **Never** include Chinese characters (or any non-English text) in the English documentation, even when linking to Chinese resources. Always localize the link text to English (e.g., `[Read Whitepaper (Simplified Chinese)](...)` instead of `[阅读白皮书]`).
2. Do not blindly copy-paste user prompt text into a localized file if the prompt's language does not match the file's target language. Always proactively translate and adapt the content to maintain a pure, professional language interface.

# Scientific Tone & Vocabulary Constraints
When communicating with the user or generating any documentation (including whitepapers, READMEs, source code comments, and reports), you must strictly maintain a rigorous, objective, cautious, and professional scientific tone. 
1. **Never** use sensationalist, absolute, hyperbolic, or "AI-scented" vocabulary (e.g., "撼动学术界", "彻底锁死", "无可辩驳", "彻底瓦解", "最高层级", "统计学灾难", "彻底斩断", "彻底秒杀", "重磅级", "震撼的", "令人生畏", "双重升华", "标杆", "石破天惊", "终极", "惊喜", "解密", "完美", "不可思议", "突破", "严酷", "性感").
2. **Never** use unprofessional or anthropomorphic metaphorical verbs in a mathematical/scientific context (e.g., "方程咬合", "坚不可摧", "死死锁在"). 
3. Present findings and methodologies objectively. Use terms like "supports," "indicates," "intercepts," "validates," or "demonstrates" rather than declaring definitive or revolutionary victories.
