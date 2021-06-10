import pandas as pd
import json
import seaborn as sb
import matplotlib.pyplot as plt
import numpy as np
from sqlalchemy import create_engine
from sqlalchemy.sql import select
engine = create_engine('postgresql://project2:test1234@localhost:5432/project2')
conn = engine.connect()
#select_st = select([ga_merge.ZCTA5CE10,ga_merge.GEOID10,ga_merge.ALAND10,ga_merge.AWATER10,ga_merge.INTPTLAT10,ga_merge.INTPTLON10,ga_merge.PARTFLG10,ga_merge.RegionID,ga_merge.SizeRank,ga_merge.RegionType,ga_merge.StateName,ga_merge.State,ga_merge.City,ga_merge.Metro,ga_merge.CountyName,ga_merge.1996-01-31,ga_merge.1996-02-29,ga_merge.1996-03-31,ga_merge.1996-04-30,ga_merge.1996-05-31,ga_merge.1996-06-30,ga_merge.1996-07-31,ga_merge.1996-08-31,ga_merge.1996-09-30,ga_merge.1996-10-31,ga_merge.1996-11-30,ga_merge.1996-12-31,ga_merge.1997-01-31,ga_merge.1997-02-28,ga_merge.1997-03-31,ga_merge.1997-04-30,ga_merge.1997-05-31,ga_merge.1997-06-30,ga_merge.1997-07-31,ga_merge.1997-08-31,ga_merge.1997-09-30,ga_merge.1997-10-31,ga_merge.1997-11-30,ga_merge.1997-12-31,ga_merge.1998-01-31,ga_merge.1998-02-28,ga_merge.1998-03-31,ga_merge.1998-04-30,ga_merge.1998-05-31,ga_merge.1998-06-30,ga_merge.1998-07-31,ga_merge.1998-08-31,ga_merge.1998-09-30,ga_merge.1998-10-31,ga_merge.1998-11-30,ga_merge.1998-12-31,ga_merge.1999-01-31,ga_merge.1999-02-28,ga_merge.1999-03-31,ga_merge.1999-04-30,ga_merge.1999-05-31,ga_merge.1999-06-30,ga_merge.1999-07-31,ga_merge.1999-08-31,ga_merge.1999-09-30,ga_merge.1999-10-31,ga_merge.1999-11-30,ga_merge.1999-12-31,ga_merge.2000-01-31,ga_merge.2000-02-29,ga_merge.2000-03-31,ga_merge.2000-04-30,ga_merge.2000-05-31,ga_merge.2000-06-30,ga_merge.2000-07-31,ga_merge.2000-08-31,ga_merge.2000-09-30,ga_merge.2000-10-31,ga_merge.2000-11-30,ga_merge.2000-12-31,ga_merge.2001-01-31,ga_merge.2001-02-28,ga_merge.2001-03-31,ga_merge.2001-04-30,ga_merge.2001-05-31,ga_merge.2001-06-30,ga_merge.2001-07-31,ga_merge.2001-08-31,ga_merge.2001-09-30,ga_merge.2001-10-31,ga_merge.2001-11-30,ga_merge.2001-12-31,ga_merge.2002-01-31,ga_merge.2002-02-28,ga_merge.2002-03-31,ga_merge.2002-04-30,ga_merge.2002-05-31,ga_merge.2002-06-30,ga_merge.2002-07-31,ga_merge.2002-08-31,ga_merge.2002-09-30,ga_merge.2002-10-31,ga_merge.2002-11-30,ga_merge.2002-12-31,ga_merge.2003-01-31,ga_merge.2003-02-28,ga_merge.2003-03-31,ga_merge.2003-04-30,ga_merge.2003-05-31,ga_merge.2003-06-30,ga_merge.2003-07-31,ga_merge.2003-08-31,ga_merge.2003-09-30,ga_merge.2003-10-31,ga_merge.2003-11-30,ga_merge.2003-12-31,ga_merge.2004-01-31,ga_merge.2004-02-29,ga_merge.2004-03-31,ga_merge.2004-04-30,ga_merge.2004-05-31,ga_merge.2004-06-30,ga_merge.2004-07-31,ga_merge.2004-08-31,ga_merge.2004-09-30,ga_merge.2004-10-31,ga_merge.2004-11-30,ga_merge.2004-12-31,ga_merge.2005-01-31,ga_merge.2005-02-28,ga_merge.2005-03-31,ga_merge.2005-04-30,ga_merge.2005-05-31,ga_merge.2005-06-30,ga_merge.2005-07-31,ga_merge.2005-08-31,ga_merge.2005-09-30,ga_merge.2005-10-31,ga_merge.2005-11-30,ga_merge.2005-12-31,ga_merge.2006-01-31,ga_merge.2006-02-28,ga_merge.2006-03-31,ga_merge.2006-04-30,ga_merge.2006-05-31,ga_merge.2006-06-30,ga_merge.2006-07-31,ga_merge.2006-08-31,ga_merge.2006-09-30,ga_merge.2006-10-31,ga_merge.2006-11-30,ga_merge.2006-12-31,ga_merge.2007-01-31,ga_merge.2007-02-28,ga_merge.2007-03-31,ga_merge.2007-04-30,ga_merge.2007-05-31,ga_merge.2007-06-30,ga_merge.2007-07-31,ga_merge.2007-08-31,ga_merge.2007-09-30,ga_merge.2007-10-31,ga_merge.2007-11-30,ga_merge.2007-12-31,ga_merge.2008-01-31,ga_merge.2008-02-29,ga_merge.2008-03-31,ga_merge.2008-04-30,ga_merge.2008-05-31,ga_merge.2008-06-30,ga_merge.2008-07-31,ga_merge.2008-08-31,ga_merge.2008-09-30,ga_merge.2008-10-31,ga_merge.2008-11-30,ga_merge.2008-12-31,ga_merge.2009-01-31,ga_merge.2009-02-28,ga_merge.2009-03-31,ga_merge.2009-04-30,ga_merge.2009-05-31,ga_merge.2009-06-30,ga_merge.2009-07-31,ga_merge.2009-08-31,ga_merge.2009-09-30,ga_merge.2009-10-31,ga_merge.2009-11-30,ga_merge.2009-12-31,ga_merge.2010-01-31,ga_merge.2010-02-28,ga_merge.2010-03-31,ga_merge.2010-04-30,ga_merge.2010-05-31,ga_merge.2010-06-30,ga_merge.2010-07-31,ga_merge.2010-08-31,ga_merge.2010-09-30,ga_merge.2010-10-31,ga_merge.2010-11-30,ga_merge.2010-12-31,ga_merge.2011-01-31,ga_merge.2011-02-28,ga_merge.2011-03-31,ga_merge.2011-04-30,ga_merge.2011-05-31,ga_merge.2011-06-30,ga_merge.2011-07-31,ga_merge.2011-08-31,ga_merge.2011-09-30,ga_merge.2011-10-31,ga_merge.2011-11-30,ga_merge.2011-12-31,ga_merge.2012-01-31,ga_merge.2012-02-29,ga_merge.2012-03-31,ga_merge.2012-04-30,ga_merge.2012-05-31,ga_merge.2012-06-30,ga_merge.2012-07-31,ga_merge.2012-08-31,ga_merge.2012-09-30,ga_merge.2012-10-31,ga_merge.2012-11-30,ga_merge.2012-12-31,ga_merge.2013-01-31,ga_merge.2013-02-28,ga_merge.2013-03-31,ga_merge.2013-04-30,ga_merge.2013-05-31,ga_merge.2013-06-30,ga_merge.2013-07-31,ga_merge.2013-08-31,ga_merge.2013-09-30,ga_merge.2013-10-31,ga_merge.2013-11-30,ga_merge.2013-12-31,ga_merge.2014-01-31,ga_merge.2014-02-28,ga_merge.2014-03-31,ga_merge.2014-04-30,ga_merge.2014-05-31,ga_merge.2014-06-30,ga_merge.2014-07-31,ga_merge.2014-08-31,ga_merge.2014-09-30,ga_merge.2014-10-31,ga_merge.2014-11-30,ga_merge.2014-12-31,ga_merge.2015-01-31,ga_merge.2015-02-28,ga_merge.2015-03-31,ga_merge.2015-04-30,ga_merge.2015-05-31,ga_merge.2015-06-30,ga_merge.2015-07-31,ga_merge.2015-08-31,ga_merge.2015-09-30,ga_merge.2015-10-31,ga_merge.2015-11-30,ga_merge.2015-12-31,ga_merge.2016-01-31,ga_merge.2016-02-29,ga_merge.2016-03-31,ga_merge.2016-04-30,ga_merge.2016-05-31,ga_merge.2016-06-30,ga_merge.2016-07-31,ga_merge.2016-08-31,ga_merge.2016-09-30,ga_merge.2016-10-31,ga_merge.2016-11-30,ga_merge.2016-12-31,ga_merge.2017-01-31,ga_merge.2017-02-28,ga_merge.2017-03-31,ga_merge.2017-04-30,ga_merge.2017-05-31,ga_merge.2017-06-30,ga_merge.2017-07-31,ga_merge.2017-08-31,ga_merge.2017-09-30,ga_merge.2017-10-31,ga_merge.2017-11-30,ga_merge.2017-12-31,ga_merge.2018-01-31,ga_merge.2018-02-28,ga_merge.2018-03-31,ga_merge.2018-04-30,ga_merge.2018-05-31,ga_merge.2018-06-30,ga_merge.2018-07-31,ga_merge.2018-08-31,ga_merge.2018-09-30,ga_merge.2018-10-31,ga_merge.2018-11-30,ga_merge.2018-12-31,ga_merge.2019-01-31,ga_merge.2019-02-28,ga_merge.2019-03-31,ga_merge.2019-04-30,ga_merge.2019-05-31,ga_merge.2019-06-30,ga_merge.2019-07-31,ga_merge.2019-08-31,ga_merge.2019-09-30,ga_merge.2019-10-31,ga_merge.2019-11-30,ga_merge.2019-12-31,ga_merge.2020-01-31,ga_merge.2020-02-29,ga_merge.2020-03-31,ga_merge.2020-04-30,ga_merge.2020-05-31,ga_merge.2020-06-30,ga_merge.2020-07-31,ga_merge.2020-08-31,ga_merge.2020-09-30,ga_merge.2020-10-31,ga_merge.2020-11-30,ga_merge.2020-12-31,ga_merge.2021-01-31,ga_merge.2021-02-28,ga_merge.2021-03-31,ga_merge.2021-04-30,ga_merge.Population,ga_merge.Median_Age,ga_merge.Household_Income,ga_merge.Per_Capita_Income,ga_merge.Poverty_Count,ga_merge.Poverty_Rate])
colname = engine.execute('select * from ga_merge').keys()
result = engine.execute('select * from ga_merge')
#data = result.fetchall()
#data = result.fetchall()
data = result.fetchall() 


