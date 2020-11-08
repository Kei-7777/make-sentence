from sys import argv
import MeCab
import markovify

def main():
    file = argv[1]
    with open(file, "r") as f:
        txt = f.read()
    tag = MeCab.Tagger("-Owakati")
    txt = tag.parse(txt)
    model = markovify.Text(txt, state_size=2)
    out = model.make_short_sentence(1000)
    out = out.replace(" ", "")
    print(out)

if __name__ == "__main__":
    main()