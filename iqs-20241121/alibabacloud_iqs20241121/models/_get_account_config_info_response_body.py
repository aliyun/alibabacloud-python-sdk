# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAccountConfigInfoResponseBody(DaraModel):
    def __init__(
        self,
        account_status: str = None,
        available_time: str = None,
        bill_qps: str = None,
        ladder_type: str = None,
        main_account_id: str = None,
        request_id: str = None,
    ):
        self.account_status = account_status
        self.available_time = available_time
        self.bill_qps = bill_qps
        self.ladder_type = ladder_type
        self.main_account_id = main_account_id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_status is not None:
            result['accountStatus'] = self.account_status

        if self.available_time is not None:
            result['availableTime'] = self.available_time

        if self.bill_qps is not None:
            result['billQps'] = self.bill_qps

        if self.ladder_type is not None:
            result['ladderType'] = self.ladder_type

        if self.main_account_id is not None:
            result['mainAccountId'] = self.main_account_id

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountStatus') is not None:
            self.account_status = m.get('accountStatus')

        if m.get('availableTime') is not None:
            self.available_time = m.get('availableTime')

        if m.get('billQps') is not None:
            self.bill_qps = m.get('billQps')

        if m.get('ladderType') is not None:
            self.ladder_type = m.get('ladderType')

        if m.get('mainAccountId') is not None:
            self.main_account_id = m.get('mainAccountId')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

