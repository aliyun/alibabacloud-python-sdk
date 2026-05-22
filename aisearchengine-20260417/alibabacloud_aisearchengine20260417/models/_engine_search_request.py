# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aisearchengine20260417 import models as main_models
from darabonba.model import DaraModel

class EngineSearchRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        grey: bool = None,
        query: main_models.EngineSearchRequestQuery = None,
        recall: main_models.EngineSearchRequestRecall = None,
        session_id: str = None,
        strategy_id: str = None,
        user: main_models.EngineSearchRequestUser = None,
        version: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        self.grey = grey
        # This parameter is required.
        self.query = query
        self.recall = recall
        self.session_id = session_id
        self.strategy_id = strategy_id
        self.user = user
        self.version = version

    def validate(self):
        if self.query:
            self.query.validate()
        if self.recall:
            self.recall.validate()
        if self.user:
            self.user.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['appId'] = self.app_id

        if self.grey is not None:
            result['grey'] = self.grey

        if self.query is not None:
            result['query'] = self.query.to_map()

        if self.recall is not None:
            result['recall'] = self.recall.to_map()

        if self.session_id is not None:
            result['sessionId'] = self.session_id

        if self.strategy_id is not None:
            result['strategyId'] = self.strategy_id

        if self.user is not None:
            result['user'] = self.user.to_map()

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')

        if m.get('grey') is not None:
            self.grey = m.get('grey')

        if m.get('query') is not None:
            temp_model = main_models.EngineSearchRequestQuery()
            self.query = temp_model.from_map(m.get('query'))

        if m.get('recall') is not None:
            temp_model = main_models.EngineSearchRequestRecall()
            self.recall = temp_model.from_map(m.get('recall'))

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        if m.get('strategyId') is not None:
            self.strategy_id = m.get('strategyId')

        if m.get('user') is not None:
            temp_model = main_models.EngineSearchRequestUser()
            self.user = temp_model.from_map(m.get('user'))

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

class EngineSearchRequestUser(DaraModel):
    def __init__(
        self,
        user_id: str = None,
    ):
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.user_id is not None:
            result['userId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        return self

class EngineSearchRequestRecall(DaraModel):
    def __init__(
        self,
        close_recall_asr: bool = None,
        need_merge_segments: bool = None,
    ):
        self.close_recall_asr = close_recall_asr
        self.need_merge_segments = need_merge_segments

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.close_recall_asr is not None:
            result['closeRecallAsr'] = self.close_recall_asr

        if self.need_merge_segments is not None:
            result['needMergeSegments'] = self.need_merge_segments

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('closeRecallAsr') is not None:
            self.close_recall_asr = m.get('closeRecallAsr')

        if m.get('needMergeSegments') is not None:
            self.need_merge_segments = m.get('needMergeSegments')

        return self



class EngineSearchRequestQuery(DaraModel):
    def __init__(
        self,
        exclude_ids: List[str] = None,
        image_urls: List[str] = None,
        page_no: int = None,
        page_size: int = None,
        texts: List[str] = None,
    ):
        self.exclude_ids = exclude_ids
        self.image_urls = image_urls
        self.page_no = page_no
        self.page_size = page_size
        self.texts = texts

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.exclude_ids is not None:
            result['excludeIds'] = self.exclude_ids

        if self.image_urls is not None:
            result['imageUrls'] = self.image_urls

        if self.page_no is not None:
            result['pageNo'] = self.page_no

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.texts is not None:
            result['texts'] = self.texts

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('excludeIds') is not None:
            self.exclude_ids = m.get('excludeIds')

        if m.get('imageUrls') is not None:
            self.image_urls = m.get('imageUrls')

        if m.get('pageNo') is not None:
            self.page_no = m.get('pageNo')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('texts') is not None:
            self.texts = m.get('texts')

        return self

