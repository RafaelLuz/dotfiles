------ Misc
-- vim.opt.exrc = true
-- vim.opt.secure = true
-- vim.opt.hidden = true
-- vim.opt.scrolloff = 8
-- vim.opt.hidden = true
-- vim.opt.scrolloff = 8
-- vim.opt.wrap = false
-- vim.opt.signcolumn = "yes" -- not quite sure what this does
-- set colorcolumn=80
-- set noerrorbells
vim.opt.clipboard = "unnamedplus"
-- vim.opt.updatetime = 300 -- default is 4000ms
-- vim.opt.conceallevel = 0 -- so that `` is visible in markdown files
vim.opt.splitright = true
-- vim.opt.completeopt = { "menuone", "noinsert", "noselect" }

-- set this to false when running macros with find (/) words
vim.opt.wrapscan = true

------ Numbering
vim.opt.relativenumber = true
vim.opt.number = true

------ Searching
vim.opt.hlsearch = true
vim.opt.incsearch = true

------ Indenting
vim.opt.tabstop = 4
vim.opt.softtabstop = 4
vim.opt.shiftwidth = 4
vim.opt.expandtab = true
vim.opt.smartindent = true

------ Appearance
-- vim.cmd([[
-- try
--   colorscheme darkplus
-- catch /^Vim\%((\a\+)\)\=:E185/
--   colorscheme default
--   set background=dark
-- endtry
-- ]])

vim.g.transparent_background = true
