# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_nas20170626 import models as main_models
from darabonba.model import DaraModel

class DescribeDataFlowsRequest(DaraModel):
    def __init__(
        self,
        file_system_id: str = None,
        filters: List[main_models.DescribeDataFlowsRequestFilters] = None,
        max_results: int = None,
        next_token: str = None,
    ):
        # The file system ID.
        # 
        # - CPFS: must start with `cpfs-`, such as cpfs-125487\\*\\*\\*\\*.
        # 
        # - CPFS for Lingjun: must start with `bmcpfs-`, such as bmcpfs-0015\\*\\*\\*\\*.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The filter keys for querying data flows.
        self.filters = filters
        # The number of results for each query.
        # 
        # Valid values: 10 to 100. Default value: 20.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. If the return results are truncated, use NextToken to obtain content starting from the truncation point.
        self.next_token = next_token

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        self.filters = []
        if m.get('Filters') is not None:
            for k1 in m.get('Filters'):
                temp_model = main_models.DescribeDataFlowsRequestFilters()
                self.filters.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        return self

class DescribeDataFlowsRequestFilters(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The name of the filter key. Valid values:
        # 
        # - DataFlowIds: filters by data flow ID.
        # - FsetIds: filters by Fileset ID.
        # - FileSystemPath: filters by the path of the Fileset in the CPFS file system.
        # - SourceStorage: filters by the access path of the source storage.
        # - ThroughputList: filters by the transmission bandwidth of the data flow.
        # - Description: filters by the description of the Fileset.
        # - Status: filters by data flow status.
        self.key = key
        # The value of the filter key. Wildcards are not supported for this parameter.
        # 
        # - If Key is set to DataFlowIds, Value is set to a data flow ID or part of a data flow ID. You can specify one or more data flow IDs. A maximum of 10 data flow IDs can be specified. Example: `df-194433a5be31****` or `df-194433a512a2****,df-234533a5be31****`.
        # 
        # - If Key is set to FsetIds, Value is set to a Fileset ID or part of a Fileset ID. You can specify one or more Fileset IDs. A maximum of 10 Fileset IDs can be specified. Example: `fset-1902718ea0ae****` or `fset-235718ea0ae****,fset-5122718ea0ae****`.
        # - If Key is set to FileSystemPath, Value is set to a path or part of a path in the CPFS file system. The value must be 1 to 1024 characters in length.
        # - If Key is set to SourceStorage, Value is set to the access path of the source storage. The maximum length is 1024 characters.
        # - If Key is set to ThroughputList, Value is set to the transmission bandwidth of the data flow. Combined queries are supported.
        # - If Key is set to Description, Value is set to the description or part of the description of the data flow.
        # - If Key is set to Status, Value is set to the data flow status.
        # - If Key is set to SourceStoragePath, Value is set to the access path of the source storage or part of the access path. The maximum length is 1024 characters.
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

