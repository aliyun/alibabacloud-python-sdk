# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetTransitMetaResponseBody(DaraModel):
    def __init__(
        self,
        download_url: str = None,
        expire_at: int = None,
        file_path: str = None,
        request_id: str = None,
        size: int = None,
        status: str = None,
        transit_id: str = None,
    ):
        # The temporary download URL. If Network is not specified, null is returned. The URL may be unavailable if the file is not yet available. Do not write this URL to logs, store it for a long time, or forward it to irrelevant users.
        self.download_url = download_url
        # The expiration time of the transit record. The value is a UTC UNIX timestamp in milliseconds, which is the number of milliseconds that have elapsed since 00:00:00 UTC on January 1, 1970. You can directly compare this value with the current UNIX timestamp in milliseconds without adding or subtracting 8 hours. Do not continue to use the record after this time.
        self.expire_at = expire_at
        # The opaque object path corresponding to the file. Callers must not parse or construct this value.
        self.file_path = file_path
        # The request ID, which is used for Tracing Analysis and troubleshooting.
        self.request_id = request_id
        # The file size, in bytes. If no available file is detected, null may be returned.
        self.size = size
        # The status of the transit file. A value of PENDING indicates that the file is not yet available, and the caller can query again later. A value of SUCCESS indicates that the file is available.
        self.status = status
        # The transit ID.
        self.transit_id = transit_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url

        if self.expire_at is not None:
            result['ExpireAt'] = self.expire_at

        if self.file_path is not None:
            result['FilePath'] = self.file_path

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.size is not None:
            result['Size'] = self.size

        if self.status is not None:
            result['Status'] = self.status

        if self.transit_id is not None:
            result['TransitId'] = self.transit_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')

        if m.get('ExpireAt') is not None:
            self.expire_at = m.get('ExpireAt')

        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TransitId') is not None:
            self.transit_id = m.get('TransitId')

        return self

