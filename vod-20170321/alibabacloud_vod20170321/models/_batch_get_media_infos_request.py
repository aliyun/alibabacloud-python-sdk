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
        # The media asset IDs, which are audio/video IDs (VideoId). Separate multiple IDs with commas (,). You can specify up to 20 IDs. You can obtain the IDs by using the following methods:
        # 
        # - For audio/video files uploaded through the console, log on to the ApsaraVideo VOD console and choose Media Files > Audio/Video to view the audio/video IDs.
        # - When you call the operation to obtain the upload URL and credential for audio/video files, the VideoId value is returned as a response parameter.
        # - After an audio/video file is uploaded, you can call the SearchMedia operation to query the VideoId value in the response.
        # 
        # This parameter is required.
        self.media_ids = media_ids
        # The list of custom IDs. Separate multiple custom IDs with commas (,). You can specify up to 20 IDs.
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

