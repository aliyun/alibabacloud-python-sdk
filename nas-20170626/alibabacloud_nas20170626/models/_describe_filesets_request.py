# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_nas20170626 import models as main_models
from darabonba.model import DaraModel

class DescribeFilesetsRequest(DaraModel):
    def __init__(
        self,
        file_system_id: str = None,
        filters: List[main_models.DescribeFilesetsRequestFilters] = None,
        max_results: int = None,
        next_token: str = None,
        order_by_field: str = None,
        sort_order: str = None,
    ):
        # The file system ID.
        # 
        # - CPFS: The ID must start with `cpfs-`, such as cpfs-099394bd928c****.
        # 
        # - CPFS for Lingjun: The ID must start with `bmcpfs-`, such as bmcpfs-290w65p03ok64ya****.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The filter key information for the filesets to query.
        self.filters = filters
        # The number of results per query.
        # 
        # Valid values: 10 to 100. Default value: 20.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. If the response is truncated, you can use this token in the next request to retrieve the remaining results.
        self.next_token = next_token
        # The field by which to sort the results.
        # 
        # - FileCountLimit: the quota file count limit.
        # - SizeLimit: the quota capacity limit.
        # - FileCountUsage: the file count usage.
        # - SpaceUsage: the capacity usage.
        self.order_by_field = order_by_field
        # The sort order. Valid values:
        # 
        # - asc (default): ascending order, which sorts results from smallest to largest.
        # - desc: descending order, which sorts results from largest to smallest.
        # > This parameter takes effect only when the OrderByField parameter is specified.
        self.sort_order = sort_order

    def validate(self):
        if self.filters:
            for v1 in self.filters:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        result['Filters'] = []
        if self.filters is not None:
            for k1 in self.filters:
                result['Filters'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.order_by_field is not None:
            result['OrderByField'] = self.order_by_field

        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        self.filters = []
        if m.get('Filters') is not None:
            for k1 in m.get('Filters'):
                temp_model = main_models.DescribeFilesetsRequestFilters()
                self.filters.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OrderByField') is not None:
            self.order_by_field = m.get('OrderByField')

        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')

        return self

class DescribeFilesetsRequestFilters(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The name of the filter key. Valid values:
        # 
        # - FsetIds: filters by fileset ID.
        # - FileSystemPath: filters by the path of the fileset in the CPFS file system.
        # - Description: filters by the description of the fileset.
        # - QuotaExists: filters by whether a quota exists.
        # > Only CPFS for Lingjun 2.7.0 and later support filtering by the QuotaExists parameter.
        self.key = key
        # The value of the filter key. Wildcards are not supported for this parameter.
        # 
        # - If Key is set to FsetIds, Value is set to a fileset ID. You can specify one or more fileset IDs, up to 10. Separate multiple values with commas (,). Example: `fset-1902718ea0ae****` or `fset-1902718ea0ae****,fset-3212718ea0ae****`.
        # - If Key is set to FileSystemPath, Value is set to the full path or a partial path of the fileset in the CPFS file system. The value must be 2 to 1,024 characters in length and encoded in UTF-8.
        # - If Key is set to Description, Value is set to the full description or a partial description of the fileset.
        # - If Key is set to QuotaExists, Value is set to true or false. If you leave this parameter empty, all filesets are returned.
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

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

