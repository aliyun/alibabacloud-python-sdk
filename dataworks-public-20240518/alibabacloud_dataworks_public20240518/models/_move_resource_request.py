# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MoveResourceRequest(DaraModel):
    def __init__(
        self,
        id: str = None,
        path: str = None,
        project_id: int = None,
    ):
        # The unique identifier of the Data Studio file resource.
        # 
        # >Notice: Before SDK version 8.0.0, this field is of the Long type. In SDK version 8.0.0 and later, this field is of the String type. **This change does not affect the normal use of the SDK. The parameter is still returned based on the type defined in the SDK**. The type change may cause project compilation failures only when you upgrade the SDK across version 8.0.0. In this case, you must manually correct the data type.
        # 
        # This parameter is required.
        self.id = id
        # The destination path for the move operation. Do not include the file resource name in the path.
        # 
        # For example, to change the path of the math.py file to root/demo/math.py, set this parameter to root/demo.
        # 
        # This parameter is required.
        self.path = path
        # The ID of the DataWorks workspace. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the Workspace Configuration page to obtain the workspace ID.
        # 
        # This parameter specifies the DataWorks workspace for this API operation.
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

