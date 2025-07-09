# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict, Any


class DataTopicLagMapValue(TeaModel):
    def __init__(
        self,
        ready_count: int = None,
        inflight_count: int = None,
        delivery_duration: int = None,
        last_consume_timestamp: int = None,
    ):
        # Ready message count
        self.ready_count = ready_count
        # The number of messages being consumed.
        self.inflight_count = inflight_count
        # Delivery delay time, in seconds
        self.delivery_duration = delivery_duration
        # lastConsumeTimestamp
        self.last_consume_timestamp = last_consume_timestamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ready_count is not None:
            result['readyCount'] = self.ready_count
        if self.inflight_count is not None:
            result['inflightCount'] = self.inflight_count
        if self.delivery_duration is not None:
            result['deliveryDuration'] = self.delivery_duration
        if self.last_consume_timestamp is not None:
            result['lastConsumeTimestamp'] = self.last_consume_timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('readyCount') is not None:
            self.ready_count = m.get('readyCount')
        if m.get('inflightCount') is not None:
            self.inflight_count = m.get('inflightCount')
        if m.get('deliveryDuration') is not None:
            self.delivery_duration = m.get('deliveryDuration')
        if m.get('lastConsumeTimestamp') is not None:
            self.last_consume_timestamp = m.get('lastConsumeTimestamp')
        return self


class AddDisasterRecoveryItemRequestTopics(TeaModel):
    def __init__(
        self,
        consumer_group_id: str = None,
        delivery_order_type: str = None,
        instance_id: str = None,
        instance_type: str = None,
        region_id: str = None,
        topic_name: str = None,
    ):
        # Consumer group ID, required for ACTIVE_ACTIVE bidirectional backup
        self.consumer_group_id = consumer_group_id
        # The order in which messages are delivered to the target instance. The parameter values ​​are as follows:
        #   - Concurrently: concurrent delivery
        #   - Orderly: sequential delivery
        self.delivery_order_type = delivery_order_type
        # Instance ID, an instance ID will be automatically generated when `instanceType` is `EXTERNAL_ROCKETMQ`, and it can be obtained by querying the backup plan.
        self.instance_id = instance_id
        # Instance type
        #   - ALIYUN_ROCKETMQ: Alibaba Cloud instance
        #   - EXTERNAL_ROCKETMQ: External instance, open-source instance, open-source cluster
        self.instance_type = instance_type
        # Region ID
        self.region_id = region_id
        # Disaster recovery topic name, required
        self.topic_name = topic_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consumer_group_id is not None:
            result['consumerGroupId'] = self.consumer_group_id
        if self.delivery_order_type is not None:
            result['deliveryOrderType'] = self.delivery_order_type
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.topic_name is not None:
            result['topicName'] = self.topic_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('consumerGroupId') is not None:
            self.consumer_group_id = m.get('consumerGroupId')
        if m.get('deliveryOrderType') is not None:
            self.delivery_order_type = m.get('deliveryOrderType')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('topicName') is not None:
            self.topic_name = m.get('topicName')
        return self


