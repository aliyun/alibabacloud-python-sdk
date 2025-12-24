# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeImagesRequest(DaraModel):
    def __init__(
        self,
        desktop_instance_type: str = None,
        fota_version: str = None,
        gpu_category: bool = None,
        gpu_driver_version: str = None,
        image_id: List[str] = None,
        image_name: str = None,
        image_status: str = None,
        image_type: str = None,
        language_type: str = None,
        max_results: int = None,
        next_token: str = None,
        os_type: str = None,
        protocol_type: str = None,
        region_id: str = None,
        session_type: str = None,
    ):
        # The instance type of the cloud computer. You can call the [DescribeDesktopTypes](https://help.aliyun.com/document_detail/436816.html) operation to obtain the parameter value.
        self.desktop_instance_type = desktop_instance_type
        # The image version.
        self.fota_version = fota_version
        # Specifies whether the images are GPU-accelerated images.
        # 
        # Valid values:
        # 
        # *   true
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   false
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.gpu_category = gpu_category
        # The version of the GPU driver.
        self.gpu_driver_version = gpu_driver_version
        # The IDs of the images. You can specify one or more image IDs.
        self.image_id = image_id
        # The image name.
        self.image_name = image_name
        # The state of the image.
        self.image_status = image_status
        # The type of the image.
        self.image_type = image_type
        # The language of the OS.
        self.language_type = language_type
        # The maximum number of entries to return on each page.
        # 
        # *   Maximum value: 100.
        # *   Default value: 10.
        self.max_results = max_results
        # The token that determines the start point of the next query. If you do not specify this parameter, all results are returned.
        self.next_token = next_token
        # The type of the operating system of the images. Default value: `null`.
        # 
        # Valid values:
        # 
        # *   Linux
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Windows
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.os_type = os_type
        # The protocol type.
        # 
        # Valid values:
        # 
        # *   HDX: High-definition Experience (HDX) protocol
        # *   ASP: in-house Adaptive Streaming Protocol (ASP) (recommended)
        self.protocol_type = protocol_type
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/196646.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The session type.
        self.session_type = session_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desktop_instance_type is not None:
            result['DesktopInstanceType'] = self.desktop_instance_type

        if self.fota_version is not None:
            result['FotaVersion'] = self.fota_version

        if self.gpu_category is not None:
            result['GpuCategory'] = self.gpu_category

        if self.gpu_driver_version is not None:
            result['GpuDriverVersion'] = self.gpu_driver_version

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.image_name is not None:
            result['ImageName'] = self.image_name

        if self.image_status is not None:
            result['ImageStatus'] = self.image_status

        if self.image_type is not None:
            result['ImageType'] = self.image_type

        if self.language_type is not None:
            result['LanguageType'] = self.language_type

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.os_type is not None:
            result['OsType'] = self.os_type

        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.session_type is not None:
            result['SessionType'] = self.session_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopInstanceType') is not None:
            self.desktop_instance_type = m.get('DesktopInstanceType')

        if m.get('FotaVersion') is not None:
            self.fota_version = m.get('FotaVersion')

        if m.get('GpuCategory') is not None:
            self.gpu_category = m.get('GpuCategory')

        if m.get('GpuDriverVersion') is not None:
            self.gpu_driver_version = m.get('GpuDriverVersion')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')

        if m.get('ImageStatus') is not None:
            self.image_status = m.get('ImageStatus')

        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')

        if m.get('LanguageType') is not None:
            self.language_type = m.get('LanguageType')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')

        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SessionType') is not None:
            self.session_type = m.get('SessionType')

        return self

