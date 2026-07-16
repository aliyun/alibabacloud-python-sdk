# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetImageBuildRiskStatusRequest(DaraModel):
    def __init__(
        self,
        image_uuids: str = None,
        risk_key: str = None,
        status: int = None,
    ):
        # The image UUIDs. Separate multiple UUIDs with commas (,).
        # >Call the [DescribeImageInstances](~~DescribeImageInstances~~) operation to obtain this parameter.
        self.image_uuids = image_uuids
        # The risk keyword.
        self.risk_key = risk_key
        # The status. Valid values:
        # - **0**: Unhandled.
        # - **1**: Ignored.
        # - **2**: False positive.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_uuids is not None:
            result['ImageUuids'] = self.image_uuids

        if self.risk_key is not None:
            result['RiskKey'] = self.risk_key

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageUuids') is not None:
            self.image_uuids = m.get('ImageUuids')

        if m.get('RiskKey') is not None:
            self.risk_key = m.get('RiskKey')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

