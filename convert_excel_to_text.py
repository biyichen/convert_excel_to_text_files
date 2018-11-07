
# coding: utf-8

# In[94]:


import xlrd


# In[98]:


i = 1


# In[99]:


for i in range(0,20):
    workbook = xlrd.open_workbook('/Users/biyichen/Desktop/IceCreamDataSet.xlsx')
    sheet = workbook.sheets()[0]
    content = sheet.col_values(1)[i]
    filename = 'file_{}.txt'.format(i)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
        i+=1;
    if i == 11:
        break
    else:
        continue

