# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDnsGtmInstanceSystemCnameResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        system_cname: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The CNAME domain name assigned by the system.
        self.system_cname = system_cname

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.system_cname is not None:
            result['SystemCname'] = self.system_cname

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SystemCname') is not None:
            self.system_cname = m.get('SystemCname')

        return self

