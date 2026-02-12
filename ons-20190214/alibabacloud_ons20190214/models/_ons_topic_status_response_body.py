# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ons20190214 import models as main_models
from darabonba.model import DaraModel

class OnsTopicStatusResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.OnsTopicStatusResponseBodyData = None,
        request_id: str = None,
    ):
        # The data structure of the queried topic.
        self.data = data
        # The ID of the request. This parameter is a common parameter. Each request has a unique ID. You can use this ID to troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.OnsTopicStatusResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class OnsTopicStatusResponseBodyData(DaraModel):
    def __init__(
        self,
        last_time_stamp: int = None,
        perm: int = None,
        total_count: int = None,
    ):
        # The point in time when the latest message is ready in the topic. If no message exists in the topic, the return value of this parameter is 0.
        # 
        # The value of this parameter is a UNIX timestamp in milliseconds.
        # 
        # For information about the definition of ready messages and ready time, see [Terms](https://help.aliyun.com/document_detail/29533.html).
        self.last_time_stamp = last_time_stamp
        # Indicates the operations that you can perform on the topic. Valid values:
        # 
        # *   **2**: You can publish messages to the topic.
        # *   **4**: You can subscribe to the topic.
        # *   **6**: You can publish messages to and subscribe to the topic.
        self.perm = perm
        # The total number of messages in all partitions of the topic.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.last_time_stamp is not None:
            result['LastTimeStamp'] = self.last_time_stamp

        if self.perm is not None:
            result['Perm'] = self.perm

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LastTimeStamp') is not None:
            self.last_time_stamp = m.get('LastTimeStamp')

        if m.get('Perm') is not None:
            self.perm = m.get('Perm')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

