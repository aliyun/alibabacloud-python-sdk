# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eflo_controller20221215 import models as main_models
from darabonba.model import DaraModel

class ListHyperNodesResponseBody(DaraModel):
    def __init__(
        self,
        hyper_nodes: List[main_models.ListHyperNodesResponseBodyHyperNodes] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
    ):
        self.hyper_nodes = hyper_nodes
        self.max_results = max_results
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.hyper_nodes:
            for v1 in self.hyper_nodes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['HyperNodes'] = []
        if self.hyper_nodes is not None:
            for k1 in self.hyper_nodes:
                result['HyperNodes'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.hyper_nodes = []
        if m.get('HyperNodes') is not None:
            for k1 in m.get('HyperNodes'):
                temp_model = main_models.ListHyperNodesResponseBodyHyperNodes()
                self.hyper_nodes.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListHyperNodesResponseBodyHyperNodes(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_name: str = None,
        commodity_code: str = None,
        create_time: str = None,
        expire_time: str = None,
        hostname: str = None,
        hpn_zone: str = None,
        hyper_node_id: str = None,
        machine_type: str = None,
        node_group_id: str = None,
        node_group_name: str = None,
        operating_state: str = None,
        resource_group_id: str = None,
        status: str = None,
        tags: List[main_models.ListHyperNodesResponseBodyHyperNodesTags] = None,
        task_id: str = None,
        zone_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.cluster_name = cluster_name
        self.commodity_code = commodity_code
        self.create_time = create_time
        self.expire_time = expire_time
        self.hostname = hostname
        self.hpn_zone = hpn_zone
        self.hyper_node_id = hyper_node_id
        self.machine_type = machine_type
        self.node_group_id = node_group_id
        self.node_group_name = node_group_name
        self.operating_state = operating_state
        self.resource_group_id = resource_group_id
        self.status = status
        self.tags = tags
        self.task_id = task_id
        self.zone_id = zone_id

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.hostname is not None:
            result['Hostname'] = self.hostname

        if self.hpn_zone is not None:
            result['HpnZone'] = self.hpn_zone

        if self.hyper_node_id is not None:
            result['HyperNodeId'] = self.hyper_node_id

        if self.machine_type is not None:
            result['MachineType'] = self.machine_type

        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id

        if self.node_group_name is not None:
            result['NodeGroupName'] = self.node_group_name

        if self.operating_state is not None:
            result['OperatingState'] = self.operating_state

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.status is not None:
            result['Status'] = self.status

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')

        if m.get('HpnZone') is not None:
            self.hpn_zone = m.get('HpnZone')

        if m.get('HyperNodeId') is not None:
            self.hyper_node_id = m.get('HyperNodeId')

        if m.get('MachineType') is not None:
            self.machine_type = m.get('MachineType')

        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')

        if m.get('NodeGroupName') is not None:
            self.node_group_name = m.get('NodeGroupName')

        if m.get('OperatingState') is not None:
            self.operating_state = m.get('OperatingState')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListHyperNodesResponseBodyHyperNodesTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class ListHyperNodesResponseBodyHyperNodesTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

