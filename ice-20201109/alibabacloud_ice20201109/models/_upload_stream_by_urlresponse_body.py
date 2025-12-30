# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UploadStreamByURLResponseBody(DaraModel):
    def __init__(
        self,
        file_url: str = None,
        job_id: str = None,
        media_id: str = None,
        request_id: str = None,
        source_url: str = None,
    ):
        # The OSS URL of the file.
        self.file_url = file_url
        # The ID of the upload job.
        self.job_id = job_id
        # The ID of the media asset.
        self.media_id = media_id
        # The request ID.
        self.request_id = request_id
        # The URL of the source file that is uploaded in the upload job.
        self.source_url = source_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_url is not None:
            result['FileURL'] = self.file_url

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.media_id is not None:
            result['MediaId'] = self.media_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.source_url is not None:
            result['SourceURL'] = self.source_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileURL') is not None:
            self.file_url = m.get('FileURL')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SourceURL') is not None:
            self.source_url = m.get('SourceURL')

        return self

