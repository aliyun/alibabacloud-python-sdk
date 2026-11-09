# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeInstanceAutoRenewalAttributeRequest(DaraModel):
    def __init__(
        self,
        auto_renewal: bool = None,
        instance_id_list: List[str] = None,
        max_results: int = None,
        next_token: str = None,
        page_no: int = None,
        page_size: int = None,
        resource_type: str = None,
        resource_type_list: List[str] = None,
        search_region_id: str = None,
    ):
        # The auto-renewal status. Valid values:
        # - true: Auto-renewal is enabled.
        # - false: Auto-renewal is disabled.
        self.auto_renewal = auto_renewal
        # The list of instance IDs for which to query the auto-renewal status.
        self.instance_id_list = instance_id_list
        # The maximum number of entries to return per query.
        self.max_results = max_results
        # The mark for paging. Leave this parameter empty for the first query. For subsequent paging, pass the NextToken value returned in the previous response as is. Do not construct or decode the value.
        self.next_token = next_token
        # The page number. Default value: 1.
        self.page_no = page_no
        # The maximum number of entries per page. Maximum value: 500. Default value: 20.
        self.page_size = page_size
        # The resource type. Example: CorePackage indicates a core-hour package.
        self.resource_type = resource_type
        # The list of resource types.
        self.resource_type_list = resource_type_list
        # The region ID used to filter instances.
        self.search_region_id = search_region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_renewal is not None:
            result['AutoRenewal'] = self.auto_renewal

        if self.instance_id_list is not None:
            result['InstanceIdList'] = self.instance_id_list

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.resource_type_list is not None:
            result['ResourceTypeList'] = self.resource_type_list

        if self.search_region_id is not None:
            result['SearchRegionId'] = self.search_region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRenewal') is not None:
            self.auto_renewal = m.get('AutoRenewal')

        if m.get('InstanceIdList') is not None:
            self.instance_id_list = m.get('InstanceIdList')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('ResourceTypeList') is not None:
            self.resource_type_list = m.get('ResourceTypeList')

        if m.get('SearchRegionId') is not None:
            self.search_region_id = m.get('SearchRegionId')

        return self

