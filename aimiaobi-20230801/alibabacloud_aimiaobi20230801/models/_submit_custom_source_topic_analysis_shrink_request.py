# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitCustomSourceTopicAnalysisShrinkRequest(DaraModel):
    def __init__(
        self,
        analysis_types_shrink: str = None,
        file_type: str = None,
        file_url: str = None,
        max_topic_size: int = None,
        news_shrink: str = None,
        workspace_id: str = None,
    ):
        self.analysis_types_shrink = analysis_types_shrink
        self.file_type = file_type
        self.file_url = file_url
        self.max_topic_size = max_topic_size
        self.news_shrink = news_shrink
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.analysis_types_shrink is not None:
            result['AnalysisTypes'] = self.analysis_types_shrink

        if self.file_type is not None:
            result['FileType'] = self.file_type

        if self.file_url is not None:
            result['FileUrl'] = self.file_url

        if self.max_topic_size is not None:
            result['MaxTopicSize'] = self.max_topic_size

        if self.news_shrink is not None:
            result['News'] = self.news_shrink

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnalysisTypes') is not None:
            self.analysis_types_shrink = m.get('AnalysisTypes')

        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')

        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')

        if m.get('MaxTopicSize') is not None:
            self.max_topic_size = m.get('MaxTopicSize')

        if m.get('News') is not None:
            self.news_shrink = m.get('News')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

