


# I made this tool to help and assist me so that i can exploit file upload vulns better
# Something I want to do with this tool is to make it so that it actually add the magic bytes to the payload thus changing the
# file from its original to something like png or mp4.


import pyperclip



with open("output.txt","w") as outputFile:
    writetofile = outputFile.write(f"{result}")
mime_types = {
    'application/atom+xml': ['.atom'],
    'application/ecmascript': ['.ecmascript'],
    'application/epub+zip': ['.epub'],
    'application/gzip': ['.gz'],
    'application/java-archive': ['.jar'],
    'application/javascript': ['.js'],
    'application/json': ['.json'],
    'application/ld+json': ['.jsonld'],
    'application/msword': ['.doc'],
    'application/octet-stream': ['.bin', '.exe', '.dmg'],
    'application/ogg': ['.ogx'],
    'application/pdf': ['.pdf'],
    'application/php': ['.php'],
    'application/vnd.apple.installer+xml': ['.mpkg'],
    'application/vnd.google-earth.kml+xml': ['.kml'],
    'application/vnd.google-earth.kmz': ['.kmz'],
    'application/vnd.ms-excel': ['.xls'],
    'application/vnd.ms-fontobject': ['.eot'],
    'application/vnd.ms-powerpoint': ['.ppt'],
    'application/vnd.oasis.opendocument.presentation': ['.odp'],
    'application/vnd.oasis.opendocument.spreadsheet': ['.ods'],
    'application/vnd.oasis.opendocument.text': ['.odt'],
    'application/vnd.openxmlformats-officedocument.presentationml.presentation': ['.pptx'],
    'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet': ['.xlsx'],
    'application/vnd.openxmlformats-officedocument.wordprocessingml.document': ['.docx'],
    'application/vnd.wap.wmlc': ['.wmlc'],
    'application/x-7z-compressed': ['.7z'],
    'application/x-abiword': ['.abw'],
    'application/x-bzip': ['.bz'],
    'application/x-bzip2': ['.bz2'],
    'application/x-csh': ['.csh'],
    'application/x-freearc': ['.arc'],
    'application/x-rar-compressed': ['.rar'],
    'application/x-sh': ['.sh'],
    'application/x-shockwave-flash': ['.swf'],
    'application/x-tar': ['.tar'],
    'application/x-xz': ['.xz'],
    'application/x-zsh': ['.zsh'],
    'audio/aac': ['.aac'],
    'audio/midi': ['.midi', '.mid'],
    'audio/mpeg': ['.mp3'],
    'audio/ogg': ['.oga'],
    'audio/wav': ['.wav'],
    'audio/webm': ['.weba'],
    'font/woff': ['.woff'],
    'font/woff2': ['.woff2'],
    'image/bmp': ['.bmp'],
    'image/gif': ['.gif'],
    'image/jpeg': ['.jpg', '.jpeg'],
    'image/png': ['.png'],
    'image/svg+xml': ['.svg'],
    'image/tiff': ['.tiff', '.tif'],
    'image/webp': ['.webp'],
    'text/calendar': ['.ics'],
    'text/css': ['.css'],
    'text/csv': ['.csv'],
    'text/html': ['.html', '.htm'],
    'text/plain': ['.txt'],
    'text/xml': ['.xml'],
    'video/mp4': ['.mp4'],
    'video/mpeg': ['.mpeg', '.mpg'],
    'video/ogg': ['.ogv'],
    'video/webm': ['.webm'],
    'video/x-msvideo': ['.avi'],
    'video/x-ms-wmv': ['.wmv'],
    'video/x-matroska': ['.mkv'],
}

print(mime_types)


def extToMime(ext):
    ext = ext
    for key, value in mime_types.items():
        for ext in value:
            print(ext)
                                   





