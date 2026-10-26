# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UploadAgentConversationLogRequest(DaraModel):
    def __init__(
        self,
        content_gzip_b64: str = None,
        file_name: str = None,
        time_range_end: str = None,
        time_range_start: str = None,
    ):
        # This parameter is required.
        self.content_gzip_b64 = content_gzip_b64
        # This parameter is required.
        self.file_name = file_name
        self.time_range_end = time_range_end
        self.time_range_start = time_range_start

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content_gzip_b64 is not None:
            result['contentGzipB64'] = self.content_gzip_b64

        if self.file_name is not None:
            result['fileName'] = self.file_name

        if self.time_range_end is not None:
            result['timeRangeEnd'] = self.time_range_end

        if self.time_range_start is not None:
            result['timeRangeStart'] = self.time_range_start

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('contentGzipB64') is not None:
            self.content_gzip_b64 = m.get('contentGzipB64')

        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')

        if m.get('timeRangeEnd') is not None:
            self.time_range_end = m.get('timeRangeEnd')

        if m.get('timeRangeStart') is not None:
            self.time_range_start = m.get('timeRangeStart')

        return self

