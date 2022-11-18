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
        self.new_resource_group_id = new_resource_group_id
        self.region_id = region_id
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
        self.code = code
        self.message = message
        self.new_resource_group_id = new_resource_group_id
        self.request_id = request_id
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        self.duration = duration
        self.instance_id = instance_id
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
        self.code = code
        self.message = message
        self.order_id = order_id
        self.request_id = request_id
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        acl_resource_name: str = None,
        acl_resource_pattern_type: str = None,
        acl_resource_type: str = None,
        instance_id: str = None,
        region_id: str = None,
        username: str = None,
    ):
        self.acl_operation_type = acl_operation_type
        self.acl_resource_name = acl_resource_name
        self.acl_resource_pattern_type = acl_resource_pattern_type
        self.acl_resource_type = acl_resource_type
        self.instance_id = instance_id
        self.region_id = region_id
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
        if self.acl_resource_name is not None:
            result['AclResourceName'] = self.acl_resource_name
        if self.acl_resource_pattern_type is not None:
            result['AclResourcePatternType'] = self.acl_resource_pattern_type
        if self.acl_resource_type is not None:
            result['AclResourceType'] = self.acl_resource_type
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
        if m.get('AclResourceName') is not None:
            self.acl_resource_name = m.get('AclResourceName')
        if m.get('AclResourcePatternType') is not None:
            self.acl_resource_pattern_type = m.get('AclResourcePatternType')
        if m.get('AclResourceType') is not None:
            self.acl_resource_type = m.get('AclResourceType')
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
        self.code = code
        self.message = message
        self.request_id = request_id
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        self.key = key
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
        self.consumer_id = consumer_id
        self.instance_id = instance_id
        self.region_id = region_id
        self.remark = remark
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
        self.code = code
        self.message = message
        self.request_id = request_id
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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


class CreatePostPayOrderRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
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
        partition_num: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        spec_type: str = None,
        tag: List[CreatePostPayOrderRequestTag] = None,
        topic_quota: int = None,
    ):
        self.deploy_type = deploy_type
        self.disk_size = disk_size
        self.disk_type = disk_type
        self.eip_max = eip_max
        self.io_max = io_max
        self.io_max_spec = io_max_spec
        self.partition_num = partition_num
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.spec_type = spec_type
        self.tag = tag
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
                temp_model = CreatePostPayOrderRequestTag()
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
        self.code = code
        self.message = message
        self.order_id = order_id
        self.request_id = request_id
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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


class CreatePrePayOrderRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
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
        deploy_type: int = None,
        disk_size: int = None,
        disk_type: str = None,
        eip_max: int = None,
        io_max: int = None,
        io_max_spec: str = None,
        partition_num: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        spec_type: str = None,
        tag: List[CreatePrePayOrderRequestTag] = None,
        topic_quota: int = None,
    ):
        self.deploy_type = deploy_type
        self.disk_size = disk_size
        self.disk_type = disk_type
        self.eip_max = eip_max
        self.io_max = io_max
        self.io_max_spec = io_max_spec
        self.partition_num = partition_num
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.spec_type = spec_type
        self.tag = tag
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


class CreatePrePayOrderResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        order_id: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.order_id = order_id
        self.request_id = request_id
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        password: str = None,
        region_id: str = None,
        type: str = None,
        username: str = None,
    ):
        self.instance_id = instance_id
        self.password = password
        self.region_id = region_id
        self.type = type
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
        self.code = code
        self.message = message
        self.request_id = request_id
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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


class CreateTopicRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
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
        config: Dict[str, Any] = None,
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
        self.compact_topic = compact_topic
        self.config = config
        self.instance_id = instance_id
        self.local_topic = local_topic
        self.min_insync_replicas = min_insync_replicas
        self.partition_num = partition_num
        self.region_id = region_id
        self.remark = remark
        self.replication_factor = replication_factor
        self.tag = tag
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


class CreateTopicShrinkRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
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


