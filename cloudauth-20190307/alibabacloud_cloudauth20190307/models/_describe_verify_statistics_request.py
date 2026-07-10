# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeVerifyStatisticsRequest(DaraModel):
    def __init__(
        self,
        age_gt: str = None,
        end_date: int = None,
        product_code: str = None,
        service_code: str = None,
        start_date: int = None,
    ):
        # Specifies whether the age is older than 14. Valid values:
        # - **T**: older than 14
        # - **F**: younger than 14.
        self.age_gt = age_gt
        # The end time of the query.
        # 
        # This parameter is required.
        self.end_date = end_date
        # The product code.
        self.product_code = product_code
        # The service type. Valid values:
        # - **antcloudauth**: financial-grade ID Verification.
        # - **cloudauthst** (discontinued): enhanced ID Verification.
        # - **cloudauth** (discontinued): ID Verification.
        # 
        # This parameter is required.
        self.service_code = service_code
        # The start time of the query.
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

        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        return self

