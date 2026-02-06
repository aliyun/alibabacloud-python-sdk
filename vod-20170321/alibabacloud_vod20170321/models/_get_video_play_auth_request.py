# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetVideoPlayAuthRequest(DaraModel):
    def __init__(
        self,
        api_version: str = None,
        auth_info_timeout: int = None,
        reference_id: str = None,
        video_id: str = None,
    ):
        # The API version. Set the value to **1.0.0**.
        self.api_version = api_version
        # The validity period of the playback credential. Unit: **seconds**. You cannot obtain the playback URL of a video by using a credential that has expired. A new credential is required.
        # 
        # *   Default value: **100**.
        # *   Valid values: `[100,3000]`.
        self.auth_info_timeout = auth_info_timeout
        self.reference_id = reference_id
        # The ID of the media file. You can specify only one ID. You can use one of the following methods to obtain the ID of the file:
        # 
        # *   Log on to the [ApsaraVideo VOD](https://vod.console.aliyun.com) console. In the left-side navigation pane, choose **Media Files** > **Audio/Video**. On the Video and Audio page, view the ID of the media file. This method is applicable to files that are uploaded by using the ApsaraVideo VOD console.
        # *   Obtain the value of the VideoId parameter from the response to the [CreateUploadVideo](https://help.aliyun.com/document_detail/55407.html) operation.
        # *   Obtain the value of the VideoId parameter from the response to the [SearchMedia](https://help.aliyun.com/document_detail/86044.html) operation. This method is applicable to files that have been uploaded.
        self.video_id = video_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_version is not None:
            result['ApiVersion'] = self.api_version

        if self.auth_info_timeout is not None:
            result['AuthInfoTimeout'] = self.auth_info_timeout

        if self.reference_id is not None:
            result['ReferenceId'] = self.reference_id

        if self.video_id is not None:
            result['VideoId'] = self.video_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiVersion') is not None:
            self.api_version = m.get('ApiVersion')

        if m.get('AuthInfoTimeout') is not None:
            self.auth_info_timeout = m.get('AuthInfoTimeout')

        if m.get('ReferenceId') is not None:
            self.reference_id = m.get('ReferenceId')

        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')

        return self

