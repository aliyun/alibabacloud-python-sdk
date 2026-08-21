# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAttachedMediaInfoRequest(DaraModel):
    def __init__(
        self,
        auth_timeout: int = None,
        media_ids: str = None,
        output_type: str = None,
    ):
        # The validity period of the auxiliary media asset URL. Unit: seconds.
        # 
        #  - If OutputType is set to **cdn**:
        #     - The URL expires only if URL authentication is enabled. Otherwise, the URL is permanently valid.
        #     - Minimum value: **1**.
        #     - Maximum value: unlimited.
        #     - Default value: If you do not specify this parameter, the default validity period specified in URL authentication is used.
        # - If OutputType is set to **oss**:
        #     - The URL expires only if the storage permission is set to private. Otherwise, the URL is permanently valid.
        #     - Minimum value: **1**.
        #     - Maximum value: To reduce security risks to the origin server, the maximum value is **2592000** (30 days) if the auxiliary media asset is stored in a bucket managed by ApsaraVideo VOD, and **129600** (36 hours) if the auxiliary media asset is stored in your own OSS bucket.
        #     - Default value: If you do not specify this parameter, the value is **3600**.
        self.auth_timeout = auth_timeout
        # The auxiliary media asset IDs.
        # - Separate multiple IDs with commas (,). You can specify up to 20 IDs.
        # - The IDs are returned after you call the [CreateUploadAttachedMedia](~~CreateUploadAttachedMedia~~) operation to obtain the upload URL and credential for the auxiliary media asset.
        # 
        # This parameter is required.
        self.media_ids = media_ids
        # The type of the output URL. Valid values:
        # 
        # - **oss**: the back-to-origin URL.
        # - **cdn** (default): the CDN-accelerated URL.
        self.output_type = output_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_timeout is not None:
            result['AuthTimeout'] = self.auth_timeout

        if self.media_ids is not None:
            result['MediaIds'] = self.media_ids

        if self.output_type is not None:
            result['OutputType'] = self.output_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthTimeout') is not None:
            self.auth_timeout = m.get('AuthTimeout')

        if m.get('MediaIds') is not None:
            self.media_ids = m.get('MediaIds')

        if m.get('OutputType') is not None:
            self.output_type = m.get('OutputType')

        return self

