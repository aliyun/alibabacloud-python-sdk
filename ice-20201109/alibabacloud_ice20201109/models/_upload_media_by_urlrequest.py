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
        # The entity ID. You can call the CreateEntity API to create an entity and define a custom dynamic metadata schema.
        self.entity_id = entity_id
        # The metadata of the media file, provided as a JSON string.
        # 
        # - This metadata takes effect only when it matches a URL in `UploadURLs`.
        # 
        # - The value must be a JSON array in the `[UploadMetadata, UploadMetadata, ...]` format, passed as a JSON string.
        # 
        # - For more information, see the UploadMetadata table below.
        self.media_meta_data = media_meta_data
        # Specifies post-upload processing actions for media files of type `video` or `audio`.
        # 
        # The only supported value for `ProcessType` is `Workflow`.
        self.post_process_config = post_process_config
        # The destination storage location.
        # 
        # - The only valid value for `StorageType` is `oss`.
        # 
        # - `StorageLocation` supports VOD storage only and does not support your own OSS buckets.
        self.upload_target_config = upload_target_config
        # The source URL of the media file.
        # 
        # - The URL must include a file extension. For example, in `https://****.mp4`, mp4 is the file extension.
        # 
        #   - If the URL does not include a file extension, you can specify it by using the `FileExtension` parameter in `MediaMetaData`.
        # 
        #   - If a file extension is present in both the URL and the `FileExtension` parameter, the value of `FileExtension` takes precedence.
        # 
        # - The URLs must be URL-encoded. Separate multiple URLs with commas (,). You can specify up to 20 URLs.
        # 
        # - To prevent upload failures due to special characters, URL-encode each URL before concatenating them with commas.
        self.upload_urls = upload_urls
        # Custom settings, provided as a JSON string. This parameter supports configurations such as message callbacks.
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

