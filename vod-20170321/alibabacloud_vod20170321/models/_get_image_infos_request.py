# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetImageInfosRequest(DaraModel):
    def __init__(
        self,
        auth_timeout: int = None,
        image_ids: str = None,
        output_type: str = None,
    ):
        # The expiration time of the image access URL. Unit: seconds.
        # 
        # - If OutputType is set to cdn:
        #     - Only image URLs for which URL authentication is enabled expire. Otherwise, the URLs are permanently valid.
        #     - Minimum value: 1.
        #     - Maximum value: unlimited.
        #     - Default value: If this parameter is not specified, the default validity period configured for URL authentication is used.
        # - If OutputType is set to oss:
        #     - Only playback URLs for images stored in private buckets expire. Otherwise, the URLs are permanently valid.
        #     - Minimum value: 1.
        #     - Maximum value: To reduce security risks to the origin server, the maximum value is **2592000** (30 days) if the image is stored in an ApsaraVideo VOD bucket, and **129600** (36 hours) if the image is stored in a custom OSS bucket.
        #     - Default value: If this parameter is not specified, the value is 3600.
        self.auth_timeout = auth_timeout
        # The list of image IDs. Separate multiple IDs with commas (,). You can specify up to 20 IDs. You can obtain the image IDs by using one of the following methods:
        # - Log on to the [ApsaraVideo VOD console](https://vod.console.aliyun.com/) and choose **Media Files > Images** to view the IDs.
        # - Call the [CreateUploadImage](~~CreateUploadImage~~) operation to obtain the upload URL and credential. The image ID is returned in the response.
        # - Call the [SearchMedia](~~SearchMedia~~) operation to query images. The image ID is returned in the response.
        # 
        # This parameter is required.
        self.image_ids = image_ids
        # The type of the output image access URL. Valid values:
        # 
        # - oss: back-to-origin URL.
        # - cdn (default): accelerated URL.
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

        if self.image_ids is not None:
            result['ImageIds'] = self.image_ids

        if self.output_type is not None:
            result['OutputType'] = self.output_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthTimeout') is not None:
            self.auth_timeout = m.get('AuthTimeout')

        if m.get('ImageIds') is not None:
            self.image_ids = m.get('ImageIds')

        if m.get('OutputType') is not None:
            self.output_type = m.get('OutputType')

        return self

