# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class GetRegistryScanDayNumResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        scan_day_num_config: main_models.GetRegistryScanDayNumResponseBodyScanDayNumConfig = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The configuration of the scan period.
        self.scan_day_num_config = scan_day_num_config

    def validate(self):
        if self.scan_day_num_config:
            self.scan_day_num_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.scan_day_num_config is not None:
            result['ScanDayNumConfig'] = self.scan_day_num_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ScanDayNumConfig') is not None:
            temp_model = main_models.GetRegistryScanDayNumResponseBodyScanDayNumConfig()
            self.scan_day_num_config = temp_model.from_map(m.get('ScanDayNumConfig'))

        return self

class GetRegistryScanDayNumResponseBodyScanDayNumConfig(DaraModel):
    def __init__(
        self,
        day_num_list: str = None,
        scan_day_num: int = None,
    ):
        # The selectable day options.
        self.day_num_list = day_num_list
        # The scan period. Unit: days.
        self.scan_day_num = scan_day_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.day_num_list is not None:
            result['DayNumList'] = self.day_num_list

        if self.scan_day_num is not None:
            result['ScanDayNum'] = self.scan_day_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DayNumList') is not None:
            self.day_num_list = m.get('DayNumList')

        if m.get('ScanDayNum') is not None:
            self.scan_day_num = m.get('ScanDayNum')

        return self

