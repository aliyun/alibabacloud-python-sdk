# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyRateLimitPolicyRequest(DaraModel):
    def __init__(
        self,
        gw_cluster_id: str = None,
        policy_id: str = None,
        rate_limit_rpm: str = None,
        rate_limit_tpm: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.gw_cluster_id = gw_cluster_id
        # This parameter is required.
        self.policy_id = policy_id
        self.rate_limit_rpm = rate_limit_rpm
        self.rate_limit_tpm = rate_limit_tpm
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gw_cluster_id is not None:
            result['GwClusterId'] = self.gw_cluster_id

        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        if self.rate_limit_rpm is not None:
            result['RateLimitRpm'] = self.rate_limit_rpm

        if self.rate_limit_tpm is not None:
            result['RateLimitTpm'] = self.rate_limit_tpm

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GwClusterId') is not None:
            self.gw_cluster_id = m.get('GwClusterId')

        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        if m.get('RateLimitRpm') is not None:
            self.rate_limit_rpm = m.get('RateLimitRpm')

        if m.get('RateLimitTpm') is not None:
            self.rate_limit_tpm = m.get('RateLimitTpm')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

