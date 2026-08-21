# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateUploadAttachedMediaRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        business_type: str = None,
        cate_ids: str = None,
        description: str = None,
        file_name: str = None,
        file_size: str = None,
        media_ext: str = None,
        storage_location: str = None,
        tags: str = None,
        title: str = None,
        user_data: str = None,
    ):
        # The application ID. Default value: **app-1000000**. If you have activated the multi-application service, specify the application ID to upload the auxiliary media asset to the specified application. For more information, see [Multi-application](https://help.aliyun.com/document_detail/113600.html).
        self.app_id = app_id
        # The type of the auxiliary media asset. Valid values:
        # 
        # - **watermark**: watermark.
        # - **subtitle**: subtitle.
        # - **material**: material.
        # 
        # This parameter is required.
        self.business_type = business_type
        # The category IDs. Separate multiple IDs with commas (,). A maximum of 5 IDs are supported. You can obtain category IDs by using the following methods:
        # - Log on to the [ApsaraVideo VOD console](https://vod.console.aliyun.com) and choose **Configuration Management** > **Media Management Configuration** > **Category Management** to view category IDs.
        # - The category ID is returned when you call the [AddCategory](~~AddCategory~~) operation to create a category.
        # - The category ID is returned when you call the [GetCategories](~~GetCategories~~) operation to query categories.
        self.cate_ids = cate_ids
        # The description of the media asset. Rules:
        # 
        # - The description can be up to 1024 bytes in length.
        # - The description must be encoded in UTF-8.
        self.description = description
        # The source file address of the auxiliary media asset to be uploaded.
        # >The file name extension is optional. If a file name extension is specified here and is different from the extension specified in MediaExt, the value of MediaExt takes precedence.
        self.file_name = file_name
        # The file size. Unit: bytes.
        self.file_size = file_size
        # The file name extension of the auxiliary media asset source file to be uploaded. Valid values:
        # 
        # - Watermark: **png, gif, apng, mov**.
        # - Subtitle: **srt, ass, stl, ttml, vtt**.
        # - Material: **jpg, gif, png, mp4, mat, zip, apk**.
        self.media_ext = media_ext
        # The storage address. You can obtain the storage address by using the following method:
        # 
        # Log on to the [ApsaraVideo VOD console](https://vod.console.aliyun.com) and choose **Configuration Management** > **Media Management Configuration** > **Storage Management** to view the storage address.
        # 
        # > If you do not specify this parameter, the auxiliary media asset is uploaded to the default storage address. If you specify this parameter, the auxiliary media asset is uploaded to the specified storage address.
        self.storage_location = storage_location
        # The tags. Rules:
        # 
        # - A maximum of 16 tags are supported.
        # - Separate multiple tags with commas (,).
        # - Each tag can be up to 32 characters or Chinese characters in length.
        # - The tags must be encoded in UTF-8.
        self.tags = tags
        # The title of the auxiliary media asset. Rules:
        # 
        # - The title can be up to 128 bytes in length.
        # - The title must be encoded in UTF-8.
        self.title = title
        # The custom settings, which is a JSON string. The settings support message callbacks, upload acceleration, and other configurations. For more information, see [UserData](~~86952#section-6fg-qll-v3w~~).
        # 
        # > - To use message callbacks in this parameter, you must configure an HTTP callback URL and select the corresponding callback event types in the console. Otherwise, the callback settings do not take effect. For information about how to configure HTTP callbacks in the console, see [Callback settings](https://help.aliyun.com/document_detail/86071.html).
        # > - To use the upload acceleration feature, submit a ticket to activate it. For more information, see [Upload instructions](https://help.aliyun.com/document_detail/55396.html). For information about how to submit a ticket, see [Contact us](https://help.aliyun.com/document_detail/464625.html).
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

        if self.business_type is not None:
            result['BusinessType'] = self.business_type

        if self.cate_ids is not None:
            result['CateIds'] = self.cate_ids

        if self.description is not None:
            result['Description'] = self.description

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.file_size is not None:
            result['FileSize'] = self.file_size

        if self.media_ext is not None:
            result['MediaExt'] = self.media_ext

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

        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')

        if m.get('CateIds') is not None:
            self.cate_ids = m.get('CateIds')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')

        if m.get('MediaExt') is not None:
            self.media_ext = m.get('MediaExt')

        if m.get('StorageLocation') is not None:
            self.storage_location = m.get('StorageLocation')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

