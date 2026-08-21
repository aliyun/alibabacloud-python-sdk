# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_vod20170321 import models as main_models
from darabonba.model import DaraModel

class GetImageInfoResponseBody(DaraModel):
    def __init__(
        self,
        image_info: main_models.GetImageInfoResponseBodyImageInfo = None,
        request_id: str = None,
    ):
        # The image information.
        self.image_info = image_info
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.image_info:
            self.image_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_info is not None:
            result['ImageInfo'] = self.image_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageInfo') is not None:
            temp_model = main_models.GetImageInfoResponseBodyImageInfo()
            self.image_info = temp_model.from_map(m.get('ImageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetImageInfoResponseBodyImageInfo(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        cate_id: int = None,
        cate_name: str = None,
        creation_time: str = None,
        description: str = None,
        image_id: str = None,
        image_type: str = None,
        mezzanine: main_models.GetImageInfoResponseBodyImageInfoMezzanine = None,
        status: str = None,
        storage_location: str = None,
        tags: str = None,
        title: str = None,
        url: str = None,
    ):
        # The application ID.
        self.app_id = app_id
        # The category ID.
        self.cate_id = cate_id
        # The category name.
        self.cate_name = cate_name
        # The time when the image was created. The time follows the ISO 8601 standard in the <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z format. The time is displayed in UTC.
        self.creation_time = creation_time
        # The image description.
        self.description = description
        # The image ID.
        self.image_id = image_id
        # The image type. Valid values:
        # 
        # - **default**: regular image.
        # - **cover**: video thumbnail.
        self.image_type = image_type
        # The mezzanine information of the image.
        self.mezzanine = mezzanine
        # The image status. Valid values:
        # 
        # - **Uploading**: The image is being uploaded. This is the initial status.
        # - **Normal**: The image is uploaded.
        # - **UploadFail**: The image failed to be uploaded.
        self.status = status
        # The storage address of the image file.
        self.storage_location = storage_location
        # The image tags. Multiple tags are separated by commas (,).
        self.tags = tags
        # The image title.
        self.title = title
        # The image access URL. If a CDN domain name is configured, the CDN URL is returned. Otherwise, the OSS URL is returned.
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
            temp_model = main_models.GetImageInfoResponseBodyImageInfoMezzanine()
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

class GetImageInfoResponseBodyImageInfoMezzanine(DaraModel):
    def __init__(
        self,
        file_size: str = None,
        file_url: str = None,
        height: int = None,
        original_file_name: str = None,
        width: int = None,
    ):
        # The file size. Unit: bytes.
        self.file_size = file_size
        # The OSS URL of the image file.
        self.file_url = file_url
        # The image height. Unit: pixel.
        self.height = height
        # The address of the uploaded source image file.
        self.original_file_name = original_file_name
        # The image width. Unit: pixel.
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

