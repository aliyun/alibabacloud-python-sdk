# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_xtee20210910 import models as main_models
from darabonba.model import DaraModel

class DescribeEventPageListResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        current_page: int = None,
        page_size: int = None,
        result_object: List[main_models.DescribeEventPageListResponseBodyResultObject] = None,
        total_item: int = None,
        total_page: int = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Current page number.
        self.current_page = current_page
        # Page size, with a default value of 10
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
                temp_model = main_models.DescribeEventPageListResponseBodyResultObject()
                self.result_object.append(temp_model.from_map(k1))

        if m.get('totalItem') is not None:
            self.total_item = m.get('totalItem')

        if m.get('totalPage') is not None:
            self.total_page = m.get('totalPage')

        return self

class DescribeEventPageListResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        children: List[main_models.DescribeEventPageListResponseBodyResultObjectChildren] = None,
        event_code: str = None,
        event_name: str = None,
        event_status: str = None,
        event_type: str = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        id: int = None,
        rule_count: int = None,
        template_code: str = None,
        template_name: str = None,
        template_type: str = None,
        user_count: int = None,
    ):
        # Object
        self.children = children
        # Event code
        self.event_code = event_code
        # Event name.
        self.event_name = event_name
        # Event status.
        self.event_status = event_status
        # Event type.
        self.event_type = event_type
        # Creation time.
        self.gmt_create = gmt_create
        # Modification time
        self.gmt_modified = gmt_modified
        # Database ID.
        self.id = id
        # Total number of rules.
        self.rule_count = rule_count
        # Template code
        self.template_code = template_code
        # Template name.
        self.template_name = template_name
        # Template type
        self.template_type = template_type
        # Number of customer authorizations
        self.user_count = user_count

    def validate(self):
        if self.children:
            for v1 in self.children:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['children'] = []
        if self.children is not None:
            for k1 in self.children:
                result['children'].append(k1.to_map() if k1 else None)

        if self.event_code is not None:
            result['eventCode'] = self.event_code

        if self.event_name is not None:
            result['eventName'] = self.event_name

        if self.event_status is not None:
            result['eventStatus'] = self.event_status

        if self.event_type is not None:
            result['eventType'] = self.event_type

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.id is not None:
            result['id'] = self.id

        if self.rule_count is not None:
            result['ruleCount'] = self.rule_count

        if self.template_code is not None:
            result['templateCode'] = self.template_code

        if self.template_name is not None:
            result['templateName'] = self.template_name

        if self.template_type is not None:
            result['templateType'] = self.template_type

        if self.user_count is not None:
            result['userCount'] = self.user_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.children = []
        if m.get('children') is not None:
            for k1 in m.get('children'):
                temp_model = main_models.DescribeEventPageListResponseBodyResultObjectChildren()
                self.children.append(temp_model.from_map(k1))

        if m.get('eventCode') is not None:
            self.event_code = m.get('eventCode')

        if m.get('eventName') is not None:
            self.event_name = m.get('eventName')

        if m.get('eventStatus') is not None:
            self.event_status = m.get('eventStatus')

        if m.get('eventType') is not None:
            self.event_type = m.get('eventType')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('ruleCount') is not None:
            self.rule_count = m.get('ruleCount')

        if m.get('templateCode') is not None:
            self.template_code = m.get('templateCode')

        if m.get('templateName') is not None:
            self.template_name = m.get('templateName')

        if m.get('templateType') is not None:
            self.template_type = m.get('templateType')

        if m.get('userCount') is not None:
            self.user_count = m.get('userCount')

        return self

class DescribeEventPageListResponseBodyResultObjectChildren(DaraModel):
    def __init__(
        self,
        event_code: str = None,
        event_name: str = None,
        event_status: str = None,
        event_type: str = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        id: int = None,
        rule_count: int = None,
    ):
        # Event code.
        self.event_code = event_code
        # Event name.
        self.event_name = event_name
        # Event status.
        self.event_status = event_status
        # Event type.
        self.event_type = event_type
        # Creation time.
        self.gmt_create = gmt_create
        # Modification time
        self.gmt_modified = gmt_modified
        # Primary key ID
        self.id = id
        # Total number of rules.
        self.rule_count = rule_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_code is not None:
            result['eventCode'] = self.event_code

        if self.event_name is not None:
            result['eventName'] = self.event_name

        if self.event_status is not None:
            result['eventStatus'] = self.event_status

        if self.event_type is not None:
            result['eventType'] = self.event_type

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.id is not None:
            result['id'] = self.id

        if self.rule_count is not None:
            result['ruleCount'] = self.rule_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('eventCode') is not None:
            self.event_code = m.get('eventCode')

        if m.get('eventName') is not None:
            self.event_name = m.get('eventName')

        if m.get('eventStatus') is not None:
            self.event_status = m.get('eventStatus')

        if m.get('eventType') is not None:
            self.event_type = m.get('eventType')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('ruleCount') is not None:
            self.rule_count = m.get('ruleCount')

        return self