# In[18]:


#data = json.load(open("ga_merge.json"))
#data = json.load(result.fetchall())
#ga_data = pd.json_normalize(result.fetchall(), "features")
ga_data = pd.json_normalize(data)
ga_df = pd.DataFrame(ga_data)
ga_df.columns = colname
ga_df


# In[20]:


#ga_clean_df = ga_df.drop(columns=['type','properties.STATEFP10' ,'geometry.coordinates', 'geometry.type', 'properties.CLASSFP10', 'properties.MTFCC10', 'properties.FUNCSTAT10' ])
#ga_clean_df.columns = ['ZCTA5CE10','GEOID10','ALAND10','AWATER10','INTPTLAT10','INTPTLON10','PARTFLG10','RegionID','SizeRank','RegionType','StateName','State','City','Metro','CountyName','1996-01-31','1996-02-29','1996-03-31','1996-04-30','1996-05-31','1996-06-30','1996-07-31','1996-08-31','1996-09-30','1996-10-31','1996-11-30','1996-12-31','1997-01-31','1997-02-28','1997-03-31','1997-04-30','1997-05-31','1997-06-30','1997-07-31','1997-08-31','1997-09-30','1997-10-31','1997-11-30','1997-12-31','1998-01-31','1998-02-28','1998-03-31','1998-04-30','1998-05-31','1998-06-30','1998-07-31','1998-08-31','1998-09-30','1998-10-31','1998-11-30','1998-12-31','1999-01-31','1999-02-28','1999-03-31','1999-04-30','1999-05-31','1999-06-30','1999-07-31','1999-08-31','1999-09-30','1999-10-31','1999-11-30','1999-12-31','2000-01-31','2000-02-29','2000-03-31','2000-04-30','2000-05-31','2000-06-30','2000-07-31','2000-08-31','2000-09-30','2000-10-31','2000-11-30','2000-12-31','2001-01-31','2001-02-28','2001-03-31','2001-04-30','2001-05-31','2001-06-30','2001-07-31','2001-08-31','2001-09-30','2001-10-31','2001-11-30','2001-12-31','2002-01-31','2002-02-28','2002-03-31','2002-04-30','2002-05-31','2002-06-30','2002-07-31','2002-08-31','2002-09-30','2002-10-31','2002-11-30','2002-12-31','2003-01-31','2003-02-28','2003-03-31','2003-04-30','2003-05-31','2003-06-30','2003-07-31','2003-08-31','2003-09-30','2003-10-31','2003-11-30','2003-12-31','2004-01-31','2004-02-29','2004-03-31','2004-04-30','2004-05-31','2004-06-30','2004-07-31','2004-08-31','2004-09-30','2004-10-31','2004-11-30','2004-12-31','2005-01-31','2005-02-28','2005-03-31','2005-04-30','2005-05-31','2005-06-30','2005-07-31','2005-08-31','2005-09-30','2005-10-31','2005-11-30','2005-12-31','2006-01-31','2006-02-28','2006-03-31','2006-04-30','2006-05-31','2006-06-30','2006-07-31','2006-08-31','2006-09-30','2006-10-31','2006-11-30','2006-12-31','2007-01-31','2007-02-28','2007-03-31','2007-04-30','2007-05-31','2007-06-30','2007-07-31','2007-08-31','2007-09-30','2007-10-31','2007-11-30','2007-12-31','2008-01-31','2008-02-29','2008-03-31','2008-04-30','2008-05-31','2008-06-30','2008-07-31','2008-08-31','2008-09-30','2008-10-31','2008-11-30','2008-12-31','2009-01-31','2009-02-28','2009-03-31','2009-04-30','2009-05-31','2009-06-30','2009-07-31','2009-08-31','2009-09-30','2009-10-31','2009-11-30','2009-12-31','2010-01-31','2010-02-28','2010-03-31','2010-04-30','2010-05-31','2010-06-30','2010-07-31','2010-08-31','2010-09-30','2010-10-31','2010-11-30','2010-12-31','2011-01-31','2011-02-28','2011-03-31','2011-04-30','2011-05-31','2011-06-30','2011-07-31','2011-08-31','2011-09-30','2011-10-31','2011-11-30','2011-12-31','2012-01-31','2012-02-29','2012-03-31','2012-04-30','2012-05-31','2012-06-30','2012-07-31','2012-08-31','2012-09-30','2012-10-31','2012-11-30','2012-12-31','2013-01-31','2013-02-28','2013-03-31','2013-04-30','2013-05-31','2013-06-30','2013-07-31','2013-08-31','2013-09-30','2013-10-31','2013-11-30','2013-12-31','2014-01-31','2014-02-28','2014-03-31','2014-04-30','2014-05-31','2014-06-30','2014-07-31','2014-08-31','2014-09-30','2014-10-31','2014-11-30','2014-12-31','2015-01-31','2015-02-28','2015-03-31','2015-04-30','2015-05-31','2015-06-30','2015-07-31','2015-08-31','2015-09-30','2015-10-31','2015-11-30','2015-12-31','2016-01-31','2016-02-29','2016-03-31','2016-04-30','2016-05-31','2016-06-30','2016-07-31','2016-08-31','2016-09-30','2016-10-31','2016-11-30','2016-12-31','2017-01-31','2017-02-28','2017-03-31','2017-04-30','2017-05-31','2017-06-30','2017-07-31','2017-08-31','2017-09-30','2017-10-31','2017-11-30','2017-12-31','2018-01-31','2018-02-28','2018-03-31','2018-04-30','2018-05-31','2018-06-30','2018-07-31','2018-08-31','2018-09-30','2018-10-31','2018-11-30','2018-12-31','2019-01-31','2019-02-28','2019-03-31','2019-04-30','2019-05-31','2019-06-30','2019-07-31','2019-08-31','2019-09-30','2019-10-31','2019-11-30','2019-12-31','2020-01-31','2020-02-29','2020-03-31','2020-04-30','2020-05-31','2020-06-30','2020-07-31','2020-08-31','2020-09-30','2020-10-31','2020-11-30','2020-12-31','2021-01-31','2021-02-28','2021-03-31','2021-04-30','Population','Median_Age','Household_Income','Per_Capita_Income','Poverty_Count','Poverty_Rate']


