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
        # The time when the instance was created. The time is displayed in UTC and follows the ISO 8601 standard in the YYYY-MM-DDTHH:mm:ss.sssZ format.
        self.gmt_create_time = gmt_create_time
        # The labels of the task for exact matching. Supported formats:
        # - Single-label query: "is_evaluation:true"
        # - Multi-label scenario (not recommended for common scenarios due to potential performance issues): "is_evaluation:true,LLM_evaluation:true". Use commas (,) to separate multiple labels, which means all specified label key-value pairs must be matched at the same time.
        self.labels = labels
        # The maximum number of results to return for the request. Default value: 10.
        self.max_results = max_results
        # The name of the run.
        self.name = name
        # Specifies the sorting of the specified field during a paged query. This parameter is used together with SortBy for paging. Valid values:
        # - ASC: ascending order.
        # - DESC (default): descending order.
        self.order = order
        # The list of strings that specify the sort order. Supported fields for sorting include GmtCreateTime and Name. The sort orders include DESC and ASC. Default value: ASC. You can specify multiple fields and separate them with commas (,).
        self.order_by = order_by
        # The current page number. Valid values: integers greater than 0. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page.
        self.page_size = page_size
        # The pagination token. The value starts from 0. Default value: 0.
        self.page_token = page_token
        # The name of the field used for sorting. Valid values:
        # - Name: the name of the run.
        # - GmtCreateTime (default): the time when the run was created.
        self.sort_by = sort_by
        # The ID of the PAI workload associated with the run.
        self.source_id = source_id
        # The type of the PAI workload associated with the run.
        self.source_type = source_type
        # Specifies whether to display detailed information, including Metrics, Params, and Labels. Valid values:
        # - true: Displays detailed information.
        # - false (default): Does not display detailed information.
        self.verbose = verbose
        # The ID of the workspace to which the experiment belongs. For more information about how to obtain the workspace ID, see [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html). If you do not specify the workspace ID, the system returns the runs in the default workspace.
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

