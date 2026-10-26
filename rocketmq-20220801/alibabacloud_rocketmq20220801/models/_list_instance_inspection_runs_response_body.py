# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rocketmq20220801 import models as main_models
from darabonba.model import DaraModel

class ListInstanceInspectionRunsResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListInstanceInspectionRunsResponseBodyData] = None,
        max_results: int = None,
        next_token: str = None,
        total: int = None,
    ):
        self.data = data
        self.max_results = max_results
        self.next_token = next_token
        self.total = total

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['data'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.ListInstanceInspectionRunsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

class ListInstanceInspectionRunsResponseBodyData(DaraModel):
    def __init__(
        self,
        ai_summary: main_models.ListInstanceInspectionRunsResponseBodyDataAiSummary = None,
        finished_at: str = None,
        instance_id: str = None,
        instance_name: str = None,
        notification: main_models.ListInstanceInspectionRunsResponseBodyDataNotification = None,
        region_id: str = None,
        report_finished_at: str = None,
        report_id: str = None,
        report_status: str = None,
        requested_at: str = None,
        run_id: str = None,
        status: str = None,
        summary: main_models.ListInstanceInspectionRunsResponseBodyDataSummary = None,
        time_range: main_models.ListInstanceInspectionRunsResponseBodyDataTimeRange = None,
        trigger_source: str = None,
    ):
        # 每次巡检结果由 LLM 总结；包含生成状态及成功后的原文，未生成时为空。
        self.ai_summary = ai_summary
        self.finished_at = finished_at
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.notification = notification
        self.region_id = region_id
        self.report_finished_at = report_finished_at
        self.report_id = report_id
        self.report_status = report_status
        self.requested_at = requested_at
        self.run_id = run_id
        self.status = status
        self.summary = summary
        self.time_range = time_range
        self.trigger_source = trigger_source

    def validate(self):
        if self.ai_summary:
            self.ai_summary.validate()
        if self.notification:
            self.notification.validate()
        if self.summary:
            self.summary.validate()
        if self.time_range:
            self.time_range.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ai_summary is not None:
            result['aiSummary'] = self.ai_summary.to_map()

        if self.finished_at is not None:
            result['finishedAt'] = self.finished_at

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.instance_name is not None:
            result['instanceName'] = self.instance_name

        if self.notification is not None:
            result['notification'] = self.notification.to_map()

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.report_finished_at is not None:
            result['reportFinishedAt'] = self.report_finished_at

        if self.report_id is not None:
            result['reportId'] = self.report_id

        if self.report_status is not None:
            result['reportStatus'] = self.report_status

        if self.requested_at is not None:
            result['requestedAt'] = self.requested_at

        if self.run_id is not None:
            result['runId'] = self.run_id

        if self.status is not None:
            result['status'] = self.status

        if self.summary is not None:
            result['summary'] = self.summary.to_map()

        if self.time_range is not None:
            result['timeRange'] = self.time_range.to_map()

        if self.trigger_source is not None:
            result['triggerSource'] = self.trigger_source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aiSummary') is not None:
            temp_model = main_models.ListInstanceInspectionRunsResponseBodyDataAiSummary()
            self.ai_summary = temp_model.from_map(m.get('aiSummary'))

        if m.get('finishedAt') is not None:
            self.finished_at = m.get('finishedAt')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('instanceName') is not None:
            self.instance_name = m.get('instanceName')

        if m.get('notification') is not None:
            temp_model = main_models.ListInstanceInspectionRunsResponseBodyDataNotification()
            self.notification = temp_model.from_map(m.get('notification'))

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('reportFinishedAt') is not None:
            self.report_finished_at = m.get('reportFinishedAt')

        if m.get('reportId') is not None:
            self.report_id = m.get('reportId')

        if m.get('reportStatus') is not None:
            self.report_status = m.get('reportStatus')

        if m.get('requestedAt') is not None:
            self.requested_at = m.get('requestedAt')

        if m.get('runId') is not None:
            self.run_id = m.get('runId')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('summary') is not None:
            temp_model = main_models.ListInstanceInspectionRunsResponseBodyDataSummary()
            self.summary = temp_model.from_map(m.get('summary'))

        if m.get('timeRange') is not None:
            temp_model = main_models.ListInstanceInspectionRunsResponseBodyDataTimeRange()
            self.time_range = temp_model.from_map(m.get('timeRange'))

        if m.get('triggerSource') is not None:
            self.trigger_source = m.get('triggerSource')

        return self

class ListInstanceInspectionRunsResponseBodyDataTimeRange(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        start_time: str = None,
    ):
        self.end_time = end_time
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.start_time is not None:
            result['startTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        return self

class ListInstanceInspectionRunsResponseBodyDataSummary(DaraModel):
    def __init__(
        self,
        info_count: int = None,
        result: str = None,
        risk_count: int = None,
    ):
        self.info_count = info_count
        self.result = result
        self.risk_count = risk_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.info_count is not None:
            result['infoCount'] = self.info_count

        if self.result is not None:
            result['result'] = self.result

        if self.risk_count is not None:
            result['riskCount'] = self.risk_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('infoCount') is not None:
            self.info_count = m.get('infoCount')

        if m.get('result') is not None:
            self.result = m.get('result')

        if m.get('riskCount') is not None:
            self.risk_count = m.get('riskCount')

        return self

class ListInstanceInspectionRunsResponseBodyDataNotification(DaraModel):
    def __init__(
        self,
        event_id: str = None,
        status: str = None,
    ):
        self.event_id = event_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_id is not None:
            result['eventId'] = self.event_id

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('eventId') is not None:
            self.event_id = m.get('eventId')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

class ListInstanceInspectionRunsResponseBodyDataAiSummary(DaraModel):
    def __init__(
        self,
        status: str = None,
        text: str = None,
    ):
        # Pending 等待、Running 生成中、Succeeded 已生成、Failed 生成失败；不改变巡检结果。
        self.status = status
        # 仅生成成功时返回，最多 200 字，不由前端拼接或截取。
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.status is not None:
            result['status'] = self.status

        if self.text is not None:
            result['text'] = self.text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('text') is not None:
            self.text = m.get('text')

        return self

