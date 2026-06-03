import pandas

"""
Auther: Varatharuban B.
Capstone project for Machine Learning
"""

class HDB:

    dataset = None
    
    def __init__(self, dataset):
        print("Initialize HDB class .....")
        self.dataset = dataset

    # Get all towns in the dataset
    def get_all_towns(self):
        return self.dataset.town.unique().tolist()

    # Get all available flat types
    def get_flat_types(self):
        return self.dataset.flat_type.unique().tolist()

    # Get all available flat models
    def get_flat_models(self):
        return self.dataset.flat_model.unique().tolist()

    # Get all available story range
    def get_storey_ranges(self):
        return self.dataset.storey_range.unique().tolist()
        
    # Get dataset by town
    def get_dataset_by_town(self, town):
        return self.dataset.loc[self.dataset['town'] == town]

    # Get average price by the town
    def get_average_price_by_town(self, town):
        return self.get_dataset_by_town(town)['resale_price'].mean()

    # Get highest price by the town
    def get_highest_price_by_town(self, town):
        return self.get_dataset_by_town(town)['resale_price'].max()
        
    # Get lowest price by the town
    def get_lowest_price_by_town(self, town):
        return self.get_dataset_by_town(town)['resale_price'].min()
        