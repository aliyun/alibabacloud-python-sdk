# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetImageInfoRequest(DaraModel):
    def __init__(
        self,
        auth_timeout: int = None,
        image_id: str = None,
        output_type: str = None,
    ):
        # The expiration time of the image access URL. Unit: seconds.
        # 
        # - If OutputType is set to cdn:
        #     - The image URL expires only if URL authentication is enabled. Otherwise, the URL is permanently valid.
        #     - Minimum value: 1.
        #     - Maximum value: unlimited.
        #     - Default value: If this parameter is not specified, the default validity period configured for URL authentication is used.
        # - If OutputType is set to oss:
        #     - The playback URL expires only if the storage permission is set to private. Otherwise, the URL is permanently valid.
        #     - Minimum value: 1.
        #     - Maximum value: To reduce security risks of the origin server, the maximum value is **2592000** (30 days) if the image is stored in an ApsaraVideo VOD bucket, and **129600** (36 hours) if the image is stored in a custom OSS bucket.
        #     - Default value: If this parameter is not specified, the value is 3600.
        self.auth_timeout = auth_timeout
        # The image ID. You can obtain the image ID by using one of the following methods:
        # - Log on to the [ApsaraVideo VOD console](https://vod.console.aliyun.com/) and choose **Media Assets** > **Images** to view the ID.
        # - Call the [CreateUploadImage](~~CreateUploadImage~~) operation to obtain the upload URL and credential. The image ID is returned in the response.
        # - Call the [SearchMedia](~~SearchMedia~~) operation to query images. The image ID is returned in the response.
        # 
        # This parameter is required.
        self.image_id = image_id
        # The type of the output image access URL. Valid values:
        # 
        # - oss: the back-to-origin URL.
        # - cdn: the accelerated URL. This is the default value.
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

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.output_type is not None:
            result['OutputType'] = self.output_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthTimeout') is not None:
            self.auth_timeout = m.get('AuthTimeout')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('OutputType') is not None:
            self.output_type = m.get('OutputType')

        return self

