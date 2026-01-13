# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AccountInfoManageRequest(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        name: str = None,
        quark_key: str = None,
        quark_name: str = None,
        test_qps: int = None,
        test_query_per_day: int = None,
    ):
        self.account_id = account_id
        self.name = name
        self.quark_key = quark_key
        self.quark_name = quark_name
        self.test_qps = test_qps
        self.test_query_per_day = test_query_per_day

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['accountId'] = self.account_id

        if self.name is not None:
            result['name'] = self.name

        if self.quark_key is not None:
            result['quarkKey'] = self.quark_key

        if self.quark_name is not None:
            result['quarkName'] = self.quark_name

        if self.test_qps is not None:
            result['testQps'] = self.test_qps

        if self.test_query_per_day is not None:
            result['testQueryPerDay'] = self.test_query_per_day

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('quarkKey') is not None:
            self.quark_key = m.get('quarkKey')

        if m.get('quarkName') is not None:
            self.quark_name = m.get('quarkName')

        if m.get('testQps') is not None:
            self.test_qps = m.get('testQps')

        if m.get('testQueryPerDay') is not None:
            self.test_query_per_day = m.get('testQueryPerDay')

        return self

