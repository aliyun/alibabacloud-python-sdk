# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class SubmitTopicSelectionPerspectiveAnalysisTaskRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        documents: List[main_models.SubmitTopicSelectionPerspectiveAnalysisTaskRequestDocuments] = None,
        perspective_types: List[str] = None,
        topic: str = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        self.documents = documents
        self.perspective_types = perspective_types
        self.topic = topic

    def validate(self):
        if self.documents:
            for v1 in self.documents:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key

        result['Documents'] = []
        if self.documents is not None:
            for k1 in self.documents:
                result['Documents'].append(k1.to_map() if k1 else None)

        if self.perspective_types is not None:
            result['PerspectiveTypes'] = self.perspective_types

        if self.topic is not None:
            result['Topic'] = self.topic

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        self.documents = []
        if m.get('Documents') is not None:
            for k1 in m.get('Documents'):
                temp_model = main_models.SubmitTopicSelectionPerspectiveAnalysisTaskRequestDocuments()
                self.documents.append(temp_model.from_map(k1))

        if m.get('PerspectiveTypes') is not None:
            self.perspective_types = m.get('PerspectiveTypes')

        if m.get('Topic') is not None:
            self.topic = m.get('Topic')

        return self

class SubmitTopicSelectionPerspectiveAnalysisTaskRequestDocuments(DaraModel):
    def __init__(
        self,
        author: str = None,
        comments: List[main_models.SubmitTopicSelectionPerspectiveAnalysisTaskRequestDocumentsComments] = None,
        content: str = None,
        pub_time: str = None,
        source: str = None,
        summary: str = None,
        title: str = None,
        url: str = None,
    ):
        self.author = author
        self.comments = comments
        # This parameter is required.
        self.content = content
        self.pub_time = pub_time
        self.source = source
        self.summary = summary
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
        if self.author is not None:
            result['Author'] = self.author

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

        if self.summary is not None:
            result['Summary'] = self.summary

        if self.title is not None:
            result['Title'] = self.title

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Author') is not None:
            self.author = m.get('Author')

        self.comments = []
        if m.get('Comments') is not None:
            for k1 in m.get('Comments'):
                temp_model = main_models.SubmitTopicSelectionPerspectiveAnalysisTaskRequestDocumentsComments()
                self.comments.append(temp_model.from_map(k1))

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('PubTime') is not None:
            self.pub_time = m.get('PubTime')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

class SubmitTopicSelectionPerspectiveAnalysisTaskRequestDocumentsComments(DaraModel):
    def __init__(
        self,
        text: str = None,
        username: str = None,
    ):
        self.text = text
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.text is not None:
            result['Text'] = self.text

        if self.username is not None:
            result['Username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Text') is not None:
            self.text = m.get('Text')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        return self

