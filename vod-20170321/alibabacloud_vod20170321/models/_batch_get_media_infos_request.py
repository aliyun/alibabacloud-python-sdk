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
        # The media asset IDs, namely the audio or video IDs (VideoId). Separate multiple IDs with commas (,). A maximum of 20 IDs are supported. You can obtain the IDs by using one of the following methods:
        # 
        # - For audio or video files uploaded through the console, log on to the ApsaraVideo VOD console and choose Media Library > Audio/Video to view the audio or video IDs.
        # - When you call the operation to obtain the upload URL and credential for an audio or video file, the ID is the value of the VideoId response parameter.
        # - After an audio or video file is uploaded, you can call the operation to search for media asset information. The ID is the value of the VideoId response parameter.
        # 
        # This parameter is required.
        self.media_ids = media_ids
        # The custom ID list. It consists of one or more custom IDs. Separate multiple IDs with commas (,). A maximum of 20 IDs are supported.
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

