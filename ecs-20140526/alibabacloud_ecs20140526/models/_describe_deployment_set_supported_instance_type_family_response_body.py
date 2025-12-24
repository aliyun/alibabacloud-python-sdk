# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDeploymentSetSupportedInstanceTypeFamilyResponseBody(DaraModel):
    def __init__(
        self,
        instance_type_families: str = None,
        request_id: str = None,
    ):
        # The instance families that support the deployment strategy.
        self.instance_type_families = instance_type_families
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_type_families is not None:
            result['InstanceTypeFamilies'] = self.instance_type_families

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceTypeFamilies') is not None:
            self.instance_type_families = m.get('InstanceTypeFamilies')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

