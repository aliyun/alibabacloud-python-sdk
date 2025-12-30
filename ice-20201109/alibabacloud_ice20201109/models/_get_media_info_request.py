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
        self.auth_timeout = auth_timeout
        # The input URL of the media asset in another service. The URL must be registered in the IMS content library and bound to the ID of the media asset in IMS.
        # 
        # *   For a media asset from Object Storage Service (OSS), the URL may have one of the following formats:
        # 
        # http(s)://example-bucket.oss-cn-shanghai.aliyuncs.com/example.mp4 or
        # 
        # oss://example-bucket/example.mp4. The second format indicates that the region in which the OSS bucket of the media asset resides is the same as the region in which OSS is activated.
        self.input_url = input_url
        # The ID of the media asset in IMS. If this parameter is left empty, the InputURL parameter must be specified.
        self.media_id = media_id
        # The type of the URL of the media asset to return in the response. Valid values:
        # 
        # *   oss (default): an OSS URL.
        # *   cdn: a CDN URL. A CDN URL is returned only if the media asset is imported from ApsaraVideo VOD and the relevant domain name is an accelerated domain name in ApsaraVideo VOD.
        self.output_type = output_type
        # Specifies whether to return detailed information for specific media asset attributes. Supported attributes: AiRoughData.StandardSmartTagJob, which specifies whether to return detailed tag information if a tagging job has been submitted for the media asset. Valid values for the attribute:
        # 
        # *   false (default): The job result is returned as a URL.
        # *   true: The job result is returned as text.
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

