# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_acc20240402 import models as main_models
from darabonba.model import DaraModel

class CreateImageCacheShrinkRequest(DaraModel):
    def __init__(
        self,
        acr_registry_infos: List[main_models.CreateImageCacheShrinkRequestAcrRegistryInfos] = None,
        client_token: str = None,
        image_cache_name: str = None,
        image_registry_credentials: List[main_models.CreateImageCacheShrinkRequestImageRegistryCredentials] = None,
        images: List[str] = None,
        network_config_shrink: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        tags: List[main_models.CreateImageCacheShrinkRequestTags] = None,
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
            for v1 in self.acr_registry_infos:
                 if v1:
                    v1.validate()
        if self.image_registry_credentials:
            for v1 in self.image_registry_credentials:
                 if v1:
                    v1.validate()
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

        if self.network_config_shrink is not None:
            result['NetworkConfig'] = self.network_config_shrink

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
                temp_model = main_models.CreateImageCacheShrinkRequestAcrRegistryInfos()
                self.acr_registry_infos.append(temp_model.from_map(k1))

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ImageCacheName') is not None:
            self.image_cache_name = m.get('ImageCacheName')

        self.image_registry_credentials = []
        if m.get('ImageRegistryCredentials') is not None:
            for k1 in m.get('ImageRegistryCredentials'):
                temp_model = main_models.CreateImageCacheShrinkRequestImageRegistryCredentials()
                self.image_registry_credentials.append(temp_model.from_map(k1))

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
            for k1 in m.get('Tags'):
                temp_model = main_models.CreateImageCacheShrinkRequestTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class CreateImageCacheShrinkRequestTags(DaraModel):
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

class CreateImageCacheShrinkRequestImageRegistryCredentials(DaraModel):
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

class CreateImageCacheShrinkRequestAcrRegistryInfos(DaraModel):
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

