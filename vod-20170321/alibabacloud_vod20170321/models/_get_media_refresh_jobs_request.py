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
        # The ID of the media file. It is the value of the `MediaIds` parameter that you specify when you call the [RefreshMediaPlayUrls](~~RefreshMediaPlayUrls~~) operation. You can specify only one media ID.
        # 
        # If you leave this parameter empty, information about all media files in the refresh or prefetch job specified by `MediaRefreshJobId` is returned. If you set this parameter, only the information about the specified media file is returned.``
        self.media_id = media_id
        # The ID of the refresh or prefetch job. It is the value of the MediaRefreshJobId parameter that is returned from the call to the [RefreshMediaPlayUrls](~~RefreshMediaPlayUrls~~) operation.
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

