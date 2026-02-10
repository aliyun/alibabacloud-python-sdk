# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class GetDockerhubImageRiskStatisticResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        risk_rank_info: main_models.GetDockerhubImageRiskStatisticResponseBodyRiskRankInfo = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The information about the risk source.
        self.risk_rank_info = risk_rank_info

    def validate(self):
        if self.risk_rank_info:
            self.risk_rank_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.risk_rank_info is not None:
            result['RiskRankInfo'] = self.risk_rank_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RiskRankInfo') is not None:
            temp_model = main_models.GetDockerhubImageRiskStatisticResponseBodyRiskRankInfo()
            self.risk_rank_info = temp_model.from_map(m.get('RiskRankInfo'))

        return self

class GetDockerhubImageRiskStatisticResponseBodyRiskRankInfo(DaraModel):
    def __init__(
        self,
        baseline: int = None,
        scan_time: int = None,
        scan_time_timestamp: int = None,
        total_scanned: int = None,
        vul_asap: int = None,
    ):
        # The number of baseline risks.
        self.baseline = baseline
        # The timestamp when the scan was performed.
        self.scan_time = scan_time
        # The timestamp when the scan was performed.
        self.scan_time_timestamp = scan_time_timestamp
        # The number of scanned Docker Hub images.
        self.total_scanned = total_scanned
        # The number of high-risk vulnerabilities.
        self.vul_asap = vul_asap

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.baseline is not None:
            result['Baseline'] = self.baseline

        if self.scan_time is not None:
            result['ScanTime'] = self.scan_time

        if self.scan_time_timestamp is not None:
            result['ScanTimeTimestamp'] = self.scan_time_timestamp

        if self.total_scanned is not None:
            result['TotalScanned'] = self.total_scanned

        if self.vul_asap is not None:
            result['VulAsap'] = self.vul_asap

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Baseline') is not None:
            self.baseline = m.get('Baseline')

        if m.get('ScanTime') is not None:
            self.scan_time = m.get('ScanTime')

        if m.get('ScanTimeTimestamp') is not None:
            self.scan_time_timestamp = m.get('ScanTimeTimestamp')

        if m.get('TotalScanned') is not None:
            self.total_scanned = m.get('TotalScanned')

        if m.get('VulAsap') is not None:
            self.vul_asap = m.get('VulAsap')

        return self

