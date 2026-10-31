import webview

def main():
    # The window title must be exactly "Galaxy" for PowerShell AppActivate to hook into it.
    window = webview.create_window(
        title='Galaxy',
        url='index.html',
        width=950,
        height=650,
        resizable=True
    )
    webview.start()

if __name__ == '__main__':
    main()