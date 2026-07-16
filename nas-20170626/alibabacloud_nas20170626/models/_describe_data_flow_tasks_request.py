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
        # - CPFS General-purpose: The ID must start with `cpfs-`, such as cpfs-099394bd928c\\*\\*\\*\\*.
        # 
        # - CPFS for AI Computing: The ID must start with `bmcpfs-`, such as bmcpfs-290w65p03ok64ya\\*\\*\\*\\*.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # A collection of filters.
        self.filters = filters
        # The maximum number of results to return per page.
        # 
        # Valid values: 10 to 100.
        # 
        # Default value: 20.
        self.max_results = max_results
        # The pagination token for the next page of results. If the response is truncated, use this token in your next request to retrieve the subsequent page.
        self.next_token = next_token
        # Specifies whether to return report information.
        # 
        # - True (default): Includes reports in the response.
        # 
        # - False: Excludes reports from the response.
        # 
        # > * Set this parameter to False to speed up the query.
        # >
        # > * This parameter is supported only in CPFS for AI Computing.
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
        # The filter key.
        # 
        # Valid values:
        # 
        # - DataFlowIds: Filters by data flow ID.
        # 
        # - TaskIds: Filters by data flow task ID.
        # 
        # - Originator: Filters by originator.
        # 
        # - TaskActions: Filters by data flow task type.
        # 
        # - DataTypes: Filters by data type.
        # 
        # - Status: Filters by status.
        # 
        # - CreateTimeBegin: Filters data flow tasks created after the specified time.
        # 
        # - CreateTimeEnd: Filters data flow tasks created before the specified time.
        # 
        # - StartTimeBegin: Filters data flow tasks that started after the specified time.
        # 
        # - StartTimeEnd: Filters data flow tasks that started before the specified time.
        # 
        # - EndTimeBegin: Filters data flow tasks that ended after the specified time.
        # 
        # - EndTimeEnd: Filters data flow tasks that ended before the specified time.
        self.key = key
        # The filter value. This parameter does not support wildcards.
        # 
        # - When `Key` is `DataFlowIds`, specify one or more data flow IDs. You can specify up to 10 data flow IDs, separated by commas. For example, `df-194433a5be31****` or `df-194433a512a2****,df-234533a5be31****`.
        # 
        # - When `Key` is `TaskId`, specify one or more data flow task IDs. You can specify up to 10 data flow task IDs, separated by commas. For example, `task-38aa8e890f45****` or `task-38aa8e890f45****,task-29ae8e890f45****`.
        # 
        # - When `Key` is `TaskActions`, specify the data flow task type. Valid values are **Import**, **Export**, **Evict**, **Inventory**, **StreamImport**, and **StreamExport**. You can specify multiple values. CPFS for AI Computing supports only Import, Export, StreamImport, and StreamExport. StreamImport and StreamExport are available only in CPFS for AI Computing 2.6.0 and later.
        # 
        # - When `Key` is `DataTypes`, specify the data type of the data flow task. Valid values are MetaAndData, Metadata, and Data. You can specify multiple values.
        # 
        # - When `Key` is `Originator`, specify the originator of the data flow task. Valid values are User and System.
        # 
        # - When `Key` is `Status`, specify the status of the data flow task. Valid values are Pending, Executing, Failed, Completed, Canceling, and Canceled. You can specify multiple values.
        # 
        # - When `Key` is `CreateTimeBegin`, specify the earliest creation time. Use the `yyyy-MM-ddTHH:mmZ` format.
        # 
        # - When `Key` is `CreateTimeEnd`, specify the latest creation time. Use the `yyyy-MM-ddTHH:mmZ` format.
        # 
        # - When `Key` is `StartTimeBegin`, specify the earliest start time. Use the `yyyy-MM-ddTHH:mmZ` format.
        # 
        # - When `Key` is `StartTimeEnd`, specify the latest start time. Use the `yyyy-MM-ddTHH:mmZ` format.
        # 
        # - When `Key` is `EndTimeBegin`, specify the earliest end time. Use the `yyyy-MM-ddTHH:mmZ` format.
        # 
        # - When `Key` is `EndTimeEnd`, specify the latest end time. Use the `yyyy-MM-ddTHH:mmZ` format.
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

