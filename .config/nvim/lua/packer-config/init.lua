return require('packer').startup(function(use) 
    -- Packer can manage itself
    use 'wbthomason/packer.nvim'

    -- colourschemes
    use {"catppuccin/nvim", as = "catppuccin"}   

    -- nvim-tree
    use {
        'kyazdani42/nvim-tree.lua',
        requires = {
            'kyazdani42/nvim-web-devicons', -- optional, for file icons
        },
        tag = 'nightly' -- optional, updated every week. (see issue #1193)
    }

    -- lsp
    use 'williamboman/mason.nvim'
    use 'williamboman/mason-lspconfig.nvim'
    use 'neovim/nvim-lspconfig'     -- Collection of configurations for built-in LSP client
    use 'hrsh7th/nvim-cmp'          -- Autocompletion plugin
    use 'hrsh7th/cmp-nvim-lsp'      -- LSP source for nvim-cmp
    use 'saadparwaiz1/cmp_luasnip'  -- Snippets source for nvim-cmp
    use 'L3MON4D3/LuaSnip'          -- Snippets plugin
    use 'onsails/lspkind-nvim'      -- vscode-like pictograms to neovim built-in lsp

    -- notify
    use 'rcarriga/nvim-notify'

    -- lualine
    use {
        'nvim-lualine/lualine.nvim',
        requires = { 'kyazdani42/nvim-web-devicons', opt = true }
    }

    -- barbar
    use {
        'romgrk/barbar.nvim',
        requires = {'kyazdani42/nvim-web-devicons'}
    }

    -- treesitter


end)
