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
        # Specifies whether to allow modifying the storage class of media assets whose storage duration does not meet the minimum requirement. Valid values:
        # 
        # - **true**: allows the modification.
        # - **false** (default): does not allow the modification.
        # 
        # > If the storage duration of a media asset does not meet the minimum requirement and you force the storage class modification, additional data retrieval fees are incurred.
        self.allow_update_without_time_limit = allow_update_without_time_limit
        # The media asset IDs, which are the audio or video IDs (VideoId). Separate multiple IDs with commas (,). You can specify up to 20 IDs. You can obtain the IDs by using one of the following methods:
        # - For audio or video files uploaded in the console, log on to the [ApsaraVideo VOD console](https://vod.console.aliyun.com) and choose **Media Assets** > **Audio/Video** to view the audio or video IDs.
        # - When you call the [Obtain the upload URL and credential for audio and video files](https://help.aliyun.com/document_detail/55407.html) operation, the value of the VideoId response parameter is the media asset ID.
        # - After an audio or video file is uploaded, you can call the [Search for media asset information](https://help.aliyun.com/document_detail/86044.html) operation to query the media asset ID. The value of the VideoId response parameter is the media asset ID.
        # 
        # This parameter is required.
        self.media_ids = media_ids
        # The restoration priority. This parameter is required only for Cold Archive media assets. If you do not specify this parameter, the default value **Standard** is used. Valid values:
        # - **Expedited**: Expedited
        # - **Standard** (default): Standard
        # - **Bulk**: Bulk
        self.restore_tier = restore_tier
        # The scope of the modification. If you do not specify this parameter, the default value **All** is used. Valid values:
        # - **All** (default): applies tiered storage to all resources of the media asset, including the source file and transcoded streams.
        # - **SourceFile**: applies tiered storage only to the video source file of the media asset ID. Resources other than the source file are stored in Standard storage.
        self.scope = scope
        # The storage class. Valid values:
        # - **Standard**: Standard
        # - **IA**: Infrequent Access (IA)
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

