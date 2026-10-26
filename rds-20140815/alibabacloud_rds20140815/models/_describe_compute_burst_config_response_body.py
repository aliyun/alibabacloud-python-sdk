# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class DescribeComputeBurstConfigResponseBody(DaraModel):
    def __init__(
        self,
        compute_burst_config: Dict[str, Any] = None,
        compute_burst_enabled: bool = None,
        request_id: str = None,
    ):
        # The configuration details of the committed Serverless feature.
        self.compute_burst_config = compute_burst_config
        # Indicates whether the committed Serverless feature is enabled. Valid values:
        # - **true**: Enabled.
        # - **false**: Disabled.
        self.compute_burst_enabled = compute_burst_enabled
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.compute_burst_config is not None:
            result['ComputeBurstConfig'] = self.compute_burst_config

        if self.compute_burst_enabled is not None:
            result['ComputeBurstEnabled'] = self.compute_burst_enabled

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComputeBurstConfig') is not None:
            self.compute_burst_config = m.get('ComputeBurstConfig')

        if m.get('ComputeBurstEnabled') is not None:
            self.compute_burst_enabled = m.get('ComputeBurstEnabled')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

