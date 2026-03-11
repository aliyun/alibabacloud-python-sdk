# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_dlfnext20250310 import models as main_models
from darabonba.model import DaraModel

class GetVpcConfigResponseBody(DaraModel):
    def __init__(
        self,
        trusted_vpcs: List[main_models.GetVpcConfigResponseBodyTrustedVpcs] = None,
    ):
        self.trusted_vpcs = trusted_vpcs

    def validate(self):
        if self.trusted_vpcs:
            for v1 in self.trusted_vpcs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['trustedVpcs'] = []
        if self.trusted_vpcs is not None:
            for k1 in self.trusted_vpcs:
                result['trustedVpcs'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.trusted_vpcs = []
        if m.get('trustedVpcs') is not None:
            for k1 in m.get('trustedVpcs'):
                temp_model = main_models.GetVpcConfigResponseBodyTrustedVpcs()
                self.trusted_vpcs.append(temp_model.from_map(k1))

        return self

class GetVpcConfigResponseBodyTrustedVpcs(DaraModel):
    def __init__(
        self,
        created_at: int = None,
        extended_options: Dict[str, str] = None,
        vpc_id: str = None,
    ):
        self.created_at = created_at
        self.extended_options = extended_options
        # VPC ID。
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.extended_options is not None:
            result['extendedOptions'] = self.extended_options

        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('extendedOptions') is not None:
            self.extended_options = m.get('extendedOptions')

        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')

        return self

