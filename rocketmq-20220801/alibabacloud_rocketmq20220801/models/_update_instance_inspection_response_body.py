# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_rocketmq20220801 import models as main_models
from darabonba.model import DaraModel

class UpdateInstanceInspectionResponseBody(DaraModel):
    def __init__(
        self,
        config: main_models.UpdateInstanceInspectionResponseBodyConfig = None,
        configured: bool = None,
        instance_id: str = None,
        items: List[main_models.UpdateInstanceInspectionResponseBodyItems] = None,
        last_run: main_models.UpdateInstanceInspectionResponseBodyLastRun = None,
        next_run_at: str = None,
        region_id: str = None,
        revision: int = None,
    ):
        self.config = config
        self.configured = configured
        self.instance_id = instance_id
        self.items = items
        self.last_run = last_run
        self.next_run_at = next_run_at
        self.region_id = region_id
        self.revision = revision

    def validate(self):
        if self.config:
            self.config.validate()
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()
        if self.last_run:
            self.last_run.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['config'] = self.config.to_map()

        if self.configured is not None:
            result['configured'] = self.configured

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        if self.last_run is not None:
            result['lastRun'] = self.last_run.to_map()

        if self.next_run_at is not None:
            result['nextRunAt'] = self.next_run_at

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.revision is not None:
            result['revision'] = self.revision

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('config') is not None:
            temp_model = main_models.UpdateInstanceInspectionResponseBodyConfig()
            self.config = temp_model.from_map(m.get('config'))

        if m.get('configured') is not None:
            self.configured = m.get('configured')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.UpdateInstanceInspectionResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('lastRun') is not None:
            temp_model = main_models.UpdateInstanceInspectionResponseBodyLastRun()
            self.last_run = temp_model.from_map(m.get('lastRun'))

        if m.get('nextRunAt') is not None:
            self.next_run_at = m.get('nextRunAt')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('revision') is not None:
            self.revision = m.get('revision')

        return self

class UpdateInstanceInspectionResponseBodyLastRun(DaraModel):
    def __init__(
        self,
        ai_summary: main_models.UpdateInstanceInspectionResponseBodyLastRunAiSummary = None,
        config_snapshot: main_models.UpdateInstanceInspectionResponseBodyLastRunConfigSnapshot = None,
        finished_at: str = None,
        instance_id: str = None,
        instance_name: str = None,
        items: List[main_models.UpdateInstanceInspectionResponseBodyLastRunItems] = None,
        notification: main_models.UpdateInstanceInspectionResponseBodyLastRunNotification = None,
        region_id: str = None,
        report: main_models.UpdateInstanceInspectionResponseBodyLastRunReport = None,
        requested_at: str = None,
        run_id: str = None,
        status: str = None,
        summary: main_models.UpdateInstanceInspectionResponseBodyLastRunSummary = None,
        time_range: main_models.UpdateInstanceInspectionResponseBodyLastRunTimeRange = None,
        trigger_source: str = None,
    ):
        # 每次巡检结果由 LLM 总结；包含生成状态及成功后的原文，未生成时为空。
        self.ai_summary = ai_summary
        self.config_snapshot = config_snapshot
        self.finished_at = finished_at
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.items = items
        self.notification = notification
        self.region_id = region_id
        self.report = report
        self.requested_at = requested_at
        self.run_id = run_id
        self.status = status
        self.summary = summary
        self.time_range = time_range
        self.trigger_source = trigger_source

    def validate(self):
        if self.ai_summary:
            self.ai_summary.validate()
        if self.config_snapshot:
            self.config_snapshot.validate()
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()
        if self.notification:
            self.notification.validate()
        if self.report:
            self.report.validate()
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

        if self.config_snapshot is not None:
            result['configSnapshot'] = self.config_snapshot.to_map()

        if self.finished_at is not None:
            result['finishedAt'] = self.finished_at

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.instance_name is not None:
            result['instanceName'] = self.instance_name

        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        if self.notification is not None:
            result['notification'] = self.notification.to_map()

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.report is not None:
            result['report'] = self.report.to_map()

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
            temp_model = main_models.UpdateInstanceInspectionResponseBodyLastRunAiSummary()
            self.ai_summary = temp_model.from_map(m.get('aiSummary'))

        if m.get('configSnapshot') is not None:
            temp_model = main_models.UpdateInstanceInspectionResponseBodyLastRunConfigSnapshot()
            self.config_snapshot = temp_model.from_map(m.get('configSnapshot'))

        if m.get('finishedAt') is not None:
            self.finished_at = m.get('finishedAt')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('instanceName') is not None:
            self.instance_name = m.get('instanceName')

        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.UpdateInstanceInspectionResponseBodyLastRunItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('notification') is not None:
            temp_model = main_models.UpdateInstanceInspectionResponseBodyLastRunNotification()
            self.notification = temp_model.from_map(m.get('notification'))

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('report') is not None:
            temp_model = main_models.UpdateInstanceInspectionResponseBodyLastRunReport()
            self.report = temp_model.from_map(m.get('report'))

        if m.get('requestedAt') is not None:
            self.requested_at = m.get('requestedAt')

        if m.get('runId') is not None:
            self.run_id = m.get('runId')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('summary') is not None:
            temp_model = main_models.UpdateInstanceInspectionResponseBodyLastRunSummary()
            self.summary = temp_model.from_map(m.get('summary'))

        if m.get('timeRange') is not None:
            temp_model = main_models.UpdateInstanceInspectionResponseBodyLastRunTimeRange()
            self.time_range = temp_model.from_map(m.get('timeRange'))

        if m.get('triggerSource') is not None:
            self.trigger_source = m.get('triggerSource')

        return self

