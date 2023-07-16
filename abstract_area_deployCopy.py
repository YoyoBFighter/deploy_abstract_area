from abc import ABCMeta, abstractmethod
import streamlit as st
st.button("By Yossef")
title= st.title("Shape Calculation")


class Shape (metaclass=ABCMeta):
    @abstractmethod
    def area(self):
        pass

class rectangle(Shape):
    def __init__(self,width,length,height):
        self.width=width
        self.length=length
        self.height=height

    def area(self):
        return self.width*self.length 
    def perimeter(self):
        return (self.width+self.length) *2
    def size(self):
        return self.height*self.width*self.length 

class square(Shape):
    def __init__(self,length):
        self.length=length

    def area(self):
        return self.length**2 
    def perimeter(self):
        return self.length*4
    def size(self):
        return self.length**3 

class circle(Shape):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return 3.14 *self.radius**2
    def perimeter(self):
        return 3.14 *self.radius*2
    def size(self):
        return 3.14 * self.radius**3 * 4/3
    
    
i=["Rectangle","Circle","Square"]
#i=st.text_input("Enter your shape one of (Rectangle - Circle - Square) : ")




while True:
    #if i=="Rectangle":
    if st.checkbox("Rectangle"):
        st.header("Rectangle")
        x=st.number_input("Enter width of rectangle")
        y=st.number_input("Enter length of rectangle")
        z=st.number_input("Enter height of rectangle")
        rect=rectangle(x,y,z)

        st.write('Area: ',rect.area())
            
        st.write('Perimeter: ',rect.perimeter())
            
        st.write('Size: ',rect.size())
        break
    elif st.checkbox("Circle"):
    #elif i=="Circle":
        st.header("Circle")
        r=st.number_input("Enter radius of circle")
        cir = circle(r)
        st.write('Area: ',cir.area())
        st.write('Perimeter: ',cir.perimeter())
        st.write('Size: ',cir.size())
        break    
    elif st.checkbox("Square"):
    #elif i=="Square":
        st.header("Square")
        l=st.number_input("Enter length of square")
        
        squ=square(l)

    

    
        st.write('Area: ',squ.area())
        st.write('Perimeter: ',squ.perimeter())
        st.write('Size: ',squ.size())

        break
