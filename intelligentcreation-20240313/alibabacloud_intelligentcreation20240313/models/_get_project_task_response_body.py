# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetProjectTaskResponseBody(DaraModel):
    def __init__(
        self,
        error_msg: str = None,
        request_id: str = None,
        status: str = None,
        video_download_url: str = None,
        video_duration: int = None,
        video_url: str = None,
    ):
        self.error_msg = error_msg
        self.request_id = request_id
        self.status = status
        self.video_download_url = video_download_url
        self.video_duration = video_duration
        self.video_url = video_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.status is not None:
            result['status'] = self.status

        if self.video_download_url is not None:
            result['videoDownloadUrl'] = self.video_download_url

        if self.video_duration is not None:
            result['videoDuration'] = self.video_duration

        if self.video_url is not None:
            result['videoUrl'] = self.video_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('videoDownloadUrl') is not None:
            self.video_download_url = m.get('videoDownloadUrl')

        if m.get('videoDuration') is not None:
            self.video_duration = m.get('videoDuration')

        if m.get('videoUrl') is not None:
            self.video_url = m.get('videoUrl')

        return self

