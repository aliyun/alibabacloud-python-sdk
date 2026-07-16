# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mns_open20220119 import models as main_models
from darabonba.model import DaraModel

class ListSubscriptionByTopicResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.ListSubscriptionByTopicResponseBodyData = None,
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
        # The request ID.
        self.request_id = request_id
        # The response status.
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
            temp_model = main_models.ListSubscriptionByTopicResponseBodyData()
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

class ListSubscriptionByTopicResponseBodyData(DaraModel):
    def __init__(
        self,
        page_data: List[main_models.ListSubscriptionByTopicResponseBodyDataPageData] = None,
        page_num: int = None,
        page_size: int = None,
        pages: int = None,
        size: int = None,
        total: int = None,
    ):
        # The entries on the current page.
        self.page_data = page_data
        # The page number of the returned page.
        self.page_num = page_num
        # The number of entries returned per page.
        self.page_size = page_size
        # The total number of pages.
        self.pages = pages
        # The number of entries on the current page.
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
                temp_model = main_models.ListSubscriptionByTopicResponseBodyDataPageData()
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

class ListSubscriptionByTopicResponseBodyDataPageData(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        dlq_policy: main_models.ListSubscriptionByTopicResponseBodyDataPageDataDlqPolicy = None,
        endpoint: str = None,
        filter_tag: str = None,
        last_modify_time: int = None,
        notify_content_format: str = None,
        notify_strategy: str = None,
        subscription_name: str = None,
        topic_name: str = None,
        topic_owner: str = None,
    ):
        # The time when the subscription was created, in Unix time format.
        self.create_time = create_time
        # The dead-letter queue policy.
        self.dlq_policy = dlq_policy
        # The endpoint of the subscription.
        self.endpoint = endpoint
        # The tag for message filtering in the subscription. Only messages with the same tag are pushed.
        self.filter_tag = filter_tag
        # The time when the subscription properties were last modified. This value is a UNIX timestamp.
        self.last_modify_time = last_modify_time
        # The format of the message content pushed to the endpoint.
        # Valid values:
        # 
        # - XML
        # 
        # - JSON
        # 
        # - SIMPLIFIED
        self.notify_content_format = notify_content_format
        # The retry policy for message push failures to the endpoint. Valid values:
        # 
        # - BACKOFF_RETRY: backoff retry.
        # 
        # - EXPONENTIAL_DECAY_RETRY: exponential decay retry.
        self.notify_strategy = notify_strategy
        # The subscription name.
        self.subscription_name = subscription_name
        # The name of the topic to which the subscription belongs.
        self.topic_name = topic_name
        # The AccountId of the owner of the topic to which the subscription belongs.
        self.topic_owner = topic_owner

    def validate(self):
        if self.dlq_policy:
            self.dlq_policy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.dlq_policy is not None:
            result['DlqPolicy'] = self.dlq_policy.to_map()

        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint

        if self.filter_tag is not None:
            result['FilterTag'] = self.filter_tag

        if self.last_modify_time is not None:
            result['LastModifyTime'] = self.last_modify_time

        if self.notify_content_format is not None:
            result['NotifyContentFormat'] = self.notify_content_format

        if self.notify_strategy is not None:
            result['NotifyStrategy'] = self.notify_strategy

        if self.subscription_name is not None:
            result['SubscriptionName'] = self.subscription_name

        if self.topic_name is not None:
            result['TopicName'] = self.topic_name

        if self.topic_owner is not None:
            result['TopicOwner'] = self.topic_owner

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DlqPolicy') is not None:
            temp_model = main_models.ListSubscriptionByTopicResponseBodyDataPageDataDlqPolicy()
            self.dlq_policy = temp_model.from_map(m.get('DlqPolicy'))

        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')

        if m.get('FilterTag') is not None:
            self.filter_tag = m.get('FilterTag')

        if m.get('LastModifyTime') is not None:
            self.last_modify_time = m.get('LastModifyTime')

        if m.get('NotifyContentFormat') is not None:
            self.notify_content_format = m.get('NotifyContentFormat')

        if m.get('NotifyStrategy') is not None:
            self.notify_strategy = m.get('NotifyStrategy')

        if m.get('SubscriptionName') is not None:
            self.subscription_name = m.get('SubscriptionName')

        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')

        if m.get('TopicOwner') is not None:
            self.topic_owner = m.get('TopicOwner')

        return self

class ListSubscriptionByTopicResponseBodyDataPageDataDlqPolicy(DaraModel):
    def __init__(
        self,
        dead_letter_target_queue: str = None,
        enabled: bool = None,
    ):
        # The destination queue for dead-letter messages.
        self.dead_letter_target_queue = dead_letter_target_queue
        # Indicates whether dead-letter message delivery is enabled.
        self.enabled = enabled

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeadLetterTargetQueue') is not None:
            self.dead_letter_target_queue = m.get('DeadLetterTargetQueue')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        return self