class AddDisasterRecoveryItemRequest(TeaModel):
    def __init__(
        self,
        topics: List[AddDisasterRecoveryItemRequestTopics] = None,
    ):
        # Topics included in the backup mapping. Required.
        self.topics = topics

    def validate(self):
        if self.topics:
            for k in self.topics:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['topics'] = []
        if self.topics is not None:
            for k in self.topics:
                result['topics'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.topics = []
        if m.get('topics') is not None:
            for k in m.get('topics'):
                temp_model = AddDisasterRecoveryItemRequestTopics()
                self.topics.append(temp_model.from_map(k))
        return self


class AddDisasterRecoveryItemResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: int = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Access denied details, only in the scenario where the user is denied access due to RAM not having permission
        self.access_denied_detail = access_denied_detail
        # Error code
        self.code = code
        # Return result, mapping task ID
        self.data = data
        # Dynamic error code
        self.dynamic_code = dynamic_code
        # Dynamic error message
        self.dynamic_message = dynamic_message
        # HTTP status code
        self.http_status_code = http_status_code
        # Error message
        self.message = message
        # Request ID
        self.request_id = request_id
        # Whether the operation was successful
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['accessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
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
        if m.get('accessDeniedDetail') is not None:
            self.access_denied_detail = m.get('accessDeniedDetail')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
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


class AddDisasterRecoveryItemResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddDisasterRecoveryItemResponseBody = None,
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
            temp_model = AddDisasterRecoveryItemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChangeResourceGroupRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        resource_group_id: str = None,
        resource_id: str = None,
        resource_type: str = None,
    ):
        # The ID of the region in which the instance resides.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group to which the instance is changed.
        # 
        # You can call the [ListResourceGroups](https://www.alibabacloud.com/help/resource-management/latest/listresourcegroups) operation to query existing resource groups.
        # 
        # This parameter is required.
        self.resource_group_id = resource_group_id
        # The ID of the resource. Set this parameter to the ID of the ApsaraMQ for RocketMQ instance whose resource group you want to change.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The type of resource.
        # 
        # Set this parameter to **instance**. The value of this parameter cannot be changed.
        # 
        # This parameter is required.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        if self.resource_id is not None:
            result['resourceId'] = self.resource_id
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        return self


class ChangeResourceGroupResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code returned if the call failed.
        self.code = code
        # The returned result.
        self.data = data
        # The dynamic error code.
        self.dynamic_code = dynamic_code
        # The dynamic error message.
        self.dynamic_message = dynamic_message
        # The HTTP status code returned.
        self.http_status_code = http_status_code
        # The error message.
        self.message = message
        # The ID of the request. Each request has a unique ID. You can use this ID to troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the call was successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
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
            self.data = m.get('data')
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


class ChangeResourceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ChangeResourceGroupResponseBody = None,
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
            temp_model = ChangeResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateConsumerGroupRequestConsumeRetryPolicy(TeaModel):
    def __init__(
        self,
        dead_letter_target_topic: str = None,
        fixed_interval_retry_time: int = None,
        max_retry_times: int = None,
        retry_policy: str = None,
    ):
        # The dead-letter topic.
        # 
        # If a message still fails to be consumed after the maximum number of retries specified in the consumption retry policy is reached, the message is delivered to the dead-letter topic for subsequent business recovery or backtracking. For more information, see [Consumption retry and dead-letter messages](https://help.aliyun.com/document_detail/440356.html).
        self.dead_letter_target_topic = dead_letter_target_topic
        # Fixed retry interval, unit: seconds.This option is effective when retryPolicy is FixedRetryPolicy.Value range：
        #   - Concurrently:10-600
        #   - Orderly:1-60
        self.fixed_interval_retry_time = fixed_interval_retry_time
        # The maximum number of retries.
        self.max_retry_times = max_retry_times
        # The retry policy. For more information, see [Message retry](https://help.aliyun.com/document_detail/440356.html).
        # 
        # Valid values:
        # 
        # *   FixedRetryPolicy: fixed-interval retry. This value is valid only if you set deliveryOrderType to Orderly.
        # *   DefaultRetryPolicy: exponential backoff retry. This value is valid only if you set deliveryOrderType to Concurrently.
        # 
        # This parameter is required.
        self.retry_policy = retry_policy

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dead_letter_target_topic is not None:
            result['deadLetterTargetTopic'] = self.dead_letter_target_topic
        if self.fixed_interval_retry_time is not None:
            result['fixedIntervalRetryTime'] = self.fixed_interval_retry_time
        if self.max_retry_times is not None:
            result['maxRetryTimes'] = self.max_retry_times
        if self.retry_policy is not None:
            result['retryPolicy'] = self.retry_policy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deadLetterTargetTopic') is not None:
            self.dead_letter_target_topic = m.get('deadLetterTargetTopic')
        if m.get('fixedIntervalRetryTime') is not None:
            self.fixed_interval_retry_time = m.get('fixedIntervalRetryTime')
        if m.get('maxRetryTimes') is not None:
            self.max_retry_times = m.get('maxRetryTimes')
        if m.get('retryPolicy') is not None:
            self.retry_policy = m.get('retryPolicy')
        return self


class CreateConsumerGroupRequest(TeaModel):
    def __init__(
        self,
        consume_retry_policy: CreateConsumerGroupRequestConsumeRetryPolicy = None,
        delivery_order_type: str = None,
        max_receive_tps: int = None,
        remark: str = None,
    ):
        # The consumption retry policy of the consumer group. For more information, see [Consumption retry](https://help.aliyun.com/document_detail/440356.html).
        # 
        # This parameter is required.
        self.consume_retry_policy = consume_retry_policy
        # The message delivery method of the consumer group.
        # 
        # Valid values:
        # 
        # *   Concurrently: concurrent delivery
        # *   Orderly: ordered delivery
        # 
        # This parameter is required.
        self.delivery_order_type = delivery_order_type
        # The maximum number of messages that can be processed by consumers per second.
        self.max_receive_tps = max_receive_tps
        # The description of the consumer group.
        self.remark = remark

    def validate(self):
        if self.consume_retry_policy:
            self.consume_retry_policy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consume_retry_policy is not None:
            result['consumeRetryPolicy'] = self.consume_retry_policy.to_map()
        if self.delivery_order_type is not None:
            result['deliveryOrderType'] = self.delivery_order_type
        if self.max_receive_tps is not None:
            result['maxReceiveTps'] = self.max_receive_tps
        if self.remark is not None:
            result['remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('consumeRetryPolicy') is not None:
            temp_model = CreateConsumerGroupRequestConsumeRetryPolicy()
            self.consume_retry_policy = temp_model.from_map(m['consumeRetryPolicy'])
        if m.get('deliveryOrderType') is not None:
            self.delivery_order_type = m.get('deliveryOrderType')
        if m.get('maxReceiveTps') is not None:
            self.max_receive_tps = m.get('maxReceiveTps')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        return self


class CreateConsumerGroupResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code.
        self.code = code
        # The result data that is returned.
        self.data = data
        # The dynamic error code.
        self.dynamic_code = dynamic_code
        # The dynamic error message.
        self.dynamic_message = dynamic_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the call was successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
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
            self.data = m.get('data')
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


class CreateConsumerGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateConsumerGroupResponseBody = None,
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
            temp_model = CreateConsumerGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDisasterRecoveryPlanRequestInstancesMessageProperty(TeaModel):
    def __init__(
        self,
        property_key: str = None,
        property_value: str = None,
    ):
        # Property key
        self.property_key = property_key
        # Property value
        self.property_value = property_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.property_key is not None:
            result['propertyKey'] = self.property_key
        if self.property_value is not None:
            result['propertyValue'] = self.property_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('propertyKey') is not None:
            self.property_key = m.get('propertyKey')
        if m.get('propertyValue') is not None:
            self.property_value = m.get('propertyValue')
        return self


class CreateDisasterRecoveryPlanRequestInstances(TeaModel):
    def __init__(
        self,
        auth_type: str = None,
        consumer_group_id: str = None,
        endpoint_url: str = None,
        instance_id: str = None,
        instance_role: str = None,
        instance_type: str = None,
        message_property: CreateDisasterRecoveryPlanRequestInstancesMessageProperty = None,
        network_type: str = None,
        password: str = None,
        region_id: str = None,
        security_group_id: str = None,
        username: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        # Authentication method. Not required for instanceType of ALIYUN_ROCKETMQ and version 4.0
        #   - NO_AUTH: No authentication required
        #   - ACL_AUTH: ACL authentication
        self.auth_type = auth_type
        self.consumer_group_id = consumer_group_id
        # Endpoint URL, not required for instanceType of ALIYUN_ROCKETMQ, but required for EXTERNAL_ROCKETMQ
        self.endpoint_url = endpoint_url
        # Instance ID, not required for instanceType of EXTERNAL_ROCKETMQ, but required for ALIYUN_ROCKETMQ
        self.instance_id = instance_id
        # Instance role, either primary or secondary
        #   - ACTIVE: Primary
        #   - PASSIVE: Secondary
        self.instance_role = instance_role
        # Instance type
        #   - ALIYUN_ROCKETMQ: Alibaba Cloud instance
        #   - EXTERNAL_ROCKETMQ: External instance, open-source instance, open-source cluster
        self.instance_type = instance_type
        # Message filtering properties. When messages are synchronized to the target cluster, this property will be automatically added for SQL filtering during message consumption.
        self.message_property = message_property
        # Network type, not required for instanceType of ALIYUN_ROCKETMQ, but required for EXTERNAL_ROCKETMQ
        # Parameter values are as follows:
        #   - TCP_INTERNET: TCP public network
        #   - TCP_VPC: TCP VPC (Virtual Private Cloud)
        self.network_type = network_type
        # Authentication password, required when authType is ACL_AUTH. Not required for instanceType of ALIYUN_ROCKETMQ
        self.password = password
        # Region where the instance is located
        self.region_id = region_id
        # Security group ID, required only when the `instanceType` is EXTERNAL_ROCKETMQ and `networkType` is TCP_VPC.
        self.security_group_id = security_group_id
        # Authentication username, required when authType is ACL_AUTH
        self.username = username
        # The ID of the switch associated with the instance, required only when the `instanceType` is EXTERNAL_ROCKETMQ and `networkType` is TCP_VPC.
        self.v_switch_id = v_switch_id
        # The ID of the private network associated with the created instance. The instanceType instance type is only EXTERNAL_ROCKETMQ. It is required when the networkType is TCP_VPC.
        self.vpc_id = vpc_id

    def validate(self):
        if self.message_property:
            self.message_property.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_type is not None:
            result['authType'] = self.auth_type
        if self.consumer_group_id is not None:
            result['consumerGroupId'] = self.consumer_group_id
        if self.endpoint_url is not None:
            result['endpointUrl'] = self.endpoint_url
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.instance_role is not None:
            result['instanceRole'] = self.instance_role
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        if self.message_property is not None:
            result['messageProperty'] = self.message_property.to_map()
        if self.network_type is not None:
            result['networkType'] = self.network_type
        if self.password is not None:
            result['password'] = self.password
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.security_group_id is not None:
            result['securityGroupId'] = self.security_group_id
        if self.username is not None:
            result['username'] = self.username
        if self.v_switch_id is not None:
            result['vSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authType') is not None:
            self.auth_type = m.get('authType')
        if m.get('consumerGroupId') is not None:
            self.consumer_group_id = m.get('consumerGroupId')
        if m.get('endpointUrl') is not None:
            self.endpoint_url = m.get('endpointUrl')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('instanceRole') is not None:
            self.instance_role = m.get('instanceRole')
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        if m.get('messageProperty') is not None:
            temp_model = CreateDisasterRecoveryPlanRequestInstancesMessageProperty()
            self.message_property = temp_model.from_map(m['messageProperty'])
        if m.get('networkType') is not None:
            self.network_type = m.get('networkType')
        if m.get('password') is not None:
            self.password = m.get('password')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('securityGroupId') is not None:
            self.security_group_id = m.get('securityGroupId')
        if m.get('username') is not None:
            self.username = m.get('username')
        if m.get('vSwitchId') is not None:
            self.v_switch_id = m.get('vSwitchId')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        return self


class CreateDisasterRecoveryPlanRequest(TeaModel):
    def __init__(
        self,
        auto_sync_checkpoint: bool = None,
        instances: List[CreateDisasterRecoveryPlanRequestInstances] = None,
        plan_desc: str = None,
        plan_name: str = None,
        plan_type: str = None,
        sync_checkpoint_enabled: bool = None,
    ):
        # Whether to enable automatic synchronization of consumption progress.
        # 
        # > This is effective only when consumption progress synchronization is enabled, i.e., the value of `syncCheckpointEnabled` is true.
        self.auto_sync_checkpoint = auto_sync_checkpoint
        # Instances involved in the backup plan. Required
        self.instances = instances
        # Plan description
        self.plan_desc = plan_desc
        # Plan name, required
        self.plan_name = plan_name
        # Backup plan type, required. Please refer to the [documentation](https://help.aliyun.com/document_detail/2843187.html).
        # Parameter values are as follows:
        #   - ACTIVE_PASSIVE: One-way backup
        #   - ACTIVE_ACTIVE: Two-way backup
        self.plan_type = plan_type
        # Switch for synchronizing consumption progress
        self.sync_checkpoint_enabled = sync_checkpoint_enabled

    def validate(self):
        if self.instances:
            for k in self.instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_sync_checkpoint is not None:
            result['autoSyncCheckpoint'] = self.auto_sync_checkpoint
        result['instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['instances'].append(k.to_map() if k else None)
        if self.plan_desc is not None:
            result['planDesc'] = self.plan_desc
        if self.plan_name is not None:
            result['planName'] = self.plan_name
        if self.plan_type is not None:
            result['planType'] = self.plan_type
        if self.sync_checkpoint_enabled is not None:
            result['syncCheckpointEnabled'] = self.sync_checkpoint_enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoSyncCheckpoint') is not None:
            self.auto_sync_checkpoint = m.get('autoSyncCheckpoint')
        self.instances = []
        if m.get('instances') is not None:
            for k in m.get('instances'):
                temp_model = CreateDisasterRecoveryPlanRequestInstances()
                self.instances.append(temp_model.from_map(k))
        if m.get('planDesc') is not None:
            self.plan_desc = m.get('planDesc')
        if m.get('planName') is not None:
            self.plan_name = m.get('planName')
        if m.get('planType') is not None:
            self.plan_type = m.get('planType')
        if m.get('syncCheckpointEnabled') is not None:
            self.sync_checkpoint_enabled = m.get('syncCheckpointEnabled')
        return self


class CreateDisasterRecoveryPlanResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: int = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Access denied details, provided only in scenarios where access is denied due to lack of RAM permissions
        self.access_denied_detail = access_denied_detail
        # Error code
        self.code = code
        # The result, which is the backup plan ID
        self.data = data
        # Dynamic error code
        self.dynamic_code = dynamic_code
        # Dynamic error message
        self.dynamic_message = dynamic_message
        # HTTP status code
        self.http_status_code = http_status_code
        # Error message
        self.message = message
        # Request ID
        self.request_id = request_id
        # Indicates whether the operation was successful
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['accessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
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
        if m.get('accessDeniedDetail') is not None:
            self.access_denied_detail = m.get('accessDeniedDetail')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
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


class CreateDisasterRecoveryPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDisasterRecoveryPlanResponseBody = None,
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
            temp_model = CreateDisasterRecoveryPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateInstanceRequestNetworkInfoInternetInfo(TeaModel):
    def __init__(
        self,
        flow_out_bandwidth: int = None,
        flow_out_type: str = None,
        internet_spec: str = None,
        ip_whitelist: List[str] = None,
    ):
        # The Internet bandwidth. Unit: MB/s.
        # 
        # This parameter is required only if you set flowOutType to payByBandwidth.
        # 
        # Valid values: 1 to 1000.
        self.flow_out_bandwidth = flow_out_bandwidth
        # The metering method of Internet usage.
        # 
        # Valid values:
        # 
        # *   payByBandwidth: pay-by-bandwidth. This value is valid only if you enable Internet access.
        # *   payByTraffic: pay-by-traffic. This value is valid only if you enable Internet access.
        # *   uninvolved: No metering method is involved. This value is valid only if you disable Internet access.
        # 
        # This parameter is required.
        self.flow_out_type = flow_out_type
        # Specifies whether to enable the Internet access feature.
        # 
        # Valid values:
        # 
        # *   enable
        # *   disable
        # 
        # By default, ApsaraMQ for RocketMQ allows you to access instances in VPCs. If you enable Internet access for an instance, you can access the instance over the Internet. After you enable this feature, you are charged for outbound Internet traffic. For more information, see [Internet access fees](https://help.aliyun.com/document_detail/427240.html).
        # 
        # This parameter is required.
        self.internet_spec = internet_spec
        # The whitelist that includes the CIDR blocks that are allowed to access the ApsaraMQ for RocketMQ broker over the Internet. This parameter can be configured only if you use the public endpoint to access the instance.
        # 
        # *   If you do not configure an IP address whitelist, all CIDR blocks are allowed to access the ApsaraMQ for RocketMQ broker over the Internet.
        # *   If you configure an IP address whitelist, only the CIDR blocks in the whitelist are allowed to access the ApsaraMQ for RocketMQ broker over the Internet.
        self.ip_whitelist = ip_whitelist

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_out_bandwidth is not None:
            result['flowOutBandwidth'] = self.flow_out_bandwidth
        if self.flow_out_type is not None:
            result['flowOutType'] = self.flow_out_type
        if self.internet_spec is not None:
            result['internetSpec'] = self.internet_spec
        if self.ip_whitelist is not None:
            result['ipWhitelist'] = self.ip_whitelist
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('flowOutBandwidth') is not None:
            self.flow_out_bandwidth = m.get('flowOutBandwidth')
        if m.get('flowOutType') is not None:
            self.flow_out_type = m.get('flowOutType')
        if m.get('internetSpec') is not None:
            self.internet_spec = m.get('internetSpec')
        if m.get('ipWhitelist') is not None:
            self.ip_whitelist = m.get('ipWhitelist')
        return self


class CreateInstanceRequestNetworkInfoVpcInfoVSwitches(TeaModel):
    def __init__(
        self,
        v_switch_id: str = None,
    ):
        # The ID of the vSwitch with which the instance is associated.
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.v_switch_id is not None:
            result['vSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('vSwitchId') is not None:
            self.v_switch_id = m.get('vSwitchId')
        return self


class CreateInstanceRequestNetworkInfoVpcInfo(TeaModel):
    def __init__(
        self,
        security_group_ids: str = None,
        v_switch_id: str = None,
        v_switches: List[CreateInstanceRequestNetworkInfoVpcInfoVSwitches] = None,
        vpc_id: str = None,
    ):
        # The ID of the security group to which the instance belongs.
        self.security_group_ids = security_group_ids
        # The ID of the vSwitch with which the instance is associated. If you want to specify multiple vSwitches, separate the vSwitches with vertical bars (|).
        # 
        # >  After you create an ApsaraMQ for RocketMQ instance, you cannot change the vSwitch with which the instance is associated. If you want to change the vSwitch with which the instance is associated, you must release the instance and purchase a new instance.
        # 
        # >  We recommend that you configure vSwitches instead of this parameter.
        self.v_switch_id = v_switch_id
        # The vSwitches.
        # 
        # >  After you create an ApsaraMQ for RocketMQ instance, you cannot change the vSwitch with which the instance is associated. If you want to change the vSwitch with which the instance is associated, you must release the instance and purchase a new instance.
        # 
        # >  This parameter is required. We recommend that you configure this parameter instead of vSwitchId.
        self.v_switches = v_switches
        # The ID of the VPC with which the instance to be created is associated.
        # 
        # >  After you create an ApsaraMQ for RocketMQ instance, you cannot change the VPC with which the instance is associated. If you want to change the VPC with which the instance is associated, you must release the instance and create a new instance.
        # 
        # This parameter is required.
        self.vpc_id = vpc_id

    def validate(self):
        if self.v_switches:
            for k in self.v_switches:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_group_ids is not None:
            result['securityGroupIds'] = self.security_group_ids
        if self.v_switch_id is not None:
            result['vSwitchId'] = self.v_switch_id
        result['vSwitches'] = []
        if self.v_switches is not None:
            for k in self.v_switches:
                result['vSwitches'].append(k.to_map() if k else None)
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('securityGroupIds') is not None:
            self.security_group_ids = m.get('securityGroupIds')
        if m.get('vSwitchId') is not None:
            self.v_switch_id = m.get('vSwitchId')
        self.v_switches = []
        if m.get('vSwitches') is not None:
            for k in m.get('vSwitches'):
                temp_model = CreateInstanceRequestNetworkInfoVpcInfoVSwitches()
                self.v_switches.append(temp_model.from_map(k))
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        return self


class CreateInstanceRequestNetworkInfo(TeaModel):
    def __init__(
        self,
        internet_info: CreateInstanceRequestNetworkInfoInternetInfo = None,
        vpc_info: CreateInstanceRequestNetworkInfoVpcInfo = None,
    ):
        # The Internet-related configurations.
        # 
        # This parameter is required.
        self.internet_info = internet_info
        # The virtual private cloud (VPC)-related configurations.
        # 
        # This parameter is required.
        self.vpc_info = vpc_info

    def validate(self):
        if self.internet_info:
            self.internet_info.validate()
        if self.vpc_info:
            self.vpc_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.internet_info is not None:
            result['internetInfo'] = self.internet_info.to_map()
        if self.vpc_info is not None:
            result['vpcInfo'] = self.vpc_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('internetInfo') is not None:
            temp_model = CreateInstanceRequestNetworkInfoInternetInfo()
            self.internet_info = temp_model.from_map(m['internetInfo'])
        if m.get('vpcInfo') is not None:
            temp_model = CreateInstanceRequestNetworkInfoVpcInfo()
            self.vpc_info = temp_model.from_map(m['vpcInfo'])
        return self


class CreateInstanceRequestProductInfo(TeaModel):
    def __init__(
        self,
        auto_scaling: bool = None,
        message_retention_time: int = None,
        msg_process_spec: str = None,
        send_receive_ratio: float = None,
        storage_encryption: bool = None,
        storage_secret_key: str = None,
    ):
        # Specifies whether to enable the elastic TPS feature for the instance.
        # 
        # Valid values:
        # 
        # *   true
        # *   false
        # 
        # After you enable the elastic TPS feature for an ApsaraMQ for RocketMQ instance, you can use a specific amount of TPS that exceeds the specification limit. You are charged for the elastic TPS feature. For more information, see [Computing fees](https://help.aliyun.com/document_detail/427237.html).
        # 
        # >  The elastic TPS feature is supported only by instances of specific editions. For more information, see [Instance editions](https://help.aliyun.com/document_detail/444715.html).
        self.auto_scaling = auto_scaling
        # The retention period of messages. Unit: hours.
        # 
        # For information about the valid values of this parameter, see the "Limits on resource quotas" section of the [Limits](https://help.aliyun.com/document_detail/440347.html) topic.
        # 
        # ApsaraMQ for RocketMQ supports serverless scaling of message storage. You are charged storage fees based on your actual storage usage. You can change the retention period of messages to manage storage capacity. For more information, see [Storage fees](https://help.aliyun.com/document_detail/427238.html).
        self.message_retention_time = message_retention_time
        # The computing specification that specifies the messaging transactions per second (TPS) of the instance. For more information, see [Instance editions](https://help.aliyun.com/document_detail/444715.html).
        self.msg_process_spec = msg_process_spec
        # The ratio of the message sending TPS to the messaging TPS of the instance.
        # 
        # For example, if the maximum messaging TPS of an instance is 1,000 and the ratio of the message sending TPS to the messaging TPS of the instance is 0.8, the maximum message sending TPS of the instance is 800 and the maximum message receiving TPS is 200.
        # 
        # Valid values: 0 to 1. Default value: 0.5.
        self.send_receive_ratio = send_receive_ratio
        # Specifies whether to enable the encryption at rest feature.
        self.storage_encryption = storage_encryption
        # The key for encryption at rest.
        self.storage_secret_key = storage_secret_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_scaling is not None:
            result['autoScaling'] = self.auto_scaling
        if self.message_retention_time is not None:
            result['messageRetentionTime'] = self.message_retention_time
        if self.msg_process_spec is not None:
            result['msgProcessSpec'] = self.msg_process_spec
        if self.send_receive_ratio is not None:
            result['sendReceiveRatio'] = self.send_receive_ratio
        if self.storage_encryption is not None:
            result['storageEncryption'] = self.storage_encryption
        if self.storage_secret_key is not None:
            result['storageSecretKey'] = self.storage_secret_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoScaling') is not None:
            self.auto_scaling = m.get('autoScaling')
        if m.get('messageRetentionTime') is not None:
            self.message_retention_time = m.get('messageRetentionTime')
        if m.get('msgProcessSpec') is not None:
            self.msg_process_spec = m.get('msgProcessSpec')
        if m.get('sendReceiveRatio') is not None:
            self.send_receive_ratio = m.get('sendReceiveRatio')
        if m.get('storageEncryption') is not None:
            self.storage_encryption = m.get('storageEncryption')
        if m.get('storageSecretKey') is not None:
            self.storage_secret_key = m.get('storageSecretKey')
        return self


class CreateInstanceRequestTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The `key` of the tag.
        self.key = key
        # The `value` of the tag.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class CreateInstanceRequest(TeaModel):
    def __init__(
        self,
        auto_renew: bool = None,
        auto_renew_period: int = None,
        commodity_code: str = None,
        instance_name: str = None,
        network_info: CreateInstanceRequestNetworkInfo = None,
        payment_type: str = None,
        period: int = None,
        period_unit: str = None,
        product_info: CreateInstanceRequestProductInfo = None,
        remark: str = None,
        resource_group_id: str = None,
        series_code: str = None,
        service_code: str = None,
        sub_series_code: str = None,
        tags: List[CreateInstanceRequestTags] = None,
        client_token: str = None,
    ):
        # Specifies whether to enable auto-renewal for the instance. This parameter takes effect only if you set paymentType to Subscription. Valid values:
        # 
        # *   true
        # *   false
        self.auto_renew = auto_renew
        # The auto-renewal cycle of the instance. This parameter takes effect only if you set autoRenew to true. Unit: months.
        # 
        # Valid values:
        # 
        # *   Monthly renewal: 1, 2, 3, 6, and 12
        self.auto_renew_period = auto_renew_period
        # The commodity code. Valid values:
        # 
        # *   ons_rmqpost_public_intl: pay-as-you-go
        # *   ons_rmqsub_public_intl: subscription
        # *   ons_rmqsrvlesspost_public_intl: serverless instance
        # serverless instance requires this parameter
        self.commodity_code = commodity_code
        # The name of the instance that you want to create.
        # 
        # If you leave this parameter empty, the instance ID is used as the instance name.
        self.instance_name = instance_name
        # The information about the network.
        # 
        # This parameter is required.
        self.network_info = network_info
        # The billing method of the instance. ApsaraMQ for RocketMQ supports the subscription and pay-as-you-go billing methods.
        # 
        # Valid values:
        # 
        # *   PayAsYouGo: This billing method allows you to use resources before you pay for the resources.
        # *   Subscription: This billing method allows you to use resources after you pay for the resources.
        # 
        # For more information, see [Billing methods](https://help.aliyun.com/document_detail/427234.html).
        # 
        # This parameter is required.
        self.payment_type = payment_type
        # The subscription duration of the instance. This parameter takes effect only if you set paymentType to Subscription.
        # 
        # Valid values:
        # 
        # *   Monthly subscription: 1, 2, 3, 4, 5, and 6
        # *   Yearly subscription: 1, 2, and 3
        self.period = period
        # The unit of the subscription duration.
        # 
        # Valid values:
        # 
        # *   Month
        # *   Year
        self.period_unit = period_unit
        # The information about instance specifications.
        self.product_info = product_info
        # The instance description.
        self.remark = remark
        # The ID of the resource group to which the instance belongs.
        self.resource_group_id = resource_group_id
        # The primary edition of the instance. For information about the differences among primary edition instances, see [Instance selection](https://help.aliyun.com/document_detail/444722.html).
        # 
        # Valid values:
        # 
        # *   standard: Standard Edition
        # *   ultimate: Enterprise Platinum Edition
        # *   professional: Professional Edition
        # 
        # >  After you create an instance, you can only upgrade the primary edition of the instance. The following editions are sorted in ascending order: Standard Edition, Professional Edition, Enterprise Platinum Edition. For example, you can upgrade an instance from Standard Edition to Professional Edition, but you cannot downgrade an instance from Professional Edition to Standard Edition.
        # 
        # This parameter is required.
        self.series_code = series_code
        # The code of the service to which the instance belongs. The service code of ApsaraMQ for RocketMQ is rmq.
        # 
        # This parameter is required.
        self.service_code = service_code
        # The sub-category edition of the instance. For information about the differences among sub-category edition instances, see [Instance selection](https://help.aliyun.com/document_detail/444722.html).
        # 
        # Valid values:
        # 
        # *   cluster_ha: Cluster High-availability Edition
        # *   single_node: Standalone Edition
        # *   serverless: serverless
        # 
        # If you set seriesCode to ultimate, you can set this parameter only to cluster_ha.
        # 
        # >  After you create an instance, you cannot change the sub-category edition of the instance.
        # 
        # Valid values:
        # 
        # *   serverless: serverless
        # *   cluster_ha: Cluster High-availability Edition
        # *   single_node: Standalone Edition
        # 
        # This parameter is required.
        self.sub_series_code = sub_series_code
        # The tags that you want to add to the instance.
        self.tags = tags
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value of this parameter, but you must ensure that the value is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token

    def validate(self):
        if self.network_info:
            self.network_info.validate()
        if self.product_info:
            self.product_info.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renew is not None:
            result['autoRenew'] = self.auto_renew
        if self.auto_renew_period is not None:
            result['autoRenewPeriod'] = self.auto_renew_period
        if self.commodity_code is not None:
            result['commodityCode'] = self.commodity_code
        if self.instance_name is not None:
            result['instanceName'] = self.instance_name
        if self.network_info is not None:
            result['networkInfo'] = self.network_info.to_map()
        if self.payment_type is not None:
            result['paymentType'] = self.payment_type
        if self.period is not None:
            result['period'] = self.period
        if self.period_unit is not None:
            result['periodUnit'] = self.period_unit
        if self.product_info is not None:
            result['productInfo'] = self.product_info.to_map()
        if self.remark is not None:
            result['remark'] = self.remark
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        if self.series_code is not None:
            result['seriesCode'] = self.series_code
        if self.service_code is not None:
            result['serviceCode'] = self.service_code
        if self.sub_series_code is not None:
            result['subSeriesCode'] = self.sub_series_code
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoRenew') is not None:
            self.auto_renew = m.get('autoRenew')
        if m.get('autoRenewPeriod') is not None:
            self.auto_renew_period = m.get('autoRenewPeriod')
        if m.get('commodityCode') is not None:
            self.commodity_code = m.get('commodityCode')
        if m.get('instanceName') is not None:
            self.instance_name = m.get('instanceName')
        if m.get('networkInfo') is not None:
            temp_model = CreateInstanceRequestNetworkInfo()
            self.network_info = temp_model.from_map(m['networkInfo'])
        if m.get('paymentType') is not None:
            self.payment_type = m.get('paymentType')
        if m.get('period') is not None:
            self.period = m.get('period')
        if m.get('periodUnit') is not None:
            self.period_unit = m.get('periodUnit')
        if m.get('productInfo') is not None:
            temp_model = CreateInstanceRequestProductInfo()
            self.product_info = temp_model.from_map(m['productInfo'])
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('seriesCode') is not None:
            self.series_code = m.get('seriesCode')
        if m.get('serviceCode') is not None:
            self.service_code = m.get('serviceCode')
        if m.get('subSeriesCode') is not None:
            self.sub_series_code = m.get('subSeriesCode')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = CreateInstanceRequestTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class CreateInstanceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code returned if the call failed.
        self.code = code
        # The ID of the created instance.
        self.data = data
        # The dynamic error code.
        self.dynamic_code = dynamic_code
        # The dynamic error message.
        self.dynamic_message = dynamic_message
        # The HTTP status code returned.
        self.http_status_code = http_status_code
        # The error message.
        self.message = message
        # The ID of the request. Each request has a unique ID. You can use this ID to troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the call was successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
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
            self.data = m.get('data')
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


class CreateInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateInstanceResponseBody = None,
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
            temp_model = CreateInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateInstanceAccountRequest(TeaModel):
    def __init__(
        self,
        password: str = None,
        username: str = None,
    ):
        # The password of the account.
        # 
        # This parameter is required.
        self.password = password
        # The username of the account.
        # 
        # This parameter is required.
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.password is not None:
            result['password'] = self.password
        if self.username is not None:
            result['username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('password') is not None:
            self.password = m.get('password')
        if m.get('username') is not None:
            self.username = m.get('username')
        return self


class CreateInstanceAccountResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: bool = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # No permission details
        self.access_denied_detail = access_denied_detail
        # The error code returned if the call failed.
        self.code = code
        # The returned result.
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
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['accessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
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
        if m.get('accessDeniedDetail') is not None:
            self.access_denied_detail = m.get('accessDeniedDetail')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
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


class CreateInstanceAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateInstanceAccountResponseBody = None,
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
            temp_model = CreateInstanceAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateInstanceAclRequest(TeaModel):
    def __init__(
        self,
        actions: List[str] = None,
        decision: str = None,
        ip_whitelists: List[str] = None,
        resource_name: str = None,
        resource_type: str = None,
    ):
        # The type of operations that can be performed on the resource.
        # 
        # The following types of operations are supported based on the resource type:
        # 
        # *   Topic: Pub, Sub, and Pub|Sub
        # *   Consumer group: Sub
        # 
        # Valid values:
        # 
        # *   SUB: subscribe
        # *   Pub|Sub: publish and subscribe
        # *   Pub: publish
        # 
        # This parameter is required.
        self.actions = actions
        # The decision result of the authorization.
        # 
        # Valid values:
        # 
        # *   Deny
        # *   Allow
        # 
        # This parameter is required.
        self.decision = decision
        # The IP address whitelists.
        self.ip_whitelists = ip_whitelists
        # The name of the resource on which you want to grant permissions.
        # 
        # This parameter is required.
        self.resource_name = resource_name
        # The type of the resource on which you want to grant permissions.
        # 
        # Valid values:
        # 
        # *   Group
        # *   Topic
        # 
        # This parameter is required.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actions is not None:
            result['actions'] = self.actions
        if self.decision is not None:
            result['decision'] = self.decision
        if self.ip_whitelists is not None:
            result['ipWhitelists'] = self.ip_whitelists
        if self.resource_name is not None:
            result['resourceName'] = self.resource_name
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actions') is not None:
            self.actions = m.get('actions')
        if m.get('decision') is not None:
            self.decision = m.get('decision')
        if m.get('ipWhitelists') is not None:
            self.ip_whitelists = m.get('ipWhitelists')
        if m.get('resourceName') is not None:
            self.resource_name = m.get('resourceName')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        return self


class CreateInstanceAclResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: bool = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details about the access denial. This parameter is returned only if the access is denied because the Resource Access Management (RAM) user does not have the required permissions.
        self.access_denied_detail = access_denied_detail
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
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['accessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
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
        if m.get('accessDeniedDetail') is not None:
            self.access_denied_detail = m.get('accessDeniedDetail')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
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


class CreateInstanceAclResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateInstanceAclResponseBody = None,
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
            temp_model = CreateInstanceAclResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateInstanceIpWhitelistRequest(TeaModel):
    def __init__(
        self,
        ip_whitelists: List[str] = None,
    ):
        # The IP address whitelists.
        # 
        # This parameter is required.
        self.ip_whitelists = ip_whitelists

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_whitelists is not None:
            result['ipWhitelists'] = self.ip_whitelists
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ipWhitelists') is not None:
            self.ip_whitelists = m.get('ipWhitelists')
        return self


class CreateInstanceIpWhitelistResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: bool = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details about the access denial. This parameter is returned only if the access is denied because the Resource Access Management (RAM) user does not have the required permissions.
        self.access_denied_detail = access_denied_detail
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
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['accessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
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
        if m.get('accessDeniedDetail') is not None:
            self.access_denied_detail = m.get('accessDeniedDetail')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
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


class CreateInstanceIpWhitelistResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateInstanceIpWhitelistResponseBody = None,
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
            temp_model = CreateInstanceIpWhitelistResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTopicRequest(TeaModel):
    def __init__(
        self,
        max_send_tps: int = None,
        message_type: str = None,
        remark: str = None,
    ):
        # The maximum TPS for message sending.
        self.max_send_tps = max_send_tps
        # The type of messages in the topic that you want to create.
        # 
        # Valid values:
        # 
        # *   TRANSACTION: transactional messages
        # *   FIFO: ordered messages
        # *   DELAY: scheduled or delayed messages
        # *   NORMAL: normal messages
        # 
        # >  The type of messages in the topic must be the same as the type of messages that you want to send. For example, if you create a topic whose message type is ordered messages, you can use the topic to send and receive only ordered messages.
        self.message_type = message_type
        # The description of the topic that you want to create.
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_send_tps is not None:
            result['maxSendTps'] = self.max_send_tps
        if self.message_type is not None:
            result['messageType'] = self.message_type
        if self.remark is not None:
            result['remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxSendTps') is not None:
            self.max_send_tps = m.get('maxSendTps')
        if m.get('messageType') is not None:
            self.message_type = m.get('messageType')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        return self


class CreateTopicResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Error code.
        self.code = code
        # Return result.
        self.data = data
        # Dynamic error code.
        self.dynamic_code = dynamic_code
        # Dynamic error message.
        self.dynamic_message = dynamic_message
        # HTTP status code.
        self.http_status_code = http_status_code
        # Error message.
        self.message = message
        # Request ID, each request\\"s ID is unique and can be used for troubleshooting and problem localization.
        self.request_id = request_id
        # Indicates whether the execution was successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
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
            self.data = m.get('data')
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


class DeleteConsumerGroupResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code.
        self.code = code
        # The result data that is returned.
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
        # Indicates whether the call is successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
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
            self.data = m.get('data')
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


class DeleteConsumerGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteConsumerGroupResponseBody = None,
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
            temp_model = DeleteConsumerGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteConsumerGroupSubscriptionRequest(TeaModel):
    def __init__(
        self,
        filter_expression: str = None,
        filter_type: str = None,
        topic_name: str = None,
    ):
        # The filter expression.
        # 
        # This parameter is required.
        self.filter_expression = filter_expression
        # The type of the filter expression. Valid values:
        # 
        # *   SQL: filters messages by using SQL expressions.
        # *   TAG: filters messages by using tags.
        # 
        # This parameter is required.
        self.filter_type = filter_type
        # The topic name.
        # 
        # This parameter is required.
        self.topic_name = topic_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter_expression is not None:
            result['filterExpression'] = self.filter_expression
        if self.filter_type is not None:
            result['filterType'] = self.filter_type
        if self.topic_name is not None:
            result['topicName'] = self.topic_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filterExpression') is not None:
            self.filter_expression = m.get('filterExpression')
        if m.get('filterType') is not None:
            self.filter_type = m.get('filterType')
        if m.get('topicName') is not None:
            self.topic_name = m.get('topicName')
        return self


class DeleteConsumerGroupSubscriptionResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: bool = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details about the access denial. This parameter is returned only if the access is denied because the Resource Access Management (RAM) user does not have the required permissions.
        self.access_denied_detail = access_denied_detail
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
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['accessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
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
        if m.get('accessDeniedDetail') is not None:
            self.access_denied_detail = m.get('accessDeniedDetail')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
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


class DeleteConsumerGroupSubscriptionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteConsumerGroupSubscriptionResponseBody = None,
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
            temp_model = DeleteConsumerGroupSubscriptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDisasterRecoveryItemResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: bool = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Access denied details, only in the scenario where the user is denied access due to RAM not having permission
        self.access_denied_detail = access_denied_detail
        # Error code
        self.code = code
        # The return data
        self.data = data
        # Dynamic error code
        self.dynamic_code = dynamic_code
        # Dynamic error message
        self.dynamic_message = dynamic_message
        # HTTP status code
        self.http_status_code = http_status_code
        # Error message
        self.message = message
        # Request ID
        self.request_id = request_id
        # Whether the operation was successful
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['accessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
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
        if m.get('accessDeniedDetail') is not None:
            self.access_denied_detail = m.get('accessDeniedDetail')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
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


class DeleteDisasterRecoveryItemResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDisasterRecoveryItemResponseBody = None,
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
            temp_model = DeleteDisasterRecoveryItemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDisasterRecoveryPlanResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: bool = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details about the access denial. This parameter is returned only if the access is denied because the Resource Access Management (RAM) user does not have the required permissions.
        self.access_denied_detail = access_denied_detail
        # The error code.
        self.code = code
        # The data returned.
        self.data = data
        # The dynamic error code.
        self.dynamic_code = dynamic_code
        # The dynamic error message.
        self.dynamic_message = dynamic_message
        # The response code.
        self.http_status_code = http_status_code
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['accessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
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
        if m.get('accessDeniedDetail') is not None:
            self.access_denied_detail = m.get('accessDeniedDetail')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
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


class DeleteDisasterRecoveryPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDisasterRecoveryPlanResponseBody = None,
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
            temp_model = DeleteDisasterRecoveryPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteInstanceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code returned if the call failed.
        self.code = code
        # The returned result.
        self.data = data
        # The dynamic error code.
        self.dynamic_code = dynamic_code
        # The dynamic error message.
        self.dynamic_message = dynamic_message
        # The HTTP status code returned.
        self.http_status_code = http_status_code
        # The error message.
        self.message = message
        # The ID of the request. Each request has a unique ID. You can use this ID to troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the call was successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
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
            self.data = m.get('data')
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


class DeleteInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteInstanceResponseBody = None,
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
            temp_model = DeleteInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteInstanceAccountResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: bool = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details about the access denial. This parameter is returned only if the access is denied because the Resource Access Management (RAM) user does not have the required permissions.
        self.access_denied_detail = access_denied_detail
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
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['accessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
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
        if m.get('accessDeniedDetail') is not None:
            self.access_denied_detail = m.get('accessDeniedDetail')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
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


class DeleteInstanceAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteInstanceAccountResponseBody = None,
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
            temp_model = DeleteInstanceAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteInstanceAclRequest(TeaModel):
    def __init__(
        self,
        resource_name: str = None,
        resource_type: str = None,
    ):
        # The name of the resource on which the permissions are granted.
        # 
        # This parameter is required.
        self.resource_name = resource_name
        # The type of the resource on which the permissions are granted.
        # 
        # Valid values:
        # 
        # *   Group
        # *   Topic
        # 
        # This parameter is required.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_name is not None:
            result['resourceName'] = self.resource_name
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resourceName') is not None:
            self.resource_name = m.get('resourceName')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        return self


class DeleteInstanceAclResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: bool = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details about the access denial. This parameter is returned only if the access is denied due to the reason that the Resource Access Management (RAM) user does not have the required permissions.
        self.access_denied_detail = access_denied_detail
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
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['accessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
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
        if m.get('accessDeniedDetail') is not None:
            self.access_denied_detail = m.get('accessDeniedDetail')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
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


class DeleteInstanceAclResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteInstanceAclResponseBody = None,
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
            temp_model = DeleteInstanceAclResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteInstanceIpWhitelistRequest(TeaModel):
    def __init__(
        self,
        ip_whitelist: str = None,
        ip_whitelists: List[str] = None,
    ):
        # The IP address whitelist.
        self.ip_whitelist = ip_whitelist
        # The IP address whitelist.
        self.ip_whitelists = ip_whitelists

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_whitelist is not None:
            result['ipWhitelist'] = self.ip_whitelist
        if self.ip_whitelists is not None:
            result['ipWhitelists'] = self.ip_whitelists
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ipWhitelist') is not None:
            self.ip_whitelist = m.get('ipWhitelist')
        if m.get('ipWhitelists') is not None:
            self.ip_whitelists = m.get('ipWhitelists')
        return self


class DeleteInstanceIpWhitelistShrinkRequest(TeaModel):
    def __init__(
        self,
        ip_whitelist: str = None,
        ip_whitelists_shrink: str = None,
    ):
        # The IP address whitelist.
        self.ip_whitelist = ip_whitelist
        # The IP address whitelist.
        self.ip_whitelists_shrink = ip_whitelists_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_whitelist is not None:
            result['ipWhitelist'] = self.ip_whitelist
        if self.ip_whitelists_shrink is not None:
            result['ipWhitelists'] = self.ip_whitelists_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ipWhitelist') is not None:
            self.ip_whitelist = m.get('ipWhitelist')
        if m.get('ipWhitelists') is not None:
            self.ip_whitelists_shrink = m.get('ipWhitelists')
        return self


class DeleteInstanceIpWhitelistResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: bool = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details about the access denial. This parameter is returned only if the access is denied due to the reason that the Resource Access Management (RAM) user does not have the required permissions.
        self.access_denied_detail = access_denied_detail
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
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['accessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
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
        if m.get('accessDeniedDetail') is not None:
            self.access_denied_detail = m.get('accessDeniedDetail')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
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


class DeleteInstanceIpWhitelistResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteInstanceIpWhitelistResponseBody = None,
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
            temp_model = DeleteInstanceIpWhitelistResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTopicResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code.
        self.code = code
        # The result data that is returned.
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
        # Indicates whether the call is successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
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
            self.data = m.get('data')
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


class GetConsumerGroupResponseBodyDataConsumeRetryPolicy(TeaModel):
    def __init__(
        self,
        dead_letter_target_topic: str = None,
        fixed_interval_retry_time: int = None,
        max_retry_times: int = None,
        retry_policy: str = None,
    ):
        # The dead-letter topic.
        # 
        # If a consumer still fails to consume a message after the message is retried for a specified number of times, the message is delivered to a dead-letter topic for subsequent business recovery or troubleshooting. For more information, see [Consumption retry and dead-letter messages](https://help.aliyun.com/document_detail/440356.html).
        self.dead_letter_target_topic = dead_letter_target_topic
        self.fixed_interval_retry_time = fixed_interval_retry_time
        # The maximum number of retries.
        self.max_retry_times = max_retry_times
        # The retry policy.
        # 
        # Valid values:
        # 
        # *   FixedRetryPolicy
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     Failed messages are retried at a fixed interval
        # 
        #     <!-- -->
        # 
        #     .
        # 
        # *   DefaultRetryPolicy
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     Failed messages are retried at incremental intervals as the number of retries increases
        # 
        #     <!-- -->
        # 
        #     .
        self.retry_policy = retry_policy

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dead_letter_target_topic is not None:
            result['deadLetterTargetTopic'] = self.dead_letter_target_topic
        if self.fixed_interval_retry_time is not None:
            result['fixedIntervalRetryTime'] = self.fixed_interval_retry_time
        if self.max_retry_times is not None:
            result['maxRetryTimes'] = self.max_retry_times
        if self.retry_policy is not None:
            result['retryPolicy'] = self.retry_policy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deadLetterTargetTopic') is not None:
            self.dead_letter_target_topic = m.get('deadLetterTargetTopic')
        if m.get('fixedIntervalRetryTime') is not None:
            self.fixed_interval_retry_time = m.get('fixedIntervalRetryTime')
        if m.get('maxRetryTimes') is not None:
            self.max_retry_times = m.get('maxRetryTimes')
        if m.get('retryPolicy') is not None:
            self.retry_policy = m.get('retryPolicy')
        return self


class GetConsumerGroupResponseBodyData(TeaModel):
    def __init__(
        self,
        consume_retry_policy: GetConsumerGroupResponseBodyDataConsumeRetryPolicy = None,
        consumer_group_id: str = None,
        create_time: str = None,
        delivery_order_type: str = None,
        instance_id: str = None,
        max_receive_tps: int = None,
        region_id: str = None,
        remark: str = None,
        status: str = None,
        update_time: str = None,
    ):
        # The consumption retry policy that you want to configure for the consumer group. For more information, see [Consumption retry](https://help.aliyun.com/document_detail/440356.html).
        self.consume_retry_policy = consume_retry_policy
        # The ID of the consumer group.
        self.consumer_group_id = consumer_group_id
        # The time when the consumer group was created.
        self.create_time = create_time
        # The message delivery order of the consumer group.
        # 
        # Valid values:
        # 
        # *   Concurrently
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     concurrent delivery
        # 
        #     <!-- -->
        # 
        # *   Orderly
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     ordered delivery
        # 
        #     <!-- -->
        self.delivery_order_type = delivery_order_type
        # The ID of the instance.
        self.instance_id = instance_id
        # Maximum received message tps
        self.max_receive_tps = max_receive_tps
        # The ID of the region in which the instance resides.
        self.region_id = region_id
        # The remarks on the consumer group.
        self.remark = remark
        # The state of the consumer group.
        # 
        # Valid values:
        # 
        # *   RUNNING
        # 
        #     <!-- -->
        # 
        #     : The consumer group is
        # 
        #     <!-- -->
        # 
        #     running
        # 
        #     <!-- -->
        # 
        #     .
        # 
        # *   CREATING
        # 
        #     <!-- -->
        # 
        #     : The consumer group is
        # 
        #     <!-- -->
        # 
        #     being created
        # 
        #     <!-- -->
        # 
        #     .
        self.status = status
        # The time when the consumer group was last updated.
        self.update_time = update_time

    def validate(self):
        if self.consume_retry_policy:
            self.consume_retry_policy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consume_retry_policy is not None:
            result['consumeRetryPolicy'] = self.consume_retry_policy.to_map()
        if self.consumer_group_id is not None:
            result['consumerGroupId'] = self.consumer_group_id
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.delivery_order_type is not None:
            result['deliveryOrderType'] = self.delivery_order_type
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.max_receive_tps is not None:
            result['maxReceiveTps'] = self.max_receive_tps
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.remark is not None:
            result['remark'] = self.remark
        if self.status is not None:
            result['status'] = self.status
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('consumeRetryPolicy') is not None:
            temp_model = GetConsumerGroupResponseBodyDataConsumeRetryPolicy()
            self.consume_retry_policy = temp_model.from_map(m['consumeRetryPolicy'])
        if m.get('consumerGroupId') is not None:
            self.consumer_group_id = m.get('consumerGroupId')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('deliveryOrderType') is not None:
            self.delivery_order_type = m.get('deliveryOrderType')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('maxReceiveTps') is not None:
            self.max_receive_tps = m.get('maxReceiveTps')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        return self


class GetConsumerGroupResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetConsumerGroupResponseBodyData = None,
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
        # Indicates whether the call is successful.
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
            temp_model = GetConsumerGroupResponseBodyData()
            self.data = temp_model.from_map(m['data'])
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


class GetConsumerGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetConsumerGroupResponseBody = None,
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
            temp_model = GetConsumerGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetConsumerGroupLagRequest(TeaModel):
    def __init__(
        self,
        topic_name: str = None,
    ):
        # The topic name.
        self.topic_name = topic_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.topic_name is not None:
            result['topicName'] = self.topic_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('topicName') is not None:
            self.topic_name = m.get('topicName')
        return self


class GetConsumerGroupLagResponseBodyDataTotalLag(TeaModel):
    def __init__(
        self,
        delivery_duration: int = None,
        inflight_count: int = None,
        last_consume_timestamp: int = None,
        ready_count: int = None,
    ):
        # Delivery delay time, in seconds
        self.delivery_duration = delivery_duration
        # The number of messages being consumed.
        self.inflight_count = inflight_count
        # Last consumption time
        self.last_consume_timestamp = last_consume_timestamp
        # Ready message count
        self.ready_count = ready_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delivery_duration is not None:
            result['deliveryDuration'] = self.delivery_duration
        if self.inflight_count is not None:
            result['inflightCount'] = self.inflight_count
        if self.last_consume_timestamp is not None:
            result['lastConsumeTimestamp'] = self.last_consume_timestamp
        if self.ready_count is not None:
            result['readyCount'] = self.ready_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deliveryDuration') is not None:
            self.delivery_duration = m.get('deliveryDuration')
        if m.get('inflightCount') is not None:
            self.inflight_count = m.get('inflightCount')
        if m.get('lastConsumeTimestamp') is not None:
            self.last_consume_timestamp = m.get('lastConsumeTimestamp')
        if m.get('readyCount') is not None:
            self.ready_count = m.get('readyCount')
        return self


class GetConsumerGroupLagResponseBodyData(TeaModel):
    def __init__(
        self,
        consumer_group_id: str = None,
        instance_id: str = None,
        region_id: str = None,
        topic_lag_map: Dict[str, DataTopicLagMapValue] = None,
        total_lag: GetConsumerGroupLagResponseBodyDataTotalLag = None,
    ):
        # Consumer Group ID
        self.consumer_group_id = consumer_group_id
        # Instance ID
        self.instance_id = instance_id
        # Region ID
        self.region_id = region_id
        # Backlog for each topic
        self.topic_lag_map = topic_lag_map
        # Total lag count
        self.total_lag = total_lag

    def validate(self):
        if self.topic_lag_map:
            for v in self.topic_lag_map.values():
                if v:
                    v.validate()
        if self.total_lag:
            self.total_lag.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consumer_group_id is not None:
            result['consumerGroupId'] = self.consumer_group_id
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.region_id is not None:
            result['regionId'] = self.region_id
        result['topicLagMap'] = {}
        if self.topic_lag_map is not None:
            for k, v in self.topic_lag_map.items():
                result['topicLagMap'][k] = v.to_map()
        if self.total_lag is not None:
            result['totalLag'] = self.total_lag.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('consumerGroupId') is not None:
            self.consumer_group_id = m.get('consumerGroupId')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        self.topic_lag_map = {}
        if m.get('topicLagMap') is not None:
            for k, v in m.get('topicLagMap').items():
                temp_model = DataTopicLagMapValue()
                self.topic_lag_map[k] = temp_model.from_map(v)
        if m.get('totalLag') is not None:
            temp_model = GetConsumerGroupLagResponseBodyDataTotalLag()
            self.total_lag = temp_model.from_map(m['totalLag'])
        return self


class GetConsumerGroupLagResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetConsumerGroupLagResponseBodyData = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Error code
        self.code = code
        # The returned data.
        self.data = data
        # Dynamic error code
        self.dynamic_code = dynamic_code
        # The dynamic error message.
        self.dynamic_message = dynamic_message
        # HTTP status code
        self.http_status_code = http_status_code
        # Error message
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
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
            temp_model = GetConsumerGroupLagResponseBodyData()
            self.data = temp_model.from_map(m['data'])
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


class GetConsumerGroupLagResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetConsumerGroupLagResponseBody = None,
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
            temp_model = GetConsumerGroupLagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetConsumerGroupSubscriptionResponseBodyDataConnectionDTO(TeaModel):
    def __init__(
        self,
        client_id: str = None,
        egress_ip: str = None,
        hostname: str = None,
        language: str = None,
        message_model: str = None,
        version: str = None,
    ):
        # The client ID.
        self.client_id = client_id
        # The public IP address of the host.
        self.egress_ip = egress_ip
        # The host name.
        self.hostname = hostname
        # The language used by the client.
        self.language = language
        # The consumption mode of the consumer group. Valid values:
        # 
        # *   BROADCASTING: broadcasting consumption
        # *   CLUSTERING: clustering consumption
        self.message_model = message_model
        # The client version.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['clientId'] = self.client_id
        if self.egress_ip is not None:
            result['egressIp'] = self.egress_ip
        if self.hostname is not None:
            result['hostname'] = self.hostname
        if self.language is not None:
            result['language'] = self.language
        if self.message_model is not None:
            result['messageModel'] = self.message_model
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientId') is not None:
            self.client_id = m.get('clientId')
        if m.get('egressIp') is not None:
            self.egress_ip = m.get('egressIp')
        if m.get('hostname') is not None:
            self.hostname = m.get('hostname')
        if m.get('language') is not None:
            self.language = m.get('language')
        if m.get('messageModel') is not None:
            self.message_model = m.get('messageModel')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class GetConsumerGroupSubscriptionResponseBodyDataSubscriptionDTO(TeaModel):
    def __init__(
        self,
        consumer_group_id: str = None,
        filter_expression: str = None,
        filter_expression_type: str = None,
        message_model: str = None,
        subscription_status: str = None,
        topic_name: str = None,
    ):
        # The consumer group ID.
        self.consumer_group_id = consumer_group_id
        # The filter expression.
        self.filter_expression = filter_expression
        # The type of the filter expression. Valid values:
        # 
        # *   SQL: filters messages by using SQL expressions.
        # *   TAG: filters messages by using tags.
        self.filter_expression_type = filter_expression_type
        # The consumption mode of the consumer group. Valid values:
        # 
        # *   BROADCASTING: broadcasting consumption
        # *   CLUSTERING: clustering consumption
        self.message_model = message_model
        # The subscription status. Valid values:
        # 
        # *   ONLINE: The consumer group is online. If the consumer group contains multiple consumers, this value is returned if at least one of the consumers is online.
        # *   OFFLINE: The consumer group is offline. If the consumer group contains multiple consumers, this value is returned only if all consumers are offline.
        self.subscription_status = subscription_status
        # The topic to which the consumer group subscribes.
        self.topic_name = topic_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consumer_group_id is not None:
            result['consumerGroupId'] = self.consumer_group_id
        if self.filter_expression is not None:
            result['filterExpression'] = self.filter_expression
        if self.filter_expression_type is not None:
            result['filterExpressionType'] = self.filter_expression_type
        if self.message_model is not None:
            result['messageModel'] = self.message_model
        if self.subscription_status is not None:
            result['subscriptionStatus'] = self.subscription_status
        if self.topic_name is not None:
            result['topicName'] = self.topic_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('consumerGroupId') is not None:
            self.consumer_group_id = m.get('consumerGroupId')
        if m.get('filterExpression') is not None:
            self.filter_expression = m.get('filterExpression')
        if m.get('filterExpressionType') is not None:
            self.filter_expression_type = m.get('filterExpressionType')
        if m.get('messageModel') is not None:
            self.message_model = m.get('messageModel')
        if m.get('subscriptionStatus') is not None:
            self.subscription_status = m.get('subscriptionStatus')
        if m.get('topicName') is not None:
            self.topic_name = m.get('topicName')
        return self


class GetConsumerGroupSubscriptionResponseBodyData(TeaModel):
    def __init__(
        self,
        connection_dto: GetConsumerGroupSubscriptionResponseBodyDataConnectionDTO = None,
        subscription_dto: GetConsumerGroupSubscriptionResponseBodyDataSubscriptionDTO = None,
    ):
        # The connection details.
        self.connection_dto = connection_dto
        # The subscription details.
        self.subscription_dto = subscription_dto

    def validate(self):
        if self.connection_dto:
            self.connection_dto.validate()
        if self.subscription_dto:
            self.subscription_dto.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_dto is not None:
            result['connectionDTO'] = self.connection_dto.to_map()
        if self.subscription_dto is not None:
            result['subscriptionDTO'] = self.subscription_dto.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('connectionDTO') is not None:
            temp_model = GetConsumerGroupSubscriptionResponseBodyDataConnectionDTO()
            self.connection_dto = temp_model.from_map(m['connectionDTO'])
        if m.get('subscriptionDTO') is not None:
            temp_model = GetConsumerGroupSubscriptionResponseBodyDataSubscriptionDTO()
            self.subscription_dto = temp_model.from_map(m['subscriptionDTO'])
        return self


class GetConsumerGroupSubscriptionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetConsumerGroupSubscriptionResponseBodyData] = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code.
        self.code = code
        # The data returned.
        self.data = data
        # The dynamic error code.
        self.dynamic_code = dynamic_code
        # The dynamic error message.
        self.dynamic_message = dynamic_message
        # The response code.
        self.http_status_code = http_status_code
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
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
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = GetConsumerGroupSubscriptionResponseBodyData()
                self.data.append(temp_model.from_map(k))
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


class GetConsumerGroupSubscriptionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetConsumerGroupSubscriptionResponseBody = None,
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
            temp_model = GetConsumerGroupSubscriptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetConsumerStackRequest(TeaModel):
    def __init__(
        self,
        client_id: str = None,
    ):
        # The client ID.
        # 
        # This parameter is required.
        self.client_id = client_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['clientId'] = self.client_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientId') is not None:
            self.client_id = m.get('clientId')
        return self


class GetConsumerStackResponseBodyDataStacks(TeaModel):
    def __init__(
        self,
        thread: str = None,
        tracks: List[str] = None,
    ):
        # Thread id.
        self.thread = thread
        # Stack Information.
        self.tracks = tracks

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.thread is not None:
            result['thread'] = self.thread
        if self.tracks is not None:
            result['tracks'] = self.tracks
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('thread') is not None:
            self.thread = m.get('thread')
        if m.get('tracks') is not None:
            self.tracks = m.get('tracks')
        return self


class GetConsumerStackResponseBodyData(TeaModel):
    def __init__(
        self,
        consumer_group_id: str = None,
        instance_id: str = None,
        region_id: str = None,
        stacks: List[GetConsumerStackResponseBodyDataStacks] = None,
    ):
        # The ID of the consumer group.
        self.consumer_group_id = consumer_group_id
        # The instance ID.
        self.instance_id = instance_id
        # The region ID.
        self.region_id = region_id
        # Stack Information.
        self.stacks = stacks

    def validate(self):
        if self.stacks:
            for k in self.stacks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consumer_group_id is not None:
            result['consumerGroupId'] = self.consumer_group_id
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.region_id is not None:
            result['regionId'] = self.region_id
        result['stacks'] = []
        if self.stacks is not None:
            for k in self.stacks:
                result['stacks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('consumerGroupId') is not None:
            self.consumer_group_id = m.get('consumerGroupId')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        self.stacks = []
        if m.get('stacks') is not None:
            for k in m.get('stacks'):
                temp_model = GetConsumerStackResponseBodyDataStacks()
                self.stacks.append(temp_model.from_map(k))
        return self


class GetConsumerStackResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetConsumerStackResponseBodyData = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code.
        self.code = code
        # The data returned.
        self.data = data
        # The dynamic error code.
        self.dynamic_code = dynamic_code
        # The dynamic error message.
        self.dynamic_message = dynamic_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
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
            temp_model = GetConsumerStackResponseBodyData()
            self.data = temp_model.from_map(m['data'])
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


class GetConsumerStackResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetConsumerStackResponseBody = None,
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
            temp_model = GetConsumerStackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDisasterRecoveryItemResponseBodyDataTopics(TeaModel):
    def __init__(
        self,
        consumer_group_id: str = None,
        delivery_order_type: str = None,
        instance_id: str = None,
        instance_type: str = None,
        region_id: str = None,
        topic_name: str = None,
    ):
        # The consumer group ID.
        self.consumer_group_id = consumer_group_id
        # The order in which messages are delivered to the target instance. The parameter values ​​are as follows:
        #   - Concurrently: concurrent delivery
        #   - Orderly: sequential delivery
        self.delivery_order_type = delivery_order_type
        # The instance ID.
        self.instance_id = instance_id
        # Instance type
        #   - ALIYUN_ROCKETMQ: Alibaba Cloud instance
        #   - EXTERNAL_ROCKETMQ: External instance, open-source instance, open-source cluster
        self.instance_type = instance_type
        # regionId
        self.region_id = region_id
        # The topic name.
        self.topic_name = topic_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consumer_group_id is not None:
            result['consumerGroupId'] = self.consumer_group_id
        if self.delivery_order_type is not None:
            result['deliveryOrderType'] = self.delivery_order_type
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.topic_name is not None:
            result['topicName'] = self.topic_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('consumerGroupId') is not None:
            self.consumer_group_id = m.get('consumerGroupId')
        if m.get('deliveryOrderType') is not None:
            self.delivery_order_type = m.get('deliveryOrderType')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('topicName') is not None:
            self.topic_name = m.get('topicName')
        return self


class GetDisasterRecoveryItemResponseBodyData(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        ext_info: Dict[str, str] = None,
        item_id: int = None,
        item_status: str = None,
        plan_id: int = None,
        topics: List[GetDisasterRecoveryItemResponseBodyDataTopics] = None,
        update_time: str = None,
    ):
        # The time when the topic mapping task was created.
        self.create_time = create_time
        # Additional Information
        self.ext_info = ext_info
        # The ID of the topic mapping
        self.item_id = item_id
        # The topic mapping task status.
        self.item_status = item_status
        # The ID of the global message backup plan.
        self.plan_id = plan_id
        # Topics included in the backup mapping
        self.topics = topics
        # The time when the topic mapping task was last updated.
        self.update_time = update_time

    def validate(self):
        if self.topics:
            for k in self.topics:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.ext_info is not None:
            result['extInfo'] = self.ext_info
        if self.item_id is not None:
            result['itemId'] = self.item_id
        if self.item_status is not None:
            result['itemStatus'] = self.item_status
        if self.plan_id is not None:
            result['planId'] = self.plan_id
        result['topics'] = []
        if self.topics is not None:
            for k in self.topics:
                result['topics'].append(k.to_map() if k else None)
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('extInfo') is not None:
            self.ext_info = m.get('extInfo')
        if m.get('itemId') is not None:
            self.item_id = m.get('itemId')
        if m.get('itemStatus') is not None:
            self.item_status = m.get('itemStatus')
        if m.get('planId') is not None:
            self.plan_id = m.get('planId')
        self.topics = []
        if m.get('topics') is not None:
            for k in m.get('topics'):
                temp_model = GetDisasterRecoveryItemResponseBodyDataTopics()
                self.topics.append(temp_model.from_map(k))
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        return self


class GetDisasterRecoveryItemResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: GetDisasterRecoveryItemResponseBodyData = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details about the access denial. This parameter is returned only if the access is denied because the Resource Access Management (RAM) user does not have the required permissions.
        self.access_denied_detail = access_denied_detail
        # The error code.
        self.code = code
        # The data returned.
        self.data = data
        # The dynamic error code.
        self.dynamic_code = dynamic_code
        # The dynamic error message.
        self.dynamic_message = dynamic_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The error message.
        self.message = message
        # Request ID
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['accessDeniedDetail'] = self.access_denied_detail
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
        if m.get('accessDeniedDetail') is not None:
            self.access_denied_detail = m.get('accessDeniedDetail')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = GetDisasterRecoveryItemResponseBodyData()
            self.data = temp_model.from_map(m['data'])
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


class GetDisasterRecoveryItemResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDisasterRecoveryItemResponseBody = None,
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
            temp_model = GetDisasterRecoveryItemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDisasterRecoveryPlanResponseBodyDataInstancesMessageProperty(TeaModel):
    def __init__(
        self,
        property_key: str = None,
        property_value: str = None,
    ):
        # Property key
        self.property_key = property_key
        # Property value
        self.property_value = property_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.property_key is not None:
            result['propertyKey'] = self.property_key
        if self.property_value is not None:
            result['propertyValue'] = self.property_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('propertyKey') is not None:
            self.property_key = m.get('propertyKey')
        if m.get('propertyValue') is not None:
            self.property_value = m.get('propertyValue')
        return self


class GetDisasterRecoveryPlanResponseBodyDataInstances(TeaModel):
    def __init__(
        self,
        auth_type: str = None,
        consumer_group_id: str = None,
        endpoint_url: str = None,
        instance_id: str = None,
        instance_role: str = None,
        instance_type: str = None,
        message_property: GetDisasterRecoveryPlanResponseBodyDataInstancesMessageProperty = None,
        network_type: str = None,
        password: str = None,
        region_id: str = None,
        security_group_id: str = None,
        username: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        # Authentication method. Not required for instanceType of ALIYUN_ROCKETMQ and version 4.0
        #   - NO_AUTH: No authentication required
        #   - ACL_AUTH: ACL authentication
        self.auth_type = auth_type
        self.consumer_group_id = consumer_group_id
        # Endpoint URL, not required for instanceType of ALIYUN_ROCKETMQ, but required for EXTERNAL_ROCKETMQ
        self.endpoint_url = endpoint_url
        # The instance ID.
        self.instance_id = instance_id
        # Instance role, either primary or secondary 
        #   - ACTIVE: Primary
        #   - PASSIVE: Secondary
        self.instance_role = instance_role
        # Instance type
        #   - ALIYUN_ROCKETMQ: Alibaba Cloud instance
        #   - EXTERNAL_ROCKETMQ: External instance, open-source instance, open-source cluster
        self.instance_type = instance_type
        # Message filtering properties. When messages are synchronized to the target cluster, this property will be automatically added for SQL filtering during message consumption.
        self.message_property = message_property
        # Network type, not required for instanceType of ALIYUN_ROCKETMQ, but required for EXTERNAL_ROCKETMQ Parameter values are as follows:
        #   - TCP_INTERNET: TCP public network
        #   - TCP_VPC: TCP VPC (Virtual Private Cloud)
        self.network_type = network_type
        # Authentication password, required when authType is ACL_AUTH. Not required for instanceType of ALIYUN_ROCKETMQ
        self.password = password
        # Region ID.
        self.region_id = region_id
        # Security group ID, required only when the instanceType is EXTERNAL_ROCKETMQ and networkType is TCP_VPC.
        self.security_group_id = security_group_id
        # Authentication username, required when authType is ACL_AUTH
        self.username = username
        # The ID of the switch associated with the instance, required only when the instanceType is EXTERNAL_ROCKETMQ and networkType is TCP_VPC.
        self.v_switch_id = v_switch_id
        # The ID of the private network associated with the created instance. The instanceType instance type is only EXTERNAL_ROCKETMQ. It is required when the networkType is TCP_VPC.
        self.vpc_id = vpc_id

    def validate(self):
        if self.message_property:
            self.message_property.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_type is not None:
            result['authType'] = self.auth_type
        if self.consumer_group_id is not None:
            result['consumerGroupId'] = self.consumer_group_id
        if self.endpoint_url is not None:
            result['endpointUrl'] = self.endpoint_url
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.instance_role is not None:
            result['instanceRole'] = self.instance_role
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        if self.message_property is not None:
            result['messageProperty'] = self.message_property.to_map()
        if self.network_type is not None:
            result['networkType'] = self.network_type
        if self.password is not None:
            result['password'] = self.password
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.security_group_id is not None:
            result['securityGroupId'] = self.security_group_id
        if self.username is not None:
            result['username'] = self.username
        if self.v_switch_id is not None:
            result['vSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authType') is not None:
            self.auth_type = m.get('authType')
        if m.get('consumerGroupId') is not None:
            self.consumer_group_id = m.get('consumerGroupId')
        if m.get('endpointUrl') is not None:
            self.endpoint_url = m.get('endpointUrl')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('instanceRole') is not None:
            self.instance_role = m.get('instanceRole')
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        if m.get('messageProperty') is not None:
            temp_model = GetDisasterRecoveryPlanResponseBodyDataInstancesMessageProperty()
            self.message_property = temp_model.from_map(m['messageProperty'])
        if m.get('networkType') is not None:
            self.network_type = m.get('networkType')
        if m.get('password') is not None:
            self.password = m.get('password')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('securityGroupId') is not None:
            self.security_group_id = m.get('securityGroupId')
        if m.get('username') is not None:
            self.username = m.get('username')
        if m.get('vSwitchId') is not None:
            self.v_switch_id = m.get('vSwitchId')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        return self


class GetDisasterRecoveryPlanResponseBodyData(TeaModel):
    def __init__(
        self,
        auto_sync_checkpoint: bool = None,
        create_time: str = None,
        ext_info: Dict[str, str] = None,
        instances: List[GetDisasterRecoveryPlanResponseBodyDataInstances] = None,
        plan_desc: str = None,
        plan_id: int = None,
        plan_name: str = None,
        plan_status: str = None,
        plan_type: str = None,
        sync_checkpoint_enabled: bool = None,
        update_time: str = None,
    ):
        # Whether to enable automatic synchronization of consumption progress.
        self.auto_sync_checkpoint = auto_sync_checkpoint
        # The time when the backup plan was created.
        self.create_time = create_time
        # Additional Information
        self.ext_info = ext_info
        # Instances involved in the backup plan
        self.instances = instances
        # The describe of the global message backup plan.
        self.plan_desc = plan_desc
        # The ID of the global message backup plan.
        self.plan_id = plan_id
        # The name of the global message backup plan.
        self.plan_name = plan_name
        # The status of the global message backup plan.
        self.plan_status = plan_status
        # The type of the global message backup plan.
        # values are as follows:
        #   - ACTIVE_PASSIVE: One-way backup
        #   - ACTIVE_ACTIVE: Two-way backup
        self.plan_type = plan_type
        # Switch for synchronizing consumption progress
        self.sync_checkpoint_enabled = sync_checkpoint_enabled
        # The time when the backup plan was created.
        self.update_time = update_time

    def validate(self):
        if self.instances:
            for k in self.instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_sync_checkpoint is not None:
            result['autoSyncCheckpoint'] = self.auto_sync_checkpoint
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.ext_info is not None:
            result['extInfo'] = self.ext_info
        result['instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['instances'].append(k.to_map() if k else None)
        if self.plan_desc is not None:
            result['planDesc'] = self.plan_desc
        if self.plan_id is not None:
            result['planId'] = self.plan_id
        if self.plan_name is not None:
            result['planName'] = self.plan_name
        if self.plan_status is not None:
            result['planStatus'] = self.plan_status
        if self.plan_type is not None:
            result['planType'] = self.plan_type
        if self.sync_checkpoint_enabled is not None:
            result['syncCheckpointEnabled'] = self.sync_checkpoint_enabled
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoSyncCheckpoint') is not None:
            self.auto_sync_checkpoint = m.get('autoSyncCheckpoint')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('extInfo') is not None:
            self.ext_info = m.get('extInfo')
        self.instances = []
        if m.get('instances') is not None:
            for k in m.get('instances'):
                temp_model = GetDisasterRecoveryPlanResponseBodyDataInstances()
                self.instances.append(temp_model.from_map(k))
        if m.get('planDesc') is not None:
            self.plan_desc = m.get('planDesc')
        if m.get('planId') is not None:
            self.plan_id = m.get('planId')
        if m.get('planName') is not None:
            self.plan_name = m.get('planName')
        if m.get('planStatus') is not None:
            self.plan_status = m.get('planStatus')
        if m.get('planType') is not None:
            self.plan_type = m.get('planType')
        if m.get('syncCheckpointEnabled') is not None:
            self.sync_checkpoint_enabled = m.get('syncCheckpointEnabled')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        return self


class GetDisasterRecoveryPlanResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: GetDisasterRecoveryPlanResponseBodyData = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details about the access denial. This parameter is returned only if the access is denied because the Resource Access Management (RAM) user does not have the required permissions.
        self.access_denied_detail = access_denied_detail
        # The error code.
        self.code = code
        # The data returned.
        self.data = data
        # The dynamic error code.
        self.dynamic_code = dynamic_code
        # The dynamic error message.
        self.dynamic_message = dynamic_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the call was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['accessDeniedDetail'] = self.access_denied_detail
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
        if m.get('accessDeniedDetail') is not None:
            self.access_denied_detail = m.get('accessDeniedDetail')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = GetDisasterRecoveryPlanResponseBodyData()
            self.data = temp_model.from_map(m['data'])
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


class GetDisasterRecoveryPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDisasterRecoveryPlanResponseBody = None,
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
            temp_model = GetDisasterRecoveryPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstanceResponseBodyDataAccountInfo(TeaModel):
    def __init__(
        self,
        username: str = None,
    ):
        # The username of the instance. If you access a ApsaraMQ for RocketMQ instance over the Internet, you must configure the username and password of the instance in the SDK code for authentication.
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.username is not None:
            result['username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('username') is not None:
            self.username = m.get('username')
        return self


class GetInstanceResponseBodyDataAclInfo(TeaModel):
    def __init__(
        self,
        acl_type: str = None,
        acl_types: List[str] = None,
        default_vpc_auth_free: bool = None,
    ):
        # The authentication type of the instance. This parameter is no longer in use. We recommend that you configure aclTypes.
        # 
        # Valid values:
        # 
        # - default: intelligent identity authentication
        # 
        # - apache_acl:access control list (ACL) identity authentication**\
        self.acl_type = acl_type
        # The authentication types of the instance.
        self.acl_types = acl_types
        # Indicates whether the authentication-free in VPCs feature is enabled.
        # 
        # Valid values:
        # 
        # *   true
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   false
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.default_vpc_auth_free = default_vpc_auth_free

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_type is not None:
            result['aclType'] = self.acl_type
        if self.acl_types is not None:
            result['aclTypes'] = self.acl_types
        if self.default_vpc_auth_free is not None:
            result['defaultVpcAuthFree'] = self.default_vpc_auth_free
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aclType') is not None:
            self.acl_type = m.get('aclType')
        if m.get('aclTypes') is not None:
            self.acl_types = m.get('aclTypes')
        if m.get('defaultVpcAuthFree') is not None:
            self.default_vpc_auth_free = m.get('defaultVpcAuthFree')
        return self


class GetInstanceResponseBodyDataExtConfig(TeaModel):
    def __init__(
        self,
        acl_type: str = None,
        auto_scaling: bool = None,
        flow_out_bandwidth: int = None,
        flow_out_type: str = None,
        internet_spec: str = None,
        message_retention_time: int = None,
        msg_process_spec: str = None,
        send_receive_ratio: float = None,
        support_auto_scaling: bool = None,
    ):
        # The authentication type of the instance.
        # 
        # Valid value:
        # 
        # *   default: intelligent authentication
        self.acl_type = acl_type
        # Specifies whether to enable the elastic TPS feature for the instance.
        # 
        # Valid values:
        # 
        # *   true: enable
        # *   false: disable
        # 
        # This parameter is valid only when the supportAutoScaling parameter is set to enable.
        self.auto_scaling = auto_scaling
        # The Internet bandwidth. Unit: MB/s.
        self.flow_out_bandwidth = flow_out_bandwidth
        # The metering method of Internet usage.
        # 
        # Valid values:
        # 
        # *   PayByTraffic: pay-by-traffic
        # *   paybybandwidth: pay-by-bandwidth
        # *   uninvolved: N/A
        self.flow_out_type = flow_out_type
        # Indicates whether Internet access is enabled.
        # 
        # Valid values:
        # 
        # *   enable
        # *   disable
        # 
        # By default, you can access ApsaraMQ for RocketMQ instances in virtual private clouds (VPCs). If you enable the Internet access feature, you are charged for Internet outbound bandwidth. For more information, see [Internet access fees](https://help.aliyun.com/document_detail/427240.html).
        self.internet_spec = internet_spec
        # The retention period of messages. Unit: hours.
        # 
        # For information about the valid values of this parameter, see the "Limits on resource quotas" section in [Usage limits](https://help.aliyun.com/document_detail/440347.html).
        # 
        # The storage of messages in ApsaraMQ for RocketMQ is serverless and scalable. You are charged for message storage based on your actual usage. You can change the retention period of messages to adjust storage capacity. For more information, see [Storage fee](https://help.aliyun.com/document_detail/427238.html).
        self.message_retention_time = message_retention_time
        # The computing specification that is used to send and receive messages. For information about the upper limit of TPS, see [Instance specifications](https://help.aliyun.com/document_detail/444715.html).
        self.msg_process_spec = msg_process_spec
        # The ratio between sent messages and received messages in the instance.
        self.send_receive_ratio = send_receive_ratio
        # Specifies whether the elastic TPS feature is supported by the instance.
        # 
        # Valid values:
        # 
        # *   true: enable
        # *   false: disable
        # 
        # After you enable the elastic TPS feature for a ApsaraMQ for RocketMQ instance, you can use a specific amount of TPS that exceeds the specification limit. You are charged for the elastic TPS feature. For more information, see [Computing fee](https://help.aliyun.com/document_detail/427237.html).
        # 
        # > The elastic TPS feature is supported only by specific instance editions. For more information, see [Instance specifications](https://help.aliyun.com/document_detail/444715.html).
        self.support_auto_scaling = support_auto_scaling

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_type is not None:
            result['aclType'] = self.acl_type
        if self.auto_scaling is not None:
            result['autoScaling'] = self.auto_scaling
        if self.flow_out_bandwidth is not None:
            result['flowOutBandwidth'] = self.flow_out_bandwidth
        if self.flow_out_type is not None:
            result['flowOutType'] = self.flow_out_type
        if self.internet_spec is not None:
            result['internetSpec'] = self.internet_spec
        if self.message_retention_time is not None:
            result['messageRetentionTime'] = self.message_retention_time
        if self.msg_process_spec is not None:
            result['msgProcessSpec'] = self.msg_process_spec
        if self.send_receive_ratio is not None:
            result['sendReceiveRatio'] = self.send_receive_ratio
        if self.support_auto_scaling is not None:
            result['supportAutoScaling'] = self.support_auto_scaling
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aclType') is not None:
            self.acl_type = m.get('aclType')
        if m.get('autoScaling') is not None:
            self.auto_scaling = m.get('autoScaling')
        if m.get('flowOutBandwidth') is not None:
            self.flow_out_bandwidth = m.get('flowOutBandwidth')
        if m.get('flowOutType') is not None:
            self.flow_out_type = m.get('flowOutType')
        if m.get('internetSpec') is not None:
            self.internet_spec = m.get('internetSpec')
        if m.get('messageRetentionTime') is not None:
            self.message_retention_time = m.get('messageRetentionTime')
        if m.get('msgProcessSpec') is not None:
            self.msg_process_spec = m.get('msgProcessSpec')
        if m.get('sendReceiveRatio') is not None:
            self.send_receive_ratio = m.get('sendReceiveRatio')
        if m.get('supportAutoScaling') is not None:
            self.support_auto_scaling = m.get('supportAutoScaling')
        return self


class GetInstanceResponseBodyDataInstanceQuotas(TeaModel):
    def __init__(
        self,
        free_count: float = None,
        quota_name: str = None,
        total_count: float = None,
        used_count: float = None,
    ):
        # The number of topics that are free of charge on the instance.
        self.free_count = free_count
        # The quota name.
        # 
        # Valid value:
        # 
        # *   TOPIC_COUNT: the number of topics that can be created on the instance
        self.quota_name = quota_name
        # The total number of topics on the instance.
        self.total_count = total_count
        # The number of used topics on the instance.
        self.used_count = used_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.free_count is not None:
            result['freeCount'] = self.free_count
        if self.quota_name is not None:
            result['quotaName'] = self.quota_name
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        if self.used_count is not None:
            result['usedCount'] = self.used_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('freeCount') is not None:
            self.free_count = m.get('freeCount')
        if m.get('quotaName') is not None:
            self.quota_name = m.get('quotaName')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        if m.get('usedCount') is not None:
            self.used_count = m.get('usedCount')
        return self


class GetInstanceResponseBodyDataNetworkInfoEndpoints(TeaModel):
    def __init__(
        self,
        endpoint_type: str = None,
        endpoint_url: str = None,
        ip_whitelist: List[str] = None,
    ):
        # The type of the endpoint that is used to access the instance.
        # 
        # Valid values:
        # 
        # *   TCP_VPC: VPC endpoint
        # *   TCP_INTERNET: public endpoint
        self.endpoint_type = endpoint_type
        # The endpoint that is used to access the instance.
        self.endpoint_url = endpoint_url
        # The whitelist that includes the IP addresses that are allowed to access the ApsaraMQ for RocketMQ broker over the Internet. This parameter can be configured only if you use the public endpoint to access the instance.
        # 
        # *   If you do not configure an IP address whitelist, all CIDR blocks are allowed to access the ApsaraMQ for RocketMQ broker over the Internet.
        # *   If you configure an IP address whitelist, only the IP addresses in the whitelist are allowed to access the ApsaraMQ for RocketMQ broker over the Internet.
        # 
        # We recommend that you configure internetInfo.ipWhitelist instead of this parameter.
        self.ip_whitelist = ip_whitelist

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_type is not None:
            result['endpointType'] = self.endpoint_type
        if self.endpoint_url is not None:
            result['endpointUrl'] = self.endpoint_url
        if self.ip_whitelist is not None:
            result['ipWhitelist'] = self.ip_whitelist
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endpointType') is not None:
            self.endpoint_type = m.get('endpointType')
        if m.get('endpointUrl') is not None:
            self.endpoint_url = m.get('endpointUrl')
        if m.get('ipWhitelist') is not None:
            self.ip_whitelist = m.get('ipWhitelist')
        return self


class GetInstanceResponseBodyDataNetworkInfoInternetInfo(TeaModel):
    def __init__(
        self,
        flow_out_bandwidth: int = None,
        flow_out_type: str = None,
        internet_spec: str = None,
        ip_whitelist: List[str] = None,
    ):
        # The Internet bandwidth. Unit: MB/s.
        self.flow_out_bandwidth = flow_out_bandwidth
        # The metering method for Internet usage.
        # 
        # Valid values:
        # 
        # *   PayByBandwidth: pay-by-bandwidth. If the Internet access feature is enabled, specify this value for the parameter.
        # *   uninvolved: N/A. If the Internet access feature is not enabled, specify this value for the parameter.
        self.flow_out_type = flow_out_type
        # Specifies whether to enable the Internet access feature.
        # 
        # Valid values:
        # 
        # *   enable
        # *   disable
        # 
        # By default, ApsaraMQ for RocketMQ instances are accessed in virtual private clouds (VPCs). If you enable the Internet access feature, you are charged for Internet outbound bandwidth. For more information, see [Internet access fee](https://help.aliyun.com/document_detail/427240.html).
        self.internet_spec = internet_spec
        # The whitelist that includes the IP addresses that are allowed to access the ApsaraMQ for RocketMQ broker.
        # 
        # *   If this parameter is not configured, all IP addresses are allowed to access the ApsaraMQ for RocketMQ broker over the Internet.
        # *   If this parameter is configured, only the IP addresses that are included in the whitelist can access the ApsaraMQ for RocketMQ broker over the Internet.
        self.ip_whitelist = ip_whitelist

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_out_bandwidth is not None:
            result['flowOutBandwidth'] = self.flow_out_bandwidth
        if self.flow_out_type is not None:
            result['flowOutType'] = self.flow_out_type
        if self.internet_spec is not None:
            result['internetSpec'] = self.internet_spec
        if self.ip_whitelist is not None:
            result['ipWhitelist'] = self.ip_whitelist
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('flowOutBandwidth') is not None:
            self.flow_out_bandwidth = m.get('flowOutBandwidth')
        if m.get('flowOutType') is not None:
            self.flow_out_type = m.get('flowOutType')
        if m.get('internetSpec') is not None:
            self.internet_spec = m.get('internetSpec')
        if m.get('ipWhitelist') is not None:
            self.ip_whitelist = m.get('ipWhitelist')
        return self


class GetInstanceResponseBodyDataNetworkInfoVpcInfoVSwitches(TeaModel):
    def __init__(
        self,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        # The vSwitch ID.
        self.v_switch_id = v_switch_id
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.v_switch_id is not None:
            result['vSwitchId'] = self.v_switch_id
        if self.zone_id is not None:
            result['zoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('vSwitchId') is not None:
            self.v_switch_id = m.get('vSwitchId')
        if m.get('zoneId') is not None:
            self.zone_id = m.get('zoneId')
        return self


class GetInstanceResponseBodyDataNetworkInfoVpcInfo(TeaModel):
    def __init__(
        self,
        security_group_ids: str = None,
        v_switch_id: str = None,
        v_switches: List[GetInstanceResponseBodyDataNetworkInfoVpcInfoVSwitches] = None,
        vpc_id: str = None,
    ):
        # The security group ID.
        self.security_group_ids = security_group_ids
        # The ID of the vSwitch with which the instance is associated.
        self.v_switch_id = v_switch_id
        # The vSwitches.
        self.v_switches = v_switches
        # The ID of the VPC with which the instance is associated.
        self.vpc_id = vpc_id

    def validate(self):
        if self.v_switches:
            for k in self.v_switches:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_group_ids is not None:
            result['securityGroupIds'] = self.security_group_ids
        if self.v_switch_id is not None:
            result['vSwitchId'] = self.v_switch_id
        result['vSwitches'] = []
        if self.v_switches is not None:
            for k in self.v_switches:
                result['vSwitches'].append(k.to_map() if k else None)
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('securityGroupIds') is not None:
            self.security_group_ids = m.get('securityGroupIds')
        if m.get('vSwitchId') is not None:
            self.v_switch_id = m.get('vSwitchId')
        self.v_switches = []
        if m.get('vSwitches') is not None:
            for k in m.get('vSwitches'):
                temp_model = GetInstanceResponseBodyDataNetworkInfoVpcInfoVSwitches()
                self.v_switches.append(temp_model.from_map(k))
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        return self


class GetInstanceResponseBodyDataNetworkInfo(TeaModel):
    def __init__(
        self,
        endpoints: List[GetInstanceResponseBodyDataNetworkInfoEndpoints] = None,
        internet_info: GetInstanceResponseBodyDataNetworkInfoInternetInfo = None,
        vpc_info: GetInstanceResponseBodyDataNetworkInfoVpcInfo = None,
    ):
        # The endpoints.
        self.endpoints = endpoints
        # The information about the Internet.
        self.internet_info = internet_info
        # The virtual private cloud (VPC) information.
        self.vpc_info = vpc_info

    def validate(self):
        if self.endpoints:
            for k in self.endpoints:
                if k:
                    k.validate()
        if self.internet_info:
            self.internet_info.validate()
        if self.vpc_info:
            self.vpc_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['endpoints'] = []
        if self.endpoints is not None:
            for k in self.endpoints:
                result['endpoints'].append(k.to_map() if k else None)
        if self.internet_info is not None:
            result['internetInfo'] = self.internet_info.to_map()
        if self.vpc_info is not None:
            result['vpcInfo'] = self.vpc_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.endpoints = []
        if m.get('endpoints') is not None:
            for k in m.get('endpoints'):
                temp_model = GetInstanceResponseBodyDataNetworkInfoEndpoints()
                self.endpoints.append(temp_model.from_map(k))
        if m.get('internetInfo') is not None:
            temp_model = GetInstanceResponseBodyDataNetworkInfoInternetInfo()
            self.internet_info = temp_model.from_map(m['internetInfo'])
        if m.get('vpcInfo') is not None:
            temp_model = GetInstanceResponseBodyDataNetworkInfoVpcInfo()
            self.vpc_info = temp_model.from_map(m['vpcInfo'])
        return self


class GetInstanceResponseBodyDataProductInfo(TeaModel):
    def __init__(
        self,
        auto_scaling: bool = None,
        message_retention_time: int = None,
        msg_process_spec: str = None,
        send_receive_ratio: float = None,
        storage_encryption: bool = None,
        storage_secret_key: str = None,
        support_auto_scaling: bool = None,
        trace_on: bool = None,
    ):
        # Specifies whether to enable the elastic TPS feature for the instance.
        # 
        # Valid values:
        # 
        # *   true: enable
        # *   false: disable
        # 
        # This parameter is valid only when the supportAutoScaling parameter is set to enable.
        self.auto_scaling = auto_scaling
        # The retention period of messages. Unit: hours.
        # 
        # For information about the valid values of this parameter, see the "Limits on resource quotas" section in [Usage limits](https://help.aliyun.com/document_detail/440347.html).
        # 
        # The storage of messages in ApsaraMQ for RocketMQ is serverless and scalable. You are charged for message storage based on your actual usage. You can change the retention period of messages to adjust storage capacity. For more information, see [Storage fee](https://help.aliyun.com/document_detail/427238.html).
        self.message_retention_time = message_retention_time
        # The computing specification that is used to send and receive messages. For information about the upper limit of TPS, see [Instance specifications](https://help.aliyun.com/document_detail/444715.html).
        self.msg_process_spec = msg_process_spec
        # The ratio between sent messages and received messages in the instance.
        self.send_receive_ratio = send_receive_ratio
        # Indicates whether storage encryption is enabled.
        self.storage_encryption = storage_encryption
        # The storage encryption key.
        self.storage_secret_key = storage_secret_key
        # Specifies whether to enable the elastic TPS feature for the instance.
        # 
        # Valid values:
        # 
        # *   true: enable
        # *   false: disable
        # 
        # After you enable the elastic TPS feature for a ApsaraMQ for RocketMQ instance, you can use a specific amount of TPS that exceeds the specification limit. You are charged for the elastic TPS feature. For more information, see [Computing fee](https://help.aliyun.com/document_detail/427237.html).
        # 
        # > The elastic TPS feature is supported by only specific instance editions. For more information, see [Instance specifications](https://help.aliyun.com/document_detail/444715.html).
        self.support_auto_scaling = support_auto_scaling
        # Indicates whether the message trace feature is enabled. Valid values:
        # 
        # *   true
        # *   false
        # 
        # This parameter is not in use. By default, the message trace feature is enabled for ApsaraMQ for RocketMQ instances, regardless of whether this parameter is configured.
        self.trace_on = trace_on

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_scaling is not None:
            result['autoScaling'] = self.auto_scaling
        if self.message_retention_time is not None:
            result['messageRetentionTime'] = self.message_retention_time
        if self.msg_process_spec is not None:
            result['msgProcessSpec'] = self.msg_process_spec
        if self.send_receive_ratio is not None:
            result['sendReceiveRatio'] = self.send_receive_ratio
        if self.storage_encryption is not None:
            result['storageEncryption'] = self.storage_encryption
        if self.storage_secret_key is not None:
            result['storageSecretKey'] = self.storage_secret_key
        if self.support_auto_scaling is not None:
            result['supportAutoScaling'] = self.support_auto_scaling
        if self.trace_on is not None:
            result['traceOn'] = self.trace_on
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoScaling') is not None:
            self.auto_scaling = m.get('autoScaling')
        if m.get('messageRetentionTime') is not None:
            self.message_retention_time = m.get('messageRetentionTime')
        if m.get('msgProcessSpec') is not None:
            self.msg_process_spec = m.get('msgProcessSpec')
        if m.get('sendReceiveRatio') is not None:
            self.send_receive_ratio = m.get('sendReceiveRatio')
        if m.get('storageEncryption') is not None:
            self.storage_encryption = m.get('storageEncryption')
        if m.get('storageSecretKey') is not None:
            self.storage_secret_key = m.get('storageSecretKey')
        if m.get('supportAutoScaling') is not None:
            self.support_auto_scaling = m.get('supportAutoScaling')
        if m.get('traceOn') is not None:
            self.trace_on = m.get('traceOn')
        return self


class GetInstanceResponseBodyDataSoftware(TeaModel):
    def __init__(
        self,
        maintain_time: str = None,
        software_version: str = None,
        upgrade_method: str = None,
    ):
        # The period of upgrade time.
        self.maintain_time = maintain_time
        # The version of software.
        self.software_version = software_version
        # The upgrade method.
        # 
        # Valid values:
        # 
        # - Auto: automatic upgrade
        # 
        # - Manual: manual upgrade
        self.upgrade_method = upgrade_method

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.maintain_time is not None:
            result['maintainTime'] = self.maintain_time
        if self.software_version is not None:
            result['softwareVersion'] = self.software_version
        if self.upgrade_method is not None:
            result['upgradeMethod'] = self.upgrade_method
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maintainTime') is not None:
            self.maintain_time = m.get('maintainTime')
        if m.get('softwareVersion') is not None:
            self.software_version = m.get('softwareVersion')
        if m.get('upgradeMethod') is not None:
            self.upgrade_method = m.get('upgradeMethod')
        return self


class GetInstanceResponseBodyDataTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the resource.
        self.key = key
        # The tag value of the resource.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class GetInstanceResponseBodyData(TeaModel):
    def __init__(
        self,
        account_info: GetInstanceResponseBodyDataAccountInfo = None,
        acl_info: GetInstanceResponseBodyDataAclInfo = None,
        bid: str = None,
        commodity_code: str = None,
        create_time: str = None,
        expire_time: str = None,
        ext_config: GetInstanceResponseBodyDataExtConfig = None,
        group_count: int = None,
        instance_id: str = None,
        instance_name: str = None,
        instance_quotas: List[GetInstanceResponseBodyDataInstanceQuotas] = None,
        network_info: GetInstanceResponseBodyDataNetworkInfo = None,
        payment_type: str = None,
        product_info: GetInstanceResponseBodyDataProductInfo = None,
        region_id: str = None,
        release_time: str = None,
        remark: str = None,
        resource_group_id: str = None,
        series_code: str = None,
        service_code: str = None,
        software: GetInstanceResponseBodyDataSoftware = None,
        start_time: str = None,
        status: str = None,
        sub_series_code: str = None,
        tags: List[GetInstanceResponseBodyDataTags] = None,
        topic_count: int = None,
        update_time: str = None,
        user_id: str = None,
    ):
        # The account information.
        self.account_info = account_info
        # The information about access control.
        self.acl_info = acl_info
        # The business ID (BID) of the commodity.
        self.bid = bid
        # The commodity code of the instance. The commodity code of a ApsaraMQ for RocketMQ 5.0 instance has a similar format as ons_rmqsub_public_cn.
        self.commodity_code = commodity_code
        # The time when the instance was created.
        self.create_time = create_time
        # The time when the instance expires.
        self.expire_time = expire_time
        # The extended configurations. We recommend you configure productInfo, internetInfo, or aclInfo instead of this parameter.
        self.ext_config = ext_config
        # The number of groups.
        self.group_count = group_count
        # The ID of the instance
        self.instance_id = instance_id
        # The name of the instance.
        self.instance_name = instance_name
        # The instance quotas.
        self.instance_quotas = instance_quotas
        # The network information.
        self.network_info = network_info
        # The billing method of the instance.
        # 
        # Valid values:
        # 
        # *   PayAsYouGo
        # *   Subscription
        self.payment_type = payment_type
        # The extended configurations of the instance.
        self.product_info = product_info
        # The ID of the region in which the instance resides.
        self.region_id = region_id
        # The time when the instance was released.
        self.release_time = release_time
        # The description of the instance.
        self.remark = remark
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The primary edition of the instance. For information about the differences between primary edition instances, see [Instance selection](https://help.aliyun.com/document_detail/444722.html).
        # 
        # Valid values:
        # 
        # *   standard: Standard Edition
        # *   ultimate: Enterprise Platinum Edition
        # *   professional: Professional Edition
        self.series_code = series_code
        # The code of the service to which the instance belongs. The service code of ApsaraMQ for RocketMQ is rmq.
        self.service_code = service_code
        # The instance software information.
        self.software = software
        # The time when the instance was started.
        self.start_time = start_time
        # The status of the instance.
        # 
        # Valid values:
        # 
        # *   RELEASED
        # *   RUNNING
        # *   STOPPED
        # *   CHANGING
        # *   CREATING
        self.status = status
        # The sub-category edition of the instance. For information about the differences between sub-category edition instances, see [Instance selection](https://help.aliyun.com/document_detail/444722.html).
        # 
        # Valid values:
        # 
        # *   cluster_ha: Cluster High-availability Edition
        # *   single_node: Standalone Edition
        self.sub_series_code = sub_series_code
        # The resource tags.
        self.tags = tags
        # The number of topics.
        self.topic_count = topic_count
        # The time when the instance was last modified.
        self.update_time = update_time
        # The ID of the user who owns the instance.
        self.user_id = user_id

    def validate(self):
        if self.account_info:
            self.account_info.validate()
        if self.acl_info:
            self.acl_info.validate()
        if self.ext_config:
            self.ext_config.validate()
        if self.instance_quotas:
            for k in self.instance_quotas:
                if k:
                    k.validate()
        if self.network_info:
            self.network_info.validate()
        if self.product_info:
            self.product_info.validate()
        if self.software:
            self.software.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_info is not None:
            result['accountInfo'] = self.account_info.to_map()
        if self.acl_info is not None:
            result['aclInfo'] = self.acl_info.to_map()
        if self.bid is not None:
            result['bid'] = self.bid
        if self.commodity_code is not None:
            result['commodityCode'] = self.commodity_code
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.expire_time is not None:
            result['expireTime'] = self.expire_time
        if self.ext_config is not None:
            result['extConfig'] = self.ext_config.to_map()
        if self.group_count is not None:
            result['groupCount'] = self.group_count
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.instance_name is not None:
            result['instanceName'] = self.instance_name
        result['instanceQuotas'] = []
        if self.instance_quotas is not None:
            for k in self.instance_quotas:
                result['instanceQuotas'].append(k.to_map() if k else None)
        if self.network_info is not None:
            result['networkInfo'] = self.network_info.to_map()
        if self.payment_type is not None:
            result['paymentType'] = self.payment_type
        if self.product_info is not None:
            result['productInfo'] = self.product_info.to_map()
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.release_time is not None:
            result['releaseTime'] = self.release_time
        if self.remark is not None:
            result['remark'] = self.remark
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        if self.series_code is not None:
            result['seriesCode'] = self.series_code
        if self.service_code is not None:
            result['serviceCode'] = self.service_code
        if self.software is not None:
            result['software'] = self.software.to_map()
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.status is not None:
            result['status'] = self.status
        if self.sub_series_code is not None:
            result['subSeriesCode'] = self.sub_series_code
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        if self.topic_count is not None:
            result['topicCount'] = self.topic_count
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountInfo') is not None:
            temp_model = GetInstanceResponseBodyDataAccountInfo()
            self.account_info = temp_model.from_map(m['accountInfo'])
        if m.get('aclInfo') is not None:
            temp_model = GetInstanceResponseBodyDataAclInfo()
            self.acl_info = temp_model.from_map(m['aclInfo'])
        if m.get('bid') is not None:
            self.bid = m.get('bid')
        if m.get('commodityCode') is not None:
            self.commodity_code = m.get('commodityCode')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('expireTime') is not None:
            self.expire_time = m.get('expireTime')
        if m.get('extConfig') is not None:
            temp_model = GetInstanceResponseBodyDataExtConfig()
            self.ext_config = temp_model.from_map(m['extConfig'])
        if m.get('groupCount') is not None:
            self.group_count = m.get('groupCount')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('instanceName') is not None:
            self.instance_name = m.get('instanceName')
        self.instance_quotas = []
        if m.get('instanceQuotas') is not None:
            for k in m.get('instanceQuotas'):
                temp_model = GetInstanceResponseBodyDataInstanceQuotas()
                self.instance_quotas.append(temp_model.from_map(k))
        if m.get('networkInfo') is not None:
            temp_model = GetInstanceResponseBodyDataNetworkInfo()
            self.network_info = temp_model.from_map(m['networkInfo'])
        if m.get('paymentType') is not None:
            self.payment_type = m.get('paymentType')
        if m.get('productInfo') is not None:
            temp_model = GetInstanceResponseBodyDataProductInfo()
            self.product_info = temp_model.from_map(m['productInfo'])
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('releaseTime') is not None:
            self.release_time = m.get('releaseTime')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('seriesCode') is not None:
            self.series_code = m.get('seriesCode')
        if m.get('serviceCode') is not None:
            self.service_code = m.get('serviceCode')
        if m.get('software') is not None:
            temp_model = GetInstanceResponseBodyDataSoftware()
            self.software = temp_model.from_map(m['software'])
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('subSeriesCode') is not None:
            self.sub_series_code = m.get('subSeriesCode')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = GetInstanceResponseBodyDataTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('topicCount') is not None:
            self.topic_count = m.get('topicCount')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class GetInstanceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetInstanceResponseBodyData = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code returned if the call failed.
        self.code = code
        # The data returned.
        self.data = data
        # The dynamic error code.
        self.dynamic_code = dynamic_code
        # The dynamic error message.
        self.dynamic_message = dynamic_message
        # The HTTP status code returned.
        self.http_status_code = http_status_code
        # The error message.
        self.message = message
        # The ID of the request. Each request has a unique ID. You can use this ID to troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the call was successful.
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
            temp_model = GetInstanceResponseBodyData()
            self.data = temp_model.from_map(m['data'])
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


class GetInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetInstanceResponseBody = None,
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
            temp_model = GetInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstanceAccountRequest(TeaModel):
    def __init__(
        self,
        username: str = None,
    ):
        # The username of the account.
        # 
        # If you do not configure this parameter, the default username of the instance is used.
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.username is not None:
            result['username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('username') is not None:
            self.username = m.get('username')
        return self


class GetInstanceAccountResponseBodyData(TeaModel):
    def __init__(
        self,
        account_status: str = None,
        password: str = None,
        username: str = None,
    ):
        # The status of the account.
        # 
        # Valid values:
        # 
        # *   DISABLE
        # *   ENABLE
        self.account_status = account_status
        # The password of the account.
        self.password = password
        # The username of the account.
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_status is not None:
            result['accountStatus'] = self.account_status
        if self.password is not None:
            result['password'] = self.password
        if self.username is not None:
            result['username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountStatus') is not None:
            self.account_status = m.get('accountStatus')
        if m.get('password') is not None:
            self.password = m.get('password')
        if m.get('username') is not None:
            self.username = m.get('username')
        return self


class GetInstanceAccountResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetInstanceAccountResponseBodyData = None,
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
        # Request ID, each request\\"s ID is unique and can be used for troubleshooting and problem localization.
        self.request_id = request_id
        # Indicates whether the request was successful.
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
            temp_model = GetInstanceAccountResponseBodyData()
            self.data = temp_model.from_map(m['data'])
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


class GetInstanceAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetInstanceAccountResponseBody = None,
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
            temp_model = GetInstanceAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstanceAclRequest(TeaModel):
    def __init__(
        self,
        resource_name: str = None,
        resource_type: str = None,
    ):
        # The name of the resource on which you want to grant permissions.
        # 
        # This parameter is required.
        self.resource_name = resource_name
        # The type of the resource on which you want to grant permissions.
        # 
        # Valid values:
        # 
        # *   Group
        # *   Topic
        # 
        # This parameter is required.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_name is not None:
            result['resourceName'] = self.resource_name
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resourceName') is not None:
            self.resource_name = m.get('resourceName')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        return self


class GetInstanceAclResponseBodyData(TeaModel):
    def __init__(
        self,
        acl_type: str = None,
        actions: List[str] = None,
        decision: str = None,
        instance_id: str = None,
        ip_whitelists: List[str] = None,
        region_id: str = None,
        resource_name: str = None,
        resource_type: str = None,
        username: str = None,
    ):
        # The authentication type of the instance.
        # 
        # Valid values:
        # 
        # *   apache_acl: open source access control list (ACL)
        # *   default: the default account of the instance
        self.acl_type = acl_type
        # The type of operations that can be performed on the resource.
        self.actions = actions
        # The decision result of the authorization.
        self.decision = decision
        # The instance ID.
        self.instance_id = instance_id
        # The IP address whitelists.
        self.ip_whitelists = ip_whitelists
        # The region ID.
        self.region_id = region_id
        # The name of the resource on which the permissions are granted.
        self.resource_name = resource_name
        # The type of the resource on which the permissions are granted.
        self.resource_type = resource_type
        # The username.
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_type is not None:
            result['aclType'] = self.acl_type
        if self.actions is not None:
            result['actions'] = self.actions
        if self.decision is not None:
            result['decision'] = self.decision
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.ip_whitelists is not None:
            result['ipWhitelists'] = self.ip_whitelists
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.resource_name is not None:
            result['resourceName'] = self.resource_name
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        if self.username is not None:
            result['username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aclType') is not None:
            self.acl_type = m.get('aclType')
        if m.get('actions') is not None:
            self.actions = m.get('actions')
        if m.get('decision') is not None:
            self.decision = m.get('decision')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('ipWhitelists') is not None:
            self.ip_whitelists = m.get('ipWhitelists')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('resourceName') is not None:
            self.resource_name = m.get('resourceName')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        if m.get('username') is not None:
            self.username = m.get('username')
        return self


class GetInstanceAclResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetInstanceAclResponseBodyData = None,
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
        # The response code.
        self.http_status_code = http_status_code
        # The error message.
        self.message = message
        # The request ID
        self.request_id = request_id
        # Indicates whether the request was successful.
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
            temp_model = GetInstanceAclResponseBodyData()
            self.data = temp_model.from_map(m['data'])
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


class GetInstanceAclResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetInstanceAclResponseBody = None,
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
            temp_model = GetInstanceAclResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstanceIpWhitelistRequest(TeaModel):
    def __init__(
        self,
        ip_whitelists: List[str] = None,
    ):
        # The  filter IP address whitelists.
        self.ip_whitelists = ip_whitelists

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_whitelists is not None:
            result['ipWhitelists'] = self.ip_whitelists
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ipWhitelists') is not None:
            self.ip_whitelists = m.get('ipWhitelists')
        return self


class GetInstanceIpWhitelistShrinkRequest(TeaModel):
    def __init__(
        self,
        ip_whitelists_shrink: str = None,
    ):
        # The  filter IP address whitelists.
        self.ip_whitelists_shrink = ip_whitelists_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_whitelists_shrink is not None:
            result['ipWhitelists'] = self.ip_whitelists_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ipWhitelists') is not None:
            self.ip_whitelists_shrink = m.get('ipWhitelists')
        return self


class GetInstanceIpWhitelistResponseBodyData(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        ip_whitelists: List[str] = None,
        region_id: str = None,
    ):
        # The instance ID.
        self.instance_id = instance_id
        # The IP address whitelists.
        self.ip_whitelists = ip_whitelists
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.ip_whitelists is not None:
            result['ipWhitelists'] = self.ip_whitelists
        if self.region_id is not None:
            result['regionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('ipWhitelists') is not None:
            self.ip_whitelists = m.get('ipWhitelists')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        return self


class GetInstanceIpWhitelistResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetInstanceIpWhitelistResponseBodyData = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code.
        self.code = code
        # The data returned.
        self.data = data
        # The dynamic error code.
        self.dynamic_code = dynamic_code
        # The dynamic error message.
        self.dynamic_message = dynamic_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the call was successful.
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
            temp_model = GetInstanceIpWhitelistResponseBodyData()
            self.data = temp_model.from_map(m['data'])
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


class GetInstanceIpWhitelistResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetInstanceIpWhitelistResponseBody = None,
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
            temp_model = GetInstanceIpWhitelistResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMessageDetailResponseBodyData(TeaModel):
    def __init__(
        self,
        body: str = None,
        body_size: int = None,
        born_host: str = None,
        born_time: str = None,
        instance_id: str = None,
        message_group: str = None,
        message_id: str = None,
        message_keys: List[str] = None,
        message_tag: str = None,
        message_type: str = None,
        region_id: str = None,
        store_host: str = None,
        store_time: str = None,
        system_properties: Dict[str, str] = None,
        topic_name: str = None,
        user_properties: Dict[str, str] = None,
    ):
        # The message body.
        self.body = body
        # The size of the message body.
        self.body_size = body_size
        # The client on which the message was produced.
        self.born_host = born_host
        # The time when the message was generated.
        self.born_time = born_time
        # The instance ID.
        self.instance_id = instance_id
        # The sharding key. This parameter is returned only for ordered messages.
        self.message_group = message_group
        # The message ID.
        self.message_id = message_id
        # The message keys.
        self.message_keys = message_keys
        # The tags.
        self.message_tag = message_tag
        # The message type.
        self.message_type = message_type
        # The region ID.
        self.region_id = region_id
        # The broker on which the message was stored.
        self.store_host = store_host
        # The time when the message was stored.
        self.store_time = store_time
        # The default system attributes.
        self.system_properties = system_properties
        # The topic name.
        self.topic_name = topic_name
        # The user attributes.
        self.user_properties = user_properties

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        if self.body_size is not None:
            result['bodySize'] = self.body_size
        if self.born_host is not None:
            result['bornHost'] = self.born_host
        if self.born_time is not None:
            result['bornTime'] = self.born_time
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
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
        if self.system_properties is not None:
            result['systemProperties'] = self.system_properties
        if self.topic_name is not None:
            result['topicName'] = self.topic_name
        if self.user_properties is not None:
            result['userProperties'] = self.user_properties
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        if m.get('bodySize') is not None:
            self.body_size = m.get('bodySize')
        if m.get('bornHost') is not None:
            self.born_host = m.get('bornHost')
        if m.get('bornTime') is not None:
            self.born_time = m.get('bornTime')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
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
        if m.get('systemProperties') is not None:
            self.system_properties = m.get('systemProperties')
        if m.get('topicName') is not None:
            self.topic_name = m.get('topicName')
        if m.get('userProperties') is not None:
            self.user_properties = m.get('userProperties')
        return self


class GetMessageDetailResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetMessageDetailResponseBodyData = None,
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
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
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
            temp_model = GetMessageDetailResponseBodyData()
            self.data = temp_model.from_map(m['data'])
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


class GetMessageDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetMessageDetailResponseBody = None,
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
            temp_model = GetMessageDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTopicResponseBodyData(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        instance_id: str = None,
        max_send_tps: int = None,
        message_type: str = None,
        region_id: str = None,
        remark: str = None,
        status: str = None,
        topic_name: str = None,
        update_time: str = None,
    ):
        # Creation time of the topic.
        self.create_time = create_time
        # The ID of the instance to which the topic belongs.
        self.instance_id = instance_id
        # The maximum TPS for message sending.
        self.max_send_tps = max_send_tps
        # The type of messages in the topic.
        # 
        # Valid values:
        # 
        # *   TRANSACTION: transactional messages
        # *   FIFO: ordered messages
        # *   DELAY: scheduled or delayed messages
        # *   NORMAL: normal messages
        # 
        # Valid values:
        # 
        # *   TRANSACTION: transactional messages
        # *   FIFO: ordered messages
        # *   DELAY: scheduled or delayed messages
        # *   NORMAL: normal messages
        self.message_type = message_type
        # The region ID to which the instance belongs.
        self.region_id = region_id
        # Remark information of the topic.
        self.remark = remark
        # The topic status.
        # 
        # Valid values:
        # 
        # *   RUNNING
        # *   CREATING
        self.status = status
        # Topic name.
        self.topic_name = topic_name
        # Last modification time of the topic.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.max_send_tps is not None:
            result['maxSendTps'] = self.max_send_tps
        if self.message_type is not None:
            result['messageType'] = self.message_type
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.remark is not None:
            result['remark'] = self.remark
        if self.status is not None:
            result['status'] = self.status
        if self.topic_name is not None:
            result['topicName'] = self.topic_name
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('maxSendTps') is not None:
            self.max_send_tps = m.get('maxSendTps')
        if m.get('messageType') is not None:
            self.message_type = m.get('messageType')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('topicName') is not None:
            self.topic_name = m.get('topicName')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        return self


class GetTopicResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetTopicResponseBodyData = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Error code.
        self.code = code
        # The returned data.
        self.data = data
        # Dynamic error code.
        self.dynamic_code = dynamic_code
        # Dynamic error message.
        self.dynamic_message = dynamic_message
        # HTTP status code.
        self.http_status_code = http_status_code
        # Error message.
        self.message = message
        # Request ID, each request\\"s ID is unique and can be used for troubleshooting and problem localization.
        self.request_id = request_id
        # Indicates whether the execution was successful.
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
            temp_model = GetTopicResponseBodyData()
            self.data = temp_model.from_map(m['data'])
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


class GetTopicResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTopicResponseBody = None,
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
            temp_model = GetTopicResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTraceResponseBodyDataBrokerInfoOperations(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetTraceResponseBodyDataBrokerInfo(TeaModel):
    def __init__(
        self,
        delay_status: str = None,
        operations: List[GetTraceResponseBodyDataBrokerInfoOperations] = None,
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
            for k in self.operations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delay_status is not None:
            result['delayStatus'] = self.delay_status
        result['operations'] = []
        if self.operations is not None:
            for k in self.operations:
                result['operations'].append(k.to_map() if k else None)
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
            for k in m.get('operations'):
                temp_model = GetTraceResponseBodyDataBrokerInfoOperations()
                self.operations.append(temp_model.from_map(k))
        if m.get('presetDelayTime') is not None:
            self.preset_delay_time = m.get('presetDelayTime')
        if m.get('recallResult') is not None:
            self.recall_result = m.get('recallResult')
        return self


class GetTraceResponseBodyDataConsumerInfosDeadLetterInfo(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetTraceResponseBodyDataConsumerInfosRecordsOperations(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetTraceResponseBodyDataConsumerInfosRecords(TeaModel):
    def __init__(
        self,
        client_host: str = None,
        consume_status: str = None,
        fifo_enable: bool = None,
        operations: List[GetTraceResponseBodyDataConsumerInfosRecordsOperations] = None,
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
            for k in self.operations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_host is not None:
            result['clientHost'] = self.client_host
        if self.consume_status is not None:
            result['consumeStatus'] = self.consume_status
        if self.fifo_enable is not None:
            result['fifoEnable'] = self.fifo_enable
        result['operations'] = []
        if self.operations is not None:
            for k in self.operations:
                result['operations'].append(k.to_map() if k else None)
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
            for k in m.get('operations'):
                temp_model = GetTraceResponseBodyDataConsumerInfosRecordsOperations()
                self.operations.append(temp_model.from_map(k))
        if m.get('popCk') is not None:
            self.pop_ck = m.get('popCk')
        if m.get('userName') is not None:
            self.user_name = m.get('userName')
        return self


class GetTraceResponseBodyDataConsumerInfos(TeaModel):
    def __init__(
        self,
        consume_status: str = None,
        consumer_group_id: str = None,
        dead_letter_info: GetTraceResponseBodyDataConsumerInfosDeadLetterInfo = None,
        dead_message: bool = None,
        records: List[GetTraceResponseBodyDataConsumerInfosRecords] = None,
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
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            for k in self.records:
                result['records'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('consumeStatus') is not None:
            self.consume_status = m.get('consumeStatus')
        if m.get('consumerGroupId') is not None:
            self.consumer_group_id = m.get('consumerGroupId')
        if m.get('deadLetterInfo') is not None:
            temp_model = GetTraceResponseBodyDataConsumerInfosDeadLetterInfo()
            self.dead_letter_info = temp_model.from_map(m['deadLetterInfo'])
        if m.get('deadMessage') is not None:
            self.dead_message = m.get('deadMessage')
        self.records = []
        if m.get('records') is not None:
            for k in m.get('records'):
                temp_model = GetTraceResponseBodyDataConsumerInfosRecords()
                self.records.append(temp_model.from_map(k))
        return self


class GetTraceResponseBodyDataMessageInfo(TeaModel):
    def __init__(
        self,
        body: str = None,
        born_host: str = None,
        born_time: str = None,
        instance_id: str = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        if self.born_host is not None:
            result['bornHost'] = self.born_host
        if self.born_time is not None:
            result['bornTime'] = self.born_time
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
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


class GetTraceResponseBodyDataProducerInfoRecords(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetTraceResponseBodyDataProducerInfo(TeaModel):
    def __init__(
        self,
        records: List[GetTraceResponseBodyDataProducerInfoRecords] = None,
    ):
        # The production records.
        self.records = records

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['records'] = []
        if self.records is not None:
            for k in self.records:
                result['records'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.records = []
        if m.get('records') is not None:
            for k in m.get('records'):
                temp_model = GetTraceResponseBodyDataProducerInfoRecords()
                self.records.append(temp_model.from_map(k))
        return self


class GetTraceResponseBodyData(TeaModel):
    def __init__(
        self,
        broker_info: GetTraceResponseBodyDataBrokerInfo = None,
        consumer_infos: List[GetTraceResponseBodyDataConsumerInfos] = None,
        instance_id: str = None,
        message_info: GetTraceResponseBodyDataMessageInfo = None,
        producer_info: GetTraceResponseBodyDataProducerInfo = None,
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
            for k in self.consumer_infos:
                if k:
                    k.validate()
        if self.message_info:
            self.message_info.validate()
        if self.producer_info:
            self.producer_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.broker_info is not None:
            result['brokerInfo'] = self.broker_info.to_map()
        result['consumerInfos'] = []
        if self.consumer_infos is not None:
            for k in self.consumer_infos:
                result['consumerInfos'].append(k.to_map() if k else None)
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
            temp_model = GetTraceResponseBodyDataBrokerInfo()
            self.broker_info = temp_model.from_map(m['brokerInfo'])
        self.consumer_infos = []
        if m.get('consumerInfos') is not None:
            for k in m.get('consumerInfos'):
                temp_model = GetTraceResponseBodyDataConsumerInfos()
                self.consumer_infos.append(temp_model.from_map(k))
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('messageInfo') is not None:
            temp_model = GetTraceResponseBodyDataMessageInfo()
            self.message_info = temp_model.from_map(m['messageInfo'])
        if m.get('producerInfo') is not None:
            temp_model = GetTraceResponseBodyDataProducerInfo()
            self.producer_info = temp_model.from_map(m['producerInfo'])
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('topicName') is not None:
            self.topic_name = m.get('topicName')
        return self


class GetTraceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetTraceResponseBodyData = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = GetTraceResponseBodyData()
            self.data = temp_model.from_map(m['data'])
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


class GetTraceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTraceResponseBody = None,
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
            temp_model = GetTraceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAvailableZonesResponseBodyData(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        update_time: str = None,
        zone_id: str = None,
        zone_name: str = None,
    ):
        # The time when the zone was created.
        self.create_time = create_time
        # The time when the zone was last updated.
        self.update_time = update_time
        # The ID of the current zone.
        self.zone_id = zone_id
        # The name of the current zone.
        self.zone_name = zone_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        if self.zone_id is not None:
            result['zoneId'] = self.zone_id
        if self.zone_name is not None:
            result['zoneName'] = self.zone_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        if m.get('zoneId') is not None:
            self.zone_id = m.get('zoneId')
        if m.get('zoneName') is not None:
            self.zone_name = m.get('zoneName')
        return self


class ListAvailableZonesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ListAvailableZonesResponseBodyData] = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code returned if the call failed.
        self.code = code
        # The result data that is returned.
        self.data = data
        # The dynamic error code.
        self.dynamic_code = dynamic_code
        # The dynamic error message.
        self.dynamic_message = dynamic_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The error message.
        self.message = message
        # The ID of the request. Each request has a unique ID. You can use this ID to troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the call was successful.
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
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
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ListAvailableZonesResponseBodyData()
                self.data.append(temp_model.from_map(k))
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


class ListAvailableZonesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAvailableZonesResponseBody = None,
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
            temp_model = ListAvailableZonesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListConsumerConnectionsResponseBodyDataConnections(TeaModel):
    def __init__(
        self,
        client_id: str = None,
        egress_ip: str = None,
        hostname: str = None,
        language: str = None,
        message_model: str = None,
        version: str = None,
    ):
        # The ID of the client.
        self.client_id = client_id
        # Host IP/Public IP
        self.egress_ip = egress_ip
        # The `hostname` of the cloud-native box.
        self.hostname = hostname
        # The language of the client.
        self.language = language
        # Consumption Mode
        # - BROADCASTING
        # - CLUSTERING
        self.message_model = message_model
        # The version of the client.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['clientId'] = self.client_id
        if self.egress_ip is not None:
            result['egressIp'] = self.egress_ip
        if self.hostname is not None:
            result['hostname'] = self.hostname
        if self.language is not None:
            result['language'] = self.language
        if self.message_model is not None:
            result['messageModel'] = self.message_model
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientId') is not None:
            self.client_id = m.get('clientId')
        if m.get('egressIp') is not None:
            self.egress_ip = m.get('egressIp')
        if m.get('hostname') is not None:
            self.hostname = m.get('hostname')
        if m.get('language') is not None:
            self.language = m.get('language')
        if m.get('messageModel') is not None:
            self.message_model = m.get('messageModel')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class ListConsumerConnectionsResponseBodyData(TeaModel):
    def __init__(
        self,
        connections: List[ListConsumerConnectionsResponseBodyDataConnections] = None,
        consumer_group_id: str = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        # The client connection list
        self.connections = connections
        # The consumer group ID.
        self.consumer_group_id = consumer_group_id
        # The instance ID.
        self.instance_id = instance_id
        # The ID of the region in which the instance resides.
        self.region_id = region_id

    def validate(self):
        if self.connections:
            for k in self.connections:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['connections'] = []
        if self.connections is not None:
            for k in self.connections:
                result['connections'].append(k.to_map() if k else None)
        if self.consumer_group_id is not None:
            result['consumerGroupId'] = self.consumer_group_id
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.region_id is not None:
            result['regionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.connections = []
        if m.get('connections') is not None:
            for k in m.get('connections'):
                temp_model = ListConsumerConnectionsResponseBodyDataConnections()
                self.connections.append(temp_model.from_map(k))
        if m.get('consumerGroupId') is not None:
            self.consumer_group_id = m.get('consumerGroupId')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        return self


class ListConsumerConnectionsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListConsumerConnectionsResponseBodyData = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The returned error code.
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
        # The ID of the request. Each request has a unique ID. You can use this ID to troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the call was successful.
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
            temp_model = ListConsumerConnectionsResponseBodyData()
            self.data = temp_model.from_map(m['data'])
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


class ListConsumerConnectionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListConsumerConnectionsResponseBody = None,
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
            temp_model = ListConsumerConnectionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListConsumerGroupSubscriptionsRequest(TeaModel):
    def __init__(
        self,
        topic_name: str = None,
    ):
        # The topic name. If you do not specify this parameter, all subscriptions of the consumer group are queried.
        self.topic_name = topic_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.topic_name is not None:
            result['topicName'] = self.topic_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('topicName') is not None:
            self.topic_name = m.get('topicName')
        return self


class ListConsumerGroupSubscriptionsResponseBodyData(TeaModel):
    def __init__(
        self,
        consistency: bool = None,
        consumer_group_id: str = None,
        filter_expression: str = None,
        filter_expression_type: str = None,
        message_model: str = None,
        subscription_status: str = None,
        topic_created: bool = None,
        topic_name: str = None,
    ):
        # Indicates whether message consumption is consistent. Valid values:
        # 
        # *   false: Unconsumed messages exist in the consumer group.
        # *   true: No unconsumed message exists in the consumer group.
        self.consistency = consistency
        # The ID of the consumer group.
        self.consumer_group_id = consumer_group_id
        # The filter expression.
        self.filter_expression = filter_expression
        # The type of the filter expression. Valid values:
        # 
        # *   SQL: filters messages by using SQL expressions.
        # *   TAG: filters messages by using tags.
        self.filter_expression_type = filter_expression_type
        # The consumption mode of the consumer group. Valid values:
        # 
        # *   BROADCASTING: broadcasting consumption
        # *   CLUSTERING: clustering consumption
        self.message_model = message_model
        # The subscription status. Valid values:
        # 
        # *   ONLINE: The consumer group is online. If the consumer group contains multiple consumers, this value is returned as long as one of the consumers is online.
        # *   OFFLINE: The consumer group is offline. If the consumer group contains multiple consumers, this value is returned only if all consumers are offline.
        self.subscription_status = subscription_status
        # Indicates whether the topic is created.
        self.topic_created = topic_created
        # The topic to which the consumer group subscribes.
        self.topic_name = topic_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consistency is not None:
            result['consistency'] = self.consistency
        if self.consumer_group_id is not None:
            result['consumerGroupId'] = self.consumer_group_id
        if self.filter_expression is not None:
            result['filterExpression'] = self.filter_expression
        if self.filter_expression_type is not None:
            result['filterExpressionType'] = self.filter_expression_type
        if self.message_model is not None:
            result['messageModel'] = self.message_model
        if self.subscription_status is not None:
            result['subscriptionStatus'] = self.subscription_status
        if self.topic_created is not None:
            result['topicCreated'] = self.topic_created
        if self.topic_name is not None:
            result['topicName'] = self.topic_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('consistency') is not None:
            self.consistency = m.get('consistency')
        if m.get('consumerGroupId') is not None:
            self.consumer_group_id = m.get('consumerGroupId')
        if m.get('filterExpression') is not None:
            self.filter_expression = m.get('filterExpression')
        if m.get('filterExpressionType') is not None:
            self.filter_expression_type = m.get('filterExpressionType')
        if m.get('messageModel') is not None:
            self.message_model = m.get('messageModel')
        if m.get('subscriptionStatus') is not None:
            self.subscription_status = m.get('subscriptionStatus')
        if m.get('topicCreated') is not None:
            self.topic_created = m.get('topicCreated')
        if m.get('topicName') is not None:
            self.topic_name = m.get('topicName')
        return self


class ListConsumerGroupSubscriptionsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ListConsumerGroupSubscriptionsResponseBodyData] = None,
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
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
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
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ListConsumerGroupSubscriptionsResponseBodyData()
                self.data.append(temp_model.from_map(k))
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


class ListConsumerGroupSubscriptionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListConsumerGroupSubscriptionsResponseBody = None,
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
            temp_model = ListConsumerGroupSubscriptionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListConsumerGroupsRequest(TeaModel):
    def __init__(
        self,
        filter: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The filter condition for the query. If not provided, all consumer groups under the specified instance will be queried.
        self.filter = filter
        # Page number, indicating which page of results to return.
        self.page_number = page_number
        # Page size, the maximum number of results to display per page.
        # 
        # Value range: [10, 100].
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter is not None:
            result['filter'] = self.filter
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filter') is not None:
            self.filter = m.get('filter')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListConsumerGroupsResponseBodyDataList(TeaModel):
    def __init__(
        self,
        consumer_group_id: str = None,
        create_time: str = None,
        instance_id: str = None,
        max_receive_tps: int = None,
        region_id: str = None,
        remark: str = None,
        status: str = None,
        update_time: str = None,
    ):
        # Consumer group ID.
        self.consumer_group_id = consumer_group_id
        # Creation time of the consumer group.
        self.create_time = create_time
        # Instance ID.
        self.instance_id = instance_id
        # The maximum TPS for message sending.
        self.max_receive_tps = max_receive_tps
        # The region ID to which the instance belongs.
        self.region_id = region_id
        # Remark information of the consumer group.
        self.remark = remark
        # Status of the consumer group.
        self.status = status
        # Last update time of the consumer group.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consumer_group_id is not None:
            result['consumerGroupId'] = self.consumer_group_id
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.max_receive_tps is not None:
            result['maxReceiveTps'] = self.max_receive_tps
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.remark is not None:
            result['remark'] = self.remark
        if self.status is not None:
            result['status'] = self.status
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('consumerGroupId') is not None:
            self.consumer_group_id = m.get('consumerGroupId')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('maxReceiveTps') is not None:
            self.max_receive_tps = m.get('maxReceiveTps')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        return self


class ListConsumerGroupsResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[ListConsumerGroupsResponseBodyDataList] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The consumer groups.
        self.list = list
        # Current page number.
        self.page_number = page_number
        # Page size.
        self.page_size = page_size
        # Total number of returned results.
        self.total_count = total_count

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = ListConsumerGroupsResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListConsumerGroupsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListConsumerGroupsResponseBodyData = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Error code.
        self.code = code
        # The returned data.
        self.data = data
        # Dynamic error code.
        self.dynamic_code = dynamic_code
        # The dynamic error message.
        self.dynamic_message = dynamic_message
        # HTTP status code.
        self.http_status_code = http_status_code
        # Error message.
        self.message = message
        # Request ID, each request has a unique ID that can be used for troubleshooting and problem localization.
        self.request_id = request_id
        # Indicates whether the execution was successful.
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
            temp_model = ListConsumerGroupsResponseBodyData()
            self.data = temp_model.from_map(m['data'])
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


class ListConsumerGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListConsumerGroupsResponseBody = None,
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
            temp_model = ListConsumerGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDisasterRecoveryCheckpointsRequest(TeaModel):
    def __init__(
        self,
        filter: str = None,
        instance_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # Filter Condition
        self.filter = filter
        # Source Instance ID
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Current page number, starting from 1.
        self.page_number = page_number
        # Page size, the maximum number of results returned per page.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter is not None:
            result['filter'] = self.filter
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filter') is not None:
            self.filter = m.get('filter')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListDisasterRecoveryCheckpointsResponseBodyDataListSourceProgressProgressData(TeaModel):
    def __init__(
        self,
        consume_timestamp: int = None,
    ):
        # Latest consumption time
        self.consume_timestamp = consume_timestamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consume_timestamp is not None:
            result['consumeTimestamp'] = self.consume_timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('consumeTimestamp') is not None:
            self.consume_timestamp = m.get('consumeTimestamp')
        return self


class ListDisasterRecoveryCheckpointsResponseBodyDataListSourceProgress(TeaModel):
    def __init__(
        self,
        consumer_group_id: str = None,
        instance_id: str = None,
        instance_type: str = None,
        last_fetch_time: int = None,
        progress_data: ListDisasterRecoveryCheckpointsResponseBodyDataListSourceProgressProgressData = None,
        region_id: str = None,
        topic_name: str = None,
    ):
        # Consumer Group ID
        self.consumer_group_id = consumer_group_id
        # Instance ID
        self.instance_id = instance_id
        # Instance type
        #   - ALIYUN_ROCKETMQ: Alibaba Cloud instance
        #   - EXTERNAL_ROCKETMQ: External instance, open-source instance, open-source cluster
        self.instance_type = instance_type
        # Last fetch time
        self.last_fetch_time = last_fetch_time
        # Consumption progress data
        self.progress_data = progress_data
        # Region ID
        self.region_id = region_id
        # The topic name.
        self.topic_name = topic_name

    def validate(self):
        if self.progress_data:
            self.progress_data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consumer_group_id is not None:
            result['consumerGroupId'] = self.consumer_group_id
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        if self.last_fetch_time is not None:
            result['lastFetchTime'] = self.last_fetch_time
        if self.progress_data is not None:
            result['progressData'] = self.progress_data.to_map()
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.topic_name is not None:
            result['topicName'] = self.topic_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('consumerGroupId') is not None:
            self.consumer_group_id = m.get('consumerGroupId')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        if m.get('lastFetchTime') is not None:
            self.last_fetch_time = m.get('lastFetchTime')
        if m.get('progressData') is not None:
            temp_model = ListDisasterRecoveryCheckpointsResponseBodyDataListSourceProgressProgressData()
            self.progress_data = temp_model.from_map(m['progressData'])
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('topicName') is not None:
            self.topic_name = m.get('topicName')
        return self


class ListDisasterRecoveryCheckpointsResponseBodyDataListTargetProgressProgressData(TeaModel):
    def __init__(
        self,
        consume_timestamp: int = None,
    ):
        # Latest consumption time
        self.consume_timestamp = consume_timestamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consume_timestamp is not None:
            result['consumeTimestamp'] = self.consume_timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('consumeTimestamp') is not None:
            self.consume_timestamp = m.get('consumeTimestamp')
        return self


class ListDisasterRecoveryCheckpointsResponseBodyDataListTargetProgress(TeaModel):
    def __init__(
        self,
        consumer_group_id: str = None,
        instance_id: str = None,
        instance_type: str = None,
        last_fetch_time: int = None,
        progress_data: ListDisasterRecoveryCheckpointsResponseBodyDataListTargetProgressProgressData = None,
        region_id: str = None,
        topic_name: str = None,
    ):
        # Consumer group ID
        self.consumer_group_id = consumer_group_id
        # Instance ID
        self.instance_id = instance_id
        # Instance type
        #   - ALIYUN_ROCKETMQ: Alibaba Cloud instance
        #   - EXTERNAL_ROCKETMQ: External instance, open-source instance, open-source cluster
        self.instance_type = instance_type
        # Latest fetch time
        self.last_fetch_time = last_fetch_time
        # Consumption progress data
        self.progress_data = progress_data
        # Region ID
        self.region_id = region_id
        # Topic name
        self.topic_name = topic_name

    def validate(self):
        if self.progress_data:
            self.progress_data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consumer_group_id is not None:
            result['consumerGroupId'] = self.consumer_group_id
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        if self.last_fetch_time is not None:
            result['lastFetchTime'] = self.last_fetch_time
        if self.progress_data is not None:
            result['progressData'] = self.progress_data.to_map()
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.topic_name is not None:
            result['topicName'] = self.topic_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('consumerGroupId') is not None:
            self.consumer_group_id = m.get('consumerGroupId')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        if m.get('lastFetchTime') is not None:
            self.last_fetch_time = m.get('lastFetchTime')
        if m.get('progressData') is not None:
            temp_model = ListDisasterRecoveryCheckpointsResponseBodyDataListTargetProgressProgressData()
            self.progress_data = temp_model.from_map(m['progressData'])
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('topicName') is not None:
            self.topic_name = m.get('topicName')
        return self


class ListDisasterRecoveryCheckpointsResponseBodyDataList(TeaModel):
    def __init__(
        self,
        checkpoint_id: int = None,
        item_id: int = None,
        last_sync_time: int = None,
        plan_id: int = None,
        source_progress: ListDisasterRecoveryCheckpointsResponseBodyDataListSourceProgress = None,
        target_progress: ListDisasterRecoveryCheckpointsResponseBodyDataListTargetProgress = None,
    ):
        # Consumption Progress ID
        self.checkpoint_id = checkpoint_id
        # Backup Mapping ID
        self.item_id = item_id
        # Last synchronization time
        self.last_sync_time = last_sync_time
        # Backup Plan ID
        self.plan_id = plan_id
        # Source consumption progress
        self.source_progress = source_progress
        # Target consumption progress
        self.target_progress = target_progress

    def validate(self):
        if self.source_progress:
            self.source_progress.validate()
        if self.target_progress:
            self.target_progress.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.checkpoint_id is not None:
            result['checkpointId'] = self.checkpoint_id
        if self.item_id is not None:
            result['itemId'] = self.item_id
        if self.last_sync_time is not None:
            result['lastSyncTime'] = self.last_sync_time
        if self.plan_id is not None:
            result['planId'] = self.plan_id
        if self.source_progress is not None:
            result['sourceProgress'] = self.source_progress.to_map()
        if self.target_progress is not None:
            result['targetProgress'] = self.target_progress.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('checkpointId') is not None:
            self.checkpoint_id = m.get('checkpointId')
        if m.get('itemId') is not None:
            self.item_id = m.get('itemId')
        if m.get('lastSyncTime') is not None:
            self.last_sync_time = m.get('lastSyncTime')
        if m.get('planId') is not None:
            self.plan_id = m.get('planId')
        if m.get('sourceProgress') is not None:
            temp_model = ListDisasterRecoveryCheckpointsResponseBodyDataListSourceProgress()
            self.source_progress = temp_model.from_map(m['sourceProgress'])
        if m.get('targetProgress') is not None:
            temp_model = ListDisasterRecoveryCheckpointsResponseBodyDataListTargetProgress()
            self.target_progress = temp_model.from_map(m['targetProgress'])
        return self


class ListDisasterRecoveryCheckpointsResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[ListDisasterRecoveryCheckpointsResponseBodyDataList] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # Paged data
        self.list = list
        # Current page number
        self.page_number = page_number
        # Page size
        self.page_size = page_size
        # Total number of records
        self.total_count = total_count

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = ListDisasterRecoveryCheckpointsResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListDisasterRecoveryCheckpointsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListDisasterRecoveryCheckpointsResponseBodyData = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Error code
        self.code = code
        # Response Data
        self.data = data
        # Dynamic error code
        self.dynamic_code = dynamic_code
        # The dynamic error message.
        self.dynamic_message = dynamic_message
        # HTTP status code
        self.http_status_code = http_status_code
        # Error message
        self.message = message
        # Request ID
        self.request_id = request_id
        # Whether the operation was successful
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
            temp_model = ListDisasterRecoveryCheckpointsResponseBodyData()
            self.data = temp_model.from_map(m['data'])
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


class ListDisasterRecoveryCheckpointsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDisasterRecoveryCheckpointsResponseBody = None,
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
            temp_model = ListDisasterRecoveryCheckpointsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDisasterRecoveryItemsRequest(TeaModel):
    def __init__(
        self,
        filter: str = None,
        page_number: int = None,
        page_size: int = None,
        topic_name: str = None,
    ):
        # Filter condition, filter by topicName
        self.filter = filter
        # Page number, indicating which page of the results to query.
        self.page_number = page_number
        # Page size, the maximum number of results displayed per page.
        self.page_size = page_size
        self.topic_name = topic_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter is not None:
            result['filter'] = self.filter
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.topic_name is not None:
            result['topicName'] = self.topic_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filter') is not None:
            self.filter = m.get('filter')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('topicName') is not None:
            self.topic_name = m.get('topicName')
        return self


class ListDisasterRecoveryItemsResponseBodyDataListTopics(TeaModel):
    def __init__(
        self,
        consumer_group_id: str = None,
        delivery_order_type: str = None,
        instance_id: str = None,
        instance_type: str = None,
        region_id: str = None,
        topic_name: str = None,
    ):
        # Consumer group ID
        self.consumer_group_id = consumer_group_id
        # The order in which messages are delivered to the target instance.
        # 
        # Parameter values are as follows:
        # - Concurrently: concurrent delivery
        # - Orderly: sequential delivery
        self.delivery_order_type = delivery_order_type
        # Instance ID
        self.instance_id = instance_id
        # Instance type
        self.instance_type = instance_type
        # Region ID
        self.region_id = region_id
        # The topic name.
        self.topic_name = topic_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consumer_group_id is not None:
            result['consumerGroupId'] = self.consumer_group_id
        if self.delivery_order_type is not None:
            result['deliveryOrderType'] = self.delivery_order_type
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.topic_name is not None:
            result['topicName'] = self.topic_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('consumerGroupId') is not None:
            self.consumer_group_id = m.get('consumerGroupId')
        if m.get('deliveryOrderType') is not None:
            self.delivery_order_type = m.get('deliveryOrderType')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('topicName') is not None:
            self.topic_name = m.get('topicName')
        return self


class ListDisasterRecoveryItemsResponseBodyDataList(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        ext_info: Dict[str, str] = None,
        item_id: int = None,
        item_status: str = None,
        plan_id: int = None,
        topics: List[ListDisasterRecoveryItemsResponseBodyDataListTopics] = None,
        update_time: str = None,
    ):
        # Creation time
        self.create_time = create_time
        # Extended information
        self.ext_info = ext_info
        # Backup plan ID
        self.item_id = item_id
        # Backup mapping status:
        #   - CREATING (Creating)
        #   - CHANGING (Changing)
        #   - RUNNING (Running)
        #   - MANUAL_STOPPED (Manually Stopped)
        #   - OVERDUE_STOPPED (Stopped Due to Overdue)
        self.item_status = item_status
        # Mapping ID
        self.plan_id = plan_id
        # Topics included in the backup mapping
        self.topics = topics
        # Update time
        self.update_time = update_time

    def validate(self):
        if self.topics:
            for k in self.topics:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.ext_info is not None:
            result['extInfo'] = self.ext_info
        if self.item_id is not None:
            result['itemId'] = self.item_id
        if self.item_status is not None:
            result['itemStatus'] = self.item_status
        if self.plan_id is not None:
            result['planId'] = self.plan_id
        result['topics'] = []
        if self.topics is not None:
            for k in self.topics:
                result['topics'].append(k.to_map() if k else None)
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('extInfo') is not None:
            self.ext_info = m.get('extInfo')
        if m.get('itemId') is not None:
            self.item_id = m.get('itemId')
        if m.get('itemStatus') is not None:
            self.item_status = m.get('itemStatus')
        if m.get('planId') is not None:
            self.plan_id = m.get('planId')
        self.topics = []
        if m.get('topics') is not None:
            for k in m.get('topics'):
                temp_model = ListDisasterRecoveryItemsResponseBodyDataListTopics()
                self.topics.append(temp_model.from_map(k))
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        return self


class ListDisasterRecoveryItemsResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[ListDisasterRecoveryItemsResponseBodyDataList] = None,
        page_number: int = None,
        page_size: int = None,
        scroll_id: str = None,
        total_count: int = None,
    ):
        # Paged data
        self.list = list
        # Current page number
        self.page_number = page_number
        # Page size
        self.page_size = page_size
        # Request scroll ID.
        # Automatically generated by the system, subsequent pagination requests need to include this return value to continue pagination.
        self.scroll_id = scroll_id
        # Total number of records
        self.total_count = total_count

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.scroll_id is not None:
            result['scrollId'] = self.scroll_id
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = ListDisasterRecoveryItemsResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('scrollId') is not None:
            self.scroll_id = m.get('scrollId')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListDisasterRecoveryItemsResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: ListDisasterRecoveryItemsResponseBodyData = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Access denied details, provided only when access is denied due to lack of RAM permissions
        self.access_denied_detail = access_denied_detail
        # Error code
        self.code = code
        # Return result
        self.data = data
        # Dynamic error code
        self.dynamic_code = dynamic_code
        # Dynamic error message
        self.dynamic_message = dynamic_message
        # HTTP status code
        self.http_status_code = http_status_code
        # Error message
        self.message = message
        # Request ID
        self.request_id = request_id
        # Whether the request was successful
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['accessDeniedDetail'] = self.access_denied_detail
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
        if m.get('accessDeniedDetail') is not None:
            self.access_denied_detail = m.get('accessDeniedDetail')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = ListDisasterRecoveryItemsResponseBodyData()
            self.data = temp_model.from_map(m['data'])
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


class ListDisasterRecoveryItemsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDisasterRecoveryItemsResponseBody = None,
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
            temp_model = ListDisasterRecoveryItemsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDisasterRecoveryPlansRequest(TeaModel):
    def __init__(
        self,
        filter: str = None,
        instance_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # Filter conditions, filter by backup name and description
        self.filter = filter
        self.instance_id = instance_id
        # Page number, the page of results to be queried.
        self.page_number = page_number
        # Page size, the maximum number of results displayed per page.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter is not None:
            result['filter'] = self.filter
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filter') is not None:
            self.filter = m.get('filter')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListDisasterRecoveryPlansResponseBodyDataListInstancesMessageProperty(TeaModel):
    def __init__(
        self,
        property_key: str = None,
        property_value: str = None,
    ):
        # Property key
        self.property_key = property_key
        # Property value
        self.property_value = property_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.property_key is not None:
            result['propertyKey'] = self.property_key
        if self.property_value is not None:
            result['propertyValue'] = self.property_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('propertyKey') is not None:
            self.property_key = m.get('propertyKey')
        if m.get('propertyValue') is not None:
            self.property_value = m.get('propertyValue')
        return self


class ListDisasterRecoveryPlansResponseBodyDataListInstances(TeaModel):
    def __init__(
        self,
        auth_type: str = None,
        consumer_group_id: str = None,
        endpoint_url: str = None,
        instance_id: str = None,
        instance_role: str = None,
        instance_type: str = None,
        message_property: ListDisasterRecoveryPlansResponseBodyDataListInstancesMessageProperty = None,
        network_type: str = None,
        password: str = None,
        region_id: str = None,
        security_group_id: str = None,
        username: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        # Authentication method
        self.auth_type = auth_type
        self.consumer_group_id = consumer_group_id
        # Endpoint URL
        self.endpoint_url = endpoint_url
        # Instance ID
        self.instance_id = instance_id
        # Instance role
        self.instance_role = instance_role
        # Instance type
        #   - ALIYUN_ROCKETMQ: Alibaba Cloud instance
        #   - EXTERNAL_ROCKETMQ: External instance, open-source instance, open-source cluster
        self.instance_type = instance_type
        # Message property
        self.message_property = message_property
        # Network type
        self.network_type = network_type
        # Authentication password
        self.password = password
        # The region where the instance is located
        self.region_id = region_id
        # Security group ID
        self.security_group_id = security_group_id
        # Authentication username
        self.username = username
        # VSwitch ID
        self.v_switch_id = v_switch_id
        # VPC ID
        self.vpc_id = vpc_id

    def validate(self):
        if self.message_property:
            self.message_property.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_type is not None:
            result['authType'] = self.auth_type
        if self.consumer_group_id is not None:
            result['consumerGroupId'] = self.consumer_group_id
        if self.endpoint_url is not None:
            result['endpointUrl'] = self.endpoint_url
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.instance_role is not None:
            result['instanceRole'] = self.instance_role
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        if self.message_property is not None:
            result['messageProperty'] = self.message_property.to_map()
        if self.network_type is not None:
            result['networkType'] = self.network_type
        if self.password is not None:
            result['password'] = self.password
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.security_group_id is not None:
            result['securityGroupId'] = self.security_group_id
        if self.username is not None:
            result['username'] = self.username
        if self.v_switch_id is not None:
            result['vSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authType') is not None:
            self.auth_type = m.get('authType')
        if m.get('consumerGroupId') is not None:
            self.consumer_group_id = m.get('consumerGroupId')
        if m.get('endpointUrl') is not None:
            self.endpoint_url = m.get('endpointUrl')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('instanceRole') is not None:
            self.instance_role = m.get('instanceRole')
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        if m.get('messageProperty') is not None:
            temp_model = ListDisasterRecoveryPlansResponseBodyDataListInstancesMessageProperty()
            self.message_property = temp_model.from_map(m['messageProperty'])
        if m.get('networkType') is not None:
            self.network_type = m.get('networkType')
        if m.get('password') is not None:
            self.password = m.get('password')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('securityGroupId') is not None:
            self.security_group_id = m.get('securityGroupId')
        if m.get('username') is not None:
            self.username = m.get('username')
        if m.get('vSwitchId') is not None:
            self.v_switch_id = m.get('vSwitchId')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        return self


class ListDisasterRecoveryPlansResponseBodyDataList(TeaModel):
    def __init__(
        self,
        auto_sync_checkpoint: bool = None,
        create_time: str = None,
        ext_info: Dict[str, str] = None,
        instances: List[ListDisasterRecoveryPlansResponseBodyDataListInstances] = None,
        plan_desc: str = None,
        plan_id: int = None,
        plan_name: str = None,
        plan_status: str = None,
        plan_type: str = None,
        sync_checkpoint_enabled: bool = None,
        update_time: str = None,
    ):
        # Whether to enable automatic synchronization of consumption progress.
        self.auto_sync_checkpoint = auto_sync_checkpoint
        # Creation time
        self.create_time = create_time
        # Extended information
        self.ext_info = ext_info
        # Instances involved in the backup plan
        self.instances = instances
        # Plan description
        self.plan_desc = plan_desc
        # Plan ID
        self.plan_id = plan_id
        # Plan name
        self.plan_name = plan_name
        # Plan status:
        #   - CREATED (Created)
        #   - RUNNING (Running)
        #   - DELETED (Deleted)
        self.plan_status = plan_status
        # Plan type:
        #   - ACTIVE_PASSIVE (One-way backup)
        #   - ACTIVE_ACTIVE (Two-way backup)
        self.plan_type = plan_type
        # Sync checkpoint switch
        self.sync_checkpoint_enabled = sync_checkpoint_enabled
        # Update time
        self.update_time = update_time

    def validate(self):
        if self.instances:
            for k in self.instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_sync_checkpoint is not None:
            result['autoSyncCheckpoint'] = self.auto_sync_checkpoint
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.ext_info is not None:
            result['extInfo'] = self.ext_info
        result['instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['instances'].append(k.to_map() if k else None)
        if self.plan_desc is not None:
            result['planDesc'] = self.plan_desc
        if self.plan_id is not None:
            result['planId'] = self.plan_id
        if self.plan_name is not None:
            result['planName'] = self.plan_name
        if self.plan_status is not None:
            result['planStatus'] = self.plan_status
        if self.plan_type is not None:
            result['planType'] = self.plan_type
        if self.sync_checkpoint_enabled is not None:
            result['syncCheckpointEnabled'] = self.sync_checkpoint_enabled
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoSyncCheckpoint') is not None:
            self.auto_sync_checkpoint = m.get('autoSyncCheckpoint')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('extInfo') is not None:
            self.ext_info = m.get('extInfo')
        self.instances = []
        if m.get('instances') is not None:
            for k in m.get('instances'):
                temp_model = ListDisasterRecoveryPlansResponseBodyDataListInstances()
                self.instances.append(temp_model.from_map(k))
        if m.get('planDesc') is not None:
            self.plan_desc = m.get('planDesc')
        if m.get('planId') is not None:
            self.plan_id = m.get('planId')
        if m.get('planName') is not None:
            self.plan_name = m.get('planName')
        if m.get('planStatus') is not None:
            self.plan_status = m.get('planStatus')
        if m.get('planType') is not None:
            self.plan_type = m.get('planType')
        if m.get('syncCheckpointEnabled') is not None:
            self.sync_checkpoint_enabled = m.get('syncCheckpointEnabled')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        return self


class ListDisasterRecoveryPlansResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[ListDisasterRecoveryPlansResponseBodyDataList] = None,
        page_number: int = None,
        page_size: int = None,
        scroll_id: str = None,
        total_count: int = None,
    ):
        # Paged data
        self.list = list
        # Current page number
        self.page_number = page_number
        # Page size
        self.page_size = page_size
        # Scroll request ID.
        # Automatically generated by the system, subsequent paging requests need to include this result to continue paging.
        self.scroll_id = scroll_id
        # Total number of records
        self.total_count = total_count

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.scroll_id is not None:
            result['scrollId'] = self.scroll_id
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = ListDisasterRecoveryPlansResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('scrollId') is not None:
            self.scroll_id = m.get('scrollId')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListDisasterRecoveryPlansResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: ListDisasterRecoveryPlansResponseBodyData = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details about the access denial. This parameter is returned only if the access is denied due to the reason that the Resource Access Management (RAM) user does not have the required permissions.
        self.access_denied_detail = access_denied_detail
        # Error code
        self.code = code
        # Return result
        self.data = data
        # Dynamic error code
        self.dynamic_code = dynamic_code
        # Dynamic error message
        self.dynamic_message = dynamic_message
        # HTTP status code
        self.http_status_code = http_status_code
        # Error message
        self.message = message
        # Request ID
        self.request_id = request_id
        # Whether the operation was successful
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['accessDeniedDetail'] = self.access_denied_detail
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
        if m.get('accessDeniedDetail') is not None:
            self.access_denied_detail = m.get('accessDeniedDetail')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = ListDisasterRecoveryPlansResponseBodyData()
            self.data = temp_model.from_map(m['data'])
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


class ListDisasterRecoveryPlansResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDisasterRecoveryPlansResponseBody = None,
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
            temp_model = ListDisasterRecoveryPlansResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstanceAccountRequest(TeaModel):
    def __init__(
        self,
        account_status: str = None,
        account_type: str = None,
        page_number: int = None,
        page_size: int = None,
        username: str = None,
    ):
        # The status of the account.
        # 
        # Valid values:
        # 
        # *   DISABLE
        # *   ENABLE
        self.account_status = account_status
        # The account type.
        #   - CUSTOMER
        #   - DEFAULT
        self.account_type = account_type
        # The page number. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 10.
        self.page_size = page_size
        # The username of the account.
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_status is not None:
            result['accountStatus'] = self.account_status
        if self.account_type is not None:
            result['accountType'] = self.account_type
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.username is not None:
            result['username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountStatus') is not None:
            self.account_status = m.get('accountStatus')
        if m.get('accountType') is not None:
            self.account_type = m.get('accountType')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('username') is not None:
            self.username = m.get('username')
        return self


class ListInstanceAccountResponseBodyDataList(TeaModel):
    def __init__(
        self,
        account_status: str = None,
        account_type: str = None,
        instance_id: str = None,
        region_id: str = None,
        username: str = None,
    ):
        # The status of the account.
        # Valid values:
        #   - DISABLE
        #   - ENABLE
        self.account_status = account_status
        # The account type.
        #   - CUSTOMER
        #   - DEFAULT
        self.account_type = account_type
        # The instance ID.
        self.instance_id = instance_id
        # The region ID.
        self.region_id = region_id
        # The username of the account.
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_status is not None:
            result['accountStatus'] = self.account_status
        if self.account_type is not None:
            result['accountType'] = self.account_type
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.username is not None:
            result['username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountStatus') is not None:
            self.account_status = m.get('accountStatus')
        if m.get('accountType') is not None:
            self.account_type = m.get('accountType')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('username') is not None:
            self.username = m.get('username')
        return self


class ListInstanceAccountResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[ListInstanceAccountResponseBodyDataList] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The pagination information.
        self.list = list
        # The page number.
        self.page_number = page_number
        # Number of items per page.
        self.page_size = page_size
        # The total number of returned entries.
        self.total_count = total_count

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = ListInstanceAccountResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListInstanceAccountResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: ListInstanceAccountResponseBodyData = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details about the access denial. This parameter is returned only if the access is denied because the Resource Access Management (RAM) user does not have the required permissions.
        self.access_denied_detail = access_denied_detail
        # The error code.
        self.code = code
        # The data returned.
        self.data = data
        # The dynamic error code.
        self.dynamic_code = dynamic_code
        # The dynamic error message.
        self.dynamic_message = dynamic_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The error message.
        self.message = message
        # The ID of the request. Each request has a unique ID. You can use this ID to troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the call was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['accessDeniedDetail'] = self.access_denied_detail
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
        if m.get('accessDeniedDetail') is not None:
            self.access_denied_detail = m.get('accessDeniedDetail')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = ListInstanceAccountResponseBodyData()
            self.data = temp_model.from_map(m['data'])
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


class ListInstanceAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListInstanceAccountResponseBody = None,
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
            temp_model = ListInstanceAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstanceAclRequest(TeaModel):
    def __init__(
        self,
        filter: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The condition that you specify to filter the ACLs. If you do not specify this parameter, all ACLs are queried.
        self.filter = filter
        # The page number. Pages start from page 1.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter is not None:
            result['filter'] = self.filter
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filter') is not None:
            self.filter = m.get('filter')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListInstanceAclResponseBodyDataList(TeaModel):
    def __init__(
        self,
        acl_type: str = None,
        actions: List[str] = None,
        decision: str = None,
        instance_id: str = None,
        ip_whitelists: List[str] = None,
        region_id: str = None,
        resource_name: str = None,
        resource_type: str = None,
        username: str = None,
    ):
        # The ACL type.
        # 
        # Valid value:
        # 
        # *   APACHE: open source ACL.
        self.acl_type = acl_type
        # The types of the operations that are allowed by the ACL.
        self.actions = actions
        # The decision result.
        # 
        # Valid values:
        # 
        # *   Deny: Access is denied.
        # *   Allow: Access is allowed.
        self.decision = decision
        # The instance ID.
        self.instance_id = instance_id
        # The IP address whitelists.
        self.ip_whitelists = ip_whitelists
        # The region ID.
        self.region_id = region_id
        # The resource name.
        self.resource_name = resource_name
        # The resource type.
        # 
        # Valid values:
        # 
        # *   Group
        # *   Topic
        self.resource_type = resource_type
        # The username.
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_type is not None:
            result['aclType'] = self.acl_type
        if self.actions is not None:
            result['actions'] = self.actions
        if self.decision is not None:
            result['decision'] = self.decision
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.ip_whitelists is not None:
            result['ipWhitelists'] = self.ip_whitelists
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.resource_name is not None:
            result['resourceName'] = self.resource_name
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        if self.username is not None:
            result['username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aclType') is not None:
            self.acl_type = m.get('aclType')
        if m.get('actions') is not None:
            self.actions = m.get('actions')
        if m.get('decision') is not None:
            self.decision = m.get('decision')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('ipWhitelists') is not None:
            self.ip_whitelists = m.get('ipWhitelists')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('resourceName') is not None:
            self.resource_name = m.get('resourceName')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        if m.get('username') is not None:
            self.username = m.get('username')
        return self


class ListInstanceAclResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[ListInstanceAclResponseBodyDataList] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The pagination information.
        self.list = list
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = ListInstanceAclResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListInstanceAclResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: ListInstanceAclResponseBodyData = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details about the access denial. This parameter is returned only if the access is denied due to the reason that the Resource Access Management (RAM) user does not have the required permissions.
        self.access_denied_detail = access_denied_detail
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
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['accessDeniedDetail'] = self.access_denied_detail
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
        if m.get('accessDeniedDetail') is not None:
            self.access_denied_detail = m.get('accessDeniedDetail')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = ListInstanceAclResponseBodyData()
            self.data = temp_model.from_map(m['data'])
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


class ListInstanceAclResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListInstanceAclResponseBody = None,
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
            temp_model = ListInstanceAclResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstanceIpWhitelistRequest(TeaModel):
    def __init__(
        self,
        ip_whitelist: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # IP whitelist.
        self.ip_whitelist = ip_whitelist
        # The page number. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_whitelist is not None:
            result['ipWhitelist'] = self.ip_whitelist
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ipWhitelist') is not None:
            self.ip_whitelist = m.get('ipWhitelist')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListInstanceIpWhitelistResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[str] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The pagination information.
        self.list = list
        # The page number.
        self.page_number = page_number
        # Number of items per page.
        self.page_size = page_size
        # The total number of returned entries.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.list is not None:
            result['list'] = self.list
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('list') is not None:
            self.list = m.get('list')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListInstanceIpWhitelistResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: ListInstanceIpWhitelistResponseBodyData = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details about the access denial. This parameter is returned only if the access is denied because the Resource Access Management (RAM) user does not have the required permissions.
        self.access_denied_detail = access_denied_detail
        # The error code.
        self.code = code
        # The data returned.
        self.data = data
        # The dynamic error code.
        self.dynamic_code = dynamic_code
        # The dynamic error message.
        self.dynamic_message = dynamic_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The error message.
        self.message = message
        # The ID of the request. Each request has a unique ID. You can use this ID to troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the call was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['accessDeniedDetail'] = self.access_denied_detail
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
        if m.get('accessDeniedDetail') is not None:
            self.access_denied_detail = m.get('accessDeniedDetail')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = ListInstanceIpWhitelistResponseBodyData()
            self.data = temp_model.from_map(m['data'])
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


class ListInstanceIpWhitelistResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListInstanceIpWhitelistResponseBody = None,
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
            temp_model = ListInstanceIpWhitelistResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstancesRequest(TeaModel):
    def __init__(
        self,
        filter: str = None,
        page_number: int = None,
        page_size: int = None,
        resource_group_id: str = None,
        series_codes: List[str] = None,
        storage_secret_key: str = None,
        tags: str = None,
    ):
        # The filter condition that is used to query instances. If you do not configure this parameter, all instances are queried.
        self.filter = filter
        # The page number.
        # 
        # Valid values: 1 to 100000000.
        # 
        # If you set this parameter to a value smaller than 1, the system uses 1 as the value. If you set this parameter to a value greater than 100000000, the system uses 100000000 as the value.
        self.page_number = page_number
        # The number of entries per page.
        # 
        # Value values: 10 to 200.
        # 
        # If you set this parameter to a value smaller than 10, the system uses 10 as the value. If you set this parameter to a value greater than 200, the system uses 200 as the value.
        self.page_size = page_size
        # The ID of the resource group to which the instance belongs.
        self.resource_group_id = resource_group_id
        # The primary edition of the instance.
        # 
        # Valid values:
        # 
        # *   standard: Standard Edition
        # *   ultimate: Enterprise Platinum Edition
        # *   professional: Professional Edition
        self.series_codes = series_codes
        # The storage encryption key.
        self.storage_secret_key = storage_secret_key
        # The tags that are used to filter instances.
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter is not None:
            result['filter'] = self.filter
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        if self.series_codes is not None:
            result['seriesCodes'] = self.series_codes
        if self.storage_secret_key is not None:
            result['storageSecretKey'] = self.storage_secret_key
        if self.tags is not None:
            result['tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filter') is not None:
            self.filter = m.get('filter')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('seriesCodes') is not None:
            self.series_codes = m.get('seriesCodes')
        if m.get('storageSecretKey') is not None:
            self.storage_secret_key = m.get('storageSecretKey')
        if m.get('tags') is not None:
            self.tags = m.get('tags')
        return self


class ListInstancesShrinkRequest(TeaModel):
    def __init__(
        self,
        filter: str = None,
        page_number: int = None,
        page_size: int = None,
        resource_group_id: str = None,
        series_codes_shrink: str = None,
        storage_secret_key: str = None,
        tags: str = None,
    ):
        # The filter condition that is used to query instances. If you do not configure this parameter, all instances are queried.
        self.filter = filter
        # The page number.
        # 
        # Valid values: 1 to 100000000.
        # 
        # If you set this parameter to a value smaller than 1, the system uses 1 as the value. If you set this parameter to a value greater than 100000000, the system uses 100000000 as the value.
        self.page_number = page_number
        # The number of entries per page.
        # 
        # Value values: 10 to 200.
        # 
        # If you set this parameter to a value smaller than 10, the system uses 10 as the value. If you set this parameter to a value greater than 200, the system uses 200 as the value.
        self.page_size = page_size
        # The ID of the resource group to which the instance belongs.
        self.resource_group_id = resource_group_id
        # The primary edition of the instance.
        # 
        # Valid values:
        # 
        # *   standard: Standard Edition
        # *   ultimate: Enterprise Platinum Edition
        # *   professional: Professional Edition
        self.series_codes_shrink = series_codes_shrink
        # The storage encryption key.
        self.storage_secret_key = storage_secret_key
        # The tags that are used to filter instances.
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter is not None:
            result['filter'] = self.filter
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        if self.series_codes_shrink is not None:
            result['seriesCodes'] = self.series_codes_shrink
        if self.storage_secret_key is not None:
            result['storageSecretKey'] = self.storage_secret_key
        if self.tags is not None:
            result['tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filter') is not None:
            self.filter = m.get('filter')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('seriesCodes') is not None:
            self.series_codes_shrink = m.get('seriesCodes')
        if m.get('storageSecretKey') is not None:
            self.storage_secret_key = m.get('storageSecretKey')
        if m.get('tags') is not None:
            self.tags = m.get('tags')
        return self


class ListInstancesResponseBodyDataListProductInfo(TeaModel):
    def __init__(
        self,
        trace_on: bool = None,
    ):
        # Indicates whether the message trace feature is enabled. Valid values:
        # 
        # *   true
        # *   false
        # 
        # This parameter is not in use. By default, the message trace feature is enabled for ApsaraMQ for RocketMQ instances, regardless of whether this parameter is configured.
        self.trace_on = trace_on

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.trace_on is not None:
            result['traceOn'] = self.trace_on
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('traceOn') is not None:
            self.trace_on = m.get('traceOn')
        return self


class ListInstancesResponseBodyDataListTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the resource.
        self.key = key
        # The tag value of the resource.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class ListInstancesResponseBodyDataList(TeaModel):
    def __init__(
        self,
        commodity_code: str = None,
        create_time: str = None,
        expire_time: str = None,
        group_count: int = None,
        instance_id: str = None,
        instance_name: str = None,
        payment_type: str = None,
        product_info: ListInstancesResponseBodyDataListProductInfo = None,
        region_id: str = None,
        release_time: str = None,
        remark: str = None,
        resource_group_id: str = None,
        series_code: str = None,
        service_code: str = None,
        start_time: str = None,
        status: str = None,
        sub_series_code: str = None,
        tags: List[ListInstancesResponseBodyDataListTags] = None,
        topic_count: int = None,
        update_time: str = None,
        user_id: str = None,
    ):
        # The commodity code of the instance. The commodity code of ApsaraMQ for RocketMQ 5.0 instances has a similar format to ons_rmqsub_public_cn.
        self.commodity_code = commodity_code
        # The time when the version of the instance was updated.
        self.create_time = create_time
        # The time when the instance expires.
        self.expire_time = expire_time
        # The number of consumer groups that are created on the instance.
        self.group_count = group_count
        # The instance ID.
        self.instance_id = instance_id
        # The instance name.
        self.instance_name = instance_name
        # The billing method of the instance.
        # 
        # Valid values:
        # 
        # *   PayAsYouGo
        # *   Subscription
        self.payment_type = payment_type
        # The product information.
        self.product_info = product_info
        # The ID of the region in which the instance resides.
        self.region_id = region_id
        # The time when the instance was released.
        self.release_time = release_time
        # The instance description.
        self.remark = remark
        # The ID of the resource group to which the instance belongs.
        self.resource_group_id = resource_group_id
        # The primary edition of the instance.
        # 
        # Valid values:
        # 
        # *   standard: Standard Edition
        # *   ultimate: Enterprise Platinum Edition
        # *   professional: Professional Edition
        self.series_code = series_code
        # The code of the service to which the instance belongs. The service code of ApsaraMQ for RocketMQ is rmq.
        self.service_code = service_code
        # The time when the instance was created.
        self.start_time = start_time
        # The status of the instance.
        # 
        # Valid values:
        # 
        # *   RELEASED
        # *   RUNNING
        # *   STOPPED
        # *   CHANGING
        # *   CREATING
        self.status = status
        # The sub-category edition of the instance.
        # 
        # Valid values:
        # 
        # *   cluster_ha: Cluster High-availability Edition
        # *   single_node: Standalone Edition
        self.sub_series_code = sub_series_code
        # The resource tags.
        self.tags = tags
        # The number of topics that are created on the instance.
        self.topic_count = topic_count
        # The time when the instance was last modified.
        self.update_time = update_time
        # The ID of the user who owns the instance.
        self.user_id = user_id

    def validate(self):
        if self.product_info:
            self.product_info.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commodity_code is not None:
            result['commodityCode'] = self.commodity_code
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.expire_time is not None:
            result['expireTime'] = self.expire_time
        if self.group_count is not None:
            result['groupCount'] = self.group_count
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.instance_name is not None:
            result['instanceName'] = self.instance_name
        if self.payment_type is not None:
            result['paymentType'] = self.payment_type
        if self.product_info is not None:
            result['productInfo'] = self.product_info.to_map()
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.release_time is not None:
            result['releaseTime'] = self.release_time
        if self.remark is not None:
            result['remark'] = self.remark
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        if self.series_code is not None:
            result['seriesCode'] = self.series_code
        if self.service_code is not None:
            result['serviceCode'] = self.service_code
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.status is not None:
            result['status'] = self.status
        if self.sub_series_code is not None:
            result['subSeriesCode'] = self.sub_series_code
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        if self.topic_count is not None:
            result['topicCount'] = self.topic_count
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commodityCode') is not None:
            self.commodity_code = m.get('commodityCode')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('expireTime') is not None:
            self.expire_time = m.get('expireTime')
        if m.get('groupCount') is not None:
            self.group_count = m.get('groupCount')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('instanceName') is not None:
            self.instance_name = m.get('instanceName')
        if m.get('paymentType') is not None:
            self.payment_type = m.get('paymentType')
        if m.get('productInfo') is not None:
            temp_model = ListInstancesResponseBodyDataListProductInfo()
            self.product_info = temp_model.from_map(m['productInfo'])
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('releaseTime') is not None:
            self.release_time = m.get('releaseTime')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('seriesCode') is not None:
            self.series_code = m.get('seriesCode')
        if m.get('serviceCode') is not None:
            self.service_code = m.get('serviceCode')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('subSeriesCode') is not None:
            self.sub_series_code = m.get('subSeriesCode')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = ListInstancesResponseBodyDataListTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('topicCount') is not None:
            self.topic_count = m.get('topicCount')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class ListInstancesResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[ListInstancesResponseBodyDataList] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The pagination information.
        self.list = list
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned on each page.
        self.page_size = page_size
        # The total number of returned entries.
        self.total_count = total_count

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = ListInstancesResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListInstancesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListInstancesResponseBodyData = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code returned if the call failed.
        self.code = code
        # The data returned.
        self.data = data
        # The dynamic error code.
        self.dynamic_code = dynamic_code
        # The dynamic error message.
        self.dynamic_message = dynamic_message
        # The HTTP status code returned.
        self.http_status_code = http_status_code
        # The error message.
        self.message = message
        # The ID of the request. Each request has a unique ID. You can use this ID to troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the call was successful.
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
            temp_model = ListInstancesResponseBodyData()
            self.data = temp_model.from_map(m['data'])
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


class ListInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListInstancesResponseBody = None,
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
            temp_model = ListInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMessagesRequest(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        message_id: str = None,
        message_key: str = None,
        page_number: int = None,
        page_size: int = None,
        scroll_id: str = None,
        start_time: str = None,
    ):
        # The end of the time range to query.
        self.end_time = end_time
        # Message Id.
        self.message_id = message_id
        # Message key.
        self.message_key = message_key
        # The page number. Pages start from page 1.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The scroll ID of the request.
        # 
        # You do not need to configure this parameter for the first page. This parameter is included in the pagination request based on the result returned for the first page.
        self.scroll_id = scroll_id
        # The beginning of the time range to query.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.message_id is not None:
            result['messageId'] = self.message_id
        if self.message_key is not None:
            result['messageKey'] = self.message_key
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.scroll_id is not None:
            result['scrollId'] = self.scroll_id
        if self.start_time is not None:
            result['startTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('messageId') is not None:
            self.message_id = m.get('messageId')
        if m.get('messageKey') is not None:
            self.message_key = m.get('messageKey')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('scrollId') is not None:
            self.scroll_id = m.get('scrollId')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        return self


class ListMessagesResponseBodyDataList(TeaModel):
    def __init__(
        self,
        body: str = None,
        body_size: int = None,
        born_host: str = None,
        born_time: str = None,
        instance_id: str = None,
        message_group: str = None,
        message_id: str = None,
        message_keys: List[str] = None,
        message_tag: str = None,
        message_type: str = None,
        region_id: str = None,
        store_host: str = None,
        store_time: str = None,
        topic_name: str = None,
        user_properties: Dict[str, str] = None,
    ):
        # Message body.
        self.body = body
        # Message body size.
        self.body_size = body_size
        # The client on which messages are produced.
        self.born_host = born_host
        # Message born time.
        self.born_time = born_time
        # The instance ID.
        self.instance_id = instance_id
        # The message group. This parameter is returned only for ordered messages.
        self.message_group = message_group
        # Message Id.
        self.message_id = message_id
        # Message keys.
        self.message_keys = message_keys
        # The message tag.
        self.message_tag = message_tag
        # Message type.
        self.message_type = message_type
        # The region ID.
        self.region_id = region_id
        # The broker on which messages are stored.
        self.store_host = store_host
        # Message store time.
        self.store_time = store_time
        # The name of the topic.
        self.topic_name = topic_name
        # Message user properties.
        self.user_properties = user_properties

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        if self.body_size is not None:
            result['bodySize'] = self.body_size
        if self.born_host is not None:
            result['bornHost'] = self.born_host
        if self.born_time is not None:
            result['bornTime'] = self.born_time
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
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
        if self.user_properties is not None:
            result['userProperties'] = self.user_properties
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        if m.get('bodySize') is not None:
            self.body_size = m.get('bodySize')
        if m.get('bornHost') is not None:
            self.born_host = m.get('bornHost')
        if m.get('bornTime') is not None:
            self.born_time = m.get('bornTime')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
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
        if m.get('userProperties') is not None:
            self.user_properties = m.get('userProperties')
        return self


class ListMessagesResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[ListMessagesResponseBodyDataList] = None,
        page_number: int = None,
        page_size: int = None,
        scroll_id: str = None,
        total_count: int = None,
    ):
        # The pagination information.
        self.list = list
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The scroll ID of the request.
        # 
        # The ID is automatically generated by the system. The result can be paginated only if this parameter is included in the pagination request.
        self.scroll_id = scroll_id
        # The total number of returned entries.
        self.total_count = total_count

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.scroll_id is not None:
            result['scrollId'] = self.scroll_id
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = ListMessagesResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('scrollId') is not None:
            self.scroll_id = m.get('scrollId')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListMessagesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListMessagesResponseBodyData = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code.
        self.code = code
        # The data returned.
        self.data = data
        # The dynamic error code.
        self.dynamic_code = dynamic_code
        # The dynamic error message.
        self.dynamic_message = dynamic_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The error message.
        self.message = message
        # The ID of the request. Each request has a unique ID. You can use this ID to troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the request was successful.
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
            temp_model = ListMessagesResponseBodyData()
            self.data = temp_model.from_map(m['data'])
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


class ListMessagesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListMessagesResponseBody = None,
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
            temp_model = ListMessagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMetricMetaRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
    ):
        # Page number, indicating which page of the results to return.
        # 
        # This parameter is required.
        self.page_number = page_number
        # Page size, indicating the maximum number of results per page.
        # 
        # This parameter is required.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListMetricMetaResponseBodyDataList(TeaModel):
    def __init__(
        self,
        category: str = None,
        description: str = None,
        metric_name: str = None,
    ):
        # Monitoring item tag
        self.category = category
        # Monitoring item description
        self.description = description
        # Monitoring item name
        self.metric_name = metric_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['category'] = self.category
        if self.description is not None:
            result['description'] = self.description
        if self.metric_name is not None:
            result['metricName'] = self.metric_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('metricName') is not None:
            self.metric_name = m.get('metricName')
        return self


class ListMetricMetaResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[ListMetricMetaResponseBodyDataList] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # Paged data
        self.list = list
        # Current page number
        self.page_number = page_number
        # Page size
        self.page_size = page_size
        # Total record count
        self.total_count = total_count

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = ListMetricMetaResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListMetricMetaResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListMetricMetaResponseBodyData = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Error code
        self.code = code
        # Return result
        self.data = data
        # Dynamic error code
        self.dynamic_code = dynamic_code
        # The dynamic error message.
        self.dynamic_message = dynamic_message
        # HTTP status code
        self.http_status_code = http_status_code
        # Error message
        self.message = message
        # Request ID
        self.request_id = request_id
        # Whether the operation was successful
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
            temp_model = ListMetricMetaResponseBodyData()
            self.data = temp_model.from_map(m['data'])
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


class ListMetricMetaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListMetricMetaResponseBody = None,
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
            temp_model = ListMetricMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRegionsResponseBodyDataTags(TeaModel):
    def __init__(
        self,
        tag_code: str = None,
        tag_value: Any = None,
    ):
        # The tag code.
        self.tag_code = tag_code
        # The tag value.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_code is not None:
            result['tagCode'] = self.tag_code
        if self.tag_value is not None:
            result['tagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tagCode') is not None:
            self.tag_code = m.get('tagCode')
        if m.get('tagValue') is not None:
            self.tag_value = m.get('tagValue')
        return self


class ListRegionsResponseBodyData(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        region_id: str = None,
        region_name: str = None,
        support_rocketmq_v4: bool = None,
        support_rocketmq_v5: bool = None,
        tags: List[ListRegionsResponseBodyDataTags] = None,
        update_time: str = None,
    ):
        # The time when the ApsaraMQ for RocketMQ instance was created.
        self.create_time = create_time
        # The region ID.
        self.region_id = region_id
        # The region name.
        self.region_name = region_name
        # Indicates whether ApsaraMQ for RocketMQ V4 is activated.
        self.support_rocketmq_v4 = support_rocketmq_v4
        # Indicates whether ApsaraMQ for RocketMQ V5 is activated.
        self.support_rocketmq_v5 = support_rocketmq_v5
        # The region tags.
        self.tags = tags
        # The time when the ApsaraMQ for RocketMQ instance was last modified.
        self.update_time = update_time

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.region_name is not None:
            result['regionName'] = self.region_name
        if self.support_rocketmq_v4 is not None:
            result['supportRocketmqV4'] = self.support_rocketmq_v4
        if self.support_rocketmq_v5 is not None:
            result['supportRocketmqV5'] = self.support_rocketmq_v5
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('regionName') is not None:
            self.region_name = m.get('regionName')
        if m.get('supportRocketmqV4') is not None:
            self.support_rocketmq_v4 = m.get('supportRocketmqV4')
        if m.get('supportRocketmqV5') is not None:
            self.support_rocketmq_v5 = m.get('supportRocketmqV5')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = ListRegionsResponseBodyDataTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        return self


class ListRegionsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ListRegionsResponseBodyData] = None,
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
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
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
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ListRegionsResponseBodyData()
                self.data.append(temp_model.from_map(k))
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


class ListRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListRegionsResponseBody = None,
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
            temp_model = ListRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequest(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_id: str = None,
        resource_type: str = None,
        tag: str = None,
    ):
        # The position from which the next query starts.
        self.next_token = next_token
        # Region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # Resource group ID.
        self.resource_group_id = resource_group_id
        # List of resource IDs, in JSON format.
        self.resource_id = resource_id
        # Resource type.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # List of tags, in JSON format.
        self.tag = tag

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        if self.resource_id is not None:
            result['resourceId'] = self.resource_id
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        if self.tag is not None:
            result['tag'] = self.tag
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        if m.get('tag') is not None:
            self.tag = m.get('tag')
        return self


class ListTagResourcesResponseBodyDataTagResources(TeaModel):
    def __init__(
        self,
        ali_uid: int = None,
        category: str = None,
        resource_id: str = None,
        resource_type: str = None,
        scope: str = None,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # UID of the resource owner.
        self.ali_uid = ali_uid
        # Tag category.
        self.category = category
        # Resource ID.
        self.resource_id = resource_id
        # Resource type.
        self.resource_type = resource_type
        # Visibility scope.
        self.scope = scope
        # Tag key.
        self.tag_key = tag_key
        # Tag value.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['aliUid'] = self.ali_uid
        if self.category is not None:
            result['category'] = self.category
        if self.resource_id is not None:
            result['resourceId'] = self.resource_id
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        if self.scope is not None:
            result['scope'] = self.scope
        if self.tag_key is not None:
            result['tagKey'] = self.tag_key
        if self.tag_value is not None:
            result['tagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aliUid') is not None:
            self.ali_uid = m.get('aliUid')
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        if m.get('scope') is not None:
            self.scope = m.get('scope')
        if m.get('tagKey') is not None:
            self.tag_key = m.get('tagKey')
        if m.get('tagValue') is not None:
            self.tag_value = m.get('tagValue')
        return self


class ListTagResourcesResponseBodyData(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        tag_resources: List[ListTagResourcesResponseBodyDataTagResources] = None,
    ):
        # The position from which the next query starts.
        self.next_token = next_token
        # Request ID.
        self.request_id = request_id
        # Resource tag relationships.
        self.tag_resources = tag_resources

    def validate(self):
        if self.tag_resources:
            for k in self.tag_resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['tagResources'] = []
        if self.tag_resources is not None:
            for k in self.tag_resources:
                result['tagResources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.tag_resources = []
        if m.get('tagResources') is not None:
            for k in m.get('tagResources'):
                temp_model = ListTagResourcesResponseBodyDataTagResources()
                self.tag_resources.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListTagResourcesResponseBodyData = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Error code
        self.code = code
        # Return result
        self.data = data
        # Dynamic error code
        self.dynamic_code = dynamic_code
        # Dynamic error message
        self.dynamic_message = dynamic_message
        # HTTP status code
        self.http_status_code = http_status_code
        # Error message
        self.message = message
        # Request ID
        self.request_id = request_id
        # Whether the operation was successful
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
            temp_model = ListTagResourcesResponseBodyData()
            self.data = temp_model.from_map(m['data'])
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


class ListTagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTagResourcesResponseBody = None,
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
            temp_model = ListTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTopicSubscriptionsResponseBodyData(TeaModel):
    def __init__(
        self,
        consistency: str = None,
        consumer_group_id: str = None,
        filter_expression: str = None,
        filter_expression_type: str = None,
        message_model: str = None,
        subscription_status: str = None,
        topic_name: str = None,
    ):
        # Indicates whether message consumption is consistent. Valid values:
        # 
        # *   false: Unconsumed messages exist in the consumer group.
        # *   true: No unconsumed message exists in the consumer group.
        self.consistency = consistency
        # The consumer group ID.
        self.consumer_group_id = consumer_group_id
        # The filter expression.
        self.filter_expression = filter_expression
        # The type of the filter expression. Valid values: SQL, TAG, and UNSPECIFIED. The value SQL indicates that messages are filtered by using SQL expressions. The value TAG indicates that messages are filtered by using tags. The value UNSPECIFIED indicates that no filter expression type is specified.
        self.filter_expression_type = filter_expression_type
        # The consumption mode. Valid values: BROADCASTING and CLUSTERING.
        self.message_model = message_model
        # The subscription status. Valid values: ONLINE and OFFLINE.
        self.subscription_status = subscription_status
        # The topic name.
        self.topic_name = topic_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consistency is not None:
            result['consistency'] = self.consistency
        if self.consumer_group_id is not None:
            result['consumerGroupId'] = self.consumer_group_id
        if self.filter_expression is not None:
            result['filterExpression'] = self.filter_expression
        if self.filter_expression_type is not None:
            result['filterExpressionType'] = self.filter_expression_type
        if self.message_model is not None:
            result['messageModel'] = self.message_model
        if self.subscription_status is not None:
            result['subscriptionStatus'] = self.subscription_status
        if self.topic_name is not None:
            result['topicName'] = self.topic_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('consistency') is not None:
            self.consistency = m.get('consistency')
        if m.get('consumerGroupId') is not None:
            self.consumer_group_id = m.get('consumerGroupId')
        if m.get('filterExpression') is not None:
            self.filter_expression = m.get('filterExpression')
        if m.get('filterExpressionType') is not None:
            self.filter_expression_type = m.get('filterExpressionType')
        if m.get('messageModel') is not None:
            self.message_model = m.get('messageModel')
        if m.get('subscriptionStatus') is not None:
            self.subscription_status = m.get('subscriptionStatus')
        if m.get('topicName') is not None:
            self.topic_name = m.get('topicName')
        return self


class ListTopicSubscriptionsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ListTopicSubscriptionsResponseBodyData] = None,
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
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
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
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ListTopicSubscriptionsResponseBodyData()
                self.data.append(temp_model.from_map(k))
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


class ListTopicSubscriptionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTopicSubscriptionsResponseBody = None,
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
            temp_model = ListTopicSubscriptionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTopicsRequest(TeaModel):
    def __init__(
        self,
        filter: str = None,
        message_types: List[str] = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The filter condition for the query. If not provided, all topics under the instance will be queried.
        self.filter = filter
        # The message type of the topic.
        self.message_types = message_types
        # Page number, indicating which page of results to return.
        self.page_number = page_number
        # Page size, the maximum number of results to display per page.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter is not None:
            result['filter'] = self.filter
        if self.message_types is not None:
            result['messageTypes'] = self.message_types
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filter') is not None:
            self.filter = m.get('filter')
        if m.get('messageTypes') is not None:
            self.message_types = m.get('messageTypes')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListTopicsShrinkRequest(TeaModel):
    def __init__(
        self,
        filter: str = None,
        message_types_shrink: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The filter condition for the query. If not provided, all topics under the instance will be queried.
        self.filter = filter
        # The message type of the topic.
        self.message_types_shrink = message_types_shrink
        # Page number, indicating which page of results to return.
        self.page_number = page_number
        # Page size, the maximum number of results to display per page.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter is not None:
            result['filter'] = self.filter
        if self.message_types_shrink is not None:
            result['messageTypes'] = self.message_types_shrink
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filter') is not None:
            self.filter = m.get('filter')
        if m.get('messageTypes') is not None:
            self.message_types_shrink = m.get('messageTypes')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListTopicsResponseBodyDataList(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        instance_id: str = None,
        max_send_tps: int = None,
        message_type: str = None,
        region_id: str = None,
        remark: str = None,
        status: str = None,
        topic_name: str = None,
        update_time: str = None,
    ):
        # Creation time.
        self.create_time = create_time
        # Instance ID.
        self.instance_id = instance_id
        # The maximum TPS for message sending.
        self.max_send_tps = max_send_tps
        # The type of messages in the topic.
        # 
        # Valid values:
        # 
        # *   TRANSACTION: transactional messages
        # *   FIFO: ordered messages
        # *   DELAY: scheduled or delayed messages
        # *   NORMAL: normal messages
        self.message_type = message_type
        # The region ID to which the instance belongs.
        self.region_id = region_id
        # Remark information of the topic.
        self.remark = remark
        # The topic status.
        # 
        # Valid values:
        # 
        # *   RUNNING
        # *   CREATING
        self.status = status
        # Topic name.
        self.topic_name = topic_name
        # Last update time of the topic.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.max_send_tps is not None:
            result['maxSendTps'] = self.max_send_tps
        if self.message_type is not None:
            result['messageType'] = self.message_type
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.remark is not None:
            result['remark'] = self.remark
        if self.status is not None:
            result['status'] = self.status
        if self.topic_name is not None:
            result['topicName'] = self.topic_name
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('maxSendTps') is not None:
            self.max_send_tps = m.get('maxSendTps')
        if m.get('messageType') is not None:
            self.message_type = m.get('messageType')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('topicName') is not None:
            self.topic_name = m.get('topicName')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        return self


class ListTopicsResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[ListTopicsResponseBodyDataList] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The topics.
        self.list = list
        # Current page number.
        self.page_number = page_number
        # Page size.
        self.page_size = page_size
        # Total number of results returned.
        self.total_count = total_count

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = ListTopicsResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListTopicsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListTopicsResponseBodyData = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Error code.
        self.code = code
        # The returned data.
        self.data = data
        # Dynamic error code.
        self.dynamic_code = dynamic_code
        # Dynamic error message.
        self.dynamic_message = dynamic_message
        self.http_status_code = http_status_code
        # Error message.
        self.message = message
        # Request ID, each request has a unique ID that can be used for troubleshooting and problem localization.
        self.request_id = request_id
        # Indicates whether the execution was successful.
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
            temp_model = ListTopicsResponseBodyData()
            self.data = temp_model.from_map(m['data'])
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


class ListTopicsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTopicsResponseBody = None,
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
            temp_model = ListTopicsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTracesRequest(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        message_id: str = None,
        message_key: str = None,
        page_number: int = None,
        page_size: int = None,
        query_type: str = None,
        start_time: str = None,
    ):
        # The end of the time range to query.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The message ID.
        # 
        # This parameter is required if you set queryType to MESSAGE_ID.
        self.message_id = message_id
        # The message key.
        # 
        # This parameter is required if you set queryType to MESSAGE_ID.
        self.message_key = message_key
        # The page number.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The number of entries per page.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The query type.
        # 
        # Valid values:
        # 
        # *   MESSAGE_ID
        # *   MESSAGE_KEY
        # *   TOPIC
        # 
        # This parameter is required.
        self.query_type = query_type
        # The beginning of the time range to query.
        # 
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.message_id is not None:
            result['messageId'] = self.message_id
        if self.message_key is not None:
            result['messageKey'] = self.message_key
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.query_type is not None:
            result['queryType'] = self.query_type
        if self.start_time is not None:
            result['startTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('messageId') is not None:
            self.message_id = m.get('messageId')
        if m.get('messageKey') is not None:
            self.message_key = m.get('messageKey')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('queryType') is not None:
            self.query_type = m.get('queryType')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        return self


class ListTracesResponseBodyDataList(TeaModel):
    def __init__(
        self,
        born_time: str = None,
        instance_id: str = None,
        message_id: str = None,
        message_keys: List[str] = None,
        message_tag: str = None,
        region_id: str = None,
        topic_name: str = None,
    ):
        # Message born time.
        self.born_time = born_time
        # The instance ID.
        self.instance_id = instance_id
        # Message id.
        self.message_id = message_id
        # Message keys.
        self.message_keys = message_keys
        # Message tag.
        self.message_tag = message_tag
        # The region ID.
        self.region_id = region_id
        # The name of the topic.
        self.topic_name = topic_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.born_time is not None:
            result['bornTime'] = self.born_time
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.message_id is not None:
            result['messageId'] = self.message_id
        if self.message_keys is not None:
            result['messageKeys'] = self.message_keys
        if self.message_tag is not None:
            result['messageTag'] = self.message_tag
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.topic_name is not None:
            result['topicName'] = self.topic_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bornTime') is not None:
            self.born_time = m.get('bornTime')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('messageId') is not None:
            self.message_id = m.get('messageId')
        if m.get('messageKeys') is not None:
            self.message_keys = m.get('messageKeys')
        if m.get('messageTag') is not None:
            self.message_tag = m.get('messageTag')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('topicName') is not None:
            self.topic_name = m.get('topicName')
        return self


class ListTracesResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[ListTracesResponseBodyDataList] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # Trace list.
        self.list = list
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The total number of returned entries.
        self.total_count = total_count

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = ListTracesResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListTracesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListTracesResponseBodyData = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code.
        self.code = code
        # The returned result.
        self.data = data
        # The dynamic error code.
        self.dynamic_code = dynamic_code
        # The dynamic error message.
        self.dynamic_message = dynamic_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The error message.
        self.message = message
        # Id of the request
        self.request_id = request_id
        # Indicates whether the request was successful.
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
            temp_model = ListTracesResponseBodyData()
            self.data = temp_model.from_map(m['data'])
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


class ListTracesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTracesResponseBody = None,
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
            temp_model = ListTracesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetConsumeOffsetRequest(TeaModel):
    def __init__(
        self,
        reset_time: str = None,
        reset_type: str = None,
    ):
        # The time when the consumer offset is reset.
        self.reset_time = reset_time
        # The method that is used to reset the consumer offset. Valid values: LATEST_OFFSET and SPECIFIED_TIME.
        self.reset_type = reset_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.reset_time is not None:
            result['resetTime'] = self.reset_time
        if self.reset_type is not None:
            result['resetType'] = self.reset_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resetTime') is not None:
            self.reset_time = m.get('resetTime')
        if m.get('resetType') is not None:
            self.reset_type = m.get('resetType')
        return self


class ResetConsumeOffsetResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The returned error code.
        self.code = code
        # The returned dynamic error code.
        self.dynamic_code = dynamic_code
        # The returned dynamic error message.
        self.dynamic_message = dynamic_message
        # The returned HTTP status code.
        self.http_status_code = http_status_code
        # The returned error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
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


class ResetConsumeOffsetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ResetConsumeOffsetResponseBody = None,
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
            temp_model = ResetConsumeOffsetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartDisasterRecoveryItemResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: bool = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details about the access denial. This parameter is returned only if the access is denied due to the reason that the Resource Access Management (RAM) user does not have the required permissions.
        self.access_denied_detail = access_denied_detail
        # Error code
        self.code = code
        # Return result
        self.data = data
        # Dynamic error code
        self.dynamic_code = dynamic_code
        # Dynamic error message
        self.dynamic_message = dynamic_message
        # HTTP status code
        self.http_status_code = http_status_code
        # Error message
        self.message = message
        # Request ID
        self.request_id = request_id
        # Whether the operation was successful
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['accessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
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
        if m.get('accessDeniedDetail') is not None:
            self.access_denied_detail = m.get('accessDeniedDetail')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
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


class StartDisasterRecoveryItemResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartDisasterRecoveryItemResponseBody = None,
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
            temp_model = StartDisasterRecoveryItemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopDisasterRecoveryItemResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: bool = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details about the access denial. This parameter is returned only if the access is denied because the Resource Access Management (RAM) user does not have the required permissions.
        self.access_denied_detail = access_denied_detail
        # Error code
        self.code = code
        # Return result
        self.data = data
        # Dynamic error code
        self.dynamic_code = dynamic_code
        # Dynamic error message
        self.dynamic_message = dynamic_message
        # HTTP status code
        self.http_status_code = http_status_code
        # Error message
        self.message = message
        # Request ID
        self.request_id = request_id
        # Whether the operation was successful
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['accessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
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
        if m.get('accessDeniedDetail') is not None:
            self.access_denied_detail = m.get('accessDeniedDetail')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
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


class StopDisasterRecoveryItemResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopDisasterRecoveryItemResponseBody = None,
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
            temp_model = StopDisasterRecoveryItemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SyncDisasterRecoveryCheckpointResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Error Code
        self.code = code
        # Result Data
        self.data = data
        # Dynamic Error Code
        self.dynamic_code = dynamic_code
        # The dynamic error message.
        self.dynamic_message = dynamic_message
        # HTTP Status Code
        self.http_status_code = http_status_code
        # Error Message
        self.message = message
        # Request ID
        self.request_id = request_id
        # Success or Not
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
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
            self.data = m.get('data')
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


class SyncDisasterRecoveryCheckpointResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SyncDisasterRecoveryCheckpointResponseBody = None,
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
            temp_model = SyncDisasterRecoveryCheckpointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        resource_id: str = None,
        resource_type: str = None,
        tag: str = None,
    ):
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource IDs, in the JSON format.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The type of resource.
        # 
        # Set this parameter to **instance**. The value of this parameter cannot be changed.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # tag, in JSON format.
        # 
        # This parameter is required.
        self.tag = tag

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.resource_id is not None:
            result['resourceId'] = self.resource_id
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        if self.tag is not None:
            result['tag'] = self.tag
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        if m.get('tag') is not None:
            self.tag = m.get('tag')
        return self


class TagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code.
        self.code = code
        # The returned result.
        self.data = data
        # The dynamic error code.
        self.dynamic_code = dynamic_code
        # The dynamic error message.
        self.dynamic_message = dynamic_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The error code.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the call was successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
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
            self.data = m.get('data')
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


class TagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TagResourcesResponseBody = None,
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
            temp_model = TagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(
        self,
        all: bool = None,
        region_id: str = None,
        resource_id: str = None,
        resource_type: str = None,
        tag_key: str = None,
    ):
        # Whether to delete all tags.
        self.all = all
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource IDs, in the JSON format.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The type of resource.
        # 
        # Set this parameter to **instance**. The value of this parameter cannot be changed.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The keys of tags.
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['all'] = self.all
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.resource_id is not None:
            result['resourceId'] = self.resource_id
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        if self.tag_key is not None:
            result['tagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('all') is not None:
            self.all = m.get('all')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        if m.get('tagKey') is not None:
            self.tag_key = m.get('tagKey')
        return self


class UntagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
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
        # The ID of the request. Each request has a unique ID. You can use this ID to troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the call was successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
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
            self.data = m.get('data')
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


class UntagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UntagResourcesResponseBody = None,
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
            temp_model = UntagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateConsumerGroupRequestConsumeRetryPolicy(TeaModel):
    def __init__(
        self,
        dead_letter_target_topic: str = None,
        fixed_interval_retry_time: int = None,
        max_retry_times: int = None,
        retry_policy: str = None,
    ):
        # The dead-letter topic.
        # 
        # If a consumer still fails to consume a message after the maximum number of retries specified for the message is reached, the message is delivered to the dead-letter topic for subsequent business recovery or troubleshooting. For more information, see [Consumption retry and dead-letter messages](https://help.aliyun.com/document_detail/440356.html).
        self.dead_letter_target_topic = dead_letter_target_topic
        self.fixed_interval_retry_time = fixed_interval_retry_time
        # The maximum number of retries.
        self.max_retry_times = max_retry_times
        # The retry policy. For more information, see [Message retry](https://help.aliyun.com/document_detail/440356.html).
        # 
        # Valid values:
        # 
        # *   FixedRetryPolicy: fixed-interval retry. This value is valid only if you set deliveryOrderType to Orderly.
        # *   DefaultRetryPolicy: exponential backoff retry. This value is valid only if you set deliveryOrderType to Concurrently.
        # 
        # This parameter is required.
        self.retry_policy = retry_policy

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dead_letter_target_topic is not None:
            result['deadLetterTargetTopic'] = self.dead_letter_target_topic
        if self.fixed_interval_retry_time is not None:
            result['fixedIntervalRetryTime'] = self.fixed_interval_retry_time
        if self.max_retry_times is not None:
            result['maxRetryTimes'] = self.max_retry_times
        if self.retry_policy is not None:
            result['retryPolicy'] = self.retry_policy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deadLetterTargetTopic') is not None:
            self.dead_letter_target_topic = m.get('deadLetterTargetTopic')
        if m.get('fixedIntervalRetryTime') is not None:
            self.fixed_interval_retry_time = m.get('fixedIntervalRetryTime')
        if m.get('maxRetryTimes') is not None:
            self.max_retry_times = m.get('maxRetryTimes')
        if m.get('retryPolicy') is not None:
            self.retry_policy = m.get('retryPolicy')
        return self


class UpdateConsumerGroupRequest(TeaModel):
    def __init__(
        self,
        consume_retry_policy: UpdateConsumerGroupRequestConsumeRetryPolicy = None,
        delivery_order_type: str = None,
        max_receive_tps: int = None,
        remark: str = None,
    ):
        # The new consumption retry policy of the consumer group. For more information, see [Consumption retry](https://help.aliyun.com/document_detail/440356.html).
        # 
        # This parameter is required.
        self.consume_retry_policy = consume_retry_policy
        # The new message delivery method of the consumer group.
        # 
        # Valid values:
        # 
        # *   Concurrently: concurrent delivery
        # *   Orderly: ordered delivery
        # 
        # This parameter is required.
        self.delivery_order_type = delivery_order_type
        # The maximum TPS for message sending.
        self.max_receive_tps = max_receive_tps
        # The new description of the consumer group.
        self.remark = remark

    def validate(self):
        if self.consume_retry_policy:
            self.consume_retry_policy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consume_retry_policy is not None:
            result['consumeRetryPolicy'] = self.consume_retry_policy.to_map()
        if self.delivery_order_type is not None:
            result['deliveryOrderType'] = self.delivery_order_type
        if self.max_receive_tps is not None:
            result['maxReceiveTps'] = self.max_receive_tps
        if self.remark is not None:
            result['remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('consumeRetryPolicy') is not None:
            temp_model = UpdateConsumerGroupRequestConsumeRetryPolicy()
            self.consume_retry_policy = temp_model.from_map(m['consumeRetryPolicy'])
        if m.get('deliveryOrderType') is not None:
            self.delivery_order_type = m.get('deliveryOrderType')
        if m.get('maxReceiveTps') is not None:
            self.max_receive_tps = m.get('maxReceiveTps')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        return self


class UpdateConsumerGroupResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Error code.
        self.code = code
        # The result returned.
        self.data = data
        # Dynamic error code.
        self.dynamic_code = dynamic_code
        # Dynamic error message.
        self.dynamic_message = dynamic_message
        # HTTP status code.
        self.http_status_code = http_status_code
        # Error message.
        self.message = message
        # The request ID, which is unique for each request and can be used for troubleshooting and problem localization.
        self.request_id = request_id
        # Indicates whether the execution was successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
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
            self.data = m.get('data')
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


class UpdateConsumerGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateConsumerGroupResponseBody = None,
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
            temp_model = UpdateConsumerGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDisasterRecoveryItemRequestTopics(TeaModel):
    def __init__(
        self,
        consumer_group_id: str = None,
        delivery_order_type: str = None,
        instance_id: str = None,
        instance_type: str = None,
        region_id: str = None,
        topic_name: str = None,
    ):
        # The ID of the consumer group. If you use the two-way backup mode, you must specify this parameter.
        self.consumer_group_id = consumer_group_id
        # The method used to deliver messages to the destination instance.
        # 
        # Valid values:
        # 
        # *   Concurrently: concurrent delivery
        # *   Orderly: ordered delivery
        self.delivery_order_type = delivery_order_type
        # The instance ID. If you set instanceType to EXTERNAL_ROCKETMQ, the system automatically generates an ID for the instance. You can obtain the ID by querying the global message backup plan.
        self.instance_id = instance_id
        # The instance type. Valid values:
        # 
        # *   ALIYUN_ROCKETMQ: ApsaraMQ for RocketMQ instance
        # *   EXTERNAL_ROCKETMQ: open source RocketMQ cluster
        self.instance_type = instance_type
        # The region ID.
        self.region_id = region_id
        # The topic name. You must specify this parameter.
        self.topic_name = topic_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consumer_group_id is not None:
            result['consumerGroupId'] = self.consumer_group_id
        if self.delivery_order_type is not None:
            result['deliveryOrderType'] = self.delivery_order_type
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.topic_name is not None:
            result['topicName'] = self.topic_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('consumerGroupId') is not None:
            self.consumer_group_id = m.get('consumerGroupId')
        if m.get('deliveryOrderType') is not None:
            self.delivery_order_type = m.get('deliveryOrderType')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('topicName') is not None:
            self.topic_name = m.get('topicName')
        return self


class UpdateDisasterRecoveryItemRequest(TeaModel):
    def __init__(
        self,
        topics: List[UpdateDisasterRecoveryItemRequestTopics] = None,
    ):
        # The topics involved in the topic mapping.
        self.topics = topics

    def validate(self):
        if self.topics:
            for k in self.topics:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['topics'] = []
        if self.topics is not None:
            for k in self.topics:
                result['topics'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.topics = []
        if m.get('topics') is not None:
            for k in m.get('topics'):
                temp_model = UpdateDisasterRecoveryItemRequestTopics()
                self.topics.append(temp_model.from_map(k))
        return self


class UpdateDisasterRecoveryItemResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
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
        # The response code.
        self.http_status_code = http_status_code
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
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
            self.data = m.get('data')
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


class UpdateDisasterRecoveryItemResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateDisasterRecoveryItemResponseBody = None,
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
            temp_model = UpdateDisasterRecoveryItemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDisasterRecoveryPlanRequestInstancesMessageProperty(TeaModel):
    def __init__(
        self,
        property_key: str = None,
        property_value: str = None,
    ):
        # The attribute key.
        self.property_key = property_key
        # The attribute value.
        self.property_value = property_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.property_key is not None:
            result['propertyKey'] = self.property_key
        if self.property_value is not None:
            result['propertyValue'] = self.property_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('propertyKey') is not None:
            self.property_key = m.get('propertyKey')
        if m.get('propertyValue') is not None:
            self.property_value = m.get('propertyValue')
        return self


class UpdateDisasterRecoveryPlanRequestInstances(TeaModel):
    def __init__(
        self,
        auth_type: str = None,
        consumer_group_id: str = None,
        endpoint_url: str = None,
        instance_id: str = None,
        instance_role: str = None,
        instance_type: str = None,
        message_property: UpdateDisasterRecoveryPlanRequestInstancesMessageProperty = None,
        network_type: str = None,
        password: str = None,
        region_id: str = None,
        security_group_id: str = None,
        username: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        # The authentication type.
        # 
        # *   NO_AUTH: no authentication
        # *   ACL_AUTH: access control list (ACL)-based authentication
        self.auth_type = auth_type
        self.consumer_group_id = consumer_group_id
        # The instance endpoint. This parameter is required only if you set instanceType to EXTERNAL_ROCKETMQ.
        self.endpoint_url = endpoint_url
        # The instance ID.
        self.instance_id = instance_id
        # The instance role. Valid values:
        # 
        # *   ACTIVE: primary instance
        # *   Passive: secondary instance
        self.instance_role = instance_role
        # The instance type. Valid values:
        # 
        # *   ALIYUN_ROCKETMQ: ApsaraMQ for RocketMQ instance
        # *   EXTERNAL_ROCKETMQ: open source RocketMQ cluster
        self.instance_type = instance_type
        # The message attribute. When you synchronize a message to the destination cluster, the system automatically adds the attribute to the message for SQL-based filtering.
        self.message_property = message_property
        # The network type. This parameter is required only if you set instanceType to EXTERNAL_ROCKETMQ. Valid values:
        # 
        # *   TCP_INTERNET: Internet over TCP
        # *   TCP_VPC: virtual private cloud (VPC) over TCP.
        self.network_type = network_type
        # The password that is used for authentication. This parameter is required only if you set authType to ACL_AUTH.
        self.password = password
        # The region in which the instance resides.
        self.region_id = region_id
        # The ID of the security group to which the instance belongs. This parameter is required only if you set instanceType to EXTERNAL_ROCKETMQ.
        self.security_group_id = security_group_id
        # The username that is used for authentication. This parameter is required only if you set authType to ACL_AUTH.
        self.username = username
        # The ID of the vSwitch with which the instance is associated. If you want to specify multiple vSwitches, separate the vSwitches with vertical bars (|).
        self.v_switch_id = v_switch_id
        # The ID of the VPC with which the instance is associated. This parameter is required only if you set instanceType to EXTERNAL_ROCKETMQ.
        self.vpc_id = vpc_id

    def validate(self):
        if self.message_property:
            self.message_property.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_type is not None:
            result['authType'] = self.auth_type
        if self.consumer_group_id is not None:
            result['consumerGroupId'] = self.consumer_group_id
        if self.endpoint_url is not None:
            result['endpointUrl'] = self.endpoint_url
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.instance_role is not None:
            result['instanceRole'] = self.instance_role
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        if self.message_property is not None:
            result['messageProperty'] = self.message_property.to_map()
        if self.network_type is not None:
            result['networkType'] = self.network_type
        if self.password is not None:
            result['password'] = self.password
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.security_group_id is not None:
            result['securityGroupId'] = self.security_group_id
        if self.username is not None:
            result['username'] = self.username
        if self.v_switch_id is not None:
            result['vSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authType') is not None:
            self.auth_type = m.get('authType')
        if m.get('consumerGroupId') is not None:
            self.consumer_group_id = m.get('consumerGroupId')
        if m.get('endpointUrl') is not None:
            self.endpoint_url = m.get('endpointUrl')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('instanceRole') is not None:
            self.instance_role = m.get('instanceRole')
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        if m.get('messageProperty') is not None:
            temp_model = UpdateDisasterRecoveryPlanRequestInstancesMessageProperty()
            self.message_property = temp_model.from_map(m['messageProperty'])
        if m.get('networkType') is not None:
            self.network_type = m.get('networkType')
        if m.get('password') is not None:
            self.password = m.get('password')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('securityGroupId') is not None:
            self.security_group_id = m.get('securityGroupId')
        if m.get('username') is not None:
            self.username = m.get('username')
        if m.get('vSwitchId') is not None:
            self.v_switch_id = m.get('vSwitchId')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        return self


class UpdateDisasterRecoveryPlanRequest(TeaModel):
    def __init__(
        self,
        auto_sync_checkpoint: bool = None,
        instances: List[UpdateDisasterRecoveryPlanRequestInstances] = None,
        plan_desc: str = None,
        plan_name: str = None,
        plan_type: str = None,
        sync_checkpoint_enabled: bool = None,
    ):
        # Whether to enable automatic synchronization of consumption progress.
        # 
        # > This is effective only when consumption progress synchronization is enabled, i.e., the value of `syncCheckpointEnabled` is true.
        self.auto_sync_checkpoint = auto_sync_checkpoint
        # The instances that are involved in the global message backup plan.
        self.instances = instances
        # The description of the global message backup plan.
        self.plan_desc = plan_desc
        # The name of the global message backup plan.
        self.plan_name = plan_name
        # The type of the global message backup plan. Valid values:
        # 
        # *   ACTIVE_PASSIVE: geo-disaster recovery
        # *   ACTIVE_ACTIVE: active geo-redundancy
        self.plan_type = plan_type
        # Switch for synchronizing consumption progress
        self.sync_checkpoint_enabled = sync_checkpoint_enabled

    def validate(self):
        if self.instances:
            for k in self.instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_sync_checkpoint is not None:
            result['autoSyncCheckpoint'] = self.auto_sync_checkpoint
        result['instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['instances'].append(k.to_map() if k else None)
        if self.plan_desc is not None:
            result['planDesc'] = self.plan_desc
        if self.plan_name is not None:
            result['planName'] = self.plan_name
        if self.plan_type is not None:
            result['planType'] = self.plan_type
        if self.sync_checkpoint_enabled is not None:
            result['syncCheckpointEnabled'] = self.sync_checkpoint_enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoSyncCheckpoint') is not None:
            self.auto_sync_checkpoint = m.get('autoSyncCheckpoint')
        self.instances = []
        if m.get('instances') is not None:
            for k in m.get('instances'):
                temp_model = UpdateDisasterRecoveryPlanRequestInstances()
                self.instances.append(temp_model.from_map(k))
        if m.get('planDesc') is not None:
            self.plan_desc = m.get('planDesc')
        if m.get('planName') is not None:
            self.plan_name = m.get('planName')
        if m.get('planType') is not None:
            self.plan_type = m.get('planType')
        if m.get('syncCheckpointEnabled') is not None:
            self.sync_checkpoint_enabled = m.get('syncCheckpointEnabled')
        return self


class UpdateDisasterRecoveryPlanResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: bool = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details about the access denial. This parameter is returned only if the access is denied because the Resource Access Management (RAM) user does not have the required permissions.
        self.access_denied_detail = access_denied_detail
        # The error code.
        self.code = code
        # The data returned.
        self.data = data
        # The dynamic error code.
        self.dynamic_code = dynamic_code
        # The dynamic error message.
        self.dynamic_message = dynamic_message
        # The response code.
        self.http_status_code = http_status_code
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['accessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
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
        if m.get('accessDeniedDetail') is not None:
            self.access_denied_detail = m.get('accessDeniedDetail')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
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


class UpdateDisasterRecoveryPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateDisasterRecoveryPlanResponseBody = None,
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
            temp_model = UpdateDisasterRecoveryPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateInstanceRequestAclInfo(TeaModel):
    def __init__(
        self,
        acl_types: List[str] = None,
        default_vpc_auth_free: bool = None,
    ):
        # The authentication type of the instance.
        self.acl_types = acl_types
        # Indicates whether the authentication-free in VPCs feature is enabled.
        # Indicates whether the authentication-free in VPCs feature is enabled.
        # Valid values:
        # - true
        # - false
        self.default_vpc_auth_free = default_vpc_auth_free

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_types is not None:
            result['aclTypes'] = self.acl_types
        if self.default_vpc_auth_free is not None:
            result['defaultVpcAuthFree'] = self.default_vpc_auth_free
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aclTypes') is not None:
            self.acl_types = m.get('aclTypes')
        if m.get('defaultVpcAuthFree') is not None:
            self.default_vpc_auth_free = m.get('defaultVpcAuthFree')
        return self


class UpdateInstanceRequestNetworkInfoInternetInfo(TeaModel):
    def __init__(
        self,
        ip_whitelist: List[str] = None,
    ):
        # The whitelist that includes the IP addresses that are allowed to access the ApsaraMQ for RocketMQ broker over the Internet.
        # 
        # *   If you do not configure an IP address whitelist, all CIDR blocks are allowed to access the ApsaraMQ for RocketMQ broker over the Internet.
        # *   If you configure an IP address whitelist, only the IP addresses in the whitelist are allowed to access the ApsaraMQ for RocketMQ broker over the Internet.
        self.ip_whitelist = ip_whitelist

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_whitelist is not None:
            result['ipWhitelist'] = self.ip_whitelist
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ipWhitelist') is not None:
            self.ip_whitelist = m.get('ipWhitelist')
        return self


class UpdateInstanceRequestNetworkInfo(TeaModel):
    def __init__(
        self,
        internet_info: UpdateInstanceRequestNetworkInfoInternetInfo = None,
    ):
        # The information about the Internet over which the instance is accessed. This parameter takes effect only if the Internet access feature is enabled for the instance.
        self.internet_info = internet_info

    def validate(self):
        if self.internet_info:
            self.internet_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.internet_info is not None:
            result['internetInfo'] = self.internet_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('internetInfo') is not None:
            temp_model = UpdateInstanceRequestNetworkInfoInternetInfo()
            self.internet_info = temp_model.from_map(m['internetInfo'])
        return self


class UpdateInstanceRequestProductInfo(TeaModel):
    def __init__(
        self,
        auto_scaling: bool = None,
        message_retention_time: int = None,
        send_receive_ratio: float = None,
        trace_on: bool = None,
    ):
        # Specifies whether to enable the elastic transactions per second (TPS) feature for the instance.
        # 
        # Valid values:
        # 
        # *   true
        # *   false
        # 
        # After you enable the elastic TPS feature for an ApsaraMQ for RocketMQ instance, you can use a specific number of TPS that exceeds the specification limit. You are charged for using the elastic TPS feature. For more information, see [Computing fees](https://help.aliyun.com/document_detail/427237.html).
        # 
        # >  The elastic TPS feature is supported only by specific instance editions. For more information, see [Instance editions](https://help.aliyun.com/document_detail/444715.html).
        self.auto_scaling = auto_scaling
        # The retention period of messages. Unit: hours.
        # 
        # For information about the valid values of this parameter, see the "Limits on resource quotas" section of the [Limits](https://help.aliyun.com/document_detail/440347.html) topic.
        # 
        # ApsaraMQ for RocketMQ supports serverless scaling of message storage. You are charged storage fees based on your actual storage usage. You can change the retention period of messages to manage storage capacity. For more information, see [Storage fees](https://help.aliyun.com/document_detail/427238.html).
        self.message_retention_time = message_retention_time
        # The ratio of the number of messages that you can send to the number of messages that you can receive on the instance.
        # 
        # Value values: 0.25 to 1.
        self.send_receive_ratio = send_receive_ratio
        # Specifies whether to enable the message trace feature.
        # 
        # *   true
        # *   false
        # 
        # This parameter is not in use. By default, the message trace feature is enabled for ApsaraMQ for RocketMQ instances, regardless of whether this parameter is configured.
        self.trace_on = trace_on

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_scaling is not None:
            result['autoScaling'] = self.auto_scaling
        if self.message_retention_time is not None:
            result['messageRetentionTime'] = self.message_retention_time
        if self.send_receive_ratio is not None:
            result['sendReceiveRatio'] = self.send_receive_ratio
        if self.trace_on is not None:
            result['traceOn'] = self.trace_on
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoScaling') is not None:
            self.auto_scaling = m.get('autoScaling')
        if m.get('messageRetentionTime') is not None:
            self.message_retention_time = m.get('messageRetentionTime')
        if m.get('sendReceiveRatio') is not None:
            self.send_receive_ratio = m.get('sendReceiveRatio')
        if m.get('traceOn') is not None:
            self.trace_on = m.get('traceOn')
        return self


class UpdateInstanceRequest(TeaModel):
    def __init__(
        self,
        acl_info: UpdateInstanceRequestAclInfo = None,
        instance_name: str = None,
        network_info: UpdateInstanceRequestNetworkInfo = None,
        product_info: UpdateInstanceRequestProductInfo = None,
        remark: str = None,
    ):
        # The access control list for the instance.
        self.acl_info = acl_info
        # The updated name of the instance.
        self.instance_name = instance_name
        # The updated network information about the instance.
        self.network_info = network_info
        # Additional configurations of the instance.
        self.product_info = product_info
        # The updated description of the instance.
        self.remark = remark

    def validate(self):
        if self.acl_info:
            self.acl_info.validate()
        if self.network_info:
            self.network_info.validate()
        if self.product_info:
            self.product_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_info is not None:
            result['aclInfo'] = self.acl_info.to_map()
        if self.instance_name is not None:
            result['instanceName'] = self.instance_name
        if self.network_info is not None:
            result['networkInfo'] = self.network_info.to_map()
        if self.product_info is not None:
            result['productInfo'] = self.product_info.to_map()
        if self.remark is not None:
            result['remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aclInfo') is not None:
            temp_model = UpdateInstanceRequestAclInfo()
            self.acl_info = temp_model.from_map(m['aclInfo'])
        if m.get('instanceName') is not None:
            self.instance_name = m.get('instanceName')
        if m.get('networkInfo') is not None:
            temp_model = UpdateInstanceRequestNetworkInfo()
            self.network_info = temp_model.from_map(m['networkInfo'])
        if m.get('productInfo') is not None:
            temp_model = UpdateInstanceRequestProductInfo()
            self.product_info = temp_model.from_map(m['productInfo'])
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        return self


class UpdateInstanceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code.
        self.code = code
        # The result data that is returned.
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
        # Indicates whether the call is successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
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
            self.data = m.get('data')
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


class UpdateInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateInstanceResponseBody = None,
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
            temp_model = UpdateInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateInstanceAccountRequest(TeaModel):
    def __init__(
        self,
        account_status: str = None,
        password: str = None,
    ):
        # The status of the account.
        # 
        # Valid values:
        # 
        # *   DISABLE
        # *   ENABLE
        self.account_status = account_status
        # The password of the account.
        self.password = password

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_status is not None:
            result['accountStatus'] = self.account_status
        if self.password is not None:
            result['password'] = self.password
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountStatus') is not None:
            self.account_status = m.get('accountStatus')
        if m.get('password') is not None:
            self.password = m.get('password')
        return self


class UpdateInstanceAccountResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: bool = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details about the access denial. This parameter is returned only if the access is denied because the Resource Access Management (RAM) user does not have the required permissions.
        self.access_denied_detail = access_denied_detail
        # The error code.
        self.code = code
        # The returned result.
        self.data = data
        # The dynamic error code.
        self.dynamic_code = dynamic_code
        # The dynamic error message.
        self.dynamic_message = dynamic_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The error message.
        self.message = message
        # The ID of the request. Each request has a unique ID. You can use this ID to troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the call is successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['accessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
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
        if m.get('accessDeniedDetail') is not None:
            self.access_denied_detail = m.get('accessDeniedDetail')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
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


class UpdateInstanceAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateInstanceAccountResponseBody = None,
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
            temp_model = UpdateInstanceAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateInstanceAclRequest(TeaModel):
    def __init__(
        self,
        actions: List[str] = None,
        decision: str = None,
        ip_whitelists: List[str] = None,
        resource_name: str = None,
        resource_type: str = None,
    ):
        # The following items describe the types of permissions that can be granted based on the resource type:
        # 
        # *   Topic: Pub, Sub, and Pub|Sub
        # *   Consumer group: Sub
        # 
        # Valid values:
        # 
        # *   SUB: subscribe
        # *   Pub|Sub: publish and subscribe
        # *   Pub: publish
        self.actions = actions
        # The decision result of the authorization.
        # 
        # Valid values:
        # 
        # *   Deny
        # *   Allow
        self.decision = decision
        # The IP address whitelists.
        self.ip_whitelists = ip_whitelists
        # The name of the resource on which you want to grant permissions.
        # 
        # This parameter is required.
        self.resource_name = resource_name
        # The type of the resource on which you want to grant permissions.
        # 
        # Valid values:
        # 
        # *   Group
        # *   Topic
        # 
        # This parameter is required.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actions is not None:
            result['actions'] = self.actions
        if self.decision is not None:
            result['decision'] = self.decision
        if self.ip_whitelists is not None:
            result['ipWhitelists'] = self.ip_whitelists
        if self.resource_name is not None:
            result['resourceName'] = self.resource_name
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actions') is not None:
            self.actions = m.get('actions')
        if m.get('decision') is not None:
            self.decision = m.get('decision')
        if m.get('ipWhitelists') is not None:
            self.ip_whitelists = m.get('ipWhitelists')
        if m.get('resourceName') is not None:
            self.resource_name = m.get('resourceName')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        return self


class UpdateInstanceAclResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: bool = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details about the access denial. This parameter is returned only if the access is denied because the Resource Access Management (RAM) user does not have the required permissions.
        self.access_denied_detail = access_denied_detail
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
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['accessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
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
        if m.get('accessDeniedDetail') is not None:
            self.access_denied_detail = m.get('accessDeniedDetail')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
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


class UpdateInstanceAclResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateInstanceAclResponseBody = None,
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
            temp_model = UpdateInstanceAclResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTopicRequest(TeaModel):
    def __init__(
        self,
        max_send_tps: int = None,
        remark: str = None,
    ):
        # Maximum send message tps
        self.max_send_tps = max_send_tps
        # Updated remarks for the topic.
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_send_tps is not None:
            result['maxSendTps'] = self.max_send_tps
        if self.remark is not None:
            result['remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxSendTps') is not None:
            self.max_send_tps = m.get('maxSendTps')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        return self


class UpdateTopicResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Error code.
        self.code = code
        # Return result.
        self.data = data
        # Dynamic error code
        self.dynamic_code = dynamic_code
        # 动态错误信息
        self.dynamic_message = dynamic_message
        # HTTP status code.
        self.http_status_code = http_status_code
        # Error message.
        self.message = message
        # Request ID, each request has a unique ID that can be used for troubleshooting and problem localization.
        self.request_id = request_id
        # Whether the execution result is successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
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
            self.data = m.get('data')
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


class UpdateTopicResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateTopicResponseBody = None,
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
            temp_model = UpdateTopicResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VerifyConsumeMessageRequest(TeaModel):
    def __init__(
        self,
        client_id: str = None,
        consumer_group_id: str = None,
    ):
        # The client ID.
        # 
        # This parameter is required.
        self.client_id = client_id
        # The ID of the consumer group.
        # 
        # This parameter is required.
        self.consumer_group_id = consumer_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['clientId'] = self.client_id
        if self.consumer_group_id is not None:
            result['consumerGroupId'] = self.consumer_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientId') is not None:
            self.client_id = m.get('clientId')
        if m.get('consumerGroupId') is not None:
            self.consumer_group_id = m.get('consumerGroupId')
        return self


class VerifyConsumeMessageResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
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
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
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
            self.data = m.get('data')
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


class VerifyConsumeMessageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: VerifyConsumeMessageResponseBody = None,
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
            temp_model = VerifyConsumeMessageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VerifySendMessageRequest(TeaModel):
    def __init__(
        self,
        message: str = None,
        message_key: str = None,
        message_tag: str = None,
    ):
        # The message body.
        self.message = message
        # The message key.
        self.message_key = message_key
        # The message tag.
        self.message_tag = message_tag

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['message'] = self.message
        if self.message_key is not None:
            result['messageKey'] = self.message_key
        if self.message_tag is not None:
            result['messageTag'] = self.message_tag
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('messageKey') is not None:
            self.message_key = m.get('messageKey')
        if m.get('messageTag') is not None:
            self.message_tag = m.get('messageTag')
        return self


class VerifySendMessageResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
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
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
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
            self.data = m.get('data')
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


class VerifySendMessageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: VerifySendMessageResponseBody = None,
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
            temp_model = VerifySendMessageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


