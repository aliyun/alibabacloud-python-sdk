# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeVerifyDeviceRiskStatisticsRequest(DaraModel):
    def __init__(
        self,
        end_date: int = None,
        product_code: str = None,
        scene_id: str = None,
        service_code: str = None,
        start_date: int = None,
    ):
        # The end time.
        # 
        # This parameter is required.
        self.end_date = end_date
        # The code of the cloud service.
        self.product_code = product_code
        # The scene ID.
        self.scene_id = scene_id
        # The service type. Valid values:
        # - **antcloudauth**: financial-grade ID Verification.
        # - **cloudauthst** (discontinued): ID Verification - Enhanced Edition.
        # - **cloudauth** (discontinued): ID Verification.
        # 
        # This parameter is required.
        self.service_code = service_code
        # The start time of the query. The value is a UNIX timestamp in milliseconds.
        # 
        # This parameter is required.
        self.start_date = start_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.scene_id is not None:
            result['SceneId'] = self.scene_id

        if self.service_code is not None:
            result['ServiceCode'] = self.service_code

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')

        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        return self

