# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dfs20180620 import models as main_models
from darabonba.model import DaraModel

class GetAccessRuleResponseBody(DaraModel):
    def __init__(
        self,
        access_rule: main_models.GetAccessRuleResponseBodyAccessRule = None,
        request_id: str = None,
    ):
        self.access_rule = access_rule
        self.request_id = request_id

    def validate(self):
        if self.access_rule:
            self.access_rule.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_rule is not None:
            result['AccessRule'] = self.access_rule.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessRule') is not None:
            temp_model = main_models.GetAccessRuleResponseBodyAccessRule()
            self.access_rule = temp_model.from_map(m.get('AccessRule'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetAccessRuleResponseBodyAccessRule(DaraModel):
    def __init__(
        self,
        access_group_id: str = None,
        access_rule_id: str = None,
        create_time: str = None,
        description: str = None,
        network_segment: str = None,
        priority: int = None,
        rwaccess_type: str = None,
        region_id: str = None,
    ):
        self.access_group_id = access_group_id
        self.access_rule_id = access_rule_id
        self.create_time = create_time
        self.description = description
        self.network_segment = network_segment
        self.priority = priority
        self.rwaccess_type = rwaccess_type
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_group_id is not None:
            result['AccessGroupId'] = self.access_group_id

        if self.access_rule_id is not None:
            result['AccessRuleId'] = self.access_rule_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.network_segment is not None:
            result['NetworkSegment'] = self.network_segment

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.rwaccess_type is not None:
            result['RWAccessType'] = self.rwaccess_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessGroupId') is not None:
            self.access_group_id = m.get('AccessGroupId')

        if m.get('AccessRuleId') is not None:
            self.access_rule_id = m.get('AccessRuleId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('NetworkSegment') is not None:
            self.network_segment = m.get('NetworkSegment')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('RWAccessType') is not None:
            self.rwaccess_type = m.get('RWAccessType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

