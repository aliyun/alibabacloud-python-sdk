# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteBrowserOut(DaraModel):
    def __init__(
        self,
        browser_id: str = None,
        browser_name: str = None,
        status: str = None,
    ):
        self.browser_id = browser_id
        self.browser_name = browser_name
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.browser_id is not None:
            result['browserId'] = self.browser_id

        if self.browser_name is not None:
            result['browserName'] = self.browser_name

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('browserId') is not None:
            self.browser_id = m.get('browserId')

        if m.get('browserName') is not None:
            self.browser_name = m.get('browserName')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

