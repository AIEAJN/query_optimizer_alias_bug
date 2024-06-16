# Installation
poetry install 

set up postgres and import database_name, dont forget to change database settings in django

start the project and go to /aliases/ for graphiql

## Query tests
Execute this query, you will see that the activeManga filter doesn't work 
```
query{
  A: Users(id:"A"){
    edges{
      node{
        id
        ActiveManga: usersMangaOwner(isActive:true orderBy:"-id"){
          edges{
            node{
              id
              name
              isActive
              isDeleted
            }
          }
        }
        AllManga: usersMangaOwner{
          edges{
            node{
              id
              name
              isActive
              isDeleted
            }
          }
        }
      }
    }
  }

}
```

Execute this query, you will see that the activeManga filter work now, just after removed the allAmanga query

```
query{
  A: Users(id:"A"){
    edges{
      node{
        id
        ActiveManga: usersMangaOwner(isActive:true orderBy:"-id"){
          edges{
            node{
              id
              name
              isActive
              isDeleted
            }
          }
        }
        # AllManga: usersMangaOwner{
        #   edges{
        #     node{
        #       id
        #       name
        #       isActive
        #       isDeleted
        #     }
        #   }
        # }
      }
    }
  }

}
```