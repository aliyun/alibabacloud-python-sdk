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
        # The audio or video ID, which is the `MediaIds` value specified when calling the [SubmitMediaRefreshJob](https://help.aliyun.com/document_detail/431095.html) operation. Only one audio or video ID can be specified.
        # 
        # If this parameter is not specified, task information for all audio or video files under the specified `MediaRefreshJobId` is returned. If this parameter is specified, only the task information for the specified audio or video ID under the `MediaRefreshJobId` is returned.
        self.media_id = media_id
        # The ID of the audio or video purge or prefetch task. This is the value of MediaRefreshJobId returned by the [SubmitMediaRefreshJob](https://help.aliyun.com/document_detail/431095.html) operation.
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

