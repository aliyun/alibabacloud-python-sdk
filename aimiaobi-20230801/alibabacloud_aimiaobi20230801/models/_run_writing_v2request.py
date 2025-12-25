# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class RunWritingV2Request(DaraModel):
    def __init__(
        self,
        articles: List[main_models.RunWritingV2RequestArticles] = None,
        distribute_writing: bool = None,
        gc_number_size: int = None,
        gc_number_size_tag: str = None,
        keywords: List[str] = None,
        language: str = None,
        mini_docs: List[main_models.RunWritingV2RequestMiniDocs] = None,
        outline_list: List[main_models.WritingOutline] = None,
        outlines: List[main_models.RunWritingV2RequestOutlines] = None,
        prompt: str = None,
        prompt_mode: str = None,
        search_sources: List[main_models.RunWritingV2RequestSearchSources] = None,
        session_id: str = None,
        source_trace_method: str = None,
        step: str = None,
        summarization: List[main_models.RunWritingV2RequestSummarization] = None,
        task_id: str = None,
        use_search: bool = None,
        workspace_id: str = None,
        writing_params: Dict[str, str] = None,
        writing_scene: str = None,
        writing_style: str = None,
    ):
        self.articles = articles
        self.distribute_writing = distribute_writing
        self.gc_number_size = gc_number_size
        self.gc_number_size_tag = gc_number_size_tag
        self.keywords = keywords
        self.language = language
        self.mini_docs = mini_docs
        self.outline_list = outline_list
        self.outlines = outlines
        self.prompt = prompt
        self.prompt_mode = prompt_mode
        self.search_sources = search_sources
        self.session_id = session_id
        self.source_trace_method = source_trace_method
        self.step = step
        self.summarization = summarization
        self.task_id = task_id
        self.use_search = use_search
        # This parameter is required.
        self.workspace_id = workspace_id
        self.writing_params = writing_params
        self.writing_scene = writing_scene
        self.writing_style = writing_style

    def validate(self):
        if self.articles:
            for v1 in self.articles:
                 if v1:
                    v1.validate()
        if self.mini_docs:
            for v1 in self.mini_docs:
                 if v1:
                    v1.validate()
        if self.outline_list:
            for v1 in self.outline_list:
                 if v1:
                    v1.validate()
        if self.outlines:
            for v1 in self.outlines:
                 if v1:
                    v1.validate()
        if self.search_sources:
            for v1 in self.search_sources:
                 if v1:
                    v1.validate()
        if self.summarization:
            for v1 in self.summarization:
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

        if self.distribute_writing is not None:
            result['DistributeWriting'] = self.distribute_writing

        if self.gc_number_size is not None:
            result['GcNumberSize'] = self.gc_number_size

        if self.gc_number_size_tag is not None:
            result['GcNumberSizeTag'] = self.gc_number_size_tag

        if self.keywords is not None:
            result['Keywords'] = self.keywords

        if self.language is not None:
            result['Language'] = self.language

        result['MiniDocs'] = []
        if self.mini_docs is not None:
            for k1 in self.mini_docs:
                result['MiniDocs'].append(k1.to_map() if k1 else None)

        result['OutlineList'] = []
        if self.outline_list is not None:
            for k1 in self.outline_list:
                result['OutlineList'].append(k1.to_map() if k1 else None)

        result['Outlines'] = []
        if self.outlines is not None:
            for k1 in self.outlines:
                result['Outlines'].append(k1.to_map() if k1 else None)

        if self.prompt is not None:
            result['Prompt'] = self.prompt

        if self.prompt_mode is not None:
            result['PromptMode'] = self.prompt_mode

        result['SearchSources'] = []
        if self.search_sources is not None:
            for k1 in self.search_sources:
                result['SearchSources'].append(k1.to_map() if k1 else None)

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.source_trace_method is not None:
            result['SourceTraceMethod'] = self.source_trace_method

        if self.step is not None:
            result['Step'] = self.step

        result['Summarization'] = []
        if self.summarization is not None:
            for k1 in self.summarization:
                result['Summarization'].append(k1.to_map() if k1 else None)

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.use_search is not None:
            result['UseSearch'] = self.use_search

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        if self.writing_params is not None:
            result['WritingParams'] = self.writing_params

        if self.writing_scene is not None:
            result['WritingScene'] = self.writing_scene

        if self.writing_style is not None:
            result['WritingStyle'] = self.writing_style

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.articles = []
        if m.get('Articles') is not None:
            for k1 in m.get('Articles'):
                temp_model = main_models.RunWritingV2RequestArticles()
                self.articles.append(temp_model.from_map(k1))

        if m.get('DistributeWriting') is not None:
            self.distribute_writing = m.get('DistributeWriting')

        if m.get('GcNumberSize') is not None:
            self.gc_number_size = m.get('GcNumberSize')

        if m.get('GcNumberSizeTag') is not None:
            self.gc_number_size_tag = m.get('GcNumberSizeTag')

        if m.get('Keywords') is not None:
            self.keywords = m.get('Keywords')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        self.mini_docs = []
        if m.get('MiniDocs') is not None:
            for k1 in m.get('MiniDocs'):
                temp_model = main_models.RunWritingV2RequestMiniDocs()
                self.mini_docs.append(temp_model.from_map(k1))

        self.outline_list = []
        if m.get('OutlineList') is not None:
            for k1 in m.get('OutlineList'):
                temp_model = main_models.WritingOutline()
                self.outline_list.append(temp_model.from_map(k1))

        self.outlines = []
        if m.get('Outlines') is not None:
            for k1 in m.get('Outlines'):
                temp_model = main_models.RunWritingV2RequestOutlines()
                self.outlines.append(temp_model.from_map(k1))

        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')

        if m.get('PromptMode') is not None:
            self.prompt_mode = m.get('PromptMode')

        self.search_sources = []
        if m.get('SearchSources') is not None:
            for k1 in m.get('SearchSources'):
                temp_model = main_models.RunWritingV2RequestSearchSources()
                self.search_sources.append(temp_model.from_map(k1))

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('SourceTraceMethod') is not None:
            self.source_trace_method = m.get('SourceTraceMethod')

        if m.get('Step') is not None:
            self.step = m.get('Step')

        self.summarization = []
        if m.get('Summarization') is not None:
            for k1 in m.get('Summarization'):
                temp_model = main_models.RunWritingV2RequestSummarization()
                self.summarization.append(temp_model.from_map(k1))

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('UseSearch') is not None:
            self.use_search = m.get('UseSearch')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        if m.get('WritingParams') is not None:
            self.writing_params = m.get('WritingParams')

        if m.get('WritingScene') is not None:
            self.writing_scene = m.get('WritingScene')

        if m.get('WritingStyle') is not None:
            self.writing_style = m.get('WritingStyle')

        return self

