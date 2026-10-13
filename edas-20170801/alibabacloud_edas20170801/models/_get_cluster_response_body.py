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
        # The cluster information.
        self.cluster = cluster
        # The status code.
        self.code = code
        # The detailed message.
        self.message = message
        # The request ID.
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
        # The cluster ID.
        self.cluster_id = cluster_id
        # The cluster import status. Valid values:
        # - 1: Imported.
        # - 2: Import failed.
        # - 3: Importing.
        # - 4: Cluster deleted.
        # - 0: Not imported.
        self.cluster_import_status = cluster_import_status
        # The cluster name.
        self.cluster_name = cluster_name
        # The cluster type. Valid values:
        # - 0: Common Docker cluster.
        # - 1: Swarm cluster.
        # - 2: ECS cluster.
        # - 3: EDAS self-managed Kubernetes cluster.
        # - 4: Pandora auto-registered application cluster.
        # - 5: Container Service Kubernetes cluster.
        self.cluster_type = cluster_type
        # The total number of CPU cores.
        self.cpu = cpu
        # The number of used CPU cores.
        self.cpu_used = cpu_used
        # The timestamp when the cluster was created.
        self.create_time = create_time
        # The Container Service cluster ID.
        self.cs_cluster_id = cs_cluster_id
        # The description.
        self.description = description
        # The IaaS resource provider.
        self.iaas_provider = iaas_provider
        # The total memory. Unit: MB.
        self.mem = mem
        # The amount of used memory. Unit: MB.
        self.mem_used = mem_used
        # The network type. Valid values:
        # - 1: Classic network.
        # - 2: VPC.
        self.network_mode = network_mode
        # The number of ECS instances.
        self.node_num = node_num
        # The CPU overselling ratio for Docker clusters. Valid values:
        # - 1: 1:1 ratio. No overselling.
        # - 2: 1:2 overselling ratio.
        # - 4: 1:4 overselling ratio.
        # - 8: 1:8 overselling ratio.
        self.oversold_factor = oversold_factor
        # The region ID.
        self.region_id = region_id
        # The subtype of the Kubernetes cluster. ManagedKubernetes indicates an ACK cluster, Ask indicates an ASK cluster, and ExternalKubernetes indicates an external cluster.
        self.sub_cluster_type = sub_cluster_type
        # The timestamp when the cluster was last modified.
        self.update_time = update_time
        # The VPC ID.
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

