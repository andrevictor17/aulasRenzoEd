public class MyTests {

    	@Test
    	public void teste_lista_vazia() {
        MyClass tester = new MyClass(); 
	assertEquals([], sort([]));
    
	}

	@Test
    	public void teste_lista_unitaria() {
        MyClass tester = new MyClass(); 
	assertEquals([1], quick_sort([1]));
    
	}

	@Test
    	public void teste_lista_binaria() {
        MyClass tester = new MyClass(); 
	assertEquals([1, 2], quick_sort([2, 1]));
    
	}

	@Test
    	public void teste_lista_desordenada() {
        MyClass tester = new MyClass(); 
	assertEquals([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], quick_sort([9, 7, 1, 8, 5, 3, 6, 4, 2, 0]));
    
	}

	@Test
    	public void teste_lista_com_elementos_repetidos() {
        MyClass tester = new MyClass(); 
	assertEquals([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9], quick_sort([9, 7, 1, 8, 5, 3, 6, 4, 2, 0, 9, 9]));
    
	}

	@Test
    	public void teste_lista_so_com_elementos_repetidos() {
        MyClass tester = new MyClass(); 
	assertEquals([9, 9, 9], quick_sort([9, 9, 9]));
    
	}



}
