import boto3

class EKSClusterInfo:
    def __init__(self, cluster_name, region='us-west-2'):
        self.cluster_name = cluster_name
        self.region = region
        self.eks_client = boto3.client('eks', region_name=region)
        self.ec2_client = boto3.client('ec2', region_name=region)

    def get_cluster_info(self):
        try:
            response = self.eks_client.describe_cluster(name=self.cluster_name)
            cluster_info = response['cluster']
            endpoint = cluster_info['endpoint']
            security_group_ids = cluster_info['resourcesVpcConfig']['securityGroupIds']
            subnet_ids = cluster_info['resourcesVpcConfig']['subnetIds']

            return {
                'endpoint': endpoint,
                'security_group_ids': security_group_ids,
                'subnet_ids': subnet_ids
            }
        except Exception as e:
            print(f"Error retrieving cluster info: {e}")
            return None

    def tag_security_group(self, security_group_id, tag_key='karpenter.sh', tag_value=None):
        if not tag_value:
            tag_value = self.cluster_name

        try:
            self.ec2_client.create_tags(
                Resources=[security_group_id],
                Tags=[{'Key': tag_key, 'Value': tag_value}]
            )
            print(f"Tagged security group {security_group_id} with {tag_key}={tag_value}")
        except Exception as e:
            print(f"Error tagging security group {security_group_id}: {e}")

    def tag_subnets(self, subnet_ids, tag_key='karpenter.sh', tag_value=None):
        if not tag_value:
            tag_value = self.cluster_name

        try:
            self.ec2_client.create_tags(
                Resources=subnet_ids,
                Tags=[{'Key': tag_key, 'Value': tag_value}]
            )
            print(f"Tagged subnets {subnet_ids} with {tag_key}={tag_value}")
        except Exception as e:
            print(f"Error tagging subnets {subnet_ids}: {e}")

    def process_cluster(self):
        cluster_info = self.get_cluster_info()
        if cluster_info:
            for sg_id in cluster_info['security_group_ids']:
                self.tag_security_group(sg_id)

            self.tag_subnets(cluster_info['subnet_ids'])
        else:
            print("Failed to retrieve cluster information.")

# Import the EKSClusterInfo class from eks_cluster_info
from eks_cluster_info import EKSClusterInfo

def main():
    # Example usage of the EKSClusterInfo class
    cluster_name = 'my-eks-cluster'
    region = 'us-west-2'

    # Create an instance of EKSClusterInfo
    cluster_info = EKSClusterInfo(cluster_name=cluster_name, region=region)
    
    # Process the cluster (retrieve info, tag resources)
    cluster_info.process_cluster()

if __name__ == '__main__':
    main()

