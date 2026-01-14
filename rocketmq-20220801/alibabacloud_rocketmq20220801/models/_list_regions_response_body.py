# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_rocketmq20220801 import models as main_models
from darabonba.model import DaraModel

class ListRegionsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.ListRegionsResponseBodyData] = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code.
        self.code = code
        # The returned data.
        self.data = data
        # The dynamic error code.
        self.dynamic_code = dynamic_code
        # The dynamic error message.
        self.dynamic_message = dynamic_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

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

        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.ListRegionsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

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

class ListRegionsResponseBodyData(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        region_id: str = None,
        region_name: str = None,
        support_rocketmq_v4: bool = None,
        support_rocketmq_v5: bool = None,
        tags: List[main_models.ListRegionsResponseBodyDataTags] = None,
        update_time: str = None,
    ):
        # The time when the ApsaraMQ for RocketMQ instance was created.
        self.create_time = create_time
        # The region ID.
        self.region_id = region_id
        # The region name.
        self.region_name = region_name
        # Indicates whether ApsaraMQ for RocketMQ V4 is activated.
        self.support_rocketmq_v4 = support_rocketmq_v4
        # Indicates whether ApsaraMQ for RocketMQ V5 is activated.
        self.support_rocketmq_v5 = support_rocketmq_v5
        # The region tags.
        self.tags = tags
        # The time when the ApsaraMQ for RocketMQ instance was last modified.
        self.update_time = update_time

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.region_name is not None:
            result['regionName'] = self.region_name

        if self.support_rocketmq_v4 is not None:
            result['supportRocketmqV4'] = self.support_rocketmq_v4

        if self.support_rocketmq_v5 is not None:
            result['supportRocketmqV5'] = self.support_rocketmq_v5

        result['tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['tags'].append(k1.to_map() if k1 else None)

        if self.update_time is not None:
            result['updateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('regionName') is not None:
            self.region_name = m.get('regionName')

        if m.get('supportRocketmqV4') is not None:
            self.support_rocketmq_v4 = m.get('supportRocketmqV4')

        if m.get('supportRocketmqV5') is not None:
            self.support_rocketmq_v5 = m.get('supportRocketmqV5')

        self.tags = []
        if m.get('tags') is not None:
            for k1 in m.get('tags'):
                temp_model = main_models.ListRegionsResponseBodyDataTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        return self

class ListRegionsResponseBodyDataTags(DaraModel):
    def __init__(
        self,
        tag_code: str = None,
        tag_value: Any = None,
    ):
        # The tag code.
        self.tag_code = tag_code
        # The tag value.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_code is not None:
            result['tagCode'] = self.tag_code

        if self.tag_value is not None:
            result['tagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tagCode') is not None:
            self.tag_code = m.get('tagCode')

        if m.get('tagValue') is not None:
            self.tag_value = m.get('tagValue')

        return self

