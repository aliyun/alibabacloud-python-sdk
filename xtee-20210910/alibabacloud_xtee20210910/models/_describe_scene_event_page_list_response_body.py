# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_xtee20210910 import models as main_models
from darabonba.model import DaraModel

class DescribeSceneEventPageListResponseBody(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        request_id: str = None,
        result_object: List[main_models.DescribeSceneEventPageListResponseBodyResultObject] = None,
        total_item: int = None,
        total_page: int = None,
    ):
        # Current page number.
        self.current_page = current_page
        # Number of items per page. Default value: 20, minimum value: 1, maximum value: 50.
        self.page_size = page_size
        # Request ID, each request has a unique value, which facilitates subsequent troubleshooting
        self.request_id = request_id
        # Return array
        self.result_object = result_object
        # Total number of items
        self.total_item = total_item
        # Total number of pages
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
        if self.current_page is not None:
            result['currentPage'] = self.current_page

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.request_id is not None:
            result['requestId'] = self.request_id

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
        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.result_object = []
        if m.get('resultObject') is not None:
            for k1 in m.get('resultObject'):
                temp_model = main_models.DescribeSceneEventPageListResponseBodyResultObject()
                self.result_object.append(temp_model.from_map(k1))

        if m.get('totalItem') is not None:
            self.total_item = m.get('totalItem')

        if m.get('totalPage') is not None:
            self.total_page = m.get('totalPage')

        return self

class DescribeSceneEventPageListResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        common_rule_count: str = None,
        custom_rule_count: str = None,
        event_code: str = None,
        event_name: str = None,
        gmt_modified: str = None,
        modifier: str = None,
        normal_rule_count: str = None,
        service: str = None,
        use_status: str = None,
        white_box_rule_count: str = None,
    ):
        # Number of common rules
        self.common_rule_count = common_rule_count
        # Number of custom rules
        self.custom_rule_count = custom_rule_count
        # Event code
        self.event_code = event_code
        # Event name.
        self.event_name = event_name
        # Modification time
        self.gmt_modified = gmt_modified
        # Modifier
        self.modifier = modifier
        # Number of custom rules
        self.normal_rule_count = normal_rule_count
        # Service code
        self.service = service
        # Usage status
        self.use_status = use_status
        # Number of white-box rules
        self.white_box_rule_count = white_box_rule_count

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

        if self.event_name is not None:
            result['eventName'] = self.event_name

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.modifier is not None:
            result['modifier'] = self.modifier

        if self.normal_rule_count is not None:
            result['normalRuleCount'] = self.normal_rule_count

        if self.service is not None:
            result['service'] = self.service

        if self.use_status is not None:
            result['useStatus'] = self.use_status

        if self.white_box_rule_count is not None:
            result['whiteBoxRuleCount'] = self.white_box_rule_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonRuleCount') is not None:
            self.common_rule_count = m.get('commonRuleCount')

        if m.get('customRuleCount') is not None:
            self.custom_rule_count = m.get('customRuleCount')

        if m.get('eventCode') is not None:
            self.event_code = m.get('eventCode')

        if m.get('eventName') is not None:
            self.event_name = m.get('eventName')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('modifier') is not None:
            self.modifier = m.get('modifier')

        if m.get('normalRuleCount') is not None:
            self.normal_rule_count = m.get('normalRuleCount')

        if m.get('service') is not None:
            self.service = m.get('service')

        if m.get('useStatus') is not None:
            self.use_status = m.get('useStatus')

        if m.get('whiteBoxRuleCount') is not None:
            self.white_box_rule_count = m.get('whiteBoxRuleCount')

        return self

