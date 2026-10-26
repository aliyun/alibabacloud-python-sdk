# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rocketmq20220801 import models as main_models
from darabonba.model import DaraModel

class GetInstanceInspectionReportResponseBody(DaraModel):
    def __init__(
        self,
        completion: str = None,
        coverage: List[main_models.GetInstanceInspectionReportResponseBodyCoverage] = None,
        findings: List[main_models.GetInstanceInspectionReportResponseBodyFindings] = None,
        finished_at: str = None,
        html: str = None,
        inspection_run_id: str = None,
        instance_id: str = None,
        instance_name: str = None,
        markdown: str = None,
        overview: str = None,
        region_id: str = None,
        report_id: str = None,
        report_summary: main_models.GetInstanceInspectionReportResponseBodyReportSummary = None,
        template_version: str = None,
        time_range: main_models.GetInstanceInspectionReportResponseBodyTimeRange = None,
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
                temp_model = main_models.GetInstanceInspectionReportResponseBodyCoverage()
                self.coverage.append(temp_model.from_map(k1))

        self.findings = []
        if m.get('findings') is not None:
            for k1 in m.get('findings'):
                temp_model = main_models.GetInstanceInspectionReportResponseBodyFindings()
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
            temp_model = main_models.GetInstanceInspectionReportResponseBodyReportSummary()
            self.report_summary = temp_model.from_map(m.get('reportSummary'))

        if m.get('templateVersion') is not None:
            self.template_version = m.get('templateVersion')

        if m.get('timeRange') is not None:
            temp_model = main_models.GetInstanceInspectionReportResponseBodyTimeRange()
            self.time_range = temp_model.from_map(m.get('timeRange'))

        return self

class GetInstanceInspectionReportResponseBodyTimeRange(DaraModel):
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

class GetInstanceInspectionReportResponseBodyReportSummary(DaraModel):
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

class GetInstanceInspectionReportResponseBodyFindings(DaraModel):
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
        resource: main_models.GetInstanceInspectionReportResponseBodyFindingsResource = None,
        risk_type: str = None,
        source: str = None,
        template_code: str = None,
        time_range: main_models.GetInstanceInspectionReportResponseBodyFindingsTimeRange = None,
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
            temp_model = main_models.GetInstanceInspectionReportResponseBodyFindingsResource()
            self.resource = temp_model.from_map(m.get('resource'))

        if m.get('riskType') is not None:
            self.risk_type = m.get('riskType')

        if m.get('source') is not None:
            self.source = m.get('source')

        if m.get('templateCode') is not None:
            self.template_code = m.get('templateCode')

        if m.get('timeRange') is not None:
            temp_model = main_models.GetInstanceInspectionReportResponseBodyFindingsTimeRange()
            self.time_range = temp_model.from_map(m.get('timeRange'))

        if m.get('verification') is not None:
            self.verification = m.get('verification')

        return self

class GetInstanceInspectionReportResponseBodyFindingsTimeRange(DaraModel):
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

class GetInstanceInspectionReportResponseBodyFindingsResource(DaraModel):
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

class GetInstanceInspectionReportResponseBodyCoverage(DaraModel):
    def __init__(
        self,
        diagnosis_status: str = None,
        name: str = None,
        observed_at: str = None,
        result: str = None,
        status: str = None,
        template_code: str = None,
        time_range: main_models.GetInstanceInspectionReportResponseBodyCoverageTimeRange = None,
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
            temp_model = main_models.GetInstanceInspectionReportResponseBodyCoverageTimeRange()
            self.time_range = temp_model.from_map(m.get('timeRange'))

        return self

class GetInstanceInspectionReportResponseBodyCoverageTimeRange(DaraModel):
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

