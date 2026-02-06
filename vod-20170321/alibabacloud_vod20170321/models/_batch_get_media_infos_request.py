# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BatchGetMediaInfosRequest(DaraModel):
    def __init__(
        self,
        media_ids: str = None,
        reference_ids: str = None,
    ):
        # The ID of the media asset. The ID can be the video ID or audio ID. Separate IDs with commas (,). You can specify a maximum of 20 IDs. You can use one of the following methods to obtain the ID of the media asset:
        # 
        # *   Log on to the ApsaraVideo VOD console. In the left-side navigation pane, choose Media Files > Audio/Video. On the Video and Audio page, view the ID of the media asset. This method is applicable to files that are uploaded by using the ApsaraVideo VOD console.
        # *   Obtain the value of VideoId from the response to the CreateUploadVideo operation that you call to upload media assets.
        # *   Obtain the value of VideoId from the response to the SearchMedia operation that you call to query the media ID after the media asset is uploaded.
        # 
        # This parameter is required.
        self.media_ids = media_ids
        self.reference_ids = reference_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.media_ids is not None:
            result['MediaIds'] = self.media_ids

        if self.reference_ids is not None:
            result['ReferenceIds'] = self.reference_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MediaIds') is not None:
            self.media_ids = m.get('MediaIds')

        if m.get('ReferenceIds') is not None:
            self.reference_ids = m.get('ReferenceIds')

        return self

