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
        # The validity period of the URL. Unit: seconds.
        # 
        # *   If you set the OutputType parameter to **cdn**:
        # 
        #     *   The URL of the auxiliary media asset has a validity period only if URL signing is enabled. Otherwise, the URL of the auxiliary media asset is permanently valid.
        #     *   Minimum value: **1**.
        #     *   Maximum value: unlimited.
        #     *   Default value: If you do not set this parameter, the default validity period that is specified in URL signing is used.
        # 
        # *   If you set the OutputType parameter to **oss**:
        # 
        #     *   The URL of the auxiliary media asset has a validity period only if the permissions on the Object Storage Service (OSS) bucket are private. Otherwise, the URL of the auxiliary media asset is permanently valid.
        #     *   Minimum value: **1**.
        #     *   The maximum value for a media asset stored in the VOD bucket is **2592000** (30 days) and the maximum value for a media asset stored in an OSS bucket is **129600** (36 hours). The maximum value is limited to reduce security risks of the origin.
        #     *   Default value: If you do not set this parameter, the default value **3600** is used.
        self.auth_timeout = auth_timeout
        # The ID of the auxiliary media asset.
        # 
        # *   Separate multiple IDs with commas (,). You can specify up to 20 IDs.
        # *   You can obtain the ID from the response to the [CreateUploadAttachedMedia](~~CreateUploadAttachedMedia~~) operation that you call to obtain the upload URL and credential.
        # 
        # This parameter is required.
        self.media_ids = media_ids
        # The type of the media asset URL. Valid values:
        # 
        # *   **oss**
        # *   **cdn** (default)
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

