# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListFileRequest(DaraModel):
    def __init__(
        self,
        category_id: str = None,
        file_name: str = None,
        max_results: int = None,
        next_token: str = None,
    ):
        # The category ID, which is the `CategoryId` returned by the [AddCategory](~~AddCategory~~) operation. To view the category ID, click the ID icon next to the category name on the Unstructured Data tab of the [Data Management](https://bailian.console.alibabacloud.com/#/data-center) page.
        # 
        # This parameter is required.
        self.category_id = category_id
        self.file_name = file_name
        self.max_results = max_results
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

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        return self

