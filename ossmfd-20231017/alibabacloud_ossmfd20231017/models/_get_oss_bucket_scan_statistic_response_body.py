# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ossmfd20231017 import models as main_models
from darabonba.model import DaraModel

class GetOssBucketScanStatisticResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetOssBucketScanStatisticResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetOssBucketScanStatisticResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetOssBucketScanStatisticResponseBodyData(DaraModel):
    def __init__(
        self,
        expire_time: int = None,
        high_risk: int = None,
        low_risk: int = None,
        medium_risk: int = None,
        no_scan_bucket: int = None,
        remain_auth: int = None,
        risk_bucket: int = None,
        scan_object: int = None,
        total_bucket: int = None,
        total_object: int = None,
    ):
        self.expire_time = expire_time
        self.high_risk = high_risk
        self.low_risk = low_risk
        self.medium_risk = medium_risk
        self.no_scan_bucket = no_scan_bucket
        self.remain_auth = remain_auth
        self.risk_bucket = risk_bucket
        self.scan_object = scan_object
        self.total_bucket = total_bucket
        self.total_object = total_object

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.high_risk is not None:
            result['HighRisk'] = self.high_risk

        if self.low_risk is not None:
            result['LowRisk'] = self.low_risk

        if self.medium_risk is not None:
            result['MediumRisk'] = self.medium_risk

        if self.no_scan_bucket is not None:
            result['NoScanBucket'] = self.no_scan_bucket

        if self.remain_auth is not None:
            result['RemainAuth'] = self.remain_auth

        if self.risk_bucket is not None:
            result['RiskBucket'] = self.risk_bucket

        if self.scan_object is not None:
            result['ScanObject'] = self.scan_object

        if self.total_bucket is not None:
            result['TotalBucket'] = self.total_bucket

        if self.total_object is not None:
            result['TotalObject'] = self.total_object

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('HighRisk') is not None:
            self.high_risk = m.get('HighRisk')

        if m.get('LowRisk') is not None:
            self.low_risk = m.get('LowRisk')

        if m.get('MediumRisk') is not None:
            self.medium_risk = m.get('MediumRisk')

        if m.get('NoScanBucket') is not None:
            self.no_scan_bucket = m.get('NoScanBucket')

        if m.get('RemainAuth') is not None:
            self.remain_auth = m.get('RemainAuth')

        if m.get('RiskBucket') is not None:
            self.risk_bucket = m.get('RiskBucket')

        if m.get('ScanObject') is not None:
            self.scan_object = m.get('ScanObject')

        if m.get('TotalBucket') is not None:
            self.total_bucket = m.get('TotalBucket')

        if m.get('TotalObject') is not None:
            self.total_object = m.get('TotalObject')

        return self

