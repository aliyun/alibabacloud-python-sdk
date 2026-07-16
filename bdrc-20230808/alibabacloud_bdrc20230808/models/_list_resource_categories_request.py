# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListResourceCategoriesRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        resource_category_id: str = None,
    ):
        # The maximum number of records to return in this request.
        self.max_results = max_results
        # The pagination token. If more entries are to be returned on the next page, a pagination token is returned. Note: If this parameter returns data, it indicates there is a next page. You can use the returned NextToken as a request parameter to obtain the next page of data until it returns Null, indicating all data has been retrieved.
        self.next_token = next_token
        self.resource_category_id = resource_category_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.resource_category_id is not None:
            result['ResourceCategoryId'] = self.resource_category_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('ResourceCategoryId') is not None:
            self.resource_category_id = m.get('ResourceCategoryId')

        return self

