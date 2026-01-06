# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryCloudRecordVideoPlayInfoResponseBody(DaraModel):
    def __init__(
        self,
        duration: int = None,
        file_size: int = None,
        mp_4file_url: str = None,
        play_url: str = None,
        request_id: str = None,
        status: int = None,
    ):
        self.duration = duration
        self.file_size = file_size
        self.mp_4file_url = mp_4file_url
        self.play_url = play_url
        # requestId
        self.request_id = request_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.duration is not None:
            result['duration'] = self.duration

        if self.file_size is not None:
            result['fileSize'] = self.file_size

        if self.mp_4file_url is not None:
            result['mp4FileUrl'] = self.mp_4file_url

        if self.play_url is not None:
            result['playUrl'] = self.play_url

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('duration') is not None:
            self.duration = m.get('duration')

        if m.get('fileSize') is not None:
            self.file_size = m.get('fileSize')

        if m.get('mp4FileUrl') is not None:
            self.mp_4file_url = m.get('mp4FileUrl')

        if m.get('playUrl') is not None:
            self.play_url = m.get('playUrl')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

