# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ehpcinstant20230701 import models as main_models
from darabonba.model import DaraModel

class GetImageResponseBody(DaraModel):
    def __init__(
        self,
        image: main_models.GetImageResponseBodyImage = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The details of the image.
        self.image = image
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true: The task is successful.
        # *   false: The error occurred.
        self.success = success
        # The total amount of data in this request.
        self.total_count = total_count

    def validate(self):
        if self.image:
            self.image.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image is not None:
            result['Image'] = self.image.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Image') is not None:
            temp_model = main_models.GetImageResponseBodyImage()
            self.image = temp_model.from_map(m.get('Image'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class GetImageResponseBodyImage(DaraModel):
    def __init__(
        self,
        additional_regions_info: List[main_models.GetImageResponseBodyImageAdditionalRegionsInfo] = None,
        app_id: str = None,
        container_image_spec: main_models.GetImageResponseBodyImageContainerImageSpec = None,
        create_time: str = None,
        description: str = None,
        document_info: main_models.GetImageResponseBodyImageDocumentInfo = None,
        image_type: str = None,
        name: str = None,
        size: str = None,
        status: str = None,
        vmimage_spec: main_models.GetImageResponseBodyImageVMImageSpec = None,
        version: str = None,
    ):
        self.additional_regions_info = additional_regions_info
        self.app_id = app_id
        # The configuration details of the container image.
        self.container_image_spec = container_image_spec
        # The time when the image was created.
        self.create_time = create_time
        # The description of the image.
        self.description = description
        self.document_info = document_info
        # The type of the image.
        # 
        # This parameter is required.
        self.image_type = image_type
        # The name of the image.
        self.name = name
        # The size of the image. Unit: GiB.
        self.size = size
        self.status = status
        # The configuration details of the virtual machine image.
        self.vmimage_spec = vmimage_spec
        # The version.
        self.version = version

    def validate(self):
        if self.additional_regions_info:
            for v1 in self.additional_regions_info:
                 if v1:
                    v1.validate()
        if self.container_image_spec:
            self.container_image_spec.validate()
        if self.document_info:
            self.document_info.validate()
        if self.vmimage_spec:
            self.vmimage_spec.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AdditionalRegionsInfo'] = []
        if self.additional_regions_info is not None:
            for k1 in self.additional_regions_info:
                result['AdditionalRegionsInfo'].append(k1.to_map() if k1 else None)

        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.container_image_spec is not None:
            result['ContainerImageSpec'] = self.container_image_spec.to_map()

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.document_info is not None:
            result['DocumentInfo'] = self.document_info.to_map()

        if self.image_type is not None:
            result['ImageType'] = self.image_type

        if self.name is not None:
            result['Name'] = self.name

        if self.size is not None:
            result['Size'] = self.size

        if self.status is not None:
            result['Status'] = self.status

        if self.vmimage_spec is not None:
            result['VMImageSpec'] = self.vmimage_spec.to_map()

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.additional_regions_info = []
        if m.get('AdditionalRegionsInfo') is not None:
            for k1 in m.get('AdditionalRegionsInfo'):
                temp_model = main_models.GetImageResponseBodyImageAdditionalRegionsInfo()
                self.additional_regions_info.append(temp_model.from_map(k1))

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('ContainerImageSpec') is not None:
            temp_model = main_models.GetImageResponseBodyImageContainerImageSpec()
            self.container_image_spec = temp_model.from_map(m.get('ContainerImageSpec'))

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DocumentInfo') is not None:
            temp_model = main_models.GetImageResponseBodyImageDocumentInfo()
            self.document_info = temp_model.from_map(m.get('DocumentInfo'))

        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('VMImageSpec') is not None:
            temp_model = main_models.GetImageResponseBodyImageVMImageSpec()
            self.vmimage_spec = temp_model.from_map(m.get('VMImageSpec'))

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class GetImageResponseBodyImageVMImageSpec(DaraModel):
    def __init__(
        self,
        architecture: str = None,
        image_id: str = None,
        os_tag: str = None,
        platform: str = None,
    ):
        # The type of the architecture.
        self.architecture = architecture
        # The image ID.
        self.image_id = image_id
        # The ID of the specific OS version.
        self.os_tag = os_tag
        # The type of the platform.
        self.platform = platform

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.architecture is not None:
            result['Architecture'] = self.architecture

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.os_tag is not None:
            result['OsTag'] = self.os_tag

        if self.platform is not None:
            result['Platform'] = self.platform

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Architecture') is not None:
            self.architecture = m.get('Architecture')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('OsTag') is not None:
            self.os_tag = m.get('OsTag')

        if m.get('Platform') is not None:
            self.platform = m.get('Platform')

        return self

class GetImageResponseBodyImageDocumentInfo(DaraModel):
    def __init__(
        self,
        document: str = None,
        document_id: str = None,
        encoding_mode: str = None,
    ):
        self.document = document
        self.document_id = document_id
        self.encoding_mode = encoding_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.document is not None:
            result['Document'] = self.document

        if self.document_id is not None:
            result['DocumentId'] = self.document_id

        if self.encoding_mode is not None:
            result['EncodingMode'] = self.encoding_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Document') is not None:
            self.document = m.get('Document')

        if m.get('DocumentId') is not None:
            self.document_id = m.get('DocumentId')

        if m.get('EncodingMode') is not None:
            self.encoding_mode = m.get('EncodingMode')

        return self

class GetImageResponseBodyImageContainerImageSpec(DaraModel):
    def __init__(
        self,
        architecture: str = None,
        is_acrenterprise: bool = None,
        is_acrregistry: bool = None,
        os_tag: str = None,
        platform: str = None,
        registry_credential: main_models.GetImageResponseBodyImageContainerImageSpecRegistryCredential = None,
        registry_cri_id: str = None,
        registry_url: str = None,
    ):
        self.architecture = architecture
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
        self.os_tag = os_tag
        self.platform = platform
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
        if self.architecture is not None:
            result['Architecture'] = self.architecture

        if self.is_acrenterprise is not None:
            result['IsACREnterprise'] = self.is_acrenterprise

        if self.is_acrregistry is not None:
            result['IsACRRegistry'] = self.is_acrregistry

        if self.os_tag is not None:
            result['OsTag'] = self.os_tag

        if self.platform is not None:
            result['Platform'] = self.platform

        if self.registry_credential is not None:
            result['RegistryCredential'] = self.registry_credential.to_map()

        if self.registry_cri_id is not None:
            result['RegistryCriId'] = self.registry_cri_id

        if self.registry_url is not None:
            result['RegistryUrl'] = self.registry_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Architecture') is not None:
            self.architecture = m.get('Architecture')

        if m.get('IsACREnterprise') is not None:
            self.is_acrenterprise = m.get('IsACREnterprise')

        if m.get('IsACRRegistry') is not None:
            self.is_acrregistry = m.get('IsACRRegistry')

        if m.get('OsTag') is not None:
            self.os_tag = m.get('OsTag')

        if m.get('Platform') is not None:
            self.platform = m.get('Platform')

        if m.get('RegistryCredential') is not None:
            temp_model = main_models.GetImageResponseBodyImageContainerImageSpecRegistryCredential()
            self.registry_credential = temp_model.from_map(m.get('RegistryCredential'))

        if m.get('RegistryCriId') is not None:
            self.registry_cri_id = m.get('RegistryCriId')

        if m.get('RegistryUrl') is not None:
            self.registry_url = m.get('RegistryUrl')

        return self

class GetImageResponseBodyImageContainerImageSpecRegistryCredential(DaraModel):
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

class GetImageResponseBodyImageAdditionalRegionsInfo(DaraModel):
    def __init__(
        self,
        image_id: str = None,
        region_id: str = None,
        status: str = None,
    ):
        self.image_id = image_id
        self.region_id = region_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

