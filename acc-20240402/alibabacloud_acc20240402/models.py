# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class CapacityResource(TeaModel):
    def __init__(
        self,
        cpu: str = None,
        gpu: str = None,
        memory: str = None,
    ):
        self.cpu = cpu
        self.gpu = gpu
        self.memory = memory

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['CPU'] = self.cpu
        if self.gpu is not None:
            result['GPU'] = self.gpu
        if self.memory is not None:
            result['Memory'] = self.memory
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CPU') is not None:
            self.cpu = m.get('CPU')
        if m.get('GPU') is not None:
            self.gpu = m.get('GPU')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        return self


class CreateImageCacheRequestAcrRegistryInfos(TeaModel):
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


class CreateImageCacheRequestImageRegistryCredentials(TeaModel):
    def __init__(
        self,
        password: str = None,
        server: str = None,
        skip_cert_verification: bool = None,
        use_plain_http: bool = None,
        username: str = None,
    ):
        self.password = password
        self.server = server
        self.skip_cert_verification = skip_cert_verification
        self.use_plain_http = use_plain_http
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
        if self.server is not None:
            result['Server'] = self.server
        if self.skip_cert_verification is not None:
            result['SkipCertVerification'] = self.skip_cert_verification
        if self.use_plain_http is not None:
            result['UsePlainHttp'] = self.use_plain_http
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Server') is not None:
            self.server = m.get('Server')
        if m.get('SkipCertVerification') is not None:
            self.skip_cert_verification = m.get('SkipCertVerification')
        if m.get('UsePlainHttp') is not None:
            self.use_plain_http = m.get('UsePlainHttp')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class CreateImageCacheRequestNetworkConfigEipInstance(TeaModel):
    def __init__(
        self,
        auto_create: bool = None,
        bandwidth: int = None,
        instance_id: str = None,
    ):
        self.auto_create = auto_create
        self.bandwidth = bandwidth
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_create is not None:
            result['AutoCreate'] = self.auto_create
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoCreate') is not None:
            self.auto_create = m.get('AutoCreate')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class CreateImageCacheRequestNetworkConfig(TeaModel):
    def __init__(
        self,
        eip_instance: CreateImageCacheRequestNetworkConfigEipInstance = None,
        security_group_id: str = None,
        v_switch_ids: List[str] = None,
    ):
        self.eip_instance = eip_instance
        # This parameter is required.
        self.security_group_id = security_group_id
        # This parameter is required.
        self.v_switch_ids = v_switch_ids

    def validate(self):
        if self.eip_instance:
            self.eip_instance.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.eip_instance is not None:
            result['EipInstance'] = self.eip_instance.to_map()
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EipInstance') is not None:
            temp_model = CreateImageCacheRequestNetworkConfigEipInstance()
            self.eip_instance = temp_model.from_map(m['EipInstance'])
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')
        return self


class CreateImageCacheRequestTags(TeaModel):
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


