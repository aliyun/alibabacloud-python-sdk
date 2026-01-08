# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePrefixListsRequest(DaraModel):
    def __init__(
        self,
        region_no: str = None,
        source_ip: str = None,
    ):
        # The region ID of the instance.
        # 
        # This parameter is required.
        self.region_no = region_no
        # The source IP address of the request.
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_no is not None:
            result['RegionNo'] = self.region_no

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        return self

