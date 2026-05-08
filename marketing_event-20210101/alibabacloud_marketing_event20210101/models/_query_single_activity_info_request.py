# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QuerySingleActivityInfoRequest(DaraModel):
    def __init__(
        self,
        activity_id: str = None,
        company_name: str = None,
        customer_name: str = None,
        mobile: str = None,
        qrcode: str = None,
    ):
        # This parameter is required.
        self.activity_id = activity_id
        self.company_name = company_name
        self.customer_name = customer_name
        self.mobile = mobile
        self.qrcode = qrcode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.activity_id is not None:
            result['ActivityId'] = self.activity_id

        if self.company_name is not None:
            result['CompanyName'] = self.company_name

        if self.customer_name is not None:
            result['CustomerName'] = self.customer_name

        if self.mobile is not None:
            result['Mobile'] = self.mobile

        if self.qrcode is not None:
            result['QRCode'] = self.qrcode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivityId') is not None:
            self.activity_id = m.get('ActivityId')

        if m.get('CompanyName') is not None:
            self.company_name = m.get('CompanyName')

        if m.get('CustomerName') is not None:
            self.customer_name = m.get('CustomerName')

        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')

        if m.get('QRCode') is not None:
            self.qrcode = m.get('QRCode')

        return self

