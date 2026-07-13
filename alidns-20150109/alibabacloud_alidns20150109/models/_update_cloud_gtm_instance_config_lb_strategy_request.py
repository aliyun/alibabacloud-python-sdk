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
        # The language of the response. Valid values:
        # 
        # - **zh-CN**: Chinese.
        # 
        # - **en-US**: English. This is the default value.
        self.accept_language = accept_language
        # The load balancing policy for the address pools. Valid values:
        # 
        # - round_robin: Returns all address pools for any DNS request. The address pools are rotated for each request.
        # 
        # - sequence: Returns the address pool with the smallest ordinal number. The smaller the ordinal number, the higher the priority. If the primary address pool is unavailable, the next address pool in the sequence is used.
        # 
        # - weight: Distributes DNS requests to address pools based on their configured weights.
        # 
        # - source_nearest: Returns an address pool based on the proximity of the DNS request source. This implements intelligent DNS resolution and directs users to the nearest access point.
        self.address_pool_lb_strategy = address_pool_lb_strategy
        # A client-generated token that is used to ensure the idempotence of the request. The token must be unique among different requests. The token can contain a maximum of 64 ASCII characters.
        self.client_token = client_token
        # The ID of the instance configuration. A GTM instance can have multiple configurations for the same domain name, such as one for A records and another for AAAA records. The ConfigId uniquely identifies the configuration that you want to modify.
        # 
        # For more information, see [ListCloudGtmInstanceConfigs](https://help.aliyun.com/document_detail/2797349.html).
        self.config_id = config_id
        # The ID of the Global Traffic Manager (GTM) 3.0 instance.
        self.instance_id = instance_id
        # The recovery mode for a primary address pool when the load balancing policy is set to sequence. Valid values:
        # 
        # - preemptive: The system switches back to the primary address pool as soon as it recovers.
        # 
        # - non_preemptive: The system continues to use the current address pool even after the primary address pool recovers.
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

