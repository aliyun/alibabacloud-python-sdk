# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetTopicAttributesRequest(DaraModel):
    def __init__(
        self,
        enable_logging: bool = None,
        enable_sse: bool = None,
        kms_key_id: str = None,
        max_message_size: int = None,
        sse_algorithm: str = None,
        sse_type: str = None,
        topic_name: str = None,
    ):
        # Specifies whether to enable the log management feature. Valid values:
        # 
        # - true: Enabled.
        # 
        # - false: Disabled.
        # Default value: false.
        self.enable_logging = enable_logging
        self.enable_sse = enable_sse
        self.kms_key_id = kms_key_id
        # The maximum length of the message body sent to the topic. Valid values: 1024 to 65536. Unit: bytes. Default value: 65536.
        self.max_message_size = max_message_size
        self.sse_algorithm = sse_algorithm
        self.sse_type = sse_type
        # The name of the topic.
        # 
        # This parameter is required.
        self.topic_name = topic_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_logging is not None:
            result['EnableLogging'] = self.enable_logging

        if self.enable_sse is not None:
            result['EnableSSE'] = self.enable_sse

        if self.kms_key_id is not None:
            result['KmsKeyId'] = self.kms_key_id

        if self.max_message_size is not None:
            result['MaxMessageSize'] = self.max_message_size

        if self.sse_algorithm is not None:
            result['SseAlgorithm'] = self.sse_algorithm

        if self.sse_type is not None:
            result['SseType'] = self.sse_type

        if self.topic_name is not None:
            result['TopicName'] = self.topic_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableLogging') is not None:
            self.enable_logging = m.get('EnableLogging')

        if m.get('EnableSSE') is not None:
            self.enable_sse = m.get('EnableSSE')

        if m.get('KmsKeyId') is not None:
            self.kms_key_id = m.get('KmsKeyId')

        if m.get('MaxMessageSize') is not None:
            self.max_message_size = m.get('MaxMessageSize')

        if m.get('SseAlgorithm') is not None:
            self.sse_algorithm = m.get('SseAlgorithm')

        if m.get('SseType') is not None:
            self.sse_type = m.get('SseType')

        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')

        return self

