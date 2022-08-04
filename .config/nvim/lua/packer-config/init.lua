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

end)
