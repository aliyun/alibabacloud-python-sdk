# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_edas20170801 import models as main_models
from darabonba.model import DaraModel

class ListClusterResponseBody(DaraModel):
    def __init__(
        self,
        cluster_list: main_models.ListClusterResponseBodyClusterList = None,
        code: int = None,
        message: str = None,
        request_id: str = None,
    ):
        self.cluster_list = cluster_list
        # The HTTP status code that is returned.
        self.code = code
        # The additional information that is returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.cluster_list:
            self.cluster_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_list is not None:
            result['ClusterList'] = self.cluster_list.to_map()

        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterList') is not None:
            temp_model = main_models.ListClusterResponseBodyClusterList()
            self.cluster_list = temp_model.from_map(m.get('ClusterList'))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListClusterResponseBodyClusterList(DaraModel):
    def __init__(
        self,
        cluster: List[main_models.ListClusterResponseBodyClusterListCluster] = None,
    ):
        self.cluster = cluster

    def validate(self):
        if self.cluster:
            for v1 in self.cluster:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Cluster'] = []
        if self.cluster is not None:
            for k1 in self.cluster:
                result['Cluster'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cluster = []
        if m.get('Cluster') is not None:
            for k1 in m.get('Cluster'):
                temp_model = main_models.ListClusterResponseBodyClusterListCluster()
                self.cluster.append(temp_model.from_map(k1))

        return self

class ListClusterResponseBodyClusterListCluster(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
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
        resource_group_id: str = None,
        update_time: int = None,
        vpc_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.cluster_name = cluster_name
        self.cluster_type = cluster_type
        self.cpu = cpu
        self.cpu_used = cpu_used
        self.create_time = create_time
        self.cs_cluster_id = cs_cluster_id
        self.description = description
        self.iaas_provider = iaas_provider
        self.mem = mem
        self.mem_used = mem_used
        self.network_mode = network_mode
        self.node_num = node_num
        self.oversold_factor = oversold_factor
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.update_time = update_time
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

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

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

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

