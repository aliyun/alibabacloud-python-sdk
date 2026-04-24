# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class ListImagesResponseBody(DaraModel):
    def __init__(
        self,
        paging_info: main_models.ListImagesResponseBodyPagingInfo = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.paging_info = paging_info
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.paging_info:
            self.paging_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.paging_info is not None:
            result['PagingInfo'] = self.paging_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PagingInfo') is not None:
            temp_model = main_models.ListImagesResponseBodyPagingInfo()
            self.paging_info = temp_model.from_map(m.get('PagingInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListImagesResponseBodyPagingInfo(DaraModel):
    def __init__(
        self,
        image_list: List[main_models.ListImagesResponseBodyPagingInfoImageList] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.image_list = image_list
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.image_list:
            for v1 in self.image_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ImageList'] = []
        if self.image_list is not None:
            for k1 in self.image_list:
                result['ImageList'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.image_list = []
        if m.get('ImageList') is not None:
            for k1 in m.get('ImageList'):
                temp_model = main_models.ListImagesResponseBodyPagingInfoImageList()
                self.image_list.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListImagesResponseBodyPagingInfoImageList(DaraModel):
    def __init__(
        self,
        accessibility: str = None,
        acr_associated_vpc_id: str = None,
        acr_endpoint: str = None,
        acr_instance_id: str = None,
        build_config: main_models.ListImagesResponseBodyPagingInfoImageListBuildConfig = None,
        created_time: int = None,
        creator: str = None,
        description: str = None,
        enable_sync_max_compute: bool = None,
        id: str = None,
        image_tag: str = None,
        image_uri: str = None,
        image_vpc_uri: str = None,
        is_default: bool = None,
        last_modified_time: int = None,
        modifier: str = None,
        name: str = None,
        namespace: str = None,
        official: bool = None,
        provider_image_id: str = None,
        provider_type: str = None,
        publish_stage: str = None,
        repository_name: str = None,
        size: str = None,
        status: str = None,
        supported: main_models.ListImagesResponseBodyPagingInfoImageListSupported = None,
        version: str = None,
    ):
        self.accessibility = accessibility
        self.acr_associated_vpc_id = acr_associated_vpc_id
        # ACR Endpoint
        self.acr_endpoint = acr_endpoint
        self.acr_instance_id = acr_instance_id
        self.build_config = build_config
        self.created_time = created_time
        self.creator = creator
        self.description = description
        self.enable_sync_max_compute = enable_sync_max_compute
        self.id = id
        self.image_tag = image_tag
        self.image_uri = image_uri
        self.image_vpc_uri = image_vpc_uri
        self.is_default = is_default
        self.last_modified_time = last_modified_time
        self.modifier = modifier
        self.name = name
        self.namespace = namespace
        self.official = official
        self.provider_image_id = provider_image_id
        self.provider_type = provider_type
        self.publish_stage = publish_stage
        self.repository_name = repository_name
        self.size = size
        self.status = status
        self.supported = supported
        self.version = version

    def validate(self):
        if self.build_config:
            self.build_config.validate()
        if self.supported:
            self.supported.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility

        if self.acr_associated_vpc_id is not None:
            result['AcrAssociatedVpcId'] = self.acr_associated_vpc_id

        if self.acr_endpoint is not None:
            result['AcrEndpoint'] = self.acr_endpoint

        if self.acr_instance_id is not None:
            result['AcrInstanceId'] = self.acr_instance_id

        if self.build_config is not None:
            result['BuildConfig'] = self.build_config.to_map()

        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.description is not None:
            result['Description'] = self.description

        if self.enable_sync_max_compute is not None:
            result['EnableSyncMaxCompute'] = self.enable_sync_max_compute

        if self.id is not None:
            result['Id'] = self.id

        if self.image_tag is not None:
            result['ImageTag'] = self.image_tag

        if self.image_uri is not None:
            result['ImageUri'] = self.image_uri

        if self.image_vpc_uri is not None:
            result['ImageVpcUri'] = self.image_vpc_uri

        if self.is_default is not None:
            result['IsDefault'] = self.is_default

        if self.last_modified_time is not None:
            result['LastModifiedTime'] = self.last_modified_time

        if self.modifier is not None:
            result['Modifier'] = self.modifier

        if self.name is not None:
            result['Name'] = self.name

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.official is not None:
            result['Official'] = self.official

        if self.provider_image_id is not None:
            result['ProviderImageId'] = self.provider_image_id

        if self.provider_type is not None:
            result['ProviderType'] = self.provider_type

        if self.publish_stage is not None:
            result['PublishStage'] = self.publish_stage

        if self.repository_name is not None:
            result['RepositoryName'] = self.repository_name

        if self.size is not None:
            result['Size'] = self.size

        if self.status is not None:
            result['Status'] = self.status

        if self.supported is not None:
            result['Supported'] = self.supported.to_map()

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')

        if m.get('AcrAssociatedVpcId') is not None:
            self.acr_associated_vpc_id = m.get('AcrAssociatedVpcId')

        if m.get('AcrEndpoint') is not None:
            self.acr_endpoint = m.get('AcrEndpoint')

        if m.get('AcrInstanceId') is not None:
            self.acr_instance_id = m.get('AcrInstanceId')

        if m.get('BuildConfig') is not None:
            temp_model = main_models.ListImagesResponseBodyPagingInfoImageListBuildConfig()
            self.build_config = temp_model.from_map(m.get('BuildConfig'))

        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnableSyncMaxCompute') is not None:
            self.enable_sync_max_compute = m.get('EnableSyncMaxCompute')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('ImageTag') is not None:
            self.image_tag = m.get('ImageTag')

        if m.get('ImageUri') is not None:
            self.image_uri = m.get('ImageUri')

        if m.get('ImageVpcUri') is not None:
            self.image_vpc_uri = m.get('ImageVpcUri')

        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')

        if m.get('LastModifiedTime') is not None:
            self.last_modified_time = m.get('LastModifiedTime')

        if m.get('Modifier') is not None:
            self.modifier = m.get('Modifier')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('Official') is not None:
            self.official = m.get('Official')

        if m.get('ProviderImageId') is not None:
            self.provider_image_id = m.get('ProviderImageId')

        if m.get('ProviderType') is not None:
            self.provider_type = m.get('ProviderType')

        if m.get('PublishStage') is not None:
            self.publish_stage = m.get('PublishStage')

        if m.get('RepositoryName') is not None:
            self.repository_name = m.get('RepositoryName')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Supported') is not None:
            temp_model = main_models.ListImagesResponseBodyPagingInfoImageListSupported()
            self.supported = temp_model.from_map(m.get('Supported'))

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class ListImagesResponseBodyPagingInfoImageListSupported(DaraModel):
    def __init__(
        self,
        module: str = None,
        task_types: List[str] = None,
    ):
        self.module = module
        self.task_types = task_types

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.module is not None:
            result['Module'] = self.module

        if self.task_types is not None:
            result['TaskTypes'] = self.task_types

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Module') is not None:
            self.module = m.get('Module')

        if m.get('TaskTypes') is not None:
            self.task_types = m.get('TaskTypes')

        return self

class ListImagesResponseBodyPagingInfoImageListBuildConfig(DaraModel):
    def __init__(
        self,
        build_type: str = None,
        package_installation_scripts: List[main_models.ListImagesResponseBodyPagingInfoImageListBuildConfigPackageInstallationScripts] = None,
    ):
        self.build_type = build_type
        self.package_installation_scripts = package_installation_scripts

    def validate(self):
        if self.package_installation_scripts:
            for v1 in self.package_installation_scripts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.build_type is not None:
            result['BuildType'] = self.build_type

        result['PackageInstallationScripts'] = []
        if self.package_installation_scripts is not None:
            for k1 in self.package_installation_scripts:
                result['PackageInstallationScripts'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuildType') is not None:
            self.build_type = m.get('BuildType')

        self.package_installation_scripts = []
        if m.get('PackageInstallationScripts') is not None:
            for k1 in m.get('PackageInstallationScripts'):
                temp_model = main_models.ListImagesResponseBodyPagingInfoImageListBuildConfigPackageInstallationScripts()
                self.package_installation_scripts.append(temp_model.from_map(k1))

        return self

class ListImagesResponseBodyPagingInfoImageListBuildConfigPackageInstallationScripts(DaraModel):
    def __init__(
        self,
        content: str = None,
        type: str = None,
    ):
        self.content = content
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

