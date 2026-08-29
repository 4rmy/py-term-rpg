let SessionLoad = 1
let s:so_save = &g:so | let s:siso_save = &g:siso | setg so=0 siso=0 | setl so=-1 siso=-1
let v:this_session=expand("<sfile>:p")
silent only
silent tabonly
cd ~/Documents/Projects/py-term-rpg
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
endif
let s:shortmess_save = &shortmess
set shortmess+=aoO
badd +73 ./items.py
badd +1 term\ py\ items.py
badd +48 term://~/Documents/Projects/py-term-rpg//17012:py\ items.py
badd +1 term://~/Documents/Projects/py-term-rpg//18000:py\ items.py
badd +1 term://~/Documents/Projects/py-term-rpg//24012:ansi\ --color-codes
badd +30 ansi.py
badd +51 term://~/Documents/Projects/py-term-rpg//21796:py\ ansi.py
badd +1 term://~/Documents/Projects/py-term-rpg//23956:py\ ansi.py
badd +1 term://~/Documents/Projects/py-term-rpg//20636:py\ ansi.py
badd +45 term://~/Documents/Projects/py-term-rpg//22884:py\ ansi.py
badd +39 term://~/Documents/Projects/py-term-rpg//3236:py\ ansi.py
badd +27 term://~/Documents/Projects/py-term-rpg//18524:py\ ansi.py
badd +1 term://~/Documents/Projects/py-term-rpg//13092:py\ items.py
badd +2 term://~/Documents/Projects/py-term-rpg//20028:py\ items.py
badd +27 term://~/Documents/Projects/py-term-rpg//23456:py\ items.py
badd +45 term://~/Documents/Projects/py-term-rpg//9728:py\ items.py
badd +48 term://~/Documents/Projects/py-term-rpg//9996:py\ items.py
badd +9 term://~/Documents/Projects/py-term-rpg//19236:py\ items.py
badd +49 term://~/Documents/Projects/py-term-rpg//6984:py\ items.py
badd +9 term://~/Documents/Projects/py-term-rpg//17952:py\ items.py
badd +10 term://~/Documents/Projects/py-term-rpg//11680:py\ items.py
badd +5 term://~/Documents/Projects/py-term-rpg//22776:py\ items.py
badd +1 term://~/Documents/Projects/py-term-rpg//240:py\ items.py
badd +11 term://~/Documents/Projects/py-term-rpg//14428:py\ items.py
badd +1 term://~/Documents/Projects/py-term-rpg//23724:py\ items.py
badd +21 term://~/Documents/Projects/py-term-rpg//23964:py\ items.py
badd +1 term://~/Documents/Projects/py-term-rpg//9736:py\ items.py
badd +19 term://~/Documents/Projects/py-term-rpg//24068:py\ items.py
badd +36 term://~/Documents/Projects/py-term-rpg//21128:py\ items.py
badd +2 term://~/Documents/Projects/py-term-rpg//6048:py\ items.py
badd +12 term://~/Documents/Projects/py-term-rpg//10500:py\ items.py
badd +4 term://~/Documents/Projects/py-term-rpg//22248:py\ items.py
badd +1 term://~/Documents/Projects/py-term-rpg//16084:py\ items.py
badd +2 term://~/Documents/Projects/py-term-rpg//11912:py\ items.py
badd +36 term://~/Documents/Projects/py-term-rpg//18460:py\ items.py
badd +0 term://~/Documents/Projects/py-term-rpg//5104:py\ items.py
argglobal
%argdel
$argadd ./items.py
edit ./items.py
let s:save_splitbelow = &splitbelow
let s:save_splitright = &splitright
set splitbelow splitright
wincmd _ | wincmd |
vsplit
1wincmd h
wincmd w
let &splitbelow = s:save_splitbelow
let &splitright = s:save_splitright
wincmd t
let s:save_winminheight = &winminheight
let s:save_winminwidth = &winminwidth
set winminheight=0
set winheight=1
set winminwidth=0
set winwidth=1
exe 'vert 1resize ' . ((&columns * 136 + 137) / 274)
exe 'vert 2resize ' . ((&columns * 137 + 137) / 274)
argglobal
balt ansi.py
setlocal foldmethod=manual
setlocal foldexpr=0
setlocal foldmarker={{{,}}}
setlocal foldignore=#
setlocal foldlevel=0
setlocal foldminlines=1
setlocal foldnestmax=20
setlocal foldenable
silent! normal! zE
let &fdl = &fdl
let s:l = 80 - ((53 * winheight(0) + 35) / 70)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 80
normal! 028|
wincmd w
argglobal
if bufexists(fnamemodify("term://~/Documents/Projects/py-term-rpg//5104:py\ items.py", ":p")) | buffer term://~/Documents/Projects/py-term-rpg//5104:py\ items.py | else | edit term://~/Documents/Projects/py-term-rpg//5104:py\ items.py | endif
if &buftype ==# 'terminal'
  silent file term://~/Documents/Projects/py-term-rpg//5104:py\ items.py
endif
balt term://~/Documents/Projects/py-term-rpg//18460:py\ items.py
setlocal foldmethod=manual
setlocal foldexpr=0
setlocal foldmarker={{{,}}}
setlocal foldignore=#
setlocal foldlevel=0
setlocal foldminlines=1
setlocal foldnestmax=20
setlocal foldenable
let s:l = 1 - ((0 * winheight(0) + 35) / 70)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 1
normal! 0
wincmd w
exe 'vert 1resize ' . ((&columns * 136 + 137) / 274)
exe 'vert 2resize ' . ((&columns * 137 + 137) / 274)
tabnext 1
if exists('s:wipebuf') && len(win_findbuf(s:wipebuf)) == 0 && getbufvar(s:wipebuf, '&buftype') isnot# 'terminal'
  silent exe 'bwipe ' . s:wipebuf
endif
unlet! s:wipebuf
set winheight=1 winwidth=20
let &shortmess = s:shortmess_save
let &winminheight = s:save_winminheight
let &winminwidth = s:save_winminwidth
let s:sx = expand("<sfile>:p:r")."x.vim"
if filereadable(s:sx)
  exe "source " . fnameescape(s:sx)
endif
let &g:so = s:so_save | let &g:siso = s:siso_save
nohlsearch
doautoall SessionLoadPost
unlet SessionLoad
" vim: set ft=vim :
