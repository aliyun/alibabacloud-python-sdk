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
        # The ID of the file system.
        # 
        # *   The IDs of CPFS file systems must start with `cpfs-`. Example: cpfs-099394bd928c\\*\\*\\*\\*.
        # *   The IDs of CPFS for Lingjun file systems must start with `bmcpfs-`. Example: bmcpfs-290w65p03ok64ya\\*\\*\\*\\*. .
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The details about filters.
        self.filters = filters
        # The number of results for each query.
        # 
        # Valid values: 10 to 100.
        # 
        # Default value: 20.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token
        # Whether to query report information.
        # 
        # *   True (default)
        # *   False
        # 
        # > 
        # 
        # *   Set it to False to speed up the query.
        # 
        # *   Only CPFS for Lingjun supports this parameter.
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
        # The filter name.
        # 
        # Valid value:
        # 
        # *   DataFlowIds: filters dataflow tasks by dataflow ID.
        # *   TaskIds: filters dataflow tasks by task ID.
        # *   Originator: filters dataflow tasks by task initiator.
        # *   TaskActions: filters dataflow tasks by task type.
        # *   DataTypes: filters dataflow tasks by data type.
        # *   Status: filters dataflow tasks by dataflow status.
        # *   CreateTimeBegin: filters dataflow tasks that are created after a specified time.
        # *   CreateTimeEnd: filters dataflow tasks that are created before a specified time.
        # *   StartTimeBegin: filters dataflow tasks that are started after a specified time.
        # *   StartTimeEnd: filters dataflow tasks that are started before a specified time.
        # *   EndTimeBegin: filters dataflow tasks that are stopped after a specified time.
        # *   EndTimeEnd: filters dataflow tasks that are stopped before a specified time.
        self.key = key
        # The value of the filter. This parameter does not support wildcards.
        # 
        # *   If Key is set to DataFlowIds, set Value to a dataflow ID or a part of the dataflow ID. You can specify a dataflow ID or a group of dataflow IDs. You can specify a maximum of 10 dataflow IDs. Example: `df-194433a5be31****` or `df-194433a512a2****,df-234533a5be31****`.
        # *   If Key is set to TaskId, set Value to a dataflow task ID or a part of the dataflow task ID. You can specify a dataflow task ID or a group of dataflow task IDs. You can specify a maximum of 10 dataflow task IDs. Example: `task-38aa8e890f45****` or `task-38aa8e890f45****,task-29ae8e890f45****`.
        # *   If Key is set to TaskActions, set Value to the type of dataflow task. The task type can be **Import**, **Export**, **Evict**, **Inventory**, **StreamImport**, or **StreamExport**. Combined query is supported. CPFS for Lingjun supports only the Import, Export, StreamImport, and StreamExport tasks. Only CPFS for Lingjun V2.6.0 and later support the StreamImport and StreamExport tasks.
        # *   If Key is set to DataTypes, set Value to the data type of the dataflow task. The data type can be MetaAndData, Metadata, or Data. Combined query is supported.
        # *   If Key is set to Originator, set Value to the initiator of the dataflow task. The initiator can be User or System.
        # *   If Key is set to Status, set Value to the status of the dataflow task. The status can be Pending, Executing, Failed, Completed, Canceling, or Canceled. Combined query is supported.
        # *   If Key is set to CreateTimeBegin, set Value to the beginning of the time range to create the dataflow task. Time format: `yyyy-MM-ddThh:mmZ`.
        # *   If Key is set to CreateTimeEnd, set Value to the end of the time range to create the dataflow task. Time format: `yyyy-MM-ddThh:mmZ`.
        # *   If Key is set to StartTimeBegin, set Value to the beginning of the time range to start the dataflow task. Time format: `yyyy-MM-ddThh:mmZ`.
        # *   If Key is set to StartTimeEnd, set Value to the end of the time range to start the dataflow task. Time format: `yyyy-MM-ddThh:mmZ`.
        # *   If Key is set to EndTimeBegin, set Value to the beginning of the time range to stop the dataflow task. Time format: `yyyy-MM-ddThh:mmZ`.
        # *   If Key is set to EndTimeEnd, set Value to the end of the time range to stop the dataflow task. Time format: `yyyy-MM-ddThh:mmZ`.
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

