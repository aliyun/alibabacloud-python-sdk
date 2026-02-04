# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dts20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeConsumerGroupResponseBody(DaraModel):
    def __init__(
        self,
        consumer_channels: main_models.DescribeConsumerGroupResponseBodyConsumerChannels = None,
        err_code: str = None,
        err_message: str = None,
        page_number: int = None,
        page_record_count: int = None,
        request_id: str = None,
        success: str = None,
        total_record_count: int = None,
    ):
        # The list of consumer groups.
        self.consumer_channels = consumer_channels
        # The error code returned if the call failed.
        self.err_code = err_code
        # The error message returned if the call failed.
        self.err_message = err_message
        # The page number of the returned page.
        self.page_number = page_number
        # The maximum number of consumer groups that can be displayed on one page.
        self.page_record_count = page_record_count
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the call was successful.
        self.success = success
        # The total number of consumer groups.
        self.total_record_count = total_record_count

    def validate(self):
        if self.consumer_channels:
            self.consumer_channels.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.consumer_channels is not None:
            result['ConsumerChannels'] = self.consumer_channels.to_map()

        if self.err_code is not None:
            result['ErrCode'] = self.err_code

        if self.err_message is not None:
            result['ErrMessage'] = self.err_message

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsumerChannels') is not None:
            temp_model = main_models.DescribeConsumerGroupResponseBodyConsumerChannels()
            self.consumer_channels = temp_model.from_map(m.get('ConsumerChannels'))

        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')

        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class DescribeConsumerGroupResponseBodyConsumerChannels(DaraModel):
    def __init__(
        self,
        describe_consumer_channel: List[main_models.DescribeConsumerGroupResponseBodyConsumerChannelsDescribeConsumerChannel] = None,
    ):
        self.describe_consumer_channel = describe_consumer_channel

    def validate(self):
        if self.describe_consumer_channel:
            for v1 in self.describe_consumer_channel:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DescribeConsumerChannel'] = []
        if self.describe_consumer_channel is not None:
            for k1 in self.describe_consumer_channel:
                result['DescribeConsumerChannel'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.describe_consumer_channel = []
        if m.get('DescribeConsumerChannel') is not None:
            for k1 in m.get('DescribeConsumerChannel'):
                temp_model = main_models.DescribeConsumerGroupResponseBodyConsumerChannelsDescribeConsumerChannel()
                self.describe_consumer_channel.append(temp_model.from_map(k1))

        return self

class DescribeConsumerGroupResponseBodyConsumerChannelsDescribeConsumerChannel(DaraModel):
    def __init__(
        self,
        consumer_group_id: str = None,
        consumer_group_name: str = None,
        consumer_group_user_name: str = None,
        consumption_checkpoint: str = None,
        message_delay: int = None,
        unconsumed_data: int = None,
    ):
        # The ID of the consumer group.
        self.consumer_group_id = consumer_group_id
        # The name of the consumer group.
        self.consumer_group_name = consumer_group_name
        # The username of the consumer group.
        self.consumer_group_user_name = consumer_group_user_name
        # The consumption checkpoint, which is the time when the latest data record was consumed by the change tracking client. The format is *yyyy-MM-dd*T*HH:mm:ss*Z. The time is displayed in UTC.
        self.consumption_checkpoint = consumption_checkpoint
        # The message delay, which is the current time minus the timestamp of the earliest unconsumed message in the change tracking instance. Unit: seconds.
        # 
        # >  If the return value of this parameter is **-1**, no client is connected to the consumer group.
        self.message_delay = message_delay
        # The total number of unconsumed messages, which is the number of unconsumed data records plus the number of heartbeat messages.
        # 
        # >  If the return value of this parameter is **-1**, no client is connected to the consumer group.
        self.unconsumed_data = unconsumed_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.consumer_group_id is not None:
            result['ConsumerGroupID'] = self.consumer_group_id

        if self.consumer_group_name is not None:
            result['ConsumerGroupName'] = self.consumer_group_name

        if self.consumer_group_user_name is not None:
            result['ConsumerGroupUserName'] = self.consumer_group_user_name

        if self.consumption_checkpoint is not None:
            result['ConsumptionCheckpoint'] = self.consumption_checkpoint

        if self.message_delay is not None:
            result['MessageDelay'] = self.message_delay

        if self.unconsumed_data is not None:
            result['UnconsumedData'] = self.unconsumed_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsumerGroupID') is not None:
            self.consumer_group_id = m.get('ConsumerGroupID')

        if m.get('ConsumerGroupName') is not None:
            self.consumer_group_name = m.get('ConsumerGroupName')

        if m.get('ConsumerGroupUserName') is not None:
            self.consumer_group_user_name = m.get('ConsumerGroupUserName')

        if m.get('ConsumptionCheckpoint') is not None:
            self.consumption_checkpoint = m.get('ConsumptionCheckpoint')

        if m.get('MessageDelay') is not None:
            self.message_delay = m.get('MessageDelay')

        if m.get('UnconsumedData') is not None:
            self.unconsumed_data = m.get('UnconsumedData')

        return self

