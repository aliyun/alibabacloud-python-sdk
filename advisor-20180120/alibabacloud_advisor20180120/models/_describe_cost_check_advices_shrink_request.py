# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCostCheckAdvicesShrinkRequest(DaraModel):
    def __init__(
        self,
        assume_aliyun_id_list_shrink: str = None,
        check_id: str = None,
        check_plan_id: int = None,
        language: str = None,
        page_number: int = None,
        page_size: int = None,
        region_ids_shrink: str = None,
        resource_group_id_list_shrink: str = None,
        resource_id: str = None,
        resource_ids_shrink: str = None,
        resource_name: str = None,
        severity: str = None,
        tag_keys_shrink: str = None,
        tag_list_shrink: str = None,
        tag_values_shrink: str = None,
    ):
        self.assume_aliyun_id_list_shrink = assume_aliyun_id_list_shrink
        self.check_id = check_id
        self.check_plan_id = check_plan_id
        self.language = language
        self.page_number = page_number
        self.page_size = page_size
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

        if self.check_id is not None:
            result['CheckId'] = self.check_id

        if self.check_plan_id is not None:
            result['CheckPlanId'] = self.check_plan_id

        if self.language is not None:
            result['Language'] = self.language

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

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

        if m.get('CheckId') is not None:
            self.check_id = m.get('CheckId')

        if m.get('CheckPlanId') is not None:
            self.check_plan_id = m.get('CheckPlanId')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

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

