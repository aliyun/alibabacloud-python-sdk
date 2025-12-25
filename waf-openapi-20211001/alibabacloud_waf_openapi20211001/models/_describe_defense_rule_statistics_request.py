# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDefenseRuleStatisticsRequest(DaraModel):
    def __init__(
        self,
        fourth_key: str = None,
        instance_id: str = None,
        primary_key: str = None,
        region_id: str = None,
        resource_manager_resource_group_id: str = None,
        secondary_key: str = None,
        template_id: int = None,
        third_key: str = None,
    ):
        self.fourth_key = fourth_key
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.primary_key = primary_key
        self.region_id = region_id
        self.resource_manager_resource_group_id = resource_manager_resource_group_id
        self.secondary_key = secondary_key
        # This parameter is required.
        self.template_id = template_id
        self.third_key = third_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fourth_key is not None:
            result['FourthKey'] = self.fourth_key

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.primary_key is not None:
            result['PrimaryKey'] = self.primary_key

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id

        if self.secondary_key is not None:
            result['SecondaryKey'] = self.secondary_key

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.third_key is not None:
            result['ThirdKey'] = self.third_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FourthKey') is not None:
            self.fourth_key = m.get('FourthKey')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PrimaryKey') is not None:
            self.primary_key = m.get('PrimaryKey')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')

        if m.get('SecondaryKey') is not None:
            self.secondary_key = m.get('SecondaryKey')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('ThirdKey') is not None:
            self.third_key = m.get('ThirdKey')

        return self