class CreateTopicShrinkRequest(TeaModel):
    def __init__(
        self,
        compact_topic: bool = None,
        config_shrink: str = None,
        instance_id: str = None,
        local_topic: bool = None,
        min_insync_replicas: int = None,
        partition_num: str = None,
        region_id: str = None,
        remark: str = None,
        replication_factor: int = None,
        tag: List[CreateTopicShrinkRequestTag] = None,
        topic: str = None,
    ):
        self.compact_topic = compact_topic
        self.config_shrink = config_shrink
        self.instance_id = instance_id
        self.local_topic = local_topic
        self.min_insync_replicas = min_insync_replicas
        self.partition_num = partition_num
        self.region_id = region_id
        self.remark = remark
        self.replication_factor = replication_factor
        self.tag = tag
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
        if self.config_shrink is not None:
            result['Config'] = self.config_shrink
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
            self.config_shrink = m.get('Config')
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
                temp_model = CreateTopicShrinkRequestTag()
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
        self.code = code
        self.message = message
        self.request_id = request_id
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        acl_resource_name: str = None,
        acl_resource_pattern_type: str = None,
        acl_resource_type: str = None,
        instance_id: str = None,
        region_id: str = None,
        username: str = None,
    ):
        self.acl_operation_type = acl_operation_type
        self.acl_resource_name = acl_resource_name
        self.acl_resource_pattern_type = acl_resource_pattern_type
        self.acl_resource_type = acl_resource_type
        self.instance_id = instance_id
        self.region_id = region_id
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
        if self.acl_resource_name is not None:
            result['AclResourceName'] = self.acl_resource_name
        if self.acl_resource_pattern_type is not None:
            result['AclResourcePatternType'] = self.acl_resource_pattern_type
        if self.acl_resource_type is not None:
            result['AclResourceType'] = self.acl_resource_type
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
        if m.get('AclResourceName') is not None:
            self.acl_resource_name = m.get('AclResourceName')
        if m.get('AclResourcePatternType') is not None:
            self.acl_resource_pattern_type = m.get('AclResourcePatternType')
        if m.get('AclResourceType') is not None:
            self.acl_resource_type = m.get('AclResourceType')
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
        self.code = code
        self.message = message
        self.request_id = request_id
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        self.consumer_id = consumer_id
        self.instance_id = instance_id
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
        self.code = code
        self.message = message
        self.request_id = request_id
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        self.instance_id = instance_id
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
        self.code = code
        self.message = message
        self.request_id = request_id
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        region_id: str = None,
        type: str = None,
        username: str = None,
    ):
        self.instance_id = instance_id
        self.region_id = region_id
        self.type = type
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
        self.code = code
        self.message = message
        self.request_id = request_id
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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


class DeleteTopicRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
        topic: str = None,
    ):
        self.instance_id = instance_id
        self.region_id = region_id
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
        self.code = code
        self.message = message
        self.request_id = request_id
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        acl_resource_name: str = None,
        acl_resource_pattern_type: str = None,
        acl_resource_type: str = None,
        instance_id: str = None,
        region_id: str = None,
        username: str = None,
    ):
        self.acl_resource_name = acl_resource_name
        self.acl_resource_pattern_type = acl_resource_pattern_type
        self.acl_resource_type = acl_resource_type
        self.instance_id = instance_id
        self.region_id = region_id
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_resource_name is not None:
            result['AclResourceName'] = self.acl_resource_name
        if self.acl_resource_pattern_type is not None:
            result['AclResourcePatternType'] = self.acl_resource_pattern_type
        if self.acl_resource_type is not None:
            result['AclResourceType'] = self.acl_resource_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclResourceName') is not None:
            self.acl_resource_name = m.get('AclResourceName')
        if m.get('AclResourcePatternType') is not None:
            self.acl_resource_pattern_type = m.get('AclResourcePatternType')
        if m.get('AclResourceType') is not None:
            self.acl_resource_type = m.get('AclResourceType')
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
        acl_resource_name: str = None,
        acl_resource_pattern_type: str = None,
        acl_resource_type: str = None,
        host: str = None,
        username: str = None,
    ):
        self.acl_operation_type = acl_operation_type
        self.acl_resource_name = acl_resource_name
        self.acl_resource_pattern_type = acl_resource_pattern_type
        self.acl_resource_type = acl_resource_type
        self.host = host
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
        self.code = code
        self.kafka_acl_list = kafka_acl_list
        self.message = message
        self.request_id = request_id
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        self.instance_id = instance_id
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
        password: str = None,
        type: str = None,
        username: str = None,
    ):
        self.password = password
        self.type = type
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.password is not None:
            result['Password'] = self.password
        if self.type is not None:
            result['Type'] = self.type
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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
        self.code = code
        self.message = message
        self.request_id = request_id
        self.sasl_user_list = sasl_user_list
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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


class GetAllInstanceIdListRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
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
        self.code = code
        self.instance_ids = instance_ids
        self.message = message
        self.request_id = request_id
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        self.instance_id = instance_id
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
        self.allowed_ip_group = allowed_ip_group
        self.allowed_ip_list = allowed_ip_list
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
        self.allowed_ip_group = allowed_ip_group
        self.allowed_ip_list = allowed_ip_list
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
        self.deploy_type = deploy_type
        self.internet_list = internet_list
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
        self.allowed_list = allowed_list
        self.code = code
        self.message = message
        self.request_id = request_id
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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


class GetConsumerListRequest(TeaModel):
    def __init__(
        self,
        consumer_id: str = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        self.consumer_id = consumer_id
        self.instance_id = instance_id
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


class GetConsumerListResponseBodyConsumerListConsumerVOTagsTagVO(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
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
        consumer_id: str = None,
        instance_id: str = None,
        region_id: str = None,
        remark: str = None,
        tags: GetConsumerListResponseBodyConsumerListConsumerVOTags = None,
    ):
        self.consumer_id = consumer_id
        self.instance_id = instance_id
        self.region_id = region_id
        self.remark = remark
        self.tags = tags

    def validate(self):
        if self.tags:
            self.tags.validate()

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
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
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
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.consumer_list = consumer_list
        self.message = message
        self.request_id = request_id
        self.success = success

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
        if m.get('ConsumerList') is not None:
            temp_model = GetConsumerListResponseBodyConsumerList()
            self.consumer_list = temp_model.from_map(m['ConsumerList'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        instance_id: str = None,
        region_id: str = None,
    ):
        self.consumer_id = consumer_id
        self.instance_id = instance_id
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


class GetConsumerProgressResponseBodyConsumerProgressTopicListTopicListOffsetListOffsetList(TeaModel):
    def __init__(
        self,
        broker_offset: int = None,
        consumer_offset: int = None,
        last_timestamp: int = None,
        partition: int = None,
    ):
        self.broker_offset = broker_offset
        self.consumer_offset = consumer_offset
        self.last_timestamp = last_timestamp
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
        self.last_timestamp = last_timestamp
        self.offset_list = offset_list
        self.topic = topic
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
        topic_list: GetConsumerProgressResponseBodyConsumerProgressTopicList = None,
        total_diff: int = None,
    ):
        self.last_timestamp = last_timestamp
        self.topic_list = topic_list
        self.total_diff = total_diff

    def validate(self):
        if self.topic_list:
            self.topic_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.last_timestamp is not None:
            result['LastTimestamp'] = self.last_timestamp
        if self.topic_list is not None:
            result['TopicList'] = self.topic_list.to_map()
        if self.total_diff is not None:
            result['TotalDiff'] = self.total_diff
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LastTimestamp') is not None:
            self.last_timestamp = m.get('LastTimestamp')
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
        self.code = code
        self.consumer_progress = consumer_progress
        self.message = message
        self.request_id = request_id
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        self.key = key
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
        tag: List[GetInstanceListRequestTag] = None,
    ):
        self.instance_id = instance_id
        self.order_id = order_id
        self.region_id = region_id
        self.resource_group_id = resource_group_id
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
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = GetInstanceListRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class GetInstanceListResponseBodyInstanceListInstanceVOTagsTagVO(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
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
        kms_key_id: str = None,
        msg_retain: int = None,
        name: str = None,
        paid_type: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        sasl_domain_endpoint: str = None,
        security_group: str = None,
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
        vpc_id: str = None,
        zone_id: str = None,
    ):
        self.all_config = all_config
        self.create_time = create_time
        self.deploy_type = deploy_type
        self.disk_size = disk_size
        self.disk_type = disk_type
        self.domain_endpoint = domain_endpoint
        self.eip_max = eip_max
        self.end_point = end_point
        self.expired_time = expired_time
        self.instance_id = instance_id
        self.io_max = io_max
        self.kms_key_id = kms_key_id
        self.msg_retain = msg_retain
        self.name = name
        self.paid_type = paid_type
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.sasl_domain_endpoint = sasl_domain_endpoint
        self.security_group = security_group
        self.service_status = service_status
        self.spec_type = spec_type
        self.ssl_domain_endpoint = ssl_domain_endpoint
        self.ssl_end_point = ssl_end_point
        self.standard_zone_id = standard_zone_id
        self.tags = tags
        self.topic_num_limit = topic_num_limit
        self.upgrade_service_detail_info = upgrade_service_detail_info
        self.used_group_count = used_group_count
        self.used_partition_count = used_partition_count
        self.used_topic_count = used_topic_count
        self.v_switch_id = v_switch_id
        self.vpc_id = vpc_id
        self.zone_id = zone_id

    def validate(self):
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
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.sasl_domain_endpoint is not None:
            result['SaslDomainEndpoint'] = self.sasl_domain_endpoint
        if self.security_group is not None:
            result['SecurityGroup'] = self.security_group
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
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllConfig') is not None:
            self.all_config = m.get('AllConfig')
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
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SaslDomainEndpoint') is not None:
            self.sasl_domain_endpoint = m.get('SaslDomainEndpoint')
        if m.get('SecurityGroup') is not None:
            self.security_group = m.get('SecurityGroup')
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
        self.code = code
        self.instance_list = instance_list
        self.message = message
        self.request_id = request_id
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        self.instance_id = instance_id
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
        partition_quata: int = None,
        partition_used: int = None,
        topic_left: int = None,
        topic_num_of_buy: int = None,
        topic_quota: int = None,
        topic_used: int = None,
    ):
        self.group_left = group_left
        self.group_used = group_used
        self.is_partition_buy = is_partition_buy
        self.partition_left = partition_left
        self.partition_num_of_buy = partition_num_of_buy
        self.partition_quata = partition_quata
        self.partition_used = partition_used
        self.topic_left = topic_left
        self.topic_num_of_buy = topic_num_of_buy
        self.topic_quota = topic_quota
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
        if self.partition_quata is not None:
            result['PartitionQuata'] = self.partition_quata
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
        if m.get('PartitionQuata') is not None:
            self.partition_quata = m.get('PartitionQuata')
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
        self.code = code
        self.message = message
        self.quota_data = quota_data
        self.request_id = request_id
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        self.current_page = current_page
        self.instance_id = instance_id
        self.page_size = page_size
        self.region_id = region_id
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
        self.key = key
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
    ):
        self.compact_topic = compact_topic
        self.create_time = create_time
        self.instance_id = instance_id
        self.local_topic = local_topic
        self.partition_num = partition_num
        self.region_id = region_id
        self.remark = remark
        self.status = status
        self.status_name = status_name
        self.tags = tags
        self.topic = topic

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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
        self.code = code
        self.current_page = current_page
        self.message = message
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.topic_list = topic_list
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        self.instance_id = instance_id
        self.region_id = region_id
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
        self.last_update_timestamp = last_update_timestamp
        self.max_offset = max_offset
        self.min_offset = min_offset
        self.partition = partition
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
        self.last_time_stamp = last_time_stamp
        self.offset_table = offset_table
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
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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


class ListTagResourcesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
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
        self.next_token = next_token
        self.region_id = region_id
        self.resource_id = resource_id
        self.resource_type = resource_type
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
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.tag_key = tag_key
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
        self.next_token = next_token
        self.request_id = request_id
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        self.instance_id = instance_id
        self.instance_name = instance_name
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
        self.code = code
        self.message = message
        self.request_id = request_id
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        self.add_partition_num = add_partition_num
        self.instance_id = instance_id
        self.region_id = region_id
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
        self.code = code
        self.message = message
        self.request_id = request_id
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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


class ModifyTopicRemarkRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
        remark: str = None,
        topic: str = None,
    ):
        self.instance_id = instance_id
        self.region_id = region_id
        self.remark = remark
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
        self.code = code
        self.message = message
        self.request_id = request_id
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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


class ReleaseInstanceRequest(TeaModel):
    def __init__(
        self,
        force_delete_instance: bool = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        self.force_delete_instance = force_delete_instance
        self.instance_id = instance_id
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
        self.code = code
        self.message = message
        self.request_id = request_id
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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


class StartInstanceRequest(TeaModel):
    def __init__(
        self,
        config: str = None,
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
        vpc_id: str = None,
        zone_id: str = None,
    ):
        self.config = config
        self.deploy_module = deploy_module
        self.instance_id = instance_id
        self.is_eip_inner = is_eip_inner
        self.is_force_selected_zones = is_force_selected_zones
        self.is_set_user_and_password = is_set_user_and_password
        self.kmskey_id = kmskey_id
        self.name = name
        self.notifier = notifier
        self.password = password
        self.region_id = region_id
        self.security_group = security_group
        self.selected_zones = selected_zones
        self.service_version = service_version
        self.user_phone_num = user_phone_num
        self.username = username
        self.v_switch_id = v_switch_id
        self.vpc_id = vpc_id
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
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
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
        self.code = code
        self.message = message
        self.request_id = request_id
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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


class TagResourcesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
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
        self.instance_id = instance_id
        self.region_id = region_id
        self.resource_id = resource_id
        self.resource_type = resource_type
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        self.all = all
        self.region_id = region_id
        self.resource_id = resource_id
        self.resource_type = resource_type
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        self.allowed_list_ip = allowed_list_ip
        self.allowed_list_type = allowed_list_type
        self.description = description
        self.instance_id = instance_id
        self.port_range = port_range
        self.region_id = region_id
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
        self.code = code
        self.message = message
        self.request_id = request_id
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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


class UpdateInstanceConfigRequest(TeaModel):
    def __init__(
        self,
        config: str = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        self.config = config
        self.instance_id = instance_id
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
        self.code = code
        self.message = message
        self.request_id = request_id
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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


class UpgradeInstanceVersionRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
        target_version: str = None,
    ):
        self.instance_id = instance_id
        self.region_id = region_id
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
        self.code = code
        self.message = message
        self.request_id = request_id
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        spec_type: str = None,
        topic_quota: int = None,
    ):
        self.disk_size = disk_size
        self.eip_max = eip_max
        self.eip_model = eip_model
        self.instance_id = instance_id
        self.io_max = io_max
        self.io_max_spec = io_max_spec
        self.partition_num = partition_num
        self.region_id = region_id
        self.spec_type = spec_type
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
        self.code = code
        self.message = message
        self.request_id = request_id
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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


class UpgradePrePayOrderRequest(TeaModel):
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
        spec_type: str = None,
        topic_quota: int = None,
    ):
        self.disk_size = disk_size
        self.eip_max = eip_max
        self.eip_model = eip_model
        self.instance_id = instance_id
        self.io_max = io_max
        self.io_max_spec = io_max_spec
        self.partition_num = partition_num
        self.region_id = region_id
        self.spec_type = spec_type
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
        self.code = code
        self.message = message
        self.request_id = request_id
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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


