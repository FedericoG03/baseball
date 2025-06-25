from database.DB_connect import DBConnect
from model.squadra import Squadra


class DAO():
    @staticmethod
    def getAnni():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ select distinct `year` 
                    from teams t 
                    where `year` >=1980"""

        cursor.execute(query,)

        for row in cursor:
            result.append((row['year']))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getSquadre(anno):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ select ID, teamCode, name 
                    from teams t 
                    where `year` = %s"""

        cursor.execute(query,(anno,) )

        for row in cursor:
            result.append(Squadra(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getEdges(anno, idMap):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select t.ID as id, sum(s.salary) as salary
                    from teams t , salaries s ,appearances a 
                    where s.`year` =t.`year`
                    and t.`year` = a.`year` 
                    and t.`year` = %s
                    and t.ID = s.teamID
                    and a.playerID = s.playerID 
                    group by t.teamCode  """

        cursor.execute(query, (anno,))

        for row in cursor:
            #result.append((idMap[row['id']], row['salary']))
            result[idMap[row['id']]] = row['salary']
        cursor.close()
        conn.close()
        return result



