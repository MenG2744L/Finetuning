# generate a python to show function usage
import os
import sys
def main():
    if len(sys.argv) < 2:
        print("Usage: python finetune.py <model_name>")
        return
    model_name = sys.argv[1]
    print("python finetune.py %s" % model_name)
if __name__ == "__main__":
    main()