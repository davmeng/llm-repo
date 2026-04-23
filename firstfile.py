fr = open('.keys/keys.txt')
expt1 = fr.readline()
expt2 = fr.readline()
expt1 = expt1[:-1]
expt2 = expt2[:-1]
os.environ["OPENAI_API_KEY"] = expt1
os.environ["ACTIVELOOP_TOKEN"] = expt2

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ACTIVELOOP_TOKEN = os.getenv("ACTIVELOOP_TOKEN")

print("OpenAI Key = ", OPENAI_API_KEY)
print("Activeloop = ", ACTIVELOOP_TOKEN)