class UpdateInstanceInspectionResponseBodyLastRunTimeRange(DaraModel):
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

class UpdateInstanceInspectionResponseBodyLastRunSummary(DaraModel):
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

class UpdateInstanceInspectionResponseBodyLastRunReport(DaraModel):
    def __init__(
        self,
        completion: str = None,
        coverage: List[main_models.UpdateInstanceInspectionResponseBodyLastRunReportCoverage] = None,
        findings: List[main_models.UpdateInstanceInspectionResponseBodyLastRunReportFindings] = None,
        finished_at: str = None,
        html: str = None,
        inspection_run_id: str = None,
        instance_id: str = None,
        instance_name: str = None,
        markdown: str = None,
        overview: str = None,
        region_id: str = None,
        report_id: str = None,
        report_summary: main_models.UpdateInstanceInspectionResponseBodyLastRunReportReportSummary = None,
        template_version: str = None,
        time_range: main_models.UpdateInstanceInspectionResponseBodyLastRunReportTimeRange = None,
    ):
        self.completion = completion
        self.coverage = coverage
        self.findings = findings
        self.finished_at = finished_at
        self.html = html
        self.inspection_run_id = inspection_run_id
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.markdown = markdown
        self.overview = overview
        self.region_id = region_id
        self.report_id = report_id
        self.report_summary = report_summary
        self.template_version = template_version
        self.time_range = time_range

    def validate(self):
        if self.coverage:
            for v1 in self.coverage:
                 if v1:
                    v1.validate()
        if self.findings:
            for v1 in self.findings:
                 if v1:
                    v1.validate()
        if self.report_summary:
            self.report_summary.validate()
        if self.time_range:
            self.time_range.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.completion is not None:
            result['completion'] = self.completion

        result['coverage'] = []
        if self.coverage is not None:
            for k1 in self.coverage:
                result['coverage'].append(k1.to_map() if k1 else None)

        result['findings'] = []
        if self.findings is not None:
            for k1 in self.findings:
                result['findings'].append(k1.to_map() if k1 else None)

        if self.finished_at is not None:
            result['finishedAt'] = self.finished_at

        if self.html is not None:
            result['html'] = self.html

        if self.inspection_run_id is not None:
            result['inspectionRunId'] = self.inspection_run_id

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.instance_name is not None:
            result['instanceName'] = self.instance_name

        if self.markdown is not None:
            result['markdown'] = self.markdown

        if self.overview is not None:
            result['overview'] = self.overview

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.report_id is not None:
            result['reportId'] = self.report_id

        if self.report_summary is not None:
            result['reportSummary'] = self.report_summary.to_map()

        if self.template_version is not None:
            result['templateVersion'] = self.template_version

        if self.time_range is not None:
            result['timeRange'] = self.time_range.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('completion') is not None:
            self.completion = m.get('completion')

        self.coverage = []
        if m.get('coverage') is not None:
            for k1 in m.get('coverage'):
                temp_model = main_models.UpdateInstanceInspectionResponseBodyLastRunReportCoverage()
                self.coverage.append(temp_model.from_map(k1))

        self.findings = []
        if m.get('findings') is not None:
            for k1 in m.get('findings'):
                temp_model = main_models.UpdateInstanceInspectionResponseBodyLastRunReportFindings()
                self.findings.append(temp_model.from_map(k1))

        if m.get('finishedAt') is not None:
            self.finished_at = m.get('finishedAt')

        if m.get('html') is not None:
            self.html = m.get('html')

        if m.get('inspectionRunId') is not None:
            self.inspection_run_id = m.get('inspectionRunId')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('instanceName') is not None:
            self.instance_name = m.get('instanceName')

        if m.get('markdown') is not None:
            self.markdown = m.get('markdown')

        if m.get('overview') is not None:
            self.overview = m.get('overview')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('reportId') is not None:
            self.report_id = m.get('reportId')

        if m.get('reportSummary') is not None:
            temp_model = main_models.UpdateInstanceInspectionResponseBodyLastRunReportReportSummary()
            self.report_summary = temp_model.from_map(m.get('reportSummary'))

        if m.get('templateVersion') is not None:
            self.template_version = m.get('templateVersion')

        if m.get('timeRange') is not None:
            temp_model = main_models.UpdateInstanceInspectionResponseBodyLastRunReportTimeRange()
            self.time_range = temp_model.from_map(m.get('timeRange'))

        return self

