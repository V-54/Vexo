local a = vim.api
local M = {}
M.config = {
    bufnum = 0,
    winnum = 0
}
function M.create_buf()
    M.bufnum = a.nvim_create_buf(true,false) 
    return M.bufnum
end

function M.open_win()
    a.nvim_command("wincmd t")
    a.nvim_command("vnew")
    a.nvim_win_set_width(0,30)
    a.nvim_win_set_buf(0, M.create_buf())
    M.winnum = a.nvim_win_get_number(0)
end

return M
