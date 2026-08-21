# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RestoreMediaRequest(DaraModel):
    def __init__(
        self,
        media_ids: str = None,
        restore_days: str = None,
        restore_tier: str = None,
        scope: str = None,
    ):
        # The media IDs, which are audio or video IDs (VideoId). Separate multiple IDs with commas (,). A maximum of 20 IDs are supported. You can obtain the IDs by using the following methods:
        # 
        # - For audio or video files uploaded in the console, log on to the ApsaraVideo VOD console and choose Media Files > Audio/Video to view the audio or video ID.
        # - When you call the CreateUploadVideo operation to obtain the upload URL and credential, the video ID is the value of the VideoId parameter in the response.
        # - After the audio or video file is uploaded, you can call the SearchMedia operation to query the video ID, which is the value of the VideoId parameter in the response.
        # 
        # This parameter is required.
        self.media_ids = media_ids
        # The restoration duration. Default value: 1 day. Maximum value for Archive media assets: 7 days. Maximum value for Cold Archive media assets: 365 days.
        self.restore_days = restore_days
        # The restoration priority. This parameter is required only for Cold Archive media assets. If this parameter is not specified, the default value **Standard** is used. Valid values:
        # - **Expedited**: High priority. The restoration is completed within 1 hour.
        # - **Standard** (default): Standard priority. The restoration is completed within 2 to 5 hours.
        # - **Bulk**: Batch priority. The restoration is completed within 5 to 12 hours.
        self.restore_tier = restore_tier
        # The scope of the change. If this parameter is not specified, the default value **All** is used. Valid values:
        # - **All** (default): Applies tiered storage to all resources (source files and transcoded streams) of the media asset.
        # - **SourceFile**: Applies tiered storage only to the video source file of the media asset ID. Resources other than the source file use Standard storage.
        self.scope = scope

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.media_ids is not None:
            result['MediaIds'] = self.media_ids

        if self.restore_days is not None:
            result['RestoreDays'] = self.restore_days

        if self.restore_tier is not None:
            result['RestoreTier'] = self.restore_tier

        if self.scope is not None:
            result['Scope'] = self.scope

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MediaIds') is not None:
            self.media_ids = m.get('MediaIds')

        if m.get('RestoreDays') is not None:
            self.restore_days = m.get('RestoreDays')

        if m.get('RestoreTier') is not None:
            self.restore_tier = m.get('RestoreTier')

        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        return self

