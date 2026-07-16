# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mns_open20220119 import models as main_models
from darabonba.model import DaraModel

class ListQueueResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.ListQueueResponseBodyData = None,
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
        # The ID of the request.
        self.request_id = request_id
        # The status of the response.
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
            temp_model = main_models.ListQueueResponseBodyData()
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

class ListQueueResponseBodyData(DaraModel):
    def __init__(
        self,
        page_data: List[main_models.ListQueueResponseBodyDataPageData] = None,
        page_num: int = None,
        page_size: int = None,
        pages: int = None,
        size: int = None,
        total: int = None,
    ):
        # The results returned on the current page.
        self.page_data = page_data
        # The page number of the returned results.
        self.page_num = page_num
        # The maximum number of entries returned per page.
        self.page_size = page_size
        # The total number of pages.
        self.pages = pages
        # The number of entries returned on the current page.
        self.size = size
        # The total number of entries.
        self.total = total

    def validate(self):
        if self.page_data:
            for v1 in self.page_data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PageData'] = []
        if self.page_data is not None:
            for k1 in self.page_data:
                result['PageData'].append(k1.to_map() if k1 else None)

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.pages is not None:
            result['Pages'] = self.pages

        if self.size is not None:
            result['Size'] = self.size

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.page_data = []
        if m.get('PageData') is not None:
            for k1 in m.get('PageData'):
                temp_model = main_models.ListQueueResponseBodyDataPageData()
                self.page_data.append(temp_model.from_map(k1))

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Pages') is not None:
            self.pages = m.get('Pages')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListQueueResponseBodyDataPageData(DaraModel):
    def __init__(
        self,
        active_messages: int = None,
        create_time: int = None,
        delay_messages: int = None,
        delay_seconds: int = None,
        dlq_policy: main_models.ListQueueResponseBodyDataPageDataDlqPolicy = None,
        enable_sse: bool = None,
        encryption_enabled: bool = None,
        inactive_messages: int = None,
        kms_key_id: str = None,
        last_modify_time: int = None,
        logging_enabled: bool = None,
        maximum_message_size: int = None,
        message_retention_period: int = None,
        polling_wait_seconds: int = None,
        queue_name: str = None,
        queue_type: str = None,
        sse_algorithm: str = None,
        sse_type: str = None,
        tags: List[main_models.ListQueueResponseBodyDataPageDataTags] = None,
        visibility_timeout: int = None,
    ):
        # The approximate total number of messages in the Active state in this queue.
        # 
        # This field will default to 0 in the future and is not recommended. Use CloudMonitor API to retrieve this metric instead.
        self.active_messages = active_messages
        # The time when the queue was created. The value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.create_time = create_time
        # The approximate total number of messages in the Delayed state in this queue.
        # 
        # This field will default to 0 in the future and is not recommended. Use CloudMonitor API to retrieve this metric instead.
        self.delay_messages = delay_messages
        # The delay period after which all messages sent to this queue become consumable. Unit: seconds.
        self.delay_seconds = delay_seconds
        # The dead-letter queue policy.
        self.dlq_policy = dlq_policy
        self.enable_sse = enable_sse
        self.encryption_enabled = encryption_enabled
        # The approximate total number of messages in the Inactive state in this queue.
        # 
        # This field will default to 0 in the future and is not recommended. Use CloudMonitor API to retrieve this metric instead.
        self.inactive_messages = inactive_messages
        self.kms_key_id = kms_key_id
        # The most recent time when the queue attributes were modified. The value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.last_modify_time = last_modify_time
        # Indicates whether the log management feature is enabled.
        # 
        # - True: Enabled.
        # 
        # - False: Disabled.
        self.logging_enabled = logging_enabled
        # The maximum size of a message body that can be sent to this queue. Unit: bytes.
        self.maximum_message_size = maximum_message_size
        # The maximum period for which a message can be retained in this queue. After the specified period elapses since a message is sent to the queue, the message is deleted regardless of whether it has been consumed. Unit: seconds.
        self.message_retention_period = message_retention_period
        # The maximum wait time for a ReceiveMessage request when the queue is empty. Unit: seconds.
        self.polling_wait_seconds = polling_wait_seconds
        # The name of the queue.
        self.queue_name = queue_name
        # The type of the queue. Valid values:
        #    * normal: standard queue
        #    * fifo: FIFO queue
        self.queue_type = queue_type
        self.sse_algorithm = sse_algorithm
        self.sse_type = sse_type
        # The list of resource tags.
        self.tags = tags
        # The duration for which a message stays in the Inactive state after it is consumed from the queue.
        # 
        # Valid values: 1 to 43200. Unit: seconds.
        # 
        # Default value: 30.
        self.visibility_timeout = visibility_timeout

    def validate(self):
        if self.dlq_policy:
            self.dlq_policy.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active_messages is not None:
            result['ActiveMessages'] = self.active_messages

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.delay_messages is not None:
            result['DelayMessages'] = self.delay_messages

        if self.delay_seconds is not None:
            result['DelaySeconds'] = self.delay_seconds

        if self.dlq_policy is not None:
            result['DlqPolicy'] = self.dlq_policy.to_map()

        if self.enable_sse is not None:
            result['EnableSSE'] = self.enable_sse

        if self.encryption_enabled is not None:
            result['EncryptionEnabled'] = self.encryption_enabled

        if self.inactive_messages is not None:
            result['InactiveMessages'] = self.inactive_messages

        if self.kms_key_id is not None:
            result['KmsKeyId'] = self.kms_key_id

        if self.last_modify_time is not None:
            result['LastModifyTime'] = self.last_modify_time

        if self.logging_enabled is not None:
            result['LoggingEnabled'] = self.logging_enabled

        if self.maximum_message_size is not None:
            result['MaximumMessageSize'] = self.maximum_message_size

        if self.message_retention_period is not None:
            result['MessageRetentionPeriod'] = self.message_retention_period

        if self.polling_wait_seconds is not None:
            result['PollingWaitSeconds'] = self.polling_wait_seconds

        if self.queue_name is not None:
            result['QueueName'] = self.queue_name

        if self.queue_type is not None:
            result['QueueType'] = self.queue_type

        if self.sse_algorithm is not None:
            result['SseAlgorithm'] = self.sse_algorithm

        if self.sse_type is not None:
            result['SseType'] = self.sse_type

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.visibility_timeout is not None:
            result['VisibilityTimeout'] = self.visibility_timeout

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveMessages') is not None:
            self.active_messages = m.get('ActiveMessages')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DelayMessages') is not None:
            self.delay_messages = m.get('DelayMessages')

        if m.get('DelaySeconds') is not None:
            self.delay_seconds = m.get('DelaySeconds')

        if m.get('DlqPolicy') is not None:
            temp_model = main_models.ListQueueResponseBodyDataPageDataDlqPolicy()
            self.dlq_policy = temp_model.from_map(m.get('DlqPolicy'))

        if m.get('EnableSSE') is not None:
            self.enable_sse = m.get('EnableSSE')

        if m.get('EncryptionEnabled') is not None:
            self.encryption_enabled = m.get('EncryptionEnabled')

        if m.get('InactiveMessages') is not None:
            self.inactive_messages = m.get('InactiveMessages')

        if m.get('KmsKeyId') is not None:
            self.kms_key_id = m.get('KmsKeyId')

        if m.get('LastModifyTime') is not None:
            self.last_modify_time = m.get('LastModifyTime')

        if m.get('LoggingEnabled') is not None:
            self.logging_enabled = m.get('LoggingEnabled')

        if m.get('MaximumMessageSize') is not None:
            self.maximum_message_size = m.get('MaximumMessageSize')

        if m.get('MessageRetentionPeriod') is not None:
            self.message_retention_period = m.get('MessageRetentionPeriod')

        if m.get('PollingWaitSeconds') is not None:
            self.polling_wait_seconds = m.get('PollingWaitSeconds')

        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')

        if m.get('QueueType') is not None:
            self.queue_type = m.get('QueueType')

        if m.get('SseAlgorithm') is not None:
            self.sse_algorithm = m.get('SseAlgorithm')

        if m.get('SseType') is not None:
            self.sse_type = m.get('SseType')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListQueueResponseBodyDataPageDataTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('VisibilityTimeout') is not None:
            self.visibility_timeout = m.get('VisibilityTimeout')

        return self

class ListQueueResponseBodyDataPageDataTags(DaraModel):
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

class ListQueueResponseBodyDataPageDataDlqPolicy(DaraModel):
    def __init__(
        self,
        dead_letter_target_queue: str = None,
        enabled: bool = None,
        max_receive_count: str = None,
    ):
        # The target queue for dead-letter message delivery.
        self.dead_letter_target_queue = dead_letter_target_queue
        # Indicates whether dead-letter message delivery is enabled.
        self.enabled = enabled
        # The maximum number of times a message can be delivered.
        self.max_receive_count = max_receive_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dead_letter_target_queue is not None:
            result['DeadLetterTargetQueue'] = self.dead_letter_target_queue

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.max_receive_count is not None:
            result['MaxReceiveCount'] = self.max_receive_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeadLetterTargetQueue') is not None:
            self.dead_letter_target_queue = m.get('DeadLetterTargetQueue')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('MaxReceiveCount') is not None:
            self.max_receive_count = m.get('MaxReceiveCount')

        return self

