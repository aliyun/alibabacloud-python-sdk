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
        topics_shrink: str = None,
        topics_file_url: str = None,
        workspace_id: str = None,
    ):
        # The types of analysis for hot topic selection. Multiple values are supported. If you omit this parameter, the service analyzes all types by default. If you pass an empty array, the service performs only clustering and skips the analysis of hot topics for selection.
        # `HotViewPoints`: Analyzes perspectives on hot topics.
        # `WebReviewPoints`: Analyzes user viewpoints. This requires comments.
        # `TimedViewPoints`: Analyzes perspectives on timeliness.
        # `FreshViewPoints`: Analyzes novel perspectives.
        # `TopicSummary`: Summarizes news content.
        self.analysis_types_shrink = analysis_types_shrink
        # The file type. Valid values: `json` (JSON array) and `jsonLine` (JSON Lines).
        self.file_type = file_type
        # The file URL. You must specify either `FileUrl` or `News`. For details on the file structure, see the description of the `News` parameter.
        self.file_url = file_url
        # The maximum number of topics to analyze. By default, the service sorts clustered news by count in descending order and analyzes the top 50 topics. The maximum value is 200.
        self.max_topic_size = max_topic_size
        # A list of news articles. You must specify either `News` or `FileUrl`.
        self.news_shrink = news_shrink
        # A list of topics.
        self.topics_shrink = topics_shrink
        # The URL of the file that contains the topic list. The file must be in JSON Lines format, with each line representing a single JSON object.
        self.topics_file_url = topics_file_url
        # [The Model Studio workspace ID.](https://help.aliyun.com/document_detail/2782167.html)
        # 
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

        if self.topics_shrink is not None:
            result['Topics'] = self.topics_shrink

        if self.topics_file_url is not None:
            result['TopicsFileUrl'] = self.topics_file_url

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

        if m.get('Topics') is not None:
            self.topics_shrink = m.get('Topics')

        if m.get('TopicsFileUrl') is not None:
            self.topics_file_url = m.get('TopicsFileUrl')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

