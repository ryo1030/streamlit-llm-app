import streamlit as st
from dotenv import load_dotenv
from langchain.schema import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

HEALTH_EXPERT = "健康に関する専門家"
HISTORY_EXPERT = "歴史に関する専門家"


def main():
    load_dotenv()

    st.title("Chapter 6 【提出課題】LLM機能を搭載したWebアプリを開発しよう")

    st.write(
        "このWebアプリは、健康または歴史の専門家としてLLMが回答を生成します。"
        "専門家を選択し、質問を入力して「実行」を押すと回答が表示されます。"
    )

    selected_item = st.radio(
        "専門家を選択してください。",
        [HEALTH_EXPERT, HISTORY_EXPERT],
    )

    st.text_input(label="文字を入力してください。", key="input_text")

    system_message = ""
    if selected_item == HEALTH_EXPERT:
        system_message = "あなたは健康に関する専門家です。"
    elif selected_item == HISTORY_EXPERT:
        system_message = "あなたは歴史に関する専門家です。"
    else:
        st.error("専門家の選択に誤りがあります。")
        return

    if st.button("実行") and len(st.session_state.input_text) > 0:
        st.divider()

        llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

        messages = [
            SystemMessage(content=system_message),
            HumanMessage(content=st.session_state.input_text),
        ]

        result = llm(messages)

        st.subheader("回答結果")
        st.write(result.content)


if __name__ == "__main__":
    main()
