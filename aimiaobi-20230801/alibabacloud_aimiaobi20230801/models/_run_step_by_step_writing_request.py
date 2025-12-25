# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class RunStepByStepWritingRequest(DaraModel):
    def __init__(
        self,
        origin_session_id: str = None,
        prompt: str = None,
        reference_data: main_models.RunStepByStepWritingRequestReferenceData = None,
        session_id: str = None,
        task_id: str = None,
        workspace_id: str = None,
        writing_config: main_models.RunStepByStepWritingRequestWritingConfig = None,
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
            temp_model = main_models.RunStepByStepWritingRequestReferenceData()
            self.reference_data = temp_model.from_map(m.get('ReferenceData'))

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        if m.get('WritingConfig') is not None:
            temp_model = main_models.RunStepByStepWritingRequestWritingConfig()
            self.writing_config = temp_model.from_map(m.get('WritingConfig'))

        return self

class RunStepByStepWritingRequestWritingConfig(DaraModel):
    def __init__(
        self,
        domain: str = None,
        keywords: List[str] = None,
        prompt_tag: main_models.RunStepByStepWritingRequestWritingConfigPromptTag = None,
        scene: str = None,
        step: str = None,
        summary_return_type: str = None,
        tags: List[main_models.RunStepByStepWritingRequestWritingConfigTags] = None,
        use_search: bool = None,
    ):
        self.domain = domain
        self.keywords = keywords
        self.prompt_tag = prompt_tag
        self.scene = scene
        self.step = step
        self.summary_return_type = summary_return_type
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

        if self.keywords is not None:
            result['Keywords'] = self.keywords

        if self.prompt_tag is not None:
            result['PromptTag'] = self.prompt_tag.to_map()

        if self.scene is not None:
            result['Scene'] = self.scene

        if self.step is not None:
            result['Step'] = self.step

        if self.summary_return_type is not None:
            result['SummaryReturnType'] = self.summary_return_type

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

        if m.get('Keywords') is not None:
            self.keywords = m.get('Keywords')

        if m.get('PromptTag') is not None:
            temp_model = main_models.RunStepByStepWritingRequestWritingConfigPromptTag()
            self.prompt_tag = temp_model.from_map(m.get('PromptTag'))

        if m.get('Scene') is not None:
            self.scene = m.get('Scene')

        if m.get('Step') is not None:
            self.step = m.get('Step')

        if m.get('SummaryReturnType') is not None:
            self.summary_return_type = m.get('SummaryReturnType')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.RunStepByStepWritingRequestWritingConfigTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('UseSearch') is not None:
            self.use_search = m.get('UseSearch')

        return self

class RunStepByStepWritingRequestWritingConfigTags(DaraModel):
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

class RunStepByStepWritingRequestWritingConfigPromptTag(DaraModel):
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

class RunStepByStepWritingRequestReferenceData(DaraModel):
    def __init__(
        self,
        articles: List[main_models.RunStepByStepWritingRequestReferenceDataArticles] = None,
        mini_doc: List[str] = None,
        outlines: List[main_models.RunStepByStepWritingRequestReferenceDataOutlines] = None,
        summarization: List[str] = None,
    ):
        self.articles = articles
        self.mini_doc = mini_doc
        self.outlines = outlines
        self.summarization = summarization

    def validate(self):
        if self.articles:
            for v1 in self.articles:
                 if v1:
                    v1.validate()
        if self.outlines:
            for v1 in self.outlines:
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

        if self.mini_doc is not None:
            result['MiniDoc'] = self.mini_doc

        result['Outlines'] = []
        if self.outlines is not None:
            for k1 in self.outlines:
                result['Outlines'].append(k1.to_map() if k1 else None)

        if self.summarization is not None:
            result['Summarization'] = self.summarization

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.articles = []
        if m.get('Articles') is not None:
            for k1 in m.get('Articles'):
                temp_model = main_models.RunStepByStepWritingRequestReferenceDataArticles()
                self.articles.append(temp_model.from_map(k1))

        if m.get('MiniDoc') is not None:
            self.mini_doc = m.get('MiniDoc')

        self.outlines = []
        if m.get('Outlines') is not None:
            for k1 in m.get('Outlines'):
                temp_model = main_models.RunStepByStepWritingRequestReferenceDataOutlines()
                self.outlines.append(temp_model.from_map(k1))

        if m.get('Summarization') is not None:
            self.summarization = m.get('Summarization')

        return self

class RunStepByStepWritingRequestReferenceDataOutlines(DaraModel):
    def __init__(
        self,
        articles: List[main_models.RunStepByStepWritingRequestReferenceDataOutlinesArticles] = None,
        outline: str = None,
    ):
        self.articles = articles
        self.outline = outline

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

        if self.outline is not None:
            result['Outline'] = self.outline

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.articles = []
        if m.get('Articles') is not None:
            for k1 in m.get('Articles'):
                temp_model = main_models.RunStepByStepWritingRequestReferenceDataOutlinesArticles()
                self.articles.append(temp_model.from_map(k1))

        if m.get('Outline') is not None:
            self.outline = m.get('Outline')

        return self

class RunStepByStepWritingRequestReferenceDataOutlinesArticles(DaraModel):
    def __init__(
        self,
        content: str = None,
        title: str = None,
        url: str = None,
    ):
        self.content = content
        self.title = title
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.title is not None:
            result['Title'] = self.title

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

class RunStepByStepWritingRequestReferenceDataArticles(DaraModel):
    def __init__(
        self,
        author: str = None,
        content: str = None,
        doc_id: str = None,
        doc_uuid: str = None,
        media_url: str = None,
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
        self.media_url = media_url
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

        if self.media_url is not None:
            result['MediaUrl'] = self.media_url

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

        if m.get('MediaUrl') is not None:
            self.media_url = m.get('MediaUrl')

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

