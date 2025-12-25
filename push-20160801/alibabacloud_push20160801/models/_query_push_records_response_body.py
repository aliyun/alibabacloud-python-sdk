# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_push20160801 import models as main_models
from darabonba.model import DaraModel

class QueryPushRecordsResponseBody(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        page: int = None,
        page_size: int = None,
        push_infos: main_models.QueryPushRecordsResponseBodyPushInfos = None,
        request_id: str = None,
        total: int = None,
    ):
        self.next_token = next_token
        self.page = page
        self.page_size = page_size
        self.push_infos = push_infos
        self.request_id = request_id
        self.total = total

    def validate(self):
        if self.push_infos:
            self.push_infos.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page is not None:
            result['Page'] = self.page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.push_infos is not None:
            result['PushInfos'] = self.push_infos.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PushInfos') is not None:
            temp_model = main_models.QueryPushRecordsResponseBodyPushInfos()
            self.push_infos = temp_model.from_map(m.get('PushInfos'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class QueryPushRecordsResponseBodyPushInfos(DaraModel):
    def __init__(
        self,
        push_info: List[main_models.QueryPushRecordsResponseBodyPushInfosPushInfo] = None,
    ):
        self.push_info = push_info

    def validate(self):
        if self.push_info:
            for v1 in self.push_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PushInfo'] = []
        if self.push_info is not None:
            for k1 in self.push_info:
                result['PushInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.push_info = []
        if m.get('PushInfo') is not None:
            for k1 in m.get('PushInfo'):
                temp_model = main_models.QueryPushRecordsResponseBodyPushInfosPushInfo()
                self.push_info.append(temp_model.from_map(k1))

        return self

class QueryPushRecordsResponseBodyPushInfosPushInfo(DaraModel):
    def __init__(
        self,
        app_key: int = None,
        body: str = None,
        device_type: str = None,
        message_id: str = None,
        push_time: str = None,
        push_type: str = None,
        source: str = None,
        status: str = None,
        target: str = None,
        title: str = None,
    ):
        self.app_key = app_key
        self.body = body
        self.device_type = device_type
        self.message_id = message_id
        self.push_time = push_time
        self.push_type = push_type
        self.source = source
        self.status = status
        self.target = target
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_key is not None:
            result['AppKey'] = self.app_key

        if self.body is not None:
            result['Body'] = self.body

        if self.device_type is not None:
            result['DeviceType'] = self.device_type

        if self.message_id is not None:
            result['MessageId'] = self.message_id

        if self.push_time is not None:
            result['PushTime'] = self.push_time

        if self.push_type is not None:
            result['PushType'] = self.push_type

        if self.source is not None:
            result['Source'] = self.source

        if self.status is not None:
            result['Status'] = self.status

        if self.target is not None:
            result['Target'] = self.target

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')

        if m.get('Body') is not None:
            self.body = m.get('Body')

        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')

        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')

        if m.get('PushTime') is not None:
            self.push_time = m.get('PushTime')

        if m.get('PushType') is not None:
            self.push_type = m.get('PushType')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Target') is not None:
            self.target = m.get('Target')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

