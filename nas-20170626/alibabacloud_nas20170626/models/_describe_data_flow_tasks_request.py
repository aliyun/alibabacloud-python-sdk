# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_nas20170626 import models as main_models
from darabonba.model import DaraModel

class DescribeDataFlowTasksRequest(DaraModel):
    def __init__(
        self,
        file_system_id: str = None,
        filters: List[main_models.DescribeDataFlowTasksRequestFilters] = None,
        max_results: int = None,
        next_token: str = None,
        with_reports: bool = None,
    ):
        # The file system ID.
        # 
        # - General-purpose CPFS: must start with `cpfs-`, such as cpfs-099394bd928c****.
        # 
        # - CPFS for Lingjun: must start with `bmcpfs-`, such as bmcpfs-290w65p03ok64ya****.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The filter conditions.
        self.filters = filters
        # The number of results for each query.
        # 
        # Valid values: 10 to 100.
        # 
        # Default value: 20.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. If the return results are truncated, you can use NextToken to initiate a new request to retrieve the content after the truncation point.
        self.next_token = next_token
        # Specifies whether to query report information.
        # 
        # - True (default): queries reports.
        # - False: does not query reports.
        # 
        # >- Setting this parameter to False can speed up queries.
        # > - Only CPFS for Lingjun is supported.
        self.with_reports = with_reports

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

        if self.with_reports is not None:
            result['WithReports'] = self.with_reports

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        self.filters = []
        if m.get('Filters') is not None:
            for k1 in m.get('Filters'):
                temp_model = main_models.DescribeDataFlowTasksRequestFilters()
                self.filters.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('WithReports') is not None:
            self.with_reports = m.get('WithReports')

        return self

class DescribeDataFlowTasksRequestFilters(DaraModel):
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
        # - TaskIds: filters by data flow task ID.
        # - Originator: filters by the initiator of the data flow task.
        # - TaskActions: filters by the type of the data flow task.
        # - DataTypes: filters by the data type of the data flow task.
        # - Status: filters by data flow status.
        # - CreateTimeBegin: filters data flow tasks created after the specified time.
        # - CreateTimeEnd: filters data flow tasks created before the specified time.
        # - StartTimeBegin: filters data flow tasks started after the specified time.
        # - StartTimeEnd: filters data flow tasks started before the specified time.
        # - EndTimeBegin: filters data flow tasks ended after the specified time.
        # - EndTimeEnd: filters data flow tasks ended before the specified time.
        self.key = key
        # The value of the filter key. Wildcards are not supported.
        # 
        # - If Key is set to DataFlowIds, Value is set to a data flow ID or part of a data flow ID. You can specify one or more data flow IDs. A maximum of 10 data flow IDs can be specified. Example: `df-194433a5be31****` or `df-194433a512a2****,df-234533a5be31****`.
        # - If Key is set to TaskId, Value is set to a data flow task ID or part of a data flow task ID. You can specify one or more data flow task IDs. A maximum of 10 data flow task IDs can be specified. Example: `task-38aa8e890f45****` or `task-38aa8e890f45****,task-29ae8e890f45****`.
        # - If Key is set to TaskActions, Value is set to the type of the data flow task, including **Import**, **Export**, **Evict**, **Inventory**, **StreamImport**, and **StreamExport**. Combined queries are supported. CPFS for Lingjun supports only Import, Export, StreamImport, and StreamExport. StreamImport and StreamExport are supported only by CPFS for Lingjun 2.6.0 and later.
        # - If Key is set to DataTypes, Value is set to the data type of the data flow task, including MetaAndData, Metadata, and Data. Combined queries are supported.
        # - If Key is set to Originator, Value is set to the initiator of the data flow task, including User and System.
        # - If Key is set to Status, Value is set to the status of the data flow task, including Pending, Executing, Failed, Completed, Canceling, and Canceled. Combined queries are supported.
        # - If Key is set to CreateTimeBegin, Value is set to the earliest creation time of data flow tasks. Format: `yyyy-MM-ddThh:mmZ`.
        # - If Key is set to CreateTimeEnd, Value is set to the latest creation time of data flow tasks. Format: `yyyy-MM-ddThh:mmZ`.
        # - If Key is set to StartTimeBegin, Value is set to the earliest start time of data flow tasks. Format: `yyyy-MM-ddThh:mmZ`.
        # - If Key is set to StartTimeEnd, Value is set to the latest start time of data flow tasks. Format: `yyyy-MM-ddThh:mmZ`.
        # - If Key is set to EndTimeBegin, Value is set to the earliest end time of data flow tasks. Format: `yyyy-MM-ddThh:mmZ`.
        # - If Key is set to EndTimeEnd, Value is set to the latest end time of data flow tasks. Format: `yyyy-MM-ddThh:mmZ`.
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

