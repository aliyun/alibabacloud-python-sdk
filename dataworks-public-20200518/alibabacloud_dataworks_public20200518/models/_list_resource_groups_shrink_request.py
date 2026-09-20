# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListResourceGroupsShrinkRequest(DaraModel):
    def __init__(
        self,
        biz_ext_key: str = None,
        keyword: str = None,
        resource_group_type: int = None,
        resource_manager_resource_group_id: str = None,
        tags_shrink: str = None,
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
        self.tags_shrink = tags_shrink

    def validate(self):
        pass

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

        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink

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

        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')

        return self

