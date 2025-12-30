# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eflo_controller20221215 import models as main_models
from darabonba.model import DaraModel

class ListFreeNodesResponseBody(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        nodes: List[main_models.ListFreeNodesResponseBodyNodes] = None,
        request_id: str = None,
    ):
        # The returned pagination token which can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The nodes.
        self.nodes = nodes
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.nodes:
            for v1 in self.nodes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_token is not None:
            result['NextToken'] = self.next_token

        result['Nodes'] = []
        if self.nodes is not None:
            for k1 in self.nodes:
                result['Nodes'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        self.nodes = []
        if m.get('Nodes') is not None:
            for k1 in m.get('Nodes'):
                temp_model = main_models.ListFreeNodesResponseBodyNodes()
                self.nodes.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListFreeNodesResponseBodyNodes(DaraModel):
    def __init__(
        self,
        commodity_code: str = None,
        create_time: str = None,
        expired_time: str = None,
        hpn_zone: str = None,
        hyper_node_id: str = None,
        machine_type: str = None,
        node_id: str = None,
        operating_state: str = None,
        resource_group_id: str = None,
        sn: str = None,
        tags: List[main_models.ListFreeNodesResponseBodyNodesTags] = None,
        zone_id: str = None,
    ):
        # The commodity code.
        self.commodity_code = commodity_code
        # The creation time.
        self.create_time = create_time
        # The time when the node expires.
        self.expired_time = expired_time
        # The cluster number.
        self.hpn_zone = hpn_zone
        self.hyper_node_id = hyper_node_id
        # The instance type.
        self.machine_type = machine_type
        # The node ID.
        self.node_id = node_id
        # The node status.
        self.operating_state = operating_state
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The serial number of the node.
        self.sn = sn
        # The tags.
        self.tags = tags
        # The zone ID.
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
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time

        if self.hpn_zone is not None:
            result['HpnZone'] = self.hpn_zone

        if self.hyper_node_id is not None:
            result['HyperNodeId'] = self.hyper_node_id

        if self.machine_type is not None:
            result['MachineType'] = self.machine_type

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.operating_state is not None:
            result['OperatingState'] = self.operating_state

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.sn is not None:
            result['Sn'] = self.sn

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')

        if m.get('HpnZone') is not None:
            self.hpn_zone = m.get('HpnZone')

        if m.get('HyperNodeId') is not None:
            self.hyper_node_id = m.get('HyperNodeId')

        if m.get('MachineType') is not None:
            self.machine_type = m.get('MachineType')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('OperatingState') is not None:
            self.operating_state = m.get('OperatingState')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Sn') is not None:
            self.sn = m.get('Sn')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListFreeNodesResponseBodyNodesTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class ListFreeNodesResponseBodyNodesTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
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

