import boto3
import subprocess
PROFILE = None

def getAllInIds(profile):
    PROFILE = profile
    dev = boto3.session.Session(profile_name=profile)
    ec2 = dev.resource('ec2')
    instanceIds=[]
    for instance in ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}]):
        instanceIds.append(instance.id)
    return instanceIds

def getProfiles():
    if subprocess.run(['./CheckInstalled.sh','boto3']).returncode == 0:
        return boto3.session.Session().available_profiles
    # return 1
    else:
        return 1


def get_instance_volumes(list_instance_ids):
    insvol = {}
    dev = boto3.session.Session(profile_name=PROFILE)
    ec2 = dev.resource('ec2')
    for instanceid in list_instance_ids:
        volumes = ec2.Instance(instanceid).volumes.all()
        insvol[instanceid] = [v.id for v in volumes]
    return insvol

