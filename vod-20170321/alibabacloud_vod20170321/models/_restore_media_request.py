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
        # The ID of the media asset (VideoId). Separate multiple IDs with commas (,). You can specify a maximum of 20 IDs. You can use one of the following methods to obtain the ID of the media asset:
        # 
        # *   Log on to the ApsaraVideo VOD console. In the left-side navigation pane, choose Media Files > Audio/Video. On the Video and Audio page, view the ID of the media asset. This method is applicable to files that are uploaded by using the ApsaraVideo VOD console.
        # *   Obtain the value of VideoId from the response to the CreateUploadVideo operation that you call to upload media assets.
        # *   Obtain the value of VideoId from the response to the SearchMedia operation that you call to query the media ID after the media asset is uploaded.
        # 
        # This parameter is required.
        self.media_ids = media_ids
        # The number of days during which media assets remain in the restored state. Default value: 1. The maximum validity period of a restored Archive media asset is 7 days and the maximum validity period of a restored Cold Archive media asset is 365 days.
        self.restore_days = restore_days
        # The restoration priority. This parameter is required only when you restore a Cold Archive media file. Valid values:
        # 
        # *   **Expedited**: The file is restored within 1 hour.
        # *   **Standard**: The file is restored within 2 to 5 hours.
        # *   **Bulk**: The file is restored within 5 to 12 hours.
        self.restore_tier = restore_tier
        # The modification range. Valid values:
        # 
        # *   **All**: restores all resources, including the source files and transcoded streams.
        # *   **SourceFile**: restores only the source files.
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

