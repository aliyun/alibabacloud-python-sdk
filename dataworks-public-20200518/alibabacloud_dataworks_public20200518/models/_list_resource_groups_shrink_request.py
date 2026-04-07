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
        # 
        # *   default (default): shared resource group
        # *   single: exclusive resource group
        self.biz_ext_key = biz_ext_key
        # The keyword that is used for fuzzy match by resource group name and identifier.
        self.keyword = keyword
        # The type of the resource group that you want to query. Valid values:
        # 
        # *   0: DataWorks
        # *   1: scheduling
        # *   2: MaxCompute
        # *   3: Platform for AI (PAI)
        # *   4: Data Integration
        # *   7: exclusive resource group for scheduling (An ID is generated for the purchased resource when you purchase an exclusive resource group for scheduling.)
        # *   9: DataService Studio
        # *   Default value: 1
        # 
        # If the value indicates a compute engine, the resource groups to query are the ones that were created when you purchased the compute engine.
        self.resource_group_type = resource_group_type
        # The resource group ID.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id
        # The tags.
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

