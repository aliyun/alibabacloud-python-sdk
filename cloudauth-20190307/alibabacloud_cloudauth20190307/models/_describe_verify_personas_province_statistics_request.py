# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeVerifyPersonasProvinceStatisticsRequest(DaraModel):
    def __init__(
        self,
        product_code: str = None,
        scene_id: int = None,
        service_code: str = None,
        time_range: str = None,
    ):
        # Cloud product code.
        self.product_code = product_code
        # Scene ID.
        self.scene_id = scene_id
        # Service type:
        # - **antcloudauth**: Financial-grade real-person authentication.
        # - **cloudauthst** (discontinued): Enhanced real-person authentication.
        # 
        # This parameter is required.
        self.service_code = service_code
        # Time range, search range is for the previous N days, TimeRange of 1 indicates the previous 1 day.
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

