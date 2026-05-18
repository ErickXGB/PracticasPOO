class SolarSetManager:
    def __init__(self):
        self.team_a_brands: set[str] = {"Victron", "Growatt", "Must Solar", "Victron", "Fronius"}

        self.team_b_brands: set[str] = {"Deye", "Victron", "Phocos", "Growatt"}

    def display_unique_sets(self) -> None:

        print("COMPONENTE DE AUDITORÍA HARDWARE (CONJUNTOS ÚNICOS)")
        print(f"Catálogo sugerido por Equipo A (Set único): {self.team_a_brands}")
        print(f"Catálogo sugerido por Equipo B (Set único): {self.team_b_brands}")

    def execute_set_algebra(self) -> None:
        print("\nOPERACIONES MATEMÁTICAS DE CONJUNTOS (ALGEBRA DE SETS)")

        all_available_brands: set[str] = self.team_a_brands | self.team_b_brands
        print(f"UNIÓN (|) - Total de marcas evaluadas sin duplicados:")
        print(all_available_brands)

        common_brands: set[str] = self.team_a_brands & self.team_b_brands
        print(f"\nINTERSECCIÓN (&) - Marcas aprobadas en consenso mutuo:")
        print(common_brands)

        exclusive_to_a: set[str] = self.team_a_brands - self.team_b_brands
        print(f"\nDIFERENCIA (-) - Marcas exclusivas del Equipo A (No elegidas por B):")
        print(exclusive_to_a)



def run_bloque11_practice():
    manager = SolarSetManager()

    manager.display_unique_sets()
    manager.execute_set_algebra()