# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MoveNodeRequest(DaraModel):
    def __init__(
        self,
        id: str = None,
        path: str = None,
        project_id: int = None,
    ):
        # The ID of the node.
        # 
        # This parameter is required.
        self.id = id
        # The path to which you want to move the node. You do not need to specify a node name in the path.
        # 
        # For example, if you want to move the test node to root/demo/test, you must set this parameter to root/demo.
        # 
        # This parameter is required.
        self.path = path
        # The DataWorks workspace ID. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the Workspace page to query the ID.
        # 
        # You can use this parameter to specify the DataWorks workspace on which you want to perform the API operation.
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
        if self.id is not None:
            result['Id'] = self.id

        if self.path is not None:
            result['Path'] = self.path

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        return self

