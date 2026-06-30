# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GrantPromotionOfferForPartnerRequest(DaraModel):
    def __init__(
        self,
        activity_code: str = None,
        activity_id: str = None,
        belong_id: str = None,
        channel: str = None,
        employee_code: str = None,
        remark: str = None,
    ):
        self.activity_code = activity_code
        # The activity ID.
        self.activity_id = activity_id
        # The user ID.
        self.belong_id = belong_id
        # The channel.
        self.channel = channel
        # The employee code.
        self.employee_code = employee_code
        # The operation remarks (audit information).
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.activity_code is not None:
            result['ActivityCode'] = self.activity_code

        if self.activity_id is not None:
            result['ActivityId'] = self.activity_id

        if self.belong_id is not None:
            result['BelongId'] = self.belong_id

        if self.channel is not None:
            result['Channel'] = self.channel

        if self.employee_code is not None:
            result['EmployeeCode'] = self.employee_code

        if self.remark is not None:
            result['Remark'] = self.remark

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivityCode') is not None:
            self.activity_code = m.get('ActivityCode')

        if m.get('ActivityId') is not None:
            self.activity_id = m.get('ActivityId')

        if m.get('BelongId') is not None:
            self.belong_id = m.get('BelongId')

        if m.get('Channel') is not None:
            self.channel = m.get('Channel')

        if m.get('EmployeeCode') is not None:
            self.employee_code = m.get('EmployeeCode')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        return self

