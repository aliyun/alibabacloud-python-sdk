# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class BindInstance2VpcRequest(TeaModel):
    def __init__(
        self,
        instance_name: str = None,
        instance_vpc_name: str = None,
        network: str = None,
        region_no: str = None,
        resource_owner_id: int = None,
        virtual_switch_id: str = None,
        vpc_id: str = None,
    ):
        self.instance_name = instance_name
        self.instance_vpc_name = instance_vpc_name
        self.network = network
        self.region_no = region_no
        self.resource_owner_id = resource_owner_id
        self.virtual_switch_id = virtual_switch_id
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_vpc_name is not None:
            result['InstanceVpcName'] = self.instance_vpc_name
        if self.network is not None:
            result['Network'] = self.network
        if self.region_no is not None:
            result['RegionNo'] = self.region_no
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.virtual_switch_id is not None:
            result['VirtualSwitchId'] = self.virtual_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceVpcName') is not None:
            self.instance_vpc_name = m.get('InstanceVpcName')
        if m.get('Network') is not None:
            self.network = m.get('Network')
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('VirtualSwitchId') is not None:
            self.virtual_switch_id = m.get('VirtualSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class BindInstance2VpcResponseBody(TeaModel):
    def __init__(
        self,
        domain: str = None,
        endpoint: str = None,
        request_id: str = None,
    ):
        self.domain = domain
        self.endpoint = endpoint
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BindInstance2VpcResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BindInstance2VpcResponseBody = None,
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
            temp_model = BindInstance2VpcResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteInstanceRequest(TeaModel):
    def __init__(
        self,
        instance_name: str = None,
        resource_owner_id: int = None,
    ):
        self.instance_name = instance_name
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DeleteInstanceResponseBody(TeaModel):
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


class DeleteTagsRequestTagInfo(TeaModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class DeleteTagsRequest(TeaModel):
    def __init__(
        self,
        instance_name: str = None,
        resource_owner_id: int = None,
        tag_info: List[DeleteTagsRequestTagInfo] = None,
    ):
        self.instance_name = instance_name
        self.resource_owner_id = resource_owner_id
        self.tag_info = tag_info

    def validate(self):
        if self.tag_info:
            for k in self.tag_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        result['TagInfo'] = []
        if self.tag_info is not None:
            for k in self.tag_info:
                result['TagInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        self.tag_info = []
        if m.get('TagInfo') is not None:
            for k in m.get('TagInfo'):
                temp_model = DeleteTagsRequestTagInfo()
                self.tag_info.append(temp_model.from_map(k))
        return self


class DeleteTagsResponseBody(TeaModel):
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


class DeleteTagsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteTagsResponseBody = None,
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
            temp_model = DeleteTagsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstanceRequest(TeaModel):
    def __init__(
        self,
        instance_name: str = None,
        resource_owner_id: int = None,
    ):
        self.instance_name = instance_name
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class GetInstanceResponseBodyInstanceInfoQuota(TeaModel):
    def __init__(
        self,
        entity_quota: int = None,
    ):
        self.entity_quota = entity_quota

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_quota is not None:
            result['EntityQuota'] = self.entity_quota
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityQuota') is not None:
            self.entity_quota = m.get('EntityQuota')
        return self


class GetInstanceResponseBodyInstanceInfoTagInfosTagInfo(TeaModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetInstanceResponseBodyInstanceInfoTagInfos(TeaModel):
    def __init__(
        self,
        tag_info: List[GetInstanceResponseBodyInstanceInfoTagInfosTagInfo] = None,
    ):
        self.tag_info = tag_info

    def validate(self):
        if self.tag_info:
            for k in self.tag_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TagInfo'] = []
        if self.tag_info is not None:
            for k in self.tag_info:
                result['TagInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag_info = []
        if m.get('TagInfo') is not None:
            for k in m.get('TagInfo'):
                temp_model = GetInstanceResponseBodyInstanceInfoTagInfosTagInfo()
                self.tag_info.append(temp_model.from_map(k))
        return self


class GetInstanceResponseBodyInstanceInfo(TeaModel):
    def __init__(
        self,
        cluster_type: str = None,
        create_time: str = None,
        description: str = None,
        instance_name: str = None,
        network: str = None,
        quota: GetInstanceResponseBodyInstanceInfoQuota = None,
        read_capacity: int = None,
        status: int = None,
        tag_infos: GetInstanceResponseBodyInstanceInfoTagInfos = None,
        user_id: str = None,
        write_capacity: int = None,
    ):
        self.cluster_type = cluster_type
        self.create_time = create_time
        self.description = description
        self.instance_name = instance_name
        self.network = network
        self.quota = quota
        self.read_capacity = read_capacity
        self.status = status
        self.tag_infos = tag_infos
        self.user_id = user_id
        self.write_capacity = write_capacity

    def validate(self):
        if self.quota:
            self.quota.validate()
        if self.tag_infos:
            self.tag_infos.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.network is not None:
            result['Network'] = self.network
        if self.quota is not None:
            result['Quota'] = self.quota.to_map()
        if self.read_capacity is not None:
            result['ReadCapacity'] = self.read_capacity
        if self.status is not None:
            result['Status'] = self.status
        if self.tag_infos is not None:
            result['TagInfos'] = self.tag_infos.to_map()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.write_capacity is not None:
            result['WriteCapacity'] = self.write_capacity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('Network') is not None:
            self.network = m.get('Network')
        if m.get('Quota') is not None:
            temp_model = GetInstanceResponseBodyInstanceInfoQuota()
            self.quota = temp_model.from_map(m['Quota'])
        if m.get('ReadCapacity') is not None:
            self.read_capacity = m.get('ReadCapacity')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TagInfos') is not None:
            temp_model = GetInstanceResponseBodyInstanceInfoTagInfos()
            self.tag_infos = temp_model.from_map(m['TagInfos'])
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('WriteCapacity') is not None:
            self.write_capacity = m.get('WriteCapacity')
        return self


class GetInstanceResponseBody(TeaModel):
    def __init__(
        self,
        instance_info: GetInstanceResponseBodyInstanceInfo = None,
        request_id: str = None,
    ):
        self.instance_info = instance_info
        self.request_id = request_id

    def validate(self):
        if self.instance_info:
            self.instance_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_info is not None:
            result['InstanceInfo'] = self.instance_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceInfo') is not None:
            temp_model = GetInstanceResponseBodyInstanceInfo()
            self.instance_info = temp_model.from_map(m['InstanceInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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


class GetOtsServiceStatusRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
    ):
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class GetOtsServiceStatusResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        err_code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.err_code = err_code
        self.http_status_code = http_status_code
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
        if self.data is not None:
            result['Data'] = self.data
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetOtsServiceStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOtsServiceStatusResponseBody = None,
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
            temp_model = GetOtsServiceStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InsertInstanceRequestTagInfo(TeaModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class InsertInstanceRequest(TeaModel):
    def __init__(
        self,
        cluster_type: str = None,
        description: str = None,
        instance_name: str = None,
        network: str = None,
        resource_owner_id: int = None,
        tag_info: List[InsertInstanceRequestTagInfo] = None,
    ):
        self.cluster_type = cluster_type
        self.description = description
        self.instance_name = instance_name
        self.network = network
        self.resource_owner_id = resource_owner_id
        self.tag_info = tag_info

    def validate(self):
        if self.tag_info:
            for k in self.tag_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.description is not None:
            result['Description'] = self.description
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.network is not None:
            result['Network'] = self.network
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        result['TagInfo'] = []
        if self.tag_info is not None:
            for k in self.tag_info:
                result['TagInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('Network') is not None:
            self.network = m.get('Network')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        self.tag_info = []
        if m.get('TagInfo') is not None:
            for k in m.get('TagInfo'):
                temp_model = InsertInstanceRequestTagInfo()
                self.tag_info.append(temp_model.from_map(k))
        return self


class InsertInstanceResponseBody(TeaModel):
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


class InsertInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: InsertInstanceResponseBody = None,
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
            temp_model = InsertInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InsertTagsRequestTagInfo(TeaModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class InsertTagsRequest(TeaModel):
    def __init__(
        self,
        instance_name: str = None,
        resource_owner_id: int = None,
        tag_info: List[InsertTagsRequestTagInfo] = None,
    ):
        self.instance_name = instance_name
        self.resource_owner_id = resource_owner_id
        self.tag_info = tag_info

    def validate(self):
        if self.tag_info:
            for k in self.tag_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        result['TagInfo'] = []
        if self.tag_info is not None:
            for k in self.tag_info:
                result['TagInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        self.tag_info = []
        if m.get('TagInfo') is not None:
            for k in m.get('TagInfo'):
                temp_model = InsertTagsRequestTagInfo()
                self.tag_info.append(temp_model.from_map(k))
        return self


class InsertTagsResponseBody(TeaModel):
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


class InsertTagsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: InsertTagsResponseBody = None,
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
            temp_model = InsertTagsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListClusterTypeRequest(TeaModel):
    def __init__(
        self,
        resource_owner_id: int = None,
    ):
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ListClusterTypeResponseBodyClusterTypeDetailListClusterTypeDetail(TeaModel):
    def __init__(
        self,
        cluster_type: str = None,
        is_multi_az: bool = None,
    ):
        self.cluster_type = cluster_type
        self.is_multi_az = is_multi_az

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.is_multi_az is not None:
            result['IsMultiAZ'] = self.is_multi_az
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('IsMultiAZ') is not None:
            self.is_multi_az = m.get('IsMultiAZ')
        return self


class ListClusterTypeResponseBodyClusterTypeDetailList(TeaModel):
    def __init__(
        self,
        cluster_type_detail: List[ListClusterTypeResponseBodyClusterTypeDetailListClusterTypeDetail] = None,
    ):
        self.cluster_type_detail = cluster_type_detail

    def validate(self):
        if self.cluster_type_detail:
            for k in self.cluster_type_detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ClusterTypeDetail'] = []
        if self.cluster_type_detail is not None:
            for k in self.cluster_type_detail:
                result['ClusterTypeDetail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cluster_type_detail = []
        if m.get('ClusterTypeDetail') is not None:
            for k in m.get('ClusterTypeDetail'):
                temp_model = ListClusterTypeResponseBodyClusterTypeDetailListClusterTypeDetail()
                self.cluster_type_detail.append(temp_model.from_map(k))
        return self


class ListClusterTypeResponseBodyClusterTypeInfos(TeaModel):
    def __init__(
        self,
        cluster_type: List[str] = None,
    ):
        self.cluster_type = cluster_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        return self


class ListClusterTypeResponseBody(TeaModel):
    def __init__(
        self,
        cluster_type_detail_list: ListClusterTypeResponseBodyClusterTypeDetailList = None,
        cluster_type_infos: ListClusterTypeResponseBodyClusterTypeInfos = None,
        request_id: str = None,
    ):
        self.cluster_type_detail_list = cluster_type_detail_list
        self.cluster_type_infos = cluster_type_infos
        self.request_id = request_id

    def validate(self):
        if self.cluster_type_detail_list:
            self.cluster_type_detail_list.validate()
        if self.cluster_type_infos:
            self.cluster_type_infos.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_type_detail_list is not None:
            result['ClusterTypeDetailList'] = self.cluster_type_detail_list.to_map()
        if self.cluster_type_infos is not None:
            result['ClusterTypeInfos'] = self.cluster_type_infos.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterTypeDetailList') is not None:
            temp_model = ListClusterTypeResponseBodyClusterTypeDetailList()
            self.cluster_type_detail_list = temp_model.from_map(m['ClusterTypeDetailList'])
        if m.get('ClusterTypeInfos') is not None:
            temp_model = ListClusterTypeResponseBodyClusterTypeInfos()
            self.cluster_type_infos = temp_model.from_map(m['ClusterTypeInfos'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListClusterTypeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListClusterTypeResponseBody = None,
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
            temp_model = ListClusterTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstanceRequestTagInfo(TeaModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListInstanceRequest(TeaModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
        resource_owner_id: int = None,
        tag_info: List[ListInstanceRequestTagInfo] = None,
    ):
        self.page_num = page_num
        self.page_size = page_size
        self.resource_owner_id = resource_owner_id
        self.tag_info = tag_info

    def validate(self):
        if self.tag_info:
            for k in self.tag_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        result['TagInfo'] = []
        if self.tag_info is not None:
            for k in self.tag_info:
                result['TagInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        self.tag_info = []
        if m.get('TagInfo') is not None:
            for k in m.get('TagInfo'):
                temp_model = ListInstanceRequestTagInfo()
                self.tag_info.append(temp_model.from_map(k))
        return self


class ListInstanceResponseBodyInstanceInfosInstanceInfo(TeaModel):
    def __init__(
        self,
        instance_name: str = None,
        timestamp: str = None,
    ):
        self.instance_name = instance_name
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class ListInstanceResponseBodyInstanceInfos(TeaModel):
    def __init__(
        self,
        instance_info: List[ListInstanceResponseBodyInstanceInfosInstanceInfo] = None,
    ):
        self.instance_info = instance_info

    def validate(self):
        if self.instance_info:
            for k in self.instance_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InstanceInfo'] = []
        if self.instance_info is not None:
            for k in self.instance_info:
                result['InstanceInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_info = []
        if m.get('InstanceInfo') is not None:
            for k in m.get('InstanceInfo'):
                temp_model = ListInstanceResponseBodyInstanceInfosInstanceInfo()
                self.instance_info.append(temp_model.from_map(k))
        return self


class ListInstanceResponseBody(TeaModel):
    def __init__(
        self,
        instance_infos: ListInstanceResponseBodyInstanceInfos = None,
        page_num: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.instance_infos = instance_infos
        self.page_num = page_num
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.instance_infos:
            self.instance_infos.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_infos is not None:
            result['InstanceInfos'] = self.instance_infos.to_map()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceInfos') is not None:
            temp_model = ListInstanceResponseBodyInstanceInfos()
            self.instance_infos = temp_model.from_map(m['InstanceInfos'])
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListInstanceResponseBody = None,
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
            temp_model = ListInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagsRequestTagInfo(TeaModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListTagsRequest(TeaModel):
    def __init__(
        self,
        instance_name: str = None,
        page_num: int = None,
        page_size: int = None,
        resource_owner_id: int = None,
        tag_info: List[ListTagsRequestTagInfo] = None,
    ):
        self.instance_name = instance_name
        self.page_num = page_num
        self.page_size = page_size
        self.resource_owner_id = resource_owner_id
        self.tag_info = tag_info

    def validate(self):
        if self.tag_info:
            for k in self.tag_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        result['TagInfo'] = []
        if self.tag_info is not None:
            for k in self.tag_info:
                result['TagInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        self.tag_info = []
        if m.get('TagInfo') is not None:
            for k in m.get('TagInfo'):
                temp_model = ListTagsRequestTagInfo()
                self.tag_info.append(temp_model.from_map(k))
        return self


class ListTagsResponseBodyTagInfosTagInfo(TeaModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListTagsResponseBodyTagInfos(TeaModel):
    def __init__(
        self,
        tag_info: List[ListTagsResponseBodyTagInfosTagInfo] = None,
    ):
        self.tag_info = tag_info

    def validate(self):
        if self.tag_info:
            for k in self.tag_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TagInfo'] = []
        if self.tag_info is not None:
            for k in self.tag_info:
                result['TagInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag_info = []
        if m.get('TagInfo') is not None:
            for k in m.get('TagInfo'):
                temp_model = ListTagsResponseBodyTagInfosTagInfo()
                self.tag_info.append(temp_model.from_map(k))
        return self


class ListTagsResponseBody(TeaModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
        request_id: str = None,
        tag_infos: ListTagsResponseBodyTagInfos = None,
        total_count: int = None,
    ):
        self.page_num = page_num
        self.page_size = page_size
        self.request_id = request_id
        self.tag_infos = tag_infos
        self.total_count = total_count

    def validate(self):
        if self.tag_infos:
            self.tag_infos.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tag_infos is not None:
            result['TagInfos'] = self.tag_infos.to_map()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TagInfos') is not None:
            temp_model = ListTagsResponseBodyTagInfos()
            self.tag_infos = temp_model.from_map(m['TagInfos'])
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListTagsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTagsResponseBody = None,
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
            temp_model = ListTagsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListVpcInfoByInstanceRequest(TeaModel):
    def __init__(
        self,
        instance_name: str = None,
        page_num: int = None,
        page_size: int = None,
        resource_owner_id: int = None,
    ):
        self.instance_name = instance_name
        self.page_num = page_num
        self.page_size = page_size
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ListVpcInfoByInstanceResponseBodyVpcInfosVpcInfo(TeaModel):
    def __init__(
        self,
        domain: str = None,
        endpoint: str = None,
        instance_vpc_name: str = None,
        region_no: str = None,
        vpc_id: str = None,
    ):
        self.domain = domain
        self.endpoint = endpoint
        self.instance_vpc_name = instance_vpc_name
        self.region_no = region_no
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.instance_vpc_name is not None:
            result['InstanceVpcName'] = self.instance_vpc_name
        if self.region_no is not None:
            result['RegionNo'] = self.region_no
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('InstanceVpcName') is not None:
            self.instance_vpc_name = m.get('InstanceVpcName')
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class ListVpcInfoByInstanceResponseBodyVpcInfos(TeaModel):
    def __init__(
        self,
        vpc_info: List[ListVpcInfoByInstanceResponseBodyVpcInfosVpcInfo] = None,
    ):
        self.vpc_info = vpc_info

    def validate(self):
        if self.vpc_info:
            for k in self.vpc_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['VpcInfo'] = []
        if self.vpc_info is not None:
            for k in self.vpc_info:
                result['VpcInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.vpc_info = []
        if m.get('VpcInfo') is not None:
            for k in m.get('VpcInfo'):
                temp_model = ListVpcInfoByInstanceResponseBodyVpcInfosVpcInfo()
                self.vpc_info.append(temp_model.from_map(k))
        return self


class ListVpcInfoByInstanceResponseBody(TeaModel):
    def __init__(
        self,
        instance_name: str = None,
        page_num: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        vpc_infos: ListVpcInfoByInstanceResponseBodyVpcInfos = None,
    ):
        self.instance_name = instance_name
        self.page_num = page_num
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count
        self.vpc_infos = vpc_infos

    def validate(self):
        if self.vpc_infos:
            self.vpc_infos.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.vpc_infos is not None:
            result['VpcInfos'] = self.vpc_infos.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('VpcInfos') is not None:
            temp_model = ListVpcInfoByInstanceResponseBodyVpcInfos()
            self.vpc_infos = temp_model.from_map(m['VpcInfos'])
        return self


class ListVpcInfoByInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListVpcInfoByInstanceResponseBody = None,
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
            temp_model = ListVpcInfoByInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListVpcInfoByVpcRequestTagInfo(TeaModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListVpcInfoByVpcRequest(TeaModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
        resource_owner_id: int = None,
        tag_info: List[ListVpcInfoByVpcRequestTagInfo] = None,
        vpc_id: str = None,
    ):
        self.page_num = page_num
        self.page_size = page_size
        self.resource_owner_id = resource_owner_id
        self.tag_info = tag_info
        self.vpc_id = vpc_id

    def validate(self):
        if self.tag_info:
            for k in self.tag_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        result['TagInfo'] = []
        if self.tag_info is not None:
            for k in self.tag_info:
                result['TagInfo'].append(k.to_map() if k else None)
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        self.tag_info = []
        if m.get('TagInfo') is not None:
            for k in m.get('TagInfo'):
                temp_model = ListVpcInfoByVpcRequestTagInfo()
                self.tag_info.append(temp_model.from_map(k))
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class ListVpcInfoByVpcResponseBodyVpcInfosVpcInfo(TeaModel):
    def __init__(
        self,
        domain: str = None,
        endpoint: str = None,
        instance_name: str = None,
        instance_vpc_name: str = None,
        region_no: str = None,
    ):
        self.domain = domain
        self.endpoint = endpoint
        self.instance_name = instance_name
        self.instance_vpc_name = instance_vpc_name
        self.region_no = region_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_vpc_name is not None:
            result['InstanceVpcName'] = self.instance_vpc_name
        if self.region_no is not None:
            result['RegionNo'] = self.region_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceVpcName') is not None:
            self.instance_vpc_name = m.get('InstanceVpcName')
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')
        return self


class ListVpcInfoByVpcResponseBodyVpcInfos(TeaModel):
    def __init__(
        self,
        vpc_info: List[ListVpcInfoByVpcResponseBodyVpcInfosVpcInfo] = None,
    ):
        self.vpc_info = vpc_info

    def validate(self):
        if self.vpc_info:
            for k in self.vpc_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['VpcInfo'] = []
        if self.vpc_info is not None:
            for k in self.vpc_info:
                result['VpcInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.vpc_info = []
        if m.get('VpcInfo') is not None:
            for k in m.get('VpcInfo'):
                temp_model = ListVpcInfoByVpcResponseBodyVpcInfosVpcInfo()
                self.vpc_info.append(temp_model.from_map(k))
        return self


class ListVpcInfoByVpcResponseBody(TeaModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        vpc_id: str = None,
        vpc_infos: ListVpcInfoByVpcResponseBodyVpcInfos = None,
    ):
        self.page_num = page_num
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count
        self.vpc_id = vpc_id
        self.vpc_infos = vpc_infos

    def validate(self):
        if self.vpc_infos:
            self.vpc_infos.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vpc_infos is not None:
            result['VpcInfos'] = self.vpc_infos.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VpcInfos') is not None:
            temp_model = ListVpcInfoByVpcResponseBodyVpcInfos()
            self.vpc_infos = temp_model.from_map(m['VpcInfos'])
        return self


class ListVpcInfoByVpcResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListVpcInfoByVpcResponseBody = None,
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
            temp_model = ListVpcInfoByVpcResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OpenOtsServiceResponseBody(TeaModel):
    def __init__(
        self,
        order_id: str = None,
        request_id: str = None,
    ):
        self.order_id = order_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class OpenOtsServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OpenOtsServiceResponseBody = None,
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
            temp_model = OpenOtsServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnbindInstance2VpcRequest(TeaModel):
    def __init__(
        self,
        instance_name: str = None,
        instance_vpc_name: str = None,
        region_no: str = None,
        resource_owner_id: int = None,
    ):
        self.instance_name = instance_name
        self.instance_vpc_name = instance_vpc_name
        self.region_no = region_no
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_vpc_name is not None:
            result['InstanceVpcName'] = self.instance_vpc_name
        if self.region_no is not None:
            result['RegionNo'] = self.region_no
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceVpcName') is not None:
            self.instance_vpc_name = m.get('InstanceVpcName')
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class UnbindInstance2VpcResponseBody(TeaModel):
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


class UnbindInstance2VpcResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UnbindInstance2VpcResponseBody = None,
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
            temp_model = UnbindInstance2VpcResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateInstanceRequest(TeaModel):
    def __init__(
        self,
        instance_name: str = None,
        network: str = None,
        resource_owner_id: int = None,
    ):
        self.instance_name = instance_name
        self.network = network
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.network is not None:
            result['Network'] = self.network
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('Network') is not None:
            self.network = m.get('Network')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class UpdateInstanceResponseBody(TeaModel):
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


