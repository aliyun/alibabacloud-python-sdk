# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetMediaRefreshJobsRequest(DaraModel):
    def __init__(
        self,
        media_id: str = None,
        media_refresh_job_id: str = None,
    ):
        # The audio or video ID. The value is the `MediaIds` parameter passed when you call the [Submit audio and video refresh or prefetch tasks](https://help.aliyun.com/document_detail/431095.html) API operation. You can specify only one audio or video ID.
        # 
        # If you do not specify this parameter, the task information of all audio and video files under the `MediaRefreshJobId` is queried. If you specify this parameter, only the task information of the specified audio or video file under the `MediaRefreshJobId` is queried.
        self.media_id = media_id
        # The task ID of the audio or video refresh or prefetch task. The value is the MediaRefreshJobId parameter returned by the [Submit audio and video refresh or prefetch tasks](https://help.aliyun.com/document_detail/431095.html) API operation.
        # 
        # This parameter is required.
        self.media_refresh_job_id = media_refresh_job_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.media_id is not None:
            result['MediaId'] = self.media_id

        if self.media_refresh_job_id is not None:
            result['MediaRefreshJobId'] = self.media_refresh_job_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        if m.get('MediaRefreshJobId') is not None:
            self.media_refresh_job_id = m.get('MediaRefreshJobId')

        return self

