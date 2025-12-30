# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ehpc20240730 import models as main_models
from darabonba.model import DaraModel

class ListAvailableImagesResponseBody(DaraModel):
    def __init__(
        self,
        images: List[main_models.ListAvailableImagesResponseBodyImages] = None,
        page_number: str = None,
        page_size: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: str = None,
    ):
        # The information about the images.
        self.images = images
        # The page number of the returned page.
        # 
        # *   Pages start from page 1.
        # *   Default value: 1.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request failed.
        self.success = success
        # The total number of entries returned.
        self.total_count = total_count

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

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.images = []
        if m.get('Images') is not None:
            for k1 in m.get('Images'):
                temp_model = main_models.ListAvailableImagesResponseBodyImages()
                self.images.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListAvailableImagesResponseBodyImages(DaraModel):
    def __init__(
        self,
        architecture: str = None,
        boot_mode: str = None,
        description: str = None,
        image_id: str = None,
        image_name: str = None,
        image_owner_alias: str = None,
        osname: str = None,
        osname_en: str = None,
        platform: str = None,
        size: str = None,
    ):
        # The OS architecture of the image. Valid values:
        # 
        # *   x86_64
        # *   arm64
        self.architecture = architecture
        # The boot mode of the image. Valid values:
        # 
        # *   BIOS: Basic Input/Output System (BIOS).
        # *   UEFI: Unified Extensible Firmware Interface (UEFI).
        # 
        # >  When you change the OS boot mode of an instance, you must make sure that the boot mode matches the boot mode of the associated image. Otherwise, the instance fails to be booted.
        self.boot_mode = boot_mode
        # The image description.
        self.description = description
        # The image ID.
        self.image_id = image_id
        # The image name.
        self.image_name = image_name
        # The image source. Valid values:
        # 
        # *   system: system image.
        # *   self: custom image.
        # *   others: shared image.
        self.image_owner_alias = image_owner_alias
        # The OS name in Chinese.
        self.osname = osname
        # The OS name in English.
        self.osname_en = osname_en
        # The OS. Valid values:
        # 
        # *   CentOS
        # *   windows
        self.platform = platform
        # The image size. Unit: GiB
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.architecture is not None:
            result['Architecture'] = self.architecture

        if self.boot_mode is not None:
            result['BootMode'] = self.boot_mode

        if self.description is not None:
            result['Description'] = self.description

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.image_name is not None:
            result['ImageName'] = self.image_name

        if self.image_owner_alias is not None:
            result['ImageOwnerAlias'] = self.image_owner_alias

        if self.osname is not None:
            result['OSName'] = self.osname

        if self.osname_en is not None:
            result['OSNameEn'] = self.osname_en

        if self.platform is not None:
            result['Platform'] = self.platform

        if self.size is not None:
            result['Size'] = self.size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Architecture') is not None:
            self.architecture = m.get('Architecture')

        if m.get('BootMode') is not None:
            self.boot_mode = m.get('BootMode')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')

        if m.get('ImageOwnerAlias') is not None:
            self.image_owner_alias = m.get('ImageOwnerAlias')

        if m.get('OSName') is not None:
            self.osname = m.get('OSName')

        if m.get('OSNameEn') is not None:
            self.osname_en = m.get('OSNameEn')

        if m.get('Platform') is not None:
            self.platform = m.get('Platform')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        return self

