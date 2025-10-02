#!/usr/bin/env python3
import os
import sys
import argparse
from dotenv import load_dotenv
from groq import Groq
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel

load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY")
console = Console()

SYSTEM_PROMPT = (
    "You are a concise, helpful assistant for command-line Q&A. "
    "Default to <=120 words unless asked for detail. Use bullets when helpful."
)

def get_client():
    if not API_KEY:
        return None, "❌ Missing GROQ_API_KEY. Put it in a .env file (e.g., GROQ_API_KEY=gsk_...)."
    try:
        return Groq(api_key=API_KEY), None
    except Exception as e:
        return None, f"❌ Failed to init Groq client: {e}"

def ask_llm(client, question: str, model: str = "llama-3.1-8b-instant", temperature: float = 0.3) -> str:
    try:
        resp = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": question},
            ],
            temperature=temperature,
        )
        return resp.choices[0].message.content.strip()
    except Exception as e:
        return f"❌ API error: {e}"

def interactive(default_model: str, default_temp: float):
    client, err = get_client()
    console.print(Panel.fit("[bold cyan]Tiny AI Q&A[/] — type 'exit' to quit"))
    if err:
        console.print(err)
        console.print("Tip: create a .env with GROQ_API_KEY=gsk_your_real_key")
        return
    while True:
        q = Prompt.ask("\n[bold green]Your question[/]")
        if q.strip().lower() in {"exit", "quit"}:
            console.print("[dim]Bye![/]")
            break
        ans = ask_llm(client, q, model=default_model, temperature=default_temp)
        console.print(Panel.fit(ans, title=f"Answer ({default_model}, temp={default_temp})", border_style="cyan"))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Tiny AI Q&A (Groq)")
    parser.add_argument("--model", default="llama-3.1-8b-instant",
                        help="Groq model (e.g., llama-3.1-8b-instant, llama-3.3-70b-versatile)")
    parser.add_argument("--temp", type=float, default=0.3, help="Response creativity (0.0–1.0)")
    parser.add_argument("question", nargs="*", help="Question in one-shot mode (leave empty for interactive)")
    args = parser.parse_args()

    client, err = get_client()
    if err:
        print(err)
        sys.exit(1)

    if args.question:
        q = " ".join(args.question)
        print(ask_llm(client, q, model=args.model, temperature=args.temp))
    else:
        # interactive mode uses defaults from flags
        interactive(default_model=args.model, default_temp=args.temp)

