## Moving the cursor between windows
### Move cursor to window:
**Keymap**
`CTRL-W h,j,k,l` - left, bottom, top, right 
**cmd variant:**
`:wincmd (side key like them 'h','j','k','l')`
**Lua config variant:** (more about vim.api - [[Neovim API]])
`vim.api.nvim_command("wincmd" ...)`
*example:*
`:wincmd h` - set cursor focus to left window
`vim.api.nvim_command("wincmd h")` - set cursor focus to left window

### Move cursor to top-left window:

^a1b2a6

**Keymap**
`CTRL-W t`
**cmd variant:**
`:wincmd t)`
**Lua config variant:** (more about vim.api - [[Neovim API]])
`vim.api.nvim_command("wincmd t")`
### Move cursor to previus window:
**Keymap**
`CTRL-W p`
**cmd variant:**
`:wincmd p)`
**Lua config variant:** (more about vim.api - [[Neovim API]])
`vim.api.nvim_command("wincmd p")`

## Resizing windows:
### Resize window by vertical

^77abde

**cmd variant**
`:vertical resize (colums num)`
**Lua varian** (more about vim.api - [[Neovim API]])
`vim.api.nvim_command("vertical resize " ...)`
*example:*
`:vertical resize 30` - set vertical size 30 columns.
`vim.api.nvim_command("vertical resize 30")` - set vertical size 30 columns. ^dc0496

### Reset windows sizing to default value
**cmd variant**
`:wincmd =`
**Lua variant** (more about vim.api - [[Neovim API]])
`vim.api.nvim_command("wincmd =")`
#neovim