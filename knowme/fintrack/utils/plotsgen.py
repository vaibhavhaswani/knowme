import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from knowme.settings import MEDIA_ROOT
import uuid
import os

def gen_plots(df):
    eda_id=str(uuid.uuid4())
    if not os.path.exists(MEDIA_ROOT):
        os.mkdir(MEDIA_ROOT)
    eda_path=os.path.join(MEDIA_ROOT,eda_id)
    os.mkdir(eda_path)
    df.type.value_counts().plot.bar().get_figure().savefig(os.path.join(eda_path,'bar.png'))
    df.type.value_counts().plot.pie().get_figure().savefig(os.path.join(eda_path,'pie.png'))
    df.important.value_counts().plot.bar().get_figure().savefig(os.path.join(eda_path,'bar2.png'))
    plt.figure(figsize=(15,10))
    plt.title('Most Expenseful days of Month')
    sns.lineplot(x=df.date,y=df.amount).get_figure().savefig(os.path.join(eda_path,'exline.png'))
    return eda_id