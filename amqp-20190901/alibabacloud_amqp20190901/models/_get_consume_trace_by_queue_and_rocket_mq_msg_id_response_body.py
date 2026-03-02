# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_amqp20190901 import models as main_models
from darabonba.model import DaraModel

class GetConsumeTraceByQueueAndRocketMqMsgIdResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: List[main_models.GetConsumeTraceByQueueAndRocketMqMsgIdResponseBodyData] = None,
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
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

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

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.GetConsumeTraceByQueueAndRocketMqMsgIdResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetConsumeTraceByQueueAndRocketMqMsgIdResponseBodyData(DaraModel):
    def __init__(
        self,
        auto_ack_tag: str = None,
        client_address: str = None,
        code: str = None,
        consume_type: str = None,
        consumer_tag: str = None,
        current_status: str = None,
        delivery_error_info: str = None,
        delivery_tag: str = None,
        dlq_queue_msg_id_map: Dict[str, Any] = None,
        reason: str = None,
        show_ack_icon: bool = None,
        time_stamp: str = None,
        user_id: str = None,
    ):
        self.auto_ack_tag = auto_ack_tag
        self.client_address = client_address
        self.code = code
        self.consume_type = consume_type
        self.consumer_tag = consumer_tag
        self.current_status = current_status
        self.delivery_error_info = delivery_error_info
        self.delivery_tag = delivery_tag
        self.dlq_queue_msg_id_map = dlq_queue_msg_id_map
        self.reason = reason
        self.show_ack_icon = show_ack_icon
        self.time_stamp = time_stamp
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_ack_tag is not None:
            result['AutoAckTag'] = self.auto_ack_tag

        if self.client_address is not None:
            result['ClientAddress'] = self.client_address

        if self.code is not None:
            result['Code'] = self.code

        if self.consume_type is not None:
            result['ConsumeType'] = self.consume_type

        if self.consumer_tag is not None:
            result['ConsumerTag'] = self.consumer_tag

        if self.current_status is not None:
            result['CurrentStatus'] = self.current_status

        if self.delivery_error_info is not None:
            result['DeliveryErrorInfo'] = self.delivery_error_info

        if self.delivery_tag is not None:
            result['DeliveryTag'] = self.delivery_tag

        if self.dlq_queue_msg_id_map is not None:
            result['DlqQueueMsgIdMap'] = self.dlq_queue_msg_id_map

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.show_ack_icon is not None:
            result['ShowAckIcon'] = self.show_ack_icon

        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoAckTag') is not None:
            self.auto_ack_tag = m.get('AutoAckTag')

        if m.get('ClientAddress') is not None:
            self.client_address = m.get('ClientAddress')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('ConsumeType') is not None:
            self.consume_type = m.get('ConsumeType')

        if m.get('ConsumerTag') is not None:
            self.consumer_tag = m.get('ConsumerTag')

        if m.get('CurrentStatus') is not None:
            self.current_status = m.get('CurrentStatus')

        if m.get('DeliveryErrorInfo') is not None:
            self.delivery_error_info = m.get('DeliveryErrorInfo')

        if m.get('DeliveryTag') is not None:
            self.delivery_tag = m.get('DeliveryTag')

        if m.get('DlqQueueMsgIdMap') is not None:
            self.dlq_queue_msg_id_map = m.get('DlqQueueMsgIdMap')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('ShowAckIcon') is not None:
            self.show_ack_icon = m.get('ShowAckIcon')

        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

