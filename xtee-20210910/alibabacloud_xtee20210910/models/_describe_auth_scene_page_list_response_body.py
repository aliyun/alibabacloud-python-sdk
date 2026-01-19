# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_xtee20210910 import models as main_models
from darabonba.model import DaraModel

class DescribeAuthScenePageListResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        current_page: int = None,
        page_size: int = None,
        result_object: List[main_models.DescribeAuthScenePageListResponseBodyResultObject] = None,
        total_item: int = None,
        total_page: int = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Current page number.
        self.current_page = current_page
        # Page size, default value is 10
        self.page_size = page_size
        # Returned object
        self.result_object = result_object
        # Total number of items
        self.total_item = total_item
        # Total number of pages.
        self.total_page = total_page

    def validate(self):
        if self.result_object:
            for v1 in self.result_object:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.current_page is not None:
            result['currentPage'] = self.current_page

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        result['resultObject'] = []
        if self.result_object is not None:
            for k1 in self.result_object:
                result['resultObject'].append(k1.to_map() if k1 else None)

        if self.total_item is not None:
            result['totalItem'] = self.total_item

        if self.total_page is not None:
            result['totalPage'] = self.total_page

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        self.result_object = []
        if m.get('resultObject') is not None:
            for k1 in m.get('resultObject'):
                temp_model = main_models.DescribeAuthScenePageListResponseBodyResultObject()
                self.result_object.append(temp_model.from_map(k1))

        if m.get('totalItem') is not None:
            self.total_item = m.get('totalItem')

        if m.get('totalPage') is not None:
            self.total_page = m.get('totalPage')

        return self

class DescribeAuthScenePageListResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        common_rule_count: int = None,
        custom_rule_count: int = None,
        event_code: str = None,
        scene_name: str = None,
        server_name: str = None,
    ):
        # Number of common rules
        self.common_rule_count = common_rule_count
        # Number of custom rules
        self.custom_rule_count = custom_rule_count
        # Event code
        self.event_code = event_code
        # Scene name.
        self.scene_name = scene_name
        # Service name.
        self.server_name = server_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.common_rule_count is not None:
            result['commonRuleCount'] = self.common_rule_count

        if self.custom_rule_count is not None:
            result['customRuleCount'] = self.custom_rule_count

        if self.event_code is not None:
            result['eventCode'] = self.event_code

        if self.scene_name is not None:
            result['sceneName'] = self.scene_name

        if self.server_name is not None:
            result['serverName'] = self.server_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonRuleCount') is not None:
            self.common_rule_count = m.get('commonRuleCount')

        if m.get('customRuleCount') is not None:
            self.custom_rule_count = m.get('customRuleCount')

        if m.get('eventCode') is not None:
            self.event_code = m.get('eventCode')

        if m.get('sceneName') is not None:
            self.scene_name = m.get('sceneName')

        if m.get('serverName') is not None:
            self.server_name = m.get('serverName')

        return self

