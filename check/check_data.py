from random import randint
from netCDF4 import Dataset
import sys

def generate_point():
    points = []

    for i in range(10):
        point = []
        part_times = randint(0,2919)
        all_times = part_times + (int(year) - 1951) * 2920
        lats = randint(0,327)
        lons = randint(0,799)

        point += part_times
        point += all_times
        point += lats
        point += lons

        points += point

    return points


def check_hus():
    part_data = Dataset(year+'_'+ensemble_member+'.nc', 'r')
    part_hus = part_data
    all_hus_data = Dataset('huss_'+ensemble_member+'_final.nc', 'r')
    printf()


def check_pr():
    all_pr_data = Data
    printf()


def check_ps():
    printf()


def check_rlds():
    printf()


def check_rsds():
    printf()


def check_wind_speed():
    printf()


def check_ta():
    printf()


if __name__ == '__main__':
    if len(sys.argv < 3):
        raise Exception('arg1: ensemble membler\narg2: year')

    ensemble_member = sys.argv[1]
    year = sys.argv[2]

    points = generate_points()

    if(check_hus() && check_pr() && check_ps()  && check_rlds()  && check_rsds()  && check_wind_speed()  && check_ta()):
        printf(year+'_'+ensemble_member+'.nc: ok')
    else:
        printf(year+'_'+ensemble_member+'.nc: corrupted')
