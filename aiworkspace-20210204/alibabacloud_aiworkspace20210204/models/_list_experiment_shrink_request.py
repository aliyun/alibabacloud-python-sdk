# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListExperimentShrinkRequest(DaraModel):
    def __init__(
        self,
        labels: str = None,
        max_results: int = None,
        name: str = None,
        options_shrink: str = None,
        order: str = None,
        order_by: str = None,
        page_number: int = None,
        page_size: int = None,
        page_token: int = None,
        sort_by: str = None,
        verbose: bool = None,
        workspace_id: str = None,
    ):
        # The label filter conditions. Separate multiple conditions with commas (,).
        # The format of a single filter condition is `Key=Value`.
        self.labels = labels
        # The maximum number of results to return for the request. Default value: 10.
        self.max_results = max_results
        # The name of the experiment.
        self.name = name
        # The optional parameters.
        self.options_shrink = options_shrink
        # The sort order of the specified field in a paged query. Valid values:
        # - ASC: ascending order.
        # - DESC: descending order.
        # Default value: DESC.
        self.order = order
        # The list of sort order strings. Supported fields for sorting include GmtCreateTime, Name, GmtModifiedTime, and ExperimentId. The sort order can be DESC or ASC. Default value: ASC.
        self.order_by = order_by
        # The page number. Pages start from 1.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The pagination token. Pages start from 0. Default value: 0.
        self.page_token = page_token
        # The field by which to sort the results of a paged query. Currently, only the GmtCreateTime field is supported for sorting.
        self.sort_by = sort_by
        # Specifies whether to retrieve the LatestRun information associated with the experiment.
        self.verbose = verbose
        # The ID of the workspace to which the experiment belongs. For more information about how to obtain the workspace ID, see [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html).
        # > If you do not specify the workspace ID, the system returns the list of experiments in the default workspace.
        # >
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.labels is not None:
            result['Labels'] = self.labels

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.name is not None:
            result['Name'] = self.name

        if self.options_shrink is not None:
            result['Options'] = self.options_shrink

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

        if self.verbose is not None:
            result['Verbose'] = self.verbose

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Options') is not None:
            self.options_shrink = m.get('Options')

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

        if m.get('Verbose') is not None:
            self.verbose = m.get('Verbose')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

