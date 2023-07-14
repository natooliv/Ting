import sys
from ting_file_management.file_management import txt_importer


def process(path, queue_instance):
    if path in queue_instance.queue:
        return None
    txt_content = txt_importer(path)
    queue_instance.enqueue(path)
    print(str({
        "nome_do_arquivo": path,
        "qtd_linhas": len(txt_content),
        "linhas_do_arquivo": txt_content}))


def remove(queue_instance):
    if not len(queue_instance.queue):
        return sys.stdout.write("Não há elementos\n")
    dequeued = queue_instance.dequeue()
    print("Arquivo", dequeued, "removido com sucesso")


def file_metadata(queue_instance, position):
    try:
        path = queue_instance.search(position)
        txt_content = txt_importer(path)
        metadata = {
            "nome_do_arquivo": path,
            "qtd_linhas": len(txt_content),
            "linhas_do_arquivo": txt_content
        }
        print(str(metadata))
    except IndexError:
        return print("Posição inválida", file=sys.stderr)
