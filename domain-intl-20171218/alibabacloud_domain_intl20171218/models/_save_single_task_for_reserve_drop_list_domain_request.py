# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SaveSingleTaskForReserveDropListDomainRequest(DaraModel):
    def __init__(
        self,
        contact_template_id: str = None,
        dns_1: str = None,
        dns_2: str = None,
        domain_name: str = None,
    ):
        # This parameter is required.
        self.contact_template_id = contact_template_id
        self.dns_1 = dns_1
        self.dns_2 = dns_2
        # This parameter is required.
        self.domain_name = domain_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_template_id is not None:
            result['ContactTemplateId'] = self.contact_template_id

        if self.dns_1 is not None:
            result['Dns1'] = self.dns_1

        if self.dns_2 is not None:
            result['Dns2'] = self.dns_2

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactTemplateId') is not None:
            self.contact_template_id = m.get('ContactTemplateId')

        if m.get('Dns1') is not None:
            self.dns_1 = m.get('Dns1')

        if m.get('Dns2') is not None:
            self.dns_2 = m.get('Dns2')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        return self

