# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAgenticTableBaseInfoRequest(DaraModel):
    def __init__(
        self,
        database_uuid: str = None,
        max_results: int = None,
        next_token: str = None,
        search_key: str = None,
        sort_field_name: str = None,
        sort_order: str = None,
        table_type: str = None,
    ):
        # The UUID of the database to which the table belongs. You can obtain the UUID by calling the ListAgenticDatabase or SearchAgenticDatabase operation.
        # 
        # This parameter is required.
        self.database_uuid = database_uuid
        # The maximum number of entries to return per page.
        self.max_results = max_results
        # The token for the next query. You do not need to specify this parameter for the first query. When you query the next page, set this parameter to the NextToken value returned in the previous response.
        self.next_token = next_token
        # The search keyword. The system matches the keyword against table names. The results are sorted by exact match, prefix match, and contains match. Within the same match level, the results are sorted by the field specified by SortFieldName.
        self.search_key = search_key
        # The field by which to sort the results. This parameter is case-sensitive. Valid values:
        # 
        # - **name**: Sorts the results by table name. This value is recommended.
        # - **numRows**: Sorts the results by the number of rows.
        # - **storeCapacity**: Sorts the results by the storage capacity.
        # 
        # If you specify other values, the request fails. If you do not specify this parameter, the results are returned in the default order, and the SortOrder parameter does not take effect.
        self.sort_field_name = sort_field_name
        # The sort order. This parameter takes effect only when SortFieldName is specified. This parameter is not case-sensitive. Valid values:
        # 
        # - **ASC**: Sorts the results in ascending order. This is the default value and is recommended.
        # - **DESC**: Sorts the results in descending order.
        # 
        # If you specify other values, the request fails.
        self.sort_order = sort_order
        # The table type. The results are strictly filtered by this type. Valid values:
        # 
        # - **NORMAL**: Regular table.
        # - **VIEW**: View.
        # - **FOREIGN**: Foreign table.
        # - **SYNONYM**: Synonym. This value is supported only for Oracle data sources.
        self.table_type = table_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.database_uuid is not None:
            result['DatabaseUuid'] = self.database_uuid

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.search_key is not None:
            result['SearchKey'] = self.search_key

        if self.sort_field_name is not None:
            result['SortFieldName'] = self.sort_field_name

        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order

        if self.table_type is not None:
            result['TableType'] = self.table_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseUuid') is not None:
            self.database_uuid = m.get('DatabaseUuid')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')

        if m.get('SortFieldName') is not None:
            self.sort_field_name = m.get('SortFieldName')

        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')

        if m.get('TableType') is not None:
            self.table_type = m.get('TableType')

        return self

