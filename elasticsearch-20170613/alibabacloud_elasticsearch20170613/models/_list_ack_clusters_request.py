# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAckClustersRequest(DaraModel):
    def __init__(
        self,
        page: int = None,
        size: int = None,
        vpc_id: str = None,
    ):
        # The number of the page to return.
        self.page = page
        # The number of entries to return on each page.
        self.size = size
        # The ID of the virtual private cloud (VPC) to which the ACK clusters belong.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page is not None:
            result['page'] = self.page

        if self.size is not None:
            result['size'] = self.size

        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('size') is not None:
            self.size = m.get('size')

        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')

        return self

