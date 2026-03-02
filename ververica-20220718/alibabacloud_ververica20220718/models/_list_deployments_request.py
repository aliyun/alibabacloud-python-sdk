# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDeploymentsRequest(DaraModel):
    def __init__(
        self,
        creator: str = None,
        execution_mode: str = None,
        label_key: str = None,
        label_value_array: str = None,
        modifier: str = None,
        name: str = None,
        page_index: int = None,
        page_size: int = None,
        sort_name: str = None,
        status: str = None,
    ):
        # The ID of the user who creates the deployment.
        self.creator = creator
        # The execution mode of the deployment.
        # 
        # Valid values:
        # 
        # *   BATCH
        # *   STREAMING
        self.execution_mode = execution_mode
        # The tag key.
        self.label_key = label_key
        # The tag value. Separate multiple values with semicolon (;).
        self.label_value_array = label_value_array
        # The ID of the user who modifies the deployment.
        self.modifier = modifier
        # The name of the deployment.
        self.name = name
        # The page number. Minimum value: 1. Default value: 1.
        self.page_index = page_index
        # The number of entries per page. Valid values: 1 to 100. Default value: 10.
        self.page_size = page_size
        self.sort_name = sort_name
        # The latest status of the deployment.
        # 
        # Valid values:
        # 
        # *   CANCELLED
        # *   FAILED
        # *   RUNNING
        # *   TRANSITIONING
        # *   FINISHED
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creator is not None:
            result['creator'] = self.creator

        if self.execution_mode is not None:
            result['executionMode'] = self.execution_mode

        if self.label_key is not None:
            result['labelKey'] = self.label_key

        if self.label_value_array is not None:
            result['labelValueArray'] = self.label_value_array

        if self.modifier is not None:
            result['modifier'] = self.modifier

        if self.name is not None:
            result['name'] = self.name

        if self.page_index is not None:
            result['pageIndex'] = self.page_index

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.sort_name is not None:
            result['sortName'] = self.sort_name

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('creator') is not None:
            self.creator = m.get('creator')

        if m.get('executionMode') is not None:
            self.execution_mode = m.get('executionMode')

        if m.get('labelKey') is not None:
            self.label_key = m.get('labelKey')

        if m.get('labelValueArray') is not None:
            self.label_value_array = m.get('labelValueArray')

        if m.get('modifier') is not None:
            self.modifier = m.get('modifier')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('sortName') is not None:
            self.sort_name = m.get('sortName')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

