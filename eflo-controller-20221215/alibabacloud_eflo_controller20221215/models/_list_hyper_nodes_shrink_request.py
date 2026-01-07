# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eflo_controller20221215 import models as main_models
from darabonba.model import DaraModel

class ListHyperNodesShrinkRequest(DaraModel):
    def __init__(
        self,
        cluster_name: str = None,
        commodity_code: str = None,
        hpn_zone: str = None,
        hyper_node_id: str = None,
        hyper_node_ids_shrink: str = None,
        machine_type: str = None,
        max_results: int = None,
        next_token: str = None,
        node_group_name: str = None,
        operating_states_shrink: str = None,
        resource_group_id: str = None,
        tags: List[main_models.ListHyperNodesShrinkRequestTags] = None,
        zone_id: str = None,
    ):
        self.cluster_name = cluster_name
        self.commodity_code = commodity_code
        self.hpn_zone = hpn_zone
        self.hyper_node_id = hyper_node_id
        self.hyper_node_ids_shrink = hyper_node_ids_shrink
        self.machine_type = machine_type
        self.max_results = max_results
        self.next_token = next_token
        self.node_group_name = node_group_name
        self.operating_states_shrink = operating_states_shrink
        self.resource_group_id = resource_group_id
        self.tags = tags
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
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code

        if self.hpn_zone is not None:
            result['HpnZone'] = self.hpn_zone

        if self.hyper_node_id is not None:
            result['HyperNodeId'] = self.hyper_node_id

        if self.hyper_node_ids_shrink is not None:
            result['HyperNodeIds'] = self.hyper_node_ids_shrink

        if self.machine_type is not None:
            result['MachineType'] = self.machine_type

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.node_group_name is not None:
            result['NodeGroupName'] = self.node_group_name

        if self.operating_states_shrink is not None:
            result['OperatingStates'] = self.operating_states_shrink

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        if m.get('HpnZone') is not None:
            self.hpn_zone = m.get('HpnZone')

        if m.get('HyperNodeId') is not None:
            self.hyper_node_id = m.get('HyperNodeId')

        if m.get('HyperNodeIds') is not None:
            self.hyper_node_ids_shrink = m.get('HyperNodeIds')

        if m.get('MachineType') is not None:
            self.machine_type = m.get('MachineType')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('NodeGroupName') is not None:
            self.node_group_name = m.get('NodeGroupName')

        if m.get('OperatingStates') is not None:
            self.operating_states_shrink = m.get('OperatingStates')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListHyperNodesShrinkRequestTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class ListHyperNodesShrinkRequestTags(DaraModel):
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

