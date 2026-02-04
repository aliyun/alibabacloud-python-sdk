# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDCdnDomainSchdmByPropertyRequest(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        property: str = None,
    ):
        # The name of the accelerated domain for which you want to change the acceleration region. You can specify only one domain name.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # The region where the acceleration service is deployed. Valid values:
        # 
        # *   **domestic**: Chinese mainland
        # *   **overseas**: global (excluding mainland China)
        # *   **global**: global
        # 
        # This parameter is required.
        self.property = property

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.property is not None:
            result['Property'] = self.property

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('Property') is not None:
            self.property = m.get('Property')

        return self

