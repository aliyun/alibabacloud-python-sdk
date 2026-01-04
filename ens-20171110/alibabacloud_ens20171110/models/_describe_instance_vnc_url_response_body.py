# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeInstanceVncUrlResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        vnc_url: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The URL of the VNC management terminal.
        self.vnc_url = vnc_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.vnc_url is not None:
            result['VncUrl'] = self.vnc_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('VncUrl') is not None:
            self.vnc_url = m.get('VncUrl')

        return self

