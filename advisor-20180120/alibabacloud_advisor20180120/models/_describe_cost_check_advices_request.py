# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_advisor20180120 import models as main_models
from darabonba.model import DaraModel

class DescribeCostCheckAdvicesRequest(DaraModel):
    def __init__(
        self,
        assume_aliyun_id_list: List[int] = None,
        check_id: str = None,
        check_plan_id: int = None,
        language: str = None,
        page_number: int = None,
        page_size: int = None,
        region_ids: List[str] = None,
        resource_group_id_list: List[str] = None,
        resource_id: str = None,
        resource_ids: List[str] = None,
        resource_name: str = None,
        severity: str = None,
        tag_keys: List[str] = None,
        tag_list: List[main_models.DescribeCostCheckAdvicesRequestTagList] = None,
        tag_values: List[str] = None,
    ):
        self.assume_aliyun_id_list = assume_aliyun_id_list
        self.check_id = check_id
        self.check_plan_id = check_plan_id
        self.language = language
        self.page_number = page_number
        self.page_size = page_size
        self.region_ids = region_ids
        self.resource_group_id_list = resource_group_id_list
        self.resource_id = resource_id
        self.resource_ids = resource_ids
        self.resource_name = resource_name
        self.severity = severity
        self.tag_keys = tag_keys
        self.tag_list = tag_list
        self.tag_values = tag_values

    def validate(self):
        if self.tag_list:
            for v1 in self.tag_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.assume_aliyun_id_list is not None:
            result['AssumeAliyunIdList'] = self.assume_aliyun_id_list

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

        if self.region_ids is not None:
            result['RegionIds'] = self.region_ids

        if self.resource_group_id_list is not None:
            result['ResourceGroupIdList'] = self.resource_group_id_list

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids

        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name

        if self.severity is not None:
            result['Severity'] = self.severity

        if self.tag_keys is not None:
            result['TagKeys'] = self.tag_keys

        result['TagList'] = []
        if self.tag_list is not None:
            for k1 in self.tag_list:
                result['TagList'].append(k1.to_map() if k1 else None)

        if self.tag_values is not None:
            result['TagValues'] = self.tag_values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssumeAliyunIdList') is not None:
            self.assume_aliyun_id_list = m.get('AssumeAliyunIdList')

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
            self.region_ids = m.get('RegionIds')

        if m.get('ResourceGroupIdList') is not None:
            self.resource_group_id_list = m.get('ResourceGroupIdList')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')

        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')

        if m.get('Severity') is not None:
            self.severity = m.get('Severity')

        if m.get('TagKeys') is not None:
            self.tag_keys = m.get('TagKeys')

        self.tag_list = []
        if m.get('TagList') is not None:
            for k1 in m.get('TagList'):
                temp_model = main_models.DescribeCostCheckAdvicesRequestTagList()
                self.tag_list.append(temp_model.from_map(k1))

        if m.get('TagValues') is not None:
            self.tag_values = m.get('TagValues')

        return self

class DescribeCostCheckAdvicesRequestTagList(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: List[str] = None,
    ):
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        return self

