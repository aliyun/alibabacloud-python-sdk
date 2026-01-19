# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_xtee20210910 import models as main_models
from darabonba.model import DaraModel

class DescribeEventLogPageResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        current_page: int = None,
        page_size: int = None,
        result_object: List[main_models.DescribeEventLogPageResponseBodyResultObject] = None,
        total_item: int = None,
        total_page: int = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Current page number.
        self.current_page = current_page
        # Page size, default value is 10.
        self.page_size = page_size
        # Returned object.
        self.result_object = result_object
        # Total number of items.
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
                temp_model = main_models.DescribeEventLogPageResponseBodyResultObject()
                self.result_object.append(temp_model.from_map(k1))

        if m.get('totalItem') is not None:
            self.total_item = m.get('totalItem')

        if m.get('totalPage') is not None:
            self.total_page = m.get('totalPage')

        return self

class DescribeEventLogPageResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        email: str = None,
        ip: str = None,
        mobile: str = None,
        nick_name: str = None,
        request_id: str = None,
        score: str = None,
        service: str = None,
        tags: str = None,
        timestamp: str = None,
        umid: str = None,
    ):
        # Account ID.
        self.account_id = account_id
        # Email.
        self.email = email
        # IP address.
        self.ip = ip
        # Mobile phone number.
        self.mobile = mobile
        # Nickname.
        self.nick_name = nick_name
        # Request ID.
        self.request_id = request_id
        # Score.
        self.score = score
        # Event name.
        self.service = service
        # Tags.
        self.tags = tags
        # Transaction time.
        self.timestamp = timestamp
        # Device ID.
        self.umid = umid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['accountId'] = self.account_id

        if self.email is not None:
            result['email'] = self.email

        if self.ip is not None:
            result['ip'] = self.ip

        if self.mobile is not None:
            result['mobile'] = self.mobile

        if self.nick_name is not None:
            result['nickName'] = self.nick_name

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.score is not None:
            result['score'] = self.score

        if self.service is not None:
            result['service'] = self.service

        if self.tags is not None:
            result['tags'] = self.tags

        if self.timestamp is not None:
            result['timestamp'] = self.timestamp

        if self.umid is not None:
            result['umid'] = self.umid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')

        if m.get('email') is not None:
            self.email = m.get('email')

        if m.get('ip') is not None:
            self.ip = m.get('ip')

        if m.get('mobile') is not None:
            self.mobile = m.get('mobile')

        if m.get('nickName') is not None:
            self.nick_name = m.get('nickName')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('score') is not None:
            self.score = m.get('score')

        if m.get('service') is not None:
            self.service = m.get('service')

        if m.get('tags') is not None:
            self.tags = m.get('tags')

        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')

        if m.get('umid') is not None:
            self.umid = m.get('umid')

        return self

