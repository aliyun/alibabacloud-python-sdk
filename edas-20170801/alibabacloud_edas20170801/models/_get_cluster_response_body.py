# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_edas20170801 import models as main_models
from darabonba.model import DaraModel

class GetClusterResponseBody(DaraModel):
    def __init__(
        self,
        cluster: main_models.GetClusterResponseBodyCluster = None,
        code: int = None,
        message: str = None,
        request_id: str = None,
    ):
        # The information about the cluster.
        self.cluster = cluster
        # The HTTP status code that is returned.
        self.code = code
        # The detailed information that is returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.cluster:
            self.cluster.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster is not None:
            result['Cluster'] = self.cluster.to_map()

        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cluster') is not None:
            temp_model = main_models.GetClusterResponseBodyCluster()
            self.cluster = temp_model.from_map(m.get('Cluster'))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetClusterResponseBodyCluster(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_import_status: int = None,
        cluster_name: str = None,
        cluster_type: int = None,
        cpu: int = None,
        cpu_used: int = None,
        create_time: int = None,
        cs_cluster_id: str = None,
        description: str = None,
        iaas_provider: str = None,
        mem: int = None,
        mem_used: int = None,
        network_mode: int = None,
        node_num: int = None,
        oversold_factor: int = None,
        region_id: str = None,
        sub_cluster_type: str = None,
        update_time: int = None,
        vpc_id: str = None,
    ):
        # The ID of the cluster.
        self.cluster_id = cluster_id
        # The import status of the cluster. Valid values:
        # 
        # - 1: The cluster is imported.
        # 
        # - 2: The cluster fails to be imported.
        # 
        # - 3: The cluster is being imported.
        # 
        # - 4: The cluster is deleted.
        # 
        # - 0: The cluster is not imported.
        self.cluster_import_status = cluster_import_status
        # The name of the cluster.
        self.cluster_name = cluster_name
        # The type of the cluster. Valid values:
        # 
        # - 0: regular Docker cluster
        # 
        # - 1: Swarm cluster
        # 
        # - 2: Elastic Compute Service (ECS) cluster
        # 
        # - 3: self-managed Kubernetes cluster in EDAS
        # 
        # - 4: cluster in which Pandora automatically registers applications
        # 
        # - 5: ACK cluster
        self.cluster_type = cluster_type
        # The total number of CPU cores.
        self.cpu = cpu
        # The number of used CPU cores.
        self.cpu_used = cpu_used
        # The time when the cluster was created. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.create_time = create_time
        # The ID of the Container Service for Kubernetes (ACK) cluster.
        self.cs_cluster_id = cs_cluster_id
        # The description of the cluster.
        self.description = description
        # The provider of Infrastructure as a Service (IaaS) resources used in the cluster.
        self.iaas_provider = iaas_provider
        # The total size of memory. Unit: MB.
        self.mem = mem
        # The size of used memory. Unit: MB.
        self.mem_used = mem_used
        # The network type of the cluster. Valid values:
        # 
        # - 1: classic network
        # 
        # - 2: virtual private cloud (VPC)
        self.network_mode = network_mode
        # The number of ECS instances.
        self.node_num = node_num
        # The overcommit ratio supported by a Docker cluster. Valid values:
        # 
        # - 1: 1:1, which means that resources are not overcommitted.
        # 
        # - 2: 1:2, which means that resources are overcommitted by 1:2.
        # 
        # - 4: 1:4, which means that resources are overcommitted by 1:4.
        # 
        # - 8: 1:8, which means that resources are overcommitted by 1:8.
        self.oversold_factor = oversold_factor
        # The ID of the region where the cluster resides.
        self.region_id = region_id
        # The subtype of the Kubernetes cluster. Valid values: ManagedKubernetes, Ask, and ExternalKubernetes. ManagedKubernetes refers to the ACK cluster. Ask refers to the Serverless Kubernetes (ASK) cluster. ExternalKubernetes refers to the external cluster.
        self.sub_cluster_type = sub_cluster_type
        # The time when the cluster was last modified. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.update_time = update_time
        # The ID of the virtual private cloud (VPC).
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.cluster_import_status is not None:
            result['ClusterImportStatus'] = self.cluster_import_status

        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type

        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.cpu_used is not None:
            result['CpuUsed'] = self.cpu_used

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.cs_cluster_id is not None:
            result['CsClusterId'] = self.cs_cluster_id

        if self.description is not None:
            result['Description'] = self.description

        if self.iaas_provider is not None:
            result['IaasProvider'] = self.iaas_provider

        if self.mem is not None:
            result['Mem'] = self.mem

        if self.mem_used is not None:
            result['MemUsed'] = self.mem_used

        if self.network_mode is not None:
            result['NetworkMode'] = self.network_mode

        if self.node_num is not None:
            result['NodeNum'] = self.node_num

        if self.oversold_factor is not None:
            result['OversoldFactor'] = self.oversold_factor

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.sub_cluster_type is not None:
            result['SubClusterType'] = self.sub_cluster_type

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ClusterImportStatus') is not None:
            self.cluster_import_status = m.get('ClusterImportStatus')

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')

        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('CpuUsed') is not None:
            self.cpu_used = m.get('CpuUsed')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CsClusterId') is not None:
            self.cs_cluster_id = m.get('CsClusterId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('IaasProvider') is not None:
            self.iaas_provider = m.get('IaasProvider')

        if m.get('Mem') is not None:
            self.mem = m.get('Mem')

        if m.get('MemUsed') is not None:
            self.mem_used = m.get('MemUsed')

        if m.get('NetworkMode') is not None:
            self.network_mode = m.get('NetworkMode')

        if m.get('NodeNum') is not None:
            self.node_num = m.get('NodeNum')

        if m.get('OversoldFactor') is not None:
            self.oversold_factor = m.get('OversoldFactor')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SubClusterType') is not None:
            self.sub_cluster_type = m.get('SubClusterType')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

