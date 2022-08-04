vim.opt_local.path:prepend(vim.fn.stdpath("config") .. "/lua")

require("options")

require("packer-setup")
-- require("nvim-tree-setup")
-- require("telescope-setup")
require("colorscheme")

-- require("mappings")
-- require("completions-setup")
-- require("lsp-setup")
-- require("treesitter-setup")
-- require("autopairs-setup")
-- require("neoclip-setup")
-- require("vimwiki-setup")
-- require("dap-setup")
-- require("luasnip-setup")
