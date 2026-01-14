# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_rocketmq20220801 import models as main_models
from darabonba.model import DaraModel

class GetTraceResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetTraceResponseBodyData = None,
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
        # The ID of the request. The system generates a unique ID for each request. You can troubleshoot issues based on the request ID.
        self.request_id = request_id
        # Indicates whether the call was successful.
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
            temp_model = main_models.GetTraceResponseBodyData()
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

class GetTraceResponseBodyData(DaraModel):
    def __init__(
        self,
        broker_info: main_models.GetTraceResponseBodyDataBrokerInfo = None,
        consumer_infos: List[main_models.GetTraceResponseBodyDataConsumerInfos] = None,
        instance_id: str = None,
        message_info: main_models.GetTraceResponseBodyDataMessageInfo = None,
        producer_info: main_models.GetTraceResponseBodyDataProducerInfo = None,
        region_id: str = None,
        topic_name: str = None,
    ):
        # The broker trace.
        self.broker_info = broker_info
        # Consumer trace info.
        self.consumer_infos = consumer_infos
        # The instance ID.
        self.instance_id = instance_id
        # The message information.
        self.message_info = message_info
        # The producer trace.
        self.producer_info = producer_info
        # The region ID.
        self.region_id = region_id
        # The topic name.
        self.topic_name = topic_name

    def validate(self):
        if self.broker_info:
            self.broker_info.validate()
        if self.consumer_infos:
            for v1 in self.consumer_infos:
                 if v1:
                    v1.validate()
        if self.message_info:
            self.message_info.validate()
        if self.producer_info:
            self.producer_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.broker_info is not None:
            result['brokerInfo'] = self.broker_info.to_map()

        result['consumerInfos'] = []
        if self.consumer_infos is not None:
            for k1 in self.consumer_infos:
                result['consumerInfos'].append(k1.to_map() if k1 else None)

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.message_info is not None:
            result['messageInfo'] = self.message_info.to_map()

        if self.producer_info is not None:
            result['producerInfo'] = self.producer_info.to_map()

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.topic_name is not None:
            result['topicName'] = self.topic_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('brokerInfo') is not None:
            temp_model = main_models.GetTraceResponseBodyDataBrokerInfo()
            self.broker_info = temp_model.from_map(m.get('brokerInfo'))

        self.consumer_infos = []
        if m.get('consumerInfos') is not None:
            for k1 in m.get('consumerInfos'):
                temp_model = main_models.GetTraceResponseBodyDataConsumerInfos()
                self.consumer_infos.append(temp_model.from_map(k1))

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('messageInfo') is not None:
            temp_model = main_models.GetTraceResponseBodyDataMessageInfo()
            self.message_info = temp_model.from_map(m.get('messageInfo'))

        if m.get('producerInfo') is not None:
            temp_model = main_models.GetTraceResponseBodyDataProducerInfo()
            self.producer_info = temp_model.from_map(m.get('producerInfo'))

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('topicName') is not None:
            self.topic_name = m.get('topicName')

        return self

