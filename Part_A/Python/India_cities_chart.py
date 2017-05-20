import pandas as pd
import pylab as plt

class india_cities:

    def __init__(self, file_name,):
        self.file_name = file_name

    def load_data(self):
        self.df_india = pd.read_csv(self.file_name)
        return

    def create_chart(self):
        df_filter = self.df_india[['state_name', 'literates_total']]
        df_filter = pd.DataFrame({
            'literates_total': df_filter.groupby(['state_name'])['literates_total'].sum()}).reset_index()
        df_filter = df_filter.sort_values(['literates_total'], ascending =False)
        df_filter = df_filter[:15]

        literates_total = list(df_filter['literates_total'])
        state_name = range(0, 15)
        LABELS = list(df_filter['state_name'])

        plt.bar(state_name, literates_total, align='center')
        plt.xticks(state_name, LABELS, rotation=15)
        plt.title('Number of Literates by State name',fontsize=20)
        plt.show()
        return


def main(file_name):
    obj_india = india_cities(file_name)
    obj_india.load_data()
    obj_india.create_chart()


if __name__ == "__main__":
    file_name = '.\cities_r2.csv'
    main(file_name)
