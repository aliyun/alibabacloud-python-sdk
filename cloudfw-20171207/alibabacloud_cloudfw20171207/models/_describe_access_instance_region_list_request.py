# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAccessInstanceRegionListRequest(DaraModel):
    def __init__(
        self,
        access_instance_status: str = None,
        access_instance_type: str = None,
    ):
        self.access_instance_status = access_instance_status
        self.access_instance_type = access_instance_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_instance_status is not None:
            result['AccessInstanceStatus'] = self.access_instance_status

        if self.access_instance_type is not None:
            result['AccessInstanceType'] = self.access_instance_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessInstanceStatus') is not None:
            self.access_instance_status = m.get('AccessInstanceStatus')

        if m.get('AccessInstanceType') is not None:
            self.access_instance_type = m.get('AccessInstanceType')

        return self

