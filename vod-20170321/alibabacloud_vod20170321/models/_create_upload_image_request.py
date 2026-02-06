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
        # The ID of the application. Default value: **app-1000000**. For more information, see [Overview](https://help.aliyun.com/document_detail/113600.html).
        self.app_id = app_id
        # The category ID of the image. You can use one of the following methods to obtain the category ID:
        # 
        # *   Log on to the [ApsaraVideo VOD console](https://vod.console.aliyun.com). In the left-side navigation pane, choose **Configuration Management** > **Media Management** > **Categories**. On the Categories page, you can view the category ID of the image.
        # *   Obtain the value of CateId from the response to the [AddCategory](https://help.aliyun.com/document_detail/56401.html) operation.
        # *   Obtain the value of CateId from the response to the [GetCategories](https://help.aliyun.com/document_detail/56406.html) operation.
        self.cate_id = cate_id
        # The description of the image.
        # 
        # *   The description can be up to 1,024 characters in length.
        # *   The value must be encoded in UTF-8.
        self.description = description
        # The file name extension of the image. Valid values:
        # 
        # *   **png** (default)
        # *   **jpg**
        # *   **jpeg**
        # *   **gif**
        self.image_ext = image_ext
        # The type of the image. Valid values:
        # 
        # *   **default**: the default image type.
        # *   **cover**: the thumbnail.
        # 
        # > You can manage only images of the **default** type in the ApsaraVideo VOD console.
        # 
        # This parameter is required.
        self.image_type = image_type
        # The name of the source file.
        # 
        # > The name must contain a file name extension. The file name extension is not case-sensitive.
        self.original_file_name = original_file_name
        # The storage address. Perform the following operations to obtain the storage address: Log on to the [ApsaraVideo VOD console](https://vod.console.aliyun.com). In the left-side navigation pane, choose **Configuration Management** > **Media Management** > **Storage**. On the Storage page, view the storage address.
        # 
        # > If you specify a storage address, media files are uploaded to the specified address.
        self.storage_location = storage_location
        # The tags of the image. The following rules apply:
        # 
        # *   Each tag can be up to 32 characters in length.
        # *   You can specify a maximum of 16 tags for an image.
        # *   Separate multiple tags with commas (,).
        # *   The value must be encoded in UTF-8.
        self.tags = tags
        # The title of the image. The following rules apply:
        # 
        # *   The title can be up to 128 characters in length.
        # *   The value must be encoded in UTF-8.
        self.title = title
        # The custom configurations, including callback configurations and upload acceleration configurations. The value must be a JSON string. For more information, see the "UserData: specifies the custom configurations for media upload" section of the [Request parameters](https://help.aliyun.com/document_detail/86952.html) topic.
        # 
        # > *   The callback configurations take effect only after you specify the HTTP callback URL and select specific callback events in the ApsaraVideo VOD console. For more information about how to configure HTTP callback settings in the ApsaraVideo VOD console, see [Configure callback settings](https://help.aliyun.com/document_detail/86071.html).
        # > *   If you want to enable the upload acceleration feature, submit a ticket. For more information, see [Overview](https://help.aliyun.com/document_detail/55396.html). For more information about how to submit a ticket, see [Contact us](https://help.aliyun.com/document_detail/464625.html).
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