class UpdateInstanceInspectionResponseBodyLastRunReportTimeRange(DaraModel):
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

class UpdateInstanceInspectionResponseBodyLastRunReportReportSummary(DaraModel):
    def __init__(
        self,
        info_count: int = None,
        risk_count: int = None,
    ):
        self.info_count = info_count
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

        if self.risk_count is not None:
            result['riskCount'] = self.risk_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('infoCount') is not None:
            self.info_count = m.get('infoCount')

        if m.get('riskCount') is not None:
            self.risk_count = m.get('riskCount')

        return self

class UpdateInstanceInspectionResponseBodyLastRunReportFindings(DaraModel):
    def __init__(
        self,
        alternatives: List[str] = None,
        boundary: str = None,
        cause: str = None,
        confidence: str = None,
        evidence: List[str] = None,
        impact: str = None,
        location: str = None,
        missing_evidence: List[str] = None,
        observations: List[str] = None,
        observed_at: str = None,
        recommendations: List[str] = None,
        resource: main_models.UpdateInstanceInspectionResponseBodyLastRunReportFindingsResource = None,
        risk_type: str = None,
        source: str = None,
        template_code: str = None,
        time_range: main_models.UpdateInstanceInspectionResponseBodyLastRunReportFindingsTimeRange = None,
        verification: List[str] = None,
    ):
        self.alternatives = alternatives
        self.boundary = boundary
        self.cause = cause
        self.confidence = confidence
        self.evidence = evidence
        self.impact = impact
        self.location = location
        self.missing_evidence = missing_evidence
        self.observations = observations
        self.observed_at = observed_at
        self.recommendations = recommendations
        self.resource = resource
        self.risk_type = risk_type
        self.source = source
        self.template_code = template_code
        self.time_range = time_range
        self.verification = verification

    def validate(self):
        if self.resource:
            self.resource.validate()
        if self.time_range:
            self.time_range.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alternatives is not None:
            result['alternatives'] = self.alternatives

        if self.boundary is not None:
            result['boundary'] = self.boundary

        if self.cause is not None:
            result['cause'] = self.cause

        if self.confidence is not None:
            result['confidence'] = self.confidence

        if self.evidence is not None:
            result['evidence'] = self.evidence

        if self.impact is not None:
            result['impact'] = self.impact

        if self.location is not None:
            result['location'] = self.location

        if self.missing_evidence is not None:
            result['missingEvidence'] = self.missing_evidence

        if self.observations is not None:
            result['observations'] = self.observations

        if self.observed_at is not None:
            result['observedAt'] = self.observed_at

        if self.recommendations is not None:
            result['recommendations'] = self.recommendations

        if self.resource is not None:
            result['resource'] = self.resource.to_map()

        if self.risk_type is not None:
            result['riskType'] = self.risk_type

        if self.source is not None:
            result['source'] = self.source

        if self.template_code is not None:
            result['templateCode'] = self.template_code

        if self.time_range is not None:
            result['timeRange'] = self.time_range.to_map()

        if self.verification is not None:
            result['verification'] = self.verification

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alternatives') is not None:
            self.alternatives = m.get('alternatives')

        if m.get('boundary') is not None:
            self.boundary = m.get('boundary')

        if m.get('cause') is not None:
            self.cause = m.get('cause')

        if m.get('confidence') is not None:
            self.confidence = m.get('confidence')

        if m.get('evidence') is not None:
            self.evidence = m.get('evidence')

        if m.get('impact') is not None:
            self.impact = m.get('impact')

        if m.get('location') is not None:
            self.location = m.get('location')

        if m.get('missingEvidence') is not None:
            self.missing_evidence = m.get('missingEvidence')

        if m.get('observations') is not None:
            self.observations = m.get('observations')

        if m.get('observedAt') is not None:
            self.observed_at = m.get('observedAt')

        if m.get('recommendations') is not None:
            self.recommendations = m.get('recommendations')

        if m.get('resource') is not None:
            temp_model = main_models.UpdateInstanceInspectionResponseBodyLastRunReportFindingsResource()
            self.resource = temp_model.from_map(m.get('resource'))

        if m.get('riskType') is not None:
            self.risk_type = m.get('riskType')

        if m.get('source') is not None:
            self.source = m.get('source')

        if m.get('templateCode') is not None:
            self.template_code = m.get('templateCode')

        if m.get('timeRange') is not None:
            temp_model = main_models.UpdateInstanceInspectionResponseBodyLastRunReportFindingsTimeRange()
            self.time_range = temp_model.from_map(m.get('timeRange'))

        if m.get('verification') is not None:
            self.verification = m.get('verification')

        return self

