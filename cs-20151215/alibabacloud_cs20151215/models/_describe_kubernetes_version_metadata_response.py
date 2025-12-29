# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List, Any

from alibabacloud_cs20151215 import models as main_models
from darabonba.model import DaraModel

class DescribeKubernetesVersionMetadataResponse(DaraModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: List[main_models.DescribeKubernetesVersionMetadataResponseBody] = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            for v1 in self.body:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.headers is not None:
            result['headers'] = self.headers

        if self.status_code is not None:
            result['statusCode'] = self.status_code

        result['body'] = []
        if self.body is not None:
            for k1 in self.body:
                result['body'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')

        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')

        self.body = []
        if m.get('body') is not None:
            for k1 in m.get('body'):
                temp_model = main_models.DescribeKubernetesVersionMetadataResponseBody()
                self.body.append(temp_model.from_map(k1))

        return self

class DescribeKubernetesVersionMetadataResponseBody(DaraModel):
    def __init__(
        self,
        capabilities: Dict[str, Any] = None,
        images: List[main_models.DescribeKubernetesVersionMetadataResponseBodyImages] = None,
        meta_data: Dict[str, Any] = None,
        runtimes: List[main_models.Runtime] = None,
        version: str = None,
        release_date: str = None,
        expiration_date: str = None,
        creatable: bool = None,
        upgradable_versions: List[str] = None,
    ):
        # Features of the queried Kubernetes version.
        self.capabilities = capabilities
        # The OS images that are returned.
        self.images = images
        # The metadata of the Kubernetes version.
        self.meta_data = meta_data
        # The container runtime configurations.
        self.runtimes = runtimes
        # The Kubernetes version supported by ACK. For more information, see [Release notes for Kubernetes versions](https://help.aliyun.com/document_detail/185269.html).
        self.version = version
        # The release date of the Kubernetes version.
        self.release_date = release_date
        # The expiration date of the Kubernetes version.
        self.expiration_date = expiration_date
        # Indicates whether you can create clusters that run the Kubernetes version.
        self.creatable = creatable
        # The list of available Kubernetes versions for updates.
        self.upgradable_versions = upgradable_versions

    def validate(self):
        if self.images:
            for v1 in self.images:
                 if v1:
                    v1.validate()
        if self.runtimes:
            for v1 in self.runtimes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.capabilities is not None:
            result['capabilities'] = self.capabilities

        result['images'] = []
        if self.images is not None:
            for k1 in self.images:
                result['images'].append(k1.to_map() if k1 else None)

        if self.meta_data is not None:
            result['meta_data'] = self.meta_data

        result['runtimes'] = []
        if self.runtimes is not None:
            for k1 in self.runtimes:
                result['runtimes'].append(k1.to_map() if k1 else None)

        if self.version is not None:
            result['version'] = self.version

        if self.release_date is not None:
            result['release_date'] = self.release_date

        if self.expiration_date is not None:
            result['expiration_date'] = self.expiration_date

        if self.creatable is not None:
            result['creatable'] = self.creatable

        if self.upgradable_versions is not None:
            result['upgradable_versions'] = self.upgradable_versions

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('capabilities') is not None:
            self.capabilities = m.get('capabilities')

        self.images = []
        if m.get('images') is not None:
            for k1 in m.get('images'):
                temp_model = main_models.DescribeKubernetesVersionMetadataResponseBodyImages()
                self.images.append(temp_model.from_map(k1))

        if m.get('meta_data') is not None:
            self.meta_data = m.get('meta_data')

        self.runtimes = []
        if m.get('runtimes') is not None:
            for k1 in m.get('runtimes'):
                temp_model = main_models.Runtime()
                self.runtimes.append(temp_model.from_map(k1))

        if m.get('version') is not None:
            self.version = m.get('version')

        if m.get('release_date') is not None:
            self.release_date = m.get('release_date')

        if m.get('expiration_date') is not None:
            self.expiration_date = m.get('expiration_date')

        if m.get('creatable') is not None:
            self.creatable = m.get('creatable')

        if m.get('upgradable_versions') is not None:
            self.upgradable_versions = m.get('upgradable_versions')

        return self

class DescribeKubernetesVersionMetadataResponseBodyImages(DaraModel):
    def __init__(
        self,
        image_id: str = None,
        image_name: str = None,
        platform: str = None,
        os_version: str = None,
        image_type: str = None,
        os_type: str = None,
        image_category: str = None,
        architecture: str = None,
    ):
        # The ID of the image.
        self.image_id = image_id
        # The image name.
        self.image_name = image_name
        # The OS platform. You can obtain the terminal ID by calling one of the following operations:
        # 
        # *   `AliyunLinux`
        # *   `CentOS`
        # *   `Windows`
        # *   `WindowsCore`
        self.platform = platform
        # The version of the image.
        self.os_version = os_version
        # The type of operating system distribution that you want to use. We recommend that you use this parameter to specify the node operating system. You can obtain the terminal ID by calling one of the following operations:
        # 
        # *   `CentOS`
        # *   `AliyunLinux`
        # *   `AliyunLinux Qboot`
        # *   `AliyunLinuxUEFI`
        # *   `AliyunLinux3`
        # *   `Windows`
        # *   `WindowsCore`
        # *   `AliyunLinux3Arm64`
        # *   `ContainerOS`
        self.image_type = image_type
        # The type of OS. Examples:
        # 
        # *   `Windows`
        # *   `Linux`
        self.os_type = os_type
        # The type of image. Valid values:
        # 
        # *   `system`: public image
        # *   `self`: custom image
        # *   `others`: shared image from other Alibaba Cloud accounts
        # *   `marketplace`: image from the marketplace
        self.image_category = image_category
        # The architecture of the image.
        self.architecture = architecture

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_id is not None:
            result['image_id'] = self.image_id

        if self.image_name is not None:
            result['image_name'] = self.image_name

        if self.platform is not None:
            result['platform'] = self.platform

        if self.os_version is not None:
            result['os_version'] = self.os_version

        if self.image_type is not None:
            result['image_type'] = self.image_type

        if self.os_type is not None:
            result['os_type'] = self.os_type

        if self.image_category is not None:
            result['image_category'] = self.image_category

        if self.architecture is not None:
            result['architecture'] = self.architecture

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('image_id') is not None:
            self.image_id = m.get('image_id')

        if m.get('image_name') is not None:
            self.image_name = m.get('image_name')

        if m.get('platform') is not None:
            self.platform = m.get('platform')

        if m.get('os_version') is not None:
            self.os_version = m.get('os_version')

        if m.get('image_type') is not None:
            self.image_type = m.get('image_type')

        if m.get('os_type') is not None:
            self.os_type = m.get('os_type')

        if m.get('image_category') is not None:
            self.image_category = m.get('image_category')

        if m.get('architecture') is not None:
            self.architecture = m.get('architecture')

        return self

