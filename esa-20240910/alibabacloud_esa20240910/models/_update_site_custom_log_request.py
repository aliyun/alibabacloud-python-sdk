# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateSiteCustomLogRequest(DaraModel):
    def __init__(
        self,
        cookies: List[str] = None,
        request_headers: List[str] = None,
        response_headers: List[str] = None,
        site_id: int = None,
    ):
        # The cookie fields.
        self.cookies = cookies
        # The request header fields.
        self.request_headers = request_headers
        # The response header fields.
        self.response_headers = response_headers
        # site id
        self.site_id = site_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cookies is not None:
            result['Cookies'] = self.cookies

        if self.request_headers is not None:
            result['RequestHeaders'] = self.request_headers

        if self.response_headers is not None:
            result['ResponseHeaders'] = self.response_headers

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cookies') is not None:
            self.cookies = m.get('Cookies')

        if m.get('RequestHeaders') is not None:
            self.request_headers = m.get('RequestHeaders')

        if m.get('ResponseHeaders') is not None:
            self.response_headers = m.get('ResponseHeaders')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        return self

