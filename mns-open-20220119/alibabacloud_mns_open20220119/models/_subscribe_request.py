# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_mns_open20220119 import models as main_models
from darabonba.model import DaraModel

class SubscribeRequest(DaraModel):
    def __init__(
        self,
        dlq_policy: main_models.SubscribeRequestDlqPolicy = None,
        dm_attributes: main_models.SubscribeRequestDmAttributes = None,
        dysms_attributes: main_models.SubscribeRequestDysmsAttributes = None,
        endpoint: str = None,
        kafka_attributes: main_models.SubscribeRequestKafkaAttributes = None,
        message_tag: str = None,
        notify_content_format: str = None,
        notify_strategy: str = None,
        push_type: str = None,
        sts_role_arn: str = None,
        subscription_name: str = None,
        tenant_rate_limit_policy: main_models.SubscribeRequestTenantRateLimitPolicy = None,
        topic_name: str = None,
    ):
        # The dead-letter queue policy.
        self.dlq_policy = dlq_policy
        # The attributes for Direct Mail push. This parameter is required when the PushType parameter is set to dm. The value is in JSON format and contains the following fields:
        # 
        # - AccountName: the sender address, which is the sender address configured in Direct Mail, such as notify@example.com.
        # - Subject: the email subject.
        self.dm_attributes = dm_attributes
        # The attributes for SMS push. This parameter is required when the PushType parameter is set to alisms. The value is in JSON format and contains the following fields:
        # 
        # - TemplateCode: the code of the SMS template, which can be obtained from the SMS console.
        # - SignName: the name of the SMS signature.
        self.dysms_attributes = dysms_attributes
        # ## Endpoint for receiving messages
        # 
        # The format varies based on the `PushType` parameter:
        # 
        # - `PushType=http`: The HTTP or HTTPS callback URL, such as `http://example.com/callback` or `https://example.com/callback`.
        # - `PushType=queue`: The ARN of the destination queue, in the format of `acs:mns:{RegionId}:{Alibaba Cloud account ID}:/queues/{QueueName}`.
        # - `PushType=dm`: The Direct Mail push endpoint, in the fixed format of `smq-ep:dm:{Alibaba Cloud account ID}:__dynamic`. Replace `{Alibaba Cloud account ID}` with the ID of your Alibaba Cloud account.
        # - `PushType=dysms`: The SMS push endpoint, in the format of `smq-ep:dysms:{Alibaba Cloud account ID}:{Phone number}`.
        # - `PushType=kafka`: The Kafka push endpoint. The Kafka push type is deprecated.
        # - `PushType=fc`: The Function Compute endpoint, in the format of `acs:fc:{RegionId}:{Alibaba Cloud account ID}:services/{ServiceName}/functions/{FunctionName}`.
        # - `PushType=eventbus`: The EventBridge endpoint, in the format of `acs:eventbridge:{RegionId}:{Alibaba Cloud account ID}:eventbus/{EventBusName}`.
        # 
        # This parameter is required.
        self.endpoint = endpoint
        # The Kafka push type is deprecated.
        self.kafka_attributes = kafka_attributes
        # The tag used for message filtering in the subscription. Only messages with a matching tag are pushed.
        # The value must be a string up to 16 characters in length.
        # 
        # By default, message filtering is not performed.
        self.message_tag = message_tag
        # ## Format of the pushed message content
        # 
        # Valid values:
        # 
        # - `XML`: XML format (default)
        # - `JSON`: JSON format
        # - `SIMPLIFIED`: original message body content without the SMQ metadata wrapper
        self.notify_content_format = notify_content_format
        # The retry strategy that is used when an error occurs during message pushing to the endpoint. Valid values:
        # 
        # - BACKOFF_RETRY: backoff retry (default)
        # - EXPONENTIAL_DECAY_RETRY: exponential decay retry
        self.notify_strategy = notify_strategy
        # ## Push types for subscriptions
        # 
        # Valid values:
        # 
        # - `http`: Pushes messages to the specified HTTP or HTTPS callback URL.
        # - `queue`: Pushes messages to the specified Simple Message Queue (SMQ) queue.
        # - `dm`: Sends notifications by using the Direct Mail service. You must also set the `DmAttributes` and `StsRoleArn` parameters.
        # - `dysms`: Sends notifications by using the Alibaba Cloud SMS service. You must also set the `DysmsAttributes` parameter.
        # - `fc`: Pushes messages to Alibaba Cloud Function Compute (FC).
        # - `eventbus`: Pushes messages to an EventBridge event bus.
        # 
        # **Note:**
        # The following values are deprecated and are retained only for compatibility with legacy subscriptions:
        # 
        # - `mpush`: mobile push
        # - `alisms`: legacy SMS
        # - `email`: legacy email, use `dm` instead
        # - `kafka`: deprecated Kafka push type
        # 
        # This parameter is required.
        self.push_type = push_type
        # The ARN of the RAM role assumed by the service. The format is acs:ram::{Alibaba Cloud account ID}:role/{RoleName}. Replace {Alibaba Cloud account ID} with the ID of the Alibaba Cloud account that calls the API operation.
        self.sts_role_arn = sts_role_arn
        # The name of the subscription. The name must be 1 to 255 characters in length. It must start with a letter or a digit, and can contain only letters, digits, and hyphens (-). The name cannot start with mns-reserved-.
        # 
        # This parameter is required.
        self.subscription_name = subscription_name
        # The throttling policy.
        self.tenant_rate_limit_policy = tenant_rate_limit_policy
        # The name of the topic. The name must be 1 to 255 characters in length. It must start with a letter or a digit, and can contain only letters, digits, and hyphens (-). The name cannot start with mns-reserved-.
        # 
        # This parameter is required.
        self.topic_name = topic_name

    def validate(self):
        if self.dlq_policy:
            self.dlq_policy.validate()
        if self.dm_attributes:
            self.dm_attributes.validate()
        if self.dysms_attributes:
            self.dysms_attributes.validate()
        if self.kafka_attributes:
            self.kafka_attributes.validate()
        if self.tenant_rate_limit_policy:
            self.tenant_rate_limit_policy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dlq_policy is not None:
            result['DlqPolicy'] = self.dlq_policy.to_map()

        if self.dm_attributes is not None:
            result['DmAttributes'] = self.dm_attributes.to_map()

        if self.dysms_attributes is not None:
            result['DysmsAttributes'] = self.dysms_attributes.to_map()

        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint

        if self.kafka_attributes is not None:
            result['KafkaAttributes'] = self.kafka_attributes.to_map()

        if self.message_tag is not None:
            result['MessageTag'] = self.message_tag

        if self.notify_content_format is not None:
            result['NotifyContentFormat'] = self.notify_content_format

        if self.notify_strategy is not None:
            result['NotifyStrategy'] = self.notify_strategy

        if self.push_type is not None:
            result['PushType'] = self.push_type

        if self.sts_role_arn is not None:
            result['StsRoleArn'] = self.sts_role_arn

        if self.subscription_name is not None:
            result['SubscriptionName'] = self.subscription_name

        if self.tenant_rate_limit_policy is not None:
            result['TenantRateLimitPolicy'] = self.tenant_rate_limit_policy.to_map()

        if self.topic_name is not None:
            result['TopicName'] = self.topic_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DlqPolicy') is not None:
            temp_model = main_models.SubscribeRequestDlqPolicy()
            self.dlq_policy = temp_model.from_map(m.get('DlqPolicy'))

        if m.get('DmAttributes') is not None:
            temp_model = main_models.SubscribeRequestDmAttributes()
            self.dm_attributes = temp_model.from_map(m.get('DmAttributes'))

        if m.get('DysmsAttributes') is not None:
            temp_model = main_models.SubscribeRequestDysmsAttributes()
            self.dysms_attributes = temp_model.from_map(m.get('DysmsAttributes'))

        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')

        if m.get('KafkaAttributes') is not None:
            temp_model = main_models.SubscribeRequestKafkaAttributes()
            self.kafka_attributes = temp_model.from_map(m.get('KafkaAttributes'))

        if m.get('MessageTag') is not None:
            self.message_tag = m.get('MessageTag')

        if m.get('NotifyContentFormat') is not None:
            self.notify_content_format = m.get('NotifyContentFormat')

        if m.get('NotifyStrategy') is not None:
            self.notify_strategy = m.get('NotifyStrategy')

        if m.get('PushType') is not None:
            self.push_type = m.get('PushType')

        if m.get('StsRoleArn') is not None:
            self.sts_role_arn = m.get('StsRoleArn')

        if m.get('SubscriptionName') is not None:
            self.subscription_name = m.get('SubscriptionName')

        if m.get('TenantRateLimitPolicy') is not None:
            temp_model = main_models.SubscribeRequestTenantRateLimitPolicy()
            self.tenant_rate_limit_policy = temp_model.from_map(m.get('TenantRateLimitPolicy'))

        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')

        return self

