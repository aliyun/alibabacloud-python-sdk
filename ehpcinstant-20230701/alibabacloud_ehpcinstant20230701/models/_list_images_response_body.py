# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ehpcinstant20230701 import models as main_models
from darabonba.model import DaraModel

class ListImagesResponseBody(DaraModel):
    def __init__(
        self,
        images: List[main_models.ListImagesResponseBodyImages] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The list of image information.
        self.images = images
        # The page number.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
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
                temp_model = main_models.ListImagesResponseBodyImages()
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

class ListImagesResponseBodyImages(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        create_time: str = None,
        description: str = None,
        document_id: int = None,
        image_id: str = None,
        image_type: str = None,
        name: str = None,
        os_tag: str = None,
        update_time: str = None,
        version: str = None,
        weight: int = None,
    ):
        # The application ID.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The time when the storage resource was created.
        self.create_time = create_time
        # The description of the image.
        self.description = description
        # The document ID.
        self.document_id = document_id
        # The image ID.
        # 
        # This parameter is required.
        self.image_id = image_id
        # The type of the image.
        # 
        # This parameter is required.
        self.image_type = image_type
        # The name of the image.
        self.name = name
        # The ID of the specific OS version.
        self.os_tag = os_tag
        # The time when the image was updated.
        self.update_time = update_time
        # The version of the image.
        self.version = version
        # The weight.
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.document_id is not None:
            result['DocumentId'] = self.document_id

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.image_type is not None:
            result['ImageType'] = self.image_type

        if self.name is not None:
            result['Name'] = self.name

        if self.os_tag is not None:
            result['OsTag'] = self.os_tag

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.version is not None:
            result['Version'] = self.version

        if self.weight is not None:
            result['Weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DocumentId') is not None:
            self.document_id = m.get('DocumentId')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OsTag') is not None:
            self.os_tag = m.get('OsTag')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        return self

