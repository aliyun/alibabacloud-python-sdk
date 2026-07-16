# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeVerifyPersonasSexStatisticsRequest(DaraModel):
    def __init__(
        self,
        product_code: str = None,
        scene_id: int = None,
        service_code: str = None,
        time_range: str = None,
    ):
        # The product code.
        self.product_code = product_code
        # The scene ID.
        self.scene_id = scene_id
        # The service type. Valid values:
        # - **antcloudauth**: financial-grade ID Verification.
        # - **cloudauthst** (discontinued): enhanced ID Verification.
        # 
        # This parameter is required.
        self.service_code = service_code
        # The time range. The search scope is the previous N days. For example, a value of 1 indicates the previous day.
        # 
        # This parameter is required.
        self.time_range = time_range

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.scene_id is not None:
            result['SceneId'] = self.scene_id

        if self.service_code is not None:
            result['ServiceCode'] = self.service_code

        if self.time_range is not None:
            result['TimeRange'] = self.time_range

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')

        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')

        if m.get('TimeRange') is not None:
            self.time_range = m.get('TimeRange')

        return self

