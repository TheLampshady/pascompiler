Program Sample_Write;
Var
    Num1, Num2, Num3 : Integer;
    Real1, Real2 : Real;

Begin
 Num1 := 5;
 Num2 := 1 + Num1 * 3;
 Num3 := Num2 + 2 * (3 + 1);
 write(num3);

 Real1 := 1.5 + Num1;
 Real2 := Real1 + 1.25;
 write(Real2);
End.