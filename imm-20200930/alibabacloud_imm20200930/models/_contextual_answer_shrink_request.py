# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ContextualAnswerShrinkRequest(DaraModel):
    def __init__(
        self,
        files_shrink: str = None,
        messages_shrink: str = None,
        project_name: str = None,
    ):
        # The content of the files involved in the current Q&A. It is recommended to use the return value of the ContextualRetrieval interface as input.
        self.files_shrink = files_shrink
        # Yes, the history of conversations and tool invocations. The latest message is at the end (index n-1), and the oldest message is at the beginning (index 0).
        # It must be in the form of user-assistant pairs, with a total count of 2*n+1, and the length of the latest question should not exceed 1000 characters.
        # The length of the historical conversation is limited to 100.
        # 
        # This parameter is required.
        self.messages_shrink = messages_shrink
        # Project name. For how to obtain it, see [Creating a Project](https://help.aliyun.com/zh/imm/getting-started/create-a-project-1?spm=a2c4g.11186623.help-menu-search-62354.d_0).
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
        if self.files_shrink is not None:
            result['Files'] = self.files_shrink

        if self.messages_shrink is not None:
            result['Messages'] = self.messages_shrink

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Files') is not None:
            self.files_shrink = m.get('Files')

        if m.get('Messages') is not None:
            self.messages_shrink = m.get('Messages')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        return self

