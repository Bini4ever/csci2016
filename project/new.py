import sqlite3

def main():

    portfolioList = sqlite3.connect('portfolio.dat')
    portfolioList.execute('drop table if exists portfolioList')
    portfolioList.execute('create table portfolioList (t1 text, t2 text, i1 int, i2 float, i3 float, i4 float)')
    portfolioList.execute('insert into portfolioList (t1, t2, i1, i2, i3, i4) values (?, ?, ?, ?, ?, ?)', ('MMM', '3M', 100, 74.00, 118.30, 11830))
    portfolioList.execute('insert into portfolioList (t1, t2, i1, i2, i3, i4) values (?, ?, ?, ?, ?, ?)', ('MDT', 'Medtronic', 50, 56.10, 48.00, 2400))
    portfolioList.execute('insert into portfolioList (t1, t2, i1, i2, i3, i4) values (?, ?, ?, ?, ?, ?)', ('NWAC', 'Northwest Airlines', 100, 67.50, 18.04, 1804))
    portfolioList.execute('insert into portfolioList (t1, t2, i1, i2, i3, i4) values (?, ?, ?, ?, ?, ?)', ('SGI', 'Silicon Graphics', 100, 22.25, 2.25, 225))

    cursor = portfolioList.execute('select * from portfolioList order by t1')
    for row in cursor:
        print(row)

    portfolioList.commit()
     

if __name__ == "__main__":
    main()
