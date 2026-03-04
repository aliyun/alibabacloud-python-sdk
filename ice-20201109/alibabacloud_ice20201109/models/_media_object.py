# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MediaObject(DaraModel):
    def __init__(
        self,
        media: str = None,
        type: str = None,
    ):
        # The identifier for the media file.
        # 
        # *   If Type is set to OSS, the value is the URL of the media file. The following formats are supported: oss://... and https://...
        # *   If Type is set to Media, the value is the ID of the media asset.
        self.media = media
        # The type of media source. Valid values:
        # 
        # *   OSS: an OSS object.
        # *   Media: a media asset.
        # *   ExternalURL: a publicly accessible external URL. This is not available for public use.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.media is not None:
            result['Media'] = self.media

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Media') is not None:
            self.media = m.get('Media')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

