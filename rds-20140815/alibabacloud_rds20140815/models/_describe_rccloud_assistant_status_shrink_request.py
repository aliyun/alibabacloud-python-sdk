# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeRCCloudAssistantStatusShrinkRequest(DaraModel):
    def __init__(
        self,
        instance_ids_shrink: str = None,
        max_results: int = None,
        next_token: str = None,
        ostype: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
    ):
        # The list of instance IDs.
        self.instance_ids_shrink = instance_ids_shrink
        # The maximum number of entries per page. If you specify `InstanceId`, this parameter does not take effect.
        # 
        # Maximum value: 50.
        # 
        # Default value: 10.
        self.max_results = max_results
        # The token that marks the end of the current returned page. If this parameter is empty, the data is queried from the first entry.
        self.next_token = next_token
        # The operating system type of the instance. Only **Linux** is supported.
        # 
        # Valid values:
        # 
        # *   Windows
        # *   Linux
        # *   FreeBSD
        self.ostype = ostype
        # >  This parameter will be removed in the future. We recommend that you use `NextToken` and `MaxResults` for a paged query.
        self.page_number = page_number
        # >  This parameter will be removed in the future. We recommend that you use `NextToken` and `MaxResults` for a paged query.
        self.page_size = page_size
        # The ID of the region where the instance resides.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_ids_shrink is not None:
            result['InstanceIds'] = self.instance_ids_shrink

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.ostype is not None:
            result['OSType'] = self.ostype

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids_shrink = m.get('InstanceIds')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OSType') is not None:
            self.ostype = m.get('OSType')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

