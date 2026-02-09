# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListFundAccountRequest(DaraModel):
    def __init__(
        self,
        nbid: str = None,
        query_only_in_use: bool = None,
        query_only_manage: bool = None,
    ):
        self.nbid = nbid
        self.query_only_in_use = query_only_in_use
        self.query_only_manage = query_only_manage

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.nbid is not None:
            result['Nbid'] = self.nbid

        if self.query_only_in_use is not None:
            result['QueryOnlyInUse'] = self.query_only_in_use

        if self.query_only_manage is not None:
            result['QueryOnlyManage'] = self.query_only_manage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')

        if m.get('QueryOnlyInUse') is not None:
            self.query_only_in_use = m.get('QueryOnlyInUse')

        if m.get('QueryOnlyManage') is not None:
            self.query_only_manage = m.get('QueryOnlyManage')

        return self

