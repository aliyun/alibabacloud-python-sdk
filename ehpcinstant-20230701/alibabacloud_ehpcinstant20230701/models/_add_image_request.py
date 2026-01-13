# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ehpcinstant20230701 import models as main_models
from darabonba.model import DaraModel

class AddImageRequest(DaraModel):
    def __init__(
        self,
        container_image_spec: main_models.AddImageRequestContainerImageSpec = None,
        description: str = None,
        image_type: str = None,
        image_version: str = None,
        name: str = None,
        vmimage_spec: main_models.AddImageRequestVMImageSpec = None,
    ):
        # The configurations of the container image.
        self.container_image_spec = container_image_spec
        # The description of the image.
        self.description = description
        # The type of the images. Valid values:
        # 
        # *   VM: virtual machine image.
        # *   Container: the container image.
        self.image_type = image_type
        # The version of the image.
        self.image_version = image_version
        # The name of the custom image.
        # 
        # This parameter is required.
        self.name = name
        # The image configuration of the virtual machine.
        self.vmimage_spec = vmimage_spec

    def validate(self):
        if self.container_image_spec:
            self.container_image_spec.validate()
        if self.vmimage_spec:
            self.vmimage_spec.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.container_image_spec is not None:
            result['ContainerImageSpec'] = self.container_image_spec.to_map()

        if self.description is not None:
            result['Description'] = self.description

        if self.image_type is not None:
            result['ImageType'] = self.image_type

        if self.image_version is not None:
            result['ImageVersion'] = self.image_version

        if self.name is not None:
            result['Name'] = self.name

        if self.vmimage_spec is not None:
            result['VMImageSpec'] = self.vmimage_spec.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContainerImageSpec') is not None:
            temp_model = main_models.AddImageRequestContainerImageSpec()
            self.container_image_spec = temp_model.from_map(m.get('ContainerImageSpec'))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')

        if m.get('ImageVersion') is not None:
            self.image_version = m.get('ImageVersion')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('VMImageSpec') is not None:
            temp_model = main_models.AddImageRequestVMImageSpec()
            self.vmimage_spec = temp_model.from_map(m.get('VMImageSpec'))

        return self

class AddImageRequestVMImageSpec(DaraModel):
    def __init__(
        self,
        image_id: str = None,
    ):
        # The image ID.
        self.image_id = image_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_id is not None:
            result['ImageId'] = self.image_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        return self

class AddImageRequestContainerImageSpec(DaraModel):
    def __init__(
        self,
        is_acrenterprise: bool = None,
        is_acrregistry: bool = None,
        registry_credential: main_models.AddImageRequestContainerImageSpecRegistryCredential = None,
        registry_cri_id: str = None,
        registry_url: str = None,
    ):
        # Whether the instance is an Alibaba Cloud image repository Enterprise Edition.
        # 
        # *   True
        # *   False
        self.is_acrenterprise = is_acrenterprise
        # Whether it is an Alibaba Cloud image repository.
        # 
        # *   True
        # *   False
        self.is_acrregistry = is_acrregistry
        # The authentication of the private image repository.
        self.registry_credential = registry_credential
        # The ID of the Container Registry Enterprise Edition image repository.
        self.registry_cri_id = registry_cri_id
        # The endpoint of the container image.
        self.registry_url = registry_url

    def validate(self):
        if self.registry_credential:
            self.registry_credential.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_acrenterprise is not None:
            result['IsACREnterprise'] = self.is_acrenterprise

        if self.is_acrregistry is not None:
            result['IsACRRegistry'] = self.is_acrregistry

        if self.registry_credential is not None:
            result['RegistryCredential'] = self.registry_credential.to_map()

        if self.registry_cri_id is not None:
            result['RegistryCriId'] = self.registry_cri_id

        if self.registry_url is not None:
            result['RegistryUrl'] = self.registry_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsACREnterprise') is not None:
            self.is_acrenterprise = m.get('IsACREnterprise')

        if m.get('IsACRRegistry') is not None:
            self.is_acrregistry = m.get('IsACRRegistry')

        if m.get('RegistryCredential') is not None:
            temp_model = main_models.AddImageRequestContainerImageSpecRegistryCredential()
            self.registry_credential = temp_model.from_map(m.get('RegistryCredential'))

        if m.get('RegistryCriId') is not None:
            self.registry_cri_id = m.get('RegistryCriId')

        if m.get('RegistryUrl') is not None:
            self.registry_url = m.get('RegistryUrl')

        return self



class AddImageRequestContainerImageSpecRegistryCredential(DaraModel):
    def __init__(
        self,
        password: str = None,
        server: str = None,
        user_name: str = None,
    ):
        # The password of the logon user.
        self.password = password
        # The registered address of the image repository.
        self.server = server
        # The username of the logon user.
        self.user_name = user_name

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

