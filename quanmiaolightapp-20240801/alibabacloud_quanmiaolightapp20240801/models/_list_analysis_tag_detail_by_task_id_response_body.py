# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_quanmiaolightapp20240801 import models as main_models
from darabonba.model import DaraModel

class ListAnalysisTagDetailByTaskIdResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.ListAnalysisTagDetailByTaskIdResponseBodyData] = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.data = data
        self.max_results = max_results
        self.message = message
        # This parameter is required.
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        result['data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['data'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.message is not None:
            result['message'] = self.message

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.ListAnalysisTagDetailByTaskIdResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListAnalysisTagDetailByTaskIdResponseBodyData(DaraModel):
    def __init__(
        self,
        content: str = None,
        content_tags: List[main_models.ListAnalysisTagDetailByTaskIdResponseBodyDataContentTags] = None,
        origin_response: str = None,
        source_list: List[str] = None,
    ):
        self.content = content
        self.content_tags = content_tags
        self.origin_response = origin_response
        self.source_list = source_list

    def validate(self):
        if self.content_tags:
            for v1 in self.content_tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        result['contentTags'] = []
        if self.content_tags is not None:
            for k1 in self.content_tags:
                result['contentTags'].append(k1.to_map() if k1 else None)

        if self.origin_response is not None:
            result['originResponse'] = self.origin_response

        if self.source_list is not None:
            result['sourceList'] = self.source_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        self.content_tags = []
        if m.get('contentTags') is not None:
            for k1 in m.get('contentTags'):
                temp_model = main_models.ListAnalysisTagDetailByTaskIdResponseBodyDataContentTags()
                self.content_tags.append(temp_model.from_map(k1))

        if m.get('originResponse') is not None:
            self.origin_response = m.get('originResponse')

        if m.get('sourceList') is not None:
            self.source_list = m.get('sourceList')

        return self

class ListAnalysisTagDetailByTaskIdResponseBodyDataContentTags(DaraModel):
    def __init__(
        self,
        tag_name: str = None,
        tags: List[str] = None,
    ):
        self.tag_name = tag_name
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_name is not None:
            result['tagName'] = self.tag_name

        if self.tags is not None:
            result['tags'] = self.tags

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tagName') is not None:
            self.tag_name = m.get('tagName')

        if m.get('tags') is not None:
            self.tags = m.get('tags')

        return self

