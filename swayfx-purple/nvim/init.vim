" plug
call plug#begin()

" List your plugins here
Plug 'catppuccin/nvim', { 'as': 'catppuccin' }
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
Plug 'ziglang/zig.vim'
Plug 'christoomey/vim-tmux-navigator'
Plug 'voldikss/vim-floaterm'
Plug 'natecraddock/workspaces.nvim'
Plug 'nvim-lua/plenary.nvim'
Plug 'stevearc/dressing.nvim'
Plug 'akinsho/flutter-tools.nvim'

call plug#end()

" looks
colorscheme catppuccin
let g:airline_theme='violet'
let g:airline_powerline_fonts = 1

hi NonText ctermbg=none guibg=NONE
hi Normal guibg=NONE ctermbg=NONE
hi NormalNC guibg=NONE ctermbg=NONE

hi SignColumn ctermbg=NONE ctermfg=NONE guibg=NONE
" Used for some floating windows
hi Pmenu ctermbg=NONE ctermfg=NONE guibg=NONE
hi FloatBorder ctermbg=NONE ctermfg=NONE guibg=NONE
hi NormalFloat ctermbg=NONE ctermfg=NONE guibg=NONE
hi TabLine ctermbg=None ctermfg=None guibg=None

" general
set number
set tabstop=4   
set softtabstop=4
set expandtab  
set shiftwidth=4
set autoindent
set showmatch
set ignorecase
set wrap!
let g:zig_fmt_autosave = 0

" keymaps
"nnoremap <silent> <C-h> <Cmd>NvimTmuxNavigateLeft<CR>
"nnoremap <silent> <C-j> <Cmd>NvimTmuxNavigateDown<CR>
"nnoremap <silent> <C-k> <Cmd>NvimTmuxNavigateUp<CR>
"nnoremap <silent> <C-l> <Cmd>NvimTmuxNavigateRight<CR>
"nnoremap <silent> <C-\> <Cmd>NvimTmuxNavigateLastActive<CR>
"nnoremap <silent> <C-Space> <Cmd>NvimTmuxNavigateNext<CR>

"nnoremap <C-J> <C-W><C-J>
"nnoremap <C-K> <C-W><C-K>
"nnoremap <C-L> <C-W><C-L>
"nnoremap <C-H> <C-W><C-H>

nnoremap <silent> <C-b> <Cmd>FloatermToggle<CR> 

 " Show hover
nnoremap K <Cmd>lua vim.lsp.buf.hover()<CR>
 " Jump to definition
nnoremap gd <Cmd>lua vim.lsp.buf.definition()<CR>
 " Open code actions using the default lsp UI, if you want to change this please see the plugins above
nnoremap <leader>ca <Cmd>lua vim.lsp.buf.code_action()<CR>
 " Open code actions for the selected visual range
xnoremap <leader>ca <Cmd>lua vim.lsp.buf.range_code_action()<CR>

