## Special kinds of buffers
- ### scratch:
	*Contains text that can be discarded at any time.  It is kept
	when closing the window, it must be deleted explicitly.
	Settings: 
		```:setlocal buftype=nofile
		:setlocal bufhidden=hide
		:setlocal noswapfile```
	The buffer name can be used to identify the buffer, if you
	give it a meaningful name.* ^b4f756
- ### directory:
	*Displays directory contents.  Can be used by a file explorer plugin.  The buffer is created with these settings: 
		```:setlocal buftype=nowrite
		:setlocal bufhidden=delete
		:setlocal noswapfile```
	The buffer name is the name of the directory and is adjusted
	when using the `:cd` command.*