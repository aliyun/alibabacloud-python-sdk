# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeHybridCloudClusterRulesRequest(DaraModel):
    def __init__(
        self,
        cluster_id: int = None,
        instance_id: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_manager_resource_group_id: str = None,
        rule_content: str = None,
        rule_match_type: str = None,
        rule_type: str = None,
    ):
        # This parameter is required.
        self.cluster_id = cluster_id
        # This parameter is required.
        self.instance_id = instance_id
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id
        self.resource_manager_resource_group_id = resource_manager_resource_group_id
        self.rule_content = rule_content
        self.rule_match_type = rule_match_type
        # This parameter is required.
        self.rule_type = rule_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id

        if self.rule_content is not None:
            result['RuleContent'] = self.rule_content

        if self.rule_match_type is not None:
            result['RuleMatchType'] = self.rule_match_type

        if self.rule_type is not None:
            result['RuleType'] = self.rule_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')

        if m.get('RuleContent') is not None:
            self.rule_content = m.get('RuleContent')

        if m.get('RuleMatchType') is not None:
            self.rule_match_type = m.get('RuleMatchType')

        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')

        return self

