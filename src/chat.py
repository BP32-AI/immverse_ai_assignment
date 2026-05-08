# src/chat.py

from rag import RAGPipeline

def main():
    rag = RAGPipeline()
    print("\nMini Manuscript Conversational System")
    print("Type 'exit' to quit\n")
    while True:
        query = input("Ask: ")
        if query.lower() == "exit":
            break
        result = rag.ask(query)
        print("\nAnswer:")
        print(result["answer"])
        print("\nSources:")
        for source in result["sources"]:
            print(source)

        print("\n" + "=" * 50 + "\n")


if __name__ == "__main__":
    main()