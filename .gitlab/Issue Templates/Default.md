## 📌 General Issue – Claude-3 Token Quota Limit and UI Crash

### Description

While using the assistant continuously for more than 5–10 queries, the Claude-3 API sometimes fails due to OpenRouter's rate limiting, which isn't handled gracefully by the app. This results in the Streamlit UI freezing or showing blank output instead of an error message.

### Purpose

This issue is being raised to improve the resilience of the AI assistant when API tokens hit a quota limit. Users should be shown a clear error message with the option to re-enter a valid token or wait before retrying.

### Relevance to the Project

This affects user experience, especially during demos, testing, or multi-user deployments where API usage may spike. Right now, users are confused when no output is shown, thinking it’s a bug in the assistant itself.

### Proposed Next Steps

Introduce a try-except block around the Claude-3 call and handle `403` or `429` errors specifically. In case of a quota breach, display a toast alert or warning message and halt further inputs temporarily.

### References or Resources

- OpenRouter API status: https://openrouter.ai/docs/rate-limits
- Streamlit alerts: https://docs.streamlit.io/library/api-reference/status/st.toast

### Additional Notes

Consider adding support for rotating API keys for authenticated users to prevent global outages on shared deployments.
