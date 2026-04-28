# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCostCheckResultsShrinkRequest(DaraModel):
    def __init__(
        self,
        assume_aliyun_id_list_shrink: str = None,
        check_ids_shrink: str = None,
        check_plan_id: int = None,
        group_by: str = None,
        language: str = None,
        product: str = None,
        region_ids_shrink: str = None,
        resource_group_id_list_shrink: str = None,
        resource_id: str = None,
        resource_ids_shrink: str = None,
        resource_name: str = None,
        severity: int = None,
        tag_keys_shrink: str = None,
        tag_list_shrink: str = None,
        tag_values_shrink: str = None,
    ):
        self.assume_aliyun_id_list_shrink = assume_aliyun_id_list_shrink
        self.check_ids_shrink = check_ids_shrink
        self.check_plan_id = check_plan_id
        self.group_by = group_by
        self.language = language
        self.product = product
        self.region_ids_shrink = region_ids_shrink
        self.resource_group_id_list_shrink = resource_group_id_list_shrink
        self.resource_id = resource_id
        self.resource_ids_shrink = resource_ids_shrink
        self.resource_name = resource_name
        self.severity = severity
        self.tag_keys_shrink = tag_keys_shrink
        self.tag_list_shrink = tag_list_shrink
        self.tag_values_shrink = tag_values_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.assume_aliyun_id_list_shrink is not None:
            result['AssumeAliyunIdList'] = self.assume_aliyun_id_list_shrink

        if self.check_ids_shrink is not None:
            result['CheckIds'] = self.check_ids_shrink

        if self.check_plan_id is not None:
            result['CheckPlanId'] = self.check_plan_id

        if self.group_by is not None:
            result['GroupBy'] = self.group_by

        if self.language is not None:
            result['Language'] = self.language

        if self.product is not None:
            result['Product'] = self.product

        if self.region_ids_shrink is not None:
            result['RegionIds'] = self.region_ids_shrink

        if self.resource_group_id_list_shrink is not None:
            result['ResourceGroupIdList'] = self.resource_group_id_list_shrink

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_ids_shrink is not None:
            result['ResourceIds'] = self.resource_ids_shrink

        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name

        if self.severity is not None:
            result['Severity'] = self.severity

        if self.tag_keys_shrink is not None:
            result['TagKeys'] = self.tag_keys_shrink

        if self.tag_list_shrink is not None:
            result['TagList'] = self.tag_list_shrink

        if self.tag_values_shrink is not None:
            result['TagValues'] = self.tag_values_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssumeAliyunIdList') is not None:
            self.assume_aliyun_id_list_shrink = m.get('AssumeAliyunIdList')

        if m.get('CheckIds') is not None:
            self.check_ids_shrink = m.get('CheckIds')

        if m.get('CheckPlanId') is not None:
            self.check_plan_id = m.get('CheckPlanId')

        if m.get('GroupBy') is not None:
            self.group_by = m.get('GroupBy')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('Product') is not None:
            self.product = m.get('Product')

        if m.get('RegionIds') is not None:
            self.region_ids_shrink = m.get('RegionIds')

        if m.get('ResourceGroupIdList') is not None:
            self.resource_group_id_list_shrink = m.get('ResourceGroupIdList')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceIds') is not None:
            self.resource_ids_shrink = m.get('ResourceIds')

        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')

        if m.get('Severity') is not None:
            self.severity = m.get('Severity')

        if m.get('TagKeys') is not None:
            self.tag_keys_shrink = m.get('TagKeys')

        if m.get('TagList') is not None:
            self.tag_list_shrink = m.get('TagList')

        if m.get('TagValues') is not None:
            self.tag_values_shrink = m.get('TagValues')

        return self

