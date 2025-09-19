# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class AddIpamPoolCidrRequest(TeaModel):
    def __init__(
        self,
        cidr: str = None,
        client_token: str = None,
        dry_run: bool = None,
        ipam_pool_id: str = None,
        netmask_length: int = None,
        region_id: str = None,
    ):
        # The CIDR block to be provisioned. 
        # > For private top-level pools, provisioning can only be done by entering a CIDR block.
        self.cidr = cidr
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The client token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the request ID as the client token. The request ID may be different for each request.
        self.client_token = client_token
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the DryRunOperation error code is returned.
        # *   **false** (default): performs a dry run and performs the actual request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The ID of the IPAM pool.
        # 
        # This parameter is required.
        self.ipam_pool_id = ipam_pool_id
        # Provision CIDR address segments through a mask method.  
        # > The public IPv6 top-level pool only supports provisioning via a mask.
        self.netmask_length = netmask_length
        # The ID of the region where the IPAM instance is hosted.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the most recent region list.
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
        if self.cidr is not None:
            result['Cidr'] = self.cidr
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.ipam_pool_id is not None:
            result['IpamPoolId'] = self.ipam_pool_id
        if self.netmask_length is not None:
            result['NetmaskLength'] = self.netmask_length
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cidr') is not None:
            self.cidr = m.get('Cidr')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IpamPoolId') is not None:
            self.ipam_pool_id = m.get('IpamPoolId')
        if m.get('NetmaskLength') is not None:
            self.netmask_length = m.get('NetmaskLength')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class AddIpamPoolCidrResponseBody(TeaModel):
    def __init__(
        self,
        cidr: str = None,
        request_id: str = None,
    ):
        # The successfully provisioned CIDR block.
        self.cidr = cidr
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cidr is not None:
            result['Cidr'] = self.cidr
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cidr') is not None:
            self.cidr = m.get('Cidr')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddIpamPoolCidrResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddIpamPoolCidrResponseBody = None,
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
            temp_model = AddIpamPoolCidrResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AssociateIpamResourceDiscoveryRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        ipam_id: str = None,
        ipam_resource_discovery_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The client token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the request ID as the client token. The request ID may be different for each request.
        self.client_token = client_token
        # Specifies whether to perform the dry run. Valid values:
        # 
        # *   **true**: Performs a dry run without associating the resource discovery and IPAM instance. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error code is returned. If the request passes the dry run, the DryRunOperation error code is returned.
        # *   **false** (default): performs a dry run and sends the request. After the request passes the check, an HTTP 2xx status code is returned and the resource discovery and IPAM instances are associated.
        self.dry_run = dry_run
        # The ID of the IPAM.
        # 
        # This parameter is required.
        self.ipam_id = ipam_id
        # The ID of resource discovery instance.
        # 
        # This parameter is required.
        self.ipam_resource_discovery_id = ipam_resource_discovery_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The request region.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.ipam_id is not None:
            result['IpamId'] = self.ipam_id
        if self.ipam_resource_discovery_id is not None:
            result['IpamResourceDiscoveryId'] = self.ipam_resource_discovery_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IpamId') is not None:
            self.ipam_id = m.get('IpamId')
        if m.get('IpamResourceDiscoveryId') is not None:
            self.ipam_resource_discovery_id = m.get('IpamResourceDiscoveryId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class AssociateIpamResourceDiscoveryResponseBody(TeaModel):
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


class AssociateIpamResourceDiscoveryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AssociateIpamResourceDiscoveryResponseBody = None,
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
            temp_model = AssociateIpamResourceDiscoveryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChangeResourceGroupRequest(TeaModel):
    def __init__(
        self,
        new_resource_group_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        resource_type: str = None,
    ):
        # The ID of the new resource group.
        # 
        # This parameter is required.
        self.new_resource_group_id = new_resource_group_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the region where the IPAM instance is hosted. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the IPAM resource.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Resource type, with values:
        # 
        # - Ipam:IPAM instance
        # 
        # - IpamScope:IPAM scope
        # 
        # - IpamPool:IPAM address pool
        # 
        # - IpamResourceDiscovery:IPAM resource discovery
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
        if self.new_resource_group_id is not None:
            result['NewResourceGroupId'] = self.new_resource_group_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NewResourceGroupId') is not None:
            self.new_resource_group_id = m.get('NewResourceGroupId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class ChangeResourceGroupResponseBody(TeaModel):
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


class CreateIpamRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the resource. You can specify at most 20 tag keys. It cannot be an empty string.
        # 
        # The tag key can be up to 64 characters in length and can contain letters, digits, periods (.), underscores (_), and hyphens (-). It must start with a letter but cannot start with `aliyun` or `acs:`. It cannot contain `http://` or `https://`.
        self.key = key
        # The tag value of the resource. You can specify up to 20 tag values. You can specify empty strings as tag values.
        # 
        # The tag value can be up to 128 characters in length and cannot contain `http://` or `https://`.
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


class CreateIpamRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        ipam_description: str = None,
        ipam_name: str = None,
        operating_region_list: List[str] = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        tag: List[CreateIpamRequestTag] = None,
    ):
        # The client token used to ensure the idempotence of the request. Use the client to generate the token, but you must make sure that the token is unique among different requests. The client token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the request ID as the client token. The request ID may be different for each request.
        self.client_token = client_token
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the DryRunOperation error code is returned.
        # *   **false** (default): performs a dry run and performs the actual request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The description of the IPAM.
        # 
        # It must be 1 to 256 characters in length. Start with a letter but cannot start with `http://` or `https://`. If you do not specify a description, the description is empty by default.
        self.ipam_description = ipam_description
        # The name of the IPAM.
        # 
        # It must be 1 to 128 characters in length and cannot start with `http://` or `https://`.
        self.ipam_name = ipam_name
        # The effective regions of the IPAM.
        # 
        # This parameter is required.
        self.operating_region_list = operating_region_list
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the region where the IPAM instance is hosted. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource group ID of the IPAM.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The tag list.
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
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.ipam_description is not None:
            result['IpamDescription'] = self.ipam_description
        if self.ipam_name is not None:
            result['IpamName'] = self.ipam_name
        if self.operating_region_list is not None:
            result['OperatingRegionList'] = self.operating_region_list
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IpamDescription') is not None:
            self.ipam_description = m.get('IpamDescription')
        if m.get('IpamName') is not None:
            self.ipam_name = m.get('IpamName')
        if m.get('OperatingRegionList') is not None:
            self.operating_region_list = m.get('OperatingRegionList')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateIpamRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class CreateIpamResponseBody(TeaModel):
    def __init__(
        self,
        default_resource_discovery_association_id: str = None,
        default_resource_discovery_id: str = None,
        ipam_id: str = None,
        private_default_scope_id: str = None,
        public_default_scope_id: str = None,
        request_id: str = None,
        resource_discovery_association_count: int = None,
    ):
        # The ID of the default resource discovery association.
        self.default_resource_discovery_association_id = default_resource_discovery_association_id
        # The ID of the default resource discovery instance.
        self.default_resource_discovery_id = default_resource_discovery_id
        # The ID of the IPAM.
        self.ipam_id = ipam_id
        # The default private scope created by the system after the IPAM is created.
        self.private_default_scope_id = private_default_scope_id
        # The default public scope created by the system after the IPAM is created.
        self.public_default_scope_id = public_default_scope_id
        # The request ID.
        self.request_id = request_id
        # The number of discovered resources.
        self.resource_discovery_association_count = resource_discovery_association_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_resource_discovery_association_id is not None:
            result['DefaultResourceDiscoveryAssociationId'] = self.default_resource_discovery_association_id
        if self.default_resource_discovery_id is not None:
            result['DefaultResourceDiscoveryId'] = self.default_resource_discovery_id
        if self.ipam_id is not None:
            result['IpamId'] = self.ipam_id
        if self.private_default_scope_id is not None:
            result['PrivateDefaultScopeId'] = self.private_default_scope_id
        if self.public_default_scope_id is not None:
            result['PublicDefaultScopeId'] = self.public_default_scope_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_discovery_association_count is not None:
            result['ResourceDiscoveryAssociationCount'] = self.resource_discovery_association_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultResourceDiscoveryAssociationId') is not None:
            self.default_resource_discovery_association_id = m.get('DefaultResourceDiscoveryAssociationId')
        if m.get('DefaultResourceDiscoveryId') is not None:
            self.default_resource_discovery_id = m.get('DefaultResourceDiscoveryId')
        if m.get('IpamId') is not None:
            self.ipam_id = m.get('IpamId')
        if m.get('PrivateDefaultScopeId') is not None:
            self.private_default_scope_id = m.get('PrivateDefaultScopeId')
        if m.get('PublicDefaultScopeId') is not None:
            self.public_default_scope_id = m.get('PublicDefaultScopeId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceDiscoveryAssociationCount') is not None:
            self.resource_discovery_association_count = m.get('ResourceDiscoveryAssociationCount')
        return self


class CreateIpamResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateIpamResponseBody = None,
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
            temp_model = CreateIpamResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateIpamPoolRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key. You can specify at most 20 tag keys. The tag key cannot be an empty string.
        # 
        # The tag key can be up to 64 characters in length and can contain letters, digits, periods (.), underscores (_), and hyphens (-). The tag key must start with a letter but cannot start with `aliyun` or `acs:`. The tag key cannot contain `http://` or `https://`.
        self.key = key
        # The tag value. You can specify up to 20 tag values. The tag value can be an empty string.
        # 
        # The tag value can be up to 128 characters in length and can contain letters, digits, periods (.), underscores (_), and hyphens (-). It cannot start with a `aliyun` or `acs:`, and cannot contain `http://` or `https://`.
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


class CreateIpamPoolRequest(TeaModel):
    def __init__(
        self,
        allocation_default_cidr_mask: int = None,
        allocation_max_cidr_mask: int = None,
        allocation_min_cidr_mask: int = None,
        auto_import: bool = None,
        client_token: str = None,
        dry_run: bool = None,
        ip_version: str = None,
        ipam_pool_description: str = None,
        ipam_pool_name: str = None,
        ipam_scope_id: str = None,
        ipv_6isp: str = None,
        owner_account: str = None,
        owner_id: int = None,
        pool_region_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        source_ipam_pool_id: str = None,
        tag: List[CreateIpamPoolRequestTag] = None,
    ):
        # The default network mask assigned by the IPAM address pool.  
        # 
        # > The IPv4 network mask value range is 0 to 32 bits, and the IPv6 network mask value range is 0 to 128 bits.
        self.allocation_default_cidr_mask = allocation_default_cidr_mask
        # The maximum network mask assigned by the IPAM address pool.  
        # > The IPv4 network mask value range is **0 to 32** bits, and the IPv6 network mask value range is **0 to 128** bits.
        self.allocation_max_cidr_mask = allocation_max_cidr_mask
        # The minimum network mask assigned by the IPAM address pool.  
        # > The IPv4 network mask value range is **0 to 32** bits, and the IPv6 network mask value range is **0 to 128** bits.
        self.allocation_min_cidr_mask = allocation_min_cidr_mask
        # Whether the pool has the auto-import feature enabled.
        self.auto_import = auto_import
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The client token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the request ID as the client token. The request ID may be different for each request.
        self.client_token = client_token
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the DryRunOperation error code is returned.
        # *   **false** (default): performs a dry run and performs the actual request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run
        # IP address protocol version. Values:
        # - **IPv4**: IPv4 protocol.
        # - **IPv6**: IPv6 protocol.
        self.ip_version = ip_version
        # Description of the IPAM address pool. 
        # The length should be between 1 to 256 characters, and it must start with an uppercase or lowercase English letter or a Chinese character, but cannot begin with `http://` or `https://`. If left blank, the default value is empty.
        self.ipam_pool_description = ipam_pool_description
        # The name of the IPAM pool.
        # 
        # It must be 1 to 128 characters in length and cannot start with `http://` or `https://`.
        self.ipam_pool_name = ipam_pool_name
        # The ID of the IPAM scope.
        # 
        # This parameter is required.
        self.ipam_scope_id = ipam_scope_id
        # The type of the IPv6 CIDR block of the VPC. Valid values:
        # 
        # *   **BGP** (default)
        # *   **ChinaMobile**\
        # *   **ChinaUnicom**\
        # *   **ChinaTelecom**\
        # 
        # >  If you are allowed to use single-ISP bandwidth, you can set the value to **ChinaTelecom**, **ChinaUnicom**, or **ChinaMobile**.
        self.ipv_6isp = ipv_6isp
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The effective region of the IPAM pool.
        self.pool_region_id = pool_region_id
        # The ID of the region where the IPAM instance is hosted. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the source IPAM pool.
        # 
        # >  If you do not specify this parameter, the pool is a parent pool.
        self.source_ipam_pool_id = source_ipam_pool_id
        # The tag list.
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
        if self.allocation_default_cidr_mask is not None:
            result['AllocationDefaultCidrMask'] = self.allocation_default_cidr_mask
        if self.allocation_max_cidr_mask is not None:
            result['AllocationMaxCidrMask'] = self.allocation_max_cidr_mask
        if self.allocation_min_cidr_mask is not None:
            result['AllocationMinCidrMask'] = self.allocation_min_cidr_mask
        if self.auto_import is not None:
            result['AutoImport'] = self.auto_import
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version
        if self.ipam_pool_description is not None:
            result['IpamPoolDescription'] = self.ipam_pool_description
        if self.ipam_pool_name is not None:
            result['IpamPoolName'] = self.ipam_pool_name
        if self.ipam_scope_id is not None:
            result['IpamScopeId'] = self.ipam_scope_id
        if self.ipv_6isp is not None:
            result['Ipv6Isp'] = self.ipv_6isp
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pool_region_id is not None:
            result['PoolRegionId'] = self.pool_region_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.source_ipam_pool_id is not None:
            result['SourceIpamPoolId'] = self.source_ipam_pool_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocationDefaultCidrMask') is not None:
            self.allocation_default_cidr_mask = m.get('AllocationDefaultCidrMask')
        if m.get('AllocationMaxCidrMask') is not None:
            self.allocation_max_cidr_mask = m.get('AllocationMaxCidrMask')
        if m.get('AllocationMinCidrMask') is not None:
            self.allocation_min_cidr_mask = m.get('AllocationMinCidrMask')
        if m.get('AutoImport') is not None:
            self.auto_import = m.get('AutoImport')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')
        if m.get('IpamPoolDescription') is not None:
            self.ipam_pool_description = m.get('IpamPoolDescription')
        if m.get('IpamPoolName') is not None:
            self.ipam_pool_name = m.get('IpamPoolName')
        if m.get('IpamScopeId') is not None:
            self.ipam_scope_id = m.get('IpamScopeId')
        if m.get('Ipv6Isp') is not None:
            self.ipv_6isp = m.get('Ipv6Isp')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PoolRegionId') is not None:
            self.pool_region_id = m.get('PoolRegionId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SourceIpamPoolId') is not None:
            self.source_ipam_pool_id = m.get('SourceIpamPoolId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateIpamPoolRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class CreateIpamPoolResponseBody(TeaModel):
    def __init__(
        self,
        ipam_pool_id: str = None,
        request_id: str = None,
    ):
        # The ID of the IPAM pool.
        self.ipam_pool_id = ipam_pool_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ipam_pool_id is not None:
            result['IpamPoolId'] = self.ipam_pool_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpamPoolId') is not None:
            self.ipam_pool_id = m.get('IpamPoolId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateIpamPoolResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateIpamPoolResponseBody = None,
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
            temp_model = CreateIpamPoolResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateIpamPoolAllocationRequest(TeaModel):
    def __init__(
        self,
        cidr: str = None,
        cidr_mask: int = None,
        client_token: str = None,
        dry_run: bool = None,
        ipam_pool_allocation_description: str = None,
        ipam_pool_allocation_name: str = None,
        ipam_pool_id: str = None,
        region_id: str = None,
    ):
        # Enter a CIDR block to reserve a custom CIDR block.
        # 
        # **Usage notes** Specify at least one of **Cidr** and **CidrMask** .
        self.cidr = cidr
        # Enter a mask to reserve a custom CIDR block.
        # 
        # **Usage notes** Specify at least one of **Cidr** and **CidrMask** .
        self.cidr_mask = cidr_mask
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The client token can contain only ASCII characters.
        # 
        # **Usage notes** If you do not specify this parameter, the system automatically uses the request ID as the client token. The request ID may be different for each request.
        self.client_token = client_token
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the DryRunOperation error code is returned.
        # *   **false** (default): performs a dry run and performs the actual request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The description of the allocation.
        self.ipam_pool_allocation_description = ipam_pool_allocation_description
        # The name of the allocation.
        self.ipam_pool_allocation_name = ipam_pool_allocation_name
        # The ID of the IPAM pool.
        # 
        # This parameter is required.
        self.ipam_pool_id = ipam_pool_id
        # The region ID of the custom CIDR block that you want to reserve.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the most recent region list.
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
        if self.cidr is not None:
            result['Cidr'] = self.cidr
        if self.cidr_mask is not None:
            result['CidrMask'] = self.cidr_mask
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.ipam_pool_allocation_description is not None:
            result['IpamPoolAllocationDescription'] = self.ipam_pool_allocation_description
        if self.ipam_pool_allocation_name is not None:
            result['IpamPoolAllocationName'] = self.ipam_pool_allocation_name
        if self.ipam_pool_id is not None:
            result['IpamPoolId'] = self.ipam_pool_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cidr') is not None:
            self.cidr = m.get('Cidr')
        if m.get('CidrMask') is not None:
            self.cidr_mask = m.get('CidrMask')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IpamPoolAllocationDescription') is not None:
            self.ipam_pool_allocation_description = m.get('IpamPoolAllocationDescription')
        if m.get('IpamPoolAllocationName') is not None:
            self.ipam_pool_allocation_name = m.get('IpamPoolAllocationName')
        if m.get('IpamPoolId') is not None:
            self.ipam_pool_id = m.get('IpamPoolId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateIpamPoolAllocationResponseBody(TeaModel):
    def __init__(
        self,
        cidr: str = None,
        ipam_pool_allocation_id: str = None,
        request_id: str = None,
        source_cidr: str = None,
    ):
        # The custom reserved CIDR block.
        self.cidr = cidr
        # The ID of the custom reserved CIDR block.
        self.ipam_pool_allocation_id = ipam_pool_allocation_id
        # The request ID.
        self.request_id = request_id
        # The source CIDR block.
        self.source_cidr = source_cidr

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cidr is not None:
            result['Cidr'] = self.cidr
        if self.ipam_pool_allocation_id is not None:
            result['IpamPoolAllocationId'] = self.ipam_pool_allocation_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.source_cidr is not None:
            result['SourceCidr'] = self.source_cidr
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cidr') is not None:
            self.cidr = m.get('Cidr')
        if m.get('IpamPoolAllocationId') is not None:
            self.ipam_pool_allocation_id = m.get('IpamPoolAllocationId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SourceCidr') is not None:
            self.source_cidr = m.get('SourceCidr')
        return self


class CreateIpamPoolAllocationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateIpamPoolAllocationResponseBody = None,
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
            temp_model = CreateIpamPoolAllocationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateIpamResourceDiscoveryRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag keys. You can specify at most 20 tag keys. It cannot be an empty string.
        # 
        # The tag key can be up to 64 characters in length and can contain letters, digits, periods (.), underscores (_), and hyphens (-). It must start with a letter but cannot start with `aliyun` or `acs:`. It cannot contain `http://` or `https://`.
        self.key = key
        # The tag value of the resource. You can specify up to 20 tag values. You can specify empty strings as tag values.
        # 
        # The tag value can be up to 128 characters in length and cannot contain `http://` or `https://`.
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


class CreateIpamResourceDiscoveryRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        ipam_resource_discovery_description: str = None,
        ipam_resource_discovery_name: str = None,
        operating_region_list: List[str] = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        tag: List[CreateIpamResourceDiscoveryRequestTag] = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The client token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the request ID as the client token. The request ID may be different for each request.
        self.client_token = client_token
        # Specifies whether to perform a dry run, without sending the actual request. Valid value:
        # 
        # *   **true**: Performs the dry run without creating a custom resource discovery instance. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error code is returned. If the request passes the dry run, the DryRunOperation error code is returned.
        # *   **false** (default): Performs a dry run and the actual request. If the request passes the dry run, an HTTP 2xx status code is returned and a custom resource discovery instance is created.
        self.dry_run = dry_run
        # The description of resource discovery.
        self.ipam_resource_discovery_description = ipam_resource_discovery_description
        # The name of the resource discovery.
        self.ipam_resource_discovery_name = ipam_resource_discovery_name
        # The list of effective regions.
        # 
        # This parameter is required.
        self.operating_region_list = operating_region_list
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The request region.
        # 
        # >  The request region is the hosted region of the resource discovery instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The tag information.
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
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.ipam_resource_discovery_description is not None:
            result['IpamResourceDiscoveryDescription'] = self.ipam_resource_discovery_description
        if self.ipam_resource_discovery_name is not None:
            result['IpamResourceDiscoveryName'] = self.ipam_resource_discovery_name
        if self.operating_region_list is not None:
            result['OperatingRegionList'] = self.operating_region_list
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IpamResourceDiscoveryDescription') is not None:
            self.ipam_resource_discovery_description = m.get('IpamResourceDiscoveryDescription')
        if m.get('IpamResourceDiscoveryName') is not None:
            self.ipam_resource_discovery_name = m.get('IpamResourceDiscoveryName')
        if m.get('OperatingRegionList') is not None:
            self.operating_region_list = m.get('OperatingRegionList')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateIpamResourceDiscoveryRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class CreateIpamResourceDiscoveryResponseBody(TeaModel):
    def __init__(
        self,
        ipam_resource_discovery_id: str = None,
        request_id: str = None,
    ):
        # The ID of the instance for resource discovery.
        self.ipam_resource_discovery_id = ipam_resource_discovery_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ipam_resource_discovery_id is not None:
            result['IpamResourceDiscoveryId'] = self.ipam_resource_discovery_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpamResourceDiscoveryId') is not None:
            self.ipam_resource_discovery_id = m.get('IpamResourceDiscoveryId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateIpamResourceDiscoveryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateIpamResourceDiscoveryResponseBody = None,
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
            temp_model = CreateIpamResourceDiscoveryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateIpamScopeRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the resource. You can specify at most 20 tag keys. It cannot be an empty string.
        # 
        # The tag key can be up to 64 characters in length and can contain letters, digits, periods (.), underscores (_), and hyphens (-). It must start with a letter but cannot start with `aliyun` or `acs:`. It cannot contain `http://` or `https://`.
        self.key = key
        # The tag value of the resource. You can specify up to 20 tag values. You can specify empty strings as tag values.
        # 
        # The tag value can be up to 128 characters in length and cannot contain `http://` or `https://`.
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


class CreateIpamScopeRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        ipam_id: str = None,
        ipam_scope_description: str = None,
        ipam_scope_name: str = None,
        ipam_scope_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        tag: List[CreateIpamScopeRequestTag] = None,
    ):
        # The client token used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The client token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the request ID as the client token. The request ID may be different for each request.
        self.client_token = client_token
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run. The system checks the request for potential issues, including invalid AccessKey pairs, unauthorized RAM users, and missing parameter values. If the request fails the dry run, an error code is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false**: performs a dry run and the actual request. After the request passes the dry run, a 2xx HTTP status code is returned and the IPAM scope is created.
        self.dry_run = dry_run
        # The ID of the IPAM.
        # 
        # This parameter is required.
        self.ipam_id = ipam_id
        # The description of the IPAM scope.
        # 
        # It must be 1 to 256 characters in length. It must start with a letter but cannot start with `http://` or `https://`. This parameter is empty by default.
        self.ipam_scope_description = ipam_scope_description
        # The name of the IPAM scope.
        # 
        # It must be 1 to 128 characters in length and cannot start with `http://` or `https://`.
        self.ipam_scope_name = ipam_scope_name
        # The type of IPAM scope: **private**\
        # 
        # 
        # **Usage notes** You can create only private IPAM scopes.
        self.ipam_scope_type = ipam_scope_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the region where the IPAM instance is hosted. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource group ID of the IPAM scope.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The tag list.
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
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.ipam_id is not None:
            result['IpamId'] = self.ipam_id
        if self.ipam_scope_description is not None:
            result['IpamScopeDescription'] = self.ipam_scope_description
        if self.ipam_scope_name is not None:
            result['IpamScopeName'] = self.ipam_scope_name
        if self.ipam_scope_type is not None:
            result['IpamScopeType'] = self.ipam_scope_type
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IpamId') is not None:
            self.ipam_id = m.get('IpamId')
        if m.get('IpamScopeDescription') is not None:
            self.ipam_scope_description = m.get('IpamScopeDescription')
        if m.get('IpamScopeName') is not None:
            self.ipam_scope_name = m.get('IpamScopeName')
        if m.get('IpamScopeType') is not None:
            self.ipam_scope_type = m.get('IpamScopeType')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateIpamScopeRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class CreateIpamScopeResponseBody(TeaModel):
    def __init__(
        self,
        ipam_scope_id: str = None,
        request_id: str = None,
    ):
        # The ID of the IPAM scope.
        self.ipam_scope_id = ipam_scope_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ipam_scope_id is not None:
            result['IpamScopeId'] = self.ipam_scope_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpamScopeId') is not None:
            self.ipam_scope_id = m.get('IpamScopeId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateIpamScopeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateIpamScopeResponseBody = None,
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
            temp_model = CreateIpamScopeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteIpamRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        ipam_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The client token can contain only ASCII characters.
        # 
        # **\
        # 
        # **Usage notes** If you do not specify this parameter, the system automatically uses the request ID as the client token. The request ID may be different for each request.
        self.client_token = client_token
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the DryRunOperation error code is returned.
        # *   **false** (default): performs a dry run and performs the actual request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The ID of the IPAM.
        # 
        # This parameter is required.
        self.ipam_id = ipam_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the region where the IPAM instance is hosted. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.ipam_id is not None:
            result['IpamId'] = self.ipam_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IpamId') is not None:
            self.ipam_id = m.get('IpamId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DeleteIpamResponseBody(TeaModel):
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


class DeleteIpamResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteIpamResponseBody = None,
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
            temp_model = DeleteIpamResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteIpamPoolRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        ipam_pool_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The client token can contain only ASCII characters.
        # 
        # **\
        # 
        # **Usage notes** If you do not specify this parameter, the system automatically uses the request ID as the client token. The request ID may be different for each request.
        self.client_token = client_token
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, DryRunOperation is returned.
        # *   **false** (default): performs a dry run and performs the actual request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The ID of the IPAM pool.
        # 
        # This parameter is required.
        self.ipam_pool_id = ipam_pool_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the region where the IPAM instance is hosted. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.ipam_pool_id is not None:
            result['IpamPoolId'] = self.ipam_pool_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IpamPoolId') is not None:
            self.ipam_pool_id = m.get('IpamPoolId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DeleteIpamPoolResponseBody(TeaModel):
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


class DeleteIpamPoolResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteIpamPoolResponseBody = None,
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
            temp_model = DeleteIpamPoolResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteIpamPoolAllocationRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        ipam_pool_allocation_id: str = None,
        region_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The client token can contain only ASCII characters.
        # 
        # **Usage notes** If you do not specify this parameter, the system automatically uses the request ID as the client token. The request ID may be different for each request.
        self.client_token = client_token
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the DryRunOperation error code is returned.
        # *   **false** (default): sends the API request. If the request passes the check, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The ID of the custom reserved CIDR block to be deleted.
        # 
        # This parameter is required.
        self.ipam_pool_allocation_id = ipam_pool_allocation_id
        # The region ID of the custom reserved CIDR block.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the most recent region list.
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
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.ipam_pool_allocation_id is not None:
            result['IpamPoolAllocationId'] = self.ipam_pool_allocation_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IpamPoolAllocationId') is not None:
            self.ipam_pool_allocation_id = m.get('IpamPoolAllocationId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteIpamPoolAllocationResponseBody(TeaModel):
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


class DeleteIpamPoolAllocationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteIpamPoolAllocationResponseBody = None,
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
            temp_model = DeleteIpamPoolAllocationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteIpamPoolCidrRequest(TeaModel):
    def __init__(
        self,
        cidr: str = None,
        client_token: str = None,
        dry_run: bool = None,
        ipam_pool_id: str = None,
        region_id: str = None,
    ):
        # The provisioned CIDR block to be deleted.
        # 
        # >  Only IPv4 CIDR blocks are supported.
        # 
        # This parameter is required.
        self.cidr = cidr
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The client token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the request ID as the client token. The request ID may be different for each request.
        self.client_token = client_token
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the DryRunOperation error code is returned.
        # *   **false** (default): performs a dry run and performs the actual request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The ID of the IPAM pool.
        # 
        # This parameter is required.
        self.ipam_pool_id = ipam_pool_id
        # The ID of the region where the IPAM instance is hosted.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the most recent region list.
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
        if self.cidr is not None:
            result['Cidr'] = self.cidr
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.ipam_pool_id is not None:
            result['IpamPoolId'] = self.ipam_pool_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cidr') is not None:
            self.cidr = m.get('Cidr')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IpamPoolId') is not None:
            self.ipam_pool_id = m.get('IpamPoolId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteIpamPoolCidrResponseBody(TeaModel):
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


class DeleteIpamPoolCidrResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteIpamPoolCidrResponseBody = None,
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
            temp_model = DeleteIpamPoolCidrResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteIpamResourceDiscoveryRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        ipam_resource_discovery_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The client token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the request ID as the client token. The request ID may be different for each request.
        self.client_token = client_token
        # Specifies whether to perform the dry run. Valid values:
        # 
        # *   **true**: Performs a dry run without deleting the resource discovery instance. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error code is returned. If the request passes the dry run, the DryRunOperation error code is returned.
        # *   **false** (default): Performs a dry run and the actual request. If the request passes the check, an HTTP 2xx status code is returned and the resource discovery instance is deleted.
        self.dry_run = dry_run
        # The ID of resource discovery instance.
        # 
        # This parameter is required.
        self.ipam_resource_discovery_id = ipam_resource_discovery_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The request region.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.ipam_resource_discovery_id is not None:
            result['IpamResourceDiscoveryId'] = self.ipam_resource_discovery_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IpamResourceDiscoveryId') is not None:
            self.ipam_resource_discovery_id = m.get('IpamResourceDiscoveryId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DeleteIpamResourceDiscoveryResponseBody(TeaModel):
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


class DeleteIpamResourceDiscoveryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteIpamResourceDiscoveryResponseBody = None,
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
            temp_model = DeleteIpamResourceDiscoveryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteIpamScopeRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        ipam_scope_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The client token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the request ID as the client token. The request ID may be different for each request.
        self.client_token = client_token
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error message is returned. If the request passes the precheck, the `DryRunOperation` error code is returned.
        # *   **false** (default): performs a dry run and performs the actual request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The ID of the IPAM scope.
        # 
        # This parameter is required.
        self.ipam_scope_id = ipam_scope_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the region where the IPAM instance is hosted. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.ipam_scope_id is not None:
            result['IpamScopeId'] = self.ipam_scope_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IpamScopeId') is not None:
            self.ipam_scope_id = m.get('IpamScopeId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DeleteIpamScopeResponseBody(TeaModel):
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


class DeleteIpamScopeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteIpamScopeResponseBody = None,
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
            temp_model = DeleteIpamScopeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DissociateIpamResourceDiscoveryRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        ipam_id: str = None,
        ipam_resource_discovery_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The client token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the request ID as the client token. The request ID may be different for each request.
        self.client_token = client_token
        # Specifies whether to perform a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: Performs a dry run without disassociating the resource discovery and IPAM instance. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error code is returned. If the request passes the dry run, the DryRunOperation error code is returned.
        # *   **false** (default): Performs a dry run and sends the request. After the request passes the check, an HTTP 2xx status code is returned and the resource discovery and IPAM instances are disassociated.
        self.dry_run = dry_run
        # The ID of the IPAM.
        # 
        # This parameter is required.
        self.ipam_id = ipam_id
        # The ID of the resource discovery instance.
        # 
        # This parameter is required.
        self.ipam_resource_discovery_id = ipam_resource_discovery_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The request region.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.ipam_id is not None:
            result['IpamId'] = self.ipam_id
        if self.ipam_resource_discovery_id is not None:
            result['IpamResourceDiscoveryId'] = self.ipam_resource_discovery_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IpamId') is not None:
            self.ipam_id = m.get('IpamId')
        if m.get('IpamResourceDiscoveryId') is not None:
            self.ipam_resource_discovery_id = m.get('IpamResourceDiscoveryId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DissociateIpamResourceDiscoveryResponseBody(TeaModel):
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


class DissociateIpamResourceDiscoveryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DissociateIpamResourceDiscoveryResponseBody = None,
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
            temp_model = DissociateIpamResourceDiscoveryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetIpamPoolAllocationRequest(TeaModel):
    def __init__(
        self,
        ipam_pool_allocation_id: str = None,
        region_id: str = None,
    ):
        # The ID of the instance to which CIDR blocks are allocated from the IPAM pool.
        # 
        # This parameter is required.
        self.ipam_pool_allocation_id = ipam_pool_allocation_id
        # The region of the IPAM pool.
        # 
        # >  If the IPAM pool to which CIDR allocation belongs has the region attribute, this parameter is the region of the IPAM pool. If not, this parameter is the IPAM hosted region.
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
        if self.ipam_pool_allocation_id is not None:
            result['IpamPoolAllocationId'] = self.ipam_pool_allocation_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpamPoolAllocationId') is not None:
            self.ipam_pool_allocation_id = m.get('IpamPoolAllocationId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetIpamPoolAllocationResponseBody(TeaModel):
    def __init__(
        self,
        cidr: str = None,
        creation_time: str = None,
        ipam_pool_allocation_description: str = None,
        ipam_pool_allocation_id: str = None,
        ipam_pool_allocation_name: str = None,
        ipam_pool_id: str = None,
        region_id: str = None,
        request_id: str = None,
        resource_id: str = None,
        resource_owner_id: int = None,
        resource_region_id: str = None,
        resource_type: str = None,
        source_cidr: str = None,
        status: str = None,
    ):
        # The allocated CIDR block.
        self.cidr = cidr
        # The time when the instance was created.
        self.creation_time = creation_time
        # The description of the CIDR allocation of the IPAM pool.
        # 
        # The description must be 1 to 256 characters in length and start with a letter, but cannot start with a `http://` or `https://`. This parameter is empty by default.
        self.ipam_pool_allocation_description = ipam_pool_allocation_description
        # The ID of the instance to which CIDR blocks are allocated from the IPAM pool.
        self.ipam_pool_allocation_id = ipam_pool_allocation_id
        # The name of the CIDR allocation of the IPAM pool.
        # 
        # It must be 1 to 128 characters in length and cannot start with `http://` or `https://`.
        self.ipam_pool_allocation_name = ipam_pool_allocation_name
        # The ID of the IPAM pool.
        self.ipam_pool_id = ipam_pool_id
        # The region of the IPAM pool.
        # 
        # >  If the IPAM pool to which the CIDR block allocation belongs has the region attribute, this parameter is the region of the IPAM pool. If not, this parameter is the IPAM hosted region.
        self.region_id = region_id
        # The request ID.
        self.request_id = request_id
        # The ID of the resource to which the CIDR block is allocated.
        self.resource_id = resource_id
        # The ID of the Alibaba Cloud account to which the resource belongs.
        self.resource_owner_id = resource_owner_id
        # The effective region ID of the resource.
        self.resource_region_id = resource_region_id
        # The type of the resource to which the CIDR block is allocated. Valid values:
        # 
        # *   **VPC**\
        # *   **IpamPool**\
        # *   **Custom**\
        self.resource_type = resource_type
        # The source CIDR block.
        self.source_cidr = source_cidr
        # The instance state. Valid values:
        # 
        # *   **Created**\
        # *   **Deleted**\
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cidr is not None:
            result['Cidr'] = self.cidr
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.ipam_pool_allocation_description is not None:
            result['IpamPoolAllocationDescription'] = self.ipam_pool_allocation_description
        if self.ipam_pool_allocation_id is not None:
            result['IpamPoolAllocationId'] = self.ipam_pool_allocation_id
        if self.ipam_pool_allocation_name is not None:
            result['IpamPoolAllocationName'] = self.ipam_pool_allocation_name
        if self.ipam_pool_id is not None:
            result['IpamPoolId'] = self.ipam_pool_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.resource_region_id is not None:
            result['ResourceRegionId'] = self.resource_region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.source_cidr is not None:
            result['SourceCidr'] = self.source_cidr
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cidr') is not None:
            self.cidr = m.get('Cidr')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('IpamPoolAllocationDescription') is not None:
            self.ipam_pool_allocation_description = m.get('IpamPoolAllocationDescription')
        if m.get('IpamPoolAllocationId') is not None:
            self.ipam_pool_allocation_id = m.get('IpamPoolAllocationId')
        if m.get('IpamPoolAllocationName') is not None:
            self.ipam_pool_allocation_name = m.get('IpamPoolAllocationName')
        if m.get('IpamPoolId') is not None:
            self.ipam_pool_id = m.get('IpamPoolId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ResourceRegionId') is not None:
            self.resource_region_id = m.get('ResourceRegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('SourceCidr') is not None:
            self.source_cidr = m.get('SourceCidr')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetIpamPoolAllocationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetIpamPoolAllocationResponseBody = None,
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
            temp_model = GetIpamPoolAllocationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetIpamPoolNextAvailableCidrRequest(TeaModel):
    def __init__(
        self,
        cidr_block: str = None,
        cidr_mask: int = None,
        client_token: str = None,
        ipam_pool_id: str = None,
        region_id: str = None,
    ):
        # CIDR to be allocated.
        # 
        # >  You must enter at least one of the CidrBlock and CidrMask fields.
        self.cidr_block = cidr_block
        # The length of the CIDR mask to be allocated.
        # 
        # >  You must enter at least one of the CidrBlock and CidrMask fields.
        self.cidr_mask = cidr_mask
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The client token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the request ID as the client token. The request ID may be different for each request.
        self.client_token = client_token
        # The ID of the IPAM pool.
        # 
        # This parameter is required.
        self.ipam_pool_id = ipam_pool_id
        # The region of the IPAM pool.
        # 
        # >  If the IPAM pool has the region attribute, this parameter is set to the effective region of the IPAM pool. If not, this is set to the hosted region.
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
        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block
        if self.cidr_mask is not None:
            result['CidrMask'] = self.cidr_mask
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.ipam_pool_id is not None:
            result['IpamPoolId'] = self.ipam_pool_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')
        if m.get('CidrMask') is not None:
            self.cidr_mask = m.get('CidrMask')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('IpamPoolId') is not None:
            self.ipam_pool_id = m.get('IpamPoolId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetIpamPoolNextAvailableCidrResponseBody(TeaModel):
    def __init__(
        self,
        cidr_block: str = None,
        request_id: str = None,
    ):
        # Available CIDR.
        self.cidr_block = cidr_block
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetIpamPoolNextAvailableCidrResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetIpamPoolNextAvailableCidrResponseBody = None,
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
            temp_model = GetIpamPoolNextAvailableCidrResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetVpcIpamServiceStatusRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The client token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the region where the IPAM instance is hosted.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class GetVpcIpamServiceStatusResponseBody(TeaModel):
    def __init__(
        self,
        enabled: bool = None,
        request_id: str = None,
    ):
        # Indicates whether IPAM is activated.
        # 
        # *   **true**\
        # *   **false**\
        self.enabled = enabled
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetVpcIpamServiceStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetVpcIpamServiceStatusResponseBody = None,
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
            temp_model = GetVpcIpamServiceStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListIpamDiscoveredResourceRequest(TeaModel):
    def __init__(
        self,
        ipam_resource_discovery_id: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        resource_region_id: str = None,
        resource_type: str = None,
    ):
        # The ID of the resource discovery instance.
        # 
        # This parameter is required.
        self.ipam_resource_discovery_id = ipam_resource_discovery_id
        # The maximum number of entries on each page. Valid values: 1 to 100. Default value: 10.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   You do not need to specify this parameter for the first request.
        # *   You must specify the token that is obtained from the previous query as the value of **NextToken**.
        self.next_token = next_token
        # The ID of the hosted region of the IPAM pool.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The region where resource discovery is performed.
        # 
        # This parameter is required.
        self.resource_region_id = resource_region_id
        # The resource type. Valid values:
        # 
        # *   **VPC**\
        # *   **VSwitch**\
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ipam_resource_discovery_id is not None:
            result['IpamResourceDiscoveryId'] = self.ipam_resource_discovery_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_region_id is not None:
            result['ResourceRegionId'] = self.resource_region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpamResourceDiscoveryId') is not None:
            self.ipam_resource_discovery_id = m.get('IpamResourceDiscoveryId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceRegionId') is not None:
            self.resource_region_id = m.get('ResourceRegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class ListIpamDiscoveredResourceResponseBodyIpamDiscoveredResourcesIpCountDetail(TeaModel):
    def __init__(
        self,
        free_ip_count: str = None,
        total_ip_count: str = None,
        used_ip_count: str = None,
    ):
        self.free_ip_count = free_ip_count
        self.total_ip_count = total_ip_count
        self.used_ip_count = used_ip_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.free_ip_count is not None:
            result['FreeIpCount'] = self.free_ip_count
        if self.total_ip_count is not None:
            result['TotalIpCount'] = self.total_ip_count
        if self.used_ip_count is not None:
            result['UsedIpCount'] = self.used_ip_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FreeIpCount') is not None:
            self.free_ip_count = m.get('FreeIpCount')
        if m.get('TotalIpCount') is not None:
            self.total_ip_count = m.get('TotalIpCount')
        if m.get('UsedIpCount') is not None:
            self.used_ip_count = m.get('UsedIpCount')
        return self


class ListIpamDiscoveredResourceResponseBodyIpamDiscoveredResources(TeaModel):
    def __init__(
        self,
        ali_uid: int = None,
        cidr: str = None,
        discovery_time: str = None,
        ip_count_detail: ListIpamDiscoveredResourceResponseBodyIpamDiscoveredResourcesIpCountDetail = None,
        ip_usage: str = None,
        ipam_resource_discovery_id: str = None,
        resource_id: str = None,
        resource_owner_id: int = None,
        resource_region_id: str = None,
        resource_type: str = None,
        source_cidr: str = None,
        vpc_id: str = None,
    ):
        # The ID of the Alibaba Cloud account.
        self.ali_uid = ali_uid
        # The CIDR block of the resource.
        self.cidr = cidr
        # The time when the resource was discovered.
        # 
        # >  If the resource has not been modified since it was created, the discovery time remains unchanged.
        self.discovery_time = discovery_time
        self.ip_count_detail = ip_count_detail
        # The IP usage in decimal form.
        self.ip_usage = ip_usage
        # The ID of resource discovery instance.
        self.ipam_resource_discovery_id = ipam_resource_discovery_id
        # The ID of the resource.
        self.resource_id = resource_id
        # The ID of the Alibaba Cloud account to which the resource belongs.
        self.resource_owner_id = resource_owner_id
        # The ID of the region to which the resource belongs.
        self.resource_region_id = resource_region_id
        # The resource type. Valid values:
        # 
        # *   **VPC**\
        # *   **VSwitch**\
        self.resource_type = resource_type
        # The source CIDR block.
        self.source_cidr = source_cidr
        # The ID of the VPC to which the resource belongs.
        self.vpc_id = vpc_id

    def validate(self):
        if self.ip_count_detail:
            self.ip_count_detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.cidr is not None:
            result['Cidr'] = self.cidr
        if self.discovery_time is not None:
            result['DiscoveryTime'] = self.discovery_time
        if self.ip_count_detail is not None:
            result['IpCountDetail'] = self.ip_count_detail.to_map()
        if self.ip_usage is not None:
            result['IpUsage'] = self.ip_usage
        if self.ipam_resource_discovery_id is not None:
            result['IpamResourceDiscoveryId'] = self.ipam_resource_discovery_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.resource_region_id is not None:
            result['ResourceRegionId'] = self.resource_region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.source_cidr is not None:
            result['SourceCidr'] = self.source_cidr
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('Cidr') is not None:
            self.cidr = m.get('Cidr')
        if m.get('DiscoveryTime') is not None:
            self.discovery_time = m.get('DiscoveryTime')
        if m.get('IpCountDetail') is not None:
            temp_model = ListIpamDiscoveredResourceResponseBodyIpamDiscoveredResourcesIpCountDetail()
            self.ip_count_detail = temp_model.from_map(m['IpCountDetail'])
        if m.get('IpUsage') is not None:
            self.ip_usage = m.get('IpUsage')
        if m.get('IpamResourceDiscoveryId') is not None:
            self.ipam_resource_discovery_id = m.get('IpamResourceDiscoveryId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ResourceRegionId') is not None:
            self.resource_region_id = m.get('ResourceRegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('SourceCidr') is not None:
            self.source_cidr = m.get('SourceCidr')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class ListIpamDiscoveredResourceResponseBody(TeaModel):
    def __init__(
        self,
        count: int = None,
        ipam_discovered_resources: List[ListIpamDiscoveredResourceResponseBodyIpamDiscoveredResources] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The maximum number of entries on each page.
        self.count = count
        # The list of resources.
        self.ipam_discovered_resources = ipam_discovered_resources
        # The maximum number of entries on each page. Valid values: 1 to 100. Default value: 10.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If **NextToken** is empty, there is no next page.
        # *   If a value of **NextToken** is returned, it indicates the token that is used for the next query.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.ipam_discovered_resources:
            for k in self.ipam_discovered_resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        result['IpamDiscoveredResources'] = []
        if self.ipam_discovered_resources is not None:
            for k in self.ipam_discovered_resources:
                result['IpamDiscoveredResources'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        self.ipam_discovered_resources = []
        if m.get('IpamDiscoveredResources') is not None:
            for k in m.get('IpamDiscoveredResources'):
                temp_model = ListIpamDiscoveredResourceResponseBodyIpamDiscoveredResources()
                self.ipam_discovered_resources.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListIpamDiscoveredResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListIpamDiscoveredResourceResponseBody = None,
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
            temp_model = ListIpamDiscoveredResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListIpamPoolAllocationsRequest(TeaModel):
    def __init__(
        self,
        cidr: str = None,
        ipam_pool_allocation_ids: List[str] = None,
        ipam_pool_allocation_name: str = None,
        ipam_pool_id: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
    ):
        # Specifies whether to query allocations by specifying allocated CIDR blocks.
        # 
        # **\
        # 
        # **Usage notes** Only IPv4 CIDR blocks are supported.
        self.cidr = cidr
        # The IDs of the instances to which CIDR blocks are allocated from the IPAM pool.
        self.ipam_pool_allocation_ids = ipam_pool_allocation_ids
        # The name of  allocations.
        self.ipam_pool_allocation_name = ipam_pool_allocation_name
        # The ID of the IPAM pool.
        # 
        # This parameter is required.
        self.ipam_pool_id = ipam_pool_id
        # The number of entries per page. Valid values: **1** to **100**. Default value: **10**.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If **NextToken** is empty, no next page exists.
        # *   If a value of **NextToken** is returned, the value indicates the token that is used for the next query.
        self.next_token = next_token
        # The ID of the region where you want to perform the operation.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the most recent region list.
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
        if self.cidr is not None:
            result['Cidr'] = self.cidr
        if self.ipam_pool_allocation_ids is not None:
            result['IpamPoolAllocationIds'] = self.ipam_pool_allocation_ids
        if self.ipam_pool_allocation_name is not None:
            result['IpamPoolAllocationName'] = self.ipam_pool_allocation_name
        if self.ipam_pool_id is not None:
            result['IpamPoolId'] = self.ipam_pool_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cidr') is not None:
            self.cidr = m.get('Cidr')
        if m.get('IpamPoolAllocationIds') is not None:
            self.ipam_pool_allocation_ids = m.get('IpamPoolAllocationIds')
        if m.get('IpamPoolAllocationName') is not None:
            self.ipam_pool_allocation_name = m.get('IpamPoolAllocationName')
        if m.get('IpamPoolId') is not None:
            self.ipam_pool_id = m.get('IpamPoolId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListIpamPoolAllocationsResponseBodyIpamPoolAllocations(TeaModel):
    def __init__(
        self,
        cidr: str = None,
        creation_time: str = None,
        ipam_pool_allocation_description: str = None,
        ipam_pool_allocation_id: str = None,
        ipam_pool_allocation_name: str = None,
        ipam_pool_id: str = None,
        region_id: str = None,
        resource_id: str = None,
        resource_owner_id: int = None,
        resource_region_id: str = None,
        resource_type: str = None,
        source_cidr: str = None,
        status: str = None,
    ):
        # The allocated CIDR block.
        self.cidr = cidr
        # The time when the instance was created.
        self.creation_time = creation_time
        # The description of the allocation.
        self.ipam_pool_allocation_description = ipam_pool_allocation_description
        # The ID of the instance to which CIDR blocks are allocated from the IPAM pool.
        self.ipam_pool_allocation_id = ipam_pool_allocation_id
        # The name of the allocation.
        self.ipam_pool_allocation_name = ipam_pool_allocation_name
        # The ID of the IPAM pool.
        self.ipam_pool_id = ipam_pool_id
        # The region ID of the resource.
        self.region_id = region_id
        # The ID of the resource to which the CIDR block is allocated.
        self.resource_id = resource_id
        # The ID of the Alibaba Cloud account to which the resource belongs.
        self.resource_owner_id = resource_owner_id
        # The effective region ID of the resource.
        self.resource_region_id = resource_region_id
        # The type of the resource to which the CIDR block is allocated. Valid values:
        # 
        # *   **VPC**\
        # *   **IpamPool**\
        # *   **Custom**\
        self.resource_type = resource_type
        # The source CIDR block.
        self.source_cidr = source_cidr
        # The status of the instance. Valid values:
        # 
        # *   **Created**\
        # *   **Deleted**\
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cidr is not None:
            result['Cidr'] = self.cidr
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.ipam_pool_allocation_description is not None:
            result['IpamPoolAllocationDescription'] = self.ipam_pool_allocation_description
        if self.ipam_pool_allocation_id is not None:
            result['IpamPoolAllocationId'] = self.ipam_pool_allocation_id
        if self.ipam_pool_allocation_name is not None:
            result['IpamPoolAllocationName'] = self.ipam_pool_allocation_name
        if self.ipam_pool_id is not None:
            result['IpamPoolId'] = self.ipam_pool_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.resource_region_id is not None:
            result['ResourceRegionId'] = self.resource_region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.source_cidr is not None:
            result['SourceCidr'] = self.source_cidr
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cidr') is not None:
            self.cidr = m.get('Cidr')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('IpamPoolAllocationDescription') is not None:
            self.ipam_pool_allocation_description = m.get('IpamPoolAllocationDescription')
        if m.get('IpamPoolAllocationId') is not None:
            self.ipam_pool_allocation_id = m.get('IpamPoolAllocationId')
        if m.get('IpamPoolAllocationName') is not None:
            self.ipam_pool_allocation_name = m.get('IpamPoolAllocationName')
        if m.get('IpamPoolId') is not None:
            self.ipam_pool_id = m.get('IpamPoolId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ResourceRegionId') is not None:
            self.resource_region_id = m.get('ResourceRegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('SourceCidr') is not None:
            self.source_cidr = m.get('SourceCidr')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListIpamPoolAllocationsResponseBody(TeaModel):
    def __init__(
        self,
        count: int = None,
        ipam_pool_allocations: List[ListIpamPoolAllocationsResponseBodyIpamPoolAllocations] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The number of entries returned.
        self.count = count
        # The IDs of the instances to which CIDR blocks are allocated from the IPAM pool.
        self.ipam_pool_allocations = ipam_pool_allocations
        # The number of entries per page.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If **NextToken** is empty, no next page exists.
        # *   If a value of **NextToken** is returned, the value indicates the token that is used for the next query.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.ipam_pool_allocations:
            for k in self.ipam_pool_allocations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        result['IpamPoolAllocations'] = []
        if self.ipam_pool_allocations is not None:
            for k in self.ipam_pool_allocations:
                result['IpamPoolAllocations'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        self.ipam_pool_allocations = []
        if m.get('IpamPoolAllocations') is not None:
            for k in m.get('IpamPoolAllocations'):
                temp_model = ListIpamPoolAllocationsResponseBodyIpamPoolAllocations()
                self.ipam_pool_allocations.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListIpamPoolAllocationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListIpamPoolAllocationsResponseBody = None,
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
            temp_model = ListIpamPoolAllocationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListIpamPoolCidrsRequest(TeaModel):
    def __init__(
        self,
        cidr: str = None,
        ipam_pool_id: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
    ):
        # The provisioned CIDR block that you want to query.
        # 
        # >  Only IPv4 CIDR blocks are supported.
        self.cidr = cidr
        # The ID of the IPAM pool.
        # 
        # This parameter is required.
        self.ipam_pool_id = ipam_pool_id
        # The number of entries per page. Valid values: **1** to **100**. Default value: **10**.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If **NextToken** is empty, no next page exists.
        # *   If a value of **NextToken** is returned, the value indicates the token that is used for the next query.
        self.next_token = next_token
        # The ID of the region where the IPAM instance is hosted.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the most recent region list.
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
        if self.cidr is not None:
            result['Cidr'] = self.cidr
        if self.ipam_pool_id is not None:
            result['IpamPoolId'] = self.ipam_pool_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cidr') is not None:
            self.cidr = m.get('Cidr')
        if m.get('IpamPoolId') is not None:
            self.ipam_pool_id = m.get('IpamPoolId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListIpamPoolCidrsResponseBodyIpamPoolCidrs(TeaModel):
    def __init__(
        self,
        cidr: str = None,
        ipam_pool_id: str = None,
        status: str = None,
    ):
        # The provisioned CIDR block.
        self.cidr = cidr
        # The ID of the IPAM pool.
        self.ipam_pool_id = ipam_pool_id
        # The status of the CIDR block provisioned to the IPAM pool. Valid values:
        # 
        # *   **Created**\
        # *   **Deleted**\
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cidr is not None:
            result['Cidr'] = self.cidr
        if self.ipam_pool_id is not None:
            result['IpamPoolId'] = self.ipam_pool_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cidr') is not None:
            self.cidr = m.get('Cidr')
        if m.get('IpamPoolId') is not None:
            self.ipam_pool_id = m.get('IpamPoolId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListIpamPoolCidrsResponseBody(TeaModel):
    def __init__(
        self,
        count: int = None,
        ipam_pool_cidrs: List[ListIpamPoolCidrsResponseBodyIpamPoolCidrs] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The number of entries returned.
        self.count = count
        # The IDs of IPAM pools.
        self.ipam_pool_cidrs = ipam_pool_cidrs
        # The number of entries per page.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If **NextToken** is empty, no next page exists.
        # *   If a value of **NextToken** is returned, the value indicates the token that is used for the next query.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.ipam_pool_cidrs:
            for k in self.ipam_pool_cidrs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        result['IpamPoolCidrs'] = []
        if self.ipam_pool_cidrs is not None:
            for k in self.ipam_pool_cidrs:
                result['IpamPoolCidrs'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        self.ipam_pool_cidrs = []
        if m.get('IpamPoolCidrs') is not None:
            for k in m.get('IpamPoolCidrs'):
                temp_model = ListIpamPoolCidrsResponseBodyIpamPoolCidrs()
                self.ipam_pool_cidrs.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListIpamPoolCidrsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListIpamPoolCidrsResponseBody = None,
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
            temp_model = ListIpamPoolCidrsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListIpamPoolsRequestTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key. You can specify at most 20 tag keys. It cannot be an empty string.
        # 
        # The tag key can be up to 64 characters in length and can contain letters, digits, periods (.), underscores (_), and hyphens (-). The tag key must start with a letter but cannot start with `aliyun` or `acs:`. The tag key cannot contain `http://` or `https://`.
        self.key = key
        # The tag value. You can specify at most 20 tag values. It can be an empty string.
        # 
        # The tag value can be up to 128 characters in length. It must start with a letter and can contain digits, periods (.), underscores (_), and hyphens (-). It cannot start with `aliyun` or `acs:`, and cannot contain `http://` or `https://`.
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


class ListIpamPoolsRequest(TeaModel):
    def __init__(
        self,
        ip_version: str = None,
        ipam_pool_ids: List[str] = None,
        ipam_pool_name: str = None,
        ipam_scope_id: str = None,
        ipv_6isp: str = None,
        is_shared: bool = None,
        max_results: int = None,
        next_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        pool_region_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        source_ipam_pool_id: str = None,
        tags: List[ListIpamPoolsRequestTags] = None,
    ):
        self.ip_version = ip_version
        # The IDs of IPAM pools. Valid values of N: 1 to 100. A maximum of 100 IPAM pools can be queried at a time.
        self.ipam_pool_ids = ipam_pool_ids
        # The name of the IPAM pool. You can enter at most 20 names.
        # 
        # It must be 1 to 128 characters in length and cannot start with `http://` or `https://`.
        self.ipam_pool_name = ipam_pool_name
        # The ID of the IPAM scope.
        self.ipam_scope_id = ipam_scope_id
        self.ipv_6isp = ipv_6isp
        # Whether it is a shared pool.
        self.is_shared = is_shared
        # The number of entries per page. Valid values: 1 to 100. Default value: 10.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If NextToken is empty, no next page exists.
        # *   You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The effective region of the IPAM pool.
        self.pool_region_id = pool_region_id
        # The ID of the region where the IPAM instance is hosted. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group to which the IPAM pool belongs.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the source IPAM pool.
        self.source_ipam_pool_id = source_ipam_pool_id
        # The tag information.
        self.tags = tags

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
        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version
        if self.ipam_pool_ids is not None:
            result['IpamPoolIds'] = self.ipam_pool_ids
        if self.ipam_pool_name is not None:
            result['IpamPoolName'] = self.ipam_pool_name
        if self.ipam_scope_id is not None:
            result['IpamScopeId'] = self.ipam_scope_id
        if self.ipv_6isp is not None:
            result['Ipv6Isp'] = self.ipv_6isp
        if self.is_shared is not None:
            result['IsShared'] = self.is_shared
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pool_region_id is not None:
            result['PoolRegionId'] = self.pool_region_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.source_ipam_pool_id is not None:
            result['SourceIpamPoolId'] = self.source_ipam_pool_id
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')
        if m.get('IpamPoolIds') is not None:
            self.ipam_pool_ids = m.get('IpamPoolIds')
        if m.get('IpamPoolName') is not None:
            self.ipam_pool_name = m.get('IpamPoolName')
        if m.get('IpamScopeId') is not None:
            self.ipam_scope_id = m.get('IpamScopeId')
        if m.get('Ipv6Isp') is not None:
            self.ipv_6isp = m.get('Ipv6Isp')
        if m.get('IsShared') is not None:
            self.is_shared = m.get('IsShared')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PoolRegionId') is not None:
            self.pool_region_id = m.get('PoolRegionId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SourceIpamPoolId') is not None:
            self.source_ipam_pool_id = m.get('SourceIpamPoolId')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListIpamPoolsRequestTags()
                self.tags.append(temp_model.from_map(k))
        return self


class ListIpamPoolsResponseBodyIpamPoolsTags(TeaModel):
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


class ListIpamPoolsResponseBodyIpamPools(TeaModel):
    def __init__(
        self,
        allocation_default_cidr_mask: int = None,
        allocation_max_cidr_mask: int = None,
        allocation_min_cidr_mask: int = None,
        auto_import: bool = None,
        cidrs: List[str] = None,
        create_time: str = None,
        has_sub_pool: bool = None,
        ip_version: str = None,
        ipam_id: str = None,
        ipam_pool_description: str = None,
        ipam_pool_id: str = None,
        ipam_pool_name: str = None,
        ipam_region_id: str = None,
        ipam_scope_id: str = None,
        ipam_scope_type: str = None,
        ipv_6isp: str = None,
        is_shared: bool = None,
        owner_id: int = None,
        pool_depth: int = None,
        pool_region_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        source_ipam_pool_id: str = None,
        status: str = None,
        tags: List[ListIpamPoolsResponseBodyIpamPoolsTags] = None,
    ):
        # The default network mask assigned to the IPAM pool.
        # 
        # An IPv4 mask must be **0 to 32** bits in length.
        self.allocation_default_cidr_mask = allocation_default_cidr_mask
        # The maximum network mask assigned to the IPAM pool.
        # 
        # An IPv4 mask must be **0 to 32** bits in length.
        self.allocation_max_cidr_mask = allocation_max_cidr_mask
        # The minimum network mask assigned to the IPAM pool.
        # 
        # An IPv4 mask must be **0 to 32** bits in length.
        self.allocation_min_cidr_mask = allocation_min_cidr_mask
        # Whether the pool has the auto-import feature enabled.
        self.auto_import = auto_import
        self.cidrs = cidrs
        # The time when the IPAM pool was created.
        self.create_time = create_time
        # Indicates whether the pool is a subpool. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.has_sub_pool = has_sub_pool
        # The IP version. Only **IPv4** may be returned.
        self.ip_version = ip_version
        # The ID of the IPAM.
        self.ipam_id = ipam_id
        # The description of the IPAM pool.
        self.ipam_pool_description = ipam_pool_description
        # The ID of the IPAM pool.
        self.ipam_pool_id = ipam_pool_id
        # The name of the IPAM pool.
        self.ipam_pool_name = ipam_pool_name
        # The ID of the region where the IPAM to which the IPAM pool belongs is hosted.
        self.ipam_region_id = ipam_region_id
        # The ID of the IPAM scope.
        self.ipam_scope_id = ipam_scope_id
        # The type of the IPAM scope. Valid values:
        # 
        # *   **public**\
        # *   **private**\
        self.ipam_scope_type = ipam_scope_type
        self.ipv_6isp = ipv_6isp
        # Whether it is a shared pool.
        self.is_shared = is_shared
        # The Alibaba Cloud account of the owner for the IPAM pool.
        self.owner_id = owner_id
        # The depth of the IPAM pool. Valid values: **0 to 10**.
        self.pool_depth = pool_depth
        # The effective region of the IPAM pool. The ID of the effective region for the IPAM pool.
        self.pool_region_id = pool_region_id
        # The ID of the region where the operation is called.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The ID of the source IPAM pool.
        self.source_ipam_pool_id = source_ipam_pool_id
        # The status of the IPAM pool. Valid values:
        # 
        # *   **Creating**\
        # *   **Created**: indicates that the creation is complete.
        # *   **Modifying**\
        # *   **Deleting**\
        # *   **Deleted**\
        self.status = status
        # The tag list.
        self.tags = tags

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
        if self.allocation_default_cidr_mask is not None:
            result['AllocationDefaultCidrMask'] = self.allocation_default_cidr_mask
        if self.allocation_max_cidr_mask is not None:
            result['AllocationMaxCidrMask'] = self.allocation_max_cidr_mask
        if self.allocation_min_cidr_mask is not None:
            result['AllocationMinCidrMask'] = self.allocation_min_cidr_mask
        if self.auto_import is not None:
            result['AutoImport'] = self.auto_import
        if self.cidrs is not None:
            result['Cidrs'] = self.cidrs
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.has_sub_pool is not None:
            result['HasSubPool'] = self.has_sub_pool
        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version
        if self.ipam_id is not None:
            result['IpamId'] = self.ipam_id
        if self.ipam_pool_description is not None:
            result['IpamPoolDescription'] = self.ipam_pool_description
        if self.ipam_pool_id is not None:
            result['IpamPoolId'] = self.ipam_pool_id
        if self.ipam_pool_name is not None:
            result['IpamPoolName'] = self.ipam_pool_name
        if self.ipam_region_id is not None:
            result['IpamRegionId'] = self.ipam_region_id
        if self.ipam_scope_id is not None:
            result['IpamScopeId'] = self.ipam_scope_id
        if self.ipam_scope_type is not None:
            result['IpamScopeType'] = self.ipam_scope_type
        if self.ipv_6isp is not None:
            result['Ipv6Isp'] = self.ipv_6isp
        if self.is_shared is not None:
            result['IsShared'] = self.is_shared
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pool_depth is not None:
            result['PoolDepth'] = self.pool_depth
        if self.pool_region_id is not None:
            result['PoolRegionId'] = self.pool_region_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.source_ipam_pool_id is not None:
            result['SourceIpamPoolId'] = self.source_ipam_pool_id
        if self.status is not None:
            result['Status'] = self.status
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocationDefaultCidrMask') is not None:
            self.allocation_default_cidr_mask = m.get('AllocationDefaultCidrMask')
        if m.get('AllocationMaxCidrMask') is not None:
            self.allocation_max_cidr_mask = m.get('AllocationMaxCidrMask')
        if m.get('AllocationMinCidrMask') is not None:
            self.allocation_min_cidr_mask = m.get('AllocationMinCidrMask')
        if m.get('AutoImport') is not None:
            self.auto_import = m.get('AutoImport')
        if m.get('Cidrs') is not None:
            self.cidrs = m.get('Cidrs')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('HasSubPool') is not None:
            self.has_sub_pool = m.get('HasSubPool')
        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')
        if m.get('IpamId') is not None:
            self.ipam_id = m.get('IpamId')
        if m.get('IpamPoolDescription') is not None:
            self.ipam_pool_description = m.get('IpamPoolDescription')
        if m.get('IpamPoolId') is not None:
            self.ipam_pool_id = m.get('IpamPoolId')
        if m.get('IpamPoolName') is not None:
            self.ipam_pool_name = m.get('IpamPoolName')
        if m.get('IpamRegionId') is not None:
            self.ipam_region_id = m.get('IpamRegionId')
        if m.get('IpamScopeId') is not None:
            self.ipam_scope_id = m.get('IpamScopeId')
        if m.get('IpamScopeType') is not None:
            self.ipam_scope_type = m.get('IpamScopeType')
        if m.get('Ipv6Isp') is not None:
            self.ipv_6isp = m.get('Ipv6Isp')
        if m.get('IsShared') is not None:
            self.is_shared = m.get('IsShared')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PoolDepth') is not None:
            self.pool_depth = m.get('PoolDepth')
        if m.get('PoolRegionId') is not None:
            self.pool_region_id = m.get('PoolRegionId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SourceIpamPoolId') is not None:
            self.source_ipam_pool_id = m.get('SourceIpamPoolId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListIpamPoolsResponseBodyIpamPoolsTags()
                self.tags.append(temp_model.from_map(k))
        return self


class ListIpamPoolsResponseBody(TeaModel):
    def __init__(
        self,
        count: int = None,
        ipam_pools: List[ListIpamPoolsResponseBodyIpamPools] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The number of entries returned.
        self.count = count
        # The IPAM pools.
        self.ipam_pools = ipam_pools
        # The number of entries per page. Valid values: 1 to 100. Default value: 10.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If **NextToken** is empty, no next page exists.
        # *   If a value of **NextToken** is returned, the value indicates the token that is used for the next query.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.ipam_pools:
            for k in self.ipam_pools:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        result['IpamPools'] = []
        if self.ipam_pools is not None:
            for k in self.ipam_pools:
                result['IpamPools'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        self.ipam_pools = []
        if m.get('IpamPools') is not None:
            for k in m.get('IpamPools'):
                temp_model = ListIpamPoolsResponseBodyIpamPools()
                self.ipam_pools.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListIpamPoolsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListIpamPoolsResponseBody = None,
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
            temp_model = ListIpamPoolsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListIpamResourceCidrsRequest(TeaModel):
    def __init__(
        self,
        ipam_pool_id: str = None,
        ipam_scope_id: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        resource_id: str = None,
        resource_owner_id: int = None,
        resource_type: str = None,
        vpc_id: str = None,
    ):
        # The ID of the IPAM pool.
        # 
        # >  You must specify at least one of **IpamScopeId** and **IpamPoolId**.
        self.ipam_pool_id = ipam_pool_id
        # The ID of the IPAM scope.
        # 
        # >  You must specify at least one of **IpamScopeId** and **IpamPoolId**.
        self.ipam_scope_id = ipam_scope_id
        # The number of entries per page. Valid values: **1** to **100**. Default value: **10**.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   You do not need to specify this parameter for the first request.
        # *   You must specify the token that is obtained from the previous query as the value of **NextToken**.
        self.next_token = next_token
        # The ID of the region where the IPAM instance is hosted.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource ID.
        self.resource_id = resource_id
        self.resource_owner_id = resource_owner_id
        # The type of resource. Valid values:
        # 
        # *   **VPC**\
        # *   **VSwitch**\
        self.resource_type = resource_type
        # The VPC ID.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ipam_pool_id is not None:
            result['IpamPoolId'] = self.ipam_pool_id
        if self.ipam_scope_id is not None:
            result['IpamScopeId'] = self.ipam_scope_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpamPoolId') is not None:
            self.ipam_pool_id = m.get('IpamPoolId')
        if m.get('IpamScopeId') is not None:
            self.ipam_scope_id = m.get('IpamScopeId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class ListIpamResourceCidrsResponseBodyIpamResourceCidrsIpCountDetail(TeaModel):
    def __init__(
        self,
        free_ip_count: str = None,
        total_ip_count: str = None,
        used_ip_count: str = None,
    ):
        self.free_ip_count = free_ip_count
        self.total_ip_count = total_ip_count
        self.used_ip_count = used_ip_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.free_ip_count is not None:
            result['FreeIpCount'] = self.free_ip_count
        if self.total_ip_count is not None:
            result['TotalIpCount'] = self.total_ip_count
        if self.used_ip_count is not None:
            result['UsedIpCount'] = self.used_ip_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FreeIpCount') is not None:
            self.free_ip_count = m.get('FreeIpCount')
        if m.get('TotalIpCount') is not None:
            self.total_ip_count = m.get('TotalIpCount')
        if m.get('UsedIpCount') is not None:
            self.used_ip_count = m.get('UsedIpCount')
        return self


class ListIpamResourceCidrsResponseBodyIpamResourceCidrsOverlapDetail(TeaModel):
    def __init__(
        self,
        overlap_resource_cidr: str = None,
        overlap_resource_id: str = None,
        overlap_resource_region: str = None,
    ):
        # The CIDR that overlaps with the current resource.
        self.overlap_resource_cidr = overlap_resource_cidr
        # Instance ID that overlaps with the current resource.
        self.overlap_resource_id = overlap_resource_id
        # The region of instance that overlaps with the current resource.
        self.overlap_resource_region = overlap_resource_region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.overlap_resource_cidr is not None:
            result['OverlapResourceCidr'] = self.overlap_resource_cidr
        if self.overlap_resource_id is not None:
            result['OverlapResourceId'] = self.overlap_resource_id
        if self.overlap_resource_region is not None:
            result['OverlapResourceRegion'] = self.overlap_resource_region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OverlapResourceCidr') is not None:
            self.overlap_resource_cidr = m.get('OverlapResourceCidr')
        if m.get('OverlapResourceId') is not None:
            self.overlap_resource_id = m.get('OverlapResourceId')
        if m.get('OverlapResourceRegion') is not None:
            self.overlap_resource_region = m.get('OverlapResourceRegion')
        return self


class ListIpamResourceCidrsResponseBodyIpamResourceCidrs(TeaModel):
    def __init__(
        self,
        ali_uid: int = None,
        cidr: str = None,
        compliance_status: str = None,
        ip_count_detail: ListIpamResourceCidrsResponseBodyIpamResourceCidrsIpCountDetail = None,
        ip_usage: str = None,
        ipam_allocation_id: str = None,
        ipam_id: str = None,
        ipam_pool_id: str = None,
        ipam_scope_id: str = None,
        management_status: str = None,
        overlap_detail: List[ListIpamResourceCidrsResponseBodyIpamResourceCidrsOverlapDetail] = None,
        overlap_status: str = None,
        resource_id: str = None,
        resource_owner_id: int = None,
        resource_region_id: str = None,
        resource_type: str = None,
        source_cidr: str = None,
        status: str = None,
        vpc_id: str = None,
    ):
        # The ID of the Alibaba Cloud account.
        self.ali_uid = ali_uid
        # The CIDR block of the resource.
        self.cidr = cidr
        # The compliance status of the resource.
        # 
        # *   **Compliant**\
        # *   **Noncompliant**\
        # *   **Ignored** Ignored resources are not monitored.
        # *   **Unmanaged**: The resource does not have a CIDR block allocated from the IPAM pool. IPAM does not monitor whether the CIDR block of the resource meets the allocation rules of the IP address pool.
        self.compliance_status = compliance_status
        self.ip_count_detail = ip_count_detail
        # The IP usage that is displayed in decimal form.
        self.ip_usage = ip_usage
        # The ID of the instance to which CIDR blocks are allocated from the IPAM pool.
        self.ipam_allocation_id = ipam_allocation_id
        # The ID of the IPAM.
        self.ipam_id = ipam_id
        # The ID of the IPAM pool.
        self.ipam_pool_id = ipam_pool_id
        # The ID of the IPAM scope.
        self.ipam_scope_id = ipam_scope_id
        # The management status of the resource.
        # 
        # *   **Managed**: The resource has a CIDR block allocated from an IPAM pool. IPAM is monitoring whether the allocated CIDR block overlaps with other CIDR blocks and whether the allocated CIDR block meets the allocation rules.
        # *   **Unmanaged**: The resource does not have a CIDR block allocated from the IPAM pool. IPAM is monitoring whether the resource has CIDR blocks that meet the allocation rules. Monitor whether CIDR blocks overlap with each other.
        # *   **Ignored**: The resource is not monitored. Ignored resources are not monitored. If you ignore a resource, CIDR blocks allocated to the resource are returned to the IPAM pool and will not be automatically allocated to the resource (if automatic allocation rules are specified).
        self.management_status = management_status
        # List of resources that overlap with the current resource.
        self.overlap_detail = overlap_detail
        # The overlapping status of the resource.
        # 
        # *   **Nonoverlapping**\
        # *   **Overlapping**\
        # *   **Ignored** Ignored resources are not monitored.
        self.overlap_status = overlap_status
        # The resource ID.
        self.resource_id = resource_id
        # The ID of the Alibaba Cloud account to which the resource belongs.
        self.resource_owner_id = resource_owner_id
        # The effective region ID of the resource.
        self.resource_region_id = resource_region_id
        # The type of resource. Valid values:
        # 
        # *   **VPC**\
        # *   **VSwitch**\
        self.resource_type = resource_type
        # The source CIDR block.
        self.source_cidr = source_cidr
        # The status of the resource in the IPAM pool. Valid values:
        # 
        # *   **Created**\
        # *   **Deleted**\
        self.status = status
        # The VPC ID.
        self.vpc_id = vpc_id

    def validate(self):
        if self.ip_count_detail:
            self.ip_count_detail.validate()
        if self.overlap_detail:
            for k in self.overlap_detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.cidr is not None:
            result['Cidr'] = self.cidr
        if self.compliance_status is not None:
            result['ComplianceStatus'] = self.compliance_status
        if self.ip_count_detail is not None:
            result['IpCountDetail'] = self.ip_count_detail.to_map()
        if self.ip_usage is not None:
            result['IpUsage'] = self.ip_usage
        if self.ipam_allocation_id is not None:
            result['IpamAllocationId'] = self.ipam_allocation_id
        if self.ipam_id is not None:
            result['IpamId'] = self.ipam_id
        if self.ipam_pool_id is not None:
            result['IpamPoolId'] = self.ipam_pool_id
        if self.ipam_scope_id is not None:
            result['IpamScopeId'] = self.ipam_scope_id
        if self.management_status is not None:
            result['ManagementStatus'] = self.management_status
        result['OverlapDetail'] = []
        if self.overlap_detail is not None:
            for k in self.overlap_detail:
                result['OverlapDetail'].append(k.to_map() if k else None)
        if self.overlap_status is not None:
            result['OverlapStatus'] = self.overlap_status
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.resource_region_id is not None:
            result['ResourceRegionId'] = self.resource_region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.source_cidr is not None:
            result['SourceCidr'] = self.source_cidr
        if self.status is not None:
            result['Status'] = self.status
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('Cidr') is not None:
            self.cidr = m.get('Cidr')
        if m.get('ComplianceStatus') is not None:
            self.compliance_status = m.get('ComplianceStatus')
        if m.get('IpCountDetail') is not None:
            temp_model = ListIpamResourceCidrsResponseBodyIpamResourceCidrsIpCountDetail()
            self.ip_count_detail = temp_model.from_map(m['IpCountDetail'])
        if m.get('IpUsage') is not None:
            self.ip_usage = m.get('IpUsage')
        if m.get('IpamAllocationId') is not None:
            self.ipam_allocation_id = m.get('IpamAllocationId')
        if m.get('IpamId') is not None:
            self.ipam_id = m.get('IpamId')
        if m.get('IpamPoolId') is not None:
            self.ipam_pool_id = m.get('IpamPoolId')
        if m.get('IpamScopeId') is not None:
            self.ipam_scope_id = m.get('IpamScopeId')
        if m.get('ManagementStatus') is not None:
            self.management_status = m.get('ManagementStatus')
        self.overlap_detail = []
        if m.get('OverlapDetail') is not None:
            for k in m.get('OverlapDetail'):
                temp_model = ListIpamResourceCidrsResponseBodyIpamResourceCidrsOverlapDetail()
                self.overlap_detail.append(temp_model.from_map(k))
        if m.get('OverlapStatus') is not None:
            self.overlap_status = m.get('OverlapStatus')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ResourceRegionId') is not None:
            self.resource_region_id = m.get('ResourceRegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('SourceCidr') is not None:
            self.source_cidr = m.get('SourceCidr')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class ListIpamResourceCidrsResponseBody(TeaModel):
    def __init__(
        self,
        count: int = None,
        ipam_resource_cidrs: List[ListIpamResourceCidrsResponseBodyIpamResourceCidrs] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The number of entries returned.
        self.count = count
        # The list of resources in the IPAM pool.
        self.ipam_resource_cidrs = ipam_resource_cidrs
        # The number of entries per page.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If **NextToken** is empty, no next page exists.
        # *   If a value of **NextToken** is returned, the value indicates the token that is used for the next query.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.ipam_resource_cidrs:
            for k in self.ipam_resource_cidrs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        result['IpamResourceCidrs'] = []
        if self.ipam_resource_cidrs is not None:
            for k in self.ipam_resource_cidrs:
                result['IpamResourceCidrs'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        self.ipam_resource_cidrs = []
        if m.get('IpamResourceCidrs') is not None:
            for k in m.get('IpamResourceCidrs'):
                temp_model = ListIpamResourceCidrsResponseBodyIpamResourceCidrs()
                self.ipam_resource_cidrs.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListIpamResourceCidrsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListIpamResourceCidrsResponseBody = None,
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
            temp_model = ListIpamResourceCidrsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListIpamResourceDiscoveriesRequestTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag. You can specify at most 20 tag keys. It cannot be an empty string.
        # 
        # The tag key can be up to 64 characters in length and can contain letters, digits, periods (.), underscores (_), and hyphens (-). The tag key must start with a letter but cannot start with `aliyun` or `acs:`. The tag key cannot contain `http://` or `https://`.
        self.key = key
        # The value of the tag. You can specify at most 20 tag values. The tag value cannot be an empty string.
        # 
        # A tag value can be up to 128 characters in length and cannot contain `http://` or `https://`.
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


class ListIpamResourceDiscoveriesRequest(TeaModel):
    def __init__(
        self,
        ipam_resource_discovery_ids: List[str] = None,
        ipam_resource_discovery_name: str = None,
        is_shared: bool = None,
        max_results: int = None,
        next_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        tags: List[ListIpamResourceDiscoveriesRequestTags] = None,
        type: str = None,
    ):
        # The IDs of resource discovery instances. Valid values of N: 1 to 100. A maximum of 100 resource discoveries can be queried at a time.
        self.ipam_resource_discovery_ids = ipam_resource_discovery_ids
        # The name of the resource discovery.
        # 
        # The name must be 1 to 128 characters in length and cannot start with http:// or https://.
        self.ipam_resource_discovery_name = ipam_resource_discovery_name
        # Whether it is a shared resource discovery.
        self.is_shared = is_shared
        # The maximum number of entries on each page. Valid values: 1 to 100. Default value: 10.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If **NextToken** is empty, there is no next page.
        # *   If a value of **NextToken** is returned, it indicates the token that is used for the next query.
        self.next_token = next_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the region where you want to query resource discovery. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group that resource discovery belongs.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The tag.
        self.tags = tags
        # The type of resource discovery.
        # 
        # > Supported types:
        # > - system: default resource discovery created by the system.
        # > - custom: custom resource discovery created by users.
        self.type = type

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
        if self.ipam_resource_discovery_ids is not None:
            result['IpamResourceDiscoveryIds'] = self.ipam_resource_discovery_ids
        if self.ipam_resource_discovery_name is not None:
            result['IpamResourceDiscoveryName'] = self.ipam_resource_discovery_name
        if self.is_shared is not None:
            result['IsShared'] = self.is_shared
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpamResourceDiscoveryIds') is not None:
            self.ipam_resource_discovery_ids = m.get('IpamResourceDiscoveryIds')
        if m.get('IpamResourceDiscoveryName') is not None:
            self.ipam_resource_discovery_name = m.get('IpamResourceDiscoveryName')
        if m.get('IsShared') is not None:
            self.is_shared = m.get('IsShared')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListIpamResourceDiscoveriesRequestTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListIpamResourceDiscoveriesResponseBodyIpamResourceDiscoveriesTags(TeaModel):
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


class ListIpamResourceDiscoveriesResponseBodyIpamResourceDiscoveries(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        ipam_resource_discovery_description: str = None,
        ipam_resource_discovery_id: str = None,
        ipam_resource_discovery_name: str = None,
        ipam_resource_discovery_status: str = None,
        operating_region_list: List[str] = None,
        owner_id: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        share_type: str = None,
        tags: List[ListIpamResourceDiscoveriesResponseBodyIpamResourceDiscoveriesTags] = None,
        type: str = None,
    ):
        # The time when the resource was discovered.
        self.create_time = create_time
        # The description of the resource discovery.
        self.ipam_resource_discovery_description = ipam_resource_discovery_description
        # The ID of resource discovery instance.
        self.ipam_resource_discovery_id = ipam_resource_discovery_id
        # The name of the resource discovery.
        self.ipam_resource_discovery_name = ipam_resource_discovery_name
        # The status of the resource discovery instance. Valid values:
        # 
        # *   **Creating**\
        # *   **Created**\
        # *   **Modifying**\
        # *   **Deleting**\
        # *   **Deleted**\
        self.ipam_resource_discovery_status = ipam_resource_discovery_status
        # The list of resource discovery regions.
        self.operating_region_list = operating_region_list
        # The Alibaba Cloud account that owns the resource discovery.
        self.owner_id = owner_id
        # The region ID of the queried resource discovery instance.
        self.region_id = region_id
        # The ID of the resource group that resource discovery belongs.
        self.resource_group_id = resource_group_id
        # The sharing status of the resource.
        # 
        # *   If the value is empty, the resource is as an average instance.
        # *   If the value is Shared, the resource discovery comes from a shared source.
        # *   If the value is Sharing, the resource discovery is being shared.
        self.share_type = share_type
        # The tag list.
        self.tags = tags
        # The type of resource discovery.
        self.type = type

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
            result['CreateTime'] = self.create_time
        if self.ipam_resource_discovery_description is not None:
            result['IpamResourceDiscoveryDescription'] = self.ipam_resource_discovery_description
        if self.ipam_resource_discovery_id is not None:
            result['IpamResourceDiscoveryId'] = self.ipam_resource_discovery_id
        if self.ipam_resource_discovery_name is not None:
            result['IpamResourceDiscoveryName'] = self.ipam_resource_discovery_name
        if self.ipam_resource_discovery_status is not None:
            result['IpamResourceDiscoveryStatus'] = self.ipam_resource_discovery_status
        if self.operating_region_list is not None:
            result['OperatingRegionList'] = self.operating_region_list
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('IpamResourceDiscoveryDescription') is not None:
            self.ipam_resource_discovery_description = m.get('IpamResourceDiscoveryDescription')
        if m.get('IpamResourceDiscoveryId') is not None:
            self.ipam_resource_discovery_id = m.get('IpamResourceDiscoveryId')
        if m.get('IpamResourceDiscoveryName') is not None:
            self.ipam_resource_discovery_name = m.get('IpamResourceDiscoveryName')
        if m.get('IpamResourceDiscoveryStatus') is not None:
            self.ipam_resource_discovery_status = m.get('IpamResourceDiscoveryStatus')
        if m.get('OperatingRegionList') is not None:
            self.operating_region_list = m.get('OperatingRegionList')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListIpamResourceDiscoveriesResponseBodyIpamResourceDiscoveriesTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListIpamResourceDiscoveriesResponseBody(TeaModel):
    def __init__(
        self,
        count: int = None,
        ipam_resource_discoveries: List[ListIpamResourceDiscoveriesResponseBodyIpamResourceDiscoveries] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The maximum number of entries on each page.
        self.count = count
        # The list of resource discovery instances.
        self.ipam_resource_discoveries = ipam_resource_discoveries
        # The maximum number of entries on each page. Valid values: 1 to 100. Default value: 10.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If **NextToken** is empty, there is no next page.
        # *   If a value of **NextToken** is returned, it indicates the token that is used for the next query.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.ipam_resource_discoveries:
            for k in self.ipam_resource_discoveries:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        result['IpamResourceDiscoveries'] = []
        if self.ipam_resource_discoveries is not None:
            for k in self.ipam_resource_discoveries:
                result['IpamResourceDiscoveries'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        self.ipam_resource_discoveries = []
        if m.get('IpamResourceDiscoveries') is not None:
            for k in m.get('IpamResourceDiscoveries'):
                temp_model = ListIpamResourceDiscoveriesResponseBodyIpamResourceDiscoveries()
                self.ipam_resource_discoveries.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListIpamResourceDiscoveriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListIpamResourceDiscoveriesResponseBody = None,
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
            temp_model = ListIpamResourceDiscoveriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListIpamResourceDiscoveryAssociationsRequest(TeaModel):
    def __init__(
        self,
        ipam_id: str = None,
        ipam_resource_discovery_id: str = None,
        max_results: int = None,
        next_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The ID of the IPAM.
        self.ipam_id = ipam_id
        # The ID of resource discovery instance.
        self.ipam_resource_discovery_id = ipam_resource_discovery_id
        # The maximum number of entries on each page. Valid values: 1 to 100. Default value: 10.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If this is your first or only query, this parameter is left empty.
        # *   If a next query is to be sent, the returned value is the value of NextToken that was returned last time this operation was called.
        self.next_token = next_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The request region.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ipam_id is not None:
            result['IpamId'] = self.ipam_id
        if self.ipam_resource_discovery_id is not None:
            result['IpamResourceDiscoveryId'] = self.ipam_resource_discovery_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpamId') is not None:
            self.ipam_id = m.get('IpamId')
        if m.get('IpamResourceDiscoveryId') is not None:
            self.ipam_resource_discovery_id = m.get('IpamResourceDiscoveryId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ListIpamResourceDiscoveryAssociationsResponseBodyIpamResourceDiscoveryAssociations(TeaModel):
    def __init__(
        self,
        ipam_id: str = None,
        ipam_resource_discovery_id: str = None,
        ipam_resource_discovery_owner_id: str = None,
        ipam_resource_discovery_status: str = None,
        ipam_resource_discovery_type: str = None,
        status: str = None,
    ):
        # The ID of the IPAM.
        self.ipam_id = ipam_id
        # The ID of resource discovery instance.
        self.ipam_resource_discovery_id = ipam_resource_discovery_id
        # The ID of the Alibaba Cloud account to which the resource discovery belongs.
        self.ipam_resource_discovery_owner_id = ipam_resource_discovery_owner_id
        # The status of the resource discovery instance. Valid values:
        # 
        # *   **Creating**\
        # *   **Created**\
        # *   **Modifying**\
        # *   **Deleting**\
        # *   **Deleted**\
        self.ipam_resource_discovery_status = ipam_resource_discovery_status
        # The type of resource discovery. Valid values:
        # 
        # *   **system**: default resource discovery created by the system.
        # *   **custom**: custom resource discovery created by users.
        self.ipam_resource_discovery_type = ipam_resource_discovery_type
        # The status of the associations. Valid values:
        # 
        # *   **Created**\
        # *   **Deleted**\
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ipam_id is not None:
            result['IpamId'] = self.ipam_id
        if self.ipam_resource_discovery_id is not None:
            result['IpamResourceDiscoveryId'] = self.ipam_resource_discovery_id
        if self.ipam_resource_discovery_owner_id is not None:
            result['IpamResourceDiscoveryOwnerId'] = self.ipam_resource_discovery_owner_id
        if self.ipam_resource_discovery_status is not None:
            result['IpamResourceDiscoveryStatus'] = self.ipam_resource_discovery_status
        if self.ipam_resource_discovery_type is not None:
            result['IpamResourceDiscoveryType'] = self.ipam_resource_discovery_type
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpamId') is not None:
            self.ipam_id = m.get('IpamId')
        if m.get('IpamResourceDiscoveryId') is not None:
            self.ipam_resource_discovery_id = m.get('IpamResourceDiscoveryId')
        if m.get('IpamResourceDiscoveryOwnerId') is not None:
            self.ipam_resource_discovery_owner_id = m.get('IpamResourceDiscoveryOwnerId')
        if m.get('IpamResourceDiscoveryStatus') is not None:
            self.ipam_resource_discovery_status = m.get('IpamResourceDiscoveryStatus')
        if m.get('IpamResourceDiscoveryType') is not None:
            self.ipam_resource_discovery_type = m.get('IpamResourceDiscoveryType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListIpamResourceDiscoveryAssociationsResponseBody(TeaModel):
    def __init__(
        self,
        count: int = None,
        ipam_resource_discovery_associations: List[ListIpamResourceDiscoveryAssociationsResponseBodyIpamResourceDiscoveryAssociations] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The number of entries on each page.
        self.count = count
        # The list of associations.
        self.ipam_resource_discovery_associations = ipam_resource_discovery_associations
        # The maximum number of entries on each page. Valid values: 1 to 100. Default value: 10.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If **NextToken** is empty, there is no next page.
        # *   If a value of **NextToken** is returned, it indicates the token that is used for the next query.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.ipam_resource_discovery_associations:
            for k in self.ipam_resource_discovery_associations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        result['IpamResourceDiscoveryAssociations'] = []
        if self.ipam_resource_discovery_associations is not None:
            for k in self.ipam_resource_discovery_associations:
                result['IpamResourceDiscoveryAssociations'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        self.ipam_resource_discovery_associations = []
        if m.get('IpamResourceDiscoveryAssociations') is not None:
            for k in m.get('IpamResourceDiscoveryAssociations'):
                temp_model = ListIpamResourceDiscoveryAssociationsResponseBodyIpamResourceDiscoveryAssociations()
                self.ipam_resource_discovery_associations.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListIpamResourceDiscoveryAssociationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListIpamResourceDiscoveryAssociationsResponseBody = None,
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
            temp_model = ListIpamResourceDiscoveryAssociationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListIpamScopesRequestTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key. You can specify at most 20 tag keys. The tag key cannot be an empty string.
        # 
        # The tag key can be up to 64 characters in length and can contain letters, digits, periods (.), underscores (_), and hyphens (-). The tag key must start with a letter but cannot start with `aliyun` or `acs:`. The tag key cannot contain `http://` or `https://`.
        self.key = key
        # The tag value. You can specify up to 20 tag values. The tag value can be an empty string.
        # 
        # The tag value can be up to 128 characters in length and can contain letters, digits, periods (.), underscores (_), and hyphens (-). It cannot start with a `aliyun` or `acs:`, and cannot contain `http://` or `https://`.
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


class ListIpamScopesRequest(TeaModel):
    def __init__(
        self,
        ipam_id: str = None,
        ipam_scope_ids: List[str] = None,
        ipam_scope_name: str = None,
        ipam_scope_type: str = None,
        max_results: int = None,
        next_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        tags: List[ListIpamScopesRequestTags] = None,
    ):
        # The ID of the IPAM.
        self.ipam_id = ipam_id
        # The IDs of IPAM scopes.
        self.ipam_scope_ids = ipam_scope_ids
        # The name of the IPAM scope.
        # 
        # It must be 1 to 128 characters in length and cannot start with `http://` or `https://`.
        self.ipam_scope_name = ipam_scope_name
        # The type of the IPAM scope. Valid values:
        # 
        # *   **public**\
        # *   **private**\
        self.ipam_scope_type = ipam_scope_type
        # The number of entries per page. Valid values: **1** to **100**. Default value: **10**.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   You do not need to specify this parameter for the first request.
        # *   You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the region where the IPAM instance is hosted. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource group ID of the IPAM scope.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The tag list.
        self.tags = tags

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
        if self.ipam_id is not None:
            result['IpamId'] = self.ipam_id
        if self.ipam_scope_ids is not None:
            result['IpamScopeIds'] = self.ipam_scope_ids
        if self.ipam_scope_name is not None:
            result['IpamScopeName'] = self.ipam_scope_name
        if self.ipam_scope_type is not None:
            result['IpamScopeType'] = self.ipam_scope_type
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpamId') is not None:
            self.ipam_id = m.get('IpamId')
        if m.get('IpamScopeIds') is not None:
            self.ipam_scope_ids = m.get('IpamScopeIds')
        if m.get('IpamScopeName') is not None:
            self.ipam_scope_name = m.get('IpamScopeName')
        if m.get('IpamScopeType') is not None:
            self.ipam_scope_type = m.get('IpamScopeType')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListIpamScopesRequestTags()
                self.tags.append(temp_model.from_map(k))
        return self


class ListIpamScopesResponseBodyIpamScopesTags(TeaModel):
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


class ListIpamScopesResponseBodyIpamScopes(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        ipam_id: str = None,
        ipam_scope_description: str = None,
        ipam_scope_id: str = None,
        ipam_scope_name: str = None,
        ipam_scope_type: str = None,
        is_default: bool = None,
        owner_id: int = None,
        pool_count: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        status: str = None,
        tags: List[ListIpamScopesResponseBodyIpamScopesTags] = None,
    ):
        # The time when the IPAM scope was created.
        self.create_time = create_time
        # The ID of the IPAM.
        self.ipam_id = ipam_id
        # The description of the IPAM scope.
        self.ipam_scope_description = ipam_scope_description
        # The ID of the IPAM scope.
        self.ipam_scope_id = ipam_scope_id
        # The name of the IPAM scope.
        self.ipam_scope_name = ipam_scope_name
        # The type of the IPAM scope. Valid values:
        # 
        # *   **public**\
        # *   **private**\
        self.ipam_scope_type = ipam_scope_type
        # Indicates whether the scope is the default scope. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.is_default = is_default
        # The Alibaba Cloud account that owns the IPAM scope.
        self.owner_id = owner_id
        # The number of pools in the IPAM scope.
        self.pool_count = pool_count
        # The region ID of the IPAM.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The status of the IPAM scope. Valid values:
        # 
        # *   **Creating**\
        # *   **Created**\
        # *   **Deleting**\
        # *   **Deleted**\
        self.status = status
        # The tag list.
        self.tags = tags

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
            result['CreateTime'] = self.create_time
        if self.ipam_id is not None:
            result['IpamId'] = self.ipam_id
        if self.ipam_scope_description is not None:
            result['IpamScopeDescription'] = self.ipam_scope_description
        if self.ipam_scope_id is not None:
            result['IpamScopeId'] = self.ipam_scope_id
        if self.ipam_scope_name is not None:
            result['IpamScopeName'] = self.ipam_scope_name
        if self.ipam_scope_type is not None:
            result['IpamScopeType'] = self.ipam_scope_type
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pool_count is not None:
            result['PoolCount'] = self.pool_count
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.status is not None:
            result['Status'] = self.status
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('IpamId') is not None:
            self.ipam_id = m.get('IpamId')
        if m.get('IpamScopeDescription') is not None:
            self.ipam_scope_description = m.get('IpamScopeDescription')
        if m.get('IpamScopeId') is not None:
            self.ipam_scope_id = m.get('IpamScopeId')
        if m.get('IpamScopeName') is not None:
            self.ipam_scope_name = m.get('IpamScopeName')
        if m.get('IpamScopeType') is not None:
            self.ipam_scope_type = m.get('IpamScopeType')
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PoolCount') is not None:
            self.pool_count = m.get('PoolCount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListIpamScopesResponseBodyIpamScopesTags()
                self.tags.append(temp_model.from_map(k))
        return self


class ListIpamScopesResponseBody(TeaModel):
    def __init__(
        self,
        count: int = None,
        ipam_scopes: List[ListIpamScopesResponseBodyIpamScopes] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The number of entries returned.
        self.count = count
        # The IPAM scopes.
        self.ipam_scopes = ipam_scopes
        # The number of entries per page.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If **NextToken** is empty, no next page exists.
        # *   If a value of **NextToken** is returned, the value indicates the token that is used for the next query.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.ipam_scopes:
            for k in self.ipam_scopes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        result['IpamScopes'] = []
        if self.ipam_scopes is not None:
            for k in self.ipam_scopes:
                result['IpamScopes'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        self.ipam_scopes = []
        if m.get('IpamScopes') is not None:
            for k in m.get('IpamScopes'):
                temp_model = ListIpamScopesResponseBodyIpamScopes()
                self.ipam_scopes.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListIpamScopesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListIpamScopesResponseBody = None,
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
            temp_model = ListIpamScopesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListIpamsRequestTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key. You can specify at most 20 tag keys. The tag key cannot be an empty string.
        # 
        # The tag key can be up to 64 characters in length and can contain letters, digits, periods (.), underscores (_), and hyphens (-). The tag key must start with a letter but cannot start with `aliyun` or `acs:`. The tag key cannot contain `http://` or `https://`.
        self.key = key
        # The tag value. You can specify at most 20 tag values. The tag value can be an empty string.
        # 
        # The tag value can be up to 128 characters in length. It must start with a letter and can contain digits, periods (.), underscores (_), and hyphens (-). It cannot start with `aliyun` or `acs:`, and cannot contain `http://` or `https://`.
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


class ListIpamsRequest(TeaModel):
    def __init__(
        self,
        ipam_ids: List[str] = None,
        ipam_name: str = None,
        max_results: int = None,
        next_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        tags: List[ListIpamsRequestTags] = None,
    ):
        # The IDs of IPAMs. Valid values of N: 1 to 100. A maximum of 100 IPAMs can be queried at a time.
        self.ipam_ids = ipam_ids
        # The name of the IPAM.
        # 
        # It must be 1 to 128 characters in length and cannot start with `http://` or `https://`.
        self.ipam_name = ipam_name
        # The number of entries per page. Valid values: **1** to **100**. Default value: **10**.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   You do not need to specify this parameter for the first request.
        # *   You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the region where the IPAM instance is hosted. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource group ID of the IPAM.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The tag information.
        self.tags = tags

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
        if self.ipam_ids is not None:
            result['IpamIds'] = self.ipam_ids
        if self.ipam_name is not None:
            result['IpamName'] = self.ipam_name
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpamIds') is not None:
            self.ipam_ids = m.get('IpamIds')
        if m.get('IpamName') is not None:
            self.ipam_name = m.get('IpamName')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListIpamsRequestTags()
                self.tags.append(temp_model.from_map(k))
        return self


class ListIpamsResponseBodyIpamsTags(TeaModel):
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


class ListIpamsResponseBodyIpams(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        default_resource_discovery_association_id: str = None,
        default_resource_discovery_id: str = None,
        ipam_description: str = None,
        ipam_id: str = None,
        ipam_name: str = None,
        ipam_status: str = None,
        operating_region_list: List[str] = None,
        owner_id: int = None,
        private_default_scope_id: str = None,
        public_default_scope_id: str = None,
        region_id: str = None,
        resource_discovery_association_count: int = None,
        resource_group_id: str = None,
        scope_count: int = None,
        tags: List[ListIpamsResponseBodyIpamsTags] = None,
    ):
        # The time when the IPAM was created.
        self.create_time = create_time
        # Default resource discovery association ID.
        self.default_resource_discovery_association_id = default_resource_discovery_association_id
        # Default resource discovery instance ID.
        self.default_resource_discovery_id = default_resource_discovery_id
        # The description of the IPAM.
        self.ipam_description = ipam_description
        # The ID of the IPAM.
        self.ipam_id = ipam_id
        # The name of the IPAM.
        self.ipam_name = ipam_name
        # The status of the IPAM. Valid values:
        # 
        # *   **Creating**\
        # *   **Created**\
        # *   **Deleting**\
        # *   **Deleted**\
        self.ipam_status = ipam_status
        # The effective regions of the IPAM.
        self.operating_region_list = operating_region_list
        # The Alibaba Cloud account that owns the IPAM.
        self.owner_id = owner_id
        # The default private scope created by the system after the IPAM is created.
        self.private_default_scope_id = private_default_scope_id
        # The default public scope created by the system after the IPAM is created.
        self.public_default_scope_id = public_default_scope_id
        # The region ID of the IPAM.
        self.region_id = region_id
        # Number of resource discovery associations.
        self.resource_discovery_association_count = resource_discovery_association_count
        # The resource group ID of the IPAM.
        self.resource_group_id = resource_group_id
        # The number of IPAM scopes. Value: **2 to 5**.
        self.scope_count = scope_count
        # The tag list.
        self.tags = tags

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
            result['CreateTime'] = self.create_time
        if self.default_resource_discovery_association_id is not None:
            result['DefaultResourceDiscoveryAssociationId'] = self.default_resource_discovery_association_id
        if self.default_resource_discovery_id is not None:
            result['DefaultResourceDiscoveryId'] = self.default_resource_discovery_id
        if self.ipam_description is not None:
            result['IpamDescription'] = self.ipam_description
        if self.ipam_id is not None:
            result['IpamId'] = self.ipam_id
        if self.ipam_name is not None:
            result['IpamName'] = self.ipam_name
        if self.ipam_status is not None:
            result['IpamStatus'] = self.ipam_status
        if self.operating_region_list is not None:
            result['OperatingRegionList'] = self.operating_region_list
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.private_default_scope_id is not None:
            result['PrivateDefaultScopeId'] = self.private_default_scope_id
        if self.public_default_scope_id is not None:
            result['PublicDefaultScopeId'] = self.public_default_scope_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_discovery_association_count is not None:
            result['ResourceDiscoveryAssociationCount'] = self.resource_discovery_association_count
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.scope_count is not None:
            result['ScopeCount'] = self.scope_count
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DefaultResourceDiscoveryAssociationId') is not None:
            self.default_resource_discovery_association_id = m.get('DefaultResourceDiscoveryAssociationId')
        if m.get('DefaultResourceDiscoveryId') is not None:
            self.default_resource_discovery_id = m.get('DefaultResourceDiscoveryId')
        if m.get('IpamDescription') is not None:
            self.ipam_description = m.get('IpamDescription')
        if m.get('IpamId') is not None:
            self.ipam_id = m.get('IpamId')
        if m.get('IpamName') is not None:
            self.ipam_name = m.get('IpamName')
        if m.get('IpamStatus') is not None:
            self.ipam_status = m.get('IpamStatus')
        if m.get('OperatingRegionList') is not None:
            self.operating_region_list = m.get('OperatingRegionList')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PrivateDefaultScopeId') is not None:
            self.private_default_scope_id = m.get('PrivateDefaultScopeId')
        if m.get('PublicDefaultScopeId') is not None:
            self.public_default_scope_id = m.get('PublicDefaultScopeId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceDiscoveryAssociationCount') is not None:
            self.resource_discovery_association_count = m.get('ResourceDiscoveryAssociationCount')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ScopeCount') is not None:
            self.scope_count = m.get('ScopeCount')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListIpamsResponseBodyIpamsTags()
                self.tags.append(temp_model.from_map(k))
        return self


class ListIpamsResponseBody(TeaModel):
    def __init__(
        self,
        count: int = None,
        ipams: List[ListIpamsResponseBodyIpams] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The number of entries returned.
        self.count = count
        # The IPAMs.
        self.ipams = ipams
        # The number of entries per page. Valid values: 1 to 100. Default value: 10.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If **NextToken** is empty, no next page exists.
        # *   If a value of **NextToken** is returned, the value indicates the token that is used for the next query.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The number of entries.
        self.total_count = total_count

    def validate(self):
        if self.ipams:
            for k in self.ipams:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        result['Ipams'] = []
        if self.ipams is not None:
            for k in self.ipams:
                result['Ipams'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        self.ipams = []
        if m.get('Ipams') is not None:
            for k in m.get('Ipams'):
                temp_model = ListIpamsResponseBodyIpams()
                self.ipams.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListIpamsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListIpamsResponseBody = None,
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
            temp_model = ListIpamsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key. You can specify at most 20 tag keys. The tag key cannot be an empty string.
        # 
        # The tag key can be up to 64 characters in length and can contain letters, digits, periods (.), underscores (_), and hyphens (-). It cannot start with a `aliyun` or `acs:`, and cannot contain `http://` or `https://`.
        # 
        # >  You must specify **ResourceId.N** or **Tag.N** that consists of **Tag.N.Key** and **Tag.N.Value**.
        self.key = key
        # The tag value. You can specify at most 20 tag values. The tag value can be an empty string.
        # 
        # The tag value can be up to 128 characters in length and can contain letters, digits, periods (.), underscores (_), and hyphens (-). It cannot start with a `aliyun` or `acs:`, and cannot contain `http://` or `https://`.
        # 
        # >  You must specify **ResourceId.N** or **Tag.N** that consists of **Tag.N.Key** and **Tag.N.Value**.
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
        max_results: int = None,
        next_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_id: List[str] = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        resource_type: str = None,
        tag: List[ListTagResourcesRequestTag] = None,
    ):
        # The number of entries per page. Valid values: **1** to **50**. Default value: **10**.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   You do not need to specify this parameter for the first request.
        # *   If a value is returned for NextToken, you must specify the token that is obtained from the previous query as the value of **NextToken**.
        self.next_token = next_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the resource.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource IDs.
        self.resource_id = resource_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The resource type. Valid values:
        # 
        # *   **IPAM**\
        # *   **IPAMSCOPE**\
        # *   **IPAMPOOL**\
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The tag list.
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
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBodyTagResources(TeaModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_type: str = None,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The resource ID.
        self.resource_id = resource_id
        # The resource type. Valid values:
        # 
        # *   **IPAM**\
        # *   **IPAMSCOPE**\
        # *   **IPAMPOOL**\
        self.resource_type = resource_type
        # The tag key.
        self.tag_key = tag_key
        # The tag value.
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


class ListTagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        tag_resources: List[ListTagResourcesResponseBodyTagResources] = None,
    ):
        # The pagination token that is used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If **NextToken** is empty, no next page exists.
        # *   If a value of **NextToken** is returned, the value indicates the token that is used for the next query.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The resources to which the tags are added.
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
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TagResources'] = []
        if self.tag_resources is not None:
            for k in self.tag_resources:
                result['TagResources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tag_resources = []
        if m.get('TagResources') is not None:
            for k in m.get('TagResources'):
                temp_model = ListTagResourcesResponseBodyTagResources()
                self.tag_resources.append(temp_model.from_map(k))
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


class OpenVpcIpamServiceRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # Client token, used to ensure the idempotence of requests.
        # 
        # Generate a unique value for this parameter from your client to ensure it is unique across different requests. ClientToken supports only ASCII characters.
        # 
        # > If not specified, the system automatically uses the RequestId of the API request as the ClientToken identifier. The RequestId may differ for each API request.
        self.client_token = client_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the region where the IPAM instance is hosted.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class OpenVpcIpamServiceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # Status code.
        self.code = code
        # Information returned upon successful IPAM activation.
        self.message = message
        # Request ID.
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class OpenVpcIpamServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OpenVpcIpamServiceResponseBody = None,
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
            temp_model = OpenVpcIpamServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key. You can specify at most 20 tag keys. The tag key cannot be an empty string.
        # 
        # The tag key can be up to 64 characters in length and can contain letters, digits, periods (.), underscores (_), and hyphens (-). It cannot start with a `aliyun` or `acs:`, and cannot contain `http://` or `https://`.
        self.key = key
        # The tag value. You can specify at most 20 tag values. The tag value can be an empty string.
        # 
        # The tag value can be up to 128 characters in length and can contain letters, digits, periods (.), underscores (_), and hyphens (-). It cannot start with a `aliyun` or `acs:`, and cannot contain `http://` or `https://`.
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
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_id: List[str] = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        resource_type: str = None,
        tag: List[TagResourcesRequestTag] = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the resource.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The IDs of the resources.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The resource type. Valid values:
        # 
        # *   **IPAM**\
        # *   **IPAMSCOPE**\
        # *   **IPAMPOOL**\
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The tags to add to the resources.
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
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
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
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_id: List[str] = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        resource_type: str = None,
        tag_key: List[str] = None,
    ):
        # Specifies whether to remove all tags from the specified resource. Valid values:
        # 
        # *   **true**\
        # *   **false** (default)
        self.all = all
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the resource.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource IDs.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The resource type. Valid values:
        # 
        # *   **IPAM**\
        # *   **IPAMSCOPE**\
        # *   **IPAMPOOL**\
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The keys of the tags that you want to remove from the resource.
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
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
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


class UpdateIpamRequest(TeaModel):
    def __init__(
        self,
        add_operating_region: List[str] = None,
        client_token: str = None,
        dry_run: bool = None,
        ipam_description: str = None,
        ipam_id: str = None,
        ipam_name: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        remove_operating_region: List[str] = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The effective region that you want to add.
        self.add_operating_region = add_operating_region
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The client token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the request ID as the client token. The request ID may be different for each request.
        self.client_token = client_token
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the DryRunOperation error code is returned.
        # *   **false** (default): performs a dry run and performs the actual request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The description of the IPAM.
        # 
        # It must be 2 to 256 characters in length and must start with a letter. It cannot start with `http://` or `https://`. The default value is empty.
        self.ipam_description = ipam_description
        # The ID of the IPAM.
        # 
        # This parameter is required.
        self.ipam_id = ipam_id
        # The name of the IPAM.
        # 
        # It must be 1 to 128 characters in length and cannot start with `http://` or `https://`.
        self.ipam_name = ipam_name
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the region where the IPAM instance is hosted. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The effective region that you want to remove.
        self.remove_operating_region = remove_operating_region
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.add_operating_region is not None:
            result['AddOperatingRegion'] = self.add_operating_region
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.ipam_description is not None:
            result['IpamDescription'] = self.ipam_description
        if self.ipam_id is not None:
            result['IpamId'] = self.ipam_id
        if self.ipam_name is not None:
            result['IpamName'] = self.ipam_name
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.remove_operating_region is not None:
            result['RemoveOperatingRegion'] = self.remove_operating_region
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddOperatingRegion') is not None:
            self.add_operating_region = m.get('AddOperatingRegion')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IpamDescription') is not None:
            self.ipam_description = m.get('IpamDescription')
        if m.get('IpamId') is not None:
            self.ipam_id = m.get('IpamId')
        if m.get('IpamName') is not None:
            self.ipam_name = m.get('IpamName')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RemoveOperatingRegion') is not None:
            self.remove_operating_region = m.get('RemoveOperatingRegion')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class UpdateIpamResponseBody(TeaModel):
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


class UpdateIpamResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateIpamResponseBody = None,
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
            temp_model = UpdateIpamResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateIpamPoolRequest(TeaModel):
    def __init__(
        self,
        allocation_default_cidr_mask: int = None,
        allocation_max_cidr_mask: int = None,
        allocation_min_cidr_mask: int = None,
        auto_import: bool = None,
        clear_allocation_default_cidr_mask: bool = None,
        client_token: str = None,
        dry_run: bool = None,
        ipam_pool_description: str = None,
        ipam_pool_id: str = None,
        ipam_pool_name: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The new default network mask for the IPAM pool.
        # 
        # The mask must be **0 to 32** bits in length.
        self.allocation_default_cidr_mask = allocation_default_cidr_mask
        # The new maximum network mask for the IPAM pool.
        # 
        # The mask must be **0 to 32** bits in length.
        self.allocation_max_cidr_mask = allocation_max_cidr_mask
        # The new minimum network mask for the IPAM pool.
        # 
        # The mask must be **0 to 32** bits in length.
        self.allocation_min_cidr_mask = allocation_min_cidr_mask
        # Whether the pool has the auto-import feature enabled.
        self.auto_import = auto_import
        # Specifies whether to delete the default network mask for the IPAM pool. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.clear_allocation_default_cidr_mask = clear_allocation_default_cidr_mask
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The client token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the request ID as the client token. The request ID may be different for each request.
        self.client_token = client_token
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the DryRunOperation error code is returned.
        # *   **false** (default): performs a dry run and performs the actual request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The new description of the IPAM pool.
        # 
        # It must be 2 to 268 characters in length. It must start with a letter but cannot start with a `http://` or `https://`. This parameter is empty by default.
        self.ipam_pool_description = ipam_pool_description
        # The ID of the IPAM pool.
        # 
        # This parameter is required.
        self.ipam_pool_id = ipam_pool_id
        # The new name of the IPAM pool.
        # 
        # It must be 1 to 128 characters in length and cannot start with `http://` or `https://`.
        self.ipam_pool_name = ipam_pool_name
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the region where the IPAM instance is hosted. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allocation_default_cidr_mask is not None:
            result['AllocationDefaultCidrMask'] = self.allocation_default_cidr_mask
        if self.allocation_max_cidr_mask is not None:
            result['AllocationMaxCidrMask'] = self.allocation_max_cidr_mask
        if self.allocation_min_cidr_mask is not None:
            result['AllocationMinCidrMask'] = self.allocation_min_cidr_mask
        if self.auto_import is not None:
            result['AutoImport'] = self.auto_import
        if self.clear_allocation_default_cidr_mask is not None:
            result['ClearAllocationDefaultCidrMask'] = self.clear_allocation_default_cidr_mask
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.ipam_pool_description is not None:
            result['IpamPoolDescription'] = self.ipam_pool_description
        if self.ipam_pool_id is not None:
            result['IpamPoolId'] = self.ipam_pool_id
        if self.ipam_pool_name is not None:
            result['IpamPoolName'] = self.ipam_pool_name
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocationDefaultCidrMask') is not None:
            self.allocation_default_cidr_mask = m.get('AllocationDefaultCidrMask')
        if m.get('AllocationMaxCidrMask') is not None:
            self.allocation_max_cidr_mask = m.get('AllocationMaxCidrMask')
        if m.get('AllocationMinCidrMask') is not None:
            self.allocation_min_cidr_mask = m.get('AllocationMinCidrMask')
        if m.get('AutoImport') is not None:
            self.auto_import = m.get('AutoImport')
        if m.get('ClearAllocationDefaultCidrMask') is not None:
            self.clear_allocation_default_cidr_mask = m.get('ClearAllocationDefaultCidrMask')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IpamPoolDescription') is not None:
            self.ipam_pool_description = m.get('IpamPoolDescription')
        if m.get('IpamPoolId') is not None:
            self.ipam_pool_id = m.get('IpamPoolId')
        if m.get('IpamPoolName') is not None:
            self.ipam_pool_name = m.get('IpamPoolName')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class UpdateIpamPoolResponseBody(TeaModel):
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


class UpdateIpamPoolResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateIpamPoolResponseBody = None,
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
            temp_model = UpdateIpamPoolResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateIpamPoolAllocationRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        ipam_pool_allocation_description: str = None,
        ipam_pool_allocation_id: str = None,
        ipam_pool_allocation_name: str = None,
        region_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The client token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the request ID as the client token. The request ID may be different for each request.
        self.client_token = client_token
        # Specifies whether to precheck this request. Valid values:
        # 
        # *   **true**: performs a dry run without modifying the CIDR blocks of IPAM pools. The system checks the required parameters, request syntax, and limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the DryRunOperation error code is returned.
        # *   **false** (default): performs a dry run and the actual request. If the request passes the check, an HTTP 2xx status code is returned and the CIDR allocation information of the IPAM address pool is modified.
        self.dry_run = dry_run
        # The description of the CIDR allocation of the IPAM pool.
        # 
        # The description must be 1 to 256 characters in length and start with a letter, but cannot start with a `http://` or `https://`. This parameter is empty by default.
        self.ipam_pool_allocation_description = ipam_pool_allocation_description
        # The ID of the instance to which CIDR blocks are allocated from the IPAM pool.
        # 
        # This parameter is required.
        self.ipam_pool_allocation_id = ipam_pool_allocation_id
        # The name of the CIDR allocation of the IPAM pool.
        # 
        # It must be 1 to 128 characters in length and cannot start with `http://` or `https://`.
        self.ipam_pool_allocation_name = ipam_pool_allocation_name
        # The ID of the region where you want to perform the operation. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the region list.
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
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.ipam_pool_allocation_description is not None:
            result['IpamPoolAllocationDescription'] = self.ipam_pool_allocation_description
        if self.ipam_pool_allocation_id is not None:
            result['IpamPoolAllocationId'] = self.ipam_pool_allocation_id
        if self.ipam_pool_allocation_name is not None:
            result['IpamPoolAllocationName'] = self.ipam_pool_allocation_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IpamPoolAllocationDescription') is not None:
            self.ipam_pool_allocation_description = m.get('IpamPoolAllocationDescription')
        if m.get('IpamPoolAllocationId') is not None:
            self.ipam_pool_allocation_id = m.get('IpamPoolAllocationId')
        if m.get('IpamPoolAllocationName') is not None:
            self.ipam_pool_allocation_name = m.get('IpamPoolAllocationName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateIpamPoolAllocationResponseBody(TeaModel):
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


class UpdateIpamPoolAllocationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateIpamPoolAllocationResponseBody = None,
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
            temp_model = UpdateIpamPoolAllocationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateIpamResourceDiscoveryRequest(TeaModel):
    def __init__(
        self,
        add_operating_region: List[str] = None,
        client_token: str = None,
        dry_run: bool = None,
        ipam_resource_discovery_description: str = None,
        ipam_resource_discovery_id: str = None,
        ipam_resource_discovery_name: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        remove_operating_region: List[str] = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The list of effective regions to add.
        self.add_operating_region = add_operating_region
        # The client token used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The client token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the request ID as the client token. The request ID may be different for each request.
        self.client_token = client_token
        # Specifies whether to perform the dry run. Valid values:
        # 
        # *   **true**: Performs a dry run without modifying the resource discovery instance. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error code is returned. If the request passes the dry run, the DryRunOperation error code is returned.
        # *   **false** (default): Performs a dry run and the actual request. If the request passes the check, an HTTP 2xx status code is returned and the resource discovery instance is modified.
        self.dry_run = dry_run
        # The description of resource discovery.
        self.ipam_resource_discovery_description = ipam_resource_discovery_description
        # The ID of resource discovery instance.
        # 
        # This parameter is required.
        self.ipam_resource_discovery_id = ipam_resource_discovery_id
        # The name of the resource discovery.
        self.ipam_resource_discovery_name = ipam_resource_discovery_name
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The request region.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The list of effective regions to remove.
        self.remove_operating_region = remove_operating_region
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.add_operating_region is not None:
            result['AddOperatingRegion'] = self.add_operating_region
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.ipam_resource_discovery_description is not None:
            result['IpamResourceDiscoveryDescription'] = self.ipam_resource_discovery_description
        if self.ipam_resource_discovery_id is not None:
            result['IpamResourceDiscoveryId'] = self.ipam_resource_discovery_id
        if self.ipam_resource_discovery_name is not None:
            result['IpamResourceDiscoveryName'] = self.ipam_resource_discovery_name
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.remove_operating_region is not None:
            result['RemoveOperatingRegion'] = self.remove_operating_region
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddOperatingRegion') is not None:
            self.add_operating_region = m.get('AddOperatingRegion')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IpamResourceDiscoveryDescription') is not None:
            self.ipam_resource_discovery_description = m.get('IpamResourceDiscoveryDescription')
        if m.get('IpamResourceDiscoveryId') is not None:
            self.ipam_resource_discovery_id = m.get('IpamResourceDiscoveryId')
        if m.get('IpamResourceDiscoveryName') is not None:
            self.ipam_resource_discovery_name = m.get('IpamResourceDiscoveryName')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RemoveOperatingRegion') is not None:
            self.remove_operating_region = m.get('RemoveOperatingRegion')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class UpdateIpamResourceDiscoveryResponseBody(TeaModel):
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


class UpdateIpamResourceDiscoveryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateIpamResourceDiscoveryResponseBody = None,
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
            temp_model = UpdateIpamResourceDiscoveryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateIpamScopeRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        ipam_scope_description: str = None,
        ipam_scope_id: str = None,
        ipam_scope_name: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The client token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the request ID as the client token. The request ID may be different for each request.
        self.client_token = client_token
        # Specifies whether to perform only a dry run without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, DryRunOperation is returned.
        # *   **false** (default): performs a dry run and performs the actual request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The new description of the IPAM scope.
        # 
        # It must be 2 to 256 characters in length. It must start with a letter but cannot start with `http://` or `https://`. This parameter is empty by default.
        self.ipam_scope_description = ipam_scope_description
        # The ID of the IPAM scope.
        # 
        # This parameter is required.
        self.ipam_scope_id = ipam_scope_id
        # The new name of the IPAM scope.
        # 
        # It must be 1 to 128 characters in length and cannot start with `http://` or `https://`.
        self.ipam_scope_name = ipam_scope_name
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the region where the IPAM instance is hosted. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.ipam_scope_description is not None:
            result['IpamScopeDescription'] = self.ipam_scope_description
        if self.ipam_scope_id is not None:
            result['IpamScopeId'] = self.ipam_scope_id
        if self.ipam_scope_name is not None:
            result['IpamScopeName'] = self.ipam_scope_name
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IpamScopeDescription') is not None:
            self.ipam_scope_description = m.get('IpamScopeDescription')
        if m.get('IpamScopeId') is not None:
            self.ipam_scope_id = m.get('IpamScopeId')
        if m.get('IpamScopeName') is not None:
            self.ipam_scope_name = m.get('IpamScopeName')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class UpdateIpamScopeResponseBody(TeaModel):
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


class UpdateIpamScopeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateIpamScopeResponseBody = None,
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
            temp_model = UpdateIpamScopeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


