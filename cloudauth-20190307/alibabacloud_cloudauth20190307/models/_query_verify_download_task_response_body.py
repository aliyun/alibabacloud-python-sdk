# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryVerifyDownloadTaskResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        finish: bool = None,
        request_id: str = None,
        status: int = None,
        url: str = None,
    ):
        # The error code.
        self.error_code = error_code
        # Indicates whether the download task is complete. Valid values:
        # - **true**: Complete.
        # - **false**: Not complete.
        self.finish = finish
        # Id of the request
        self.request_id = request_id
        # The task status. Valid values:
        # - **1**: The file is being generated.
        # - **2**: The file is generated.
        # - **3**: The file failed to be generated.
        self.status = status
        # The download URL.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.finish is not None:
            result['Finish'] = self.finish

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('Finish') is not None:
            self.finish = m.get('Finish')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

