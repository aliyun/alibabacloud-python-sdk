# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateUploadImageRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        cate_id: int = None,
        description: str = None,
        image_ext: str = None,
        image_type: str = None,
        original_file_name: str = None,
        storage_location: str = None,
        tags: str = None,
        title: str = None,
        user_data: str = None,
    ):
        # The application ID. Default value: **app-1000000**. If you have enabled the multi-application system, you can specify an application ID to upload the image to a specified application. For more information, see [Multi-application system](https://help.aliyun.com/document_detail/113600.html).
        self.app_id = app_id
        # The category ID. You can obtain the category ID by using one of the following methods:
        # - Log on to the [ApsaraVideo VOD console](https://vod.console.aliyun.com) and choose **Configuration Management** > **Media Asset Management Configuration** > **Category Management** to view the category ID.
        # - Call the [AddCategory](~~AddCategory~~) operation to create a category. The category ID is the value of the CateId response parameter.
        # - Call the [GetCategories](~~GetCategories~~) operation to query categories. The category ID is the value of the CateId response parameter.
        self.cate_id = cate_id
        # The description of the image.
        # 
        # - The description can be up to 1,024 characters in length.
        # - The description must be encoded in UTF-8.
        self.description = description
        # The file name extension of the source image file to be uploaded. Valid values:
        # 
        # - **png**: default value.
        # - **jpg**
        # - **jpeg**
        # - **gif**
        # - **heic**
        # - **webp**
        self.image_ext = image_ext
        # The type of the image. Valid values:
        # 
        # - **default**: regular image. This is the default value.
        # - **cover**: video thumbnail.
        # 
        # > The ApsaraVideo VOD console currently supports viewing and managing only images of the **default** type.
        # 
        # This parameter is required.
        self.image_type = image_type
        # The address of the source image file to be uploaded.
        # > The address can exclude the file name extension. If the address includes a file name extension that is different from the one specified by `ImageExt`, the value of `ImageExt` prevails.
        self.original_file_name = original_file_name
        # The storage address. You can obtain the storage address by using the following method:
        # Log on to the [ApsaraVideo VOD console](https://vod.console.aliyun.com) and choose **Configuration Management** > **Media Asset Management Configuration** > **Storage Management** to view the storage address.
        # 
        # > If you do not specify this parameter, the image is uploaded to the default storage address. If you specify this parameter, the image is uploaded to the specified storage address.
        self.storage_location = storage_location
        # The tags of the image. Rules:
        # 
        # - A single tag can be up to 32 characters in length.
        # - You can specify up to 16 tags.
        # - Separate multiple tags with commas (,).
        # - The tags must be encoded in UTF-8.
        self.tags = tags
        # The title of the image. Rules:
        # 
        # - The title can be up to 128 characters in length.
        # - The title must be encoded in UTF-8.
        self.title = title
        # The custom settings. The value is a JSON string that supports settings such as message callbacks and upload acceleration. For more information, see [UserData](https://help.aliyun.com/document_detail/86952.html).
        # 
        # > - To use message callbacks in this parameter, you must configure an HTTP callback URL and select the corresponding callback event types in the console. Otherwise, the callback settings do not take effect. For more information about how to configure HTTP callbacks in the console, see [Callback settings](https://help.aliyun.com/document_detail/86071.html).
        # > - To use the upload acceleration feature, submit a ticket to apply for activation. For more information, see [Upload instructions](https://help.aliyun.com/document_detail/55396.html). For more information about how to submit a ticket, see [Contact us](https://help.aliyun.com/document_detail/464625.html).
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.cate_id is not None:
            result['CateId'] = self.cate_id

        if self.description is not None:
            result['Description'] = self.description

        if self.image_ext is not None:
            result['ImageExt'] = self.image_ext

        if self.image_type is not None:
            result['ImageType'] = self.image_type

        if self.original_file_name is not None:
            result['OriginalFileName'] = self.original_file_name

        if self.storage_location is not None:
            result['StorageLocation'] = self.storage_location

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.title is not None:
            result['Title'] = self.title

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('CateId') is not None:
            self.cate_id = m.get('CateId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ImageExt') is not None:
            self.image_ext = m.get('ImageExt')

        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')

        if m.get('OriginalFileName') is not None:
            self.original_file_name = m.get('OriginalFileName')

        if m.get('StorageLocation') is not None:
            self.storage_location = m.get('StorageLocation')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

