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
        # The ID of the application. Default value: **app-1000000**. If you have activated the multi-application service, specify the ID of the application to add the watermark template in the specified application. For more information, see [Overview](https://help.aliyun.com/document_detail/113600.html).
        self.app_id = app_id
        # The type of the auxiliary media asset. Valid values:
        # 
        # *   **watermark**
        # *   **subtitle**
        # *   **material**
        # 
        # This parameter is required.
        self.business_type = business_type
        # The ID of the category. Separate multiple IDs with commas (,). You can specify up to five IDs. You can use one of the following methods to obtain the ID:
        # 
        # *   Log on to the [ApsaraVideo VOD console](https://vod.console.aliyun.com). In the left-side navigation pane, choose **Configuration Management** > **Media Management** > **Categories** to view the category ID of the media file.
        # *   Obtain the category ID from the response to the [AddCategory](~~AddCategory~~) operation that you call to create a category.
        # *   Obtain the category ID from the response to the [GetCategories](~~GetCategories~~) operation that you call to query categories.
        self.cate_ids = cate_ids
        # The description of the auxiliary media asset. Take note of the following items:
        # 
        # *   The description can be up to 1,024 bytes in length.
        # *   The value must be encoded in UTF-8.
        self.description = description
        # The source file URL of the auxiliary media asset.
        # 
        # >  The file name extension is optional. If the file name extension that you specified for this parameter is different from the value of MediaExt, the value of MediaExt takes effect.
        self.file_name = file_name
        # The size of the auxiliary media asset. Unit: byte.
        self.file_size = file_size
        # The file name extension of the auxiliary media asset.
        # 
        # *   Valid values for watermarks: **png, gif, apng, and mov**
        # *   Valid values for subtitles: **srt, ass, stl, ttml, and vtt**
        # *   Valid values for materials: **jpg, gif, png, mp4, mat, zip, and apk**
        self.media_ext = media_ext
        # The storage address. Perform the following operations to obtain the storage address:
        # 
        # Log on to the [ApsaraVideo VOD console](https://vod.console.aliyun.com). In the left-side navigation pane, choose **Configuration Management** > **Media Management** > **Storage**. On the Storage page, view the storage address.
        # 
        # >  If you leave this parameter empty, the auxiliary media asset is uploaded to the default storage address. If you specify this parameter, the auxiliary media asset is uploaded to the specified storage address.
        self.storage_location = storage_location
        # The one or more tags of the auxiliary media asset. Take note of the following items:
        # 
        # *   You can specify a maximum of 16 tags.
        # *   If you need to specify multiple tags, separate the tags with commas (,).
        # *   Each tag can be up to 32 characters in length.
        # *   The value must be encoded in UTF-8.
        self.tags = tags
        # The title of the auxiliary media asset. The following rules apply:
        # 
        # *   The title cannot exceed 128 bytes.
        # *   The title must be encoded in UTF-8.
        self.title = title
        # The custom configurations. For example, you can specify callback configurations and upload acceleration configurations. The value must be a JSON string. For more information, see [Request parameters](~~86952#section-6fg-qll-v3w~~).
        # 
        # > *   The callback configurations take effect only after you specify the HTTP callback URL and select the specific callback events in the ApsaraVideo VOD console. For more information about how to configure HTTP callback settings in the ApsaraVideo VOD console, see [Configure callback settings](https://help.aliyun.com/document_detail/86071.html).
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