class SubscribeRequestTenantRateLimitPolicy(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        max_receives_per_second: int = None,
    ):
        # Specifies whether to enable the throttling policy. Valid values:
        # 
        # - true: enabled
        # - false: disabled (default)
        self.enabled = enabled
        # The maximum number of pushes or consumptions per second. The value must be a positive integer and is valid only when the PushType parameter is set to http or https. The specific minimum value varies by region.
        self.max_receives_per_second = max_receives_per_second

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.max_receives_per_second is not None:
            result['MaxReceivesPerSecond'] = self.max_receives_per_second

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('MaxReceivesPerSecond') is not None:
            self.max_receives_per_second = m.get('MaxReceivesPerSecond')

        return self

class SubscribeRequestKafkaAttributes(DaraModel):
    def __init__(
        self,
        business_mode: str = None,
    ):
        # The Kafka push type is deprecated.
        self.business_mode = business_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_mode is not None:
            result['BusinessMode'] = self.business_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessMode') is not None:
            self.business_mode = m.get('BusinessMode')

        return self

class SubscribeRequestDysmsAttributes(DaraModel):
    def __init__(
        self,
        sign_name: str = None,
        template_code: str = None,
    ):
        # The name of the SMS signature.
        self.sign_name = sign_name
        # The code of the SMS template.
        self.template_code = template_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.sign_name is not None:
            result['SignName'] = self.sign_name

        if self.template_code is not None:
            result['TemplateCode'] = self.template_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')

        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')

        return self

class SubscribeRequestDmAttributes(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        subject: str = None,
    ):
        # The sender address.
        self.account_name = account_name
        # The email subject.
        self.subject = subject

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.subject is not None:
            result['Subject'] = self.subject

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('Subject') is not None:
            self.subject = m.get('Subject')

        return self

class SubscribeRequestDlqPolicy(DaraModel):
    def __init__(
        self,
        dead_letter_target_queue: str = None,
        enabled: bool = None,
    ):
        # The destination queue for dead-letter message delivery. The queue must already exist in the current region.
        self.dead_letter_target_queue = dead_letter_target_queue
        # Specifies whether to enable dead-letter message delivery. Default value: false.
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

