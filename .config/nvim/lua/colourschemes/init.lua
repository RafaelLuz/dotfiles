-- catppuccin configuration
vim.g.catppuccin_flavour = "macchiato" -- latte, frappe, macchiato, mocha
require("catppuccin").setup({
    transparent_background = true,
    integrations = {
        nvimtree = {
            enabled = true,
            show_root = true,
            transparent_panel = true
        }
    }
})

vim.cmd [[colorscheme catppuccin]]
