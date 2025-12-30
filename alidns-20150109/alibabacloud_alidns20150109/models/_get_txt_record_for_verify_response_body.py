# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetTxtRecordForVerifyResponseBody(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        parent_domain_name: str = None,
        rr: str = None,
        request_id: str = None,
        value: str = None,
    ):
        # The domain name.
        # 
        # >  If you do not specify this parameter, it is not returned.
        self.domain_name = domain_name
        # The top-level domain name.
        self.parent_domain_name = parent_domain_name
        # The hostname.
        self.rr = rr
        # The request ID.
        self.request_id = request_id
        # The record value.
        # 
        # >  The validity period is three days.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.parent_domain_name is not None:
            result['ParentDomainName'] = self.parent_domain_name

        if self.rr is not None:
            result['RR'] = self.rr

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('ParentDomainName') is not None:
            self.parent_domain_name = m.get('ParentDomainName')

        if m.get('RR') is not None:
            self.rr = m.get('RR')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

