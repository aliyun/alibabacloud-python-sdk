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
        # The ID of the experiment to which the run belongs.
        self.experiment_id = experiment_id
        # The time when the instance was created.
        self.gmt_create_time = gmt_create_time
        # The labels of the run for an exact match. The following formats are supported:
        # 
        # - Single-label query: "is_evaluation:true"
        # 
        # - Multi-label query: "is_evaluation:true,LLM_evaluation:true". This method is not recommended for common scenarios because it may degrade performance. Use commas (,) to separate multiple labels. The system matches all specified key-value pairs.
        self.labels = labels
        # The maximum number of results to return. The default value is 10.
        self.max_results = max_results
        # The name of the run.
        self.name = name
        # The sort order for the paged query. Use this parameter with SortBy.
        # 
        # - ASC: ascending order.
        # 
        # - DESC (default): descending order.
        self.order = order
        # The fields to sort by and the sort order. You can sort by GmtCreateTime and Name. Valid sort orders are DESC and ASC. The default is ASC. To sort by multiple fields, separate them with a comma (,).
        self.order_by = order_by
        # The page number. The value must be greater than 0. Default value: 1.
        self.page_number = page_number
        # The number of records to display on each page.
        self.page_size = page_size
        # The paging token. The value starts from 0. The default value is 0.
        self.page_token = page_token
        # The field to use for sorting. Valid values:
        # 
        # - Name: the name of the run.
        # 
        # - GmtCreateTime (default): the time when the run was created.
        self.sort_by = sort_by
        # The ID of the PAI workload associated with the run.
        self.source_id = source_id
        # The type of the PAI workload associated with the run.
        self.source_type = source_type
        # Specifies whether to display details, including Metrics, Params, and Labels. Valid values:
        # 
        # - true: displays details.
        # 
        # - false (default): does not display details.
        self.verbose = verbose
        # The ID of the workspace where the experiment resides. For more information about how to obtain a workspace ID, see [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html).
        # 
        # > If you do not specify a workspace ID, the system returns the list of runs in the default workspace.
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

