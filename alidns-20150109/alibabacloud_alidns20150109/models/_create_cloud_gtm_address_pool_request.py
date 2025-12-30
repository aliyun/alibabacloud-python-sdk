# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateCloudGtmAddressPoolRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        address_pool_name: str = None,
        address_pool_type: str = None,
        client_token: str = None,
        enable_status: str = None,
        health_judgement: str = None,
        remark: str = None,
    ):
        # The language of the response. Valid values:
        # 
        # *   zh-CN: Chinese
        # *   en-US (default): English
        self.accept_language = accept_language
        # Address pool name, helping users distinguish the purpose of address pools.
        self.address_pool_name = address_pool_name
        # The type of the address pool. Valid values:
        # 
        # *   IPv4: IPv4 addresses are returned for Domain Name System (DNS) resolution.
        # *   IPv6: IPv6 addresses are returned for DNS resolution.
        # *   domain: Domain names are returned for DNS resolution.
        self.address_pool_type = address_pool_type
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The enabling state of the address pool. Valid values:
        # 
        # *   enable: The address pool is enabled, and the addresses in the address pool are returned for DNS resolution when the health check results are normal.
        # *   disable: The address pool is disabled, and the addresses in the address pool are not returned for DNS resolution regardless of whether the health check results are normal or not.
        self.enable_status = enable_status
        # The condition for determining the health status of the address pool. Valid values:
        # 
        # *   any_ok: At least one address in the address pool is available.
        # *   p30_ok: At least 30% of the addresses in the address pool are available.
        # *   p50_ok: At least 50% of the addresses in the address pool are available.
        # *   p70_ok: At least 70% of the addresses in the address pool are available.
        # *   all_ok: All addresses in the address pool are available.
        self.health_judgement = health_judgement
        # Remarks for the address pool, helping users distinguish the usage scenarios of different address pools.
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.address_pool_name is not None:
            result['AddressPoolName'] = self.address_pool_name

        if self.address_pool_type is not None:
            result['AddressPoolType'] = self.address_pool_type

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.enable_status is not None:
            result['EnableStatus'] = self.enable_status

        if self.health_judgement is not None:
            result['HealthJudgement'] = self.health_judgement

        if self.remark is not None:
            result['Remark'] = self.remark

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('AddressPoolName') is not None:
            self.address_pool_name = m.get('AddressPoolName')

        if m.get('AddressPoolType') is not None:
            self.address_pool_type = m.get('AddressPoolType')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('EnableStatus') is not None:
            self.enable_status = m.get('EnableStatus')

        if m.get('HealthJudgement') is not None:
            self.health_judgement = m.get('HealthJudgement')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        return self

