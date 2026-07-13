# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateCloudGtmAddressPoolBasicConfigRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        address_pool_id: str = None,
        address_pool_name: str = None,
        client_token: str = None,
        health_judgement: str = None,
    ):
        # The language of the response. Valid values:
        # 
        # - zh-CN: Chinese
        # 
        # - en-US (default): English
        self.accept_language = accept_language
        # The unique ID of the address pool.
        self.address_pool_id = address_pool_id
        # The name of the address pool.
        self.address_pool_name = address_pool_name
        # The client token that is used to ensure the idempotence of the request. The client generates this token to make sure that each request is unique. The token can contain a maximum of 64 ASCII characters.
        self.client_token = client_token
        # The condition for determining the health status of the address pool.
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

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.address_pool_id is not None:
            result['AddressPoolId'] = self.address_pool_id

        if self.address_pool_name is not None:
            result['AddressPoolName'] = self.address_pool_name

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.health_judgement is not None:
            result['HealthJudgement'] = self.health_judgement

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('AddressPoolId') is not None:
            self.address_pool_id = m.get('AddressPoolId')

        if m.get('AddressPoolName') is not None:
            self.address_pool_name = m.get('AddressPoolName')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('HealthJudgement') is not None:
            self.health_judgement = m.get('HealthJudgement')

        return self

