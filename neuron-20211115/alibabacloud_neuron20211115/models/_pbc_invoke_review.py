# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PbcInvokeReview(DaraModel):
    def __init__(
        self,
        applicant: str = None,
        gmt_create: str = None,
        id: int = None,
        invoke_id: int = None,
        invoke_pbc_id: int = None,
        invoke_pbc_name: str = None,
        pbc_id: int = None,
        pbc_name: str = None,
        request_id: str = None,
        reviewer: str = None,
        reviewer_id: str = None,
        status: str = None,
        usage: str = None,
    ):
        self.applicant = applicant
        self.gmt_create = gmt_create
        self.id = id
        self.invoke_id = invoke_id
        self.invoke_pbc_id = invoke_pbc_id
        self.invoke_pbc_name = invoke_pbc_name
        self.pbc_id = pbc_id
        self.pbc_name = pbc_name
        self.request_id = request_id
        self.reviewer = reviewer
        self.reviewer_id = reviewer_id
        self.status = status
        self.usage = usage

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.applicant is not None:
            result['applicant'] = self.applicant

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.id is not None:
            result['id'] = self.id

        if self.invoke_id is not None:
            result['invokeId'] = self.invoke_id

        if self.invoke_pbc_id is not None:
            result['invokePbcId'] = self.invoke_pbc_id

        if self.invoke_pbc_name is not None:
            result['invokePbcName'] = self.invoke_pbc_name

        if self.pbc_id is not None:
            result['pbcId'] = self.pbc_id

        if self.pbc_name is not None:
            result['pbcName'] = self.pbc_name

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.reviewer is not None:
            result['reviewer'] = self.reviewer

        if self.reviewer_id is not None:
            result['reviewerId'] = self.reviewer_id

        if self.status is not None:
            result['status'] = self.status

        if self.usage is not None:
            result['usage'] = self.usage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('applicant') is not None:
            self.applicant = m.get('applicant')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('invokeId') is not None:
            self.invoke_id = m.get('invokeId')

        if m.get('invokePbcId') is not None:
            self.invoke_pbc_id = m.get('invokePbcId')

        if m.get('invokePbcName') is not None:
            self.invoke_pbc_name = m.get('invokePbcName')

        if m.get('pbcId') is not None:
            self.pbc_id = m.get('pbcId')

        if m.get('pbcName') is not None:
            self.pbc_name = m.get('pbcName')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('reviewer') is not None:
            self.reviewer = m.get('reviewer')

        if m.get('reviewerId') is not None:
            self.reviewer_id = m.get('reviewerId')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('usage') is not None:
            self.usage = m.get('usage')

        return self

