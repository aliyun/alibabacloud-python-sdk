# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListSlbRequest(DaraModel):
    def __init__(
        self,
        address_type: str = None,
        slb_type: str = None,
        vpc_id: str = None,
    ):
        # The address type. Valid values:
        # - Internet: public address.
        # - Intranet: private network address.
        self.address_type = address_type
        # The SLB type. Valid values:
        # - clb: classic load balancing.
        # - alb: application load balancing.
        self.slb_type = slb_type
        # The VPC ID.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address_type is not None:
            result['AddressType'] = self.address_type

        if self.slb_type is not None:
            result['SlbType'] = self.slb_type

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')

        if m.get('SlbType') is not None:
            self.slb_type = m.get('SlbType')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

