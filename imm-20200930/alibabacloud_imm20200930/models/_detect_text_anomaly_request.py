# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DetectTextAnomalyRequest(DaraModel):
    def __init__(
        self,
        content: str = None,
        project_name: str = None,
    ):
        # The text to be detected. It can contain up to 10,000 characters (including punctuation marks). Only Chinese text can be detected.
        # 
        # This parameter is required.
        self.content = content
        # The name of the project. For more information, see [CreateProject](https://help.aliyun.com/document_detail/478153.html).
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
        if self.content is not None:
            result['Content'] = self.content

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        return self

