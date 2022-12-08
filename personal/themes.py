class Split:
    
    @staticmethod
    def data(data):
        lines = data.split("\n") # list of lines

        return lines

    @staticmethod
    def lines(lines):
        groups = []
        
        for line in lines:
            group = line.split(", ") 
            groups.append(group) # list of lists of themes

        return groups

    @staticmethod
    def groups(groups):
        # [[1,2,3], [4,5,6]] -> [1,2,3,4,5,6]
        # use manual for loops
            # instead of themes = sum(groups,[])
            # bc string.strip() for strings only, not lists
            
        themes = []
        
        for group in groups:
            for theme in group:
                theme = theme.strip()
                themes.append(theme)
        
        return themes

class Themes:
    
    @staticmethod
    def count(themes):
        theme_count = {}
        
        for theme in themes:
            if theme not in theme_count.keys():
                theme_count.update({theme : 0})
                
            theme_count[theme] += 1

        return theme_count

    @staticmethod
    def sort(theme_count):
        # in:  {theme2:count2, theme1:count1, theme3:count3}
        # out: {theme1:count1, theme2:count2: theme3:count3}

        theme_count_list = theme_count.items() # list of tuples
        theme_count_list = sorted(theme_count_list) # alphabetical

        count = lambda theme_count_list: theme_count_list[1] # 1 bc second tuple element (key)
        theme_count_list = sorted(theme_count_list, key=count) # by value

        theme_count = dict(theme_count_list)

        return theme_count

    @staticmethod
    def show(theme_count):
        for theme in theme_count:
            # don't use enumerate(dict) bc doesn't give values
                # theme : count -> n. theme, n = 0,1,2...
            print(f"{theme}: {theme_count[theme]}")

def main():
    data = """Beauty Standards, Media Exposure, Body Image
    Beauty Standards, Cultural Hybridization
    Body Image, Beauty and Race/Culture
    Cultivation Theory, Body Image, Beauty-related Consumption
    Hallyu Consumption Behavior, Beauty Standards, Cultural Hybridization 
    Beauty Standards, Cultural Hybridization
    Human Beauty
    Hallyu Consumption Behavior, Self-presentation
    Beauty Standards, Body Image, Media Exposure
    Cultivation Theory, Hallyu Consumption Behavior, Beauty Standards, Body Image
    Sexism, Sikolohiyang Pilipino, Kagandahang Panloob at Panlabas
    Beauty Standards, Hallyu Consumption Behavior"""
    
    lines  = Split.data(data)
    groups = Split.lines(lines)
    themes = Split.groups(groups)

    theme_count = Themes.count(themes)
    theme_count = Themes.sort(theme_count)

    Themes.show(theme_count)

if __name__ == "__main__":
    main()