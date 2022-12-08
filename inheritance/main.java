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
public class main {
    public static void main(String[] args){
        luas_segitiga tiga = new luas_segitiga(2, 2);
        persegi_panjang pp = new persegi_panjang(5, 5);
        
        System.out.println("luas segitiga = " + tiga.luassegitiga());
        System.out.println("luas persegi_panjang = " + pp.luaspersegipanjang());
    }
    
}