# In[21]:


ga_clean_df = ga_df
ga_clean_df.describe()


# In[22]:


ga_proverty_df = ga_clean_df.loc[ga_clean_df['Poverty_Rate'] >= 20]
ga_proverty_df = ga_proverty_df.dropna()
ga_proverty_df.head(10)


# In[23]:


ga_proverty_df = ga_proverty_df.replace(-666666666, 0)
ga_proverty_stats_df = ga_proverty_df[['Household_Income', 'Poverty_Rate', '2020-06-30', '2019-06-30', '2018-06-30', '2017-06-30', '2016-06-30']].describe()


# In[24]:


ga_proverty_stats_df


# In[25]:


ax = sb.regplot(x="2020-06-30", y="Household_Income", data=ga_proverty_df)
ax.figure.savefig("2020-06-30-pro.png")

# In[26]:


ax = sb.regplot(x="2019-06-30", y="Household_Income", data=ga_proverty_df)
ax.figure.savefig("2019-06-30-pro.png")

# In[27]:


ax = sb.regplot(x="2018-06-30", y="Household_Income", data=ga_proverty_df)
ax.figure.savefig("2018-06-30-pro.png")

# In[28]:


ax = sb.regplot(x="2017-06-30", y="Household_Income", data=ga_proverty_df)
ax.figure.savefig("2017-06-30-pro.png")

