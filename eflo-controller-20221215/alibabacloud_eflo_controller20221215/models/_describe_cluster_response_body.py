# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eflo_controller20221215 import models as main_models
from darabonba.model import DaraModel

class DescribeClusterResponseBody(DaraModel):
    def __init__(
        self,
        cluster_description: str = None,
        cluster_id: str = None,
        cluster_name: str = None,
        cluster_type: str = None,
        components: List[main_models.DescribeClusterResponseBodyComponents] = None,
        computing_ip_version: str = None,
        create_time: str = None,
        hpn_zone: str = None,
        networks: main_models.DescribeClusterResponseBodyNetworks = None,
        node_count: int = None,
        node_group_count: int = None,
        open_eni_jumbo_frame: str = None,
        operating_state: str = None,
        request_id: str = None,
        resource_group_id: str = None,
        security_group_id: str = None,
        task_id: str = None,
        update_time: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        # The cluster description.
        self.cluster_description = cluster_description
        # The cluster ID.
        self.cluster_id = cluster_id
        # The cluster name.
        self.cluster_name = cluster_name
        # The cluster type.
        self.cluster_type = cluster_type
        # The component information.
        self.components = components
        # The IP type of the computing network.
        self.computing_ip_version = computing_ip_version
        # The creation time.
        self.create_time = create_time
        # The cluster number.
        self.hpn_zone = hpn_zone
        # The network information.
        self.networks = networks
        # The number of nodes.
        self.node_count = node_count
        # The number of node groups.
        self.node_group_count = node_group_count
        # The status of Jumbo Frames for the elastic network interface (ENI).
        self.open_eni_jumbo_frame = open_eni_jumbo_frame
        # The cluster status.
        self.operating_state = operating_state
        # The request ID.
        self.request_id = request_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        self.security_group_id = security_group_id
        # The job ID.
        self.task_id = task_id
        # The update time.
        self.update_time = update_time
        self.v_switch_id = v_switch_id
        # The ID of the virtual private cloud (VPC).
        self.vpc_id = vpc_id

    def validate(self):
        if self.components:
            for v1 in self.components:
                 if v1:
                    v1.validate()
        if self.networks:
            self.networks.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_description is not None:
            result['ClusterDescription'] = self.cluster_description

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type

        result['Components'] = []
        if self.components is not None:
            for k1 in self.components:
                result['Components'].append(k1.to_map() if k1 else None)

        if self.computing_ip_version is not None:
            result['ComputingIpVersion'] = self.computing_ip_version

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.hpn_zone is not None:
            result['HpnZone'] = self.hpn_zone

        if self.networks is not None:
            result['Networks'] = self.networks.to_map()

        if self.node_count is not None:
            result['NodeCount'] = self.node_count

        if self.node_group_count is not None:
            result['NodeGroupCount'] = self.node_group_count

        if self.open_eni_jumbo_frame is not None:
            result['OpenEniJumboFrame'] = self.open_eni_jumbo_frame

        if self.operating_state is not None:
            result['OperatingState'] = self.operating_state

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterDescription') is not None:
            self.cluster_description = m.get('ClusterDescription')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')

        self.components = []
        if m.get('Components') is not None:
            for k1 in m.get('Components'):
                temp_model = main_models.DescribeClusterResponseBodyComponents()
                self.components.append(temp_model.from_map(k1))

        if m.get('ComputingIpVersion') is not None:
            self.computing_ip_version = m.get('ComputingIpVersion')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('HpnZone') is not None:
            self.hpn_zone = m.get('HpnZone')

        if m.get('Networks') is not None:
            temp_model = main_models.DescribeClusterResponseBodyNetworks()
            self.networks = temp_model.from_map(m.get('Networks'))

        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')

        if m.get('NodeGroupCount') is not None:
            self.node_group_count = m.get('NodeGroupCount')

        if m.get('OpenEniJumboFrame') is not None:
            self.open_eni_jumbo_frame = m.get('OpenEniJumboFrame')

        if m.get('OperatingState') is not None:
            self.operating_state = m.get('OperatingState')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class DescribeClusterResponseBodyNetworks(DaraModel):
    def __init__(
        self,
        vpd_id: str = None,
    ):
        # The ID of the CIDR block for the cluster.
        self.vpd_id = vpd_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.vpd_id is not None:
            result['VpdId'] = self.vpd_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VpdId') is not None:
            self.vpd_id = m.get('VpdId')

        return self

class DescribeClusterResponseBodyComponents(DaraModel):
    def __init__(
        self,
        component_id: str = None,
        component_type: str = None,
    ):
        # The component ID.
        self.component_id = component_id
        # The component type.
        # 
        # Valid values:
        # 
        # *   ARMS
        # *   ACKEdge
        self.component_type = component_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.component_id is not None:
            result['ComponentId'] = self.component_id

        if self.component_type is not None:
            result['ComponentType'] = self.component_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComponentId') is not None:
            self.component_id = m.get('ComponentId')

        if m.get('ComponentType') is not None:
            self.component_type = m.get('ComponentType')

        return self

