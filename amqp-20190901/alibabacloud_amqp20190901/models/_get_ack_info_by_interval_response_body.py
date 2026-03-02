# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_amqp20190901 import models as main_models
from darabonba.model import DaraModel

class GetAckInfoByIntervalResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.GetAckInfoByIntervalResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
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

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetAckInfoByIntervalResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetAckInfoByIntervalResponseBodyData(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
        vo_list: List[main_models.GetAckInfoByIntervalResponseBodyDataVoList] = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.total_count = total_count
        self.vo_list = vo_list

    def validate(self):
        if self.vo_list:
            for v1 in self.vo_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        result['VoList'] = []
        if self.vo_list is not None:
            for k1 in self.vo_list:
                result['VoList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.vo_list = []
        if m.get('VoList') is not None:
            for k1 in m.get('VoList'):
                temp_model = main_models.GetAckInfoByIntervalResponseBodyDataVoList()
                self.vo_list.append(temp_model.from_map(k1))

        return self

class GetAckInfoByIntervalResponseBodyDataVoList(DaraModel):
    def __init__(
        self,
        action: str = None,
        channel_id: str = None,
        connection_id: str = None,
        delivery_tag: int = None,
        queue_name: str = None,
        rocket_mq_msg_id: str = None,
        rt: int = None,
        time_stamp: str = None,
    ):
        self.action = action
        self.channel_id = channel_id
        self.connection_id = connection_id
        self.delivery_tag = delivery_tag
        self.queue_name = queue_name
        self.rocket_mq_msg_id = rocket_mq_msg_id
        self.rt = rt
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id

        if self.connection_id is not None:
            result['ConnectionId'] = self.connection_id

        if self.delivery_tag is not None:
            result['DeliveryTag'] = self.delivery_tag

        if self.queue_name is not None:
            result['QueueName'] = self.queue_name

        if self.rocket_mq_msg_id is not None:
            result['RocketMqMsgId'] = self.rocket_mq_msg_id

        if self.rt is not None:
            result['Rt'] = self.rt

        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        if m.get('ConnectionId') is not None:
            self.connection_id = m.get('ConnectionId')

        if m.get('DeliveryTag') is not None:
            self.delivery_tag = m.get('DeliveryTag')

        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')

        if m.get('RocketMqMsgId') is not None:
            self.rocket_mq_msg_id = m.get('RocketMqMsgId')

        if m.get('Rt') is not None:
            self.rt = m.get('Rt')

        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        return self

