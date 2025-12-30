# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RegisterMediaStreamRequest(DaraModel):
    def __init__(
        self,
        input_url: str = None,
        media_id: str = None,
        stream_tags: str = None,
        user_data: str = None,
    ):
        # The URL of the media asset in another service. The URL is associated with the ID of the media asset in IMS. The URL cannot be modified once registered.
        # 
        # Set this parameter to the OSS URL of the media asset. The following formats are supported:
        # 
        # http(s)://example-bucket.oss-cn-shanghai.aliyuncs.com/example.mp4
        # 
        # oss://example-bucket/example.mp4: In this format, it is considered by default that the region of the OSS bucket in which the media asset resides is the same as the region in which IMS is activated.
        self.input_url = input_url
        # The ID of the media asset.
        self.media_id = media_id
        self.stream_tags = stream_tags
        # The user data.
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.input_url is not None:
            result['InputURL'] = self.input_url

        if self.media_id is not None:
            result['MediaId'] = self.media_id

        if self.stream_tags is not None:
            result['StreamTags'] = self.stream_tags

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InputURL') is not None:
            self.input_url = m.get('InputURL')

        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        if m.get('StreamTags') is not None:
            self.stream_tags = m.get('StreamTags')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

