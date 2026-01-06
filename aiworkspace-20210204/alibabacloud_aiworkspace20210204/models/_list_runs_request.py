# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListRunsRequest(DaraModel):
    def __init__(
        self,
        experiment_id: str = None,
        gmt_create_time: str = None,
        labels: str = None,
        max_results: int = None,
        name: str = None,
        order: str = None,
        order_by: str = None,
        page_number: int = None,
        page_size: int = None,
        page_token: int = None,
        sort_by: str = None,
        source_id: str = None,
        source_type: str = None,
        verbose: bool = None,
        workspace_id: str = None,
    ):
        # The ID of the experiment that the run belongs.
        self.experiment_id = experiment_id
        # The time when the instance was created.
        self.gmt_create_time = gmt_create_time
        # The label. Exact match is supported. Valid values:
        # 
        # *   Single-label query: Set the value to is_evaluation.
        # *   Multi-label query (not recommended in non-special scenarios and may have performance issues): Set the value to is_evaluation:true,LLM_evaluation:true. Multiple labels are separated with commas (,), indicating that the key-value pairs of multiple labels must be matched at the same time.
        self.labels = labels
        # The maximum number of entries in the request. Default value: 10.
        self.max_results = max_results
        # The run name.
        self.name = name
        # The order in which the entries are sorted by the specific field on the returned page. This parameter must be used together with SortBy.
        # 
        # *   ASC
        # *   DESC (default)
        self.order = order
        # The strings by which the results are sorted. The following parameters can be used to sort the results: GmtCreateTime and Name. The sorting order can be ASC (default) and DESC. Separate multiple strings with commas (,).
        self.order_by = order_by
        # The page number. The value must be greater than 0. Default value: 1.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The pagination token, which starts from 0. Default value: 0.
        self.page_token = page_token
        # The field used for sorting. Valid values:
        # 
        # *   Name: the name of the run.
        # *   GmtCreateTime: the time when the run is created.
        self.sort_by = sort_by
        # The ID of the workload associated with the run.
        self.source_id = source_id
        # The type of the workload associated with the run.
        self.source_type = source_type
        # Specifies whether to show detailed information, including Metrics, Params, and Labels. Valid values:
        # 
        # *   true
        # *   false (default)
        self.verbose = verbose
        # The ID of the workspace to which the experiment belongs. You can call [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html) to obtain the workspace ID.
        # 
        # >  If you do not specify a workspace ID, the system returns the runs of the default workspace.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.labels is not None:
            result['Labels'] = self.labels

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.name is not None:
            result['Name'] = self.name

        if self.order is not None:
            result['Order'] = self.order

        if self.order_by is not None:
            result['OrderBy'] = self.order_by

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.page_token is not None:
            result['PageToken'] = self.page_token

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.source_id is not None:
            result['SourceId'] = self.source_id

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.verbose is not None:
            result['Verbose'] = self.verbose

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('Labels') is not None:
            self.labels = m.get('Labels')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PageToken') is not None:
            self.page_token = m.get('PageToken')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('Verbose') is not None:
            self.verbose = m.get('Verbose')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

