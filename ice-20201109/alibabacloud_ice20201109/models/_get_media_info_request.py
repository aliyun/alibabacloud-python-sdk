# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetMediaInfoRequest(DaraModel):
    def __init__(
        self,
        auth_timeout: int = None,
        input_url: str = None,
        media_id: str = None,
        output_type: str = None,
        return_detailed_info: str = None,
    ):
        # The validity period of the signed URL, in seconds.
        self.auth_timeout = auth_timeout
        # The address of the media asset to query. You must first register the media asset in the IMS media library and bind it to a `mediaId`.
        # 
        # - Object Storage Service (OSS) URL. Two formats are supported:
        # 
        # `http(s)://example-bucket.oss-cn-shanghai.aliyuncs.com/example.mp4`
        # 
        # `oss://example-bucket/example.mp4`. When you use this format, the OSS region defaults to the service endpoint region.
        self.input_url = input_url
        # The ID of the media asset in Intelligent Media Services (IMS). If you omit this parameter, you must specify `InputURL`.
        self.media_id = media_id
        # The type of URL to return for the media asset file.
        # 
        # - `oss`: Returns the OSS URL. This is the default value.
        # 
        # - `cdn`: Returns the Content Delivery Network (CDN) URL. A CDN URL is returned only if the media asset was imported from Video on Demand (VOD) and has a CDN domain name configured in VOD.
        self.output_type = output_type
        # Whether to return detailed information for specific media asset fields. The only supported field is `AiRoughData.StandardSmartTagJob`, which specifies how the result of a tag analysis task is returned.
        # 
        # - `false`: The task result is returned as a URL. This is the default value.
        # 
        # - `true`: The task result is returned as a string.
        self.return_detailed_info = return_detailed_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_timeout is not None:
            result['AuthTimeout'] = self.auth_timeout

        if self.input_url is not None:
            result['InputURL'] = self.input_url

        if self.media_id is not None:
            result['MediaId'] = self.media_id

        if self.output_type is not None:
            result['OutputType'] = self.output_type

        if self.return_detailed_info is not None:
            result['ReturnDetailedInfo'] = self.return_detailed_info

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthTimeout') is not None:
            self.auth_timeout = m.get('AuthTimeout')

        if m.get('InputURL') is not None:
            self.input_url = m.get('InputURL')

        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        if m.get('OutputType') is not None:
            self.output_type = m.get('OutputType')

        if m.get('ReturnDetailedInfo') is not None:
            self.return_detailed_info = m.get('ReturnDetailedInfo')

        return self

