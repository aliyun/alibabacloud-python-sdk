# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aiworkspace20210204 import models as main_models
from darabonba.model import DaraModel

class ListExperimentRequest(DaraModel):
    def __init__(
        self,
        labels: str = None,
        max_results: int = None,
        name: str = None,
        options: main_models.ListExperimentRequestOptions = None,
        order: str = None,
        order_by: str = None,
        page_number: int = None,
        page_size: int = None,
        page_token: int = None,
        sort_by: str = None,
        verbose: bool = None,
        workspace_id: str = None,
    ):
        # The tag filter conditions. Multiple conditions are separated by commas (,). The format of a single condition filter is `key=value`.
        self.labels = labels
        # The maximum number of entries in the request. Default value: 10.
        self.max_results = max_results
        # The experiment name.
        self.name = name
        # The optional parameters.
        self.options = options
        # The order of specific fields of results in a paged query (ascending or descending).
        # 
        # *   ASC: ascending order
        # *   DESC: descending order. This is the default value.
        self.order = order
        # The strings used for sorting. The following fields can be used for sorting: GmtCreateTime, Name, GmtModifiedTime, and ExperimentId. The sorting order can be ASC (default) and DESC.
        self.order_by = order_by
        # The page number. The value starts from 1.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The pagination token, which starts from 0. Default value: 0.
        self.page_token = page_token
        # The field used for sorting. The GmtCreateTime field is used.
        self.sort_by = sort_by
        # Specifies whether to obtain the LatestRun value that is related to the experiment.
        self.verbose = verbose
        # The ID of the workspace to which the experiment belongs. You can call [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html) to obtain the workspace ID.
        # 
        # >  If you do not specify a workspace ID, the system returns the experiments in the default workspace.
        self.workspace_id = workspace_id

    def validate(self):
        if self.options:
            self.options.validate()

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

        if self.options is not None:
            result['Options'] = self.options.to_map()

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
            temp_model = main_models.ListExperimentRequestOptions()
            self.options = temp_model.from_map(m.get('Options'))

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

class ListExperimentRequestOptions(DaraModel):
    def __init__(
        self,
        match_name_exactly: str = None,
    ):
        # Specifies whether to exactly match the experiment by name. Valid values: true and false.
        self.match_name_exactly = match_name_exactly

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.match_name_exactly is not None:
            result['match_name_exactly'] = self.match_name_exactly

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('match_name_exactly') is not None:
            self.match_name_exactly = m.get('match_name_exactly')

        return self

