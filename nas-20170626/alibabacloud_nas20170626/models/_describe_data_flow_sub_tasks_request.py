# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_nas20170626 import models as main_models
from darabonba.model import DaraModel

class DescribeDataFlowSubTasksRequest(DaraModel):
    def __init__(
        self,
        file_system_id: str = None,
        filters: List[main_models.DescribeDataFlowSubTasksRequestFilters] = None,
        max_results: int = None,
        next_token: str = None,
    ):
        # The ID of the file system. Only CPFS for Lingjun file systems are supported. The ID must start with `bmcpfs-`.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The filter keys used to query streaming tasks of a data flow.
        self.filters = filters
        # The maximum number of entries to return for a single request.
        # 
        # Valid values: 20 to 100.
        # 
        # Default value: 20.
        self.max_results = max_results
        # The token that is used to retrieve the next page of results when the returned results are truncated. You can use NextToken to initiate another request to retrieve the results after the current truncation point.
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
                temp_model = main_models.DescribeDataFlowSubTasksRequestFilters()
                self.filters.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        return self

class DescribeDataFlowSubTasksRequestFilters(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The name of the filter key.
        # 
        # Valid values:
        # 
        # - DataFlowIds: filters by data flow ID.
        # - DataFlowTaskIds: filters by data flow task ID.
        # - DataFlowSubTaskIds: filters by data flow streaming task ID.
        # - Status: filters by data flow status.
        # - SrcFilePath: filters by source file path.
        # - DstFilePath: filters by destination file path.
        self.key = key
        # The value of the filter key. This parameter does not support wildcards.
        # 
        # - If Key is set to DataFlowIds, Value is set to a data flow ID or a part of a data flow ID. You can specify one or more data flow IDs. A maximum of 10 data flow IDs can be specified. Example: `df-194433a5be31****` or `df-194433a512a2****,df-234533a5be31****`.
        # - If Key is set to DataFlowTaskIds, Value is set to a data flow task ID or a part of a data flow task ID. You can specify one or more data flow task IDs. A maximum of 10 data flow task IDs can be specified. Example: `task-29ee8e890f45****` or `task-29ee8e890f45****,task-38ae8e890f45****`.
        # - If Key is set to DataFlowSubTaskIds, Value is set to a data flow streaming task ID or a part of a data flow streaming task ID. You can specify one or more data flow streaming task IDs. A maximum of 10 data flow streaming task IDs can be specified. Example: `subTaskId-370kyfmyknxcyzw****` or `subTaskId-247kyfmyknxcyzw****,subTaskId-256kyfmyknxcyzw****`.
        # - If Key is set to Status, Value is set to the status of the data flow task. Valid values: EXPIRED, CREATED, RUNNING, COMPLETE, CANCELING, FAILED, and CANCELED. Combined queries are supported.
        # - If Key is set to SrcFilePath, Value is set to the source file path. The path can be up to 1,023 characters in length.
        # - If Key is set to DstFilePath, Value is set to the destination file path. The path can be up to 1,023 characters in length.
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

