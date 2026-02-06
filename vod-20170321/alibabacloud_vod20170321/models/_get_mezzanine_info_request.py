# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetMezzanineInfoRequest(DaraModel):
    def __init__(
        self,
        addition_type: str = None,
        auth_timeout: int = None,
        output_type: str = None,
        reference_id: str = None,
        video_id: str = None,
    ):
        # The type of additional information. Separate multiple values with commas (,). By default, only the basic information is returned. Valid values:
        # 
        # *   **video**: video stream information
        # *   **audio**: audio stream information
        self.addition_type = addition_type
        # The validity period of the mezzanine file URL. Unit: seconds. Default value: **1800**. Minimum value: **1**.
        # 
        # *   If the OutputType parameter is set to **cdn**:
        # 
        #     *   The mezzanine file URL has a validity period only if URL signing is enabled. Otherwise, the mezzanine file URL is permanently valid.
        #     *   Minimum value: **1**.
        #     *   Maximum Value: unlimited.
        #     *   Default value: If you do not set this parameter, the default validity period that is specified in URL signing is used.
        # 
        # <!---->
        # 
        # *   If the OutputType parameter is set to **oss**:
        # 
        #     *   The mezzanine file URL has a validity period only if the permissions on the Object Storage Service (OSS) bucket are private. Otherwise, the mezzanine file URL is permanently valid.
        #     *   Minimum value: **1**.
        #     *   Maximum value: **2592000** (30 days). The maximum value is limited to reduce security risks of the origin.
        #     *   Default value: If you do not set this parameter, the default value is **3600**.
        self.auth_timeout = auth_timeout
        # The type of the mezzanine file URL. Valid values:
        # 
        # - **oss**: OSS URL
        # - **cdn** (default): Content Delivery Network (CDN) URL
        # 
        # > If the mezzanine file is stored in a bucket of the in type, only an OSS URL is returned.
        self.output_type = output_type
        self.reference_id = reference_id
        # The ID of the video.
        self.video_id = video_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.addition_type is not None:
            result['AdditionType'] = self.addition_type

        if self.auth_timeout is not None:
            result['AuthTimeout'] = self.auth_timeout

        if self.output_type is not None:
            result['OutputType'] = self.output_type

        if self.reference_id is not None:
            result['ReferenceId'] = self.reference_id

        if self.video_id is not None:
            result['VideoId'] = self.video_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdditionType') is not None:
            self.addition_type = m.get('AdditionType')

        if m.get('AuthTimeout') is not None:
            self.auth_timeout = m.get('AuthTimeout')

        if m.get('OutputType') is not None:
            self.output_type = m.get('OutputType')

        if m.get('ReferenceId') is not None:
            self.reference_id = m.get('ReferenceId')

        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')

        return self

