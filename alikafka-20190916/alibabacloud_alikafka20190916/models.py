# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class ChangeResourceGroupRequest(TeaModel):
    def __init__(
        self,
        new_resource_group_id: str = None,
        region_id: str = None,
        resource_id: str = None,
    ):
        # The ID of the resource group to which you want to transfer the cloud resource.
        # 
        # >  You can use resource groups to manage resources owned by your Alibaba Cloud account. Resource groups simplify the resource and permission management of your Alibaba Cloud account. For more information, see [What is resource management?](https://help.aliyun.com/document_detail/94475.html)
        # 
        # This parameter is required.
        self.new_resource_group_id = new_resource_group_id
        # The region ID of the resource.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource to which you want to attach a tag. Only the ID of a Message Queue for Apache Kafka instance is supported.
        # 
        # For example, if the ID of the instance is alikafka_post-cn-v0h1fgs2xxxx, the resource ID is alikafka_post-cn-v0h1fgs2xxxx.
        # 
        # This parameter is required.
        self.resource_id = resource_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.new_resource_group_id is not None:
            result['NewResourceGroupId'] = self.new_resource_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NewResourceGroupId') is not None:
            self.new_resource_group_id = m.get('NewResourceGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        return self


class ChangeResourceGroupResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        new_resource_group_id: str = None,
        request_id: str = None,
        success: int = None,
    ):
        # The HTTP status code returned. The HTTP status code 200 indicates that the request is successful.
        self.code = code
        # The returned message.
        self.message = message
        # The ID of the new resource group. You can view the available resource groups in the Resource Management console.
        self.new_resource_group_id = new_resource_group_id
        # The ID of the request.
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
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.new_resource_group_id is not None:
            result['NewResourceGroupId'] = self.new_resource_group_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NewResourceGroupId') is not None:
            self.new_resource_group_id = m.get('NewResourceGroupId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
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


class ConvertPostPayOrderRequest(TeaModel):
    def __init__(
        self,
        duration: int = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        # The subscription duration. Unit: months. Valid values:
        # 
        # *   **1~12**\
        # *   **24**\
        # *   **36**\
        self.duration = duration
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The region ID of the instance.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ConvertPostPayOrderResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        order_id: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code returned. The HTTP status code 200 indicates that the request is successful.
        self.code = code
        # The error message returned.
        self.message = message
        # The ID of the order.
        self.order_id = order_id
        # The ID of the request.
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
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ConvertPostPayOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ConvertPostPayOrderResponseBody = None,
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
            temp_model = ConvertPostPayOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAclRequest(TeaModel):
    def __init__(
        self,
        acl_operation_type: str = None,
        acl_operation_types: str = None,
        acl_permission_type: str = None,
        acl_resource_name: str = None,
        acl_resource_pattern_type: str = None,
        acl_resource_type: str = None,
        host: str = None,
        instance_id: str = None,
        region_id: str = None,
        username: str = None,
    ):
        # The type of the operation allowed by the access control list (ACL). Valid values:
        # 
        # *   **Write**\
        # *   **Read**\
        # *   **Describe**: reads of transactional IDs.
        # *   **IdempotentWrite**: idempotent data writes to clusters.
        # *   **IDEMPOTENT_WRITE**: idempotent data writes to clusters. This value is available only for ApsaraMQ for Kafka V3 instances.
        # *   **DESCRIBE_CONFIGS**: queries of configurations. This value is available only for ApsaraMQ for Kafka V3 instances.
        # 
        # This parameter is required.
        self.acl_operation_type = acl_operation_type
        # The types of operations allowed by the ACL. Separate multiple operation types with commas (,).
        # 
        # Valid values:
        # 
        # *   **Write**\
        # *   **Read**\
        # *   **Describe**: reads of transactional IDs.
        # *   **IdempotentWrite**: idempotent data writes to clusters.
        # *   **IDEMPOTENT_WRITE**: idempotent data writes to clusters. This value is available only for ApsaraMQ for Kafka V3 instances.
        # *   **DESCRIBE_CONFIGS**: queries of configurations. This value is available only for ApsaraMQ for Kafka V3 instances.
        # 
        # >  This parameter is available only for ApsaraMQ for Kafka V3 serverless instances.
        self.acl_operation_types = acl_operation_types
        # The authorization method. Valid values:
        # 
        # *   **DENY**\
        # *   **ALLOW**\
        # 
        # >  This parameter is available only for ApsaraMQ for Kafka V3 serverless instances.
        self.acl_permission_type = acl_permission_type
        # The resource name.
        # 
        # *   The value can be a topic name, a group ID, a cluster name, or a transaction ID.
        # *   You can use an asterisk (\\*) to specify the names of all resources of the specified type.
        # 
        # > You can use an asterisk (\\*) to query the resources on which permissions are granted only after you grant the user the required permissions on all resources.
        # 
        # This parameter is required.
        self.acl_resource_name = acl_resource_name
        # The matching mode. Valid values:
        # 
        # *   **LITERAL**: exact match
        # *   **PREFIXED**: prefix match
        # 
        # This parameter is required.
        self.acl_resource_pattern_type = acl_resource_pattern_type
        # The resource type. Valid values:
        # 
        # *   **Topic**\
        # *   **Group**\
        # *   **Cluster**\
        # *   **TransactionalId**: transactional ID
        # 
        # This parameter is required.
        self.acl_resource_type = acl_resource_type
        # The source IP address.
        # 
        # > -  You can specify only a specific IP address or use the asterisk (\\*) wildcard character to specify all IP addresses. CIDR blocks are not supported.
        # > -  This parameter is available only for ApsaraMQ for Kafka V3 serverless instances.
        self.host = host
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The username.
        # 
        # *   You can use an asterisk (\\*) to specify all usernames.
        # 
        # > You can use an asterisk (\\*) to query the authorized users only after you grant the required permissions to all users.
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
        if self.acl_operation_type is not None:
            result['AclOperationType'] = self.acl_operation_type
        if self.acl_operation_types is not None:
            result['AclOperationTypes'] = self.acl_operation_types
        if self.acl_permission_type is not None:
            result['AclPermissionType'] = self.acl_permission_type
        if self.acl_resource_name is not None:
            result['AclResourceName'] = self.acl_resource_name
        if self.acl_resource_pattern_type is not None:
            result['AclResourcePatternType'] = self.acl_resource_pattern_type
        if self.acl_resource_type is not None:
            result['AclResourceType'] = self.acl_resource_type
        if self.host is not None:
            result['Host'] = self.host
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclOperationType') is not None:
            self.acl_operation_type = m.get('AclOperationType')
        if m.get('AclOperationTypes') is not None:
            self.acl_operation_types = m.get('AclOperationTypes')
        if m.get('AclPermissionType') is not None:
            self.acl_permission_type = m.get('AclPermissionType')
        if m.get('AclResourceName') is not None:
            self.acl_resource_name = m.get('AclResourceName')
        if m.get('AclResourcePatternType') is not None:
            self.acl_resource_pattern_type = m.get('AclResourcePatternType')
        if m.get('AclResourceType') is not None:
            self.acl_resource_type = m.get('AclResourceType')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class CreateAclResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code returned. The HTTP status code 200 indicates that the request is successful.
        self.code = code
        # The message returned.
        self.message = message
        # The ID of the request.
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
            result['Code'] = self.code
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateAclResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAclResponseBody = None,
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
            temp_model = CreateAclResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateConsumerGroupRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        # 
        # *   You must specify this parameter.
        # *   The tag key can be up to 128 characters in length and cannot start with acs: or aliyun. It cannot contain `http://` or `https://`.
        # 
        # This parameter is required.
        self.key = key
        # The tag value.
        # 
        # *   You can leave this parameter empty.
        # *   The tag value can be up to 128 characters in length and cannot start with acs: or aliyun. It cannot contain `http://` or `https://`.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateConsumerGroupRequest(TeaModel):
    def __init__(
        self,
        consumer_id: str = None,
        instance_id: str = None,
        region_id: str = None,
        remark: str = None,
        tag: List[CreateConsumerGroupRequestTag] = None,
    ):
        # The name of the consumer group.
        # 
        # *   The value can contain only letters, digits, hyphens (-), and underscores (_), and the value must contain at least one letter or digit.
        # *   The value must be 3 to 128 characters in length. If the value that you specify contains more than 128 characters, the system automatically truncates the value to 128 characters.
        # *   After a consumer group is created, you cannot change the name of the consumer group.
        # 
        # This parameter is required.
        self.consumer_id = consumer_id
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The region ID of the instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The description of the consumer group.
        self.remark = remark
        # The tags.
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consumer_id is not None:
            result['ConsumerId'] = self.consumer_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.remark is not None:
            result['Remark'] = self.remark
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsumerId') is not None:
            self.consumer_id = m.get('ConsumerId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateConsumerGroupRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class CreateConsumerGroupResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code returned. The HTTP status code 200 indicates that the request is successful.
        self.code = code
        # The message returned.
        self.message = message
        # The ID of the request.
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
            result['Code'] = self.code
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
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


class CreatePostPayOrderRequestServerlessConfig(TeaModel):
    def __init__(
        self,
        reserved_publish_capacity: int = None,
        reserved_subscribe_capacity: int = None,
    ):
        # The reserved capacity for publishing messages. You can specify only an integer for this parameter. Minimum value: 60.
        # 
        # >  The actual maximum reserved capacity for publishing messages varies based on available resources in the region. The actual range displayed on the buy page shall prevail.
        self.reserved_publish_capacity = reserved_publish_capacity
        # The reserved capacity for subscribing to messages. You can specify only an integer for this parameter. Minimum value: 20.
        # 
        # >  The actual maximum reserved capacity for subscribing to messages varies based on available resources in the region. The actual range displayed on the buy page shall prevail.
        self.reserved_subscribe_capacity = reserved_subscribe_capacity

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.reserved_publish_capacity is not None:
            result['ReservedPublishCapacity'] = self.reserved_publish_capacity
        if self.reserved_subscribe_capacity is not None:
            result['ReservedSubscribeCapacity'] = self.reserved_subscribe_capacity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReservedPublishCapacity') is not None:
            self.reserved_publish_capacity = m.get('ReservedPublishCapacity')
        if m.get('ReservedSubscribeCapacity') is not None:
            self.reserved_subscribe_capacity = m.get('ReservedSubscribeCapacity')
        return self


class CreatePostPayOrderRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N.
        # 
        # *   Valid values of N: 1 to 20.
        # *   If this parameter is left empty, the keys of all tags are matched.
        # *   The tag key must be up to 128 characters in length. It cannot start with acs: or aliyun or contain [http:// or https://.](http://https://。)
        # 
        # This parameter is required.
        self.key = key
        # The value of tag N.
        # 
        # *   Valid values of N: 1 to 20.
        # *   If you do not specify a tag key, you cannot specify a tag value. If this parameter is not configured, all tag values are matched.
        # *   The tag value must be 1 to 128 characters in length. It cannot start with acs: or aliyun or contain [http:// or https://.](http://https://。)
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreatePostPayOrderRequest(TeaModel):
    def __init__(
        self,
        deploy_type: int = None,
        disk_size: int = None,
        disk_type: str = None,
        eip_max: int = None,
        io_max: int = None,
        io_max_spec: str = None,
        paid_type: int = None,
        partition_num: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        serverless_config: CreatePostPayOrderRequestServerlessConfig = None,
        spec_type: str = None,
        tag: List[CreatePostPayOrderRequestTag] = None,
        topic_quota: int = None,
    ):
        # The deployment mode of the instance. Valid values:
        # 
        # *   **4**: deploys the instance that allows access from the Internet and a VPC.
        # *   **5**: deploys the instance that allows access only from a VPC.
        # 
        # This parameter is required.
        self.deploy_type = deploy_type
        # The disk size.
        # 
        # For information about the valid values of this parameter, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        # 
        # >  If you create a serverless ApsaraMQ for Kafka V3 instance, you do not need to configure this parameter.
        self.disk_size = disk_size
        # The disk type. Valid values:
        # 
        # *   **0**: ultra disk
        # *   **1**: standard SSD
        # 
        # >  If you create a serverless ApsaraMQ for Kafka V3 instance, you do not need to configure this parameter.
        self.disk_type = disk_type
        # The maximum Internet traffic in the instance.
        # 
        # *   If you set **DeployType** to **4**, you must configure this parameter.
        # *   For information about the valid values of this parameter, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        # 
        # >  If you create a serverless ApsaraMQ for Kafka V3 instance, you do not need to configure this parameter.
        self.eip_max = eip_max
        # The maximum traffic in the instance. We recommend that you do not configure this parameter.
        # 
        # *   You must configure at least one of IoMax and IoMaxSpec. If you configure both parameters, the value of IoMaxSpec takes effect. We recommend that you configure only IoMaxSpec.
        # *   For information about the valid values of this parameter, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        # 
        # >  If you create a serverless ApsaraMQ for Kafka V3 instance, you do not need to configure this parameter.
        self.io_max = io_max
        # The traffic specification of the instance. We recommend that you configure this parameter.
        # 
        # *   You must configure at least one of IoMax and IoMaxSpec. If you configure both parameters, the value of IoMaxSpec takes effect. We recommend that you configure only IoMaxSpec.
        # *   For information about the valid values of this parameter, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        # 
        # >  If you create a serverless ApsaraMQ for Kafka V3 instance, you do not need to configure this parameter.
        self.io_max_spec = io_max_spec
        # The billing method of the instance. Valid values:
        # 
        # *   1: the pay-as-you-go billing method for ApsaraMQ for Kafka V2 instances.
        # *   3: the pay-as-you-go billing method for serverless ApsaraMQ for Kafka V3 instances.
        self.paid_type = paid_type
        # The number of partitions. We recommend that you configure this parameter.
        # 
        # *   You must configure one of PartitionNum and TopicQuota. We recommend that you configure only ParittionNum.
        # *   If you configure PartitionNum and TopicQuota at the same time, the system verifies whether the price of the partitions equals the price of the topics based on the previous topic-based selling mode. If the price of the partitions does not equal the price of the topics, an error is returned. If the price of the partitions equals the price of the topics, the instance is purchased based on the partition number.
        # *   For information about the valid values of this parameter, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        # 
        # >  If you create a serverless ApsaraMQ for Kafka V3 instance, you do not need to configure this parameter.
        self.partition_num = partition_num
        # The region ID of the instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group.
        # 
        # If this parameter is left empty, the default resource group is used. You can view the resource group ID on the Resource Group page in the Resource Management console.
        self.resource_group_id = resource_group_id
        # The parameters configured for the serverless ApsaraMQ for Kafka V3 instance. When you create a Serverless ApsaraMQ for Kafka V3 serverless instance, you must configure these parameters.
        self.serverless_config = serverless_config
        # The instance edition.
        # 
        # Valid values if you set PaidType to 1:
        # 
        # *   normal: Standard Edition (High Write)
        # *   professional: Professional Edition (High Write)
        # *   professionalForHighRead: Professional Edition (High Read)
        # 
        # Valid values if you set PaidType to 3:
        # 
        # *   normal: Serverless Standard Edition
        # 
        # For more information about the instance editions, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        self.spec_type = spec_type
        # The tags.
        self.tag = tag
        # The number of topics. We recommend that you do not configure this parameter.
        # 
        # *   You must configure one of PartitionNum and TopicQuota. We recommend that you configure only ParittionNum.
        # *   If you configure PartitionNum and TopicQuota at the same time, the system verifies whether the price of the partitions equals the price of the topics based on the previous topic-based selling mode. If the price of the partitions does not equal the price of the topics, an error is returned. If the price of the partitions equals the price of the topics, the instance is purchased based on the partition number.
        # *   The default value of TopicQuota varies based on the value of IoMaxSpec. If the number of topics that you consume exceeds the default value, you are charged additional fees.
        # *   For information about the valid values of this parameter, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        # 
        # >  If you create a serverless ApsaraMQ for Kafka V3 instance, you do not need to configure this parameter.
        self.topic_quota = topic_quota

    def validate(self):
        if self.serverless_config:
            self.serverless_config.validate()
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deploy_type is not None:
            result['DeployType'] = self.deploy_type
        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size
        if self.disk_type is not None:
            result['DiskType'] = self.disk_type
        if self.eip_max is not None:
            result['EipMax'] = self.eip_max
        if self.io_max is not None:
            result['IoMax'] = self.io_max
        if self.io_max_spec is not None:
            result['IoMaxSpec'] = self.io_max_spec
        if self.paid_type is not None:
            result['PaidType'] = self.paid_type
        if self.partition_num is not None:
            result['PartitionNum'] = self.partition_num
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.serverless_config is not None:
            result['ServerlessConfig'] = self.serverless_config.to_map()
        if self.spec_type is not None:
            result['SpecType'] = self.spec_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.topic_quota is not None:
            result['TopicQuota'] = self.topic_quota
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeployType') is not None:
            self.deploy_type = m.get('DeployType')
        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')
        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')
        if m.get('EipMax') is not None:
            self.eip_max = m.get('EipMax')
        if m.get('IoMax') is not None:
            self.io_max = m.get('IoMax')
        if m.get('IoMaxSpec') is not None:
            self.io_max_spec = m.get('IoMaxSpec')
        if m.get('PaidType') is not None:
            self.paid_type = m.get('PaidType')
        if m.get('PartitionNum') is not None:
            self.partition_num = m.get('PartitionNum')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ServerlessConfig') is not None:
            temp_model = CreatePostPayOrderRequestServerlessConfig()
            self.serverless_config = temp_model.from_map(m['ServerlessConfig'])
        if m.get('SpecType') is not None:
            self.spec_type = m.get('SpecType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreatePostPayOrderRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('TopicQuota') is not None:
            self.topic_quota = m.get('TopicQuota')
        return self


class CreatePostPayOrderShrinkRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N.
        # 
        # *   Valid values of N: 1 to 20.
        # *   If this parameter is left empty, the keys of all tags are matched.
        # *   The tag key must be up to 128 characters in length. It cannot start with acs: or aliyun or contain [http:// or https://.](http://https://。)
        # 
        # This parameter is required.
        self.key = key
        # The value of tag N.
        # 
        # *   Valid values of N: 1 to 20.
        # *   If you do not specify a tag key, you cannot specify a tag value. If this parameter is not configured, all tag values are matched.
        # *   The tag value must be 1 to 128 characters in length. It cannot start with acs: or aliyun or contain [http:// or https://.](http://https://。)
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreatePostPayOrderShrinkRequest(TeaModel):
    def __init__(
        self,
        deploy_type: int = None,
        disk_size: int = None,
        disk_type: str = None,
        eip_max: int = None,
        io_max: int = None,
        io_max_spec: str = None,
        paid_type: int = None,
        partition_num: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        serverless_config_shrink: str = None,
        spec_type: str = None,
        tag: List[CreatePostPayOrderShrinkRequestTag] = None,
        topic_quota: int = None,
    ):
        # The deployment mode of the instance. Valid values:
        # 
        # *   **4**: deploys the instance that allows access from the Internet and a VPC.
        # *   **5**: deploys the instance that allows access only from a VPC.
        # 
        # This parameter is required.
        self.deploy_type = deploy_type
        # The disk size.
        # 
        # For information about the valid values of this parameter, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        # 
        # >  If you create a serverless ApsaraMQ for Kafka V3 instance, you do not need to configure this parameter.
        self.disk_size = disk_size
        # The disk type. Valid values:
        # 
        # *   **0**: ultra disk
        # *   **1**: standard SSD
        # 
        # >  If you create a serverless ApsaraMQ for Kafka V3 instance, you do not need to configure this parameter.
        self.disk_type = disk_type
        # The maximum Internet traffic in the instance.
        # 
        # *   If you set **DeployType** to **4**, you must configure this parameter.
        # *   For information about the valid values of this parameter, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        # 
        # >  If you create a serverless ApsaraMQ for Kafka V3 instance, you do not need to configure this parameter.
        self.eip_max = eip_max
        # The maximum traffic in the instance. We recommend that you do not configure this parameter.
        # 
        # *   You must configure at least one of IoMax and IoMaxSpec. If you configure both parameters, the value of IoMaxSpec takes effect. We recommend that you configure only IoMaxSpec.
        # *   For information about the valid values of this parameter, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        # 
        # >  If you create a serverless ApsaraMQ for Kafka V3 instance, you do not need to configure this parameter.
        self.io_max = io_max
        # The traffic specification of the instance. We recommend that you configure this parameter.
        # 
        # *   You must configure at least one of IoMax and IoMaxSpec. If you configure both parameters, the value of IoMaxSpec takes effect. We recommend that you configure only IoMaxSpec.
        # *   For information about the valid values of this parameter, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        # 
        # >  If you create a serverless ApsaraMQ for Kafka V3 instance, you do not need to configure this parameter.
        self.io_max_spec = io_max_spec
        # The billing method of the instance. Valid values:
        # 
        # *   1: the pay-as-you-go billing method for ApsaraMQ for Kafka V2 instances.
        # *   3: the pay-as-you-go billing method for serverless ApsaraMQ for Kafka V3 instances.
        self.paid_type = paid_type
        # The number of partitions. We recommend that you configure this parameter.
        # 
        # *   You must configure one of PartitionNum and TopicQuota. We recommend that you configure only ParittionNum.
        # *   If you configure PartitionNum and TopicQuota at the same time, the system verifies whether the price of the partitions equals the price of the topics based on the previous topic-based selling mode. If the price of the partitions does not equal the price of the topics, an error is returned. If the price of the partitions equals the price of the topics, the instance is purchased based on the partition number.
        # *   For information about the valid values of this parameter, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        # 
        # >  If you create a serverless ApsaraMQ for Kafka V3 instance, you do not need to configure this parameter.
        self.partition_num = partition_num
        # The region ID of the instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group.
        # 
        # If this parameter is left empty, the default resource group is used. You can view the resource group ID on the Resource Group page in the Resource Management console.
        self.resource_group_id = resource_group_id
        # The parameters configured for the serverless ApsaraMQ for Kafka V3 instance. When you create a Serverless ApsaraMQ for Kafka V3 serverless instance, you must configure these parameters.
        self.serverless_config_shrink = serverless_config_shrink
        # The instance edition.
        # 
        # Valid values if you set PaidType to 1:
        # 
        # *   normal: Standard Edition (High Write)
        # *   professional: Professional Edition (High Write)
        # *   professionalForHighRead: Professional Edition (High Read)
        # 
        # Valid values if you set PaidType to 3:
        # 
        # *   normal: Serverless Standard Edition
        # 
        # For more information about the instance editions, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        self.spec_type = spec_type
        # The tags.
        self.tag = tag
        # The number of topics. We recommend that you do not configure this parameter.
        # 
        # *   You must configure one of PartitionNum and TopicQuota. We recommend that you configure only ParittionNum.
        # *   If you configure PartitionNum and TopicQuota at the same time, the system verifies whether the price of the partitions equals the price of the topics based on the previous topic-based selling mode. If the price of the partitions does not equal the price of the topics, an error is returned. If the price of the partitions equals the price of the topics, the instance is purchased based on the partition number.
        # *   The default value of TopicQuota varies based on the value of IoMaxSpec. If the number of topics that you consume exceeds the default value, you are charged additional fees.
        # *   For information about the valid values of this parameter, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        # 
        # >  If you create a serverless ApsaraMQ for Kafka V3 instance, you do not need to configure this parameter.
        self.topic_quota = topic_quota

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deploy_type is not None:
            result['DeployType'] = self.deploy_type
        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size
        if self.disk_type is not None:
            result['DiskType'] = self.disk_type
        if self.eip_max is not None:
            result['EipMax'] = self.eip_max
        if self.io_max is not None:
            result['IoMax'] = self.io_max
        if self.io_max_spec is not None:
            result['IoMaxSpec'] = self.io_max_spec
        if self.paid_type is not None:
            result['PaidType'] = self.paid_type
        if self.partition_num is not None:
            result['PartitionNum'] = self.partition_num
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.serverless_config_shrink is not None:
            result['ServerlessConfig'] = self.serverless_config_shrink
        if self.spec_type is not None:
            result['SpecType'] = self.spec_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.topic_quota is not None:
            result['TopicQuota'] = self.topic_quota
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeployType') is not None:
            self.deploy_type = m.get('DeployType')
        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')
        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')
        if m.get('EipMax') is not None:
            self.eip_max = m.get('EipMax')
        if m.get('IoMax') is not None:
            self.io_max = m.get('IoMax')
        if m.get('IoMaxSpec') is not None:
            self.io_max_spec = m.get('IoMaxSpec')
        if m.get('PaidType') is not None:
            self.paid_type = m.get('PaidType')
        if m.get('PartitionNum') is not None:
            self.partition_num = m.get('PartitionNum')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ServerlessConfig') is not None:
            self.serverless_config_shrink = m.get('ServerlessConfig')
        if m.get('SpecType') is not None:
            self.spec_type = m.get('SpecType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreatePostPayOrderShrinkRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('TopicQuota') is not None:
            self.topic_quota = m.get('TopicQuota')
        return self


class CreatePostPayOrderResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        order_id: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code returned. The HTTP status code 200 indicates that the request is successful.
        self.code = code
        # The message returned.
        self.message = message
        # The ID of the order.
        self.order_id = order_id
        # The ID of the request.
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
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreatePostPayOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreatePostPayOrderResponseBody = None,
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
            temp_model = CreatePostPayOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePrePayOrderRequestConfluentConfig(TeaModel):
    def __init__(
        self,
        connect_cu: int = None,
        connect_replica: int = None,
        control_center_cu: int = None,
        control_center_replica: int = None,
        control_center_storage: int = None,
        kafka_cu: int = None,
        kafka_replica: int = None,
        kafka_rest_proxy_cu: int = None,
        kafka_rest_proxy_replica: int = None,
        kafka_storage: int = None,
        ksql_cu: int = None,
        ksql_replica: int = None,
        ksql_storage: int = None,
        schema_registry_cu: int = None,
        schema_registry_replica: int = None,
        zoo_keeper_cu: int = None,
        zoo_keeper_replica: int = None,
        zoo_keeper_storage: int = None,
    ):
        # The number of CPU cores of Connect.
        self.connect_cu = connect_cu
        # The number of replicas of Connect.
        self.connect_replica = connect_replica
        # The number of CPU cores of Control Center.
        self.control_center_cu = control_center_cu
        # The number of replicas of Control Center.
        self.control_center_replica = control_center_replica
        # The disk capacity of Control Center. Unit: GB
        self.control_center_storage = control_center_storage
        # The number of CPU cores of the Kafka broker.
        self.kafka_cu = kafka_cu
        # The number of replicas of the Kafka broker.
        self.kafka_replica = kafka_replica
        # The number of CPU cores of Kafka Rest Proxy.
        self.kafka_rest_proxy_cu = kafka_rest_proxy_cu
        # The number of replicas of Kafka Rest Proxy.
        self.kafka_rest_proxy_replica = kafka_rest_proxy_replica
        # The disk capacity of the Kafka broker. Unit: GB
        self.kafka_storage = kafka_storage
        # The number of CPU cores of ksqIDB.
        self.ksql_cu = ksql_cu
        # The number of replicas of ksqlDB.
        self.ksql_replica = ksql_replica
        # The disk capacity of ksqlDB. Unit: GB
        self.ksql_storage = ksql_storage
        # The number of CPU cores of Schema Registry.
        self.schema_registry_cu = schema_registry_cu
        # The number of replicas of Schema Registry.
        self.schema_registry_replica = schema_registry_replica
        # The number of CPU cores of ZooKeeper.
        self.zoo_keeper_cu = zoo_keeper_cu
        # The number of replicas of ZooKeeper.
        self.zoo_keeper_replica = zoo_keeper_replica
        # The disk capacity of ZooKeeper. Unit: GB
        self.zoo_keeper_storage = zoo_keeper_storage

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connect_cu is not None:
            result['ConnectCU'] = self.connect_cu
        if self.connect_replica is not None:
            result['ConnectReplica'] = self.connect_replica
        if self.control_center_cu is not None:
            result['ControlCenterCU'] = self.control_center_cu
        if self.control_center_replica is not None:
            result['ControlCenterReplica'] = self.control_center_replica
        if self.control_center_storage is not None:
            result['ControlCenterStorage'] = self.control_center_storage
        if self.kafka_cu is not None:
            result['KafkaCU'] = self.kafka_cu
        if self.kafka_replica is not None:
            result['KafkaReplica'] = self.kafka_replica
        if self.kafka_rest_proxy_cu is not None:
            result['KafkaRestProxyCU'] = self.kafka_rest_proxy_cu
        if self.kafka_rest_proxy_replica is not None:
            result['KafkaRestProxyReplica'] = self.kafka_rest_proxy_replica
        if self.kafka_storage is not None:
            result['KafkaStorage'] = self.kafka_storage
        if self.ksql_cu is not None:
            result['KsqlCU'] = self.ksql_cu
        if self.ksql_replica is not None:
            result['KsqlReplica'] = self.ksql_replica
        if self.ksql_storage is not None:
            result['KsqlStorage'] = self.ksql_storage
        if self.schema_registry_cu is not None:
            result['SchemaRegistryCU'] = self.schema_registry_cu
        if self.schema_registry_replica is not None:
            result['SchemaRegistryReplica'] = self.schema_registry_replica
        if self.zoo_keeper_cu is not None:
            result['ZooKeeperCU'] = self.zoo_keeper_cu
        if self.zoo_keeper_replica is not None:
            result['ZooKeeperReplica'] = self.zoo_keeper_replica
        if self.zoo_keeper_storage is not None:
            result['ZooKeeperStorage'] = self.zoo_keeper_storage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectCU') is not None:
            self.connect_cu = m.get('ConnectCU')
        if m.get('ConnectReplica') is not None:
            self.connect_replica = m.get('ConnectReplica')
        if m.get('ControlCenterCU') is not None:
            self.control_center_cu = m.get('ControlCenterCU')
        if m.get('ControlCenterReplica') is not None:
            self.control_center_replica = m.get('ControlCenterReplica')
        if m.get('ControlCenterStorage') is not None:
            self.control_center_storage = m.get('ControlCenterStorage')
        if m.get('KafkaCU') is not None:
            self.kafka_cu = m.get('KafkaCU')
        if m.get('KafkaReplica') is not None:
            self.kafka_replica = m.get('KafkaReplica')
        if m.get('KafkaRestProxyCU') is not None:
            self.kafka_rest_proxy_cu = m.get('KafkaRestProxyCU')
        if m.get('KafkaRestProxyReplica') is not None:
            self.kafka_rest_proxy_replica = m.get('KafkaRestProxyReplica')
        if m.get('KafkaStorage') is not None:
            self.kafka_storage = m.get('KafkaStorage')
        if m.get('KsqlCU') is not None:
            self.ksql_cu = m.get('KsqlCU')
        if m.get('KsqlReplica') is not None:
            self.ksql_replica = m.get('KsqlReplica')
        if m.get('KsqlStorage') is not None:
            self.ksql_storage = m.get('KsqlStorage')
        if m.get('SchemaRegistryCU') is not None:
            self.schema_registry_cu = m.get('SchemaRegistryCU')
        if m.get('SchemaRegistryReplica') is not None:
            self.schema_registry_replica = m.get('SchemaRegistryReplica')
        if m.get('ZooKeeperCU') is not None:
            self.zoo_keeper_cu = m.get('ZooKeeperCU')
        if m.get('ZooKeeperReplica') is not None:
            self.zoo_keeper_replica = m.get('ZooKeeperReplica')
        if m.get('ZooKeeperStorage') is not None:
            self.zoo_keeper_storage = m.get('ZooKeeperStorage')
        return self


class CreatePrePayOrderRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N.
        # 
        # *   Valid values of N: 1 to 20.
        # *   If this parameter is left empty, the keys of all tags are matched.
        # *   The tag key can be up to 128 characters in length and cannot start with acs: or aliyun or contain [http:// or https://.](http://https://。)
        # 
        # This parameter is required.
        self.key = key
        # The value of tag N.
        # 
        # *   Valid values of N: 1 to 20.
        # *   This parameter can be left empty.
        # *   The tag value can be 1 to 128 characters in length and cannot start with acs: or aliyun or contain [http:// or https://.](http://https://。)
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreatePrePayOrderRequest(TeaModel):
    def __init__(
        self,
        confluent_config: CreatePrePayOrderRequestConfluentConfig = None,
        deploy_type: int = None,
        disk_size: int = None,
        disk_type: str = None,
        duration: int = None,
        eip_max: int = None,
        io_max: int = None,
        io_max_spec: str = None,
        paid_type: int = None,
        partition_num: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        spec_type: str = None,
        tag: List[CreatePrePayOrderRequestTag] = None,
        topic_quota: int = None,
    ):
        # The configurations of Confluent.
        # 
        # >  When you create an ApsaraMQ for Confluent instance, you must configure this parameter.
        self.confluent_config = confluent_config
        # The type of the network in which the instance is deployed. Valid values:
        # 
        # *   **4**: Internet and virtual private cloud (VPC)
        # *   **5**: VPC
        # 
        # >  If you create an ApsaraMQ for Confluent instance, set the value to 5. After the instance is created, you can specify whether to enable each component.
        self.deploy_type = deploy_type
        # The disk size. Unit: GB
        # 
        # For information about the valid values of this parameter, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        # 
        # >  If you create an ApsaraMQ for Confluent instance, you do not need to configure this parameter.
        self.disk_size = disk_size
        # The disk type. Valid values:
        # 
        # *   **0**: ultra disk
        # *   **1**: standard SSD
        # 
        # >  If you create an ApsaraMQ for Confluent instance, you do not need to configure this parameter.
        self.disk_type = disk_type
        # The subscription duration. Unit: months. Default value: 1. Valid values:
        # 
        # *   **1 to 12**\
        self.duration = duration
        # The maximum Internet traffic in the instance.
        # 
        # *   If you set **DeployType** to **4**, you must configure this parameter.
        # *   For information about the valid values, see [Pay-as-you-go](https://help.aliyun.com/document_detail/72142.html).
        # 
        # >  If you create an ApsaraMQ for Confluent instance, you do not need to configure this parameter.
        self.eip_max = eip_max
        # The maximum traffic in the instance. We recommend that you do not configure this parameter.
        # 
        # *   You must set one of **IoMax** and **IoMaxSpec**. If both parameters are configured, the value of **IoMaxSpec** is used. We recommend that you configure only **IoMaxSpec**.
        # *   For information about the valid values of this parameter, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        # 
        # >  If you create an ApsaraMQ for Confluent instance, you do not need to configure this parameter.
        self.io_max = io_max
        # The traffic specification of the instance. We recommend that you configure this parameter.
        # 
        # *   You must configure one of **IoMax** and **IoMaxSpec**. If both parameters are configured, the value of **IoMaxSpec** is used. We recommend that you configure only **IoMaxSpec**.
        # *   For more information about the valid values of this parameter, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        # 
        # >  If you create an ApsaraMQ for Confluent instance, you do not need to configure this parameter.
        self.io_max_spec = io_max_spec
        # The billing method of the instance. Valid values:
        # 
        # *   **0**: the subscription billing method
        # *   **4**: the subscription billing method for ApsaraMQ for Confluent instances
        self.paid_type = paid_type
        # The number of partitions. We recommend that you configure this parameter.
        # 
        # *   You must configure one of PartitionNum and TopicQuota. We recommend that you configure only PartitionNum.
        # *   If you configure PartitionNum and TopicQuota at the same time, the system verifies whether the price of the partitions equals the price of the topics based on the previous topic-based selling mode. If the price of the partitions does not equal the price of the topics, an error is returned. If the price of the partitions equals the price of the topics, the instance is purchased based on the partition number.
        # *   For information about the valid values of this parameter, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        # 
        # >  If you create an ApsaraMQ for Confluent instance, you do not need to configure this parameter.
        self.partition_num = partition_num
        # The region ID of the instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group.
        # 
        # If this parameter is left empty, the default resource group is used. You can view the resource group ID on the Resource Group page in the Resource Management console.
        self.resource_group_id = resource_group_id
        # The instance edition. Valid values:
        # 
        # *   **normal**: Standard Edition (High Write)
        # *   **professional**: Professional Edition (High Write)
        # *   **professionalForHighRead**: Professional Edition (High Read)
        # 
        # For more information, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        # 
        # >  If you create an ApsaraMQ for Confluent instance, you do not need to configure this parameter.
        self.spec_type = spec_type
        # The tags.
        self.tag = tag
        # The number of topics. We recommend that you do not configure this parameter.
        # 
        # *   You must configure one of PartitionNum and TopicQuota. We recommend that you configure only PartitionNum.
        # *   If you configure PartitionNum and TopicQuota at the same time, the system verifies whether the price of the partitions equals the price of the topics based on the previous topic-based selling mode. If the price of the partitions does not equal the price of the topics, an error is returned. If the price of the partitions equals the price of the topics, the instance is purchased based on the partition number.
        # *   The default value of TopicQuota varies based on the value of IoMaxSpec. If the number of topics that you use exceeds the default value, you are charged additional fees.
        # *   For information about the valid values of this parameter, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        # 
        # >  If you create an ApsaraMQ for Confluent instance, you do not need to configure this parameter.
        self.topic_quota = topic_quota

    def validate(self):
        if self.confluent_config:
            self.confluent_config.validate()
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.confluent_config is not None:
            result['ConfluentConfig'] = self.confluent_config.to_map()
        if self.deploy_type is not None:
            result['DeployType'] = self.deploy_type
        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size
        if self.disk_type is not None:
            result['DiskType'] = self.disk_type
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.eip_max is not None:
            result['EipMax'] = self.eip_max
        if self.io_max is not None:
            result['IoMax'] = self.io_max
        if self.io_max_spec is not None:
            result['IoMaxSpec'] = self.io_max_spec
        if self.paid_type is not None:
            result['PaidType'] = self.paid_type
        if self.partition_num is not None:
            result['PartitionNum'] = self.partition_num
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.spec_type is not None:
            result['SpecType'] = self.spec_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.topic_quota is not None:
            result['TopicQuota'] = self.topic_quota
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfluentConfig') is not None:
            temp_model = CreatePrePayOrderRequestConfluentConfig()
            self.confluent_config = temp_model.from_map(m['ConfluentConfig'])
        if m.get('DeployType') is not None:
            self.deploy_type = m.get('DeployType')
        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')
        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('EipMax') is not None:
            self.eip_max = m.get('EipMax')
        if m.get('IoMax') is not None:
            self.io_max = m.get('IoMax')
        if m.get('IoMaxSpec') is not None:
            self.io_max_spec = m.get('IoMaxSpec')
        if m.get('PaidType') is not None:
            self.paid_type = m.get('PaidType')
        if m.get('PartitionNum') is not None:
            self.partition_num = m.get('PartitionNum')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SpecType') is not None:
            self.spec_type = m.get('SpecType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreatePrePayOrderRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('TopicQuota') is not None:
            self.topic_quota = m.get('TopicQuota')
        return self


class CreatePrePayOrderShrinkRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N.
        # 
        # *   Valid values of N: 1 to 20.
        # *   If this parameter is left empty, the keys of all tags are matched.
        # *   The tag key can be up to 128 characters in length and cannot start with acs: or aliyun or contain [http:// or https://.](http://https://。)
        # 
        # This parameter is required.
        self.key = key
        # The value of tag N.
        # 
        # *   Valid values of N: 1 to 20.
        # *   This parameter can be left empty.
        # *   The tag value can be 1 to 128 characters in length and cannot start with acs: or aliyun or contain [http:// or https://.](http://https://。)
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreatePrePayOrderShrinkRequest(TeaModel):
    def __init__(
        self,
        confluent_config_shrink: str = None,
        deploy_type: int = None,
        disk_size: int = None,
        disk_type: str = None,
        duration: int = None,
        eip_max: int = None,
        io_max: int = None,
        io_max_spec: str = None,
        paid_type: int = None,
        partition_num: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        spec_type: str = None,
        tag: List[CreatePrePayOrderShrinkRequestTag] = None,
        topic_quota: int = None,
    ):
        # The configurations of Confluent.
        # 
        # >  When you create an ApsaraMQ for Confluent instance, you must configure this parameter.
        self.confluent_config_shrink = confluent_config_shrink
        # The type of the network in which the instance is deployed. Valid values:
        # 
        # *   **4**: Internet and virtual private cloud (VPC)
        # *   **5**: VPC
        # 
        # >  If you create an ApsaraMQ for Confluent instance, set the value to 5. After the instance is created, you can specify whether to enable each component.
        self.deploy_type = deploy_type
        # The disk size. Unit: GB
        # 
        # For information about the valid values of this parameter, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        # 
        # >  If you create an ApsaraMQ for Confluent instance, you do not need to configure this parameter.
        self.disk_size = disk_size
        # The disk type. Valid values:
        # 
        # *   **0**: ultra disk
        # *   **1**: standard SSD
        # 
        # >  If you create an ApsaraMQ for Confluent instance, you do not need to configure this parameter.
        self.disk_type = disk_type
        # The subscription duration. Unit: months. Default value: 1. Valid values:
        # 
        # *   **1 to 12**\
        self.duration = duration
        # The maximum Internet traffic in the instance.
        # 
        # *   If you set **DeployType** to **4**, you must configure this parameter.
        # *   For information about the valid values, see [Pay-as-you-go](https://help.aliyun.com/document_detail/72142.html).
        # 
        # >  If you create an ApsaraMQ for Confluent instance, you do not need to configure this parameter.
        self.eip_max = eip_max
        # The maximum traffic in the instance. We recommend that you do not configure this parameter.
        # 
        # *   You must set one of **IoMax** and **IoMaxSpec**. If both parameters are configured, the value of **IoMaxSpec** is used. We recommend that you configure only **IoMaxSpec**.
        # *   For information about the valid values of this parameter, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        # 
        # >  If you create an ApsaraMQ for Confluent instance, you do not need to configure this parameter.
        self.io_max = io_max
        # The traffic specification of the instance. We recommend that you configure this parameter.
        # 
        # *   You must configure one of **IoMax** and **IoMaxSpec**. If both parameters are configured, the value of **IoMaxSpec** is used. We recommend that you configure only **IoMaxSpec**.
        # *   For more information about the valid values of this parameter, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        # 
        # >  If you create an ApsaraMQ for Confluent instance, you do not need to configure this parameter.
        self.io_max_spec = io_max_spec
        # The billing method of the instance. Valid values:
        # 
        # *   **0**: the subscription billing method
        # *   **4**: the subscription billing method for ApsaraMQ for Confluent instances
        self.paid_type = paid_type
        # The number of partitions. We recommend that you configure this parameter.
        # 
        # *   You must configure one of PartitionNum and TopicQuota. We recommend that you configure only PartitionNum.
        # *   If you configure PartitionNum and TopicQuota at the same time, the system verifies whether the price of the partitions equals the price of the topics based on the previous topic-based selling mode. If the price of the partitions does not equal the price of the topics, an error is returned. If the price of the partitions equals the price of the topics, the instance is purchased based on the partition number.
        # *   For information about the valid values of this parameter, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        # 
        # >  If you create an ApsaraMQ for Confluent instance, you do not need to configure this parameter.
        self.partition_num = partition_num
        # The region ID of the instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group.
        # 
        # If this parameter is left empty, the default resource group is used. You can view the resource group ID on the Resource Group page in the Resource Management console.
        self.resource_group_id = resource_group_id
        # The instance edition. Valid values:
        # 
        # *   **normal**: Standard Edition (High Write)
        # *   **professional**: Professional Edition (High Write)
        # *   **professionalForHighRead**: Professional Edition (High Read)
        # 
        # For more information, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        # 
        # >  If you create an ApsaraMQ for Confluent instance, you do not need to configure this parameter.
        self.spec_type = spec_type
        # The tags.
        self.tag = tag
        # The number of topics. We recommend that you do not configure this parameter.
        # 
        # *   You must configure one of PartitionNum and TopicQuota. We recommend that you configure only PartitionNum.
        # *   If you configure PartitionNum and TopicQuota at the same time, the system verifies whether the price of the partitions equals the price of the topics based on the previous topic-based selling mode. If the price of the partitions does not equal the price of the topics, an error is returned. If the price of the partitions equals the price of the topics, the instance is purchased based on the partition number.
        # *   The default value of TopicQuota varies based on the value of IoMaxSpec. If the number of topics that you use exceeds the default value, you are charged additional fees.
        # *   For information about the valid values of this parameter, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        # 
        # >  If you create an ApsaraMQ for Confluent instance, you do not need to configure this parameter.
        self.topic_quota = topic_quota

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.confluent_config_shrink is not None:
            result['ConfluentConfig'] = self.confluent_config_shrink
        if self.deploy_type is not None:
            result['DeployType'] = self.deploy_type
        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size
        if self.disk_type is not None:
            result['DiskType'] = self.disk_type
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.eip_max is not None:
            result['EipMax'] = self.eip_max
        if self.io_max is not None:
            result['IoMax'] = self.io_max
        if self.io_max_spec is not None:
            result['IoMaxSpec'] = self.io_max_spec
        if self.paid_type is not None:
            result['PaidType'] = self.paid_type
        if self.partition_num is not None:
            result['PartitionNum'] = self.partition_num
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.spec_type is not None:
            result['SpecType'] = self.spec_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.topic_quota is not None:
            result['TopicQuota'] = self.topic_quota
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfluentConfig') is not None:
            self.confluent_config_shrink = m.get('ConfluentConfig')
        if m.get('DeployType') is not None:
            self.deploy_type = m.get('DeployType')
        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')
        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('EipMax') is not None:
            self.eip_max = m.get('EipMax')
        if m.get('IoMax') is not None:
            self.io_max = m.get('IoMax')
        if m.get('IoMaxSpec') is not None:
            self.io_max_spec = m.get('IoMaxSpec')
        if m.get('PaidType') is not None:
            self.paid_type = m.get('PaidType')
        if m.get('PartitionNum') is not None:
            self.partition_num = m.get('PartitionNum')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SpecType') is not None:
            self.spec_type = m.get('SpecType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreatePrePayOrderShrinkRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('TopicQuota') is not None:
            self.topic_quota = m.get('TopicQuota')
        return self


class CreatePrePayOrderResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        order_id: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code returned. The HTTP status code 200 indicates that the request is successful.
        self.code = code
        # The message returned.
        self.message = message
        # The ID of the order.
        self.order_id = order_id
        # The ID of the request.
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
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreatePrePayOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreatePrePayOrderResponseBody = None,
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
            temp_model = CreatePrePayOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSaslUserRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        mechanism: str = None,
        password: str = None,
        region_id: str = None,
        type: str = None,
        username: str = None,
    ):
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The encryption method. Valid values:
        # 
        # *   SCRAM-SHA-512 (default)
        # *   SCRAM-SHA-256
        # 
        # > 
        # 
        # *   This parameter is available only for ApsaraMQ for Kafka V3 serverless instances.
        self.mechanism = mechanism
        # The password of the SASL user.
        # 
        # This parameter is required.
        self.password = password
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The type of the Simple Authentication and Security Layer (SASL) user. Valid values:
        # 
        # *   **plain**: a simple mechanism that uses usernames and passwords to verify user identities. ApsaraMQ for Kafka provides an improved PLAIN mechanism that allows you to dynamically add SASL users without the need to restart an instance.
        # *   **SCRAM**: a mechanism that uses usernames and passwords to verify user identities. Compared with the PLAIN mechanism, this mechanism provides better security protection. ApsaraMQ for Kafka uses the SCRAM-SHA-256 algorithm.
        # *   **LDAP**: This value is available only for the SASL users of ApsaraMQ for Confluent instances.
        # 
        # Default value: **plain**.
        self.type = type
        # The name of the SASL user.
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
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.mechanism is not None:
            result['Mechanism'] = self.mechanism
        if self.password is not None:
            result['Password'] = self.password
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.type is not None:
            result['Type'] = self.type
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Mechanism') is not None:
            self.mechanism = m.get('Mechanism')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class CreateSaslUserResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code returned. The HTTP status code 200 indicates that the request is successful.
        self.code = code
        # The returned message.
        self.message = message
        # The ID of the request.
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
            result['Code'] = self.code
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateSaslUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateSaslUserResponseBody = None,
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
            temp_model = CreateSaslUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateScheduledScalingRuleRequest(TeaModel):
    def __init__(
        self,
        duration_minutes: int = None,
        enable: bool = None,
        first_scheduled_time: int = None,
        instance_id: str = None,
        region_id: str = None,
        repeat_type: str = None,
        reserved_pub_flow: int = None,
        reserved_sub_flow: int = None,
        rule_name: str = None,
        schedule_type: str = None,
        time_zone: str = None,
        weekly_types: List[str] = None,
    ):
        # The duration of each scheduled scaling task. Unit: minutes.
        # 
        # >  The value of this parameter must be greater than or equal to 15.
        # 
        # This parameter is required.
        self.duration_minutes = duration_minutes
        # Specifies whether to enable the scheduled scaling rule. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.enable = enable
        # The time when the scheduled scaling task is executed.
        # 
        # If you set ScheduleType to at, make sure that the value of this parameter is at least 30 minutes later than the current point in time.
        # 
        # >Notice: To prevent the broker from repeatedly executing instance upgrade and downgrade tasks, make sure that the interval between two consecutive scheduled scaling tasks is at least 60 minutes.
        # 
        # This parameter is required.
        self.first_scheduled_time = first_scheduled_time
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the region where the instance resides.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The frequency to execute the scheduled scaling task. This parameter is required only if you set ScheduleType to repeat. Valid values:
        # 
        # *   Daily: The scheduled scaling task is executed every day.
        # 
        # *   Weekly: The scheduled scaling task is executed every week.
        self.repeat_type = repeat_type
        # The reserved production capacity for scheduled scaling. Unit: MB/s.
        # 
        # >  You must specify a higher value than the instance specification for at least one of ReservedPubFlow and ReservedSubFlow.
        # 
        # This parameter is required.
        self.reserved_pub_flow = reserved_pub_flow
        # The reserved consumption capacity for scheduled scaling. Unit: MB/s.
        # 
        # >  You must specify a higher value than the instance specification for at least one of ReservedPubFlow and ReservedSubFlow.
        # 
        # This parameter is required.
        self.reserved_sub_flow = reserved_sub_flow
        # The name of the scheduled scaling rule.
        # 
        # >  The name of the scheduled scaling rule cannot be the same as the names of other rules for the instance.
        # 
        # This parameter is required.
        self.rule_name = rule_name
        # The type of the scheduled scaling task. Valid values:
        # 
        # *   at: The scheduled scaling task is executed only once.
        # *   repeat: The scheduled scaling task is repeatedly executed.
        # 
        # This parameter is required.
        self.schedule_type = schedule_type
        # The time zone in Coordinated Universal Time (UTC).
        # 
        # This parameter is required.
        self.time_zone = time_zone
        # The day on which the scheduled scaling task is executed every week. You can specify multiple days.
        self.weekly_types = weekly_types

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration_minutes is not None:
            result['DurationMinutes'] = self.duration_minutes
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.first_scheduled_time is not None:
            result['FirstScheduledTime'] = self.first_scheduled_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.repeat_type is not None:
            result['RepeatType'] = self.repeat_type
        if self.reserved_pub_flow is not None:
            result['ReservedPubFlow'] = self.reserved_pub_flow
        if self.reserved_sub_flow is not None:
            result['ReservedSubFlow'] = self.reserved_sub_flow
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.schedule_type is not None:
            result['ScheduleType'] = self.schedule_type
        if self.time_zone is not None:
            result['TimeZone'] = self.time_zone
        if self.weekly_types is not None:
            result['WeeklyTypes'] = self.weekly_types
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DurationMinutes') is not None:
            self.duration_minutes = m.get('DurationMinutes')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('FirstScheduledTime') is not None:
            self.first_scheduled_time = m.get('FirstScheduledTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RepeatType') is not None:
            self.repeat_type = m.get('RepeatType')
        if m.get('ReservedPubFlow') is not None:
            self.reserved_pub_flow = m.get('ReservedPubFlow')
        if m.get('ReservedSubFlow') is not None:
            self.reserved_sub_flow = m.get('ReservedSubFlow')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('ScheduleType') is not None:
            self.schedule_type = m.get('ScheduleType')
        if m.get('TimeZone') is not None:
            self.time_zone = m.get('TimeZone')
        if m.get('WeeklyTypes') is not None:
            self.weekly_types = m.get('WeeklyTypes')
        return self


class CreateScheduledScalingRuleShrinkRequest(TeaModel):
    def __init__(
        self,
        duration_minutes: int = None,
        enable: bool = None,
        first_scheduled_time: int = None,
        instance_id: str = None,
        region_id: str = None,
        repeat_type: str = None,
        reserved_pub_flow: int = None,
        reserved_sub_flow: int = None,
        rule_name: str = None,
        schedule_type: str = None,
        time_zone: str = None,
        weekly_types_shrink: str = None,
    ):
        # The duration of each scheduled scaling task. Unit: minutes.
        # 
        # >  The value of this parameter must be greater than or equal to 15.
        # 
        # This parameter is required.
        self.duration_minutes = duration_minutes
        # Specifies whether to enable the scheduled scaling rule. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.enable = enable
        # The time when the scheduled scaling task is executed.
        # 
        # If you set ScheduleType to at, make sure that the value of this parameter is at least 30 minutes later than the current point in time.
        # 
        # >Notice: To prevent the broker from repeatedly executing instance upgrade and downgrade tasks, make sure that the interval between two consecutive scheduled scaling tasks is at least 60 minutes.
        # 
        # This parameter is required.
        self.first_scheduled_time = first_scheduled_time
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the region where the instance resides.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The frequency to execute the scheduled scaling task. This parameter is required only if you set ScheduleType to repeat. Valid values:
        # 
        # *   Daily: The scheduled scaling task is executed every day.
        # 
        # *   Weekly: The scheduled scaling task is executed every week.
        self.repeat_type = repeat_type
        # The reserved production capacity for scheduled scaling. Unit: MB/s.
        # 
        # >  You must specify a higher value than the instance specification for at least one of ReservedPubFlow and ReservedSubFlow.
        # 
        # This parameter is required.
        self.reserved_pub_flow = reserved_pub_flow
        # The reserved consumption capacity for scheduled scaling. Unit: MB/s.
        # 
        # >  You must specify a higher value than the instance specification for at least one of ReservedPubFlow and ReservedSubFlow.
        # 
        # This parameter is required.
        self.reserved_sub_flow = reserved_sub_flow
        # The name of the scheduled scaling rule.
        # 
        # >  The name of the scheduled scaling rule cannot be the same as the names of other rules for the instance.
        # 
        # This parameter is required.
        self.rule_name = rule_name
        # The type of the scheduled scaling task. Valid values:
        # 
        # *   at: The scheduled scaling task is executed only once.
        # *   repeat: The scheduled scaling task is repeatedly executed.
        # 
        # This parameter is required.
        self.schedule_type = schedule_type
        # The time zone in Coordinated Universal Time (UTC).
        # 
        # This parameter is required.
        self.time_zone = time_zone
        # The day on which the scheduled scaling task is executed every week. You can specify multiple days.
        self.weekly_types_shrink = weekly_types_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration_minutes is not None:
            result['DurationMinutes'] = self.duration_minutes
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.first_scheduled_time is not None:
            result['FirstScheduledTime'] = self.first_scheduled_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.repeat_type is not None:
            result['RepeatType'] = self.repeat_type
        if self.reserved_pub_flow is not None:
            result['ReservedPubFlow'] = self.reserved_pub_flow
        if self.reserved_sub_flow is not None:
            result['ReservedSubFlow'] = self.reserved_sub_flow
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.schedule_type is not None:
            result['ScheduleType'] = self.schedule_type
        if self.time_zone is not None:
            result['TimeZone'] = self.time_zone
        if self.weekly_types_shrink is not None:
            result['WeeklyTypes'] = self.weekly_types_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DurationMinutes') is not None:
            self.duration_minutes = m.get('DurationMinutes')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('FirstScheduledTime') is not None:
            self.first_scheduled_time = m.get('FirstScheduledTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RepeatType') is not None:
            self.repeat_type = m.get('RepeatType')
        if m.get('ReservedPubFlow') is not None:
            self.reserved_pub_flow = m.get('ReservedPubFlow')
        if m.get('ReservedSubFlow') is not None:
            self.reserved_sub_flow = m.get('ReservedSubFlow')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('ScheduleType') is not None:
            self.schedule_type = m.get('ScheduleType')
        if m.get('TimeZone') is not None:
            self.time_zone = m.get('TimeZone')
        if m.get('WeeklyTypes') is not None:
            self.weekly_types_shrink = m.get('WeeklyTypes')
        return self


class CreateScheduledScalingRuleResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code. The value 200 indicates that the request was successful.
        self.code = code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**\
        # *   **false**\
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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateScheduledScalingRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateScheduledScalingRuleResponseBody = None,
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
            temp_model = CreateScheduledScalingRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTopicRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        # 
        # *   If you do not specify this parameter, the keys of all tags are matched.
        # *   The tag key must be 1 to 128 characters in length and cannot contain `http://` or `https://`. The tag key cannot start with `aliyun` or `acs:`.
        # 
        # This parameter is required.
        self.key = key
        # The tag value.
        # 
        # *   You can leave this parameter empty.
        # *   The tag value must be 1 to 128 characters in length and cannot contain http:// or https://. The tag value cannot start with aliyun or acs:.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateTopicRequest(TeaModel):
    def __init__(
        self,
        compact_topic: bool = None,
        config: str = None,
        instance_id: str = None,
        local_topic: bool = None,
        min_insync_replicas: int = None,
        partition_num: str = None,
        region_id: str = None,
        remark: str = None,
        replication_factor: int = None,
        tag: List[CreateTopicRequestTag] = None,
        topic: str = None,
    ):
        # The log cleanup policy that is used for the topic. This parameter is available only when LocalTopic is set to true. Valid values:
        # 
        # *   false: The topic uses the default log cleanup policy.
        # *   true: The topic uses the log compaction policy.
        self.compact_topic = compact_topic
        # The additional configurations.
        # 
        # *   The value must be in JSON format.
        # *   Set Key to **replications**. This value specifies the number of replicas of the topic. The value must be an integer that ranges from 1 to 3.
        # *   You can configure this parameter only if you set **LocalTopic** to **true** or specify **Open Source Edition (Local Disk)** as the instance edition.****\
        # 
        # >  If you specify replications in this parameter, **ReplicationFactor** does not take effect.
        self.config = config
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The type of storage that the topic uses. Valid values:
        # 
        # *   false: The topic uses cloud storage.
        # *   true: The topic uses local storage.
        self.local_topic = local_topic
        # The minimum number of in-sync replicas (ISRs).
        # 
        # *   This parameter is available only when **LocalTopic** is set to **true**, or the instance is of the **Open Source Edition (Local Disk)**.****\
        # *   The value of this parameter must be smaller than the value of ReplicationFactor.
        # *   Valid values: 1 to 3.
        self.min_insync_replicas = min_insync_replicas
        # The number of partitions in the topic.
        # 
        # *   Valid values: 1 to 360.
        # *   In the ApsaraMQ for Kafka console, you can view the number of partitions that the system recommends based on the specifications of the instance. We recommend that you specify the number that is recommended by the system as the value of this parameter to reduce the risk of data skew.
        # 
        # Default values:
        # 
        # *   ApsaraMQ for Kafka V2 instance: 12
        # *   ApsaraMQ for Kafka V3 instance: 3
        self.partition_num = partition_num
        # The region ID of the instance in which you want to create a topic.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The description of the topic.
        # 
        # *   The description can contain only letters, digits, hyphens (-), and underscores (_).
        # *   The description must be 3 to 64 characters in length.
        # 
        # This parameter is required.
        self.remark = remark
        # The number of replicas for the topic.
        # 
        # *   This parameter is available only when **LocalTopic** is set to **true**, or the instance is of the **Open Source Edition (Local Disk)**.****\
        # *   Valid values: 1 to 3.
        # 
        # > If you set this parameter to **1**, data loss may occur. Exercise caution when you configure this parameter.
        self.replication_factor = replication_factor
        # The tags that you want to add to the topic.
        self.tag = tag
        # The topic name.
        # 
        # *   The name can contain only letters, digits, hyphens (-), and underscores (_).
        # *   The name must be 3 to 64 characters in length. If the name that you specify contains more than 64 characters, the system automatically truncates the name.
        # *   After a topic is created, you cannot change the name of the topic.
        # 
        # This parameter is required.
        self.topic = topic

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compact_topic is not None:
            result['CompactTopic'] = self.compact_topic
        if self.config is not None:
            result['Config'] = self.config
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.local_topic is not None:
            result['LocalTopic'] = self.local_topic
        if self.min_insync_replicas is not None:
            result['MinInsyncReplicas'] = self.min_insync_replicas
        if self.partition_num is not None:
            result['PartitionNum'] = self.partition_num
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.replication_factor is not None:
            result['ReplicationFactor'] = self.replication_factor
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompactTopic') is not None:
            self.compact_topic = m.get('CompactTopic')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('LocalTopic') is not None:
            self.local_topic = m.get('LocalTopic')
        if m.get('MinInsyncReplicas') is not None:
            self.min_insync_replicas = m.get('MinInsyncReplicas')
        if m.get('PartitionNum') is not None:
            self.partition_num = m.get('PartitionNum')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('ReplicationFactor') is not None:
            self.replication_factor = m.get('ReplicationFactor')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateTopicRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class CreateTopicResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code returned. The HTTP status code 200 indicates that the call is successful.
        self.code = code
        # The message returned.
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
            result['Code'] = self.code
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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


class DeleteAclRequest(TeaModel):
    def __init__(
        self,
        acl_operation_type: str = None,
        acl_operation_types: str = None,
        acl_permission_type: str = None,
        acl_resource_name: str = None,
        acl_resource_pattern_type: str = None,
        acl_resource_type: str = None,
        host: str = None,
        instance_id: str = None,
        region_id: str = None,
        username: str = None,
    ):
        # The operation allowed by the access control list (ACL). Valid values:
        # 
        # *   **Write**\
        # *   **Read**\
        # *   **Describe**: reads of transactional IDs
        # *   **IdempotentWrite**: idempotent data writes to clusters
        # *   **IDEMPOTENT_WRITE**: idempotent data writes to clusters. This value is available only for ApsaraMQ for Kafka V3 instances.
        # *   **DESCRIBE_CONFIGS**: configuration queries. This value is available only for ApsaraMQ for Kafka V3 instances.
        # 
        # This parameter is required.
        self.acl_operation_type = acl_operation_type
        # The operations allowed by the ACL. Separate multiple operations with commas (,).
        # 
        # Valid values:
        # 
        # *   **Write**: data writes
        # *   **Read**: data reads
        # *   **Describe**: reads of transactional IDs
        # *   **IdempotentWrite**: idempotent data writes to clusters
        # *   **IDEMPOTENT_WRITE**: idempotent data writes to clusters. This value is available only for ApsaraMQ for Kafka V3 instances.
        # *   **DESCRIBE_CONFIGS**: queries of configurations. This value is available only for ApsaraMQ for Kafka V3 instances.
        # 
        # >  This parameter is available only for ApsaraMQ for Kafka V3 serverless instances.
        self.acl_operation_types = acl_operation_types
        # The authorization method. Valid values:
        # 
        # *   Deny
        # *   ALLOW
        # 
        # >  This parameter is available only for ApsaraMQ for Kafka V3 serverless instances.
        self.acl_permission_type = acl_permission_type
        # The name of the resource.
        # 
        # *   The value can be the name of a topic or consumer group.
        # *   You can use an asterisk (\\*) to indicate the names of all topics or consumer groups.
        # 
        # This parameter is required.
        self.acl_resource_name = acl_resource_name
        # The mode that is used to match resources. Valid values:
        # 
        # *   **LITERAL:** full match
        # *   **PREFIXED**: prefix match
        # 
        # This parameter is required.
        self.acl_resource_pattern_type = acl_resource_pattern_type
        # The resource type. Valid values:
        # 
        # *   **Topic**: topic
        # *   **Group**: consumer group
        # *   **Cluster**: cluster
        # *   **TransactionalId**: transactional ID
        # 
        # This parameter is required.
        self.acl_resource_type = acl_resource_type
        # The IP address of the source.
        # 
        # > - You can specify only a specific IP address or use the asterisk (\\*) wildcard character to specify all IP addresses. CIDR blocks are not supported.
        # >- This parameter is available only for serverless ApsaraMQ for Kafka V3 instances.
        self.host = host
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the region.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The name of the user.
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
        if self.acl_operation_type is not None:
            result['AclOperationType'] = self.acl_operation_type
        if self.acl_operation_types is not None:
            result['AclOperationTypes'] = self.acl_operation_types
        if self.acl_permission_type is not None:
            result['AclPermissionType'] = self.acl_permission_type
        if self.acl_resource_name is not None:
            result['AclResourceName'] = self.acl_resource_name
        if self.acl_resource_pattern_type is not None:
            result['AclResourcePatternType'] = self.acl_resource_pattern_type
        if self.acl_resource_type is not None:
            result['AclResourceType'] = self.acl_resource_type
        if self.host is not None:
            result['Host'] = self.host
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclOperationType') is not None:
            self.acl_operation_type = m.get('AclOperationType')
        if m.get('AclOperationTypes') is not None:
            self.acl_operation_types = m.get('AclOperationTypes')
        if m.get('AclPermissionType') is not None:
            self.acl_permission_type = m.get('AclPermissionType')
        if m.get('AclResourceName') is not None:
            self.acl_resource_name = m.get('AclResourceName')
        if m.get('AclResourcePatternType') is not None:
            self.acl_resource_pattern_type = m.get('AclResourcePatternType')
        if m.get('AclResourceType') is not None:
            self.acl_resource_type = m.get('AclResourceType')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class DeleteAclResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code returned. The HTTP status code 200 indicates that the request is successful.
        self.code = code
        # The message returned.
        self.message = message
        # The ID of the request.
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
            result['Code'] = self.code
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteAclResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteAclResponseBody = None,
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
            temp_model = DeleteAclResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteConsumerGroupRequest(TeaModel):
    def __init__(
        self,
        consumer_id: str = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        # The name of the consumer group.
        # 
        # This parameter is required.
        self.consumer_id = consumer_id
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The region ID of the instance.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consumer_id is not None:
            result['ConsumerId'] = self.consumer_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsumerId') is not None:
            self.consumer_id = m.get('ConsumerId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteConsumerGroupResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code returned. The HTTP status code 200 indicates that the request is successful.
        self.code = code
        # The returned message.
        self.message = message
        # The ID of the request.
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
            result['Code'] = self.code
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
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


class DeleteInstanceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
    ):
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The region ID of the instance.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteInstanceResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code returned. The HTTP status code 200 indicates that the request is successful.
        self.code = code
        # The returned message.
        self.message = message
        # The ID of the request.
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
            result['Code'] = self.code
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
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


class DeleteSaslUserRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        mechanism: str = None,
        region_id: str = None,
        type: str = None,
        username: str = None,
    ):
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The encryption method. Valid values:
        # 
        # *   SCRAM-SHA-512. This is the default value.
        # *   SCRAM-SHA-256
        # 
        # >  This parameter is available only for ApsaraMQ for Kafka V3 serverless instances.
        self.mechanism = mechanism
        # The ID of the region.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The type of the Simple Authentication and Security Layer (SASL) user. Valid values:
        # 
        # *   **plain**: a simple mechanism that uses usernames and passwords to verify user identities. ApsaraMQ for Kafka provides an improved PLAIN mechanism that allows you to dynamically add SASL users without the need to restart an instance.
        # *   **SCRAM**: a mechanism that uses usernames and passwords to verify user identities. Compared with the PLAIN mechanism, this mechanism provides better security protection. ApsaraMQ for Kafka uses the SCRAM-SHA-256 algorithm.
        # *   **LDAP**: This value is available only for the SASL users of ApsaraMQ for Confluent instances.
        # 
        # Default value: **plain**.
        self.type = type
        # The name of the user.
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
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.mechanism is not None:
            result['Mechanism'] = self.mechanism
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.type is not None:
            result['Type'] = self.type
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Mechanism') is not None:
            self.mechanism = m.get('Mechanism')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class DeleteSaslUserResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code. If the request is successful, 200 is returned.
        self.code = code
        # The returned message.
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
            result['Code'] = self.code
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteSaslUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteSaslUserResponseBody = None,
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
            temp_model = DeleteSaslUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteScheduledScalingRuleRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
        rule_name: str = None,
    ):
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the region where the instance resides.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The name of the scheduled scaling rule.
        # 
        # >  You can delete only rules that are disabled and rules that are scheduled only once and have been executed.
        # 
        # This parameter is required.
        self.rule_name = rule_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class DeleteScheduledScalingRuleResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The responses code. The value 200 indicates that the request was successful.
        self.code = code
        # The returned message.
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
            result['Code'] = self.code
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteScheduledScalingRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteScheduledScalingRuleResponseBody = None,
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
            temp_model = DeleteScheduledScalingRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTopicRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
        topic: str = None,
    ):
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The region ID of the instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The name of the topic.
        # 
        # This parameter is required.
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class DeleteTopicResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code. The status code 200 indicates that the request is successful.
        self.code = code
        # The returned message.
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
            result['Code'] = self.code
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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


class DescribeAclsRequest(TeaModel):
    def __init__(
        self,
        acl_operation_type: str = None,
        acl_permission_type: str = None,
        acl_resource_name: str = None,
        acl_resource_pattern_type: str = None,
        acl_resource_type: str = None,
        host: str = None,
        instance_id: str = None,
        region_id: str = None,
        username: str = None,
    ):
        # The types of operations allowed by the ACL. Separate multiple operation types with commas (,).
        # - Valid values:
        # - Write
        # - Read
        # - Describe: reads of transactional IDs.
        # - IdempotentWrite: idempotent data writes to clusters.
        # - IDEMPOTENT_WRITE: idempotent data writes to clusters. This value is available only for ApsaraMQ for Kafka V3 instances.
        # - DESCRIBE_CONFIGS: queries of configurations. This value is available only for ApsaraMQ for Kafka V3 instances.
        # > This parameter is available only for ApsaraMQ for Kafka V3 serverless instances.
        self.acl_operation_type = acl_operation_type
        # The authorization method. Valid values:
        # - DENY
        # - ALLOW
        # > This parameter is available only for ApsaraMQ for Kafka V3 serverless instances.
        self.acl_permission_type = acl_permission_type
        # The resource name.
        # 
        # *   The value can be the name of a topic or consumer group.
        # *   You can use an asterisk (\\*) to specify the names of all topics or consumer groups.
        # 
        # > You can query the resources on which permissions are granted only after you grant the user the required permissions on all resources.
        # 
        # This parameter is required.
        self.acl_resource_name = acl_resource_name
        # The match mode. Valid values:
        # 
        # *   LITERAL: full-name match
        # *   PREFIXED: prefix match
        self.acl_resource_pattern_type = acl_resource_pattern_type
        # The resource type. Valid values:
        # 
        # *   **Topic**\
        # *   **Group**\
        # 
        # This parameter is required.
        self.acl_resource_type = acl_resource_type
        # The source IP address.
        # >-  You can specify only a specific IP address or use the asterisk (*) wildcard character to specify all IP addresses. CIDR blocks are not supported.
        # > - This parameter is available only for ApsaraMQ for Kafka V3 serverless instances.
        self.host = host
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the region.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The username.
        # 
        # *   You can use an asterisk (\\*) to specify all users.
        # 
        # > You can use an asterisk (\\*) to query the authorized users only after you grant the required permissions to all users.
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
        if self.acl_operation_type is not None:
            result['AclOperationType'] = self.acl_operation_type
        if self.acl_permission_type is not None:
            result['AclPermissionType'] = self.acl_permission_type
        if self.acl_resource_name is not None:
            result['AclResourceName'] = self.acl_resource_name
        if self.acl_resource_pattern_type is not None:
            result['AclResourcePatternType'] = self.acl_resource_pattern_type
        if self.acl_resource_type is not None:
            result['AclResourceType'] = self.acl_resource_type
        if self.host is not None:
            result['Host'] = self.host
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclOperationType') is not None:
            self.acl_operation_type = m.get('AclOperationType')
        if m.get('AclPermissionType') is not None:
            self.acl_permission_type = m.get('AclPermissionType')
        if m.get('AclResourceName') is not None:
            self.acl_resource_name = m.get('AclResourceName')
        if m.get('AclResourcePatternType') is not None:
            self.acl_resource_pattern_type = m.get('AclResourcePatternType')
        if m.get('AclResourceType') is not None:
            self.acl_resource_type = m.get('AclResourceType')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class DescribeAclsResponseBodyKafkaAclListKafkaAclVO(TeaModel):
    def __init__(
        self,
        acl_operation_type: str = None,
        acl_permission_type: str = None,
        acl_resource_name: str = None,
        acl_resource_pattern_type: str = None,
        acl_resource_type: str = None,
        host: str = None,
        username: str = None,
    ):
        # The types of operations allowed by the ACL. Separate multiple operation types with commas (,).
        # - Valid values:
        # - Write
        # - Read
        # - Describe: reads of transactional IDs.
        # - IdempotentWrite: idempotent data writes to clusters.
        # - IDEMPOTENT_WRITE: idempotent data writes to clusters. This value is available only for ApsaraMQ for Kafka V3 instances.
        # - DESCRIBE_CONFIGS: queries of configurations. This value is available only for ApsaraMQ for Kafka V3 instances.
        # > This parameter is available only for ApsaraMQ for Kafka V3 serverless instances.
        self.acl_operation_type = acl_operation_type
        # The authorization method. Valid values:
        # - DENY
        # - ALLOW
        # > This parameter is available only for ApsaraMQ for Kafka V3 serverless instances.
        self.acl_permission_type = acl_permission_type
        # The resource name.
        # 
        # *   The value can be the name of a topic or consumer group.
        # *   You can use the asterisk (\\*) wildcard character to specify the names of all topics or consumer groups.
        self.acl_resource_name = acl_resource_name
        # The matching mode. Valid values:
        # 
        # *   **LITERAL:** full-name match
        # *   **PREFIXED**: prefix match
        self.acl_resource_pattern_type = acl_resource_pattern_type
        # The resource type. Valid values:
        # 
        # *   **Topic**\
        # *   **Group**\
        self.acl_resource_type = acl_resource_type
        # The host.
        self.host = host
        # The username.
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_operation_type is not None:
            result['AclOperationType'] = self.acl_operation_type
        if self.acl_permission_type is not None:
            result['AclPermissionType'] = self.acl_permission_type
        if self.acl_resource_name is not None:
            result['AclResourceName'] = self.acl_resource_name
        if self.acl_resource_pattern_type is not None:
            result['AclResourcePatternType'] = self.acl_resource_pattern_type
        if self.acl_resource_type is not None:
            result['AclResourceType'] = self.acl_resource_type
        if self.host is not None:
            result['Host'] = self.host
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclOperationType') is not None:
            self.acl_operation_type = m.get('AclOperationType')
        if m.get('AclPermissionType') is not None:
            self.acl_permission_type = m.get('AclPermissionType')
        if m.get('AclResourceName') is not None:
            self.acl_resource_name = m.get('AclResourceName')
        if m.get('AclResourcePatternType') is not None:
            self.acl_resource_pattern_type = m.get('AclResourcePatternType')
        if m.get('AclResourceType') is not None:
            self.acl_resource_type = m.get('AclResourceType')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class DescribeAclsResponseBodyKafkaAclList(TeaModel):
    def __init__(
        self,
        kafka_acl_vo: List[DescribeAclsResponseBodyKafkaAclListKafkaAclVO] = None,
    ):
        self.kafka_acl_vo = kafka_acl_vo

    def validate(self):
        if self.kafka_acl_vo:
            for k in self.kafka_acl_vo:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['KafkaAclVO'] = []
        if self.kafka_acl_vo is not None:
            for k in self.kafka_acl_vo:
                result['KafkaAclVO'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.kafka_acl_vo = []
        if m.get('KafkaAclVO') is not None:
            for k in m.get('KafkaAclVO'):
                temp_model = DescribeAclsResponseBodyKafkaAclListKafkaAclVO()
                self.kafka_acl_vo.append(temp_model.from_map(k))
        return self


class DescribeAclsResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        kafka_acl_list: DescribeAclsResponseBodyKafkaAclList = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code returned. The HTTP status code 200 indicates that the request is successful.
        self.code = code
        # The access control lists (ACLs).
        self.kafka_acl_list = kafka_acl_list
        # The returned message.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        if self.kafka_acl_list:
            self.kafka_acl_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.kafka_acl_list is not None:
            result['KafkaAclList'] = self.kafka_acl_list.to_map()
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
        if m.get('KafkaAclList') is not None:
            temp_model = DescribeAclsResponseBodyKafkaAclList()
            self.kafka_acl_list = temp_model.from_map(m['KafkaAclList'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeAclsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAclsResponseBody = None,
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
            temp_model = DescribeAclsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSaslUsersRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
    ):
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the region.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeSaslUsersResponseBodySaslUserListSaslUserVO(TeaModel):
    def __init__(
        self,
        mechanism: str = None,
        password: str = None,
        type: str = None,
        username: str = None,
    ):
        # The encryption method.
        # 
        # >  This field is available only for serverless ApsaraMQ for Kafka V3 instances.
        self.mechanism = mechanism
        # The password.
        self.password = password
        # The type of the SASL user. Valid values:
        # 
        # *   **plain**: a simple mechanism that uses usernames and passwords to verify user identities. ApsaraMQ for Kafka provides an improved PLAIN mechanism that allows you to dynamically add SASL users without the need to restart an instance.
        # *   **SCRAM**: a mechanism that uses usernames and passwords to verify user identities. Compared with the PLAIN mechanism, this mechanism provides better security protection. ApsaraMQ for Kafka uses the SCRAM-SHA-256 algorithm.
        # *   **LDAP**: This value is available only for the SASL users of ApsaraMQ for Confluent instances.
        # 
        # Default value: **plain**.
        self.type = type
        # The username.
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mechanism is not None:
            result['Mechanism'] = self.mechanism
        if self.password is not None:
            result['Password'] = self.password
        if self.type is not None:
            result['Type'] = self.type
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Mechanism') is not None:
            self.mechanism = m.get('Mechanism')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class DescribeSaslUsersResponseBodySaslUserList(TeaModel):
    def __init__(
        self,
        sasl_user_vo: List[DescribeSaslUsersResponseBodySaslUserListSaslUserVO] = None,
    ):
        self.sasl_user_vo = sasl_user_vo

    def validate(self):
        if self.sasl_user_vo:
            for k in self.sasl_user_vo:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SaslUserVO'] = []
        if self.sasl_user_vo is not None:
            for k in self.sasl_user_vo:
                result['SaslUserVO'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.sasl_user_vo = []
        if m.get('SaslUserVO') is not None:
            for k in m.get('SaslUserVO'):
                temp_model = DescribeSaslUsersResponseBodySaslUserListSaslUserVO()
                self.sasl_user_vo.append(temp_model.from_map(k))
        return self


class DescribeSaslUsersResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        sasl_user_list: DescribeSaslUsersResponseBodySaslUserList = None,
        success: bool = None,
    ):
        # The HTTP status code returned. The HTTP status code 200 indicates that the request is successful.
        self.code = code
        # The returned message.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # The Simple Authentication and Security Layer (SASL) users.
        self.sasl_user_list = sasl_user_list
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        if self.sasl_user_list:
            self.sasl_user_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sasl_user_list is not None:
            result['SaslUserList'] = self.sasl_user_list.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SaslUserList') is not None:
            temp_model = DescribeSaslUsersResponseBodySaslUserList()
            self.sasl_user_list = temp_model.from_map(m['SaslUserList'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeSaslUsersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSaslUsersResponseBody = None,
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
            temp_model = DescribeSaslUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableAutoGroupCreationRequest(TeaModel):
    def __init__(
        self,
        enable: bool = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        # Specify whether to enable the flexible group creation feature. Valid values:
        # 
        # *   **true**: enables the flexible group creation feature.
        # *   **false**: disabled the flexible group creation feature.
        # 
        # This parameter is required.
        self.enable = enable
        # The instance ID.
        # 
        # You can call the [GetInstanceList](https://help.aliyun.com/document_detail/437663.html) operation to query instances.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class EnableAutoGroupCreationResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The returned HTTP status code.
        # 
        # If the value **200** is returned, the request is successful.
        self.code = code
        # The returned message.
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
            result['Code'] = self.code
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class EnableAutoGroupCreationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnableAutoGroupCreationResponseBody = None,
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
            temp_model = EnableAutoGroupCreationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableAutoTopicCreationRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        operate: str = None,
        partition_num: int = None,
        region_id: str = None,
    ):
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The operation that you want to perform. Valid values:
        # 
        # *   enable: enables the automatic topic creation feature.
        # *   disable: disables the automatic topic creation feature.
        # *   updatePartition: changes the number of partitions in topics that are automatically created.
        # 
        # This parameter is required.
        self.operate = operate
        # The changed number of partitions in topics that are automatically created.
        # 
        # This parameter takes effect only if you set Operate to updatePartition.
        self.partition_num = partition_num
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.operate is not None:
            result['Operate'] = self.operate
        if self.partition_num is not None:
            result['PartitionNum'] = self.partition_num
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Operate') is not None:
            self.operate = m.get('Operate')
        if m.get('PartitionNum') is not None:
            self.partition_num = m.get('PartitionNum')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class EnableAutoTopicCreationResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The returned status code. If the request is successful, 200 is returned.
        self.code = code
        # The returned message.
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
            result['Code'] = self.code
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class EnableAutoTopicCreationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnableAutoTopicCreationResponseBody = None,
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
            temp_model = EnableAutoTopicCreationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAllInstanceIdListRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        # The region ID of the instance. This parameter is reserved.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetAllInstanceIdListResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        instance_ids: Dict[str, Any] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code returned. The HTTP status code 200 indicates that the request is successful.
        self.code = code
        # The IDs of instances that are managed by the Alibaba Cloud account in all the regions.
        self.instance_ids = instance_ids
        # The returned message.
        self.message = message
        # The ID of the request.
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
            result['Code'] = self.code
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
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
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetAllInstanceIdListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAllInstanceIdListResponseBody = None,
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
            temp_model = GetAllInstanceIdListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAllowedIpListRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
    ):
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetAllowedIpListResponseBodyAllowedListInternetList(TeaModel):
    def __init__(
        self,
        allowed_ip_group: Dict[str, str] = None,
        allowed_ip_list: List[str] = None,
        port_range: str = None,
    ):
        # The group to which the IP address whitelist belongs.
        self.allowed_ip_group = allowed_ip_group
        # The information about the IP address whitelist.
        self.allowed_ip_list = allowed_ip_list
        # The port range. Valid value:
        # 
        # **9093/9093**.
        self.port_range = port_range

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allowed_ip_group is not None:
            result['AllowedIpGroup'] = self.allowed_ip_group
        if self.allowed_ip_list is not None:
            result['AllowedIpList'] = self.allowed_ip_list
        if self.port_range is not None:
            result['PortRange'] = self.port_range
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowedIpGroup') is not None:
            self.allowed_ip_group = m.get('AllowedIpGroup')
        if m.get('AllowedIpList') is not None:
            self.allowed_ip_list = m.get('AllowedIpList')
        if m.get('PortRange') is not None:
            self.port_range = m.get('PortRange')
        return self


class GetAllowedIpListResponseBodyAllowedListVpcList(TeaModel):
    def __init__(
        self,
        allowed_ip_group: Dict[str, str] = None,
        allowed_ip_list: List[str] = None,
        port_range: str = None,
    ):
        # The group to which the IP address whitelist belongs.
        self.allowed_ip_group = allowed_ip_group
        # The information about the IP address whitelist.
        self.allowed_ip_list = allowed_ip_list
        # The port range. Valid value:
        # 
        # **9092/9092**.
        self.port_range = port_range

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allowed_ip_group is not None:
            result['AllowedIpGroup'] = self.allowed_ip_group
        if self.allowed_ip_list is not None:
            result['AllowedIpList'] = self.allowed_ip_list
        if self.port_range is not None:
            result['PortRange'] = self.port_range
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowedIpGroup') is not None:
            self.allowed_ip_group = m.get('AllowedIpGroup')
        if m.get('AllowedIpList') is not None:
            self.allowed_ip_list = m.get('AllowedIpList')
        if m.get('PortRange') is not None:
            self.port_range = m.get('PortRange')
        return self


class GetAllowedIpListResponseBodyAllowedList(TeaModel):
    def __init__(
        self,
        deploy_type: int = None,
        internet_list: List[GetAllowedIpListResponseBodyAllowedListInternetList] = None,
        vpc_list: List[GetAllowedIpListResponseBodyAllowedListVpcList] = None,
    ):
        # The deployment mode of the instance. Valid values:
        # 
        # *   **4**: allows access from the Internet and a virtual private cloud (VPC).
        # *   **5**: allows access from a VPC.
        # 
        # >  Only integrators need to concern themselves with the value of this parameter.
        self.deploy_type = deploy_type
        # The whitelist for access from the Internet.
        self.internet_list = internet_list
        # The whitelist for access from a virtual private cloud (VPC).
        self.vpc_list = vpc_list

    def validate(self):
        if self.internet_list:
            for k in self.internet_list:
                if k:
                    k.validate()
        if self.vpc_list:
            for k in self.vpc_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deploy_type is not None:
            result['DeployType'] = self.deploy_type
        result['InternetList'] = []
        if self.internet_list is not None:
            for k in self.internet_list:
                result['InternetList'].append(k.to_map() if k else None)
        result['VpcList'] = []
        if self.vpc_list is not None:
            for k in self.vpc_list:
                result['VpcList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeployType') is not None:
            self.deploy_type = m.get('DeployType')
        self.internet_list = []
        if m.get('InternetList') is not None:
            for k in m.get('InternetList'):
                temp_model = GetAllowedIpListResponseBodyAllowedListInternetList()
                self.internet_list.append(temp_model.from_map(k))
        self.vpc_list = []
        if m.get('VpcList') is not None:
            for k in m.get('VpcList'):
                temp_model = GetAllowedIpListResponseBodyAllowedListVpcList()
                self.vpc_list.append(temp_model.from_map(k))
        return self


class GetAllowedIpListResponseBody(TeaModel):
    def __init__(
        self,
        allowed_list: GetAllowedIpListResponseBodyAllowedList = None,
        code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The IP address whitelist.
        self.allowed_list = allowed_list
        # The HTTP status code returned. The HTTP status code 200 indicates that the request is successful.
        self.code = code
        # The message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        if self.allowed_list:
            self.allowed_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allowed_list is not None:
            result['AllowedList'] = self.allowed_list.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowedList') is not None:
            temp_model = GetAllowedIpListResponseBodyAllowedList()
            self.allowed_list = temp_model.from_map(m['AllowedList'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetAllowedIpListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAllowedIpListResponseBody = None,
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
            temp_model = GetAllowedIpListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAutoScalingConfigurationRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
    ):
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the region where the instance resides.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetAutoScalingConfigurationResponseBodyDataScheduledScalingRulesScheduledScalingRulesWeeklyTypes(TeaModel):
    def __init__(
        self,
        weekly_types: List[str] = None,
    ):
        self.weekly_types = weekly_types

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.weekly_types is not None:
            result['WeeklyTypes'] = self.weekly_types
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WeeklyTypes') is not None:
            self.weekly_types = m.get('WeeklyTypes')
        return self


class GetAutoScalingConfigurationResponseBodyDataScheduledScalingRulesScheduledScalingRules(TeaModel):
    def __init__(
        self,
        duration_minutes: int = None,
        enable: bool = None,
        estimated_elastic_scaling_down_time_secs: int = None,
        estimated_elastic_scaling_up_time_secs: int = None,
        first_scheduled_time: int = None,
        repeat_type: str = None,
        reserved_pub_flow: int = None,
        reserved_sub_flow: int = None,
        rule_id: int = None,
        rule_name: str = None,
        schedule_type: str = None,
        time_zone: str = None,
        weekly_types: GetAutoScalingConfigurationResponseBodyDataScheduledScalingRulesScheduledScalingRulesWeeklyTypes = None,
    ):
        # The duration of a scheduled scaling task. Unit: minutes.
        self.duration_minutes = duration_minutes
        # Indicates whether the scheduled scaling rule is enabled. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.enable = enable
        # The estimated scale-in duration. Unit: seconds.
        self.estimated_elastic_scaling_down_time_secs = estimated_elastic_scaling_down_time_secs
        # The estimated scale-out duration. Unit: seconds.
        self.estimated_elastic_scaling_up_time_secs = estimated_elastic_scaling_up_time_secs
        # The timestamp that indicates the start time of the scheduled scaling task.
        self.first_scheduled_time = first_scheduled_time
        # The frequency at which the scheduled scaling task is executed. This parameter is returned only if ScheduleType is set to repeat. Valid values:
        # 
        # *   Daily: The scheduled scaling task is executed every day.
        # 
        # *   Weekly: The scheduled scaling task is executed every week.
        self.repeat_type = repeat_type
        # The reserved production capacity for scheduled scaling. Unit: MB/s.
        self.reserved_pub_flow = reserved_pub_flow
        # The reserved consumption capacity for scheduled scaling. Unit: MB/s.
        self.reserved_sub_flow = reserved_sub_flow
        # The ID of the scheduled scaling rule.
        self.rule_id = rule_id
        # The name of the scheduled scaling rule.
        self.rule_name = rule_name
        # The type of the scheduled scaling task. Valid values:
        # 
        # *   at: The scheduled scaling task is executed only once.
        # *   repeat: The scheduled scaling task is repeatedly executed.
        self.schedule_type = schedule_type
        # The time zone in Coordinated Universal Time (UTC).
        self.time_zone = time_zone
        # The day on which the scheduled scaling task is repeatedly executed. You can specify multiple days for this parameter.
        self.weekly_types = weekly_types

    def validate(self):
        if self.weekly_types:
            self.weekly_types.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration_minutes is not None:
            result['DurationMinutes'] = self.duration_minutes
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.estimated_elastic_scaling_down_time_secs is not None:
            result['EstimatedElasticScalingDownTimeSecs'] = self.estimated_elastic_scaling_down_time_secs
        if self.estimated_elastic_scaling_up_time_secs is not None:
            result['EstimatedElasticScalingUpTimeSecs'] = self.estimated_elastic_scaling_up_time_secs
        if self.first_scheduled_time is not None:
            result['FirstScheduledTime'] = self.first_scheduled_time
        if self.repeat_type is not None:
            result['RepeatType'] = self.repeat_type
        if self.reserved_pub_flow is not None:
            result['ReservedPubFlow'] = self.reserved_pub_flow
        if self.reserved_sub_flow is not None:
            result['ReservedSubFlow'] = self.reserved_sub_flow
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.schedule_type is not None:
            result['ScheduleType'] = self.schedule_type
        if self.time_zone is not None:
            result['TimeZone'] = self.time_zone
        if self.weekly_types is not None:
            result['WeeklyTypes'] = self.weekly_types.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DurationMinutes') is not None:
            self.duration_minutes = m.get('DurationMinutes')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('EstimatedElasticScalingDownTimeSecs') is not None:
            self.estimated_elastic_scaling_down_time_secs = m.get('EstimatedElasticScalingDownTimeSecs')
        if m.get('EstimatedElasticScalingUpTimeSecs') is not None:
            self.estimated_elastic_scaling_up_time_secs = m.get('EstimatedElasticScalingUpTimeSecs')
        if m.get('FirstScheduledTime') is not None:
            self.first_scheduled_time = m.get('FirstScheduledTime')
        if m.get('RepeatType') is not None:
            self.repeat_type = m.get('RepeatType')
        if m.get('ReservedPubFlow') is not None:
            self.reserved_pub_flow = m.get('ReservedPubFlow')
        if m.get('ReservedSubFlow') is not None:
            self.reserved_sub_flow = m.get('ReservedSubFlow')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('ScheduleType') is not None:
            self.schedule_type = m.get('ScheduleType')
        if m.get('TimeZone') is not None:
            self.time_zone = m.get('TimeZone')
        if m.get('WeeklyTypes') is not None:
            temp_model = GetAutoScalingConfigurationResponseBodyDataScheduledScalingRulesScheduledScalingRulesWeeklyTypes()
            self.weekly_types = temp_model.from_map(m['WeeklyTypes'])
        return self


class GetAutoScalingConfigurationResponseBodyDataScheduledScalingRules(TeaModel):
    def __init__(
        self,
        scheduled_scaling_rules: List[GetAutoScalingConfigurationResponseBodyDataScheduledScalingRulesScheduledScalingRules] = None,
    ):
        self.scheduled_scaling_rules = scheduled_scaling_rules

    def validate(self):
        if self.scheduled_scaling_rules:
            for k in self.scheduled_scaling_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ScheduledScalingRules'] = []
        if self.scheduled_scaling_rules is not None:
            for k in self.scheduled_scaling_rules:
                result['ScheduledScalingRules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.scheduled_scaling_rules = []
        if m.get('ScheduledScalingRules') is not None:
            for k in m.get('ScheduledScalingRules'):
                temp_model = GetAutoScalingConfigurationResponseBodyDataScheduledScalingRulesScheduledScalingRules()
                self.scheduled_scaling_rules.append(temp_model.from_map(k))
        return self


class GetAutoScalingConfigurationResponseBodyData(TeaModel):
    def __init__(
        self,
        scheduled_scaling_rules: GetAutoScalingConfigurationResponseBodyDataScheduledScalingRules = None,
    ):
        # The scheduled scaling rules.
        self.scheduled_scaling_rules = scheduled_scaling_rules

    def validate(self):
        if self.scheduled_scaling_rules:
            self.scheduled_scaling_rules.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scheduled_scaling_rules is not None:
            result['ScheduledScalingRules'] = self.scheduled_scaling_rules.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ScheduledScalingRules') is not None:
            temp_model = GetAutoScalingConfigurationResponseBodyDataScheduledScalingRules()
            self.scheduled_scaling_rules = temp_model.from_map(m['ScheduledScalingRules'])
        return self


class GetAutoScalingConfigurationResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetAutoScalingConfigurationResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code. The value 200 indicates that the request was successful.
        self.code = code
        # The returned data.
        self.data = data
        # The returned message.
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
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = GetAutoScalingConfigurationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetAutoScalingConfigurationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAutoScalingConfigurationResponseBody = None,
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
            temp_model = GetAutoScalingConfigurationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetConsumerListRequest(TeaModel):
    def __init__(
        self,
        consumer_id: str = None,
        current_page: int = None,
        instance_id: str = None,
        page_size: int = None,
        region_id: str = None,
    ):
        # The name of the consumer group. If you do not configure this parameter, all consumer groups are queried.
        self.consumer_id = consumer_id
        # The page number.
        self.current_page = current_page
        # The ID of the instance to which the consumer group belongs.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The number of entries to be returned per page.
        self.page_size = page_size
        # The region ID of the instance to which the consumer group belongs.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consumer_id is not None:
            result['ConsumerId'] = self.consumer_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsumerId') is not None:
            self.consumer_id = m.get('ConsumerId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetConsumerListResponseBodyConsumerListConsumerVOTagsTagVO(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetConsumerListResponseBodyConsumerListConsumerVOTags(TeaModel):
    def __init__(
        self,
        tag_vo: List[GetConsumerListResponseBodyConsumerListConsumerVOTagsTagVO] = None,
    ):
        self.tag_vo = tag_vo

    def validate(self):
        if self.tag_vo:
            for k in self.tag_vo:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TagVO'] = []
        if self.tag_vo is not None:
            for k in self.tag_vo:
                result['TagVO'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag_vo = []
        if m.get('TagVO') is not None:
            for k in m.get('TagVO'):
                temp_model = GetConsumerListResponseBodyConsumerListConsumerVOTagsTagVO()
                self.tag_vo.append(temp_model.from_map(k))
        return self


class GetConsumerListResponseBodyConsumerListConsumerVO(TeaModel):
    def __init__(
        self,
        automatically_created_group: bool = None,
        consumer_id: str = None,
        instance_id: str = None,
        region_id: str = None,
        remark: str = None,
        tags: GetConsumerListResponseBodyConsumerListConsumerVOTags = None,
    ):
        # Indicates that the consumer group was automatically created by the system.
        self.automatically_created_group = automatically_created_group
        # The consumer group ID.
        self.consumer_id = consumer_id
        # The instance ID.
        self.instance_id = instance_id
        # The ID of the region where the instance resides.
        self.region_id = region_id
        # The instance description.
        self.remark = remark
        # The tags.
        self.tags = tags

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.automatically_created_group is not None:
            result['AutomaticallyCreatedGroup'] = self.automatically_created_group
        if self.consumer_id is not None:
            result['ConsumerId'] = self.consumer_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutomaticallyCreatedGroup') is not None:
            self.automatically_created_group = m.get('AutomaticallyCreatedGroup')
        if m.get('ConsumerId') is not None:
            self.consumer_id = m.get('ConsumerId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Tags') is not None:
            temp_model = GetConsumerListResponseBodyConsumerListConsumerVOTags()
            self.tags = temp_model.from_map(m['Tags'])
        return self


class GetConsumerListResponseBodyConsumerList(TeaModel):
    def __init__(
        self,
        consumer_vo: List[GetConsumerListResponseBodyConsumerListConsumerVO] = None,
    ):
        self.consumer_vo = consumer_vo

    def validate(self):
        if self.consumer_vo:
            for k in self.consumer_vo:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ConsumerVO'] = []
        if self.consumer_vo is not None:
            for k in self.consumer_vo:
                result['ConsumerVO'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.consumer_vo = []
        if m.get('ConsumerVO') is not None:
            for k in m.get('ConsumerVO'):
                temp_model = GetConsumerListResponseBodyConsumerListConsumerVO()
                self.consumer_vo.append(temp_model.from_map(k))
        return self


class GetConsumerListResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        consumer_list: GetConsumerListResponseBodyConsumerList = None,
        current_page: int = None,
        message: str = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total: int = None,
    ):
        # The HTTP status code returned. The HTTP status code 200 indicates that the request is successful.
        self.code = code
        # The consumer groups.
        self.consumer_list = consumer_list
        # The number of the page to return. Pages start from page 1.
        self.current_page = current_page
        # The returned message.
        self.message = message
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success
        # The total number of entries returned.
        self.total = total

    def validate(self):
        if self.consumer_list:
            self.consumer_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.consumer_list is not None:
            result['ConsumerList'] = self.consumer_list.to_map()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ConsumerList') is not None:
            temp_model = GetConsumerListResponseBodyConsumerList()
            self.consumer_list = temp_model.from_map(m['ConsumerList'])
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class GetConsumerListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetConsumerListResponseBody = None,
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
            temp_model = GetConsumerListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetConsumerProgressRequest(TeaModel):
    def __init__(
        self,
        consumer_id: str = None,
        hide_last_timestamp: bool = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        # The name of the consumer group.
        # 
        # This parameter is required.
        self.consumer_id = consumer_id
        self.hide_last_timestamp = hide_last_timestamp
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The region ID of the instance.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consumer_id is not None:
            result['ConsumerId'] = self.consumer_id
        if self.hide_last_timestamp is not None:
            result['HideLastTimestamp'] = self.hide_last_timestamp
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsumerId') is not None:
            self.consumer_id = m.get('ConsumerId')
        if m.get('HideLastTimestamp') is not None:
            self.hide_last_timestamp = m.get('HideLastTimestamp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetConsumerProgressResponseBodyConsumerProgressRebalanceInfoListRebalanceInfoList(TeaModel):
    def __init__(
        self,
        generation: int = None,
        group_id: str = None,
        last_rebalance_timestamp: int = None,
        reason: str = None,
        rebalance_success: bool = None,
        rebalance_time_consuming: int = None,
    ):
        # The number of rebalances.
        self.generation = generation
        # The group ID of the subscriber.
        self.group_id = group_id
        # The time when the last rebalance occurred. Unit: milliseconds.
        self.last_rebalance_timestamp = last_rebalance_timestamp
        # The cause of the rebalance.
        self.reason = reason
        # Indicates whether new members are added to the consumer group in the rebalance.
        self.rebalance_success = rebalance_success
        # The duration of the rebalance. Unit: milliseconds.
        self.rebalance_time_consuming = rebalance_time_consuming

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.generation is not None:
            result['Generation'] = self.generation
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.last_rebalance_timestamp is not None:
            result['LastRebalanceTimestamp'] = self.last_rebalance_timestamp
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.rebalance_success is not None:
            result['RebalanceSuccess'] = self.rebalance_success
        if self.rebalance_time_consuming is not None:
            result['RebalanceTimeConsuming'] = self.rebalance_time_consuming
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Generation') is not None:
            self.generation = m.get('Generation')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('LastRebalanceTimestamp') is not None:
            self.last_rebalance_timestamp = m.get('LastRebalanceTimestamp')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('RebalanceSuccess') is not None:
            self.rebalance_success = m.get('RebalanceSuccess')
        if m.get('RebalanceTimeConsuming') is not None:
            self.rebalance_time_consuming = m.get('RebalanceTimeConsuming')
        return self


class GetConsumerProgressResponseBodyConsumerProgressRebalanceInfoList(TeaModel):
    def __init__(
        self,
        rebalance_info_list: List[GetConsumerProgressResponseBodyConsumerProgressRebalanceInfoListRebalanceInfoList] = None,
    ):
        self.rebalance_info_list = rebalance_info_list

    def validate(self):
        if self.rebalance_info_list:
            for k in self.rebalance_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RebalanceInfoList'] = []
        if self.rebalance_info_list is not None:
            for k in self.rebalance_info_list:
                result['RebalanceInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.rebalance_info_list = []
        if m.get('RebalanceInfoList') is not None:
            for k in m.get('RebalanceInfoList'):
                temp_model = GetConsumerProgressResponseBodyConsumerProgressRebalanceInfoListRebalanceInfoList()
                self.rebalance_info_list.append(temp_model.from_map(k))
        return self


class GetConsumerProgressResponseBodyConsumerProgressTopicListTopicListOffsetListOffsetList(TeaModel):
    def __init__(
        self,
        broker_offset: int = None,
        consumer_offset: int = None,
        last_timestamp: int = None,
        partition: int = None,
    ):
        # The latest offset in the partition of the topic.
        self.broker_offset = broker_offset
        # The consumer offset in the partition of the topic.
        self.consumer_offset = consumer_offset
        # The time when the last consumed message in the partition was generated.
        self.last_timestamp = last_timestamp
        # The partition ID.
        self.partition = partition

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.broker_offset is not None:
            result['BrokerOffset'] = self.broker_offset
        if self.consumer_offset is not None:
            result['ConsumerOffset'] = self.consumer_offset
        if self.last_timestamp is not None:
            result['LastTimestamp'] = self.last_timestamp
        if self.partition is not None:
            result['Partition'] = self.partition
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BrokerOffset') is not None:
            self.broker_offset = m.get('BrokerOffset')
        if m.get('ConsumerOffset') is not None:
            self.consumer_offset = m.get('ConsumerOffset')
        if m.get('LastTimestamp') is not None:
            self.last_timestamp = m.get('LastTimestamp')
        if m.get('Partition') is not None:
            self.partition = m.get('Partition')
        return self


class GetConsumerProgressResponseBodyConsumerProgressTopicListTopicListOffsetList(TeaModel):
    def __init__(
        self,
        offset_list: List[GetConsumerProgressResponseBodyConsumerProgressTopicListTopicListOffsetListOffsetList] = None,
    ):
        self.offset_list = offset_list

    def validate(self):
        if self.offset_list:
            for k in self.offset_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['OffsetList'] = []
        if self.offset_list is not None:
            for k in self.offset_list:
                result['OffsetList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.offset_list = []
        if m.get('OffsetList') is not None:
            for k in m.get('OffsetList'):
                temp_model = GetConsumerProgressResponseBodyConsumerProgressTopicListTopicListOffsetListOffsetList()
                self.offset_list.append(temp_model.from_map(k))
        return self


class GetConsumerProgressResponseBodyConsumerProgressTopicListTopicList(TeaModel):
    def __init__(
        self,
        last_timestamp: int = None,
        offset_list: GetConsumerProgressResponseBodyConsumerProgressTopicListTopicListOffsetList = None,
        topic: str = None,
        total_diff: int = None,
    ):
        # The time when the last consumed message in the topic was generated.
        self.last_timestamp = last_timestamp
        # The consumer offsets.
        self.offset_list = offset_list
        # The topic name.
        self.topic = topic
        # The number of unconsumed messages in the topic to which the consumer group subscribes.
        self.total_diff = total_diff

    def validate(self):
        if self.offset_list:
            self.offset_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.last_timestamp is not None:
            result['LastTimestamp'] = self.last_timestamp
        if self.offset_list is not None:
            result['OffsetList'] = self.offset_list.to_map()
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.total_diff is not None:
            result['TotalDiff'] = self.total_diff
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LastTimestamp') is not None:
            self.last_timestamp = m.get('LastTimestamp')
        if m.get('OffsetList') is not None:
            temp_model = GetConsumerProgressResponseBodyConsumerProgressTopicListTopicListOffsetList()
            self.offset_list = temp_model.from_map(m['OffsetList'])
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('TotalDiff') is not None:
            self.total_diff = m.get('TotalDiff')
        return self


class GetConsumerProgressResponseBodyConsumerProgressTopicList(TeaModel):
    def __init__(
        self,
        topic_list: List[GetConsumerProgressResponseBodyConsumerProgressTopicListTopicList] = None,
    ):
        self.topic_list = topic_list

    def validate(self):
        if self.topic_list:
            for k in self.topic_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TopicList'] = []
        if self.topic_list is not None:
            for k in self.topic_list:
                result['TopicList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.topic_list = []
        if m.get('TopicList') is not None:
            for k in m.get('TopicList'):
                temp_model = GetConsumerProgressResponseBodyConsumerProgressTopicListTopicList()
                self.topic_list.append(temp_model.from_map(k))
        return self


class GetConsumerProgressResponseBodyConsumerProgress(TeaModel):
    def __init__(
        self,
        last_timestamp: int = None,
        rebalance_info_list: GetConsumerProgressResponseBodyConsumerProgressRebalanceInfoList = None,
        topic_list: GetConsumerProgressResponseBodyConsumerProgressTopicList = None,
        total_diff: int = None,
    ):
        # The time when the last message consumed by the consumer group was generated.
        self.last_timestamp = last_timestamp
        # The details of rebalances in the consumer group.
        self.rebalance_info_list = rebalance_info_list
        # The consumer progress of each topic to which the consumer group subscribes.
        self.topic_list = topic_list
        # The total number of unconsumed messages in all topics to which the consumer group subscribes.
        self.total_diff = total_diff

    def validate(self):
        if self.rebalance_info_list:
            self.rebalance_info_list.validate()
        if self.topic_list:
            self.topic_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.last_timestamp is not None:
            result['LastTimestamp'] = self.last_timestamp
        if self.rebalance_info_list is not None:
            result['RebalanceInfoList'] = self.rebalance_info_list.to_map()
        if self.topic_list is not None:
            result['TopicList'] = self.topic_list.to_map()
        if self.total_diff is not None:
            result['TotalDiff'] = self.total_diff
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LastTimestamp') is not None:
            self.last_timestamp = m.get('LastTimestamp')
        if m.get('RebalanceInfoList') is not None:
            temp_model = GetConsumerProgressResponseBodyConsumerProgressRebalanceInfoList()
            self.rebalance_info_list = temp_model.from_map(m['RebalanceInfoList'])
        if m.get('TopicList') is not None:
            temp_model = GetConsumerProgressResponseBodyConsumerProgressTopicList()
            self.topic_list = temp_model.from_map(m['TopicList'])
        if m.get('TotalDiff') is not None:
            self.total_diff = m.get('TotalDiff')
        return self


class GetConsumerProgressResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        consumer_progress: GetConsumerProgressResponseBodyConsumerProgress = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The returned HTTP status code. If the request is successful, 200 is returned.
        self.code = code
        # The consumer progress of the consumer group.
        self.consumer_progress = consumer_progress
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        if self.consumer_progress:
            self.consumer_progress.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.consumer_progress is not None:
            result['ConsumerProgress'] = self.consumer_progress.to_map()
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
        if m.get('ConsumerProgress') is not None:
            temp_model = GetConsumerProgressResponseBodyConsumerProgress()
            self.consumer_progress = temp_model.from_map(m['ConsumerProgress'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetConsumerProgressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetConsumerProgressResponseBody = None,
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
            temp_model = GetConsumerProgressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstanceListRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        # 
        # *   If you leave this parameter empty, the keys of all tags are matched.
        # *   The tag key can be up to 128 characters in length. It cannot start with aliyun or acs: and cannot contain `http://` or `https://`.
        self.key = key
        # The tag value.
        # 
        # *   If you leave Key empty, you must also leave this parameter empty. If you leave this parameter empty, the values of all tags are matched.
        # *   The tag value can be up to 128 characters in length. It cannot start with aliyun or acs: and cannot contain `http://` or `https://`.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetInstanceListRequest(TeaModel):
    def __init__(
        self,
        instance_id: List[str] = None,
        order_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        series: str = None,
        tag: List[GetInstanceListRequestTag] = None,
    ):
        # The IDs of instances.
        self.instance_id = instance_id
        # The ID of the order. You can obtain the order ID on the [Orders](https://usercenter2-intl.aliyun.com/order/list?pageIndex=1\\&pageSize=20\\&spm=5176.12818093.top-nav.ditem-ord.36f016d0OQFmJa) page in Alibaba Cloud User Center.
        self.order_id = order_id
        # The ID of the region where the instance resides.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group. You can obtain this ID on the Resource Group page in the Resource Management console.
        self.resource_group_id = resource_group_id
        # The instance version. You can use instance versions to filter different versions of instances. Valid values:
        # 
        # *   v2
        # *   v3
        # *   confluent
        self.series = series
        # The tags.
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.series is not None:
            result['Series'] = self.series
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Series') is not None:
            self.series = m.get('Series')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = GetInstanceListRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class GetInstanceListResponseBodyInstanceListInstanceVOConfluentConfig(TeaModel):
    def __init__(
        self,
        connect_cu: int = None,
        connect_replica: int = None,
        control_center_cu: int = None,
        control_center_replica: int = None,
        control_center_storage: int = None,
        kafka_cu: int = None,
        kafka_replica: int = None,
        kafka_rest_proxy_cu: int = None,
        kafka_rest_proxy_replica: int = None,
        kafka_storage: int = None,
        ksql_cu: int = None,
        ksql_replica: int = None,
        ksql_storage: int = None,
        schema_registry_cu: int = None,
        schema_registry_replica: int = None,
        zoo_keeper_cu: int = None,
        zoo_keeper_replica: int = None,
        zoo_keeper_storage: int = None,
    ):
        # The number of CPU cores of Connect.
        self.connect_cu = connect_cu
        # The number of replicas of Connect.
        self.connect_replica = connect_replica
        # The number of CPU cores of Control Center.
        self.control_center_cu = control_center_cu
        # The number of replicas of Control Center.
        self.control_center_replica = control_center_replica
        # The disk capacity of Control Center. Unit: GB.
        self.control_center_storage = control_center_storage
        # The number of CPU cores of the Kafka broker.
        self.kafka_cu = kafka_cu
        # The number of replicas of the Kafka broker.
        self.kafka_replica = kafka_replica
        # The number of CPU cores of Kafka Rest Proxy.
        self.kafka_rest_proxy_cu = kafka_rest_proxy_cu
        # The number of replicas of Kafka Rest Proxy.
        self.kafka_rest_proxy_replica = kafka_rest_proxy_replica
        # The disk capacity of the Kafka broker. Unit: GB.
        self.kafka_storage = kafka_storage
        # The number of CPU cores of ksqlDB.
        self.ksql_cu = ksql_cu
        # The number of replicas of ksqlDB.
        self.ksql_replica = ksql_replica
        # The disk capacity of ksqlDB. Unit: GB.
        self.ksql_storage = ksql_storage
        # The number of CPU cores of Schema Registry.
        self.schema_registry_cu = schema_registry_cu
        # The number of replicas of Schema Registry.
        self.schema_registry_replica = schema_registry_replica
        # The number of CPU cores of ZooKeeper.
        self.zoo_keeper_cu = zoo_keeper_cu
        # The number of replicas of ZooKeeper.
        self.zoo_keeper_replica = zoo_keeper_replica
        # The disk capacity of ZooKeeper. Unit: GB.
        self.zoo_keeper_storage = zoo_keeper_storage

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connect_cu is not None:
            result['ConnectCU'] = self.connect_cu
        if self.connect_replica is not None:
            result['ConnectReplica'] = self.connect_replica
        if self.control_center_cu is not None:
            result['ControlCenterCU'] = self.control_center_cu
        if self.control_center_replica is not None:
            result['ControlCenterReplica'] = self.control_center_replica
        if self.control_center_storage is not None:
            result['ControlCenterStorage'] = self.control_center_storage
        if self.kafka_cu is not None:
            result['KafkaCU'] = self.kafka_cu
        if self.kafka_replica is not None:
            result['KafkaReplica'] = self.kafka_replica
        if self.kafka_rest_proxy_cu is not None:
            result['KafkaRestProxyCU'] = self.kafka_rest_proxy_cu
        if self.kafka_rest_proxy_replica is not None:
            result['KafkaRestProxyReplica'] = self.kafka_rest_proxy_replica
        if self.kafka_storage is not None:
            result['KafkaStorage'] = self.kafka_storage
        if self.ksql_cu is not None:
            result['KsqlCU'] = self.ksql_cu
        if self.ksql_replica is not None:
            result['KsqlReplica'] = self.ksql_replica
        if self.ksql_storage is not None:
            result['KsqlStorage'] = self.ksql_storage
        if self.schema_registry_cu is not None:
            result['SchemaRegistryCU'] = self.schema_registry_cu
        if self.schema_registry_replica is not None:
            result['SchemaRegistryReplica'] = self.schema_registry_replica
        if self.zoo_keeper_cu is not None:
            result['ZooKeeperCU'] = self.zoo_keeper_cu
        if self.zoo_keeper_replica is not None:
            result['ZooKeeperReplica'] = self.zoo_keeper_replica
        if self.zoo_keeper_storage is not None:
            result['ZooKeeperStorage'] = self.zoo_keeper_storage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectCU') is not None:
            self.connect_cu = m.get('ConnectCU')
        if m.get('ConnectReplica') is not None:
            self.connect_replica = m.get('ConnectReplica')
        if m.get('ControlCenterCU') is not None:
            self.control_center_cu = m.get('ControlCenterCU')
        if m.get('ControlCenterReplica') is not None:
            self.control_center_replica = m.get('ControlCenterReplica')
        if m.get('ControlCenterStorage') is not None:
            self.control_center_storage = m.get('ControlCenterStorage')
        if m.get('KafkaCU') is not None:
            self.kafka_cu = m.get('KafkaCU')
        if m.get('KafkaReplica') is not None:
            self.kafka_replica = m.get('KafkaReplica')
        if m.get('KafkaRestProxyCU') is not None:
            self.kafka_rest_proxy_cu = m.get('KafkaRestProxyCU')
        if m.get('KafkaRestProxyReplica') is not None:
            self.kafka_rest_proxy_replica = m.get('KafkaRestProxyReplica')
        if m.get('KafkaStorage') is not None:
            self.kafka_storage = m.get('KafkaStorage')
        if m.get('KsqlCU') is not None:
            self.ksql_cu = m.get('KsqlCU')
        if m.get('KsqlReplica') is not None:
            self.ksql_replica = m.get('KsqlReplica')
        if m.get('KsqlStorage') is not None:
            self.ksql_storage = m.get('KsqlStorage')
        if m.get('SchemaRegistryCU') is not None:
            self.schema_registry_cu = m.get('SchemaRegistryCU')
        if m.get('SchemaRegistryReplica') is not None:
            self.schema_registry_replica = m.get('SchemaRegistryReplica')
        if m.get('ZooKeeperCU') is not None:
            self.zoo_keeper_cu = m.get('ZooKeeperCU')
        if m.get('ZooKeeperReplica') is not None:
            self.zoo_keeper_replica = m.get('ZooKeeperReplica')
        if m.get('ZooKeeperStorage') is not None:
            self.zoo_keeper_storage = m.get('ZooKeeperStorage')
        return self


class GetInstanceListResponseBodyInstanceListInstanceVOTagsTagVO(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetInstanceListResponseBodyInstanceListInstanceVOTags(TeaModel):
    def __init__(
        self,
        tag_vo: List[GetInstanceListResponseBodyInstanceListInstanceVOTagsTagVO] = None,
    ):
        self.tag_vo = tag_vo

    def validate(self):
        if self.tag_vo:
            for k in self.tag_vo:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TagVO'] = []
        if self.tag_vo is not None:
            for k in self.tag_vo:
                result['TagVO'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag_vo = []
        if m.get('TagVO') is not None:
            for k in m.get('TagVO'):
                temp_model = GetInstanceListResponseBodyInstanceListInstanceVOTagsTagVO()
                self.tag_vo.append(temp_model.from_map(k))
        return self


class GetInstanceListResponseBodyInstanceListInstanceVOUpgradeServiceDetailInfo(TeaModel):
    def __init__(
        self,
        current_2open_source_version: str = None,
    ):
        # The open source Apache Kafka version that corresponds to the instance.
        self.current_2open_source_version = current_2open_source_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_2open_source_version is not None:
            result['Current2OpenSourceVersion'] = self.current_2open_source_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Current2OpenSourceVersion') is not None:
            self.current_2open_source_version = m.get('Current2OpenSourceVersion')
        return self


class GetInstanceListResponseBodyInstanceListInstanceVO(TeaModel):
    def __init__(
        self,
        all_config: str = None,
        confluent_config: GetInstanceListResponseBodyInstanceListInstanceVOConfluentConfig = None,
        create_time: int = None,
        deploy_type: int = None,
        disk_size: int = None,
        disk_type: int = None,
        domain_endpoint: str = None,
        eip_max: int = None,
        end_point: str = None,
        expired_time: int = None,
        instance_id: str = None,
        io_max: int = None,
        io_max_read: int = None,
        io_max_spec: str = None,
        io_max_write: int = None,
        kms_key_id: str = None,
        msg_retain: int = None,
        name: str = None,
        paid_type: int = None,
        region_id: str = None,
        reserved_publish_capacity: int = None,
        reserved_subscribe_capacity: int = None,
        resource_group_id: str = None,
        sasl_domain_endpoint: str = None,
        security_group: str = None,
        series: str = None,
        service_status: int = None,
        spec_type: str = None,
        ssl_domain_endpoint: str = None,
        ssl_end_point: str = None,
        standard_zone_id: str = None,
        tags: GetInstanceListResponseBodyInstanceListInstanceVOTags = None,
        topic_num_limit: int = None,
        upgrade_service_detail_info: GetInstanceListResponseBodyInstanceListInstanceVOUpgradeServiceDetailInfo = None,
        used_group_count: int = None,
        used_partition_count: int = None,
        used_topic_count: int = None,
        v_switch_id: str = None,
        view_instance_status_code: int = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        # The configurations of the deployed ApsaraMQ for Kafka instance.
        self.all_config = all_config
        # The parameters that are returned for the ApsaraMQ for Confluent instance.
        self.confluent_config = confluent_config
        # The time when the instance was created. Unit: milliseconds.
        self.create_time = create_time
        # The type of the network in which the instance is deployed. Valid values:
        # 
        # *   **4**: Internet and VPC
        # *   **5**: VPC
        self.deploy_type = deploy_type
        # The disk size. Unit: GB
        self.disk_size = disk_size
        # The disk type of the instance. Valid values:
        # 
        # *   **0**: ultra disk
        # *   **1**: standard SSD
        self.disk_type = disk_type
        # The default endpoint of the instance in domain name mode. ApsaraMQ for Kafka instances support endpoints in domain name mode and IP address mode.
        # 
        # *   Endpoints in domain name mode: An endpoint in this mode consists of the domain name of the instance and a port number. The format of an endpoint in this mode is `{Instance domain name}:{Port number}`.
        # *   Endpoints in IP address mode: An endpoint in this mode consists of the IP address of the broker and a port number. The format of an endpoint in this mode is `{Broker IP address}:{Port number}`.
        self.domain_endpoint = domain_endpoint
        # The maximum Internet traffic in the instance.
        self.eip_max = eip_max
        # The default endpoint of the instance in IP address mode. ApsaraMQ for Kafka instances support endpoints in domain name mode and IP address mode.
        # 
        # *   Endpoints in domain name mode: An endpoint in this mode consists of the domain name of the instance and a port number. The format of an endpoint in this mode is `{Instance domain name}:{Port number}`.
        # *   Endpoints in IP address mode: An endpoint in this mode consists of the IP address of the broker and a port number. The format of an endpoint in this mode is `{Broker IP address}:{Port number}`.
        self.end_point = end_point
        # The time when the instance expires. Unit: milliseconds.
        self.expired_time = expired_time
        # The instance ID.
        self.instance_id = instance_id
        # The maximum traffic in the instance.
        self.io_max = io_max
        # The maximum read traffic in the instance. Unit: Mbit/s.
        self.io_max_read = io_max_read
        # The traffic specification.
        self.io_max_spec = io_max_spec
        # The maximum write traffic. Unit: Mbit/s.
        self.io_max_write = io_max_write
        # The ID of the key that is used for disk encryption in the region where the instance is deployed.
        self.kms_key_id = kms_key_id
        # The retention period of messages in the instance. Unit: hours.
        self.msg_retain = msg_retain
        # The instance name.
        self.name = name
        # The billing method of the instance. Valid values:
        # 
        # *   **0**: the subscription billing method
        # *   **1**: the pay-as-you-go billing method
        # *   **3**: the pay-as-you-go billing method for serverless ApsaraMQ for Kafka V3 instances
        # *   **4**: the pay-as-you-go billing method for ApsaraMQ for Confluent instances
        self.paid_type = paid_type
        # The ID of the region where the instance resides.
        self.region_id = region_id
        # The traffic reserved for message publishing. Unit: MB/s.
        # 
        # >  This parameter is returned only if the instance is a serverless ApsaraMQ for Kafka V3 instance.
        self.reserved_publish_capacity = reserved_publish_capacity
        # The traffic reserved for message subscription. Unit: MB/s.
        # 
        # >  This parameter is returned only if the instance is a serverless ApsaraMQ for Kafka V3 instance.
        self.reserved_subscribe_capacity = reserved_subscribe_capacity
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The Simple Authentication and Security Layer (SASL) endpoint of the instance in domain name mode. ApsaraMQ for Kafka instances support endpoints in domain name mode and IP address mode.
        # 
        # *   Endpoints in domain name mode: An endpoint in this mode consists of the domain name of the instance and a port number. The format of an endpoint in this mode is `{Instance domain name}:{Port number}`.
        # *   Endpoints in IP address mode: An endpoint in this mode consists of the IP address of the broker and a port number. The format of an endpoint in this mode is `{Broker IP address}:{Port number}`.
        self.sasl_domain_endpoint = sasl_domain_endpoint
        # The security group to which the instance belongs.
        # 
        # *   If the instance is deployed in the ApsaraMQ for Kafka console or by calling the [StartInstance](https://help.aliyun.com/document_detail/157786.html) operation without a security group configured, no value is returned.
        # *   If the instance is deployed by calling the [StartInstance](https://help.aliyun.com/document_detail/157786.html) operation with a security group configured, the returned value is the configured security group.
        self.security_group = security_group
        # The instance version. Valid values: v2, v3, and confluent.
        self.series = series
        # >  This parameter is out of date. We recommend that you refer to the ViewInstanceStatusCode parameter.
        # 
        # The instance status. Valid values:
        # 
        # *   **0**: pending
        # *   **1**: preparing hardware resources
        # *   **2**: initializing
        # *   **3**: starting
        # *   **5**: running
        # *   **6**: migrating
        # *   **7**: ready for upgrade
        # *   **8**: upgrading
        # *   **9**: ready for change
        # *   **10**: released
        # *   **11**: changing
        # *   **15**: expired
        # *   **30**: scaling
        self.service_status = service_status
        # The instance edition. Valid values:
        # 
        # *   **professional**: Professional Edition (High Write)
        # *   **professionalForHighRead**: Professional Edition (High Read)
        # *   **normal**: Standard Edition
        self.spec_type = spec_type
        # The SSL endpoint of the instance in domain name mode. ApsaraMQ for Kafka instances support endpoints in domain name mode and IP address mode.
        # 
        # *   Endpoints in domain name mode: An endpoint in this mode consists of the domain name of the instance and a port number. The format of an endpoint in this mode is `{Instance domain name}:{Port number}`.
        # *   Endpoints in IP address mode: An endpoint in this mode consists of the IP address of the broker and a port number. The format of an endpoint in this mode is `{Broker IP address}:{Port number}`.
        self.ssl_domain_endpoint = ssl_domain_endpoint
        # The Secure Sockets Layer (SSL) endpoint of the instance in IP address mode. ApsaraMQ for Kafka instances support endpoints in domain name mode and IP address mode.
        # 
        # *   Endpoints in domain name mode: An endpoint in this mode consists of the domain name of the instance and a port number. The format of an endpoint in this mode is `{Instance domain name}:{Port number}`.
        # *   Endpoints in IP address mode: An endpoint in this mode consists of the IP address of the broker and a port number. The format of an endpoint in this mode is `{Broker IP address}:{Port number}`.
        self.ssl_end_point = ssl_end_point
        # The zone ID.
        self.standard_zone_id = standard_zone_id
        # The tags.
        self.tags = tags
        # The maximum number of topics on the instance.
        self.topic_num_limit = topic_num_limit
        # The upgrade information about the instance.
        self.upgrade_service_detail_info = upgrade_service_detail_info
        # The number of used groups.
        self.used_group_count = used_group_count
        # The number of used partitions.
        self.used_partition_count = used_partition_count
        # The number of used topics.
        self.used_topic_count = used_topic_count
        # The ID of the vSwitch to which the instance belongs.
        self.v_switch_id = v_switch_id
        # The instance status. The valid values are consistent with the values displayed in the ApsaraMQ for Kafka console. This parameter is used in the new version of ApsaraMQ for Kafka.
        # 
        # Valid values:
        # 
        # *   **0**: pending
        # *   **1**: deploying
        # *   **2**: running
        # *   **3**: stopped
        # *   **4**: expiring
        # *   **5**: expired
        # *   **6**: released
        # *   **7**: upgrading
        # *   **8**: migrating
        # *   **21**: stopping
        # *   **22**: starting
        # *   **23**: releasing
        # *   **30**: auto scaling
        # *   **101**: deployment failed
        # *   **102**: upgrade failed
        # *   **103**: migration failed
        self.view_instance_status_code = view_instance_status_code
        # The virtual private cloud (VPC) ID.
        self.vpc_id = vpc_id
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        if self.confluent_config:
            self.confluent_config.validate()
        if self.tags:
            self.tags.validate()
        if self.upgrade_service_detail_info:
            self.upgrade_service_detail_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all_config is not None:
            result['AllConfig'] = self.all_config
        if self.confluent_config is not None:
            result['ConfluentConfig'] = self.confluent_config.to_map()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deploy_type is not None:
            result['DeployType'] = self.deploy_type
        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size
        if self.disk_type is not None:
            result['DiskType'] = self.disk_type
        if self.domain_endpoint is not None:
            result['DomainEndpoint'] = self.domain_endpoint
        if self.eip_max is not None:
            result['EipMax'] = self.eip_max
        if self.end_point is not None:
            result['EndPoint'] = self.end_point
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.io_max is not None:
            result['IoMax'] = self.io_max
        if self.io_max_read is not None:
            result['IoMaxRead'] = self.io_max_read
        if self.io_max_spec is not None:
            result['IoMaxSpec'] = self.io_max_spec
        if self.io_max_write is not None:
            result['IoMaxWrite'] = self.io_max_write
        if self.kms_key_id is not None:
            result['KmsKeyId'] = self.kms_key_id
        if self.msg_retain is not None:
            result['MsgRetain'] = self.msg_retain
        if self.name is not None:
            result['Name'] = self.name
        if self.paid_type is not None:
            result['PaidType'] = self.paid_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.reserved_publish_capacity is not None:
            result['ReservedPublishCapacity'] = self.reserved_publish_capacity
        if self.reserved_subscribe_capacity is not None:
            result['ReservedSubscribeCapacity'] = self.reserved_subscribe_capacity
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.sasl_domain_endpoint is not None:
            result['SaslDomainEndpoint'] = self.sasl_domain_endpoint
        if self.security_group is not None:
            result['SecurityGroup'] = self.security_group
        if self.series is not None:
            result['Series'] = self.series
        if self.service_status is not None:
            result['ServiceStatus'] = self.service_status
        if self.spec_type is not None:
            result['SpecType'] = self.spec_type
        if self.ssl_domain_endpoint is not None:
            result['SslDomainEndpoint'] = self.ssl_domain_endpoint
        if self.ssl_end_point is not None:
            result['SslEndPoint'] = self.ssl_end_point
        if self.standard_zone_id is not None:
            result['StandardZoneId'] = self.standard_zone_id
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        if self.topic_num_limit is not None:
            result['TopicNumLimit'] = self.topic_num_limit
        if self.upgrade_service_detail_info is not None:
            result['UpgradeServiceDetailInfo'] = self.upgrade_service_detail_info.to_map()
        if self.used_group_count is not None:
            result['UsedGroupCount'] = self.used_group_count
        if self.used_partition_count is not None:
            result['UsedPartitionCount'] = self.used_partition_count
        if self.used_topic_count is not None:
            result['UsedTopicCount'] = self.used_topic_count
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.view_instance_status_code is not None:
            result['ViewInstanceStatusCode'] = self.view_instance_status_code
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllConfig') is not None:
            self.all_config = m.get('AllConfig')
        if m.get('ConfluentConfig') is not None:
            temp_model = GetInstanceListResponseBodyInstanceListInstanceVOConfluentConfig()
            self.confluent_config = temp_model.from_map(m['ConfluentConfig'])
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DeployType') is not None:
            self.deploy_type = m.get('DeployType')
        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')
        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')
        if m.get('DomainEndpoint') is not None:
            self.domain_endpoint = m.get('DomainEndpoint')
        if m.get('EipMax') is not None:
            self.eip_max = m.get('EipMax')
        if m.get('EndPoint') is not None:
            self.end_point = m.get('EndPoint')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IoMax') is not None:
            self.io_max = m.get('IoMax')
        if m.get('IoMaxRead') is not None:
            self.io_max_read = m.get('IoMaxRead')
        if m.get('IoMaxSpec') is not None:
            self.io_max_spec = m.get('IoMaxSpec')
        if m.get('IoMaxWrite') is not None:
            self.io_max_write = m.get('IoMaxWrite')
        if m.get('KmsKeyId') is not None:
            self.kms_key_id = m.get('KmsKeyId')
        if m.get('MsgRetain') is not None:
            self.msg_retain = m.get('MsgRetain')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PaidType') is not None:
            self.paid_type = m.get('PaidType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ReservedPublishCapacity') is not None:
            self.reserved_publish_capacity = m.get('ReservedPublishCapacity')
        if m.get('ReservedSubscribeCapacity') is not None:
            self.reserved_subscribe_capacity = m.get('ReservedSubscribeCapacity')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SaslDomainEndpoint') is not None:
            self.sasl_domain_endpoint = m.get('SaslDomainEndpoint')
        if m.get('SecurityGroup') is not None:
            self.security_group = m.get('SecurityGroup')
        if m.get('Series') is not None:
            self.series = m.get('Series')
        if m.get('ServiceStatus') is not None:
            self.service_status = m.get('ServiceStatus')
        if m.get('SpecType') is not None:
            self.spec_type = m.get('SpecType')
        if m.get('SslDomainEndpoint') is not None:
            self.ssl_domain_endpoint = m.get('SslDomainEndpoint')
        if m.get('SslEndPoint') is not None:
            self.ssl_end_point = m.get('SslEndPoint')
        if m.get('StandardZoneId') is not None:
            self.standard_zone_id = m.get('StandardZoneId')
        if m.get('Tags') is not None:
            temp_model = GetInstanceListResponseBodyInstanceListInstanceVOTags()
            self.tags = temp_model.from_map(m['Tags'])
        if m.get('TopicNumLimit') is not None:
            self.topic_num_limit = m.get('TopicNumLimit')
        if m.get('UpgradeServiceDetailInfo') is not None:
            temp_model = GetInstanceListResponseBodyInstanceListInstanceVOUpgradeServiceDetailInfo()
            self.upgrade_service_detail_info = temp_model.from_map(m['UpgradeServiceDetailInfo'])
        if m.get('UsedGroupCount') is not None:
            self.used_group_count = m.get('UsedGroupCount')
        if m.get('UsedPartitionCount') is not None:
            self.used_partition_count = m.get('UsedPartitionCount')
        if m.get('UsedTopicCount') is not None:
            self.used_topic_count = m.get('UsedTopicCount')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ViewInstanceStatusCode') is not None:
            self.view_instance_status_code = m.get('ViewInstanceStatusCode')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class GetInstanceListResponseBodyInstanceList(TeaModel):
    def __init__(
        self,
        instance_vo: List[GetInstanceListResponseBodyInstanceListInstanceVO] = None,
    ):
        self.instance_vo = instance_vo

    def validate(self):
        if self.instance_vo:
            for k in self.instance_vo:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InstanceVO'] = []
        if self.instance_vo is not None:
            for k in self.instance_vo:
                result['InstanceVO'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_vo = []
        if m.get('InstanceVO') is not None:
            for k in m.get('InstanceVO'):
                temp_model = GetInstanceListResponseBodyInstanceListInstanceVO()
                self.instance_vo.append(temp_model.from_map(k))
        return self


class GetInstanceListResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        instance_list: GetInstanceListResponseBodyInstanceList = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code returned. The HTTP status code 200 indicates that the call is successful.
        self.code = code
        # The instances.
        self.instance_list = instance_list
        # The message returned.
        self.message = message
        # The ID of the region.
        self.request_id = request_id
        # Indicates whether the call was successful.
        self.success = success

    def validate(self):
        if self.instance_list:
            self.instance_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.instance_list is not None:
            result['InstanceList'] = self.instance_list.to_map()
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
        if m.get('InstanceList') is not None:
            temp_model = GetInstanceListResponseBodyInstanceList()
            self.instance_list = temp_model.from_map(m['InstanceList'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetInstanceListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetInstanceListResponseBody = None,
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
            temp_model = GetInstanceListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetQuotaTipRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
    ):
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the region in which the instance resides.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetQuotaTipResponseBodyQuotaData(TeaModel):
    def __init__(
        self,
        group_left: int = None,
        group_used: int = None,
        is_partition_buy: int = None,
        partition_left: int = None,
        partition_num_of_buy: int = None,
        partition_quota: int = None,
        partition_used: int = None,
        topic_left: int = None,
        topic_num_of_buy: int = None,
        topic_quota: int = None,
        topic_used: int = None,
    ):
        # The number of available groups.
        self.group_left = group_left
        # The number of used groups.
        self.group_used = group_used
        # The method that you use to purchase partitions. Valid values:
        # 
        # *   0: indicates that the instance is purchased based on topics.
        # *   1: indicates that the instance is purchased based on partitions.
        self.is_partition_buy = is_partition_buy
        # The number of available partitions.
        self.partition_left = partition_left
        # The number of purchased partitions.
        self.partition_num_of_buy = partition_num_of_buy
        # The quota of partitions.
        self.partition_quota = partition_quota
        # The number of used partitions.
        self.partition_used = partition_used
        # The number of available topics.
        self.topic_left = topic_left
        # The number of purchased topics.
        self.topic_num_of_buy = topic_num_of_buy
        # The quota of topics.
        self.topic_quota = topic_quota
        # The number of used topics.
        self.topic_used = topic_used

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_left is not None:
            result['GroupLeft'] = self.group_left
        if self.group_used is not None:
            result['GroupUsed'] = self.group_used
        if self.is_partition_buy is not None:
            result['IsPartitionBuy'] = self.is_partition_buy
        if self.partition_left is not None:
            result['PartitionLeft'] = self.partition_left
        if self.partition_num_of_buy is not None:
            result['PartitionNumOfBuy'] = self.partition_num_of_buy
        if self.partition_quota is not None:
            result['PartitionQuota'] = self.partition_quota
        if self.partition_used is not None:
            result['PartitionUsed'] = self.partition_used
        if self.topic_left is not None:
            result['TopicLeft'] = self.topic_left
        if self.topic_num_of_buy is not None:
            result['TopicNumOfBuy'] = self.topic_num_of_buy
        if self.topic_quota is not None:
            result['TopicQuota'] = self.topic_quota
        if self.topic_used is not None:
            result['TopicUsed'] = self.topic_used
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupLeft') is not None:
            self.group_left = m.get('GroupLeft')
        if m.get('GroupUsed') is not None:
            self.group_used = m.get('GroupUsed')
        if m.get('IsPartitionBuy') is not None:
            self.is_partition_buy = m.get('IsPartitionBuy')
        if m.get('PartitionLeft') is not None:
            self.partition_left = m.get('PartitionLeft')
        if m.get('PartitionNumOfBuy') is not None:
            self.partition_num_of_buy = m.get('PartitionNumOfBuy')
        if m.get('PartitionQuota') is not None:
            self.partition_quota = m.get('PartitionQuota')
        if m.get('PartitionUsed') is not None:
            self.partition_used = m.get('PartitionUsed')
        if m.get('TopicLeft') is not None:
            self.topic_left = m.get('TopicLeft')
        if m.get('TopicNumOfBuy') is not None:
            self.topic_num_of_buy = m.get('TopicNumOfBuy')
        if m.get('TopicQuota') is not None:
            self.topic_quota = m.get('TopicQuota')
        if m.get('TopicUsed') is not None:
            self.topic_used = m.get('TopicUsed')
        return self


class GetQuotaTipResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        quota_data: GetQuotaTipResponseBodyQuotaData = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code returned. The HTTP status code 200 indicates that the request is successful.
        self.code = code
        # The additional message. This message is typically used to describe API call failures for troubleshooting.
        self.message = message
        # The quota.
        self.quota_data = quota_data
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        if self.quota_data:
            self.quota_data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.quota_data is not None:
            result['QuotaData'] = self.quota_data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('QuotaData') is not None:
            temp_model = GetQuotaTipResponseBodyQuotaData()
            self.quota_data = temp_model.from_map(m['QuotaData'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetQuotaTipResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetQuotaTipResponseBody = None,
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
            temp_model = GetQuotaTipResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTopicListRequest(TeaModel):
    def __init__(
        self,
        current_page: str = None,
        instance_id: str = None,
        page_size: str = None,
        region_id: str = None,
        topic: str = None,
    ):
        # The page number. Default value: 1
        self.current_page = current_page
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The number of entries to return on each page. Default value: 10.
        self.page_size = page_size
        # The region ID of the instance to which the topics that you want to query belong.
        self.region_id = region_id
        # The name of the topic that you want to query.
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class GetTopicListResponseBodyTopicListTopicVOTagsTagVO(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetTopicListResponseBodyTopicListTopicVOTags(TeaModel):
    def __init__(
        self,
        tag_vo: List[GetTopicListResponseBodyTopicListTopicVOTagsTagVO] = None,
    ):
        self.tag_vo = tag_vo

    def validate(self):
        if self.tag_vo:
            for k in self.tag_vo:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TagVO'] = []
        if self.tag_vo is not None:
            for k in self.tag_vo:
                result['TagVO'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag_vo = []
        if m.get('TagVO') is not None:
            for k in m.get('TagVO'):
                temp_model = GetTopicListResponseBodyTopicListTopicVOTagsTagVO()
                self.tag_vo.append(temp_model.from_map(k))
        return self


class GetTopicListResponseBodyTopicListTopicVO(TeaModel):
    def __init__(
        self,
        auto_create: bool = None,
        compact_topic: bool = None,
        create_time: int = None,
        instance_id: str = None,
        local_topic: bool = None,
        partition_num: int = None,
        region_id: str = None,
        remark: str = None,
        status: int = None,
        status_name: str = None,
        tags: GetTopicListResponseBodyTopicListTopicVOTags = None,
        topic: str = None,
        topic_config: str = None,
    ):
        # Indicates whether the topic was automatically created.
        self.auto_create = auto_create
        # The log cleanup policy for the topic. This parameter is returned only if **LocalTopic** is set to **true**. Valid values:
        # 
        # *   false: the default log cleanup policy.
        # *   true: the Apache Kafka log compaction policy.
        self.compact_topic = compact_topic
        # The timestamp that indicates when the topic was created. Unit: milliseconds.
        self.create_time = create_time
        # The instance ID.
        self.instance_id = instance_id
        # The storage type that is used for the topic. Valid values:
        # 
        # *   false: cloud storage
        # *   true: local storage
        self.local_topic = local_topic
        # The number of partitions in the topic.
        self.partition_num = partition_num
        # The ID of the region where the instance resides.
        self.region_id = region_id
        # The topic description. Valid values:
        # 
        # *   The description can contain only letters, digits, hyphens (-), and underscores (_).
        # *   The description must be 3 to 64 characters in length.
        self.remark = remark
        # The topic status. Valid value:
        # 
        # **0**: running.
        # 
        # If the topic is deleted, this parameter is not returned.
        self.status = status
        # The topic status. Valid value:
        # 
        # **Running**.
        # 
        # If the topic is deleted, this parameter is not returned.
        self.status_name = status_name
        # The tags.
        self.tags = tags
        # The topic name. Valid values:
        # 
        # *   The name can contain only letters, digits, hyphens (-), and underscores (_).
        # *   The name must be 3 to 64 characters in length. If the name contains more than 64 characters, the system automatically truncates the name.
        self.topic = topic
        # The topic configuration.
        self.topic_config = topic_config

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_create is not None:
            result['AutoCreate'] = self.auto_create
        if self.compact_topic is not None:
            result['CompactTopic'] = self.compact_topic
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.local_topic is not None:
            result['LocalTopic'] = self.local_topic
        if self.partition_num is not None:
            result['PartitionNum'] = self.partition_num
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.status is not None:
            result['Status'] = self.status
        if self.status_name is not None:
            result['StatusName'] = self.status_name
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.topic_config is not None:
            result['TopicConfig'] = self.topic_config
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoCreate') is not None:
            self.auto_create = m.get('AutoCreate')
        if m.get('CompactTopic') is not None:
            self.compact_topic = m.get('CompactTopic')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('LocalTopic') is not None:
            self.local_topic = m.get('LocalTopic')
        if m.get('PartitionNum') is not None:
            self.partition_num = m.get('PartitionNum')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusName') is not None:
            self.status_name = m.get('StatusName')
        if m.get('Tags') is not None:
            temp_model = GetTopicListResponseBodyTopicListTopicVOTags()
            self.tags = temp_model.from_map(m['Tags'])
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('TopicConfig') is not None:
            self.topic_config = m.get('TopicConfig')
        return self


class GetTopicListResponseBodyTopicList(TeaModel):
    def __init__(
        self,
        topic_vo: List[GetTopicListResponseBodyTopicListTopicVO] = None,
    ):
        self.topic_vo = topic_vo

    def validate(self):
        if self.topic_vo:
            for k in self.topic_vo:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TopicVO'] = []
        if self.topic_vo is not None:
            for k in self.topic_vo:
                result['TopicVO'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.topic_vo = []
        if m.get('TopicVO') is not None:
            for k in m.get('TopicVO'):
                temp_model = GetTopicListResponseBodyTopicListTopicVO()
                self.topic_vo.append(temp_model.from_map(k))
        return self


class GetTopicListResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        current_page: int = None,
        message: str = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        topic_list: GetTopicListResponseBodyTopicList = None,
        total: int = None,
    ):
        # The HTTP status code returned. The HTTP status code 200 indicates that the request is successful.
        self.code = code
        # The page number of the returned page.
        self.current_page = current_page
        # The message returned.
        self.message = message
        # The number of entries returned on each page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success
        # The topics.
        self.topic_list = topic_list
        # The number of topics.
        self.total = total

    def validate(self):
        if self.topic_list:
            self.topic_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.topic_list is not None:
            result['TopicList'] = self.topic_list.to_map()
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TopicList') is not None:
            temp_model = GetTopicListResponseBodyTopicList()
            self.topic_list = temp_model.from_map(m['TopicList'])
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class GetTopicListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTopicListResponseBody = None,
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
            temp_model = GetTopicListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTopicStatusRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
        topic: str = None,
    ):
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The region ID of the instance.
        self.region_id = region_id
        # The name of the topic.
        # 
        # This parameter is required.
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class GetTopicStatusResponseBodyTopicStatusOffsetTableOffsetTable(TeaModel):
    def __init__(
        self,
        last_update_timestamp: int = None,
        max_offset: int = None,
        min_offset: int = None,
        partition: int = None,
        topic: str = None,
    ):
        # The last time when the partition was modified.
        self.last_update_timestamp = last_update_timestamp
        # The latest offset in the partition of the topic.
        self.max_offset = max_offset
        # The earliest offset in the partition of the topic.
        self.min_offset = min_offset
        # The ID of the partition.
        self.partition = partition
        # The name of the topic.
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.last_update_timestamp is not None:
            result['LastUpdateTimestamp'] = self.last_update_timestamp
        if self.max_offset is not None:
            result['MaxOffset'] = self.max_offset
        if self.min_offset is not None:
            result['MinOffset'] = self.min_offset
        if self.partition is not None:
            result['Partition'] = self.partition
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LastUpdateTimestamp') is not None:
            self.last_update_timestamp = m.get('LastUpdateTimestamp')
        if m.get('MaxOffset') is not None:
            self.max_offset = m.get('MaxOffset')
        if m.get('MinOffset') is not None:
            self.min_offset = m.get('MinOffset')
        if m.get('Partition') is not None:
            self.partition = m.get('Partition')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class GetTopicStatusResponseBodyTopicStatusOffsetTable(TeaModel):
    def __init__(
        self,
        offset_table: List[GetTopicStatusResponseBodyTopicStatusOffsetTableOffsetTable] = None,
    ):
        self.offset_table = offset_table

    def validate(self):
        if self.offset_table:
            for k in self.offset_table:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['OffsetTable'] = []
        if self.offset_table is not None:
            for k in self.offset_table:
                result['OffsetTable'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.offset_table = []
        if m.get('OffsetTable') is not None:
            for k in m.get('OffsetTable'):
                temp_model = GetTopicStatusResponseBodyTopicStatusOffsetTableOffsetTable()
                self.offset_table.append(temp_model.from_map(k))
        return self


class GetTopicStatusResponseBodyTopicStatus(TeaModel):
    def __init__(
        self,
        last_time_stamp: int = None,
        offset_table: GetTopicStatusResponseBodyTopicStatusOffsetTable = None,
        total_count: int = None,
    ):
        # The time when the last consumed message was generated.
        self.last_time_stamp = last_time_stamp
        # The information about offsets in the topic.
        self.offset_table = offset_table
        # The number of messages in the topic.
        self.total_count = total_count

    def validate(self):
        if self.offset_table:
            self.offset_table.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.last_time_stamp is not None:
            result['LastTimeStamp'] = self.last_time_stamp
        if self.offset_table is not None:
            result['OffsetTable'] = self.offset_table.to_map()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LastTimeStamp') is not None:
            self.last_time_stamp = m.get('LastTimeStamp')
        if m.get('OffsetTable') is not None:
            temp_model = GetTopicStatusResponseBodyTopicStatusOffsetTable()
            self.offset_table = temp_model.from_map(m['OffsetTable'])
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetTopicStatusResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        topic_status: GetTopicStatusResponseBodyTopicStatus = None,
    ):
        # The HTTP status code returned. The HTTP status code 200 indicates that the request is successful.
        self.code = code
        # The returned message.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success
        # The status information about messages in the topic.
        self.topic_status = topic_status

    def validate(self):
        if self.topic_status:
            self.topic_status.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.topic_status is not None:
            result['TopicStatus'] = self.topic_status.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TopicStatus') is not None:
            temp_model = GetTopicStatusResponseBodyTopicStatus()
            self.topic_status = temp_model.from_map(m['TopicStatus'])
        return self


class GetTopicStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTopicStatusResponseBody = None,
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
            temp_model = GetTopicStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTopicSubscribeStatusRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
        topic: str = None,
    ):
        # The instance ID.
        # 
        # You can call the [GetInstanceList](https://help.aliyun.com/document_detail/437663.html) operation to query the list of instances.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The topic name.
        # 
        # You can call the [GetTopicList](https://help.aliyun.com/document_detail/437677.html) operation to query the list of topics.
        # 
        # This parameter is required.
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class GetTopicSubscribeStatusResponseBodyTopicSubscribeStatus(TeaModel):
    def __init__(
        self,
        consumer_groups: List[str] = None,
        topic: str = None,
    ):
        # The groups that subscribe to the topic.
        self.consumer_groups = consumer_groups
        # The topic name.
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consumer_groups is not None:
            result['ConsumerGroups'] = self.consumer_groups
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsumerGroups') is not None:
            self.consumer_groups = m.get('ConsumerGroups')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class GetTopicSubscribeStatusResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        topic_subscribe_status: GetTopicSubscribeStatusResponseBodyTopicSubscribeStatus = None,
    ):
        # The HTTP status code.
        self.code = code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success
        # The subscription details.
        self.topic_subscribe_status = topic_subscribe_status

    def validate(self):
        if self.topic_subscribe_status:
            self.topic_subscribe_status.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.topic_subscribe_status is not None:
            result['TopicSubscribeStatus'] = self.topic_subscribe_status.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TopicSubscribeStatus') is not None:
            temp_model = GetTopicSubscribeStatusResponseBodyTopicSubscribeStatus()
            self.topic_subscribe_status = temp_model.from_map(m['TopicSubscribeStatus'])
        return self


class GetTopicSubscribeStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTopicSubscribeStatusResponseBody = None,
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
            temp_model = GetTopicSubscribeStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the resource tag.
        # 
        # *   If you leave this parameter empty, the keys of all tags are matched.
        # *   The tag key can be up to 128 characters in length and cannot contain http:// or https://. The tag key cannot start with acs: or aliyun.
        self.key = key
        # The value of the resource tag.
        # 
        # *   If you leave Key empty, you must also leave this parameter empty. If you leave this parameter empty, the values of all tags are matched.
        # *   The tag value can be up to 128 characters in length and cannot contain http:// or https://. The tag value cannot start with acs: or aliyun.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListTagResourcesRequest(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        region_id: str = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag: List[ListTagResourcesRequestTag] = None,
    ):
        # The token that determines the start point of the next query.
        self.next_token = next_token
        # The ID of the region in which the resource is deployed.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource whose tags you want to query. The resource ID follows the following rules:
        # 
        # *   Instance ID: instanceId
        # *   Topic ID: Kafka_alikafka_instanceId_topic
        # *   Group ID: Kafka_alikafka_instanceId_consumerGroup
        # 
        # For example, if the instance ID is alikafka_post-cn-v0h1fgs2xxxx, the topic name is test-topic, and the group name is test-consumer-group, the resource IDs are alikafka_post-cn-v0h1fgs2xxxx, Kafka_alikafka_post-cn-v0h1fgs2xxxx_test-topic, and Kafka_alikafka_post-cn-v0h1fgs2xxxx_test-consumer-group, respectively.
        # 
        # >  You must configure one of **ResourceId** and **Tag** to query the tags that are bound to a resource. Otherwise, the request fails.
        self.resource_id = resource_id
        # The type of the resource whose tags you want to query. The value is an enumerated value. Valid values:
        # 
        # *   **INSTANCE**\
        # *   **TOPIC**\
        # *   **CONSUMERGROUP**\
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The tags.
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBodyTagResourcesTagResource(TeaModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_type: str = None,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The ID of the resource. A resource ID complies with the following rules:
        # 
        # *   The resource ID of an instance is the value of the instanceId parameter.
        # *   The resource ID of a topic is the value of the Kafka_alikafka_instanceId_topic parameter.
        # *   The resource ID of a consumer group is the value of the Kafka_alikafka_instanceId_consumerGroup parameter.
        # 
        # For example, the resources whose tags you want to query include the alikafka_post-cn-v0h1fgs2xxxx instance, the test-topic topic, and the test-consumer-group consumer group. In this case, their resource IDs are alikafka_post-cn-v0h1fgs2xxxx, Kafka_alikafka_post-cn-v0h1fgs2xxxx_test-topic, and Kafka_alikafka_post-cn-v0h1fgs2xxxx_test-consumer-group.
        self.resource_id = resource_id
        # The type of the resource. The value is an enumerated value. Valid values:
        # 
        # *   **Instance**\
        # *   **Topic**\
        # *   **Consumergroup**\
        self.resource_type = resource_type
        # The key of the tag.
        self.tag_key = tag_key
        # The value of the tag.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class ListTagResourcesResponseBodyTagResources(TeaModel):
    def __init__(
        self,
        tag_resource: List[ListTagResourcesResponseBodyTagResourcesTagResource] = None,
    ):
        self.tag_resource = tag_resource

    def validate(self):
        if self.tag_resource:
            for k in self.tag_resource:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TagResource'] = []
        if self.tag_resource is not None:
            for k in self.tag_resource:
                result['TagResource'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag_resource = []
        if m.get('TagResource') is not None:
            for k in m.get('TagResource'):
                temp_model = ListTagResourcesResponseBodyTagResourcesTagResource()
                self.tag_resource.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        tag_resources: ListTagResourcesResponseBodyTagResources = None,
    ):
        # The token that determines the start point of the next query.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # Details of the resource and tags, such as the resource ID, the resource type, tag keys, and tag values.
        self.tag_resources = tag_resources

    def validate(self):
        if self.tag_resources:
            self.tag_resources.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tag_resources is not None:
            result['TagResources'] = self.tag_resources.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TagResources') is not None:
            temp_model = ListTagResourcesResponseBodyTagResources()
            self.tag_resources = temp_model.from_map(m['TagResources'])
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


class ModifyInstanceNameRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        instance_name: str = None,
        region_id: str = None,
    ):
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The instance name. Valid values:
        # 
        # *   The name can contain only letters, digits, hyphens (-), and underscores (_).
        # *   The name must be 3 to 64 characters in length. A name that contains more than 64 characters is automatically truncated.
        # 
        # This parameter is required.
        self.instance_name = instance_name
        # The region ID of the instance.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyInstanceNameResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code. The status code 200 indicates that the call is successful.
        self.code = code
        # The returned message.
        self.message = message
        # The request ID.
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
            result['Code'] = self.code
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyInstanceNameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyInstanceNameResponseBody = None,
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
            temp_model = ModifyInstanceNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyPartitionNumRequest(TeaModel):
    def __init__(
        self,
        add_partition_num: int = None,
        instance_id: str = None,
        region_id: str = None,
        topic: str = None,
    ):
        # The number of partitions that you want to add to the topic.
        # 
        # *   The value must be an integer that is greater than 0.
        # *   To reduce the risk of data skew, we recommend that you set the value to a multiple of 6.
        # *   The number of total partitions ranges from 1 to 360.
        # 
        # This parameter is required.
        self.add_partition_num = add_partition_num
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The region ID of the instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The topic name.
        # 
        # This parameter is required.
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.add_partition_num is not None:
            result['AddPartitionNum'] = self.add_partition_num
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddPartitionNum') is not None:
            self.add_partition_num = m.get('AddPartitionNum')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class ModifyPartitionNumResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code returned. The HTTP status code 200 indicates that the request is successful.
        self.code = code
        # The message returned.
        self.message = message
        # The ID of the request.
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
            result['Code'] = self.code
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyPartitionNumResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyPartitionNumResponseBody = None,
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
            temp_model = ModifyPartitionNumResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyScheduledScalingRuleRequest(TeaModel):
    def __init__(
        self,
        enable: bool = None,
        instance_id: str = None,
        region_id: str = None,
        rule_name: str = None,
    ):
        # Specifies whether to enable the scheduled scaling rule. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        # 
        # >  If the scaling task is scheduled to execute only once and you want to enable the scheduled scaling rule, make sure that the value of this parameter is at least 30 minutes later than the current point in time.
        # 
        # This parameter is required.
        self.enable = enable
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the region where the instance resides.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The name of the scheduled scaling rule.
        # 
        # This parameter is required.
        self.rule_name = rule_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class ModifyScheduledScalingRuleResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code.
        # 
        # The value **200** indicates that the request was successful.
        self.code = code
        # The returned message.
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
            result['Code'] = self.code
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyScheduledScalingRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyScheduledScalingRuleResponseBody = None,
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
            temp_model = ModifyScheduledScalingRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyTopicRemarkRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
        remark: str = None,
        topic: str = None,
    ):
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The region ID of the instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The description of the topic.
        self.remark = remark
        # The name of the topic.
        # 
        # This parameter is required.
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class ModifyTopicRemarkResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code returned. The HTTP status code 200 indicates that the request is successful.
        self.code = code
        # The returned message.
        self.message = message
        # The ID of the request.
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
            result['Code'] = self.code
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyTopicRemarkResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyTopicRemarkResponseBody = None,
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
            temp_model = ModifyTopicRemarkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryMessageRequest(TeaModel):
    def __init__(
        self,
        begin_time: int = None,
        instance_id: str = None,
        offset: str = None,
        partition: str = None,
        query_type: str = None,
        region_id: str = None,
        topic: str = None,
    ):
        # The beginning of the time range to query. The value of this parameter is a UNIX timestamp in milliseconds.
        self.begin_time = begin_time
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The consumer offset of the partition.
        self.offset = offset
        # The partition ID.
        self.partition = partition
        # The query type. Valid values:
        # 
        # *   byOffset: queries messages by offset. If you select this value, you must configure Partition and Offset.
        # *   byTimestamp: queries messages by time. If you select this value, you must configure BeginTime.
        # 
        # This parameter is required.
        self.query_type = query_type
        # The ID of the region where the resource resides.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The topic name.
        # 
        # This parameter is required.
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.offset is not None:
            result['Offset'] = self.offset
        if self.partition is not None:
            result['Partition'] = self.partition
        if self.query_type is not None:
            result['QueryType'] = self.query_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')
        if m.get('Partition') is not None:
            self.partition = m.get('Partition')
        if m.get('QueryType') is not None:
            self.query_type = m.get('QueryType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class QueryMessageResponseBodyMessageList(TeaModel):
    def __init__(
        self,
        checksum: int = None,
        key: str = None,
        key_truncated: bool = None,
        offset: int = None,
        partition: int = None,
        serialized_key_size: int = None,
        serialized_value_size: int = None,
        timestamp: int = None,
        timestamp_type: str = None,
        topic: str = None,
        truncated_key_size: int = None,
        truncated_value_size: int = None,
        value: str = None,
        value_truncated: bool = None,
    ):
        # The check value of the chaincode.
        self.checksum = checksum
        # The message key.
        self.key = key
        # Indicates whether the key is truncated.
        self.key_truncated = key_truncated
        # The consumer offset of the partition.
        self.offset = offset
        # The partition ID.
        self.partition = partition
        # The size of the key after serialization. Unit: bytes.
        self.serialized_key_size = serialized_key_size
        # The size of the value after serialization. Unit: bytes.
        self.serialized_value_size = serialized_value_size
        # The time when the message was created. The value of this parameter is a UNIX timestamp in milliseconds.
        self.timestamp = timestamp
        # The time type.
        self.timestamp_type = timestamp_type
        # The topic name.
        self.topic = topic
        # The truncated size of the message key. Unit: bytes.
        # 
        # >  A maximum of 1 KB of content can be displayed for each message. Content that exceeds 1 KB is automatically truncated. For more information, see [Query messages](https://help.aliyun.com/document_detail/113172.html).
        self.truncated_key_size = truncated_key_size
        # The truncated size of the message value. Unit: bytes.
        # 
        # >  A maximum of 1 KB of content can be displayed for each message. Content that exceeds 1 KB is automatically truncated. For more information, see [Query messages](https://help.aliyun.com/document_detail/113172.html).
        self.truncated_value_size = truncated_value_size
        # The message value.
        self.value = value
        # Indicates whether the value is truncated.
        self.value_truncated = value_truncated

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.checksum is not None:
            result['Checksum'] = self.checksum
        if self.key is not None:
            result['Key'] = self.key
        if self.key_truncated is not None:
            result['KeyTruncated'] = self.key_truncated
        if self.offset is not None:
            result['Offset'] = self.offset
        if self.partition is not None:
            result['Partition'] = self.partition
        if self.serialized_key_size is not None:
            result['SerializedKeySize'] = self.serialized_key_size
        if self.serialized_value_size is not None:
            result['SerializedValueSize'] = self.serialized_value_size
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.timestamp_type is not None:
            result['TimestampType'] = self.timestamp_type
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.truncated_key_size is not None:
            result['TruncatedKeySize'] = self.truncated_key_size
        if self.truncated_value_size is not None:
            result['TruncatedValueSize'] = self.truncated_value_size
        if self.value is not None:
            result['Value'] = self.value
        if self.value_truncated is not None:
            result['ValueTruncated'] = self.value_truncated
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Checksum') is not None:
            self.checksum = m.get('Checksum')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('KeyTruncated') is not None:
            self.key_truncated = m.get('KeyTruncated')
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')
        if m.get('Partition') is not None:
            self.partition = m.get('Partition')
        if m.get('SerializedKeySize') is not None:
            self.serialized_key_size = m.get('SerializedKeySize')
        if m.get('SerializedValueSize') is not None:
            self.serialized_value_size = m.get('SerializedValueSize')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('TimestampType') is not None:
            self.timestamp_type = m.get('TimestampType')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('TruncatedKeySize') is not None:
            self.truncated_key_size = m.get('TruncatedKeySize')
        if m.get('TruncatedValueSize') is not None:
            self.truncated_value_size = m.get('TruncatedValueSize')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('ValueTruncated') is not None:
            self.value_truncated = m.get('ValueTruncated')
        return self


class QueryMessageResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        message_list: List[QueryMessageResponseBodyMessageList] = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The returned HTTP status code. If the request is successful, 200 is returned.
        self.code = code
        # The returned message.
        self.message = message
        # The messages.
        self.message_list = message_list
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.success = success

    def validate(self):
        if self.message_list:
            for k in self.message_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        result['MessageList'] = []
        if self.message_list is not None:
            for k in self.message_list:
                result['MessageList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        self.message_list = []
        if m.get('MessageList') is not None:
            for k in m.get('MessageList'):
                temp_model = QueryMessageResponseBodyMessageList()
                self.message_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryMessageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryMessageResponseBody = None,
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
            temp_model = QueryMessageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReleaseInstanceRequest(TeaModel):
    def __init__(
        self,
        force_delete_instance: bool = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        # Specifies whether to immediately release the physical resources of the instance. Valid values:
        # 
        # *   **true**: The physical resources of the instance are immediately released.
        # *   **false**: The physical resources of the instance are retained for a period of time before they are released.
        self.force_delete_instance = force_delete_instance
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The region ID of the instance.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.force_delete_instance is not None:
            result['ForceDeleteInstance'] = self.force_delete_instance
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ForceDeleteInstance') is not None:
            self.force_delete_instance = m.get('ForceDeleteInstance')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ReleaseInstanceResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code returned. The HTTP status code 200 indicates that the request is successful.
        self.code = code
        # The returned message.
        self.message = message
        # The ID of the request.
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
            result['Code'] = self.code
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ReleaseInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReleaseInstanceResponseBody = None,
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
            temp_model = ReleaseInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReopenInstanceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
    ):
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the region where the instance resides.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ReopenInstanceResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The returned HTTP status code. If the request is successful, 200 is returned.
        self.code = code
        # The returned message.
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
            result['Code'] = self.code
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ReopenInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReopenInstanceResponseBody = None,
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
            temp_model = ReopenInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartInstanceRequest(TeaModel):
    def __init__(
        self,
        config: str = None,
        cross_zone: bool = None,
        deploy_module: str = None,
        instance_id: str = None,
        is_eip_inner: bool = None,
        is_force_selected_zones: bool = None,
        is_set_user_and_password: bool = None,
        kmskey_id: str = None,
        name: str = None,
        notifier: str = None,
        password: str = None,
        region_id: str = None,
        security_group: str = None,
        selected_zones: str = None,
        service_version: str = None,
        user_phone_num: str = None,
        username: str = None,
        v_switch_id: str = None,
        v_switch_ids: List[str] = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        # The initial configurations of the ApsaraMQ for Kafka instance. The values must be valid JSON strings. If you do not specify this parameter, it is left empty.
        # 
        # > - You cannot configure this parameter when you deploy an ApsaraMQ for Confluent instance.
        # > - You cannot configure enable.acl for instances whose versions are earlier than 2.2.0.
        # 
        # The **Config** parameter supports the following parameters:
        # 
        # *   **enable.vpc_sasl_ssl**: specifies whether to enable VPC transmission encryption. Valid values:
        # 
        #     *   **true**: enables VPC transmission encryption. If you enable VPC transmission encryption, you must also enable access control list (ACL).
        #     *   **false**: disables VPC transmission encryption. This is the default value.
        # 
        # *   **enable.acl**: specifies whether to enable ACL. Valid values:
        # 
        #     *   **true**: enables ACL.
        #     *   **false**: disables the ACL feature. This is the default value.
        # 
        # *   **kafka.log.retention.hours**: the maximum message retention period when the disk capacity is sufficient. Unit: hours. Valid values: 24 to 480. Default value: **72**. When the disk usage reaches 85%, the disk capacity is insufficient. In this case, the system deletes the earliest stored messages to ensure service availability.
        # 
        # *   **kafka.message.max.bytes**: the maximum size of a message that can be sent and received by ApsaraMQ for Kafka. Unit: bytes. Valid values: 1048576 to 10485760. Default value: **1048576**. Before you change the maximum message size to a new value, make sure that the new value matches the configurations of the producers and consumers.
        self.config = config
        # Specifies whether cross-zone deployment is required. Valid values:
        # 
        # *   true
        # *   false
        # 
        # Default value: true.
        self.cross_zone = cross_zone
        # The deployment mode. If the instance is an ApsaraMQ for Kafka V2 instance, this parameter is required. If the instance is an ApsaraMQ for Kafka V3 instance or an ApsaraMQ for Confluent instance, this parameter is optional. Valid values:
        # 
        # *   **vpc**: deploys the instance in a virtual private cloud (VPC).
        # *   **eip**: deploys the instance over the Internet and in the VPC.
        # 
        # The deployment mode of the ApsaraMQ for Kafka instance must be consistent with the instance type. If the instance is a VPC-connected instance, set this parameter to **vpc**. If the instance is an Internet- and VPC-connected instance, set this parameter to **eip**.
        self.deploy_module = deploy_module
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Specifies whether the instance supports elastic IP addresses (EIPs). Valid values:
        # 
        # *   **true**: supports EIPs and allows access from the Internet and a VPC.
        # *   **false**: does not support EIPs and allows access only from a VPC.
        # 
        # The value of this parameter must match the type of the instance. For example, if the instance allows access only from a VPC, set this parameter to **false**.
        self.is_eip_inner = is_eip_inner
        # Specifies whether to forcibly deploy the instance in the selected zones.
        self.is_force_selected_zones = is_force_selected_zones
        # Specifies whether to set a new username and password. Valid values:
        # 
        # *   **true**: sets a new username and password.
        # *   **false**: does not set a new username or password.
        # 
        # This parameter is available only if you deploy an instance that allows access from the Internet and a VPC.
        self.is_set_user_and_password = is_set_user_and_password
        # The ID of the key that is used for disk encryption in the region where the instance is deployed. You can obtain the ID of the key in the [Key Management Service (KMS) console](https://kms.console.aliyun.com/?spm=a2c4g.11186623.2.5.336745b8hfiU21) or create a key. For more information, see [Manage CMKs](https://help.aliyun.com/document_detail/181610.html).
        # 
        # If this parameter is configured, disk encryption is enabled for the instance. You cannot disable disk encryption after disk encryption is enabled. When you call this operation, the system checks whether the AliyunServiceRoleForAlikafkaInstanceEncryption service-linked role is created. If the role is not created, the system automatically creates the role. For more information, see [Service-linked roles](https://help.aliyun.com/document_detail/190460.html).
        # 
        # > When you deploy a serverless ApsaraMQ for Kafka V3 instance, you cannot configure this parameter.
        self.kmskey_id = kmskey_id
        # The name of the instance.
        # 
        # >  If you specify a value for this parameter, make sure that the specified value is unique in the region of the instance.
        self.name = name
        # The alert contact.
        self.notifier = notifier
        # The instance password.
        # 
        # *   This parameter is available only for Internet- and VPC- connected ApsaraMQ for Kafka V2 and V3 instances.
        # *   If the instance is an ApsaraMQ for Confluent instance, this parameter is required. The value of this parameter must be 8 to 32 characters in length and contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. The following special characters are supported: ! @ # $ % ^ & \\* () _ + - =\
        self.password = password
        # The region ID of the instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The security group of the instance.
        # 
        # If you do not specify this parameter, ApsaraMQ for Kafka automatically configures a security group for your instance. If you specify this parameter, you must create a security group in advance. For more information, see [Create a security group](https://help.aliyun.com/document_detail/25468.html).
        self.security_group = security_group
        # The two-dimensional arrays that consist of the candidate set for primary zones and the candidate set for secondary zones. Custom code in the `zone {zone}` format and standard code in the `cn-RegionID-{zone}` format are supported.
        # 
        # *   If you set CrossZone to true and specify Zone H and Zone F as the candidate set for primary zones and Zone K as the candidate set for secondary zones, set this parameter to `[["zoneh","zonef"],["zonek"]]`.
        # 
        # > If you specify multiple zones as the primary or secondary zones, the system deploys the instance in one of the zones without prioritizing them. For example, if you set this parameter to `[["zoneh","zonef"],["zonek"]]`, the primary zone in which the instance is deployed can be Zone H or Zone F, and the secondary zone is Zone K.
        # 
        # *   If you set CrossZone to false and want to deploy the instance in Zone K, set this parameter to `[["zonek"],[]]`. In this case, the value of this parameter must still be two-dimensional arrays, but the array that specifies the candidate for secondary zones is left empty.
        self.selected_zones = selected_zones
        # The version of the ApsaraMQ for Kafka instance. Valid values:
        # 
        # *   ApsaraMQ for Kafka V2 instances: 2.2.0 and 2.6.2.
        # *   ApsaraMQ for Kafka V3 instances: 3.3.1.
        # *   ApsaraMQ for Confluent instances: 7.4.0.
        # 
        # Default value:
        # 
        # *   ApsaraMQ for Kafka V2 instances: 2.2.0.
        # *   ApsaraMQ for Kafka V3 instances: 3.3.1.
        # *   ApsaraMQ for Confluent instances: 7.4.0.
        self.service_version = service_version
        # The mobile phone number of the alert contact.
        self.user_phone_num = user_phone_num
        # The instance username.
        # 
        # *   This parameter is available only for Internet- and VPC- connected ApsaraMQ for Kafka V2 and V3 instances.
        # *   If the instance is an ApsaraMQ for Confluent instance, set this parameter to root or leave this parameter empty.
        # 
        # Default value for ApsaraMQ for Kafka V2 and V3 instances: username. Default value for ApsaraMQ for Confluent instances: root.
        self.username = username
        # The ID of the vSwitch to which you want to connect the instance.
        # 
        # This parameter is required.
        self.v_switch_id = v_switch_id
        # The IDs of the vSwitches with which the instance is associated. If the instance is an ApsaraMQ for Kafka V2 or V3 instance, this parameter is required. If the instance is an ApsaraMQ for Confluent instance, you must configure one of VSwitchIds and VSwitchId. If you configure both of the parameters, the value of VSwitchIds takes effect.
        self.v_switch_ids = v_switch_ids
        # The ID of the virtual private cloud (VPC) in which you want to deploy the instance.
        # 
        # This parameter is required.
        self.vpc_id = vpc_id
        # The ID of the zone where you want to deploy the ApsaraMQ for Kafka instance.
        # 
        # *   The zone ID of the ApsaraMQ for Kafka instance must be the same as that of the vSwitch.
        # *   The value must be in the zoneX or Region ID-X format. Examples: zonea and cn-hangzhou-k.
        # 
        # >  If resources in the specified zone is insufficient, the instance may be deployed in another zone.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.cross_zone is not None:
            result['CrossZone'] = self.cross_zone
        if self.deploy_module is not None:
            result['DeployModule'] = self.deploy_module
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.is_eip_inner is not None:
            result['IsEipInner'] = self.is_eip_inner
        if self.is_force_selected_zones is not None:
            result['IsForceSelectedZones'] = self.is_force_selected_zones
        if self.is_set_user_and_password is not None:
            result['IsSetUserAndPassword'] = self.is_set_user_and_password
        if self.kmskey_id is not None:
            result['KMSKeyId'] = self.kmskey_id
        if self.name is not None:
            result['Name'] = self.name
        if self.notifier is not None:
            result['Notifier'] = self.notifier
        if self.password is not None:
            result['Password'] = self.password
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.security_group is not None:
            result['SecurityGroup'] = self.security_group
        if self.selected_zones is not None:
            result['SelectedZones'] = self.selected_zones
        if self.service_version is not None:
            result['ServiceVersion'] = self.service_version
        if self.user_phone_num is not None:
            result['UserPhoneNum'] = self.user_phone_num
        if self.username is not None:
            result['Username'] = self.username
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('CrossZone') is not None:
            self.cross_zone = m.get('CrossZone')
        if m.get('DeployModule') is not None:
            self.deploy_module = m.get('DeployModule')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IsEipInner') is not None:
            self.is_eip_inner = m.get('IsEipInner')
        if m.get('IsForceSelectedZones') is not None:
            self.is_force_selected_zones = m.get('IsForceSelectedZones')
        if m.get('IsSetUserAndPassword') is not None:
            self.is_set_user_and_password = m.get('IsSetUserAndPassword')
        if m.get('KMSKeyId') is not None:
            self.kmskey_id = m.get('KMSKeyId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Notifier') is not None:
            self.notifier = m.get('Notifier')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecurityGroup') is not None:
            self.security_group = m.get('SecurityGroup')
        if m.get('SelectedZones') is not None:
            self.selected_zones = m.get('SelectedZones')
        if m.get('ServiceVersion') is not None:
            self.service_version = m.get('ServiceVersion')
        if m.get('UserPhoneNum') is not None:
            self.user_phone_num = m.get('UserPhoneNum')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class StartInstanceResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code returned. The HTTP status code 200 indicates that the request is successful.
        self.code = code
        # The returned message.
        self.message = message
        # The ID of the request.
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
            result['Code'] = self.code
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class StartInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartInstanceResponseBody = None,
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
            temp_model = StartInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopInstanceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
    ):
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the region where the instance resides.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class StopInstanceResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The returned status code. If the request is successful, 200 is returned.
        self.code = code
        # The returned message.
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
            result['Code'] = self.code
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class StopInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopInstanceResponseBody = None,
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
            temp_model = StopInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the resource tag.
        # 
        # *   You must specify this parameter.
        # *   The tag key can be up to 128 characters in length and cannot contain `http://` or `https://`. The tag key cannot start with `acs:` or `aliyun`.
        # 
        # This parameter is required.
        self.key = key
        # The value of the resource tag.
        # 
        # *   You can leave this parameter empty.
        # *   The tag value can be up to 128 characters in length and cannot contain http:// or https://. The tag value cannot start with acs: or aliyun.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class TagResourcesRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag: List[TagResourcesRequestTag] = None,
    ):
        # The ID of the Message Queue for Apache RocketMQ instance which contains the resource to which you want to attach tags.
        self.instance_id = instance_id
        # The ID of the region in which the resource is deployed.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource IDs.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The type of the resources. The value is an enumerated value. Valid values:
        # 
        # *   **INSTANCE**\
        # *   **TOPIC**\
        # *   **CONSUMERGROUP**\
        # 
        # >  The value of this parameter is not case-sensitive.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The tags that you want to add.
        # 
        # This parameter is required.
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = TagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class TagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
        resource_id: List[str] = None,
        resource_type: str = None,
        tag_key: List[str] = None,
    ):
        # Specifies whether to detach all tags from the resource. This parameter only takes effect when the TagKey.N parameter is not configured. Default value: **false**.
        self.all = all
        # The ID of the region in which the resource is deployed.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The IDs of the resources from which you want to detach tags.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The type of the resources. Valid values:
        # 
        # *   **INSTANCE**\
        # *   **TOPIC**\
        # *   **CONSUMERGROUP**\
        # 
        # >  The value of this parameter is not case-sensitive.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The key of the resource tag.
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['All'] = self.all
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class UntagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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


class UpdateAllowedIpRequest(TeaModel):
    def __init__(
        self,
        allowed_list_ip: str = None,
        allowed_list_type: str = None,
        description: str = None,
        instance_id: str = None,
        port_range: str = None,
        region_id: str = None,
        update_type: str = None,
    ):
        # The IP addresses that you want to manage. You can specify a CIDR block. Example: **192.168.0.0/16**.
        # 
        # *   If the **UpdateType** parameter is set to **add**, specify one or more IP addresses for this parameter. Separate multiple IP addresses with commas (,).
        # *   If the **UpdateType** parameter is set to **delete**, specify only one IP address.
        # *   Exercise caution when you delete IP addresses.
        # 
        # This parameter is required.
        self.allowed_list_ip = allowed_list_ip
        # The type of the whitelist. Valid values:
        # 
        # *   **vpc**: a whitelist for access from a VPC.
        # *   **internet**: a whitelist for access from the Internet.
        # 
        # This parameter is required.
        self.allowed_list_type = allowed_list_type
        # The description of the whitelist.
        self.description = description
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The port range. Valid values:
        # 
        # *   **9092/9092**: Messages are transmitted in a virtual private cloud (VPC) by using the PLAINTEXT protocol.
        # *   **9093/9093**: Messages are transmitted over the Internet by using the SASL_SSL protocol.
        # *   **9094/9094**: Messages are transmitted in a VPC by using the SASL_PLAINTEXT protocol.
        # *   **9095/9095**: Messages are transmitted in a VPC by using the SASL_SSL protocol.
        # 
        # This parameter must correspond to **AllowdedListType**.
        # 
        # This parameter is required.
        self.port_range = port_range
        # The ID of the region where the instance resides.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The type of configuration change. Valid values:
        # 
        # *   **add**\
        # *   **delete**\
        # 
        # This parameter is required.
        self.update_type = update_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allowed_list_ip is not None:
            result['AllowedListIp'] = self.allowed_list_ip
        if self.allowed_list_type is not None:
            result['AllowedListType'] = self.allowed_list_type
        if self.description is not None:
            result['Description'] = self.description
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.port_range is not None:
            result['PortRange'] = self.port_range
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.update_type is not None:
            result['UpdateType'] = self.update_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowedListIp') is not None:
            self.allowed_list_ip = m.get('AllowedListIp')
        if m.get('AllowedListType') is not None:
            self.allowed_list_type = m.get('AllowedListType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PortRange') is not None:
            self.port_range = m.get('PortRange')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UpdateType') is not None:
            self.update_type = m.get('UpdateType')
        return self


class UpdateAllowedIpResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code that is returned. The HTTP status code 200 indicates that the request is successful.
        self.code = code
        # The message returned.
        self.message = message
        # The ID of the request.
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
            result['Code'] = self.code
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateAllowedIpResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateAllowedIpResponseBody = None,
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
            temp_model = UpdateAllowedIpResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateConsumerOffsetRequestOffsets(TeaModel):
    def __init__(
        self,
        offset: int = None,
        partition: int = None,
    ):
        # The consumer offset of the partition.
        self.offset = offset
        # The partition ID.
        self.partition = partition

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.offset is not None:
            result['Offset'] = self.offset
        if self.partition is not None:
            result['Partition'] = self.partition
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')
        if m.get('Partition') is not None:
            self.partition = m.get('Partition')
        return self


class UpdateConsumerOffsetRequest(TeaModel):
    def __init__(
        self,
        consumer_id: str = None,
        instance_id: str = None,
        offsets: List[UpdateConsumerOffsetRequestOffsets] = None,
        region_id: str = None,
        reset_type: str = None,
        time: str = None,
        topic: str = None,
    ):
        # The name of the consumer group.
        # 
        # *   The name can contain letters, digits, hyphens (-), and underscores (_).
        # *   The name must be **3 to 64** characters in length. If a name contains more than **64** characters, the name is automatically truncated.
        # *   The name of a consumer group cannot be changed after the consumer group is created.
        # 
        # This parameter is required.
        self.consumer_id = consumer_id
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # If you set resetType to offset, you can use this parameter to reset the consumer offset of each partition of a specific topic in the consumer group.
        self.offsets = offsets
        # The region ID of the instance to which the consumer group belongs.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The method that is used to reset the consumer offsets of the subscribed topics of a consumer group. Valid values:
        # 
        # *   **timestamp** (default)
        # *   **offset**\
        self.reset_type = reset_type
        # The point in time when message consumption starts. The value of this parameter is a UNIX timestamp in milliseconds. The value of this parameter must be **less than 0** or **within the retention period of the consumer offset**. This parameter takes effect only if you set resetType to timestamp.
        # 
        # *   If you want to reset the consumer offset to the latest offset, set this parameter to -1.
        # *   If you want to reset the consumer offset to the earliest offset, set this parameter to -2.
        self.time = time
        # The topic name.
        # 
        # *   The name can contain letters, digits, underscores (_), and hyphens (-).
        # *   The name must be **3 to 64** characters in length. If a name contains more than **64** characters, the name is automatically truncated.
        # *   The name of a topic cannot be changed after the topic is created.
        # 
        # **If you want to reset the consumer offsets of all topics to which the consumer subscribes, specify an empty string.**\
        # 
        # This parameter is required.
        self.topic = topic

    def validate(self):
        if self.offsets:
            for k in self.offsets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consumer_id is not None:
            result['ConsumerId'] = self.consumer_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        result['Offsets'] = []
        if self.offsets is not None:
            for k in self.offsets:
                result['Offsets'].append(k.to_map() if k else None)
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.reset_type is not None:
            result['ResetType'] = self.reset_type
        if self.time is not None:
            result['Time'] = self.time
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsumerId') is not None:
            self.consumer_id = m.get('ConsumerId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        self.offsets = []
        if m.get('Offsets') is not None:
            for k in m.get('Offsets'):
                temp_model = UpdateConsumerOffsetRequestOffsets()
                self.offsets.append(temp_model.from_map(k))
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResetType') is not None:
            self.reset_type = m.get('ResetType')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class UpdateConsumerOffsetShrinkRequest(TeaModel):
    def __init__(
        self,
        consumer_id: str = None,
        instance_id: str = None,
        offsets_shrink: str = None,
        region_id: str = None,
        reset_type: str = None,
        time: str = None,
        topic: str = None,
    ):
        # The name of the consumer group.
        # 
        # *   The name can contain letters, digits, hyphens (-), and underscores (_).
        # *   The name must be **3 to 64** characters in length. If a name contains more than **64** characters, the name is automatically truncated.
        # *   The name of a consumer group cannot be changed after the consumer group is created.
        # 
        # This parameter is required.
        self.consumer_id = consumer_id
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # If you set resetType to offset, you can use this parameter to reset the consumer offset of each partition of a specific topic in the consumer group.
        self.offsets_shrink = offsets_shrink
        # The region ID of the instance to which the consumer group belongs.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The method that is used to reset the consumer offsets of the subscribed topics of a consumer group. Valid values:
        # 
        # *   **timestamp** (default)
        # *   **offset**\
        self.reset_type = reset_type
        # The point in time when message consumption starts. The value of this parameter is a UNIX timestamp in milliseconds. The value of this parameter must be **less than 0** or **within the retention period of the consumer offset**. This parameter takes effect only if you set resetType to timestamp.
        # 
        # *   If you want to reset the consumer offset to the latest offset, set this parameter to -1.
        # *   If you want to reset the consumer offset to the earliest offset, set this parameter to -2.
        self.time = time
        # The topic name.
        # 
        # *   The name can contain letters, digits, underscores (_), and hyphens (-).
        # *   The name must be **3 to 64** characters in length. If a name contains more than **64** characters, the name is automatically truncated.
        # *   The name of a topic cannot be changed after the topic is created.
        # 
        # **If you want to reset the consumer offsets of all topics to which the consumer subscribes, specify an empty string.**\
        # 
        # This parameter is required.
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consumer_id is not None:
            result['ConsumerId'] = self.consumer_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.offsets_shrink is not None:
            result['Offsets'] = self.offsets_shrink
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.reset_type is not None:
            result['ResetType'] = self.reset_type
        if self.time is not None:
            result['Time'] = self.time
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsumerId') is not None:
            self.consumer_id = m.get('ConsumerId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Offsets') is not None:
            self.offsets_shrink = m.get('Offsets')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResetType') is not None:
            self.reset_type = m.get('ResetType')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class UpdateConsumerOffsetResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code that is returned. The status code **200** indicates that the request is successful.
        self.code = code
        # The returned message.
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
            result['Code'] = self.code
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateConsumerOffsetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateConsumerOffsetResponseBody = None,
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
            temp_model = UpdateConsumerOffsetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateInstanceConfigRequest(TeaModel):
    def __init__(
        self,
        config: str = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        # The configurations that you want to update for the ApsaraMQ for Kafka instance. The value must be a valid JSON string.
        # 
        # This parameter is required.
        self.config = config
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The region ID of the instance.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateInstanceConfigResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code. The status code 200 indicates that the call is successful.
        self.code = code
        # The returned message.
        self.message = message
        # The request ID.
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
            result['Code'] = self.code
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateInstanceConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateInstanceConfigResponseBody = None,
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
            temp_model = UpdateInstanceConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTopicConfigRequest(TeaModel):
    def __init__(
        self,
        config: str = None,
        instance_id: str = None,
        region_id: str = None,
        topic: str = None,
        value: str = None,
    ):
        # The key of the topic configuration.
        # 
        # *   ApsaraMQ for Kafka V2 instances allow you to modify configurations only for topics that use local storage.
        # *   ApsaraMQ for Kafka V3 instances allow you to modify configurations for all topics.
        # *   The following keys are supported by `local topic` of ApsaraMQ for Kafka V2 instances: retention.ms, retention.bytes, and replications.
        # *   The following keys are supported by ApsaraMQ for Kafka V3 instances: retention.hours and max.message.bytes.
        # 
        # This parameter is required.
        self.config = config
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the region where the instance resides.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The topic name.
        # 
        # This parameter is required.
        self.topic = topic
        # The configuration item that you want to update for the topic. The following configuration items are supported by ApsaraMQ for Kafka V3 instances:
        # 
        # *   `retention.hours` specifies the message retention period. Value type: string. Valid values: 24 to 8760.
        # *   `max.message.bytes` specifies the maximum size of a sent message. Value type: string. Valid values: 1048576 to 10485760.
        # 
        # This parameter is required.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateTopicConfigResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code. If the request is successful, 200 is returned.
        self.code = code
        # The returned data.
        self.data = data
        # The returned message.
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
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateTopicConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateTopicConfigResponseBody = None,
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
            temp_model = UpdateTopicConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpgradeInstanceVersionRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
        target_version: str = None,
    ):
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the region where the instance resides.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The major version to be upgraded to. Valid values:
        # 
        # *   **0.10.2**\
        # *   **2.2.0**\
        # 
        # If you set this parameter to the current major version, the system upgrades the instance to the latest minor version.
        # 
        # This parameter is required.
        self.target_version = target_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.target_version is not None:
            result['TargetVersion'] = self.target_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TargetVersion') is not None:
            self.target_version = m.get('TargetVersion')
        return self


class UpgradeInstanceVersionResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code that is returned. The HTTP status code 200 indicates that the request is successful.
        self.code = code
        # The error message returned.
        self.message = message
        # The ID of the request.
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
            result['Code'] = self.code
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpgradeInstanceVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpgradeInstanceVersionResponseBody = None,
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
            temp_model = UpgradeInstanceVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpgradePostPayOrderRequestServerlessConfig(TeaModel):
    def __init__(
        self,
        reserved_publish_capacity: int = None,
        reserved_subscribe_capacity: int = None,
    ):
        # The reserved capacity for publishing messages. You can specify only integers for this parameter. Minimum value: 60.
        # 
        # >  The maximum capacity that you can reserve for an instance varies based on available resources in a region. The reserved capacity range displayed on the buy page shall prevail.
        self.reserved_publish_capacity = reserved_publish_capacity
        # The reserved capacity for subscribing to messages. You can specify only integers for this parameter. Minimum value: 50.
        # 
        # >  The maximum capacity that you can reserve for an instance varies based on available resources in a region. The reserved capacity range displayed on the buy page shall prevail.
        self.reserved_subscribe_capacity = reserved_subscribe_capacity

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.reserved_publish_capacity is not None:
            result['ReservedPublishCapacity'] = self.reserved_publish_capacity
        if self.reserved_subscribe_capacity is not None:
            result['ReservedSubscribeCapacity'] = self.reserved_subscribe_capacity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReservedPublishCapacity') is not None:
            self.reserved_publish_capacity = m.get('ReservedPublishCapacity')
        if m.get('ReservedSubscribeCapacity') is not None:
            self.reserved_subscribe_capacity = m.get('ReservedSubscribeCapacity')
        return self


class UpgradePostPayOrderRequest(TeaModel):
    def __init__(
        self,
        disk_size: int = None,
        eip_max: int = None,
        eip_model: bool = None,
        instance_id: str = None,
        io_max: int = None,
        io_max_spec: str = None,
        partition_num: int = None,
        region_id: str = None,
        serverless_config: UpgradePostPayOrderRequestServerlessConfig = None,
        spec_type: str = None,
        topic_quota: int = None,
    ):
        # The disk size. Unit: GB.
        # 
        # *   The disk size that you specify must be greater than or equal to the current disk size of the instance.
        # *   For information about the valid values of this parameter, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        # 
        # >  When you create an ApsaraMQ for Kafka V3 serverless instance, you do not need to configure this parameter.
        self.disk_size = disk_size
        # The Internet traffic for the instance.
        # 
        # *   The Internet traffic that you specify must be greater than or equal to the current Internet traffic of the instance.
        # *   For information about the valid values of this parameter, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        # 
        # > -  If you set **EipModel** to **true**, set **EipMax** to a value that is greater than 0.
        # >- If you set **EipModel** to **false**, set **EipMax** to **0**.
        # >- When you create an ApsaraMQ for Kafka V3 serverless instance, you do not need to configure this parameter.
        self.eip_max = eip_max
        # Specifies whether to enable Internet access for the instance. Valid values:
        # 
        # *   true: enables Internet access.
        # *   false: disables Internet access.
        self.eip_model = eip_model
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The maximum traffic for the instance. We recommend that you do not configure this parameter.
        # 
        # *   The maximum traffic that you specify must be greater than or equal to the current maximum traffic of the instance.
        # *   You must configure at least one of IoMax and IoMaxSpec. If you configure both parameters, the value of IoMaxSpec takes effect. We recommend that you configure only IoMaxSpec.
        # *   For information about the valid values of this parameter, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        # 
        # >  When you create an ApsaraMQ for Kafka V3 serverless instance, you do not need to configure this parameter.
        self.io_max = io_max
        # The traffic specification of the instance. We recommend that you configure this parameter.
        # 
        # *   The traffic specification that you specify must be greater than or equal to the current traffic specification of the instance.
        # *   You must configure at least one of IoMax and IoMaxSpec. If you configure both parameters, the value of IoMaxSpec takes effect. We recommend that you configure only IoMaxSpec.
        # *   For information about the valid values of this parameter, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        # 
        # >  When you create an ApsaraMQ for Kafka V3 serverless instance, you do not need to configure this parameter.
        self.io_max_spec = io_max_spec
        # The number of partitions. We recommend that you configure this parameter.
        # 
        # *   You must configure one of PartitionNum and TopicQuota. We recommend that you configure only ParittionNum.
        # *   If you configure PartitionNum and TopicQuota at the same time, the system verifies whether the price of the partitions equals the price of the topics based on the previous topic-based selling mode. If the price of the partitions does not equal the price of the topics, an error is returned. If the price of the partitions equals the price of the topics, the instance is purchased based on the partition number.
        # *   For information about the valid values of this parameter, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        # 
        # >  When you create an ApsaraMQ for Kafka V3 serverless instance, you do not need to configure this parameter.
        self.partition_num = partition_num
        # The region ID of the instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The parameters that are configured for the ApsaraMQ for Kafka serverless instance. When you create a serverless ApsaraMQ for Kafka instance, you must configure these parameters.
        self.serverless_config = serverless_config
        # The instance edition.
        # 
        # Valid values for this parameter if you set PaidType to 1:
        # 
        # *   normal: Standard Edition (High Write)
        # *   professional: Professional Edition (High Write)
        # *   professionalForHighRead: Professional Edition (High Read)
        # 
        # Valid values for this parameter if you set PaidType to 3:
        # 
        # *   normal: Serverless Standard Edition
        # 
        # For more information, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        self.spec_type = spec_type
        # The number of topics. We recommend that you do not configure this parameter.
        # 
        # *   You must configure one of PartitionNum and TopicQuota. We recommend that you configure only ParittionNum.
        # *   If you configure PartitionNum and TopicQuota at the same time, the system verifies whether the price of the partitions equals the price of the topics based on the previous topic-based selling mode. If the price of the partitions does not equal the price of the topics, an error is returned. If the price of the partitions equals the price of the topics, the instance is purchased based on the partition number.
        # *   The default value of TopicQuota varies based on the value of IoMaxSpec. If the number of topics that you consume exceeds the default value, you are charged additional fees.
        # *   For information about the valid values of this parameter, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        # 
        # >  When you create an ApsaraMQ for Kafka V3 serverless instance, you do not need to configure this parameter.
        self.topic_quota = topic_quota

    def validate(self):
        if self.serverless_config:
            self.serverless_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size
        if self.eip_max is not None:
            result['EipMax'] = self.eip_max
        if self.eip_model is not None:
            result['EipModel'] = self.eip_model
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.io_max is not None:
            result['IoMax'] = self.io_max
        if self.io_max_spec is not None:
            result['IoMaxSpec'] = self.io_max_spec
        if self.partition_num is not None:
            result['PartitionNum'] = self.partition_num
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.serverless_config is not None:
            result['ServerlessConfig'] = self.serverless_config.to_map()
        if self.spec_type is not None:
            result['SpecType'] = self.spec_type
        if self.topic_quota is not None:
            result['TopicQuota'] = self.topic_quota
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')
        if m.get('EipMax') is not None:
            self.eip_max = m.get('EipMax')
        if m.get('EipModel') is not None:
            self.eip_model = m.get('EipModel')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IoMax') is not None:
            self.io_max = m.get('IoMax')
        if m.get('IoMaxSpec') is not None:
            self.io_max_spec = m.get('IoMaxSpec')
        if m.get('PartitionNum') is not None:
            self.partition_num = m.get('PartitionNum')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServerlessConfig') is not None:
            temp_model = UpgradePostPayOrderRequestServerlessConfig()
            self.serverless_config = temp_model.from_map(m['ServerlessConfig'])
        if m.get('SpecType') is not None:
            self.spec_type = m.get('SpecType')
        if m.get('TopicQuota') is not None:
            self.topic_quota = m.get('TopicQuota')
        return self


class UpgradePostPayOrderShrinkRequest(TeaModel):
    def __init__(
        self,
        disk_size: int = None,
        eip_max: int = None,
        eip_model: bool = None,
        instance_id: str = None,
        io_max: int = None,
        io_max_spec: str = None,
        partition_num: int = None,
        region_id: str = None,
        serverless_config_shrink: str = None,
        spec_type: str = None,
        topic_quota: int = None,
    ):
        # The disk size. Unit: GB.
        # 
        # *   The disk size that you specify must be greater than or equal to the current disk size of the instance.
        # *   For information about the valid values of this parameter, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        # 
        # >  When you create an ApsaraMQ for Kafka V3 serverless instance, you do not need to configure this parameter.
        self.disk_size = disk_size
        # The Internet traffic for the instance.
        # 
        # *   The Internet traffic that you specify must be greater than or equal to the current Internet traffic of the instance.
        # *   For information about the valid values of this parameter, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        # 
        # > -  If you set **EipModel** to **true**, set **EipMax** to a value that is greater than 0.
        # >- If you set **EipModel** to **false**, set **EipMax** to **0**.
        # >- When you create an ApsaraMQ for Kafka V3 serverless instance, you do not need to configure this parameter.
        self.eip_max = eip_max
        # Specifies whether to enable Internet access for the instance. Valid values:
        # 
        # *   true: enables Internet access.
        # *   false: disables Internet access.
        self.eip_model = eip_model
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The maximum traffic for the instance. We recommend that you do not configure this parameter.
        # 
        # *   The maximum traffic that you specify must be greater than or equal to the current maximum traffic of the instance.
        # *   You must configure at least one of IoMax and IoMaxSpec. If you configure both parameters, the value of IoMaxSpec takes effect. We recommend that you configure only IoMaxSpec.
        # *   For information about the valid values of this parameter, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        # 
        # >  When you create an ApsaraMQ for Kafka V3 serverless instance, you do not need to configure this parameter.
        self.io_max = io_max
        # The traffic specification of the instance. We recommend that you configure this parameter.
        # 
        # *   The traffic specification that you specify must be greater than or equal to the current traffic specification of the instance.
        # *   You must configure at least one of IoMax and IoMaxSpec. If you configure both parameters, the value of IoMaxSpec takes effect. We recommend that you configure only IoMaxSpec.
        # *   For information about the valid values of this parameter, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        # 
        # >  When you create an ApsaraMQ for Kafka V3 serverless instance, you do not need to configure this parameter.
        self.io_max_spec = io_max_spec
        # The number of partitions. We recommend that you configure this parameter.
        # 
        # *   You must configure one of PartitionNum and TopicQuota. We recommend that you configure only ParittionNum.
        # *   If you configure PartitionNum and TopicQuota at the same time, the system verifies whether the price of the partitions equals the price of the topics based on the previous topic-based selling mode. If the price of the partitions does not equal the price of the topics, an error is returned. If the price of the partitions equals the price of the topics, the instance is purchased based on the partition number.
        # *   For information about the valid values of this parameter, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        # 
        # >  When you create an ApsaraMQ for Kafka V3 serverless instance, you do not need to configure this parameter.
        self.partition_num = partition_num
        # The region ID of the instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The parameters that are configured for the ApsaraMQ for Kafka serverless instance. When you create a serverless ApsaraMQ for Kafka instance, you must configure these parameters.
        self.serverless_config_shrink = serverless_config_shrink
        # The instance edition.
        # 
        # Valid values for this parameter if you set PaidType to 1:
        # 
        # *   normal: Standard Edition (High Write)
        # *   professional: Professional Edition (High Write)
        # *   professionalForHighRead: Professional Edition (High Read)
        # 
        # Valid values for this parameter if you set PaidType to 3:
        # 
        # *   normal: Serverless Standard Edition
        # 
        # For more information, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        self.spec_type = spec_type
        # The number of topics. We recommend that you do not configure this parameter.
        # 
        # *   You must configure one of PartitionNum and TopicQuota. We recommend that you configure only ParittionNum.
        # *   If you configure PartitionNum and TopicQuota at the same time, the system verifies whether the price of the partitions equals the price of the topics based on the previous topic-based selling mode. If the price of the partitions does not equal the price of the topics, an error is returned. If the price of the partitions equals the price of the topics, the instance is purchased based on the partition number.
        # *   The default value of TopicQuota varies based on the value of IoMaxSpec. If the number of topics that you consume exceeds the default value, you are charged additional fees.
        # *   For information about the valid values of this parameter, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        # 
        # >  When you create an ApsaraMQ for Kafka V3 serverless instance, you do not need to configure this parameter.
        self.topic_quota = topic_quota

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size
        if self.eip_max is not None:
            result['EipMax'] = self.eip_max
        if self.eip_model is not None:
            result['EipModel'] = self.eip_model
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.io_max is not None:
            result['IoMax'] = self.io_max
        if self.io_max_spec is not None:
            result['IoMaxSpec'] = self.io_max_spec
        if self.partition_num is not None:
            result['PartitionNum'] = self.partition_num
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.serverless_config_shrink is not None:
            result['ServerlessConfig'] = self.serverless_config_shrink
        if self.spec_type is not None:
            result['SpecType'] = self.spec_type
        if self.topic_quota is not None:
            result['TopicQuota'] = self.topic_quota
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')
        if m.get('EipMax') is not None:
            self.eip_max = m.get('EipMax')
        if m.get('EipModel') is not None:
            self.eip_model = m.get('EipModel')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IoMax') is not None:
            self.io_max = m.get('IoMax')
        if m.get('IoMaxSpec') is not None:
            self.io_max_spec = m.get('IoMaxSpec')
        if m.get('PartitionNum') is not None:
            self.partition_num = m.get('PartitionNum')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServerlessConfig') is not None:
            self.serverless_config_shrink = m.get('ServerlessConfig')
        if m.get('SpecType') is not None:
            self.spec_type = m.get('SpecType')
        if m.get('TopicQuota') is not None:
            self.topic_quota = m.get('TopicQuota')
        return self


class UpgradePostPayOrderResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code returned. The HTTP status code 200 indicates that the request is successful.
        self.code = code
        # The message returned.
        self.message = message
        # The ID of the request.
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
            result['Code'] = self.code
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpgradePostPayOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpgradePostPayOrderResponseBody = None,
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
            temp_model = UpgradePostPayOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpgradePrePayOrderRequestConfluentConfig(TeaModel):
    def __init__(
        self,
        connect_cu: int = None,
        connect_replica: int = None,
        control_center_cu: int = None,
        control_center_replica: int = None,
        control_center_storage: int = None,
        kafka_cu: int = None,
        kafka_replica: int = None,
        kafka_rest_proxy_cu: int = None,
        kafka_rest_proxy_replica: int = None,
        kafka_storage: int = None,
        ksql_cu: int = None,
        ksql_replica: int = None,
        ksql_storage: int = None,
        schema_registry_cu: int = None,
        schema_registry_replica: int = None,
        zoo_keeper_cu: int = None,
        zoo_keeper_replica: int = None,
        zoo_keeper_storage: int = None,
    ):
        self.connect_cu = connect_cu
        self.connect_replica = connect_replica
        self.control_center_cu = control_center_cu
        self.control_center_replica = control_center_replica
        self.control_center_storage = control_center_storage
        self.kafka_cu = kafka_cu
        self.kafka_replica = kafka_replica
        self.kafka_rest_proxy_cu = kafka_rest_proxy_cu
        self.kafka_rest_proxy_replica = kafka_rest_proxy_replica
        self.kafka_storage = kafka_storage
        self.ksql_cu = ksql_cu
        self.ksql_replica = ksql_replica
        self.ksql_storage = ksql_storage
        self.schema_registry_cu = schema_registry_cu
        self.schema_registry_replica = schema_registry_replica
        self.zoo_keeper_cu = zoo_keeper_cu
        self.zoo_keeper_replica = zoo_keeper_replica
        self.zoo_keeper_storage = zoo_keeper_storage

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connect_cu is not None:
            result['ConnectCU'] = self.connect_cu
        if self.connect_replica is not None:
            result['ConnectReplica'] = self.connect_replica
        if self.control_center_cu is not None:
            result['ControlCenterCU'] = self.control_center_cu
        if self.control_center_replica is not None:
            result['ControlCenterReplica'] = self.control_center_replica
        if self.control_center_storage is not None:
            result['ControlCenterStorage'] = self.control_center_storage
        if self.kafka_cu is not None:
            result['KafkaCU'] = self.kafka_cu
        if self.kafka_replica is not None:
            result['KafkaReplica'] = self.kafka_replica
        if self.kafka_rest_proxy_cu is not None:
            result['KafkaRestProxyCU'] = self.kafka_rest_proxy_cu
        if self.kafka_rest_proxy_replica is not None:
            result['KafkaRestProxyReplica'] = self.kafka_rest_proxy_replica
        if self.kafka_storage is not None:
            result['KafkaStorage'] = self.kafka_storage
        if self.ksql_cu is not None:
            result['KsqlCU'] = self.ksql_cu
        if self.ksql_replica is not None:
            result['KsqlReplica'] = self.ksql_replica
        if self.ksql_storage is not None:
            result['KsqlStorage'] = self.ksql_storage
        if self.schema_registry_cu is not None:
            result['SchemaRegistryCU'] = self.schema_registry_cu
        if self.schema_registry_replica is not None:
            result['SchemaRegistryReplica'] = self.schema_registry_replica
        if self.zoo_keeper_cu is not None:
            result['ZooKeeperCU'] = self.zoo_keeper_cu
        if self.zoo_keeper_replica is not None:
            result['ZooKeeperReplica'] = self.zoo_keeper_replica
        if self.zoo_keeper_storage is not None:
            result['ZooKeeperStorage'] = self.zoo_keeper_storage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectCU') is not None:
            self.connect_cu = m.get('ConnectCU')
        if m.get('ConnectReplica') is not None:
            self.connect_replica = m.get('ConnectReplica')
        if m.get('ControlCenterCU') is not None:
            self.control_center_cu = m.get('ControlCenterCU')
        if m.get('ControlCenterReplica') is not None:
            self.control_center_replica = m.get('ControlCenterReplica')
        if m.get('ControlCenterStorage') is not None:
            self.control_center_storage = m.get('ControlCenterStorage')
        if m.get('KafkaCU') is not None:
            self.kafka_cu = m.get('KafkaCU')
        if m.get('KafkaReplica') is not None:
            self.kafka_replica = m.get('KafkaReplica')
        if m.get('KafkaRestProxyCU') is not None:
            self.kafka_rest_proxy_cu = m.get('KafkaRestProxyCU')
        if m.get('KafkaRestProxyReplica') is not None:
            self.kafka_rest_proxy_replica = m.get('KafkaRestProxyReplica')
        if m.get('KafkaStorage') is not None:
            self.kafka_storage = m.get('KafkaStorage')
        if m.get('KsqlCU') is not None:
            self.ksql_cu = m.get('KsqlCU')
        if m.get('KsqlReplica') is not None:
            self.ksql_replica = m.get('KsqlReplica')
        if m.get('KsqlStorage') is not None:
            self.ksql_storage = m.get('KsqlStorage')
        if m.get('SchemaRegistryCU') is not None:
            self.schema_registry_cu = m.get('SchemaRegistryCU')
        if m.get('SchemaRegistryReplica') is not None:
            self.schema_registry_replica = m.get('SchemaRegistryReplica')
        if m.get('ZooKeeperCU') is not None:
            self.zoo_keeper_cu = m.get('ZooKeeperCU')
        if m.get('ZooKeeperReplica') is not None:
            self.zoo_keeper_replica = m.get('ZooKeeperReplica')
        if m.get('ZooKeeperStorage') is not None:
            self.zoo_keeper_storage = m.get('ZooKeeperStorage')
        return self


class UpgradePrePayOrderRequest(TeaModel):
    def __init__(
        self,
        confluent_config: UpgradePrePayOrderRequestConfluentConfig = None,
        disk_size: int = None,
        eip_max: int = None,
        eip_model: bool = None,
        instance_id: str = None,
        io_max: int = None,
        io_max_spec: str = None,
        paid_type: int = None,
        partition_num: int = None,
        region_id: str = None,
        spec_type: str = None,
        topic_quota: int = None,
    ):
        self.confluent_config = confluent_config
        # The size of the disk.
        # 
        # *   The disk size that you specify must be greater than or equal to the current disk size of the instance.
        # *   For more information about the valid values, see [Billing overview](https://help.aliyun.com/document_detail/84737.html).
        self.disk_size = disk_size
        # The Internet traffic for the instance.
        # 
        # *   The Internet traffic volume that you specify must be greater than or equal to the current Internet traffic volume of the instance.
        # *   For more information about the valid values, see [Billing overview](https://help.aliyun.com/document_detail/84737.html).
        # > - If the **EipModel** parameter is set to **true**, set the **EipMax** parameter to a value that is greater than 0.
        # > - If the **EipModel** parameter is set to **false**, set the **EipMax** parameter to **0**.
        self.eip_max = eip_max
        # Specifies whether to enable Internet access for the instance. Valid values:
        # 
        # *   true: enables Internet access.
        # *   false: disables Internet access.
        self.eip_model = eip_model
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The maximum traffic for the instance. We recommend that you do not configure this parameter.
        # 
        # *   The maximum traffic volume that you specify must be greater than or equal to the current maximum traffic volume of the instance.
        # *   You must configure at least one of the IoMax and IoMaxSpec parameters. If you configure both parameters, the value of the IoMaxSpec parameter takes effect. We recommend that you configure only the IoMaxSpec parameter.
        # *   For more information about the valid values, see [Billing overview](https://help.aliyun.com/document_detail/84737.html).
        self.io_max = io_max
        # The traffic specification of the instance. We recommend that you configure this parameter.
        # 
        # *   The traffic specification that you specify must be greater than or equal to the current traffic specification of the instance.
        # *   You must configure at least one of the IoMax and IoMaxSpec parameters. If you configure both parameters, the value of the IoMaxSpec parameter takes effect. We recommend that you configure only the IoMaxSpec parameter.
        # *   For more information about the valid values, see [Billing overview](https://help.aliyun.com/document_detail/84737.html).
        self.io_max_spec = io_max_spec
        self.paid_type = paid_type
        # The number of partitions. We recommend that you configure this parameter.
        # 
        # *   You must specify at least one of the PartitionNum and TopicQuota parameters. We recommend that you configure only the PartitionNum parameter.
        # *   If you specify both parameters, the topic-based sales model is used to check whether the PartitionNum value and the TopicQuota value are the same. If they are not the same, a failure response is returned. If they are the same, the order is placed based on the PartitionNum value.
        # *   For more information about the valid values, see [Billing overview](https://help.aliyun.com/document_detail/84737.html).
        self.partition_num = partition_num
        # The region ID of the instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The edition of the instance. Valid values:
        # 
        # *   **normal**: Standard Edition (High Write)
        # *   **professional**: Professional Edition (High Write)
        # *   **professionalForHighRead**: Professional Edition (High Read)
        # 
        # You cannot downgrade an instance from the Professional Edition to the Standard Edition. For more information about these instance editions, see [Billing overview](https://help.aliyun.com/document_detail/84737.html).
        self.spec_type = spec_type
        # The number of topics. We recommend that you do not configure this parameter.
        # 
        # *   You must specify at least one of the PartitionNum and TopicQuota parameters. We recommend that you configure only the PartitionNum parameter.
        # *   If you specify both parameters, the topic-based sales model is used to check whether the PartitionNum value and the TopicQuota value are the same. If they are not the same, a failure response is returned. If they are the same, the order is placed based on the PartitionNum value.
        # *   The default value of the TopicQuota parameter varies based on the value of the IoMaxSpec parameter. If the number of topics that you consume exceeds the default value, you are charged additional fees.
        # *   For more information about the valid values, see [Billing overview](https://help.aliyun.com/document_detail/84737.html).
        self.topic_quota = topic_quota

    def validate(self):
        if self.confluent_config:
            self.confluent_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.confluent_config is not None:
            result['ConfluentConfig'] = self.confluent_config.to_map()
        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size
        if self.eip_max is not None:
            result['EipMax'] = self.eip_max
        if self.eip_model is not None:
            result['EipModel'] = self.eip_model
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.io_max is not None:
            result['IoMax'] = self.io_max
        if self.io_max_spec is not None:
            result['IoMaxSpec'] = self.io_max_spec
        if self.paid_type is not None:
            result['PaidType'] = self.paid_type
        if self.partition_num is not None:
            result['PartitionNum'] = self.partition_num
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.spec_type is not None:
            result['SpecType'] = self.spec_type
        if self.topic_quota is not None:
            result['TopicQuota'] = self.topic_quota
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfluentConfig') is not None:
            temp_model = UpgradePrePayOrderRequestConfluentConfig()
            self.confluent_config = temp_model.from_map(m['ConfluentConfig'])
        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')
        if m.get('EipMax') is not None:
            self.eip_max = m.get('EipMax')
        if m.get('EipModel') is not None:
            self.eip_model = m.get('EipModel')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IoMax') is not None:
            self.io_max = m.get('IoMax')
        if m.get('IoMaxSpec') is not None:
            self.io_max_spec = m.get('IoMaxSpec')
        if m.get('PaidType') is not None:
            self.paid_type = m.get('PaidType')
        if m.get('PartitionNum') is not None:
            self.partition_num = m.get('PartitionNum')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SpecType') is not None:
            self.spec_type = m.get('SpecType')
        if m.get('TopicQuota') is not None:
            self.topic_quota = m.get('TopicQuota')
        return self


class UpgradePrePayOrderShrinkRequest(TeaModel):
    def __init__(
        self,
        confluent_config_shrink: str = None,
        disk_size: int = None,
        eip_max: int = None,
        eip_model: bool = None,
        instance_id: str = None,
        io_max: int = None,
        io_max_spec: str = None,
        paid_type: int = None,
        partition_num: int = None,
        region_id: str = None,
        spec_type: str = None,
        topic_quota: int = None,
    ):
        self.confluent_config_shrink = confluent_config_shrink
        # The size of the disk.
        # 
        # *   The disk size that you specify must be greater than or equal to the current disk size of the instance.
        # *   For more information about the valid values, see [Billing overview](https://help.aliyun.com/document_detail/84737.html).
        self.disk_size = disk_size
        # The Internet traffic for the instance.
        # 
        # *   The Internet traffic volume that you specify must be greater than or equal to the current Internet traffic volume of the instance.
        # *   For more information about the valid values, see [Billing overview](https://help.aliyun.com/document_detail/84737.html).
        # > - If the **EipModel** parameter is set to **true**, set the **EipMax** parameter to a value that is greater than 0.
        # > - If the **EipModel** parameter is set to **false**, set the **EipMax** parameter to **0**.
        self.eip_max = eip_max
        # Specifies whether to enable Internet access for the instance. Valid values:
        # 
        # *   true: enables Internet access.
        # *   false: disables Internet access.
        self.eip_model = eip_model
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The maximum traffic for the instance. We recommend that you do not configure this parameter.
        # 
        # *   The maximum traffic volume that you specify must be greater than or equal to the current maximum traffic volume of the instance.
        # *   You must configure at least one of the IoMax and IoMaxSpec parameters. If you configure both parameters, the value of the IoMaxSpec parameter takes effect. We recommend that you configure only the IoMaxSpec parameter.
        # *   For more information about the valid values, see [Billing overview](https://help.aliyun.com/document_detail/84737.html).
        self.io_max = io_max
        # The traffic specification of the instance. We recommend that you configure this parameter.
        # 
        # *   The traffic specification that you specify must be greater than or equal to the current traffic specification of the instance.
        # *   You must configure at least one of the IoMax and IoMaxSpec parameters. If you configure both parameters, the value of the IoMaxSpec parameter takes effect. We recommend that you configure only the IoMaxSpec parameter.
        # *   For more information about the valid values, see [Billing overview](https://help.aliyun.com/document_detail/84737.html).
        self.io_max_spec = io_max_spec
        self.paid_type = paid_type
        # The number of partitions. We recommend that you configure this parameter.
        # 
        # *   You must specify at least one of the PartitionNum and TopicQuota parameters. We recommend that you configure only the PartitionNum parameter.
        # *   If you specify both parameters, the topic-based sales model is used to check whether the PartitionNum value and the TopicQuota value are the same. If they are not the same, a failure response is returned. If they are the same, the order is placed based on the PartitionNum value.
        # *   For more information about the valid values, see [Billing overview](https://help.aliyun.com/document_detail/84737.html).
        self.partition_num = partition_num
        # The region ID of the instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The edition of the instance. Valid values:
        # 
        # *   **normal**: Standard Edition (High Write)
        # *   **professional**: Professional Edition (High Write)
        # *   **professionalForHighRead**: Professional Edition (High Read)
        # 
        # You cannot downgrade an instance from the Professional Edition to the Standard Edition. For more information about these instance editions, see [Billing overview](https://help.aliyun.com/document_detail/84737.html).
        self.spec_type = spec_type
        # The number of topics. We recommend that you do not configure this parameter.
        # 
        # *   You must specify at least one of the PartitionNum and TopicQuota parameters. We recommend that you configure only the PartitionNum parameter.
        # *   If you specify both parameters, the topic-based sales model is used to check whether the PartitionNum value and the TopicQuota value are the same. If they are not the same, a failure response is returned. If they are the same, the order is placed based on the PartitionNum value.
        # *   The default value of the TopicQuota parameter varies based on the value of the IoMaxSpec parameter. If the number of topics that you consume exceeds the default value, you are charged additional fees.
        # *   For more information about the valid values, see [Billing overview](https://help.aliyun.com/document_detail/84737.html).
        self.topic_quota = topic_quota

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.confluent_config_shrink is not None:
            result['ConfluentConfig'] = self.confluent_config_shrink
        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size
        if self.eip_max is not None:
            result['EipMax'] = self.eip_max
        if self.eip_model is not None:
            result['EipModel'] = self.eip_model
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.io_max is not None:
            result['IoMax'] = self.io_max
        if self.io_max_spec is not None:
            result['IoMaxSpec'] = self.io_max_spec
        if self.paid_type is not None:
            result['PaidType'] = self.paid_type
        if self.partition_num is not None:
            result['PartitionNum'] = self.partition_num
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.spec_type is not None:
            result['SpecType'] = self.spec_type
        if self.topic_quota is not None:
            result['TopicQuota'] = self.topic_quota
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfluentConfig') is not None:
            self.confluent_config_shrink = m.get('ConfluentConfig')
        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')
        if m.get('EipMax') is not None:
            self.eip_max = m.get('EipMax')
        if m.get('EipModel') is not None:
            self.eip_model = m.get('EipModel')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IoMax') is not None:
            self.io_max = m.get('IoMax')
        if m.get('IoMaxSpec') is not None:
            self.io_max_spec = m.get('IoMaxSpec')
        if m.get('PaidType') is not None:
            self.paid_type = m.get('PaidType')
        if m.get('PartitionNum') is not None:
            self.partition_num = m.get('PartitionNum')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SpecType') is not None:
            self.spec_type = m.get('SpecType')
        if m.get('TopicQuota') is not None:
            self.topic_quota = m.get('TopicQuota')
        return self


class UpgradePrePayOrderResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code returned. The HTTP status code 200 indicates that the request is successful.
        self.code = code
        # The error message returned.
        self.message = message
        # The ID of the request.
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
            result['Code'] = self.code
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpgradePrePayOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpgradePrePayOrderResponseBody = None,
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
            temp_model = UpgradePrePayOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


