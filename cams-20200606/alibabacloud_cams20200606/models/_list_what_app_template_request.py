# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListWhatAppTemplateRequest(DaraModel):
    def __init__(
        self,
        cust_space_id: str = None,
        hetu_params: str = None,
    ):
        self.cust_space_id = cust_space_id
        self.hetu_params = hetu_params

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id

        if self.hetu_params is not None:
            result['HetuParams'] = self.hetu_params

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')

        if m.get('HetuParams') is not None:
            self.hetu_params = m.get('HetuParams')

        return self

