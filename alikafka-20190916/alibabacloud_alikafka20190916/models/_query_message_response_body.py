# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alikafka20190916 import models as main_models
from darabonba.model import DaraModel

class QueryMessageResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        message_list: List[main_models.QueryMessageResponseBodyMessageList] = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The returned HTTP status code. If the request is successful, 200 is returned.
        self.code = code
        # The returned message.
        self.message = message
        # The messages.
        self.message_list = message_list
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.success = success

    def validate(self):
        if self.message_list:
            for v1 in self.message_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        result['MessageList'] = []
        if self.message_list is not None:
            for k1 in self.message_list:
                result['MessageList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        self.message_list = []
        if m.get('MessageList') is not None:
            for k1 in m.get('MessageList'):
                temp_model = main_models.QueryMessageResponseBodyMessageList()
                self.message_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryMessageResponseBodyMessageList(DaraModel):
    def __init__(
        self,
        checksum: int = None,
        key: str = None,
        key_truncated: bool = None,
        offset: int = None,
        partition: int = None,
        serialized_key_size: int = None,
        serialized_value_size: int = None,
        timestamp: int = None,
        timestamp_type: str = None,
        topic: str = None,
        truncated_key_size: int = None,
        truncated_value_size: int = None,
        value: str = None,
        value_truncated: bool = None,
    ):
        # The check value of the chaincode.
        self.checksum = checksum
        # The message key.
        self.key = key
        # Indicates whether the key is truncated.
        self.key_truncated = key_truncated
        # The consumer offset of the partition.
        self.offset = offset
        # The partition ID.
        self.partition = partition
        # The size of the key after serialization. Unit: bytes.
        self.serialized_key_size = serialized_key_size
        # The size of the value after serialization. Unit: bytes.
        self.serialized_value_size = serialized_value_size
        # The time when the message was created. The value of this parameter is a UNIX timestamp in milliseconds.
        self.timestamp = timestamp
        # The time type.
        self.timestamp_type = timestamp_type
        # The topic name.
        self.topic = topic
        # The truncated size of the message key. Unit: bytes.
        # 
        # >  A maximum of 1 KB of content can be displayed for each message. Content that exceeds 1 KB is automatically truncated. For more information, see [Query messages](https://help.aliyun.com/document_detail/113172.html).
        self.truncated_key_size = truncated_key_size
        # The truncated size of the message value. Unit: bytes.
        # 
        # >  A maximum of 1 KB of content can be displayed for each message. Content that exceeds 1 KB is automatically truncated. For more information, see [Query messages](https://help.aliyun.com/document_detail/113172.html).
        self.truncated_value_size = truncated_value_size
        # The message value.
        self.value = value
        # Indicates whether the value is truncated.
        self.value_truncated = value_truncated

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.checksum is not None:
            result['Checksum'] = self.checksum

        if self.key is not None:
            result['Key'] = self.key

        if self.key_truncated is not None:
            result['KeyTruncated'] = self.key_truncated

        if self.offset is not None:
            result['Offset'] = self.offset

        if self.partition is not None:
            result['Partition'] = self.partition

        if self.serialized_key_size is not None:
            result['SerializedKeySize'] = self.serialized_key_size

        if self.serialized_value_size is not None:
            result['SerializedValueSize'] = self.serialized_value_size

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        if self.timestamp_type is not None:
            result['TimestampType'] = self.timestamp_type

        if self.topic is not None:
            result['Topic'] = self.topic

        if self.truncated_key_size is not None:
            result['TruncatedKeySize'] = self.truncated_key_size

        if self.truncated_value_size is not None:
            result['TruncatedValueSize'] = self.truncated_value_size

        if self.value is not None:
            result['Value'] = self.value

        if self.value_truncated is not None:
            result['ValueTruncated'] = self.value_truncated

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Checksum') is not None:
            self.checksum = m.get('Checksum')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('KeyTruncated') is not None:
            self.key_truncated = m.get('KeyTruncated')

        if m.get('Offset') is not None:
            self.offset = m.get('Offset')

        if m.get('Partition') is not None:
            self.partition = m.get('Partition')

        if m.get('SerializedKeySize') is not None:
            self.serialized_key_size = m.get('SerializedKeySize')

        if m.get('SerializedValueSize') is not None:
            self.serialized_value_size = m.get('SerializedValueSize')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        if m.get('TimestampType') is not None:
            self.timestamp_type = m.get('TimestampType')

        if m.get('Topic') is not None:
            self.topic = m.get('Topic')

        if m.get('TruncatedKeySize') is not None:
            self.truncated_key_size = m.get('TruncatedKeySize')

        if m.get('TruncatedValueSize') is not None:
            self.truncated_value_size = m.get('TruncatedValueSize')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        if m.get('ValueTruncated') is not None:
            self.value_truncated = m.get('ValueTruncated')

        return self

