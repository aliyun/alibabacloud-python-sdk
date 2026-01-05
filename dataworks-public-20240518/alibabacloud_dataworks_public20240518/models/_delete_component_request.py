# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteComponentRequest(DaraModel):
    def __init__(
        self,
        component_id: str = None,
        project_id: int = None,
    ):
        # The component ID. It can be used as a request parameter for querying the list of production studio components and modifying production studio components.
        # 
        # This parameter is required.
        self.component_id = component_id
        # The ID of the DataWorks workspace. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the Workspace page to query the ID.
        # 
        # This parameter specifies the DataWorks workspace to which the API operation is applied.
        # 
        # This parameter is required.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.component_id is not None:
            result['ComponentId'] = self.component_id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComponentId') is not None:
            self.component_id = m.get('ComponentId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        return self

