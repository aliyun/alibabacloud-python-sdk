# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ListCheckRuleInstanceRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        instance_list: List[main_models.ListCheckRuleInstanceRequestInstanceList] = None,
        page_size: int = None,
        rule_id: int = None,
    ):
        # The page number of the current page when performing a paginated query.
        self.current_page = current_page
        # Instance list.
        self.instance_list = instance_list
        # The maximum number of items per page in a paginated query. The default value is **20**.
        self.page_size = page_size
        # Rule ID.
        # > You can call the [LisCheckRule](https://help.aliyun.com/document_detail/2590599.html) interface to get this parameter.
        # 
        # This parameter is required.
        self.rule_id = rule_id

    def validate(self):
        if self.instance_list:
            for v1 in self.instance_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        result['InstanceList'] = []
        if self.instance_list is not None:
            for k1 in self.instance_list:
                result['InstanceList'].append(k1.to_map() if k1 else None)

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        self.instance_list = []
        if m.get('InstanceList') is not None:
            for k1 in m.get('InstanceList'):
                temp_model = main_models.ListCheckRuleInstanceRequestInstanceList()
                self.instance_list.append(temp_model.from_map(k1))

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        return self

class ListCheckRuleInstanceRequestInstanceList(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
    ):
        # Asset instance ID.
        # > Call the [ListCheckInstanceResult](~~ListCheckInstanceResult~~) interface to get this parameter.
        self.instance_id = instance_id
        # The region where the asset is located.
        # > Call the [ListCheckInstanceResult](~~ListCheckInstanceResult~~) interface to get this parameter.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

