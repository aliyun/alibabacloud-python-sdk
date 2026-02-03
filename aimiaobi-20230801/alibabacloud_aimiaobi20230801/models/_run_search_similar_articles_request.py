# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class RunSearchSimilarArticlesRequest(DaraModel):
    def __init__(
        self,
        chat_config: main_models.RunSearchSimilarArticlesRequestChatConfig = None,
        doc_type: str = None,
        title: str = None,
        url: str = None,
        workspace_id: str = None,
    ):
        self.chat_config = chat_config
        self.doc_type = doc_type
        self.title = title
        # This parameter is required.
        self.url = url
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        if self.chat_config:
            self.chat_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.chat_config is not None:
            result['ChatConfig'] = self.chat_config.to_map()

        if self.doc_type is not None:
            result['DocType'] = self.doc_type

        if self.title is not None:
            result['Title'] = self.title

        if self.url is not None:
            result['Url'] = self.url

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChatConfig') is not None:
            temp_model = main_models.RunSearchSimilarArticlesRequestChatConfig()
            self.chat_config = temp_model.from_map(m.get('ChatConfig'))

        if m.get('DocType') is not None:
            self.doc_type = m.get('DocType')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

class RunSearchSimilarArticlesRequestChatConfig(DaraModel):
    def __init__(
        self,
        search_param: main_models.RunSearchSimilarArticlesRequestChatConfigSearchParam = None,
    ):
        self.search_param = search_param

    def validate(self):
        if self.search_param:
            self.search_param.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.search_param is not None:
            result['SearchParam'] = self.search_param.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SearchParam') is not None:
            temp_model = main_models.RunSearchSimilarArticlesRequestChatConfigSearchParam()
            self.search_param = temp_model.from_map(m.get('SearchParam'))

        return self

class RunSearchSimilarArticlesRequestChatConfigSearchParam(DaraModel):
    def __init__(
        self,
        category_uuids: List[str] = None,
        create_time_end: int = None,
        create_time_start: int = None,
        doc_ids: List[str] = None,
        doc_types: List[str] = None,
        doc_uuids: List[str] = None,
        end_time: int = None,
        extend_1: str = None,
        extend_2: str = None,
        extend_3: str = None,
        search_sources: List[main_models.RunSearchSimilarArticlesRequestChatConfigSearchParamSearchSources] = None,
        start_time: int = None,
        tags: List[str] = None,
    ):
        self.category_uuids = category_uuids
        self.create_time_end = create_time_end
        self.create_time_start = create_time_start
        self.doc_ids = doc_ids
        self.doc_types = doc_types
        self.doc_uuids = doc_uuids
        self.end_time = end_time
        self.extend_1 = extend_1
        self.extend_2 = extend_2
        self.extend_3 = extend_3
        self.search_sources = search_sources
        self.start_time = start_time
        self.tags = tags

    def validate(self):
        if self.search_sources:
            for v1 in self.search_sources:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_uuids is not None:
            result['CategoryUuids'] = self.category_uuids

        if self.create_time_end is not None:
            result['CreateTimeEnd'] = self.create_time_end

        if self.create_time_start is not None:
            result['CreateTimeStart'] = self.create_time_start

        if self.doc_ids is not None:
            result['DocIds'] = self.doc_ids

        if self.doc_types is not None:
            result['DocTypes'] = self.doc_types

        if self.doc_uuids is not None:
            result['DocUuids'] = self.doc_uuids

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.extend_1 is not None:
            result['Extend1'] = self.extend_1

        if self.extend_2 is not None:
            result['Extend2'] = self.extend_2

        if self.extend_3 is not None:
            result['Extend3'] = self.extend_3

        result['SearchSources'] = []
        if self.search_sources is not None:
            for k1 in self.search_sources:
                result['SearchSources'].append(k1.to_map() if k1 else None)

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.tags is not None:
            result['Tags'] = self.tags

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryUuids') is not None:
            self.category_uuids = m.get('CategoryUuids')

        if m.get('CreateTimeEnd') is not None:
            self.create_time_end = m.get('CreateTimeEnd')

        if m.get('CreateTimeStart') is not None:
            self.create_time_start = m.get('CreateTimeStart')

        if m.get('DocIds') is not None:
            self.doc_ids = m.get('DocIds')

        if m.get('DocTypes') is not None:
            self.doc_types = m.get('DocTypes')

        if m.get('DocUuids') is not None:
            self.doc_uuids = m.get('DocUuids')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Extend1') is not None:
            self.extend_1 = m.get('Extend1')

        if m.get('Extend2') is not None:
            self.extend_2 = m.get('Extend2')

        if m.get('Extend3') is not None:
            self.extend_3 = m.get('Extend3')

        self.search_sources = []
        if m.get('SearchSources') is not None:
            for k1 in m.get('SearchSources'):
                temp_model = main_models.RunSearchSimilarArticlesRequestChatConfigSearchParamSearchSources()
                self.search_sources.append(temp_model.from_map(k1))

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        return self

class RunSearchSimilarArticlesRequestChatConfigSearchParamSearchSources(DaraModel):
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

