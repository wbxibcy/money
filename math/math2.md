**变量定义：**

- $n$：工件数量
- $F$：工厂数量
- $m$：每个工厂的机器数量
- $k$：装配工厂的装配流水线长度
- $x_{ijf}$：工件 $i$ 在工厂 $f$ 的机器 $j$ 上的加工顺序。取值为 0 或 1，表示工件 $i$ 在工厂 $f$ 的机器 $j$ 上加工的顺序。
- $y_{if}$：工件 $i$ 是否被分配给工厂 $f$ 进行加工。取值为 0 或 1，表示工件 $i$ 是否被分配给工厂 $f$ 进行加工。
- $a_{if}$：工件 $i$ 在工厂 $f$ 的加工时间。
- $b_{iq}$：工件 $i$ 在产品 $q$ 的装配顺序。取值为 0 或 1，表示工件 $i$ 在产品 $q$ 的装配顺序。

**参数定义：**

- $O_{ij}$：工件 $i$ 在机器 $j$ 上的加工时间。
- $L$：工艺路线数量，即装配阶段的产品数量。

**约束条件：**

1. 每个工件只能分配给一个工厂进行加工：
   - $\sum_{f=1}^{F} y_{if} = 1, \quad \forall i$
2. 每个工厂的机器容量约束：
   - $\sum_{j=1}^{m} x_{ijf} \leq 1, \quad \forall i, f$
3. 工件加工顺序约束：
   - $b_{iq} \leq b_{i+1, q}, \quad \forall i < n, \forall q$
4. 机器互斥约束：
   - $\sum_{i=1}^{n} x_{ijf} \leq 1, \quad \forall j, f$

**优化目标：**

最小化总生产时间（makespan），即从零件生产开始直到产品装配完成的总时间：

- $\min \sum_{f=1}^{F} \left( \sum_{j=1}^{m} \left( \sum_{i=1}^{n} a_{if} \cdot x_{ijf} \right) + \sum_{q=1}^{L} \left( \sum_{i=1}^{n} b_{iq} \right) \right)$






$$
x_{ijf} = \left\{
\begin{array}{ll}
1, & \text{如果工件 } i \text{ 需要在工厂 } f \text{ 的第 } j \text{ 台机器上加工} \\
0, & \text{否则}
\end{array}
\right.
\quad (j=1,2,\dots,m)
$$
当j=1时：

$$x_{i1f} = \left\{
\begin{array}{ll}
1, & \text{如果工件 } i \text{ 需要在工厂 } f \text{ 的第一台机器上加工}\\
0, & \text{否则}
\end{array}
\right.
$$

当j=2时：

$$x_{i2f} = \left\{
\begin{array}{ll}
1, & \text{如果工件 } i \text{ 需要在工厂 } f \text{ 的第二台机器上加工}\\
0, & \text{否则}
\end{array}
\right.
$$

···

当 *j*=*m* 时：

$$x_{imf} = \left\{
\begin{array}{ll}
1, & \text{如果工件 } i \text{ 需要在工厂 } f \text{ 的第 } m \text{ 台机器上加工}\\
0, & \text{否则}
\end{array}
\right.
$$



使用整数变量 $p_{ij}$描述工件 *i* 在工艺路线中被安排到第 *j* 步进行加工

当工件 *i* 在工厂 *f* 的第 *j* 个位置需要加工时，我们就让$p_{ij}$ 取值为 *k*，其中 *k* 代表该工件在工艺路线中的第 *k* 步
$$
p_{ij} = k \quad (k = 1,2,\dots,m) \quad \text{当且仅当}\quad x_{ijk} = 1 \\
\sum_{k=1}^{m}x_{ijk} = 1 \quad (\forall i,j)
$$
这个约束条件确保了每个工件只能在工艺路线中的一个位置被加工，从而避免了出现重复加工或未加工的情况。


$$
x_{ijk} = \left\{
\begin{array}{ll}
1, & \text{如果工件 } i \text{ 在工艺路线中的第 } j \text{ 步需要在工厂 } f \text{ 的第 } k \text{ 台机器上加工}\\
0, & \text{否则}
\end{array}
\right. \\
p_{ij} - p_{i,j-1}\geq 0 \quad \text{当且仅当} \quad x_{ijk}=x_{i,j-1,k}=1, j=2,\dots,n
$$
