import operations_rational as op
import calculatortype as ty
import operations_complex as opCom

type = ty.type()

while type ==  'rational':
    op.mainterminal()
    
if type == 'complex':
    repeat = True
    while repeat == True:
        operands = opCom.Insert_Numbers()
        if operands[2] == "+":
            opCom.record_in_file(opCom.Addition(opCom.Take_Rational_Part(operands[0]), opCom.Take_Symbol(operands[0]), opCom.Take_Imaginary_Part(operands[0]), opCom.Take_Rational_Part(operands[1]), opCom.Take_Symbol(operands[1]), opCom.Take_Imaginary_Part(operands[1])))
        elif operands[2] == "-":
            opCom.record_in_file(opCom.Deduction(opCom.Take_Rational_Part(operands[0]), opCom.Take_Symbol(operands[0]), opCom.Take_Imaginary_Part(operands[0]), opCom.Take_Rational_Part(operands[1]), opCom.Take_Symbol(operands[1]), opCom.Take_Imaginary_Part(operands[1])))
        elif operands[2] == "*":
            opCom.record_in_file(opCom.Multiply(opCom.Take_Rational_Part(operands[0]), opCom.Take_Symbol(operands[0]), opCom.Take_Imaginary_Part(operands[0]), opCom.Take_Rational_Part(operands[1]), opCom.Take_Symbol(operands[1]), opCom.Take_Imaginary_Part(operands[1])))
        else:
            opCom.record_in_file(opCom.division(opCom.Take_Rational_Part(operands[0]), opCom.Take_Symbol(operands[0]), opCom.Take_Imaginary_Part(operands[0]), opCom.Take_Rational_Part(operands[1]), opCom.Take_Symbol(operands[1]), opCom.Take_Imaginary_Part(operands[1])))
        repeat = opCom.Repeat_Or_No()