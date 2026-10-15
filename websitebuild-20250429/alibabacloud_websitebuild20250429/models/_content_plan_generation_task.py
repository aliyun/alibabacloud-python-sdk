# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_websitebuild20250429 import models as main_models
from darabonba.model import DaraModel

class ContentPlanGenerationTask(DaraModel):
    def __init__(
        self,
        analysis: main_models.ContentPlanGenerationTaskAnalysis = None,
        analysis_task_id: str = None,
        config_revision: int = None,
        diagnosis_task_id: str = None,
        error_code: str = None,
        error_message: str = None,
        plan_id: str = None,
        progress: int = None,
        project_id: str = None,
        report_config_revision: int = None,
        stale_config: bool = None,
        status: str = None,
        submitted_at: int = None,
        task_id: str = None,
        task_type: str = None,
        updated_at: int = None,
    ):
        # The analysis conclusions, returned only after the analysis task succeeds.
        self.analysis = analysis
        # The ID of the analysis task on which the scheduling task is based.
        self.analysis_task_id = analysis_task_id
        # The current configuration version of the workspace when the analysis is initiated.
        self.config_revision = config_revision
        # The ID of the GEO diagnostic task used by the analysis node.
        self.diagnosis_task_id = diagnosis_task_id
        # The error code for the failure.
        self.error_code = error_code
        # The error message for the failure.
        self.error_message = error_message
        # The ID of the content plan generated after the scheduling task succeeds.
        self.plan_id = plan_id
        # The task progress, ranging from 0 to 10000.
        self.progress = progress
        # The ID of the workspace, which refers to the GEO workspace for brand marketing, namely the appWorkspaceId.
        self.project_id = project_id
        # The workspace configuration version on which the diagnostic report is based. The analysis, scheduling, and article generation processes always read this version.
        self.report_config_revision = report_config_revision
        # Indicates whether the diagnostic report is generated based on an outdated configuration. If the value is true, the frontend should prompt the user.
        self.stale_config = stale_config
        # The task status.
        self.status = status
        # The submission time, in milliseconds.
        self.submitted_at = submitted_at
        # The ID of the generation task.
        self.task_id = task_id
        # The task type. Valid values: ANALYSIS and SCHEDULE.
        self.task_type = task_type
        # The last update time, in milliseconds.
        self.updated_at = updated_at

    def validate(self):
        if self.analysis:
            self.analysis.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.analysis is not None:
            result['Analysis'] = self.analysis.to_map()

        if self.analysis_task_id is not None:
            result['AnalysisTaskId'] = self.analysis_task_id

        if self.config_revision is not None:
            result['ConfigRevision'] = self.config_revision

        if self.diagnosis_task_id is not None:
            result['DiagnosisTaskId'] = self.diagnosis_task_id

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.plan_id is not None:
            result['PlanId'] = self.plan_id

        if self.progress is not None:
            result['Progress'] = self.progress

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.report_config_revision is not None:
            result['ReportConfigRevision'] = self.report_config_revision

        if self.stale_config is not None:
            result['StaleConfig'] = self.stale_config

        if self.status is not None:
            result['Status'] = self.status

        if self.submitted_at is not None:
            result['SubmittedAt'] = self.submitted_at

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Analysis') is not None:
            temp_model = main_models.ContentPlanGenerationTaskAnalysis()
            self.analysis = temp_model.from_map(m.get('Analysis'))

        if m.get('AnalysisTaskId') is not None:
            self.analysis_task_id = m.get('AnalysisTaskId')

        if m.get('ConfigRevision') is not None:
            self.config_revision = m.get('ConfigRevision')

        if m.get('DiagnosisTaskId') is not None:
            self.diagnosis_task_id = m.get('DiagnosisTaskId')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ReportConfigRevision') is not None:
            self.report_config_revision = m.get('ReportConfigRevision')

        if m.get('StaleConfig') is not None:
            self.stale_config = m.get('StaleConfig')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SubmittedAt') is not None:
            self.submitted_at = m.get('SubmittedAt')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')

        return self

class ContentPlanGenerationTaskAnalysis(DaraModel):
    def __init__(
        self,
        modules: List[main_models.ContentPlanGenerationTaskAnalysisModules] = None,
        reference_writing_notes: List[str] = None,
        summary: str = None,
    ):
        # The analysis modules.
        self.modules = modules
        # The reference article writing guidelines, which include only structure and perspective, excluding third-party facts.
        self.reference_writing_notes = reference_writing_notes
        # The analysis summary.
        self.summary = summary

    def validate(self):
        if self.modules:
            for v1 in self.modules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Modules'] = []
        if self.modules is not None:
            for k1 in self.modules:
                result['Modules'].append(k1.to_map() if k1 else None)

        if self.reference_writing_notes is not None:
            result['ReferenceWritingNotes'] = self.reference_writing_notes

        if self.summary is not None:
            result['Summary'] = self.summary

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.modules = []
        if m.get('Modules') is not None:
            for k1 in m.get('Modules'):
                temp_model = main_models.ContentPlanGenerationTaskAnalysisModules()
                self.modules.append(temp_model.from_map(k1))

        if m.get('ReferenceWritingNotes') is not None:
            self.reference_writing_notes = m.get('ReferenceWritingNotes')

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        return self

class ContentPlanGenerationTaskAnalysisModules(DaraModel):
    def __init__(
        self,
        content: str = None,
        key_questions: List[str] = None,
        title: str = None,
    ):
        # The module content.
        self.content = content
        # The key questions.
        self.key_questions = key_questions
        # The module title.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.key_questions is not None:
            result['KeyQuestions'] = self.key_questions

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('KeyQuestions') is not None:
            self.key_questions = m.get('KeyQuestions')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