# In[29]:


ga_proverty_hp_2017 = ga_proverty_df['2017-06-30'].median()
ga_proverty_hp_2018 = ga_proverty_df['2018-06-30'].median()
ga_proverty_hp_2019 = ga_proverty_df['2019-06-30'].median()
ga_proverty_hp_2020 = ga_proverty_df['2020-06-30'].median()
#ga_proverty_hp_5yr_df = pd.append([ga_proverty_hp_2017_df, gdescribea_proverty_hp_2018_df, ga_proverty_hp_2019_df, ga_proverty_hp_2020_df])
dpoor ={ '2006':ga_proverty_df['2006-06-30'].median(),'2007':ga_proverty_df['2007-06-30'].median(), '2008': ga_proverty_df['2008-06-30'].median(),'2009': ga_proverty_df['2009-06-30'].median(),'2010':ga_proverty_df['2010-06-30'].median(),'2011': ga_proverty_df['2011-06-30'].median(),'2012': ga_proverty_df['2012-06-30'].median(),'2013': ga_proverty_df['2013-06-30'].median(),'2014': ga_proverty_df['2014-06-30'].median(),'2015': ga_proverty_df['2015-06-30'].median(), '2016': ga_proverty_df['2016-06-30'].median(),'2017': ga_proverty_df['2017-06-30'].median(), '2018': ga_proverty_df['2018-06-30'].median(), '2019': ga_proverty_df['2019-06-30'].median(), '2020': ga_proverty_df['2020-06-30'].median()}

