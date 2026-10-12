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
        # The time when the instance was created. The time follows the ISO 8601 standard in UTC. Format: YYYY-MM-DDTHH:mm:ss.sssZ.
        self.gmt_create_time = gmt_create_time
        # The labels of the task for exact match. Supported formats:
        # - Single-label query: "is_evaluation:true"
        # - Multi-label scenario (not recommended except in special cases due to potential performance issues): "is_evaluation:true,LLM_evaluation:true" separated by commas (,), indicating that multiple label key-value pairs must all match.
        self.labels = labels
        # The maximum number of results to return. Default value: 10.
        self.max_results = max_results
        # The run name.
        self.name = name
        # The sorting order for the specified field in a paging query. Used together with SortBy. Valid values:
        # - ASC: Ascending order.
        # - DESC (default): Descending order.
        self.order = order
        # A comma-separated list of sorting strings. Supported fields: GmtCreateTime and Name. Supported sorting orders: DESC and ASC. Default: ASC. Separate multiple fields with commas (,).
        self.order_by = order_by
        # The page number. Valid values: greater than 0. Default value: 1.
        self.page_number = page_number
        # The number of records per page.
        self.page_size = page_size
        # The pagination token. Starts from 0. Default value: 0.
        self.page_token = page_token
        # The field used for sorting. Valid values:
        # - Name: The run name.
        # - GmtCreateTime (default): The run creation time.
        self.sort_by = sort_by
        # The ID of the PAI workload associated with the run.
        self.source_id = source_id
        # The type of the PAI workload associated with the run.
        self.source_type = source_type
        # Specifies whether to display detailed information, including Metrics, Params, and Labels. Valid values:
        # - true: Detailed information is displayed.
        # - false (default): Detailed information is not displayed.
        self.verbose = verbose
        # The ID of the workspace where the experiment resides. For information about how to obtain the workspace ID, see [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html).
        # > If you do not specify a workspace ID, the system returns the run list of the default workspace.
        # >
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

