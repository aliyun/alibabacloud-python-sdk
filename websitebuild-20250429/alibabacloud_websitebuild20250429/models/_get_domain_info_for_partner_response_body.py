# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_websitebuild20250429 import models as main_models
from darabonba.model import DaraModel

class GetDomainInfoForPartnerResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetDomainInfoForPartnerResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetDomainInfoForPartnerResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetDomainInfoForPartnerResponseBodyData(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        name_servers: str = None,
        ownership: main_models.GetDomainInfoForPartnerResponseBodyDataOwnership = None,
        registrar: str = None,
    ):
        self.domain_name = domain_name
        self.name_servers = name_servers
        self.ownership = ownership
        self.registrar = registrar

    def validate(self):
        if self.ownership:
            self.ownership.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.name_servers is not None:
            result['NameServers'] = self.name_servers

        if self.ownership is not None:
            result['Ownership'] = self.ownership.to_map()

        if self.registrar is not None:
            result['Registrar'] = self.registrar

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('NameServers') is not None:
            self.name_servers = m.get('NameServers')

        if m.get('Ownership') is not None:
            temp_model = main_models.GetDomainInfoForPartnerResponseBodyDataOwnership()
            self.ownership = temp_model.from_map(m.get('Ownership'))

        if m.get('Registrar') is not None:
            self.registrar = m.get('Registrar')

        return self

class GetDomainInfoForPartnerResponseBodyDataOwnership(DaraModel):
    def __init__(
        self,
        account: str = None,
        provider: str = None,
    ):
        self.account = account
        self.provider = provider

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account is not None:
            result['Account'] = self.account

        if self.provider is not None:
            result['Provider'] = self.provider

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            self.account = m.get('Account')

        if m.get('Provider') is not None:
            self.provider = m.get('Provider')

        return self

