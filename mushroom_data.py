import pandas as pd 
import matplotlib.pyplot as plt

df=pd.read_csv('C:/Users/Nishu/Desktop/matplotlib/mushrooms.csv')

df=df.dropna(subset=['class','cap-shape','cap-surface','cap-color','bruises','odor','gill-attachment','gill-spacing','gill-size','gill-color'])

#BAR CHART
df['class']=df['class'].map({'e':'Edible','p':'Poisonous'})
class_counts=df['class'].value_counts()
plt.figure(figsize=(8,6))
plt.bar(class_counts.index,class_counts.values,color=['lightgreen','skyblue'])
plt.title('Class Distribution')
plt.xlabel('Varieties of Mushroom')
plt.ylabel('Number of Mushroom')
plt.tight_layout()
plt.savefig('Class_Distribution_In_Mushroom.png')
plt.show()

#PIE CHART

cap_shape_counts=df['cap-shape'].value_counts()
plt.figure(figsize=(8,6))
plt.pie(cap_shape_counts,labels=cap_shape_counts.index,autopct='%1.1f%%',startangle=90)
plt.title('Cap-shape Distribution')
plt.tight_layout()
plt.savefig('Cap-shape_In_Mushroom.png')
plt.show()

#BAR CHART [CAP-SURFACE]

df['cap-surface']=df['cap-surface'].map({'f':'Fibrous','g':'Groves','y':'Scaly Cap','s':'Smooth'})
surface_variation=df['cap-surface'].value_counts()
plt.figure(figsize=(8,6))
plt.bar(surface_variation.index,surface_variation.values)
plt.title('Types of Surface in Mushroom')
plt.xlabel('Varieties')
plt.ylabel('Counts')
plt.tight_layout()
plt.savefig('Cap_Surface_Varieties_In_Mushroom.png')
plt.show()


#PIE CHART [CAP COLOR]

df['cap-color']=df['cap-color'].map({'n':'Brown','b':'Buff','c':'Cinnamon','g':'Gray','r':'Green','p':'Pink','u':'Purple','e':'Red','w':'White','y':'Yellow'})
color_varieties=df['cap-color'].value_counts()
plt.figure(figsize=(8,6))
plt.pie(color_varieties,labels=color_varieties.index,autopct='%1.1f%%',startangle=90)
plt.title('Color Varieties in Mushroom')
plt.savefig('Color_Varieties_In_Mushroom.png')
plt.show()

#PIE CHART

df['bruises']=df['bruises'].map({'t':'True','f':'False'})
injured_or_not=df['bruises'].value_counts()
plt.figure(figsize=(8,6))
plt.pie(injured_or_not,labels=injured_or_not.index,autopct='%1.1f%%',startangle=90)
plt.title('Percent of Mushroom have bruises or not')
plt.tight_layout()
plt.savefig("Percentage_of_Mushroom_Have_Bruises_or_Not.png")
plt.show()

#BAR CHART

df['odor']=df['odor'].map({'a':'Almond','l':'Anise','c':'Creosote','y':'Fishy','f':'Foul','m':'Musty','n':'None','p':'Pungent','s':'Spicy'})
odor_counts=df['odor'].value_counts()
plt.figure(figsize=(8,6))
plt.barh(odor_counts.index,odor_counts.values)
plt.tight_layout()
plt.title('Types of Odor in Mushroom')
plt.xlabel('Odors')
plt.ylabel('Counts')
plt.savefig('Odor_In_Mushroom.png')
plt.show()

#PIE CHART

df['gill-attachment']=df['gill-attachment'].map({'a':'attached','d':'descending','f':'free','n':'notched'})
gill_attachment=df['gill-attachment'].value_counts()
plt.figure(figsize=(8,6))
plt.pie(gill_attachment,labels=gill_attachment.index,autopct='%1.1f%%',startangle=90)
plt.tight_layout()
plt.title("Gill Attchment")
plt.savefig('Gill_Attachment_in_Mushroom.png')
plt.show()

#GILL SPACING
df['gill-spacing']=df['gill-spacing'].map({'c':'close','d':'distant','c':'crowded'})
gill_spacing=df['gill-spacing'].value_counts()
plt.figure(figsize=(8,6))
plt.pie(gill_spacing,labels=gill_spacing.index,autopct='%1.1f%%',startangle=90)
plt.tight_layout()
plt.title("Gill Spacing")
plt.savefig('Gill_Spacing_in_Mushroom.png')
plt.show()

#HORIZONTAL BAR CHART

df['gill-color']=df['gill-color'].map({'k':'black','n':'brown','b':'buff','h':'chocolate','g':'gray','r':'green','o':'orange','p':'pink','u':'purple','e':'red','w':'white','y':'yellow'})
gill_color=df['gill-color'].value_counts()
plt.figure(figsize=(8,6))
plt.barh(gill_color.index,gill_color.values)
plt.tight_layout()
plt.title('Gill_Color')
plt.xlabel('Color')
plt.ylabel('Counts')
plt.savefig('Gill_Color_In_Color.png')
plt.show()