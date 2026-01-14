# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_rocketmq20220801 import models as main_models
from darabonba.model import DaraModel

class GetMessageDetailResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetMessageDetailResponseBodyData = None,
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
            temp_model = main_models.GetMessageDetailResponseBodyData()
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

class GetMessageDetailResponseBodyData(DaraModel):
    def __init__(
        self,
        body: str = None,
        body_size: int = None,
        born_host: str = None,
        born_time: str = None,
        instance_id: str = None,
        lite_topic_name: str = None,
        message_group: str = None,
        message_id: str = None,
        message_keys: List[str] = None,
        message_tag: str = None,
        message_type: str = None,
        region_id: str = None,
        store_host: str = None,
        store_time: str = None,
        system_properties: Dict[str, str] = None,
        topic_name: str = None,
        user_properties: Dict[str, str] = None,
    ):
        # The message body.
        self.body = body
        # The size of the message body.
        self.body_size = body_size
        # The client on which the message was produced.
        self.born_host = born_host
        # The time when the message was generated.
        self.born_time = born_time
        # The instance ID.
        self.instance_id = instance_id
        self.lite_topic_name = lite_topic_name
        # The sharding key. This parameter is returned only for ordered messages.
        self.message_group = message_group
        # The message ID.
        self.message_id = message_id
        # The message keys.
        self.message_keys = message_keys
        # The tags.
        self.message_tag = message_tag
        # The message type.
        self.message_type = message_type
        # The region ID.
        self.region_id = region_id
        # The broker on which the message was stored.
        self.store_host = store_host
        # The time when the message was stored.
        self.store_time = store_time
        # The default system attributes.
        self.system_properties = system_properties
        # The topic name.
        self.topic_name = topic_name
        # The user attributes.
        self.user_properties = user_properties

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body is not None:
            result['body'] = self.body

        if self.body_size is not None:
            result['bodySize'] = self.body_size

        if self.born_host is not None:
            result['bornHost'] = self.born_host

        if self.born_time is not None:
            result['bornTime'] = self.born_time

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.lite_topic_name is not None:
            result['liteTopicName'] = self.lite_topic_name

        if self.message_group is not None:
            result['messageGroup'] = self.message_group

        if self.message_id is not None:
            result['messageId'] = self.message_id

        if self.message_keys is not None:
            result['messageKeys'] = self.message_keys

        if self.message_tag is not None:
            result['messageTag'] = self.message_tag

        if self.message_type is not None:
            result['messageType'] = self.message_type

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.store_host is not None:
            result['storeHost'] = self.store_host

        if self.store_time is not None:
            result['storeTime'] = self.store_time

        if self.system_properties is not None:
            result['systemProperties'] = self.system_properties

        if self.topic_name is not None:
            result['topicName'] = self.topic_name

        if self.user_properties is not None:
            result['userProperties'] = self.user_properties

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')

        if m.get('bodySize') is not None:
            self.body_size = m.get('bodySize')

        if m.get('bornHost') is not None:
            self.born_host = m.get('bornHost')

        if m.get('bornTime') is not None:
            self.born_time = m.get('bornTime')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('liteTopicName') is not None:
            self.lite_topic_name = m.get('liteTopicName')

        if m.get('messageGroup') is not None:
            self.message_group = m.get('messageGroup')

        if m.get('messageId') is not None:
            self.message_id = m.get('messageId')

        if m.get('messageKeys') is not None:
            self.message_keys = m.get('messageKeys')

        if m.get('messageTag') is not None:
            self.message_tag = m.get('messageTag')

        if m.get('messageType') is not None:
            self.message_type = m.get('messageType')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('storeHost') is not None:
            self.store_host = m.get('storeHost')

        if m.get('storeTime') is not None:
            self.store_time = m.get('storeTime')

        if m.get('systemProperties') is not None:
            self.system_properties = m.get('systemProperties')

        if m.get('topicName') is not None:
            self.topic_name = m.get('topicName')

        if m.get('userProperties') is not None:
            self.user_properties = m.get('userProperties')

        return self

