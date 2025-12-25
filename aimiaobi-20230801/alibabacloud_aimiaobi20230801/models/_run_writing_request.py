# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class RunWritingRequest(DaraModel):
    def __init__(
        self,
        origin_session_id: str = None,
        prompt: str = None,
        reference_data: main_models.RunWritingRequestReferenceData = None,
        session_id: str = None,
        task_id: str = None,
        workspace_id: str = None,
        writing_config: main_models.RunWritingRequestWritingConfig = None,
    ):
        self.origin_session_id = origin_session_id
        # This parameter is required.
        self.prompt = prompt
        self.reference_data = reference_data
        self.session_id = session_id
        self.task_id = task_id
        # This parameter is required.
        self.workspace_id = workspace_id
        self.writing_config = writing_config

    def validate(self):
        if self.reference_data:
            self.reference_data.validate()
        if self.writing_config:
            self.writing_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.origin_session_id is not None:
            result['OriginSessionId'] = self.origin_session_id

        if self.prompt is not None:
            result['Prompt'] = self.prompt

        if self.reference_data is not None:
            result['ReferenceData'] = self.reference_data.to_map()

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        if self.writing_config is not None:
            result['WritingConfig'] = self.writing_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OriginSessionId') is not None:
            self.origin_session_id = m.get('OriginSessionId')

        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')

        if m.get('ReferenceData') is not None:
            temp_model = main_models.RunWritingRequestReferenceData()
            self.reference_data = temp_model.from_map(m.get('ReferenceData'))

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        if m.get('WritingConfig') is not None:
            temp_model = main_models.RunWritingRequestWritingConfig()
            self.writing_config = temp_model.from_map(m.get('WritingConfig'))

        return self

class RunWritingRequestWritingConfig(DaraModel):
    def __init__(
        self,
        domain: str = None,
        prompt_tag: main_models.RunWritingRequestWritingConfigPromptTag = None,
        tags: List[main_models.RunWritingRequestWritingConfigTags] = None,
        use_search: bool = None,
    ):
        self.domain = domain
        self.prompt_tag = prompt_tag
        self.tags = tags
        self.use_search = use_search

    def validate(self):
        if self.prompt_tag:
            self.prompt_tag.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain is not None:
            result['Domain'] = self.domain

        if self.prompt_tag is not None:
            result['PromptTag'] = self.prompt_tag.to_map()

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.use_search is not None:
            result['UseSearch'] = self.use_search

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('PromptTag') is not None:
            temp_model = main_models.RunWritingRequestWritingConfigPromptTag()
            self.prompt_tag = temp_model.from_map(m.get('PromptTag'))

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.RunWritingRequestWritingConfigTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('UseSearch') is not None:
            self.use_search = m.get('UseSearch')

        return self

class RunWritingRequestWritingConfigTags(DaraModel):
    def __init__(
        self,
        keyword: str = None,
        tag: str = None,
    ):
        self.keyword = keyword
        self.tag = tag

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.tag is not None:
            result['Tag'] = self.tag

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        return self

class RunWritingRequestWritingConfigPromptTag(DaraModel):
    def __init__(
        self,
        necessary_tips: str = None,
        position: str = None,
        reverse_words: str = None,
        theme: str = None,
    ):
        self.necessary_tips = necessary_tips
        self.position = position
        self.reverse_words = reverse_words
        self.theme = theme

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.necessary_tips is not None:
            result['NecessaryTips'] = self.necessary_tips

        if self.position is not None:
            result['Position'] = self.position

        if self.reverse_words is not None:
            result['ReverseWords'] = self.reverse_words

        if self.theme is not None:
            result['Theme'] = self.theme

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NecessaryTips') is not None:
            self.necessary_tips = m.get('NecessaryTips')

        if m.get('Position') is not None:
            self.position = m.get('Position')

        if m.get('ReverseWords') is not None:
            self.reverse_words = m.get('ReverseWords')

        if m.get('Theme') is not None:
            self.theme = m.get('Theme')

        return self

class RunWritingRequestReferenceData(DaraModel):
    def __init__(
        self,
        articles: List[main_models.RunWritingRequestReferenceDataArticles] = None,
    ):
        self.articles = articles

    def validate(self):
        if self.articles:
            for v1 in self.articles:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Articles'] = []
        if self.articles is not None:
            for k1 in self.articles:
                result['Articles'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.articles = []
        if m.get('Articles') is not None:
            for k1 in m.get('Articles'):
                temp_model = main_models.RunWritingRequestReferenceDataArticles()
                self.articles.append(temp_model.from_map(k1))

        return self

class RunWritingRequestReferenceDataArticles(DaraModel):
    def __init__(
        self,
        author: str = None,
        content: str = None,
        doc_id: str = None,
        doc_uuid: str = None,
        pub_time: str = None,
        source: str = None,
        summary: str = None,
        tag: str = None,
        title: str = None,
        url: str = None,
    ):
        self.author = author
        self.content = content
        self.doc_id = doc_id
        self.doc_uuid = doc_uuid
        self.pub_time = pub_time
        self.source = source
        self.summary = summary
        self.tag = tag
        self.title = title
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.author is not None:
            result['Author'] = self.author

        if self.content is not None:
            result['Content'] = self.content

        if self.doc_id is not None:
            result['DocId'] = self.doc_id

        if self.doc_uuid is not None:
            result['DocUuid'] = self.doc_uuid

        if self.pub_time is not None:
            result['PubTime'] = self.pub_time

        if self.source is not None:
            result['Source'] = self.source

        if self.summary is not None:
            result['Summary'] = self.summary

        if self.tag is not None:
            result['Tag'] = self.tag

        if self.title is not None:
            result['Title'] = self.title

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Author') is not None:
            self.author = m.get('Author')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('DocId') is not None:
            self.doc_id = m.get('DocId')

        if m.get('DocUuid') is not None:
            self.doc_uuid = m.get('DocUuid')

        if m.get('PubTime') is not None:
            self.pub_time = m.get('PubTime')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

