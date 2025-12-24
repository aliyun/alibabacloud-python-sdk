# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class DescribeImagesResponseBody(DaraModel):
    def __init__(
        self,
        images: List[main_models.DescribeImagesResponseBodyImages] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The details of the images.
        self.images = images
        # The token that determines the start point of the next query. If this parameter is empty, all results are returned.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.images:
            for v1 in self.images:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Images'] = []
        if self.images is not None:
            for k1 in self.images:
                result['Images'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.images = []
        if m.get('Images') is not None:
            for k1 in m.get('Images'):
                temp_model = main_models.DescribeImagesResponseBodyImages()
                self.images.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeImagesResponseBodyImages(DaraModel):
    def __init__(
        self,
        app_version: str = None,
        creation_time: str = None,
        data_disk_size: int = None,
        description: str = None,
        gpu_category: bool = None,
        gpu_driver_version: str = None,
        image_id: str = None,
        image_type: str = None,
        name: str = None,
        os_type: str = None,
        platform: str = None,
        progress: str = None,
        protocol_type: str = None,
        session_type: str = None,
        shared_count: int = None,
        size: int = None,
        status: str = None,
        supported_languages: List[str] = None,
        update_time: str = None,
        volume_encryption_enabled: bool = None,
        volume_encryption_key: str = None,
    ):
        # The version of the image.
        self.app_version = app_version
        # The time when the image was created.
        self.creation_time = creation_time
        # The size of the data disk. Unit: GiB.
        self.data_disk_size = data_disk_size
        # The description of the image.
        self.description = description
        # Indicates whether the image is a GPU-accelerated image.
        self.gpu_category = gpu_category
        # The version number of the GPU driver.
        self.gpu_driver_version = gpu_driver_version
        # The ID of the image.
        self.image_id = image_id
        # The type of the image.
        # 
        # Valid values:
        # 
        # *   SYSTEM
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   CUSTOM
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.image_type = image_type
        # The name of the image.
        self.name = name
        # The type of the operating system.
        self.os_type = os_type
        # The operating system type of the image.
        # 
        # Valid values:
        # 
        # *   Ubuntu
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Windows Server 2022
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   UOS
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   CentOS
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Windows Server 2019
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   SQL Server 2016
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Windows 10
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.platform = platform
        # The creation progress of the image. Unit: %.
        self.progress = progress
        # The protocol type.
        # 
        # Valid values:
        # 
        # *   HDX: High-definition Experience (HDX) protocol
        # *   ASP: in-house Adaptive Streaming Protocol (ASP) (recommended)
        self.protocol_type = protocol_type
        # The type of the image session.
        # 
        # Valid values:
        # 
        # *   SINGLE_SESSION: single-session image.
        # 
        # *   MULTIPLE_SESSION: multi-session image.
        self.session_type = session_type
        # The number of shared images.
        self.shared_count = shared_count
        # The size of the image. Unit: GiB.
        self.size = size
        # The status of the image.
        # 
        # Valid values:
        # 
        # *   Creating
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Available
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   CreateFailed
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.status = status
        # The languages of the operating system.
        self.supported_languages = supported_languages
        # The time when the image was last modified.
        self.update_time = update_time
        # Indicates whether disk encryption is enabled.
        self.volume_encryption_enabled = volume_encryption_enabled
        # The ID of the Key Management Service (KMS) key that is used when disk encryption is enabled. You can call the [ListKeys](https://help.aliyun.com/document_detail/28951.html) operation to query the list of KMS keys.
        self.volume_encryption_key = volume_encryption_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_version is not None:
            result['AppVersion'] = self.app_version

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.data_disk_size is not None:
            result['DataDiskSize'] = self.data_disk_size

        if self.description is not None:
            result['Description'] = self.description

        if self.gpu_category is not None:
            result['GpuCategory'] = self.gpu_category

        if self.gpu_driver_version is not None:
            result['GpuDriverVersion'] = self.gpu_driver_version

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.image_type is not None:
            result['ImageType'] = self.image_type

        if self.name is not None:
            result['Name'] = self.name

        if self.os_type is not None:
            result['OsType'] = self.os_type

        if self.platform is not None:
            result['Platform'] = self.platform

        if self.progress is not None:
            result['Progress'] = self.progress

        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type

        if self.session_type is not None:
            result['SessionType'] = self.session_type

        if self.shared_count is not None:
            result['SharedCount'] = self.shared_count

        if self.size is not None:
            result['Size'] = self.size

        if self.status is not None:
            result['Status'] = self.status

        if self.supported_languages is not None:
            result['SupportedLanguages'] = self.supported_languages

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.volume_encryption_enabled is not None:
            result['VolumeEncryptionEnabled'] = self.volume_encryption_enabled

        if self.volume_encryption_key is not None:
            result['VolumeEncryptionKey'] = self.volume_encryption_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('DataDiskSize') is not None:
            self.data_disk_size = m.get('DataDiskSize')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GpuCategory') is not None:
            self.gpu_category = m.get('GpuCategory')

        if m.get('GpuDriverVersion') is not None:
            self.gpu_driver_version = m.get('GpuDriverVersion')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')

        if m.get('Platform') is not None:
            self.platform = m.get('Platform')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')

        if m.get('SessionType') is not None:
            self.session_type = m.get('SessionType')

        if m.get('SharedCount') is not None:
            self.shared_count = m.get('SharedCount')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SupportedLanguages') is not None:
            self.supported_languages = m.get('SupportedLanguages')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('VolumeEncryptionEnabled') is not None:
            self.volume_encryption_enabled = m.get('VolumeEncryptionEnabled')

        if m.get('VolumeEncryptionKey') is not None:
            self.volume_encryption_key = m.get('VolumeEncryptionKey')

        return self

