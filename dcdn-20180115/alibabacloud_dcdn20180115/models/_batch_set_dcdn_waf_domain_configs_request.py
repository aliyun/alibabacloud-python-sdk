# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BatchSetDcdnWafDomainConfigsRequest(DaraModel):
    def __init__(
        self,
        client_ip_tag: str = None,
        defense_status: str = None,
        domain_names: str = None,
    ):
        # Specifies the header that records the IP address to be obtained. If the default header is selected, the value of this parameter is empty. If a custom header is selected, the value of this parameter is the value specified by the user. Separate multiple values with commas (,). You can specify a maximum of five values.
        self.client_ip_tag = client_ip_tag
        # The protection status of the domain name. Valid values: on, off, and empty string.
        # 
        # *   When you add a domain name, the value of this parameter is **on**, and the value of ClientIpTag takes effect, which is empty if the default header is selected and is the value specified by the user if a custom header is selected.
        # *   When you delete a domain name, the value of this parameter is **off**, and the value of ClientIpTag does not take effect.
        # *   When you only modify the value of ClientIpTag, the value of DefenseStatus is an empty string.
        self.defense_status = defense_status
        # The protected domain names for which you want to change the protection status. You can specify up to 50 domain names. Separate multiple domain names with commas (,).
        # 
        # This parameter is required.
        self.domain_names = domain_names

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_ip_tag is not None:
            result['ClientIpTag'] = self.client_ip_tag

        if self.defense_status is not None:
            result['DefenseStatus'] = self.defense_status

        if self.domain_names is not None:
            result['DomainNames'] = self.domain_names

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientIpTag') is not None:
            self.client_ip_tag = m.get('ClientIpTag')

        if m.get('DefenseStatus') is not None:
            self.defense_status = m.get('DefenseStatus')

        if m.get('DomainNames') is not None:
            self.domain_names = m.get('DomainNames')

        return self

