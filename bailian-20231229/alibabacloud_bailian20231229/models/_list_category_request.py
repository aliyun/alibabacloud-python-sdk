# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListCategoryRequest(DaraModel):
    def __init__(
        self,
        category_name: str = None,
        category_type: str = None,
        connector_id: str = None,
        max_results: int = None,
        next_token: str = None,
        parent_category_id: str = None,
    ):
        # Filters the results to include only the category with this exact name. If this parameter is omitted, no filtering is applied.
        self.category_name = category_name
        # The type of category to query. Valid value:
        # 
        # - `UNSTRUCTURED`: A category for unstructured data.
        # 
        # <props="china">
        # 
        # > This API does not support querying structured data tables.
        # 
        # 
        # 
        # <props="intl">
        # 
        # > This API does not support querying structured data tables.
        # 
        # This parameter is required.
        self.category_type = category_type
        # The ID of the connector.
        self.connector_id = connector_id
        # The maximum number of categories to return per page. The valid range is 1 to 200.
        # 
        # Default value: 20. If this parameter is not specified or is set to a value less than 1, the default value is used. If a value greater than 200 is specified, the maximum value of 200 is used.
        self.max_results = max_results
        # The pagination token. To retrieve the next page of results, pass the `NextToken` value from the previous response.
        self.next_token = next_token
        # The ID of the parent category.
        self.parent_category_id = parent_category_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_name is not None:
            result['CategoryName'] = self.category_name

        if self.category_type is not None:
            result['CategoryType'] = self.category_type

        if self.connector_id is not None:
            result['ConnectorId'] = self.connector_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.parent_category_id is not None:
            result['ParentCategoryId'] = self.parent_category_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')

        if m.get('CategoryType') is not None:
            self.category_type = m.get('CategoryType')

        if m.get('ConnectorId') is not None:
            self.connector_id = m.get('ConnectorId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('ParentCategoryId') is not None:
            self.parent_category_id = m.get('ParentCategoryId')

        return self

