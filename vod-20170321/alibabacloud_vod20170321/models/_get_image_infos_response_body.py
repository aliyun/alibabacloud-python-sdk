# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vod20170321 import models as main_models
from darabonba.model import DaraModel

class GetImageInfosResponseBody(DaraModel):
    def __init__(
        self,
        image_info: List[main_models.GetImageInfosResponseBodyImageInfo] = None,
        non_exist_image_ids: List[str] = None,
        request_id: str = None,
    ):
        # The image information.
        self.image_info = image_info
        # The IDs of the images that do not exist.
        self.non_exist_image_ids = non_exist_image_ids
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.image_info:
            for v1 in self.image_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ImageInfo'] = []
        if self.image_info is not None:
            for k1 in self.image_info:
                result['ImageInfo'].append(k1.to_map() if k1 else None)

        if self.non_exist_image_ids is not None:
            result['NonExistImageIds'] = self.non_exist_image_ids

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.image_info = []
        if m.get('ImageInfo') is not None:
            for k1 in m.get('ImageInfo'):
                temp_model = main_models.GetImageInfosResponseBodyImageInfo()
                self.image_info.append(temp_model.from_map(k1))

        if m.get('NonExistImageIds') is not None:
            self.non_exist_image_ids = m.get('NonExistImageIds')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetImageInfosResponseBodyImageInfo(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        cate_id: int = None,
        cate_name: str = None,
        creation_time: str = None,
        description: str = None,
        image_id: str = None,
        image_type: str = None,
        mezzanine: main_models.GetImageInfosResponseBodyImageInfoMezzanine = None,
        status: str = None,
        storage_location: str = None,
        tags: str = None,
        title: str = None,
        url: str = None,
    ):
        # The ID of the application.
        self.app_id = app_id
        # The ID of the category.
        self.cate_id = cate_id
        # The name of the category.
        self.cate_name = cate_name
        # The time when the image was created. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.creation_time = creation_time
        # The description of the image.
        self.description = description
        # The ID of the image.
        self.image_id = image_id
        # The type of the image. Valid values:
        # 
        # *   **default**: regular images
        # *   **cover**: video thumbnail
        self.image_type = image_type
        # The source information about the image.
        self.mezzanine = mezzanine
        # The status of the image file. Valid values:
        # 
        # *   **Uploading**: The image is being uploaded. This is the initial status.
        # *   **Normal**: The image is uploaded.
        # *   **UploadFail**: The image fails to be uploaded.
        self.status = status
        # The bucket in which the image is stored.
        self.storage_location = storage_location
        # The tags of the image. Multiple tags are separated by commas (,).
        self.tags = tags
        # The title of the image.
        self.title = title
        # The image URL. If a domain name for CDN is specified, a CDN URL is returned. Otherwise, an OSS URL is returned.
        self.url = url

    def validate(self):
        if self.mezzanine:
            self.mezzanine.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.cate_id is not None:
            result['CateId'] = self.cate_id

        if self.cate_name is not None:
            result['CateName'] = self.cate_name

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.description is not None:
            result['Description'] = self.description

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.image_type is not None:
            result['ImageType'] = self.image_type

        if self.mezzanine is not None:
            result['Mezzanine'] = self.mezzanine.to_map()

        if self.status is not None:
            result['Status'] = self.status

        if self.storage_location is not None:
            result['StorageLocation'] = self.storage_location

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.title is not None:
            result['Title'] = self.title

        if self.url is not None:
            result['URL'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('CateId') is not None:
            self.cate_id = m.get('CateId')

        if m.get('CateName') is not None:
            self.cate_name = m.get('CateName')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')

        if m.get('Mezzanine') is not None:
            temp_model = main_models.GetImageInfosResponseBodyImageInfoMezzanine()
            self.mezzanine = temp_model.from_map(m.get('Mezzanine'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StorageLocation') is not None:
            self.storage_location = m.get('StorageLocation')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('URL') is not None:
            self.url = m.get('URL')

        return self

class GetImageInfosResponseBodyImageInfoMezzanine(DaraModel):
    def __init__(
        self,
        file_size: str = None,
        file_url: str = None,
        height: int = None,
        original_file_name: str = None,
        width: int = None,
    ):
        # The size of the file to be uploaded. Unit: bytes.
        self.file_size = file_size
        # The OSS URL of the image file.
        self.file_url = file_url
        # The height of the image. Unit: pixels.
        self.height = height
        # The URL of the source file.
        self.original_file_name = original_file_name
        # The width of the image. Unit: pixels.
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_size is not None:
            result['FileSize'] = self.file_size

        if self.file_url is not None:
            result['FileURL'] = self.file_url

        if self.height is not None:
            result['Height'] = self.height

        if self.original_file_name is not None:
            result['OriginalFileName'] = self.original_file_name

        if self.width is not None:
            result['Width'] = self.width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')

        if m.get('FileURL') is not None:
            self.file_url = m.get('FileURL')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('OriginalFileName') is not None:
            self.original_file_name = m.get('OriginalFileName')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        return self

