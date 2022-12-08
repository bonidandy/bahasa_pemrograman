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
public class luas_segitiga extends datar {
    //inisialisasi
    luas_segitiga(double tinggi, double alas){
    super (0.0, 0.0, alas, tinggi);
        
    }
    public double luassegitiga(){
       return 0.5 * alas * tinggi;
    }
}

