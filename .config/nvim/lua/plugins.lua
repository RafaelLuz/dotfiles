-- Autocommand that reloads neovim whenever you save the plugins.lua file
vim.cmd([[
    augroup packer_user_config
       autocmd!
        autocmd BufWritePost plugins.lua source <afile> | PackerSync
    augroup end
]])

-- Have packer use a popup window
require("packer").init({
	display = {
		open_fn = function()
			return require("packer.util").float({ border = "rounded" })
		end,
	},
})

return require("packer").startup(function()
	use("wbthomason/packer.nvim")

    use {
        'kyazdani42/nvim-tree.lua',
        requires = {
            'kyazdani42/nvim-web-devicons', -- optional, for file icon
        },
        config = function() require'nvim-tree'.setup {} end
    }
	-- Misc
	-- use("ThePrimeagen/vim-be-good")
	-- use("mbbill/undotree")
	-- use("vimwiki/vimwiki")
	-- use("mfussenegger/nvim-dap")
	-- use("tpope/vim-fugitive")
	-- use("tpope/vim-rhubarb") -- :GBrowse command

	-- Remaps
	-- use("tpope/vim-surround")
	-- use("machakann/vim-sandwich") -- like vim-surround but highlights text and also supports dot command
	-- use("tpope/vim-commentary")
	-- use("windwp/nvim-autopairs")
	-- use("andrewradev/splitjoin.vim") -- gS (not working) and gJ commands

	-- Colorschemes
    use("lunarvim/colorschemes")
    use("dracula/vim")
    use("folke/tokyonight.nvim")
    use("gruvbox-community/gruvbox")
	use("lunarvim/darkplus.nvim")
  -- use("tribela/vim-transparent")
	-- use({ "nvim-treesitter/nvim-treesitter", run = ":TSUpdate" })
	-- use("p00f/nvim-ts-rainbow")
	-- use({ "rrethy/vim-hexokinase", run = "make hexokinase" }) -- shows color as a virtual text

	-- Completions
	-- use("hrsh7th/nvim-cmp")
	-- use("hrsh7th/cmp-buffer")
	-- use("hrsh7th/cmp-path")
	-- use("hrsh7th/cmp-cmdline")
	-- use("saadparwaiz1/cmp_luasnip")
	-- use("hrsh7th/cmp-nvim-lsp")
	-- use("hrsh7th/cmp-nvim-lua") -- for neovim API (if I ever develop a plugin)

	-- Snippets
	-- use("L3MON4D3/LuaSnip")
	-- use("rafamadriz/friendly-snippets")

	-- LSP
	-- use("neovim/nvim-lspconfig")
	-- use("williamboman/nvim-lsp-installer")
	-- use("jose-elias-alvarez/null-ls.nvim") -- for formatters and linters

	-- Telescope
	use({
		"nvim-telescope/telescope.nvim",
		-- module = "telescope",
		-- cmd = "Telescope", -- only starts when we run this command. check :PackerStatus before running it
		requires = {
			{ "nvim-lua/popup.nvim" },
			{ "nvim-lua/plenary.nvim" },
			{ "nvim-telescope/telescope-fzf-native.nvim", run = "make" },
		},
	})
	-- use({
	-- 	"AckslD/nvim-neoclip.lua",
	-- 	requires = {
	-- 		{ "tami5/sqlite.lua", module = "sqlite" },
	-- 	},
	-- }) -- show registers in telescope
	-- use("dhruvmanila/telescope-bookmarks.nvim")
end)
