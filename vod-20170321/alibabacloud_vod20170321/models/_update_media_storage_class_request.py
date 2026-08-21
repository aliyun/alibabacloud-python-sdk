# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateMediaStorageClassRequest(DaraModel):
    def __init__(
        self,
        allow_update_without_time_limit: bool = None,
        media_ids: str = None,
        restore_tier: str = None,
        scope: str = None,
        storage_class: str = None,
    ):
        # Specifies whether to allow storage class modification for media assets that have not met the minimum storage duration requirement. Valid values:
        # 
        # - **true**: Allowed.
        # - **false (default)**: Not allowed.
        # 
        # >If the storage duration of a media asset is insufficient and you force a storage class modification, additional retrieval fees are incurred.
        self.allow_update_without_time_limit = allow_update_without_time_limit
        # The media IDs, which are audio or video IDs (VideoId). Separate multiple IDs with commas (,). A maximum of 20 IDs are supported. You can obtain the IDs by using the following methods:
        # - For audio or video files uploaded through the console, log on to the [ApsaraVideo VOD console](https://vod.console.aliyun.com) and choose **Media Files** > **Audio/Video** to view the audio or video ID.
        # - When you call the [CreateUploadVideo](https://help.aliyun.com/document_detail/55407.html) operation to obtain the upload URL and credential, the video ID is the value of the VideoId response parameter.
        # - After the audio or video file is uploaded, you can call the [SearchMedia](https://help.aliyun.com/document_detail/86044.html) operation to query the video ID, which is the value of the VideoId response parameter.
        # 
        # This parameter is required.
        self.media_ids = media_ids
        # The restore priority (required only for ColdArchive media assets). If this parameter is not specified, the default value **Standard** is used. Valid values:
        # - **Expedited**: Expedited
        # - **Standard** (default): Standard
        # - **Bulk**: Bulk
        self.restore_tier = restore_tier
        # The scope of the modification. If this parameter is not specified, the default value **All** is used. Valid values:
        # - **All** (default): Applies tiered storage to all resources (source files and transcoded streams) of the media asset.
        # - **SourceFile**: Applies tiered storage only to the source file of the media asset. Resources other than the source file use Standard storage.
        self.scope = scope
        # The storage class. Valid values:
        # - **Standard**: Standard
        # - **IA**: Infrequent Access
        # - **Archive**: Archive
        # - **ColdArchive**: Cold Archive
        # 
        # This parameter is required.
        self.storage_class = storage_class

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow_update_without_time_limit is not None:
            result['AllowUpdateWithoutTimeLimit'] = self.allow_update_without_time_limit

        if self.media_ids is not None:
            result['MediaIds'] = self.media_ids

        if self.restore_tier is not None:
            result['RestoreTier'] = self.restore_tier

        if self.scope is not None:
            result['Scope'] = self.scope

        if self.storage_class is not None:
            result['StorageClass'] = self.storage_class

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowUpdateWithoutTimeLimit') is not None:
            self.allow_update_without_time_limit = m.get('AllowUpdateWithoutTimeLimit')

        if m.get('MediaIds') is not None:
            self.media_ids = m.get('MediaIds')

        if m.get('RestoreTier') is not None:
            self.restore_tier = m.get('RestoreTier')

        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        if m.get('StorageClass') is not None:
            self.storage_class = m.get('StorageClass')

        return self