class CreateImageCacheRequest(TeaModel):
    def __init__(
        self,
        acr_registry_infos: List[CreateImageCacheRequestAcrRegistryInfos] = None,
        client_token: str = None,
        image_cache_name: str = None,
        image_registry_credentials: List[CreateImageCacheRequestImageRegistryCredentials] = None,
        images: List[str] = None,
        network_config: CreateImageCacheRequestNetworkConfig = None,
        region_id: str = None,
        resource_group_id: str = None,
        tags: List[CreateImageCacheRequestTags] = None,
    ):
        self.acr_registry_infos = acr_registry_infos
        self.client_token = client_token
        # This parameter is required.
        self.image_cache_name = image_cache_name
        self.image_registry_credentials = image_registry_credentials
        # This parameter is required.
        self.images = images
        # This parameter is required.
        self.network_config = network_config
        # This parameter is required.
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.tags = tags

    def validate(self):
        if self.acr_registry_infos:
            for k in self.acr_registry_infos:
                if k:
                    k.validate()
        if self.image_registry_credentials:
            for k in self.image_registry_credentials:
                if k:
                    k.validate()
        if self.network_config:
            self.network_config.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AcrRegistryInfos'] = []
        if self.acr_registry_infos is not None:
            for k in self.acr_registry_infos:
                result['AcrRegistryInfos'].append(k.to_map() if k else None)
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.image_cache_name is not None:
            result['ImageCacheName'] = self.image_cache_name
        result['ImageRegistryCredentials'] = []
        if self.image_registry_credentials is not None:
            for k in self.image_registry_credentials:
                result['ImageRegistryCredentials'].append(k.to_map() if k else None)
        if self.images is not None:
            result['Images'] = self.images
        if self.network_config is not None:
            result['NetworkConfig'] = self.network_config.to_map()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.acr_registry_infos = []
        if m.get('AcrRegistryInfos') is not None:
            for k in m.get('AcrRegistryInfos'):
                temp_model = CreateImageCacheRequestAcrRegistryInfos()
                self.acr_registry_infos.append(temp_model.from_map(k))
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ImageCacheName') is not None:
            self.image_cache_name = m.get('ImageCacheName')
        self.image_registry_credentials = []
        if m.get('ImageRegistryCredentials') is not None:
            for k in m.get('ImageRegistryCredentials'):
                temp_model = CreateImageCacheRequestImageRegistryCredentials()
                self.image_registry_credentials.append(temp_model.from_map(k))
        if m.get('Images') is not None:
            self.images = m.get('Images')
        if m.get('NetworkConfig') is not None:
            temp_model = CreateImageCacheRequestNetworkConfig()
            self.network_config = temp_model.from_map(m['NetworkConfig'])
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = CreateImageCacheRequestTags()
                self.tags.append(temp_model.from_map(k))
        return self


class CreateImageCacheShrinkRequestAcrRegistryInfos(TeaModel):
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


class CreateImageCacheShrinkRequestImageRegistryCredentials(TeaModel):
    def __init__(
        self,
        password: str = None,
        server: str = None,
        skip_cert_verification: bool = None,
        use_plain_http: bool = None,
        username: str = None,
    ):
        self.password = password
        self.server = server
        self.skip_cert_verification = skip_cert_verification
        self.use_plain_http = use_plain_http
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
        if self.server is not None:
            result['Server'] = self.server
        if self.skip_cert_verification is not None:
            result['SkipCertVerification'] = self.skip_cert_verification
        if self.use_plain_http is not None:
            result['UsePlainHttp'] = self.use_plain_http
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Server') is not None:
            self.server = m.get('Server')
        if m.get('SkipCertVerification') is not None:
            self.skip_cert_verification = m.get('SkipCertVerification')
        if m.get('UsePlainHttp') is not None:
            self.use_plain_http = m.get('UsePlainHttp')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class CreateImageCacheShrinkRequestTags(TeaModel):
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


class CreateImageCacheShrinkRequest(TeaModel):
    def __init__(
        self,
        acr_registry_infos: List[CreateImageCacheShrinkRequestAcrRegistryInfos] = None,
        client_token: str = None,
        image_cache_name: str = None,
        image_registry_credentials: List[CreateImageCacheShrinkRequestImageRegistryCredentials] = None,
        images: List[str] = None,
        network_config_shrink: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        tags: List[CreateImageCacheShrinkRequestTags] = None,
    ):
        self.acr_registry_infos = acr_registry_infos
        self.client_token = client_token
        # This parameter is required.
        self.image_cache_name = image_cache_name
        self.image_registry_credentials = image_registry_credentials
        # This parameter is required.
        self.images = images
        # This parameter is required.
        self.network_config_shrink = network_config_shrink
        # This parameter is required.
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.tags = tags

    def validate(self):
        if self.acr_registry_infos:
            for k in self.acr_registry_infos:
                if k:
                    k.validate()
        if self.image_registry_credentials:
            for k in self.image_registry_credentials:
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
        result['AcrRegistryInfos'] = []
        if self.acr_registry_infos is not None:
            for k in self.acr_registry_infos:
                result['AcrRegistryInfos'].append(k.to_map() if k else None)
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.image_cache_name is not None:
            result['ImageCacheName'] = self.image_cache_name
        result['ImageRegistryCredentials'] = []
        if self.image_registry_credentials is not None:
            for k in self.image_registry_credentials:
                result['ImageRegistryCredentials'].append(k.to_map() if k else None)
        if self.images is not None:
            result['Images'] = self.images
        if self.network_config_shrink is not None:
            result['NetworkConfig'] = self.network_config_shrink
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.acr_registry_infos = []
        if m.get('AcrRegistryInfos') is not None:
            for k in m.get('AcrRegistryInfos'):
                temp_model = CreateImageCacheShrinkRequestAcrRegistryInfos()
                self.acr_registry_infos.append(temp_model.from_map(k))
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ImageCacheName') is not None:
            self.image_cache_name = m.get('ImageCacheName')
        self.image_registry_credentials = []
        if m.get('ImageRegistryCredentials') is not None:
            for k in m.get('ImageRegistryCredentials'):
                temp_model = CreateImageCacheShrinkRequestImageRegistryCredentials()
                self.image_registry_credentials.append(temp_model.from_map(k))
        if m.get('Images') is not None:
            self.images = m.get('Images')
        if m.get('NetworkConfig') is not None:
            self.network_config_shrink = m.get('NetworkConfig')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = CreateImageCacheShrinkRequestTags()
                self.tags.append(temp_model.from_map(k))
        return self


