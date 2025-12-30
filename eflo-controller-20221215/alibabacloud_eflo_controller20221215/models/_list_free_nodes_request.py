# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eflo_controller20221215 import models as main_models
from darabonba.model import DaraModel

class ListFreeNodesRequest(DaraModel):
    def __init__(
        self,
        hpn_zone: str = None,
        machine_type: str = None,
        max_results: int = None,
        next_token: str = None,
        operating_states: List[str] = None,
        resource_group_id: str = None,
        tags: List[main_models.ListFreeNodesRequestTags] = None,
    ):
        # The cluster number.
        self.hpn_zone = hpn_zone
        # The instance type.
        self.machine_type = machine_type
        # The number of entries per page. Default value: 20.
        self.max_results = max_results
        # The token that determines the start position of the query. Set this parameter to the value of the NextToken parameter that is returned from the last call.
        self.next_token = next_token
        # The types of the returned nodes that are not used.
        self.operating_states = operating_states
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The tags.
        self.tags = tags

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
        if self.hpn_zone is not None:
            result['HpnZone'] = self.hpn_zone

        if self.machine_type is not None:
            result['MachineType'] = self.machine_type

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.operating_states is not None:
            result['OperatingStates'] = self.operating_states

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HpnZone') is not None:
            self.hpn_zone = m.get('HpnZone')

        if m.get('MachineType') is not None:
            self.machine_type = m.get('MachineType')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OperatingStates') is not None:
            self.operating_states = m.get('OperatingStates')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListFreeNodesRequestTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class ListFreeNodesRequestTags(DaraModel):
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

