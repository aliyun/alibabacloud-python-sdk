# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RenewRenderingInstanceRequest(DaraModel):
    def __init__(
        self,
        auto_renew: bool = None,
        period: str = None,
        rendering_instance_id: str = None,
    ):
        # Specifies whether to enable auto-renewal. Valid values:
        # * **true**: Enabled.
        # * **false**: Disabled.
        self.auto_renew = auto_renew
        # The subscription duration. Valid values: 1, 2, 3, 4, 5, 6, 7, 8, 9, and 12. Default value: 1. A value of 12 indicates one year, while other values indicate months.
        self.period = period
        # The cloud application service instance ID.
        # 
        # This parameter is required.
        self.rendering_instance_id = rendering_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.period is not None:
            result['Period'] = self.period

        if self.rendering_instance_id is not None:
            result['RenderingInstanceId'] = self.rendering_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('RenderingInstanceId') is not None:
            self.rendering_instance_id = m.get('RenderingInstanceId')

        return self

