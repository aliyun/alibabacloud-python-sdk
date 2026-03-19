# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeBackSourceCidrResponseBody(DaraModel):
    def __init__(
        self,
        cidr_list: List[str] = None,
        request_id: str = None,
    ):
        self.cidr_list = cidr_list
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cidr_list is not None:
            result['CidrList'] = self.cidr_list

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CidrList') is not None:
            self.cidr_list = m.get('CidrList')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

