# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class SubmitCustomSourceTopicAnalysisRequest(DaraModel):
    def __init__(
        self,
        analysis_types: List[str] = None,
        file_type: str = None,
        file_url: str = None,
        max_topic_size: int = None,
        news: List[main_models.SubmitCustomSourceTopicAnalysisRequestNews] = None,
        workspace_id: str = None,
    ):
        self.analysis_types = analysis_types
        self.file_type = file_type
        self.file_url = file_url
        self.max_topic_size = max_topic_size
        self.news = news
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        if self.news:
            for v1 in self.news:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.analysis_types is not None:
            result['AnalysisTypes'] = self.analysis_types

        if self.file_type is not None:
            result['FileType'] = self.file_type

        if self.file_url is not None:
            result['FileUrl'] = self.file_url

        if self.max_topic_size is not None:
            result['MaxTopicSize'] = self.max_topic_size

        result['News'] = []
        if self.news is not None:
            for k1 in self.news:
                result['News'].append(k1.to_map() if k1 else None)

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnalysisTypes') is not None:
            self.analysis_types = m.get('AnalysisTypes')

        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')

        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')

        if m.get('MaxTopicSize') is not None:
            self.max_topic_size = m.get('MaxTopicSize')

        self.news = []
        if m.get('News') is not None:
            for k1 in m.get('News'):
                temp_model = main_models.SubmitCustomSourceTopicAnalysisRequestNews()
                self.news.append(temp_model.from_map(k1))

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

class SubmitCustomSourceTopicAnalysisRequestNews(DaraModel):
    def __init__(
        self,
        comments: List[main_models.SubmitCustomSourceTopicAnalysisRequestNewsComments] = None,
        content: str = None,
        pub_time: str = None,
        source: str = None,
        title: str = None,
        url: str = None,
    ):
        self.comments = comments
        self.content = content
        self.pub_time = pub_time
        self.source = source
        self.title = title
        self.url = url

    def validate(self):
        if self.comments:
            for v1 in self.comments:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Comments'] = []
        if self.comments is not None:
            for k1 in self.comments:
                result['Comments'].append(k1.to_map() if k1 else None)

        if self.content is not None:
            result['Content'] = self.content

        if self.pub_time is not None:
            result['PubTime'] = self.pub_time

        if self.source is not None:
            result['Source'] = self.source

        if self.title is not None:
            result['Title'] = self.title

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.comments = []
        if m.get('Comments') is not None:
            for k1 in m.get('Comments'):
                temp_model = main_models.SubmitCustomSourceTopicAnalysisRequestNewsComments()
                self.comments.append(temp_model.from_map(k1))

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('PubTime') is not None:
            self.pub_time = m.get('PubTime')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

class SubmitCustomSourceTopicAnalysisRequestNewsComments(DaraModel):
    def __init__(
        self,
        text: str = None,
    ):
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.text is not None:
            result['Text'] = self.text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Text') is not None:
            self.text = m.get('Text')

        return self

