# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class UpdateImageRequest(DaraModel):
    def __init__(
        self,
        accessibility: str = None,
        acr_associated_vpc_id: str = None,
        acr_instance_id: str = None,
        build_config: main_models.UpdateImageRequestBuildConfig = None,
        description: str = None,
        id: str = None,
        image_uri: str = None,
        name: str = None,
        namespace: str = None,
        provider_image_id: str = None,
        repository_name: str = None,
        supported: main_models.UpdateImageRequestSupported = None,
    ):
        # The image visibility. Valid values:
        # - Public: visible to all users.
        # - Private: visible only to the creator.
        self.accessibility = accessibility
        # The VPC ID associated with the ACR instance. This parameter is required when referencing an ACR image.
        self.acr_associated_vpc_id = acr_associated_vpc_id
        # The Container Registry (ACR) instance ID. This parameter is required when referencing an ACR image.
        self.acr_instance_id = acr_instance_id
        # The image build configuration.
        self.build_config = build_config
        # The image description.
        self.description = description
        # The image ID.
        # 
        # This parameter is required.
        self.id = id
        # The image URI. This parameter is required when referencing an ACR image.
        self.image_uri = image_uri
        # The image name.
        self.name = name
        # The image namespace. Set this parameter to DataWorks Default when referencing a DataWorks official image.
        self.namespace = namespace
        # The provider image ID. This parameter is required when referencing a DataWorks official image.
        self.provider_image_id = provider_image_id
        # The image repository name. Set this parameter to DataWorks Default when referencing a DataWorks official image.
        self.repository_name = repository_name
        # The image sub-purpose.
        self.supported = supported

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

        if self.acr_instance_id is not None:
            result['AcrInstanceId'] = self.acr_instance_id

        if self.build_config is not None:
            result['BuildConfig'] = self.build_config.to_map()

        if self.description is not None:
            result['Description'] = self.description

        if self.id is not None:
            result['Id'] = self.id

        if self.image_uri is not None:
            result['ImageUri'] = self.image_uri

        if self.name is not None:
            result['Name'] = self.name

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.provider_image_id is not None:
            result['ProviderImageId'] = self.provider_image_id

        if self.repository_name is not None:
            result['RepositoryName'] = self.repository_name

        if self.supported is not None:
            result['Supported'] = self.supported.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')

        if m.get('AcrAssociatedVpcId') is not None:
            self.acr_associated_vpc_id = m.get('AcrAssociatedVpcId')

        if m.get('AcrInstanceId') is not None:
            self.acr_instance_id = m.get('AcrInstanceId')

        if m.get('BuildConfig') is not None:
            temp_model = main_models.UpdateImageRequestBuildConfig()
            self.build_config = temp_model.from_map(m.get('BuildConfig'))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('ImageUri') is not None:
            self.image_uri = m.get('ImageUri')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('ProviderImageId') is not None:
            self.provider_image_id = m.get('ProviderImageId')

        if m.get('RepositoryName') is not None:
            self.repository_name = m.get('RepositoryName')

        if m.get('Supported') is not None:
            temp_model = main_models.UpdateImageRequestSupported()
            self.supported = temp_model.from_map(m.get('Supported'))

        return self

class UpdateImageRequestSupported(DaraModel):
    def __init__(
        self,
        module: str = None,
        task_types: List[str] = None,
    ):
        # The image sub-module. Valid values:
        # - Scheduler: data development.
        self.module = module
        # The list of node types supported by the image.
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

class UpdateImageRequestBuildConfig(DaraModel):
    def __init__(
        self,
        build_type: str = None,
        package_installation_scripts: List[main_models.UpdateImageRequestBuildConfigPackageInstallationScripts] = None,
    ):
        # The build type.
        self.build_type = build_type
        # The list of pre-installation scripts.
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
                temp_model = main_models.UpdateImageRequestBuildConfigPackageInstallationScripts()
                self.package_installation_scripts.append(temp_model.from_map(k1))

        return self

class UpdateImageRequestBuildConfigPackageInstallationScripts(DaraModel):
    def __init__(
        self,
        content: str = None,
        type: str = None,
    ):
        # The script content. If the content consists of package names, separate them with commas (,).
        self.content = content
        # The script type.
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

