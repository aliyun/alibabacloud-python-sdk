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
        # The ID of the file system.
        # 
        # *   The IDs of CPFS file systems must start with `cpfs-`. Example: cpfs-099394bd928c\\*\\*\\*\\*.
        # *   The IDs of CPFS for LINGJUN file systems must start with `bmcpfs-`. Example: bmcpfs-290w65p03ok64ya\\*\\*\\*\\*.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The filter that is used to query filesets.
        self.filters = filters
        # The number of results for each query.
        # 
        # Valid values: 10 to 100. Default value: 20.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token
        # The condition by which the results are sorted. Valid values:
        # 
        # *   FileCountLimit: the file quantity quota
        # *   SizeLimit: the capacity quota
        # *   FileCountUsage: the usage of the file quantity quota
        # *   SpaceUsage: the capacity usage
        self.order_by_field = order_by_field
        # The order in which you want to sort the results. Valid values:
        # 
        # *   asc (default): ascending order
        # *   desc: descending order
        # 
        # >  This parameter takes effect only if you specify the OrderByField parameter.
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
        # The filter name. Valid values:
        # 
        # *   FsetIds: filters filesets by fileset ID.
        # *   FileSystemPath: filters filesets based on the path of a fileset in a CPFS file system.
        # *   Description: filters filesets based on the fileset description.
        # *   QuotaExists: filters filesets based on whether quotas exist.
        # 
        # >  Only CPFS for LINGJUN V2.7.0 and later support the QuotaExists parameter.
        self.key = key
        # The filter value. This parameter does not support wildcards.
        # 
        # *   If Key is set to FsetIds, set Value to a fileset ID or a part of the fileset ID. You can specify a fileset ID or a group of fileset IDs. You can specify a maximum of 10 fileset IDs. Example: `fset-1902718ea0ae****` or `fset-1902718ea0ae****,fset-3212718ea0ae****`.
        # *   If Key is set to FileSystemPath, set Value to the path or a part of the path of a fileset in a CPFS file system. The value must be 2 to 1024 characters in length. The value must be encoded in UTF-8.
        # *   If Key is set to Description, set Value to a fileset description or a part of the fileset description.
        # *   If Key is set to QuotaExists, set Value to true or false. If you do not specify the parameter, all filesets are returned.
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

