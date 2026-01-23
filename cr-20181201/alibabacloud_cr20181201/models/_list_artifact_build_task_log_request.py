# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListArtifactBuildTaskLogRequest(DaraModel):
    def __init__(
        self,
        build_task_id: str = None,
        instance_id: str = None,
        page: int = None,
        page_size: int = None,
    ):
        # The ID of the artifact build task.
        # 
        # This parameter is required.
        self.build_task_id = build_task_id
        # The ID of the Container Registry instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The number of the page to return.
        # 
        # This parameter is required.
        self.page = page
        # The number of entries per page. Maximum value: 100. If you specify a value greater than 100 for this parameter, the system reports a parameter error or uses 100 as the maximum value.
        # 
        # This parameter is required.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.build_task_id is not None:
            result['BuildTaskId'] = self.build_task_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.page is not None:
            result['Page'] = self.page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuildTaskId') is not None:
            self.build_task_id = m.get('BuildTaskId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

