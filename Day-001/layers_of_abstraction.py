layers = [
    "⚡ Electrons",
    "🔌 Transistors",
    "🧮 Logic Gates",
    "🖥️ CPU",
    "💾 Memory",
    "⚙️ Operating System",
    "💻 Programming Language",
    "🚀 Application",
    "🌍 Internet",
    "🤖 AI",
]

print("\n Everything in computing is a hierarchy of abstractions.\n")

for lower, higher in zip(layers, layers[1:]):
    print(f"{lower} -> {higher}")