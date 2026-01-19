# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_acc20240402 import models as main_models
from darabonba.model import DaraModel

class CreateImageCacheRequest(DaraModel):
    def __init__(
        self,
        acr_registry_infos: List[main_models.CreateImageCacheRequestAcrRegistryInfos] = None,
        client_token: str = None,
        image_cache_name: str = None,
        image_registry_credentials: List[main_models.CreateImageCacheRequestImageRegistryCredentials] = None,
        images: List[str] = None,
        network_config: main_models.CreateImageCacheRequestNetworkConfig = None,
        region_id: str = None,
        resource_group_id: str = None,
        tags: List[main_models.CreateImageCacheRequestTags] = None,
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
            for v1 in self.acr_registry_infos:
                 if v1:
                    v1.validate()
        if self.image_registry_credentials:
            for v1 in self.image_registry_credentials:
                 if v1:
                    v1.validate()
        if self.network_config:
            self.network_config.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AcrRegistryInfos'] = []
        if self.acr_registry_infos is not None:
            for k1 in self.acr_registry_infos:
                result['AcrRegistryInfos'].append(k1.to_map() if k1 else None)

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.image_cache_name is not None:
            result['ImageCacheName'] = self.image_cache_name

        result['ImageRegistryCredentials'] = []
        if self.image_registry_credentials is not None:
            for k1 in self.image_registry_credentials:
                result['ImageRegistryCredentials'].append(k1.to_map() if k1 else None)

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
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.acr_registry_infos = []
        if m.get('AcrRegistryInfos') is not None:
            for k1 in m.get('AcrRegistryInfos'):
                temp_model = main_models.CreateImageCacheRequestAcrRegistryInfos()
                self.acr_registry_infos.append(temp_model.from_map(k1))

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ImageCacheName') is not None:
            self.image_cache_name = m.get('ImageCacheName')

        self.image_registry_credentials = []
        if m.get('ImageRegistryCredentials') is not None:
            for k1 in m.get('ImageRegistryCredentials'):
                temp_model = main_models.CreateImageCacheRequestImageRegistryCredentials()
                self.image_registry_credentials.append(temp_model.from_map(k1))

        if m.get('Images') is not None:
            self.images = m.get('Images')

        if m.get('NetworkConfig') is not None:
            temp_model = main_models.CreateImageCacheRequestNetworkConfig()
            self.network_config = temp_model.from_map(m.get('NetworkConfig'))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.CreateImageCacheRequestTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class CreateImageCacheRequestTags(DaraModel):
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
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class CreateImageCacheRequestNetworkConfig(DaraModel):
    def __init__(
        self,
        eip_instance: main_models.CreateImageCacheRequestNetworkConfigEipInstance = None,
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
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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
            temp_model = main_models.CreateImageCacheRequestNetworkConfigEipInstance()
            self.eip_instance = temp_model.from_map(m.get('EipInstance'))

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')

        return self

class CreateImageCacheRequestNetworkConfigEipInstance(DaraModel):
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
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class CreateImageCacheRequestImageRegistryCredentials(DaraModel):
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
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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



class CreateImageCacheRequestAcrRegistryInfos(DaraModel):
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
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