class RunWritingV2RequestSummarization(DaraModel):
    def __init__(
        self,
        event: str = None,
        message: str = None,
    ):
        self.event = event
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event is not None:
            result['Event'] = self.event

        if self.message is not None:
            result['Message'] = self.message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Event') is not None:
            self.event = m.get('Event')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        return self

class RunWritingV2RequestSearchSources(DaraModel):
    def __init__(
        self,
        code: str = None,
        dataset_name: str = None,
        name: str = None,
    ):
        self.code = code
        self.dataset_name = dataset_name
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class RunWritingV2RequestOutlines(DaraModel):
    def __init__(
        self,
        articles: List[main_models.RunWritingV2RequestOutlinesArticles] = None,
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
                temp_model = main_models.RunWritingV2RequestOutlinesArticles()
                self.articles.append(temp_model.from_map(k1))

        if m.get('Outline') is not None:
            self.outline = m.get('Outline')

        return self

class RunWritingV2RequestOutlinesArticles(DaraModel):
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

class RunWritingV2RequestMiniDocs(DaraModel):
    def __init__(
        self,
        content: str = None,
        index: str = None,
        star: bool = None,
    ):
        self.content = content
        self.index = index
        self.star = star

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.index is not None:
            result['Index'] = self.index

        if self.star is not None:
            result['Star'] = self.star

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Index') is not None:
            self.index = m.get('Index')

        if m.get('Star') is not None:
            self.star = m.get('Star')

        return self

class RunWritingV2RequestArticles(DaraModel):
    def __init__(
        self,
        content: str = None,
        pub_time: str = None,
        search_source_name: str = None,
        source: str = None,
        title: str = None,
        url: str = None,
    ):
        self.content = content
        self.pub_time = pub_time
        self.search_source_name = search_source_name
        self.source = source
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

        if self.pub_time is not None:
            result['PubTime'] = self.pub_time

        if self.search_source_name is not None:
            result['SearchSourceName'] = self.search_source_name

        if self.source is not None:
            result['Source'] = self.source

        if self.title is not None:
            result['Title'] = self.title

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('PubTime') is not None:
            self.pub_time = m.get('PubTime')

        if m.get('SearchSourceName') is not None:
            self.search_source_name = m.get('SearchSourceName')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