class UpdateInstanceInspectionResponseBodyLastRunReportFindingsTimeRange(DaraModel):
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

class UpdateInstanceInspectionResponseBodyLastRunReportFindingsResource(DaraModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        type: str = None,
    ):
        self.id = id
        self.name = name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['id'] = self.id

        if self.name is not None:
            result['name'] = self.name

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class UpdateInstanceInspectionResponseBodyLastRunReportCoverage(DaraModel):
    def __init__(
        self,
        diagnosis_status: str = None,
        name: str = None,
        observed_at: str = None,
        result: str = None,
        status: str = None,
        template_code: str = None,
        time_range: main_models.UpdateInstanceInspectionResponseBodyLastRunReportCoverageTimeRange = None,
    ):
        self.diagnosis_status = diagnosis_status
        self.name = name
        self.observed_at = observed_at
        self.result = result
        self.status = status
        self.template_code = template_code
        self.time_range = time_range

    def validate(self):
        if self.time_range:
            self.time_range.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.diagnosis_status is not None:
            result['diagnosisStatus'] = self.diagnosis_status

        if self.name is not None:
            result['name'] = self.name

        if self.observed_at is not None:
            result['observedAt'] = self.observed_at

        if self.result is not None:
            result['result'] = self.result

        if self.status is not None:
            result['status'] = self.status

        if self.template_code is not None:
            result['templateCode'] = self.template_code

        if self.time_range is not None:
            result['timeRange'] = self.time_range.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('diagnosisStatus') is not None:
            self.diagnosis_status = m.get('diagnosisStatus')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('observedAt') is not None:
            self.observed_at = m.get('observedAt')

        if m.get('result') is not None:
            self.result = m.get('result')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('templateCode') is not None:
            self.template_code = m.get('templateCode')

        if m.get('timeRange') is not None:
            temp_model = main_models.UpdateInstanceInspectionResponseBodyLastRunReportCoverageTimeRange()
            self.time_range = temp_model.from_map(m.get('timeRange'))

        return self

class UpdateInstanceInspectionResponseBodyLastRunReportCoverageTimeRange(DaraModel):
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

class UpdateInstanceInspectionResponseBodyLastRunNotification(DaraModel):
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

