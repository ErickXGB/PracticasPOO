class BatteryBalanceManager:
    def __init__(self):
        self.total_capacity_ah: int = 100
        self.consumed_capacity_ah: int = 20
        self.parallel_strings: int = 2
        self.cell_divider: int = 4
        self.safety_constant: int = 52

    def calculate_energy_metrics(self) -> None:
        print("DIAGNÓSTICO DEL BANCO SOLAR")
        
        remaining = self.total_capacity_ah - self.consumed_capacity_ah  
        total_parallel = remaining * self.parallel_strings              
        per_cell_float = total_parallel / self.cell_divider           
        per_cell_int = total_parallel // self.cell_divider             
        cell_residue = total_parallel % self.cell_divider              
        scaled_power = self.parallel_strings ** 3                       

        print(f"Capacidad Restante:        {remaining} Ah")
        print(f"Capacidad Total Paralela:  {total_parallel} Ah")
        print(f"Amperaje por Celda (Real):  {per_cell_float} Ah")
        print(f"Amperaje por Celda (Entero):{per_cell_int} Ah")
        print(f"Residuo de Distribución:   {cell_residue} Ah")
        print(f"Factor de Potencia Escalar: {scaled_power}")

    def evaluate_cell_identity(self) -> None:
        print("\nAUDITORÍA DE CELDAS")
        
        cell_voltages_pack1: list[float] = [3.2, 3.2, 3.3]
        cell_voltages_pack2: list[float] = [3.2, 3.2, 3.3]

        are_contents_equal = (cell_voltages_pack1 == cell_voltages_pack2)
        are_objects_identical = (cell_voltages_pack1 is cell_voltages_pack2)

        print(f"Voltajes Pack 1: {cell_voltages_pack1}")
        print(f"Voltajes Pack 2: {cell_voltages_pack2}")
        print(f"¿Tienen los mismos voltajes internos? (==): {are_contents_equal}")
        print(f"¿Apuntan al mismo objeto en memoria RAM? (is): {are_objects_identical}")
        print("[Explicación]: Tienen los mismos datos, pero son dos paquetes físicos distintos.")

    def analyze_operator_precedence(self) -> None:
        print("\nEVALUACIÓN CON JERARQUÍA DE OPERADORES")

        net_charge = (self.total_capacity_ah - self.consumed_capacity_ah) * self.parallel_strings // self.cell_divider + self.safety_constant
        
        print("Fórmula Ejecutada: (100 - 20) * 2 // 4 + 52")
        print(f"Resultado de Carga Neta: {net_charge} %")
        print("Orden de Resolución: (Paréntesis) -> Multiplicación -> División Entera -> Suma")


def run_bloque3_practice():
    manager = BatteryBalanceManager()

    manager.calculate_energy_metrics()
    manager.evaluate_cell_identity()
    manager.analyze_operator_precedence()