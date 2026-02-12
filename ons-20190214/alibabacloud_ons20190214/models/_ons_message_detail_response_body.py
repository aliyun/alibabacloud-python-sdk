# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ons20190214 import models as main_models
from darabonba.model import DaraModel

class OnsMessageDetailResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.OnsMessageDetailResponseBodyData = None,
        request_id: str = None,
    ):
        # The data returned.
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
            temp_model = main_models.OnsMessageDetailResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class OnsMessageDetailResponseBodyData(DaraModel):
    def __init__(
        self,
        body: str = None,
        body_crc: int = None,
        body_str: str = None,
        born_host: str = None,
        born_timestamp: int = None,
        instance_id: str = None,
        msg_id: str = None,
        property_list: List[main_models.OnsMessageDetailResponseBodyDataPropertyList] = None,
        reconsume_times: int = None,
        store_host: str = None,
        store_size: int = None,
        store_timestamp: int = None,
        topic: str = None,
    ):
        # The string that is obtained after the message body is encrypted by using the Base 64 algorithm.
        self.body = body
        # The cyclic redundancy check (CRC) value of the message body.
        self.body_crc = body_crc
        # The information about the message body.
        self.body_str = body_str
        # The producer instance that generated the message.
        self.born_host = born_host
        # The timestamp that indicates the point in time when the message was generated. Unit: milliseconds.
        self.born_timestamp = born_timestamp
        # The ID of the ApsaraMQ for RocketMQ Instance.
        self.instance_id = instance_id
        # The ID of the message.
        self.msg_id = msg_id
        # The attributes of the message.
        self.property_list = property_list
        # The number of retries that ApsaraMQ for RocketMQ performed to send the message to consumers.
        self.reconsume_times = reconsume_times
        # The ApsaraMQ for RocketMQ broker that stores the message.
        self.store_host = store_host
        # The size of the message. Unit: KB.
        self.store_size = store_size
        # The timestamp that indicates the point in time when the ApsaraMQ for RocketMQ broker stored the message. Unit: milliseconds.
        self.store_timestamp = store_timestamp
        # The topic to which the message belongs.
        self.topic = topic

    def validate(self):
        if self.property_list:
            for v1 in self.property_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body is not None:
            result['Body'] = self.body

        if self.body_crc is not None:
            result['BodyCRC'] = self.body_crc

        if self.body_str is not None:
            result['BodyStr'] = self.body_str

        if self.born_host is not None:
            result['BornHost'] = self.born_host

        if self.born_timestamp is not None:
            result['BornTimestamp'] = self.born_timestamp

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.msg_id is not None:
            result['MsgId'] = self.msg_id

        result['PropertyList'] = []
        if self.property_list is not None:
            for k1 in self.property_list:
                result['PropertyList'].append(k1.to_map() if k1 else None)

        if self.reconsume_times is not None:
            result['ReconsumeTimes'] = self.reconsume_times

        if self.store_host is not None:
            result['StoreHost'] = self.store_host

        if self.store_size is not None:
            result['StoreSize'] = self.store_size

        if self.store_timestamp is not None:
            result['StoreTimestamp'] = self.store_timestamp

        if self.topic is not None:
            result['Topic'] = self.topic

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Body') is not None:
            self.body = m.get('Body')

        if m.get('BodyCRC') is not None:
            self.body_crc = m.get('BodyCRC')

        if m.get('BodyStr') is not None:
            self.body_str = m.get('BodyStr')

        if m.get('BornHost') is not None:
            self.born_host = m.get('BornHost')

        if m.get('BornTimestamp') is not None:
            self.born_timestamp = m.get('BornTimestamp')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')

        self.property_list = []
        if m.get('PropertyList') is not None:
            for k1 in m.get('PropertyList'):
                temp_model = main_models.OnsMessageDetailResponseBodyDataPropertyList()
                self.property_list.append(temp_model.from_map(k1))

        if m.get('ReconsumeTimes') is not None:
            self.reconsume_times = m.get('ReconsumeTimes')

        if m.get('StoreHost') is not None:
            self.store_host = m.get('StoreHost')

        if m.get('StoreSize') is not None:
            self.store_size = m.get('StoreSize')

        if m.get('StoreTimestamp') is not None:
            self.store_timestamp = m.get('StoreTimestamp')

        if m.get('Topic') is not None:
            self.topic = m.get('Topic')

        return self

class OnsMessageDetailResponseBodyDataPropertyList(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The name of the attribute. Valid values:
        # 
        # *   **TRACE_ON**: indicates whether the trace of the message exists.
        # *   **MSG_REGION**: The region ID of the instance to which the topic belongs.
        # *   **__MESSAGE_DECODED_TIME**: The time when the message was decoded.
        # *   **__BORNHOST**: The IP address of the producer client.
        # *   **UNIQ_KEY**: The ID of the message.
        # 
        # For information about the terms that are used in ApsaraMQ for RocketMQ, see [Terms](https://help.aliyun.com/document_detail/29533.html).
        self.name = name
        # The value of the attribute.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

