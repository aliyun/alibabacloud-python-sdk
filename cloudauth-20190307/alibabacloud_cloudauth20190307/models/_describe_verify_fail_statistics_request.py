# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeVerifyFailStatisticsRequest(DaraModel):
    def __init__(
        self,
        age_gt: str = None,
        api: str = None,
        device_type: str = None,
        end_date: int = None,
        product_code: str = None,
        service_code: str = None,
        start_date: int = None,
    ):
        # Age greater than 14 years old:
        # - **T**: Greater than
        # - **F**: Less than
        self.age_gt = age_gt
        # API code:
        # - **INIT_SERVICE**: Server-side initialization failure
        # - **INIT_DEVICE**: Client-side failure
        # - **VERIFY_DEVICE**: Authentication failed
        # 
        # This parameter is required.
        self.api = api
        # Device type.
        # - ios
        # - android
        # - websdk
        self.device_type = device_type
        # End time of the query.
        # 
        # This parameter is required.
        self.end_date = end_date
        # Product code.
        # 
        # This parameter is required.
        self.product_code = product_code
        # Service type:
        # - **antcloudauth**: Financial-grade real-person authentication.
        # - **cloudauthst** (discontinued): Enhanced real-person authentication.
        # - **cloudauth** (discontinued): Real-person authentication.
        # 
        # This parameter is required.
        self.service_code = service_code
        # Start time of the query.
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
        if self.age_gt is not None:
            result['AgeGt'] = self.age_gt

        if self.api is not None:
            result['Api'] = self.api

        if self.device_type is not None:
            result['DeviceType'] = self.device_type

        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.service_code is not None:
            result['ServiceCode'] = self.service_code

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgeGt') is not None:
            self.age_gt = m.get('AgeGt')

        if m.get('Api') is not None:
            self.api = m.get('Api')

        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')

        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        return self

