# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateCloudGtmInstanceConfigLbStrategyRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        address_pool_lb_strategy: str = None,
        client_token: str = None,
        config_id: str = None,
        instance_id: str = None,
        sequence_lb_strategy_mode: str = None,
    ):
        # The language in which the returned results are displayed. Valid values:
        # 
        # *   **zh-CN**: Chinese
        # *   **en-US** (default): English
        self.accept_language = accept_language
        # The new policy for load balancing between address pools. Valid values:
        # 
        # *   round_robin: All address pools are returned for Domain Name System (DNS) requests from any source. All address pools are sorted in round-robin mode each time they are returned.
        # *   sequence: The address pool with the smallest sequence number is preferentially returned for DNS requests from any source. The sequence number indicates the priority for returning the address pool. A smaller sequence number indicates a higher priority. If the address pool with the smallest sequence number is unavailable, the address pool with the second smallest sequence number is returned.
        # *   weight: You can set a different weight value for each address pool. This way, address pools are returned based on the weight values.
        # *   source_nearest: GTM returns different address pools based on the sources of DNS requests. This way, users can access nearby address pools.
        self.address_pool_lb_strategy = address_pool_lb_strategy
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The configuration ID of the access domain name. Two configuration IDs exist when the access domain name is bound to the same GTM instance but an A record and an AAAA record are configured for the access domain name. The configuration ID uniquely identifies a configuration.
        # 
        # You can call the [ListCloudGtmInstanceConfigs](~~ListCloudGtmInstanceConfigs~~) operation to query the configuration ID of the desired access domain name.
        self.config_id = config_id
        # The ID of the GTM 3.0 instance for which you want to modify the load balancing policy.
        self.instance_id = instance_id
        # The mode used if the address pool with the smallest sequence number is recovered. This parameter is required when AddressPoolLbStrategy is set to sequence. Valid values:
        # 
        # *   preemptive: The address pool with the smallest sequence number is preferentially used if this address pool is recovered.
        # *   non_preemptive: The current address pool is still used even if the address pool with the smallest sequence number is recovered.
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

        if self.address_pool_lb_strategy is not None:
            result['AddressPoolLbStrategy'] = self.address_pool_lb_strategy

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.config_id is not None:
            result['ConfigId'] = self.config_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.sequence_lb_strategy_mode is not None:
            result['SequenceLbStrategyMode'] = self.sequence_lb_strategy_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('AddressPoolLbStrategy') is not None:
            self.address_pool_lb_strategy = m.get('AddressPoolLbStrategy')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('SequenceLbStrategyMode') is not None:
            self.sequence_lb_strategy_mode = m.get('SequenceLbStrategyMode')

        return self