class GetTraceResponseBodyDataProducerInfo(DaraModel):
    def __init__(
        self,
        records: List[main_models.GetTraceResponseBodyDataProducerInfoRecords] = None,
    ):
        # The production records.
        self.records = records

    def validate(self):
        if self.records:
            for v1 in self.records:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['records'] = []
        if self.records is not None:
            for k1 in self.records:
                result['records'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.records = []
        if m.get('records') is not None:
            for k1 in m.get('records'):
                temp_model = main_models.GetTraceResponseBodyDataProducerInfoRecords()
                self.records.append(temp_model.from_map(k1))

        return self

class GetTraceResponseBodyDataProducerInfoRecords(DaraModel):
    def __init__(
        self,
        arrive_time: str = None,
        client_host: str = None,
        dlq_origin_message_id: str = None,
        dlq_origin_topic: str = None,
        message_source: str = None,
        produce_duration: int = None,
        produce_status: str = None,
        produce_time: str = None,
        recall_time: str = None,
        user_name: str = None,
    ):
        # Arrive time.
        self.arrive_time = arrive_time
        # Client host.
        self.client_host = client_host
        # Dead-letter queue message ID.
        self.dlq_origin_message_id = dlq_origin_message_id
        # Dead-letter queue topic.
        self.dlq_origin_topic = dlq_origin_topic
        # Message source.
        self.message_source = message_source
        # Producer duration.
        self.produce_duration = produce_duration
        # Producer status.
        self.produce_status = produce_status
        # Producer time.
        self.produce_time = produce_time
        # The time when the scheduled message withdrawal request was initiated
        self.recall_time = recall_time
        # Producer name.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arrive_time is not None:
            result['arriveTime'] = self.arrive_time

        if self.client_host is not None:
            result['clientHost'] = self.client_host

        if self.dlq_origin_message_id is not None:
            result['dlqOriginMessageId'] = self.dlq_origin_message_id

        if self.dlq_origin_topic is not None:
            result['dlqOriginTopic'] = self.dlq_origin_topic

        if self.message_source is not None:
            result['messageSource'] = self.message_source

        if self.produce_duration is not None:
            result['produceDuration'] = self.produce_duration

        if self.produce_status is not None:
            result['produceStatus'] = self.produce_status

        if self.produce_time is not None:
            result['produceTime'] = self.produce_time

        if self.recall_time is not None:
            result['recallTime'] = self.recall_time

        if self.user_name is not None:
            result['userName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('arriveTime') is not None:
            self.arrive_time = m.get('arriveTime')

        if m.get('clientHost') is not None:
            self.client_host = m.get('clientHost')

        if m.get('dlqOriginMessageId') is not None:
            self.dlq_origin_message_id = m.get('dlqOriginMessageId')

        if m.get('dlqOriginTopic') is not None:
            self.dlq_origin_topic = m.get('dlqOriginTopic')

        if m.get('messageSource') is not None:
            self.message_source = m.get('messageSource')

        if m.get('produceDuration') is not None:
            self.produce_duration = m.get('produceDuration')

        if m.get('produceStatus') is not None:
            self.produce_status = m.get('produceStatus')

        if m.get('produceTime') is not None:
            self.produce_time = m.get('produceTime')

        if m.get('recallTime') is not None:
            self.recall_time = m.get('recallTime')

        if m.get('userName') is not None:
            self.user_name = m.get('userName')

        return self

class GetTraceResponseBodyDataMessageInfo(DaraModel):
    def __init__(
        self,
        body: str = None,
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
        topic_name: str = None,
        transaction_id: str = None,
        user_properties: Dict[str, str] = None,
    ):
        # Message body.
        self.body = body
        # Message born host.
        self.born_host = born_host
        # Message born time.
        self.born_time = born_time
        # The instance ID.
        self.instance_id = instance_id
        self.lite_topic_name = lite_topic_name
        # Message grpup.
        self.message_group = message_group
        # The message ID.
        self.message_id = message_id
        # Message keys.
        self.message_keys = message_keys
        # Message tag.
        self.message_tag = message_tag
        # Message type.
        self.message_type = message_type
        # The region ID.
        self.region_id = region_id
        # Message store host.
        self.store_host = store_host
        # Message store time.
        self.store_time = store_time
        # The topic name.
        self.topic_name = topic_name
        # Message transaction id.
        self.transaction_id = transaction_id
        # Message user properties.
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

        if self.topic_name is not None:
            result['topicName'] = self.topic_name

        if self.transaction_id is not None:
            result['transactionId'] = self.transaction_id

        if self.user_properties is not None:
            result['userProperties'] = self.user_properties

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')

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

        if m.get('topicName') is not None:
            self.topic_name = m.get('topicName')

        if m.get('transactionId') is not None:
            self.transaction_id = m.get('transactionId')

        if m.get('userProperties') is not None:
            self.user_properties = m.get('userProperties')

        return self

class GetTraceResponseBodyDataConsumerInfos(DaraModel):
    def __init__(
        self,
        consume_status: str = None,
        consumer_group_id: str = None,
        dead_letter_info: main_models.GetTraceResponseBodyDataConsumerInfosDeadLetterInfo = None,
        dead_message: bool = None,
        records: List[main_models.GetTraceResponseBodyDataConsumerInfosRecords] = None,
    ):
        # Consume status.
        self.consume_status = consume_status
        # The consumer group ID.
        self.consumer_group_id = consumer_group_id
        # Dead letter info.
        self.dead_letter_info = dead_letter_info
        # Whether it is a dead letter message.
        self.dead_message = dead_message
        # Consumer record list.
        self.records = records

    def validate(self):
        if self.dead_letter_info:
            self.dead_letter_info.validate()
        if self.records:
            for v1 in self.records:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.consume_status is not None:
            result['consumeStatus'] = self.consume_status

        if self.consumer_group_id is not None:
            result['consumerGroupId'] = self.consumer_group_id

        if self.dead_letter_info is not None:
            result['deadLetterInfo'] = self.dead_letter_info.to_map()

        if self.dead_message is not None:
            result['deadMessage'] = self.dead_message

        result['records'] = []
        if self.records is not None:
            for k1 in self.records:
                result['records'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('consumeStatus') is not None:
            self.consume_status = m.get('consumeStatus')

        if m.get('consumerGroupId') is not None:
            self.consumer_group_id = m.get('consumerGroupId')

        if m.get('deadLetterInfo') is not None:
            temp_model = main_models.GetTraceResponseBodyDataConsumerInfosDeadLetterInfo()
            self.dead_letter_info = temp_model.from_map(m.get('deadLetterInfo'))

        if m.get('deadMessage') is not None:
            self.dead_message = m.get('deadMessage')

        self.records = []
        if m.get('records') is not None:
            for k1 in m.get('records'):
                temp_model = main_models.GetTraceResponseBodyDataConsumerInfosRecords()
                self.records.append(temp_model.from_map(k1))

        return self

class GetTraceResponseBodyDataConsumerInfosRecords(DaraModel):
    def __init__(
        self,
        client_host: str = None,
        consume_status: str = None,
        fifo_enable: bool = None,
        operations: List[main_models.GetTraceResponseBodyDataConsumerInfosRecordsOperations] = None,
        pop_ck: str = None,
        user_name: str = None,
    ):
        # Client host.
        self.client_host = client_host
        # Consume status.
        self.consume_status = consume_status
        # Whether to consume fifo.
        self.fifo_enable = fifo_enable
        # Operation list.
        self.operations = operations
        # POP_CK
        self.pop_ck = pop_ck
        # Consumer name.
        self.user_name = user_name

    def validate(self):
        if self.operations:
            for v1 in self.operations:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_host is not None:
            result['clientHost'] = self.client_host

        if self.consume_status is not None:
            result['consumeStatus'] = self.consume_status

        if self.fifo_enable is not None:
            result['fifoEnable'] = self.fifo_enable

        result['operations'] = []
        if self.operations is not None:
            for k1 in self.operations:
                result['operations'].append(k1.to_map() if k1 else None)

        if self.pop_ck is not None:
            result['popCk'] = self.pop_ck

        if self.user_name is not None:
            result['userName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientHost') is not None:
            self.client_host = m.get('clientHost')

        if m.get('consumeStatus') is not None:
            self.consume_status = m.get('consumeStatus')

        if m.get('fifoEnable') is not None:
            self.fifo_enable = m.get('fifoEnable')

        self.operations = []
        if m.get('operations') is not None:
            for k1 in m.get('operations'):
                temp_model = main_models.GetTraceResponseBodyDataConsumerInfosRecordsOperations()
                self.operations.append(temp_model.from_map(k1))

        if m.get('popCk') is not None:
            self.pop_ck = m.get('popCk')

        if m.get('userName') is not None:
            self.user_name = m.get('userName')

        return self

class GetTraceResponseBodyDataConsumerInfosRecordsOperations(DaraModel):
    def __init__(
        self,
        dead_message: bool = None,
        invisible_time: int = None,
        operate_time: str = None,
        operate_type: str = None,
    ):
        # Whether it is a dead letter message.
        self.dead_message = dead_message
        # Invisible time, milliseconds.
        self.invisible_time = invisible_time
        # Operation time.
        self.operate_time = operate_time
        # Operation type.
        self.operate_type = operate_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dead_message is not None:
            result['deadMessage'] = self.dead_message

        if self.invisible_time is not None:
            result['invisibleTime'] = self.invisible_time

        if self.operate_time is not None:
            result['operateTime'] = self.operate_time

        if self.operate_type is not None:
            result['operateType'] = self.operate_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deadMessage') is not None:
            self.dead_message = m.get('deadMessage')

        if m.get('invisibleTime') is not None:
            self.invisible_time = m.get('invisibleTime')

        if m.get('operateTime') is not None:
            self.operate_time = m.get('operateTime')

        if m.get('operateType') is not None:
            self.operate_type = m.get('operateType')

        return self

class GetTraceResponseBodyDataConsumerInfosDeadLetterInfo(DaraModel):
    def __init__(
        self,
        message_id: str = None,
        to_dlq_time: str = None,
        topic_name: str = None,
    ):
        # MessageId.
        self.message_id = message_id
        # Arrival time in the dead letter queue.
        self.to_dlq_time = to_dlq_time
        # The topic name.
        self.topic_name = topic_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message_id is not None:
            result['messageId'] = self.message_id

        if self.to_dlq_time is not None:
            result['toDlqTime'] = self.to_dlq_time

        if self.topic_name is not None:
            result['topicName'] = self.topic_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('messageId') is not None:
            self.message_id = m.get('messageId')

        if m.get('toDlqTime') is not None:
            self.to_dlq_time = m.get('toDlqTime')

        if m.get('topicName') is not None:
            self.topic_name = m.get('topicName')

        return self

class GetTraceResponseBodyDataBrokerInfo(DaraModel):
    def __init__(
        self,
        delay_status: str = None,
        operations: List[main_models.GetTraceResponseBodyDataBrokerInfoOperations] = None,
        preset_delay_time: str = None,
        recall_result: str = None,
    ):
        # Delay status.
        self.delay_status = delay_status
        # Operation list.
        self.operations = operations
        # Preset delivery time.
        self.preset_delay_time = preset_delay_time
        # Withdraw scheduled message request result
        self.recall_result = recall_result

    def validate(self):
        if self.operations:
            for v1 in self.operations:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.delay_status is not None:
            result['delayStatus'] = self.delay_status

        result['operations'] = []
        if self.operations is not None:
            for k1 in self.operations:
                result['operations'].append(k1.to_map() if k1 else None)

        if self.preset_delay_time is not None:
            result['presetDelayTime'] = self.preset_delay_time

        if self.recall_result is not None:
            result['recallResult'] = self.recall_result

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('delayStatus') is not None:
            self.delay_status = m.get('delayStatus')

        self.operations = []
        if m.get('operations') is not None:
            for k1 in m.get('operations'):
                temp_model = main_models.GetTraceResponseBodyDataBrokerInfoOperations()
                self.operations.append(temp_model.from_map(k1))

        if m.get('presetDelayTime') is not None:
            self.preset_delay_time = m.get('presetDelayTime')

        if m.get('recallResult') is not None:
            self.recall_result = m.get('recallResult')

        return self

class GetTraceResponseBodyDataBrokerInfoOperations(DaraModel):
    def __init__(
        self,
        operate_time: str = None,
        operate_type: str = None,
    ):
        # Operation time.
        self.operate_time = operate_time
        # Operation type.
        self.operate_type = operate_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.operate_time is not None:
            result['operateTime'] = self.operate_time

        if self.operate_type is not None:
            result['operateType'] = self.operate_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('operateTime') is not None:
            self.operate_time = m.get('operateTime')

        if m.get('operateType') is not None:
            self.operate_type = m.get('operateType')

        return self