#'2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020'
index=['2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020']
ga_proverty_hp_5yr_df = pd.DataFrame(data=dpoor, index=['Time'])
#ga_proverty_hp_5yr_df.set_index(['2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020'])


# In[30]:


plt.rcParams['figure.figsize'] = [15, 10]
years = list(dpoor.keys())
values = list(dpoor.values())
my_colors = 'rgbkymc'

plt.bar(years, values, color=my_colors)
#plt.hist(ga_proverty_hp_5yr_df)
plt.show()
plt.savefig("proverty-hp-2006-2020.png")





ga_clean2_df = ga_clean_df.dropna()
ga_rich_df = ga_clean2_df.loc[ga_clean2_df['Poverty_Rate'] < 10]
ga_rich_df


# In[32]:


ax = sb.regplot(x="2020-06-30", y="Household_Income", data=ga_rich_df)
#plt.xlim(0, 100000)
plt.ticklabel_formaga_proverty_hp_2017 = ga_proverty_df['2017-06-30'].median()
ga_proverty_hp_2018 = ga_proverty_df['2018-06-30'].median()
ga_proverty_hp_2019 = ga_proverty_df['2019-06-30'].median()
ga_proverty_hp_2020 = ga_proverty_df['2020-06-30'].median()
plt.ticklabel_format(style='plain', axis='x')
plt.show()
plt.savefig("rich-hp-2018-2020.png")

