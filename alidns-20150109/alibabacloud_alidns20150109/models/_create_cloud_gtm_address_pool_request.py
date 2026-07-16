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
        # - zh-CN: Chinese.
        # 
        # - en-US: English. This is the default value.
        self.accept_language = accept_language
        # The name of the address pool. The name helps you identify the purpose of the address pool.
        self.address_pool_name = address_pool_name
        # The type of the address pool. Valid values:
        # 
        # - IPv4: The endpoint is an IPv4 address.
        # 
        # - IPv6: The endpoint is an IPv6 address.
        # 
        # - domain: The endpoint is a domain name.
        self.address_pool_type = address_pool_type
        # The client token that is used to ensure the idempotence of the request. Generate a unique token for each request. The token can be up to 64 ASCII characters in length.
        self.client_token = client_token
        # The status of the address pool. Valid values:
        # 
        # - enable: The address pool is enabled and can be used for DNS resolution if it passes health checks.
        # 
        # - disable: The address pool is disabled and cannot be used for DNS resolution, regardless of its health check status.
        self.enable_status = enable_status
        # The health status condition of the address pool. Valid values:
        # 
        # - any_ok: At least one address in the address pool is active.
        # 
        # - p30_ok: At least 30% of the addresses in the address pool are active.
        # 
        # - p50_ok: At least 50% of the addresses in the address pool are active.
        # 
        # - p70_ok: At least 70% of the addresses in the address pool are active.
        # 
        # - all_ok: All addresses in the address pool are active.
        self.health_judgement = health_judgement
        # Remarks about the address pool. The remarks help you identify the scenario in which the address pool is used.
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

