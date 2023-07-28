transcript on
if {[file exists rtl_work]} {
	vdel -lib rtl_work -all
}
vlib rtl_work
vmap work rtl_work

vlog -vlog01compat -work work +incdir+W:/SDP/Prac2/prac2_restored {W:/SDP/Prac2/prac2_restored/LCD_SYNC.v}
vlog -vlog01compat -work work +incdir+W:/SDP/Prac2/prac2_restored {W:/SDP/Prac2/prac2_restored/COUNT.v}
vlog -vlog01compat -work work +incdir+W:/SDP/Prac2/prac2_restored {W:/SDP/Prac2/prac2_restored/pll_ltm.v}
vlog -vlog01compat -work work +incdir+W:/SDP/Prac2/prac2_restored/db {W:/SDP/Prac2/prac2_restored/db/pll_ltm_altpll.v}

vlog -vlog01compat -work work +incdir+W:/SDP/Prac2/prac2_restored {W:/SDP/Prac2/prac2_restored/tb_LCD_SYNC.v}

vsim -t 1ps -L altera_ver -L lpm_ver -L sgate_ver -L altera_mf_ver -L altera_lnsim_ver -L cycloneive_ver -L rtl_work -L work -voptargs="+acc"  tb_LCD_SYNC

add wave *
view structure
view signals
run -all
