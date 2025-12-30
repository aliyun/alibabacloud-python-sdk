# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UploadMediaByURLRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        entity_id: str = None,
        media_meta_data: str = None,
        post_process_config: str = None,
        upload_target_config: str = None,
        upload_urls: str = None,
        user_data: str = None,
    ):
        # The application ID.
        self.app_id = app_id
        # The entity ID. You can call the CreateEntity operation to create an entity and specify a dynamic metadata structure.
        self.entity_id = entity_id
        # The metadata of the media file that you want to upload. The value must be a JSON string.
        # 
        # *   This parameter takes effect only if its value matches a URL that is specified in UploadURLs.
        # *   You must convert the JSON-formatted data, such as [UploadMetadata, UploadMetadata,…], into a JSON string.
        # *   For more information, see the "UploadMetadata" section of this topic.
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
        # The URL of the source file.
        # 
        # *   The URL must contain a file name extension, such as mp4 in `https://****.mp4`.
        # 
        #     *   If the URL does not contain a file name extension, you can specify one by setting `FileExtension` in `UploadMetadata`.
        #     *   If the URL contains a file name extension and `FileExtension` is also specified, the value of `FileExtension` prevails.
        # 
        # *   URL encoding is required. Separate multiple URLs with commas (,). You can specify a maximum of 20 URLs.
        # 
        # *   Special characters may cause upload failures. Therefore, you must encode URLs before you separate them with commas (,).
        self.upload_urls = upload_urls
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

        if self.media_meta_data is not None:
            result['MediaMetaData'] = self.media_meta_data

        if self.post_process_config is not None:
            result['PostProcessConfig'] = self.post_process_config

        if self.upload_target_config is not None:
            result['UploadTargetConfig'] = self.upload_target_config

        if self.upload_urls is not None:
            result['UploadURLs'] = self.upload_urls

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')

        if m.get('MediaMetaData') is not None:
            self.media_meta_data = m.get('MediaMetaData')

        if m.get('PostProcessConfig') is not None:
            self.post_process_config = m.get('PostProcessConfig')

        if m.get('UploadTargetConfig') is not None:
            self.upload_target_config = m.get('UploadTargetConfig')

        if m.get('UploadURLs') is not None:
            self.upload_urls = m.get('UploadURLs')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

