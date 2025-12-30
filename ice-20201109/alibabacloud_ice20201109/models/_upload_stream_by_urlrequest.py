# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UploadStreamByURLRequest(DaraModel):
    def __init__(
        self,
        definition: str = None,
        file_extension: str = None,
        hdrtype: str = None,
        media_id: str = None,
        stream_url: str = None,
        user_data: str = None,
    ):
        # The quality of the media stream. Valid values:
        # 
        # *   FD: low definition.
        # *   LD: standard definition.
        # *   SD: high definition.
        # *   HD: ultra-high definition.
        # *   OD: original quality.
        # *   2K: 2K resolution.
        # *   4K: 4K resolution.
        # *   SQ: standard sound quality.
        # *   HQ: high sound quality.
        self.definition = definition
        # The file name extension of the media stream.
        self.file_extension = file_extension
        # The high dynamic range (HDR) format of the transcoded stream. Valid values:
        # 
        # *   HDR
        # *   HDR10
        # *   HLG
        # *   DolbyVision
        # *   HDRVivid
        # *   SDR+
        # 
        # > 
        # 
        # *   The value is not case-sensitive,
        # 
        # *   You can leave this parameter empty for non-HDR streams.
        self.hdrtype = hdrtype
        # The ID of the media asset.
        self.media_id = media_id
        # The URL of the transcoded stream file.
        # 
        # If the URL of the transcoded stream requires authentication, you must specify the authentication parameters in the stream URL and make sure that the URL can be accessed over the Internet.
        self.stream_url = stream_url
        # The user data.
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.definition is not None:
            result['Definition'] = self.definition

        if self.file_extension is not None:
            result['FileExtension'] = self.file_extension

        if self.hdrtype is not None:
            result['HDRType'] = self.hdrtype

        if self.media_id is not None:
            result['MediaId'] = self.media_id

        if self.stream_url is not None:
            result['StreamURL'] = self.stream_url

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Definition') is not None:
            self.definition = m.get('Definition')

        if m.get('FileExtension') is not None:
            self.file_extension = m.get('FileExtension')

        if m.get('HDRType') is not None:
            self.hdrtype = m.get('HDRType')

        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        if m.get('StreamURL') is not None:
            self.stream_url = m.get('StreamURL')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