# In[33]:


ax = sb.regplot(x="2019-06-30", y="Household_Income", data=ga_rich_df)
plt.ticklabel_format(style='plain', axis='x')
plt.show()
plt.savefig("rich-hp-2019.png")

# In[34]:


ax = sb.regplot(x="2018-06-30", y="Household_Income", data=ga_rich_df)
plt.ticklabel_format(style='plain', axis='x')
plt.show()
plt.savefig("rich-hp-2018.png")

# In[35]:


ax = sb.regplot(x="2017-06-30", y="Household_Income", data=ga_rich_df)
plt.ticklabel_format(style='plain', axis='x')
plt.show()
plt.savefig("rich-hp-2017.png")

# In[36]:


ga_rich_stats_df = ga_rich_df[['Household_Income', 'Poverty_Rate', '2020-06-30', '2019-06-30', '2018-06-30', '2017-06-30', '2016-06-30']].astype('int64').describe()


# In[37]:


ga_rich_stats_df


# In[38]:


ga_rich_hp_2017 = ga_rich_df['2017-06-30'].median()
ga_rich_hp_2018 = ga_rich_df['2018-06-30'].median()
ga_rich_hp_2019 = ga_rich_df['2019-06-30'].median()
ga_rich_hp_2020 = ga_rich_df['2020-06-30'].median()
drich ={ '2006':ga_rich_df['2006-06-30'].median(),'2007':ga_rich_df['2007-06-30'].median(), '2008': ga_rich_df['2008-06-30'].median(),'2009': ga_rich_df['2009-06-30'].median(),'2010':ga_rich_df['2010-06-30'].median(),'2011': ga_rich_df['2011-06-30'].median(),'2012': ga_rich_df['2012-06-30'].median(),'2013': ga_rich_df['2013-06-30'].median(),'2014': ga_rich_df['2014-06-30'].median(),'2015': ga_rich_df['2015-06-30'].median(), '2016': ga_rich_df['2016-06-30'].median(),'2017': ga_rich_df['2017-06-30'].median(), '2018': ga_rich_df['2018-06-30'].median(), '2019': ga_rich_df['2019-06-30'].median(), '2020': ga_rich_df['2020-06-30'].median()}
ga_rich_hp_5yr_df = pd.DataFrame(data=drich, index=['Time'])
plt.rcParams['figure.figsize'] = [20, 10]
my_colors = 'rgbkymc'
ryears = list(drich.keys())
rvalues = list(drich.values())
plt.bar(ryears, rvalues, color=my_colors)

plt.savefig("rich-hp-2006-2020.png")
# In[ ]:





# In[ ]:




