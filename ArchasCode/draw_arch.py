from diagrams import Diagram, Cluster
from diagrams.aws.compute import EC2
from diagrams.aws.network import ELB
from diagrams.aws.network import Route53
# Would typically use RDS from aws.database
from diagrams.onprem.database import PostgreSQL
# Would typically use ElastiCache from aws.database
from diagrams.onprem.inmemory import Redis
import os

os.environ["PATH"] += os.pathsep + 'C://Program Files//Graphviz//bin'


def generate_diagram():
    # It's LR by default, but you have a few options with the orientation
    with Diagram("Simple Website Diagram", direction='LR') as diag:
        dns = Route53("dns")
        load_balancer = ELB("Load Balancer")
        database = PostgreSQL("User Database")
        # cache = Redis("Cache")
        with Cluster("Webserver Cluster"):
            svc_group = [EC2("Webserver 1"),
                         EC2("Webserver 2"),
                         EC2("Webserver 3")]
        dns >> load_balancer >> svc_group
        #svc_group >> cache
        svc_group >> database
    diag
    return
