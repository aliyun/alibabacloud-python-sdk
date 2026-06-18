# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListFileShrinkRequest(DaraModel):
    def __init__(
        self,
        category_id: str = None,
        file_ids_shrink: str = None,
        file_name: str = None,
        max_results: int = None,
        next_token: str = None,
    ):
        # <props="china">
        # 
        # The category ID, which is the `CategoryId` returned by the **AddCategory** operation. You can also obtain it on the [Application Data](https://bailian.console.aliyun.com/?tab=app#/data-center) - Files tab by clicking the ID icon next to the category name.
        # 
        # 
        # 
        # <props="intl">
        # 
        # The category ID, which is the `CategoryId` returned by the **AddCategory** operation. You can also obtain it on the [Application Data](https://modelstudio.console.alibabacloud.com/?tab=app#/data-center) - Files tab by clicking the ID icon next to the category name.
        # 
        # .
        # 
        # This parameter is required.
        self.category_id = category_id
        # The list of file IDs to query. A maximum of 20 files can be queried per request.
        self.file_ids_shrink = file_ids_shrink
        # The file name (without extension). Only exact match is supported. Fuzzy search is not supported.
        self.file_name = file_name
        # The number of entries per page for paging. Valid values: 1 to 200.
        # 
        # Default value:
        # If the value is not set or is less than 1, the default value is 20. If the value is greater than 200, the default value is 200.
        self.max_results = max_results
        # The pagination token. Set this to the NextToken value returned by the previous API call.
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_id is not None:
            result['CategoryId'] = self.category_id

        if self.file_ids_shrink is not None:
            result['FileIds'] = self.file_ids_shrink

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')

        if m.get('FileIds') is not None:
            self.file_ids_shrink = m.get('FileIds')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        return self

