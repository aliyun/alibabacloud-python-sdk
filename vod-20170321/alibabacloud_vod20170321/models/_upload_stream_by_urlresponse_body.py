# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UploadStreamByURLResponseBody(DaraModel):
    def __init__(
        self,
        file_url: str = None,
        request_id: str = None,
        source_url: str = None,
        stream_job_id: str = None,
    ):
        # The URL of the OSS object.
        self.file_url = file_url
        # The ID of the request.
        self.request_id = request_id
        # The URL of the input stream. This parameter is used when you call the [GetURLUploadInfos](https://help.aliyun.com/document_detail/106830.html) operation.
        self.source_url = source_url
        # The ID of the stream upload job. This parameter is used when you call the [GetURLUploadInfos](https://help.aliyun.com/document_detail/106830.html) operation.
        # 
        # In ApsaraVideo VOD, you can upload only one transcoded stream in an upload job. For more information, see the PlayInfo: the playback information about a video stream section in [Basic structures](https://help.aliyun.com/document_detail/52839.html).
        self.stream_job_id = stream_job_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_url is not None:
            result['FileURL'] = self.file_url

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.source_url is not None:
            result['SourceURL'] = self.source_url

        if self.stream_job_id is not None:
            result['StreamJobId'] = self.stream_job_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileURL') is not None:
            self.file_url = m.get('FileURL')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SourceURL') is not None:
            self.source_url = m.get('SourceURL')

        if m.get('StreamJobId') is not None:
            self.stream_job_id = m.get('StreamJobId')

        return self

