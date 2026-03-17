# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListEnterpriseCodeRequest(DaraModel):
    def __init__(
        self,
        enterprise_code: str = None,
        is_default: bool = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
    ):
        # The enterprise code that you want to query.
        self.enterprise_code = enterprise_code
        # Specifies whether to query only default enterprise codes. Valid values:
        # 
        # *   **true**: yes
        # *   **false** (default): no
        self.is_default = is_default
        # The number of entries returned per page.
        # 
        # Valid values: **1** to **100**. Default value: **10**.
        self.max_results = max_results
        # The token for returning the next page when the data is returned in more than one page.
        self.next_token = next_token
        # The ID of the region.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the most recent region list.
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
        if self.enterprise_code is not None:
            result['EnterpriseCode'] = self.enterprise_code

        if self.is_default is not None:
            result['IsDefault'] = self.is_default

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnterpriseCode') is not None:
            self.enterprise_code = m.get('EnterpriseCode')

        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

