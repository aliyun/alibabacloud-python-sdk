# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class AddIpRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        ip_list: str = None,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        # The ID of the Anti-DDoS Origin Enterprise instance.
        # 
        # >  You can call the [DescribeInstanceList](https://help.aliyun.com/document_detail/118698.html) operation to query the IDs of all Anti-DDoS Origin Enterprise instances.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The list of IP addresses that you want to add to the Anti-DDoS Origin Enterprise instance. This parameter is a string consisting of JSON arrays. Each element in a JSON array is a JSON struct that includes the following field:
        # 
        # *   **ip**: required. The IP address that you want to add. Data type: string.
        # 
        #     > The IP address must be the IP address of an asset that belongs to the current Alibaba Cloud account.
        # 
        # This parameter is required.
        self.ip_list = ip_list
        # The region ID of the Anti-DDoS Origin Enterprise instance.
        # 
        # >  You can call the [DescribeRegions](https://help.aliyun.com/document_detail/118703.html) operation to query all regions supported by Anti-DDoS Origin.
        self.region_id = region_id
        # The ID of the resource group to which the Anti-DDoS Origin Enterprise instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        # 
        # For more information about resource groups, see [Create a resource group](https://help.aliyun.com/document_detail/94485.html).
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ip_list is not None:
            result['IpList'] = self.ip_list
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IpList') is not None:
            self.ip_list = m.get('IpList')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class AddIpResponseBody(TeaModel):
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


class AddIpResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddIpResponseBody = None,
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
            temp_model = AddIpResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddRdMemberListRequestMemberList(TeaModel):
    def __init__(
        self,
        uid: str = None,
    ):
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class AddRdMemberListRequest(TeaModel):
    def __init__(
        self,
        member_list: List[AddRdMemberListRequestMemberList] = None,
    ):
        # This parameter is required.
        self.member_list = member_list

    def validate(self):
        if self.member_list:
            for k in self.member_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MemberList'] = []
        if self.member_list is not None:
            for k in self.member_list:
                result['MemberList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.member_list = []
        if m.get('MemberList') is not None:
            for k in m.get('MemberList'):
                temp_model = AddRdMemberListRequestMemberList()
                self.member_list.append(temp_model.from_map(k))
        return self


class AddRdMemberListShrinkRequest(TeaModel):
    def __init__(
        self,
        member_list_shrink: str = None,
    ):
        # This parameter is required.
        self.member_list_shrink = member_list_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.member_list_shrink is not None:
            result['MemberList'] = self.member_list_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MemberList') is not None:
            self.member_list_shrink = m.get('MemberList')
        return self


class AddRdMemberListResponseBody(TeaModel):
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


class AddRdMemberListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddRdMemberListResponseBody = None,
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
            temp_model = AddRdMemberListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachAssetGroupToInstanceRequestAssetGroupList(TeaModel):
    def __init__(
        self,
        member_uid: str = None,
        name: str = None,
        region: str = None,
        type: str = None,
    ):
        # The UID of the member to which the asset belongs.
        self.member_uid = member_uid
        # The ID of the asset that you want to add. If the asset is a Web Application Firewall (WAF) instance, specify the ID of the WAF instance.
        # 
        # This parameter is required.
        self.name = name
        # The region ID of the asset.
        # 
        # This parameter is required.
        self.region = region
        # The type of the asset.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid
        if self.name is not None:
            result['Name'] = self.name
        if self.region is not None:
            result['Region'] = self.region
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class AttachAssetGroupToInstanceRequest(TeaModel):
    def __init__(
        self,
        asset_group_list: List[AttachAssetGroupToInstanceRequestAssetGroupList] = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        # The information about the asset to be associated.
        # 
        # This parameter is required.
        self.asset_group_list = asset_group_list
        # The ID of the instance to query.
        # 
        # >  You can call the [DescribeInstanceList](https://help.aliyun.com/document_detail/118698.html) operation to query the IDs of all Anti-DDoS Origin instances of paid editions.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the region in which the instance resides.
        # 
        # >  You can call the [DescribeRegions](https://help.aliyun.com/document_detail/118703.html) operation to query the most recent region list.
        self.region_id = region_id

    def validate(self):
        if self.asset_group_list:
            for k in self.asset_group_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AssetGroupList'] = []
        if self.asset_group_list is not None:
            for k in self.asset_group_list:
                result['AssetGroupList'].append(k.to_map() if k else None)
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.asset_group_list = []
        if m.get('AssetGroupList') is not None:
            for k in m.get('AssetGroupList'):
                temp_model = AttachAssetGroupToInstanceRequestAssetGroupList()
                self.asset_group_list.append(temp_model.from_map(k))
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class AttachAssetGroupToInstanceShrinkRequest(TeaModel):
    def __init__(
        self,
        asset_group_list_shrink: str = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        # The information about the asset to be associated.
        # 
        # This parameter is required.
        self.asset_group_list_shrink = asset_group_list_shrink
        # The ID of the instance to query.
        # 
        # >  You can call the [DescribeInstanceList](https://help.aliyun.com/document_detail/118698.html) operation to query the IDs of all Anti-DDoS Origin instances of paid editions.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the region in which the instance resides.
        # 
        # >  You can call the [DescribeRegions](https://help.aliyun.com/document_detail/118703.html) operation to query the most recent region list.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.asset_group_list_shrink is not None:
            result['AssetGroupList'] = self.asset_group_list_shrink
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetGroupList') is not None:
            self.asset_group_list_shrink = m.get('AssetGroupList')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class AttachAssetGroupToInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class AttachAssetGroupToInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AttachAssetGroupToInstanceResponseBody = None,
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
            temp_model = AttachAssetGroupToInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachToPolicyRequestIpPortProtocolList(TeaModel):
    def __init__(
        self,
        ip: str = None,
        port: int = None,
        protocol: str = None,
    ):
        # This parameter is required.
        self.ip = ip
        self.port = port
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.port is not None:
            result['Port'] = self.port
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        return self


class AttachToPolicyRequest(TeaModel):
    def __init__(
        self,
        ip_port_protocol_list: List[AttachToPolicyRequestIpPortProtocolList] = None,
        policy_id: str = None,
    ):
        # This parameter is required.
        self.ip_port_protocol_list = ip_port_protocol_list
        # This parameter is required.
        self.policy_id = policy_id

    def validate(self):
        if self.ip_port_protocol_list:
            for k in self.ip_port_protocol_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['IpPortProtocolList'] = []
        if self.ip_port_protocol_list is not None:
            for k in self.ip_port_protocol_list:
                result['IpPortProtocolList'].append(k.to_map() if k else None)
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ip_port_protocol_list = []
        if m.get('IpPortProtocolList') is not None:
            for k in m.get('IpPortProtocolList'):
                temp_model = AttachToPolicyRequestIpPortProtocolList()
                self.ip_port_protocol_list.append(temp_model.from_map(k))
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        return self


class AttachToPolicyShrinkRequest(TeaModel):
    def __init__(
        self,
        ip_port_protocol_list_shrink: str = None,
        policy_id: str = None,
    ):
        # This parameter is required.
        self.ip_port_protocol_list_shrink = ip_port_protocol_list_shrink
        # This parameter is required.
        self.policy_id = policy_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_port_protocol_list_shrink is not None:
            result['IpPortProtocolList'] = self.ip_port_protocol_list_shrink
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpPortProtocolList') is not None:
            self.ip_port_protocol_list_shrink = m.get('IpPortProtocolList')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        return self


class AttachToPolicyResponseBody(TeaModel):
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


class AttachToPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AttachToPolicyResponseBody = None,
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
            temp_model = AttachToPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckAccessLogAuthRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        # The ID of the region where the Anti-DDoS Origin instance resides.
        # 
        # For more information about the valid values of this parameter, see [Regions and zones](https://help.aliyun.com/document_detail/188196.html).
        self.region_id = region_id
        # The ID of the resource group to which the Anti-DDoS Origin instance belongs in Resource Management. This parameter is empty by default, which indicates that the Anti-DDoS Origin instance belongs to the default resource group.
        # 
        # For more information about resource groups, see [Create a resource group](https://help.aliyun.com/document_detail/94485.html).
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class CheckAccessLogAuthResponseBody(TeaModel):
    def __init__(
        self,
        access_log_auth: bool = None,
        request_id: str = None,
    ):
        # Indicates whether Anti-DDoS Origin was authorized to access Log Service. Valid values:
        # 
        # *   **true**: Anti-DDoS Origin was authorized.
        # *   **false**: Anti-DDoS Origin was not authorized.
        self.access_log_auth = access_log_auth
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_log_auth is not None:
            result['AccessLogAuth'] = self.access_log_auth
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessLogAuth') is not None:
            self.access_log_auth = m.get('AccessLogAuth')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CheckAccessLogAuthResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckAccessLogAuthResponseBody = None,
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
            temp_model = CheckAccessLogAuthResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckGrantRequest(TeaModel):
    def __init__(
        self,
        is_slr: bool = None,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        # Specifies whether to allow Anti-DDoS Origin to check the service-linked role. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.is_slr = is_slr
        # The ID of the region where the Anti-DDoS Origin instance resides.
        # 
        # >  You can call the [DescribeRegions](https://help.aliyun.com/document_detail/118703.html) operation to query the most recent region list.
        self.region_id = region_id
        # The ID of the resource group to which the Anti-DDoS Origin instance belongs in Resource Management.
        # 
        # If you do not specify this parameter, the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_slr is not None:
            result['IsSlr'] = self.is_slr
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsSlr') is not None:
            self.is_slr = m.get('IsSlr')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class CheckGrantResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        status: int = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether Anti-DDoS Origin is authorized to obtain information about the assets within the current Alibaba Cloud account. Valid values:
        # 
        # *   **1**: Anti-DDoS Origin is authorized to obtain information about the assets within the current Alibaba Cloud account.
        # *   **0**: Anti-DDoS Origin is not authorized to obtain information about the assets within the current Alibaba Cloud account.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CheckGrantResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckGrantResponseBody = None,
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
            temp_model = CheckGrantResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfigSchedruleOnDemandRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
        rule_action: str = None,
        rule_condition_cnt: str = None,
        rule_condition_kpps: str = None,
        rule_condition_mbps: str = None,
        rule_name: str = None,
        rule_switch: str = None,
        rule_undo_begin_time: str = None,
        rule_undo_end_time: str = None,
        rule_undo_mode: str = None,
        time_zone: str = None,
    ):
        # The ID of the on-demand instance.
        # 
        # >  You can call the [DescribeOnDemandInstance](https://help.aliyun.com/document_detail/152120.html) operation to query the IDs of all on-demand instances.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The region ID of the on-demand instance.
        # 
        # >  You can call the [DescribeRegions](https://help.aliyun.com/document_detail/118703.html) operation to query all regions supported by Anti-DDoS Origin.
        self.region_id = region_id
        # The scheduling action. Set the value to **declare**, which indicates that the route is advertised.
        # 
        # This parameter is required.
        self.rule_action = rule_action
        # If the inbound bandwidth or packets consecutively exceed the threshold for the specified number of times, the scheduling rule is triggered and traffic is rerouted to the on-demand instance. The specified number of times is the value of this parameter.
        # 
        # >  The threshold of inbound bandwidth is the value of **RuleConditionMbps**. The threshold of inbound packets is the value of **RuleConditionKpps**.
        # 
        # This parameter is required.
        self.rule_condition_cnt = rule_condition_cnt
        # The threshold of inbound packets. Unit: Kpps. Minimum value: **10**.
        # 
        # This parameter is required.
        self.rule_condition_kpps = rule_condition_kpps
        # The threshold of inbound bandwidth. Unit: Mbit/s. Minimum value: **100**.
        # 
        # This parameter is required.
        self.rule_condition_mbps = rule_condition_mbps
        # The name of the scheduling rule.
        # 
        # The name can contain lowercase letters, digits, hyphens (-), and underscores (_). The name can be up to 32 characters in length. We recommend that you use the ID of the on-demand instance as the name. Example: `ddosbgp-cn-z2q1qzxb****`.
        # 
        # This parameter is required.
        self.rule_name = rule_name
        # Specifies whether the scheduling rule is enabled. Valid values:
        # 
        # *   **on**: enabled
        # *   **off**: disabled
        # 
        # This parameter is required.
        self.rule_switch = rule_switch
        # The start time of the period during which the scheduling rule is automatically stopped. The time must be in the 24-hour clock and in the `hh:mm` format.
        # 
        # If the system detects that DDoS attacks stop, the system no longer reroutes traffic to the on-demand instance from the time you specified. We recommend that you set this parameter to a value that is defined as off-peak hours.
        # 
        # >  This parameter takes effect only when the **RuleUndoMode** parameter is set to **auto**.
        # 
        # This parameter is required.
        self.rule_undo_begin_time = rule_undo_begin_time
        # The end time of the period during which the scheduling rule is automatically stopped. The time must be in the 24-hour clock and in the `hh:mm` format.
        self.rule_undo_end_time = rule_undo_end_time
        # The stop method of the scheduling rule. Valid values:
        # 
        # *   **auto**: The scheduling rule automatically stops.
        # *   **manual**: The scheduling rule is manually stopped.
        # 
        # This parameter is required.
        self.rule_undo_mode = rule_undo_mode
        # The time zone of the time when the scheduling rule automatically stops. The time zone must be in the `GMT-hh:mm` format.
        # 
        # For example, the value `GMT-08:00` indicates that the time zone is UTC+8.
        # 
        # >  This parameter takes effect only when the **RuleUndoMode** parameter is set to **auto**.
        # 
        # This parameter is required.
        self.time_zone = time_zone

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
        if self.rule_action is not None:
            result['RuleAction'] = self.rule_action
        if self.rule_condition_cnt is not None:
            result['RuleConditionCnt'] = self.rule_condition_cnt
        if self.rule_condition_kpps is not None:
            result['RuleConditionKpps'] = self.rule_condition_kpps
        if self.rule_condition_mbps is not None:
            result['RuleConditionMbps'] = self.rule_condition_mbps
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_switch is not None:
            result['RuleSwitch'] = self.rule_switch
        if self.rule_undo_begin_time is not None:
            result['RuleUndoBeginTime'] = self.rule_undo_begin_time
        if self.rule_undo_end_time is not None:
            result['RuleUndoEndTime'] = self.rule_undo_end_time
        if self.rule_undo_mode is not None:
            result['RuleUndoMode'] = self.rule_undo_mode
        if self.time_zone is not None:
            result['TimeZone'] = self.time_zone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RuleAction') is not None:
            self.rule_action = m.get('RuleAction')
        if m.get('RuleConditionCnt') is not None:
            self.rule_condition_cnt = m.get('RuleConditionCnt')
        if m.get('RuleConditionKpps') is not None:
            self.rule_condition_kpps = m.get('RuleConditionKpps')
        if m.get('RuleConditionMbps') is not None:
            self.rule_condition_mbps = m.get('RuleConditionMbps')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleSwitch') is not None:
            self.rule_switch = m.get('RuleSwitch')
        if m.get('RuleUndoBeginTime') is not None:
            self.rule_undo_begin_time = m.get('RuleUndoBeginTime')
        if m.get('RuleUndoEndTime') is not None:
            self.rule_undo_end_time = m.get('RuleUndoEndTime')
        if m.get('RuleUndoMode') is not None:
            self.rule_undo_mode = m.get('RuleUndoMode')
        if m.get('TimeZone') is not None:
            self.time_zone = m.get('TimeZone')
        return self


class ConfigSchedruleOnDemandResponseBody(TeaModel):
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


class ConfigSchedruleOnDemandResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ConfigSchedruleOnDemandResponseBody = None,
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
            temp_model = ConfigSchedruleOnDemandResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePolicyRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
    ):
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreatePolicyResponseBody(TeaModel):
    def __init__(
        self,
        id: str = None,
        request_id: str = None,
    ):
        self.id = id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreatePolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreatePolicyResponseBody = None,
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
            temp_model = CreatePolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSchedruleOnDemandRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
        rule_action: str = None,
        rule_condition_cnt: str = None,
        rule_condition_kpps: str = None,
        rule_condition_mbps: str = None,
        rule_name: str = None,
        rule_switch: str = None,
        rule_undo_begin_time: str = None,
        rule_undo_end_time: str = None,
        rule_undo_mode: str = None,
        time_zone: str = None,
    ):
        # The ID of the on-demand instance.
        # 
        # >  You can call the [DescribeOnDemandInstance](https://help.aliyun.com/document_detail/152120.html) operation to query the IDs of all on-demand instances.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The region ID of the on-demand instance.
        # 
        # >  You can call the [DescribeRegions](https://help.aliyun.com/document_detail/118703.html) operation to query all regions supported by Anti-DDoS Origin.
        self.region_id = region_id
        # The scheduling action. Set the value to **declare**, which indicates that the route is advertised.
        # 
        # This parameter is required.
        self.rule_action = rule_action
        # If the inbound bandwidth or packets consecutively exceed the threshold for the specified number of times, the scheduling rule is triggered and traffic is rerouted to the on-demand instance. The specified number of times is the value of this parameter.
        # 
        # >  The threshold of inbound bandwidth is the value of **RuleConditionMbps**. The threshold of inbound packets is the value of **RuleConditionKpps**.
        # 
        # This parameter is required.
        self.rule_condition_cnt = rule_condition_cnt
        # The threshold of inbound packets. Unit: Kpps. Minimum value: **10**.
        # 
        # This parameter is required.
        self.rule_condition_kpps = rule_condition_kpps
        # The threshold of inbound bandwidth. Unit: Mbit/s. Minimum value: **100**.
        # 
        # This parameter is required.
        self.rule_condition_mbps = rule_condition_mbps
        # The name of the scheduling rule.
        # 
        # The name can contain lowercase letters, digits, hyphens (-), and underscores (_). The name can be up to 32 characters in length. We recommend that you use the ID of the on-demand instance as the name. Example: `ddosbgp-cn-z2q1qzxb****`.
        # 
        # This parameter is required.
        self.rule_name = rule_name
        # Specifies whether the scheduling rule is enabled. Valid values:
        # 
        # *   **on**: enabled
        # *   **off**: disabled
        # 
        # This parameter is required.
        self.rule_switch = rule_switch
        # The start time of the period during which the scheduling rule is automatically stopped. The time must be in the 24-hour clock and in the `hh:mm` format.
        # 
        # If the system detects that DDoS attacks stop, the system no longer reroutes traffic to the on-demand instance from the time you specified. We recommend that you set this parameter to a value that is defined as off-peak hours.
        # 
        # >  This parameter takes effect only when the **RuleUndoMode** parameter is set to **auto**.
        # 
        # This parameter is required.
        self.rule_undo_begin_time = rule_undo_begin_time
        # The end time of the period during which the scheduling rule is automatically stopped. The time must be in the 24-hour clock and in the `hh:mm` format.
        self.rule_undo_end_time = rule_undo_end_time
        # The stop method of the scheduling rule. Valid values:
        # 
        # *   **auto**: The scheduling rule automatically stops.
        # *   **manual**: The scheduling rule is manually stopped.
        # 
        # This parameter is required.
        self.rule_undo_mode = rule_undo_mode
        # The time zone of the time when the scheduling rule automatically stops. The time zone must be in the `GMT-hh:mm` format.
        # 
        # For example, the value `GMT-08:00` indicates that the time zone is UTC+8.
        # 
        # >  This parameter takes effect only when the **RuleUndoMode** parameter is set to **auto**.
        # 
        # This parameter is required.
        self.time_zone = time_zone

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
        if self.rule_action is not None:
            result['RuleAction'] = self.rule_action
        if self.rule_condition_cnt is not None:
            result['RuleConditionCnt'] = self.rule_condition_cnt
        if self.rule_condition_kpps is not None:
            result['RuleConditionKpps'] = self.rule_condition_kpps
        if self.rule_condition_mbps is not None:
            result['RuleConditionMbps'] = self.rule_condition_mbps
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_switch is not None:
            result['RuleSwitch'] = self.rule_switch
        if self.rule_undo_begin_time is not None:
            result['RuleUndoBeginTime'] = self.rule_undo_begin_time
        if self.rule_undo_end_time is not None:
            result['RuleUndoEndTime'] = self.rule_undo_end_time
        if self.rule_undo_mode is not None:
            result['RuleUndoMode'] = self.rule_undo_mode
        if self.time_zone is not None:
            result['TimeZone'] = self.time_zone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RuleAction') is not None:
            self.rule_action = m.get('RuleAction')
        if m.get('RuleConditionCnt') is not None:
            self.rule_condition_cnt = m.get('RuleConditionCnt')
        if m.get('RuleConditionKpps') is not None:
            self.rule_condition_kpps = m.get('RuleConditionKpps')
        if m.get('RuleConditionMbps') is not None:
            self.rule_condition_mbps = m.get('RuleConditionMbps')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleSwitch') is not None:
            self.rule_switch = m.get('RuleSwitch')
        if m.get('RuleUndoBeginTime') is not None:
            self.rule_undo_begin_time = m.get('RuleUndoBeginTime')
        if m.get('RuleUndoEndTime') is not None:
            self.rule_undo_end_time = m.get('RuleUndoEndTime')
        if m.get('RuleUndoMode') is not None:
            self.rule_undo_mode = m.get('RuleUndoMode')
        if m.get('TimeZone') is not None:
            self.time_zone = m.get('TimeZone')
        return self


class CreateSchedruleOnDemandResponseBody(TeaModel):
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


class CreateSchedruleOnDemandResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateSchedruleOnDemandResponseBody = None,
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
            temp_model = CreateSchedruleOnDemandResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteBlackholeRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        ip: str = None,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        # The ID of the Anti-DDoS Origin instance.
        # 
        # >  You can call the [DescribeInstanceList](https://help.aliyun.com/document_detail/118698.html) operation to query the IDs of all Anti-DDoS Origin instances.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The IP address for which you want to deactivate blackhole filtering.
        # 
        # >  You can call the [DescribePackIpList](https://help.aliyun.com/document_detail/118701.html) operation to query all the IP addresses that are protected by the Anti-DDoS Origin instance and the protection status of the IP addresses. For example, you can query whether blackhole filtering is triggered for an IP address.
        # 
        # This parameter is required.
        self.ip = ip
        # The ID of the region where the Anti-DDoS Origin instance resides.
        # 
        # >  You can call the [DescribeRegions](https://help.aliyun.com/document_detail/118703.html) operation to query the most recent region list.
        self.region_id = region_id
        # The ID of the resource group to which the Anti-DDoS Origin instance belongs in Resource Management.
        # 
        # If you do not specify this parameter, the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DeleteBlackholeResponseBody(TeaModel):
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


class DeleteBlackholeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteBlackholeResponseBody = None,
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
            temp_model = DeleteBlackholeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteIpRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        ip_list: str = None,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        # The ID of the Anti-DDoS Origin Enterprise instance.
        # 
        # >  You can call the [DescribeInstanceList](https://help.aliyun.com/document_detail/118698.html) operation to query the IDs of all Anti-DDoS Origin Enterprise instances.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The list of IP addresses that you want to remove from the Anti-DDoS Origin Enterprise instance. This parameter is a string consisting of JSON arrays. Each element in a JSON array is a JSON struct that includes the following field:
        # 
        # *   **ip**: required. The IP address that you want to remove. Data type: string.
        # 
        #     > The IP addresses that you want to remove must be protected by the Anti-DDoS Origin Enterprise instance.
        # 
        # This parameter is required.
        self.ip_list = ip_list
        # The region ID of the Anti-DDoS Origin Enterprise instance.
        # 
        # >  You can call the [DescribeRegions](https://help.aliyun.com/document_detail/118703.html) operation to query all regions supported by Anti-DDoS Origin.
        self.region_id = region_id
        # The ID of the resource group to which the Anti-DDoS Origin Enterprise instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        # 
        # For more information about resource groups, see [Create a resource group](https://help.aliyun.com/document_detail/94485.html).
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ip_list is not None:
            result['IpList'] = self.ip_list
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IpList') is not None:
            self.ip_list = m.get('IpList')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DeleteIpResponseBody(TeaModel):
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


class DeleteIpResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteIpResponseBody = None,
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
            temp_model = DeleteIpResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePolicyRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        # This parameter is required.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DeletePolicyResponseBody(TeaModel):
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


class DeletePolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeletePolicyResponseBody = None,
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
            temp_model = DeletePolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRdMemberListRequestMemberList(TeaModel):
    def __init__(
        self,
        uid: str = None,
    ):
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class DeleteRdMemberListRequest(TeaModel):
    def __init__(
        self,
        member_list: List[DeleteRdMemberListRequestMemberList] = None,
    ):
        # This parameter is required.
        self.member_list = member_list

    def validate(self):
        if self.member_list:
            for k in self.member_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MemberList'] = []
        if self.member_list is not None:
            for k in self.member_list:
                result['MemberList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.member_list = []
        if m.get('MemberList') is not None:
            for k in m.get('MemberList'):
                temp_model = DeleteRdMemberListRequestMemberList()
                self.member_list.append(temp_model.from_map(k))
        return self


class DeleteRdMemberListShrinkRequest(TeaModel):
    def __init__(
        self,
        member_list_shrink: str = None,
    ):
        # This parameter is required.
        self.member_list_shrink = member_list_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.member_list_shrink is not None:
            result['MemberList'] = self.member_list_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MemberList') is not None:
            self.member_list_shrink = m.get('MemberList')
        return self


class DeleteRdMemberListResponseBody(TeaModel):
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


class DeleteRdMemberListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteRdMemberListResponseBody = None,
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
            temp_model = DeleteRdMemberListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSchedruleOnDemandRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
        rule_name: str = None,
    ):
        # The ID of the on-demand instance.
        # 
        # >  You can call the [DescribeOnDemandInstance](https://help.aliyun.com/document_detail/152120.html) operation to query the IDs of all on-demand instances.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The region ID of the on-demand instance.
        # 
        # >  You can call the [DescribeRegions](https://help.aliyun.com/document_detail/118703.html) operation to query all regions supported by Anti-DDoS Origin.
        self.region_id = region_id
        # The name of the scheduling rule that you want to delete.
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


class DeleteSchedruleOnDemandResponseBody(TeaModel):
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


class DeleteSchedruleOnDemandResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteSchedruleOnDemandResponseBody = None,
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
            temp_model = DeleteSchedruleOnDemandResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAssetGroupRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        region: str = None,
        region_id: str = None,
        type: str = None,
    ):
        # The ID of the asset. If the asset is a Web Application Firewall (WAF) instance, specify the ID of the WAF instance.
        self.name = name
        # The region ID of the asset.
        # 
        # This parameter is required.
        self.region = region
        # The ID of the region in which the instance resides.
        # 
        # >  You can call the [DescribeRegions](https://help.aliyun.com/document_detail/118703.html) operation to query the most recent region list.
        self.region_id = region_id
        # The type of the asset. Valid values:
        # 
        # *   **waf**: WAF instance
        # *   **ga**: Global Accelerator (GA) instance
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.region is not None:
            result['Region'] = self.region
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeAssetGroupResponseBodyAssetGroupList(TeaModel):
    def __init__(
        self,
        name: str = None,
        region: str = None,
        type: str = None,
    ):
        # The ID of the asset.
        self.name = name
        # The region to which the asset belongs.
        self.region = region
        # The type of the asset.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.region is not None:
            result['Region'] = self.region
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeAssetGroupResponseBody(TeaModel):
    def __init__(
        self,
        asset_group_list: List[DescribeAssetGroupResponseBodyAssetGroupList] = None,
        request_id: str = None,
        total: int = None,
    ):
        # The information about the asset.
        self.asset_group_list = asset_group_list
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total = total

    def validate(self):
        if self.asset_group_list:
            for k in self.asset_group_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AssetGroupList'] = []
        if self.asset_group_list is not None:
            for k in self.asset_group_list:
                result['AssetGroupList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.asset_group_list = []
        if m.get('AssetGroupList') is not None:
            for k in m.get('AssetGroupList'):
                temp_model = DescribeAssetGroupResponseBodyAssetGroupList()
                self.asset_group_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribeAssetGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAssetGroupResponseBody = None,
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
            temp_model = DescribeAssetGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAssetGroupToInstanceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        member_uid: str = None,
        name: str = None,
        region: str = None,
        region_id: str = None,
        type: str = None,
    ):
        # The ID of the instance to query.
        # 
        # >  You can call the [DescribeInstanceList](https://help.aliyun.com/document_detail/118698.html) operation to query the IDs of all Anti-DDoS Origin instances of paid editions.
        self.instance_id = instance_id
        # The UID of the member to which the asset belongs.
        self.member_uid = member_uid
        # The ID of the asset. If the asset is a Web Application Firewall (WAF) instance, specify the ID of the WAF instance.
        self.name = name
        # The region ID of the asset.
        self.region = region
        # The ID of the region in which the instance resides.
        # 
        # >  You can call the [DescribeRegions](https://help.aliyun.com/document_detail/118703.html) operation to query the most recent region list.
        self.region_id = region_id
        # The type of the asset. Valid values:
        # 
        # *   **waf**: WAF instance
        # *   **ga**: Global Accelerator (GA) instance
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid
        if self.name is not None:
            result['Name'] = self.name
        if self.region is not None:
            result['Region'] = self.region
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeAssetGroupToInstanceResponseBodyDataList(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        member_uid: str = None,
        name: str = None,
        region: str = None,
        type: str = None,
    ):
        # The ID of the Anti-DDoS Origin instance of a paid edition.
        self.instance_id = instance_id
        # The UID of the member to which the asset belongs.
        self.member_uid = member_uid
        # The ID of the asset.
        self.name = name
        # The region ID of the asset.
        self.region = region
        # The type of the asset.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid
        if self.name is not None:
            result['Name'] = self.name
        if self.region is not None:
            result['Region'] = self.region
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeAssetGroupToInstanceResponseBody(TeaModel):
    def __init__(
        self,
        data_list: List[DescribeAssetGroupToInstanceResponseBodyDataList] = None,
        request_id: str = None,
        total: int = None,
    ):
        # The response parameters.
        self.data_list = data_list
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total = total

    def validate(self):
        if self.data_list:
            for k in self.data_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataList'] = []
        if self.data_list is not None:
            for k in self.data_list:
                result['DataList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_list = []
        if m.get('DataList') is not None:
            for k in m.get('DataList'):
                temp_model = DescribeAssetGroupToInstanceResponseBodyDataList()
                self.data_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribeAssetGroupToInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAssetGroupToInstanceResponseBody = None,
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
            temp_model = DescribeAssetGroupToInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDdosEventRequest(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        instance_id: str = None,
        ip: str = None,
        page_no: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        start_time: int = None,
    ):
        # The end time of the DDoS attack event to query. This value is a UNIX timestamp. Unit: seconds.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The ID of the Anti-DDoS Origin instance to query.
        # 
        # >  You can call the [DescribeInstanceList](https://help.aliyun.com/document_detail/118698.html) operation to query the IDs of all Anti-DDoS Origin instances.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The attacked IP address to query.
        self.ip = ip
        # The number of the page to return.
        # 
        # This parameter is required.
        self.page_no = page_no
        # The number of entries to return on each page.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The ID of the region where the Anti-DDoS Origin instance resides.
        # 
        # >  You can call the [DescribeRegions](https://help.aliyun.com/document_detail/118703.html) operation to query the most recent region list.
        self.region_id = region_id
        # The ID of the resource group to which the Anti-DDoS Origin instance belongs in Resource Management.
        # 
        # If you do not specify this parameter, the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id
        # The start time of the DDoS attack event to query. This value is a UNIX timestamp. Unit: seconds.
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
            result['EndTime'] = self.end_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDdosEventResponseBodyEvents(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        ip: str = None,
        mbps: int = None,
        pps: int = None,
        start_time: int = None,
        status: str = None,
    ):
        # The time when the DDoS attack stopped. This value is a UNIX timestamp. Unit: seconds.
        self.end_time = end_time
        # The attacked IP address.
        self.ip = ip
        # The volume of the request traffic at the start of the DDoS attack. Unit: Mbit/s.
        self.mbps = mbps
        # The number of packets at the start of the DDoS attack. Unit: packets per second (PPS).
        self.pps = pps
        # The time when the DDoS attack started. This value is a UNIX timestamp. Unit: seconds.
        self.start_time = start_time
        # The status of the DDoS attack event. Valid values:
        # 
        # *   **hole_begin**: indicates that blackhole filtering is triggered for the attacked IP address.
        # *   **hole_end**: indicates that blackhole filtering is deactivated for the attacked IP address.
        # *   **defense_begin**: indicates that attack traffic is being scrubbed.
        # *   **defense_end**: indicates that attack traffic is scrubbed.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.mbps is not None:
            result['Mbps'] = self.mbps
        if self.pps is not None:
            result['Pps'] = self.pps
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Mbps') is not None:
            self.mbps = m.get('Mbps')
        if m.get('Pps') is not None:
            self.pps = m.get('Pps')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeDdosEventResponseBody(TeaModel):
    def __init__(
        self,
        events: List[DescribeDdosEventResponseBodyEvents] = None,
        request_id: str = None,
        total: int = None,
    ):
        # The details about the DDoS attack event.
        self.events = events
        # The ID of the request.
        self.request_id = request_id
        # The total number of DDoS attack events.
        self.total = total

    def validate(self):
        if self.events:
            for k in self.events:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Events'] = []
        if self.events is not None:
            for k in self.events:
                result['Events'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.events = []
        if m.get('Events') is not None:
            for k in m.get('Events'):
                temp_model = DescribeDdosEventResponseBodyEvents()
                self.events.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribeDdosEventResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDdosEventResponseBody = None,
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
            temp_model = DescribeDdosEventResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDdosOriginInstanceBillRequest(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        is_show_list: bool = None,
        start_time: int = None,
        type: str = None,
    ):
        self.end_time = end_time
        self.is_show_list = is_show_list
        self.start_time = start_time
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.is_show_list is not None:
            result['IsShowList'] = self.is_show_list
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('IsShowList') is not None:
            self.is_show_list = m.get('IsShowList')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeDdosOriginInstanceBillResponseBodyFlowList(TeaModel):
    def __init__(
        self,
        member_flow: str = None,
        region_flow: str = None,
        time: int = None,
        total_flow: int = None,
    ):
        self.member_flow = member_flow
        self.region_flow = region_flow
        self.time = time
        self.total_flow = total_flow

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.member_flow is not None:
            result['MemberFlow'] = self.member_flow
        if self.region_flow is not None:
            result['RegionFlow'] = self.region_flow
        if self.time is not None:
            result['Time'] = self.time
        if self.total_flow is not None:
            result['TotalFlow'] = self.total_flow
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MemberFlow') is not None:
            self.member_flow = m.get('MemberFlow')
        if m.get('RegionFlow') is not None:
            self.region_flow = m.get('RegionFlow')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('TotalFlow') is not None:
            self.total_flow = m.get('TotalFlow')
        return self


class DescribeDdosOriginInstanceBillResponseBodyIpCountOrFunctionList(TeaModel):
    def __init__(
        self,
        coverage: str = None,
        ip_cnt_cn: int = None,
        ip_cnt_ov: int = None,
        member_ip_cnt: str = None,
        time: int = None,
    ):
        self.coverage = coverage
        self.ip_cnt_cn = ip_cnt_cn
        self.ip_cnt_ov = ip_cnt_ov
        self.member_ip_cnt = member_ip_cnt
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.coverage is not None:
            result['Coverage'] = self.coverage
        if self.ip_cnt_cn is not None:
            result['IpCntCn'] = self.ip_cnt_cn
        if self.ip_cnt_ov is not None:
            result['IpCntOv'] = self.ip_cnt_ov
        if self.member_ip_cnt is not None:
            result['MemberIpCnt'] = self.member_ip_cnt
        if self.time is not None:
            result['Time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Coverage') is not None:
            self.coverage = m.get('Coverage')
        if m.get('IpCntCn') is not None:
            self.ip_cnt_cn = m.get('IpCntCn')
        if m.get('IpCntOv') is not None:
            self.ip_cnt_ov = m.get('IpCntOv')
        if m.get('MemberIpCnt') is not None:
            self.member_ip_cnt = m.get('MemberIpCnt')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        return self


class DescribeDdosOriginInstanceBillResponseBodyStandardAssetsFlowList(TeaModel):
    def __init__(
        self,
        member_flow: str = None,
        region_flow: str = None,
        time: int = None,
        total_flow: int = None,
    ):
        self.member_flow = member_flow
        self.region_flow = region_flow
        self.time = time
        self.total_flow = total_flow

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.member_flow is not None:
            result['MemberFlow'] = self.member_flow
        if self.region_flow is not None:
            result['RegionFlow'] = self.region_flow
        if self.time is not None:
            result['Time'] = self.time
        if self.total_flow is not None:
            result['TotalFlow'] = self.total_flow
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MemberFlow') is not None:
            self.member_flow = m.get('MemberFlow')
        if m.get('RegionFlow') is not None:
            self.region_flow = m.get('RegionFlow')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('TotalFlow') is not None:
            self.total_flow = m.get('TotalFlow')
        return self


class DescribeDdosOriginInstanceBillResponseBody(TeaModel):
    def __init__(
        self,
        debt_status: int = None,
        flow_list: List[DescribeDdosOriginInstanceBillResponseBodyFlowList] = None,
        flow_region: Dict[str, Any] = None,
        instance_id: str = None,
        ip_count: int = None,
        ip_count_or_function_list: List[DescribeDdosOriginInstanceBillResponseBodyIpCountOrFunctionList] = None,
        ip_info: str = None,
        request_id: str = None,
        standard_assets_flow_list: List[DescribeDdosOriginInstanceBillResponseBodyStandardAssetsFlowList] = None,
        standard_assets_flow_region: Dict[str, Any] = None,
        standard_assets_total_flow_cn: int = None,
        standard_assets_total_flow_ov: int = None,
        status: int = None,
        total_flow_cn: int = None,
        total_flow_ov: int = None,
    ):
        self.debt_status = debt_status
        self.flow_list = flow_list
        self.flow_region = flow_region
        self.instance_id = instance_id
        self.ip_count = ip_count
        self.ip_count_or_function_list = ip_count_or_function_list
        self.ip_info = ip_info
        self.request_id = request_id
        self.standard_assets_flow_list = standard_assets_flow_list
        self.standard_assets_flow_region = standard_assets_flow_region
        self.standard_assets_total_flow_cn = standard_assets_total_flow_cn
        self.standard_assets_total_flow_ov = standard_assets_total_flow_ov
        self.status = status
        self.total_flow_cn = total_flow_cn
        self.total_flow_ov = total_flow_ov

    def validate(self):
        if self.flow_list:
            for k in self.flow_list:
                if k:
                    k.validate()
        if self.ip_count_or_function_list:
            for k in self.ip_count_or_function_list:
                if k:
                    k.validate()
        if self.standard_assets_flow_list:
            for k in self.standard_assets_flow_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.debt_status is not None:
            result['DebtStatus'] = self.debt_status
        result['FlowList'] = []
        if self.flow_list is not None:
            for k in self.flow_list:
                result['FlowList'].append(k.to_map() if k else None)
        if self.flow_region is not None:
            result['FlowRegion'] = self.flow_region
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ip_count is not None:
            result['IpCount'] = self.ip_count
        result['IpCountOrFunctionList'] = []
        if self.ip_count_or_function_list is not None:
            for k in self.ip_count_or_function_list:
                result['IpCountOrFunctionList'].append(k.to_map() if k else None)
        if self.ip_info is not None:
            result['IpInfo'] = self.ip_info
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['StandardAssetsFlowList'] = []
        if self.standard_assets_flow_list is not None:
            for k in self.standard_assets_flow_list:
                result['StandardAssetsFlowList'].append(k.to_map() if k else None)
        if self.standard_assets_flow_region is not None:
            result['StandardAssetsFlowRegion'] = self.standard_assets_flow_region
        if self.standard_assets_total_flow_cn is not None:
            result['StandardAssetsTotalFlowCn'] = self.standard_assets_total_flow_cn
        if self.standard_assets_total_flow_ov is not None:
            result['StandardAssetsTotalFlowOv'] = self.standard_assets_total_flow_ov
        if self.status is not None:
            result['Status'] = self.status
        if self.total_flow_cn is not None:
            result['TotalFlowCn'] = self.total_flow_cn
        if self.total_flow_ov is not None:
            result['TotalFlowOv'] = self.total_flow_ov
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DebtStatus') is not None:
            self.debt_status = m.get('DebtStatus')
        self.flow_list = []
        if m.get('FlowList') is not None:
            for k in m.get('FlowList'):
                temp_model = DescribeDdosOriginInstanceBillResponseBodyFlowList()
                self.flow_list.append(temp_model.from_map(k))
        if m.get('FlowRegion') is not None:
            self.flow_region = m.get('FlowRegion')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IpCount') is not None:
            self.ip_count = m.get('IpCount')
        self.ip_count_or_function_list = []
        if m.get('IpCountOrFunctionList') is not None:
            for k in m.get('IpCountOrFunctionList'):
                temp_model = DescribeDdosOriginInstanceBillResponseBodyIpCountOrFunctionList()
                self.ip_count_or_function_list.append(temp_model.from_map(k))
        if m.get('IpInfo') is not None:
            self.ip_info = m.get('IpInfo')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.standard_assets_flow_list = []
        if m.get('StandardAssetsFlowList') is not None:
            for k in m.get('StandardAssetsFlowList'):
                temp_model = DescribeDdosOriginInstanceBillResponseBodyStandardAssetsFlowList()
                self.standard_assets_flow_list.append(temp_model.from_map(k))
        if m.get('StandardAssetsFlowRegion') is not None:
            self.standard_assets_flow_region = m.get('StandardAssetsFlowRegion')
        if m.get('StandardAssetsTotalFlowCn') is not None:
            self.standard_assets_total_flow_cn = m.get('StandardAssetsTotalFlowCn')
        if m.get('StandardAssetsTotalFlowOv') is not None:
            self.standard_assets_total_flow_ov = m.get('StandardAssetsTotalFlowOv')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TotalFlowCn') is not None:
            self.total_flow_cn = m.get('TotalFlowCn')
        if m.get('TotalFlowOv') is not None:
            self.total_flow_ov = m.get('TotalFlowOv')
        return self


class DescribeDdosOriginInstanceBillResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDdosOriginInstanceBillResponseBody = None,
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
            temp_model = DescribeDdosOriginInstanceBillResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeExcpetionCountRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        # The ID of the region where the Anti-DDoS Origin instance resides.
        # 
        # >  You can call the [DescribeRegions](https://help.aliyun.com/document_detail/118703.html) operation to query the most recent region list.
        self.region_id = region_id
        # The ID of the resource group to which the Anti-DDoS Origin instance belongs in Resource Management.
        # 
        # If you do not specify this parameter, the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeExcpetionCountResponseBody(TeaModel):
    def __init__(
        self,
        exception_ip_count: int = None,
        expire_time_count: int = None,
        request_id: str = None,
    ):
        # The number of assets that are in an abnormal state.
        self.exception_ip_count = exception_ip_count
        # The number of Anti-DDoS Origin instances that are about to expire.
        self.expire_time_count = expire_time_count
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exception_ip_count is not None:
            result['ExceptionIpCount'] = self.exception_ip_count
        if self.expire_time_count is not None:
            result['ExpireTimeCount'] = self.expire_time_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExceptionIpCount') is not None:
            self.exception_ip_count = m.get('ExceptionIpCount')
        if m.get('ExpireTimeCount') is not None:
            self.expire_time_count = m.get('ExpireTimeCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeExcpetionCountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeExcpetionCountResponseBody = None,
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
            temp_model = DescribeExcpetionCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceListRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag that is added to the Anti-DDoS Origin instance to query.
        self.key = key
        # The value of the tag that is added to the Anti-DDoS Origin instance to query.
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


class DescribeInstanceListRequest(TeaModel):
    def __init__(
        self,
        instance_id_list: str = None,
        instance_type: str = None,
        instance_type_list: List[str] = None,
        ip: str = None,
        ip_version: str = None,
        orderby: str = None,
        orderdire: str = None,
        page_no: int = None,
        page_size: int = None,
        region_id: str = None,
        remark: str = None,
        resource_group_id: str = None,
        tag: List[DescribeInstanceListRequestTag] = None,
    ):
        # The IDs of the Anti-DDoS Origin instances to query. Specify the value is in the `["<Instance ID 1>","<Instance ID 2>",……]` format.
        self.instance_id_list = instance_id_list
        # The mitigation plan of the Anti-DDoS Origin instance to query. Valid values:
        # 
        # *   **0**: the Professional mitigation plan
        # *   **1**: the Enterprise mitigation plan
        self.instance_type = instance_type
        self.instance_type_list = instance_type_list
        # The IP address of the object that is protected by the Anti-DDoS Origin instance to query.
        self.ip = ip
        # The protocol type of the IP address asset that is protected by the Anti-DDoS Origin instance to query. Valid values:
        # 
        # *   **Ipv4**: IPv4
        # *   **Ipv6**: IPv6
        self.ip_version = ip_version
        # The field that is used to sort the Anti-DDoS Origin instances. Set the value to **expireTime**, which indicates that the instances are sorted based on the expiration time.
        # 
        # You can set the **Orderdire** parameter to specify the sorting method.
        self.orderby = orderby
        # The sorting method. Valid values:
        # 
        # *   **desc**: the descending order. This is the default value.
        # *   **asc**: the ascending order.
        self.orderdire = orderdire
        # The number of the page to return.
        # 
        # This parameter is required.
        self.page_no = page_no
        # The number of entries to return on each page.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The ID of the region where the Anti-DDoS Origin instance to query resides.
        # 
        # >  You can call the [DescribeRegions](https://help.aliyun.com/document_detail/118703.html) operation to query the most recent region list.
        self.region_id = region_id
        # The remarks of the Anti-DDoS Origin instance to query. Fuzzy match is supported.
        self.remark = remark
        # The ID of the resource group to which the Anti-DDoS Origin instance belongs in Resource Management.
        # 
        # If you do not specify this parameter, the instance belongs to the default resource group.
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
        if self.instance_id_list is not None:
            result['InstanceIdList'] = self.instance_id_list
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.instance_type_list is not None:
            result['InstanceTypeList'] = self.instance_type_list
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version
        if self.orderby is not None:
            result['Orderby'] = self.orderby
        if self.orderdire is not None:
            result['Orderdire'] = self.orderdire
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIdList') is not None:
            self.instance_id_list = m.get('InstanceIdList')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('InstanceTypeList') is not None:
            self.instance_type_list = m.get('InstanceTypeList')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')
        if m.get('Orderby') is not None:
            self.orderby = m.get('Orderby')
        if m.get('Orderdire') is not None:
            self.orderdire = m.get('Orderdire')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeInstanceListRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeInstanceListResponseBodyInstanceListAutoProtectCondition(TeaModel):
    def __init__(
        self,
        events: List[str] = None,
    ):
        self.events = events

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.events is not None:
            result['Events'] = self.events
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Events') is not None:
            self.events = m.get('Events')
        return self


class DescribeInstanceListResponseBodyInstanceList(TeaModel):
    def __init__(
        self,
        auto_protect_condition: DescribeInstanceListResponseBodyInstanceListAutoProtectCondition = None,
        auto_renewal: bool = None,
        blackholding_count: str = None,
        commodity_type: str = None,
        coverage_type: int = None,
        expire_time: int = None,
        gmt_create: int = None,
        instance_id: str = None,
        instance_type: str = None,
        ip_type: str = None,
        product: str = None,
        remark: str = None,
        status: str = None,
    ):
        self.auto_protect_condition = auto_protect_condition
        # Indicates whether auto-renewal is enabled for the instance. Valid values:
        # 
        # *   **true**: enabled
        # *   **false**: disabled
        self.auto_renewal = auto_renewal
        # The number of protected public IP addresses for which blackhole filtering is triggered.
        # 
        # >  You can call the [DeleteBlackhole](https://help.aliyun.com/document_detail/118692.html) operation to deactivate blackhole filtering for a protected IP address.
        self.blackholding_count = blackholding_count
        self.commodity_type = commodity_type
        self.coverage_type = coverage_type
        # The time when the instance expires. This value is a UNIX timestamp. Unit: milliseconds.
        self.expire_time = expire_time
        # The time when the instance was purchased. This value is a UNIX timestamp. Unit: milliseconds.
        self.gmt_create = gmt_create
        # The ID of the instance.
        self.instance_id = instance_id
        # The mitigation plan of the instance. Valid values:
        # 
        # *   **0**: the Professional mitigation plan
        # *   **1**: the Enterprise mitigation plan
        self.instance_type = instance_type
        # The protocol type of the IP address asset that is protected by the instance. Valid values:
        # 
        # *   **Ipv4**: IPv4
        # *   **Ipv6**: IPv6
        self.ip_type = ip_type
        # The type of the cloud service that is associated with the Anti-DDoS Origin instance. By default, this parameter is not returned. If the Anti-DDoS Origin instance is created by using a different cloud service, the code of the cloud service is returned.
        # 
        # Valid values:
        # 
        # *   **gamebox**: The Anti-DDoS Origin instance is created by using Game Security Box.
        # *   **eip**: The Anti-DDoS Origin instance is created by using an elastic IP address (EIP) for which Anti-DDoS (Enhanced Edition) is enabled.
        self.product = product
        # The remarks of the instance.
        self.remark = remark
        # The status of the instance. Valid values:
        # 
        # *   **1**: normal
        # *   **2**: expired
        # *   **3**: released
        self.status = status

    def validate(self):
        if self.auto_protect_condition:
            self.auto_protect_condition.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_protect_condition is not None:
            result['AutoProtectCondition'] = self.auto_protect_condition.to_map()
        if self.auto_renewal is not None:
            result['AutoRenewal'] = self.auto_renewal
        if self.blackholding_count is not None:
            result['BlackholdingCount'] = self.blackholding_count
        if self.commodity_type is not None:
            result['CommodityType'] = self.commodity_type
        if self.coverage_type is not None:
            result['CoverageType'] = self.coverage_type
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.ip_type is not None:
            result['IpType'] = self.ip_type
        if self.product is not None:
            result['Product'] = self.product
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoProtectCondition') is not None:
            temp_model = DescribeInstanceListResponseBodyInstanceListAutoProtectCondition()
            self.auto_protect_condition = temp_model.from_map(m['AutoProtectCondition'])
        if m.get('AutoRenewal') is not None:
            self.auto_renewal = m.get('AutoRenewal')
        if m.get('BlackholdingCount') is not None:
            self.blackholding_count = m.get('BlackholdingCount')
        if m.get('CommodityType') is not None:
            self.commodity_type = m.get('CommodityType')
        if m.get('CoverageType') is not None:
            self.coverage_type = m.get('CoverageType')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('IpType') is not None:
            self.ip_type = m.get('IpType')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeInstanceListResponseBody(TeaModel):
    def __init__(
        self,
        instance_list: List[DescribeInstanceListResponseBodyInstanceList] = None,
        request_id: str = None,
        total: int = None,
    ):
        # The details about the Anti-DDoS Origin instance.
        self.instance_list = instance_list
        # The ID of the request.
        self.request_id = request_id
        # The total number of Anti-DDoS Origin instances.
        self.total = total

    def validate(self):
        if self.instance_list:
            for k in self.instance_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InstanceList'] = []
        if self.instance_list is not None:
            for k in self.instance_list:
                result['InstanceList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_list = []
        if m.get('InstanceList') is not None:
            for k in m.get('InstanceList'):
                temp_model = DescribeInstanceListResponseBodyInstanceList()
                self.instance_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribeInstanceListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeInstanceListResponseBody = None,
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
            temp_model = DescribeInstanceListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceSpecsRequest(TeaModel):
    def __init__(
        self,
        instance_id_list: str = None,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        # The ID of the Anti-DDoS Origin Enterprise instance. This parameter value is a string consisting of JSON arrays. Each element in a JSON array indicates an instance ID. If you want to query more than one instance, separate instance IDs with commas (,).
        # 
        # >  You can call the [DescribeInstanceList](https://help.aliyun.com/document_detail/118698.html) operation to query the IDs of all Anti-DDoS Origin Enterprise instances in a specific region.
        # 
        # This parameter is required.
        self.instance_id_list = instance_id_list
        # The region ID of the Anti-DDoS Origin Enterprise instance. Default value: **cn-hangzhou**, which indicates the China (Hangzhou) region.
        # 
        # >  If your instance does not reside in the China (Hangzhou) region, you must specify this parameter to the region ID of your instance. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/118703.html) operation to query the regions of cloud assets that are supported by an Anti-DDoS Origin instance.
        self.region_id = region_id
        # The ID of the resource group to which the Anti-DDoS Origin Enterprise instance belongs in Resource Management. This parameter is empty by default, which indicates that the Anti-DDoS Origin Enterprise instance belongs to the default resource group.
        # 
        # For more information about resource groups, see [Create a resource group](https://help.aliyun.com/document_detail/94485.html).
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id_list is not None:
            result['InstanceIdList'] = self.instance_id_list
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIdList') is not None:
            self.instance_id_list = m.get('InstanceIdList')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeInstanceSpecsResponseBodyInstanceSpecsPackConfig(TeaModel):
    def __init__(
        self,
        bandwidth: int = None,
        bind_ip_count: int = None,
        ip_advance_thre: int = None,
        ip_basic_thre: int = None,
        ip_spec: int = None,
        normal_bandwidth: int = None,
        pack_adv_thre: int = None,
        pack_basic_thre: int = None,
    ):
        # The bandwidth of the package configuration.
        self.bandwidth = bandwidth
        # The number of IP addresses that are protected by the Anti-DDoS Origin Enterprise instance.
        self.bind_ip_count = bind_ip_count
        # The burstable bandwidth of each protected IP address. Unit: Gbit/s.
        self.ip_advance_thre = ip_advance_thre
        # The basic bandwidth of each protected IP address. Unit: Gbit/s.
        self.ip_basic_thre = ip_basic_thre
        # The number of IP addresses that can be protected by the Anti-DDoS Origin Enterprise instance.
        self.ip_spec = ip_spec
        # The normal clean bandwidth. Unit: Mbit/s.
        self.normal_bandwidth = normal_bandwidth
        # The burstable protection bandwidth of the Anti-DDoS Origin Enterprise instance. Unit: Gbit/s.
        self.pack_adv_thre = pack_adv_thre
        # The basic protection bandwidth of the Anti-DDoS Origin Enterprise instance. Unit: Gbit/s.
        self.pack_basic_thre = pack_basic_thre

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.bind_ip_count is not None:
            result['BindIpCount'] = self.bind_ip_count
        if self.ip_advance_thre is not None:
            result['IpAdvanceThre'] = self.ip_advance_thre
        if self.ip_basic_thre is not None:
            result['IpBasicThre'] = self.ip_basic_thre
        if self.ip_spec is not None:
            result['IpSpec'] = self.ip_spec
        if self.normal_bandwidth is not None:
            result['NormalBandwidth'] = self.normal_bandwidth
        if self.pack_adv_thre is not None:
            result['PackAdvThre'] = self.pack_adv_thre
        if self.pack_basic_thre is not None:
            result['PackBasicThre'] = self.pack_basic_thre
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('BindIpCount') is not None:
            self.bind_ip_count = m.get('BindIpCount')
        if m.get('IpAdvanceThre') is not None:
            self.ip_advance_thre = m.get('IpAdvanceThre')
        if m.get('IpBasicThre') is not None:
            self.ip_basic_thre = m.get('IpBasicThre')
        if m.get('IpSpec') is not None:
            self.ip_spec = m.get('IpSpec')
        if m.get('NormalBandwidth') is not None:
            self.normal_bandwidth = m.get('NormalBandwidth')
        if m.get('PackAdvThre') is not None:
            self.pack_adv_thre = m.get('PackAdvThre')
        if m.get('PackBasicThre') is not None:
            self.pack_basic_thre = m.get('PackBasicThre')
        return self


class DescribeInstanceSpecsResponseBodyInstanceSpecs(TeaModel):
    def __init__(
        self,
        available_defense_times: int = None,
        available_delete_blackhole_count: str = None,
        defense_times_percent: int = None,
        instance_id: str = None,
        is_full_defense_mode: int = None,
        pack_config: DescribeInstanceSpecsResponseBodyInstanceSpecsPackConfig = None,
        region: str = None,
        total_defense_times: int = None,
    ):
        # The number of times that the unlimited protection feature can be enabled.
        self.available_defense_times = available_defense_times
        # The number of times that blackhole filtering can be deactivated.
        self.available_delete_blackhole_count = available_delete_blackhole_count
        self.defense_times_percent = defense_times_percent
        # The ID of the Anti-DDoS Origin Enterprise instance.
        self.instance_id = instance_id
        # Indicates whether the unlimited protection feature is enabled. Valid values:
        # 
        # *   **0**: The unlimited protection feature is disabled.
        # *   **1**: The unlimited protection feature is enabled.
        self.is_full_defense_mode = is_full_defense_mode
        # The configurations of the Anti-DDoS Origin Enterprise instance, including the number of protected IP addresses and protection bandwidth.
        self.pack_config = pack_config
        # The region ID of the Anti-DDoS Origin Enterprise instance.
        # 
        # >  You can call the [DescribeRegions](https://help.aliyun.com/document_detail/118703.html) operation to query the name of the region.
        self.region = region
        # The number of times that the unlimited protection feature can be enabled.
        self.total_defense_times = total_defense_times

    def validate(self):
        if self.pack_config:
            self.pack_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.available_defense_times is not None:
            result['AvailableDefenseTimes'] = self.available_defense_times
        if self.available_delete_blackhole_count is not None:
            result['AvailableDeleteBlackholeCount'] = self.available_delete_blackhole_count
        if self.defense_times_percent is not None:
            result['DefenseTimesPercent'] = self.defense_times_percent
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.is_full_defense_mode is not None:
            result['IsFullDefenseMode'] = self.is_full_defense_mode
        if self.pack_config is not None:
            result['PackConfig'] = self.pack_config.to_map()
        if self.region is not None:
            result['Region'] = self.region
        if self.total_defense_times is not None:
            result['TotalDefenseTimes'] = self.total_defense_times
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableDefenseTimes') is not None:
            self.available_defense_times = m.get('AvailableDefenseTimes')
        if m.get('AvailableDeleteBlackholeCount') is not None:
            self.available_delete_blackhole_count = m.get('AvailableDeleteBlackholeCount')
        if m.get('DefenseTimesPercent') is not None:
            self.defense_times_percent = m.get('DefenseTimesPercent')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IsFullDefenseMode') is not None:
            self.is_full_defense_mode = m.get('IsFullDefenseMode')
        if m.get('PackConfig') is not None:
            temp_model = DescribeInstanceSpecsResponseBodyInstanceSpecsPackConfig()
            self.pack_config = temp_model.from_map(m['PackConfig'])
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('TotalDefenseTimes') is not None:
            self.total_defense_times = m.get('TotalDefenseTimes')
        return self


class DescribeInstanceSpecsResponseBody(TeaModel):
    def __init__(
        self,
        instance_specs: List[DescribeInstanceSpecsResponseBodyInstanceSpecs] = None,
        request_id: str = None,
    ):
        # The specifications of the Anti-DDoS Origin Enterprise instance, including whether the unlimited protection feature is enabled, and the numbers of times that the unlimited protection feature can be enabled and has been enabled.
        self.instance_specs = instance_specs
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.instance_specs:
            for k in self.instance_specs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InstanceSpecs'] = []
        if self.instance_specs is not None:
            for k in self.instance_specs:
                result['InstanceSpecs'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_specs = []
        if m.get('InstanceSpecs') is not None:
            for k in m.get('InstanceSpecs'):
                temp_model = DescribeInstanceSpecsResponseBodyInstanceSpecs()
                self.instance_specs.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeInstanceSpecsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeInstanceSpecsResponseBody = None,
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
            temp_model = DescribeInstanceSpecsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeOnDemandDdosEventRequest(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        instance_id: str = None,
        ip: str = None,
        page_no: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        start_time: int = None,
    ):
        # The timestamp that specifies the end of the time range to query. Unit: seconds. The timestamp follows the UNIX time format. It is the number of seconds that have elapsed since 00:00:00 Thursday, 1 January 1970.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The ID of the on-demand instance to query.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The IP address of the protection target.
        self.ip = ip
        # The number of the page to return. Default value: **1**.
        # 
        # This parameter is required.
        self.page_no = page_no
        # The number of entries to return on each page. The maximum value is **50**. The default value is **10**.
        # 
        # This parameter is required.
        self.page_size = page_size
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The timestamp that specifies the beginning of the time range to query. Unit: seconds. The timestamp follows the UNIX time format. It is the number of seconds that have elapsed since 00:00:00 Thursday, 1 January 1970.
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
            result['EndTime'] = self.end_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeOnDemandDdosEventResponseBodyEvents(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        ip: str = None,
        mbps: int = None,
        pps: int = None,
        start_time: int = None,
        status: str = None,
    ):
        # The timestamp that indicates the end time of the attack. Unit: seconds. The timestamp follows the UNIX time format. It is the number of seconds that have elapsed since 00:00:00 Thursday, 1 January 1970.
        self.end_time = end_time
        # The IP address of the protection target that encounters the DDoS attack.
        self.ip = ip
        # The throughput of the DDoS attack. Unit: Mbit/s.
        self.mbps = mbps
        # The packet forwarding rate of the DDoS attack. Unit: packets per second (PPS).
        self.pps = pps
        # The timestamp that indicates the start time of the attack. Unit: seconds. The timestamp follows the UNIX time format. It is the number of seconds that have elapsed since 00:00:00 Thursday, 1 January 1970.
        self.start_time = start_time
        # The status of the event. Valid values:
        # 
        # *   **hole_begin **: indicates that the event is in the blackhole state.
        # *   **hole_end **: indicates that blackhole ends.
        # *   **defense_begin **: indicates that the event is in the cleaning state.
        # *   **defense_end **: indicates that cleaning ends.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.mbps is not None:
            result['Mbps'] = self.mbps
        if self.pps is not None:
            result['Pps'] = self.pps
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Mbps') is not None:
            self.mbps = m.get('Mbps')
        if m.get('Pps') is not None:
            self.pps = m.get('Pps')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeOnDemandDdosEventResponseBody(TeaModel):
    def __init__(
        self,
        events: List[DescribeOnDemandDdosEventResponseBodyEvents] = None,
        request_id: str = None,
        total: int = None,
    ):
        # The list of DDoS events and the details of each event.
        self.events = events
        # The ID of the request.
        self.request_id = request_id
        # The total number of DDoS events.
        self.total = total

    def validate(self):
        if self.events:
            for k in self.events:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Events'] = []
        if self.events is not None:
            for k in self.events:
                result['Events'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.events = []
        if m.get('Events') is not None:
            for k in m.get('Events'):
                temp_model = DescribeOnDemandDdosEventResponseBodyEvents()
                self.events.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribeOnDemandDdosEventResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeOnDemandDdosEventResponseBody = None,
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
            temp_model = DescribeOnDemandDdosEventResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeOnDemandInstanceStatusRequest(TeaModel):
    def __init__(
        self,
        instance_id_list: List[str] = None,
        region_id: str = None,
    ):
        # The IDs of on-demand instances.
        # 
        # >  You can call the [DescribeOnDemandInstance](https://help.aliyun.com/document_detail/152120.html) operation to query the IDs of all on-demand instances.
        # 
        # This parameter is required.
        self.instance_id_list = instance_id_list
        # The region ID of the on-demand instance.
        # 
        # >  You can call the [DescribeRegions](https://help.aliyun.com/document_detail/118703.html) operation to query all regions supported by Anti-DDoS Origin.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id_list is not None:
            result['InstanceIdList'] = self.instance_id_list
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIdList') is not None:
            self.instance_id_list = m.get('InstanceIdList')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeOnDemandInstanceStatusResponseBodyInstances(TeaModel):
    def __init__(
        self,
        declared: str = None,
        desc: str = None,
        instance_id: str = None,
        mode: str = None,
        net: str = None,
        registed_as: str = None,
        user_id: str = None,
    ):
        # The details of route advertisement for data centers outside the Chinese mainland. This parameter is a JSON string. The following fields are included in the value:
        # 
        # *   **region**: The code of the data center outside the Chinese mainland. The value is of the STRING type. For more information, see **Codes of data centers outside the Chinese mainland**.
        # *   **declared**: indicates whether the data center advertised the route. The value is of the STRING type. Valid values: **0** and **1**. The value of 0 indicates that the data center did not advertise the route. The value of 1 indicates that the data center advertised the route.
        self.declared = declared
        # The description of the on-demand instance.
        # 
        # >  The value of this parameter is returned only when the information about multiple on-demand instances is returned. The value of this parameter is not returned because the information about only one on-demand instance is returned.
        self.desc = desc
        # The ID of the on-demand instance.
        # 
        # >  The value of this parameter is returned only when the information about multiple on-demand instances is returned. The value of this parameter is not returned because the information about only one on-demand instance is returned.
        self.instance_id = instance_id
        # The mode used to start the on-demand instance. Valid values:
        # 
        # *   **manual**: The instance is manually started.
        # *   **netflow-auto**: The instance is automatically started by using NetFlow that monitors network traffic.
        self.mode = mode
        # The CIDR block of the on-demand instance.
        self.net = net
        # The number of the autonomous system (AS). Set the value to **0**, which indicates that AS is disabled.
        self.registed_as = registed_as
        # The ID of the Alibaba Cloud account.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.declared is not None:
            result['Declared'] = self.declared
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.net is not None:
            result['Net'] = self.net
        if self.registed_as is not None:
            result['RegistedAs'] = self.registed_as
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Declared') is not None:
            self.declared = m.get('Declared')
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('Net') is not None:
            self.net = m.get('Net')
        if m.get('RegistedAs') is not None:
            self.registed_as = m.get('RegistedAs')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DescribeOnDemandInstanceStatusResponseBody(TeaModel):
    def __init__(
        self,
        instances: List[DescribeOnDemandInstanceStatusResponseBodyInstances] = None,
        request_id: str = None,
    ):
        # The details of the on-demand instance.
        self.instances = instances
        # The ID of the request.
        self.request_id = request_id

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
        result['Instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['Instances'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instances = []
        if m.get('Instances') is not None:
            for k in m.get('Instances'):
                temp_model = DescribeOnDemandInstanceStatusResponseBodyInstances()
                self.instances.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeOnDemandInstanceStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeOnDemandInstanceStatusResponseBody = None,
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
            temp_model = DescribeOnDemandInstanceStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeOpEntitiesRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        end_time: int = None,
        instance_id: str = None,
        order_by: str = None,
        order_dir: str = None,
        page_size: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        start_time: int = None,
    ):
        # The operation that you want to perform. Set the value to **DescribeOpEntities**.
        # 
        # This parameter is required.
        self.current_page = current_page
        # The details of the operation log.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The page number of the returned page.
        self.instance_id = instance_id
        # The sort order of operation logs. Valid values:
        # 
        # *   **ASC**: the ascending order.
        # *   **DESC**: the descending order.
        self.order_by = order_by
        # The ID of the region where the Anti-DDoS Origin instance resides.
        # 
        # >  You can call the [DescribeRegions](https://help.aliyun.com/document_detail/118703.html) operation to query the most recent region list.
        self.order_dir = order_dir
        # The type of the operation object. The value is fixed as **1**, which indicates Anti-DDoS Origin instances.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The ID of the Alibaba Cloud account that performs the operation.
        # 
        # >  If the value is **system**, the operation is performed by Anti-DDoS Origin.
        self.region_id = region_id
        # The details about the operation. The value is a string that consists of a JSON struct. The JSON struct contains the following fields:
        # 
        # *   **entity**: the operation object. Data type: object. The fields that are included in the value of the **entity** parameter vary based on the value of the **OpAction** parameter. Take note of the following items:
        # 
        #     *   If the value of the **OpAction** parameter is **3**, the value of the **entity** parameter consists of the following field:
        # 
        #         *   **ips**: the public IP addresses that are protected by the Anti-DDoS Origin instance. Data type: array
        # 
        #     *   If the value of the **OpAction** parameter is **4**, the value of the **entity** parameter consists of the following field:
        # 
        #         *   **ips**: the public IP addresses that are no longer protected by the Anti-DDoS Origin instance. Data type: array.
        # 
        #     *   If the value of the **OpAction** parameter is **5**, the value of the **entity** parameter consists of the following fields:
        # 
        #         *   **baseBandwidth**: the basic protection bandwidth. Unit: Gbit/s. Data type: integer.
        #         *   **elasticBandwidth**: the burstable protection bandwidth. Unit: Gbit/s. Data type: integer.
        #         *   **opSource**: the source of the operation. The value is fixed as **1**, indicating that the operation is performed by Anti-DDoS Origin. Data type: integer.
        # 
        #     *   If the value of the **OpAction** parameter is **6**, the value of the **entity** parameter consists of the following field:
        # 
        #         *   **ips**: the public IP addresses for which to deactivate blackhole filtering. Data type: array.
        # 
        #     *   If the value of the **OpAction** parameter is **7**, the **entity** parameter is not returned.
        # 
        #     *   If the value of the **OpAction** parameter is **8**, the value of the **entity** parameter consists of the following fields:
        # 
        #         *   **baseBandwidth**: the basic protection bandwidth. Unit: Gbit/s. Data type: integer.
        #         *   **elasticBandwidth**: the burstable protection bandwidth. Unit: Gbit/s. Data type: integer.
        self.resource_group_id = resource_group_id
        # The sorting method of operation logs. Set the value to **opdate**, which indicates sorting based on the operation time.
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
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.order_dir is not None:
            result['OrderDir'] = self.order_dir
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('OrderDir') is not None:
            self.order_dir = m.get('OrderDir')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeOpEntitiesResponseBodyOpEntities(TeaModel):
    def __init__(
        self,
        entity_object: str = None,
        entity_type: int = None,
        gmt_create: int = None,
        op_account: str = None,
        op_action: int = None,
        op_desc: str = None,
    ):
        # Queries the operation logs of an Anti-DDoS Origin instance.
        self.entity_object = entity_object
        # All Alibaba Cloud API operations must include common request parameters. For more information about common request parameters, see [Common parameters](https://help.aliyun.com/document_detail/118841.html).
        # 
        # For more information about sample requests, see the **"Examples"** section of this topic.
        self.entity_type = entity_type
        # WB01342967
        self.gmt_create = gmt_create
        self.op_account = op_account
        # DescribeOpEntities
        self.op_action = op_action
        self.op_desc = op_desc

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_object is not None:
            result['EntityObject'] = self.entity_object
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.op_account is not None:
            result['OpAccount'] = self.op_account
        if self.op_action is not None:
            result['OpAction'] = self.op_action
        if self.op_desc is not None:
            result['OpDesc'] = self.op_desc
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityObject') is not None:
            self.entity_object = m.get('EntityObject')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('OpAccount') is not None:
            self.op_account = m.get('OpAccount')
        if m.get('OpAction') is not None:
            self.op_action = m.get('OpAction')
        if m.get('OpDesc') is not None:
            self.op_desc = m.get('OpDesc')
        return self


class DescribeOpEntitiesResponseBody(TeaModel):
    def __init__(
        self,
        op_entities: List[DescribeOpEntitiesResponseBodyOpEntities] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The ID of the request.
        self.op_entities = op_entities
        # The end time. Operation logs that were generated before this time are queried.**** This value is a UNIX timestamp. Unit: milliseconds.
        self.request_id = request_id
        # The time when the log was generated. This value is a UNIX timestamp. Unit: milliseconds.
        self.total_count = total_count

    def validate(self):
        if self.op_entities:
            for k in self.op_entities:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['OpEntities'] = []
        if self.op_entities is not None:
            for k in self.op_entities:
                result['OpEntities'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.op_entities = []
        if m.get('OpEntities') is not None:
            for k in m.get('OpEntities'):
                temp_model = DescribeOpEntitiesResponseBodyOpEntities()
                self.op_entities.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeOpEntitiesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeOpEntitiesResponseBody = None,
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
            temp_model = DescribeOpEntitiesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePackIpListRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        ip: str = None,
        member_uid: str = None,
        page_no: int = None,
        page_size: int = None,
        product_name: str = None,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        # The ID of the Anti-DDoS Origin instance to query.
        # 
        # >  You can call the [DescribeInstanceList](https://help.aliyun.com/document_detail/118698.html) operation to query the IDs of all Anti-DDoS Origin instances.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The protected IP address to query.
        self.ip = ip
        # The ID of the member.
        self.member_uid = member_uid
        # The number of the page to return.
        # 
        # This parameter is required.
        self.page_no = page_no
        # The number of entries to return on each page.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The type of the cloud asset to which the protected IP address to query belongs. Valid values:
        # 
        # *   **ECS**: an Elastic Compute Service (ECS) instance.
        # *   **SLB**: a Classic Load Balancer (CLB) instance, originally called a Server Load Balancer (SLB) instance.
        # *   **EIP**: an elastic IP address (EIP). An Internet-facing Application Load Balancer (ALB) instance uses an EIP. If the IP address belongs to the Internet-facing ALB instance, set this parameter to EIP.
        # *   **WAF**: a Web Application Firewall (WAF) instance.
        self.product_name = product_name
        # The ID of the region where the Anti-DDoS Origin instance resides.
        # 
        # >  You can call the [DescribeRegions](https://help.aliyun.com/document_detail/118703.html) operation to query the most recent region list.
        self.region_id = region_id
        # The ID of the resource group to which the Anti-DDoS Origin instance belongs in Resource Management.
        # 
        # If you do not specify this parameter, the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribePackIpListResponseBodyIpList(TeaModel):
    def __init__(
        self,
        ip: str = None,
        member_uid: str = None,
        nsm_expire_at: int = None,
        nsm_start_at: int = None,
        nsm_status: int = None,
        product: str = None,
        region: str = None,
        remark: str = None,
        status: str = None,
    ):
        # The IP address.
        self.ip = ip
        # The ID of the member.
        self.member_uid = member_uid
        self.nsm_expire_at = nsm_expire_at
        self.nsm_start_at = nsm_start_at
        self.nsm_status = nsm_status
        # The type of the cloud asset to which the IP address belongs. Valid values:
        # 
        # *   **ECS**: an ECS instance.
        # *   **SLB**: a CLB instance, originally called an SLB instance.
        # *   **EIP**: an EIP. If the IP address belongs to an ALB instance, the value EIP is returned.
        # *   **WAF**: a WAF instance.
        self.product = product
        # The region to which the protected IP address belongs.
        # 
        # >  If the protected IP address is in the same region as the instance, this parameter is not returned.
        self.region = region
        # The description of the cloud asset to which the IP address belongs. The asset can be an ECS instance or an SLB instance.
        # 
        # >  If no descriptions are provided for the asset, this parameter is not returned.
        self.remark = remark
        # The status of the IP address. Valid values:
        # 
        # *   **normal**: The IP address is in the normal state, which indicates that the IP address is not under attack.
        # *   **hole_begin**: Blackhole filtering is triggered for the IP address.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid
        if self.nsm_expire_at is not None:
            result['NsmExpireAt'] = self.nsm_expire_at
        if self.nsm_start_at is not None:
            result['NsmStartAt'] = self.nsm_start_at
        if self.nsm_status is not None:
            result['NsmStatus'] = self.nsm_status
        if self.product is not None:
            result['Product'] = self.product
        if self.region is not None:
            result['Region'] = self.region
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')
        if m.get('NsmExpireAt') is not None:
            self.nsm_expire_at = m.get('NsmExpireAt')
        if m.get('NsmStartAt') is not None:
            self.nsm_start_at = m.get('NsmStartAt')
        if m.get('NsmStatus') is not None:
            self.nsm_status = m.get('NsmStatus')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribePackIpListResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        ip_list: List[DescribePackIpListResponseBodyIpList] = None,
        request_id: str = None,
        success: bool = None,
        total: int = None,
    ):
        # The HTTP status code of the request.
        # 
        # For more information about status codes, see [Common parameters](https://help.aliyun.com/document_detail/118841.html).
        self.code = code
        # The IP addresses that are protected by the instance.
        self.ip_list = ip_list
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values:
        # 
        # *   **true**: The call is successful.
        # *   **false**: The call fails.
        self.success = success
        # The number of protected IP addresses.
        self.total = total

    def validate(self):
        if self.ip_list:
            for k in self.ip_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['IpList'] = []
        if self.ip_list is not None:
            for k in self.ip_list:
                result['IpList'].append(k.to_map() if k else None)
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
        self.ip_list = []
        if m.get('IpList') is not None:
            for k in m.get('IpList'):
                temp_model = DescribePackIpListResponseBodyIpList()
                self.ip_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribePackIpListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribePackIpListResponseBody = None,
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
            temp_model = DescribePackIpListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRdMemberListRequest(TeaModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        resource_directory_id: str = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        self.resource_directory_id = resource_directory_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_directory_id is not None:
            result['ResourceDirectoryId'] = self.resource_directory_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceDirectoryId') is not None:
            self.resource_directory_id = m.get('ResourceDirectoryId')
        return self


class DescribeRdMemberListResponseBodyMemberList(TeaModel):
    def __init__(
        self,
        gmt_create: int = None,
        name: str = None,
        uid: str = None,
    ):
        self.gmt_create = gmt_create
        self.name = name
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.name is not None:
            result['Name'] = self.name
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class DescribeRdMemberListResponseBody(TeaModel):
    def __init__(
        self,
        member_list: List[DescribeRdMemberListResponseBodyMemberList] = None,
        request_id: str = None,
        total: int = None,
    ):
        self.member_list = member_list
        self.request_id = request_id
        self.total = total

    def validate(self):
        if self.member_list:
            for k in self.member_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MemberList'] = []
        if self.member_list is not None:
            for k in self.member_list:
                result['MemberList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.member_list = []
        if m.get('MemberList') is not None:
            for k in m.get('MemberList'):
                temp_model = DescribeRdMemberListResponseBodyMemberList()
                self.member_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribeRdMemberListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeRdMemberListResponseBody = None,
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
            temp_model = DescribeRdMemberListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRdStatusResponseBody(TeaModel):
    def __init__(
        self,
        current_uid: str = None,
        current_uid_type: str = None,
        enabled: bool = None,
        local_enable: bool = None,
        master_uid: str = None,
        remote_enable: bool = None,
        request_id: str = None,
        root_uid: str = None,
        service_principal_enabled: bool = None,
    ):
        self.current_uid = current_uid
        self.current_uid_type = current_uid_type
        self.enabled = enabled
        self.local_enable = local_enable
        self.master_uid = master_uid
        self.remote_enable = remote_enable
        self.request_id = request_id
        self.root_uid = root_uid
        self.service_principal_enabled = service_principal_enabled

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_uid is not None:
            result['CurrentUid'] = self.current_uid
        if self.current_uid_type is not None:
            result['CurrentUidType'] = self.current_uid_type
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.local_enable is not None:
            result['LocalEnable'] = self.local_enable
        if self.master_uid is not None:
            result['MasterUid'] = self.master_uid
        if self.remote_enable is not None:
            result['RemoteEnable'] = self.remote_enable
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.root_uid is not None:
            result['RootUid'] = self.root_uid
        if self.service_principal_enabled is not None:
            result['ServicePrincipalEnabled'] = self.service_principal_enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentUid') is not None:
            self.current_uid = m.get('CurrentUid')
        if m.get('CurrentUidType') is not None:
            self.current_uid_type = m.get('CurrentUidType')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('LocalEnable') is not None:
            self.local_enable = m.get('LocalEnable')
        if m.get('MasterUid') is not None:
            self.master_uid = m.get('MasterUid')
        if m.get('RemoteEnable') is not None:
            self.remote_enable = m.get('RemoteEnable')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RootUid') is not None:
            self.root_uid = m.get('RootUid')
        if m.get('ServicePrincipalEnabled') is not None:
            self.service_principal_enabled = m.get('ServicePrincipalEnabled')
        return self


class DescribeRdStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeRdStatusResponseBody = None,
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
            temp_model = DescribeRdStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        # The region ID to query. The default value is **cn-hangzhou**, which indicates that the regions of cloud assets that are supported by an Anti-DDoS Origin instance in the China (Hangzhou) region are queried.
        # 
        # For more information about the IDs of other regions, see [Regions and zones](https://help.aliyun.com/document_detail/40654.html).
        self.region_id = region_id
        # The ID of the resource group to which the Anti-DDoS Origin instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        # 
        # For more information about resource groups, see [Create a resource group](https://help.aliyun.com/document_detail/94485.html).
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeRegionsResponseBodyRegions(TeaModel):
    def __init__(
        self,
        region_en_name: str = None,
        region_id: str = None,
        region_name: str = None,
    ):
        # The English name of the region where the cloud assets reside.
        self.region_en_name = region_en_name
        # The ID of the region.
        self.region_id = region_id
        # The name of the region where the cloud assets reside.
        self.region_name = region_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_en_name is not None:
            result['RegionEnName'] = self.region_en_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.region_name is not None:
            result['RegionName'] = self.region_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionEnName') is not None:
            self.region_en_name = m.get('RegionEnName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        regions: List[DescribeRegionsResponseBodyRegions] = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code.
        self.code = code
        # The information about regions of the cloud assets that are supported by the Anti-DDoS Origin instance. The information includes region IDs and names.
        self.regions = regions
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values:
        # 
        # *   **true**: The request is successful.
        # *   **false**: The request failed.
        self.success = success

    def validate(self):
        if self.regions:
            for k in self.regions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Regions'] = []
        if self.regions is not None:
            for k in self.regions:
                result['Regions'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.regions = []
        if m.get('Regions') is not None:
            for k in m.get('Regions'):
                temp_model = DescribeRegionsResponseBodyRegions()
                self.regions.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeRegionsResponseBody = None,
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
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTrafficRequest(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        flow_type: str = None,
        instance_id: str = None,
        interval: int = None,
        ip: str = None,
        ipnet: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        start_time: int = None,
    ):
        # The end of the time range to query. The value is a UNIX timestamp. Unit: seconds.
        # 
        # If you do not specify this parameter, the current system time is used as the end time.
        self.end_time = end_time
        # The type of the traffic statistics to query. Valid values:
        # 
        # *   **max**: the peak traffic within the specified interval
        # *   **avg**: the average traffic within the specified interval
        self.flow_type = flow_type
        # The ID of the Anti-DDoS Origin instance to query.
        # 
        # >  You can call the [DescribeInstanceList](https://help.aliyun.com/document_detail/118698.html) operation to query the IDs of all Anti-DDoS Origin instances.
        # 
        # If you specify an on-demand instance, you must configure the **Interval** parameter.
        self.instance_id = instance_id
        # The interval at which the traffic statistics are calculated. Unit: seconds. Default value: **5**.
        self.interval = interval
        # The public IP address of the asset to query. If you do not specify this parameter, the traffic statistics of all public IP addresses that are protected by the Anti-DDoS Origin instance are queried.
        # 
        # >  The public IP address must be a protected object of the Anti-DDoS Origin instance. You can call the [DescribePackIpList](https://help.aliyun.com/document_detail/118701.html) operation to query all protected objects of the Anti-DDoS Origin instance.
        self.ip = ip
        # The Classless Inter-Domain Routing (CIDR) block of the on-demand instance that you want to query.
        self.ipnet = ipnet
        # The ID of the region where the Anti-DDoS Origin instance resides.
        # 
        # >  You can call the [DescribeRegions](https://help.aliyun.com/document_detail/118703.html) operation to query the most recent region list.
        self.region_id = region_id
        # The ID of the resource group to which the Anti-DDoS Origin instance belongs in Resource Management.
        # 
        # If you do not specify this parameter, the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id
        # The beginning of the time range to query. The value is a UNIX timestamp. Unit: seconds.
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
            result['EndTime'] = self.end_time
        if self.flow_type is not None:
            result['FlowType'] = self.flow_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.ipnet is not None:
            result['Ipnet'] = self.ipnet
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('FlowType') is not None:
            self.flow_type = m.get('FlowType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Ipnet') is not None:
            self.ipnet = m.get('Ipnet')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeTrafficResponseBodyFlowList(TeaModel):
    def __init__(
        self,
        attack_bps: int = None,
        attack_pps: int = None,
        flow_type: str = None,
        kbps: int = None,
        name: str = None,
        pps: int = None,
        time: int = None,
    ):
        # The bandwidth of attack traffic. Unit: bit/s.
        # 
        # >  This parameter is returned only if attack traffic exists.
        self.attack_bps = attack_bps
        # The packet forwarding rate of attack traffic. Unit: packets per second.
        # 
        # >  This parameter is returned only if attack traffic exists.
        self.attack_pps = attack_pps
        # The type of the traffic statistics. Valid values:
        # 
        # *   **max**: the peak traffic within the specified interval
        # *   **avg**: the average traffic within the specified interval
        self.flow_type = flow_type
        # The bandwidth of the total traffic. Unit: Kbit/s.
        self.kbps = kbps
        # The ID of the traffic statistics.
        self.name = name
        # The packet forwarding rate of the total traffic. Unit: packets per second.
        self.pps = pps
        # The time when the traffic statistics are calculated. This value is a UNIX timestamp. Unit: seconds.
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attack_bps is not None:
            result['AttackBps'] = self.attack_bps
        if self.attack_pps is not None:
            result['AttackPps'] = self.attack_pps
        if self.flow_type is not None:
            result['FlowType'] = self.flow_type
        if self.kbps is not None:
            result['Kbps'] = self.kbps
        if self.name is not None:
            result['Name'] = self.name
        if self.pps is not None:
            result['Pps'] = self.pps
        if self.time is not None:
            result['Time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttackBps') is not None:
            self.attack_bps = m.get('AttackBps')
        if m.get('AttackPps') is not None:
            self.attack_pps = m.get('AttackPps')
        if m.get('FlowType') is not None:
            self.flow_type = m.get('FlowType')
        if m.get('Kbps') is not None:
            self.kbps = m.get('Kbps')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Pps') is not None:
            self.pps = m.get('Pps')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        return self


class DescribeTrafficResponseBody(TeaModel):
    def __init__(
        self,
        flow_list: List[DescribeTrafficResponseBodyFlowList] = None,
        request_id: str = None,
    ):
        # The queried traffic statistics.
        self.flow_list = flow_list
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.flow_list:
            for k in self.flow_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FlowList'] = []
        if self.flow_list is not None:
            for k in self.flow_list:
                result['FlowList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.flow_list = []
        if m.get('FlowList') is not None:
            for k in m.get('FlowList'):
                temp_model = DescribeTrafficResponseBodyFlowList()
                self.flow_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeTrafficResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeTrafficResponseBody = None,
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
            temp_model = DescribeTrafficResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachFromPolicyRequestIpPortProtocolList(TeaModel):
    def __init__(
        self,
        ip: str = None,
        port: int = None,
        protocol: str = None,
    ):
        # This parameter is required.
        self.ip = ip
        self.port = port
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.port is not None:
            result['Port'] = self.port
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        return self


class DetachFromPolicyRequest(TeaModel):
    def __init__(
        self,
        ip_port_protocol_list: List[DetachFromPolicyRequestIpPortProtocolList] = None,
        policy_type: str = None,
    ):
        # This parameter is required.
        self.ip_port_protocol_list = ip_port_protocol_list
        # This parameter is required.
        self.policy_type = policy_type

    def validate(self):
        if self.ip_port_protocol_list:
            for k in self.ip_port_protocol_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['IpPortProtocolList'] = []
        if self.ip_port_protocol_list is not None:
            for k in self.ip_port_protocol_list:
                result['IpPortProtocolList'].append(k.to_map() if k else None)
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ip_port_protocol_list = []
        if m.get('IpPortProtocolList') is not None:
            for k in m.get('IpPortProtocolList'):
                temp_model = DetachFromPolicyRequestIpPortProtocolList()
                self.ip_port_protocol_list.append(temp_model.from_map(k))
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        return self


class DetachFromPolicyShrinkRequest(TeaModel):
    def __init__(
        self,
        ip_port_protocol_list_shrink: str = None,
        policy_type: str = None,
    ):
        # This parameter is required.
        self.ip_port_protocol_list_shrink = ip_port_protocol_list_shrink
        # This parameter is required.
        self.policy_type = policy_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_port_protocol_list_shrink is not None:
            result['IpPortProtocolList'] = self.ip_port_protocol_list_shrink
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpPortProtocolList') is not None:
            self.ip_port_protocol_list_shrink = m.get('IpPortProtocolList')
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        return self


class DetachFromPolicyResponseBody(TeaModel):
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


class DetachFromPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DetachFromPolicyResponseBody = None,
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
            temp_model = DetachFromPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DettachAssetGroupToInstanceRequestAssetGroupList(TeaModel):
    def __init__(
        self,
        name: str = None,
        region: str = None,
        type: str = None,
    ):
        # The ID of the asset. If the asset is a Web Application Firewall (WAF) instance, specify the ID of the WAF instance.
        # 
        # This parameter is required.
        self.name = name
        # The region ID of the asset.
        # 
        # This parameter is required.
        self.region = region
        # The type of the asset. Valid values:
        # 
        # *   **waf**: WAF instance
        # *   **ga**: Global Accelerator (GA) instance
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.region is not None:
            result['Region'] = self.region
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DettachAssetGroupToInstanceRequest(TeaModel):
    def __init__(
        self,
        asset_group_list: List[DettachAssetGroupToInstanceRequestAssetGroupList] = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        # The information about the asset that you want to dissociate.
        # 
        # This parameter is required.
        self.asset_group_list = asset_group_list
        # The ID of the instance.
        # 
        # >  You can call the [DescribeInstanceList](https://help.aliyun.com/document_detail/118698.html) operation to query the IDs of all Anti-DDoS Origin instances of paid editions.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the region in which the instance resides.
        # 
        # >  You can call the [DescribeRegions](https://help.aliyun.com/document_detail/118703.html) operation to query the most recent region list.
        self.region_id = region_id

    def validate(self):
        if self.asset_group_list:
            for k in self.asset_group_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AssetGroupList'] = []
        if self.asset_group_list is not None:
            for k in self.asset_group_list:
                result['AssetGroupList'].append(k.to_map() if k else None)
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.asset_group_list = []
        if m.get('AssetGroupList') is not None:
            for k in m.get('AssetGroupList'):
                temp_model = DettachAssetGroupToInstanceRequestAssetGroupList()
                self.asset_group_list.append(temp_model.from_map(k))
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DettachAssetGroupToInstanceShrinkRequest(TeaModel):
    def __init__(
        self,
        asset_group_list_shrink: str = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        # The information about the asset that you want to dissociate.
        # 
        # This parameter is required.
        self.asset_group_list_shrink = asset_group_list_shrink
        # The ID of the instance.
        # 
        # >  You can call the [DescribeInstanceList](https://help.aliyun.com/document_detail/118698.html) operation to query the IDs of all Anti-DDoS Origin instances of paid editions.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the region in which the instance resides.
        # 
        # >  You can call the [DescribeRegions](https://help.aliyun.com/document_detail/118703.html) operation to query the most recent region list.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.asset_group_list_shrink is not None:
            result['AssetGroupList'] = self.asset_group_list_shrink
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetGroupList') is not None:
            self.asset_group_list_shrink = m.get('AssetGroupList')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DettachAssetGroupToInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class DettachAssetGroupToInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DettachAssetGroupToInstanceResponseBody = None,
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
            temp_model = DettachAssetGroupToInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSlsOpenStatusRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        # The ID of the region where the Anti-DDoS Origin instance resides.
        # 
        # For more information about the valid values of this parameter, see [Regions and zones](https://help.aliyun.com/document_detail/188196.html).
        self.region_id = region_id
        # The ID of the resource group to which the Anti-DDoS Origin instance belongs in Resource Management. This parameter is empty by default, which indicates that the Anti-DDoS Origin instance belongs to the default resource group.
        # 
        # For more information about resource groups, see [Create a resource group](https://help.aliyun.com/document_detail/94485.html).
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class GetSlsOpenStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        sls_open_status: bool = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether Log Service was activated. Valid values:
        # 
        # *   **true**: Log Service was activated.
        # *   **false**: Log Service was not activated.
        self.sls_open_status = sls_open_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sls_open_status is not None:
            result['SlsOpenStatus'] = self.sls_open_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SlsOpenStatus') is not None:
            self.sls_open_status = m.get('SlsOpenStatus')
        return self


class GetSlsOpenStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSlsOpenStatusResponseBody = None,
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
            temp_model = GetSlsOpenStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOpenedAccessLogInstancesRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        resource_group_id: str = None,
    ):
        # The number of the page to return. Pages start from page 1. Default value: **1**.
        self.page_number = page_number
        # The number of entries to return on each page. Default value: **10**.
        self.page_size = page_size
        # The ID of the resource group to which the Anti-DDoS Origin instance belongs in Resource Management. This parameter is empty by default, which indicates that the Anti-DDoS Origin instance belongs to the default resource group.
        # 
        # For more information about resource groups, see [Create a resource group](https://help.aliyun.com/document_detail/94485.html).
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class ListOpenedAccessLogInstancesResponseBodySlsConfigStatus(TeaModel):
    def __init__(
        self,
        enable: bool = None,
        instance_id: str = None,
    ):
        # Indicates whether log analysis was enabled for the Anti-DDoS Origin instance. Valid values:
        # 
        # *   **true**: Log analysis was enabled.
        # *   **false**: Log analysis was disabled.
        self.enable = enable
        # The ID of the Anti-DDoS Origin instance.
        self.instance_id = instance_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ListOpenedAccessLogInstancesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        sls_config_status: List[ListOpenedAccessLogInstancesResponseBodySlsConfigStatus] = None,
        total_count: int = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The configuration of log analysis for the Anti-DDoS Origin instance.
        self.sls_config_status = sls_config_status
        # The number of the Anti-DDoS Origin instances for which log analysis was enabled.
        self.total_count = total_count

    def validate(self):
        if self.sls_config_status:
            for k in self.sls_config_status:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SlsConfigStatus'] = []
        if self.sls_config_status is not None:
            for k in self.sls_config_status:
                result['SlsConfigStatus'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.sls_config_status = []
        if m.get('SlsConfigStatus') is not None:
            for k in m.get('SlsConfigStatus'):
                temp_model = ListOpenedAccessLogInstancesResponseBodySlsConfigStatus()
                self.sls_config_status.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListOpenedAccessLogInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListOpenedAccessLogInstancesResponseBody = None,
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
            temp_model = ListOpenedAccessLogInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPolicyRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        page_no: int = None,
        page_size: int = None,
        type: str = None,
    ):
        self.name = name
        self.page_no = page_no
        self.page_size = page_size
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListPolicyResponseBodyPolicyListContentFingerPrintRuleList(TeaModel):
    def __init__(
        self,
        dst_port_end: int = None,
        dst_port_start: int = None,
        id: str = None,
        match_action: str = None,
        max_pkt_len: int = None,
        min_pkt_len: int = None,
        offset: int = None,
        payload_bytes: str = None,
        protocol: str = None,
        rate_value: int = None,
        seq_no: int = None,
        src_port_end: int = None,
        src_port_start: int = None,
    ):
        self.dst_port_end = dst_port_end
        self.dst_port_start = dst_port_start
        self.id = id
        self.match_action = match_action
        self.max_pkt_len = max_pkt_len
        self.min_pkt_len = min_pkt_len
        self.offset = offset
        self.payload_bytes = payload_bytes
        self.protocol = protocol
        self.rate_value = rate_value
        self.seq_no = seq_no
        self.src_port_end = src_port_end
        self.src_port_start = src_port_start

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dst_port_end is not None:
            result['DstPortEnd'] = self.dst_port_end
        if self.dst_port_start is not None:
            result['DstPortStart'] = self.dst_port_start
        if self.id is not None:
            result['Id'] = self.id
        if self.match_action is not None:
            result['MatchAction'] = self.match_action
        if self.max_pkt_len is not None:
            result['MaxPktLen'] = self.max_pkt_len
        if self.min_pkt_len is not None:
            result['MinPktLen'] = self.min_pkt_len
        if self.offset is not None:
            result['Offset'] = self.offset
        if self.payload_bytes is not None:
            result['PayloadBytes'] = self.payload_bytes
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.rate_value is not None:
            result['RateValue'] = self.rate_value
        if self.seq_no is not None:
            result['SeqNo'] = self.seq_no
        if self.src_port_end is not None:
            result['SrcPortEnd'] = self.src_port_end
        if self.src_port_start is not None:
            result['SrcPortStart'] = self.src_port_start
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DstPortEnd') is not None:
            self.dst_port_end = m.get('DstPortEnd')
        if m.get('DstPortStart') is not None:
            self.dst_port_start = m.get('DstPortStart')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('MatchAction') is not None:
            self.match_action = m.get('MatchAction')
        if m.get('MaxPktLen') is not None:
            self.max_pkt_len = m.get('MaxPktLen')
        if m.get('MinPktLen') is not None:
            self.min_pkt_len = m.get('MinPktLen')
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')
        if m.get('PayloadBytes') is not None:
            self.payload_bytes = m.get('PayloadBytes')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('RateValue') is not None:
            self.rate_value = m.get('RateValue')
        if m.get('SeqNo') is not None:
            self.seq_no = m.get('SeqNo')
        if m.get('SrcPortEnd') is not None:
            self.src_port_end = m.get('SrcPortEnd')
        if m.get('SrcPortStart') is not None:
            self.src_port_start = m.get('SrcPortStart')
        return self


class ListPolicyResponseBodyPolicyListContentL4RuleListConditionList(TeaModel):
    def __init__(
        self,
        arg: str = None,
        depth: int = None,
        position: int = None,
    ):
        self.arg = arg
        self.depth = depth
        self.position = position

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arg is not None:
            result['Arg'] = self.arg
        if self.depth is not None:
            result['Depth'] = self.depth
        if self.position is not None:
            result['Position'] = self.position
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arg') is not None:
            self.arg = m.get('Arg')
        if m.get('Depth') is not None:
            self.depth = m.get('Depth')
        if m.get('Position') is not None:
            self.position = m.get('Position')
        return self


class ListPolicyResponseBodyPolicyListContentL4RuleList(TeaModel):
    def __init__(
        self,
        action: str = None,
        condition_list: List[ListPolicyResponseBodyPolicyListContentL4RuleListConditionList] = None,
        limited: int = None,
        match: str = None,
        method: str = None,
        name: str = None,
        priority: int = None,
    ):
        self.action = action
        self.condition_list = condition_list
        self.limited = limited
        self.match = match
        self.method = method
        self.name = name
        self.priority = priority

    def validate(self):
        if self.condition_list:
            for k in self.condition_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        result['ConditionList'] = []
        if self.condition_list is not None:
            for k in self.condition_list:
                result['ConditionList'].append(k.to_map() if k else None)
        if self.limited is not None:
            result['Limited'] = self.limited
        if self.match is not None:
            result['Match'] = self.match
        if self.method is not None:
            result['Method'] = self.method
        if self.name is not None:
            result['Name'] = self.name
        if self.priority is not None:
            result['Priority'] = self.priority
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        self.condition_list = []
        if m.get('ConditionList') is not None:
            for k in m.get('ConditionList'):
                temp_model = ListPolicyResponseBodyPolicyListContentL4RuleListConditionList()
                self.condition_list.append(temp_model.from_map(k))
        if m.get('Limited') is not None:
            self.limited = m.get('Limited')
        if m.get('Match') is not None:
            self.match = m.get('Match')
        if m.get('Method') is not None:
            self.method = m.get('Method')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        return self


class ListPolicyResponseBodyPolicyListContentPortRuleList(TeaModel):
    def __init__(
        self,
        dst_port_end: int = None,
        dst_port_start: int = None,
        id: str = None,
        match_action: str = None,
        protocol: str = None,
        seq_no: int = None,
        src_port_end: int = None,
        src_port_start: int = None,
    ):
        self.dst_port_end = dst_port_end
        self.dst_port_start = dst_port_start
        self.id = id
        self.match_action = match_action
        self.protocol = protocol
        self.seq_no = seq_no
        self.src_port_end = src_port_end
        self.src_port_start = src_port_start

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dst_port_end is not None:
            result['DstPortEnd'] = self.dst_port_end
        if self.dst_port_start is not None:
            result['DstPortStart'] = self.dst_port_start
        if self.id is not None:
            result['Id'] = self.id
        if self.match_action is not None:
            result['MatchAction'] = self.match_action
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.seq_no is not None:
            result['SeqNo'] = self.seq_no
        if self.src_port_end is not None:
            result['SrcPortEnd'] = self.src_port_end
        if self.src_port_start is not None:
            result['SrcPortStart'] = self.src_port_start
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DstPortEnd') is not None:
            self.dst_port_end = m.get('DstPortEnd')
        if m.get('DstPortStart') is not None:
            self.dst_port_start = m.get('DstPortStart')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('MatchAction') is not None:
            self.match_action = m.get('MatchAction')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('SeqNo') is not None:
            self.seq_no = m.get('SeqNo')
        if m.get('SrcPortEnd') is not None:
            self.src_port_end = m.get('SrcPortEnd')
        if m.get('SrcPortStart') is not None:
            self.src_port_start = m.get('SrcPortStart')
        return self


class ListPolicyResponseBodyPolicyListContentSourceBlockList(TeaModel):
    def __init__(
        self,
        block_expire_seconds: int = None,
        every_seconds: int = None,
        exceed_limit_times: int = None,
        type: int = None,
    ):
        self.block_expire_seconds = block_expire_seconds
        self.every_seconds = every_seconds
        self.exceed_limit_times = exceed_limit_times
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.block_expire_seconds is not None:
            result['BlockExpireSeconds'] = self.block_expire_seconds
        if self.every_seconds is not None:
            result['EverySeconds'] = self.every_seconds
        if self.exceed_limit_times is not None:
            result['ExceedLimitTimes'] = self.exceed_limit_times
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlockExpireSeconds') is not None:
            self.block_expire_seconds = m.get('BlockExpireSeconds')
        if m.get('EverySeconds') is not None:
            self.every_seconds = m.get('EverySeconds')
        if m.get('ExceedLimitTimes') is not None:
            self.exceed_limit_times = m.get('ExceedLimitTimes')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListPolicyResponseBodyPolicyListContentSourceLimit(TeaModel):
    def __init__(
        self,
        bps: int = None,
        pps: int = None,
        syn_bps: int = None,
        syn_pps: int = None,
    ):
        self.bps = bps
        self.pps = pps
        self.syn_bps = syn_bps
        self.syn_pps = syn_pps

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bps is not None:
            result['Bps'] = self.bps
        if self.pps is not None:
            result['Pps'] = self.pps
        if self.syn_bps is not None:
            result['SynBps'] = self.syn_bps
        if self.syn_pps is not None:
            result['SynPps'] = self.syn_pps
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bps') is not None:
            self.bps = m.get('Bps')
        if m.get('Pps') is not None:
            self.pps = m.get('Pps')
        if m.get('SynBps') is not None:
            self.syn_bps = m.get('SynBps')
        if m.get('SynPps') is not None:
            self.syn_pps = m.get('SynPps')
        return self


class ListPolicyResponseBodyPolicyListContent(TeaModel):
    def __init__(
        self,
        black_ip_list_expire_at: int = None,
        enable_drop_icmp: bool = None,
        enable_intelligence: bool = None,
        enable_l4defense: bool = None,
        finger_print_rule_list: List[ListPolicyResponseBodyPolicyListContentFingerPrintRuleList] = None,
        intelligence_level: str = None,
        l_4rule_list: List[ListPolicyResponseBodyPolicyListContentL4RuleList] = None,
        port_rule_list: List[ListPolicyResponseBodyPolicyListContentPortRuleList] = None,
        reflect_block_udp_port_list: List[int] = None,
        region_block_country_list: List[int] = None,
        region_block_province_list: List[int] = None,
        source_block_list: List[ListPolicyResponseBodyPolicyListContentSourceBlockList] = None,
        source_limit: ListPolicyResponseBodyPolicyListContentSourceLimit = None,
        whiten_gfbr_nets: bool = None,
    ):
        self.black_ip_list_expire_at = black_ip_list_expire_at
        self.enable_drop_icmp = enable_drop_icmp
        self.enable_intelligence = enable_intelligence
        self.enable_l4defense = enable_l4defense
        self.finger_print_rule_list = finger_print_rule_list
        self.intelligence_level = intelligence_level
        self.l_4rule_list = l_4rule_list
        self.port_rule_list = port_rule_list
        self.reflect_block_udp_port_list = reflect_block_udp_port_list
        self.region_block_country_list = region_block_country_list
        self.region_block_province_list = region_block_province_list
        self.source_block_list = source_block_list
        self.source_limit = source_limit
        self.whiten_gfbr_nets = whiten_gfbr_nets

    def validate(self):
        if self.finger_print_rule_list:
            for k in self.finger_print_rule_list:
                if k:
                    k.validate()
        if self.l_4rule_list:
            for k in self.l_4rule_list:
                if k:
                    k.validate()
        if self.port_rule_list:
            for k in self.port_rule_list:
                if k:
                    k.validate()
        if self.source_block_list:
            for k in self.source_block_list:
                if k:
                    k.validate()
        if self.source_limit:
            self.source_limit.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.black_ip_list_expire_at is not None:
            result['BlackIpListExpireAt'] = self.black_ip_list_expire_at
        if self.enable_drop_icmp is not None:
            result['EnableDropIcmp'] = self.enable_drop_icmp
        if self.enable_intelligence is not None:
            result['EnableIntelligence'] = self.enable_intelligence
        if self.enable_l4defense is not None:
            result['EnableL4Defense'] = self.enable_l4defense
        result['FingerPrintRuleList'] = []
        if self.finger_print_rule_list is not None:
            for k in self.finger_print_rule_list:
                result['FingerPrintRuleList'].append(k.to_map() if k else None)
        if self.intelligence_level is not None:
            result['IntelligenceLevel'] = self.intelligence_level
        result['L4RuleList'] = []
        if self.l_4rule_list is not None:
            for k in self.l_4rule_list:
                result['L4RuleList'].append(k.to_map() if k else None)
        result['PortRuleList'] = []
        if self.port_rule_list is not None:
            for k in self.port_rule_list:
                result['PortRuleList'].append(k.to_map() if k else None)
        if self.reflect_block_udp_port_list is not None:
            result['ReflectBlockUdpPortList'] = self.reflect_block_udp_port_list
        if self.region_block_country_list is not None:
            result['RegionBlockCountryList'] = self.region_block_country_list
        if self.region_block_province_list is not None:
            result['RegionBlockProvinceList'] = self.region_block_province_list
        result['SourceBlockList'] = []
        if self.source_block_list is not None:
            for k in self.source_block_list:
                result['SourceBlockList'].append(k.to_map() if k else None)
        if self.source_limit is not None:
            result['SourceLimit'] = self.source_limit.to_map()
        if self.whiten_gfbr_nets is not None:
            result['WhitenGfbrNets'] = self.whiten_gfbr_nets
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlackIpListExpireAt') is not None:
            self.black_ip_list_expire_at = m.get('BlackIpListExpireAt')
        if m.get('EnableDropIcmp') is not None:
            self.enable_drop_icmp = m.get('EnableDropIcmp')
        if m.get('EnableIntelligence') is not None:
            self.enable_intelligence = m.get('EnableIntelligence')
        if m.get('EnableL4Defense') is not None:
            self.enable_l4defense = m.get('EnableL4Defense')
        self.finger_print_rule_list = []
        if m.get('FingerPrintRuleList') is not None:
            for k in m.get('FingerPrintRuleList'):
                temp_model = ListPolicyResponseBodyPolicyListContentFingerPrintRuleList()
                self.finger_print_rule_list.append(temp_model.from_map(k))
        if m.get('IntelligenceLevel') is not None:
            self.intelligence_level = m.get('IntelligenceLevel')
        self.l_4rule_list = []
        if m.get('L4RuleList') is not None:
            for k in m.get('L4RuleList'):
                temp_model = ListPolicyResponseBodyPolicyListContentL4RuleList()
                self.l_4rule_list.append(temp_model.from_map(k))
        self.port_rule_list = []
        if m.get('PortRuleList') is not None:
            for k in m.get('PortRuleList'):
                temp_model = ListPolicyResponseBodyPolicyListContentPortRuleList()
                self.port_rule_list.append(temp_model.from_map(k))
        if m.get('ReflectBlockUdpPortList') is not None:
            self.reflect_block_udp_port_list = m.get('ReflectBlockUdpPortList')
        if m.get('RegionBlockCountryList') is not None:
            self.region_block_country_list = m.get('RegionBlockCountryList')
        if m.get('RegionBlockProvinceList') is not None:
            self.region_block_province_list = m.get('RegionBlockProvinceList')
        self.source_block_list = []
        if m.get('SourceBlockList') is not None:
            for k in m.get('SourceBlockList'):
                temp_model = ListPolicyResponseBodyPolicyListContentSourceBlockList()
                self.source_block_list.append(temp_model.from_map(k))
        if m.get('SourceLimit') is not None:
            temp_model = ListPolicyResponseBodyPolicyListContentSourceLimit()
            self.source_limit = temp_model.from_map(m['SourceLimit'])
        if m.get('WhitenGfbrNets') is not None:
            self.whiten_gfbr_nets = m.get('WhitenGfbrNets')
        return self


class ListPolicyResponseBodyPolicyList(TeaModel):
    def __init__(
        self,
        attached_count: int = None,
        content: ListPolicyResponseBodyPolicyListContent = None,
        id: str = None,
        name: str = None,
        type: str = None,
    ):
        self.attached_count = attached_count
        self.content = content
        self.id = id
        self.name = name
        self.type = type

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attached_count is not None:
            result['AttachedCount'] = self.attached_count
        if self.content is not None:
            result['Content'] = self.content.to_map()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttachedCount') is not None:
            self.attached_count = m.get('AttachedCount')
        if m.get('Content') is not None:
            temp_model = ListPolicyResponseBodyPolicyListContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListPolicyResponseBody(TeaModel):
    def __init__(
        self,
        policy_list: List[ListPolicyResponseBodyPolicyList] = None,
        request_id: str = None,
        total: int = None,
    ):
        self.policy_list = policy_list
        self.request_id = request_id
        self.total = total

    def validate(self):
        if self.policy_list:
            for k in self.policy_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PolicyList'] = []
        if self.policy_list is not None:
            for k in self.policy_list:
                result['PolicyList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.policy_list = []
        if m.get('PolicyList') is not None:
            for k in m.get('PolicyList'):
                temp_model = ListPolicyResponseBodyPolicyList()
                self.policy_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListPolicyResponseBody = None,
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
            temp_model = ListPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPolicyAttachmentRequestIpPortProtocolList(TeaModel):
    def __init__(
        self,
        ip: str = None,
        port: int = None,
        protocol: str = None,
    ):
        # This parameter is required.
        self.ip = ip
        self.port = port
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.port is not None:
            result['Port'] = self.port
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        return self


class ListPolicyAttachmentRequest(TeaModel):
    def __init__(
        self,
        ip_port_protocol_list: List[ListPolicyAttachmentRequestIpPortProtocolList] = None,
        page_no: int = None,
        page_size: int = None,
        policy_id: str = None,
        policy_type: str = None,
    ):
        self.ip_port_protocol_list = ip_port_protocol_list
        self.page_no = page_no
        self.page_size = page_size
        self.policy_id = policy_id
        self.policy_type = policy_type

    def validate(self):
        if self.ip_port_protocol_list:
            for k in self.ip_port_protocol_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['IpPortProtocolList'] = []
        if self.ip_port_protocol_list is not None:
            for k in self.ip_port_protocol_list:
                result['IpPortProtocolList'].append(k.to_map() if k else None)
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ip_port_protocol_list = []
        if m.get('IpPortProtocolList') is not None:
            for k in m.get('IpPortProtocolList'):
                temp_model = ListPolicyAttachmentRequestIpPortProtocolList()
                self.ip_port_protocol_list.append(temp_model.from_map(k))
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        return self


class ListPolicyAttachmentShrinkRequest(TeaModel):
    def __init__(
        self,
        ip_port_protocol_list_shrink: str = None,
        page_no: int = None,
        page_size: int = None,
        policy_id: str = None,
        policy_type: str = None,
    ):
        self.ip_port_protocol_list_shrink = ip_port_protocol_list_shrink
        self.page_no = page_no
        self.page_size = page_size
        self.policy_id = policy_id
        self.policy_type = policy_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_port_protocol_list_shrink is not None:
            result['IpPortProtocolList'] = self.ip_port_protocol_list_shrink
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpPortProtocolList') is not None:
            self.ip_port_protocol_list_shrink = m.get('IpPortProtocolList')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        return self


class ListPolicyAttachmentResponseBodyAttachmentList(TeaModel):
    def __init__(
        self,
        ip: str = None,
        member_uid: str = None,
        policy_id: str = None,
        policy_name: str = None,
        policy_type: str = None,
        port: int = None,
        protocol: str = None,
        region: str = None,
    ):
        self.ip = ip
        self.member_uid = member_uid
        self.policy_id = policy_id
        self.policy_name = policy_name
        self.policy_type = policy_type
        self.port = port
        self.protocol = protocol
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        if self.port is not None:
            result['Port'] = self.port
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class ListPolicyAttachmentResponseBody(TeaModel):
    def __init__(
        self,
        attachment_list: List[ListPolicyAttachmentResponseBodyAttachmentList] = None,
        request_id: str = None,
        total: int = None,
    ):
        self.attachment_list = attachment_list
        self.request_id = request_id
        self.total = total

    def validate(self):
        if self.attachment_list:
            for k in self.attachment_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AttachmentList'] = []
        if self.attachment_list is not None:
            for k in self.attachment_list:
                result['AttachmentList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attachment_list = []
        if m.get('AttachmentList') is not None:
            for k in m.get('AttachmentList'):
                temp_model = ListPolicyAttachmentResponseBodyAttachmentList()
                self.attachment_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListPolicyAttachmentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListPolicyAttachmentResponseBody = None,
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
            temp_model = ListPolicyAttachmentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagKeysRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_type: str = None,
    ):
        # The number of the page to return. Pages start from page **1**. Default value: **1**.
        self.current_page = current_page
        # The number of entries to return on each page. Valid values: 1 to **50**. Default value: **10**.
        self.page_size = page_size
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The type of the resource. Valid value: **INSTANCE**.
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
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class ListTagKeysResponseBodyTagKeys(TeaModel):
    def __init__(
        self,
        tag_count: int = None,
        tag_key: str = None,
    ):
        # The total number of tag values that correspond to each key.
        self.tag_count = tag_count
        # The key of each tag.
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_count is not None:
            result['TagCount'] = self.tag_count
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagCount') is not None:
            self.tag_count = m.get('TagCount')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class ListTagKeysResponseBody(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        request_id: str = None,
        tag_keys: List[ListTagKeysResponseBodyTagKeys] = None,
        total_count: int = None,
    ):
        # The page number of the returned page.
        self.current_page = current_page
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The list of tags and the details of each tag.
        self.tag_keys = tag_keys
        # The total number of tags.
        self.total_count = total_count

    def validate(self):
        if self.tag_keys:
            for k in self.tag_keys:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TagKeys'] = []
        if self.tag_keys is not None:
            for k in self.tag_keys:
                result['TagKeys'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tag_keys = []
        if m.get('TagKeys') is not None:
            for k in m.get('TagKeys'):
                temp_model = ListTagKeysResponseBodyTagKeys()
                self.tag_keys.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListTagKeysResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTagKeysResponseBody = None,
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
            temp_model = ListTagKeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag to query.
        # 
        # >  The **ResourceIds.N** parameter and the key-value pair (Tag.N.Key and Tag.N.Value) cannot be left empty at the same time.
        self.key = key
        # The value of the tag to query.
        # 
        # >  The **ResourceIds.N** parameter and the key-value pair (Tag.N.Key and Tag.N.Value) cannot be left empty at the same time.
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
        resource_group_id: str = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag: List[ListTagResourcesRequestTag] = None,
    ):
        # The query token. Set the value to the **NextToken** value that is returned in the last call to the ListTagResources operation. Leave this parameter empty the first time you call this operation.
        self.next_token = next_token
        # The ID of the region where the Anti-DDoS Origin instance resides.
        # 
        # >  You can call the [DescribeRegions](https://help.aliyun.com/document_detail/118703.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group to which the Anti-DDoS Origin instance belongs in Resource Management.
        # 
        # If you do not specify this parameter, the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id
        # The IDs of Anti-DDoS Origin Instances to query.
        # 
        # >  You can call the [DescribeInstanceList](https://help.aliyun.com/document_detail/118698.html) operation to query the IDs of all Anti-DDoS Origin instances.
        self.resource_id = resource_id
        # The type of the resource to query. Set the value to **INSTANCE**, which indicates instances.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The tags to query.
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
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
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
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
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
        # The ID of the Anti-DDoS Origin instance.
        self.resource_id = resource_id
        # The type of the resource. The value is fixed as **INSTANCE**, which indicates instances.
        self.resource_type = resource_type
        # The key of the tag that is added to the instance.
        self.tag_key = tag_key
        # The value of the tag that is added to the instance.
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
        # The query token that is returned in this call.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The list of tags that are added to the Anti-DDoS Origin instance.
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


class ModifyPolicyRequestContentFingerPrintRuleList(TeaModel):
    def __init__(
        self,
        dst_port_end: int = None,
        dst_port_start: int = None,
        id: str = None,
        match_action: str = None,
        max_pkt_len: int = None,
        min_pkt_len: int = None,
        offset: int = None,
        payload_bytes: str = None,
        protocol: str = None,
        rate_value: int = None,
        seq_no: int = None,
        src_port_end: int = None,
        src_port_start: int = None,
    ):
        # This parameter is required.
        self.dst_port_end = dst_port_end
        # This parameter is required.
        self.dst_port_start = dst_port_start
        self.id = id
        # This parameter is required.
        self.match_action = match_action
        # This parameter is required.
        self.max_pkt_len = max_pkt_len
        # This parameter is required.
        self.min_pkt_len = min_pkt_len
        self.offset = offset
        self.payload_bytes = payload_bytes
        # This parameter is required.
        self.protocol = protocol
        self.rate_value = rate_value
        # This parameter is required.
        self.seq_no = seq_no
        # This parameter is required.
        self.src_port_end = src_port_end
        # This parameter is required.
        self.src_port_start = src_port_start

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dst_port_end is not None:
            result['DstPortEnd'] = self.dst_port_end
        if self.dst_port_start is not None:
            result['DstPortStart'] = self.dst_port_start
        if self.id is not None:
            result['Id'] = self.id
        if self.match_action is not None:
            result['MatchAction'] = self.match_action
        if self.max_pkt_len is not None:
            result['MaxPktLen'] = self.max_pkt_len
        if self.min_pkt_len is not None:
            result['MinPktLen'] = self.min_pkt_len
        if self.offset is not None:
            result['Offset'] = self.offset
        if self.payload_bytes is not None:
            result['PayloadBytes'] = self.payload_bytes
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.rate_value is not None:
            result['RateValue'] = self.rate_value
        if self.seq_no is not None:
            result['SeqNo'] = self.seq_no
        if self.src_port_end is not None:
            result['SrcPortEnd'] = self.src_port_end
        if self.src_port_start is not None:
            result['SrcPortStart'] = self.src_port_start
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DstPortEnd') is not None:
            self.dst_port_end = m.get('DstPortEnd')
        if m.get('DstPortStart') is not None:
            self.dst_port_start = m.get('DstPortStart')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('MatchAction') is not None:
            self.match_action = m.get('MatchAction')
        if m.get('MaxPktLen') is not None:
            self.max_pkt_len = m.get('MaxPktLen')
        if m.get('MinPktLen') is not None:
            self.min_pkt_len = m.get('MinPktLen')
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')
        if m.get('PayloadBytes') is not None:
            self.payload_bytes = m.get('PayloadBytes')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('RateValue') is not None:
            self.rate_value = m.get('RateValue')
        if m.get('SeqNo') is not None:
            self.seq_no = m.get('SeqNo')
        if m.get('SrcPortEnd') is not None:
            self.src_port_end = m.get('SrcPortEnd')
        if m.get('SrcPortStart') is not None:
            self.src_port_start = m.get('SrcPortStart')
        return self


class ModifyPolicyRequestContentL4RuleListConditionList(TeaModel):
    def __init__(
        self,
        arg: str = None,
        depth: int = None,
        position: int = None,
    ):
        # This parameter is required.
        self.arg = arg
        # This parameter is required.
        self.depth = depth
        # This parameter is required.
        self.position = position

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arg is not None:
            result['Arg'] = self.arg
        if self.depth is not None:
            result['Depth'] = self.depth
        if self.position is not None:
            result['Position'] = self.position
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arg') is not None:
            self.arg = m.get('Arg')
        if m.get('Depth') is not None:
            self.depth = m.get('Depth')
        if m.get('Position') is not None:
            self.position = m.get('Position')
        return self


class ModifyPolicyRequestContentL4RuleList(TeaModel):
    def __init__(
        self,
        action: str = None,
        condition_list: List[ModifyPolicyRequestContentL4RuleListConditionList] = None,
        limited: int = None,
        match: str = None,
        method: str = None,
        name: str = None,
        priority: int = None,
    ):
        # This parameter is required.
        self.action = action
        # This parameter is required.
        self.condition_list = condition_list
        # This parameter is required.
        self.limited = limited
        # This parameter is required.
        self.match = match
        # This parameter is required.
        self.method = method
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.priority = priority

    def validate(self):
        if self.condition_list:
            for k in self.condition_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        result['ConditionList'] = []
        if self.condition_list is not None:
            for k in self.condition_list:
                result['ConditionList'].append(k.to_map() if k else None)
        if self.limited is not None:
            result['Limited'] = self.limited
        if self.match is not None:
            result['Match'] = self.match
        if self.method is not None:
            result['Method'] = self.method
        if self.name is not None:
            result['Name'] = self.name
        if self.priority is not None:
            result['Priority'] = self.priority
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        self.condition_list = []
        if m.get('ConditionList') is not None:
            for k in m.get('ConditionList'):
                temp_model = ModifyPolicyRequestContentL4RuleListConditionList()
                self.condition_list.append(temp_model.from_map(k))
        if m.get('Limited') is not None:
            self.limited = m.get('Limited')
        if m.get('Match') is not None:
            self.match = m.get('Match')
        if m.get('Method') is not None:
            self.method = m.get('Method')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        return self


class ModifyPolicyRequestContentPortRuleList(TeaModel):
    def __init__(
        self,
        dst_port_end: int = None,
        dst_port_start: int = None,
        id: str = None,
        match_action: str = None,
        protocol: str = None,
        seq_no: int = None,
        src_port_end: int = None,
        src_port_start: int = None,
    ):
        # This parameter is required.
        self.dst_port_end = dst_port_end
        # This parameter is required.
        self.dst_port_start = dst_port_start
        self.id = id
        # This parameter is required.
        self.match_action = match_action
        # This parameter is required.
        self.protocol = protocol
        # This parameter is required.
        self.seq_no = seq_no
        # This parameter is required.
        self.src_port_end = src_port_end
        # This parameter is required.
        self.src_port_start = src_port_start

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dst_port_end is not None:
            result['DstPortEnd'] = self.dst_port_end
        if self.dst_port_start is not None:
            result['DstPortStart'] = self.dst_port_start
        if self.id is not None:
            result['Id'] = self.id
        if self.match_action is not None:
            result['MatchAction'] = self.match_action
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.seq_no is not None:
            result['SeqNo'] = self.seq_no
        if self.src_port_end is not None:
            result['SrcPortEnd'] = self.src_port_end
        if self.src_port_start is not None:
            result['SrcPortStart'] = self.src_port_start
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DstPortEnd') is not None:
            self.dst_port_end = m.get('DstPortEnd')
        if m.get('DstPortStart') is not None:
            self.dst_port_start = m.get('DstPortStart')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('MatchAction') is not None:
            self.match_action = m.get('MatchAction')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('SeqNo') is not None:
            self.seq_no = m.get('SeqNo')
        if m.get('SrcPortEnd') is not None:
            self.src_port_end = m.get('SrcPortEnd')
        if m.get('SrcPortStart') is not None:
            self.src_port_start = m.get('SrcPortStart')
        return self


class ModifyPolicyRequestContentSourceBlockList(TeaModel):
    def __init__(
        self,
        block_expire_seconds: int = None,
        every_seconds: int = None,
        exceed_limit_times: int = None,
        type: int = None,
    ):
        # This parameter is required.
        self.block_expire_seconds = block_expire_seconds
        # This parameter is required.
        self.every_seconds = every_seconds
        # This parameter is required.
        self.exceed_limit_times = exceed_limit_times
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.block_expire_seconds is not None:
            result['BlockExpireSeconds'] = self.block_expire_seconds
        if self.every_seconds is not None:
            result['EverySeconds'] = self.every_seconds
        if self.exceed_limit_times is not None:
            result['ExceedLimitTimes'] = self.exceed_limit_times
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlockExpireSeconds') is not None:
            self.block_expire_seconds = m.get('BlockExpireSeconds')
        if m.get('EverySeconds') is not None:
            self.every_seconds = m.get('EverySeconds')
        if m.get('ExceedLimitTimes') is not None:
            self.exceed_limit_times = m.get('ExceedLimitTimes')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ModifyPolicyRequestContentSourceLimit(TeaModel):
    def __init__(
        self,
        bps: int = None,
        pps: int = None,
        syn_bps: int = None,
        syn_pps: int = None,
    ):
        self.bps = bps
        self.pps = pps
        self.syn_bps = syn_bps
        self.syn_pps = syn_pps

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bps is not None:
            result['Bps'] = self.bps
        if self.pps is not None:
            result['Pps'] = self.pps
        if self.syn_bps is not None:
            result['SynBps'] = self.syn_bps
        if self.syn_pps is not None:
            result['SynPps'] = self.syn_pps
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bps') is not None:
            self.bps = m.get('Bps')
        if m.get('Pps') is not None:
            self.pps = m.get('Pps')
        if m.get('SynBps') is not None:
            self.syn_bps = m.get('SynBps')
        if m.get('SynPps') is not None:
            self.syn_pps = m.get('SynPps')
        return self


class ModifyPolicyRequestContent(TeaModel):
    def __init__(
        self,
        black_ip_list: List[str] = None,
        black_ip_list_expire_at: int = None,
        enable_drop_icmp: bool = None,
        enable_intelligence: bool = None,
        enable_l4defense: bool = None,
        finger_print_rule_list: List[ModifyPolicyRequestContentFingerPrintRuleList] = None,
        intelligence_level: str = None,
        l_4rule_list: List[ModifyPolicyRequestContentL4RuleList] = None,
        port_rule_list: List[ModifyPolicyRequestContentPortRuleList] = None,
        reflect_block_udp_port_list: List[int] = None,
        region_block_country_list: List[int] = None,
        region_block_province_list: List[int] = None,
        source_block_list: List[ModifyPolicyRequestContentSourceBlockList] = None,
        source_limit: ModifyPolicyRequestContentSourceLimit = None,
        white_ip_list: List[str] = None,
        whiten_gfbr_nets: bool = None,
    ):
        self.black_ip_list = black_ip_list
        self.black_ip_list_expire_at = black_ip_list_expire_at
        self.enable_drop_icmp = enable_drop_icmp
        self.enable_intelligence = enable_intelligence
        self.enable_l4defense = enable_l4defense
        self.finger_print_rule_list = finger_print_rule_list
        self.intelligence_level = intelligence_level
        self.l_4rule_list = l_4rule_list
        self.port_rule_list = port_rule_list
        self.reflect_block_udp_port_list = reflect_block_udp_port_list
        self.region_block_country_list = region_block_country_list
        self.region_block_province_list = region_block_province_list
        self.source_block_list = source_block_list
        self.source_limit = source_limit
        self.white_ip_list = white_ip_list
        self.whiten_gfbr_nets = whiten_gfbr_nets

    def validate(self):
        if self.finger_print_rule_list:
            for k in self.finger_print_rule_list:
                if k:
                    k.validate()
        if self.l_4rule_list:
            for k in self.l_4rule_list:
                if k:
                    k.validate()
        if self.port_rule_list:
            for k in self.port_rule_list:
                if k:
                    k.validate()
        if self.source_block_list:
            for k in self.source_block_list:
                if k:
                    k.validate()
        if self.source_limit:
            self.source_limit.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.black_ip_list is not None:
            result['BlackIpList'] = self.black_ip_list
        if self.black_ip_list_expire_at is not None:
            result['BlackIpListExpireAt'] = self.black_ip_list_expire_at
        if self.enable_drop_icmp is not None:
            result['EnableDropIcmp'] = self.enable_drop_icmp
        if self.enable_intelligence is not None:
            result['EnableIntelligence'] = self.enable_intelligence
        if self.enable_l4defense is not None:
            result['EnableL4Defense'] = self.enable_l4defense
        result['FingerPrintRuleList'] = []
        if self.finger_print_rule_list is not None:
            for k in self.finger_print_rule_list:
                result['FingerPrintRuleList'].append(k.to_map() if k else None)
        if self.intelligence_level is not None:
            result['IntelligenceLevel'] = self.intelligence_level
        result['L4RuleList'] = []
        if self.l_4rule_list is not None:
            for k in self.l_4rule_list:
                result['L4RuleList'].append(k.to_map() if k else None)
        result['PortRuleList'] = []
        if self.port_rule_list is not None:
            for k in self.port_rule_list:
                result['PortRuleList'].append(k.to_map() if k else None)
        if self.reflect_block_udp_port_list is not None:
            result['ReflectBlockUdpPortList'] = self.reflect_block_udp_port_list
        if self.region_block_country_list is not None:
            result['RegionBlockCountryList'] = self.region_block_country_list
        if self.region_block_province_list is not None:
            result['RegionBlockProvinceList'] = self.region_block_province_list
        result['SourceBlockList'] = []
        if self.source_block_list is not None:
            for k in self.source_block_list:
                result['SourceBlockList'].append(k.to_map() if k else None)
        if self.source_limit is not None:
            result['SourceLimit'] = self.source_limit.to_map()
        if self.white_ip_list is not None:
            result['WhiteIpList'] = self.white_ip_list
        if self.whiten_gfbr_nets is not None:
            result['WhitenGfbrNets'] = self.whiten_gfbr_nets
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlackIpList') is not None:
            self.black_ip_list = m.get('BlackIpList')
        if m.get('BlackIpListExpireAt') is not None:
            self.black_ip_list_expire_at = m.get('BlackIpListExpireAt')
        if m.get('EnableDropIcmp') is not None:
            self.enable_drop_icmp = m.get('EnableDropIcmp')
        if m.get('EnableIntelligence') is not None:
            self.enable_intelligence = m.get('EnableIntelligence')
        if m.get('EnableL4Defense') is not None:
            self.enable_l4defense = m.get('EnableL4Defense')
        self.finger_print_rule_list = []
        if m.get('FingerPrintRuleList') is not None:
            for k in m.get('FingerPrintRuleList'):
                temp_model = ModifyPolicyRequestContentFingerPrintRuleList()
                self.finger_print_rule_list.append(temp_model.from_map(k))
        if m.get('IntelligenceLevel') is not None:
            self.intelligence_level = m.get('IntelligenceLevel')
        self.l_4rule_list = []
        if m.get('L4RuleList') is not None:
            for k in m.get('L4RuleList'):
                temp_model = ModifyPolicyRequestContentL4RuleList()
                self.l_4rule_list.append(temp_model.from_map(k))
        self.port_rule_list = []
        if m.get('PortRuleList') is not None:
            for k in m.get('PortRuleList'):
                temp_model = ModifyPolicyRequestContentPortRuleList()
                self.port_rule_list.append(temp_model.from_map(k))
        if m.get('ReflectBlockUdpPortList') is not None:
            self.reflect_block_udp_port_list = m.get('ReflectBlockUdpPortList')
        if m.get('RegionBlockCountryList') is not None:
            self.region_block_country_list = m.get('RegionBlockCountryList')
        if m.get('RegionBlockProvinceList') is not None:
            self.region_block_province_list = m.get('RegionBlockProvinceList')
        self.source_block_list = []
        if m.get('SourceBlockList') is not None:
            for k in m.get('SourceBlockList'):
                temp_model = ModifyPolicyRequestContentSourceBlockList()
                self.source_block_list.append(temp_model.from_map(k))
        if m.get('SourceLimit') is not None:
            temp_model = ModifyPolicyRequestContentSourceLimit()
            self.source_limit = temp_model.from_map(m['SourceLimit'])
        if m.get('WhiteIpList') is not None:
            self.white_ip_list = m.get('WhiteIpList')
        if m.get('WhitenGfbrNets') is not None:
            self.whiten_gfbr_nets = m.get('WhitenGfbrNets')
        return self


class ModifyPolicyRequest(TeaModel):
    def __init__(
        self,
        action_type: int = None,
        content: ModifyPolicyRequestContent = None,
        id: str = None,
        name: str = None,
    ):
        # This parameter is required.
        self.action_type = action_type
        self.content = content
        # This parameter is required.
        self.id = id
        self.name = name

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_type is not None:
            result['ActionType'] = self.action_type
        if self.content is not None:
            result['Content'] = self.content.to_map()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')
        if m.get('Content') is not None:
            temp_model = ModifyPolicyRequestContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ModifyPolicyShrinkRequest(TeaModel):
    def __init__(
        self,
        action_type: int = None,
        content_shrink: str = None,
        id: str = None,
        name: str = None,
    ):
        # This parameter is required.
        self.action_type = action_type
        self.content_shrink = content_shrink
        # This parameter is required.
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_type is not None:
            result['ActionType'] = self.action_type
        if self.content_shrink is not None:
            result['Content'] = self.content_shrink
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')
        if m.get('Content') is not None:
            self.content_shrink = m.get('Content')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ModifyPolicyResponseBody(TeaModel):
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


class ModifyPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyPolicyResponseBody = None,
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
            temp_model = ModifyPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyPolicyContentRequestContentFingerPrintRuleList(TeaModel):
    def __init__(
        self,
        dst_port_end: int = None,
        dst_port_start: int = None,
        id: str = None,
        match_action: str = None,
        max_pkt_len: int = None,
        min_pkt_len: int = None,
        offset: int = None,
        payload_bytes: str = None,
        protocol: str = None,
        rate_value: int = None,
        seq_no: int = None,
        src_port_end: int = None,
        src_port_start: int = None,
    ):
        # This parameter is required.
        self.dst_port_end = dst_port_end
        # This parameter is required.
        self.dst_port_start = dst_port_start
        self.id = id
        # This parameter is required.
        self.match_action = match_action
        # This parameter is required.
        self.max_pkt_len = max_pkt_len
        # This parameter is required.
        self.min_pkt_len = min_pkt_len
        self.offset = offset
        self.payload_bytes = payload_bytes
        # This parameter is required.
        self.protocol = protocol
        self.rate_value = rate_value
        # This parameter is required.
        self.seq_no = seq_no
        # This parameter is required.
        self.src_port_end = src_port_end
        # This parameter is required.
        self.src_port_start = src_port_start

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dst_port_end is not None:
            result['DstPortEnd'] = self.dst_port_end
        if self.dst_port_start is not None:
            result['DstPortStart'] = self.dst_port_start
        if self.id is not None:
            result['Id'] = self.id
        if self.match_action is not None:
            result['MatchAction'] = self.match_action
        if self.max_pkt_len is not None:
            result['MaxPktLen'] = self.max_pkt_len
        if self.min_pkt_len is not None:
            result['MinPktLen'] = self.min_pkt_len
        if self.offset is not None:
            result['Offset'] = self.offset
        if self.payload_bytes is not None:
            result['PayloadBytes'] = self.payload_bytes
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.rate_value is not None:
            result['RateValue'] = self.rate_value
        if self.seq_no is not None:
            result['SeqNo'] = self.seq_no
        if self.src_port_end is not None:
            result['SrcPortEnd'] = self.src_port_end
        if self.src_port_start is not None:
            result['SrcPortStart'] = self.src_port_start
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DstPortEnd') is not None:
            self.dst_port_end = m.get('DstPortEnd')
        if m.get('DstPortStart') is not None:
            self.dst_port_start = m.get('DstPortStart')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('MatchAction') is not None:
            self.match_action = m.get('MatchAction')
        if m.get('MaxPktLen') is not None:
            self.max_pkt_len = m.get('MaxPktLen')
        if m.get('MinPktLen') is not None:
            self.min_pkt_len = m.get('MinPktLen')
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')
        if m.get('PayloadBytes') is not None:
            self.payload_bytes = m.get('PayloadBytes')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('RateValue') is not None:
            self.rate_value = m.get('RateValue')
        if m.get('SeqNo') is not None:
            self.seq_no = m.get('SeqNo')
        if m.get('SrcPortEnd') is not None:
            self.src_port_end = m.get('SrcPortEnd')
        if m.get('SrcPortStart') is not None:
            self.src_port_start = m.get('SrcPortStart')
        return self


class ModifyPolicyContentRequestContentL4RuleListConditionList(TeaModel):
    def __init__(
        self,
        arg: str = None,
        depth: int = None,
        position: int = None,
    ):
        # This parameter is required.
        self.arg = arg
        # This parameter is required.
        self.depth = depth
        # This parameter is required.
        self.position = position

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arg is not None:
            result['Arg'] = self.arg
        if self.depth is not None:
            result['Depth'] = self.depth
        if self.position is not None:
            result['Position'] = self.position
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arg') is not None:
            self.arg = m.get('Arg')
        if m.get('Depth') is not None:
            self.depth = m.get('Depth')
        if m.get('Position') is not None:
            self.position = m.get('Position')
        return self


class ModifyPolicyContentRequestContentL4RuleList(TeaModel):
    def __init__(
        self,
        action: str = None,
        condition_list: List[ModifyPolicyContentRequestContentL4RuleListConditionList] = None,
        limited: int = None,
        match: str = None,
        method: str = None,
        name: str = None,
        priority: int = None,
    ):
        # This parameter is required.
        self.action = action
        # This parameter is required.
        self.condition_list = condition_list
        # This parameter is required.
        self.limited = limited
        # This parameter is required.
        self.match = match
        # This parameter is required.
        self.method = method
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.priority = priority

    def validate(self):
        if self.condition_list:
            for k in self.condition_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        result['ConditionList'] = []
        if self.condition_list is not None:
            for k in self.condition_list:
                result['ConditionList'].append(k.to_map() if k else None)
        if self.limited is not None:
            result['Limited'] = self.limited
        if self.match is not None:
            result['Match'] = self.match
        if self.method is not None:
            result['Method'] = self.method
        if self.name is not None:
            result['Name'] = self.name
        if self.priority is not None:
            result['Priority'] = self.priority
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        self.condition_list = []
        if m.get('ConditionList') is not None:
            for k in m.get('ConditionList'):
                temp_model = ModifyPolicyContentRequestContentL4RuleListConditionList()
                self.condition_list.append(temp_model.from_map(k))
        if m.get('Limited') is not None:
            self.limited = m.get('Limited')
        if m.get('Match') is not None:
            self.match = m.get('Match')
        if m.get('Method') is not None:
            self.method = m.get('Method')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        return self


class ModifyPolicyContentRequestContentPortRuleList(TeaModel):
    def __init__(
        self,
        dst_port_end: int = None,
        dst_port_start: int = None,
        id: str = None,
        match_action: str = None,
        protocol: str = None,
        seq_no: int = None,
        src_port_end: int = None,
        src_port_start: int = None,
    ):
        # This parameter is required.
        self.dst_port_end = dst_port_end
        # This parameter is required.
        self.dst_port_start = dst_port_start
        self.id = id
        # This parameter is required.
        self.match_action = match_action
        # This parameter is required.
        self.protocol = protocol
        # This parameter is required.
        self.seq_no = seq_no
        # This parameter is required.
        self.src_port_end = src_port_end
        # This parameter is required.
        self.src_port_start = src_port_start

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dst_port_end is not None:
            result['DstPortEnd'] = self.dst_port_end
        if self.dst_port_start is not None:
            result['DstPortStart'] = self.dst_port_start
        if self.id is not None:
            result['Id'] = self.id
        if self.match_action is not None:
            result['MatchAction'] = self.match_action
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.seq_no is not None:
            result['SeqNo'] = self.seq_no
        if self.src_port_end is not None:
            result['SrcPortEnd'] = self.src_port_end
        if self.src_port_start is not None:
            result['SrcPortStart'] = self.src_port_start
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DstPortEnd') is not None:
            self.dst_port_end = m.get('DstPortEnd')
        if m.get('DstPortStart') is not None:
            self.dst_port_start = m.get('DstPortStart')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('MatchAction') is not None:
            self.match_action = m.get('MatchAction')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('SeqNo') is not None:
            self.seq_no = m.get('SeqNo')
        if m.get('SrcPortEnd') is not None:
            self.src_port_end = m.get('SrcPortEnd')
        if m.get('SrcPortStart') is not None:
            self.src_port_start = m.get('SrcPortStart')
        return self


class ModifyPolicyContentRequestContentSourceBlockList(TeaModel):
    def __init__(
        self,
        block_expire_seconds: int = None,
        every_seconds: int = None,
        exceed_limit_times: int = None,
        type: int = None,
    ):
        # This parameter is required.
        self.block_expire_seconds = block_expire_seconds
        # This parameter is required.
        self.every_seconds = every_seconds
        # This parameter is required.
        self.exceed_limit_times = exceed_limit_times
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.block_expire_seconds is not None:
            result['BlockExpireSeconds'] = self.block_expire_seconds
        if self.every_seconds is not None:
            result['EverySeconds'] = self.every_seconds
        if self.exceed_limit_times is not None:
            result['ExceedLimitTimes'] = self.exceed_limit_times
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlockExpireSeconds') is not None:
            self.block_expire_seconds = m.get('BlockExpireSeconds')
        if m.get('EverySeconds') is not None:
            self.every_seconds = m.get('EverySeconds')
        if m.get('ExceedLimitTimes') is not None:
            self.exceed_limit_times = m.get('ExceedLimitTimes')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ModifyPolicyContentRequestContentSourceLimit(TeaModel):
    def __init__(
        self,
        bps: int = None,
        pps: int = None,
        syn_bps: int = None,
        syn_pps: int = None,
    ):
        self.bps = bps
        self.pps = pps
        self.syn_bps = syn_bps
        self.syn_pps = syn_pps

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bps is not None:
            result['Bps'] = self.bps
        if self.pps is not None:
            result['Pps'] = self.pps
        if self.syn_bps is not None:
            result['SynBps'] = self.syn_bps
        if self.syn_pps is not None:
            result['SynPps'] = self.syn_pps
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bps') is not None:
            self.bps = m.get('Bps')
        if m.get('Pps') is not None:
            self.pps = m.get('Pps')
        if m.get('SynBps') is not None:
            self.syn_bps = m.get('SynBps')
        if m.get('SynPps') is not None:
            self.syn_pps = m.get('SynPps')
        return self


class ModifyPolicyContentRequestContent(TeaModel):
    def __init__(
        self,
        black_ip_list_expire_at: int = None,
        enable_drop_icmp: bool = None,
        enable_intelligence: bool = None,
        enable_l4defense: bool = None,
        finger_print_rule_list: List[ModifyPolicyContentRequestContentFingerPrintRuleList] = None,
        intelligence_level: str = None,
        l_4rule_list: List[ModifyPolicyContentRequestContentL4RuleList] = None,
        port_rule_list: List[ModifyPolicyContentRequestContentPortRuleList] = None,
        reflect_block_udp_port_list: List[int] = None,
        region_block_country_list: List[int] = None,
        region_block_province_list: List[int] = None,
        source_block_list: List[ModifyPolicyContentRequestContentSourceBlockList] = None,
        source_limit: ModifyPolicyContentRequestContentSourceLimit = None,
        whiten_gfbr_nets: bool = None,
    ):
        self.black_ip_list_expire_at = black_ip_list_expire_at
        self.enable_drop_icmp = enable_drop_icmp
        self.enable_intelligence = enable_intelligence
        self.enable_l4defense = enable_l4defense
        self.finger_print_rule_list = finger_print_rule_list
        self.intelligence_level = intelligence_level
        self.l_4rule_list = l_4rule_list
        self.port_rule_list = port_rule_list
        self.reflect_block_udp_port_list = reflect_block_udp_port_list
        self.region_block_country_list = region_block_country_list
        self.region_block_province_list = region_block_province_list
        self.source_block_list = source_block_list
        self.source_limit = source_limit
        self.whiten_gfbr_nets = whiten_gfbr_nets

    def validate(self):
        if self.finger_print_rule_list:
            for k in self.finger_print_rule_list:
                if k:
                    k.validate()
        if self.l_4rule_list:
            for k in self.l_4rule_list:
                if k:
                    k.validate()
        if self.port_rule_list:
            for k in self.port_rule_list:
                if k:
                    k.validate()
        if self.source_block_list:
            for k in self.source_block_list:
                if k:
                    k.validate()
        if self.source_limit:
            self.source_limit.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.black_ip_list_expire_at is not None:
            result['BlackIpListExpireAt'] = self.black_ip_list_expire_at
        if self.enable_drop_icmp is not None:
            result['EnableDropIcmp'] = self.enable_drop_icmp
        if self.enable_intelligence is not None:
            result['EnableIntelligence'] = self.enable_intelligence
        if self.enable_l4defense is not None:
            result['EnableL4Defense'] = self.enable_l4defense
        result['FingerPrintRuleList'] = []
        if self.finger_print_rule_list is not None:
            for k in self.finger_print_rule_list:
                result['FingerPrintRuleList'].append(k.to_map() if k else None)
        if self.intelligence_level is not None:
            result['IntelligenceLevel'] = self.intelligence_level
        result['L4RuleList'] = []
        if self.l_4rule_list is not None:
            for k in self.l_4rule_list:
                result['L4RuleList'].append(k.to_map() if k else None)
        result['PortRuleList'] = []
        if self.port_rule_list is not None:
            for k in self.port_rule_list:
                result['PortRuleList'].append(k.to_map() if k else None)
        if self.reflect_block_udp_port_list is not None:
            result['ReflectBlockUdpPortList'] = self.reflect_block_udp_port_list
        if self.region_block_country_list is not None:
            result['RegionBlockCountryList'] = self.region_block_country_list
        if self.region_block_province_list is not None:
            result['RegionBlockProvinceList'] = self.region_block_province_list
        result['SourceBlockList'] = []
        if self.source_block_list is not None:
            for k in self.source_block_list:
                result['SourceBlockList'].append(k.to_map() if k else None)
        if self.source_limit is not None:
            result['SourceLimit'] = self.source_limit.to_map()
        if self.whiten_gfbr_nets is not None:
            result['WhitenGfbrNets'] = self.whiten_gfbr_nets
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlackIpListExpireAt') is not None:
            self.black_ip_list_expire_at = m.get('BlackIpListExpireAt')
        if m.get('EnableDropIcmp') is not None:
            self.enable_drop_icmp = m.get('EnableDropIcmp')
        if m.get('EnableIntelligence') is not None:
            self.enable_intelligence = m.get('EnableIntelligence')
        if m.get('EnableL4Defense') is not None:
            self.enable_l4defense = m.get('EnableL4Defense')
        self.finger_print_rule_list = []
        if m.get('FingerPrintRuleList') is not None:
            for k in m.get('FingerPrintRuleList'):
                temp_model = ModifyPolicyContentRequestContentFingerPrintRuleList()
                self.finger_print_rule_list.append(temp_model.from_map(k))
        if m.get('IntelligenceLevel') is not None:
            self.intelligence_level = m.get('IntelligenceLevel')
        self.l_4rule_list = []
        if m.get('L4RuleList') is not None:
            for k in m.get('L4RuleList'):
                temp_model = ModifyPolicyContentRequestContentL4RuleList()
                self.l_4rule_list.append(temp_model.from_map(k))
        self.port_rule_list = []
        if m.get('PortRuleList') is not None:
            for k in m.get('PortRuleList'):
                temp_model = ModifyPolicyContentRequestContentPortRuleList()
                self.port_rule_list.append(temp_model.from_map(k))
        if m.get('ReflectBlockUdpPortList') is not None:
            self.reflect_block_udp_port_list = m.get('ReflectBlockUdpPortList')
        if m.get('RegionBlockCountryList') is not None:
            self.region_block_country_list = m.get('RegionBlockCountryList')
        if m.get('RegionBlockProvinceList') is not None:
            self.region_block_province_list = m.get('RegionBlockProvinceList')
        self.source_block_list = []
        if m.get('SourceBlockList') is not None:
            for k in m.get('SourceBlockList'):
                temp_model = ModifyPolicyContentRequestContentSourceBlockList()
                self.source_block_list.append(temp_model.from_map(k))
        if m.get('SourceLimit') is not None:
            temp_model = ModifyPolicyContentRequestContentSourceLimit()
            self.source_limit = temp_model.from_map(m['SourceLimit'])
        if m.get('WhitenGfbrNets') is not None:
            self.whiten_gfbr_nets = m.get('WhitenGfbrNets')
        return self


class ModifyPolicyContentRequest(TeaModel):
    def __init__(
        self,
        content: ModifyPolicyContentRequestContent = None,
        id: str = None,
        name: str = None,
    ):
        self.content = content
        # This parameter is required.
        self.id = id
        self.name = name

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content.to_map()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            temp_model = ModifyPolicyContentRequestContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ModifyPolicyContentShrinkRequest(TeaModel):
    def __init__(
        self,
        content_shrink: str = None,
        id: str = None,
        name: str = None,
    ):
        self.content_shrink = content_shrink
        # This parameter is required.
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content_shrink is not None:
            result['Content'] = self.content_shrink
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content_shrink = m.get('Content')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ModifyPolicyContentResponseBody(TeaModel):
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


class ModifyPolicyContentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyPolicyContentResponseBody = None,
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
            temp_model = ModifyPolicyContentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyRemarkRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
        remark: str = None,
        resource_group_id: str = None,
    ):
        # The ID of the Anti-DDoS Origin instance for which you want to add remarks.
        # 
        # >  You can call the [DescribeInstanceList](https://help.aliyun.com/document_detail/118698.html) operation to query the IDs of all Anti-DDoS Origin instances.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the region where the Anti-DDoS Origin instance resides.
        # 
        # >  You can call the [DescribeRegions](https://help.aliyun.com/document_detail/118703.html) operation to query the most recent region list.
        self.region_id = region_id
        # The remarks for the Anti-DDoS Origin instance.
        # 
        # This parameter is required.
        self.remark = remark
        # The ID of the resource group to which the Anti-DDoS Origin instance belongs in Resource Management.
        # 
        # If you do not specify this parameter, the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id

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
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class ModifyRemarkResponseBody(TeaModel):
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


class ModifyRemarkResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyRemarkResponseBody = None,
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
            temp_model = ModifyRemarkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySchedruleOnDemandRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
    ):
        # The ID of the on-demand instance.
        # 
        # >  You can call the [DescribeOnDemandInstance](https://help.aliyun.com/document_detail/152120.html) operation to query the IDs of all on-demand instances.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The region ID of the on-demand instance.
        # 
        # >  You can call the [DescribeRegions](https://help.aliyun.com/document_detail/118703.html) operation to query all regions supported by Anti-DDoS Origin.
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


class QuerySchedruleOnDemandResponseBodyRuleConfig(TeaModel):
    def __init__(
        self,
        rule_action: str = None,
        rule_condition_cnt: str = None,
        rule_condition_kpps: str = None,
        rule_condition_mbps: str = None,
        rule_name: str = None,
        rule_switch: str = None,
        rule_undo_begin_time: str = None,
        rule_undo_end_time: str = None,
        rule_undo_mode: str = None,
        time_zone: str = None,
    ):
        # The scheduling action. Set the value to **declare**, which indicates that the route is advertised.
        self.rule_action = rule_action
        # If the inbound bandwidth or packets consecutively exceed the threshold for the specified number of times, the scheduling rule is triggered and traffic is rerouted to the on-demand instance. The specified number of times is the value of this parameter.
        # 
        # >  The threshold of inbound bandwidth is the value of **RuleConditionMbps**. The threshold of inbound packets is the value of **RuleConditionKpps**.
        self.rule_condition_cnt = rule_condition_cnt
        # The threshold of inbound packets. Unit: Kpps. Minimum value: **10**.
        self.rule_condition_kpps = rule_condition_kpps
        # The threshold of inbound bandwidth. Unit: Mbit/s. Minimum value: **100**.
        self.rule_condition_mbps = rule_condition_mbps
        # The name of the scheduling rule.
        self.rule_name = rule_name
        # Indicates whether the scheduling rule is enabled. Valid values:
        # 
        # *   **on**: enabled
        # *   **off**: disabled
        self.rule_switch = rule_switch
        # The start time of the period during which the scheduling rule is automatically stopped. The time must be in the 24-hour clock and in the `hh:mm` format.
        # 
        # If the system detects that DDoS attacks stop, the system no longer reroutes traffic to the on-demand instance from the time you specified. We recommend that you set this parameter to a value that is defined as off-peak hours.
        # 
        # >  This parameter takes effect only when the **RuleUndoMode** parameter is set to **auto**.
        self.rule_undo_begin_time = rule_undo_begin_time
        # The end time of the period during which the scheduling rule is automatically stopped. The time must be in the 24-hour clock and in the `hh:mm` format.
        self.rule_undo_end_time = rule_undo_end_time
        # The stop method of the scheduling rule. Valid values:
        # 
        # *   **auto**: The scheduling rule automatically stops.
        # *   **manual**: The scheduling rule is manually stopped.
        self.rule_undo_mode = rule_undo_mode
        # The time zone of the time when the scheduling rule automatically stops. The time zone must be in the `GMT-hh:mm` format.
        # 
        # For example, the value `GMT-08:00` indicates that the time zone is UTC+8.
        # 
        # >  This parameter takes effect only when the **RuleUndoMode** parameter is set to **auto**.
        self.time_zone = time_zone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_action is not None:
            result['RuleAction'] = self.rule_action
        if self.rule_condition_cnt is not None:
            result['RuleConditionCnt'] = self.rule_condition_cnt
        if self.rule_condition_kpps is not None:
            result['RuleConditionKpps'] = self.rule_condition_kpps
        if self.rule_condition_mbps is not None:
            result['RuleConditionMbps'] = self.rule_condition_mbps
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_switch is not None:
            result['RuleSwitch'] = self.rule_switch
        if self.rule_undo_begin_time is not None:
            result['RuleUndoBeginTime'] = self.rule_undo_begin_time
        if self.rule_undo_end_time is not None:
            result['RuleUndoEndTime'] = self.rule_undo_end_time
        if self.rule_undo_mode is not None:
            result['RuleUndoMode'] = self.rule_undo_mode
        if self.time_zone is not None:
            result['TimeZone'] = self.time_zone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleAction') is not None:
            self.rule_action = m.get('RuleAction')
        if m.get('RuleConditionCnt') is not None:
            self.rule_condition_cnt = m.get('RuleConditionCnt')
        if m.get('RuleConditionKpps') is not None:
            self.rule_condition_kpps = m.get('RuleConditionKpps')
        if m.get('RuleConditionMbps') is not None:
            self.rule_condition_mbps = m.get('RuleConditionMbps')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleSwitch') is not None:
            self.rule_switch = m.get('RuleSwitch')
        if m.get('RuleUndoBeginTime') is not None:
            self.rule_undo_begin_time = m.get('RuleUndoBeginTime')
        if m.get('RuleUndoEndTime') is not None:
            self.rule_undo_end_time = m.get('RuleUndoEndTime')
        if m.get('RuleUndoMode') is not None:
            self.rule_undo_mode = m.get('RuleUndoMode')
        if m.get('TimeZone') is not None:
            self.time_zone = m.get('TimeZone')
        return self


class QuerySchedruleOnDemandResponseBodyRuleStatus(TeaModel):
    def __init__(
        self,
        net: str = None,
        rule_sched_status: str = None,
    ):
        # The CIDR block of the on-demand instance.
        self.net = net
        # The scheduling status. Valid values:
        # 
        # *   **scheduled**\
        # *   **unscheduled**\
        self.rule_sched_status = rule_sched_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.net is not None:
            result['Net'] = self.net
        if self.rule_sched_status is not None:
            result['RuleSchedStatus'] = self.rule_sched_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Net') is not None:
            self.net = m.get('Net')
        if m.get('RuleSchedStatus') is not None:
            self.rule_sched_status = m.get('RuleSchedStatus')
        return self


class QuerySchedruleOnDemandResponseBody(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        request_id: str = None,
        rule_config: List[QuerySchedruleOnDemandResponseBodyRuleConfig] = None,
        rule_status: List[QuerySchedruleOnDemandResponseBodyRuleStatus] = None,
        user_id: str = None,
    ):
        # The ID of the on-demand instance.
        self.instance_id = instance_id
        # The ID of the request.
        self.request_id = request_id
        # The configurations of the scheduling rule.
        self.rule_config = rule_config
        # The status of the scheduling rule.
        self.rule_status = rule_status
        # The ID of the Alibaba Cloud account.
        self.user_id = user_id

    def validate(self):
        if self.rule_config:
            for k in self.rule_config:
                if k:
                    k.validate()
        if self.rule_status:
            for k in self.rule_status:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['RuleConfig'] = []
        if self.rule_config is not None:
            for k in self.rule_config:
                result['RuleConfig'].append(k.to_map() if k else None)
        result['RuleStatus'] = []
        if self.rule_status is not None:
            for k in self.rule_status:
                result['RuleStatus'].append(k.to_map() if k else None)
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.rule_config = []
        if m.get('RuleConfig') is not None:
            for k in m.get('RuleConfig'):
                temp_model = QuerySchedruleOnDemandResponseBodyRuleConfig()
                self.rule_config.append(temp_model.from_map(k))
        self.rule_status = []
        if m.get('RuleStatus') is not None:
            for k in m.get('RuleStatus'):
                temp_model = QuerySchedruleOnDemandResponseBodyRuleStatus()
                self.rule_status.append(temp_model.from_map(k))
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class QuerySchedruleOnDemandResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QuerySchedruleOnDemandResponseBody = None,
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
            temp_model = QuerySchedruleOnDemandResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReleaseDdosOriginInstanceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ReleaseDdosOriginInstanceResponseBody(TeaModel):
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


class ReleaseDdosOriginInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReleaseDdosOriginInstanceResponseBody = None,
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
            temp_model = ReleaseDdosOriginInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetInstanceModeOnDemandRequest(TeaModel):
    def __init__(
        self,
        instance_id_list: List[str] = None,
        mode: str = None,
        region_id: str = None,
    ):
        # The IDs of on-demand instances.
        # 
        # >  You can call the [DescribeOnDemandInstance](https://help.aliyun.com/document_detail/152120.html) operation to query the IDs of all on-demand instances.
        # 
        # This parameter is required.
        self.instance_id_list = instance_id_list
        # The scheduling mode of the on-demand instance. Valid values:
        # 
        # *   **manual**: manual scheduling
        # *   **netflow-auto**: automatic scheduling
        # 
        # This parameter is required.
        self.mode = mode
        # The region ID of the on-demand instance.
        # 
        # >  You can call the [DescribeRegions](https://help.aliyun.com/document_detail/118703.html) operation to query all regions supported by Anti-DDoS Origin.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id_list is not None:
            result['InstanceIdList'] = self.instance_id_list
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIdList') is not None:
            self.instance_id_list = m.get('InstanceIdList')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class SetInstanceModeOnDemandResponseBody(TeaModel):
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


class SetInstanceModeOnDemandResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetInstanceModeOnDemandResponseBody = None,
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
            temp_model = SetInstanceModeOnDemandResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag to add.
        # 
        # >  If the specified key does not exist, a key is created.
        self.key = key
        # The value of the tag to add.
        # 
        # >  If the specified value does not exist, a value is created.
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
        region_id: str = None,
        resource_group_id: str = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag: List[TagResourcesRequestTag] = None,
    ):
        # The ID of the region where the Anti-DDoS Origin instance resides.
        # 
        # >  You can call the [DescribeRegions](https://help.aliyun.com/document_detail/118703.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group to which the Anti-DDoS Origin instance belongs in Resource Management.
        # 
        # If you do not specify this parameter, the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id
        # This parameter is required.
        self.resource_id = resource_id
        # The type of the resource to which you want to add tags. Set the value to **INSTANCE**, which indicates instances.
        # 
        # This parameter is required.
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
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
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
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
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
        resource_group_id: str = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag_key: List[str] = None,
    ):
        # Specifies whether to remove all tags from the specified Anti-DDoS Origin Enterprise instances.
        self.all = all
        # The ID of the region where the Anti-DDoS Origin Enterprise instances reside.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # This parameter is required.
        self.resource_id = resource_id
        # The type of the specified resource. Set the value to **INSTANCE**.
        # 
        # This parameter is required.
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
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
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
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
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


