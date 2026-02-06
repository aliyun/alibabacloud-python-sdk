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
        # The time when the image URL expires. Unit: seconds.
        # 
        # *   If the OutputType parameter is set to cdn:
        # 
        #     *   This parameter takes effect only if URL authentication is enabled. Otherwise, the image URL does not expire.
        #     *   Minimum value: 1.
        #     *   Maximum value: unlimited.
        #     *   Default value: The default validity period that is specified in URL authentication is used.
        # 
        # *   If the OutputType parameter is set to oss:
        # 
        #     *   This parameter takes effect only when the ACL of the Object Storage Service (OSS) bucket is private. Otherwise, the image URL does not expire.
        #     *   Minimum value: 1.
        #     *   If you store the image in the VOD bucket, the maximum value of this parameter is **2592000** (30 days). If you store the image in an OSS bucket, the maximum value of this parameter is **129600** (36 hours). The maximum value is limited to reduce security risks of the origin.
        #     *   Default value: 3600.
        self.auth_timeout = auth_timeout
        # The image IDs. Separate multiple IDs with commas (,). You can specify up to 20 image IDs. You can use one of the following methods to obtain the ID:
        # 
        # *   Log on to the [ApsaraVideo VOD console](https://vod.console.aliyun.com/) and choose **Media Files > Images** in the left-side navigation pane.
        # *   Obtain the value of ImageId from the response to the CreateUploadImage operation that you call to obtain the upload URL and credential.
        # *   Obtain the value of ImageId from the response to the [SearchMedia](~~SearchMedia~~) operation after you upload images.
        # 
        # This parameter is required.
        self.image_ids = image_ids
        # The type of the output image URL. Valid values:
        # 
        # *   oss: OSS URL
        # *   cdn: CDN URL
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

