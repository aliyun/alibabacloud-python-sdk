# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class PreloadSparkAppMetricsResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.PreloadSparkAppMetricsResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # The request ID.
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
            temp_model = main_models.PreloadSparkAppMetricsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class PreloadSparkAppMetricsResponseBodyData(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        attempt_id: str = None,
        event_log_path: str = None,
        finished: bool = None,
        scan_metrics: main_models.PreloadSparkAppMetricsResponseBodyDataScanMetrics = None,
    ):
        # The ID of the Spark application.
        self.app_id = app_id
        # The retry ID of the Spark application.
        self.attempt_id = attempt_id
        # The event log path.
        self.event_log_path = event_log_path
        # Indicates whether parsing is complete. Valid values:
        # 
        # *   true
        # *   false
        self.finished = finished
        # The metrics.
        self.scan_metrics = scan_metrics

    def validate(self):
        if self.scan_metrics:
            self.scan_metrics.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.attempt_id is not None:
            result['AttemptId'] = self.attempt_id

        if self.event_log_path is not None:
            result['EventLogPath'] = self.event_log_path

        if self.finished is not None:
            result['Finished'] = self.finished

        if self.scan_metrics is not None:
            result['ScanMetrics'] = self.scan_metrics.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AttemptId') is not None:
            self.attempt_id = m.get('AttemptId')

        if m.get('EventLogPath') is not None:
            self.event_log_path = m.get('EventLogPath')

        if m.get('Finished') is not None:
            self.finished = m.get('Finished')

        if m.get('ScanMetrics') is not None:
            temp_model = main_models.PreloadSparkAppMetricsResponseBodyDataScanMetrics()
            self.scan_metrics = temp_model.from_map(m.get('ScanMetrics'))

        return self

class PreloadSparkAppMetricsResponseBodyDataScanMetrics(DaraModel):
    def __init__(
        self,
        output_rows_count: int = None,
        total_read_file_size_in_byte: int = None,
    ):
        # The number of rows scanned.
        self.output_rows_count = output_rows_count
        # The size of the scanned data. Unit: bytes.
        self.total_read_file_size_in_byte = total_read_file_size_in_byte

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.output_rows_count is not None:
            result['OutputRowsCount'] = self.output_rows_count

        if self.total_read_file_size_in_byte is not None:
            result['TotalReadFileSizeInByte'] = self.total_read_file_size_in_byte

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OutputRowsCount') is not None:
            self.output_rows_count = m.get('OutputRowsCount')

        if m.get('TotalReadFileSizeInByte') is not None:
            self.total_read_file_size_in_byte = m.get('TotalReadFileSizeInByte')

        return self

