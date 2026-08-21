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
        # The validity period of the image access URL. Unit: seconds.
        # 
        # - If OutputType is set to cdn:
        #     - The image URL expires only if URL signing is enabled. Otherwise, the URL is permanently valid.
        #     - Minimum value: 1.
        #     - Maximum value: unlimited.
        #     - Default value: If this parameter is not specified, the default validity period specified in URL signing is used.
        # - If OutputType is set to oss:
        #     - The image URL expires only if the storage permission is set to private. Otherwise, the URL is permanently valid.
        #     - Minimum value: 1.
        #     - Maximum value: To reduce security risks to the origin server, the maximum value is **2592000** (30 days) if the image is stored in a bucket managed by ApsaraVideo VOD, and **129600** (36 hours) if the image is stored in your own OSS bucket.
        #     - Default value: If this parameter is not specified, the value is 3600.
        self.auth_timeout = auth_timeout
        # The list of image IDs. Separate multiple IDs with commas (,). A maximum of 20 IDs are supported. You can obtain image IDs by using the following methods:
        # - Log on to the [ApsaraVideo VOD console](https://vod.console.aliyun.com/) and choose **Media Files > Images** to view the IDs.
        # - Obtain the IDs from the response when you call [CreateUploadImage](~~CreateUploadImage~~) to obtain the upload URL and credential.
        # - Obtain the IDs from the response when you call [SearchMedia](~~SearchMedia~~) to query images.
        # 
        # This parameter is required.
        self.image_ids = image_ids
        # The type of the image access URL to return. Valid values:
        # 
        # - oss: the storage address.
        # - cdn (default): the CDN-accelerated URL.
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

