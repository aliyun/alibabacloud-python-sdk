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
        # The application ID. Default value: app-1000000.
        self.app_id = app_id
        # The entity ID. You can call the CreateEntity operation to create an entity and specify a dynamic metadata structure.
        self.entity_id = entity_id
        # The file information, which is in the JSON format and contains the following fields:
        # 
        # *   Type: required. The file type. Valid values: video, image, audio, text, and other.
        # *   Name: required. The file name without the extension.
        # *   Size: optional. The file size.
        # *   Ext: required. The file name extension.
        self.file_info = file_info
        # The metadata of the media asset, which is a JSON string that contains the following fields:
        # 
        # Title: required.
        # 
        # *   The value can be up to 128 characters in length.
        # *   The value must be encoded in UTF-8.
        # 
        # Description: optional.
        # 
        # *   The value can be up to 1,024 characters in length.
        # *   The value must be encoded in UTF-8.
        # 
        # CateId: optional.
        # 
        # Tags: optional.
        # 
        # BusinessType: required. Valid values:
        # 
        # *   opening or ending if Type is set to video
        # *   default or cover if Type is set to image
        # *   subtitles or font if Type is set to text
        # *   watermark if Type is set to material
        # *   general CoverURL: optional.
        # 
        # DynamicMetaData: The value is a string.
        self.media_meta_data = media_meta_data
        # The postprocessing configurations. You can specify this parameter if Type is set to video or audio.
        # 
        # Set ProcessType to Workflow.
        self.post_process_config = post_process_config
        # The destination storage address.
        # 
        # Set StorageType to oss.
        # 
        # Set StorageLocation to an address in ApsaraVideo VOD. You cannot set this field to an OSS URL.
        self.upload_target_config = upload_target_config
        # The user data. The value must be a JSON string. You can configure settings such as message callbacks.
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

