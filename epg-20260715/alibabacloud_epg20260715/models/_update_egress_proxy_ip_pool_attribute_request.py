# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateEgressProxyIpPoolAttributeRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        dry_run: bool = None,
        egress_proxy_ip_pool_id: str = None,
        egress_proxy_ip_pool_name: str = None,
        hash_factor: str = None,
        hash_header_name: str = None,
        scheduler: str = None,
    ):
        self.client_token = client_token
        self.description = description
        self.dry_run = dry_run
        # This parameter is required.
        self.egress_proxy_ip_pool_id = egress_proxy_ip_pool_id
        self.egress_proxy_ip_pool_name = egress_proxy_ip_pool_name
        self.hash_factor = hash_factor
        self.hash_header_name = hash_header_name
        self.scheduler = scheduler

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.description is not None:
            result['Description'] = self.description

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.egress_proxy_ip_pool_id is not None:
            result['EgressProxyIpPoolId'] = self.egress_proxy_ip_pool_id

        if self.egress_proxy_ip_pool_name is not None:
            result['EgressProxyIpPoolName'] = self.egress_proxy_ip_pool_name

        if self.hash_factor is not None:
            result['HashFactor'] = self.hash_factor

        if self.hash_header_name is not None:
            result['HashHeaderName'] = self.hash_header_name

        if self.scheduler is not None:
            result['Scheduler'] = self.scheduler

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('EgressProxyIpPoolId') is not None:
            self.egress_proxy_ip_pool_id = m.get('EgressProxyIpPoolId')

        if m.get('EgressProxyIpPoolName') is not None:
            self.egress_proxy_ip_pool_name = m.get('EgressProxyIpPoolName')

        if m.get('HashFactor') is not None:
            self.hash_factor = m.get('HashFactor')

        if m.get('HashHeaderName') is not None:
            self.hash_header_name = m.get('HashHeaderName')

        if m.get('Scheduler') is not None:
            self.scheduler = m.get('Scheduler')

        return self