class UpdateInstanceInspectionResponseBodyLastRunItems(DaraModel):
    def __init__(
        self,
        description: str = None,
        effective_config: main_models.UpdateInstanceInspectionResponseBodyLastRunItemsEffectiveConfig = None,
        error_code: str = None,
        headline: str = None,
        metrics: List[main_models.UpdateInstanceInspectionResponseBodyLastRunItemsMetrics] = None,
        name: str = None,
        observed_at: str = None,
        resource_count: int = None,
        resource_summary: main_models.UpdateInstanceInspectionResponseBodyLastRunItemsResourceSummary = None,
        resource_types: List[str] = None,
        result: str = None,
        severity: str = None,
        status: str = None,
        template_code: str = None,
        time_range: main_models.UpdateInstanceInspectionResponseBodyLastRunItemsTimeRange = None,
    ):
        self.description = description
        self.effective_config = effective_config
        self.error_code = error_code
        self.headline = headline
        self.metrics = metrics
        self.name = name
        self.observed_at = observed_at
        self.resource_count = resource_count
        self.resource_summary = resource_summary
        self.resource_types = resource_types
        self.result = result
        self.severity = severity
        self.status = status
        self.template_code = template_code
        self.time_range = time_range

    def validate(self):
        if self.effective_config:
            self.effective_config.validate()
        if self.metrics:
            for v1 in self.metrics:
                 if v1:
                    v1.validate()
        if self.resource_summary:
            self.resource_summary.validate()
        if self.time_range:
            self.time_range.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.effective_config is not None:
            result['effectiveConfig'] = self.effective_config.to_map()

        if self.error_code is not None:
            result['errorCode'] = self.error_code

        if self.headline is not None:
            result['headline'] = self.headline

        result['metrics'] = []
        if self.metrics is not None:
            for k1 in self.metrics:
                result['metrics'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['name'] = self.name

        if self.observed_at is not None:
            result['observedAt'] = self.observed_at

        if self.resource_count is not None:
            result['resourceCount'] = self.resource_count

        if self.resource_summary is not None:
            result['resourceSummary'] = self.resource_summary.to_map()

        if self.resource_types is not None:
            result['resourceTypes'] = self.resource_types

        if self.result is not None:
            result['result'] = self.result

        if self.severity is not None:
            result['severity'] = self.severity

        if self.status is not None:
            result['status'] = self.status

        if self.template_code is not None:
            result['templateCode'] = self.template_code

        if self.time_range is not None:
            result['timeRange'] = self.time_range.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('effectiveConfig') is not None:
            temp_model = main_models.UpdateInstanceInspectionResponseBodyLastRunItemsEffectiveConfig()
            self.effective_config = temp_model.from_map(m.get('effectiveConfig'))

        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')

        if m.get('headline') is not None:
            self.headline = m.get('headline')

        self.metrics = []
        if m.get('metrics') is not None:
            for k1 in m.get('metrics'):
                temp_model = main_models.UpdateInstanceInspectionResponseBodyLastRunItemsMetrics()
                self.metrics.append(temp_model.from_map(k1))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('observedAt') is not None:
            self.observed_at = m.get('observedAt')

        if m.get('resourceCount') is not None:
            self.resource_count = m.get('resourceCount')

        if m.get('resourceSummary') is not None:
            temp_model = main_models.UpdateInstanceInspectionResponseBodyLastRunItemsResourceSummary()
            self.resource_summary = temp_model.from_map(m.get('resourceSummary'))

        if m.get('resourceTypes') is not None:
            self.resource_types = m.get('resourceTypes')

        if m.get('result') is not None:
            self.result = m.get('result')

        if m.get('severity') is not None:
            self.severity = m.get('severity')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('templateCode') is not None:
            self.template_code = m.get('templateCode')

        if m.get('timeRange') is not None:
            temp_model = main_models.UpdateInstanceInspectionResponseBodyLastRunItemsTimeRange()
            self.time_range = temp_model.from_map(m.get('timeRange'))

        return self

class UpdateInstanceInspectionResponseBodyLastRunItemsTimeRange(DaraModel):
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

class UpdateInstanceInspectionResponseBodyLastRunItemsResourceSummary(DaraModel):
    def __init__(
        self,
        info_count: int = None,
        risk_count: int = None,
    ):
        self.info_count = info_count
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

        if self.risk_count is not None:
            result['riskCount'] = self.risk_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('infoCount') is not None:
            self.info_count = m.get('infoCount')

        if m.get('riskCount') is not None:
            self.risk_count = m.get('riskCount')

        return self

class UpdateInstanceInspectionResponseBodyLastRunItemsMetrics(DaraModel):
    def __init__(
        self,
        bad: bool = None,
        good: bool = None,
        k: str = None,
        v: str = None,
    ):
        self.bad = bad
        self.good = good
        self.k = k
        self.v = v

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bad is not None:
            result['bad'] = self.bad

        if self.good is not None:
            result['good'] = self.good

        if self.k is not None:
            result['k'] = self.k

        if self.v is not None:
            result['v'] = self.v

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bad') is not None:
            self.bad = m.get('bad')

        if m.get('good') is not None:
            self.good = m.get('good')

        if m.get('k') is not None:
            self.k = m.get('k')

        if m.get('v') is not None:
            self.v = m.get('v')

        return self

class UpdateInstanceInspectionResponseBodyLastRunItemsEffectiveConfig(DaraModel):
    def __init__(
        self,
        parameters: Any = None,
        template_code: str = None,
    ):
        self.parameters = parameters
        self.template_code = template_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.parameters is not None:
            result['parameters'] = self.parameters

        if self.template_code is not None:
            result['templateCode'] = self.template_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('parameters') is not None:
            self.parameters = m.get('parameters')

        if m.get('templateCode') is not None:
            self.template_code = m.get('templateCode')

        return self

class UpdateInstanceInspectionResponseBodyLastRunConfigSnapshot(DaraModel):
    def __init__(
        self,
        items: List[main_models.UpdateInstanceInspectionResponseBodyLastRunConfigSnapshotItems] = None,
        resource_scope: main_models.UpdateInstanceInspectionResponseBodyLastRunConfigSnapshotResourceScope = None,
        schedule: main_models.UpdateInstanceInspectionResponseBodyLastRunConfigSnapshotSchedule = None,
    ):
        # This parameter is required.
        self.items = items
        # This parameter is required.
        self.resource_scope = resource_scope
        # This parameter is required.
        self.schedule = schedule

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()
        if self.resource_scope:
            self.resource_scope.validate()
        if self.schedule:
            self.schedule.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        if self.resource_scope is not None:
            result['resourceScope'] = self.resource_scope.to_map()

        if self.schedule is not None:
            result['schedule'] = self.schedule.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.UpdateInstanceInspectionResponseBodyLastRunConfigSnapshotItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('resourceScope') is not None:
            temp_model = main_models.UpdateInstanceInspectionResponseBodyLastRunConfigSnapshotResourceScope()
            self.resource_scope = temp_model.from_map(m.get('resourceScope'))

        if m.get('schedule') is not None:
            temp_model = main_models.UpdateInstanceInspectionResponseBodyLastRunConfigSnapshotSchedule()
            self.schedule = temp_model.from_map(m.get('schedule'))

        return self

class UpdateInstanceInspectionResponseBodyLastRunConfigSnapshotSchedule(DaraModel):
    def __init__(
        self,
        cron: str = None,
        enabled: bool = None,
    ):
        self.cron = cron
        # This parameter is required.
        self.enabled = enabled

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cron is not None:
            result['cron'] = self.cron

        if self.enabled is not None:
            result['enabled'] = self.enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cron') is not None:
            self.cron = m.get('cron')

        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        return self

class UpdateInstanceInspectionResponseBodyLastRunConfigSnapshotResourceScope(DaraModel):
    def __init__(
        self,
        consumer_groups: List[str] = None,
        mode: str = None,
        topics: List[str] = None,
    ):
        self.consumer_groups = consumer_groups
        # This parameter is required.
        self.mode = mode
        self.topics = topics

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.consumer_groups is not None:
            result['consumerGroups'] = self.consumer_groups

        if self.mode is not None:
            result['mode'] = self.mode

        if self.topics is not None:
            result['topics'] = self.topics

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('consumerGroups') is not None:
            self.consumer_groups = m.get('consumerGroups')

        if m.get('mode') is not None:
            self.mode = m.get('mode')

        if m.get('topics') is not None:
            self.topics = m.get('topics')

        return self

class UpdateInstanceInspectionResponseBodyLastRunConfigSnapshotItems(DaraModel):
    def __init__(
        self,
        parameters: Any = None,
        template_code: str = None,
    ):
        # This parameter is required.
        self.parameters = parameters
        # This parameter is required.
        self.template_code = template_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.parameters is not None:
            result['parameters'] = self.parameters

        if self.template_code is not None:
            result['templateCode'] = self.template_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('parameters') is not None:
            self.parameters = m.get('parameters')

        if m.get('templateCode') is not None:
            self.template_code = m.get('templateCode')

        return self

class UpdateInstanceInspectionResponseBodyLastRunAiSummary(DaraModel):
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

class UpdateInstanceInspectionResponseBodyItems(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        resource_count: int = None,
        resource_types: List[str] = None,
        template_code: str = None,
    ):
        self.description = description
        self.name = name
        self.resource_count = resource_count
        self.resource_types = resource_types
        self.template_code = template_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.name is not None:
            result['name'] = self.name

        if self.resource_count is not None:
            result['resourceCount'] = self.resource_count

        if self.resource_types is not None:
            result['resourceTypes'] = self.resource_types

        if self.template_code is not None:
            result['templateCode'] = self.template_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('resourceCount') is not None:
            self.resource_count = m.get('resourceCount')

        if m.get('resourceTypes') is not None:
            self.resource_types = m.get('resourceTypes')

        if m.get('templateCode') is not None:
            self.template_code = m.get('templateCode')

        return self

class UpdateInstanceInspectionResponseBodyConfig(DaraModel):
    def __init__(
        self,
        items: List[main_models.UpdateInstanceInspectionResponseBodyConfigItems] = None,
        resource_scope: main_models.UpdateInstanceInspectionResponseBodyConfigResourceScope = None,
        schedule: main_models.UpdateInstanceInspectionResponseBodyConfigSchedule = None,
    ):
        # This parameter is required.
        self.items = items
        # This parameter is required.
        self.resource_scope = resource_scope
        # This parameter is required.
        self.schedule = schedule

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()
        if self.resource_scope:
            self.resource_scope.validate()
        if self.schedule:
            self.schedule.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        if self.resource_scope is not None:
            result['resourceScope'] = self.resource_scope.to_map()

        if self.schedule is not None:
            result['schedule'] = self.schedule.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.UpdateInstanceInspectionResponseBodyConfigItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('resourceScope') is not None:
            temp_model = main_models.UpdateInstanceInspectionResponseBodyConfigResourceScope()
            self.resource_scope = temp_model.from_map(m.get('resourceScope'))

        if m.get('schedule') is not None:
            temp_model = main_models.UpdateInstanceInspectionResponseBodyConfigSchedule()
            self.schedule = temp_model.from_map(m.get('schedule'))

        return self

class UpdateInstanceInspectionResponseBodyConfigSchedule(DaraModel):
    def __init__(
        self,
        cron: str = None,
        enabled: bool = None,
    ):
        self.cron = cron
        # This parameter is required.
        self.enabled = enabled

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cron is not None:
            result['cron'] = self.cron

        if self.enabled is not None:
            result['enabled'] = self.enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cron') is not None:
            self.cron = m.get('cron')

        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        return self

class UpdateInstanceInspectionResponseBodyConfigResourceScope(DaraModel):
    def __init__(
        self,
        consumer_groups: List[str] = None,
        mode: str = None,
        topics: List[str] = None,
    ):
        self.consumer_groups = consumer_groups
        # This parameter is required.
        self.mode = mode
        self.topics = topics

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.consumer_groups is not None:
            result['consumerGroups'] = self.consumer_groups

        if self.mode is not None:
            result['mode'] = self.mode

        if self.topics is not None:
            result['topics'] = self.topics

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('consumerGroups') is not None:
            self.consumer_groups = m.get('consumerGroups')

        if m.get('mode') is not None:
            self.mode = m.get('mode')

        if m.get('topics') is not None:
            self.topics = m.get('topics')

        return self

class UpdateInstanceInspectionResponseBodyConfigItems(DaraModel):
    def __init__(
        self,
        parameters: Any = None,
        template_code: str = None,
    ):
        # This parameter is required.
        self.parameters = parameters
        # This parameter is required.
        self.template_code = template_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.parameters is not None:
            result['parameters'] = self.parameters

        if self.template_code is not None:
            result['templateCode'] = self.template_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('parameters') is not None:
            self.parameters = m.get('parameters')

        if m.get('templateCode') is not None:
            self.template_code = m.get('templateCode')

        return self

