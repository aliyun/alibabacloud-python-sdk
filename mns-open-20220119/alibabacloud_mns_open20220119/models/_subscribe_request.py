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
        # The email push attributes. This parameter is required when PushType is set to dm. The value is in JSON format and contains the following fields:
        # 
        # - AccountName: The sender address configured in DirectMail (such as notify@example.com).
        # - Subject: The email subject.
        self.dm_attributes = dm_attributes
        # The SMS push attributes. This parameter is required when PushType is set to alisms. The value is in JSON format and contains the following fields:
        # 
        # - TemplateCode: The SMS template code, which can be obtained from the Short Message Service console.
        # - SignName: The SMS signature name.
        self.dysms_attributes = dysms_attributes
        # ## Endpoint address for receiving messages
        # 
        # The format varies depending on the value of `PushType`:
        # 
        # - `PushType=http`: An HTTP/HTTPS callback URL, such as `http://example.com/callback` or `https://example.com/callback`.
        # - `PushType=queue`: The ARN of the destination queue, in the format `acs:mns:{RegionId}:{Alibaba Cloud account ID}:queues/{QueueName}`.
        # - `PushType=dm`: The email push endpoint, in the fixed format `smq-ep:dm:{Alibaba Cloud account ID}:__dynamic`. Replace `{Alibaba Cloud account ID}` with your Alibaba Cloud account ID.
        # - `PushType=dysms`: The SMS push endpoint, in the format `smq-ep:dysms:{Alibaba Cloud account ID}:{PhoneNumber}`.
        # - `PushType=kafka`: The Kafka push endpoint. The Kafka push type is deprecated.
        # - `PushType=fc`: The Function Compute endpoint, in the format `acs:fc:{RegionId}:{Alibaba Cloud account ID}:services/{ServiceName}/functions/{FunctionName}`.
        # - `PushType=eventbus`: The EventBridge endpoint, in the format `acs:eventbridge:{RegionId}:{Alibaba Cloud account ID}:eventbus/{EventBusName}`.
        # 
        # This parameter is required.
        self.endpoint = endpoint
        # The Kafka push type is deprecated.
        self.kafka_attributes = kafka_attributes
        # The tag used for message filtering in this subscription. Only messages with a matching tag are pushed. The value is a string of up to 16 characters.
        # 
        # By default, no message filtering is applied.
        self.message_tag = message_tag
        # ## Format of the pushed message content
        # 
        # Valid values:
        # 
        # - `XML`: The message body is pushed in XML format. This is the default value.
        # - `JSON`: The message body is pushed in JSON format.
        # - `SIMPLIFIED`: Only the raw message body content is pushed, without SMQ metadata wrapping.
        self.notify_content_format = notify_content_format
        # The retry strategy when an error occurs while pushing messages to the endpoint. Valid values:
        # 
        # - BACKOFF_RETRY: backoff retry.
        # 
        # - EXPONENTIAL_DECAY_RETRY: exponential decay retry.
        self.notify_strategy = notify_strategy
        # ## Push type of the subscription
        # 
        # Valid values:
        # 
        # - `http`: HTTP/HTTPS push. Pushes messages to a specified HTTP or HTTPS callback URL.
        # - `queue`: Queue push. Pushes messages to a specified SMQ queue.
        # - `dm`: Email push. Sends notifications through DirectMail. You must also set the `DmAttributes` and `StsRoleArn` parameters.
        # - `dysms`: SMS push. Sends notifications through Alibaba Cloud Short Message Service. You must also set the `DysmsAttributes` parameter.
        # 
        # - `fc`: Function Compute push. Pushes messages to Alibaba Cloud Function Compute (FC).
        # - `eventbus`: EventBridge push. Pushes messages to an EventBridge event bus.
        # 
        # **Note:**
        # The following values are deprecated and are only used for compatibility with legacy subscriptions:
        # 
        # - `mpush`: Mobile push.
        # - `alisms`: Legacy SMS.
        # - `email`: Legacy email. Use `dm` instead.
        # - `kafka`: Kafka push type is deprecated.
        # 
        # This parameter is required.
        self.push_type = push_type
        # The ARN of the RAM role assumed by the service. The format is acs:ram::{Alibaba Cloud account ID}:role/{RoleName}. Replace {Alibaba Cloud account ID} with the Alibaba Cloud account ID that calls the API operation.
        self.sts_role_arn = sts_role_arn
        # The name of the subscription.
        # 
        # This parameter is required.
        self.subscription_name = subscription_name
        # The throttling policy.
        self.tenant_rate_limit_policy = tenant_rate_limit_policy
        # The name of the topic.
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
        # Specifies whether to enable the throttling policy. Valid values: true and false.
        self.enabled = enabled
        # The maximum number of pushes or consumptions per second.
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
        # The SMS signature name.
        self.sign_name = sign_name
        # The SMS template code.
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
        # The destination queue for dead-letter message delivery.
        self.dead_letter_target_queue = dead_letter_target_queue
        # Specifies whether to enable dead-letter message delivery.
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

