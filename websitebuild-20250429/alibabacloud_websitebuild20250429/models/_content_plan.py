# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ContentPlan(DaraModel):
    def __init__(
        self,
        additional_requirements: str = None,
        analysis_task_id: str = None,
        config_revision: int = None,
        diagnosis_completed_at: int = None,
        diagnosis_task_id: str = None,
        diagnosis_type: str = None,
        end_date: str = None,
        generation_task_id: str = None,
        plan_id: str = None,
        project_id: str = None,
        publish_frequency: int = None,
        report_config_revision: int = None,
        start_date: str = None,
        status: str = None,
        summary: str = None,
        superseded_by: str = None,
        timezone: str = None,
        weekdays: List[int] = None,
    ):
        # The additional user comments.
        self.additional_requirements = additional_requirements
        # The ID of the analysis task used for scheduling.
        self.analysis_task_id = analysis_task_id
        # The current configuration version of the workspace when the analysis is initiated.
        self.config_revision = config_revision
        # The completion time of the GEO diagnosis, in milliseconds.
        self.diagnosis_completed_at = diagnosis_completed_at
        # The ID of the GEO diagnostic node.
        self.diagnosis_task_id = diagnosis_task_id
        # The type of the GEO diagnosis.
        self.diagnosis_type = diagnosis_type
        # The end date of the plan in the yyyy-MM-dd format.
        self.end_date = end_date
        # The ID of the generation task.
        self.generation_task_id = generation_task_id
        # The ID of the content plan.
        self.plan_id = plan_id
        # The ID of the workspace, which is the GEO workspace for brand marketing and corresponds to the appWorkspaceId.
        self.project_id = project_id
        # The number of scheduled articles, which equals the number of matched generation days.
        self.publish_frequency = publish_frequency
        # The workspace configuration version used for the diagnostic report, which is strictly read during article generation.
        self.report_config_revision = report_config_revision
        # The start date of the plan in the yyyy-MM-dd format.
        self.start_date = start_date
        # The status of the plan. Valid values: ACTIVE, SUPERSEDED, COMPLETED, and FAILED.
        self.status = status
        # The summary of the overall strategy for the plan.
        self.summary = summary
        # The ID of the new plan that supersedes the current plan.
        self.superseded_by = superseded_by
        # The IANA time zone used for scheduling.
        self.timezone = timezone
        # The weekly generation days, where ISO weekday 1 represents Monday and 7 represents Sunday.
        self.weekdays = weekdays

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.additional_requirements is not None:
            result['AdditionalRequirements'] = self.additional_requirements

        if self.analysis_task_id is not None:
            result['AnalysisTaskId'] = self.analysis_task_id

        if self.config_revision is not None:
            result['ConfigRevision'] = self.config_revision

        if self.diagnosis_completed_at is not None:
            result['DiagnosisCompletedAt'] = self.diagnosis_completed_at

        if self.diagnosis_task_id is not None:
            result['DiagnosisTaskId'] = self.diagnosis_task_id

        if self.diagnosis_type is not None:
            result['DiagnosisType'] = self.diagnosis_type

        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.generation_task_id is not None:
            result['GenerationTaskId'] = self.generation_task_id

        if self.plan_id is not None:
            result['PlanId'] = self.plan_id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.publish_frequency is not None:
            result['PublishFrequency'] = self.publish_frequency

        if self.report_config_revision is not None:
            result['ReportConfigRevision'] = self.report_config_revision

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        if self.status is not None:
            result['Status'] = self.status

        if self.summary is not None:
            result['Summary'] = self.summary

        if self.superseded_by is not None:
            result['SupersededBy'] = self.superseded_by

        if self.timezone is not None:
            result['Timezone'] = self.timezone

        if self.weekdays is not None:
            result['Weekdays'] = self.weekdays

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdditionalRequirements') is not None:
            self.additional_requirements = m.get('AdditionalRequirements')

        if m.get('AnalysisTaskId') is not None:
            self.analysis_task_id = m.get('AnalysisTaskId')

        if m.get('ConfigRevision') is not None:
            self.config_revision = m.get('ConfigRevision')

        if m.get('DiagnosisCompletedAt') is not None:
            self.diagnosis_completed_at = m.get('DiagnosisCompletedAt')

        if m.get('DiagnosisTaskId') is not None:
            self.diagnosis_task_id = m.get('DiagnosisTaskId')

        if m.get('DiagnosisType') is not None:
            self.diagnosis_type = m.get('DiagnosisType')

        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('GenerationTaskId') is not None:
            self.generation_task_id = m.get('GenerationTaskId')

        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('PublishFrequency') is not None:
            self.publish_frequency = m.get('PublishFrequency')

        if m.get('ReportConfigRevision') is not None:
            self.report_config_revision = m.get('ReportConfigRevision')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        if m.get('SupersededBy') is not None:
            self.superseded_by = m.get('SupersededBy')

        if m.get('Timezone') is not None:
            self.timezone = m.get('Timezone')

        if m.get('Weekdays') is not None:
            self.weekdays = m.get('Weekdays')

        return self

