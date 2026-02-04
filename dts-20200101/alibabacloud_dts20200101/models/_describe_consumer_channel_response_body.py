# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dts20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeConsumerChannelResponseBody(DaraModel):
    def __init__(
        self,
        consumer_channels: List[main_models.DescribeConsumerChannelResponseBodyConsumerChannels] = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: str = None,
        page_number: int = None,
        page_record_count: int = None,
        request_id: str = None,
        success: str = None,
        total_record_count: int = None,
    ):
        # The details of the consumer groups.
        self.consumer_channels = consumer_channels
        # The error code returned if the request failed.
        self.err_code = err_code
        # The error message returned if the request failed.
        self.err_message = err_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The number of the returned page.
        self.page_number = page_number
        # The maximum number of consumer groups that can be displayed on one page.
        self.page_record_count = page_record_count
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success
        # The total number of consumer groups.
        self.total_record_count = total_record_count

    def validate(self):
        if self.consumer_channels:
            for v1 in self.consumer_channels:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ConsumerChannels'] = []
        if self.consumer_channels is not None:
            for k1 in self.consumer_channels:
                result['ConsumerChannels'].append(k1.to_map() if k1 else None)

        if self.err_code is not None:
            result['ErrCode'] = self.err_code

        if self.err_message is not None:
            result['ErrMessage'] = self.err_message

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

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
        self.consumer_channels = []
        if m.get('ConsumerChannels') is not None:
            for k1 in m.get('ConsumerChannels'):
                temp_model = main_models.DescribeConsumerChannelResponseBodyConsumerChannels()
                self.consumer_channels.append(temp_model.from_map(k1))

        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')

        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

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

class DescribeConsumerChannelResponseBodyConsumerChannels(DaraModel):
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
        # The consumption checkpoint, which is the time when the latest data record was consumed by the change tracking client. The time is displayed in the yyyy-MM-ddTHH:mm:ssZ format in UTC.
        self.consumption_checkpoint = consumption_checkpoint
        # The message latency, which is the timestamp of the latest data consumed by the downstream client minus the timestamp of the latest data tracked by the change tracking task. The value is a UNIX timestamp. Unit: seconds.
        # 
        # For example, the latest data in the source database is generated at 10:00. The change tracking task reads the data generated at 09:55, and the downstream client consumes the data generated at 09:30. In this case, the message latency is the UNIX timestamp difference between 09:55 and 09:30.
        # 
        # >  If the return value of this parameter is **-1**, no client is connected to the consumer group.
        self.message_delay = message_delay
        # The total number of unconsumed messages, which is the number of unconsumed data records plus the number of heartbeat messages.
        # 
        # >  If the return value of this parameter is -1, no client is connected to the consumer group.
        self.unconsumed_data = unconsumed_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.consumer_group_id is not None:
            result['ConsumerGroupId'] = self.consumer_group_id

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
        if m.get('ConsumerGroupId') is not None:
            self.consumer_group_id = m.get('ConsumerGroupId')

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

