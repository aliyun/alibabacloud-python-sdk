# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class CommitContainerRequestAcrRegistryInfo(TeaModel):
    def __init__(
        self,
        arn_service: str = None,
        arn_user: str = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        # The Alibaba Cloud Resource Access (ARN) of the RAM role that is assigned to the user (the authorized account) in cross-account authorization scenarios.
        self.arn_service = arn_service
        # The ARN of the RAM role that is assigned to the authorizer in cross-account authorization scenarios.
        self.arn_user = arn_user
        # The ID of the Container Registry Enterprise Edition instance.
        self.instance_id = instance_id
        # The region ID of the Container Registry Enterprise Edition instance.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn_service is not None:
            result['ArnService'] = self.arn_service
        if self.arn_user is not None:
            result['ArnUser'] = self.arn_user
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArnService') is not None:
            self.arn_service = m.get('ArnService')
        if m.get('ArnUser') is not None:
            self.arn_user = m.get('ArnUser')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CommitContainerRequestArn(TeaModel):
    def __init__(
        self,
        role_arn: str = None,
        role_type: str = None,
    ):
        # The ARN of the authorized role.
        self.role_arn = role_arn
        # The authorization type. A value of service indicates that RAM roles are used for authorization.
        self.role_type = role_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn
        if self.role_type is not None:
            result['RoleType'] = self.role_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')
        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')
        return self


class CommitContainerRequestImage(TeaModel):
    def __init__(
        self,
        author: str = None,
        message: str = None,
        repository: str = None,
        tag: str = None,
    ):
        # The authorization of the image.
        self.author = author
        # The message about the image.
        self.message = message
        # The image repository.
        # 
        # This parameter is required.
        self.repository = repository
        # The tag of the image. This parameter is empty by default, which indicates that the tag is not modified.
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
        if self.author is not None:
            result['Author'] = self.author
        if self.message is not None:
            result['Message'] = self.message
        if self.repository is not None:
            result['Repository'] = self.repository
        if self.tag is not None:
            result['Tag'] = self.tag
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Author') is not None:
            self.author = m.get('Author')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Repository') is not None:
            self.repository = m.get('Repository')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        return self


class CommitContainerRequest(TeaModel):
    def __init__(
        self,
        acr_registry_info: CommitContainerRequestAcrRegistryInfo = None,
        arn: CommitContainerRequestArn = None,
        container_group_id: str = None,
        container_name: str = None,
        image: CommitContainerRequestImage = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The access credential configurations of the Container Registry Enterprise Edition instance.
        # 
        # >  If you use a Container Registry Personal Edition instance, you do not need to configure this parameter. If you use a Container Registry Enterprise Edition instance, you must configure this parameter.
        self.acr_registry_info = acr_registry_info
        # The details about the ARN that is required for authorization.
        self.arn = arn
        # The ID of the container group.
        # 
        # This parameter is required.
        self.container_group_id = container_group_id
        # The name of the container.
        # 
        # This parameter is required.
        self.container_name = container_name
        # The image of the container.
        self.image = image
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        if self.acr_registry_info:
            self.acr_registry_info.validate()
        if self.arn:
            self.arn.validate()
        if self.image:
            self.image.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acr_registry_info is not None:
            result['AcrRegistryInfo'] = self.acr_registry_info.to_map()
        if self.arn is not None:
            result['Arn'] = self.arn.to_map()
        if self.container_group_id is not None:
            result['ContainerGroupId'] = self.container_group_id
        if self.container_name is not None:
            result['ContainerName'] = self.container_name
        if self.image is not None:
            result['Image'] = self.image.to_map()
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
        if m.get('AcrRegistryInfo') is not None:
            temp_model = CommitContainerRequestAcrRegistryInfo()
            self.acr_registry_info = temp_model.from_map(m['AcrRegistryInfo'])
        if m.get('Arn') is not None:
            temp_model = CommitContainerRequestArn()
            self.arn = temp_model.from_map(m['Arn'])
        if m.get('ContainerGroupId') is not None:
            self.container_group_id = m.get('ContainerGroupId')
        if m.get('ContainerName') is not None:
            self.container_name = m.get('ContainerName')
        if m.get('Image') is not None:
            temp_model = CommitContainerRequestImage()
            self.image = temp_model.from_map(m['Image'])
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


class CommitContainerResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The ID of the task.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CommitContainerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CommitContainerResponseBody = None,
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
            temp_model = CommitContainerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CopyDataCacheRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag.
        self.key = key
        # The value of the tag.
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


class CopyDataCacheRequest(TeaModel):
    def __init__(
        self,
        bucket: str = None,
        client_token: str = None,
        data_cache_id: str = None,
        destination_region_id: str = None,
        name: str = None,
        owner_account: str = None,
        owner_id: int = None,
        path: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        retention_days: int = None,
        tag: List[CopyDataCacheRequestTag] = None,
    ):
        # The bucket in which the DataCache is stored.
        self.bucket = bucket
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The ID of the DataCache in the source region.
        # 
        # This parameter is required.
        self.data_cache_id = data_cache_id
        # The destination region of the DataCache.
        # 
        # This parameter is required.
        self.destination_region_id = destination_region_id
        # The DataCache name.
        self.name = name
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The storage path of the data.
        self.path = path
        # The source region of the DataCache.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource group to which the DataCache belongs.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The number of days for which the DataCache is retained.
        self.retention_days = retention_days
        # The tags of the DataCache.
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
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.data_cache_id is not None:
            result['DataCacheId'] = self.data_cache_id
        if self.destination_region_id is not None:
            result['DestinationRegionId'] = self.destination_region_id
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.path is not None:
            result['Path'] = self.path
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.retention_days is not None:
            result['RetentionDays'] = self.retention_days
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DataCacheId') is not None:
            self.data_cache_id = m.get('DataCacheId')
        if m.get('DestinationRegionId') is not None:
            self.destination_region_id = m.get('DestinationRegionId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RetentionDays') is not None:
            self.retention_days = m.get('RetentionDays')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CopyDataCacheRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class CopyDataCacheResponseBody(TeaModel):
    def __init__(
        self,
        data_cache_id: str = None,
        request_id: str = None,
    ):
        # The ID generated for the DataCache in the destination region.
        self.data_cache_id = data_cache_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_cache_id is not None:
            result['DataCacheId'] = self.data_cache_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataCacheId') is not None:
            self.data_cache_id = m.get('DataCacheId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CopyDataCacheResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CopyDataCacheResponseBody = None,
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
            temp_model = CopyDataCacheResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateContainerGroupRequestDnsConfigOption(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The name of the option.
        self.name = name
        # The value of the option.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateContainerGroupRequestDnsConfig(TeaModel):
    def __init__(
        self,
        name_server: List[str] = None,
        option: List[CreateContainerGroupRequestDnsConfigOption] = None,
        search: List[str] = None,
    ):
        # The IP addresses of DNS servers.
        self.name_server = name_server
        # Configuration options of the DNS server.
        self.option = option
        # The search domains of DNS servers.
        self.search = search

    def validate(self):
        if self.option:
            for k in self.option:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name_server is not None:
            result['NameServer'] = self.name_server
        result['Option'] = []
        if self.option is not None:
            for k in self.option:
                result['Option'].append(k.to_map() if k else None)
        if self.search is not None:
            result['Search'] = self.search
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NameServer') is not None:
            self.name_server = m.get('NameServer')
        self.option = []
        if m.get('Option') is not None:
            for k in m.get('Option'):
                temp_model = CreateContainerGroupRequestDnsConfigOption()
                self.option.append(temp_model.from_map(k))
        if m.get('Search') is not None:
            self.search = m.get('Search')
        return self


class CreateContainerGroupRequestHostSecurityContextSysctl(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The name of the unsafe sysctl when you modify sysctls by configuring a security context. Valid values:
        # 
        # *   kernel.shm \\* (except kernel.shm_rmid_forced)
        # *   kernel.msg\\*\
        # *   kernel.sem
        # *   fs.mqueue.\\*\
        # *   net.\\*(except net.ipv4.tcp_syncookies, net.ipv4.ping_group_range, and net.ipv4.ip_unprivileged_port_start)
        self.name = name
        # The value of the unsafe sysctl when you modify sysctls by configuring a security context.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateContainerGroupRequestHostSecurityContext(TeaModel):
    def __init__(
        self,
        sysctl: List[CreateContainerGroupRequestHostSecurityContextSysctl] = None,
    ):
        # Configure a security context to modify unsafe sysctls. For more information, see [Configure a security context](https://help.aliyun.com/document_detail/462313.html).
        self.sysctl = sysctl

    def validate(self):
        if self.sysctl:
            for k in self.sysctl:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Sysctl'] = []
        if self.sysctl is not None:
            for k in self.sysctl:
                result['Sysctl'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.sysctl = []
        if m.get('Sysctl') is not None:
            for k in m.get('Sysctl'):
                temp_model = CreateContainerGroupRequestHostSecurityContextSysctl()
                self.sysctl.append(temp_model.from_map(k))
        return self


class CreateContainerGroupRequestSecurityContextSysctl(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The name of the safe sysctl when you modify sysctls by configuring a security context. Valid values:
        # 
        # *   net.ipv4.ping_group_range
        # *   net.ipv4.ip_unprivileged_port_start
        self.name = name
        # The value of the safe sysctl when you modify sysctls by configuring a security context.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateContainerGroupRequestSecurityContext(TeaModel):
    def __init__(
        self,
        sysctl: List[CreateContainerGroupRequestSecurityContextSysctl] = None,
    ):
        # Configure a security context to modify safe sysctls. For more information, see [Configure a security context](https://help.aliyun.com/document_detail/462313.html).
        self.sysctl = sysctl

    def validate(self):
        if self.sysctl:
            for k in self.sysctl:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Sysctl'] = []
        if self.sysctl is not None:
            for k in self.sysctl:
                result['Sysctl'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.sysctl = []
        if m.get('Sysctl') is not None:
            for k in m.get('Sysctl'):
                temp_model = CreateContainerGroupRequestSecurityContextSysctl()
                self.sysctl.append(temp_model.from_map(k))
        return self


class CreateContainerGroupRequestAcrRegistryInfo(TeaModel):
    def __init__(
        self,
        arn_service: str = None,
        arn_user: str = None,
        domain: List[str] = None,
        instance_id: str = None,
        instance_name: str = None,
        region_id: str = None,
    ):
        # The Alibaba Cloud Resource Name (ARN) of the RAM role in the Alibaba Cloud account to which the elastic container instance belongs.
        self.arn_service = arn_service
        # The ARN of the RAM role in the Alibaba Cloud account to which the Container Registry Enterprise Edition instance belongs.
        self.arn_user = arn_user
        # The domain names of the Container Registry Enterprise Edition instance. By default, all domain names of the instance are displayed. You can specify multiple domain names. Separate multiple domain names with commas (,).
        self.domain = domain
        # The ID of the Container Registry Enterprise Edition instance.
        self.instance_id = instance_id
        # The name of the Container Registry Enterprise Edition instance.
        self.instance_name = instance_name
        # The region ID of the Container Registry Enterprise Edition instance.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn_service is not None:
            result['ArnService'] = self.arn_service
        if self.arn_user is not None:
            result['ArnUser'] = self.arn_user
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArnService') is not None:
            self.arn_service = m.get('ArnService')
        if m.get('ArnUser') is not None:
            self.arn_user = m.get('ArnUser')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateContainerGroupRequestContainerLivenessProbeExec(TeaModel):
    def __init__(
        self,
        command: List[str] = None,
    ):
        self.command = command

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.command is not None:
            result['Command'] = self.command
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Command') is not None:
            self.command = m.get('Command')
        return self


class CreateContainerGroupRequestContainerLivenessProbeHttpGet(TeaModel):
    def __init__(
        self,
        path: str = None,
        port: int = None,
        scheme: str = None,
    ):
        self.path = path
        self.port = port
        self.scheme = scheme

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.path is not None:
            result['Path'] = self.path
        if self.port is not None:
            result['Port'] = self.port
        if self.scheme is not None:
            result['Scheme'] = self.scheme
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Scheme') is not None:
            self.scheme = m.get('Scheme')
        return self


class CreateContainerGroupRequestContainerLivenessProbeTcpSocket(TeaModel):
    def __init__(
        self,
        port: int = None,
    ):
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class CreateContainerGroupRequestContainerLivenessProbe(TeaModel):
    def __init__(
        self,
        exec: CreateContainerGroupRequestContainerLivenessProbeExec = None,
        failure_threshold: int = None,
        http_get: CreateContainerGroupRequestContainerLivenessProbeHttpGet = None,
        initial_delay_seconds: int = None,
        period_seconds: int = None,
        success_threshold: int = None,
        tcp_socket: CreateContainerGroupRequestContainerLivenessProbeTcpSocket = None,
        timeout_seconds: int = None,
    ):
        self.exec = exec
        self.failure_threshold = failure_threshold
        self.http_get = http_get
        self.initial_delay_seconds = initial_delay_seconds
        self.period_seconds = period_seconds
        self.success_threshold = success_threshold
        self.tcp_socket = tcp_socket
        self.timeout_seconds = timeout_seconds

    def validate(self):
        if self.exec:
            self.exec.validate()
        if self.http_get:
            self.http_get.validate()
        if self.tcp_socket:
            self.tcp_socket.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exec is not None:
            result['Exec'] = self.exec.to_map()
        if self.failure_threshold is not None:
            result['FailureThreshold'] = self.failure_threshold
        if self.http_get is not None:
            result['HttpGet'] = self.http_get.to_map()
        if self.initial_delay_seconds is not None:
            result['InitialDelaySeconds'] = self.initial_delay_seconds
        if self.period_seconds is not None:
            result['PeriodSeconds'] = self.period_seconds
        if self.success_threshold is not None:
            result['SuccessThreshold'] = self.success_threshold
        if self.tcp_socket is not None:
            result['TcpSocket'] = self.tcp_socket.to_map()
        if self.timeout_seconds is not None:
            result['TimeoutSeconds'] = self.timeout_seconds
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Exec') is not None:
            temp_model = CreateContainerGroupRequestContainerLivenessProbeExec()
            self.exec = temp_model.from_map(m['Exec'])
        if m.get('FailureThreshold') is not None:
            self.failure_threshold = m.get('FailureThreshold')
        if m.get('HttpGet') is not None:
            temp_model = CreateContainerGroupRequestContainerLivenessProbeHttpGet()
            self.http_get = temp_model.from_map(m['HttpGet'])
        if m.get('InitialDelaySeconds') is not None:
            self.initial_delay_seconds = m.get('InitialDelaySeconds')
        if m.get('PeriodSeconds') is not None:
            self.period_seconds = m.get('PeriodSeconds')
        if m.get('SuccessThreshold') is not None:
            self.success_threshold = m.get('SuccessThreshold')
        if m.get('TcpSocket') is not None:
            temp_model = CreateContainerGroupRequestContainerLivenessProbeTcpSocket()
            self.tcp_socket = temp_model.from_map(m['TcpSocket'])
        if m.get('TimeoutSeconds') is not None:
            self.timeout_seconds = m.get('TimeoutSeconds')
        return self


class CreateContainerGroupRequestContainerReadinessProbeExec(TeaModel):
    def __init__(
        self,
        command: List[str] = None,
    ):
        self.command = command

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.command is not None:
            result['Command'] = self.command
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Command') is not None:
            self.command = m.get('Command')
        return self


class CreateContainerGroupRequestContainerReadinessProbeHttpGet(TeaModel):
    def __init__(
        self,
        path: str = None,
        port: int = None,
        scheme: str = None,
    ):
        self.path = path
        self.port = port
        self.scheme = scheme

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.path is not None:
            result['Path'] = self.path
        if self.port is not None:
            result['Port'] = self.port
        if self.scheme is not None:
            result['Scheme'] = self.scheme
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Scheme') is not None:
            self.scheme = m.get('Scheme')
        return self


class CreateContainerGroupRequestContainerReadinessProbeTcpSocket(TeaModel):
    def __init__(
        self,
        port: int = None,
    ):
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class CreateContainerGroupRequestContainerReadinessProbe(TeaModel):
    def __init__(
        self,
        exec: CreateContainerGroupRequestContainerReadinessProbeExec = None,
        failure_threshold: int = None,
        http_get: CreateContainerGroupRequestContainerReadinessProbeHttpGet = None,
        initial_delay_seconds: int = None,
        period_seconds: int = None,
        success_threshold: int = None,
        tcp_socket: CreateContainerGroupRequestContainerReadinessProbeTcpSocket = None,
        timeout_seconds: int = None,
    ):
        self.exec = exec
        self.failure_threshold = failure_threshold
        self.http_get = http_get
        self.initial_delay_seconds = initial_delay_seconds
        self.period_seconds = period_seconds
        self.success_threshold = success_threshold
        self.tcp_socket = tcp_socket
        self.timeout_seconds = timeout_seconds

    def validate(self):
        if self.exec:
            self.exec.validate()
        if self.http_get:
            self.http_get.validate()
        if self.tcp_socket:
            self.tcp_socket.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exec is not None:
            result['Exec'] = self.exec.to_map()
        if self.failure_threshold is not None:
            result['FailureThreshold'] = self.failure_threshold
        if self.http_get is not None:
            result['HttpGet'] = self.http_get.to_map()
        if self.initial_delay_seconds is not None:
            result['InitialDelaySeconds'] = self.initial_delay_seconds
        if self.period_seconds is not None:
            result['PeriodSeconds'] = self.period_seconds
        if self.success_threshold is not None:
            result['SuccessThreshold'] = self.success_threshold
        if self.tcp_socket is not None:
            result['TcpSocket'] = self.tcp_socket.to_map()
        if self.timeout_seconds is not None:
            result['TimeoutSeconds'] = self.timeout_seconds
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Exec') is not None:
            temp_model = CreateContainerGroupRequestContainerReadinessProbeExec()
            self.exec = temp_model.from_map(m['Exec'])
        if m.get('FailureThreshold') is not None:
            self.failure_threshold = m.get('FailureThreshold')
        if m.get('HttpGet') is not None:
            temp_model = CreateContainerGroupRequestContainerReadinessProbeHttpGet()
            self.http_get = temp_model.from_map(m['HttpGet'])
        if m.get('InitialDelaySeconds') is not None:
            self.initial_delay_seconds = m.get('InitialDelaySeconds')
        if m.get('PeriodSeconds') is not None:
            self.period_seconds = m.get('PeriodSeconds')
        if m.get('SuccessThreshold') is not None:
            self.success_threshold = m.get('SuccessThreshold')
        if m.get('TcpSocket') is not None:
            temp_model = CreateContainerGroupRequestContainerReadinessProbeTcpSocket()
            self.tcp_socket = temp_model.from_map(m['TcpSocket'])
        if m.get('TimeoutSeconds') is not None:
            self.timeout_seconds = m.get('TimeoutSeconds')
        return self


class CreateContainerGroupRequestContainerSecurityContextCapability(TeaModel):
    def __init__(
        self,
        add: List[str] = None,
    ):
        self.add = add

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.add is not None:
            result['Add'] = self.add
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Add') is not None:
            self.add = m.get('Add')
        return self


class CreateContainerGroupRequestContainerSecurityContext(TeaModel):
    def __init__(
        self,
        capability: CreateContainerGroupRequestContainerSecurityContextCapability = None,
        read_only_root_filesystem: bool = None,
        run_as_user: int = None,
    ):
        self.capability = capability
        self.read_only_root_filesystem = read_only_root_filesystem
        self.run_as_user = run_as_user

    def validate(self):
        if self.capability:
            self.capability.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.capability is not None:
            result['Capability'] = self.capability.to_map()
        if self.read_only_root_filesystem is not None:
            result['ReadOnlyRootFilesystem'] = self.read_only_root_filesystem
        if self.run_as_user is not None:
            result['RunAsUser'] = self.run_as_user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Capability') is not None:
            temp_model = CreateContainerGroupRequestContainerSecurityContextCapability()
            self.capability = temp_model.from_map(m['Capability'])
        if m.get('ReadOnlyRootFilesystem') is not None:
            self.read_only_root_filesystem = m.get('ReadOnlyRootFilesystem')
        if m.get('RunAsUser') is not None:
            self.run_as_user = m.get('RunAsUser')
        return self


class CreateContainerGroupRequestContainerEnvironmentVarFieldRef(TeaModel):
    def __init__(
        self,
        field_path: str = None,
    ):
        self.field_path = field_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_path is not None:
            result['FieldPath'] = self.field_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldPath') is not None:
            self.field_path = m.get('FieldPath')
        return self


class CreateContainerGroupRequestContainerEnvironmentVar(TeaModel):
    def __init__(
        self,
        field_ref: CreateContainerGroupRequestContainerEnvironmentVarFieldRef = None,
        key: str = None,
        value: str = None,
    ):
        self.field_ref = field_ref
        # The name of the environment variable. The name must be 1 to 128 bits in length and can contain letters, digits, and underscores (_). It cannot start with a digit.``
        self.key = key
        # The value of the environment variable. The value can be up to 256 characters in length.
        self.value = value

    def validate(self):
        if self.field_ref:
            self.field_ref.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_ref is not None:
            result['FieldRef'] = self.field_ref.to_map()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldRef') is not None:
            temp_model = CreateContainerGroupRequestContainerEnvironmentVarFieldRef()
            self.field_ref = temp_model.from_map(m['FieldRef'])
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateContainerGroupRequestContainerLifecyclePostStartHandlerHttpGetHttpHeader(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The name of the custom field in the HTTP GET request header when you use HTTP requests to specify a postStart hook.
        self.name = name
        # The value of the custom field in the HTTP GET request header when you use HTTP requests to specify a postStart hook.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateContainerGroupRequestContainerLifecyclePreStopHandlerHttpGetHttpHeader(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The name of the custom field in the HTTP GET request header when you use HTTP requests to specify a presto hook.
        self.name = name
        # The value of the custom field in the HTTP GET request header when you use HTTP requests to specify a preStop hook.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateContainerGroupRequestContainerPort(TeaModel):
    def __init__(
        self,
        port: int = None,
        protocol: str = None,
    ):
        # The port number. Valid values: 1 to 65535.
        self.port = port
        # The type of the protocol. Valid values:
        # 
        # *   TCP
        # *   UDP
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.port is not None:
            result['Port'] = self.port
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        return self


class CreateContainerGroupRequestContainerVolumeMount(TeaModel):
    def __init__(
        self,
        mount_path: str = None,
        mount_propagation: str = None,
        name: str = None,
        read_only: bool = None,
        sub_path: str = None,
    ):
        # The directory to which the volume is mounted.
        # 
        # >  The data stored in this directory is overwritten by the data on the volume. Specify this parameter with caution.
        self.mount_path = mount_path
        # The mount propagation settings of the volume. Mount propagation allows volumes that are mounted on one container to be shared with other containers in the same pod, or even with other pods on the same node. Valid values:
        # 
        # *   None: The volume mount does not receive subsequent mounts that are performed on this volume or subdirectories of this volume.
        # *   HostToCotainer: The volume mount receives subsequent mounts that are performed on this volume or the subdirectories of this volume.
        # *   Bidirectional: This value is similar to HostToContainer. The volume mount receives subsequent mounts that are performed on this volume or the subdirectories of this volume. In addition, all volume mounts that are mounted on the container are propagated back to the host and all containers of all pods that use the same volume.
        # 
        # Default value: None.
        self.mount_propagation = mount_propagation
        # The name of the volume. The value of this parameter is the same as the value of Volume.N.Name.
        self.name = name
        # Specifies whether the volume is read-only. Default value: false.
        self.read_only = read_only
        # The subdirectory of the volume.
        self.sub_path = sub_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mount_path is not None:
            result['MountPath'] = self.mount_path
        if self.mount_propagation is not None:
            result['MountPropagation'] = self.mount_propagation
        if self.name is not None:
            result['Name'] = self.name
        if self.read_only is not None:
            result['ReadOnly'] = self.read_only
        if self.sub_path is not None:
            result['SubPath'] = self.sub_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')
        if m.get('MountPropagation') is not None:
            self.mount_propagation = m.get('MountPropagation')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ReadOnly') is not None:
            self.read_only = m.get('ReadOnly')
        if m.get('SubPath') is not None:
            self.sub_path = m.get('SubPath')
        return self


class CreateContainerGroupRequestContainer(TeaModel):
    def __init__(
        self,
        liveness_probe: CreateContainerGroupRequestContainerLivenessProbe = None,
        readiness_probe: CreateContainerGroupRequestContainerReadinessProbe = None,
        security_context: CreateContainerGroupRequestContainerSecurityContext = None,
        arg: List[str] = None,
        command: List[str] = None,
        cpu: float = None,
        environment_var: List[CreateContainerGroupRequestContainerEnvironmentVar] = None,
        environment_var_hide: bool = None,
        gpu: int = None,
        image: str = None,
        image_pull_policy: str = None,
        lifecycle_post_start_handler_exec: List[str] = None,
        lifecycle_post_start_handler_http_get_host: str = None,
        lifecycle_post_start_handler_http_get_http_header: List[CreateContainerGroupRequestContainerLifecyclePostStartHandlerHttpGetHttpHeader] = None,
        lifecycle_post_start_handler_http_get_path: str = None,
        lifecycle_post_start_handler_http_get_port: int = None,
        lifecycle_post_start_handler_http_get_scheme: str = None,
        lifecycle_post_start_handler_tcp_socket_host: str = None,
        lifecycle_post_start_handler_tcp_socket_port: int = None,
        lifecycle_pre_stop_handler_exec: List[str] = None,
        lifecycle_pre_stop_handler_http_get_host: str = None,
        lifecycle_pre_stop_handler_http_get_http_header: List[CreateContainerGroupRequestContainerLifecyclePreStopHandlerHttpGetHttpHeader] = None,
        lifecycle_pre_stop_handler_http_get_path: str = None,
        lifecycle_pre_stop_handler_http_get_port: int = None,
        lifecycle_pre_stop_handler_http_get_scheme: str = None,
        lifecycle_pre_stop_handler_tcp_socket_host: str = None,
        lifecycle_pre_stop_handler_tcp_socket_port: int = None,
        memory: float = None,
        name: str = None,
        port: List[CreateContainerGroupRequestContainerPort] = None,
        security_context_privileged: bool = None,
        security_context_run_as_group: int = None,
        security_context_run_as_non_root: bool = None,
        stdin: bool = None,
        stdin_once: bool = None,
        termination_message_path: str = None,
        termination_message_policy: str = None,
        tty: bool = None,
        volume_mount: List[CreateContainerGroupRequestContainerVolumeMount] = None,
        working_dir: str = None,
    ):
        self.liveness_probe = liveness_probe
        self.readiness_probe = readiness_probe
        self.security_context = security_context
        # The arguments that are passed to the startup command of the container. You can specify up to 10 arguments.
        self.arg = arg
        # The commands to be executed in containers when you use a CLI to perform health checks.
        # 
        # >  When you configure ReadinessProbe-related parameters, you can select only one of the HttpGet, Exec, and TcpSocket check methods.
        self.command = command
        # The number of vCPUs that are allocated to the container.
        self.cpu = cpu
        # The environment variables of the container.
        self.environment_var = environment_var
        # Specifies whether to hide the information about environment variables when you query the details of an elastic container instance. Valid values:
        # 
        # *   false
        # *   true If environment variables contain sensitive information, you can set this parameter to true to improve security of the information.
        self.environment_var_hide = environment_var_hide
        # The number of GPUs that you want to allocate to the container.
        self.gpu = gpu
        # The image of the container.
        # 
        # This parameter is required.
        self.image = image
        # The policy that you want to use to pull images. Valid values:
        # 
        # *   Always: Each time instances are created, image pulling is performed.
        # *   IfNotPresent: On-premises images are preferentially used. If no on-premises images are available, image pulling is performed.
        # *   Never: On-premises images are always used. Image pulling is not performed.
        self.image_pull_policy = image_pull_policy
        # The commands to be executed in containers when you use a CLI to specify a postStart hook.
        self.lifecycle_post_start_handler_exec = lifecycle_post_start_handler_exec
        # The IP address of the host that receives the HTTP GET request when you use an HTTP request to specify a postStart hook.
        self.lifecycle_post_start_handler_http_get_host = lifecycle_post_start_handler_http_get_host
        # The HTTP GET request header.
        self.lifecycle_post_start_handler_http_get_http_header = lifecycle_post_start_handler_http_get_http_header
        # The path to which the system sends an HTTP GET request for a health check when you use an HTTP request to specify a postStart hook.
        self.lifecycle_post_start_handler_http_get_path = lifecycle_post_start_handler_http_get_path
        # The port to which the system sends an HTTP GET request when you use an HTTP request to specify a postStart hook.
        self.lifecycle_post_start_handler_http_get_port = lifecycle_post_start_handler_http_get_port
        # The protocol type of HTTP GET requests when you use HTTP requests to specify a postStart hook. Valid values:
        # 
        # *   HTTP
        # *   HTTPS
        self.lifecycle_post_start_handler_http_get_scheme = lifecycle_post_start_handler_http_get_scheme
        # The IP address of the host that receives the TCP socket request when you use a TCP socket request to specify a postStart hook.
        self.lifecycle_post_start_handler_tcp_socket_host = lifecycle_post_start_handler_tcp_socket_host
        # The port to which the system sends a TCP socket request for a health check when you use TCP sockets to specify a postStart hook.
        self.lifecycle_post_start_handler_tcp_socket_port = lifecycle_post_start_handler_tcp_socket_port
        # The commands to be executed in containers when you use a CLI to specify a preStop hook.
        self.lifecycle_pre_stop_handler_exec = lifecycle_pre_stop_handler_exec
        # The IP address of the host that receives the HTTP GET request when you use an HTTP request to specify a preStop hook.
        self.lifecycle_pre_stop_handler_http_get_host = lifecycle_pre_stop_handler_http_get_host
        # The HTTP GET request header.
        self.lifecycle_pre_stop_handler_http_get_http_header = lifecycle_pre_stop_handler_http_get_http_header
        # The path to which the system sends an HTTP GET request for a health check when you use an HTTP request to specify a preSop hook.
        self.lifecycle_pre_stop_handler_http_get_path = lifecycle_pre_stop_handler_http_get_path
        # The port to which the system sends an HTTP GET request for a health check when you use HTTP requests to specify a preStop hook.
        self.lifecycle_pre_stop_handler_http_get_port = lifecycle_pre_stop_handler_http_get_port
        # The protocol type of the HTTP GET request when you use an HTTP request to specify a preStop hook. Valid values:
        # 
        # *   HTTP
        # *   HTTPS
        self.lifecycle_pre_stop_handler_http_get_scheme = lifecycle_pre_stop_handler_http_get_scheme
        # The IP address of the host that receives the TCP socket request when you use a TCP socket request to specify a preStop hook.
        self.lifecycle_pre_stop_handler_tcp_socket_host = lifecycle_pre_stop_handler_tcp_socket_host
        # The port to which the system sends a TCP socket request for a health check when you use TCP sockets to specify a preStop hook.
        self.lifecycle_pre_stop_handler_tcp_socket_port = lifecycle_pre_stop_handler_tcp_socket_port
        # The memory size of the container. Unit: GiB.
        self.memory = memory
        # The name of the container.
        # 
        # This parameter is required.
        self.name = name
        # The port to which the system sends an HTTP GET request for a health check when you use HTTP requests to perform health checks.
        # 
        # >  When you configure LivenessProbe-related parameters, you can select only one of the HttpGet, Exec, and TcpSocket check methods.
        self.port = port
        self.security_context_privileged = security_context_privileged
        # The user group that runs the container.
        self.security_context_run_as_group = security_context_run_as_group
        # Specifies whether to run the container as a non-root user.
        self.security_context_run_as_non_root = security_context_run_as_non_root
        # Specifies whether the container allocates buffer resources to standard input streams when the container is running. If you do not specify this parameter, an end-of-file (EOF) error may occur when standard input streams in the container are read. Default value: false.
        self.stdin = stdin
        # Specifies whether standard input streams are disconnected from multiple sessions after a client is disconnected.\\
        # If StdinOnce is set to true, standard input streams are connected after the container is started, and remain idle until a client is connected to receive data. After the client is disconnected, standard input streams are also disconnected, and remain disconnected until the container restarts.
        self.stdin_once = stdin_once
        # The path of the file from which the system retrieves termination messages of the container when the container exits.
        self.termination_message_path = termination_message_path
        # The message notification policy. This parameter is empty by default. Only Message Service (MNS) queue message notifications can be sent.
        self.termination_message_policy = termination_message_policy
        # Specifies whether to enable interaction. Default value: false.
        # 
        # If the command is a /bin/bash command, set the value to true.
        self.tty = tty
        # The information about the volume that you want to mount on the container.
        self.volume_mount = volume_mount
        # The working directory of the container.
        self.working_dir = working_dir

    def validate(self):
        if self.liveness_probe:
            self.liveness_probe.validate()
        if self.readiness_probe:
            self.readiness_probe.validate()
        if self.security_context:
            self.security_context.validate()
        if self.environment_var:
            for k in self.environment_var:
                if k:
                    k.validate()
        if self.lifecycle_post_start_handler_http_get_http_header:
            for k in self.lifecycle_post_start_handler_http_get_http_header:
                if k:
                    k.validate()
        if self.lifecycle_pre_stop_handler_http_get_http_header:
            for k in self.lifecycle_pre_stop_handler_http_get_http_header:
                if k:
                    k.validate()
        if self.port:
            for k in self.port:
                if k:
                    k.validate()
        if self.volume_mount:
            for k in self.volume_mount:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.liveness_probe is not None:
            result['LivenessProbe'] = self.liveness_probe.to_map()
        if self.readiness_probe is not None:
            result['ReadinessProbe'] = self.readiness_probe.to_map()
        if self.security_context is not None:
            result['SecurityContext'] = self.security_context.to_map()
        if self.arg is not None:
            result['Arg'] = self.arg
        if self.command is not None:
            result['Command'] = self.command
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        result['EnvironmentVar'] = []
        if self.environment_var is not None:
            for k in self.environment_var:
                result['EnvironmentVar'].append(k.to_map() if k else None)
        if self.environment_var_hide is not None:
            result['EnvironmentVarHide'] = self.environment_var_hide
        if self.gpu is not None:
            result['Gpu'] = self.gpu
        if self.image is not None:
            result['Image'] = self.image
        if self.image_pull_policy is not None:
            result['ImagePullPolicy'] = self.image_pull_policy
        if self.lifecycle_post_start_handler_exec is not None:
            result['LifecyclePostStartHandlerExec'] = self.lifecycle_post_start_handler_exec
        if self.lifecycle_post_start_handler_http_get_host is not None:
            result['LifecyclePostStartHandlerHttpGetHost'] = self.lifecycle_post_start_handler_http_get_host
        result['LifecyclePostStartHandlerHttpGetHttpHeader'] = []
        if self.lifecycle_post_start_handler_http_get_http_header is not None:
            for k in self.lifecycle_post_start_handler_http_get_http_header:
                result['LifecyclePostStartHandlerHttpGetHttpHeader'].append(k.to_map() if k else None)
        if self.lifecycle_post_start_handler_http_get_path is not None:
            result['LifecyclePostStartHandlerHttpGetPath'] = self.lifecycle_post_start_handler_http_get_path
        if self.lifecycle_post_start_handler_http_get_port is not None:
            result['LifecyclePostStartHandlerHttpGetPort'] = self.lifecycle_post_start_handler_http_get_port
        if self.lifecycle_post_start_handler_http_get_scheme is not None:
            result['LifecyclePostStartHandlerHttpGetScheme'] = self.lifecycle_post_start_handler_http_get_scheme
        if self.lifecycle_post_start_handler_tcp_socket_host is not None:
            result['LifecyclePostStartHandlerTcpSocketHost'] = self.lifecycle_post_start_handler_tcp_socket_host
        if self.lifecycle_post_start_handler_tcp_socket_port is not None:
            result['LifecyclePostStartHandlerTcpSocketPort'] = self.lifecycle_post_start_handler_tcp_socket_port
        if self.lifecycle_pre_stop_handler_exec is not None:
            result['LifecyclePreStopHandlerExec'] = self.lifecycle_pre_stop_handler_exec
        if self.lifecycle_pre_stop_handler_http_get_host is not None:
            result['LifecyclePreStopHandlerHttpGetHost'] = self.lifecycle_pre_stop_handler_http_get_host
        result['LifecyclePreStopHandlerHttpGetHttpHeader'] = []
        if self.lifecycle_pre_stop_handler_http_get_http_header is not None:
            for k in self.lifecycle_pre_stop_handler_http_get_http_header:
                result['LifecyclePreStopHandlerHttpGetHttpHeader'].append(k.to_map() if k else None)
        if self.lifecycle_pre_stop_handler_http_get_path is not None:
            result['LifecyclePreStopHandlerHttpGetPath'] = self.lifecycle_pre_stop_handler_http_get_path
        if self.lifecycle_pre_stop_handler_http_get_port is not None:
            result['LifecyclePreStopHandlerHttpGetPort'] = self.lifecycle_pre_stop_handler_http_get_port
        if self.lifecycle_pre_stop_handler_http_get_scheme is not None:
            result['LifecyclePreStopHandlerHttpGetScheme'] = self.lifecycle_pre_stop_handler_http_get_scheme
        if self.lifecycle_pre_stop_handler_tcp_socket_host is not None:
            result['LifecyclePreStopHandlerTcpSocketHost'] = self.lifecycle_pre_stop_handler_tcp_socket_host
        if self.lifecycle_pre_stop_handler_tcp_socket_port is not None:
            result['LifecyclePreStopHandlerTcpSocketPort'] = self.lifecycle_pre_stop_handler_tcp_socket_port
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.name is not None:
            result['Name'] = self.name
        result['Port'] = []
        if self.port is not None:
            for k in self.port:
                result['Port'].append(k.to_map() if k else None)
        if self.security_context_privileged is not None:
            result['SecurityContextPrivileged'] = self.security_context_privileged
        if self.security_context_run_as_group is not None:
            result['SecurityContextRunAsGroup'] = self.security_context_run_as_group
        if self.security_context_run_as_non_root is not None:
            result['SecurityContextRunAsNonRoot'] = self.security_context_run_as_non_root
        if self.stdin is not None:
            result['Stdin'] = self.stdin
        if self.stdin_once is not None:
            result['StdinOnce'] = self.stdin_once
        if self.termination_message_path is not None:
            result['TerminationMessagePath'] = self.termination_message_path
        if self.termination_message_policy is not None:
            result['TerminationMessagePolicy'] = self.termination_message_policy
        if self.tty is not None:
            result['Tty'] = self.tty
        result['VolumeMount'] = []
        if self.volume_mount is not None:
            for k in self.volume_mount:
                result['VolumeMount'].append(k.to_map() if k else None)
        if self.working_dir is not None:
            result['WorkingDir'] = self.working_dir
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LivenessProbe') is not None:
            temp_model = CreateContainerGroupRequestContainerLivenessProbe()
            self.liveness_probe = temp_model.from_map(m['LivenessProbe'])
        if m.get('ReadinessProbe') is not None:
            temp_model = CreateContainerGroupRequestContainerReadinessProbe()
            self.readiness_probe = temp_model.from_map(m['ReadinessProbe'])
        if m.get('SecurityContext') is not None:
            temp_model = CreateContainerGroupRequestContainerSecurityContext()
            self.security_context = temp_model.from_map(m['SecurityContext'])
        if m.get('Arg') is not None:
            self.arg = m.get('Arg')
        if m.get('Command') is not None:
            self.command = m.get('Command')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        self.environment_var = []
        if m.get('EnvironmentVar') is not None:
            for k in m.get('EnvironmentVar'):
                temp_model = CreateContainerGroupRequestContainerEnvironmentVar()
                self.environment_var.append(temp_model.from_map(k))
        if m.get('EnvironmentVarHide') is not None:
            self.environment_var_hide = m.get('EnvironmentVarHide')
        if m.get('Gpu') is not None:
            self.gpu = m.get('Gpu')
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('ImagePullPolicy') is not None:
            self.image_pull_policy = m.get('ImagePullPolicy')
        if m.get('LifecyclePostStartHandlerExec') is not None:
            self.lifecycle_post_start_handler_exec = m.get('LifecyclePostStartHandlerExec')
        if m.get('LifecyclePostStartHandlerHttpGetHost') is not None:
            self.lifecycle_post_start_handler_http_get_host = m.get('LifecyclePostStartHandlerHttpGetHost')
        self.lifecycle_post_start_handler_http_get_http_header = []
        if m.get('LifecyclePostStartHandlerHttpGetHttpHeader') is not None:
            for k in m.get('LifecyclePostStartHandlerHttpGetHttpHeader'):
                temp_model = CreateContainerGroupRequestContainerLifecyclePostStartHandlerHttpGetHttpHeader()
                self.lifecycle_post_start_handler_http_get_http_header.append(temp_model.from_map(k))
        if m.get('LifecyclePostStartHandlerHttpGetPath') is not None:
            self.lifecycle_post_start_handler_http_get_path = m.get('LifecyclePostStartHandlerHttpGetPath')
        if m.get('LifecyclePostStartHandlerHttpGetPort') is not None:
            self.lifecycle_post_start_handler_http_get_port = m.get('LifecyclePostStartHandlerHttpGetPort')
        if m.get('LifecyclePostStartHandlerHttpGetScheme') is not None:
            self.lifecycle_post_start_handler_http_get_scheme = m.get('LifecyclePostStartHandlerHttpGetScheme')
        if m.get('LifecyclePostStartHandlerTcpSocketHost') is not None:
            self.lifecycle_post_start_handler_tcp_socket_host = m.get('LifecyclePostStartHandlerTcpSocketHost')
        if m.get('LifecyclePostStartHandlerTcpSocketPort') is not None:
            self.lifecycle_post_start_handler_tcp_socket_port = m.get('LifecyclePostStartHandlerTcpSocketPort')
        if m.get('LifecyclePreStopHandlerExec') is not None:
            self.lifecycle_pre_stop_handler_exec = m.get('LifecyclePreStopHandlerExec')
        if m.get('LifecyclePreStopHandlerHttpGetHost') is not None:
            self.lifecycle_pre_stop_handler_http_get_host = m.get('LifecyclePreStopHandlerHttpGetHost')
        self.lifecycle_pre_stop_handler_http_get_http_header = []
        if m.get('LifecyclePreStopHandlerHttpGetHttpHeader') is not None:
            for k in m.get('LifecyclePreStopHandlerHttpGetHttpHeader'):
                temp_model = CreateContainerGroupRequestContainerLifecyclePreStopHandlerHttpGetHttpHeader()
                self.lifecycle_pre_stop_handler_http_get_http_header.append(temp_model.from_map(k))
        if m.get('LifecyclePreStopHandlerHttpGetPath') is not None:
            self.lifecycle_pre_stop_handler_http_get_path = m.get('LifecyclePreStopHandlerHttpGetPath')
        if m.get('LifecyclePreStopHandlerHttpGetPort') is not None:
            self.lifecycle_pre_stop_handler_http_get_port = m.get('LifecyclePreStopHandlerHttpGetPort')
        if m.get('LifecyclePreStopHandlerHttpGetScheme') is not None:
            self.lifecycle_pre_stop_handler_http_get_scheme = m.get('LifecyclePreStopHandlerHttpGetScheme')
        if m.get('LifecyclePreStopHandlerTcpSocketHost') is not None:
            self.lifecycle_pre_stop_handler_tcp_socket_host = m.get('LifecyclePreStopHandlerTcpSocketHost')
        if m.get('LifecyclePreStopHandlerTcpSocketPort') is not None:
            self.lifecycle_pre_stop_handler_tcp_socket_port = m.get('LifecyclePreStopHandlerTcpSocketPort')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.port = []
        if m.get('Port') is not None:
            for k in m.get('Port'):
                temp_model = CreateContainerGroupRequestContainerPort()
                self.port.append(temp_model.from_map(k))
        if m.get('SecurityContextPrivileged') is not None:
            self.security_context_privileged = m.get('SecurityContextPrivileged')
        if m.get('SecurityContextRunAsGroup') is not None:
            self.security_context_run_as_group = m.get('SecurityContextRunAsGroup')
        if m.get('SecurityContextRunAsNonRoot') is not None:
            self.security_context_run_as_non_root = m.get('SecurityContextRunAsNonRoot')
        if m.get('Stdin') is not None:
            self.stdin = m.get('Stdin')
        if m.get('StdinOnce') is not None:
            self.stdin_once = m.get('StdinOnce')
        if m.get('TerminationMessagePath') is not None:
            self.termination_message_path = m.get('TerminationMessagePath')
        if m.get('TerminationMessagePolicy') is not None:
            self.termination_message_policy = m.get('TerminationMessagePolicy')
        if m.get('Tty') is not None:
            self.tty = m.get('Tty')
        self.volume_mount = []
        if m.get('VolumeMount') is not None:
            for k in m.get('VolumeMount'):
                temp_model = CreateContainerGroupRequestContainerVolumeMount()
                self.volume_mount.append(temp_model.from_map(k))
        if m.get('WorkingDir') is not None:
            self.working_dir = m.get('WorkingDir')
        return self


class CreateContainerGroupRequestHostAliase(TeaModel):
    def __init__(
        self,
        hostname: List[str] = None,
        ip: str = None,
    ):
        # The hostnames of the elastic container instance.
        self.hostname = hostname
        # The IP address of the elastic container instance.
        self.ip = ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hostname is not None:
            result['Hostname'] = self.hostname
        if self.ip is not None:
            result['Ip'] = self.ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        return self


class CreateContainerGroupRequestImageRegistryCredential(TeaModel):
    def __init__(
        self,
        password: str = None,
        server: str = None,
        user_name: str = None,
    ):
        # The password that you use to access the image repository.
        self.password = password
        # The address of the image repository.
        self.server = server
        # The username that you use to access the image repository.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.password is not None:
            result['Password'] = self.password
        if self.server is not None:
            result['Server'] = self.server
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Server') is not None:
            self.server = m.get('Server')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class CreateContainerGroupRequestInitContainerSecurityContextCapability(TeaModel):
    def __init__(
        self,
        add: List[str] = None,
    ):
        self.add = add

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.add is not None:
            result['Add'] = self.add
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Add') is not None:
            self.add = m.get('Add')
        return self


class CreateContainerGroupRequestInitContainerSecurityContext(TeaModel):
    def __init__(
        self,
        capability: CreateContainerGroupRequestInitContainerSecurityContextCapability = None,
        read_only_root_filesystem: bool = None,
        run_as_user: int = None,
    ):
        self.capability = capability
        self.read_only_root_filesystem = read_only_root_filesystem
        self.run_as_user = run_as_user

    def validate(self):
        if self.capability:
            self.capability.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.capability is not None:
            result['Capability'] = self.capability.to_map()
        if self.read_only_root_filesystem is not None:
            result['ReadOnlyRootFilesystem'] = self.read_only_root_filesystem
        if self.run_as_user is not None:
            result['RunAsUser'] = self.run_as_user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Capability') is not None:
            temp_model = CreateContainerGroupRequestInitContainerSecurityContextCapability()
            self.capability = temp_model.from_map(m['Capability'])
        if m.get('ReadOnlyRootFilesystem') is not None:
            self.read_only_root_filesystem = m.get('ReadOnlyRootFilesystem')
        if m.get('RunAsUser') is not None:
            self.run_as_user = m.get('RunAsUser')
        return self


class CreateContainerGroupRequestInitContainerEnvironmentVarFieldRef(TeaModel):
    def __init__(
        self,
        field_path: str = None,
    ):
        self.field_path = field_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_path is not None:
            result['FieldPath'] = self.field_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldPath') is not None:
            self.field_path = m.get('FieldPath')
        return self


class CreateContainerGroupRequestInitContainerEnvironmentVar(TeaModel):
    def __init__(
        self,
        field_ref: CreateContainerGroupRequestInitContainerEnvironmentVarFieldRef = None,
        key: str = None,
        value: str = None,
    ):
        self.field_ref = field_ref
        # The name of the environment variable. The name must be 1 to 128 bits in length and can contain letters, digits, and underscores (_). It cannot start with a digit.``
        self.key = key
        # The value of the environment variable. The value must be 0 to 256 bits in length.
        self.value = value

    def validate(self):
        if self.field_ref:
            self.field_ref.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_ref is not None:
            result['FieldRef'] = self.field_ref.to_map()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldRef') is not None:
            temp_model = CreateContainerGroupRequestInitContainerEnvironmentVarFieldRef()
            self.field_ref = temp_model.from_map(m['FieldRef'])
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateContainerGroupRequestInitContainerPort(TeaModel):
    def __init__(
        self,
        port: int = None,
        protocol: str = None,
    ):
        # The port number. Valid values: 1 to 65535.
        self.port = port
        # The protocol type. Valid values:
        # 
        # *   TCP
        # *   UDP
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.port is not None:
            result['Port'] = self.port
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        return self


class CreateContainerGroupRequestInitContainerVolumeMount(TeaModel):
    def __init__(
        self,
        mount_path: str = None,
        mount_propagation: str = None,
        name: str = None,
        read_only: bool = None,
        sub_path: str = None,
    ):
        # The directory to which the volume is mounted. The data stored in this directory is overwritten by the data on the volume. Specify this parameter with caution.
        self.mount_path = mount_path
        # The mount propagation settings of the volume. Mount propagation allows volumes that are mounted on one init container to be shared with other init containers in the same pod, or even with other pods on the same node. Valid values:
        # 
        # *   None: The volume mount does not receive subsequent mounts that are performed on this volume or subdirectories of this volume.
        # *   HostToCotainer: The volume mount receives subsequent mounts that are performed on this volume or the subdirectories of this volume.
        # *   Bidirectional: This value is similar to HostToContainer. The volume mount receives subsequent mounts that are performed on this volume or the subdirectories of this volume. In addition, all volume mounts that are mounted on the init container are propagated back to the host and all init containers of all pods that use the same volume.
        # 
        # Default value: None.
        self.mount_propagation = mount_propagation
        # The name of the volume.
        self.name = name
        # Specifies whether the mount path is read-only. Default value: false.
        self.read_only = read_only
        # The subdirectory of the volume. The pod can mount different directories of the same volume to different subdirectories of init containers.
        self.sub_path = sub_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mount_path is not None:
            result['MountPath'] = self.mount_path
        if self.mount_propagation is not None:
            result['MountPropagation'] = self.mount_propagation
        if self.name is not None:
            result['Name'] = self.name
        if self.read_only is not None:
            result['ReadOnly'] = self.read_only
        if self.sub_path is not None:
            result['SubPath'] = self.sub_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')
        if m.get('MountPropagation') is not None:
            self.mount_propagation = m.get('MountPropagation')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ReadOnly') is not None:
            self.read_only = m.get('ReadOnly')
        if m.get('SubPath') is not None:
            self.sub_path = m.get('SubPath')
        return self


class CreateContainerGroupRequestInitContainer(TeaModel):
    def __init__(
        self,
        security_context: CreateContainerGroupRequestInitContainerSecurityContext = None,
        arg: List[str] = None,
        command: List[str] = None,
        cpu: float = None,
        environment_var: List[CreateContainerGroupRequestInitContainerEnvironmentVar] = None,
        gpu: int = None,
        image: str = None,
        image_pull_policy: str = None,
        memory: float = None,
        name: str = None,
        port: List[CreateContainerGroupRequestInitContainerPort] = None,
        termination_message_path: str = None,
        termination_message_policy: str = None,
        volume_mount: List[CreateContainerGroupRequestInitContainerVolumeMount] = None,
        working_dir: str = None,
    ):
        self.security_context = security_context
        # The arguments that are passed to the startup command of the init container.
        self.arg = arg
        # The startup commands of the init container.
        self.command = command
        # The number of vCPUs that you want to allocate to the init container.
        self.cpu = cpu
        # The environment variable of the init container.
        self.environment_var = environment_var
        # The number of GPUs that you want to allocate to the init container.
        self.gpu = gpu
        # The image of the init container.
        self.image = image
        # The policy that you want to use to pull images. Valid values:
        # 
        # *   Always: Each time instances are created, image pulling is performed.
        # *   IfNotPresent: On-premises images are preferentially used. If no on-premises images are available, image pulling is performed.
        # *   Never: On-premises images are always used. Image pulling is not performed.
        self.image_pull_policy = image_pull_policy
        # The memory size that you want to allocate to the init container. Unit: GiB.
        self.memory = memory
        # The name of the init container.
        self.name = name
        # The information about the port.
        self.port = port
        # The path of the file from which the system retrieves termination messages of the init container when the init container exits.
        self.termination_message_path = termination_message_path
        # The message notification policy. This parameter is empty by default.
        self.termination_message_policy = termination_message_policy
        # The information about the volumes that you want to mount to the init containers.
        self.volume_mount = volume_mount
        # The working directory of the init container.
        self.working_dir = working_dir

    def validate(self):
        if self.security_context:
            self.security_context.validate()
        if self.environment_var:
            for k in self.environment_var:
                if k:
                    k.validate()
        if self.port:
            for k in self.port:
                if k:
                    k.validate()
        if self.volume_mount:
            for k in self.volume_mount:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_context is not None:
            result['SecurityContext'] = self.security_context.to_map()
        if self.arg is not None:
            result['Arg'] = self.arg
        if self.command is not None:
            result['Command'] = self.command
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        result['EnvironmentVar'] = []
        if self.environment_var is not None:
            for k in self.environment_var:
                result['EnvironmentVar'].append(k.to_map() if k else None)
        if self.gpu is not None:
            result['Gpu'] = self.gpu
        if self.image is not None:
            result['Image'] = self.image
        if self.image_pull_policy is not None:
            result['ImagePullPolicy'] = self.image_pull_policy
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.name is not None:
            result['Name'] = self.name
        result['Port'] = []
        if self.port is not None:
            for k in self.port:
                result['Port'].append(k.to_map() if k else None)
        if self.termination_message_path is not None:
            result['TerminationMessagePath'] = self.termination_message_path
        if self.termination_message_policy is not None:
            result['TerminationMessagePolicy'] = self.termination_message_policy
        result['VolumeMount'] = []
        if self.volume_mount is not None:
            for k in self.volume_mount:
                result['VolumeMount'].append(k.to_map() if k else None)
        if self.working_dir is not None:
            result['WorkingDir'] = self.working_dir
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityContext') is not None:
            temp_model = CreateContainerGroupRequestInitContainerSecurityContext()
            self.security_context = temp_model.from_map(m['SecurityContext'])
        if m.get('Arg') is not None:
            self.arg = m.get('Arg')
        if m.get('Command') is not None:
            self.command = m.get('Command')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        self.environment_var = []
        if m.get('EnvironmentVar') is not None:
            for k in m.get('EnvironmentVar'):
                temp_model = CreateContainerGroupRequestInitContainerEnvironmentVar()
                self.environment_var.append(temp_model.from_map(k))
        if m.get('Gpu') is not None:
            self.gpu = m.get('Gpu')
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('ImagePullPolicy') is not None:
            self.image_pull_policy = m.get('ImagePullPolicy')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.port = []
        if m.get('Port') is not None:
            for k in m.get('Port'):
                temp_model = CreateContainerGroupRequestInitContainerPort()
                self.port.append(temp_model.from_map(k))
        if m.get('TerminationMessagePath') is not None:
            self.termination_message_path = m.get('TerminationMessagePath')
        if m.get('TerminationMessagePolicy') is not None:
            self.termination_message_policy = m.get('TerminationMessagePolicy')
        self.volume_mount = []
        if m.get('VolumeMount') is not None:
            for k in m.get('VolumeMount'):
                temp_model = CreateContainerGroupRequestInitContainerVolumeMount()
                self.volume_mount.append(temp_model.from_map(k))
        if m.get('WorkingDir') is not None:
            self.working_dir = m.get('WorkingDir')
        return self


class CreateContainerGroupRequestOverheadReservationOption(TeaModel):
    def __init__(
        self,
        enable_overhead_reservation: bool = None,
    ):
        # Specify whether to enable the overhead reservation feature. Default: false. Valid values: true and false. After you enable the overhead reservation feature, the system automatically adds the overhead to the specification of the elastic container instance, and then adjusts the specification of the instance upward to the most approximate specification. You are charged based on the new specification after the adjustment.
        self.enable_overhead_reservation = enable_overhead_reservation

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_overhead_reservation is not None:
            result['EnableOverheadReservation'] = self.enable_overhead_reservation
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableOverheadReservation') is not None:
            self.enable_overhead_reservation = m.get('EnableOverheadReservation')
        return self


class CreateContainerGroupRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key. The tag key cannot be an empty string and must be unique. The tag key can be up to 64 characters in length and cannot contain `http://` or `https://`. The tag key cannot start with `acs:` or `aliyun`.
        self.key = key
        # The tag value. The tag value can be an empty string. The tag value can be up to 128 characters in length. It cannot start with `acs:` and cannot contain `http://` or `https://`.
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


class CreateContainerGroupRequestVolumeConfigFileVolumeConfigFileToPath(TeaModel):
    def __init__(
        self,
        content: str = None,
        mode: int = None,
        path: str = None,
    ):
        self.content = content
        self.mode = mode
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class CreateContainerGroupRequestVolumeConfigFileVolume(TeaModel):
    def __init__(
        self,
        config_file_to_path: List[CreateContainerGroupRequestVolumeConfigFileVolumeConfigFileToPath] = None,
        default_mode: int = None,
    ):
        self.config_file_to_path = config_file_to_path
        self.default_mode = default_mode

    def validate(self):
        if self.config_file_to_path:
            for k in self.config_file_to_path:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ConfigFileToPath'] = []
        if self.config_file_to_path is not None:
            for k in self.config_file_to_path:
                result['ConfigFileToPath'].append(k.to_map() if k else None)
        if self.default_mode is not None:
            result['DefaultMode'] = self.default_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.config_file_to_path = []
        if m.get('ConfigFileToPath') is not None:
            for k in m.get('ConfigFileToPath'):
                temp_model = CreateContainerGroupRequestVolumeConfigFileVolumeConfigFileToPath()
                self.config_file_to_path.append(temp_model.from_map(k))
        if m.get('DefaultMode') is not None:
            self.default_mode = m.get('DefaultMode')
        return self


class CreateContainerGroupRequestVolumeDiskVolume(TeaModel):
    def __init__(
        self,
        disk_id: str = None,
        disk_size: int = None,
        fs_type: str = None,
    ):
        self.disk_id = disk_id
        self.disk_size = disk_size
        self.fs_type = fs_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disk_id is not None:
            result['DiskId'] = self.disk_id
        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size
        if self.fs_type is not None:
            result['FsType'] = self.fs_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')
        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')
        if m.get('FsType') is not None:
            self.fs_type = m.get('FsType')
        return self


class CreateContainerGroupRequestVolumeEmptyDirVolume(TeaModel):
    def __init__(
        self,
        medium: str = None,
        size_limit: str = None,
    ):
        self.medium = medium
        self.size_limit = size_limit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.medium is not None:
            result['Medium'] = self.medium
        if self.size_limit is not None:
            result['SizeLimit'] = self.size_limit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Medium') is not None:
            self.medium = m.get('Medium')
        if m.get('SizeLimit') is not None:
            self.size_limit = m.get('SizeLimit')
        return self


class CreateContainerGroupRequestVolumeFlexVolume(TeaModel):
    def __init__(
        self,
        driver: str = None,
        fs_type: str = None,
        options: str = None,
    ):
        self.driver = driver
        self.fs_type = fs_type
        self.options = options

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.driver is not None:
            result['Driver'] = self.driver
        if self.fs_type is not None:
            result['FsType'] = self.fs_type
        if self.options is not None:
            result['Options'] = self.options
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Driver') is not None:
            self.driver = m.get('Driver')
        if m.get('FsType') is not None:
            self.fs_type = m.get('FsType')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        return self


class CreateContainerGroupRequestVolumeHostPathVolume(TeaModel):
    def __init__(
        self,
        path: str = None,
        type: str = None,
    ):
        self.path = path
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.path is not None:
            result['Path'] = self.path
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateContainerGroupRequestVolumeNFSVolume(TeaModel):
    def __init__(
        self,
        path: str = None,
        read_only: bool = None,
        server: str = None,
    ):
        self.path = path
        self.read_only = read_only
        self.server = server

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.path is not None:
            result['Path'] = self.path
        if self.read_only is not None:
            result['ReadOnly'] = self.read_only
        if self.server is not None:
            result['Server'] = self.server
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('ReadOnly') is not None:
            self.read_only = m.get('ReadOnly')
        if m.get('Server') is not None:
            self.server = m.get('Server')
        return self


class CreateContainerGroupRequestVolume(TeaModel):
    def __init__(
        self,
        config_file_volume: CreateContainerGroupRequestVolumeConfigFileVolume = None,
        disk_volume: CreateContainerGroupRequestVolumeDiskVolume = None,
        empty_dir_volume: CreateContainerGroupRequestVolumeEmptyDirVolume = None,
        flex_volume: CreateContainerGroupRequestVolumeFlexVolume = None,
        host_path_volume: CreateContainerGroupRequestVolumeHostPathVolume = None,
        nfsvolume: CreateContainerGroupRequestVolumeNFSVolume = None,
        name: str = None,
        type: str = None,
    ):
        self.config_file_volume = config_file_volume
        self.disk_volume = disk_volume
        self.empty_dir_volume = empty_dir_volume
        self.flex_volume = flex_volume
        self.host_path_volume = host_path_volume
        self.nfsvolume = nfsvolume
        # The name of the volume.
        self.name = name
        # The type of the HostPath volume. Valid values:
        # 
        # *   Directory
        # *   File
        # 
        # >  Only users in the whitelist can mount HostPath volumes.
        self.type = type

    def validate(self):
        if self.config_file_volume:
            self.config_file_volume.validate()
        if self.disk_volume:
            self.disk_volume.validate()
        if self.empty_dir_volume:
            self.empty_dir_volume.validate()
        if self.flex_volume:
            self.flex_volume.validate()
        if self.host_path_volume:
            self.host_path_volume.validate()
        if self.nfsvolume:
            self.nfsvolume.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_file_volume is not None:
            result['ConfigFileVolume'] = self.config_file_volume.to_map()
        if self.disk_volume is not None:
            result['DiskVolume'] = self.disk_volume.to_map()
        if self.empty_dir_volume is not None:
            result['EmptyDirVolume'] = self.empty_dir_volume.to_map()
        if self.flex_volume is not None:
            result['FlexVolume'] = self.flex_volume.to_map()
        if self.host_path_volume is not None:
            result['HostPathVolume'] = self.host_path_volume.to_map()
        if self.nfsvolume is not None:
            result['NFSVolume'] = self.nfsvolume.to_map()
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigFileVolume') is not None:
            temp_model = CreateContainerGroupRequestVolumeConfigFileVolume()
            self.config_file_volume = temp_model.from_map(m['ConfigFileVolume'])
        if m.get('DiskVolume') is not None:
            temp_model = CreateContainerGroupRequestVolumeDiskVolume()
            self.disk_volume = temp_model.from_map(m['DiskVolume'])
        if m.get('EmptyDirVolume') is not None:
            temp_model = CreateContainerGroupRequestVolumeEmptyDirVolume()
            self.empty_dir_volume = temp_model.from_map(m['EmptyDirVolume'])
        if m.get('FlexVolume') is not None:
            temp_model = CreateContainerGroupRequestVolumeFlexVolume()
            self.flex_volume = temp_model.from_map(m['FlexVolume'])
        if m.get('HostPathVolume') is not None:
            temp_model = CreateContainerGroupRequestVolumeHostPathVolume()
            self.host_path_volume = temp_model.from_map(m['HostPathVolume'])
        if m.get('NFSVolume') is not None:
            temp_model = CreateContainerGroupRequestVolumeNFSVolume()
            self.nfsvolume = temp_model.from_map(m['NFSVolume'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateContainerGroupRequest(TeaModel):
    def __init__(
        self,
        dns_config: CreateContainerGroupRequestDnsConfig = None,
        host_security_context: CreateContainerGroupRequestHostSecurityContext = None,
        security_context: CreateContainerGroupRequestSecurityContext = None,
        acr_registry_info: List[CreateContainerGroupRequestAcrRegistryInfo] = None,
        active_deadline_seconds: int = None,
        auto_create_eip: bool = None,
        auto_match_image_cache: bool = None,
        client_token: str = None,
        compute_category: List[str] = None,
        container: List[CreateContainerGroupRequestContainer] = None,
        container_group_name: str = None,
        container_resource_view: bool = None,
        core_pattern: str = None,
        cpu: float = None,
        cpu_architecture: str = None,
        cpu_options_core: int = None,
        cpu_options_numa: str = None,
        cpu_options_threads_per_core: int = None,
        data_cache_bucket: str = None,
        data_cache_bursting_enabled: bool = None,
        data_cache_pl: str = None,
        data_cache_provisioned_iops: int = None,
        dns_policy: str = None,
        dry_run: bool = None,
        egress_bandwidth: int = None,
        eip_bandwidth: int = None,
        eip_common_bandwidth_package: str = None,
        eip_isp: str = None,
        eip_instance_id: str = None,
        ephemeral_storage: int = None,
        fixed_ip: str = None,
        fixed_ip_retain_hour: int = None,
        gpu_driver_version: str = None,
        host_aliase: List[CreateContainerGroupRequestHostAliase] = None,
        host_name: str = None,
        image_accelerate_mode: str = None,
        image_registry_credential: List[CreateContainerGroupRequestImageRegistryCredential] = None,
        image_snapshot_id: str = None,
        ingress_bandwidth: int = None,
        init_container: List[CreateContainerGroupRequestInitContainer] = None,
        insecure_registry: str = None,
        instance_type: str = None,
        ipv_6address_count: int = None,
        ipv_6gateway_bandwidth: str = None,
        ipv_6gateway_bandwidth_enable: bool = None,
        memory: float = None,
        ntp_server: List[str] = None,
        os_type: str = None,
        overhead_reservation_option: CreateContainerGroupRequestOverheadReservationOption = None,
        owner_account: str = None,
        owner_id: int = None,
        plain_http_registry: str = None,
        private_ip_address: str = None,
        ram_role_name: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        restart_policy: str = None,
        schedule_strategy: str = None,
        security_group_id: str = None,
        share_process_namespace: bool = None,
        spot_duration: int = None,
        spot_price_limit: float = None,
        spot_strategy: str = None,
        strict_spot: bool = None,
        tag: List[CreateContainerGroupRequestTag] = None,
        termination_grace_period_seconds: int = None,
        v_switch_id: str = None,
        volume: List[CreateContainerGroupRequestVolume] = None,
        zone_id: str = None,
    ):
        self.dns_config = dns_config
        self.host_security_context = host_security_context
        self.security_context = security_context
        # The information about the Container Registry Enterprise Edition instance that provides the image for the creation of the elastic container instance. For more information, see [Pull images from a Container Registry Enterprise Edition instance without using a secret](https://help.aliyun.com/document_detail/194250.html).
        self.acr_registry_info = acr_registry_info
        # The active period of the elastic container instance. After this period expires, the instance is forced to exit. Unit: seconds.
        self.active_deadline_seconds = active_deadline_seconds
        # Specifies whether to automatically create an EIP and associate it with the elastic container instance.
        self.auto_create_eip = auto_create_eip
        # Specifies whether to automatically match image caches. Default value: false.
        self.auto_match_image_cache = auto_match_image_cache
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotency](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The computing power type of the instance. For more information, see [Set the computing power type to economy when you create an elastic container instance](https://help.aliyun.com/document_detail/2638061.html).
        self.compute_category = compute_category
        # The information about the container.
        # 
        # This parameter is required.
        self.container = container
        # The name of the elastic container instance (container group). The name must meet the following requirements:
        # 
        # *   The name must be 2 to 128 characters in length.
        # *   The name can contain lowercase letters, digits, and hyphens (-). It cannot start or end with a hyphen (-).
        # 
        # This parameter is required.
        self.container_group_name = container_group_name
        # Specifies whether to enable container resource view. Container resource view displays the actual container resource data instead of data of the host. If the specifications of the generated elastic container instance are larger than the specifications that you request for when you create the instance, you can enable the ContainerResourceView feature to ensure that the resources that you view in the container are the same as the resources that you request for.
        self.container_resource_view = container_resource_view
        # The path to core dump files. For more information, see [Save core files to volumes](https://help.aliyun.com/document_detail/167801.html).
        # 
        # >  The path cannot start with |. You cannot use core dump files to configure executable programs.``
        self.core_pattern = core_pattern
        # The number of vCPUs that you want to allocate to the instance.
        self.cpu = cpu
        # The CPU architecture of the instance. Default value: AMD64. Valid values:
        # 
        # *   AMD64
        # *   ARM64
        self.cpu_architecture = cpu_architecture
        # The number of physical CPU cores. You can specify this parameter for only specific ECS instance types.
        self.cpu_options_core = cpu_options_core
        # This parameter is not available.
        self.cpu_options_numa = cpu_options_numa
        # The number of threads per core. You can specify this parameter for only specific ECS instance types. A value of 1 specifies that Hyper-Threading is disabled.
        self.cpu_options_threads_per_core = cpu_options_threads_per_core
        # The bucket that stores the data cache.
        self.data_cache_bucket = data_cache_bucket
        # Specifies whether to enable the performance burst feature when ESSDs AutoPL are used to store data caches. For more information, see [ESSDs AutoPL](https://help.aliyun.com/document_detail/368372.html).
        self.data_cache_bursting_enabled = data_cache_bursting_enabled
        # The performance level (PL) of the disk that you want to use to store data caches.\\
        # Enhanced SSDs (ESSDs) are preferentially used to store data caches. The default performance level is PL1.
        self.data_cache_pl = data_cache_pl
        # The input/output operations per second (IOPS) provisioned for ESSDs AutoPL when ESSDs AutoPL are used to store data caches.\\
        # Valid values: 0 to min{50000, 1000 × Storage capacity - Baseline IOPS}. Baseline IOPS = min{1,800 + 50 × Storage capacity, 50,000}.\\
        # For more information, see [ESSDs AutoPL](https://help.aliyun.com/document_detail/368372.html).
        self.data_cache_provisioned_iops = data_cache_provisioned_iops
        # The Domain Name System (DNS) policy. Valid values:
        # 
        # *   None: uses the DNS that is specified by DnsConfig.
        # *   Default: uses the DNS that is specified for the runtime environment.
        self.dns_policy = dns_policy
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   true: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, service limits, and available resources. If the request passes the dry run, the DryRunOperation error code is returned. Otherwise, an error message is returned.
        # *   false (default): performs a dry run and performs the actual request. If the request passes the dry run, the elastic container instance is created.
        self.dry_run = dry_run
        # The maximum outbound bandwidth. Unit: bit/s.
        self.egress_bandwidth = egress_bandwidth
        # The maximum bandwidth value for the EIP. Unit: Mbit/s. Default value: 5.\\
        # This parameter is valid only when AutoCreateEip is set to true.
        self.eip_bandwidth = eip_bandwidth
        # The EIP bandwidth plan that you want to associate with the instance.
        self.eip_common_bandwidth_package = eip_common_bandwidth_package
        # The line type of the EIP. Default value: BGP. Valid values:
        # 
        # *   BGP: BGP (Multi-ISP) line
        # *   BGP_PRO: BGP (Multi-ISP) Pro line
        self.eip_isp = eip_isp
        # The ID of the elastic IP address (EIP).
        self.eip_instance_id = eip_instance_id
        # The increased capacity of the temporary storage space. Unit: GiB.\\
        # For more information, see [Increase the size of the temporary storage space](https://help.aliyun.com/document_detail/204066.html).
        self.ephemeral_storage = ephemeral_storage
        # Specifies whether to configure the instance to use a fixed IP address. For more information, see [Configure an elastic container instance to use a fixed IP address](https://help.aliyun.com/document_detail/2381086.html).
        self.fixed_ip = fixed_ip
        # The retention period of the fixed IP address after the original instance is released and the fixed IP address becomes idle. Unit: hours. Default value: 48.
        self.fixed_ip_retain_hour = fixed_ip_retain_hour
        # The version of the GPU driver. Default value: tesla=470.82.01. Valid values:
        # 
        # *   tesla=470.82.01
        # *   tesla=525.85.12
        # 
        # >  You can switch the GPU driver version only for a few Elastic Compute Service (ECS) instance types. For more information, see [Specify GPU-accelerated ECS instance types to create an elastic container instance](https://help.aliyun.com/document_detail/2579486.html).
        self.gpu_driver_version = gpu_driver_version
        # The alias of the elastic container instance.
        self.host_aliase = host_aliase
        # The hostname.
        self.host_name = host_name
        # The image acceleration mode. Valid values:
        # 
        # *   nydus: uses Nydus to accelerate image pulling. The images must support Nydus.
        # *   dadi: uses DADI to accelerate image pulling. The images must support DADI.
        # *   p2p: uses P2P to accelerate image pulling. The images must support p2p.
        # *   imc: uses image caches to accelerate image pulling.
        self.image_accelerate_mode = image_accelerate_mode
        # The information about the logon credentials.
        self.image_registry_credential = image_registry_credential
        # The ID of the image cache. For more information, see [Use image caches to accelerate the creation of instances](https://help.aliyun.com/document_detail/141281.html).
        self.image_snapshot_id = image_snapshot_id
        # The maximum inbound bandwidth. Unit: bit/s.
        self.ingress_bandwidth = ingress_bandwidth
        # The information about the init containers.
        self.init_container = init_container
        # The address of the self-managed image repository. When you create an elastic container instance by using an image in a self-managed image repository that uses a self-signed certificate, you must specify this parameter to skip the certificate authentication. This prevents image pull failures caused by certificate authentication failures.
        self.insecure_registry = insecure_registry
        # The ECS instance types that you specify to create the elastic container instance. Multiple instance types are supported. For more information, see [Specify ECS instance types to create an elastic container instance](https://help.aliyun.com/document_detail/114664.html).
        self.instance_type = instance_type
        # The number of IPv6 addresses that are assigned to the instance. Set the value to 1. You can assign only one IPv6 address to an elastic container instance.
        self.ipv_6address_count = ipv_6address_count
        # The maximum IPv6 Internet bandwidth when you set Ipv6GatewayBandwidthEnable to true. Valid values:
        # 
        # *   If the billing method for IPv6 network usage is pay-by-bandwidth, the maximum IPv6 Internet bandwidth ranges from 1 to 2,000 Mbit/s.
        # 
        # *   If the billing method for IPv6 network usage is pay-by-traffic, the maximum IPv6 Internet bandwidth varies based on the edition of the IPv6 gateway.
        # 
        #     *   If the IPv6 gateway is of Free Edition, the maximum IPv6 Internet bandwidth ranges from 1 to 200 Mbit/s.
        #     *   If the IPv6 gateway is of Enterprise Edition, the maximum IPv6 Internet bandwidth ranges from 1 to 500 Mbit/s.
        #     *   If the IPv6 gateway is of Enhanced Enterprise Edition, the maximum IPv6 Internet bandwidth ranges from 1 to 1000 Mbit/s.
        # 
        # The default value is the maximum value in the Internet bandwidth range of the IPv6 gateway.
        self.ipv_6gateway_bandwidth = ipv_6gateway_bandwidth
        # Specifies whether to enable Internet access to the elastic container instance over IPv6 addresses.
        self.ipv_6gateway_bandwidth_enable = ipv_6gateway_bandwidth_enable
        # The memory size that you want to allocate to the instance. Unit: GiB.
        self.memory = memory
        # The endpoints of the Network Time Protocol (NTP) servers.
        self.ntp_server = ntp_server
        # The operating system of the elastic container instance. Default value: Linux. Valid values:
        # 
        # *   Linux
        # *   Windows
        # 
        # >  Windows instances are in invitational preview. To use the operating system, submit a ticket.
        self.os_type = os_type
        # The options that you can configure when you enable the overhead reservation feature.
        self.overhead_reservation_option = overhead_reservation_option
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The address of the self-managed image repository. When you create an elastic container instance by using an image in a self-managed image repository that uses the HTTP protocol, you must specify this parameter. This way, Elastic Container Instance pulls the image over the HTTP protocol instead of the default HTTPS protocol. This prevents image pull failures caused by different protocols.
        self.plain_http_registry = plain_http_registry
        # The private IP address of the elastic container instance. Only IPv4 addresses are supported. Make sure that the IP address is idle.
        self.private_ip_address = private_ip_address
        # The name of the instance Resource Access Management (RAM) role. You can use the same RAM role to access elastic container instances and ECS instances. For more information, see [Use an instance RAM role by calling API operations](https://help.aliyun.com/document_detail/61178.html).
        self.ram_role_name = ram_role_name
        # The region ID of the instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The restart policy of the instance. Valid values:
        # 
        # *   Always: Always restarts the instance if a container in the instance exits upon termination.
        # *   Never: Never restarts the instance if a container in the instance exits upon termination.
        # *   OnFailure: Restarts the instance only if a container in the instance exists upon failure with a status code of non-zero.
        # 
        # Default value: Always.
        self.restart_policy = restart_policy
        # The resource scheduling policy when you specify multiple zones to create an elastic container instance. To specify multiple zones, you can use the VSwitchId to specify multiple vSwitches. Valid values:
        # 
        # *   VSwitchOrdered: The system schedules resources in the sequence of the vSwitches.
        # *   VSwitchRandom: The system schedules resources at random.
        # 
        # For more information, see [Specify multiple zones to create an elastic container instance](https://help.aliyun.com/document_detail/157290.html).
        self.schedule_strategy = schedule_strategy
        # The ID of the security group to which the instance belongs. Instances in the same security group can access each other.
        # 
        # If you do not specify a security group, the system automatically uses the default security group in the region that you selected. Make sure that the inbound rules of the security group contain the container protocols and port numbers that you want to expose. If you do not have a default security group in the region, the system creates a default security group, and then adds the container protocols and port numbers that you specified to the inbound rules of the security group.
        self.security_group_id = security_group_id
        # Specifies whether to use a shared namespace. Default value: false.
        self.share_process_namespace = share_process_namespace
        # The protection period of the preemptible elastic container instance. Unit: hours. Default value: 1. A value of 0 indicates no protection period.
        self.spot_duration = spot_duration
        # The maximum hourly price of the preemptible elastic container instance. The value can be accurate to three decimal places.
        # 
        # If you set SpotStrategy to SpotWithPriceLimit, you must specify the SpotPriceLimit parameter.
        self.spot_price_limit = spot_price_limit
        # The bid policy for the instance. Valid values:
        # 
        # *   NoSpot: The instance is created as a pay-as-you-go instance.
        # *   SpotWithPriceLimit: The instance is created as a preemptible instance for which you specify the maximum hourly price.
        # *   SpotAsPriceGo: The instance is created as a preemptible instance for which the market price at the time of purchase is automatically used as the bid price.
        # 
        # Default value: NoSpot.
        self.spot_strategy = spot_strategy
        # Specifies whether to enable periodical execution.
        # 
        # *   true: enables periodical execution.
        # *   false: disables periodical execution.
        self.strict_spot = strict_spot
        # The tags that you want to add to the instance. You can bind a maximum of 20 tags. For more information, see [Use tags to manage elastic container instances](https://help.aliyun.com/document_detail/146608.html).
        self.tag = tag
        # The buffer period of time during which the program handles operations before the program is stopped. Unit: seconds.
        self.termination_grace_period_seconds = termination_grace_period_seconds
        # The IDs of the vSwitches that connect to the instance. You can specify up to 10 vSwitch IDs at a time. Separate multiple vSwitch IDs with commas (,). Example: `vsw-***,vsw-***`.
        # 
        # If you do not specify a vSwitch, the system automatically uses the default vSwitch in the default VPC in the region that you selected. If you do not have a default VPC or a default vSwitch in the region, the system automatically creates a default VPC and a default vSwitch.
        # 
        # >  The number of IP addresses in the vSwitch CIDR block determines the maximum number of elastic container instances that you can create for the vSwitch. Before you create elastic container instances, you must plan the CIDR block of the vSwitch.
        self.v_switch_id = v_switch_id
        # The information about the volume that you want to mount to the container.
        self.volume = volume
        # The zone ID of the instance. If you do not specify this parameter, the system selects a zone.
        # 
        # This parameter is empty by default.
        self.zone_id = zone_id

    def validate(self):
        if self.dns_config:
            self.dns_config.validate()
        if self.host_security_context:
            self.host_security_context.validate()
        if self.security_context:
            self.security_context.validate()
        if self.acr_registry_info:
            for k in self.acr_registry_info:
                if k:
                    k.validate()
        if self.container:
            for k in self.container:
                if k:
                    k.validate()
        if self.host_aliase:
            for k in self.host_aliase:
                if k:
                    k.validate()
        if self.image_registry_credential:
            for k in self.image_registry_credential:
                if k:
                    k.validate()
        if self.init_container:
            for k in self.init_container:
                if k:
                    k.validate()
        if self.overhead_reservation_option:
            self.overhead_reservation_option.validate()
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()
        if self.volume:
            for k in self.volume:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dns_config is not None:
            result['DnsConfig'] = self.dns_config.to_map()
        if self.host_security_context is not None:
            result['HostSecurityContext'] = self.host_security_context.to_map()
        if self.security_context is not None:
            result['SecurityContext'] = self.security_context.to_map()
        result['AcrRegistryInfo'] = []
        if self.acr_registry_info is not None:
            for k in self.acr_registry_info:
                result['AcrRegistryInfo'].append(k.to_map() if k else None)
        if self.active_deadline_seconds is not None:
            result['ActiveDeadlineSeconds'] = self.active_deadline_seconds
        if self.auto_create_eip is not None:
            result['AutoCreateEip'] = self.auto_create_eip
        if self.auto_match_image_cache is not None:
            result['AutoMatchImageCache'] = self.auto_match_image_cache
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.compute_category is not None:
            result['ComputeCategory'] = self.compute_category
        result['Container'] = []
        if self.container is not None:
            for k in self.container:
                result['Container'].append(k.to_map() if k else None)
        if self.container_group_name is not None:
            result['ContainerGroupName'] = self.container_group_name
        if self.container_resource_view is not None:
            result['ContainerResourceView'] = self.container_resource_view
        if self.core_pattern is not None:
            result['CorePattern'] = self.core_pattern
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.cpu_architecture is not None:
            result['CpuArchitecture'] = self.cpu_architecture
        if self.cpu_options_core is not None:
            result['CpuOptionsCore'] = self.cpu_options_core
        if self.cpu_options_numa is not None:
            result['CpuOptionsNuma'] = self.cpu_options_numa
        if self.cpu_options_threads_per_core is not None:
            result['CpuOptionsThreadsPerCore'] = self.cpu_options_threads_per_core
        if self.data_cache_bucket is not None:
            result['DataCacheBucket'] = self.data_cache_bucket
        if self.data_cache_bursting_enabled is not None:
            result['DataCacheBurstingEnabled'] = self.data_cache_bursting_enabled
        if self.data_cache_pl is not None:
            result['DataCachePL'] = self.data_cache_pl
        if self.data_cache_provisioned_iops is not None:
            result['DataCacheProvisionedIops'] = self.data_cache_provisioned_iops
        if self.dns_policy is not None:
            result['DnsPolicy'] = self.dns_policy
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.egress_bandwidth is not None:
            result['EgressBandwidth'] = self.egress_bandwidth
        if self.eip_bandwidth is not None:
            result['EipBandwidth'] = self.eip_bandwidth
        if self.eip_common_bandwidth_package is not None:
            result['EipCommonBandwidthPackage'] = self.eip_common_bandwidth_package
        if self.eip_isp is not None:
            result['EipISP'] = self.eip_isp
        if self.eip_instance_id is not None:
            result['EipInstanceId'] = self.eip_instance_id
        if self.ephemeral_storage is not None:
            result['EphemeralStorage'] = self.ephemeral_storage
        if self.fixed_ip is not None:
            result['FixedIp'] = self.fixed_ip
        if self.fixed_ip_retain_hour is not None:
            result['FixedIpRetainHour'] = self.fixed_ip_retain_hour
        if self.gpu_driver_version is not None:
            result['GpuDriverVersion'] = self.gpu_driver_version
        result['HostAliase'] = []
        if self.host_aliase is not None:
            for k in self.host_aliase:
                result['HostAliase'].append(k.to_map() if k else None)
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.image_accelerate_mode is not None:
            result['ImageAccelerateMode'] = self.image_accelerate_mode
        result['ImageRegistryCredential'] = []
        if self.image_registry_credential is not None:
            for k in self.image_registry_credential:
                result['ImageRegistryCredential'].append(k.to_map() if k else None)
        if self.image_snapshot_id is not None:
            result['ImageSnapshotId'] = self.image_snapshot_id
        if self.ingress_bandwidth is not None:
            result['IngressBandwidth'] = self.ingress_bandwidth
        result['InitContainer'] = []
        if self.init_container is not None:
            for k in self.init_container:
                result['InitContainer'].append(k.to_map() if k else None)
        if self.insecure_registry is not None:
            result['InsecureRegistry'] = self.insecure_registry
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.ipv_6address_count is not None:
            result['Ipv6AddressCount'] = self.ipv_6address_count
        if self.ipv_6gateway_bandwidth is not None:
            result['Ipv6GatewayBandwidth'] = self.ipv_6gateway_bandwidth
        if self.ipv_6gateway_bandwidth_enable is not None:
            result['Ipv6GatewayBandwidthEnable'] = self.ipv_6gateway_bandwidth_enable
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.ntp_server is not None:
            result['NtpServer'] = self.ntp_server
        if self.os_type is not None:
            result['OsType'] = self.os_type
        if self.overhead_reservation_option is not None:
            result['OverheadReservationOption'] = self.overhead_reservation_option.to_map()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.plain_http_registry is not None:
            result['PlainHttpRegistry'] = self.plain_http_registry
        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address
        if self.ram_role_name is not None:
            result['RamRoleName'] = self.ram_role_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.restart_policy is not None:
            result['RestartPolicy'] = self.restart_policy
        if self.schedule_strategy is not None:
            result['ScheduleStrategy'] = self.schedule_strategy
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.share_process_namespace is not None:
            result['ShareProcessNamespace'] = self.share_process_namespace
        if self.spot_duration is not None:
            result['SpotDuration'] = self.spot_duration
        if self.spot_price_limit is not None:
            result['SpotPriceLimit'] = self.spot_price_limit
        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy
        if self.strict_spot is not None:
            result['StrictSpot'] = self.strict_spot
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.termination_grace_period_seconds is not None:
            result['TerminationGracePeriodSeconds'] = self.termination_grace_period_seconds
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        result['Volume'] = []
        if self.volume is not None:
            for k in self.volume:
                result['Volume'].append(k.to_map() if k else None)
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DnsConfig') is not None:
            temp_model = CreateContainerGroupRequestDnsConfig()
            self.dns_config = temp_model.from_map(m['DnsConfig'])
        if m.get('HostSecurityContext') is not None:
            temp_model = CreateContainerGroupRequestHostSecurityContext()
            self.host_security_context = temp_model.from_map(m['HostSecurityContext'])
        if m.get('SecurityContext') is not None:
            temp_model = CreateContainerGroupRequestSecurityContext()
            self.security_context = temp_model.from_map(m['SecurityContext'])
        self.acr_registry_info = []
        if m.get('AcrRegistryInfo') is not None:
            for k in m.get('AcrRegistryInfo'):
                temp_model = CreateContainerGroupRequestAcrRegistryInfo()
                self.acr_registry_info.append(temp_model.from_map(k))
        if m.get('ActiveDeadlineSeconds') is not None:
            self.active_deadline_seconds = m.get('ActiveDeadlineSeconds')
        if m.get('AutoCreateEip') is not None:
            self.auto_create_eip = m.get('AutoCreateEip')
        if m.get('AutoMatchImageCache') is not None:
            self.auto_match_image_cache = m.get('AutoMatchImageCache')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ComputeCategory') is not None:
            self.compute_category = m.get('ComputeCategory')
        self.container = []
        if m.get('Container') is not None:
            for k in m.get('Container'):
                temp_model = CreateContainerGroupRequestContainer()
                self.container.append(temp_model.from_map(k))
        if m.get('ContainerGroupName') is not None:
            self.container_group_name = m.get('ContainerGroupName')
        if m.get('ContainerResourceView') is not None:
            self.container_resource_view = m.get('ContainerResourceView')
        if m.get('CorePattern') is not None:
            self.core_pattern = m.get('CorePattern')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('CpuArchitecture') is not None:
            self.cpu_architecture = m.get('CpuArchitecture')
        if m.get('CpuOptionsCore') is not None:
            self.cpu_options_core = m.get('CpuOptionsCore')
        if m.get('CpuOptionsNuma') is not None:
            self.cpu_options_numa = m.get('CpuOptionsNuma')
        if m.get('CpuOptionsThreadsPerCore') is not None:
            self.cpu_options_threads_per_core = m.get('CpuOptionsThreadsPerCore')
        if m.get('DataCacheBucket') is not None:
            self.data_cache_bucket = m.get('DataCacheBucket')
        if m.get('DataCacheBurstingEnabled') is not None:
            self.data_cache_bursting_enabled = m.get('DataCacheBurstingEnabled')
        if m.get('DataCachePL') is not None:
            self.data_cache_pl = m.get('DataCachePL')
        if m.get('DataCacheProvisionedIops') is not None:
            self.data_cache_provisioned_iops = m.get('DataCacheProvisionedIops')
        if m.get('DnsPolicy') is not None:
            self.dns_policy = m.get('DnsPolicy')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EgressBandwidth') is not None:
            self.egress_bandwidth = m.get('EgressBandwidth')
        if m.get('EipBandwidth') is not None:
            self.eip_bandwidth = m.get('EipBandwidth')
        if m.get('EipCommonBandwidthPackage') is not None:
            self.eip_common_bandwidth_package = m.get('EipCommonBandwidthPackage')
        if m.get('EipISP') is not None:
            self.eip_isp = m.get('EipISP')
        if m.get('EipInstanceId') is not None:
            self.eip_instance_id = m.get('EipInstanceId')
        if m.get('EphemeralStorage') is not None:
            self.ephemeral_storage = m.get('EphemeralStorage')
        if m.get('FixedIp') is not None:
            self.fixed_ip = m.get('FixedIp')
        if m.get('FixedIpRetainHour') is not None:
            self.fixed_ip_retain_hour = m.get('FixedIpRetainHour')
        if m.get('GpuDriverVersion') is not None:
            self.gpu_driver_version = m.get('GpuDriverVersion')
        self.host_aliase = []
        if m.get('HostAliase') is not None:
            for k in m.get('HostAliase'):
                temp_model = CreateContainerGroupRequestHostAliase()
                self.host_aliase.append(temp_model.from_map(k))
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('ImageAccelerateMode') is not None:
            self.image_accelerate_mode = m.get('ImageAccelerateMode')
        self.image_registry_credential = []
        if m.get('ImageRegistryCredential') is not None:
            for k in m.get('ImageRegistryCredential'):
                temp_model = CreateContainerGroupRequestImageRegistryCredential()
                self.image_registry_credential.append(temp_model.from_map(k))
        if m.get('ImageSnapshotId') is not None:
            self.image_snapshot_id = m.get('ImageSnapshotId')
        if m.get('IngressBandwidth') is not None:
            self.ingress_bandwidth = m.get('IngressBandwidth')
        self.init_container = []
        if m.get('InitContainer') is not None:
            for k in m.get('InitContainer'):
                temp_model = CreateContainerGroupRequestInitContainer()
                self.init_container.append(temp_model.from_map(k))
        if m.get('InsecureRegistry') is not None:
            self.insecure_registry = m.get('InsecureRegistry')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('Ipv6AddressCount') is not None:
            self.ipv_6address_count = m.get('Ipv6AddressCount')
        if m.get('Ipv6GatewayBandwidth') is not None:
            self.ipv_6gateway_bandwidth = m.get('Ipv6GatewayBandwidth')
        if m.get('Ipv6GatewayBandwidthEnable') is not None:
            self.ipv_6gateway_bandwidth_enable = m.get('Ipv6GatewayBandwidthEnable')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('NtpServer') is not None:
            self.ntp_server = m.get('NtpServer')
        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')
        if m.get('OverheadReservationOption') is not None:
            temp_model = CreateContainerGroupRequestOverheadReservationOption()
            self.overhead_reservation_option = temp_model.from_map(m['OverheadReservationOption'])
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PlainHttpRegistry') is not None:
            self.plain_http_registry = m.get('PlainHttpRegistry')
        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')
        if m.get('RamRoleName') is not None:
            self.ram_role_name = m.get('RamRoleName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RestartPolicy') is not None:
            self.restart_policy = m.get('RestartPolicy')
        if m.get('ScheduleStrategy') is not None:
            self.schedule_strategy = m.get('ScheduleStrategy')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('ShareProcessNamespace') is not None:
            self.share_process_namespace = m.get('ShareProcessNamespace')
        if m.get('SpotDuration') is not None:
            self.spot_duration = m.get('SpotDuration')
        if m.get('SpotPriceLimit') is not None:
            self.spot_price_limit = m.get('SpotPriceLimit')
        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')
        if m.get('StrictSpot') is not None:
            self.strict_spot = m.get('StrictSpot')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateContainerGroupRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('TerminationGracePeriodSeconds') is not None:
            self.termination_grace_period_seconds = m.get('TerminationGracePeriodSeconds')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        self.volume = []
        if m.get('Volume') is not None:
            for k in m.get('Volume'):
                temp_model = CreateContainerGroupRequestVolume()
                self.volume.append(temp_model.from_map(k))
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CreateContainerGroupResponseBody(TeaModel):
    def __init__(
        self,
        container_group_id: str = None,
        request_id: str = None,
    ):
        # The ID of the instance.
        self.container_group_id = container_group_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.container_group_id is not None:
            result['ContainerGroupId'] = self.container_group_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContainerGroupId') is not None:
            self.container_group_id = m.get('ContainerGroupId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateContainerGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateContainerGroupResponseBody = None,
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
            temp_model = CreateContainerGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDataCacheRequestDataSource(TeaModel):
    def __init__(
        self,
        options: Dict[str, str] = None,
        type: str = None,
    ):
        # The parameters that are configured for the data source.
        self.options = options
        # The type of the data source. Valid values:
        # 
        # *   URL
        # *   NAS
        # *   OSS
        # *   SNAPSHOT
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.options is not None:
            result['Options'] = self.options
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Options') is not None:
            self.options = m.get('Options')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateDataCacheRequestEipCreateParam(TeaModel):
    def __init__(
        self,
        bandwidth: int = None,
        common_bandwidth_package: str = None,
        isp: str = None,
        internet_charge_type: str = None,
        public_ip_address_pool_id: str = None,
    ):
        # The bandwidth of the EIP. Unit: Mbit/s. Default value: 5.
        self.bandwidth = bandwidth
        # The EIP bandwidth plan to be associated.
        self.common_bandwidth_package = common_bandwidth_package
        # The line type of the EIP. Valid values:
        # 
        # *   BGP: BGP (Multi-ISP) line
        # *   BGP_PRO: BGP (Multi-ISP) Pro line
        self.isp = isp
        # The metering method of the EIP. Valid values:
        # 
        # *   PayByBandwidth: pay-by-bandwidth
        # *   PayByTraffic: pay-by-data-transfer
        self.internet_charge_type = internet_charge_type
        # The ID of the IP address pool. The EIP is allocated from the IP address pool. You cannot use the IP address pool feature by default. To use this feature, you must apply for the privilege in the Quota Center console.
        self.public_ip_address_pool_id = public_ip_address_pool_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.common_bandwidth_package is not None:
            result['CommonBandwidthPackage'] = self.common_bandwidth_package
        if self.isp is not None:
            result['ISP'] = self.isp
        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type
        if self.public_ip_address_pool_id is not None:
            result['PublicIpAddressPoolId'] = self.public_ip_address_pool_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('CommonBandwidthPackage') is not None:
            self.common_bandwidth_package = m.get('CommonBandwidthPackage')
        if m.get('ISP') is not None:
            self.isp = m.get('ISP')
        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')
        if m.get('PublicIpAddressPoolId') is not None:
            self.public_ip_address_pool_id = m.get('PublicIpAddressPoolId')
        return self


class CreateDataCacheRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag.
        self.key = key
        # The value of the tag.
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


class CreateDataCacheRequest(TeaModel):
    def __init__(
        self,
        bucket: str = None,
        client_token: str = None,
        data_source: CreateDataCacheRequestDataSource = None,
        eip_create_param: CreateDataCacheRequestEipCreateParam = None,
        eip_instance_id: str = None,
        name: str = None,
        owner_account: str = None,
        owner_id: int = None,
        path: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        retention_days: int = None,
        security_group_id: str = None,
        size: int = None,
        tag: List[CreateDataCacheRequestTag] = None,
        v_switch_id: str = None,
    ):
        # The bucket in which the data is stored. By default, the default bucket is used. You can use a custom bucket for business grouping and to prevent path conflicts.
        # 
        # >  eci-system is the reserved bucket of the ECI and cannot be used.
        self.bucket = bucket
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The data source.
        self.data_source = data_source
        # The elastic IP address (EIP) to be created and associated. If no NAT gateway is configured for the virtual private cloud (VPC), you can associate an EIP to pull data from the Internet.
        self.eip_create_param = eip_create_param
        # The existing elastic IP address (EIP) to be associated. If no NAT gateway is configured for the virtual private cloud (VPC), you can associate an EIP to pull data from the Internet.
        self.eip_instance_id = eip_instance_id
        # The DataCache name.
        self.name = name
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The storage path of the data.
        self.path = path
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The number of days for which the DataCache is retained. When the retention days end, the DataCache is deleted. By default, DataCaches do not expire.
        self.retention_days = retention_days
        # The ID of the security group to which the generated ECI belongs during the creation of the data cache.
        self.security_group_id = security_group_id
        # The size of the data cache. Unit: GiB. Default value: 20. Evaluate the required size based on the actual data size.
        self.size = size
        # The tags to be bound to the data cache.
        self.tag = tag
        # The ID of the vSwitch to which the generated ECI belongs during the creation of the data cache.
        self.v_switch_id = v_switch_id

    def validate(self):
        if self.data_source:
            self.data_source.validate()
        if self.eip_create_param:
            self.eip_create_param.validate()
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.data_source is not None:
            result['DataSource'] = self.data_source.to_map()
        if self.eip_create_param is not None:
            result['EipCreateParam'] = self.eip_create_param.to_map()
        if self.eip_instance_id is not None:
            result['EipInstanceId'] = self.eip_instance_id
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.path is not None:
            result['Path'] = self.path
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.retention_days is not None:
            result['RetentionDays'] = self.retention_days
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.size is not None:
            result['Size'] = self.size
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DataSource') is not None:
            temp_model = CreateDataCacheRequestDataSource()
            self.data_source = temp_model.from_map(m['DataSource'])
        if m.get('EipCreateParam') is not None:
            temp_model = CreateDataCacheRequestEipCreateParam()
            self.eip_create_param = temp_model.from_map(m['EipCreateParam'])
        if m.get('EipInstanceId') is not None:
            self.eip_instance_id = m.get('EipInstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RetentionDays') is not None:
            self.retention_days = m.get('RetentionDays')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateDataCacheRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        return self


class CreateDataCacheResponseBody(TeaModel):
    def __init__(
        self,
        data_cache_id: str = None,
        request_id: str = None,
    ):
        # The DataCache ID.
        self.data_cache_id = data_cache_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_cache_id is not None:
            result['DataCacheId'] = self.data_cache_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataCacheId') is not None:
            self.data_cache_id = m.get('DataCacheId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDataCacheResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDataCacheResponseBody = None,
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
            temp_model = CreateDataCacheResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateImageCacheRequestAcrRegistryInfo(TeaModel):
    def __init__(
        self,
        arn_service: str = None,
        arn_user: str = None,
        domain: List[str] = None,
        instance_id: str = None,
        instance_name: str = None,
        region_id: str = None,
    ):
        # The Alibaba Cloud Resource Name (ARN) of the RAM roles in the Alibaba Cloud account to which the elastic container instance belongs.
        self.arn_service = arn_service
        # The ARN of the RAM roles in the Alibaba Cloud account to which the Container Registry Enterprise Edition instance belongs.
        self.arn_user = arn_user
        # The domain names of the Container Registry Enterprise Edition instance. By default, all domain names of the instance are displayed. You can specify multiple domain names. Separate multiple domain names with commas (,).
        self.domain = domain
        # The ID of Container Registry Enterprise Edition instance N.
        self.instance_id = instance_id
        # The name of Container Registry Enterprise Edition instance N.
        self.instance_name = instance_name
        # The region ID of Container Registry Enterprise Edition instance N.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn_service is not None:
            result['ArnService'] = self.arn_service
        if self.arn_user is not None:
            result['ArnUser'] = self.arn_user
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArnService') is not None:
            self.arn_service = m.get('ArnService')
        if m.get('ArnUser') is not None:
            self.arn_user = m.get('ArnUser')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateImageCacheRequestImageRegistryCredential(TeaModel):
    def __init__(
        self,
        password: str = None,
        server: str = None,
        user_name: str = None,
    ):
        # The password that is used to log on to image repository N.
        self.password = password
        # The address of the image repository without the `http://` or `https://` prefix.
        self.server = server
        # The username that is used to log on to image repository N.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.password is not None:
            result['Password'] = self.password
        if self.server is not None:
            result['Server'] = self.server
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Server') is not None:
            self.server = m.get('Server')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class CreateImageCacheRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N of the image cache. Valid values of N: 1 to 20.
        self.key = key
        # The value of tag N of the image cache. Valid values of N: 1 to 20.
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


class CreateImageCacheRequest(TeaModel):
    def __init__(
        self,
        acr_registry_info: List[CreateImageCacheRequestAcrRegistryInfo] = None,
        annotations: str = None,
        auto_match_image_cache: bool = None,
        client_token: str = None,
        eip_instance_id: str = None,
        elimination_strategy: str = None,
        flash: bool = None,
        flash_copy_count: int = None,
        image: List[str] = None,
        image_cache_name: str = None,
        image_cache_size: int = None,
        image_registry_credential: List[CreateImageCacheRequestImageRegistryCredential] = None,
        insecure_registry: str = None,
        owner_account: str = None,
        owner_id: int = None,
        plain_http_registry: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        retention_days: int = None,
        security_group_id: str = None,
        standard_copy_count: int = None,
        tag: List[CreateImageCacheRequestTag] = None,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        # Information about the Container Registry Enterprise Edition instance. For more information, see [Pull images from a Container Registry Enterprise Edition instance without using secrets](https://help.aliyun.com/document_detail/194250.html).
        self.acr_registry_info = acr_registry_info
        # Comments.
        self.annotations = annotations
        # Specifies whether to enable reuse of image cache layers. If you enable this feature, and the image cache that you want to create and an existing image cache contain duplicate image layers, the system reuses the duplicate image layers to create the new image cache. This accelerates the creation of the image cache. Valid values:
        # 
        # *   true: enables reuse of image cache layers.
        # *   false: disables reuse of image cache layers.
        # 
        # Default value: false.
        self.auto_match_image_cache = auto_match_image_cache
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that the value is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure the idempotence of a request](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The ID of the elastic IP address (EIP). If you want to pull images over the Internet, make sure that the elastic container instance can access the Internet. You can configure an EIP or a NAT gateway for the elastic container instance to access the Internet.
        self.eip_instance_id = eip_instance_id
        # The elimination policy of the image cache. This parameter is empty by default, which indicates that the image cache is always retained.
        # 
        # You can set this parameter to LRU, which indicates that the image cache can be automatically deleted. When the number of image caches reaches the quota, the system automatically deletes the image caches whose EliminationStrategy parameter is set to LRU and that are least commonly used.
        self.elimination_strategy = elimination_strategy
        # Specifies whether to enable the instant image cache feature. The feature can accelerate the creation of image caches. Valid values:
        # 
        # *   true
        # *   false
        # 
        # Default value: false.
        self.flash = flash
        # The number of temporary local snapshots. By default, the system creates one snapshot for each image cache. If an image cache is used to create multiple elastic container instances at a time, we recommend that you set this parameter to create multiple snapshots for the image cache. We recommend that you create one snapshot for creation of every 1,000 elastic container instances.
        # 
        # >  If you set the Flash parameter to true, instant image cache is enabled. During the creation of the image cache, the system first creates a temporary local snapshot for you to instantly use the snapshot. After the temporary local snapshot is created, the system begins to create a regular snapshot. After the regular snapshot is created, the temporary local snapshot is automatically deleted.
        self.flash_copy_count = flash_copy_count
        # Container image N that is used to create the image cache.
        # 
        # This parameter is required.
        self.image = image
        # The name of the image cache.
        # 
        # This parameter is required.
        self.image_cache_name = image_cache_name
        # The size of the image cache. Unit: GiB. Default value: 20.
        self.image_cache_size = image_cache_size
        # The image repository.
        self.image_registry_credential = image_registry_credential
        # The address of the self-managed image repository.
        # 
        # When you create an image cache by using an image in a self-managed image repository that uses a self-signed certificate, you must specify this parameter to skip the certificate authentication. This can prevent the image from failing to pull due to certificate authentication failures.
        self.insecure_registry = insecure_registry
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The address of the self-managed image repository. When you create an image cache by using an image in a self-managed image repository that uses the HTTP protocol, you must specify this parameter. This way, Elastic Container Instance uses the HTTP protocol instead of the default HTTPS protocol to pull the image. This can prevent the image from failing to pull due to different protocols.
        self.plain_http_registry = plain_http_registry
        # The region ID of the image cache.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The retention period of the image cache. Unit: days. When the retention period ends, the image cache expires and is deleted. By default, image caches never expire.
        # 
        # >  The image caches that fail to be created are only retained for one day.
        self.retention_days = retention_days
        # The ID of the security group.
        self.security_group_id = security_group_id
        # The number of regular snapshots. By default, the system creates one snapshot for each image cache. If an image cache is used to create multiple elastic container instances at a time, we recommend that you set this parameter to create multiple snapshots for the image cache. We recommend that you create one snapshot for creation of every 1,000 elastic container instances.
        # 
        # >  If you set the Flash parameter to false, instant image cache is disabled. In this case, only regular snapshots are generated during the creation of the image cache.
        self.standard_copy_count = standard_copy_count
        # The tag of the image cache.
        self.tag = tag
        # The ID of the vSwitch. You can specify up to 10 vSwitch IDs. Separate multiple vSwitch IDs with commas (,). Example: `vsw-***,vsw-***`.
        self.v_switch_id = v_switch_id
        # The zone ID of the image cache.
        self.zone_id = zone_id

    def validate(self):
        if self.acr_registry_info:
            for k in self.acr_registry_info:
                if k:
                    k.validate()
        if self.image_registry_credential:
            for k in self.image_registry_credential:
                if k:
                    k.validate()
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AcrRegistryInfo'] = []
        if self.acr_registry_info is not None:
            for k in self.acr_registry_info:
                result['AcrRegistryInfo'].append(k.to_map() if k else None)
        if self.annotations is not None:
            result['Annotations'] = self.annotations
        if self.auto_match_image_cache is not None:
            result['AutoMatchImageCache'] = self.auto_match_image_cache
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.eip_instance_id is not None:
            result['EipInstanceId'] = self.eip_instance_id
        if self.elimination_strategy is not None:
            result['EliminationStrategy'] = self.elimination_strategy
        if self.flash is not None:
            result['Flash'] = self.flash
        if self.flash_copy_count is not None:
            result['FlashCopyCount'] = self.flash_copy_count
        if self.image is not None:
            result['Image'] = self.image
        if self.image_cache_name is not None:
            result['ImageCacheName'] = self.image_cache_name
        if self.image_cache_size is not None:
            result['ImageCacheSize'] = self.image_cache_size
        result['ImageRegistryCredential'] = []
        if self.image_registry_credential is not None:
            for k in self.image_registry_credential:
                result['ImageRegistryCredential'].append(k.to_map() if k else None)
        if self.insecure_registry is not None:
            result['InsecureRegistry'] = self.insecure_registry
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.plain_http_registry is not None:
            result['PlainHttpRegistry'] = self.plain_http_registry
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.retention_days is not None:
            result['RetentionDays'] = self.retention_days
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.standard_copy_count is not None:
            result['StandardCopyCount'] = self.standard_copy_count
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.acr_registry_info = []
        if m.get('AcrRegistryInfo') is not None:
            for k in m.get('AcrRegistryInfo'):
                temp_model = CreateImageCacheRequestAcrRegistryInfo()
                self.acr_registry_info.append(temp_model.from_map(k))
        if m.get('Annotations') is not None:
            self.annotations = m.get('Annotations')
        if m.get('AutoMatchImageCache') is not None:
            self.auto_match_image_cache = m.get('AutoMatchImageCache')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('EipInstanceId') is not None:
            self.eip_instance_id = m.get('EipInstanceId')
        if m.get('EliminationStrategy') is not None:
            self.elimination_strategy = m.get('EliminationStrategy')
        if m.get('Flash') is not None:
            self.flash = m.get('Flash')
        if m.get('FlashCopyCount') is not None:
            self.flash_copy_count = m.get('FlashCopyCount')
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('ImageCacheName') is not None:
            self.image_cache_name = m.get('ImageCacheName')
        if m.get('ImageCacheSize') is not None:
            self.image_cache_size = m.get('ImageCacheSize')
        self.image_registry_credential = []
        if m.get('ImageRegistryCredential') is not None:
            for k in m.get('ImageRegistryCredential'):
                temp_model = CreateImageCacheRequestImageRegistryCredential()
                self.image_registry_credential.append(temp_model.from_map(k))
        if m.get('InsecureRegistry') is not None:
            self.insecure_registry = m.get('InsecureRegistry')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PlainHttpRegistry') is not None:
            self.plain_http_registry = m.get('PlainHttpRegistry')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RetentionDays') is not None:
            self.retention_days = m.get('RetentionDays')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('StandardCopyCount') is not None:
            self.standard_copy_count = m.get('StandardCopyCount')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateImageCacheRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CreateImageCacheResponseBody(TeaModel):
    def __init__(
        self,
        container_group_id: str = None,
        image_cache_id: str = None,
        request_id: str = None,
    ):
        # The ID of the intermediate elastic container instance that is used to create the image cache.
        self.container_group_id = container_group_id
        # The ID of the image cache.
        self.image_cache_id = image_cache_id
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.container_group_id is not None:
            result['ContainerGroupId'] = self.container_group_id
        if self.image_cache_id is not None:
            result['ImageCacheId'] = self.image_cache_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContainerGroupId') is not None:
            self.container_group_id = m.get('ContainerGroupId')
        if m.get('ImageCacheId') is not None:
            self.image_cache_id = m.get('ImageCacheId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateImageCacheResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateImageCacheResponseBody = None,
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
            temp_model = CreateImageCacheResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateInstanceOpsTaskRequest(TeaModel):
    def __init__(
        self,
        container_group_id: str = None,
        ops_type: str = None,
        ops_value: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The ID of the container group.
        # 
        # This parameter is required.
        self.container_group_id = container_group_id
        # The type of the O&M task. Valid values:
        # 
        # *   coredump
        # *   tcpdump
        # 
        # This parameter is required.
        self.ops_type = ops_type
        # The value of the O\\&M task. You can set this parameter based on the value of OpsType.
        # 
        # *   If OpsType is set to coredump, the valid values of OpsValue are:
        # 
        #     *   enable: enables coredump.
        #     *   disable: disables coredump.
        # 
        # *   If OpsType is set to tcpdump, the value of OpsValue is a JSON-formatted parameter string. Example: `{"Enable":true, "IfDeviceName":"eth0"}`. The value may contain the following parameters:
        # 
        #     *   Enable: specifies whether to enable tcpdump. You must specify this parameter. Valid values: true and false.
        #     *   Protocol: the network protocol. Valid values: tcp, udp, and icmpv4.
        #     *   SourceIp: the source IP address.
        #     *   SourceCidr: the source CIDR block. If you specify both an IP address and a CIDR block, the IP address is ignored if the CIDR block is valid.
        #     *   SourcePort: the source port. Valid values: 1 to 65535.
        #     *   DestIp: the destination IP address.
        #     *   DestCidr: the destination CIDR block. If you specify both an IP address and a CIDR block, the IP address is ignored if the CIDR block is valid.
        #     *   DestPort: the destination port. Valid values: 1 to 65535.
        #     *   IfDeviceName: the destination network interface controller. Default value: eth0.
        #     *   Snaplen: the length to be captured. Default value: 65535. Unit: bytes.
        #     *   Duration: the captured period. Unit: seconds.
        #     *   PacketNum: the number of packets to be captured.
        #     *   FileSize: the size of the destination files on packets. Unit: bytes. Maximum value: 1073741824. 1073741824 bytes is equal to 1 GB.
        # 
        # This parameter is required.
        self.ops_value = ops_value
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the O&M task.
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
        if self.container_group_id is not None:
            result['ContainerGroupId'] = self.container_group_id
        if self.ops_type is not None:
            result['OpsType'] = self.ops_type
        if self.ops_value is not None:
            result['OpsValue'] = self.ops_value
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
        if m.get('ContainerGroupId') is not None:
            self.container_group_id = m.get('ContainerGroupId')
        if m.get('OpsType') is not None:
            self.ops_type = m.get('OpsType')
        if m.get('OpsValue') is not None:
            self.ops_value = m.get('OpsValue')
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


class CreateInstanceOpsTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The creation result of the O&M task.
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class CreateInstanceOpsTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateInstanceOpsTaskResponseBody = None,
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
            temp_model = CreateInstanceOpsTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateVirtualNodeRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag.
        self.key = key
        # The value of tag.
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


class CreateVirtualNodeRequestTaint(TeaModel):
    def __init__(
        self,
        effect: str = None,
        key: str = None,
        value: str = None,
    ):
        # The effect of taint N. Valid values of N: 1 to 20. Valid values:
        # 
        # - NoSchedule: No pods are scheduled to the nodes that have the taint.
        # - NoExecute: Existing pods in the node are evicted while no pods are scheduled to the nodes that have the taint.
        # - PreferNoSchedule: Pods are preferentially not scheduled to the nodes that have the taint.
        self.effect = effect
        # The key of taint.
        self.key = key
        # The value of taint.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.effect is not None:
            result['Effect'] = self.effect
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Effect') is not None:
            self.effect = m.get('Effect')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateVirtualNodeRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        cluster_dns: str = None,
        cluster_domain: str = None,
        custom_resources: str = None,
        eip_instance_id: str = None,
        enable_public_network: bool = None,
        kube_config: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_group_id: str = None,
        tag: List[CreateVirtualNodeRequestTag] = None,
        taint: List[CreateVirtualNodeRequestTaint] = None,
        tls_bootstrap_enabled: bool = None,
        v_switch_id: str = None,
        virtual_node_name: str = None,
        zone_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that the value is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The IP address of the DNS server. If dnsPolicy=ClusterFirst is configured for the Elastic Container Instance pod, Elastic Container Instance uses the configuration to provide DNS services to containers. You can configure multiple IP addresses. Separate multiple IP addresses with commas (,).
        self.cluster_dns = cluster_dns
        # The domain name of the cluster. If this parameter is specified, in addition to the search domain of the host, Kubelet configures all containers to search for the specified domain name.
        self.cluster_domain = cluster_domain
        # The custom resources that are supported by the virtual node. If a custom resource is specified in the request of an Elastic Container Instance pod, the pod is scheduled to run on the virtual node that supports the custom resource. You can use the Resource name = Number of resources format to specify custom resources. Separate multiple resources with commas (,).
        self.custom_resources = custom_resources
        # The ID of the elastic IP address (EIP).
        self.eip_instance_id = eip_instance_id
        # Specifies whether to enable Internet access for the VNode. Default value: false.
        # 
        # If the value of this parameter is true, the VNode exposes a public IP address to external services.
        self.enable_public_network = enable_public_network
        # KubeConfig of the Kubernetes cluster to which the VNode is to be connected. The value must be Base64-encoded.
        self.kube_config = kube_config
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the virtual node.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the security group. The VNode and the elastic container instances in the VNode are added to the security group.
        # 
        # This parameter is required.
        self.security_group_id = security_group_id
        # Tag.
        self.tag = tag
        # Taint.
        self.taint = taint
        # Specifies whether to enable TLS bootstrapping. If you set this parameter to true, use the KubeConfig certificate for TLS bootstrapping. Valid values:
        # 
        # - true
        # - false
        # 
        # Default value: false.
        self.tls_bootstrap_enabled = tls_bootstrap_enabled
        # The ID of the vSwitch. The vSwitch is connected to the VNode and the elastic container instances in the VNode.
        # 
        # You can specify 1 to 10 vSwitches for a VPC.
        # 
        # This parameter is required.
        self.v_switch_id = v_switch_id
        # The name of the VNode. The name must be 2 to 128 characters in length, and can contain lowercase letters, digits, periods (.), and hyphens (-).
        self.virtual_node_name = virtual_node_name
        # The zone ID of the VNode.
        self.zone_id = zone_id

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()
        if self.taint:
            for k in self.taint:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.cluster_dns is not None:
            result['ClusterDNS'] = self.cluster_dns
        if self.cluster_domain is not None:
            result['ClusterDomain'] = self.cluster_domain
        if self.custom_resources is not None:
            result['CustomResources'] = self.custom_resources
        if self.eip_instance_id is not None:
            result['EipInstanceId'] = self.eip_instance_id
        if self.enable_public_network is not None:
            result['EnablePublicNetwork'] = self.enable_public_network
        if self.kube_config is not None:
            result['KubeConfig'] = self.kube_config
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
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        result['Taint'] = []
        if self.taint is not None:
            for k in self.taint:
                result['Taint'].append(k.to_map() if k else None)
        if self.tls_bootstrap_enabled is not None:
            result['TlsBootstrapEnabled'] = self.tls_bootstrap_enabled
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.virtual_node_name is not None:
            result['VirtualNodeName'] = self.virtual_node_name
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ClusterDNS') is not None:
            self.cluster_dns = m.get('ClusterDNS')
        if m.get('ClusterDomain') is not None:
            self.cluster_domain = m.get('ClusterDomain')
        if m.get('CustomResources') is not None:
            self.custom_resources = m.get('CustomResources')
        if m.get('EipInstanceId') is not None:
            self.eip_instance_id = m.get('EipInstanceId')
        if m.get('EnablePublicNetwork') is not None:
            self.enable_public_network = m.get('EnablePublicNetwork')
        if m.get('KubeConfig') is not None:
            self.kube_config = m.get('KubeConfig')
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
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateVirtualNodeRequestTag()
                self.tag.append(temp_model.from_map(k))
        self.taint = []
        if m.get('Taint') is not None:
            for k in m.get('Taint'):
                temp_model = CreateVirtualNodeRequestTaint()
                self.taint.append(temp_model.from_map(k))
        if m.get('TlsBootstrapEnabled') is not None:
            self.tls_bootstrap_enabled = m.get('TlsBootstrapEnabled')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VirtualNodeName') is not None:
            self.virtual_node_name = m.get('VirtualNodeName')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CreateVirtualNodeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        virtual_node_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The ID of the VNode.
        self.virtual_node_id = virtual_node_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.virtual_node_id is not None:
            result['VirtualNodeId'] = self.virtual_node_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('VirtualNodeId') is not None:
            self.virtual_node_id = m.get('VirtualNodeId')
        return self


class CreateVirtualNodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateVirtualNodeResponseBody = None,
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
            temp_model = CreateVirtualNodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteContainerGroupRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        container_group_id: str = None,
        force: bool = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure the idempotence of a request?](https://help.aliyun.com/document_detail/25693.html)
        self.client_token = client_token
        # The instance ID.
        # 
        # This parameter is required.
        self.container_group_id = container_group_id
        self.force = force
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the instance.
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
        if self.container_group_id is not None:
            result['ContainerGroupId'] = self.container_group_id
        if self.force is not None:
            result['Force'] = self.force
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
        if m.get('ContainerGroupId') is not None:
            self.container_group_id = m.get('ContainerGroupId')
        if m.get('Force') is not None:
            self.force = m.get('Force')
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


class DeleteContainerGroupResponseBody(TeaModel):
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


class DeleteContainerGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteContainerGroupResponseBody = None,
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
            temp_model = DeleteContainerGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDataCacheRequest(TeaModel):
    def __init__(
        self,
        bucket: str = None,
        client_token: str = None,
        data_cache_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        path: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The bucket that stores the DataCache. By default, the bucket is named default.
        self.bucket = bucket
        # The client token that is used to ensure the idempotency of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure the idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The ID of the DataCache.
        self.data_cache_id = data_cache_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The directory in which the virtual host of the DataCache is located.
        self.path = path
        # The region ID of the DataCache.
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
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.data_cache_id is not None:
            result['DataCacheId'] = self.data_cache_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.path is not None:
            result['Path'] = self.path
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DataCacheId') is not None:
            self.data_cache_id = m.get('DataCacheId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DeleteDataCacheResponseBody(TeaModel):
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


class DeleteDataCacheResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDataCacheResponseBody = None,
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
            temp_model = DeleteDataCacheResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteImageCacheRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        image_cache_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The client token that is used to ensure the idempotency of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure the idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The ID of the image cache.
        # 
        # This parameter is required.
        self.image_cache_id = image_cache_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the image cache.
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
        if self.image_cache_id is not None:
            result['ImageCacheId'] = self.image_cache_id
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
        if m.get('ImageCacheId') is not None:
            self.image_cache_id = m.get('ImageCacheId')
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


class DeleteImageCacheResponseBody(TeaModel):
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


class DeleteImageCacheResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteImageCacheResponseBody = None,
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
            temp_model = DeleteImageCacheResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteVirtualNodeRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        virtual_node_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that the value is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotency of requests](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the virtual node.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the virtual node.
        # 
        # This parameter is required.
        self.virtual_node_id = virtual_node_id

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
        if self.virtual_node_id is not None:
            result['VirtualNodeId'] = self.virtual_node_id
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
        if m.get('VirtualNodeId') is not None:
            self.virtual_node_id = m.get('VirtualNodeId')
        return self


class DeleteVirtualNodeResponseBody(TeaModel):
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


class DeleteVirtualNodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteVirtualNodeResponseBody = None,
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
            temp_model = DeleteVirtualNodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAvailableResourceRequestDestinationResource(TeaModel):
    def __init__(
        self,
        category: str = None,
        cores: float = None,
        memory: float = None,
        value: str = None,
    ):
        # The type of the resource. Valid values:
        # 
        # *   InstanceTypeFamily: queries instance families. If you use this parameter value, you must also specify the Value parameter.
        # *   InstanceType: queries instance types. If you use this parameter value, you must also specify the Value, Cores, and Memory parameters.
        # 
        # This parameter is required.
        self.category = category
        # The number of vCPUs. This parameter is available only when the Category parameter is set to InstanceType.
        self.cores = cores
        # The size of the memory. Unit: GiB. This parameter is available only when the Category parameter is set to InstanceType.
        self.memory = memory
        # Instance families or instance types.
        # 
        # *   If you set Category to InstanceTypeFamily, you must set this parameter to instance families such as ecs.c5.
        # *   If you set Category to InstanceType, you must set this parameter to instance types such as ecs.c5.large.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.cores is not None:
            result['Cores'] = self.cores
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Cores') is not None:
            self.cores = m.get('Cores')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeAvailableResourceRequestSpotResource(TeaModel):
    def __init__(
        self,
        spot_duration: int = None,
        spot_price_limit: float = None,
        spot_strategy: str = None,
    ):
        # The protection period of the preemptible instance. Unit: hours. Default value: 1. The value of 0 indicates no protection period.
        self.spot_duration = spot_duration
        # The maximum hourly price of the preemptible elastic container instance. The value can be accurate to three decimal places. If you set SpotStrategy to SpotWithPriceLimit, you must specify the SpotPriceLimit parameter.
        self.spot_price_limit = spot_price_limit
        # The bidding policy for the elastic container instance. Valid values:
        # 
        # *   NoSpot: The instance is created as a regular pay-as-you-go instance.
        # *   SpotWithPriceLimit: The instance is created as a preemptible instance with a user-defined maximum hourly price.
        # *   SpotAsPriceGo: The instance is created as a preemptible instance for which the market price at the time of purchase is automatically used as the bid price.
        # 
        # Default value: NoSpot.
        # 
        # > If you set this parameter to SpotWithPriceLimit or SpotAsPriceGo to query preemptible instances, you must set Category to InstanceType. You must also use the Value parameter to specify instance types, or use the Cores and Memory parameters to specify the number of vCPUs and memory size.
        self.spot_strategy = spot_strategy

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.spot_duration is not None:
            result['SpotDuration'] = self.spot_duration
        if self.spot_price_limit is not None:
            result['SpotPriceLimit'] = self.spot_price_limit
        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpotDuration') is not None:
            self.spot_duration = m.get('SpotDuration')
        if m.get('SpotPriceLimit') is not None:
            self.spot_price_limit = m.get('SpotPriceLimit')
        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')
        return self


class DescribeAvailableResourceRequest(TeaModel):
    def __init__(
        self,
        destination_resource: DescribeAvailableResourceRequestDestinationResource = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        spot_resource: DescribeAvailableResourceRequestSpotResource = None,
        zone_id: str = None,
    ):
        # The information about the resource that you want to query.
        # 
        # This parameter is required.
        self.destination_resource = destination_resource
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the ECS instance families.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/146965.html) operation to query the most recent list of regions.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The information about the preemptible instances that you want to query.
        self.spot_resource = spot_resource
        # The zone ID of the ECS instance families.
        # 
        # This parameter is empty by default, which indicates that ECS instance families available in all zones in the specified region are queried.
        self.zone_id = zone_id

    def validate(self):
        if self.destination_resource:
            self.destination_resource.validate()
        if self.spot_resource:
            self.spot_resource.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_resource is not None:
            result['DestinationResource'] = self.destination_resource.to_map()
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
        if self.spot_resource is not None:
            result['SpotResource'] = self.spot_resource.to_map()
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationResource') is not None:
            temp_model = DescribeAvailableResourceRequestDestinationResource()
            self.destination_resource = temp_model.from_map(m['DestinationResource'])
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
        if m.get('SpotResource') is not None:
            temp_model = DescribeAvailableResourceRequestSpotResource()
            self.spot_resource = temp_model.from_map(m['SpotResource'])
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneAvailableResourcesAvailableResourceSupportedResourcesSupportedResource(TeaModel):
    def __init__(
        self,
        status_category: str = None,
        value: str = None,
    ):
        # The category of resources based on stock status. Valid values:
        # 
        # *   WithStock: Resources are in sufficient stock.
        # *   ClosedWithStock: Resources are insufficient. We recommend that you use instance types that are in sufficient stock.
        # *   WithoutStock: Resources are sold out and will be replenished. We recommend that you use instance types that are in sufficient stock.
        # *   ClosedWithoutStock: Resources are sold out and will not be replenished. We recommend that you use instance types that are in sufficient stock.
        self.status_category = status_category
        # The ECS instance types or instance families that are available in the zones.
        # 
        # *   If the return value of the Type parameter is InstanceTypeFamily, this parameter indicates instance families that are returned.
        # *   If the return value of the Type parameter is InstanceType, this parameter indicates instance types that are returned.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status_category is not None:
            result['StatusCategory'] = self.status_category
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StatusCategory') is not None:
            self.status_category = m.get('StatusCategory')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneAvailableResourcesAvailableResourceSupportedResources(TeaModel):
    def __init__(
        self,
        supported_resource: List[DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneAvailableResourcesAvailableResourceSupportedResourcesSupportedResource] = None,
    ):
        self.supported_resource = supported_resource

    def validate(self):
        if self.supported_resource:
            for k in self.supported_resource:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SupportedResource'] = []
        if self.supported_resource is not None:
            for k in self.supported_resource:
                result['SupportedResource'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.supported_resource = []
        if m.get('SupportedResource') is not None:
            for k in m.get('SupportedResource'):
                temp_model = DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneAvailableResourcesAvailableResourceSupportedResourcesSupportedResource()
                self.supported_resource.append(temp_model.from_map(k))
        return self


class DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneAvailableResourcesAvailableResource(TeaModel):
    def __init__(
        self,
        supported_resources: DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneAvailableResourcesAvailableResourceSupportedResources = None,
        type: str = None,
    ):
        # The information about the resources that are available in the zones.
        self.supported_resources = supported_resources
        # The type of the resource. Valid values:
        # 
        # *   InstanceTypeFamily: instance families.
        # *   InstanceType: instance types.
        self.type = type

    def validate(self):
        if self.supported_resources:
            self.supported_resources.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.supported_resources is not None:
            result['SupportedResources'] = self.supported_resources.to_map()
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SupportedResources') is not None:
            temp_model = DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneAvailableResourcesAvailableResourceSupportedResources()
            self.supported_resources = temp_model.from_map(m['SupportedResources'])
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneAvailableResources(TeaModel):
    def __init__(
        self,
        available_resource: List[DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneAvailableResourcesAvailableResource] = None,
    ):
        self.available_resource = available_resource

    def validate(self):
        if self.available_resource:
            for k in self.available_resource:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AvailableResource'] = []
        if self.available_resource is not None:
            for k in self.available_resource:
                result['AvailableResource'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.available_resource = []
        if m.get('AvailableResource') is not None:
            for k in m.get('AvailableResource'):
                temp_model = DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneAvailableResourcesAvailableResource()
                self.available_resource.append(temp_model.from_map(k))
        return self


class DescribeAvailableResourceResponseBodyAvailableZonesAvailableZone(TeaModel):
    def __init__(
        self,
        available_resources: DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneAvailableResources = None,
        region_id: str = None,
        zone_id: str = None,
    ):
        # The resources that are available in the specified zone.
        self.available_resources = available_resources
        # The region ID of the resources.
        self.region_id = region_id
        # The zone ID of the resources.
        self.zone_id = zone_id

    def validate(self):
        if self.available_resources:
            self.available_resources.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.available_resources is not None:
            result['AvailableResources'] = self.available_resources.to_map()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableResources') is not None:
            temp_model = DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneAvailableResources()
            self.available_resources = temp_model.from_map(m['AvailableResources'])
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeAvailableResourceResponseBodyAvailableZones(TeaModel):
    def __init__(
        self,
        available_zone: List[DescribeAvailableResourceResponseBodyAvailableZonesAvailableZone] = None,
    ):
        self.available_zone = available_zone

    def validate(self):
        if self.available_zone:
            for k in self.available_zone:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AvailableZone'] = []
        if self.available_zone is not None:
            for k in self.available_zone:
                result['AvailableZone'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.available_zone = []
        if m.get('AvailableZone') is not None:
            for k in m.get('AvailableZone'):
                temp_model = DescribeAvailableResourceResponseBodyAvailableZonesAvailableZone()
                self.available_zone.append(temp_model.from_map(k))
        return self


class DescribeAvailableResourceResponseBody(TeaModel):
    def __init__(
        self,
        available_zones: DescribeAvailableResourceResponseBodyAvailableZones = None,
        request_id: str = None,
    ):
        # The zones in which the specified resources are available.
        self.available_zones = available_zones
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.available_zones:
            self.available_zones.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.available_zones is not None:
            result['AvailableZones'] = self.available_zones.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableZones') is not None:
            temp_model = DescribeAvailableResourceResponseBodyAvailableZones()
            self.available_zones = temp_model.from_map(m['AvailableZones'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeAvailableResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAvailableResourceResponseBody = None,
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
            temp_model = DescribeAvailableResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCommitContainerTaskRequest(TeaModel):
    def __init__(
        self,
        container_group_id: str = None,
        max_results: int = None,
        next_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        task_id: List[str] = None,
        task_status: str = None,
    ):
        # The ID of the elastic container instance on which the CommitContainer task is executed.\\
        # You must enter the instance ID, the task ID, or both for the request.
        self.container_group_id = container_group_id
        # The number of entries to return on each page.\\
        # Maximum value: 50.\\
        # Default value: 10.
        self.max_results = max_results
        # The token that determines the start point of the query. Set the value to the value of NextToken that is returned from the last request.
        self.next_token = next_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the region.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the task.
        self.task_id = task_id
        # The status of the task. Valid values:
        # 
        # *   Running
        # *   Succeeded
        # *   Failed
        self.task_status = task_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.container_group_id is not None:
            result['ContainerGroupId'] = self.container_group_id
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
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContainerGroupId') is not None:
            self.container_group_id = m.get('ContainerGroupId')
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
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        return self


class DescribeCommitContainerTaskResponseBodyCommitTasksCommitPhaseInfos(TeaModel):
    def __init__(
        self,
        message: str = None,
        phase: str = None,
        record_time: str = None,
        status: str = None,
    ):
        # The message about the phase.
        self.message = message
        # The phase name. Valid values:
        # 
        # *   PullBaseImage: Pull the original container image.
        # *   CommitContainer: Commit the container to generate an image.
        # *   PushCommittedImage: Push the image to Container Registry.
        self.phase = phase
        # The record time of the phase.
        self.record_time = record_time
        # The state of the phase.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.phase is not None:
            result['Phase'] = self.phase
        if self.record_time is not None:
            result['RecordTime'] = self.record_time
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Phase') is not None:
            self.phase = m.get('Phase')
        if m.get('RecordTime') is not None:
            self.record_time = m.get('RecordTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeCommitContainerTaskResponseBodyCommitTasks(TeaModel):
    def __init__(
        self,
        commit_phase_infos: List[DescribeCommitContainerTaskResponseBodyCommitTasksCommitPhaseInfos] = None,
        container_name: str = None,
        status_message: str = None,
        task_creation_time: str = None,
        task_finished_time: str = None,
        task_id: str = None,
        task_progress: str = None,
        task_status: str = None,
    ):
        # The information about the phase that the task arrives.
        self.commit_phase_infos = commit_phase_infos
        # The container name.
        self.container_name = container_name
        # The message about the state.
        self.status_message = status_message
        # The time when the task was started.
        self.task_creation_time = task_creation_time
        # The time when the task was complete.
        self.task_finished_time = task_finished_time
        # The task ID.
        self.task_id = task_id
        # The progress of the task in percentage.
        self.task_progress = task_progress
        # The state of the task. Valid values:
        # 
        # *   Running
        # *   Succeeded
        # *   Failed
        self.task_status = task_status

    def validate(self):
        if self.commit_phase_infos:
            for k in self.commit_phase_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CommitPhaseInfos'] = []
        if self.commit_phase_infos is not None:
            for k in self.commit_phase_infos:
                result['CommitPhaseInfos'].append(k.to_map() if k else None)
        if self.container_name is not None:
            result['ContainerName'] = self.container_name
        if self.status_message is not None:
            result['StatusMessage'] = self.status_message
        if self.task_creation_time is not None:
            result['TaskCreationTime'] = self.task_creation_time
        if self.task_finished_time is not None:
            result['TaskFinishedTime'] = self.task_finished_time
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_progress is not None:
            result['TaskProgress'] = self.task_progress
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.commit_phase_infos = []
        if m.get('CommitPhaseInfos') is not None:
            for k in m.get('CommitPhaseInfos'):
                temp_model = DescribeCommitContainerTaskResponseBodyCommitTasksCommitPhaseInfos()
                self.commit_phase_infos.append(temp_model.from_map(k))
        if m.get('ContainerName') is not None:
            self.container_name = m.get('ContainerName')
        if m.get('StatusMessage') is not None:
            self.status_message = m.get('StatusMessage')
        if m.get('TaskCreationTime') is not None:
            self.task_creation_time = m.get('TaskCreationTime')
        if m.get('TaskFinishedTime') is not None:
            self.task_finished_time = m.get('TaskFinishedTime')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskProgress') is not None:
            self.task_progress = m.get('TaskProgress')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        return self


class DescribeCommitContainerTaskResponseBody(TeaModel):
    def __init__(
        self,
        commit_tasks: List[DescribeCommitContainerTaskResponseBodyCommitTasks] = None,
        max_results: str = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # Details of the task.
        self.commit_tasks = commit_tasks
        # The number of entries returned per page.
        self.max_results = max_results
        # The query token that is returned in this request.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.commit_tasks:
            for k in self.commit_tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CommitTasks'] = []
        if self.commit_tasks is not None:
            for k in self.commit_tasks:
                result['CommitTasks'].append(k.to_map() if k else None)
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
        self.commit_tasks = []
        if m.get('CommitTasks') is not None:
            for k in m.get('CommitTasks'):
                temp_model = DescribeCommitContainerTaskResponseBodyCommitTasks()
                self.commit_tasks.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeCommitContainerTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCommitContainerTaskResponseBody = None,
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
            temp_model = DescribeCommitContainerTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeContainerGroupEventsRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag.
        self.key = key
        # The value of the tag.
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


class DescribeContainerGroupEventsRequest(TeaModel):
    def __init__(
        self,
        container_group_ids: str = None,
        event_source: str = None,
        limit: int = None,
        next_token: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        since_second: int = None,
        tag: List[DescribeContainerGroupEventsRequestTag] = None,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        # The IDs of the elastic container instances. You can specify up to 20 IDs. Each ID must be a JSON string.
        self.container_group_ids = container_group_ids
        # The event source. Valid values:
        # 
        # *   EciService
        # *   K8sAgent
        # 
        # This parameter is empty by default. This indicates that all events are queried.
        self.event_source = event_source
        # The maximum number of elastic container instances to be returned for this request. Default value: 200.
        # 
        # >  The number of elastic container instances to be returned is no greater than this parameter value.
        self.limit = limit
        # The pagination token that is used in the next request to retrieve a new page of results. If NextToken is empty, no next page exists.
        # 
        # You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # A relative time in seconds before the current time from which to show event information. This parameter is used to poll incremental events.
        self.since_second = since_second
        # The tag that is added to the elastic container instances.
        self.tag = tag
        # The vSwitch ID.
        self.v_switch_id = v_switch_id
        # The zone ID.
        self.zone_id = zone_id

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
        if self.container_group_ids is not None:
            result['ContainerGroupIds'] = self.container_group_ids
        if self.event_source is not None:
            result['EventSource'] = self.event_source
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.since_second is not None:
            result['SinceSecond'] = self.since_second
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContainerGroupIds') is not None:
            self.container_group_ids = m.get('ContainerGroupIds')
        if m.get('EventSource') is not None:
            self.event_source = m.get('EventSource')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SinceSecond') is not None:
            self.since_second = m.get('SinceSecond')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeContainerGroupEventsRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeContainerGroupEventsResponseBodyDataEventsMetadata(TeaModel):
    def __init__(
        self,
        name: str = None,
        namespace: str = None,
    ):
        # The event name.
        self.name = name
        # The namespace.
        self.namespace = namespace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        return self


class DescribeContainerGroupEventsResponseBodyDataEventsSource(TeaModel):
    def __init__(
        self,
        component: str = None,
        host: str = None,
    ):
        # The component.
        self.component = component
        # The host.
        self.host = host

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component is not None:
            result['Component'] = self.component
        if self.host is not None:
            result['Host'] = self.host
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Component') is not None:
            self.component = m.get('Component')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        return self


class DescribeContainerGroupEventsResponseBodyDataEventsInvolvedObject(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        name: str = None,
        namespace: str = None,
        uid: str = None,
    ):
        # The version of Kubernetes.
        self.api_version = api_version
        # The resource type.
        self.kind = kind
        # The resource name.
        self.name = name
        # The namespace where the resource resides.
        self.namespace = namespace
        # The resource ID.
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['ApiVersion'] = self.api_version
        if self.kind is not None:
            result['Kind'] = self.kind
        if self.name is not None:
            result['Name'] = self.name
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiVersion') is not None:
            self.api_version = m.get('ApiVersion')
        if m.get('Kind') is not None:
            self.kind = m.get('Kind')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class DescribeContainerGroupEventsResponseBodyDataEvents(TeaModel):
    def __init__(
        self,
        count: int = None,
        first_timestamp: str = None,
        last_timestamp: str = None,
        message: str = None,
        metadata: DescribeContainerGroupEventsResponseBodyDataEventsMetadata = None,
        reason: str = None,
        reporting_component: str = None,
        reporting_instance: str = None,
        source: DescribeContainerGroupEventsResponseBodyDataEventsSource = None,
        type: str = None,
        involved_object: DescribeContainerGroupEventsResponseBodyDataEventsInvolvedObject = None,
    ):
        # The number of events.
        self.count = count
        # The first occurrence time of the event.
        self.first_timestamp = first_timestamp
        # The most recent occurrence time of the event.
        self.last_timestamp = last_timestamp
        # The message about the event.
        self.message = message
        # The metadata of the event.
        self.metadata = metadata
        # The cause of the event.
        self.reason = reason
        # The component from which the event is reported.
        self.reporting_component = reporting_component
        # The instance from which the event is reported.
        self.reporting_instance = reporting_instance
        # The source.
        self.source = source
        # The event type. Valid values:
        # 
        # *   Normal
        # *   Warning
        self.type = type
        # The resource object that the event is about.
        self.involved_object = involved_object

    def validate(self):
        if self.metadata:
            self.metadata.validate()
        if self.source:
            self.source.validate()
        if self.involved_object:
            self.involved_object.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.first_timestamp is not None:
            result['FirstTimestamp'] = self.first_timestamp
        if self.last_timestamp is not None:
            result['LastTimestamp'] = self.last_timestamp
        if self.message is not None:
            result['Message'] = self.message
        if self.metadata is not None:
            result['Metadata'] = self.metadata.to_map()
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.reporting_component is not None:
            result['ReportingComponent'] = self.reporting_component
        if self.reporting_instance is not None:
            result['ReportingInstance'] = self.reporting_instance
        if self.source is not None:
            result['Source'] = self.source.to_map()
        if self.type is not None:
            result['Type'] = self.type
        if self.involved_object is not None:
            result['involvedObject'] = self.involved_object.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('FirstTimestamp') is not None:
            self.first_timestamp = m.get('FirstTimestamp')
        if m.get('LastTimestamp') is not None:
            self.last_timestamp = m.get('LastTimestamp')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Metadata') is not None:
            temp_model = DescribeContainerGroupEventsResponseBodyDataEventsMetadata()
            self.metadata = temp_model.from_map(m['Metadata'])
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('ReportingComponent') is not None:
            self.reporting_component = m.get('ReportingComponent')
        if m.get('ReportingInstance') is not None:
            self.reporting_instance = m.get('ReportingInstance')
        if m.get('Source') is not None:
            temp_model = DescribeContainerGroupEventsResponseBodyDataEventsSource()
            self.source = temp_model.from_map(m['Source'])
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('involvedObject') is not None:
            temp_model = DescribeContainerGroupEventsResponseBodyDataEventsInvolvedObject()
            self.involved_object = temp_model.from_map(m['involvedObject'])
        return self


class DescribeContainerGroupEventsResponseBodyData(TeaModel):
    def __init__(
        self,
        annotations: str = None,
        container_group_id: str = None,
        events: List[DescribeContainerGroupEventsResponseBodyDataEvents] = None,
        name: str = None,
        namespace: str = None,
        uuid: str = None,
    ):
        # The annotations of the elastic container instance.
        self.annotations = annotations
        # The ID of the elastic container instance.
        self.container_group_id = container_group_id
        # The events.
        self.events = events
        # The name of the elastic container instance.
        self.name = name
        # The namespace where the elastic container instance resides.
        self.namespace = namespace
        # The UUID of the elastic container instance.
        self.uuid = uuid

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
        if self.annotations is not None:
            result['Annotations'] = self.annotations
        if self.container_group_id is not None:
            result['ContainerGroupId'] = self.container_group_id
        result['Events'] = []
        if self.events is not None:
            for k in self.events:
                result['Events'].append(k.to_map() if k else None)
        if self.name is not None:
            result['Name'] = self.name
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.uuid is not None:
            result['uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Annotations') is not None:
            self.annotations = m.get('Annotations')
        if m.get('ContainerGroupId') is not None:
            self.container_group_id = m.get('ContainerGroupId')
        self.events = []
        if m.get('Events') is not None:
            for k in m.get('Events'):
                temp_model = DescribeContainerGroupEventsResponseBodyDataEvents()
                self.events.append(temp_model.from_map(k))
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('uuid') is not None:
            self.uuid = m.get('uuid')
        return self


class DescribeContainerGroupEventsResponseBody(TeaModel):
    def __init__(
        self,
        data: List[DescribeContainerGroupEventsResponseBodyData] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # Details of the events.
        self.data = data
        # The request ID.
        self.request_id = request_id
        # The total number of entries of returned events.
        self.total_count = total_count

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
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeContainerGroupEventsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeContainerGroupEventsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeContainerGroupEventsResponseBody = None,
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
            temp_model = DescribeContainerGroupEventsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeContainerGroupMetricRequest(TeaModel):
    def __init__(
        self,
        container_group_id: str = None,
        end_time: str = None,
        owner_account: str = None,
        owner_id: int = None,
        period: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        start_time: str = None,
    ):
        # The instance ID.
        # 
        # This parameter is required.
        self.container_group_id = container_group_id
        # The end of the time range to query. The default value is the current time.
        # 
        # Specify the time in RFC 3339 format.
        self.end_time = end_time
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The data aggregation period. Unit: seconds. Valid values: 15, 30, 60, and 600. Default value: 60.
        # 
        # >  If the StartTime and EndTime parameters are not specified, the system returns the monitoring data generated in the last 5 minutes with a data aggregation period of 15s. The Period parameter is ignored.
        self.period = period
        # The region ID of the instance.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The beginning of the time range to query. The beginning of the time range must be a time point in the last 30 days. The default value is 5 minutes before the value of EndTime.
        # 
        # Specify the time in RFC 3339 format. For example, to query the data starting from March 12, 2019, 09:00 UTC+8, you can set the parameter to 2019-03-12T09:00:00.000+08:00 or 2019-03-12T01:00:00.000Z.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.container_group_id is not None:
            result['ContainerGroupId'] = self.container_group_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.period is not None:
            result['Period'] = self.period
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContainerGroupId') is not None:
            self.container_group_id = m.get('ContainerGroupId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeContainerGroupMetricResponseBodyRecordsCPU(TeaModel):
    def __init__(
        self,
        limit: int = None,
        load: int = None,
        usage_core_nano_seconds: int = None,
        usage_nano_cores: int = None,
    ):
        # The upper limit of vCPU usage. The calculation formula for this parameter: The number of vCPUs × 1000.
        self.limit = limit
        # The average load in the last 10 seconds.
        self.load = load
        # The cumulative usage of vCPUs.
        self.usage_core_nano_seconds = usage_core_nano_seconds
        # The vCPU usage in the sampling window. Unit for the sampling window: nanoseconds.
        self.usage_nano_cores = usage_nano_cores

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.load is not None:
            result['Load'] = self.load
        if self.usage_core_nano_seconds is not None:
            result['UsageCoreNanoSeconds'] = self.usage_core_nano_seconds
        if self.usage_nano_cores is not None:
            result['UsageNanoCores'] = self.usage_nano_cores
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('Load') is not None:
            self.load = m.get('Load')
        if m.get('UsageCoreNanoSeconds') is not None:
            self.usage_core_nano_seconds = m.get('UsageCoreNanoSeconds')
        if m.get('UsageNanoCores') is not None:
            self.usage_nano_cores = m.get('UsageNanoCores')
        return self


class DescribeContainerGroupMetricResponseBodyRecordsContainersCPU(TeaModel):
    def __init__(
        self,
        limit: int = None,
        load: int = None,
        usage_core_nano_seconds: int = None,
        usage_nano_cores: int = None,
    ):
        # The upper limit of vCPU usage. The calculation formula for this parameter: The number of vCPUs × 1000.
        self.limit = limit
        # The average load in the last 10 seconds.
        self.load = load
        # The cumulative usage of vCPUs.
        self.usage_core_nano_seconds = usage_core_nano_seconds
        # The vCPU usage in the sampling window. Unit for the sampling window: nanoseconds.
        self.usage_nano_cores = usage_nano_cores

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.load is not None:
            result['Load'] = self.load
        if self.usage_core_nano_seconds is not None:
            result['UsageCoreNanoSeconds'] = self.usage_core_nano_seconds
        if self.usage_nano_cores is not None:
            result['UsageNanoCores'] = self.usage_nano_cores
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('Load') is not None:
            self.load = m.get('Load')
        if m.get('UsageCoreNanoSeconds') is not None:
            self.usage_core_nano_seconds = m.get('UsageCoreNanoSeconds')
        if m.get('UsageNanoCores') is not None:
            self.usage_nano_cores = m.get('UsageNanoCores')
        return self


class DescribeContainerGroupMetricResponseBodyRecordsContainersMemory(TeaModel):
    def __init__(
        self,
        available_bytes: int = None,
        cache: int = None,
        rss: int = None,
        usage_bytes: int = None,
        working_set: int = None,
    ):
        # The size of the available memory. Unit: bytes.
        self.available_bytes = available_bytes
        # The size of the cache. Unit: bytes.
        self.cache = cache
        # The size of the resident memory set, which indicates the size of the physical memory that is actually used. Unit: bytes.
        self.rss = rss
        # The size of the used memory. Unit: bytes.
        self.usage_bytes = usage_bytes
        # The usage of the working set. Unit: bytes.
        self.working_set = working_set

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.available_bytes is not None:
            result['AvailableBytes'] = self.available_bytes
        if self.cache is not None:
            result['Cache'] = self.cache
        if self.rss is not None:
            result['Rss'] = self.rss
        if self.usage_bytes is not None:
            result['UsageBytes'] = self.usage_bytes
        if self.working_set is not None:
            result['WorkingSet'] = self.working_set
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableBytes') is not None:
            self.available_bytes = m.get('AvailableBytes')
        if m.get('Cache') is not None:
            self.cache = m.get('Cache')
        if m.get('Rss') is not None:
            self.rss = m.get('Rss')
        if m.get('UsageBytes') is not None:
            self.usage_bytes = m.get('UsageBytes')
        if m.get('WorkingSet') is not None:
            self.working_set = m.get('WorkingSet')
        return self


class DescribeContainerGroupMetricResponseBodyRecordsContainers(TeaModel):
    def __init__(
        self,
        cpu: DescribeContainerGroupMetricResponseBodyRecordsContainersCPU = None,
        memory: DescribeContainerGroupMetricResponseBodyRecordsContainersMemory = None,
        name: str = None,
    ):
        # The vCPU monitoring data of the container.
        self.cpu = cpu
        # The memory monitoring data of the container.
        self.memory = memory
        # The name of the container.
        self.name = name

    def validate(self):
        if self.cpu:
            self.cpu.validate()
        if self.memory:
            self.memory.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['CPU'] = self.cpu.to_map()
        if self.memory is not None:
            result['Memory'] = self.memory.to_map()
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CPU') is not None:
            temp_model = DescribeContainerGroupMetricResponseBodyRecordsContainersCPU()
            self.cpu = temp_model.from_map(m['CPU'])
        if m.get('Memory') is not None:
            temp_model = DescribeContainerGroupMetricResponseBodyRecordsContainersMemory()
            self.memory = temp_model.from_map(m['Memory'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeContainerGroupMetricResponseBodyRecordsDisk(TeaModel):
    def __init__(
        self,
        device: str = None,
        read_bytes: int = None,
        read_io: int = None,
        write_bytes: int = None,
        write_io: int = None,
    ):
        # The name of the disk.
        self.device = device
        # The amount of data that was read from the disk. Unit: bytes.
        self.read_bytes = read_bytes
        # This parameter is unavailable for public use.
        self.read_io = read_io
        # The amount of data that was written to the disk. Unit: bytes.
        self.write_bytes = write_bytes
        # This parameter is unavailable for public use.
        self.write_io = write_io

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device is not None:
            result['Device'] = self.device
        if self.read_bytes is not None:
            result['ReadBytes'] = self.read_bytes
        if self.read_io is not None:
            result['ReadIO'] = self.read_io
        if self.write_bytes is not None:
            result['WriteBytes'] = self.write_bytes
        if self.write_io is not None:
            result['WriteIO'] = self.write_io
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Device') is not None:
            self.device = m.get('Device')
        if m.get('ReadBytes') is not None:
            self.read_bytes = m.get('ReadBytes')
        if m.get('ReadIO') is not None:
            self.read_io = m.get('ReadIO')
        if m.get('WriteBytes') is not None:
            self.write_bytes = m.get('WriteBytes')
        if m.get('WriteIO') is not None:
            self.write_io = m.get('WriteIO')
        return self


class DescribeContainerGroupMetricResponseBodyRecordsFilesystem(TeaModel):
    def __init__(
        self,
        available: int = None,
        capacity: int = None,
        category: str = None,
        fs_name: str = None,
        usage: int = None,
    ):
        # The size of the available space.
        self.available = available
        # The total file system space.
        self.capacity = capacity
        # The type of the partition. Valid values:
        # 
        # *   System
        # *   Volume
        # *   Other
        self.category = category
        # The name of the partition.
        self.fs_name = fs_name
        # The size of used space.
        self.usage = usage

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.available is not None:
            result['Available'] = self.available
        if self.capacity is not None:
            result['Capacity'] = self.capacity
        if self.category is not None:
            result['Category'] = self.category
        if self.fs_name is not None:
            result['FsName'] = self.fs_name
        if self.usage is not None:
            result['Usage'] = self.usage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Available') is not None:
            self.available = m.get('Available')
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('FsName') is not None:
            self.fs_name = m.get('FsName')
        if m.get('Usage') is not None:
            self.usage = m.get('Usage')
        return self


class DescribeContainerGroupMetricResponseBodyRecordsMemory(TeaModel):
    def __init__(
        self,
        available_bytes: int = None,
        cache: int = None,
        rss: int = None,
        usage_bytes: int = None,
        working_set: int = None,
    ):
        # The size of the available memory. Unit: bytes.
        self.available_bytes = available_bytes
        # The size of the cache. Unit: bytes.
        self.cache = cache
        # The size of the resident memory set, which indicates the size of the physical memory that is actually used. Unit: bytes.
        self.rss = rss
        # The size of the used memory. Unit: bytes.
        self.usage_bytes = usage_bytes
        # The usage of the working set. Unit: bytes.
        self.working_set = working_set

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.available_bytes is not None:
            result['AvailableBytes'] = self.available_bytes
        if self.cache is not None:
            result['Cache'] = self.cache
        if self.rss is not None:
            result['Rss'] = self.rss
        if self.usage_bytes is not None:
            result['UsageBytes'] = self.usage_bytes
        if self.working_set is not None:
            result['WorkingSet'] = self.working_set
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableBytes') is not None:
            self.available_bytes = m.get('AvailableBytes')
        if m.get('Cache') is not None:
            self.cache = m.get('Cache')
        if m.get('Rss') is not None:
            self.rss = m.get('Rss')
        if m.get('UsageBytes') is not None:
            self.usage_bytes = m.get('UsageBytes')
        if m.get('WorkingSet') is not None:
            self.working_set = m.get('WorkingSet')
        return self


class DescribeContainerGroupMetricResponseBodyRecordsNetworkInterfaces(TeaModel):
    def __init__(
        self,
        name: str = None,
        rx_bytes: int = None,
        rx_drops: int = None,
        rx_errors: int = None,
        rx_packets: int = None,
        tx_bytes: int = None,
        tx_drops: int = None,
        tx_errors: int = None,
        tx_packets: int = None,
    ):
        # The name of the NIC.
        self.name = name
        # The number of bytes received by the NIC.
        self.rx_bytes = rx_bytes
        # The number of received packets dropped on the NIC.
        self.rx_drops = rx_drops
        # The number of received packet errors on the NIC.
        self.rx_errors = rx_errors
        # The number of packets received by the NIC.
        self.rx_packets = rx_packets
        # The number of bytes transmitted by the NIC.
        self.tx_bytes = tx_bytes
        # The number of transmitted packets dropped on the NIC.
        self.tx_drops = tx_drops
        # The number of transmitted packet errors on the NIC.
        self.tx_errors = tx_errors
        # The number of packets transmitted by the NIC.
        self.tx_packets = tx_packets

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.rx_bytes is not None:
            result['RxBytes'] = self.rx_bytes
        if self.rx_drops is not None:
            result['RxDrops'] = self.rx_drops
        if self.rx_errors is not None:
            result['RxErrors'] = self.rx_errors
        if self.rx_packets is not None:
            result['RxPackets'] = self.rx_packets
        if self.tx_bytes is not None:
            result['TxBytes'] = self.tx_bytes
        if self.tx_drops is not None:
            result['TxDrops'] = self.tx_drops
        if self.tx_errors is not None:
            result['TxErrors'] = self.tx_errors
        if self.tx_packets is not None:
            result['TxPackets'] = self.tx_packets
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RxBytes') is not None:
            self.rx_bytes = m.get('RxBytes')
        if m.get('RxDrops') is not None:
            self.rx_drops = m.get('RxDrops')
        if m.get('RxErrors') is not None:
            self.rx_errors = m.get('RxErrors')
        if m.get('RxPackets') is not None:
            self.rx_packets = m.get('RxPackets')
        if m.get('TxBytes') is not None:
            self.tx_bytes = m.get('TxBytes')
        if m.get('TxDrops') is not None:
            self.tx_drops = m.get('TxDrops')
        if m.get('TxErrors') is not None:
            self.tx_errors = m.get('TxErrors')
        if m.get('TxPackets') is not None:
            self.tx_packets = m.get('TxPackets')
        return self


class DescribeContainerGroupMetricResponseBodyRecordsNetwork(TeaModel):
    def __init__(
        self,
        interfaces: List[DescribeContainerGroupMetricResponseBodyRecordsNetworkInterfaces] = None,
    ):
        # The monitoring data of network interface controllers (NICs).
        self.interfaces = interfaces

    def validate(self):
        if self.interfaces:
            for k in self.interfaces:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Interfaces'] = []
        if self.interfaces is not None:
            for k in self.interfaces:
                result['Interfaces'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.interfaces = []
        if m.get('Interfaces') is not None:
            for k in m.get('Interfaces'):
                temp_model = DescribeContainerGroupMetricResponseBodyRecordsNetworkInterfaces()
                self.interfaces.append(temp_model.from_map(k))
        return self


class DescribeContainerGroupMetricResponseBodyRecords(TeaModel):
    def __init__(
        self,
        cpu: DescribeContainerGroupMetricResponseBodyRecordsCPU = None,
        containers: List[DescribeContainerGroupMetricResponseBodyRecordsContainers] = None,
        disk: List[DescribeContainerGroupMetricResponseBodyRecordsDisk] = None,
        filesystem: List[DescribeContainerGroupMetricResponseBodyRecordsFilesystem] = None,
        memory: DescribeContainerGroupMetricResponseBodyRecordsMemory = None,
        network: DescribeContainerGroupMetricResponseBodyRecordsNetwork = None,
        timestamp: str = None,
    ):
        # The monitoring data of vCPUs.
        self.cpu = cpu
        # The monitoring data of containers.
        self.containers = containers
        # The monitoring data of disks.
        self.disk = disk
        # The monitoring data of file system partitions.
        self.filesystem = filesystem
        # The monitoring data of the memory.
        self.memory = memory
        # The monitoring data of the network.
        self.network = network
        # The time when the monitoring data entry was collected. The time follows the RFC 3339 format.
        self.timestamp = timestamp

    def validate(self):
        if self.cpu:
            self.cpu.validate()
        if self.containers:
            for k in self.containers:
                if k:
                    k.validate()
        if self.disk:
            for k in self.disk:
                if k:
                    k.validate()
        if self.filesystem:
            for k in self.filesystem:
                if k:
                    k.validate()
        if self.memory:
            self.memory.validate()
        if self.network:
            self.network.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['CPU'] = self.cpu.to_map()
        result['Containers'] = []
        if self.containers is not None:
            for k in self.containers:
                result['Containers'].append(k.to_map() if k else None)
        result['Disk'] = []
        if self.disk is not None:
            for k in self.disk:
                result['Disk'].append(k.to_map() if k else None)
        result['Filesystem'] = []
        if self.filesystem is not None:
            for k in self.filesystem:
                result['Filesystem'].append(k.to_map() if k else None)
        if self.memory is not None:
            result['Memory'] = self.memory.to_map()
        if self.network is not None:
            result['Network'] = self.network.to_map()
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CPU') is not None:
            temp_model = DescribeContainerGroupMetricResponseBodyRecordsCPU()
            self.cpu = temp_model.from_map(m['CPU'])
        self.containers = []
        if m.get('Containers') is not None:
            for k in m.get('Containers'):
                temp_model = DescribeContainerGroupMetricResponseBodyRecordsContainers()
                self.containers.append(temp_model.from_map(k))
        self.disk = []
        if m.get('Disk') is not None:
            for k in m.get('Disk'):
                temp_model = DescribeContainerGroupMetricResponseBodyRecordsDisk()
                self.disk.append(temp_model.from_map(k))
        self.filesystem = []
        if m.get('Filesystem') is not None:
            for k in m.get('Filesystem'):
                temp_model = DescribeContainerGroupMetricResponseBodyRecordsFilesystem()
                self.filesystem.append(temp_model.from_map(k))
        if m.get('Memory') is not None:
            temp_model = DescribeContainerGroupMetricResponseBodyRecordsMemory()
            self.memory = temp_model.from_map(m['Memory'])
        if m.get('Network') is not None:
            temp_model = DescribeContainerGroupMetricResponseBodyRecordsNetwork()
            self.network = temp_model.from_map(m['Network'])
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class DescribeContainerGroupMetricResponseBody(TeaModel):
    def __init__(
        self,
        container_group_id: str = None,
        records: List[DescribeContainerGroupMetricResponseBodyRecords] = None,
        request_id: str = None,
    ):
        # The instance ID.
        self.container_group_id = container_group_id
        # The monitoring data of the elastic container instance.
        self.records = records
        # The request ID.
        self.request_id = request_id

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
        if self.container_group_id is not None:
            result['ContainerGroupId'] = self.container_group_id
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContainerGroupId') is not None:
            self.container_group_id = m.get('ContainerGroupId')
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = DescribeContainerGroupMetricResponseBodyRecords()
                self.records.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeContainerGroupMetricResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeContainerGroupMetricResponseBody = None,
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
            temp_model = DescribeContainerGroupMetricResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeContainerGroupPriceRequest(TeaModel):
    def __init__(
        self,
        compute_category: str = None,
        cpu: float = None,
        ephemeral_storage: int = None,
        instance_type: str = None,
        memory: float = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        spot_duration: int = None,
        spot_price_limit: float = None,
        spot_strategy: str = None,
        zone_id: str = None,
    ):
        # The computing power type. A value of economy specifies economic instances.
        self.compute_category = compute_category
        # The number of vCPUs. For information about the vCPU and memory specifications that are supported by Elastic Container Instance, see [vCPU and memory specifications](https://help.aliyun.com/document_detail/114662.html).
        self.cpu = cpu
        # The storage size of the temporary storage space. Unit: GiB.
        self.ephemeral_storage = ephemeral_storage
        # The instance type of the Elastic Compute Service (ECS) instance that is used to create the elastic container instance. For information about the ECS instance types that are supported by Elastic Container Instance, see [ECS instance types that are supported by Elastic Container Instance](https://help.aliyun.com/document_detail/114664.html).
        # 
        # > If you specify this parameter, the specified specifications of vCPUs and memory are ignored. Only the price of the ECS instance type is returned.
        self.instance_type = instance_type
        # The size of the memory. Unit: GiB. For information about the vCPU and memory specifications that are supported by Elastic Container Instance, see [vCPU and memory specifications](https://help.aliyun.com/document_detail/114662.html).
        self.memory = memory
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the instance. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/146965.html) operation to query the most recent region and zone list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The protection period of the preemptible instance. Unit: hours. Default value: 1. The value of 0 indicates no protection period.
        self.spot_duration = spot_duration
        # The maximum hourly price of the preemptible elastic container instance. The value can contain up to three decimal places. If you set SpotStrategy to SpotWithPriceLimit, you must specify SpotPriceLimit.
        self.spot_price_limit = spot_price_limit
        # The bidding policy for the elastic container instance. Valid values:
        # 
        # *   NoSpot: The instance is a regular pay-as-you-go instance.
        # *   SpotWithPriceLimit: The instance is a preemptible instance with a user-defined maximum hourly price.
        # *   SpotAsPriceGo: The instance is a preemptible instance for which the market price at the time of purchase is automatically used as the bid price.
        # 
        # Default value: NoSpot.
        self.spot_strategy = spot_strategy
        # The zone ID of the instance. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/146965.html) operation to query the most recent region and zone list.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compute_category is not None:
            result['ComputeCategory'] = self.compute_category
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.ephemeral_storage is not None:
            result['EphemeralStorage'] = self.ephemeral_storage
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.memory is not None:
            result['Memory'] = self.memory
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
        if self.spot_duration is not None:
            result['SpotDuration'] = self.spot_duration
        if self.spot_price_limit is not None:
            result['SpotPriceLimit'] = self.spot_price_limit
        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComputeCategory') is not None:
            self.compute_category = m.get('ComputeCategory')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('EphemeralStorage') is not None:
            self.ephemeral_storage = m.get('EphemeralStorage')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
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
        if m.get('SpotDuration') is not None:
            self.spot_duration = m.get('SpotDuration')
        if m.get('SpotPriceLimit') is not None:
            self.spot_price_limit = m.get('SpotPriceLimit')
        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeContainerGroupPriceResponseBodyPriceInfoPriceDetailInfosDetailInfoRulesRule(TeaModel):
    def __init__(
        self,
        description: str = None,
        rule_id: int = None,
    ):
        # The description of the rule.
        self.description = description
        # The rule ID.
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class DescribeContainerGroupPriceResponseBodyPriceInfoPriceDetailInfosDetailInfoRules(TeaModel):
    def __init__(
        self,
        rule: List[DescribeContainerGroupPriceResponseBodyPriceInfoPriceDetailInfosDetailInfoRulesRule] = None,
    ):
        self.rule = rule

    def validate(self):
        if self.rule:
            for k in self.rule:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Rule'] = []
        if self.rule is not None:
            for k in self.rule:
                result['Rule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.rule = []
        if m.get('Rule') is not None:
            for k in m.get('Rule'):
                temp_model = DescribeContainerGroupPriceResponseBodyPriceInfoPriceDetailInfosDetailInfoRulesRule()
                self.rule.append(temp_model.from_map(k))
        return self


class DescribeContainerGroupPriceResponseBodyPriceInfoPriceDetailInfosDetailInfo(TeaModel):
    def __init__(
        self,
        discount_price: float = None,
        original_price: float = None,
        resource: str = None,
        rules: DescribeContainerGroupPriceResponseBodyPriceInfoPriceDetailInfosDetailInfoRules = None,
        trade_price: float = None,
    ):
        # The discount.
        self.discount_price = discount_price
        # The original price.
        self.original_price = original_price
        # The name of the resource.
        self.resource = resource
        # Details about the pricing rules.
        self.rules = rules
        # The transaction price.
        self.trade_price = trade_price

    def validate(self):
        if self.rules:
            self.rules.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        if self.resource is not None:
            result['Resource'] = self.resource
        if self.rules is not None:
            result['Rules'] = self.rules.to_map()
        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        if m.get('Rules') is not None:
            temp_model = DescribeContainerGroupPriceResponseBodyPriceInfoPriceDetailInfosDetailInfoRules()
            self.rules = temp_model.from_map(m['Rules'])
        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')
        return self


class DescribeContainerGroupPriceResponseBodyPriceInfoPriceDetailInfos(TeaModel):
    def __init__(
        self,
        detail_info: List[DescribeContainerGroupPriceResponseBodyPriceInfoPriceDetailInfosDetailInfo] = None,
    ):
        self.detail_info = detail_info

    def validate(self):
        if self.detail_info:
            for k in self.detail_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DetailInfo'] = []
        if self.detail_info is not None:
            for k in self.detail_info:
                result['DetailInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.detail_info = []
        if m.get('DetailInfo') is not None:
            for k in m.get('DetailInfo'):
                temp_model = DescribeContainerGroupPriceResponseBodyPriceInfoPriceDetailInfosDetailInfo()
                self.detail_info.append(temp_model.from_map(k))
        return self


class DescribeContainerGroupPriceResponseBodyPriceInfoPrice(TeaModel):
    def __init__(
        self,
        currency: str = None,
        detail_infos: DescribeContainerGroupPriceResponseBodyPriceInfoPriceDetailInfos = None,
        discount_price: float = None,
        original_price: float = None,
        trade_price: float = None,
    ):
        # The currency unit. Valid values:
        # 
        # *   CNY: This value only applies to the China site (aliyun.com).
        # *   USD: This value only applies to the International site (alibabacloud.com).
        self.currency = currency
        # The information about the price.
        self.detail_infos = detail_infos
        # The discount.
        self.discount_price = discount_price
        # The original price.
        self.original_price = original_price
        # The transaction price, which is equal to the original price minus the discount.
        self.trade_price = trade_price

    def validate(self):
        if self.detail_infos:
            self.detail_infos.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.detail_infos is not None:
            result['DetailInfos'] = self.detail_infos.to_map()
        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('DetailInfos') is not None:
            temp_model = DescribeContainerGroupPriceResponseBodyPriceInfoPriceDetailInfos()
            self.detail_infos = temp_model.from_map(m['DetailInfos'])
        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')
        return self


class DescribeContainerGroupPriceResponseBodyPriceInfoRulesRule(TeaModel):
    def __init__(
        self,
        description: str = None,
        rule_id: int = None,
    ):
        # The description of the promotion rule.
        self.description = description
        # The ID of the promotion rule.
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class DescribeContainerGroupPriceResponseBodyPriceInfoRules(TeaModel):
    def __init__(
        self,
        rule: List[DescribeContainerGroupPriceResponseBodyPriceInfoRulesRule] = None,
    ):
        self.rule = rule

    def validate(self):
        if self.rule:
            for k in self.rule:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Rule'] = []
        if self.rule is not None:
            for k in self.rule:
                result['Rule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.rule = []
        if m.get('Rule') is not None:
            for k in m.get('Rule'):
                temp_model = DescribeContainerGroupPriceResponseBodyPriceInfoRulesRule()
                self.rule.append(temp_model.from_map(k))
        return self


class DescribeContainerGroupPriceResponseBodyPriceInfoSpotPricesSpotPrice(TeaModel):
    def __init__(
        self,
        instance_type: str = None,
        origin_price: float = None,
        spot_price: float = None,
        zone_id: str = None,
    ):
        # The ECS instance type.
        self.instance_type = instance_type
        # The original price.
        self.origin_price = origin_price
        # The prices of preemptible elastic container instances.
        self.spot_price = spot_price
        # The zone ID of the instance.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.origin_price is not None:
            result['OriginPrice'] = self.origin_price
        if self.spot_price is not None:
            result['SpotPrice'] = self.spot_price
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('OriginPrice') is not None:
            self.origin_price = m.get('OriginPrice')
        if m.get('SpotPrice') is not None:
            self.spot_price = m.get('SpotPrice')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeContainerGroupPriceResponseBodyPriceInfoSpotPrices(TeaModel):
    def __init__(
        self,
        spot_price: List[DescribeContainerGroupPriceResponseBodyPriceInfoSpotPricesSpotPrice] = None,
    ):
        self.spot_price = spot_price

    def validate(self):
        if self.spot_price:
            for k in self.spot_price:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SpotPrice'] = []
        if self.spot_price is not None:
            for k in self.spot_price:
                result['SpotPrice'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.spot_price = []
        if m.get('SpotPrice') is not None:
            for k in m.get('SpotPrice'):
                temp_model = DescribeContainerGroupPriceResponseBodyPriceInfoSpotPricesSpotPrice()
                self.spot_price.append(temp_model.from_map(k))
        return self


class DescribeContainerGroupPriceResponseBodyPriceInfo(TeaModel):
    def __init__(
        self,
        price: DescribeContainerGroupPriceResponseBodyPriceInfoPrice = None,
        rules: DescribeContainerGroupPriceResponseBodyPriceInfoRules = None,
        spot_prices: DescribeContainerGroupPriceResponseBodyPriceInfoSpotPrices = None,
    ):
        # The price.
        self.price = price
        # Details about the promotion rules.
        self.rules = rules
        # The information about the prices of preemptible elastic container instances.
        self.spot_prices = spot_prices

    def validate(self):
        if self.price:
            self.price.validate()
        if self.rules:
            self.rules.validate()
        if self.spot_prices:
            self.spot_prices.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.price is not None:
            result['Price'] = self.price.to_map()
        if self.rules is not None:
            result['Rules'] = self.rules.to_map()
        if self.spot_prices is not None:
            result['SpotPrices'] = self.spot_prices.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Price') is not None:
            temp_model = DescribeContainerGroupPriceResponseBodyPriceInfoPrice()
            self.price = temp_model.from_map(m['Price'])
        if m.get('Rules') is not None:
            temp_model = DescribeContainerGroupPriceResponseBodyPriceInfoRules()
            self.rules = temp_model.from_map(m['Rules'])
        if m.get('SpotPrices') is not None:
            temp_model = DescribeContainerGroupPriceResponseBodyPriceInfoSpotPrices()
            self.spot_prices = temp_model.from_map(m['SpotPrices'])
        return self


class DescribeContainerGroupPriceResponseBody(TeaModel):
    def __init__(
        self,
        price_info: DescribeContainerGroupPriceResponseBodyPriceInfo = None,
        request_id: str = None,
    ):
        # The information about the prices and discount rules.
        self.price_info = price_info
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.price_info:
            self.price_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.price_info is not None:
            result['PriceInfo'] = self.price_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PriceInfo') is not None:
            temp_model = DescribeContainerGroupPriceResponseBodyPriceInfo()
            self.price_info = temp_model.from_map(m['PriceInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeContainerGroupPriceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeContainerGroupPriceResponseBody = None,
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
            temp_model = DescribeContainerGroupPriceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeContainerGroupStatusRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag.
        self.key = key
        # The value of the tag.
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


class DescribeContainerGroupStatusRequest(TeaModel):
    def __init__(
        self,
        container_group_ids: str = None,
        limit: int = None,
        next_token: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        since_second: int = None,
        tag: List[DescribeContainerGroupStatusRequestTag] = None,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        # The IDs of the instances. You can specify up to 20 IDs. Each ID must be a string in the JSON format.
        self.container_group_ids = container_group_ids
        # Specifies the maximum number of elastic container instances to be returned for this request. Default value: 200.
        # 
        # > The number of returned resources can be less than or equal to the value of this parameter.
        self.limit = limit
        # The pagination token that is used in the next request to retrieve a new page of results. If NextToken is empty, no next page exists.\\
        # You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token
        # The region ID of the instances.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group to which the instances belong.
        self.resource_group_id = resource_group_id
        # A relative time in seconds before the current time from which to show elastic container instances whose status changes. This parameter is used to poll status of elastic container instances.
        self.since_second = since_second
        # The tag that is bound to the instances.
        self.tag = tag
        # The vSwitch ID.
        self.v_switch_id = v_switch_id
        # The zone ID of the instances.
        self.zone_id = zone_id

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
        if self.container_group_ids is not None:
            result['ContainerGroupIds'] = self.container_group_ids
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.since_second is not None:
            result['SinceSecond'] = self.since_second
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContainerGroupIds') is not None:
            self.container_group_ids = m.get('ContainerGroupIds')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SinceSecond') is not None:
            self.since_second = m.get('SinceSecond')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeContainerGroupStatusRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeContainerGroupStatusResponseBodyDataPodStatusConditions(TeaModel):
    def __init__(
        self,
        message: str = None,
        reason: str = None,
        last_transition_time: str = None,
        status: str = None,
        type: str = None,
    ):
        # The message about the event.
        self.message = message
        # The reason for the transition into the current status of the event.
        self.reason = reason
        # The time when the status last changed.
        self.last_transition_time = last_transition_time
        # The status of the condition.
        self.status = status
        # The type of the condition. Valid values:
        # 
        # *   PodReadyToStartContainers
        # *   Initialized
        # *   Ready
        # *   ContainersReady
        # *   PodScheduled
        # *   ContainerHasSufficientDisk
        # *   ContainerInstanceCreated
        # *   Unschedulable
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.last_transition_time is not None:
            result['lastTransitionTime'] = self.last_transition_time
        if self.status is not None:
            result['status'] = self.status
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('lastTransitionTime') is not None:
            self.last_transition_time = m.get('lastTransitionTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class DescribeContainerGroupStatusResponseBodyDataPodStatusContainerStatusesLastStateRunning(TeaModel):
    def __init__(
        self,
        started_atstarted_at: str = None,
    ):
        # The time when the container started to run.
        self.started_atstarted_at = started_atstarted_at

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.started_atstarted_at is not None:
            result['StartedAtstartedAt'] = self.started_atstarted_at
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartedAtstartedAt') is not None:
            self.started_atstarted_at = m.get('StartedAtstartedAt')
        return self


class DescribeContainerGroupStatusResponseBodyDataPodStatusContainerStatusesLastStateTerminated(TeaModel):
    def __init__(
        self,
        container_id: str = None,
        exit_code: int = None,
        finished_at: str = None,
        message: str = None,
        reason: str = None,
        signal: int = None,
        started_at: str = None,
    ):
        # The container ID.
        self.container_id = container_id
        # The exit code.
        self.exit_code = exit_code
        # The time when the container ends running.
        self.finished_at = finished_at
        # The message about the event.
        self.message = message
        # The reason for the transition into the current status of the event.
        self.reason = reason
        # The signal code.
        self.signal = signal
        # The time when the container started to run.
        self.started_at = started_at

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.container_id is not None:
            result['ContainerID'] = self.container_id
        if self.exit_code is not None:
            result['ExitCode'] = self.exit_code
        if self.finished_at is not None:
            result['FinishedAt'] = self.finished_at
        if self.message is not None:
            result['Message'] = self.message
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.signal is not None:
            result['Signal'] = self.signal
        if self.started_at is not None:
            result['StartedAt'] = self.started_at
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContainerID') is not None:
            self.container_id = m.get('ContainerID')
        if m.get('ExitCode') is not None:
            self.exit_code = m.get('ExitCode')
        if m.get('FinishedAt') is not None:
            self.finished_at = m.get('FinishedAt')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('Signal') is not None:
            self.signal = m.get('Signal')
        if m.get('StartedAt') is not None:
            self.started_at = m.get('StartedAt')
        return self


class DescribeContainerGroupStatusResponseBodyDataPodStatusContainerStatusesLastStateWaiting(TeaModel):
    def __init__(
        self,
        message: str = None,
        reason: str = None,
    ):
        # The message about the event.
        self.message = message
        # The reason for the transition into the current status of the event.
        self.reason = reason

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.reason is not None:
            result['Reason'] = self.reason
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        return self


class DescribeContainerGroupStatusResponseBodyDataPodStatusContainerStatusesLastState(TeaModel):
    def __init__(
        self,
        running: DescribeContainerGroupStatusResponseBodyDataPodStatusContainerStatusesLastStateRunning = None,
        terminated: DescribeContainerGroupStatusResponseBodyDataPodStatusContainerStatusesLastStateTerminated = None,
        waiting: DescribeContainerGroupStatusResponseBodyDataPodStatusContainerStatusesLastStateWaiting = None,
    ):
        # The container is created and running.
        self.running = running
        # The container is terminated and exits after a successful or failed running.
        self.terminated = terminated
        # The container is waiting for being created.
        self.waiting = waiting

    def validate(self):
        if self.running:
            self.running.validate()
        if self.terminated:
            self.terminated.validate()
        if self.waiting:
            self.waiting.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.running is not None:
            result['Running'] = self.running.to_map()
        if self.terminated is not None:
            result['Terminated'] = self.terminated.to_map()
        if self.waiting is not None:
            result['Waiting'] = self.waiting.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Running') is not None:
            temp_model = DescribeContainerGroupStatusResponseBodyDataPodStatusContainerStatusesLastStateRunning()
            self.running = temp_model.from_map(m['Running'])
        if m.get('Terminated') is not None:
            temp_model = DescribeContainerGroupStatusResponseBodyDataPodStatusContainerStatusesLastStateTerminated()
            self.terminated = temp_model.from_map(m['Terminated'])
        if m.get('Waiting') is not None:
            temp_model = DescribeContainerGroupStatusResponseBodyDataPodStatusContainerStatusesLastStateWaiting()
            self.waiting = temp_model.from_map(m['Waiting'])
        return self


class DescribeContainerGroupStatusResponseBodyDataPodStatusContainerStatusesStateRunning(TeaModel):
    def __init__(
        self,
        started_atstarted_at: str = None,
    ):
        # The time when the container started to run.
        self.started_atstarted_at = started_atstarted_at

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.started_atstarted_at is not None:
            result['StartedAtstartedAt'] = self.started_atstarted_at
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartedAtstartedAt') is not None:
            self.started_atstarted_at = m.get('StartedAtstartedAt')
        return self


class DescribeContainerGroupStatusResponseBodyDataPodStatusContainerStatusesStateTerminated(TeaModel):
    def __init__(
        self,
        container_id: str = None,
        exit_code: int = None,
        finished_at: str = None,
        message: str = None,
        reason: str = None,
        signal: int = None,
        started_at: str = None,
    ):
        # The container ID.
        self.container_id = container_id
        # The exit code.
        self.exit_code = exit_code
        # The time when the container ends running.
        self.finished_at = finished_at
        # The message about the event.
        self.message = message
        # The reason for the transition into the current status of the event.
        self.reason = reason
        # The signal code.
        self.signal = signal
        # The time when the container started to run.
        self.started_at = started_at

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.container_id is not None:
            result['ContainerID'] = self.container_id
        if self.exit_code is not None:
            result['ExitCode'] = self.exit_code
        if self.finished_at is not None:
            result['FinishedAt'] = self.finished_at
        if self.message is not None:
            result['Message'] = self.message
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.signal is not None:
            result['Signal'] = self.signal
        if self.started_at is not None:
            result['StartedAt'] = self.started_at
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContainerID') is not None:
            self.container_id = m.get('ContainerID')
        if m.get('ExitCode') is not None:
            self.exit_code = m.get('ExitCode')
        if m.get('FinishedAt') is not None:
            self.finished_at = m.get('FinishedAt')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('Signal') is not None:
            self.signal = m.get('Signal')
        if m.get('StartedAt') is not None:
            self.started_at = m.get('StartedAt')
        return self


class DescribeContainerGroupStatusResponseBodyDataPodStatusContainerStatusesStateWaiting(TeaModel):
    def __init__(
        self,
        message: str = None,
        reason: str = None,
    ):
        # The message about the event.
        self.message = message
        # The reason for the transition into the current status of the event.
        self.reason = reason

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.reason is not None:
            result['Reason'] = self.reason
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        return self


class DescribeContainerGroupStatusResponseBodyDataPodStatusContainerStatusesState(TeaModel):
    def __init__(
        self,
        running: DescribeContainerGroupStatusResponseBodyDataPodStatusContainerStatusesStateRunning = None,
        terminated: DescribeContainerGroupStatusResponseBodyDataPodStatusContainerStatusesStateTerminated = None,
        waiting: DescribeContainerGroupStatusResponseBodyDataPodStatusContainerStatusesStateWaiting = None,
    ):
        # The container is created and running.
        self.running = running
        # The container is terminated and exits after a successful or failed running.
        self.terminated = terminated
        # The container is waiting for being created.
        self.waiting = waiting

    def validate(self):
        if self.running:
            self.running.validate()
        if self.terminated:
            self.terminated.validate()
        if self.waiting:
            self.waiting.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.running is not None:
            result['Running'] = self.running.to_map()
        if self.terminated is not None:
            result['Terminated'] = self.terminated.to_map()
        if self.waiting is not None:
            result['Waiting'] = self.waiting.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Running') is not None:
            temp_model = DescribeContainerGroupStatusResponseBodyDataPodStatusContainerStatusesStateRunning()
            self.running = temp_model.from_map(m['Running'])
        if m.get('Terminated') is not None:
            temp_model = DescribeContainerGroupStatusResponseBodyDataPodStatusContainerStatusesStateTerminated()
            self.terminated = temp_model.from_map(m['Terminated'])
        if m.get('Waiting') is not None:
            temp_model = DescribeContainerGroupStatusResponseBodyDataPodStatusContainerStatusesStateWaiting()
            self.waiting = temp_model.from_map(m['Waiting'])
        return self


class DescribeContainerGroupStatusResponseBodyDataPodStatusContainerStatuses(TeaModel):
    def __init__(
        self,
        image: str = None,
        image_id: str = None,
        last_state: DescribeContainerGroupStatusResponseBodyDataPodStatusContainerStatusesLastState = None,
        name: str = None,
        ready: bool = None,
        restart_count: int = None,
        started: bool = None,
        state: DescribeContainerGroupStatusResponseBodyDataPodStatusContainerStatusesState = None,
    ):
        # The image of the container.
        self.image = image
        # The image ID.
        self.image_id = image_id
        # The last status of the container.
        self.last_state = last_state
        # The name of the container.
        self.name = name
        # Indicates whether the container is ready.
        self.ready = ready
        # The number of times that the container restarted.
        self.restart_count = restart_count
        # Indicates whether the container is started.
        self.started = started
        # The status of the container. Valid values:
        # 
        # *   Waiting
        # *   Running
        # *   Terminated
        self.state = state

    def validate(self):
        if self.last_state:
            self.last_state.validate()
        if self.state:
            self.state.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image is not None:
            result['Image'] = self.image
        if self.image_id is not None:
            result['ImageID'] = self.image_id
        if self.last_state is not None:
            result['LastState'] = self.last_state.to_map()
        if self.name is not None:
            result['Name'] = self.name
        if self.ready is not None:
            result['Ready'] = self.ready
        if self.restart_count is not None:
            result['RestartCount'] = self.restart_count
        if self.started is not None:
            result['Started'] = self.started
        if self.state is not None:
            result['State'] = self.state.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('ImageID') is not None:
            self.image_id = m.get('ImageID')
        if m.get('LastState') is not None:
            temp_model = DescribeContainerGroupStatusResponseBodyDataPodStatusContainerStatusesLastState()
            self.last_state = temp_model.from_map(m['LastState'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Ready') is not None:
            self.ready = m.get('Ready')
        if m.get('RestartCount') is not None:
            self.restart_count = m.get('RestartCount')
        if m.get('Started') is not None:
            self.started = m.get('Started')
        if m.get('State') is not None:
            temp_model = DescribeContainerGroupStatusResponseBodyDataPodStatusContainerStatusesState()
            self.state = temp_model.from_map(m['State'])
        return self


class DescribeContainerGroupStatusResponseBodyDataPodStatusPodIps(TeaModel):
    def __init__(
        self,
        ip: str = None,
    ):
        # The IP address of the container group.
        self.ip = ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['Ip'] = self.ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        return self


class DescribeContainerGroupStatusResponseBodyDataPodStatus(TeaModel):
    def __init__(
        self,
        conditions: List[DescribeContainerGroupStatusResponseBodyDataPodStatusConditions] = None,
        container_statuses: List[DescribeContainerGroupStatusResponseBodyDataPodStatusContainerStatuses] = None,
        host_ip: str = None,
        phase: str = None,
        pod_ip: str = None,
        pod_ips: List[DescribeContainerGroupStatusResponseBodyDataPodStatusPodIps] = None,
        qos_class: str = None,
        start_time: str = None,
    ):
        # The conditions of the container group.
        self.conditions = conditions
        # The statuses about the containers.
        self.container_statuses = container_statuses
        # The IP address of the host.
        self.host_ip = host_ip
        # The lifecycle phase of the container group.
        self.phase = phase
        # The IP address of the container group.
        self.pod_ip = pod_ip
        # The IP addresses of the container groups.
        self.pod_ips = pod_ips
        # The quality of service (QoS) of the container group.
        self.qos_class = qos_class
        # The time when the container started to run.
        self.start_time = start_time

    def validate(self):
        if self.conditions:
            for k in self.conditions:
                if k:
                    k.validate()
        if self.container_statuses:
            for k in self.container_statuses:
                if k:
                    k.validate()
        if self.pod_ips:
            for k in self.pod_ips:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Conditions'] = []
        if self.conditions is not None:
            for k in self.conditions:
                result['Conditions'].append(k.to_map() if k else None)
        result['ContainerStatuses'] = []
        if self.container_statuses is not None:
            for k in self.container_statuses:
                result['ContainerStatuses'].append(k.to_map() if k else None)
        if self.host_ip is not None:
            result['HostIp'] = self.host_ip
        if self.phase is not None:
            result['Phase'] = self.phase
        if self.pod_ip is not None:
            result['PodIp'] = self.pod_ip
        result['PodIps'] = []
        if self.pod_ips is not None:
            for k in self.pod_ips:
                result['PodIps'].append(k.to_map() if k else None)
        if self.qos_class is not None:
            result['QosClass'] = self.qos_class
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.conditions = []
        if m.get('Conditions') is not None:
            for k in m.get('Conditions'):
                temp_model = DescribeContainerGroupStatusResponseBodyDataPodStatusConditions()
                self.conditions.append(temp_model.from_map(k))
        self.container_statuses = []
        if m.get('ContainerStatuses') is not None:
            for k in m.get('ContainerStatuses'):
                temp_model = DescribeContainerGroupStatusResponseBodyDataPodStatusContainerStatuses()
                self.container_statuses.append(temp_model.from_map(k))
        if m.get('HostIp') is not None:
            self.host_ip = m.get('HostIp')
        if m.get('Phase') is not None:
            self.phase = m.get('Phase')
        if m.get('PodIp') is not None:
            self.pod_ip = m.get('PodIp')
        self.pod_ips = []
        if m.get('PodIps') is not None:
            for k in m.get('PodIps'):
                temp_model = DescribeContainerGroupStatusResponseBodyDataPodStatusPodIps()
                self.pod_ips.append(temp_model.from_map(k))
        if m.get('QosClass') is not None:
            self.qos_class = m.get('QosClass')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeContainerGroupStatusResponseBodyData(TeaModel):
    def __init__(
        self,
        annotations: str = None,
        container_group_id: str = None,
        name: str = None,
        namespace: str = None,
        pod_status: DescribeContainerGroupStatusResponseBodyDataPodStatus = None,
        status: str = None,
        uuid: str = None,
    ):
        # Annotations that are added to the container groups.
        self.annotations = annotations
        # The ID of the container group.
        self.container_group_id = container_group_id
        # The name of the container group.
        self.name = name
        # The namespace in which the container group resides.
        self.namespace = namespace
        # The status of the container group.
        self.pod_status = pod_status
        # The status of the container group.
        self.status = status
        # The universally unique identifier (UUID) of the container group, which is similar to the unique identifier (UID) of the Kubernetes pod in terms of the concept and usage.
        self.uuid = uuid

    def validate(self):
        if self.pod_status:
            self.pod_status.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.annotations is not None:
            result['Annotations'] = self.annotations
        if self.container_group_id is not None:
            result['ContainerGroupId'] = self.container_group_id
        if self.name is not None:
            result['Name'] = self.name
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.pod_status is not None:
            result['PodStatus'] = self.pod_status.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.uuid is not None:
            result['uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Annotations') is not None:
            self.annotations = m.get('Annotations')
        if m.get('ContainerGroupId') is not None:
            self.container_group_id = m.get('ContainerGroupId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('PodStatus') is not None:
            temp_model = DescribeContainerGroupStatusResponseBodyDataPodStatus()
            self.pod_status = temp_model.from_map(m['PodStatus'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('uuid') is not None:
            self.uuid = m.get('uuid')
        return self


class DescribeContainerGroupStatusResponseBody(TeaModel):
    def __init__(
        self,
        data: List[DescribeContainerGroupStatusResponseBodyData] = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The collection of the statuses of the container groups.
        self.data = data
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

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
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeContainerGroupStatusResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeContainerGroupStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeContainerGroupStatusResponseBody = None,
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
            temp_model = DescribeContainerGroupStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeContainerGroupsRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the instances.
        self.key = key
        # The tag value of the instances.
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


class DescribeContainerGroupsRequest(TeaModel):
    def __init__(
        self,
        compute_category: str = None,
        container_group_ids: str = None,
        container_group_name: str = None,
        limit: int = None,
        next_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_group_id: str = None,
        status: str = None,
        tag: List[DescribeContainerGroupsRequestTag] = None,
        v_switch_id: str = None,
        with_event: bool = None,
        zone_id: str = None,
    ):
        # The computing power type of the elastic container instance. A value of economy specifies economic elastic container instances.
        self.compute_category = compute_category
        # The IDs of the elastic container instances in JSON format. You can specify up to 20 IDs.
        self.container_group_ids = container_group_ids
        # The name of the elastic container instance.
        self.container_group_name = container_group_name
        # The maximum number of resources to return. Default value: 20. Maximum value: 20.
        # 
        # >  The number of returned resources is less than or equal to the specified number.
        self.limit = limit
        # The token that determines the start point of the query. If this parameter is left empty, all results have been returned.
        # 
        # > You do not need to specify this parameter in the first request. Starting from the second request, you can obtain the token from the result returned by the previous request.
        self.next_token = next_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group to which the instance belongs.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the security group to which the instance belongs.
        self.security_group_id = security_group_id
        # The status of the elastic container instance. Valid values:
        # 
        # *   Pending: The instance is being started.
        # *   Running: The instance is running.
        # *   Succeeded: The instance runs successfully.
        # *   Failed: The instance fails to run.
        # *   Scheduling: The instance is being created.
        # *   ScheduleFailed: The instance fails to be created.
        # *   Restarting: The instance is being restarted.
        # *   Updating: The instance is being updated.
        # *   Terminating: The instance is being terminated.
        # *   Expired: The instance expires.
        self.status = status
        # The tag of the instances.
        self.tag = tag
        # The ID of the vSwitch to which the elastic container instances are connected.
        self.v_switch_id = v_switch_id
        # Specify whether to return event information.
        self.with_event = with_event
        # The ID of the zone in which the elastic container instances are deployed. If you do not specify this parameter, the system selects a zone.
        # 
        # This parameter is empty by default.
        self.zone_id = zone_id

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
        if self.compute_category is not None:
            result['ComputeCategory'] = self.compute_category
        if self.container_group_ids is not None:
            result['ContainerGroupIds'] = self.container_group_ids
        if self.container_group_name is not None:
            result['ContainerGroupName'] = self.container_group_name
        if self.limit is not None:
            result['Limit'] = self.limit
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
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.status is not None:
            result['Status'] = self.status
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.with_event is not None:
            result['WithEvent'] = self.with_event
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComputeCategory') is not None:
            self.compute_category = m.get('ComputeCategory')
        if m.get('ContainerGroupIds') is not None:
            self.container_group_ids = m.get('ContainerGroupIds')
        if m.get('ContainerGroupName') is not None:
            self.container_group_name = m.get('ContainerGroupName')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
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
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeContainerGroupsRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('WithEvent') is not None:
            self.with_event = m.get('WithEvent')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsContainersCurrentState(TeaModel):
    def __init__(
        self,
        detail_status: str = None,
        exit_code: int = None,
        finish_time: str = None,
        message: str = None,
        reason: str = None,
        signal: int = None,
        start_time: str = None,
        state: str = None,
    ):
        # The details of the container status.
        self.detail_status = detail_status
        # The exit code of the container.
        self.exit_code = exit_code
        # The time when the container stopped running.
        self.finish_time = finish_time
        # The message about the container status.
        self.message = message
        # The reason why the container is in this status.
        self.reason = reason
        # The code of the container status.
        self.signal = signal
        # The time when the container started to run.
        self.start_time = start_time
        # The container status. Valid values:
        # 
        # *   Waiting
        # *   Running
        # *   Terminated
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detail_status is not None:
            result['DetailStatus'] = self.detail_status
        if self.exit_code is not None:
            result['ExitCode'] = self.exit_code
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time
        if self.message is not None:
            result['Message'] = self.message
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.signal is not None:
            result['Signal'] = self.signal
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DetailStatus') is not None:
            self.detail_status = m.get('DetailStatus')
        if m.get('ExitCode') is not None:
            self.exit_code = m.get('ExitCode')
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('Signal') is not None:
            self.signal = m.get('Signal')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsContainersEnvironmentVarsValueFromFieldRef(TeaModel):
    def __init__(
        self,
        field_path: str = None,
    ):
        # The path of the field.
        self.field_path = field_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_path is not None:
            result['FieldPath'] = self.field_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldPath') is not None:
            self.field_path = m.get('FieldPath')
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsContainersEnvironmentVarsValueFrom(TeaModel):
    def __init__(
        self,
        field_ref: DescribeContainerGroupsResponseBodyContainerGroupsContainersEnvironmentVarsValueFromFieldRef = None,
    ):
        # The specified field.
        self.field_ref = field_ref

    def validate(self):
        if self.field_ref:
            self.field_ref.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_ref is not None:
            result['FieldRef'] = self.field_ref.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldRef') is not None:
            temp_model = DescribeContainerGroupsResponseBodyContainerGroupsContainersEnvironmentVarsValueFromFieldRef()
            self.field_ref = temp_model.from_map(m['FieldRef'])
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsContainersEnvironmentVars(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
        value_from: DescribeContainerGroupsResponseBodyContainerGroupsContainersEnvironmentVarsValueFrom = None,
    ):
        # The name of the environment variable.
        self.key = key
        # The value of the environment variable.
        self.value = value
        # The source of the environment variable value. This parameter has a value only when the Value parameter is left empty.
        self.value_from = value_from

    def validate(self):
        if self.value_from:
            self.value_from.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        if self.value_from is not None:
            result['ValueFrom'] = self.value_from.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('ValueFrom') is not None:
            temp_model = DescribeContainerGroupsResponseBodyContainerGroupsContainersEnvironmentVarsValueFrom()
            self.value_from = temp_model.from_map(m['ValueFrom'])
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsContainersLivenessProbeHttpGet(TeaModel):
    def __init__(
        self,
        path: str = None,
        port: int = None,
        scheme: str = None,
    ):
        # The path to which the system sends an HTTP GET request for a health check.
        self.path = path
        # The port to which the system sends an HTTP GET request for a health check.
        self.port = port
        # The protocol type supported by the method. Valid values: HTTP and HTTPS.
        self.scheme = scheme

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.path is not None:
            result['Path'] = self.path
        if self.port is not None:
            result['Port'] = self.port
        if self.scheme is not None:
            result['Scheme'] = self.scheme
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Scheme') is not None:
            self.scheme = m.get('Scheme')
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsContainersLivenessProbeTcpSocket(TeaModel):
    def __init__(
        self,
        host: str = None,
        port: int = None,
    ):
        # The hostname.
        self.host = host
        # The port number.
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host is not None:
            result['Host'] = self.host
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsContainersLivenessProbe(TeaModel):
    def __init__(
        self,
        execs: List[str] = None,
        failure_threshold: int = None,
        http_get: DescribeContainerGroupsResponseBodyContainerGroupsContainersLivenessProbeHttpGet = None,
        initial_delay_seconds: int = None,
        period_seconds: int = None,
        success_threshold: int = None,
        tcp_socket: DescribeContainerGroupsResponseBodyContainerGroupsContainersLivenessProbeTcpSocket = None,
        timeout_seconds: int = None,
    ):
        # The commands that are used to check the containers.
        self.execs = execs
        # The minimum number of consecutive failures that must occur for the check to be considered failed. Default value: 3.
        self.failure_threshold = failure_threshold
        # The HTTP GET method that is used to check the container.
        self.http_get = http_get
        # The number of seconds between the time when the startup of the container ends and the time when the probe starts.
        self.initial_delay_seconds = initial_delay_seconds
        # The interval at which the health check is performed. Default value: 10. Minimum value: 1. Unit: seconds.
        self.period_seconds = period_seconds
        # The minimum number of consecutive successes that must occur for the check to be considered successful. Default value: 1. The value must be 1.
        self.success_threshold = success_threshold
        # The TCP socket method that is used to check the container.
        self.tcp_socket = tcp_socket
        # The timeout period of the check. Default value: 1. Minimum value: 1. Unit: seconds.
        self.timeout_seconds = timeout_seconds

    def validate(self):
        if self.http_get:
            self.http_get.validate()
        if self.tcp_socket:
            self.tcp_socket.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.execs is not None:
            result['Execs'] = self.execs
        if self.failure_threshold is not None:
            result['FailureThreshold'] = self.failure_threshold
        if self.http_get is not None:
            result['HttpGet'] = self.http_get.to_map()
        if self.initial_delay_seconds is not None:
            result['InitialDelaySeconds'] = self.initial_delay_seconds
        if self.period_seconds is not None:
            result['PeriodSeconds'] = self.period_seconds
        if self.success_threshold is not None:
            result['SuccessThreshold'] = self.success_threshold
        if self.tcp_socket is not None:
            result['TcpSocket'] = self.tcp_socket.to_map()
        if self.timeout_seconds is not None:
            result['TimeoutSeconds'] = self.timeout_seconds
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Execs') is not None:
            self.execs = m.get('Execs')
        if m.get('FailureThreshold') is not None:
            self.failure_threshold = m.get('FailureThreshold')
        if m.get('HttpGet') is not None:
            temp_model = DescribeContainerGroupsResponseBodyContainerGroupsContainersLivenessProbeHttpGet()
            self.http_get = temp_model.from_map(m['HttpGet'])
        if m.get('InitialDelaySeconds') is not None:
            self.initial_delay_seconds = m.get('InitialDelaySeconds')
        if m.get('PeriodSeconds') is not None:
            self.period_seconds = m.get('PeriodSeconds')
        if m.get('SuccessThreshold') is not None:
            self.success_threshold = m.get('SuccessThreshold')
        if m.get('TcpSocket') is not None:
            temp_model = DescribeContainerGroupsResponseBodyContainerGroupsContainersLivenessProbeTcpSocket()
            self.tcp_socket = temp_model.from_map(m['TcpSocket'])
        if m.get('TimeoutSeconds') is not None:
            self.timeout_seconds = m.get('TimeoutSeconds')
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsContainersPorts(TeaModel):
    def __init__(
        self,
        port: int = None,
        protocol: str = None,
    ):
        # The port number. Valid values: 1 to 65535.
        self.port = port
        # The protocol type.
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.port is not None:
            result['Port'] = self.port
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsContainersPreviousState(TeaModel):
    def __init__(
        self,
        detail_status: str = None,
        exit_code: int = None,
        finish_time: str = None,
        message: str = None,
        reason: str = None,
        signal: int = None,
        start_time: str = None,
        state: str = None,
    ):
        # The details of the container status.
        self.detail_status = detail_status
        # The exit code of the container.
        self.exit_code = exit_code
        # The time when the container stopped running.
        self.finish_time = finish_time
        # The message about the container status.
        self.message = message
        # The reason why the container is in this status.
        self.reason = reason
        # The code of the container status.
        self.signal = signal
        # The time when the container started to run.
        self.start_time = start_time
        # The container status. Valid values:
        # 
        # *   Waiting: The container is being started.
        # *   Running: The container is running.
        # *   Terminated: The container stops running.
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detail_status is not None:
            result['DetailStatus'] = self.detail_status
        if self.exit_code is not None:
            result['ExitCode'] = self.exit_code
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time
        if self.message is not None:
            result['Message'] = self.message
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.signal is not None:
            result['Signal'] = self.signal
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DetailStatus') is not None:
            self.detail_status = m.get('DetailStatus')
        if m.get('ExitCode') is not None:
            self.exit_code = m.get('ExitCode')
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('Signal') is not None:
            self.signal = m.get('Signal')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsContainersReadinessProbeHttpGet(TeaModel):
    def __init__(
        self,
        path: str = None,
        port: int = None,
        scheme: str = None,
    ):
        # The path to which the system sends an HTTP GET request for a health check.
        self.path = path
        # The port to which the system sends an HTTP GET request for a health check.
        self.port = port
        # The protocol type supported by the method. Valid values: HTTP and HTTPS.
        self.scheme = scheme

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.path is not None:
            result['Path'] = self.path
        if self.port is not None:
            result['Port'] = self.port
        if self.scheme is not None:
            result['Scheme'] = self.scheme
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Scheme') is not None:
            self.scheme = m.get('Scheme')
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsContainersReadinessProbeTcpSocket(TeaModel):
    def __init__(
        self,
        host: str = None,
        port: int = None,
    ):
        # The hostname.
        self.host = host
        # The port number.
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host is not None:
            result['Host'] = self.host
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsContainersReadinessProbe(TeaModel):
    def __init__(
        self,
        execs: List[str] = None,
        failure_threshold: int = None,
        http_get: DescribeContainerGroupsResponseBodyContainerGroupsContainersReadinessProbeHttpGet = None,
        initial_delay_seconds: int = None,
        period_seconds: int = None,
        success_threshold: int = None,
        tcp_socket: DescribeContainerGroupsResponseBodyContainerGroupsContainersReadinessProbeTcpSocket = None,
        timeout_seconds: int = None,
    ):
        # The commands that are run in the container when you use a CLI to perform health checks.
        self.execs = execs
        # The minimum number of consecutive failures that must occur for the check to be considered failed. Default value: 3.
        self.failure_threshold = failure_threshold
        # The HTTP GET method that is used to check the container.
        self.http_get = http_get
        # The number of seconds between the time when the startup of the container ends and the time when the probe starts.
        self.initial_delay_seconds = initial_delay_seconds
        # The interval at which the health check is performed. Default value: 10. Minimum value: 1. Unit: seconds.
        self.period_seconds = period_seconds
        # The minimum number of consecutive successes that must occur for the check to be considered successful. Default value: 1. The value must be 1.
        self.success_threshold = success_threshold
        # The TCP socket method that is used to check the container.
        self.tcp_socket = tcp_socket
        # The timeout period of the check. Default value: 1. Minimum value: 1. Unit: seconds.
        self.timeout_seconds = timeout_seconds

    def validate(self):
        if self.http_get:
            self.http_get.validate()
        if self.tcp_socket:
            self.tcp_socket.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.execs is not None:
            result['Execs'] = self.execs
        if self.failure_threshold is not None:
            result['FailureThreshold'] = self.failure_threshold
        if self.http_get is not None:
            result['HttpGet'] = self.http_get.to_map()
        if self.initial_delay_seconds is not None:
            result['InitialDelaySeconds'] = self.initial_delay_seconds
        if self.period_seconds is not None:
            result['PeriodSeconds'] = self.period_seconds
        if self.success_threshold is not None:
            result['SuccessThreshold'] = self.success_threshold
        if self.tcp_socket is not None:
            result['TcpSocket'] = self.tcp_socket.to_map()
        if self.timeout_seconds is not None:
            result['TimeoutSeconds'] = self.timeout_seconds
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Execs') is not None:
            self.execs = m.get('Execs')
        if m.get('FailureThreshold') is not None:
            self.failure_threshold = m.get('FailureThreshold')
        if m.get('HttpGet') is not None:
            temp_model = DescribeContainerGroupsResponseBodyContainerGroupsContainersReadinessProbeHttpGet()
            self.http_get = temp_model.from_map(m['HttpGet'])
        if m.get('InitialDelaySeconds') is not None:
            self.initial_delay_seconds = m.get('InitialDelaySeconds')
        if m.get('PeriodSeconds') is not None:
            self.period_seconds = m.get('PeriodSeconds')
        if m.get('SuccessThreshold') is not None:
            self.success_threshold = m.get('SuccessThreshold')
        if m.get('TcpSocket') is not None:
            temp_model = DescribeContainerGroupsResponseBodyContainerGroupsContainersReadinessProbeTcpSocket()
            self.tcp_socket = temp_model.from_map(m['TcpSocket'])
        if m.get('TimeoutSeconds') is not None:
            self.timeout_seconds = m.get('TimeoutSeconds')
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsContainersSecurityContextCapability(TeaModel):
    def __init__(
        self,
        adds: List[str] = None,
    ):
        # The permissions specific to the process in the container.
        self.adds = adds

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adds is not None:
            result['Adds'] = self.adds
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Adds') is not None:
            self.adds = m.get('Adds')
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsContainersSecurityContext(TeaModel):
    def __init__(
        self,
        capability: DescribeContainerGroupsResponseBodyContainerGroupsContainersSecurityContextCapability = None,
        read_only_root_filesystem: bool = None,
        run_as_user: int = None,
    ):
        # The permissions specific to the processes in the container.
        self.capability = capability
        # Indicates whether permissions on the root file system are read-only. Valid value: true.
        self.read_only_root_filesystem = read_only_root_filesystem
        # The user ID (UID) that is used to run the container.
        self.run_as_user = run_as_user

    def validate(self):
        if self.capability:
            self.capability.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.capability is not None:
            result['Capability'] = self.capability.to_map()
        if self.read_only_root_filesystem is not None:
            result['ReadOnlyRootFilesystem'] = self.read_only_root_filesystem
        if self.run_as_user is not None:
            result['RunAsUser'] = self.run_as_user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Capability') is not None:
            temp_model = DescribeContainerGroupsResponseBodyContainerGroupsContainersSecurityContextCapability()
            self.capability = temp_model.from_map(m['Capability'])
        if m.get('ReadOnlyRootFilesystem') is not None:
            self.read_only_root_filesystem = m.get('ReadOnlyRootFilesystem')
        if m.get('RunAsUser') is not None:
            self.run_as_user = m.get('RunAsUser')
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsContainersVolumeMounts(TeaModel):
    def __init__(
        self,
        mount_path: str = None,
        mount_propagation: str = None,
        name: str = None,
        read_only: bool = None,
        sub_path: str = None,
    ):
        # The directory of the volume that is mounted to the container. The data in this directory is overwritten by the data on the volume.
        self.mount_path = mount_path
        # The mount propagation setting of the volume. Mount propagation allows volumes that are mounted on one container to be shared with other containers in the same pod, or even with other pods on the same node. Valid values:
        # 
        # *   None: The volume mount does not receive subsequent mounts that are performed on this volume or on the subdirectories of this volume.
        # *   HostToCotainer: The volume mount receives subsequent mounts that are performed on this volume or on the subdirectories of this volume.
        # *   Bidirectional: This value is similar to HostToCotainer. The volume mount receives subsequent mounts that are performed on this volume or on the subdirectories of this volume. In addition, all volume mounts that are performed on the container are propagated back to the host and all containers of all pods that use the same volume.
        self.mount_propagation = mount_propagation
        # The volume name.
        self.name = name
        # Indicates whether the volume is read-only.
        self.read_only = read_only
        # The subdirectory of the volume. You can use this parameter to mount the same volume to different subdirectories of the container.
        self.sub_path = sub_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mount_path is not None:
            result['MountPath'] = self.mount_path
        if self.mount_propagation is not None:
            result['MountPropagation'] = self.mount_propagation
        if self.name is not None:
            result['Name'] = self.name
        if self.read_only is not None:
            result['ReadOnly'] = self.read_only
        if self.sub_path is not None:
            result['SubPath'] = self.sub_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')
        if m.get('MountPropagation') is not None:
            self.mount_propagation = m.get('MountPropagation')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ReadOnly') is not None:
            self.read_only = m.get('ReadOnly')
        if m.get('SubPath') is not None:
            self.sub_path = m.get('SubPath')
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsContainers(TeaModel):
    def __init__(
        self,
        args: List[str] = None,
        commands: List[str] = None,
        cpu: float = None,
        current_state: DescribeContainerGroupsResponseBodyContainerGroupsContainersCurrentState = None,
        environment_vars: List[DescribeContainerGroupsResponseBodyContainerGroupsContainersEnvironmentVars] = None,
        gpu: int = None,
        image: str = None,
        image_pull_policy: str = None,
        liveness_probe: DescribeContainerGroupsResponseBodyContainerGroupsContainersLivenessProbe = None,
        memory: float = None,
        name: str = None,
        ports: List[DescribeContainerGroupsResponseBodyContainerGroupsContainersPorts] = None,
        previous_state: DescribeContainerGroupsResponseBodyContainerGroupsContainersPreviousState = None,
        readiness_probe: DescribeContainerGroupsResponseBodyContainerGroupsContainersReadinessProbe = None,
        ready: bool = None,
        restart_count: int = None,
        security_context: DescribeContainerGroupsResponseBodyContainerGroupsContainersSecurityContext = None,
        stdin: bool = None,
        stdin_once: bool = None,
        tty: bool = None,
        volume_mounts: List[DescribeContainerGroupsResponseBodyContainerGroupsContainersVolumeMounts] = None,
        working_dir: str = None,
    ):
        # The arguments that are passed to the startup commands of the container.
        self.args = args
        # The startup commands of the container.
        self.commands = commands
        # The number of vCPUs that are allocated to the container.
        self.cpu = cpu
        # The current container status.
        self.current_state = current_state
        # The environment variables of the container.
        self.environment_vars = environment_vars
        # The number of GPUs.
        self.gpu = gpu
        # The image in the container.
        self.image = image
        # The image pulling policy. Valid values:
        # 
        # *   Always: Each time the instance is updated, image pulling is performed.
        # *   IfNotPresent: On-premises images are preferentially used. If no on-premises images are available, image pulling is performed.
        # *   Never: On-premises images are always used. Image pulling is not performed.
        self.image_pull_policy = image_pull_policy
        # The liveness probe of the container.
        self.liveness_probe = liveness_probe
        # The memory size of the container. Unit: GiB.
        self.memory = memory
        # The name of the container.
        self.name = name
        # The exposed port and protocol of the container.
        self.ports = ports
        # The previous state of the container.
        self.previous_state = previous_state
        # The readiness probe that is used to check whether the container is ready to serve a request.
        self.readiness_probe = readiness_probe
        # Indicates whether the container passed the readiness probe.
        self.ready = ready
        # The number of times that the container restarted.
        self.restart_count = restart_count
        # The security context of the elastic container instance.
        self.security_context = security_context
        # Indicates whether the container allocates buffer resources to standard input streams when the container is running. If you do not specify this parameter, an end-of-file (EOF) error may occur when standard input streams in the container are read. Default value: false.
        self.stdin = stdin
        # Indicates whether standard input streams are disconnected after a client is disconnected. If Stdin is set to true, standard input streams remain connected among multiple sessions. If StdinOnce is set to true, standard input streams are connected after the container is started, and remain idle until a client is connected to receive data. After the client is disconnected, streams are also disconnected, and remain disconnected until the container restarts.
        self.stdin_once = stdin_once
        # Indicates whether interaction is enabled. Default value: false. If the value of the Command parameter is `/bin/bash`, the value of this parameter is true.
        self.tty = tty
        # Information about the mounted volumes.
        self.volume_mounts = volume_mounts
        # The working directory of the container.
        self.working_dir = working_dir

    def validate(self):
        if self.current_state:
            self.current_state.validate()
        if self.environment_vars:
            for k in self.environment_vars:
                if k:
                    k.validate()
        if self.liveness_probe:
            self.liveness_probe.validate()
        if self.ports:
            for k in self.ports:
                if k:
                    k.validate()
        if self.previous_state:
            self.previous_state.validate()
        if self.readiness_probe:
            self.readiness_probe.validate()
        if self.security_context:
            self.security_context.validate()
        if self.volume_mounts:
            for k in self.volume_mounts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.args is not None:
            result['Args'] = self.args
        if self.commands is not None:
            result['Commands'] = self.commands
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.current_state is not None:
            result['CurrentState'] = self.current_state.to_map()
        result['EnvironmentVars'] = []
        if self.environment_vars is not None:
            for k in self.environment_vars:
                result['EnvironmentVars'].append(k.to_map() if k else None)
        if self.gpu is not None:
            result['Gpu'] = self.gpu
        if self.image is not None:
            result['Image'] = self.image
        if self.image_pull_policy is not None:
            result['ImagePullPolicy'] = self.image_pull_policy
        if self.liveness_probe is not None:
            result['LivenessProbe'] = self.liveness_probe.to_map()
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.name is not None:
            result['Name'] = self.name
        result['Ports'] = []
        if self.ports is not None:
            for k in self.ports:
                result['Ports'].append(k.to_map() if k else None)
        if self.previous_state is not None:
            result['PreviousState'] = self.previous_state.to_map()
        if self.readiness_probe is not None:
            result['ReadinessProbe'] = self.readiness_probe.to_map()
        if self.ready is not None:
            result['Ready'] = self.ready
        if self.restart_count is not None:
            result['RestartCount'] = self.restart_count
        if self.security_context is not None:
            result['SecurityContext'] = self.security_context.to_map()
        if self.stdin is not None:
            result['Stdin'] = self.stdin
        if self.stdin_once is not None:
            result['StdinOnce'] = self.stdin_once
        if self.tty is not None:
            result['Tty'] = self.tty
        result['VolumeMounts'] = []
        if self.volume_mounts is not None:
            for k in self.volume_mounts:
                result['VolumeMounts'].append(k.to_map() if k else None)
        if self.working_dir is not None:
            result['WorkingDir'] = self.working_dir
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Args') is not None:
            self.args = m.get('Args')
        if m.get('Commands') is not None:
            self.commands = m.get('Commands')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('CurrentState') is not None:
            temp_model = DescribeContainerGroupsResponseBodyContainerGroupsContainersCurrentState()
            self.current_state = temp_model.from_map(m['CurrentState'])
        self.environment_vars = []
        if m.get('EnvironmentVars') is not None:
            for k in m.get('EnvironmentVars'):
                temp_model = DescribeContainerGroupsResponseBodyContainerGroupsContainersEnvironmentVars()
                self.environment_vars.append(temp_model.from_map(k))
        if m.get('Gpu') is not None:
            self.gpu = m.get('Gpu')
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('ImagePullPolicy') is not None:
            self.image_pull_policy = m.get('ImagePullPolicy')
        if m.get('LivenessProbe') is not None:
            temp_model = DescribeContainerGroupsResponseBodyContainerGroupsContainersLivenessProbe()
            self.liveness_probe = temp_model.from_map(m['LivenessProbe'])
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.ports = []
        if m.get('Ports') is not None:
            for k in m.get('Ports'):
                temp_model = DescribeContainerGroupsResponseBodyContainerGroupsContainersPorts()
                self.ports.append(temp_model.from_map(k))
        if m.get('PreviousState') is not None:
            temp_model = DescribeContainerGroupsResponseBodyContainerGroupsContainersPreviousState()
            self.previous_state = temp_model.from_map(m['PreviousState'])
        if m.get('ReadinessProbe') is not None:
            temp_model = DescribeContainerGroupsResponseBodyContainerGroupsContainersReadinessProbe()
            self.readiness_probe = temp_model.from_map(m['ReadinessProbe'])
        if m.get('Ready') is not None:
            self.ready = m.get('Ready')
        if m.get('RestartCount') is not None:
            self.restart_count = m.get('RestartCount')
        if m.get('SecurityContext') is not None:
            temp_model = DescribeContainerGroupsResponseBodyContainerGroupsContainersSecurityContext()
            self.security_context = temp_model.from_map(m['SecurityContext'])
        if m.get('Stdin') is not None:
            self.stdin = m.get('Stdin')
        if m.get('StdinOnce') is not None:
            self.stdin_once = m.get('StdinOnce')
        if m.get('Tty') is not None:
            self.tty = m.get('Tty')
        self.volume_mounts = []
        if m.get('VolumeMounts') is not None:
            for k in m.get('VolumeMounts'):
                temp_model = DescribeContainerGroupsResponseBodyContainerGroupsContainersVolumeMounts()
                self.volume_mounts.append(temp_model.from_map(k))
        if m.get('WorkingDir') is not None:
            self.working_dir = m.get('WorkingDir')
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsDnsConfigOptions(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The variable name of the option.
        self.name = name
        # The variable value of the option.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsDnsConfig(TeaModel):
    def __init__(
        self,
        name_servers: List[str] = None,
        options: List[DescribeContainerGroupsResponseBodyContainerGroupsDnsConfigOptions] = None,
        searches: List[str] = None,
    ):
        # The IP addresses of DNS servers.
        self.name_servers = name_servers
        # The options. Each option is a name-value pair. The value in the name-value pair is optional.
        self.options = options
        # The search domains of DNS servers.
        self.searches = searches

    def validate(self):
        if self.options:
            for k in self.options:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name_servers is not None:
            result['NameServers'] = self.name_servers
        result['Options'] = []
        if self.options is not None:
            for k in self.options:
                result['Options'].append(k.to_map() if k else None)
        if self.searches is not None:
            result['Searches'] = self.searches
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NameServers') is not None:
            self.name_servers = m.get('NameServers')
        self.options = []
        if m.get('Options') is not None:
            for k in m.get('Options'):
                temp_model = DescribeContainerGroupsResponseBodyContainerGroupsDnsConfigOptions()
                self.options.append(temp_model.from_map(k))
        if m.get('Searches') is not None:
            self.searches = m.get('Searches')
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsEciSecurityContextSysctls(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The name of the Sysctl parameter.
        self.name = name
        # The value of the Sysctl parameter.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsEciSecurityContext(TeaModel):
    def __init__(
        self,
        sysctls: List[DescribeContainerGroupsResponseBodyContainerGroupsEciSecurityContextSysctls] = None,
    ):
        # sysctl parameters.
        self.sysctls = sysctls

    def validate(self):
        if self.sysctls:
            for k in self.sysctls:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Sysctls'] = []
        if self.sysctls is not None:
            for k in self.sysctls:
                result['Sysctls'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.sysctls = []
        if m.get('Sysctls') is not None:
            for k in m.get('Sysctls'):
                temp_model = DescribeContainerGroupsResponseBodyContainerGroupsEciSecurityContextSysctls()
                self.sysctls.append(temp_model.from_map(k))
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsEvents(TeaModel):
    def __init__(
        self,
        count: int = None,
        first_timestamp: str = None,
        last_timestamp: str = None,
        message: str = None,
        name: str = None,
        reason: str = None,
        type: str = None,
    ):
        # The number of the events.
        self.count = count
        # The start time of the event.
        self.first_timestamp = first_timestamp
        # The end time of the event.
        self.last_timestamp = last_timestamp
        # The event message.
        self.message = message
        # The category to which the event belongs.
        self.name = name
        # The event name.
        self.reason = reason
        # The type of the event. Valid values:
        # 
        # *   Normal
        # *   Warning
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.first_timestamp is not None:
            result['FirstTimestamp'] = self.first_timestamp
        if self.last_timestamp is not None:
            result['LastTimestamp'] = self.last_timestamp
        if self.message is not None:
            result['Message'] = self.message
        if self.name is not None:
            result['Name'] = self.name
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('FirstTimestamp') is not None:
            self.first_timestamp = m.get('FirstTimestamp')
        if m.get('LastTimestamp') is not None:
            self.last_timestamp = m.get('LastTimestamp')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsHostAliases(TeaModel):
    def __init__(
        self,
        hostnames: List[str] = None,
        ip: str = None,
    ):
        # The information about the hosts.
        self.hostnames = hostnames
        # The IP address of the instance.
        self.ip = ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hostnames is not None:
            result['Hostnames'] = self.hostnames
        if self.ip is not None:
            result['Ip'] = self.ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Hostnames') is not None:
            self.hostnames = m.get('Hostnames')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsInitContainersCurrentState(TeaModel):
    def __init__(
        self,
        detail_status: str = None,
        exit_code: int = None,
        finish_time: str = None,
        message: str = None,
        reason: str = None,
        signal: int = None,
        start_time: str = None,
        state: str = None,
    ):
        # The details of the container status.
        self.detail_status = detail_status
        # The exit code of the container.
        self.exit_code = exit_code
        # The time when the container stopped running.
        self.finish_time = finish_time
        # The event message.
        self.message = message
        # The reason why the container is in this status.
        self.reason = reason
        # The code of the container status.
        self.signal = signal
        # The time when the container started to run.
        self.start_time = start_time
        # The container status. Valid values:
        # 
        # *   Waiting
        # *   Running
        # *   Terminated
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detail_status is not None:
            result['DetailStatus'] = self.detail_status
        if self.exit_code is not None:
            result['ExitCode'] = self.exit_code
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time
        if self.message is not None:
            result['Message'] = self.message
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.signal is not None:
            result['Signal'] = self.signal
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DetailStatus') is not None:
            self.detail_status = m.get('DetailStatus')
        if m.get('ExitCode') is not None:
            self.exit_code = m.get('ExitCode')
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('Signal') is not None:
            self.signal = m.get('Signal')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsInitContainersEnvironmentVarsValueFromFieldRef(TeaModel):
    def __init__(
        self,
        field_path: str = None,
    ):
        # The path of the field. Only `status.podIP` is supported.
        self.field_path = field_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_path is not None:
            result['FieldPath'] = self.field_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldPath') is not None:
            self.field_path = m.get('FieldPath')
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsInitContainersEnvironmentVarsValueFrom(TeaModel):
    def __init__(
        self,
        field_ref: DescribeContainerGroupsResponseBodyContainerGroupsInitContainersEnvironmentVarsValueFromFieldRef = None,
    ):
        # The specified fields.
        self.field_ref = field_ref

    def validate(self):
        if self.field_ref:
            self.field_ref.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_ref is not None:
            result['FieldRef'] = self.field_ref.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldRef') is not None:
            temp_model = DescribeContainerGroupsResponseBodyContainerGroupsInitContainersEnvironmentVarsValueFromFieldRef()
            self.field_ref = temp_model.from_map(m['FieldRef'])
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsInitContainersEnvironmentVars(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
        value_from: DescribeContainerGroupsResponseBodyContainerGroupsInitContainersEnvironmentVarsValueFrom = None,
    ):
        # The name of the environment variable.
        self.key = key
        # The value of the environment variable.
        self.value = value
        # The source of the environment variable value. This parameter has a value only when the Value parameter is left empty.
        self.value_from = value_from

    def validate(self):
        if self.value_from:
            self.value_from.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        if self.value_from is not None:
            result['ValueFrom'] = self.value_from.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('ValueFrom') is not None:
            temp_model = DescribeContainerGroupsResponseBodyContainerGroupsInitContainersEnvironmentVarsValueFrom()
            self.value_from = temp_model.from_map(m['ValueFrom'])
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsInitContainersPorts(TeaModel):
    def __init__(
        self,
        port: int = None,
        protocol: str = None,
    ):
        # The port number. Valid values: 1 to 65535.
        self.port = port
        # The protocol type.
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.port is not None:
            result['Port'] = self.port
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsInitContainersPreviousState(TeaModel):
    def __init__(
        self,
        detail_status: str = None,
        exit_code: int = None,
        finish_time: str = None,
        message: str = None,
        reason: str = None,
        signal: int = None,
        start_time: str = None,
        state: str = None,
    ):
        # The details of the container status.
        self.detail_status = detail_status
        # The exit code of the container.
        self.exit_code = exit_code
        # The time when the container stopped running.
        self.finish_time = finish_time
        # The message about the container status.
        self.message = message
        # The reason why the container is in this status.
        self.reason = reason
        # The code of the container status.
        self.signal = signal
        # The time when the container started to run.
        self.start_time = start_time
        # The container status. Valid values: Waiting, Running, and Terminated.
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detail_status is not None:
            result['DetailStatus'] = self.detail_status
        if self.exit_code is not None:
            result['ExitCode'] = self.exit_code
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time
        if self.message is not None:
            result['Message'] = self.message
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.signal is not None:
            result['Signal'] = self.signal
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DetailStatus') is not None:
            self.detail_status = m.get('DetailStatus')
        if m.get('ExitCode') is not None:
            self.exit_code = m.get('ExitCode')
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('Signal') is not None:
            self.signal = m.get('Signal')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsInitContainersSecurityContextCapability(TeaModel):
    def __init__(
        self,
        adds: List[str] = None,
    ):
        # The permissions specific to the processes in the container.
        self.adds = adds

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adds is not None:
            result['Adds'] = self.adds
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Adds') is not None:
            self.adds = m.get('Adds')
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsInitContainersSecurityContext(TeaModel):
    def __init__(
        self,
        capability: DescribeContainerGroupsResponseBodyContainerGroupsInitContainersSecurityContextCapability = None,
        read_only_root_filesystem: bool = None,
        run_as_user: int = None,
    ):
        # The permissions specific to the processes in the container.
        self.capability = capability
        # Indicates whether permissions on the root file system are read-only.
        self.read_only_root_filesystem = read_only_root_filesystem
        # The UID that is used to run the entry point of the container process.
        self.run_as_user = run_as_user

    def validate(self):
        if self.capability:
            self.capability.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.capability is not None:
            result['Capability'] = self.capability.to_map()
        if self.read_only_root_filesystem is not None:
            result['ReadOnlyRootFilesystem'] = self.read_only_root_filesystem
        if self.run_as_user is not None:
            result['RunAsUser'] = self.run_as_user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Capability') is not None:
            temp_model = DescribeContainerGroupsResponseBodyContainerGroupsInitContainersSecurityContextCapability()
            self.capability = temp_model.from_map(m['Capability'])
        if m.get('ReadOnlyRootFilesystem') is not None:
            self.read_only_root_filesystem = m.get('ReadOnlyRootFilesystem')
        if m.get('RunAsUser') is not None:
            self.run_as_user = m.get('RunAsUser')
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsInitContainersVolumeMounts(TeaModel):
    def __init__(
        self,
        mount_path: str = None,
        mount_propagation: str = None,
        name: str = None,
        read_only: bool = None,
    ):
        # The directory of the volume that is mounted to the container. The data in this directory is overwritten by the data on the volume.
        self.mount_path = mount_path
        # The mount propagation setting of the volume. Mount propagation allows volumes that are mounted on one container to be shared with other containers in the same pod, or even with other pods on the same node. Valid values:
        # 
        # *   None: The volume mount does not receive subsequent mounts that are performed on this volume or on the subdirectories of this volume.
        # *   HostToCotainer: The volume mount receives subsequent mounts that are performed on this volume or on the subdirectories of this volume.
        # *   Bidirectional: This value is similar to HostToCotainer. The volume mount receives subsequent mounts that are performed on this volume or on the subdirectories of this volume. In addition, all volume mounts that are performed on the container are propagated back to the host and all containers of all pods that use the same volume.
        self.mount_propagation = mount_propagation
        # The name of the volume. The value of this parameter is the same as the name of the volume that you selected when you purchased the container.
        self.name = name
        # Indicates whether the volume is read-only.
        self.read_only = read_only

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mount_path is not None:
            result['MountPath'] = self.mount_path
        if self.mount_propagation is not None:
            result['MountPropagation'] = self.mount_propagation
        if self.name is not None:
            result['Name'] = self.name
        if self.read_only is not None:
            result['ReadOnly'] = self.read_only
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')
        if m.get('MountPropagation') is not None:
            self.mount_propagation = m.get('MountPropagation')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ReadOnly') is not None:
            self.read_only = m.get('ReadOnly')
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsInitContainers(TeaModel):
    def __init__(
        self,
        args: List[str] = None,
        command: List[str] = None,
        cpu: float = None,
        current_state: DescribeContainerGroupsResponseBodyContainerGroupsInitContainersCurrentState = None,
        environment_vars: List[DescribeContainerGroupsResponseBodyContainerGroupsInitContainersEnvironmentVars] = None,
        gpu: int = None,
        image: str = None,
        image_pull_policy: str = None,
        memory: float = None,
        name: str = None,
        ports: List[DescribeContainerGroupsResponseBodyContainerGroupsInitContainersPorts] = None,
        previous_state: DescribeContainerGroupsResponseBodyContainerGroupsInitContainersPreviousState = None,
        ready: bool = None,
        restart_count: int = None,
        security_context: DescribeContainerGroupsResponseBodyContainerGroupsInitContainersSecurityContext = None,
        volume_mounts: List[DescribeContainerGroupsResponseBodyContainerGroupsInitContainersVolumeMounts] = None,
        working_dir: str = None,
    ):
        # The arguments that are passed to the startup commands of the container.
        self.args = args
        # The startup commands of the containers.
        self.command = command
        # The number of vCPUs that are allocated to the container.
        self.cpu = cpu
        # The current container status.
        self.current_state = current_state
        # The environment variables of the init container.
        self.environment_vars = environment_vars
        # The number of GPUs.
        self.gpu = gpu
        # The image of the container.
        self.image = image
        # The image pulling policy. Valid values:
        # 
        # *   Always: Each time the instance is updated, image pulling is performed.
        # *   IfNotPresent: On-premises images are preferentially used. If no on-premises images are available, image pulling is performed.
        # *   Never: On-premises images are always used. Image pulling is not performed.
        self.image_pull_policy = image_pull_policy
        # The memory size of the init container. Unit: GiB.
        self.memory = memory
        # The name of the init container.
        self.name = name
        # The exposed port and protocol of the container.
        self.ports = ports
        # The previous state of the container.
        self.previous_state = previous_state
        # Indicates whether the container passed the readiness probe.
        self.ready = ready
        # The number of times that the container restarted.
        self.restart_count = restart_count
        # The security context of the container.
        self.security_context = security_context
        # The information about the volumes that are mounted to the init container.
        self.volume_mounts = volume_mounts
        # The working directory of the container.
        self.working_dir = working_dir

    def validate(self):
        if self.current_state:
            self.current_state.validate()
        if self.environment_vars:
            for k in self.environment_vars:
                if k:
                    k.validate()
        if self.ports:
            for k in self.ports:
                if k:
                    k.validate()
        if self.previous_state:
            self.previous_state.validate()
        if self.security_context:
            self.security_context.validate()
        if self.volume_mounts:
            for k in self.volume_mounts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.args is not None:
            result['Args'] = self.args
        if self.command is not None:
            result['Command'] = self.command
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.current_state is not None:
            result['CurrentState'] = self.current_state.to_map()
        result['EnvironmentVars'] = []
        if self.environment_vars is not None:
            for k in self.environment_vars:
                result['EnvironmentVars'].append(k.to_map() if k else None)
        if self.gpu is not None:
            result['Gpu'] = self.gpu
        if self.image is not None:
            result['Image'] = self.image
        if self.image_pull_policy is not None:
            result['ImagePullPolicy'] = self.image_pull_policy
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.name is not None:
            result['Name'] = self.name
        result['Ports'] = []
        if self.ports is not None:
            for k in self.ports:
                result['Ports'].append(k.to_map() if k else None)
        if self.previous_state is not None:
            result['PreviousState'] = self.previous_state.to_map()
        if self.ready is not None:
            result['Ready'] = self.ready
        if self.restart_count is not None:
            result['RestartCount'] = self.restart_count
        if self.security_context is not None:
            result['SecurityContext'] = self.security_context.to_map()
        result['VolumeMounts'] = []
        if self.volume_mounts is not None:
            for k in self.volume_mounts:
                result['VolumeMounts'].append(k.to_map() if k else None)
        if self.working_dir is not None:
            result['WorkingDir'] = self.working_dir
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Args') is not None:
            self.args = m.get('Args')
        if m.get('Command') is not None:
            self.command = m.get('Command')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('CurrentState') is not None:
            temp_model = DescribeContainerGroupsResponseBodyContainerGroupsInitContainersCurrentState()
            self.current_state = temp_model.from_map(m['CurrentState'])
        self.environment_vars = []
        if m.get('EnvironmentVars') is not None:
            for k in m.get('EnvironmentVars'):
                temp_model = DescribeContainerGroupsResponseBodyContainerGroupsInitContainersEnvironmentVars()
                self.environment_vars.append(temp_model.from_map(k))
        if m.get('Gpu') is not None:
            self.gpu = m.get('Gpu')
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('ImagePullPolicy') is not None:
            self.image_pull_policy = m.get('ImagePullPolicy')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.ports = []
        if m.get('Ports') is not None:
            for k in m.get('Ports'):
                temp_model = DescribeContainerGroupsResponseBodyContainerGroupsInitContainersPorts()
                self.ports.append(temp_model.from_map(k))
        if m.get('PreviousState') is not None:
            temp_model = DescribeContainerGroupsResponseBodyContainerGroupsInitContainersPreviousState()
            self.previous_state = temp_model.from_map(m['PreviousState'])
        if m.get('Ready') is not None:
            self.ready = m.get('Ready')
        if m.get('RestartCount') is not None:
            self.restart_count = m.get('RestartCount')
        if m.get('SecurityContext') is not None:
            temp_model = DescribeContainerGroupsResponseBodyContainerGroupsInitContainersSecurityContext()
            self.security_context = temp_model.from_map(m['SecurityContext'])
        self.volume_mounts = []
        if m.get('VolumeMounts') is not None:
            for k in m.get('VolumeMounts'):
                temp_model = DescribeContainerGroupsResponseBodyContainerGroupsInitContainersVolumeMounts()
                self.volume_mounts.append(temp_model.from_map(k))
        if m.get('WorkingDir') is not None:
            self.working_dir = m.get('WorkingDir')
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsTags(TeaModel):
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


class DescribeContainerGroupsResponseBodyContainerGroupsVolumesConfigFileVolumeConfigFileToPaths(TeaModel):
    def __init__(
        self,
        content: str = None,
        path: str = None,
    ):
        # The content of the ConfigFile volume. Maximum size: 32 KB.
        self.content = content
        # The relative path of the ConfigFile volume.
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsVolumes(TeaModel):
    def __init__(
        self,
        config_file_volume_config_file_to_paths: List[DescribeContainerGroupsResponseBodyContainerGroupsVolumesConfigFileVolumeConfigFileToPaths] = None,
        disk_volume_disk_id: str = None,
        disk_volume_fs_type: str = None,
        empty_dir_volume_medium: str = None,
        empty_dir_volume_size_limit: str = None,
        flex_volume_driver: str = None,
        flex_volume_fs_type: str = None,
        flex_volume_options: str = None,
        nfsvolume_path: str = None,
        nfsvolume_read_only: bool = None,
        nfsvolume_server: str = None,
        name: str = None,
        type: str = None,
    ):
        # The path of the ConfigFile volume.
        self.config_file_volume_config_file_to_paths = config_file_volume_config_file_to_paths
        # The ID of the disk when you set Type to DiskVolume.
        self.disk_volume_disk_id = disk_volume_disk_id
        # The file system type of the disk volume.
        self.disk_volume_fs_type = disk_volume_fs_type
        # The storage media for the emptyDir volume. This parameter is empty by default, indicating that the node file system is used as the storage media. Valid values:
        # 
        # *   Memory: Memory is used as the storage media.
        # *   LocalRaid0: Local disks are formed into RAID 0. This value is valid only if an elastic container instance that has local disks mounted is created. For more information, see [Create an elastic container instance that has local disks mounted](https://help.aliyun.com/document_detail/114664.html).
        self.empty_dir_volume_medium = empty_dir_volume_medium
        # The storage size of the emptyDir volume.
        self.empty_dir_volume_size_limit = empty_dir_volume_size_limit
        # The name of the driver when you set the Type parameter to FlexVolume.
        self.flex_volume_driver = flex_volume_driver
        # The file system type when you set the Type parameter to FlexVolume. The default value varies based on the script of the FlexVolume plug-in.
        self.flex_volume_fs_type = flex_volume_fs_type
        # The options when you set the Type parameter to FlexVolume.
        self.flex_volume_options = flex_volume_options
        # The path of the NFS volume.
        self.nfsvolume_path = nfsvolume_path
        # Indicates whether the NFS volume is read-only.
        self.nfsvolume_read_only = nfsvolume_read_only
        # The address of the NFS server.
        self.nfsvolume_server = nfsvolume_server
        # The volume name.
        self.name = name
        # The type of the volume. Valid values:
        # 
        # *   EmptyDirVolume
        # *   NFSVolume
        # *   ConfigFileVolume
        # *   FlexVolume
        self.type = type

    def validate(self):
        if self.config_file_volume_config_file_to_paths:
            for k in self.config_file_volume_config_file_to_paths:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ConfigFileVolumeConfigFileToPaths'] = []
        if self.config_file_volume_config_file_to_paths is not None:
            for k in self.config_file_volume_config_file_to_paths:
                result['ConfigFileVolumeConfigFileToPaths'].append(k.to_map() if k else None)
        if self.disk_volume_disk_id is not None:
            result['DiskVolumeDiskId'] = self.disk_volume_disk_id
        if self.disk_volume_fs_type is not None:
            result['DiskVolumeFsType'] = self.disk_volume_fs_type
        if self.empty_dir_volume_medium is not None:
            result['EmptyDirVolumeMedium'] = self.empty_dir_volume_medium
        if self.empty_dir_volume_size_limit is not None:
            result['EmptyDirVolumeSizeLimit'] = self.empty_dir_volume_size_limit
        if self.flex_volume_driver is not None:
            result['FlexVolumeDriver'] = self.flex_volume_driver
        if self.flex_volume_fs_type is not None:
            result['FlexVolumeFsType'] = self.flex_volume_fs_type
        if self.flex_volume_options is not None:
            result['FlexVolumeOptions'] = self.flex_volume_options
        if self.nfsvolume_path is not None:
            result['NFSVolumePath'] = self.nfsvolume_path
        if self.nfsvolume_read_only is not None:
            result['NFSVolumeReadOnly'] = self.nfsvolume_read_only
        if self.nfsvolume_server is not None:
            result['NFSVolumeServer'] = self.nfsvolume_server
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.config_file_volume_config_file_to_paths = []
        if m.get('ConfigFileVolumeConfigFileToPaths') is not None:
            for k in m.get('ConfigFileVolumeConfigFileToPaths'):
                temp_model = DescribeContainerGroupsResponseBodyContainerGroupsVolumesConfigFileVolumeConfigFileToPaths()
                self.config_file_volume_config_file_to_paths.append(temp_model.from_map(k))
        if m.get('DiskVolumeDiskId') is not None:
            self.disk_volume_disk_id = m.get('DiskVolumeDiskId')
        if m.get('DiskVolumeFsType') is not None:
            self.disk_volume_fs_type = m.get('DiskVolumeFsType')
        if m.get('EmptyDirVolumeMedium') is not None:
            self.empty_dir_volume_medium = m.get('EmptyDirVolumeMedium')
        if m.get('EmptyDirVolumeSizeLimit') is not None:
            self.empty_dir_volume_size_limit = m.get('EmptyDirVolumeSizeLimit')
        if m.get('FlexVolumeDriver') is not None:
            self.flex_volume_driver = m.get('FlexVolumeDriver')
        if m.get('FlexVolumeFsType') is not None:
            self.flex_volume_fs_type = m.get('FlexVolumeFsType')
        if m.get('FlexVolumeOptions') is not None:
            self.flex_volume_options = m.get('FlexVolumeOptions')
        if m.get('NFSVolumePath') is not None:
            self.nfsvolume_path = m.get('NFSVolumePath')
        if m.get('NFSVolumeReadOnly') is not None:
            self.nfsvolume_read_only = m.get('NFSVolumeReadOnly')
        if m.get('NFSVolumeServer') is not None:
            self.nfsvolume_server = m.get('NFSVolumeServer')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeContainerGroupsResponseBodyContainerGroups(TeaModel):
    def __init__(
        self,
        compute_category: str = None,
        container_group_id: str = None,
        container_group_name: str = None,
        containers: List[DescribeContainerGroupsResponseBodyContainerGroupsContainers] = None,
        cpu: float = None,
        creation_time: str = None,
        discount: int = None,
        dns_config: DescribeContainerGroupsResponseBodyContainerGroupsDnsConfig = None,
        eci_security_context: DescribeContainerGroupsResponseBodyContainerGroupsEciSecurityContext = None,
        eni_instance_id: str = None,
        ephemeral_storage: int = None,
        events: List[DescribeContainerGroupsResponseBodyContainerGroupsEvents] = None,
        expired_time: str = None,
        failed_time: str = None,
        host_aliases: List[DescribeContainerGroupsResponseBodyContainerGroupsHostAliases] = None,
        init_containers: List[DescribeContainerGroupsResponseBodyContainerGroupsInitContainers] = None,
        instance_type: str = None,
        internet_ip: str = None,
        intranet_ip: str = None,
        ipv_6address: str = None,
        memory: float = None,
        ram_role_name: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        restart_policy: str = None,
        security_group_id: str = None,
        spot_price_limit: float = None,
        spot_strategy: str = None,
        status: str = None,
        succeeded_time: str = None,
        tags: List[DescribeContainerGroupsResponseBodyContainerGroupsTags] = None,
        tenant_eni_instance_id: str = None,
        tenant_eni_ip: str = None,
        tenant_security_group_id: str = None,
        tenant_vswitch_id: str = None,
        v_switch_id: str = None,
        volumes: List[DescribeContainerGroupsResponseBodyContainerGroupsVolumes] = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        # The computing power type of the elastic container instance. Valid values:
        # 
        # *   economy: economic computing power.
        # *   general: general-purpose computing power.
        self.compute_category = compute_category
        # The instance ID.
        self.container_group_id = container_group_id
        # The instance name.
        self.container_group_name = container_group_name
        # The information about containers in the elastic container instance.
        self.containers = containers
        # The number of vCPUs that are allocated to the elastic container instance.
        self.cpu = cpu
        # The time when the instance was created. The time follows the RFC 3339 standard. The time is displayed in UTC.
        self.creation_time = creation_time
        # The discount.
        self.discount = discount
        # The Domain Name System (DNS) settings.
        self.dns_config = dns_config
        # The security context of the elastic container instance.
        self.eci_security_context = eci_security_context
        # The ID of the elastic network interface (ENI).
        self.eni_instance_id = eni_instance_id
        # The size of the temporary storage space. Unit: GiB.
        self.ephemeral_storage = ephemeral_storage
        # The events of the elastic container instance. A maximum of 50 events can be returned.
        self.events = events
        # The time when the elastic container instance failed to run due to overdue payments. The time follows the RFC 3339 standard. The time is displayed in UTC.
        self.expired_time = expired_time
        # The time when the instance failed to run. The time follows the RFC 3339 standard. The time is displayed in UTC.
        self.failed_time = failed_time
        # The hostnames and IP addresses for a container that are added to the hosts file of the elastic container instance.
        self.host_aliases = host_aliases
        # The information about the init containers.
        self.init_containers = init_containers
        # The instance type of the specified Elastic Compute Service (ECS) instance.
        self.instance_type = instance_type
        # The public IP address.
        self.internet_ip = internet_ip
        # The private IP address.
        self.intranet_ip = intranet_ip
        # The IPv6 address of the instance.
        self.ipv_6address = ipv_6address
        # The memory size of the instance. Unit: GiB.
        self.memory = memory
        # The name of the instance RAM role. The elastic container instance and the ECS instance share a RAM role. For more information, see [Use an instance RAM role by calling API operations](https://help.aliyun.com/document_detail/61178.html).
        self.ram_role_name = ram_role_name
        # The region ID of the instance.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The restart policy of the elastic container instance. Valid values:
        # 
        # *   Never: Never restarts the instance if a container in the instance exits upon termination.
        # *   Always: Always restarts the instance if a container in the instance exits upon termination.
        # *   OnFailure: Restarts the instance only if a container in the instance exists upon failure with a status code of non-zero.
        self.restart_policy = restart_policy
        # The ID of the security group to which the instances belong.
        self.security_group_id = security_group_id
        # The maximum hourly price for the preemptible elastic container instance.
        # 
        # This parameter is returned only when SpotStrategy is set to SpotWithPriceLimit.
        self.spot_price_limit = spot_price_limit
        # The bid policy for the instance. Default value: NoSpot. Valid values:
        # 
        # *   NoSpot: The instance is a regular pay-as-you-go instance.
        # *   SpotWithPriceLimit: The instance is a preemptible instance that has a user-defined maximum hourly price.
        # *   SpotAsPriceGo: The instance is a preemptible instance for which the market price at the time of purchase is automatically used as the bid price.
        self.spot_strategy = spot_strategy
        # The status of the instance. Valid values:
        # 
        # *   Pending: The instance is being started.
        # *   Running: The instance is running.
        # *   Succeeded: The instance successfully runs.
        # *   Failed: The instance fails to run.
        # *   Scheduling: The instance is being created.
        # *   ScheduleFailed: The instance fails to be created.
        # *   Restarting: The instance is being restarted.
        # *   Updating: The instance is being updated.
        # *   Terminating: The instance is being terminated.
        # *   Expired: The instance is expired.
        self.status = status
        # The time when all containers exited on success. The time follows the RFC 3339 standard. The time is displayed in UTC.
        self.succeeded_time = succeeded_time
        # The tags that are added to the instance.
        self.tags = tags
        # This parameter is not publicly available.
        self.tenant_eni_instance_id = tenant_eni_instance_id
        # This parameter is not publicly available.
        self.tenant_eni_ip = tenant_eni_ip
        # This parameter is not publicly available.
        self.tenant_security_group_id = tenant_security_group_id
        # This parameter is not publicly available.
        self.tenant_vswitch_id = tenant_vswitch_id
        # The ID of the vSwitch to which the instance is connected.
        self.v_switch_id = v_switch_id
        # The information about the volumes.
        self.volumes = volumes
        # The ID of the VPC to which the instance belongs.
        self.vpc_id = vpc_id
        # The zone to which the instance belongs.
        self.zone_id = zone_id

    def validate(self):
        if self.containers:
            for k in self.containers:
                if k:
                    k.validate()
        if self.dns_config:
            self.dns_config.validate()
        if self.eci_security_context:
            self.eci_security_context.validate()
        if self.events:
            for k in self.events:
                if k:
                    k.validate()
        if self.host_aliases:
            for k in self.host_aliases:
                if k:
                    k.validate()
        if self.init_containers:
            for k in self.init_containers:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()
        if self.volumes:
            for k in self.volumes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compute_category is not None:
            result['ComputeCategory'] = self.compute_category
        if self.container_group_id is not None:
            result['ContainerGroupId'] = self.container_group_id
        if self.container_group_name is not None:
            result['ContainerGroupName'] = self.container_group_name
        result['Containers'] = []
        if self.containers is not None:
            for k in self.containers:
                result['Containers'].append(k.to_map() if k else None)
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.discount is not None:
            result['Discount'] = self.discount
        if self.dns_config is not None:
            result['DnsConfig'] = self.dns_config.to_map()
        if self.eci_security_context is not None:
            result['EciSecurityContext'] = self.eci_security_context.to_map()
        if self.eni_instance_id is not None:
            result['EniInstanceId'] = self.eni_instance_id
        if self.ephemeral_storage is not None:
            result['EphemeralStorage'] = self.ephemeral_storage
        result['Events'] = []
        if self.events is not None:
            for k in self.events:
                result['Events'].append(k.to_map() if k else None)
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.failed_time is not None:
            result['FailedTime'] = self.failed_time
        result['HostAliases'] = []
        if self.host_aliases is not None:
            for k in self.host_aliases:
                result['HostAliases'].append(k.to_map() if k else None)
        result['InitContainers'] = []
        if self.init_containers is not None:
            for k in self.init_containers:
                result['InitContainers'].append(k.to_map() if k else None)
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip
        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip
        if self.ipv_6address is not None:
            result['Ipv6Address'] = self.ipv_6address
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.ram_role_name is not None:
            result['RamRoleName'] = self.ram_role_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.restart_policy is not None:
            result['RestartPolicy'] = self.restart_policy
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.spot_price_limit is not None:
            result['SpotPriceLimit'] = self.spot_price_limit
        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy
        if self.status is not None:
            result['Status'] = self.status
        if self.succeeded_time is not None:
            result['SucceededTime'] = self.succeeded_time
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.tenant_eni_instance_id is not None:
            result['TenantEniInstanceId'] = self.tenant_eni_instance_id
        if self.tenant_eni_ip is not None:
            result['TenantEniIp'] = self.tenant_eni_ip
        if self.tenant_security_group_id is not None:
            result['TenantSecurityGroupId'] = self.tenant_security_group_id
        if self.tenant_vswitch_id is not None:
            result['TenantVSwitchId'] = self.tenant_vswitch_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        result['Volumes'] = []
        if self.volumes is not None:
            for k in self.volumes:
                result['Volumes'].append(k.to_map() if k else None)
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComputeCategory') is not None:
            self.compute_category = m.get('ComputeCategory')
        if m.get('ContainerGroupId') is not None:
            self.container_group_id = m.get('ContainerGroupId')
        if m.get('ContainerGroupName') is not None:
            self.container_group_name = m.get('ContainerGroupName')
        self.containers = []
        if m.get('Containers') is not None:
            for k in m.get('Containers'):
                temp_model = DescribeContainerGroupsResponseBodyContainerGroupsContainers()
                self.containers.append(temp_model.from_map(k))
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Discount') is not None:
            self.discount = m.get('Discount')
        if m.get('DnsConfig') is not None:
            temp_model = DescribeContainerGroupsResponseBodyContainerGroupsDnsConfig()
            self.dns_config = temp_model.from_map(m['DnsConfig'])
        if m.get('EciSecurityContext') is not None:
            temp_model = DescribeContainerGroupsResponseBodyContainerGroupsEciSecurityContext()
            self.eci_security_context = temp_model.from_map(m['EciSecurityContext'])
        if m.get('EniInstanceId') is not None:
            self.eni_instance_id = m.get('EniInstanceId')
        if m.get('EphemeralStorage') is not None:
            self.ephemeral_storage = m.get('EphemeralStorage')
        self.events = []
        if m.get('Events') is not None:
            for k in m.get('Events'):
                temp_model = DescribeContainerGroupsResponseBodyContainerGroupsEvents()
                self.events.append(temp_model.from_map(k))
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('FailedTime') is not None:
            self.failed_time = m.get('FailedTime')
        self.host_aliases = []
        if m.get('HostAliases') is not None:
            for k in m.get('HostAliases'):
                temp_model = DescribeContainerGroupsResponseBodyContainerGroupsHostAliases()
                self.host_aliases.append(temp_model.from_map(k))
        self.init_containers = []
        if m.get('InitContainers') is not None:
            for k in m.get('InitContainers'):
                temp_model = DescribeContainerGroupsResponseBodyContainerGroupsInitContainers()
                self.init_containers.append(temp_model.from_map(k))
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')
        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')
        if m.get('Ipv6Address') is not None:
            self.ipv_6address = m.get('Ipv6Address')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('RamRoleName') is not None:
            self.ram_role_name = m.get('RamRoleName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('RestartPolicy') is not None:
            self.restart_policy = m.get('RestartPolicy')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('SpotPriceLimit') is not None:
            self.spot_price_limit = m.get('SpotPriceLimit')
        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SucceededTime') is not None:
            self.succeeded_time = m.get('SucceededTime')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = DescribeContainerGroupsResponseBodyContainerGroupsTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('TenantEniInstanceId') is not None:
            self.tenant_eni_instance_id = m.get('TenantEniInstanceId')
        if m.get('TenantEniIp') is not None:
            self.tenant_eni_ip = m.get('TenantEniIp')
        if m.get('TenantSecurityGroupId') is not None:
            self.tenant_security_group_id = m.get('TenantSecurityGroupId')
        if m.get('TenantVSwitchId') is not None:
            self.tenant_vswitch_id = m.get('TenantVSwitchId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        self.volumes = []
        if m.get('Volumes') is not None:
            for k in m.get('Volumes'):
                temp_model = DescribeContainerGroupsResponseBodyContainerGroupsVolumes()
                self.volumes.append(temp_model.from_map(k))
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeContainerGroupsResponseBody(TeaModel):
    def __init__(
        self,
        container_groups: List[DescribeContainerGroupsResponseBodyContainerGroups] = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # Details about the queried elastic container instances.
        self.container_groups = container_groups
        # The token that determines the start point of the query.
        self.next_token = next_token
        # The ID of the request. The value is unique.
        self.request_id = request_id
        # The number of queried instances.
        self.total_count = total_count

    def validate(self):
        if self.container_groups:
            for k in self.container_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ContainerGroups'] = []
        if self.container_groups is not None:
            for k in self.container_groups:
                result['ContainerGroups'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.container_groups = []
        if m.get('ContainerGroups') is not None:
            for k in m.get('ContainerGroups'):
                temp_model = DescribeContainerGroupsResponseBodyContainerGroups()
                self.container_groups.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeContainerGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeContainerGroupsResponseBody = None,
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
            temp_model = DescribeContainerGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeContainerLogRequest(TeaModel):
    def __init__(
        self,
        container_group_id: str = None,
        container_name: str = None,
        last_time: bool = None,
        limit_bytes: int = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        since_seconds: int = None,
        start_time: str = None,
        tail: int = None,
        timestamps: bool = None,
    ):
        # The instance ID.
        # 
        # This parameter is required.
        self.container_group_id = container_group_id
        # The name of the container.
        # 
        # This parameter is required.
        self.container_name = container_name
        # Specifies whether to query the logs of the previous container if the container exits and restarts. Valid values:
        # 
        # *   true
        # *   false
        # 
        # Default value: false.
        self.last_time = last_time
        # The limit on the total size of logs. Unit: bytes. Valid values: 1 to 1048576(1 MB).
        self.limit_bytes = limit_bytes
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the elastic container instance.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # A relative time in seconds before the current time from which to show logs. Examples: 10, 20, and 30.
        self.since_seconds = since_seconds
        # The beginning of the time range to query. Specify the time in the RFC 3339 standard. The time must be in UTC.
        self.start_time = start_time
        # The number of the most recent log entries that you want to query. Default value: 500. Maximum value: 2000.\\
        # A maximum of 1 MB log data can be returned.
        self.tail = tail
        # Specifies whether to return the timestamps of logs. Valid values:
        # 
        # *   true
        # *   false
        # 
        # Default value: false.
        self.timestamps = timestamps

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.container_group_id is not None:
            result['ContainerGroupId'] = self.container_group_id
        if self.container_name is not None:
            result['ContainerName'] = self.container_name
        if self.last_time is not None:
            result['LastTime'] = self.last_time
        if self.limit_bytes is not None:
            result['LimitBytes'] = self.limit_bytes
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
        if self.since_seconds is not None:
            result['SinceSeconds'] = self.since_seconds
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.tail is not None:
            result['Tail'] = self.tail
        if self.timestamps is not None:
            result['Timestamps'] = self.timestamps
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContainerGroupId') is not None:
            self.container_group_id = m.get('ContainerGroupId')
        if m.get('ContainerName') is not None:
            self.container_name = m.get('ContainerName')
        if m.get('LastTime') is not None:
            self.last_time = m.get('LastTime')
        if m.get('LimitBytes') is not None:
            self.limit_bytes = m.get('LimitBytes')
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
        if m.get('SinceSeconds') is not None:
            self.since_seconds = m.get('SinceSeconds')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Tail') is not None:
            self.tail = m.get('Tail')
        if m.get('Timestamps') is not None:
            self.timestamps = m.get('Timestamps')
        return self


class DescribeContainerLogResponseBody(TeaModel):
    def __init__(
        self,
        container_name: str = None,
        content: str = None,
        request_id: str = None,
    ):
        # The container name.
        self.container_name = container_name
        # The content of the log.
        self.content = content
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.container_name is not None:
            result['ContainerName'] = self.container_name
        if self.content is not None:
            result['Content'] = self.content
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContainerName') is not None:
            self.container_name = m.get('ContainerName')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeContainerLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeContainerLogResponseBody = None,
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
            temp_model = DescribeContainerLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDataCachesRequestTag(TeaModel):
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


class DescribeDataCachesRequest(TeaModel):
    def __init__(
        self,
        bucket: str = None,
        data_cache_id: List[str] = None,
        limit: int = None,
        next_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        path: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        tag: List[DescribeDataCachesRequestTag] = None,
    ):
        # The bucket that stores the data cache. Default value: default.
        self.bucket = bucket
        # The data cache IDs.
        self.data_cache_id = data_cache_id
        # The maximum entries of query results that are allowed to be displayed. Valid values: 1 to 20. Default value: 20.
        self.limit = limit
        # The query token. Set the value to the NextToken value that is returned in the previous call.
        self.next_token = next_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The virtual host (vHost) directory in which the data cache resides.
        self.path = path
        # The region ID of the data caches that you want to query.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group to which the data cache belongs.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The tags that are attached to the data cache.
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
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        if self.data_cache_id is not None:
            result['DataCacheId'] = self.data_cache_id
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.path is not None:
            result['Path'] = self.path
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
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        if m.get('DataCacheId') is not None:
            self.data_cache_id = m.get('DataCacheId')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Path') is not None:
            self.path = m.get('Path')
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
                temp_model = DescribeDataCachesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeDataCachesResponseBodyDataCachesDataSource(TeaModel):
    def __init__(
        self,
        options: str = None,
        type: str = None,
    ):
        # The parameters that are configured for the data source.
        self.options = options
        # The type of the data source. Valid values:
        # 
        # *   NAS
        # *   OSS
        # *   URL
        # *   SNAPSHOT
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.options is not None:
            result['Options'] = self.options
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Options') is not None:
            self.options = m.get('Options')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeDataCachesResponseBodyDataCachesEvents(TeaModel):
    def __init__(
        self,
        count: int = None,
        first_timestamp: str = None,
        last_timestamp: str = None,
        message: str = None,
        name: str = None,
        reason: str = None,
        type: str = None,
    ):
        # The number of times that the event occurred.
        self.count = count
        # The time when the event started.
        self.first_timestamp = first_timestamp
        # The time when the event ended.
        self.last_timestamp = last_timestamp
        # The message about the event.
        self.message = message
        # The event name.
        self.name = name
        # The reason for the transition into the current status of the event.
        self.reason = reason
        # The type of the event. Valid values:
        # 
        # *   Normal
        # *   Warning
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.first_timestamp is not None:
            result['FirstTimestamp'] = self.first_timestamp
        if self.last_timestamp is not None:
            result['LastTimestamp'] = self.last_timestamp
        if self.message is not None:
            result['Message'] = self.message
        if self.name is not None:
            result['Name'] = self.name
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('FirstTimestamp') is not None:
            self.first_timestamp = m.get('FirstTimestamp')
        if m.get('LastTimestamp') is not None:
            self.last_timestamp = m.get('LastTimestamp')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeDataCachesResponseBodyDataCachesTags(TeaModel):
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


class DescribeDataCachesResponseBodyDataCaches(TeaModel):
    def __init__(
        self,
        bucket: str = None,
        container_group_id: str = None,
        creation_time: str = None,
        data_cache_id: str = None,
        data_source: DescribeDataCachesResponseBodyDataCachesDataSource = None,
        events: List[DescribeDataCachesResponseBodyDataCachesEvents] = None,
        expire_date_time: str = None,
        flash_snapshot_id: str = None,
        last_matched_time: str = None,
        name: str = None,
        path: str = None,
        progress: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        size: int = None,
        snapshot_id: str = None,
        status: str = None,
        tags: List[DescribeDataCachesResponseBodyDataCachesTags] = None,
    ):
        # The bucket that stores the data cache.
        self.bucket = bucket
        # The ID of the elastic container instance that was generated when the data cache was created.
        self.container_group_id = container_group_id
        # The time when the data cache was created.
        self.creation_time = creation_time
        # The ID of the data cache.
        self.data_cache_id = data_cache_id
        # The information about the data source.
        self.data_source = data_source
        # The events.
        self.events = events
        # The time when the data cache expires.
        self.expire_date_time = expire_date_time
        # The ID of the on-premises snapshot.
        self.flash_snapshot_id = flash_snapshot_id
        # The time when the data cache was last matched.
        self.last_matched_time = last_matched_time
        # The name of the data cache.
        self.name = name
        # The directory in which the virtual host of the data cache resides.
        self.path = path
        # The creation progress of the data cache.
        self.progress = progress
        # The region ID.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The size of the data cache. Unit: GiB.
        self.size = size
        # The snapshot ID.
        self.snapshot_id = snapshot_id
        # The status of the data cache. Valid values:
        # 
        # *   Loading: The data cache is loading data.
        # *   Creating: The data cache is being created.
        # *   Available: The data cache is created.
        # *   Failed: The data cache failed to be created.
        # *   Updating: The data cache is being updated.
        # *   UpdateFailed: The data cache failed to be updated.
        # 
        # If the data cache is in the Available state, the data cache can be used.
        self.status = status
        # The tags that are attached to the data cache.
        self.tags = tags

    def validate(self):
        if self.data_source:
            self.data_source.validate()
        if self.events:
            for k in self.events:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        if self.container_group_id is not None:
            result['ContainerGroupId'] = self.container_group_id
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.data_cache_id is not None:
            result['DataCacheId'] = self.data_cache_id
        if self.data_source is not None:
            result['DataSource'] = self.data_source.to_map()
        result['Events'] = []
        if self.events is not None:
            for k in self.events:
                result['Events'].append(k.to_map() if k else None)
        if self.expire_date_time is not None:
            result['ExpireDateTime'] = self.expire_date_time
        if self.flash_snapshot_id is not None:
            result['FlashSnapshotId'] = self.flash_snapshot_id
        if self.last_matched_time is not None:
            result['LastMatchedTime'] = self.last_matched_time
        if self.name is not None:
            result['Name'] = self.name
        if self.path is not None:
            result['Path'] = self.path
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.size is not None:
            result['Size'] = self.size
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        if self.status is not None:
            result['Status'] = self.status
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        if m.get('ContainerGroupId') is not None:
            self.container_group_id = m.get('ContainerGroupId')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('DataCacheId') is not None:
            self.data_cache_id = m.get('DataCacheId')
        if m.get('DataSource') is not None:
            temp_model = DescribeDataCachesResponseBodyDataCachesDataSource()
            self.data_source = temp_model.from_map(m['DataSource'])
        self.events = []
        if m.get('Events') is not None:
            for k in m.get('Events'):
                temp_model = DescribeDataCachesResponseBodyDataCachesEvents()
                self.events.append(temp_model.from_map(k))
        if m.get('ExpireDateTime') is not None:
            self.expire_date_time = m.get('ExpireDateTime')
        if m.get('FlashSnapshotId') is not None:
            self.flash_snapshot_id = m.get('FlashSnapshotId')
        if m.get('LastMatchedTime') is not None:
            self.last_matched_time = m.get('LastMatchedTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = DescribeDataCachesResponseBodyDataCachesTags()
                self.tags.append(temp_model.from_map(k))
        return self


class DescribeDataCachesResponseBody(TeaModel):
    def __init__(
        self,
        data_caches: List[DescribeDataCachesResponseBodyDataCaches] = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The information about the data caches.
        self.data_caches = data_caches
        # The query token. Set the value to the NextToken value that is returned in the previous call.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.data_caches:
            for k in self.data_caches:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataCaches'] = []
        if self.data_caches is not None:
            for k in self.data_caches:
                result['DataCaches'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_caches = []
        if m.get('DataCaches') is not None:
            for k in m.get('DataCaches'):
                temp_model = DescribeDataCachesResponseBodyDataCaches()
                self.data_caches.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDataCachesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDataCachesResponseBody = None,
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
            temp_model = DescribeDataCachesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeImageCachesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N of the image cache.
        self.key = key
        # The value of tag N of the image cache.
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


class DescribeImageCachesRequest(TeaModel):
    def __init__(
        self,
        image: str = None,
        image_cache_id: str = None,
        image_cache_name: str = None,
        image_full_match: bool = None,
        image_match_count_request: int = None,
        limit: int = None,
        match_image: List[str] = None,
        next_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        snapshot_id: str = None,
        tag: List[DescribeImageCachesRequestTag] = None,
    ):
        # The container images.
        self.image = image
        # The IDs of the image caches.
        self.image_cache_id = image_cache_id
        # The names of the image caches.
        self.image_cache_name = image_cache_name
        # Specifies whether the image layers of the image caches must contain all image layers of the container image.\\
        # If you configure MatchImage, you can configure this parameter to further filter query results.
        self.image_full_match = image_full_match
        # The quantity of image caches whose image layers contain all image layers of the container image.\\
        # If you configure MatchImage, you can configure this parameter to further filter query results.
        self.image_match_count_request = image_match_count_request
        # The maximum entries of query results that are allowed to be displayed.
        self.limit = limit
        # The container images used to match the image caches that you want to query. You can specify a maximum of 100 container images.
        self.match_image = match_image
        # The pagination token that is used in the next request to retrieve a new page of results. You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the image caches.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group to which the image caches belong.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The IDs of the snapshots that correspond to the image caches.
        self.snapshot_id = snapshot_id
        # The tags to add to the image caches.
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
        if self.image is not None:
            result['Image'] = self.image
        if self.image_cache_id is not None:
            result['ImageCacheId'] = self.image_cache_id
        if self.image_cache_name is not None:
            result['ImageCacheName'] = self.image_cache_name
        if self.image_full_match is not None:
            result['ImageFullMatch'] = self.image_full_match
        if self.image_match_count_request is not None:
            result['ImageMatchCountRequest'] = self.image_match_count_request
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.match_image is not None:
            result['MatchImage'] = self.match_image
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
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('ImageCacheId') is not None:
            self.image_cache_id = m.get('ImageCacheId')
        if m.get('ImageCacheName') is not None:
            self.image_cache_name = m.get('ImageCacheName')
        if m.get('ImageFullMatch') is not None:
            self.image_full_match = m.get('ImageFullMatch')
        if m.get('ImageMatchCountRequest') is not None:
            self.image_match_count_request = m.get('ImageMatchCountRequest')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('MatchImage') is not None:
            self.match_image = m.get('MatchImage')
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
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeImageCachesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeImageCachesResponseBodyImageCachesEvents(TeaModel):
    def __init__(
        self,
        count: int = None,
        first_timestamp: str = None,
        last_timestamp: str = None,
        message: str = None,
        name: str = None,
        reason: str = None,
        type: str = None,
    ):
        # The number of events.
        self.count = count
        # The time when the event started.
        self.first_timestamp = first_timestamp
        # The time when the event ended.
        self.last_timestamp = last_timestamp
        # The message about the event.
        self.message = message
        # The name of the event.
        self.name = name
        # The cause of the event.
        self.reason = reason
        # The type of the event. Valid values:
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.first_timestamp is not None:
            result['FirstTimestamp'] = self.first_timestamp
        if self.last_timestamp is not None:
            result['LastTimestamp'] = self.last_timestamp
        if self.message is not None:
            result['Message'] = self.message
        if self.name is not None:
            result['Name'] = self.name
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('FirstTimestamp') is not None:
            self.first_timestamp = m.get('FirstTimestamp')
        if m.get('LastTimestamp') is not None:
            self.last_timestamp = m.get('LastTimestamp')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeImageCachesResponseBodyImageCachesTags(TeaModel):
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


class DescribeImageCachesResponseBodyImageCaches(TeaModel):
    def __init__(
        self,
        container_group_id: str = None,
        creation_time: str = None,
        elimination_strategy: str = None,
        events: List[DescribeImageCachesResponseBodyImageCachesEvents] = None,
        expire_date_time: str = None,
        flash_snapshot_id: str = None,
        image_cache_id: str = None,
        image_cache_name: str = None,
        image_cache_size: int = None,
        images: List[str] = None,
        last_matched_time: str = None,
        progress: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        snapshot_id: str = None,
        status: str = None,
        tags: List[DescribeImageCachesResponseBodyImageCachesTags] = None,
    ):
        # The ID of the elastic container instance.
        self.container_group_id = container_group_id
        # The time when the image cache was created.
        self.creation_time = creation_time
        # The elimination policy of the image cache. This parameter is empty by default, which indicates that the image cache is always retained.
        # 
        # You can set this parameter to LRU, which indicates that the image cache can be automatically deleted. When the number of image caches reaches the quota, the system automatically deletes the image caches whose EliminationStrategy parameter is set to LRU and that are least regularly used.
        self.elimination_strategy = elimination_strategy
        # The events of pulling an image to create the image cache.
        self.events = events
        # The time when the image cache expires.
        self.expire_date_time = expire_date_time
        # The ID of the local snapshot. A temporary local snapshot is created if the instant image cache feature is enabled.
        self.flash_snapshot_id = flash_snapshot_id
        # The ID of the image cache.
        self.image_cache_id = image_cache_id
        # The name of the image cache.
        self.image_cache_name = image_cache_name
        # The size of the image cache. Unit: GiB.
        self.image_cache_size = image_cache_size
        # The images contained in the image cache.
        self.images = images
        # The time when the image cache was last matched.
        self.last_matched_time = last_matched_time
        # The progress of creating the snapshot that is used to create the image cache.
        # 
        # >  If the instant image cache feature is enabled, the system creates a temporary local snapshot and then a regular snapshot. In this case, this parameter indicates the progress of creating the regular snapshot.
        self.progress = progress
        # The region ID of the image cache.
        self.region_id = region_id
        # The ID of the resource group to which the image cache belongs.
        self.resource_group_id = resource_group_id
        # The ID of the snapshot that corresponds to the image cache.
        self.snapshot_id = snapshot_id
        # The status of the image cache. Valid values:
        # 
        # *   Preparing: The image cache is being prepared.
        # *   Creating: The image is being created.
        # *   Ready: The image cache is created.
        # *   Failed: The image cache failed to be created.
        # *   Updating: The image cache is being updated.
        # *   UpdateFailed: The image cache failed to be updated.
        # 
        # The image cache is ready for use when it is in the Ready state.
        self.status = status
        # The tags of the image cache.
        self.tags = tags

    def validate(self):
        if self.events:
            for k in self.events:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.container_group_id is not None:
            result['ContainerGroupId'] = self.container_group_id
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.elimination_strategy is not None:
            result['EliminationStrategy'] = self.elimination_strategy
        result['Events'] = []
        if self.events is not None:
            for k in self.events:
                result['Events'].append(k.to_map() if k else None)
        if self.expire_date_time is not None:
            result['ExpireDateTime'] = self.expire_date_time
        if self.flash_snapshot_id is not None:
            result['FlashSnapshotId'] = self.flash_snapshot_id
        if self.image_cache_id is not None:
            result['ImageCacheId'] = self.image_cache_id
        if self.image_cache_name is not None:
            result['ImageCacheName'] = self.image_cache_name
        if self.image_cache_size is not None:
            result['ImageCacheSize'] = self.image_cache_size
        if self.images is not None:
            result['Images'] = self.images
        if self.last_matched_time is not None:
            result['LastMatchedTime'] = self.last_matched_time
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        if self.status is not None:
            result['Status'] = self.status
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContainerGroupId') is not None:
            self.container_group_id = m.get('ContainerGroupId')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('EliminationStrategy') is not None:
            self.elimination_strategy = m.get('EliminationStrategy')
        self.events = []
        if m.get('Events') is not None:
            for k in m.get('Events'):
                temp_model = DescribeImageCachesResponseBodyImageCachesEvents()
                self.events.append(temp_model.from_map(k))
        if m.get('ExpireDateTime') is not None:
            self.expire_date_time = m.get('ExpireDateTime')
        if m.get('FlashSnapshotId') is not None:
            self.flash_snapshot_id = m.get('FlashSnapshotId')
        if m.get('ImageCacheId') is not None:
            self.image_cache_id = m.get('ImageCacheId')
        if m.get('ImageCacheName') is not None:
            self.image_cache_name = m.get('ImageCacheName')
        if m.get('ImageCacheSize') is not None:
            self.image_cache_size = m.get('ImageCacheSize')
        if m.get('Images') is not None:
            self.images = m.get('Images')
        if m.get('LastMatchedTime') is not None:
            self.last_matched_time = m.get('LastMatchedTime')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = DescribeImageCachesResponseBodyImageCachesTags()
                self.tags.append(temp_model.from_map(k))
        return self


class DescribeImageCachesResponseBody(TeaModel):
    def __init__(
        self,
        image_caches: List[DescribeImageCachesResponseBodyImageCaches] = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The information about image caches.
        self.image_caches = image_caches
        # The returned value of NextToken is a pagination token, which can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.image_caches:
            for k in self.image_caches:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ImageCaches'] = []
        if self.image_caches is not None:
            for k in self.image_caches:
                result['ImageCaches'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.image_caches = []
        if m.get('ImageCaches') is not None:
            for k in m.get('ImageCaches'):
                temp_model = DescribeImageCachesResponseBodyImageCaches()
                self.image_caches.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeImageCachesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeImageCachesResponseBody = None,
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
            temp_model = DescribeImageCachesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceOpsRecordsRequest(TeaModel):
    def __init__(
        self,
        container_group_id: str = None,
        ops_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The ID of the elastic container instance.
        # 
        # This parameter is required.
        self.container_group_id = container_group_id
        # The type of the O\\&M task. Valid values:
        # 
        # *   coredump
        # *   tcpdump
        # 
        # This parameter is required.
        self.ops_type = ops_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the instance.
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
        if self.container_group_id is not None:
            result['ContainerGroupId'] = self.container_group_id
        if self.ops_type is not None:
            result['OpsType'] = self.ops_type
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
        if m.get('ContainerGroupId') is not None:
            self.container_group_id = m.get('ContainerGroupId')
        if m.get('OpsType') is not None:
            self.ops_type = m.get('OpsType')
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


class DescribeInstanceOpsRecordsResponseBodyRecords(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        expire_time: str = None,
        ops_status: str = None,
        ops_type: str = None,
        result_content: str = None,
        result_type: str = None,
    ):
        # The time when the O\\&M task was created.
        self.create_time = create_time
        # The time when the O\\&M task expires.
        self.expire_time = expire_time
        # The status of the O\\&M task.
        # - Ready
        # - Failed
        # - Expired
        # - Closed
        # - Success
        self.ops_status = ops_status
        # The type of the O\\&M task.
        self.ops_type = ops_type
        # The content of the O\\&M result. The content is the download URL of the files that are generated for the O\\&M task.
        self.result_content = result_content
        # The type of the O\\&M result. Valid value: OSS. This value indicates that the files generated for the O\\&M task are saved to Object Storage Service (OSS) buckets.
        self.result_type = result_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.ops_status is not None:
            result['OpsStatus'] = self.ops_status
        if self.ops_type is not None:
            result['OpsType'] = self.ops_type
        if self.result_content is not None:
            result['ResultContent'] = self.result_content
        if self.result_type is not None:
            result['ResultType'] = self.result_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('OpsStatus') is not None:
            self.ops_status = m.get('OpsStatus')
        if m.get('OpsType') is not None:
            self.ops_type = m.get('OpsType')
        if m.get('ResultContent') is not None:
            self.result_content = m.get('ResultContent')
        if m.get('ResultType') is not None:
            self.result_type = m.get('ResultType')
        return self


class DescribeInstanceOpsRecordsResponseBody(TeaModel):
    def __init__(
        self,
        records: List[DescribeInstanceOpsRecordsResponseBodyRecords] = None,
        request_id: str = None,
    ):
        # The details of the O\\&M tasks.
        self.records = records
        # The request ID.
        self.request_id = request_id

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
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = DescribeInstanceOpsRecordsResponseBodyRecords()
                self.records.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeInstanceOpsRecordsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeInstanceOpsRecordsResponseBody = None,
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
            temp_model = DescribeInstanceOpsRecordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMultiContainerGroupMetricRequest(TeaModel):
    def __init__(
        self,
        container_group_ids: str = None,
        metric_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The instance ID. The value is a JSON array. You can specify up to 20 instance IDs at a time.
        # 
        # This parameter is required.
        self.container_group_ids = container_group_ids
        # The type of the monitoring data. Set the value to summary. This value indicates that records are returned.
        self.metric_type = metric_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group to which the elastic container instances belong.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.container_group_ids is not None:
            result['ContainerGroupIds'] = self.container_group_ids
        if self.metric_type is not None:
            result['MetricType'] = self.metric_type
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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContainerGroupIds') is not None:
            self.container_group_ids = m.get('ContainerGroupIds')
        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')
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
        return self


class DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecordsCPU(TeaModel):
    def __init__(
        self,
        limit: int = None,
        load: int = None,
        usage_core_nano_seconds: int = None,
        usage_nano_cores: int = None,
    ):
        # The upper limit of vCPU usage. The calculation formula for this parameter: The number of vCPUs × 1000.
        self.limit = limit
        # The average load in the last 10 seconds.
        self.load = load
        # The cumulative usage of vCPUs.
        self.usage_core_nano_seconds = usage_core_nano_seconds
        # The vCPU usage in the sampling window. Unit for the sampling window: nanoseconds.
        self.usage_nano_cores = usage_nano_cores

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.load is not None:
            result['Load'] = self.load
        if self.usage_core_nano_seconds is not None:
            result['UsageCoreNanoSeconds'] = self.usage_core_nano_seconds
        if self.usage_nano_cores is not None:
            result['UsageNanoCores'] = self.usage_nano_cores
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('Load') is not None:
            self.load = m.get('Load')
        if m.get('UsageCoreNanoSeconds') is not None:
            self.usage_core_nano_seconds = m.get('UsageCoreNanoSeconds')
        if m.get('UsageNanoCores') is not None:
            self.usage_nano_cores = m.get('UsageNanoCores')
        return self


class DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecordsContainersCPU(TeaModel):
    def __init__(
        self,
        limit: int = None,
        load: int = None,
        usage_core_nano_seconds: int = None,
        usage_nano_cores: int = None,
    ):
        # The upper limit of vCPU usage. The calculation formula for this parameter: The number of vCPUs × 1000.
        self.limit = limit
        # The average load in the last 10 seconds.
        self.load = load
        # The cumulative usage of vCPUs.
        self.usage_core_nano_seconds = usage_core_nano_seconds
        # The vCPU usage in the sampling window. Unit for the sampling window: nanoseconds.
        self.usage_nano_cores = usage_nano_cores

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.load is not None:
            result['Load'] = self.load
        if self.usage_core_nano_seconds is not None:
            result['UsageCoreNanoSeconds'] = self.usage_core_nano_seconds
        if self.usage_nano_cores is not None:
            result['UsageNanoCores'] = self.usage_nano_cores
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('Load') is not None:
            self.load = m.get('Load')
        if m.get('UsageCoreNanoSeconds') is not None:
            self.usage_core_nano_seconds = m.get('UsageCoreNanoSeconds')
        if m.get('UsageNanoCores') is not None:
            self.usage_nano_cores = m.get('UsageNanoCores')
        return self


class DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecordsContainersMemory(TeaModel):
    def __init__(
        self,
        available_bytes: int = None,
        cache: int = None,
        rss: int = None,
        usage_bytes: int = None,
        working_set: int = None,
    ):
        # The size of the available memory. Unit: bytes.
        self.available_bytes = available_bytes
        # The size of the cache. Unit: bytes.
        self.cache = cache
        # The size of the resident memory set, which indicates the size of the physical memory that is actually used. Unit: bytes.
        self.rss = rss
        # The size of the used memory. Unit: bytes.
        self.usage_bytes = usage_bytes
        # The usage of the working set. Unit: bytes.
        self.working_set = working_set

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.available_bytes is not None:
            result['AvailableBytes'] = self.available_bytes
        if self.cache is not None:
            result['Cache'] = self.cache
        if self.rss is not None:
            result['Rss'] = self.rss
        if self.usage_bytes is not None:
            result['UsageBytes'] = self.usage_bytes
        if self.working_set is not None:
            result['WorkingSet'] = self.working_set
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableBytes') is not None:
            self.available_bytes = m.get('AvailableBytes')
        if m.get('Cache') is not None:
            self.cache = m.get('Cache')
        if m.get('Rss') is not None:
            self.rss = m.get('Rss')
        if m.get('UsageBytes') is not None:
            self.usage_bytes = m.get('UsageBytes')
        if m.get('WorkingSet') is not None:
            self.working_set = m.get('WorkingSet')
        return self


class DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecordsContainers(TeaModel):
    def __init__(
        self,
        cpu: DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecordsContainersCPU = None,
        memory: DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecordsContainersMemory = None,
        name: str = None,
    ):
        # The vCPU monitoring data of the container.
        self.cpu = cpu
        # The memory monitoring data of the container.
        self.memory = memory
        # The name.
        self.name = name

    def validate(self):
        if self.cpu:
            self.cpu.validate()
        if self.memory:
            self.memory.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['CPU'] = self.cpu.to_map()
        if self.memory is not None:
            result['Memory'] = self.memory.to_map()
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CPU') is not None:
            temp_model = DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecordsContainersCPU()
            self.cpu = temp_model.from_map(m['CPU'])
        if m.get('Memory') is not None:
            temp_model = DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecordsContainersMemory()
            self.memory = temp_model.from_map(m['Memory'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecordsDisk(TeaModel):
    def __init__(
        self,
        device: str = None,
        read_bytes: int = None,
        read_io: int = None,
        write_bytes: int = None,
        write_io: int = None,
    ):
        # The name of the disk.
        self.device = device
        # The amount of data that was read from the disk. Unit: bytes.
        self.read_bytes = read_bytes
        # This parameter is unavailable for public use.
        self.read_io = read_io
        # The amount of data that was written to the disk. Unit: bytes.
        self.write_bytes = write_bytes
        # This parameter is unavailable for public use.
        self.write_io = write_io

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device is not None:
            result['Device'] = self.device
        if self.read_bytes is not None:
            result['ReadBytes'] = self.read_bytes
        if self.read_io is not None:
            result['ReadIo'] = self.read_io
        if self.write_bytes is not None:
            result['WriteBytes'] = self.write_bytes
        if self.write_io is not None:
            result['WriteIo'] = self.write_io
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Device') is not None:
            self.device = m.get('Device')
        if m.get('ReadBytes') is not None:
            self.read_bytes = m.get('ReadBytes')
        if m.get('ReadIo') is not None:
            self.read_io = m.get('ReadIo')
        if m.get('WriteBytes') is not None:
            self.write_bytes = m.get('WriteBytes')
        if m.get('WriteIo') is not None:
            self.write_io = m.get('WriteIo')
        return self


class DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecordsFilesystem(TeaModel):
    def __init__(
        self,
        available: int = None,
        capacity: int = None,
        fs_name: str = None,
        usage: int = None,
    ):
        # The size of the available space.
        self.available = available
        # The total file system space.
        self.capacity = capacity
        # The name of the partition.
        self.fs_name = fs_name
        # The size of used space.
        self.usage = usage

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.available is not None:
            result['Available'] = self.available
        if self.capacity is not None:
            result['Capacity'] = self.capacity
        if self.fs_name is not None:
            result['FsName'] = self.fs_name
        if self.usage is not None:
            result['Usage'] = self.usage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Available') is not None:
            self.available = m.get('Available')
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')
        if m.get('FsName') is not None:
            self.fs_name = m.get('FsName')
        if m.get('Usage') is not None:
            self.usage = m.get('Usage')
        return self


class DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecordsMemory(TeaModel):
    def __init__(
        self,
        available_bytes: int = None,
        cache: int = None,
        rss: int = None,
        usage_bytes: int = None,
        working_set: int = None,
    ):
        # The size of the available memory. Unit: bytes.
        self.available_bytes = available_bytes
        # The size of the cache. Unit: bytes.
        self.cache = cache
        # The size of the resident memory set, which indicates the size of the physical memory that is actually used. Unit: bytes.
        self.rss = rss
        # The size of the used memory. Unit: bytes.
        self.usage_bytes = usage_bytes
        # The usage of the working set. Unit: bytes.
        self.working_set = working_set

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.available_bytes is not None:
            result['AvailableBytes'] = self.available_bytes
        if self.cache is not None:
            result['Cache'] = self.cache
        if self.rss is not None:
            result['Rss'] = self.rss
        if self.usage_bytes is not None:
            result['UsageBytes'] = self.usage_bytes
        if self.working_set is not None:
            result['WorkingSet'] = self.working_set
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableBytes') is not None:
            self.available_bytes = m.get('AvailableBytes')
        if m.get('Cache') is not None:
            self.cache = m.get('Cache')
        if m.get('Rss') is not None:
            self.rss = m.get('Rss')
        if m.get('UsageBytes') is not None:
            self.usage_bytes = m.get('UsageBytes')
        if m.get('WorkingSet') is not None:
            self.working_set = m.get('WorkingSet')
        return self


class DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecordsNetworkInterfaces(TeaModel):
    def __init__(
        self,
        name: str = None,
        rx_bytes: int = None,
        rx_drops: int = None,
        rx_errors: int = None,
        rx_packets: int = None,
        tx_bytes: int = None,
        tx_drops: int = None,
        tx_errors: int = None,
        tx_packets: int = None,
    ):
        # The name of the NIC.
        self.name = name
        # The total number of bytes received.
        self.rx_bytes = rx_bytes
        # The number of packets that fail to be received.
        self.rx_drops = rx_drops
        # The number of receipt errors.
        self.rx_errors = rx_errors
        # The total number of packets received.
        self.rx_packets = rx_packets
        # The total number of bytes sent.
        self.tx_bytes = tx_bytes
        # The number of packets that fail to arrive at their destination.
        self.tx_drops = tx_drops
        # The total number of sending errors.
        self.tx_errors = tx_errors
        # The total number of packets sent.
        self.tx_packets = tx_packets

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.rx_bytes is not None:
            result['RxBytes'] = self.rx_bytes
        if self.rx_drops is not None:
            result['RxDrops'] = self.rx_drops
        if self.rx_errors is not None:
            result['RxErrors'] = self.rx_errors
        if self.rx_packets is not None:
            result['RxPackets'] = self.rx_packets
        if self.tx_bytes is not None:
            result['TxBytes'] = self.tx_bytes
        if self.tx_drops is not None:
            result['TxDrops'] = self.tx_drops
        if self.tx_errors is not None:
            result['TxErrors'] = self.tx_errors
        if self.tx_packets is not None:
            result['TxPackets'] = self.tx_packets
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RxBytes') is not None:
            self.rx_bytes = m.get('RxBytes')
        if m.get('RxDrops') is not None:
            self.rx_drops = m.get('RxDrops')
        if m.get('RxErrors') is not None:
            self.rx_errors = m.get('RxErrors')
        if m.get('RxPackets') is not None:
            self.rx_packets = m.get('RxPackets')
        if m.get('TxBytes') is not None:
            self.tx_bytes = m.get('TxBytes')
        if m.get('TxDrops') is not None:
            self.tx_drops = m.get('TxDrops')
        if m.get('TxErrors') is not None:
            self.tx_errors = m.get('TxErrors')
        if m.get('TxPackets') is not None:
            self.tx_packets = m.get('TxPackets')
        return self


class DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecordsNetwork(TeaModel):
    def __init__(
        self,
        interfaces: List[DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecordsNetworkInterfaces] = None,
    ):
        # The monitoring data of network interface controllers (NICs).
        self.interfaces = interfaces

    def validate(self):
        if self.interfaces:
            for k in self.interfaces:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Interfaces'] = []
        if self.interfaces is not None:
            for k in self.interfaces:
                result['Interfaces'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.interfaces = []
        if m.get('Interfaces') is not None:
            for k in m.get('Interfaces'):
                temp_model = DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecordsNetworkInterfaces()
                self.interfaces.append(temp_model.from_map(k))
        return self


class DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecords(TeaModel):
    def __init__(
        self,
        cpu: DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecordsCPU = None,
        containers: List[DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecordsContainers] = None,
        disk: List[DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecordsDisk] = None,
        filesystem: List[DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecordsFilesystem] = None,
        memory: DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecordsMemory = None,
        network: DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecordsNetwork = None,
        timestamp: str = None,
    ):
        # The monitoring data of vCPUs.
        self.cpu = cpu
        # The monitoring data of containers.
        self.containers = containers
        # The monitoring data of disks.
        self.disk = disk
        # The monitoring data of file system partitions.
        self.filesystem = filesystem
        # The monitoring data of the memory.
        self.memory = memory
        # The monitoring data of the network.
        self.network = network
        # The time when the entry of monitoring data was collected. The time follows the RFC 3339 format.
        self.timestamp = timestamp

    def validate(self):
        if self.cpu:
            self.cpu.validate()
        if self.containers:
            for k in self.containers:
                if k:
                    k.validate()
        if self.disk:
            for k in self.disk:
                if k:
                    k.validate()
        if self.filesystem:
            for k in self.filesystem:
                if k:
                    k.validate()
        if self.memory:
            self.memory.validate()
        if self.network:
            self.network.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['CPU'] = self.cpu.to_map()
        result['Containers'] = []
        if self.containers is not None:
            for k in self.containers:
                result['Containers'].append(k.to_map() if k else None)
        result['Disk'] = []
        if self.disk is not None:
            for k in self.disk:
                result['Disk'].append(k.to_map() if k else None)
        result['Filesystem'] = []
        if self.filesystem is not None:
            for k in self.filesystem:
                result['Filesystem'].append(k.to_map() if k else None)
        if self.memory is not None:
            result['Memory'] = self.memory.to_map()
        if self.network is not None:
            result['Network'] = self.network.to_map()
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CPU') is not None:
            temp_model = DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecordsCPU()
            self.cpu = temp_model.from_map(m['CPU'])
        self.containers = []
        if m.get('Containers') is not None:
            for k in m.get('Containers'):
                temp_model = DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecordsContainers()
                self.containers.append(temp_model.from_map(k))
        self.disk = []
        if m.get('Disk') is not None:
            for k in m.get('Disk'):
                temp_model = DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecordsDisk()
                self.disk.append(temp_model.from_map(k))
        self.filesystem = []
        if m.get('Filesystem') is not None:
            for k in m.get('Filesystem'):
                temp_model = DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecordsFilesystem()
                self.filesystem.append(temp_model.from_map(k))
        if m.get('Memory') is not None:
            temp_model = DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecordsMemory()
            self.memory = temp_model.from_map(m['Memory'])
        if m.get('Network') is not None:
            temp_model = DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecordsNetwork()
            self.network = temp_model.from_map(m['Network'])
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class DescribeMultiContainerGroupMetricResponseBodyMonitorDatas(TeaModel):
    def __init__(
        self,
        container_group_id: str = None,
        records: List[DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecords] = None,
    ):
        # The ID of the elastic container instance.
        self.container_group_id = container_group_id
        # The details about monitoring data.
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
        if self.container_group_id is not None:
            result['ContainerGroupId'] = self.container_group_id
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContainerGroupId') is not None:
            self.container_group_id = m.get('ContainerGroupId')
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecords()
                self.records.append(temp_model.from_map(k))
        return self


class DescribeMultiContainerGroupMetricResponseBody(TeaModel):
    def __init__(
        self,
        monitor_datas: List[DescribeMultiContainerGroupMetricResponseBodyMonitorDatas] = None,
        request_id: str = None,
    ):
        # The monitoring data of the elastic container instances.
        self.monitor_datas = monitor_datas
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.monitor_datas:
            for k in self.monitor_datas:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MonitorDatas'] = []
        if self.monitor_datas is not None:
            for k in self.monitor_datas:
                result['MonitorDatas'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.monitor_datas = []
        if m.get('MonitorDatas') is not None:
            for k in m.get('MonitorDatas'):
                temp_model = DescribeMultiContainerGroupMetricResponseBodyMonitorDatas()
                self.monitor_datas.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeMultiContainerGroupMetricResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeMultiContainerGroupMetricResponseBody = None,
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
            temp_model = DescribeMultiContainerGroupMetricResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID.
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


class DescribeRegionsResponseBodyRegions(TeaModel):
    def __init__(
        self,
        recommend_zones: List[str] = None,
        region_endpoint: str = None,
        region_id: str = None,
        zones: List[str] = None,
    ):
        # The recommended zones. Recommended zones are zones that have relatively sufficient resources in the current region.
        self.recommend_zones = recommend_zones
        # The endpoint for the region.
        self.region_endpoint = region_endpoint
        # The region ID.
        self.region_id = region_id
        # The queried zones.
        self.zones = zones

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.recommend_zones is not None:
            result['RecommendZones'] = self.recommend_zones
        if self.region_endpoint is not None:
            result['RegionEndpoint'] = self.region_endpoint
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.zones is not None:
            result['Zones'] = self.zones
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RecommendZones') is not None:
            self.recommend_zones = m.get('RecommendZones')
        if m.get('RegionEndpoint') is not None:
            self.region_endpoint = m.get('RegionEndpoint')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Zones') is not None:
            self.zones = m.get('Zones')
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(
        self,
        regions: List[DescribeRegionsResponseBodyRegions] = None,
        request_id: str = None,
    ):
        # The queried regions.
        self.regions = regions
        # The request ID.
        self.request_id = request_id

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
        result['Regions'] = []
        if self.regions is not None:
            for k in self.regions:
                result['Regions'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.regions = []
        if m.get('Regions') is not None:
            for k in m.get('Regions'):
                temp_model = DescribeRegionsResponseBodyRegions()
                self.regions.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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


class DescribeVirtualNodesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N.
        self.key = key
        # The value of tag N.
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


class DescribeVirtualNodesRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        limit: int = None,
        next_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        status: str = None,
        tag: List[DescribeVirtualNodesRequestTag] = None,
        virtual_node_ids: str = None,
        virtual_node_name: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotency of requests?](https://help.aliyun.com/document_detail/25693.html)
        self.client_token = client_token
        # The maximum number of resources that are allowed to return for this request. Default value: 20. Maximum value: 20.
        # 
        # >  The number of returned resources is less than or equal to the specified number.
        self.limit = limit
        # The token that determines the start point of the next query. If this parameter is empty, all results have been returned.
        # 
        # You do not need to specify this parameter in the first request. From the second request, you can obtain the token from the result returned by the previous request.
        self.next_token = next_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the virtual nodes.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The status of the virtual node. Valid values:
        # 
        # *   Pending
        # *   Ready
        # *   Failed
        self.status = status
        # The tags that are bound to the virtual node.
        self.tag = tag
        # The IDs of the virtual nodes. You can specify up to 20 IDs. Each ID must be a string in the JSON format.
        self.virtual_node_ids = virtual_node_ids
        # The names of the virtual nodes.
        self.virtual_node_name = virtual_node_name

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
        if self.limit is not None:
            result['Limit'] = self.limit
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
        if self.status is not None:
            result['Status'] = self.status
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.virtual_node_ids is not None:
            result['VirtualNodeIds'] = self.virtual_node_ids
        if self.virtual_node_name is not None:
            result['VirtualNodeName'] = self.virtual_node_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
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
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeVirtualNodesRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('VirtualNodeIds') is not None:
            self.virtual_node_ids = m.get('VirtualNodeIds')
        if m.get('VirtualNodeName') is not None:
            self.virtual_node_name = m.get('VirtualNodeName')
        return self


class DescribeVirtualNodesResponseBodyVirtualNodesEvents(TeaModel):
    def __init__(
        self,
        count: int = None,
        first_timestamp: str = None,
        last_timestamp: str = None,
        message: str = None,
        name: str = None,
        reason: str = None,
        type: str = None,
    ):
        # The number of events.
        self.count = count
        # The time when the event started.
        self.first_timestamp = first_timestamp
        # The time when the event ended.
        self.last_timestamp = last_timestamp
        # The message of the event.
        self.message = message
        # The name of the object to which the event belongs.
        self.name = name
        # The name of the event.
        self.reason = reason
        # The type of the event. Valid values:
        # 
        # *   Normal
        # *   Warning
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.first_timestamp is not None:
            result['FirstTimestamp'] = self.first_timestamp
        if self.last_timestamp is not None:
            result['LastTimestamp'] = self.last_timestamp
        if self.message is not None:
            result['Message'] = self.message
        if self.name is not None:
            result['Name'] = self.name
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('FirstTimestamp') is not None:
            self.first_timestamp = m.get('FirstTimestamp')
        if m.get('LastTimestamp') is not None:
            self.last_timestamp = m.get('LastTimestamp')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeVirtualNodesResponseBodyVirtualNodesTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag.
        self.key = key
        # The value of the tag.
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


class DescribeVirtualNodesResponseBodyVirtualNodes(TeaModel):
    def __init__(
        self,
        creation_time: str = None,
        events: List[DescribeVirtualNodesResponseBodyVirtualNodesEvents] = None,
        internet_ip: str = None,
        intranet_ip: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        status: str = None,
        tags: List[DescribeVirtualNodesResponseBodyVirtualNodesTags] = None,
        virtual_node_id: str = None,
        virtual_node_name: str = None,
        virtual_node_security_group_id: str = None,
        virtual_node_vswitch_id: str = None,
        vpc_id: str = None,
    ):
        # The time when the virtual node was created. The time follows the RFC 3339 standard and is displayed in UTC.
        self.creation_time = creation_time
        # The events about the virtual node.
        self.events = events
        # The public IP address of the virtual node.
        self.internet_ip = internet_ip
        # The private IP address of the virtual node.
        self.intranet_ip = intranet_ip
        # The ID of the region in which the virtual node resides.
        self.region_id = region_id
        # The ID of the resource group to which the virtual node belongs.
        self.resource_group_id = resource_group_id
        # The status of the virtual node. Valid values:
        # 
        # *   Pending
        # *   Ready
        # *   Failed
        self.status = status
        # The tags that are bound to the virtual node.
        self.tags = tags
        # The ID of the virtual node.
        self.virtual_node_id = virtual_node_id
        # The name of the virtual node.
        self.virtual_node_name = virtual_node_name
        # The ID of the security group to which the virtual node belongs.
        self.virtual_node_security_group_id = virtual_node_security_group_id
        # The ID of the vSwitch with which the virtual node is associated.
        self.virtual_node_vswitch_id = virtual_node_vswitch_id
        # The ID of the VPC to which the virtual node belongs.
        self.vpc_id = vpc_id

    def validate(self):
        if self.events:
            for k in self.events:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        result['Events'] = []
        if self.events is not None:
            for k in self.events:
                result['Events'].append(k.to_map() if k else None)
        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip
        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip
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
        if self.virtual_node_id is not None:
            result['VirtualNodeId'] = self.virtual_node_id
        if self.virtual_node_name is not None:
            result['VirtualNodeName'] = self.virtual_node_name
        if self.virtual_node_security_group_id is not None:
            result['VirtualNodeSecurityGroupId'] = self.virtual_node_security_group_id
        if self.virtual_node_vswitch_id is not None:
            result['VirtualNodeVSwitchId'] = self.virtual_node_vswitch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        self.events = []
        if m.get('Events') is not None:
            for k in m.get('Events'):
                temp_model = DescribeVirtualNodesResponseBodyVirtualNodesEvents()
                self.events.append(temp_model.from_map(k))
        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')
        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = DescribeVirtualNodesResponseBodyVirtualNodesTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('VirtualNodeId') is not None:
            self.virtual_node_id = m.get('VirtualNodeId')
        if m.get('VirtualNodeName') is not None:
            self.virtual_node_name = m.get('VirtualNodeName')
        if m.get('VirtualNodeSecurityGroupId') is not None:
            self.virtual_node_security_group_id = m.get('VirtualNodeSecurityGroupId')
        if m.get('VirtualNodeVSwitchId') is not None:
            self.virtual_node_vswitch_id = m.get('VirtualNodeVSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class DescribeVirtualNodesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
        virtual_nodes: List[DescribeVirtualNodesResponseBodyVirtualNodes] = None,
    ):
        # The token that determines the start point of the next query.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The number of virtual nodes that were queried.
        self.total_count = total_count
        # The virtual nodes that were queried.
        self.virtual_nodes = virtual_nodes

    def validate(self):
        if self.virtual_nodes:
            for k in self.virtual_nodes:
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
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['VirtualNodes'] = []
        if self.virtual_nodes is not None:
            for k in self.virtual_nodes:
                result['VirtualNodes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.virtual_nodes = []
        if m.get('VirtualNodes') is not None:
            for k in m.get('VirtualNodes'):
                temp_model = DescribeVirtualNodesResponseBodyVirtualNodes()
                self.virtual_nodes.append(temp_model.from_map(k))
        return self


class DescribeVirtualNodesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeVirtualNodesResponseBody = None,
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
            temp_model = DescribeVirtualNodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExecContainerCommandRequest(TeaModel):
    def __init__(
        self,
        command: str = None,
        container_group_id: str = None,
        container_name: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        stdin: bool = None,
        sync: bool = None,
        tty: bool = None,
    ):
        # The commands to run in the container. You can specify up to 20 commands. Each command can be up to 256 characters in length.\\
        # The strings must be in the JSON format. Example: `["/bin/sh", "-c", "ls -a"]`.
        # 
        # This parameter is required.
        self.command = command
        # The ID of the elastic container instance.
        # 
        # This parameter is required.
        self.container_group_id = container_group_id
        # The name of the container.
        # 
        # This parameter is required.
        self.container_name = container_name
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Specifies whether to read the commands from standard input (stdin). Default value: true.
        self.stdin = stdin
        # Specifies whether to immediately run the command and synchronously return the result. Default value: false.\\
        # If this parameter is set to true, TTY must be set to false. Command cannot be set to `/bin/bash`.
        self.sync = sync
        # Specifies whether to enable interaction. Default value: false.\\
        # If the Command parameter is set to `/bin/bash`, set this parameter to true.
        self.tty = tty

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.command is not None:
            result['Command'] = self.command
        if self.container_group_id is not None:
            result['ContainerGroupId'] = self.container_group_id
        if self.container_name is not None:
            result['ContainerName'] = self.container_name
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
        if self.stdin is not None:
            result['Stdin'] = self.stdin
        if self.sync is not None:
            result['Sync'] = self.sync
        if self.tty is not None:
            result['TTY'] = self.tty
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Command') is not None:
            self.command = m.get('Command')
        if m.get('ContainerGroupId') is not None:
            self.container_group_id = m.get('ContainerGroupId')
        if m.get('ContainerName') is not None:
            self.container_name = m.get('ContainerName')
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
        if m.get('Stdin') is not None:
            self.stdin = m.get('Stdin')
        if m.get('Sync') is not None:
            self.sync = m.get('Sync')
        if m.get('TTY') is not None:
            self.tty = m.get('TTY')
        return self


class ExecContainerCommandResponseBody(TeaModel):
    def __init__(
        self,
        http_url: str = None,
        request_id: str = None,
        sync_response: str = None,
        web_socket_uri: str = None,
    ):
        # The HTTP URL. You can use this URL to enter the container within 30 seconds after this operation is called. For more information, see [Use and integrate the Elastic Container Instance terminal](https://help.aliyun.com/document_detail/202846.html).
        self.http_url = http_url
        # The request ID.
        self.request_id = request_id
        # The output of the command. This parameter is returned only if Sync is set to true.
        self.sync_response = sync_response
        # The WebSocket URL. You can use this URL to establish a WebSocket connection with the container.
        self.web_socket_uri = web_socket_uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_url is not None:
            result['HttpUrl'] = self.http_url
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sync_response is not None:
            result['SyncResponse'] = self.sync_response
        if self.web_socket_uri is not None:
            result['WebSocketUri'] = self.web_socket_uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpUrl') is not None:
            self.http_url = m.get('HttpUrl')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SyncResponse') is not None:
            self.sync_response = m.get('SyncResponse')
        if m.get('WebSocketUri') is not None:
            self.web_socket_uri = m.get('WebSocketUri')
        return self


class ExecContainerCommandResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExecContainerCommandResponseBody = None,
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
            temp_model = ExecContainerCommandResponseBody()
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
        limit: str = None,
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
        self.limit = limit
        self.next_token = next_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        # This parameter is required.
        self.region_id = region_id
        self.resource_id = resource_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
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
        if self.limit is not None:
            result['Limit'] = self.limit
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
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
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


class ListTagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        tag_resources: List[ListTagResourcesResponseBodyTagResources] = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
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


class ListUsageRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID.
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


class ListUsageResponseBody(TeaModel):
    def __init__(
        self,
        attributes: Dict[str, Any] = None,
        request_id: str = None,
    ):
        # The information about the used amounts and upper limits of privileges and quotas that you have in the specified region. The information contains the following items:
        # 
        # *   UsedCpu: the number of existing vCPUs.
        # *   MaxCpu: the upper limit of vCPUs.
        # *   MaxImageCacheCount: the upper limit of manually created image caches.
        # *   UsedImageCacheCount: the number of existing image caches that are manually created.
        # *   MaxAutoImageCacheCount: the upper limit of automatically created image caches.
        # *   UsedAutoImageCacheCount: the number of existing image caches that are automatically created.
        # *   MaxDataCacheCount: the upper limit of DataCaches.
        # *   UsedDataCacheCount: the number of existing DataCaches.
        self.attributes = attributes
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListUsageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListUsageResponseBody = None,
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
            temp_model = ListUsageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResizeContainerGroupVolumeRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        container_group_id: str = None,
        new_size: int = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        volume_name: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The ID of the elastic container instance.
        # 
        # This parameter is required.
        self.container_group_id = container_group_id
        # The size of the volume after the volume is scaled up. Unit: GiB. Valid values:
        # 
        # *   Ultra disk (cloud_efficiency): 20 to 32768
        # *   Standard SSD (cloud_ssd): 20 to 32768
        # *   Enhanced SSD (cloud_essd): 20 to 32768
        # *   Basic disk (cloud): 5 to 2000
        # 
        # >  The capacity of the volume after the volume is scaled up must be greater than the original capacity of the volume. If the new capacity is equal to the original capacity of the volume, only the file system is scaled up.
        # 
        # This parameter is required.
        self.new_size = new_size
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The name of the volume that you want to scale up. The volume must be an Alibaba Cloud disk.
        # 
        # This parameter is required.
        self.volume_name = volume_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.container_group_id is not None:
            result['ContainerGroupId'] = self.container_group_id
        if self.new_size is not None:
            result['NewSize'] = self.new_size
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
        if self.volume_name is not None:
            result['VolumeName'] = self.volume_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ContainerGroupId') is not None:
            self.container_group_id = m.get('ContainerGroupId')
        if m.get('NewSize') is not None:
            self.new_size = m.get('NewSize')
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
        if m.get('VolumeName') is not None:
            self.volume_name = m.get('VolumeName')
        return self


class ResizeContainerGroupVolumeResponseBody(TeaModel):
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


class ResizeContainerGroupVolumeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ResizeContainerGroupVolumeResponseBody = None,
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
            temp_model = ResizeContainerGroupVolumeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RestartContainerGroupRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        container_group_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure the idempotence of a request?](https://help.aliyun.com/document_detail/25693.html)
        self.client_token = client_token
        # The instance ID.
        # 
        # This parameter is required.
        self.container_group_id = container_group_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the instance.
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
        if self.container_group_id is not None:
            result['ContainerGroupId'] = self.container_group_id
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
        if m.get('ContainerGroupId') is not None:
            self.container_group_id = m.get('ContainerGroupId')
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


class RestartContainerGroupResponseBody(TeaModel):
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


class RestartContainerGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RestartContainerGroupResponseBody = None,
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
            temp_model = RestartContainerGroupResponseBody()
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
        # This parameter is required.
        self.region_id = region_id
        # This parameter is required.
        self.resource_id = resource_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # This parameter is required.
        self.resource_type = resource_type
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
        client_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_id: List[str] = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        resource_type: str = None,
        tag_key: List[str] = None,
    ):
        self.all = all
        self.client_token = client_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        # This parameter is required.
        self.region_id = region_id
        # This parameter is required.
        self.resource_id = resource_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
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
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
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
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
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


class UpdateContainerGroupRequestDnsConfigOption(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The option name of DNS configurations.
        self.name = name
        # The option value of DNS configurations.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateContainerGroupRequestDnsConfig(TeaModel):
    def __init__(
        self,
        name_server: List[str] = None,
        option: List[UpdateContainerGroupRequestDnsConfigOption] = None,
        search: List[str] = None,
    ):
        # The IP addresses of DNS servers.
        self.name_server = name_server
        # The configurations of DNS.
        self.option = option
        # The search domains of the Domain Name System (DNS) server.
        self.search = search

    def validate(self):
        if self.option:
            for k in self.option:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name_server is not None:
            result['NameServer'] = self.name_server
        result['Option'] = []
        if self.option is not None:
            for k in self.option:
                result['Option'].append(k.to_map() if k else None)
        if self.search is not None:
            result['Search'] = self.search
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NameServer') is not None:
            self.name_server = m.get('NameServer')
        self.option = []
        if m.get('Option') is not None:
            for k in m.get('Option'):
                temp_model = UpdateContainerGroupRequestDnsConfigOption()
                self.option.append(temp_model.from_map(k))
        if m.get('Search') is not None:
            self.search = m.get('Search')
        return self


class UpdateContainerGroupRequestAcrRegistryInfo(TeaModel):
    def __init__(
        self,
        domain: List[str] = None,
        instance_id: str = None,
        instance_name: str = None,
        region_id: str = None,
    ):
        # The domain names of the Container Registry Enterprise Edition instance. By default, all domain names of the instance are displayed. You can specify specific domain names. Separate multiple domain names with commas (,).
        self.domain = domain
        # The ID of the Container Registry Enterprise Edition instance.
        self.instance_id = instance_id
        # The name of the Container Registry Enterprise Edition instance.
        self.instance_name = instance_name
        # The ID of the region where the Container Registry Enterprise Edition instance resides.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateContainerGroupRequestContainerLivenessProbeExec(TeaModel):
    def __init__(
        self,
        command: List[str] = None,
    ):
        self.command = command

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.command is not None:
            result['Command'] = self.command
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Command') is not None:
            self.command = m.get('Command')
        return self


class UpdateContainerGroupRequestContainerLivenessProbeHttpGet(TeaModel):
    def __init__(
        self,
        path: str = None,
        port: int = None,
        scheme: str = None,
    ):
        self.path = path
        self.port = port
        self.scheme = scheme

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.path is not None:
            result['Path'] = self.path
        if self.port is not None:
            result['Port'] = self.port
        if self.scheme is not None:
            result['Scheme'] = self.scheme
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Scheme') is not None:
            self.scheme = m.get('Scheme')
        return self


class UpdateContainerGroupRequestContainerLivenessProbeTcpSocket(TeaModel):
    def __init__(
        self,
        port: int = None,
    ):
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class UpdateContainerGroupRequestContainerLivenessProbe(TeaModel):
    def __init__(
        self,
        exec: UpdateContainerGroupRequestContainerLivenessProbeExec = None,
        failure_threshold: int = None,
        http_get: UpdateContainerGroupRequestContainerLivenessProbeHttpGet = None,
        initial_delay_seconds: int = None,
        period_seconds: int = None,
        success_threshold: int = None,
        tcp_socket: UpdateContainerGroupRequestContainerLivenessProbeTcpSocket = None,
        timeout_seconds: int = None,
    ):
        self.exec = exec
        self.failure_threshold = failure_threshold
        self.http_get = http_get
        self.initial_delay_seconds = initial_delay_seconds
        self.period_seconds = period_seconds
        self.success_threshold = success_threshold
        self.tcp_socket = tcp_socket
        self.timeout_seconds = timeout_seconds

    def validate(self):
        if self.exec:
            self.exec.validate()
        if self.http_get:
            self.http_get.validate()
        if self.tcp_socket:
            self.tcp_socket.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exec is not None:
            result['Exec'] = self.exec.to_map()
        if self.failure_threshold is not None:
            result['FailureThreshold'] = self.failure_threshold
        if self.http_get is not None:
            result['HttpGet'] = self.http_get.to_map()
        if self.initial_delay_seconds is not None:
            result['InitialDelaySeconds'] = self.initial_delay_seconds
        if self.period_seconds is not None:
            result['PeriodSeconds'] = self.period_seconds
        if self.success_threshold is not None:
            result['SuccessThreshold'] = self.success_threshold
        if self.tcp_socket is not None:
            result['TcpSocket'] = self.tcp_socket.to_map()
        if self.timeout_seconds is not None:
            result['TimeoutSeconds'] = self.timeout_seconds
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Exec') is not None:
            temp_model = UpdateContainerGroupRequestContainerLivenessProbeExec()
            self.exec = temp_model.from_map(m['Exec'])
        if m.get('FailureThreshold') is not None:
            self.failure_threshold = m.get('FailureThreshold')
        if m.get('HttpGet') is not None:
            temp_model = UpdateContainerGroupRequestContainerLivenessProbeHttpGet()
            self.http_get = temp_model.from_map(m['HttpGet'])
        if m.get('InitialDelaySeconds') is not None:
            self.initial_delay_seconds = m.get('InitialDelaySeconds')
        if m.get('PeriodSeconds') is not None:
            self.period_seconds = m.get('PeriodSeconds')
        if m.get('SuccessThreshold') is not None:
            self.success_threshold = m.get('SuccessThreshold')
        if m.get('TcpSocket') is not None:
            temp_model = UpdateContainerGroupRequestContainerLivenessProbeTcpSocket()
            self.tcp_socket = temp_model.from_map(m['TcpSocket'])
        if m.get('TimeoutSeconds') is not None:
            self.timeout_seconds = m.get('TimeoutSeconds')
        return self


class UpdateContainerGroupRequestContainerReadinessProbeExec(TeaModel):
    def __init__(
        self,
        command: List[str] = None,
    ):
        self.command = command

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.command is not None:
            result['Command'] = self.command
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Command') is not None:
            self.command = m.get('Command')
        return self


class UpdateContainerGroupRequestContainerReadinessProbeHttpGet(TeaModel):
    def __init__(
        self,
        path: str = None,
        port: int = None,
        scheme: str = None,
    ):
        self.path = path
        self.port = port
        self.scheme = scheme

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.path is not None:
            result['Path'] = self.path
        if self.port is not None:
            result['Port'] = self.port
        if self.scheme is not None:
            result['Scheme'] = self.scheme
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Scheme') is not None:
            self.scheme = m.get('Scheme')
        return self


class UpdateContainerGroupRequestContainerReadinessProbeTcpSocket(TeaModel):
    def __init__(
        self,
        port: int = None,
    ):
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class UpdateContainerGroupRequestContainerReadinessProbe(TeaModel):
    def __init__(
        self,
        exec: UpdateContainerGroupRequestContainerReadinessProbeExec = None,
        failure_threshold: int = None,
        http_get: UpdateContainerGroupRequestContainerReadinessProbeHttpGet = None,
        initial_delay_seconds: int = None,
        period_seconds: int = None,
        success_threshold: int = None,
        tcp_socket: UpdateContainerGroupRequestContainerReadinessProbeTcpSocket = None,
        timeout_seconds: int = None,
    ):
        self.exec = exec
        self.failure_threshold = failure_threshold
        self.http_get = http_get
        self.initial_delay_seconds = initial_delay_seconds
        self.period_seconds = period_seconds
        self.success_threshold = success_threshold
        self.tcp_socket = tcp_socket
        self.timeout_seconds = timeout_seconds

    def validate(self):
        if self.exec:
            self.exec.validate()
        if self.http_get:
            self.http_get.validate()
        if self.tcp_socket:
            self.tcp_socket.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exec is not None:
            result['Exec'] = self.exec.to_map()
        if self.failure_threshold is not None:
            result['FailureThreshold'] = self.failure_threshold
        if self.http_get is not None:
            result['HttpGet'] = self.http_get.to_map()
        if self.initial_delay_seconds is not None:
            result['InitialDelaySeconds'] = self.initial_delay_seconds
        if self.period_seconds is not None:
            result['PeriodSeconds'] = self.period_seconds
        if self.success_threshold is not None:
            result['SuccessThreshold'] = self.success_threshold
        if self.tcp_socket is not None:
            result['TcpSocket'] = self.tcp_socket.to_map()
        if self.timeout_seconds is not None:
            result['TimeoutSeconds'] = self.timeout_seconds
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Exec') is not None:
            temp_model = UpdateContainerGroupRequestContainerReadinessProbeExec()
            self.exec = temp_model.from_map(m['Exec'])
        if m.get('FailureThreshold') is not None:
            self.failure_threshold = m.get('FailureThreshold')
        if m.get('HttpGet') is not None:
            temp_model = UpdateContainerGroupRequestContainerReadinessProbeHttpGet()
            self.http_get = temp_model.from_map(m['HttpGet'])
        if m.get('InitialDelaySeconds') is not None:
            self.initial_delay_seconds = m.get('InitialDelaySeconds')
        if m.get('PeriodSeconds') is not None:
            self.period_seconds = m.get('PeriodSeconds')
        if m.get('SuccessThreshold') is not None:
            self.success_threshold = m.get('SuccessThreshold')
        if m.get('TcpSocket') is not None:
            temp_model = UpdateContainerGroupRequestContainerReadinessProbeTcpSocket()
            self.tcp_socket = temp_model.from_map(m['TcpSocket'])
        if m.get('TimeoutSeconds') is not None:
            self.timeout_seconds = m.get('TimeoutSeconds')
        return self


class UpdateContainerGroupRequestContainerSecurityContextCapability(TeaModel):
    def __init__(
        self,
        add: List[str] = None,
    ):
        self.add = add

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.add is not None:
            result['Add'] = self.add
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Add') is not None:
            self.add = m.get('Add')
        return self


class UpdateContainerGroupRequestContainerSecurityContext(TeaModel):
    def __init__(
        self,
        capability: UpdateContainerGroupRequestContainerSecurityContextCapability = None,
        read_only_root_filesystem: bool = None,
        run_as_user: int = None,
    ):
        self.capability = capability
        self.read_only_root_filesystem = read_only_root_filesystem
        self.run_as_user = run_as_user

    def validate(self):
        if self.capability:
            self.capability.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.capability is not None:
            result['Capability'] = self.capability.to_map()
        if self.read_only_root_filesystem is not None:
            result['ReadOnlyRootFilesystem'] = self.read_only_root_filesystem
        if self.run_as_user is not None:
            result['RunAsUser'] = self.run_as_user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Capability') is not None:
            temp_model = UpdateContainerGroupRequestContainerSecurityContextCapability()
            self.capability = temp_model.from_map(m['Capability'])
        if m.get('ReadOnlyRootFilesystem') is not None:
            self.read_only_root_filesystem = m.get('ReadOnlyRootFilesystem')
        if m.get('RunAsUser') is not None:
            self.run_as_user = m.get('RunAsUser')
        return self


class UpdateContainerGroupRequestContainerEnvironmentVarFieldRef(TeaModel):
    def __init__(
        self,
        field_path: str = None,
    ):
        self.field_path = field_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_path is not None:
            result['FieldPath'] = self.field_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldPath') is not None:
            self.field_path = m.get('FieldPath')
        return self


class UpdateContainerGroupRequestContainerEnvironmentVar(TeaModel):
    def __init__(
        self,
        field_ref: UpdateContainerGroupRequestContainerEnvironmentVarFieldRef = None,
        key: str = None,
        value: str = None,
    ):
        self.field_ref = field_ref
        # The name of the environment variable for the container.
        self.key = key
        # The value of the environment variable for the container.
        self.value = value

    def validate(self):
        if self.field_ref:
            self.field_ref.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_ref is not None:
            result['FieldRef'] = self.field_ref.to_map()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldRef') is not None:
            temp_model = UpdateContainerGroupRequestContainerEnvironmentVarFieldRef()
            self.field_ref = temp_model.from_map(m['FieldRef'])
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateContainerGroupRequestContainerLifecyclePostStartHandlerHttpGetHttpHeaders(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The request parameter of the HTTP GET request when you use an HTTP request to specify the postStart callback function.
        self.name = name
        # The request parameter value of the HTTP GET request when you use an HTTP request to specify the postStart callback function.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateContainerGroupRequestContainerLifecyclePreStopHandlerHttpGetHttpHeader(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The request parameter of the HTTP GET request when you use an HTTP request to specify the preStop callback function.
        self.name = name
        # The request parameter value of the HTTP GET request when you use an HTTP request to specify the preStop callback function.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateContainerGroupRequestContainerPort(TeaModel):
    def __init__(
        self,
        port: int = None,
        protocol: str = None,
    ):
        # The port number. Valid values: 1 to 65535.
        self.port = port
        # The protocol of the container. Valid values: TCP and UDP.
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.port is not None:
            result['Port'] = self.port
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        return self


class UpdateContainerGroupRequestContainerVolumeMount(TeaModel):
    def __init__(
        self,
        mount_path: str = None,
        mount_propagation: str = None,
        name: str = None,
        read_only: bool = None,
        sub_path: str = None,
    ):
        # The directory of the volume that is mounted to the container. The data in this directory is overwritten by the data on the volume. Specify this parameter with caution.
        self.mount_path = mount_path
        # The mount propagation settings of the volume. Mount propagation allows volumes that are mounted on one container to be shared with other containers in the same pod, or even with other pods on the same node. Valid values:
        # 
        # *   None: This volume mount does not receive subsequent mounts that are performed on this volume or subdirectories of this volume.
        # *   HostToCotainer: The volume mount receives subsequent mounts that are performed on this volume or the subdirectories of this volume.
        # *   Bidirectional: The volume mount behaves the same as the HostToContainer mount. The volume mount receives subsequent mounts that are performed on the volume or the subdirectories of the volume. In addition, all volume mounts that are mounted on the container are propagated back to the host and all containers of all pods that use the same volume.
        # 
        # Default value: None.
        self.mount_propagation = mount_propagation
        # The name of the volume that is mounted to the container. Valid values: the values of Volume.N.Name, which are the names of volumes that are mounted to the elastic container instance.
        self.name = name
        # Specifies whether the volume is read-only. Default value: false.
        self.read_only = read_only
        # The subdirectory of the volume that is mounted to the container. You can use this parameter to mount the same volume to different subdirectories of the container.
        self.sub_path = sub_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mount_path is not None:
            result['MountPath'] = self.mount_path
        if self.mount_propagation is not None:
            result['MountPropagation'] = self.mount_propagation
        if self.name is not None:
            result['Name'] = self.name
        if self.read_only is not None:
            result['ReadOnly'] = self.read_only
        if self.sub_path is not None:
            result['SubPath'] = self.sub_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')
        if m.get('MountPropagation') is not None:
            self.mount_propagation = m.get('MountPropagation')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ReadOnly') is not None:
            self.read_only = m.get('ReadOnly')
        if m.get('SubPath') is not None:
            self.sub_path = m.get('SubPath')
        return self


class UpdateContainerGroupRequestContainer(TeaModel):
    def __init__(
        self,
        liveness_probe: UpdateContainerGroupRequestContainerLivenessProbe = None,
        readiness_probe: UpdateContainerGroupRequestContainerReadinessProbe = None,
        security_context: UpdateContainerGroupRequestContainerSecurityContext = None,
        arg: List[str] = None,
        command: List[str] = None,
        cpu: float = None,
        environment_var: List[UpdateContainerGroupRequestContainerEnvironmentVar] = None,
        gpu: int = None,
        image: str = None,
        image_pull_policy: str = None,
        lifecycle_post_start_handler_exec: List[str] = None,
        lifecycle_post_start_handler_http_get_host: str = None,
        lifecycle_post_start_handler_http_get_http_headers: List[UpdateContainerGroupRequestContainerLifecyclePostStartHandlerHttpGetHttpHeaders] = None,
        lifecycle_post_start_handler_http_get_path: str = None,
        lifecycle_post_start_handler_http_get_port: int = None,
        lifecycle_post_start_handler_http_get_scheme: str = None,
        lifecycle_post_start_handler_tcp_socket_host: str = None,
        lifecycle_post_start_handler_tcp_socket_port: int = None,
        lifecycle_pre_stop_handler_exec: List[str] = None,
        lifecycle_pre_stop_handler_http_get_host: str = None,
        lifecycle_pre_stop_handler_http_get_http_header: List[UpdateContainerGroupRequestContainerLifecyclePreStopHandlerHttpGetHttpHeader] = None,
        lifecycle_pre_stop_handler_http_get_path: str = None,
        lifecycle_pre_stop_handler_http_get_port: int = None,
        lifecycle_pre_stop_handler_http_get_scheme: str = None,
        lifecycle_pre_stop_handler_tcp_socket_host: str = None,
        lifecycle_pre_stop_handler_tcp_socket_port: int = None,
        memory: float = None,
        name: str = None,
        port: List[UpdateContainerGroupRequestContainerPort] = None,
        stdin: bool = None,
        stdin_once: bool = None,
        tty: bool = None,
        volume_mount: List[UpdateContainerGroupRequestContainerVolumeMount] = None,
        working_dir: str = None,
    ):
        self.liveness_probe = liveness_probe
        self.readiness_probe = readiness_probe
        self.security_context = security_context
        # The arguments that you want to pass to the startup command of the container. You can specify up to 10 arguments.
        self.arg = arg
        # The commands that you want to run to perform the health check.
        self.command = command
        # The number of vCPUs that you want to allocate to the container
        self.cpu = cpu
        # The environment variables for the container.
        self.environment_var = environment_var
        # The number of GPUs that you want to allocate to the container.
        self.gpu = gpu
        # The image of the container.
        self.image = image
        # The image pulling policy. Valid values:
        # 
        # *   Always: Each time the instance is updated, image pulling is performed.
        # *   IfNotPresent: On-premises images are used first. If no on-premises images are available, image pulling is performed.
        # *   Never: On-premises images are always used. Image pulling is not performed.
        self.image_pull_policy = image_pull_policy
        # The commands to be executed in the container when you use the CLI to specify the postStart callback function.
        self.lifecycle_post_start_handler_exec = lifecycle_post_start_handler_exec
        # The IP address of the host that receives the HTTP GET request when you use an HTTP request to specify the postStart callback function.
        self.lifecycle_post_start_handler_http_get_host = lifecycle_post_start_handler_http_get_host
        # The information about the valid HTTP request headers among the generated HTTP request headers.
        self.lifecycle_post_start_handler_http_get_http_headers = lifecycle_post_start_handler_http_get_http_headers
        # The path to which the system sends an HTTP GET request for a health check when you use an HTTP request to specify the postStart callback function.
        self.lifecycle_post_start_handler_http_get_path = lifecycle_post_start_handler_http_get_path
        # The port to which the system sends the HTTP GET request when you use an HTTP request to specify the postStart callback function.
        self.lifecycle_post_start_handler_http_get_port = lifecycle_post_start_handler_http_get_port
        # The path to which the system sends an HTTP GET request for a health check when you use an HTTP request to specify the postStart callback function.
        self.lifecycle_post_start_handler_http_get_scheme = lifecycle_post_start_handler_http_get_scheme
        # The IP address of the host that receives the TCP socket request when you use a TCP socket request to specify the postStart callback function.
        self.lifecycle_post_start_handler_tcp_socket_host = lifecycle_post_start_handler_tcp_socket_host
        # The port to which the system sends a TCP socket request for a health check when you use TCP sockets to specify the postStart callback function.
        self.lifecycle_post_start_handler_tcp_socket_port = lifecycle_post_start_handler_tcp_socket_port
        # The commands to be executed in the container when you use the CLI to specify the preStop callback function.
        self.lifecycle_pre_stop_handler_exec = lifecycle_pre_stop_handler_exec
        # The IP address of the host that receives the HTTP GET request when you use an HTTP request to specify the preStop callback function.
        self.lifecycle_pre_stop_handler_http_get_host = lifecycle_pre_stop_handler_http_get_host
        # The information about the generated HTTP request header.
        self.lifecycle_pre_stop_handler_http_get_http_header = lifecycle_pre_stop_handler_http_get_http_header
        # The path to which the system sends an HTTP GET request for a health check when you use an HTTP request to specify the preSop callback function.
        self.lifecycle_pre_stop_handler_http_get_path = lifecycle_pre_stop_handler_http_get_path
        # The port to which the system sends the HTTP GET request for a health check when you use an HTTP request to specify the preStop callback function.
        self.lifecycle_pre_stop_handler_http_get_port = lifecycle_pre_stop_handler_http_get_port
        # The protocol type of the HTTP GET request when you use an HTTP request to specify the preStop callback function. Valid values:
        # 
        # *   HTTP
        # *   HTTPS
        self.lifecycle_pre_stop_handler_http_get_scheme = lifecycle_pre_stop_handler_http_get_scheme
        # The IP address of the host that receives the TCP socket request when you use a TCP socket request to specify the preStop callback function.
        self.lifecycle_pre_stop_handler_tcp_socket_host = lifecycle_pre_stop_handler_tcp_socket_host
        # The port to which the system sends a TCP socket request for a health check when you use TCP sockets to specify the preStop callback function.
        self.lifecycle_pre_stop_handler_tcp_socket_port = lifecycle_pre_stop_handler_tcp_socket_port
        # The memory size of the container.
        self.memory = memory
        # The name of the container.
        self.name = name
        # The port to which the system sends an HTTP GET request for a health check.
        self.port = port
        # Specifies whether the container allocates buffer resources to standard input streams when the container is running. If you do not specify this parameter, an end-of-file (EOF) error may occur when standard input streams in the container are read. Default value: false.
        self.stdin = stdin
        # Specifies whether standard input streams are disconnected after a client is disconnected. If Stdin is set to true, standard input streams remain connected among multiple sessions. If StdinOnce is set to true, standard input streams are connected after the container is started, and remain idle until a client is connected to receive data. After the client is disconnected, streams are also disconnected, and remain disconnected until the container restarts.
        self.stdin_once = stdin_once
        # Specifies whether to enable interaction. Default value: false. If the command is a /bin/bash command, set the value to true.
        self.tty = tty
        # Pod volumes that you want to mount into the filesystem of the container.
        self.volume_mount = volume_mount
        # The working directory of the container.
        self.working_dir = working_dir

    def validate(self):
        if self.liveness_probe:
            self.liveness_probe.validate()
        if self.readiness_probe:
            self.readiness_probe.validate()
        if self.security_context:
            self.security_context.validate()
        if self.environment_var:
            for k in self.environment_var:
                if k:
                    k.validate()
        if self.lifecycle_post_start_handler_http_get_http_headers:
            for k in self.lifecycle_post_start_handler_http_get_http_headers:
                if k:
                    k.validate()
        if self.lifecycle_pre_stop_handler_http_get_http_header:
            for k in self.lifecycle_pre_stop_handler_http_get_http_header:
                if k:
                    k.validate()
        if self.port:
            for k in self.port:
                if k:
                    k.validate()
        if self.volume_mount:
            for k in self.volume_mount:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.liveness_probe is not None:
            result['LivenessProbe'] = self.liveness_probe.to_map()
        if self.readiness_probe is not None:
            result['ReadinessProbe'] = self.readiness_probe.to_map()
        if self.security_context is not None:
            result['SecurityContext'] = self.security_context.to_map()
        if self.arg is not None:
            result['Arg'] = self.arg
        if self.command is not None:
            result['Command'] = self.command
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        result['EnvironmentVar'] = []
        if self.environment_var is not None:
            for k in self.environment_var:
                result['EnvironmentVar'].append(k.to_map() if k else None)
        if self.gpu is not None:
            result['Gpu'] = self.gpu
        if self.image is not None:
            result['Image'] = self.image
        if self.image_pull_policy is not None:
            result['ImagePullPolicy'] = self.image_pull_policy
        if self.lifecycle_post_start_handler_exec is not None:
            result['LifecyclePostStartHandlerExec'] = self.lifecycle_post_start_handler_exec
        if self.lifecycle_post_start_handler_http_get_host is not None:
            result['LifecyclePostStartHandlerHttpGetHost'] = self.lifecycle_post_start_handler_http_get_host
        result['LifecyclePostStartHandlerHttpGetHttpHeaders'] = []
        if self.lifecycle_post_start_handler_http_get_http_headers is not None:
            for k in self.lifecycle_post_start_handler_http_get_http_headers:
                result['LifecyclePostStartHandlerHttpGetHttpHeaders'].append(k.to_map() if k else None)
        if self.lifecycle_post_start_handler_http_get_path is not None:
            result['LifecyclePostStartHandlerHttpGetPath'] = self.lifecycle_post_start_handler_http_get_path
        if self.lifecycle_post_start_handler_http_get_port is not None:
            result['LifecyclePostStartHandlerHttpGetPort'] = self.lifecycle_post_start_handler_http_get_port
        if self.lifecycle_post_start_handler_http_get_scheme is not None:
            result['LifecyclePostStartHandlerHttpGetScheme'] = self.lifecycle_post_start_handler_http_get_scheme
        if self.lifecycle_post_start_handler_tcp_socket_host is not None:
            result['LifecyclePostStartHandlerTcpSocketHost'] = self.lifecycle_post_start_handler_tcp_socket_host
        if self.lifecycle_post_start_handler_tcp_socket_port is not None:
            result['LifecyclePostStartHandlerTcpSocketPort'] = self.lifecycle_post_start_handler_tcp_socket_port
        if self.lifecycle_pre_stop_handler_exec is not None:
            result['LifecyclePreStopHandlerExec'] = self.lifecycle_pre_stop_handler_exec
        if self.lifecycle_pre_stop_handler_http_get_host is not None:
            result['LifecyclePreStopHandlerHttpGetHost'] = self.lifecycle_pre_stop_handler_http_get_host
        result['LifecyclePreStopHandlerHttpGetHttpHeader'] = []
        if self.lifecycle_pre_stop_handler_http_get_http_header is not None:
            for k in self.lifecycle_pre_stop_handler_http_get_http_header:
                result['LifecyclePreStopHandlerHttpGetHttpHeader'].append(k.to_map() if k else None)
        if self.lifecycle_pre_stop_handler_http_get_path is not None:
            result['LifecyclePreStopHandlerHttpGetPath'] = self.lifecycle_pre_stop_handler_http_get_path
        if self.lifecycle_pre_stop_handler_http_get_port is not None:
            result['LifecyclePreStopHandlerHttpGetPort'] = self.lifecycle_pre_stop_handler_http_get_port
        if self.lifecycle_pre_stop_handler_http_get_scheme is not None:
            result['LifecyclePreStopHandlerHttpGetScheme'] = self.lifecycle_pre_stop_handler_http_get_scheme
        if self.lifecycle_pre_stop_handler_tcp_socket_host is not None:
            result['LifecyclePreStopHandlerTcpSocketHost'] = self.lifecycle_pre_stop_handler_tcp_socket_host
        if self.lifecycle_pre_stop_handler_tcp_socket_port is not None:
            result['LifecyclePreStopHandlerTcpSocketPort'] = self.lifecycle_pre_stop_handler_tcp_socket_port
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.name is not None:
            result['Name'] = self.name
        result['Port'] = []
        if self.port is not None:
            for k in self.port:
                result['Port'].append(k.to_map() if k else None)
        if self.stdin is not None:
            result['Stdin'] = self.stdin
        if self.stdin_once is not None:
            result['StdinOnce'] = self.stdin_once
        if self.tty is not None:
            result['Tty'] = self.tty
        result['VolumeMount'] = []
        if self.volume_mount is not None:
            for k in self.volume_mount:
                result['VolumeMount'].append(k.to_map() if k else None)
        if self.working_dir is not None:
            result['WorkingDir'] = self.working_dir
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LivenessProbe') is not None:
            temp_model = UpdateContainerGroupRequestContainerLivenessProbe()
            self.liveness_probe = temp_model.from_map(m['LivenessProbe'])
        if m.get('ReadinessProbe') is not None:
            temp_model = UpdateContainerGroupRequestContainerReadinessProbe()
            self.readiness_probe = temp_model.from_map(m['ReadinessProbe'])
        if m.get('SecurityContext') is not None:
            temp_model = UpdateContainerGroupRequestContainerSecurityContext()
            self.security_context = temp_model.from_map(m['SecurityContext'])
        if m.get('Arg') is not None:
            self.arg = m.get('Arg')
        if m.get('Command') is not None:
            self.command = m.get('Command')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        self.environment_var = []
        if m.get('EnvironmentVar') is not None:
            for k in m.get('EnvironmentVar'):
                temp_model = UpdateContainerGroupRequestContainerEnvironmentVar()
                self.environment_var.append(temp_model.from_map(k))
        if m.get('Gpu') is not None:
            self.gpu = m.get('Gpu')
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('ImagePullPolicy') is not None:
            self.image_pull_policy = m.get('ImagePullPolicy')
        if m.get('LifecyclePostStartHandlerExec') is not None:
            self.lifecycle_post_start_handler_exec = m.get('LifecyclePostStartHandlerExec')
        if m.get('LifecyclePostStartHandlerHttpGetHost') is not None:
            self.lifecycle_post_start_handler_http_get_host = m.get('LifecyclePostStartHandlerHttpGetHost')
        self.lifecycle_post_start_handler_http_get_http_headers = []
        if m.get('LifecyclePostStartHandlerHttpGetHttpHeaders') is not None:
            for k in m.get('LifecyclePostStartHandlerHttpGetHttpHeaders'):
                temp_model = UpdateContainerGroupRequestContainerLifecyclePostStartHandlerHttpGetHttpHeaders()
                self.lifecycle_post_start_handler_http_get_http_headers.append(temp_model.from_map(k))
        if m.get('LifecyclePostStartHandlerHttpGetPath') is not None:
            self.lifecycle_post_start_handler_http_get_path = m.get('LifecyclePostStartHandlerHttpGetPath')
        if m.get('LifecyclePostStartHandlerHttpGetPort') is not None:
            self.lifecycle_post_start_handler_http_get_port = m.get('LifecyclePostStartHandlerHttpGetPort')
        if m.get('LifecyclePostStartHandlerHttpGetScheme') is not None:
            self.lifecycle_post_start_handler_http_get_scheme = m.get('LifecyclePostStartHandlerHttpGetScheme')
        if m.get('LifecyclePostStartHandlerTcpSocketHost') is not None:
            self.lifecycle_post_start_handler_tcp_socket_host = m.get('LifecyclePostStartHandlerTcpSocketHost')
        if m.get('LifecyclePostStartHandlerTcpSocketPort') is not None:
            self.lifecycle_post_start_handler_tcp_socket_port = m.get('LifecyclePostStartHandlerTcpSocketPort')
        if m.get('LifecyclePreStopHandlerExec') is not None:
            self.lifecycle_pre_stop_handler_exec = m.get('LifecyclePreStopHandlerExec')
        if m.get('LifecyclePreStopHandlerHttpGetHost') is not None:
            self.lifecycle_pre_stop_handler_http_get_host = m.get('LifecyclePreStopHandlerHttpGetHost')
        self.lifecycle_pre_stop_handler_http_get_http_header = []
        if m.get('LifecyclePreStopHandlerHttpGetHttpHeader') is not None:
            for k in m.get('LifecyclePreStopHandlerHttpGetHttpHeader'):
                temp_model = UpdateContainerGroupRequestContainerLifecyclePreStopHandlerHttpGetHttpHeader()
                self.lifecycle_pre_stop_handler_http_get_http_header.append(temp_model.from_map(k))
        if m.get('LifecyclePreStopHandlerHttpGetPath') is not None:
            self.lifecycle_pre_stop_handler_http_get_path = m.get('LifecyclePreStopHandlerHttpGetPath')
        if m.get('LifecyclePreStopHandlerHttpGetPort') is not None:
            self.lifecycle_pre_stop_handler_http_get_port = m.get('LifecyclePreStopHandlerHttpGetPort')
        if m.get('LifecyclePreStopHandlerHttpGetScheme') is not None:
            self.lifecycle_pre_stop_handler_http_get_scheme = m.get('LifecyclePreStopHandlerHttpGetScheme')
        if m.get('LifecyclePreStopHandlerTcpSocketHost') is not None:
            self.lifecycle_pre_stop_handler_tcp_socket_host = m.get('LifecyclePreStopHandlerTcpSocketHost')
        if m.get('LifecyclePreStopHandlerTcpSocketPort') is not None:
            self.lifecycle_pre_stop_handler_tcp_socket_port = m.get('LifecyclePreStopHandlerTcpSocketPort')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.port = []
        if m.get('Port') is not None:
            for k in m.get('Port'):
                temp_model = UpdateContainerGroupRequestContainerPort()
                self.port.append(temp_model.from_map(k))
        if m.get('Stdin') is not None:
            self.stdin = m.get('Stdin')
        if m.get('StdinOnce') is not None:
            self.stdin_once = m.get('StdinOnce')
        if m.get('Tty') is not None:
            self.tty = m.get('Tty')
        self.volume_mount = []
        if m.get('VolumeMount') is not None:
            for k in m.get('VolumeMount'):
                temp_model = UpdateContainerGroupRequestContainerVolumeMount()
                self.volume_mount.append(temp_model.from_map(k))
        if m.get('WorkingDir') is not None:
            self.working_dir = m.get('WorkingDir')
        return self


class UpdateContainerGroupRequestImageRegistryCredential(TeaModel):
    def __init__(
        self,
        password: str = None,
        server: str = None,
        user_name: str = None,
    ):
        # The password that you use to access the image repository.
        self.password = password
        # The address of the image repository. This address does not contain `http://` or `https://`.
        self.server = server
        # The username that you use to access the image repository.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.password is not None:
            result['Password'] = self.password
        if self.server is not None:
            result['Server'] = self.server
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Server') is not None:
            self.server = m.get('Server')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class UpdateContainerGroupRequestInitContainerSecurityContextCapability(TeaModel):
    def __init__(
        self,
        add: List[str] = None,
    ):
        self.add = add

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.add is not None:
            result['Add'] = self.add
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Add') is not None:
            self.add = m.get('Add')
        return self


class UpdateContainerGroupRequestInitContainerSecurityContext(TeaModel):
    def __init__(
        self,
        capability: UpdateContainerGroupRequestInitContainerSecurityContextCapability = None,
        read_only_root_filesystem: bool = None,
        run_as_user: int = None,
    ):
        self.capability = capability
        self.read_only_root_filesystem = read_only_root_filesystem
        self.run_as_user = run_as_user

    def validate(self):
        if self.capability:
            self.capability.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.capability is not None:
            result['Capability'] = self.capability.to_map()
        if self.read_only_root_filesystem is not None:
            result['ReadOnlyRootFilesystem'] = self.read_only_root_filesystem
        if self.run_as_user is not None:
            result['RunAsUser'] = self.run_as_user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Capability') is not None:
            temp_model = UpdateContainerGroupRequestInitContainerSecurityContextCapability()
            self.capability = temp_model.from_map(m['Capability'])
        if m.get('ReadOnlyRootFilesystem') is not None:
            self.read_only_root_filesystem = m.get('ReadOnlyRootFilesystem')
        if m.get('RunAsUser') is not None:
            self.run_as_user = m.get('RunAsUser')
        return self


class UpdateContainerGroupRequestInitContainerEnvironmentVarFieldRef(TeaModel):
    def __init__(
        self,
        field_path: str = None,
    ):
        self.field_path = field_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_path is not None:
            result['FieldPath'] = self.field_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldPath') is not None:
            self.field_path = m.get('FieldPath')
        return self


class UpdateContainerGroupRequestInitContainerEnvironmentVar(TeaModel):
    def __init__(
        self,
        field_ref: UpdateContainerGroupRequestInitContainerEnvironmentVarFieldRef = None,
        key: str = None,
        value: str = None,
    ):
        self.field_ref = field_ref
        # The name of the environment variable for the init container.
        self.key = key
        # The value of the environment variable for the init container.
        self.value = value

    def validate(self):
        if self.field_ref:
            self.field_ref.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_ref is not None:
            result['FieldRef'] = self.field_ref.to_map()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldRef') is not None:
            temp_model = UpdateContainerGroupRequestInitContainerEnvironmentVarFieldRef()
            self.field_ref = temp_model.from_map(m['FieldRef'])
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateContainerGroupRequestInitContainerPort(TeaModel):
    def __init__(
        self,
        port: int = None,
        protocol: str = None,
    ):
        # The port number of the init container. Valid values: 1 to 65535.
        self.port = port
        # The protocol of the init container. Valid values: TCP and UDP.
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.port is not None:
            result['Port'] = self.port
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        return self


class UpdateContainerGroupRequestInitContainerVolumeMount(TeaModel):
    def __init__(
        self,
        mount_path: str = None,
        mount_propagation: str = None,
        name: str = None,
        read_only: bool = None,
        sub_path: str = None,
    ):
        # The mount directory of the init container. The data in this directory is overwritten by the data on the volume. Specify this parameter with caution.
        self.mount_path = mount_path
        # The mount propagation settings of the volume. Mount propagation allows volumes that are mounted on one container to be shared with other containers in the same pod, or even with other pods on the same node. Valid values:
        # 
        # *   None: The volume mount does not receive subsequent mounts that are performed on this volume or subdirectories of this volume.
        # *   HostToContainer: The volume mount receives all subsequent mounts that are performed on this volume or subdirectories of this volume.
        # *   Bidirectional: The volume mount behaves the same as the HostToContainer mount. The volume mount receives subsequent mounts that are performed on the volume or the subdirectories of the volume. In addition, all volume mounts that are mounted on the container are propagated back to the host and all containers of all pods that use the same volume.
        # 
        # Default value: None.
        self.mount_propagation = mount_propagation
        # The name of the volume that is mounted to the init container. Valid values: the values of Volume.N.Name, which are the names of volumes that are mounted to the elastic container instance.
        self.name = name
        # Specifies whether the volume is read-only. Default value: false.
        self.read_only = read_only
        # The subdirectory of the volume that is mounted to the init container. You can use this parameter to mount the same volume to different subdirectories of the init container.
        self.sub_path = sub_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mount_path is not None:
            result['MountPath'] = self.mount_path
        if self.mount_propagation is not None:
            result['MountPropagation'] = self.mount_propagation
        if self.name is not None:
            result['Name'] = self.name
        if self.read_only is not None:
            result['ReadOnly'] = self.read_only
        if self.sub_path is not None:
            result['SubPath'] = self.sub_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')
        if m.get('MountPropagation') is not None:
            self.mount_propagation = m.get('MountPropagation')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ReadOnly') is not None:
            self.read_only = m.get('ReadOnly')
        if m.get('SubPath') is not None:
            self.sub_path = m.get('SubPath')
        return self


class UpdateContainerGroupRequestInitContainer(TeaModel):
    def __init__(
        self,
        security_context: UpdateContainerGroupRequestInitContainerSecurityContext = None,
        arg: List[str] = None,
        command: List[str] = None,
        cpu: float = None,
        environment_var: List[UpdateContainerGroupRequestInitContainerEnvironmentVar] = None,
        gpu: int = None,
        image: str = None,
        image_pull_policy: str = None,
        memory: float = None,
        name: str = None,
        port: List[UpdateContainerGroupRequestInitContainerPort] = None,
        stdin: bool = None,
        stdin_once: bool = None,
        tty: bool = None,
        volume_mount: List[UpdateContainerGroupRequestInitContainerVolumeMount] = None,
        working_dir: str = None,
    ):
        self.security_context = security_context
        # The arguments that you want to pass to the startup command of the init container.
        self.arg = arg
        # The commands that are used to start the init container.
        self.command = command
        # The number of vCPUs that you want to allocate to the init container.
        self.cpu = cpu
        # The environment variable of the init container.
        self.environment_var = environment_var
        # The number of GPUs you want to allocate to the init container.
        self.gpu = gpu
        # The image of the init container.
        self.image = image
        # The image pulling policy. Valid values:
        # 
        # *   Always: Each time the instance is updated, image pulling is performed.
        # *   IfNotPresent: On-premises images are used first. If no on-premises images are available, image pulling is performed.
        # *   Never: On-premises images are always used. Image pulling is not performed.
        self.image_pull_policy = image_pull_policy
        # The memory size of the init container.
        self.memory = memory
        # The name of the init container.
        self.name = name
        # The port number. Valid values: 1 to 65535.
        self.port = port
        # Specifies whether the init container allocates buffer resources to standard input streams when the init container is running. If you do not specify this parameter, an EOF error may occur when standard input streams in the init container are read. Default value: false.
        self.stdin = stdin
        # Specifies whether standard input streams are disconnected after a client is disconnected. If Stdin is set to true, standard input streams remain connected among multiple sessions. If StdinOnce is set to true, standard input streams are connected after the init container is started, and remain idle until a client is connected to receive data. After the client is disconnected, streams are also disconnected, and remain disconnected until the init container restarts.
        self.stdin_once = stdin_once
        # Specifies whether to enable interaction. Default value: false. If the command is a /bin/bash command, set the value to true.
        self.tty = tty
        # The information about the volume that you want to mount on the init container.
        self.volume_mount = volume_mount
        # The working directory of the init container.
        self.working_dir = working_dir

    def validate(self):
        if self.security_context:
            self.security_context.validate()
        if self.environment_var:
            for k in self.environment_var:
                if k:
                    k.validate()
        if self.port:
            for k in self.port:
                if k:
                    k.validate()
        if self.volume_mount:
            for k in self.volume_mount:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_context is not None:
            result['SecurityContext'] = self.security_context.to_map()
        if self.arg is not None:
            result['Arg'] = self.arg
        if self.command is not None:
            result['Command'] = self.command
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        result['EnvironmentVar'] = []
        if self.environment_var is not None:
            for k in self.environment_var:
                result['EnvironmentVar'].append(k.to_map() if k else None)
        if self.gpu is not None:
            result['Gpu'] = self.gpu
        if self.image is not None:
            result['Image'] = self.image
        if self.image_pull_policy is not None:
            result['ImagePullPolicy'] = self.image_pull_policy
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.name is not None:
            result['Name'] = self.name
        result['Port'] = []
        if self.port is not None:
            for k in self.port:
                result['Port'].append(k.to_map() if k else None)
        if self.stdin is not None:
            result['Stdin'] = self.stdin
        if self.stdin_once is not None:
            result['StdinOnce'] = self.stdin_once
        if self.tty is not None:
            result['Tty'] = self.tty
        result['VolumeMount'] = []
        if self.volume_mount is not None:
            for k in self.volume_mount:
                result['VolumeMount'].append(k.to_map() if k else None)
        if self.working_dir is not None:
            result['WorkingDir'] = self.working_dir
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityContext') is not None:
            temp_model = UpdateContainerGroupRequestInitContainerSecurityContext()
            self.security_context = temp_model.from_map(m['SecurityContext'])
        if m.get('Arg') is not None:
            self.arg = m.get('Arg')
        if m.get('Command') is not None:
            self.command = m.get('Command')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        self.environment_var = []
        if m.get('EnvironmentVar') is not None:
            for k in m.get('EnvironmentVar'):
                temp_model = UpdateContainerGroupRequestInitContainerEnvironmentVar()
                self.environment_var.append(temp_model.from_map(k))
        if m.get('Gpu') is not None:
            self.gpu = m.get('Gpu')
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('ImagePullPolicy') is not None:
            self.image_pull_policy = m.get('ImagePullPolicy')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.port = []
        if m.get('Port') is not None:
            for k in m.get('Port'):
                temp_model = UpdateContainerGroupRequestInitContainerPort()
                self.port.append(temp_model.from_map(k))
        if m.get('Stdin') is not None:
            self.stdin = m.get('Stdin')
        if m.get('StdinOnce') is not None:
            self.stdin_once = m.get('StdinOnce')
        if m.get('Tty') is not None:
            self.tty = m.get('Tty')
        self.volume_mount = []
        if m.get('VolumeMount') is not None:
            for k in m.get('VolumeMount'):
                temp_model = UpdateContainerGroupRequestInitContainerVolumeMount()
                self.volume_mount.append(temp_model.from_map(k))
        if m.get('WorkingDir') is not None:
            self.working_dir = m.get('WorkingDir')
        return self


class UpdateContainerGroupRequestTag(TeaModel):
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


class UpdateContainerGroupRequestVolumeConfigFileVolumeConfigFileToPath(TeaModel):
    def __init__(
        self,
        content: str = None,
        path: str = None,
    ):
        self.content = content
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class UpdateContainerGroupRequestVolumeConfigFileVolume(TeaModel):
    def __init__(
        self,
        config_file_to_path: List[UpdateContainerGroupRequestVolumeConfigFileVolumeConfigFileToPath] = None,
    ):
        self.config_file_to_path = config_file_to_path

    def validate(self):
        if self.config_file_to_path:
            for k in self.config_file_to_path:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ConfigFileToPath'] = []
        if self.config_file_to_path is not None:
            for k in self.config_file_to_path:
                result['ConfigFileToPath'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.config_file_to_path = []
        if m.get('ConfigFileToPath') is not None:
            for k in m.get('ConfigFileToPath'):
                temp_model = UpdateContainerGroupRequestVolumeConfigFileVolumeConfigFileToPath()
                self.config_file_to_path.append(temp_model.from_map(k))
        return self


class UpdateContainerGroupRequestVolumeEmptyDirVolume(TeaModel):
    def __init__(
        self,
        medium: str = None,
        size_limit: str = None,
    ):
        self.medium = medium
        self.size_limit = size_limit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.medium is not None:
            result['Medium'] = self.medium
        if self.size_limit is not None:
            result['SizeLimit'] = self.size_limit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Medium') is not None:
            self.medium = m.get('Medium')
        if m.get('SizeLimit') is not None:
            self.size_limit = m.get('SizeLimit')
        return self


class UpdateContainerGroupRequestVolumeFlexVolume(TeaModel):
    def __init__(
        self,
        driver: str = None,
        fs_type: str = None,
        options: str = None,
    ):
        self.driver = driver
        self.fs_type = fs_type
        self.options = options

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.driver is not None:
            result['Driver'] = self.driver
        if self.fs_type is not None:
            result['FsType'] = self.fs_type
        if self.options is not None:
            result['Options'] = self.options
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Driver') is not None:
            self.driver = m.get('Driver')
        if m.get('FsType') is not None:
            self.fs_type = m.get('FsType')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        return self


class UpdateContainerGroupRequestVolumeHostPathVolume(TeaModel):
    def __init__(
        self,
        path: str = None,
        type: str = None,
    ):
        self.path = path
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.path is not None:
            result['Path'] = self.path
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class UpdateContainerGroupRequestVolumeNFSVolume(TeaModel):
    def __init__(
        self,
        path: str = None,
        read_only: bool = None,
        server: str = None,
    ):
        self.path = path
        self.read_only = read_only
        self.server = server

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.path is not None:
            result['Path'] = self.path
        if self.read_only is not None:
            result['ReadOnly'] = self.read_only
        if self.server is not None:
            result['Server'] = self.server
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('ReadOnly') is not None:
            self.read_only = m.get('ReadOnly')
        if m.get('Server') is not None:
            self.server = m.get('Server')
        return self


class UpdateContainerGroupRequestVolume(TeaModel):
    def __init__(
        self,
        config_file_volume: UpdateContainerGroupRequestVolumeConfigFileVolume = None,
        empty_dir_volume: UpdateContainerGroupRequestVolumeEmptyDirVolume = None,
        flex_volume: UpdateContainerGroupRequestVolumeFlexVolume = None,
        host_path_volume: UpdateContainerGroupRequestVolumeHostPathVolume = None,
        nfsvolume: UpdateContainerGroupRequestVolumeNFSVolume = None,
        name: str = None,
        type: str = None,
    ):
        self.config_file_volume = config_file_volume
        self.empty_dir_volume = empty_dir_volume
        self.flex_volume = flex_volume
        self.host_path_volume = host_path_volume
        self.nfsvolume = nfsvolume
        # The volume name.
        self.name = name
        # The type of the HostPath volume. Valid values:
        # 
        # *   Directory
        # *   File
        # 
        # >  This parameter is not publicly available.
        self.type = type

    def validate(self):
        if self.config_file_volume:
            self.config_file_volume.validate()
        if self.empty_dir_volume:
            self.empty_dir_volume.validate()
        if self.flex_volume:
            self.flex_volume.validate()
        if self.host_path_volume:
            self.host_path_volume.validate()
        if self.nfsvolume:
            self.nfsvolume.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_file_volume is not None:
            result['ConfigFileVolume'] = self.config_file_volume.to_map()
        if self.empty_dir_volume is not None:
            result['EmptyDirVolume'] = self.empty_dir_volume.to_map()
        if self.flex_volume is not None:
            result['FlexVolume'] = self.flex_volume.to_map()
        if self.host_path_volume is not None:
            result['HostPathVolume'] = self.host_path_volume.to_map()
        if self.nfsvolume is not None:
            result['NFSVolume'] = self.nfsvolume.to_map()
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigFileVolume') is not None:
            temp_model = UpdateContainerGroupRequestVolumeConfigFileVolume()
            self.config_file_volume = temp_model.from_map(m['ConfigFileVolume'])
        if m.get('EmptyDirVolume') is not None:
            temp_model = UpdateContainerGroupRequestVolumeEmptyDirVolume()
            self.empty_dir_volume = temp_model.from_map(m['EmptyDirVolume'])
        if m.get('FlexVolume') is not None:
            temp_model = UpdateContainerGroupRequestVolumeFlexVolume()
            self.flex_volume = temp_model.from_map(m['FlexVolume'])
        if m.get('HostPathVolume') is not None:
            temp_model = UpdateContainerGroupRequestVolumeHostPathVolume()
            self.host_path_volume = temp_model.from_map(m['HostPathVolume'])
        if m.get('NFSVolume') is not None:
            temp_model = UpdateContainerGroupRequestVolumeNFSVolume()
            self.nfsvolume = temp_model.from_map(m['NFSVolume'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class UpdateContainerGroupRequest(TeaModel):
    def __init__(
        self,
        dns_config: UpdateContainerGroupRequestDnsConfig = None,
        acr_registry_info: List[UpdateContainerGroupRequestAcrRegistryInfo] = None,
        client_token: str = None,
        container: List[UpdateContainerGroupRequestContainer] = None,
        container_group_id: str = None,
        cpu: float = None,
        image_registry_credential: List[UpdateContainerGroupRequestImageRegistryCredential] = None,
        init_container: List[UpdateContainerGroupRequestInitContainer] = None,
        memory: float = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        restart_policy: str = None,
        tag: List[UpdateContainerGroupRequestTag] = None,
        update_type: str = None,
        volume: List[UpdateContainerGroupRequestVolume] = None,
    ):
        self.dns_config = dns_config
        # Details of the Container Registry Enterprise Edition instance that hosts the image of the init container.
        self.acr_registry_info = acr_registry_info
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that the value is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotency](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The new configurations of the container group.
        self.container = container
        # The ID of the elastic container instance that you want to update.
        # 
        # This parameter is required.
        self.container_group_id = container_group_id
        # The number of vCPUs that are allocated to the elastic container instance.
        self.cpu = cpu
        # The information about the credentials of the image repository.
        self.image_registry_credential = image_registry_credential
        # The information about the new init container.
        self.init_container = init_container
        # The size of the memory that is allocated to the elastic container instance. Unit: GiB.
        self.memory = memory
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The restart policy of the elastic container instance. Valid values:
        # 
        # *   Always: Always restarts the instance if a container in the instance exits upon termination.
        # *   Never: Never restarts the instance if a container in the instance exits upon termination.
        # *   OnFailure: Restarts the instance only if a container in the instance exists upon failure with a status code of non-zero.
        self.restart_policy = restart_policy
        # The tags that are bound to the instance.
        self.tag = tag
        # The update type. Valid values:
        # 
        # *   RenewUpdate: full updates. You must specify all relevant parameters to update the elastic container instance. For a parameter of the list type, you must specify all the items contained in the parameter even if you want to update only some of the items. For a parameter of the struct type, you must specify all the members even if you want to update only some of the members.
        # *   IncrementalUpdate: incremental updates. You may specify only the parameter that you want to update. Other related parameters remain unchanged.
        # 
        # Default value: RenewUpdate.
        self.update_type = update_type
        # The volumes that are mounted to the instance.
        self.volume = volume

    def validate(self):
        if self.dns_config:
            self.dns_config.validate()
        if self.acr_registry_info:
            for k in self.acr_registry_info:
                if k:
                    k.validate()
        if self.container:
            for k in self.container:
                if k:
                    k.validate()
        if self.image_registry_credential:
            for k in self.image_registry_credential:
                if k:
                    k.validate()
        if self.init_container:
            for k in self.init_container:
                if k:
                    k.validate()
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()
        if self.volume:
            for k in self.volume:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dns_config is not None:
            result['DnsConfig'] = self.dns_config.to_map()
        result['AcrRegistryInfo'] = []
        if self.acr_registry_info is not None:
            for k in self.acr_registry_info:
                result['AcrRegistryInfo'].append(k.to_map() if k else None)
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        result['Container'] = []
        if self.container is not None:
            for k in self.container:
                result['Container'].append(k.to_map() if k else None)
        if self.container_group_id is not None:
            result['ContainerGroupId'] = self.container_group_id
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        result['ImageRegistryCredential'] = []
        if self.image_registry_credential is not None:
            for k in self.image_registry_credential:
                result['ImageRegistryCredential'].append(k.to_map() if k else None)
        result['InitContainer'] = []
        if self.init_container is not None:
            for k in self.init_container:
                result['InitContainer'].append(k.to_map() if k else None)
        if self.memory is not None:
            result['Memory'] = self.memory
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
        if self.restart_policy is not None:
            result['RestartPolicy'] = self.restart_policy
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.update_type is not None:
            result['UpdateType'] = self.update_type
        result['Volume'] = []
        if self.volume is not None:
            for k in self.volume:
                result['Volume'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DnsConfig') is not None:
            temp_model = UpdateContainerGroupRequestDnsConfig()
            self.dns_config = temp_model.from_map(m['DnsConfig'])
        self.acr_registry_info = []
        if m.get('AcrRegistryInfo') is not None:
            for k in m.get('AcrRegistryInfo'):
                temp_model = UpdateContainerGroupRequestAcrRegistryInfo()
                self.acr_registry_info.append(temp_model.from_map(k))
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        self.container = []
        if m.get('Container') is not None:
            for k in m.get('Container'):
                temp_model = UpdateContainerGroupRequestContainer()
                self.container.append(temp_model.from_map(k))
        if m.get('ContainerGroupId') is not None:
            self.container_group_id = m.get('ContainerGroupId')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        self.image_registry_credential = []
        if m.get('ImageRegistryCredential') is not None:
            for k in m.get('ImageRegistryCredential'):
                temp_model = UpdateContainerGroupRequestImageRegistryCredential()
                self.image_registry_credential.append(temp_model.from_map(k))
        self.init_container = []
        if m.get('InitContainer') is not None:
            for k in m.get('InitContainer'):
                temp_model = UpdateContainerGroupRequestInitContainer()
                self.init_container.append(temp_model.from_map(k))
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
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
        if m.get('RestartPolicy') is not None:
            self.restart_policy = m.get('RestartPolicy')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = UpdateContainerGroupRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('UpdateType') is not None:
            self.update_type = m.get('UpdateType')
        self.volume = []
        if m.get('Volume') is not None:
            for k in m.get('Volume'):
                temp_model = UpdateContainerGroupRequestVolume()
                self.volume.append(temp_model.from_map(k))
        return self


class UpdateContainerGroupResponseBody(TeaModel):
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


class UpdateContainerGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateContainerGroupResponseBody = None,
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
            temp_model = UpdateContainerGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDataCacheRequestDataSource(TeaModel):
    def __init__(
        self,
        options: Dict[str, str] = None,
        type: str = None,
    ):
        # The parameters that are configured for the data source.
        self.options = options
        # The type of the data source. Valid values:
        # 
        # *   URL
        # *   NAS
        # *   OSS
        # *   SNAPSHOT
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.options is not None:
            result['Options'] = self.options
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Options') is not None:
            self.options = m.get('Options')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class UpdateDataCacheRequestEipCreateParam(TeaModel):
    def __init__(
        self,
        bandwidth: int = None,
        common_bandwidth_package: str = None,
        isp: str = None,
        internet_charge_type: str = None,
        public_ip_address_pool_id: str = None,
    ):
        # The bandwidth of the EIP. Unit: Mbit/s. Default value: 5.
        self.bandwidth = bandwidth
        # The EIP bandwidth plan to be associated.
        self.common_bandwidth_package = common_bandwidth_package
        # The line type of the EIP. Valid values:
        # 
        # *   BGP (default): BGP (Multi-ISP) line
        # *   BGP_PRO: BGP (Multi-ISP) Pro line
        self.isp = isp
        # The metering method of the EIP. Valid values:
        # 
        # *   PayByBandwidth: pay-by-bandwidth
        # *   PayByTraffic: pay-by-data-transfer
        self.internet_charge_type = internet_charge_type
        # The ID of the IP address pool. The EIP is allocated from the IP address pool. You cannot use the IP address pool feature by default. To use this feature, you must apply for the privilege in the Quota Center console.
        self.public_ip_address_pool_id = public_ip_address_pool_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.common_bandwidth_package is not None:
            result['CommonBandwidthPackage'] = self.common_bandwidth_package
        if self.isp is not None:
            result['ISP'] = self.isp
        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type
        if self.public_ip_address_pool_id is not None:
            result['PublicIpAddressPoolId'] = self.public_ip_address_pool_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('CommonBandwidthPackage') is not None:
            self.common_bandwidth_package = m.get('CommonBandwidthPackage')
        if m.get('ISP') is not None:
            self.isp = m.get('ISP')
        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')
        if m.get('PublicIpAddressPoolId') is not None:
            self.public_ip_address_pool_id = m.get('PublicIpAddressPoolId')
        return self


class UpdateDataCacheRequestTag(TeaModel):
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


class UpdateDataCacheRequest(TeaModel):
    def __init__(
        self,
        bucket: str = None,
        client_token: str = None,
        data_cache_id: str = None,
        data_source: UpdateDataCacheRequestDataSource = None,
        eip_create_param: UpdateDataCacheRequestEipCreateParam = None,
        eip_instance_id: str = None,
        name: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        retention_days: int = None,
        security_group_id: str = None,
        size: int = None,
        tag: List[UpdateDataCacheRequestTag] = None,
        v_switch_id: str = None,
    ):
        # The bucket in which the data cache is stored. Default value: default.
        self.bucket = bucket
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate a token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure the idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The data cache ID.
        self.data_cache_id = data_cache_id
        # The information about the data source.
        self.data_source = data_source
        # The elastic IP address (EIP) to be created and associated. If no NAT gateway is configured for the virtual private cloud (VPC), you can associate an EIP to pull data from the Internet.
        self.eip_create_param = eip_create_param
        # The ID of the elastic IP address (EIP). If no NAT gateway is configured for the virtual private cloud (VPC), you can bind an EIP to the elastic container instance to pull data from the Internet.
        self.eip_instance_id = eip_instance_id
        # The data cache name.
        self.name = name
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The retention period for the data cache. The data cache is deleted after the retention period expires. By default, the data cache does not expire.
        self.retention_days = retention_days
        # The ID of the security group.
        self.security_group_id = security_group_id
        # The data cache size.
        self.size = size
        # The tags that are added to the data cache.
        self.tag = tag
        # The vSwitch ID.
        self.v_switch_id = v_switch_id

    def validate(self):
        if self.data_source:
            self.data_source.validate()
        if self.eip_create_param:
            self.eip_create_param.validate()
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.data_cache_id is not None:
            result['DataCacheId'] = self.data_cache_id
        if self.data_source is not None:
            result['DataSource'] = self.data_source.to_map()
        if self.eip_create_param is not None:
            result['EipCreateParam'] = self.eip_create_param.to_map()
        if self.eip_instance_id is not None:
            result['EipInstanceId'] = self.eip_instance_id
        if self.name is not None:
            result['Name'] = self.name
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
        if self.retention_days is not None:
            result['RetentionDays'] = self.retention_days
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.size is not None:
            result['Size'] = self.size
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DataCacheId') is not None:
            self.data_cache_id = m.get('DataCacheId')
        if m.get('DataSource') is not None:
            temp_model = UpdateDataCacheRequestDataSource()
            self.data_source = temp_model.from_map(m['DataSource'])
        if m.get('EipCreateParam') is not None:
            temp_model = UpdateDataCacheRequestEipCreateParam()
            self.eip_create_param = temp_model.from_map(m['EipCreateParam'])
        if m.get('EipInstanceId') is not None:
            self.eip_instance_id = m.get('EipInstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
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
        if m.get('RetentionDays') is not None:
            self.retention_days = m.get('RetentionDays')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = UpdateDataCacheRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        return self


class UpdateDataCacheResponseBody(TeaModel):
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


class UpdateDataCacheResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateDataCacheResponseBody = None,
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
            temp_model = UpdateDataCacheResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateImageCacheRequestAcrRegistryInfo(TeaModel):
    def __init__(
        self,
        domain: List[str] = None,
        instance_id: str = None,
        instance_name: str = None,
        region_id: str = None,
    ):
        # The domain names of the Container Registry Enterprise Edition instance. By default, all domain names of the instance are displayed. You can specify multiple domain names. Separate multiple domain names with commas (,).
        self.domain = domain
        # The ID of the Container Registry Enterprise Edition instance.
        self.instance_id = instance_id
        # The name of the Container Registry Enterprise Edition instance.
        self.instance_name = instance_name
        # The region ID of the Container Registry Enterprise Edition instance.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateImageCacheRequestImageRegistryCredential(TeaModel):
    def __init__(
        self,
        password: str = None,
        server: str = None,
        user_name: str = None,
    ):
        # The password that is used to access the image repository.
        self.password = password
        # The image repository address without `http://` or `https://` as a prefix.
        self.server = server
        # The username that is used to access the image repository.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.password is not None:
            result['Password'] = self.password
        if self.server is not None:
            result['Server'] = self.server
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Server') is not None:
            self.server = m.get('Server')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class UpdateImageCacheRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N to add to the image cache.
        self.key = key
        # The value of tag N to add to the image cache.
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


class UpdateImageCacheRequest(TeaModel):
    def __init__(
        self,
        acr_registry_info: List[UpdateImageCacheRequestAcrRegistryInfo] = None,
        auto_match_image_cache: bool = None,
        client_token: str = None,
        eip_instance_id: str = None,
        elimination_strategy: str = None,
        flash: bool = None,
        flash_copy_count: int = None,
        image: List[str] = None,
        image_cache_id: str = None,
        image_cache_name: str = None,
        image_cache_size: int = None,
        image_registry_credential: List[UpdateImageCacheRequestImageRegistryCredential] = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        retention_days: int = None,
        security_group_id: str = None,
        standard_copy_count: int = None,
        tag: List[UpdateImageCacheRequestTag] = None,
        v_switch_id: str = None,
    ):
        # The information about the Container Registry Enterprise Edition instance.
        self.acr_registry_info = acr_registry_info
        # Specifies whether to enable reuse of image cache layers. If you enable this feature and the image cache that you want to create and an existing image cache contain duplicate image layers, the system reuses the duplicate image layers to create the new image cache. This accelerates the creation of the image cache. Valid values:
        # 
        # *   true
        # *   false
        # 
        # Default value: false.
        self.auto_match_image_cache = auto_match_image_cache
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure the idempotence of a request?](https://help.aliyun.com/document_detail/25693.html)
        self.client_token = client_token
        # The ID of the elastic IP address (EIP). If you want to pull public images, you must make sure that the elastic container instance can access the Internet. To enable Internet access, you can configure an EIP or a NAT gateway for the instance.
        self.eip_instance_id = eip_instance_id
        # The elimination policy for the image cache. This parameter is empty by default, which indicates that the image cache is always retained.
        # 
        # You can set this parameter to LRU, which indicates that the image cache can be automatically deleted. When the number of image caches reaches the quota, the system automatically deletes the image caches whose EliminationStrategy parameter is set to LRU and that are least recently used.
        self.elimination_strategy = elimination_strategy
        # Specifies whether to enable the instant image cache feature. The feature can accelerate the creation of image caches. Valid values:
        # 
        # *   true
        # *   false
        # 
        # Default value: false.
        self.flash = flash
        # The number of duplicates of temporary local snapshots. By default, the system creates one snapshot for each image cache. If you use the image cache to create multiple elastic container instances at a time, we recommend that you configure this parameter to create multiple snapshot duplicates for the image cache. We recommend that you create one snapshot duplicate for creation of every 1,000 elastic container instances.
        # 
        # > If you enable the instant image cache feature by setting Flash to true, a local snapshot is first created during the creation of the image cache. After the local snapshot is created, regular snapshots start to be created. After the regular snapshots are created, the local snapshot is automatically deleted.
        self.flash_copy_count = flash_copy_count
        # Container images that are used to create the image cache.
        self.image = image
        # The ID of the image cache.
        # 
        # This parameter is required.
        self.image_cache_id = image_cache_id
        # The name of the image cache.
        self.image_cache_name = image_cache_name
        # The size of the image cache. Unit: GiB. Default value: 20.
        self.image_cache_size = image_cache_size
        # The information about the image repository.
        self.image_registry_credential = image_registry_credential
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the image cache.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group to which the image cache belongs.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The retention period of the image cache. Unit: days. When the retention period elapses, the image cache expires and is deleted. By default, image caches never expire.
        # 
        # > The image caches that fail to be created are retained for only 1 day.
        self.retention_days = retention_days
        # The ID of the security group to which the image cache belongs.
        self.security_group_id = security_group_id
        # The number of duplicates of regular snapshots. By default, the system creates one snapshot for each image cache. If you use the image cache to create multiple elastic container instances at a time, we recommend that you configure this parameter to create multiple snapshot duplicates for the image cache. We recommend that you create one snapshot duplicate for creation of every 1,000 elastic container instances.
        # 
        # > If you disable the instant image cache feature by setting Flash to false, only regular snapshots are generated when you create an image cache.
        self.standard_copy_count = standard_copy_count
        # The tags to add to the image cache. A maximum of 20 tags can be added to the image cache.
        self.tag = tag
        # The ID of the vSwitch to which the image cache is connected.
        self.v_switch_id = v_switch_id

    def validate(self):
        if self.acr_registry_info:
            for k in self.acr_registry_info:
                if k:
                    k.validate()
        if self.image_registry_credential:
            for k in self.image_registry_credential:
                if k:
                    k.validate()
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AcrRegistryInfo'] = []
        if self.acr_registry_info is not None:
            for k in self.acr_registry_info:
                result['AcrRegistryInfo'].append(k.to_map() if k else None)
        if self.auto_match_image_cache is not None:
            result['AutoMatchImageCache'] = self.auto_match_image_cache
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.eip_instance_id is not None:
            result['EipInstanceId'] = self.eip_instance_id
        if self.elimination_strategy is not None:
            result['EliminationStrategy'] = self.elimination_strategy
        if self.flash is not None:
            result['Flash'] = self.flash
        if self.flash_copy_count is not None:
            result['FlashCopyCount'] = self.flash_copy_count
        if self.image is not None:
            result['Image'] = self.image
        if self.image_cache_id is not None:
            result['ImageCacheId'] = self.image_cache_id
        if self.image_cache_name is not None:
            result['ImageCacheName'] = self.image_cache_name
        if self.image_cache_size is not None:
            result['ImageCacheSize'] = self.image_cache_size
        result['ImageRegistryCredential'] = []
        if self.image_registry_credential is not None:
            for k in self.image_registry_credential:
                result['ImageRegistryCredential'].append(k.to_map() if k else None)
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
        if self.retention_days is not None:
            result['RetentionDays'] = self.retention_days
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.standard_copy_count is not None:
            result['StandardCopyCount'] = self.standard_copy_count
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.acr_registry_info = []
        if m.get('AcrRegistryInfo') is not None:
            for k in m.get('AcrRegistryInfo'):
                temp_model = UpdateImageCacheRequestAcrRegistryInfo()
                self.acr_registry_info.append(temp_model.from_map(k))
        if m.get('AutoMatchImageCache') is not None:
            self.auto_match_image_cache = m.get('AutoMatchImageCache')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('EipInstanceId') is not None:
            self.eip_instance_id = m.get('EipInstanceId')
        if m.get('EliminationStrategy') is not None:
            self.elimination_strategy = m.get('EliminationStrategy')
        if m.get('Flash') is not None:
            self.flash = m.get('Flash')
        if m.get('FlashCopyCount') is not None:
            self.flash_copy_count = m.get('FlashCopyCount')
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('ImageCacheId') is not None:
            self.image_cache_id = m.get('ImageCacheId')
        if m.get('ImageCacheName') is not None:
            self.image_cache_name = m.get('ImageCacheName')
        if m.get('ImageCacheSize') is not None:
            self.image_cache_size = m.get('ImageCacheSize')
        self.image_registry_credential = []
        if m.get('ImageRegistryCredential') is not None:
            for k in m.get('ImageRegistryCredential'):
                temp_model = UpdateImageCacheRequestImageRegistryCredential()
                self.image_registry_credential.append(temp_model.from_map(k))
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
        if m.get('RetentionDays') is not None:
            self.retention_days = m.get('RetentionDays')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('StandardCopyCount') is not None:
            self.standard_copy_count = m.get('StandardCopyCount')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = UpdateImageCacheRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        return self


class UpdateImageCacheResponseBody(TeaModel):
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


class UpdateImageCacheResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateImageCacheResponseBody = None,
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
            temp_model = UpdateImageCacheResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateVirtualNodeRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N to add to the virtual node.
        self.key = key
        # The value of tag N to add to the virtual node.
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


class UpdateVirtualNodeRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        cluster_dns: str = None,
        cluster_domain: str = None,
        custom_resources: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        tag: List[UpdateVirtualNodeRequestTag] = None,
        virtual_node_id: str = None,
        virtual_node_name: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotency of requests?](https://help.aliyun.com/document_detail/25693.html)
        self.client_token = client_token
        # The IP address of the DNS server. If `dnsPolicy=ClusterFirst` is configured for the Elastic Container Instance pod, Elastic Container Instance uses the configuration to provide DNS services to containers. You can configure multiple IP addresses. Separate multiple IP addresses with commas (,).
        self.cluster_dns = cluster_dns
        # The domain name of the cluster. If this parameter is specified, in addition to the search domain of the host, Kubelet configures all containers to search for the specified domain name.
        self.cluster_domain = cluster_domain
        # The custom resources that are supported by the virtual node. If a custom resource is specified in the request of an Elastic Container Instance pod, the pod is scheduled to run on the virtual node that supports the custom resource. You can use the `Resource name = Number of resources` format to specify custom resources. Separate multiple resources with commas (,).
        self.custom_resources = custom_resources
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the virtual node.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The tags to add to the virtual node.
        self.tag = tag
        # The ID of the virtual node.
        # 
        # This parameter is required.
        self.virtual_node_id = virtual_node_id
        # The name of the virtual node.
        self.virtual_node_name = virtual_node_name

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
        if self.cluster_dns is not None:
            result['ClusterDNS'] = self.cluster_dns
        if self.cluster_domain is not None:
            result['ClusterDomain'] = self.cluster_domain
        if self.custom_resources is not None:
            result['CustomResources'] = self.custom_resources
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
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.virtual_node_id is not None:
            result['VirtualNodeId'] = self.virtual_node_id
        if self.virtual_node_name is not None:
            result['VirtualNodeName'] = self.virtual_node_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ClusterDNS') is not None:
            self.cluster_dns = m.get('ClusterDNS')
        if m.get('ClusterDomain') is not None:
            self.cluster_domain = m.get('ClusterDomain')
        if m.get('CustomResources') is not None:
            self.custom_resources = m.get('CustomResources')
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
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = UpdateVirtualNodeRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('VirtualNodeId') is not None:
            self.virtual_node_id = m.get('VirtualNodeId')
        if m.get('VirtualNodeName') is not None:
            self.virtual_node_name = m.get('VirtualNodeName')
        return self


class UpdateVirtualNodeResponseBody(TeaModel):
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


class UpdateVirtualNodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateVirtualNodeResponseBody = None,
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
            temp_model = UpdateVirtualNodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


