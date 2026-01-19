# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_xtee20210910 import models as main_models
from darabonba.model import DaraModel

class DescribeSceneAllEventNameCodeListResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: str = None,
        message: str = None,
        request_id: str = None,
        result_object: List[main_models.DescribeSceneAllEventNameCodeListResponseBodyResultObject] = None,
        success: bool = None,
    ):
        # Status code
        self.code = code
        # HTTP status code
        self.http_status_code = http_status_code
        # Error details
        self.message = message
        # Request ID, which is unique for each request, facilitating subsequent troubleshooting
        self.request_id = request_id
        # Returned object
        self.result_object = result_object
        # Indicates whether the operation was successful, where true means success.
        self.success = success

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
        if self.code is not None:
            result['code'] = self.code

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        result['resultObject'] = []
        if self.result_object is not None:
            for k1 in self.result_object:
                result['resultObject'].append(k1.to_map() if k1 else None)

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.result_object = []
        if m.get('resultObject') is not None:
            for k1 in m.get('resultObject'):
                temp_model = main_models.DescribeSceneAllEventNameCodeListResponseBodyResultObject()
                self.result_object.append(temp_model.from_map(k1))

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class DescribeSceneAllEventNameCodeListResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        children: List[main_models.DescribeSceneAllEventNameCodeListResponseBodyResultObjectChildren] = None,
        create_type: str = None,
        event_code: str = None,
        event_name: str = None,
        event_type: str = None,
    ):
        # Child objects
        self.children = children
        # Creation type
        self.create_type = create_type
        # Event code
        self.event_code = event_code
        # Event name.
        self.event_name = event_name
        # Event type
        self.event_type = event_type

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

        if self.create_type is not None:
            result['createType'] = self.create_type

        if self.event_code is not None:
            result['eventCode'] = self.event_code

        if self.event_name is not None:
            result['eventName'] = self.event_name

        if self.event_type is not None:
            result['eventType'] = self.event_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.children = []
        if m.get('children') is not None:
            for k1 in m.get('children'):
                temp_model = main_models.DescribeSceneAllEventNameCodeListResponseBodyResultObjectChildren()
                self.children.append(temp_model.from_map(k1))

        if m.get('createType') is not None:
            self.create_type = m.get('createType')

        if m.get('eventCode') is not None:
            self.event_code = m.get('eventCode')

        if m.get('eventName') is not None:
            self.event_name = m.get('eventName')

        if m.get('eventType') is not None:
            self.event_type = m.get('eventType')

        return self

class DescribeSceneAllEventNameCodeListResponseBodyResultObjectChildren(DaraModel):
    def __init__(
        self,
        create_type: str = None,
        event_code: str = None,
        event_name: str = None,
        event_type: str = None,
    ):
        # Creation type
        self.create_type = create_type
        # Event code
        self.event_code = event_code
        # Event name.
        self.event_name = event_name
        # Event type
        self.event_type = event_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_type is not None:
            result['createType'] = self.create_type

        if self.event_code is not None:
            result['eventCode'] = self.event_code

        if self.event_name is not None:
            result['eventName'] = self.event_name

        if self.event_type is not None:
            result['eventType'] = self.event_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createType') is not None:
            self.create_type = m.get('createType')

        if m.get('eventCode') is not None:
            self.event_code = m.get('eventCode')

        if m.get('eventName') is not None:
            self.event_name = m.get('eventName')

        if m.get('eventType') is not None:
            self.event_type = m.get('eventType')

        return self

