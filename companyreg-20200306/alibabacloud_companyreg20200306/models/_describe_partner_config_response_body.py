# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePartnerConfigResponseBody(DaraModel):
    def __init__(
        self,
        contact: str = None,
        partner_code: str = None,
        partner_name: str = None,
        request_id: str = None,
    ):
        self.contact = contact
        self.partner_code = partner_code
        self.partner_name = partner_name
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact is not None:
            result['Contact'] = self.contact

        if self.partner_code is not None:
            result['PartnerCode'] = self.partner_code

        if self.partner_name is not None:
            result['PartnerName'] = self.partner_name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Contact') is not None:
            self.contact = m.get('Contact')

        if m.get('PartnerCode') is not None:
            self.partner_code = m.get('PartnerCode')

        if m.get('PartnerName') is not None:
            self.partner_name = m.get('PartnerName')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

