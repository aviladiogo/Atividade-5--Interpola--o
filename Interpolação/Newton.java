package Interpolação;

public class Newton {
    public static void main(String[] args) {
        double Valores[] = { 0, 0, 0.3010, 0, 0.6020, 0, 0.0, 0, 0.9030, 0, 1.0000, 0, 1.0792, 0, 0.0, 0, 1.2041, 0,
                1.2552, 0, 0.0, 0, 1.3424 };
        // grau 2
        double Pn, F0, F1, F2;
        // Pn = F(x0)+(X-x0)*F(x0,x1)+ (X-x0)*(x-x1)*f(x0,x1,x2)
        // F(x0,x1) = F(x1) - F(x0) / x1-x0 ----> F0
        // F(x1,x2) = F(x2) - F(x1) / x2-x1 --> F1
        // F(x0,x1,x2) = F(x1,x2) - F(x0,x1) / x2-x0 ---> F2
        int x, x0, x1, x2, n = 20;

        x = n;
        x0 = n - 4;
        x1 = n - 2;
        x2 = n + 2;
        F0 = (Valores[x1] - Valores[x0]) / (x1-x0);
        F1 = (Valores[x2] - Valores[x1]) / (x2 - x1);
        F2 = (F1 - F0) / (x2 - x0);

        Pn = Valores[x0] + ((x - x0) * F0) + ((x - x0) * (x- x1)) * F2;
        System.out.println(Pn);
    }
}