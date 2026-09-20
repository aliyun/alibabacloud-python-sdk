# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class ListResourceGroupsRequest(DaraModel):
    def __init__(
        self,
        biz_ext_key: str = None,
        keyword: str = None,
        resource_group_type: int = None,
        resource_manager_resource_group_id: str = None,
        tags: List[main_models.ListResourceGroupsRequestTags] = None,
    ):
        # The category of the resource group. Valid values:
        # - default: public resource group.
        # - single: dedicated resource group.
        self.biz_ext_key = biz_ext_key
        # The keyword. Used for fuzzy matching of resource group names and resource group identifiers.
        self.keyword = keyword
        # The type ID of the resource group to query. Valid values:
        # - 0: DataWorks
        # - 1: scheduling
        # - 2: MaxCompute
        # - 3: PAI
        # - 4: data integration
        # - 7: the purchase resource ID generated when you purchase a dedicated schedule resource group
        # - 9: dataService
        # - Default value: 1 (scheduling).
        # 
        # When the value represents an engine, the returned resource group list contains the resource groups created when you purchased that type of engine.
        self.resource_group_type = resource_group_type
        # The resource group ID.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id
        # The list of tags.
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
        if self.biz_ext_key is not None:
            result['BizExtKey'] = self.biz_ext_key

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.resource_group_type is not None:
            result['ResourceGroupType'] = self.resource_group_type

        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizExtKey') is not None:
            self.biz_ext_key = m.get('BizExtKey')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('ResourceGroupType') is not None:
            self.resource_group_type = m.get('ResourceGroupType')

        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListResourceGroupsRequestTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class ListResourceGroupsRequestTags(DaraModel):
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

