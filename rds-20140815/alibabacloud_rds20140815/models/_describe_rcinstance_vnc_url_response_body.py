# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeRCInstanceVncUrlResponseBody(DaraModel):
    def __init__(
        self,
        login_url: str = None,
        request_id: str = None,
    ):
        # The VNC logon URL.
        # 
        # 
        # >Notice: The VNC logon URL is time-sensitive and valid for 15 seconds. If the URL is not used within 15 seconds after a successful API call, it automatically expires. You must call the API operation again to obtain a new URL.
        self.login_url = login_url
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.login_url is not None:
            result['LoginUrl'] = self.login_url

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LoginUrl') is not None:
            self.login_url = m.get('LoginUrl')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

