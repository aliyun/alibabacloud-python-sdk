# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class VerifyLiveDomainOwnerRequest(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        owner_id: int = None,
        region_id: str = None,
        verify_type: str = None,
    ):
        # The domain name for which you want to verify the ownership. You can specify only one domain name in each request.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        self.owner_id = owner_id
        self.region_id = region_id
        # The verification method. Valid values:
        # 
        # *   dnsCheck: DNS record verification
        # *   fileCheck: file verification
        # 
        # This parameter is required.
        self.verify_type = verify_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.verify_type is not None:
            result['VerifyType'] = self.verify_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('VerifyType') is not None:
            self.verify_type = m.get('VerifyType')

        return self

