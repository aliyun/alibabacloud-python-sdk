# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentloop20260520 import models as main_models
from darabonba.model import DaraModel

class GetPipelineStatsResponseBody(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        granularity: str = None,
        pipeline_name: str = None,
        request_id: str = None,
        start_time: int = None,
        summary: main_models.GetPipelineStatsResponseBodySummary = None,
        time_series: List[main_models.GetPipelineStatsResponseBodyTimeSeries] = None,
    ):
        self.end_time = end_time
        self.granularity = granularity
        # The name of the pipeline.
        self.pipeline_name = pipeline_name
        # The request ID, which is used to locate the request during troubleshooting.
        self.request_id = request_id
        self.start_time = start_time
        self.summary = summary
        self.time_series = time_series

    def validate(self):
        if self.summary:
            self.summary.validate()
        if self.time_series:
            for v1 in self.time_series:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.granularity is not None:
            result['granularity'] = self.granularity

        if self.pipeline_name is not None:
            result['pipelineName'] = self.pipeline_name

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.summary is not None:
            result['summary'] = self.summary.to_map()

        result['timeSeries'] = []
        if self.time_series is not None:
            for k1 in self.time_series:
                result['timeSeries'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('granularity') is not None:
            self.granularity = m.get('granularity')

        if m.get('pipelineName') is not None:
            self.pipeline_name = m.get('pipelineName')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('summary') is not None:
            temp_model = main_models.GetPipelineStatsResponseBodySummary()
            self.summary = temp_model.from_map(m.get('summary'))

        self.time_series = []
        if m.get('timeSeries') is not None:
            for k1 in m.get('timeSeries'):
                temp_model = main_models.GetPipelineStatsResponseBodyTimeSeries()
                self.time_series.append(temp_model.from_map(k1))

        return self

class GetPipelineStatsResponseBodyTimeSeries(DaraModel):
    def __init__(
        self,
        avg_elapsed_ms: int = None,
        output_bytes: int = None,
        output_rows: int = None,
        processed_bytes: int = None,
        processed_rows: int = None,
        runs: int = None,
        succeeded_runs: int = None,
        timestamp: int = None,
    ):
        self.avg_elapsed_ms = avg_elapsed_ms
        self.output_bytes = output_bytes
        self.output_rows = output_rows
        self.processed_bytes = processed_bytes
        self.processed_rows = processed_rows
        self.runs = runs
        self.succeeded_runs = succeeded_runs
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.avg_elapsed_ms is not None:
            result['avgElapsedMs'] = self.avg_elapsed_ms

        if self.output_bytes is not None:
            result['outputBytes'] = self.output_bytes

        if self.output_rows is not None:
            result['outputRows'] = self.output_rows

        if self.processed_bytes is not None:
            result['processedBytes'] = self.processed_bytes

        if self.processed_rows is not None:
            result['processedRows'] = self.processed_rows

        if self.runs is not None:
            result['runs'] = self.runs

        if self.succeeded_runs is not None:
            result['succeededRuns'] = self.succeeded_runs

        if self.timestamp is not None:
            result['timestamp'] = self.timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('avgElapsedMs') is not None:
            self.avg_elapsed_ms = m.get('avgElapsedMs')

        if m.get('outputBytes') is not None:
            self.output_bytes = m.get('outputBytes')

        if m.get('outputRows') is not None:
            self.output_rows = m.get('outputRows')

        if m.get('processedBytes') is not None:
            self.processed_bytes = m.get('processedBytes')

        if m.get('processedRows') is not None:
            self.processed_rows = m.get('processedRows')

        if m.get('runs') is not None:
            self.runs = m.get('runs')

        if m.get('succeededRuns') is not None:
            self.succeeded_runs = m.get('succeededRuns')

        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')

        return self

class GetPipelineStatsResponseBodySummary(DaraModel):
    def __init__(
        self,
        avg_elapsed_ms: int = None,
        cancelled_runs: int = None,
        committed_watermark: int = None,
        failed_runs: int = None,
        schedule_lag_seconds: int = None,
        succeeded_runs: int = None,
        success_rate: float = None,
        total_output_bytes: int = None,
        total_output_rows: int = None,
        total_processed_bytes: int = None,
        total_processed_rows: int = None,
        total_runs: int = None,
    ):
        self.avg_elapsed_ms = avg_elapsed_ms
        self.cancelled_runs = cancelled_runs
        self.committed_watermark = committed_watermark
        self.failed_runs = failed_runs
        self.schedule_lag_seconds = schedule_lag_seconds
        self.succeeded_runs = succeeded_runs
        self.success_rate = success_rate
        self.total_output_bytes = total_output_bytes
        self.total_output_rows = total_output_rows
        self.total_processed_bytes = total_processed_bytes
        self.total_processed_rows = total_processed_rows
        self.total_runs = total_runs

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.avg_elapsed_ms is not None:
            result['avgElapsedMs'] = self.avg_elapsed_ms

        if self.cancelled_runs is not None:
            result['cancelledRuns'] = self.cancelled_runs

        if self.committed_watermark is not None:
            result['committedWatermark'] = self.committed_watermark

        if self.failed_runs is not None:
            result['failedRuns'] = self.failed_runs

        if self.schedule_lag_seconds is not None:
            result['scheduleLagSeconds'] = self.schedule_lag_seconds

        if self.succeeded_runs is not None:
            result['succeededRuns'] = self.succeeded_runs

        if self.success_rate is not None:
            result['successRate'] = self.success_rate

        if self.total_output_bytes is not None:
            result['totalOutputBytes'] = self.total_output_bytes

        if self.total_output_rows is not None:
            result['totalOutputRows'] = self.total_output_rows

        if self.total_processed_bytes is not None:
            result['totalProcessedBytes'] = self.total_processed_bytes

        if self.total_processed_rows is not None:
            result['totalProcessedRows'] = self.total_processed_rows

        if self.total_runs is not None:
            result['totalRuns'] = self.total_runs

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('avgElapsedMs') is not None:
            self.avg_elapsed_ms = m.get('avgElapsedMs')

        if m.get('cancelledRuns') is not None:
            self.cancelled_runs = m.get('cancelledRuns')

        if m.get('committedWatermark') is not None:
            self.committed_watermark = m.get('committedWatermark')

        if m.get('failedRuns') is not None:
            self.failed_runs = m.get('failedRuns')

        if m.get('scheduleLagSeconds') is not None:
            self.schedule_lag_seconds = m.get('scheduleLagSeconds')

        if m.get('succeededRuns') is not None:
            self.succeeded_runs = m.get('succeededRuns')

        if m.get('successRate') is not None:
            self.success_rate = m.get('successRate')

        if m.get('totalOutputBytes') is not None:
            self.total_output_bytes = m.get('totalOutputBytes')

        if m.get('totalOutputRows') is not None:
            self.total_output_rows = m.get('totalOutputRows')

        if m.get('totalProcessedBytes') is not None:
            self.total_processed_bytes = m.get('totalProcessedBytes')

        if m.get('totalProcessedRows') is not None:
            self.total_processed_rows = m.get('totalProcessedRows')

        if m.get('totalRuns') is not None:
            self.total_runs = m.get('totalRuns')

        return self

