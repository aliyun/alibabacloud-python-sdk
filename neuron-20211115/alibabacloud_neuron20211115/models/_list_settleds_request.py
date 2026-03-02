# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListSettledsRequest(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        applicant: str = None,
        enterprise_name: str = None,
        status: str = None,
    ):
        self.account_id = account_id
        self.applicant = applicant
        self.enterprise_name = enterprise_name
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['accountId'] = self.account_id

        if self.applicant is not None:
            result['applicant'] = self.applicant

        if self.enterprise_name is not None:
            result['enterpriseName'] = self.enterprise_name

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')

        if m.get('applicant') is not None:
            self.applicant = m.get('applicant')

        if m.get('enterpriseName') is not None:
            self.enterprise_name = m.get('enterpriseName')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

