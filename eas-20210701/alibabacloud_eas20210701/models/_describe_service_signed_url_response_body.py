# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeServiceSignedUrlResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        signed_url: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        # The service URL.
        self.signed_url = signed_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.signed_url is not None:
            result['SignedUrl'] = self.signed_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SignedUrl') is not None:
            self.signed_url = m.get('SignedUrl')

        return self

