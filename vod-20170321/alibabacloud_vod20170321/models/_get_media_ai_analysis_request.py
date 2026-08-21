# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetMediaAiAnalysisRequest(DaraModel):
    def __init__(
        self,
        auth_timeout: str = None,
        media_id: str = None,
        output_type: str = None,
        result_types: str = None,
    ):
        # The expiration time of the image access URL. Unit: seconds.
        # 
        # - If OutputType is set to cdn:
        #     - Only image URLs with URL authentication enabled expire. Otherwise, the URLs are permanently valid.
        #     - Minimum value: 1.
        #     - Maximum value: unlimited.
        #     - Default value: If this parameter is not specified, the default validity period specified in URL authentication settings is used.
        # - If OutputType is set to oss:
        #     - Only image URLs with private storage permissions expire. Otherwise, the URLs are permanently valid.
        #     - Minimum value: 1.
        #     - Maximum value: To reduce security risks to the origin server, the maximum value is **2592000** (30 days) if images are stored in a bucket managed by ApsaraVideo VOD, and **129600** (36 hours) if images are stored in your own OSS bucket.
        #     - Default value: If this parameter is not specified, the value is 3600.
        self.auth_timeout = auth_timeout
        # The audio ID. You can query the audio ID in the ApsaraVideo VOD console or obtain it from the response of the [SearchMedia](https://help.aliyun.com/document_detail/86044.html) operation.
        self.media_id = media_id
        # The type of the output URL. Valid values:
        # 
        # - **oss**: back-to-origin URL.
        # - **cdn** (default): accelerated URL.
        self.output_type = output_type
        # The type of analysis results. Separate multiple types with commas (,).
        self.result_types = result_types

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_timeout is not None:
            result['AuthTimeout'] = self.auth_timeout

        if self.media_id is not None:
            result['MediaId'] = self.media_id

        if self.output_type is not None:
            result['OutputType'] = self.output_type

        if self.result_types is not None:
            result['ResultTypes'] = self.result_types

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthTimeout') is not None:
            self.auth_timeout = m.get('AuthTimeout')

        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        if m.get('OutputType') is not None:
            self.output_type = m.get('OutputType')

        if m.get('ResultTypes') is not None:
            self.result_types = m.get('ResultTypes')

        return self

