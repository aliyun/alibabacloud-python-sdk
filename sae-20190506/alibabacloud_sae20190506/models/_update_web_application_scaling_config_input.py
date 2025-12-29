# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateWebApplicationScalingConfigInput(DaraModel):
    def __init__(
        self,
        maximum_instance_count: int = None,
        minimum_instance_count: int = None,
    ):
        # This parameter is required.
        self.maximum_instance_count = maximum_instance_count
        # This parameter is required.
        self.minimum_instance_count = minimum_instance_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.maximum_instance_count is not None:
            result['MaximumInstanceCount'] = self.maximum_instance_count

        if self.minimum_instance_count is not None:
            result['MinimumInstanceCount'] = self.minimum_instance_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaximumInstanceCount') is not None:
            self.maximum_instance_count = m.get('MaximumInstanceCount')

        if m.get('MinimumInstanceCount') is not None:
            self.minimum_instance_count = m.get('MinimumInstanceCount')

        return self

