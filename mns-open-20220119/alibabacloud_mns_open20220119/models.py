# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, Any, List


class CreateQueueRequest(TeaModel):
    def __init__(
        self,
        delay_seconds: int = None,
        enable_logging: bool = None,
        maximum_message_size: int = None,
        message_retention_period: int = None,
        polling_wait_seconds: int = None,
        queue_name: str = None,
        visibility_timeout: int = None,
    ):
        self.delay_seconds = delay_seconds
        self.enable_logging = enable_logging
        self.maximum_message_size = maximum_message_size
        self.message_retention_period = message_retention_period
        self.polling_wait_seconds = polling_wait_seconds
        self.queue_name = queue_name
        self.visibility_timeout = visibility_timeout

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delay_seconds is not None:
            result['DelaySeconds'] = self.delay_seconds
        if self.enable_logging is not None:
            result['EnableLogging'] = self.enable_logging
        if self.maximum_message_size is not None:
            result['MaximumMessageSize'] = self.maximum_message_size
        if self.message_retention_period is not None:
            result['MessageRetentionPeriod'] = self.message_retention_period
        if self.polling_wait_seconds is not None:
            result['PollingWaitSeconds'] = self.polling_wait_seconds
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.visibility_timeout is not None:
            result['VisibilityTimeout'] = self.visibility_timeout
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DelaySeconds') is not None:
            self.delay_seconds = m.get('DelaySeconds')
        if m.get('EnableLogging') is not None:
            self.enable_logging = m.get('EnableLogging')
        if m.get('MaximumMessageSize') is not None:
            self.maximum_message_size = m.get('MaximumMessageSize')
        if m.get('MessageRetentionPeriod') is not None:
            self.message_retention_period = m.get('MessageRetentionPeriod')
        if m.get('PollingWaitSeconds') is not None:
            self.polling_wait_seconds = m.get('PollingWaitSeconds')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('VisibilityTimeout') is not None:
            self.visibility_timeout = m.get('VisibilityTimeout')
        return self


