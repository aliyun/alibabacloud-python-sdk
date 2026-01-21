# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListHostGroupAccountNamesForUserResponseBody(DaraModel):
    def __init__(
        self,
        host_account_names: List[str] = None,
        request_id: str = None,
    ):
        # An array that consists of the names of host accounts.
        self.host_account_names = host_account_names
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.host_account_names is not None:
            result['HostAccountNames'] = self.host_account_names

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostAccountNames') is not None:
            self.host_account_names = m.get('HostAccountNames')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

