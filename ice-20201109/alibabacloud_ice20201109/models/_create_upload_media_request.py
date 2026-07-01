# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateUploadMediaRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        entity_id: str = None,
        file_info: str = None,
        media_meta_data: str = None,
        post_process_config: str = None,
        upload_target_config: str = None,
        user_data: str = None,
    ):
        # The application ID. The default value is `app-1000000`.
        self.app_id = app_id
        # The ID of the entity. You can call the `CreateEntity` operation to create an entity and define a custom schema for dynamic metadata.
        self.entity_id = entity_id
        # The file information, provided as a JSON string containing the following fields:
        # 
        # - `Type` (Required): The file type. Valid values: `video`, `image`, `audio`, `text`, and `other`.
        # 
        # - `Name` (Required): The filename without the extension.
        # 
        # - `Size` (Optional): The file size.
        # 
        # - `Ext` (Required): The file extension.
        self.file_info = file_info
        # The media asset metadata, provided as a JSON string.
        # 
        # `Title` (Required):
        # 
        # - The title can be up to 128 characters in length.
        # 
        # - The title must be UTF-8 encoded.
        # 
        # `Description` (Optional):
        # 
        # - The description can be up to 1,024 characters in length.
        # 
        # - The description must be UTF-8 encoded.
        # 
        # `CateId` (Optional): The category ID.
        # 
        # `Tags` (Optional): The tags of the media asset, separated by commas.
        # 
        # `BusinessType` (Required): The business type. Valid values depend on the `Type` specified in `FileInfo`.
        # 
        # - If `Type` is `video`: `opening` or `ending`.
        # 
        # - If `Type` is `image`: `default`, `cover`, or `watermark`.
        # 
        # - If `Type` is `text`: `subtitles` or `font`.
        # 
        # -
        # 
        # - If `Type` is `other`: `general`.
        # 
        # `CoverURL` (Optional): The URL of the cover image.<br>`DynamicMetaData` (Optional): A string for custom dynamic metadata.<br>
        self.media_meta_data = media_meta_data
        # The post-processing configuration for `video` or `audio` uploads.
        # 
        # Set `ProcessType` to `Workflow`.
        # 
        # > - This parameter specifies an [asynchronous task](https://help.aliyun.com/document_detail/3027141.html), which is queued and runs in the background after you submit the request.
        self.post_process_config = post_process_config
        # The destination storage configuration, provided as a JSON string.
        # 
        # - `StorageType`: Only `oss` is supported.
        # 
        # - `StorageLocation`: Only VOD storage is supported. You cannot upload to your own OSS buckets.
        self.upload_target_config = upload_target_config
        # A JSON string for custom settings, such as configuring a message callback.
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

        if self.entity_id is not None:
            result['EntityId'] = self.entity_id

        if self.file_info is not None:
            result['FileInfo'] = self.file_info

        if self.media_meta_data is not None:
            result['MediaMetaData'] = self.media_meta_data

        if self.post_process_config is not None:
            result['PostProcessConfig'] = self.post_process_config

        if self.upload_target_config is not None:
            result['UploadTargetConfig'] = self.upload_target_config

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')

        if m.get('FileInfo') is not None:
            self.file_info = m.get('FileInfo')

        if m.get('MediaMetaData') is not None:
            self.media_meta_data = m.get('MediaMetaData')

        if m.get('PostProcessConfig') is not None:
            self.post_process_config = m.get('PostProcessConfig')

        if m.get('UploadTargetConfig') is not None:
            self.upload_target_config = m.get('UploadTargetConfig')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

