# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class WebsiteAddDnsRecordRequest(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        rr: str = None,
        source: str = None,
        type: str = None,
        user_id: str = None,
        value: str = None,
        website_no: str = None,
    ):
        self.domain_name = domain_name
        self.rr = rr
        self.source = source
        self.type = type
        self.user_id = user_id
        self.value = value
        self.website_no = website_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.rr is not None:
            result['Rr'] = self.rr

        if self.source is not None:
            result['Source'] = self.source

        if self.type is not None:
            result['Type'] = self.type

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.value is not None:
            result['Value'] = self.value

        if self.website_no is not None:
            result['WebsiteNo'] = self.website_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('Rr') is not None:
            self.rr = m.get('Rr')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        if m.get('WebsiteNo') is not None:
            self.website_no = m.get('WebsiteNo')

        return self

