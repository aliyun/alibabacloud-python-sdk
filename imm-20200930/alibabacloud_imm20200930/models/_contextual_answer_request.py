# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class ContextualAnswerRequest(DaraModel):
    def __init__(
        self,
        files: List[main_models.ContextualFile] = None,
        messages: List[main_models.ContextualMessage] = None,
        project_name: str = None,
    ):
        # The content of the files involved in the current Q&A. It is recommended to use the return value of the ContextualRetrieval interface as input.
        self.files = files
        # Yes, the history of conversations and tool invocations. The latest message is at the end (index n-1), and the oldest message is at the beginning (index 0).
        # It must be in the form of user-assistant pairs, with a total count of 2*n+1, and the length of the latest question should not exceed 1000 characters.
        # The length of the historical conversation is limited to 100.
        # 
        # This parameter is required.
        self.messages = messages
        # Project name. For how to obtain it, see [Creating a Project](https://help.aliyun.com/zh/imm/getting-started/create-a-project-1?spm=a2c4g.11186623.help-menu-search-62354.d_0).
        # 
        # This parameter is required.
        self.project_name = project_name

    def validate(self):
        if self.files:
            for v1 in self.files:
                 if v1:
                    v1.validate()
        if self.messages:
            for v1 in self.messages:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Files'] = []
        if self.files is not None:
            for k1 in self.files:
                result['Files'].append(k1.to_map() if k1 else None)

        result['Messages'] = []
        if self.messages is not None:
            for k1 in self.messages:
                result['Messages'].append(k1.to_map() if k1 else None)

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.files = []
        if m.get('Files') is not None:
            for k1 in m.get('Files'):
                temp_model = main_models.ContextualFile()
                self.files.append(temp_model.from_map(k1))

        self.messages = []
        if m.get('Messages') is not None:
            for k1 in m.get('Messages'):
                temp_model = main_models.ContextualMessage()
                self.messages.append(temp_model.from_map(k1))

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        return self

