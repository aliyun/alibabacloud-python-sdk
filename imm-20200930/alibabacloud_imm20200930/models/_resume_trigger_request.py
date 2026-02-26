# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ResumeTriggerRequest(DaraModel):
    def __init__(
        self,
        id: str = None,
        project_name: str = None,
    ):
        # The ID of the trigger. You can obtain the ID from the response of the [CreateTrigger](https://help.aliyun.com/document_detail/479912.html) operation.
        # 
        # This parameter is required.
        self.id = id
        # The name of the project. You can obtain the name of the project from the response of the [CreateProject](https://help.aliyun.com/document_detail/478153.html) operation.
        # 
        # This parameter is required.
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        return self

