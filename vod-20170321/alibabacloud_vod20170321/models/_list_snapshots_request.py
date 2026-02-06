# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListSnapshotsRequest(DaraModel):
    def __init__(
        self,
        auth_timeout: str = None,
        page_no: str = None,
        page_size: str = None,
        snapshot_type: str = None,
        video_id: str = None,
    ):
        # The validity period of the snapshot URL. Default value: **3600**. Minimum value: **3600**. Unit: seconds.
        # 
        # *   This parameter takes effect only when you enable URL signing. For more information, see [Configure URL signing](https://help.aliyun.com/document_detail/57007.html).
        # *   If you specify a value smaller than **3,600 seconds**, **3600** is used by default.
        # *   If the snapshot URL is an Object Storage Service (OSS) URL, the maximum value for this parameter is **2592000** (30 days). This reduces risks on the origin.
        self.auth_timeout = auth_timeout
        # The page number. Default value: **1**.
        self.page_no = page_no
        # The number of entries per page. Default value: **20**. Maximum value: **100**.
        self.page_size = page_size
        # The type of snapshots to return. Valid values:
        # 
        # *   **CoverSnapshot**: thumbnail snapshot
        # *   **NormalSnapshot**: regular snapshot
        # *   **SpriteSnapshot**: sprite snapshot
        # *   **SpriteOriginSnapshot**: sprite source snapshot
        # *   **WebVttSnapshot**: WebVTT snapshot
        self.snapshot_type = snapshot_type
        # The ID of the video. You can use one of the following methods to obtain the ID:
        # 
        # *   Log on to the [ApsaraVideo VOD console](https://vod.console.aliyun.com). In the left-side navigation pane, choose **Media Files** > **Audio/Video** to view the video ID.
        # *   Obtain the video ID from the response to the [CreateUploadVideo](~~CreateUploadVideo~~) operation that you call to obtain the upload URL and credential.
        # *   Obtain the video ID from the response to the [SearchMedia](~~SearchMedia~~) operation that you call to query videos.
        # 
        # This parameter is required.
        self.video_id = video_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_timeout is not None:
            result['AuthTimeout'] = self.auth_timeout

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.snapshot_type is not None:
            result['SnapshotType'] = self.snapshot_type

        if self.video_id is not None:
            result['VideoId'] = self.video_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthTimeout') is not None:
            self.auth_timeout = m.get('AuthTimeout')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SnapshotType') is not None:
            self.snapshot_type = m.get('SnapshotType')

        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')

        return self

