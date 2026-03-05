# =====================================
# SkibidiScript Gen Alpha Compiler
# =====================================
import re

# -----------------------------
# FULL KEYWORD MAP
# -----------------------------
KEYWORD_MAP = {
    # Control Flow
    "vibe_check": "if",
    "side_quest": "elif",
    "lowkey": "else",
    "grind": "while",
    "loop_de_loop": "for",
    "inside_the_vibes": "in",
    "ragequit": "break",
    "keep_grinding": "continue",
    "npc_move": "pass",

    # Boolean
    "big_w": "True",
    "big_l": "False",
    "no_aura": "None",
    "plus": "and",
    "or_whatever": "or",
    "nah": "not",
    "same_vibes": "is",

    # Functions
    "chef": "def",
    "serve": "return",
    "mini_chef": "lambda",

    # Classes
    "sigma": "class",
    "me_fr": "self",

    # Imports
    "steal": "import",
    "yoink_from": "from",
    "aka": "as",

    # Error Handling
    "risk_it": "try",
    "skill_issue": "except",
    "no_matter_what": "finally",
    "throw_fit": "raise",
    "bet": "assert",

    # Scope
    "worldwide": "global",
    "family_meeting": "nonlocal",

    # With / Yield
    "lock_in": "with",
    "drip_feed": "yield",

    # Async
    "lowkey_async": "async",
    "wait_fr": "await",

    # Built-ins
    "yap": "print",
    "ask": "input",
    "yeet": "del",
    "throw_confetti": "exit()",
    "dab": 'print("💨 dab!")',
    "no_cap": 'print("🧢 no cap")',
    "pog": 'print("POG!!")',
    "spawn_bruh": 'print("bruh moment!")',
    "sus_check": 'print("sus check!")',
    "yolo": 'print("random chaos!")',
    "spawn_memes": 'print("memes incoming!")'
}

# -----------------------------
# OPERATOR MAP
# -----------------------------
OPERATOR_MAP = {
    "sus": "==",
    "not_sus": "!=",
    "mog": ">",
    "beta": "<",
    "mega_mog": ">=",
    "mini_beta": "<=",
    "gyatt": "+",
    "minus_aura": "-",
    "times_rizz": "*",
    "split_the_bag": "/",
    "budget_cut": "//",
    "leftovers": "%",
    "infinite_aura": "**",
    "cooks": "=",
    "++": "+= 1",
    "--": "-= 1"
}

# -----------------------------
# SAFE REPLACEMENT FUNCTION
# -----------------------------
def replace_words(code, mapping):
    for skibidi_word, python_word in mapping.items():
        pattern = r'\b' + re.escape(skibidi_word) + r'\b'
        code = re.sub(pattern, python_word, code)
    return code

# -----------------------------
# TRANSLATOR
# -----------------------------
def translate(code):
    # Operators first
    code = replace_words(code, OPERATOR_MAP)
    # Then keywords
    code = replace_words(code, KEYWORD_MAP)
    # Support simple f-strings
    code = re.sub(r'f"([^"]*)"', lambda m: f'f"{m.group(1)}"', code)
    return code

# -----------------------------
# EXECUTOR
# -----------------------------
def execute(code):
    try:
        exec(code, globals())
    except Exception as e:
        print("💀 SkibidiScript Error!")
        print("Error:", e)

# -----------------------------
# REPL MODE
# -----------------------------
def repl():
    print("Welcome to SkibidiScript Gen Alpha REPL! Type 'exit_skibidi' to quit.")
    buffer = []
    while True:
        try:
            line = input(">>> " if not buffer else "... ")
            if line.strip() == "exit_skibidi":
                break
            buffer.append(line)
            # Execute block if line doesn't end with colon
            if line.strip() == "" or not line.strip().endswith(":"):
                python_code = translate("\n".join(buffer))
                execute(python_code)
                buffer = []
        except KeyboardInterrupt:
            print("\nExiting REPL...")
            break

# -----------------------------
# MAIN
# -----------------------------
if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        try:
            with open(filename, "r", encoding="utf-8") as f:
                skibidi_code = f.read()
            python_code = translate(skibidi_code)
            execute(python_code)
        except FileNotFoundError:
            print(f"💀 File '{filename}' not found!")
        except Exception as e:
            print("💀 Something went wrong:")
            print(e)
    else:
        repl()
