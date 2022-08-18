vim.notify = require("notify")

-- Numbering
vim.opt.number = true                 -- print the line number in front of each line
vim.opt.relativenumber = true         -- show relative line number in front of each line

-- Searching
vim.opt.hlsearch = true               -- highlight matches with last search pattern
vim.opt.incsearch = true              -- highlight match while typing search pattern
vim.opt.ignorecase = true             -- ignore case in search patterns
vim.opt.smartcase = true              -- no ignore case when pattern has uppercase

-- Indenting
vim.opt.tabstop = 4                   -- number of spaces that <Tab> in file uses
vim.opt.softtabstop = 4               -- number of spaces that <Tab> uses while editing
vim.opt.shiftwidth = 4                -- number of spaces to use for (auto)indent step
vim.opt.expandtab = true              -- use spaces when <Tab> is inserted
vim.opt.smarttab = true               -- smart autoindenting for C programs

-- Scrolling
vim.opt.scrolloff = 8                 -- minimum nr. of lines above and below cursor

-- miscellaneous
vim.opt.clipboard = "unnamedplus"     -- use the clipboard as the unnamed register. Refer to https://neovim.io/doc/user/options.html#'clipboard'
vim.opt.wrap = false                   -- long lines wrap and continue on the next line
vim.opt.splitright = true             -- new window is put right of the current one
vim.opt.spelllang = 'en_gb'
vim.opt.hidden = true                 -- don't unload buffer when it is abandoned
