# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_domain20180129 import models as main_models
from darabonba.model import DaraModel

class SaveBatchTaskForReserveDropListDomainRequest(DaraModel):
    def __init__(
        self,
        contact_template_id: str = None,
        domains: List[main_models.SaveBatchTaskForReserveDropListDomainRequestDomains] = None,
    ):
        # This parameter is required.
        self.contact_template_id = contact_template_id
        # This parameter is required.
        self.domains = domains

    def validate(self):
        if self.domains:
            for v1 in self.domains:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_template_id is not None:
            result['ContactTemplateId'] = self.contact_template_id

        result['Domains'] = []
        if self.domains is not None:
            for k1 in self.domains:
                result['Domains'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactTemplateId') is not None:
            self.contact_template_id = m.get('ContactTemplateId')

        self.domains = []
        if m.get('Domains') is not None:
            for k1 in m.get('Domains'):
                temp_model = main_models.SaveBatchTaskForReserveDropListDomainRequestDomains()
                self.domains.append(temp_model.from_map(k1))

        return self

class SaveBatchTaskForReserveDropListDomainRequestDomains(DaraModel):
    def __init__(
        self,
        dns_1: str = None,
        dns_2: str = None,
        domain_name: str = None,
    ):
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
        if self.dns_1 is not None:
            result['Dns1'] = self.dns_1

        if self.dns_2 is not None:
            result['Dns2'] = self.dns_2

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Dns1') is not None:
            self.dns_1 = m.get('Dns1')

        if m.get('Dns2') is not None:
            self.dns_2 = m.get('Dns2')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        return self

