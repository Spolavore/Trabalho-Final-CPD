def teste():
  ratings = [4, 5, 2 , 3 , 1] * 4
  orr_ratings = []
  ratings_already_checked = []
  i = 0
  while i != 20:
            maior = -1
           
            for rating in ratings:
            
                if rating > maior and rating not in ratings_already_checked:
                    maior = rating

            orr_ratings.append(maior)
            ratings_already_checked.append(maior)
            i += 1
  print(orr_ratings)
teste()