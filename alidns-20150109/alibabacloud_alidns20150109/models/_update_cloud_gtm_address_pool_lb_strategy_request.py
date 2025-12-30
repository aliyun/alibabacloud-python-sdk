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
        # *   zh-CN: Chinese
        # *   en-US (default): English
        self.accept_language = accept_language
        # Load balancing policy among addresses in the address pool:
        # - round_robin: Round-robin, for any source of DNS resolution requests, all addresses are returned. The order of all addresses is rotated each time.
        # - sequence: Sequential, for any source of DNS resolution requests, the address with the smaller sequence number (the sequence number indicates the priority of address returns, with smaller numbers having higher priority) is returned. If the address with the smaller sequence number is unavailable, the next address with a smaller sequence number is returned.
        # - weight: Weighted, supports setting different weight values for each address, realizing the return of addresses according to the weight ratio for resolution queries.
        # - source_nearest: Source-nearest, i.e., intelligent resolution function, where GTM can return different addresses based on the source of different DNS resolution requests, achieving the effect of users accessing nearby.
        self.address_lb_strategy = address_lb_strategy
        # The ID of the address pool. This ID uniquely identifies the address pool.
        self.address_pool_id = address_pool_id
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The mode used if the address with the smallest sequence number is recovered. This parameter is required only when AddressLbStrategy is set to sequence. Valid values:
        # 
        # *   preemptive: The address with the smallest sequence number is preferentially used if this address is recovered.
        # *   non_preemptive: The current address is still used even if the address with the smallest sequence number is recovered.
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

