# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_iqs20241111 import models as main_models
from darabonba.model import DaraModel

class GenericSearchResult(DaraModel):
    def __init__(
        self,
        page_items: List[main_models.ScorePageItem] = None,
        query_context: main_models.QueryContext = None,
        request_id: str = None,
        scene_items: List[main_models.SceneItem] = None,
        search_information: main_models.SearchInformation = None,
        weibo_items: List[main_models.WeiboItem] = None,
    ):
        self.page_items = page_items
        self.query_context = query_context
        self.request_id = request_id
        self.scene_items = scene_items
        self.search_information = search_information
        self.weibo_items = weibo_items

    def validate(self):
        if self.page_items:
            for v1 in self.page_items:
                 if v1:
                    v1.validate()
        if self.query_context:
            self.query_context.validate()
        if self.scene_items:
            for v1 in self.scene_items:
                 if v1:
                    v1.validate()
        if self.search_information:
            self.search_information.validate()
        if self.weibo_items:
            for v1 in self.weibo_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['pageItems'] = []
        if self.page_items is not None:
            for k1 in self.page_items:
                result['pageItems'].append(k1.to_map() if k1 else None)

        if self.query_context is not None:
            result['queryContext'] = self.query_context.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        result['sceneItems'] = []
        if self.scene_items is not None:
            for k1 in self.scene_items:
                result['sceneItems'].append(k1.to_map() if k1 else None)

        if self.search_information is not None:
            result['searchInformation'] = self.search_information.to_map()

        result['weiboItems'] = []
        if self.weibo_items is not None:
            for k1 in self.weibo_items:
                result['weiboItems'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.page_items = []
        if m.get('pageItems') is not None:
            for k1 in m.get('pageItems'):
                temp_model = main_models.ScorePageItem()
                self.page_items.append(temp_model.from_map(k1))

        if m.get('queryContext') is not None:
            temp_model = main_models.QueryContext()
            self.query_context = temp_model.from_map(m.get('queryContext'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.scene_items = []
        if m.get('sceneItems') is not None:
            for k1 in m.get('sceneItems'):
                temp_model = main_models.SceneItem()
                self.scene_items.append(temp_model.from_map(k1))

        if m.get('searchInformation') is not None:
            temp_model = main_models.SearchInformation()
            self.search_information = temp_model.from_map(m.get('searchInformation'))

        self.weibo_items = []
        if m.get('weiboItems') is not None:
            for k1 in m.get('weiboItems'):
                temp_model = main_models.WeiboItem()
                self.weibo_items.append(temp_model.from_map(k1))

        return self

