def content_file_name(instance,filename):
    return 'articulos/{0}/{1}'.format(instance.semillero.nombre,filename)