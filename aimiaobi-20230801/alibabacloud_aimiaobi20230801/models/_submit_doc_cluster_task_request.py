# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class SubmitDocClusterTaskRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        documents: List[main_models.SubmitDocClusterTaskRequestDocuments] = None,
        summary_length: int = None,
        title_length: int = None,
        topic_count: int = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        # This parameter is required.
        self.documents = documents
        self.summary_length = summary_length
        self.title_length = title_length
        self.topic_count = topic_count

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

        if self.summary_length is not None:
            result['SummaryLength'] = self.summary_length

        if self.title_length is not None:
            result['TitleLength'] = self.title_length

        if self.topic_count is not None:
            result['TopicCount'] = self.topic_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        self.documents = []
        if m.get('Documents') is not None:
            for k1 in m.get('Documents'):
                temp_model = main_models.SubmitDocClusterTaskRequestDocuments()
                self.documents.append(temp_model.from_map(k1))

        if m.get('SummaryLength') is not None:
            self.summary_length = m.get('SummaryLength')

        if m.get('TitleLength') is not None:
            self.title_length = m.get('TitleLength')

        if m.get('TopicCount') is not None:
            self.topic_count = m.get('TopicCount')

        return self

class SubmitDocClusterTaskRequestDocuments(DaraModel):
    def __init__(
        self,
        content: str = None,
        doc_id: str = None,
        title: str = None,
    ):
        # This parameter is required.
        self.content = content
        self.doc_id = doc_id
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.doc_id is not None:
            result['DocId'] = self.doc_id

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('DocId') is not None:
            self.doc_id = m.get('DocId')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

