# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_resourcecenter20221201 import models as main_models
from darabonba.model import DaraModel

class GetMultiAccountResourceCountsRequest(DaraModel):
    def __init__(
        self,
        filter: List[main_models.GetMultiAccountResourceCountsRequestFilter] = None,
        group_by_key: str = None,
        scope: str = None,
    ):
        # The filter condition.
        self.filter = filter
        # The dimension by which resources are queried. Valid values:
        # 
        # - ResourceType: resource type
        # 
        # - RegionId: region
        # 
        # - ResourceGroupId: resource group
        # 
        # > If this parameter is not configured, the total number of resources that meet the conditions is returned.
        self.group_by_key = group_by_key
        # The search scope. Valid values:
        # 
        # - ID of a resource directory: Resources within the management account and all members of the resource directory are searched.
        # 
        # - ID of the Root folder: Resources within all members in the Root folder and the subfolders of the Root folder are searched.
        # 
        # - ID of a folder: Resources within all members in the folder are searched.
        # 
        # - ID of a member: Resources within the member are searched.
        # 
        # For information about how to obtain the ID of a resource directory, the Root folder, a folder, or a member, see [GetResourceDirectory](https://help.aliyun.com/document_detail/159995.html), [ListFoldersForParent](https://help.aliyun.com/document_detail/159997.html), or [ListAccounts](https://help.aliyun.com/document_detail/160016.html).
        self.scope = scope

    def validate(self):
        if self.filter:
            for v1 in self.filter:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Filter'] = []
        if self.filter is not None:
            for k1 in self.filter:
                result['Filter'].append(k1.to_map() if k1 else None)

        if self.group_by_key is not None:
            result['GroupByKey'] = self.group_by_key

        if self.scope is not None:
            result['Scope'] = self.scope

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.filter = []
        if m.get('Filter') is not None:
            for k1 in m.get('Filter'):
                temp_model = main_models.GetMultiAccountResourceCountsRequestFilter()
                self.filter.append(temp_model.from_map(k1))

        if m.get('GroupByKey') is not None:
            self.group_by_key = m.get('GroupByKey')

        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        return self

class GetMultiAccountResourceCountsRequestFilter(DaraModel):
    def __init__(
        self,
        key: str = None,
        match_type: str = None,
        value: List[str] = None,
    ):
        # The key of the filter condition. For more information, see `Supported filter parameters`.
        self.key = key
        # The matching method.
        # 
        # Set the value to Equals, which indicates an exact match.
        self.match_type = match_type
        # The values of the filter condition.
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

        if self.match_type is not None:
            result['MatchType'] = self.match_type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('MatchType') is not None:
            self.match_type = m.get('MatchType')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