class CreateQueueResponseBodyData(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateQueueResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: CreateQueueResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.status = status
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = CreateQueueResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateQueueResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateQueueResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateQueueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTopicRequest(TeaModel):
    def __init__(
        self,
        enable_logging: bool = None,
        max_message_size: int = None,
        topic_name: str = None,
    ):
        self.enable_logging = enable_logging
        self.max_message_size = max_message_size
        self.topic_name = topic_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_logging is not None:
            result['EnableLogging'] = self.enable_logging
        if self.max_message_size is not None:
            result['MaxMessageSize'] = self.max_message_size
        if self.topic_name is not None:
            result['TopicName'] = self.topic_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableLogging') is not None:
            self.enable_logging = m.get('EnableLogging')
        if m.get('MaxMessageSize') is not None:
            self.max_message_size = m.get('MaxMessageSize')
        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')
        return self


class CreateTopicResponseBodyData(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateTopicResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: CreateTopicResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.status = status
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = CreateTopicResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateTopicResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateTopicResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateTopicResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteQueueRequest(TeaModel):
    def __init__(
        self,
        queue_name: str = None,
    ):
        self.queue_name = queue_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        return self


class DeleteQueueResponseBodyData(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteQueueResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: DeleteQueueResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.status = status
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = DeleteQueueResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteQueueResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteQueueResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteQueueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTopicRequest(TeaModel):
    def __init__(
        self,
        topic_name: str = None,
    ):
        self.topic_name = topic_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.topic_name is not None:
            result['TopicName'] = self.topic_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')
        return self


class DeleteTopicResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: Dict[str, Any] = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.status = status
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteTopicResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteTopicResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteTopicResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetQueueAttributesRequest(TeaModel):
    def __init__(
        self,
        queue_name: str = None,
    ):
        self.queue_name = queue_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        return self


class GetQueueAttributesResponseBodyData(TeaModel):
    def __init__(
        self,
        active_messages: int = None,
        create_time: int = None,
        delay_messages: int = None,
        delay_seconds: int = None,
        inactive_messages: int = None,
        last_modify_time: int = None,
        logging_enabled: bool = None,
        maximum_message_size: int = None,
        message_retention_period: int = None,
        polling_wait_seconds: int = None,
        queue_name: str = None,
        visibility_timeout: int = None,
    ):
        self.active_messages = active_messages
        self.create_time = create_time
        self.delay_messages = delay_messages
        self.delay_seconds = delay_seconds
        self.inactive_messages = inactive_messages
        self.last_modify_time = last_modify_time
        self.logging_enabled = logging_enabled
        self.maximum_message_size = maximum_message_size
        self.message_retention_period = message_retention_period
        self.polling_wait_seconds = polling_wait_seconds
        self.queue_name = queue_name
        self.visibility_timeout = visibility_timeout

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active_messages is not None:
            result['ActiveMessages'] = self.active_messages
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.delay_messages is not None:
            result['DelayMessages'] = self.delay_messages
        if self.delay_seconds is not None:
            result['DelaySeconds'] = self.delay_seconds
        if self.inactive_messages is not None:
            result['InactiveMessages'] = self.inactive_messages
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
        if m.get('InactiveMessages') is not None:
            self.inactive_messages = m.get('InactiveMessages')
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
        if m.get('VisibilityTimeout') is not None:
            self.visibility_timeout = m.get('VisibilityTimeout')
        return self


class GetQueueAttributesResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetQueueAttributesResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.status = status
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = GetQueueAttributesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetQueueAttributesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetQueueAttributesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetQueueAttributesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSubscriptionAttributesRequest(TeaModel):
    def __init__(
        self,
        subscription_name: str = None,
        topic_name: str = None,
    ):
        self.subscription_name = subscription_name
        self.topic_name = topic_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.subscription_name is not None:
            result['SubscriptionName'] = self.subscription_name
        if self.topic_name is not None:
            result['TopicName'] = self.topic_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SubscriptionName') is not None:
            self.subscription_name = m.get('SubscriptionName')
        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')
        return self


class GetSubscriptionAttributesResponseBodyData(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        endpoint: str = None,
        filter_tag: str = None,
        last_modify_time: int = None,
        notify_content_format: str = None,
        notify_strategy: str = None,
        subscription_name: str = None,
        topic_name: str = None,
        topic_owner: str = None,
    ):
        self.create_time = create_time
        self.endpoint = endpoint
        self.filter_tag = filter_tag
        self.last_modify_time = last_modify_time
        self.notify_content_format = notify_content_format
        self.notify_strategy = notify_strategy
        self.subscription_name = subscription_name
        self.topic_name = topic_name
        self.topic_owner = topic_owner

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
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


class GetSubscriptionAttributesResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetSubscriptionAttributesResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.status = status
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = GetSubscriptionAttributesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetSubscriptionAttributesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSubscriptionAttributesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetSubscriptionAttributesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTopicAttributesRequest(TeaModel):
    def __init__(
        self,
        topic_name: str = None,
    ):
        self.topic_name = topic_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.topic_name is not None:
            result['TopicName'] = self.topic_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')
        return self


class GetTopicAttributesResponseBodyData(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        last_modify_time: int = None,
        logging_enabled: bool = None,
        max_message_size: int = None,
        message_count: int = None,
        message_retention_period: int = None,
        topic_name: str = None,
    ):
        self.create_time = create_time
        self.last_modify_time = last_modify_time
        self.logging_enabled = logging_enabled
        self.max_message_size = max_message_size
        self.message_count = message_count
        self.message_retention_period = message_retention_period
        self.topic_name = topic_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.last_modify_time is not None:
            result['LastModifyTime'] = self.last_modify_time
        if self.logging_enabled is not None:
            result['LoggingEnabled'] = self.logging_enabled
        if self.max_message_size is not None:
            result['MaxMessageSize'] = self.max_message_size
        if self.message_count is not None:
            result['MessageCount'] = self.message_count
        if self.message_retention_period is not None:
            result['MessageRetentionPeriod'] = self.message_retention_period
        if self.topic_name is not None:
            result['TopicName'] = self.topic_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('LastModifyTime') is not None:
            self.last_modify_time = m.get('LastModifyTime')
        if m.get('LoggingEnabled') is not None:
            self.logging_enabled = m.get('LoggingEnabled')
        if m.get('MaxMessageSize') is not None:
            self.max_message_size = m.get('MaxMessageSize')
        if m.get('MessageCount') is not None:
            self.message_count = m.get('MessageCount')
        if m.get('MessageRetentionPeriod') is not None:
            self.message_retention_period = m.get('MessageRetentionPeriod')
        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')
        return self


class GetTopicAttributesResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetTopicAttributesResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.status = status
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = GetTopicAttributesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetTopicAttributesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTopicAttributesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetTopicAttributesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListQueueRequest(TeaModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
        queue_name: str = None,
    ):
        self.page_num = page_num
        self.page_size = page_size
        self.queue_name = queue_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        return self


class ListQueueResponseBodyDataPageData(TeaModel):
    def __init__(
        self,
        active_messages: int = None,
        create_time: int = None,
        delay_messages: int = None,
        delay_seconds: int = None,
        inactive_messages: int = None,
        last_modify_time: int = None,
        logging_enabled: bool = None,
        maximum_message_size: int = None,
        message_retention_period: int = None,
        polling_wait_seconds: int = None,
        queue_name: str = None,
        visibility_timeout: int = None,
    ):
        self.active_messages = active_messages
        self.create_time = create_time
        self.delay_messages = delay_messages
        self.delay_seconds = delay_seconds
        self.inactive_messages = inactive_messages
        self.last_modify_time = last_modify_time
        self.logging_enabled = logging_enabled
        self.maximum_message_size = maximum_message_size
        self.message_retention_period = message_retention_period
        self.polling_wait_seconds = polling_wait_seconds
        self.queue_name = queue_name
        self.visibility_timeout = visibility_timeout

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active_messages is not None:
            result['ActiveMessages'] = self.active_messages
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.delay_messages is not None:
            result['DelayMessages'] = self.delay_messages
        if self.delay_seconds is not None:
            result['DelaySeconds'] = self.delay_seconds
        if self.inactive_messages is not None:
            result['InactiveMessages'] = self.inactive_messages
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
        if m.get('InactiveMessages') is not None:
            self.inactive_messages = m.get('InactiveMessages')
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
        if m.get('VisibilityTimeout') is not None:
            self.visibility_timeout = m.get('VisibilityTimeout')
        return self


class ListQueueResponseBodyData(TeaModel):
    def __init__(
        self,
        page_data: List[ListQueueResponseBodyDataPageData] = None,
        page_num: int = None,
        page_size: int = None,
        pages: int = None,
        size: int = None,
        total: int = None,
    ):
        self.page_data = page_data
        self.page_num = page_num
        self.page_size = page_size
        self.pages = pages
        self.size = size
        self.total = total

    def validate(self):
        if self.page_data:
            for k in self.page_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PageData'] = []
        if self.page_data is not None:
            for k in self.page_data:
                result['PageData'].append(k.to_map() if k else None)
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
            for k in m.get('PageData'):
                temp_model = ListQueueResponseBodyDataPageData()
                self.page_data.append(temp_model.from_map(k))
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


class ListQueueResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: ListQueueResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.status = status
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = ListQueueResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListQueueResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListQueueResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListQueueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSubscriptionByTopicRequest(TeaModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
        subscription_name: str = None,
        topic_name: str = None,
    ):
        self.page_num = page_num
        self.page_size = page_size
        self.subscription_name = subscription_name
        self.topic_name = topic_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.subscription_name is not None:
            result['SubscriptionName'] = self.subscription_name
        if self.topic_name is not None:
            result['TopicName'] = self.topic_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SubscriptionName') is not None:
            self.subscription_name = m.get('SubscriptionName')
        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')
        return self


class ListSubscriptionByTopicResponseBodyDataPageData(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        endpoint: str = None,
        filter_tag: str = None,
        last_modify_time: int = None,
        notify_content_format: str = None,
        notify_strategy: str = None,
        subscription_name: str = None,
        topic_name: str = None,
        topic_owner: str = None,
    ):
        self.create_time = create_time
        self.endpoint = endpoint
        self.filter_tag = filter_tag
        self.last_modify_time = last_modify_time
        self.notify_content_format = notify_content_format
        self.notify_strategy = notify_strategy
        self.subscription_name = subscription_name
        self.topic_name = topic_name
        self.topic_owner = topic_owner

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
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


class ListSubscriptionByTopicResponseBodyData(TeaModel):
    def __init__(
        self,
        page_data: List[ListSubscriptionByTopicResponseBodyDataPageData] = None,
        page_num: int = None,
        page_size: int = None,
        pages: int = None,
        size: int = None,
        total: int = None,
    ):
        self.page_data = page_data
        self.page_num = page_num
        self.page_size = page_size
        self.pages = pages
        self.size = size
        self.total = total

    def validate(self):
        if self.page_data:
            for k in self.page_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PageData'] = []
        if self.page_data is not None:
            for k in self.page_data:
                result['PageData'].append(k.to_map() if k else None)
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
            for k in m.get('PageData'):
                temp_model = ListSubscriptionByTopicResponseBodyDataPageData()
                self.page_data.append(temp_model.from_map(k))
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


class ListSubscriptionByTopicResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: ListSubscriptionByTopicResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.status = status
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = ListSubscriptionByTopicResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListSubscriptionByTopicResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListSubscriptionByTopicResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListSubscriptionByTopicResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTopicRequest(TeaModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
        topic_name: str = None,
    ):
        self.page_num = page_num
        self.page_size = page_size
        self.topic_name = topic_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.topic_name is not None:
            result['TopicName'] = self.topic_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')
        return self


class ListTopicResponseBodyDataPageData(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        last_modify_time: int = None,
        logging_enabled: bool = None,
        max_message_size: int = None,
        message_count: int = None,
        message_retention_period: int = None,
        topic_inner_url: str = None,
        topic_name: str = None,
        topic_url: str = None,
    ):
        self.create_time = create_time
        self.last_modify_time = last_modify_time
        self.logging_enabled = logging_enabled
        self.max_message_size = max_message_size
        self.message_count = message_count
        self.message_retention_period = message_retention_period
        self.topic_inner_url = topic_inner_url
        self.topic_name = topic_name
        self.topic_url = topic_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.last_modify_time is not None:
            result['LastModifyTime'] = self.last_modify_time
        if self.logging_enabled is not None:
            result['LoggingEnabled'] = self.logging_enabled
        if self.max_message_size is not None:
            result['MaxMessageSize'] = self.max_message_size
        if self.message_count is not None:
            result['MessageCount'] = self.message_count
        if self.message_retention_period is not None:
            result['MessageRetentionPeriod'] = self.message_retention_period
        if self.topic_inner_url is not None:
            result['TopicInnerUrl'] = self.topic_inner_url
        if self.topic_name is not None:
            result['TopicName'] = self.topic_name
        if self.topic_url is not None:
            result['TopicUrl'] = self.topic_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('LastModifyTime') is not None:
            self.last_modify_time = m.get('LastModifyTime')
        if m.get('LoggingEnabled') is not None:
            self.logging_enabled = m.get('LoggingEnabled')
        if m.get('MaxMessageSize') is not None:
            self.max_message_size = m.get('MaxMessageSize')
        if m.get('MessageCount') is not None:
            self.message_count = m.get('MessageCount')
        if m.get('MessageRetentionPeriod') is not None:
            self.message_retention_period = m.get('MessageRetentionPeriod')
        if m.get('TopicInnerUrl') is not None:
            self.topic_inner_url = m.get('TopicInnerUrl')
        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')
        if m.get('TopicUrl') is not None:
            self.topic_url = m.get('TopicUrl')
        return self


class ListTopicResponseBodyData(TeaModel):
    def __init__(
        self,
        page_data: List[ListTopicResponseBodyDataPageData] = None,
        page_num: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.page_data = page_data
        self.page_num = page_num
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.page_data:
            for k in self.page_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PageData'] = []
        if self.page_data is not None:
            for k in self.page_data:
                result['PageData'].append(k.to_map() if k else None)
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.page_data = []
        if m.get('PageData') is not None:
            for k in m.get('PageData'):
                temp_model = ListTopicResponseBodyDataPageData()
                self.page_data.append(temp_model.from_map(k))
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListTopicResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: ListTopicResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.status = status
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = ListTopicResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListTopicResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTopicResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTopicResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetQueueAttributesRequest(TeaModel):
    def __init__(
        self,
        delay_seconds: int = None,
        enable_logging: bool = None,
        maximum_message_size: int = None,
        message_retention_period: int = None,
        polling_wait_seconds: int = None,
        queue_name: str = None,
        visibility_timeout: int = None,
    ):
        self.delay_seconds = delay_seconds
        self.enable_logging = enable_logging
        self.maximum_message_size = maximum_message_size
        self.message_retention_period = message_retention_period
        self.polling_wait_seconds = polling_wait_seconds
        self.queue_name = queue_name
        self.visibility_timeout = visibility_timeout

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delay_seconds is not None:
            result['DelaySeconds'] = self.delay_seconds
        if self.enable_logging is not None:
            result['EnableLogging'] = self.enable_logging
        if self.maximum_message_size is not None:
            result['MaximumMessageSize'] = self.maximum_message_size
        if self.message_retention_period is not None:
            result['MessageRetentionPeriod'] = self.message_retention_period
        if self.polling_wait_seconds is not None:
            result['PollingWaitSeconds'] = self.polling_wait_seconds
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.visibility_timeout is not None:
            result['VisibilityTimeout'] = self.visibility_timeout
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DelaySeconds') is not None:
            self.delay_seconds = m.get('DelaySeconds')
        if m.get('EnableLogging') is not None:
            self.enable_logging = m.get('EnableLogging')
        if m.get('MaximumMessageSize') is not None:
            self.maximum_message_size = m.get('MaximumMessageSize')
        if m.get('MessageRetentionPeriod') is not None:
            self.message_retention_period = m.get('MessageRetentionPeriod')
        if m.get('PollingWaitSeconds') is not None:
            self.polling_wait_seconds = m.get('PollingWaitSeconds')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('VisibilityTimeout') is not None:
            self.visibility_timeout = m.get('VisibilityTimeout')
        return self


class SetQueueAttributesResponseBodyData(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SetQueueAttributesResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: SetQueueAttributesResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.status = status
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = SetQueueAttributesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SetQueueAttributesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetQueueAttributesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SetQueueAttributesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetSubscriptionAttributesRequest(TeaModel):
    def __init__(
        self,
        notify_strategy: str = None,
        subscription_name: str = None,
        topic_name: str = None,
    ):
        self.notify_strategy = notify_strategy
        self.subscription_name = subscription_name
        self.topic_name = topic_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.notify_strategy is not None:
            result['NotifyStrategy'] = self.notify_strategy
        if self.subscription_name is not None:
            result['SubscriptionName'] = self.subscription_name
        if self.topic_name is not None:
            result['TopicName'] = self.topic_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NotifyStrategy') is not None:
            self.notify_strategy = m.get('NotifyStrategy')
        if m.get('SubscriptionName') is not None:
            self.subscription_name = m.get('SubscriptionName')
        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')
        return self


class SetSubscriptionAttributesResponseBodyData(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SetSubscriptionAttributesResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: SetSubscriptionAttributesResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.status = status
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = SetSubscriptionAttributesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SetSubscriptionAttributesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetSubscriptionAttributesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SetSubscriptionAttributesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetTopicAttributesRequest(TeaModel):
    def __init__(
        self,
        enable_logging: bool = None,
        max_message_size: int = None,
        topic_name: str = None,
    ):
        self.enable_logging = enable_logging
        self.max_message_size = max_message_size
        self.topic_name = topic_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_logging is not None:
            result['EnableLogging'] = self.enable_logging
        if self.max_message_size is not None:
            result['MaxMessageSize'] = self.max_message_size
        if self.topic_name is not None:
            result['TopicName'] = self.topic_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableLogging') is not None:
            self.enable_logging = m.get('EnableLogging')
        if m.get('MaxMessageSize') is not None:
            self.max_message_size = m.get('MaxMessageSize')
        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')
        return self


class SetTopicAttributesResponseBodyData(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SetTopicAttributesResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: SetTopicAttributesResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.status = status
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = SetTopicAttributesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SetTopicAttributesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetTopicAttributesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SetTopicAttributesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubscribeRequest(TeaModel):
    def __init__(
        self,
        endpoint: str = None,
        message_tag: str = None,
        notify_content_format: str = None,
        notify_strategy: str = None,
        push_type: str = None,
        subscription_name: str = None,
        topic_name: str = None,
    ):
        self.endpoint = endpoint
        self.message_tag = message_tag
        self.notify_content_format = notify_content_format
        self.notify_strategy = notify_strategy
        self.push_type = push_type
        self.subscription_name = subscription_name
        self.topic_name = topic_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.message_tag is not None:
            result['MessageTag'] = self.message_tag
        if self.notify_content_format is not None:
            result['NotifyContentFormat'] = self.notify_content_format
        if self.notify_strategy is not None:
            result['NotifyStrategy'] = self.notify_strategy
        if self.push_type is not None:
            result['PushType'] = self.push_type
        if self.subscription_name is not None:
            result['SubscriptionName'] = self.subscription_name
        if self.topic_name is not None:
            result['TopicName'] = self.topic_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('MessageTag') is not None:
            self.message_tag = m.get('MessageTag')
        if m.get('NotifyContentFormat') is not None:
            self.notify_content_format = m.get('NotifyContentFormat')
        if m.get('NotifyStrategy') is not None:
            self.notify_strategy = m.get('NotifyStrategy')
        if m.get('PushType') is not None:
            self.push_type = m.get('PushType')
        if m.get('SubscriptionName') is not None:
            self.subscription_name = m.get('SubscriptionName')
        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')
        return self


class SubscribeResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.status = status
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SubscribeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubscribeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SubscribeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnsubscribeRequest(TeaModel):
    def __init__(
        self,
        subscription_name: str = None,
        topic_name: str = None,
    ):
        self.subscription_name = subscription_name
        self.topic_name = topic_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.subscription_name is not None:
            result['SubscriptionName'] = self.subscription_name
        if self.topic_name is not None:
            result['TopicName'] = self.topic_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SubscriptionName') is not None:
            self.subscription_name = m.get('SubscriptionName')
        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')
        return self


class UnsubscribeResponseBodyData(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UnsubscribeResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: UnsubscribeResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.status = status
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = UnsubscribeResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UnsubscribeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UnsubscribeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UnsubscribeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


