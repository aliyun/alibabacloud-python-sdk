# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_rocketmq20220801 import models as main_models
from darabonba.model import DaraModel

class GetTopicResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetTopicResponseBodyData = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Error code.
        self.code = code
        # The returned data.
        self.data = data
        # Dynamic error code.
        self.dynamic_code = dynamic_code
        # Dynamic error message.
        self.dynamic_message = dynamic_message
        # HTTP status code.
        self.http_status_code = http_status_code
        # Error message.
        self.message = message
        # Request ID, each request\\"s ID is unique and can be used for troubleshooting and problem localization.
        self.request_id = request_id
        # Indicates whether the execution was successful.
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
            temp_model = main_models.GetTopicResponseBodyData()
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

class GetTopicResponseBodyData(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        instance_id: str = None,
        lite_topic_expiration: int = None,
        max_send_tps: int = None,
        message_type: str = None,
        region_id: str = None,
        remark: str = None,
        status: str = None,
        topic_name: str = None,
        update_time: str = None,
    ):
        # Creation time of the topic.
        self.create_time = create_time
        # The ID of the instance to which the topic belongs.
        self.instance_id = instance_id
        self.lite_topic_expiration = lite_topic_expiration
        # The maximum TPS for message sending.
        self.max_send_tps = max_send_tps
        # The type of messages in the topic.
        # 
        # Valid values:
        # 
        # *   TRANSACTION: transactional messages
        # *   FIFO: ordered messages
        # *   DELAY: scheduled or delayed messages
        # *   NORMAL: normal messages
        # 
        # Valid values:
        # 
        # *   TRANSACTION: transactional messages
        # *   FIFO: ordered messages
        # *   DELAY: scheduled or delayed messages
        # *   NORMAL: normal messages
        self.message_type = message_type
        # The region ID to which the instance belongs.
        self.region_id = region_id
        # Remark information of the topic.
        self.remark = remark
        # The topic status.
        # 
        # Valid values:
        # 
        # *   RUNNING
        # *   CREATING
        self.status = status
        # Topic name.
        self.topic_name = topic_name
        # Last modification time of the topic.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.lite_topic_expiration is not None:
            result['liteTopicExpiration'] = self.lite_topic_expiration

        if self.max_send_tps is not None:
            result['maxSendTps'] = self.max_send_tps

        if self.message_type is not None:
            result['messageType'] = self.message_type

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.remark is not None:
            result['remark'] = self.remark

        if self.status is not None:
            result['status'] = self.status

        if self.topic_name is not None:
            result['topicName'] = self.topic_name

        if self.update_time is not None:
            result['updateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('liteTopicExpiration') is not None:
            self.lite_topic_expiration = m.get('liteTopicExpiration')

        if m.get('maxSendTps') is not None:
            self.max_send_tps = m.get('maxSendTps')

        if m.get('messageType') is not None:
            self.message_type = m.get('messageType')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('remark') is not None:
            self.remark = m.get('remark')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('topicName') is not None:
            self.topic_name = m.get('topicName')

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        return self

