# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PushResourceRuleShrinkRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        metric_info_shrink: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.metric_info_shrink = metric_info_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.metric_info_shrink is not None:
            result['MetricInfo'] = self.metric_info_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MetricInfo') is not None:
            self.metric_info_shrink = m.get('MetricInfo')

        return self

