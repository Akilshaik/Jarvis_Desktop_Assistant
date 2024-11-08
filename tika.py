import tika
from tika import parser


def main():
    tika.initVM()
    project_pdf = parser.from_file("D:\Project\Neuronix-project-report.pdf")
    print(project_pdf)



if __name__ == "__main__":
    main()