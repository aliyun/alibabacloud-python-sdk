# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListJobsRequest(DaraModel):
    def __init__(
        self,
        deployment_id: str = None,
        page_index: int = None,
        page_size: int = None,
        sort_name: str = None,
        sort_order: str = None,
    ):
        # The deployment ID.
        # 
        # This parameter is required.
        self.deployment_id = deployment_id
        # The page number. Minimum value: 1. Default value: 1.
        self.page_index = page_index
        # The number of entries per page. Valid values: 1 to 100. Default value: 10.
        self.page_size = page_size
        # The collation.
        # 
        # Valid values:
        # 
        # *   gmt_create
        # *   job_id
        # *   status
        self.sort_name = sort_name
        self.sort_order = sort_order

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.deployment_id is not None:
            result['deploymentId'] = self.deployment_id

        if self.page_index is not None:
            result['pageIndex'] = self.page_index

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.sort_name is not None:
            result['sortName'] = self.sort_name

        if self.sort_order is not None:
            result['sortOrder'] = self.sort_order

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deploymentId') is not None:
            self.deployment_id = m.get('deploymentId')

        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('sortName') is not None:
            self.sort_name = m.get('sortName')

        if m.get('sortOrder') is not None:
            self.sort_order = m.get('sortOrder')

        return self

