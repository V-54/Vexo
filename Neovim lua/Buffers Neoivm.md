### Create buffer with default params
`vim.api.nvim_create_buf()` - func get two parametrs:
- (boolean) - defines will there be new buffer add to buffers list
- (boolean) - defines will there be new buffer is [[Windows options#^b4f756|scratch-buffer]]
---
### Set buffer option 
`nvim_buf_set_option()` - func get three parametrs:
*Sets a buffer option value. Passing `nil` as value deletes the option
(only works if there's a global fallback)*
- (num) - buffer number or 0 for current buffer
- (String) - option name
- (String) - option value
---
### Get buffer option
`nvim_buf_get_option()` - func get tow parametrs:
*Gets a buffer option value*
- (num) - buffer number or 0 for current buffer
- (String) - option name

**Return:**
	option value

---