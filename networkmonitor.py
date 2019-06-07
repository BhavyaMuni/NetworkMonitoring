import click
from psutil import net_io_counters
import time


@click.command()
@click.option("--type", prompt="Type(u/d/both)")
def get_bandwidth(type):
    while True:
        if type == 'both':
            up1 = net_io_counters().bytes_sent
            down1 = net_io_counters().bytes_recv
            t1 = time.time()
            time.sleep(2)
            up2 = net_io_counters().bytes_sent
            down2 = net_io_counters().bytes_recv
            t2 = time.time()

            down_kb = ((down2-down1)/(t2-t1))/1024
            up_kb = ((up2-up1)/(t2-t1))/1024
        
            click.echo("Upload : {} kb/s \nDownload : {} kb/s\n".format(up_kb, down_kb))
        elif type == 'd':
            down1 = net_io_counters().bytes_recv
            t1 = time.time()
            time.sleep(2)
            down2 = net_io_counters().bytes_recv
            t2 = time.time()

            down_kb = ((down2-down1)/(t2-t1))/1024

            click.echo("Download : {} kb/s\n".format(down_kb))
        elif type == 'u':
            up1 = net_io_counters().bytes_sent
            t1 = time.time()
            time.sleep(2)
            up2 = net_io_counters().bytes_sent
            t2 = time.time()

            up_kb = ((up2-up1)/(t2-t1))/1024

            click.echo("Upload : {} kb/s\n".format(up_kb))

    click.clear()

if __name__ == '__main__':
    get_bandwidth()