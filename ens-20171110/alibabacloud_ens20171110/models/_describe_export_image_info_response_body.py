# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class DescribeExportImageInfoResponseBody(DaraModel):
    def __init__(
        self,
        images: main_models.DescribeExportImageInfoResponseBodyImages = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The returned result. For more information, see the Images parameter described in the JSON-formatted sample success response.
        self.images = images
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.images:
            self.images.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.images is not None:
            result['Images'] = self.images.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Images') is not None:
            temp_model = main_models.DescribeExportImageInfoResponseBodyImages()
            self.images = temp_model.from_map(m.get('Images'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeExportImageInfoResponseBodyImages(DaraModel):
    def __init__(
        self,
        image: List[main_models.DescribeExportImageInfoResponseBodyImagesImage] = None,
    ):
        self.image = image

    def validate(self):
        if self.image:
            for v1 in self.image:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Image'] = []
        if self.image is not None:
            for k1 in self.image:
                result['Image'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.image = []
        if m.get('Image') is not None:
            for k1 in m.get('Image'):
                temp_model = main_models.DescribeExportImageInfoResponseBodyImagesImage()
                self.image.append(temp_model.from_map(k1))

        return self

class DescribeExportImageInfoResponseBodyImagesImage(DaraModel):
    def __init__(
        self,
        architecture: str = None,
        creation_time: str = None,
        exported_image_url: str = None,
        image_export_status: str = None,
        image_id: str = None,
        image_name: str = None,
        image_owner_alias: str = None,
        platform: str = None,
    ):
        # The architecture of the image. Example: **x86_64**.
        self.architecture = architecture
        # The time when the image was created.
        self.creation_time = creation_time
        # The URL of the exported image.
        self.exported_image_url = exported_image_url
        # The export status of the image. Valid values:
        # 
        # *   Exporting
        # *   Exported
        # *   ExportError
        # *   Unexported
        self.image_export_status = image_export_status
        # The ID of the image.
        self.image_id = image_id
        # The name of the image.
        self.image_name = image_name
        # The source of the image. Valid values:
        # 
        # *   system: public image
        # *   self: custom image
        self.image_owner_alias = image_owner_alias
        # The OS.
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

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.exported_image_url is not None:
            result['ExportedImageURL'] = self.exported_image_url

        if self.image_export_status is not None:
            result['ImageExportStatus'] = self.image_export_status

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.image_name is not None:
            result['ImageName'] = self.image_name

        if self.image_owner_alias is not None:
            result['ImageOwnerAlias'] = self.image_owner_alias

        if self.platform is not None:
            result['Platform'] = self.platform

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Architecture') is not None:
            self.architecture = m.get('Architecture')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('ExportedImageURL') is not None:
            self.exported_image_url = m.get('ExportedImageURL')

        if m.get('ImageExportStatus') is not None:
            self.image_export_status = m.get('ImageExportStatus')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')

        if m.get('ImageOwnerAlias') is not None:
            self.image_owner_alias = m.get('ImageOwnerAlias')

        if m.get('Platform') is not None:
            self.platform = m.get('Platform')

        return self

