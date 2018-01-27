	.file	"factorial.c"
	.text
	.globl	main
	.type	main, @function
main:
.LFB0:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	movl	%edi, -20(%rbp)
	movq	%rsi, -32(%rbp)
	movl	$10, -4(%rbp)
	movl	$1, -12(%rbp)
	movl	-4(%rbp), %eax
	movl	%eax, -8(%rbp)
	jmp	.L2
.L3:
	movl	-12(%rbp), %eax
	imull	-8(%rbp), %eax
	movl	%eax, -12(%rbp)
	subl	$1, -8(%rbp)
.L2:
	cmpl	$0, -8(%rbp)
	jg	.L3
	movl	-12(%rbp), %eax
	popq	%rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE0:
	.size	main, .-main
	.ident	"GCC: (Ubuntu 5.4.0-6ubuntu1~16.04.5) 5.4.0 20160609"
	.section	.note.GNU-stack,"",@progbits
