# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rocketmq20220801 import models as main_models
from darabonba.model import DaraModel

class ListTracesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListTracesResponseBodyData = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code.
        self.code = code
        # The returned result.
        self.data = data
        # The dynamic error code.
        self.dynamic_code = dynamic_code
        # The dynamic error message.
        self.dynamic_message = dynamic_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The error message.
        self.message = message
        # Id of the request
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.dynamic_code is not None:
            result['dynamicCode'] = self.dynamic_code

        if self.dynamic_message is not None:
            result['dynamicMessage'] = self.dynamic_message

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.ListTracesResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('dynamicCode') is not None:
            self.dynamic_code = m.get('dynamicCode')

        if m.get('dynamicMessage') is not None:
            self.dynamic_message = m.get('dynamicMessage')

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class ListTracesResponseBodyData(DaraModel):
    def __init__(
        self,
        list: List[main_models.ListTracesResponseBodyDataList] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # Trace list.
        self.list = list
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The total number of returned entries.
        self.total_count = total_count

    def validate(self):
        if self.list:
            for v1 in self.list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['list'] = []
        if self.list is not None:
            for k1 in self.list:
                result['list'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k1 in m.get('list'):
                temp_model = main_models.ListTracesResponseBodyDataList()
                self.list.append(temp_model.from_map(k1))

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListTracesResponseBodyDataList(DaraModel):
    def __init__(
        self,
        born_time: str = None,
        instance_id: str = None,
        message_id: str = None,
        message_keys: List[str] = None,
        message_tag: str = None,
        region_id: str = None,
        topic_name: str = None,
    ):
        # Message born time.
        self.born_time = born_time
        # The instance ID.
        self.instance_id = instance_id
        # Message id.
        self.message_id = message_id
        # Message keys.
        self.message_keys = message_keys
        # Message tag.
        self.message_tag = message_tag
        # The region ID.
        self.region_id = region_id
        # The name of the topic.
        self.topic_name = topic_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.born_time is not None:
            result['bornTime'] = self.born_time

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.message_id is not None:
            result['messageId'] = self.message_id

        if self.message_keys is not None:
            result['messageKeys'] = self.message_keys

        if self.message_tag is not None:
            result['messageTag'] = self.message_tag

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.topic_name is not None:
            result['topicName'] = self.topic_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bornTime') is not None:
            self.born_time = m.get('bornTime')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('messageId') is not None:
            self.message_id = m.get('messageId')

        if m.get('messageKeys') is not None:
            self.message_keys = m.get('messageKeys')

        if m.get('messageTag') is not None:
            self.message_tag = m.get('messageTag')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('topicName') is not None:
            self.topic_name = m.get('topicName')

        return self

