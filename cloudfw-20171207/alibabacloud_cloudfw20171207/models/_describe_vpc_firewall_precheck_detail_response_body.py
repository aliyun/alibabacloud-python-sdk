# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeVpcFirewallPrecheckDetailResponseBody(DaraModel):
    def __init__(
        self,
        is_found: bool = None,
        precheck_detail: main_models.DescribeVpcFirewallPrecheckDetailResponseBodyPrecheckDetail = None,
        request_id: str = None,
    ):
        self.is_found = is_found
        self.precheck_detail = precheck_detail
        self.request_id = request_id

    def validate(self):
        if self.precheck_detail:
            self.precheck_detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_found is not None:
            result['IsFound'] = self.is_found

        if self.precheck_detail is not None:
            result['PrecheckDetail'] = self.precheck_detail.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsFound') is not None:
            self.is_found = m.get('IsFound')

        if m.get('PrecheckDetail') is not None:
            temp_model = main_models.DescribeVpcFirewallPrecheckDetailResponseBodyPrecheckDetail()
            self.precheck_detail = temp_model.from_map(m.get('PrecheckDetail'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeVpcFirewallPrecheckDetailResponseBodyPrecheckDetail(DaraModel):
    def __init__(
        self,
        firewall_id: str = None,
        network_instance_id: str = None,
        precheck_entity_groups: List[main_models.DescribeVpcFirewallPrecheckDetailResponseBodyPrecheckDetailPrecheckEntityGroups] = None,
        precheck_status: str = None,
        precheck_timestamp: str = None,
        region_no: str = None,
    ):
        self.firewall_id = firewall_id
        self.network_instance_id = network_instance_id
        self.precheck_entity_groups = precheck_entity_groups
        self.precheck_status = precheck_status
        self.precheck_timestamp = precheck_timestamp
        self.region_no = region_no

    def validate(self):
        if self.precheck_entity_groups:
            for v1 in self.precheck_entity_groups:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.firewall_id is not None:
            result['FirewallId'] = self.firewall_id

        if self.network_instance_id is not None:
            result['NetworkInstanceId'] = self.network_instance_id

        result['PrecheckEntityGroups'] = []
        if self.precheck_entity_groups is not None:
            for k1 in self.precheck_entity_groups:
                result['PrecheckEntityGroups'].append(k1.to_map() if k1 else None)

        if self.precheck_status is not None:
            result['PrecheckStatus'] = self.precheck_status

        if self.precheck_timestamp is not None:
            result['PrecheckTimestamp'] = self.precheck_timestamp

        if self.region_no is not None:
            result['RegionNo'] = self.region_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FirewallId') is not None:
            self.firewall_id = m.get('FirewallId')

        if m.get('NetworkInstanceId') is not None:
            self.network_instance_id = m.get('NetworkInstanceId')

        self.precheck_entity_groups = []
        if m.get('PrecheckEntityGroups') is not None:
            for k1 in m.get('PrecheckEntityGroups'):
                temp_model = main_models.DescribeVpcFirewallPrecheckDetailResponseBodyPrecheckDetailPrecheckEntityGroups()
                self.precheck_entity_groups.append(temp_model.from_map(k1))

        if m.get('PrecheckStatus') is not None:
            self.precheck_status = m.get('PrecheckStatus')

        if m.get('PrecheckTimestamp') is not None:
            self.precheck_timestamp = m.get('PrecheckTimestamp')

        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')

        return self

class DescribeVpcFirewallPrecheckDetailResponseBodyPrecheckDetailPrecheckEntityGroups(DaraModel):
    def __init__(
        self,
        failed_count: int = None,
        name: str = None,
        precheck_entities: List[main_models.DescribeVpcFirewallPrecheckDetailResponseBodyPrecheckDetailPrecheckEntityGroupsPrecheckEntities] = None,
        precheck_entity_group_status: str = None,
    ):
        self.failed_count = failed_count
        self.name = name
        self.precheck_entities = precheck_entities
        self.precheck_entity_group_status = precheck_entity_group_status

    def validate(self):
        if self.precheck_entities:
            for v1 in self.precheck_entities:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failed_count is not None:
            result['FailedCount'] = self.failed_count

        if self.name is not None:
            result['Name'] = self.name

        result['PrecheckEntities'] = []
        if self.precheck_entities is not None:
            for k1 in self.precheck_entities:
                result['PrecheckEntities'].append(k1.to_map() if k1 else None)

        if self.precheck_entity_group_status is not None:
            result['PrecheckEntityGroupStatus'] = self.precheck_entity_group_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailedCount') is not None:
            self.failed_count = m.get('FailedCount')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.precheck_entities = []
        if m.get('PrecheckEntities') is not None:
            for k1 in m.get('PrecheckEntities'):
                temp_model = main_models.DescribeVpcFirewallPrecheckDetailResponseBodyPrecheckDetailPrecheckEntityGroupsPrecheckEntities()
                self.precheck_entities.append(temp_model.from_map(k1))

        if m.get('PrecheckEntityGroupStatus') is not None:
            self.precheck_entity_group_status = m.get('PrecheckEntityGroupStatus')

        return self

class DescribeVpcFirewallPrecheckDetailResponseBodyPrecheckDetailPrecheckEntityGroupsPrecheckEntities(DaraModel):
    def __init__(
        self,
        info: str = None,
        name: str = None,
        status: str = None,
        suggestion: str = None,
    ):
        self.info = info
        self.name = name
        self.status = status
        self.suggestion = suggestion

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.info is not None:
            result['Info'] = self.info

        if self.name is not None:
            result['Name'] = self.name

        if self.status is not None:
            result['Status'] = self.status

        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Info') is not None:
            self.info = m.get('Info')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')

        return self

