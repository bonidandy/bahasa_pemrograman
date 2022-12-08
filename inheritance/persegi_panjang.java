/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package segitiga;

/**
 *
 * @author lenovo
 */
public class persegi_panjang extends datar {
    //inisialisasi
    persegi_panjang(double panjang, double lebar){
    super (panjang, lebar, 0.0, 0.0);
        
    }
    public double luaspersegipanjang(){
       return panjang*lebar;
    }
}
