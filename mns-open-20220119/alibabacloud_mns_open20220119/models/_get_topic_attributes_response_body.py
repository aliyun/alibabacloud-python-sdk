# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mns_open20220119 import models as main_models
from darabonba.model import DaraModel

class GetTopicAttributesResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.GetTopicAttributesResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        # The response code.
        self.code = code
        # The response data.
        self.data = data
        # The response message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The response status.
        self.status = status
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
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetTopicAttributesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetTopicAttributesResponseBodyData(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        enable_sse: bool = None,
        encryption_enabled: bool = None,
        kms_key_id: str = None,
        last_modify_time: int = None,
        logging_enabled: bool = None,
        max_message_size: int = None,
        message_count: int = None,
        message_retention_period: int = None,
        sse_algorithm: str = None,
        sse_type: str = None,
        tags: List[main_models.GetTopicAttributesResponseBodyDataTags] = None,
        topic_inner_url: str = None,
        topic_name: str = None,
        topic_type: str = None,
        topic_url: str = None,
    ):
        # The time when the topic was created. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.create_time = create_time
        self.enable_sse = enable_sse
        self.encryption_enabled = encryption_enabled
        self.kms_key_id = kms_key_id
        # The most recent time when the topic attributes were modified. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.last_modify_time = last_modify_time
        # Indicates whether the Log Management feature is enabled. Valid values:
        # 
        # - True: Enabled.
        # 
        # - False: Disabled.
        self.logging_enabled = logging_enabled
        # The maximum length of the message body sent to the topic. Unit: bytes.
        self.max_message_size = max_message_size
        # The number of messages in the topic.
        self.message_count = message_count
        # The maximum duration for which a message is retained in the topic. After the period of time specified by this parameter elapses since the message is sent to the topic, the message is deleted regardless of whether it is successfully pushed to the user. Unit: seconds.
        self.message_retention_period = message_retention_period
        self.sse_algorithm = sse_algorithm
        self.sse_type = sse_type
        # The list of resource tags.
        self.tags = tags
        self.topic_inner_url = topic_inner_url
        # The name of the topic.
        self.topic_name = topic_name
        # The type of the topic. Valid values:
        #    * normal: normal topic
        #    * fifo: FIFO topic
        self.topic_type = topic_type
        self.topic_url = topic_url

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
            result['CreateTime'] = self.create_time

        if self.enable_sse is not None:
            result['EnableSSE'] = self.enable_sse

        if self.encryption_enabled is not None:
            result['EncryptionEnabled'] = self.encryption_enabled

        if self.kms_key_id is not None:
            result['KmsKeyId'] = self.kms_key_id

        if self.last_modify_time is not None:
            result['LastModifyTime'] = self.last_modify_time

        if self.logging_enabled is not None:
            result['LoggingEnabled'] = self.logging_enabled

        if self.max_message_size is not None:
            result['MaxMessageSize'] = self.max_message_size

        if self.message_count is not None:
            result['MessageCount'] = self.message_count

        if self.message_retention_period is not None:
            result['MessageRetentionPeriod'] = self.message_retention_period

        if self.sse_algorithm is not None:
            result['SseAlgorithm'] = self.sse_algorithm

        if self.sse_type is not None:
            result['SseType'] = self.sse_type

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.topic_inner_url is not None:
            result['TopicInnerUrl'] = self.topic_inner_url

        if self.topic_name is not None:
            result['TopicName'] = self.topic_name

        if self.topic_type is not None:
            result['TopicType'] = self.topic_type

        if self.topic_url is not None:
            result['TopicUrl'] = self.topic_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('EnableSSE') is not None:
            self.enable_sse = m.get('EnableSSE')

        if m.get('EncryptionEnabled') is not None:
            self.encryption_enabled = m.get('EncryptionEnabled')

        if m.get('KmsKeyId') is not None:
            self.kms_key_id = m.get('KmsKeyId')

        if m.get('LastModifyTime') is not None:
            self.last_modify_time = m.get('LastModifyTime')

        if m.get('LoggingEnabled') is not None:
            self.logging_enabled = m.get('LoggingEnabled')

        if m.get('MaxMessageSize') is not None:
            self.max_message_size = m.get('MaxMessageSize')

        if m.get('MessageCount') is not None:
            self.message_count = m.get('MessageCount')

        if m.get('MessageRetentionPeriod') is not None:
            self.message_retention_period = m.get('MessageRetentionPeriod')

        if m.get('SseAlgorithm') is not None:
            self.sse_algorithm = m.get('SseAlgorithm')

        if m.get('SseType') is not None:
            self.sse_type = m.get('SseType')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.GetTopicAttributesResponseBodyDataTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('TopicInnerUrl') is not None:
            self.topic_inner_url = m.get('TopicInnerUrl')

        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')

        if m.get('TopicType') is not None:
            self.topic_type = m.get('TopicType')

        if m.get('TopicUrl') is not None:
            self.topic_url = m.get('TopicUrl')

        return self

class GetTopicAttributesResponseBodyDataTags(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The key of the tag.
        self.tag_key = tag_key
        # The value of the tag.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        return self