class CreateImageCacheResponseBody(TeaModel):
    def __init__(
        self,
        image_cache_id: str = None,
        request_id: str = None,
    ):
        self.image_cache_id = image_cache_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_cache_id is not None:
            result['ImageCacheId'] = self.image_cache_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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


class DeleteImageCacheRequest(TeaModel):
    def __init__(
        self,
        force: bool = None,
        image_cache_id: str = None,
        region_id: str = None,
    ):
        self.force = force
        # This parameter is required.
        self.image_cache_id = image_cache_id
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.force is not None:
            result['Force'] = self.force
        if self.image_cache_id is not None:
            result['ImageCacheId'] = self.image_cache_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Force') is not None:
            self.force = m.get('Force')
        if m.get('ImageCacheId') is not None:
            self.image_cache_id = m.get('ImageCacheId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteImageCacheResponseBody(TeaModel):
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


class GetImageCacheRequest(TeaModel):
    def __init__(
        self,
        image_cache_id: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.image_cache_id = image_cache_id
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_cache_id is not None:
            result['ImageCacheId'] = self.image_cache_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageCacheId') is not None:
            self.image_cache_id = m.get('ImageCacheId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetImageCacheResponseBodyEvents(TeaModel):
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
        self.count = count
        self.first_timestamp = first_timestamp
        self.last_timestamp = last_timestamp
        self.message = message
        self.name = name
        self.reason = reason
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


class GetImageCacheResponseBodyNetworkConfigEipInstance(TeaModel):
    def __init__(
        self,
        auto_create: bool = None,
        bandwidth: int = None,
        instance_id: str = None,
    ):
        self.auto_create = auto_create
        self.bandwidth = bandwidth
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_create is not None:
            result['AutoCreate'] = self.auto_create
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoCreate') is not None:
            self.auto_create = m.get('AutoCreate')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetImageCacheResponseBodyNetworkConfig(TeaModel):
    def __init__(
        self,
        eip_instance: GetImageCacheResponseBodyNetworkConfigEipInstance = None,
        security_group_id: str = None,
        v_switch_ids: List[str] = None,
    ):
        self.eip_instance = eip_instance
        self.security_group_id = security_group_id
        self.v_switch_ids = v_switch_ids

    def validate(self):
        if self.eip_instance:
            self.eip_instance.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.eip_instance is not None:
            result['EipInstance'] = self.eip_instance.to_map()
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EipInstance') is not None:
            temp_model = GetImageCacheResponseBodyNetworkConfigEipInstance()
            self.eip_instance = temp_model.from_map(m['EipInstance'])
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')
        return self


class GetImageCacheResponseBodyTags(TeaModel):
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


class GetImageCacheResponseBody(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        events: List[GetImageCacheResponseBodyEvents] = None,
        image_cache_id: str = None,
        image_cache_name: str = None,
        images: List[str] = None,
        network_config: GetImageCacheResponseBodyNetworkConfig = None,
        payment_type: str = None,
        ready_time: str = None,
        region_id: str = None,
        request_id: str = None,
        resource_group_id: str = None,
        size: int = None,
        status: str = None,
        tags: List[GetImageCacheResponseBodyTags] = None,
    ):
        self.create_time = create_time
        self.events = events
        self.image_cache_id = image_cache_id
        self.image_cache_name = image_cache_name
        self.images = images
        self.network_config = network_config
        self.payment_type = payment_type
        self.ready_time = ready_time
        self.region_id = region_id
        self.request_id = request_id
        self.resource_group_id = resource_group_id
        self.size = size
        self.status = status
        self.tags = tags

    def validate(self):
        if self.events:
            for k in self.events:
                if k:
                    k.validate()
        if self.network_config:
            self.network_config.validate()
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
        result['Events'] = []
        if self.events is not None:
            for k in self.events:
                result['Events'].append(k.to_map() if k else None)
        if self.image_cache_id is not None:
            result['ImageCacheId'] = self.image_cache_id
        if self.image_cache_name is not None:
            result['ImageCacheName'] = self.image_cache_name
        if self.images is not None:
            result['Images'] = self.images
        if self.network_config is not None:
            result['NetworkConfig'] = self.network_config.to_map()
        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type
        if self.ready_time is not None:
            result['ReadyTime'] = self.ready_time
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.size is not None:
            result['Size'] = self.size
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
        self.events = []
        if m.get('Events') is not None:
            for k in m.get('Events'):
                temp_model = GetImageCacheResponseBodyEvents()
                self.events.append(temp_model.from_map(k))
        if m.get('ImageCacheId') is not None:
            self.image_cache_id = m.get('ImageCacheId')
        if m.get('ImageCacheName') is not None:
            self.image_cache_name = m.get('ImageCacheName')
        if m.get('Images') is not None:
            self.images = m.get('Images')
        if m.get('NetworkConfig') is not None:
            temp_model = GetImageCacheResponseBodyNetworkConfig()
            self.network_config = temp_model.from_map(m['NetworkConfig'])
        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')
        if m.get('ReadyTime') is not None:
            self.ready_time = m.get('ReadyTime')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = GetImageCacheResponseBodyTags()
                self.tags.append(temp_model.from_map(k))
        return self


class GetImageCacheResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetImageCacheResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetImageCacheResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListImageCachesRequestTags(TeaModel):
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


class ListImageCachesRequest(TeaModel):
    def __init__(
        self,
        image_cache_name: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        status: str = None,
        tags: List[ListImageCachesRequestTags] = None,
    ):
        self.image_cache_name = image_cache_name
        self.max_results = max_results
        self.next_token = next_token
        # This parameter is required.
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.status = status
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
        if self.image_cache_name is not None:
            result['ImageCacheName'] = self.image_cache_name
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
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
        if m.get('ImageCacheName') is not None:
            self.image_cache_name = m.get('ImageCacheName')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListImageCachesRequestTags()
                self.tags.append(temp_model.from_map(k))
        return self


class ListImageCachesResponseBodyImageCaches(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        image_cache_id: str = None,
        image_cache_name: str = None,
        images: List[str] = None,
        ready_time: str = None,
        resource_group_id: str = None,
        size: int = None,
        status: str = None,
    ):
        self.create_time = create_time
        self.image_cache_id = image_cache_id
        self.image_cache_name = image_cache_name
        self.images = images
        self.ready_time = ready_time
        self.resource_group_id = resource_group_id
        self.size = size
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.image_cache_id is not None:
            result['ImageCacheId'] = self.image_cache_id
        if self.image_cache_name is not None:
            result['ImageCacheName'] = self.image_cache_name
        if self.images is not None:
            result['Images'] = self.images
        if self.ready_time is not None:
            result['ReadyTime'] = self.ready_time
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.size is not None:
            result['Size'] = self.size
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ImageCacheId') is not None:
            self.image_cache_id = m.get('ImageCacheId')
        if m.get('ImageCacheName') is not None:
            self.image_cache_name = m.get('ImageCacheName')
        if m.get('Images') is not None:
            self.images = m.get('Images')
        if m.get('ReadyTime') is not None:
            self.ready_time = m.get('ReadyTime')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListImageCachesResponseBody(TeaModel):
    def __init__(
        self,
        image_caches: List[ListImageCachesResponseBodyImageCaches] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.image_caches = image_caches
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
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
        self.image_caches = []
        if m.get('ImageCaches') is not None:
            for k in m.get('ImageCaches'):
                temp_model = ListImageCachesResponseBodyImageCaches()
                self.image_caches.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListImageCachesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListImageCachesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListImageCachesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


