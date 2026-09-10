# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetBwmMigrationTaskWriterWorkflowListRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        page_index: int = None,
        page_size: int = None,
        workflow_name: str = None,
    ):
        # The submit instance identifier.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The page number. Default value: 1.
        self.page_index = page_index
        # The number of entries per page. Default value: 10.
        self.page_size = page_size
        # The workflow name.
        self.workflow_name = workflow_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.page_index is not None:
            result['pageIndex'] = self.page_index

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.workflow_name is not None:
            result['workflowName'] = self.workflow_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('workflowName') is not None:
            self.workflow_name = m.get('workflowName')

        return self

