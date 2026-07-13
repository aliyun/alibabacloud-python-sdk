# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateCloudGtmAddressPoolLbStrategyRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        address_lb_strategy: str = None,
        address_pool_id: str = None,
        client_token: str = None,
        sequence_lb_strategy_mode: str = None,
    ):
        # The language of the response. Valid values:
        # 
        # - zh-CN: Chinese
        # 
        # - en-US (default): English
        self.accept_language = accept_language
        # The load balancing policy for the addresses in the address pool.
        # 
        # - round_robin: Round robin. For each DNS query, all addresses are returned in a rotating order.
        # 
        # - sequence: Sequence. The address with the highest priority is returned. Priority is determined by the ordinal number of an address. A smaller ordinal number indicates a higher priority. If an address is unavailable, the address with the next highest priority is returned.
        # 
        # - weight: Weight. DNS queries are resolved based on the weight that you set for each address.
        # 
        # - source_nearest: Source nearest. This is an intelligent DNS resolution feature. GTM returns an address based on the source of the DNS query. This directs users to the nearest resource.
        self.address_lb_strategy = address_lb_strategy
        # The unique ID of the address pool.
        self.address_pool_id = address_pool_id
        # A client-generated token that is used to ensure the idempotence of the request. The token must be unique for each request and can contain up to 64 ASCII characters.
        self.client_token = client_token
        # The recovery mode when the load balancing policy is \\`sequence\\`.
        # 
        # - preemptive: Preemptive mode. If a higher-priority address recovers, it is used preferentially.
        # 
        # - non_preemptive: Non-preemptive mode. If a higher-priority address recovers, the current address continues to be used.
        self.sequence_lb_strategy_mode = sequence_lb_strategy_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.address_lb_strategy is not None:
            result['AddressLbStrategy'] = self.address_lb_strategy

        if self.address_pool_id is not None:
            result['AddressPoolId'] = self.address_pool_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.sequence_lb_strategy_mode is not None:
            result['SequenceLbStrategyMode'] = self.sequence_lb_strategy_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('AddressLbStrategy') is not None:
            self.address_lb_strategy = m.get('AddressLbStrategy')

        if m.get('AddressPoolId') is not None:
            self.address_pool_id = m.get('AddressPoolId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('SequenceLbStrategyMode') is not None:
            self.sequence_lb_strategy_mode = m.get('SequenceLbStrategyMode')

        return self

