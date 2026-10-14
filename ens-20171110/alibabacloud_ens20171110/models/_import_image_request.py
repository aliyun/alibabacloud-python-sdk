# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class ImportImageRequest(DaraModel):
    def __init__(
        self,
        architecture: str = None,
        compute_type: str = None,
        disk_device_mapping: List[main_models.ImportImageRequestDiskDeviceMapping] = None,
        image_format: str = None,
        image_name: str = None,
        license_type: str = None,
        ossbucket: str = None,
        ossobject: str = None,
        ossregion: str = None,
        ostype: str = None,
        osversion: str = None,
        platform: str = None,
        target_ossregion_id: str = None,
    ):
        # The system architecture. Valid values:</br>
        # 
        # - x86_64
        # 
        # Currently, only x86_64 is supported.
        # 
        # This parameter is required.
        self.architecture = architecture
        # The image type. Valid values:
        # 
        # ens_vm: ENS virtual machine image (default).
        # 
        # This parameter is required.
        self.compute_type = compute_type
        # The list of custom image information.
        self.disk_device_mapping = disk_device_mapping
        # The image format. Valid values:</br>
        # qcow2.</br>
        # Currently, only qcow2 is supported.
        # 
        # This parameter is required.
        self.image_format = image_format
        # The image name. The name must be 2 to 128 characters in length and can contain letters, digits, colons (:), underscores (_), and hyphens (-). It must start with a letter and cannot start with http:// or https://.
        # 
        # This parameter is required.
        self.image_name = image_name
        # The image license type. Valid values: Aliyun (Alibaba Cloud license) and BYOL (Bring Your Own Key).
        self.license_type = license_type
        # The OSS bucket that stores the image file.
        self.ossbucket = ossbucket
        # The name of the image file.
        self.ossobject = ossobject
        # The region where the image resides. Currently, only cn-beijing is supported.
        self.ossregion = ossregion
        # The type of the operating system platform. Valid values:
        # 
        # - windows
        # - linux
        # 
        # Currently, only linux is supported.
        # 
        # This parameter is required.
        self.ostype = ostype
        # The version of the operating system distribution.
        self.osversion = osversion
        # The operating system distribution. Valid values:
        # * centos
        # * ubuntu
        self.platform = platform
        # The region of the destination OSS bucket where the image is stored.</br>
        # 
        # > Currently, only cn-beijing and ap-southeast-1 are supported.
        self.target_ossregion_id = target_ossregion_id

    def validate(self):
        if self.disk_device_mapping:
            for v1 in self.disk_device_mapping:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.architecture is not None:
            result['Architecture'] = self.architecture

        if self.compute_type is not None:
            result['ComputeType'] = self.compute_type

        result['DiskDeviceMapping'] = []
        if self.disk_device_mapping is not None:
            for k1 in self.disk_device_mapping:
                result['DiskDeviceMapping'].append(k1.to_map() if k1 else None)

        if self.image_format is not None:
            result['ImageFormat'] = self.image_format

        if self.image_name is not None:
            result['ImageName'] = self.image_name

        if self.license_type is not None:
            result['LicenseType'] = self.license_type

        if self.ossbucket is not None:
            result['OSSBucket'] = self.ossbucket

        if self.ossobject is not None:
            result['OSSObject'] = self.ossobject

        if self.ossregion is not None:
            result['OSSRegion'] = self.ossregion

        if self.ostype is not None:
            result['OSType'] = self.ostype

        if self.osversion is not None:
            result['OSVersion'] = self.osversion

        if self.platform is not None:
            result['Platform'] = self.platform

        if self.target_ossregion_id is not None:
            result['TargetOSSRegionId'] = self.target_ossregion_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Architecture') is not None:
            self.architecture = m.get('Architecture')

        if m.get('ComputeType') is not None:
            self.compute_type = m.get('ComputeType')

        self.disk_device_mapping = []
        if m.get('DiskDeviceMapping') is not None:
            for k1 in m.get('DiskDeviceMapping'):
                temp_model = main_models.ImportImageRequestDiskDeviceMapping()
                self.disk_device_mapping.append(temp_model.from_map(k1))

        if m.get('ImageFormat') is not None:
            self.image_format = m.get('ImageFormat')

        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')

        if m.get('LicenseType') is not None:
            self.license_type = m.get('LicenseType')

        if m.get('OSSBucket') is not None:
            self.ossbucket = m.get('OSSBucket')

        if m.get('OSSObject') is not None:
            self.ossobject = m.get('OSSObject')

        if m.get('OSSRegion') is not None:
            self.ossregion = m.get('OSSRegion')

        if m.get('OSType') is not None:
            self.ostype = m.get('OSType')

        if m.get('OSVersion') is not None:
            self.osversion = m.get('OSVersion')

        if m.get('Platform') is not None:
            self.platform = m.get('Platform')

        if m.get('TargetOSSRegionId') is not None:
            self.target_ossregion_id = m.get('TargetOSSRegionId')

        return self

class ImportImageRequestDiskDeviceMapping(DaraModel):
    def __init__(
        self,
        ossbucket: str = None,
        ossobject: str = None,
        ossregion: str = None,
    ):
        # The OSS bucket that stores the image.
        self.ossbucket = ossbucket
        # The file name (key) of the image file stored in the OSS bucket after the image is uploaded.
        self.ossobject = ossobject
        # The region where the image resides.
        self.ossregion = ossregion

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ossbucket is not None:
            result['OSSBucket'] = self.ossbucket

        if self.ossobject is not None:
            result['OSSObject'] = self.ossobject

        if self.ossregion is not None:
            result['OSSRegion'] = self.ossregion

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OSSBucket') is not None:
            self.ossbucket = m.get('OSSBucket')

        if m.get('OSSObject') is not None:
            self.ossobject = m.get('OSSObject')

        if m.get('OSSRegion') is not None:
            self.ossregion = m.get('OSSRegion')

        return self

