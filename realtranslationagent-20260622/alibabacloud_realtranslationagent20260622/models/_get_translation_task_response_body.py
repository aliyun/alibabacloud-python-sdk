# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_realtranslationagent20260622 import models as main_models
from darabonba.model import DaraModel

class GetTranslationTaskResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetTranslationTaskResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetTranslationTaskResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetTranslationTaskResponseBodyData(DaraModel):
    def __init__(
        self,
        base_task_id: str = None,
        config: main_models.GetTranslationTaskResponseBodyDataConfig = None,
        cost_credits: float = None,
        cost_time: int = None,
        error_message: str = None,
        estimated_cost_credits: float = None,
        estimated_time: int = None,
        extracted_terms: List[main_models.GetTranslationTaskResponseBodyDataExtractedTerms] = None,
        file_format: str = None,
        file_name: str = None,
        finished_at: str = None,
        fonts: Dict[str, List[str]] = None,
        org_id: str = None,
        original_file_name: str = None,
        page_count: int = None,
        progress: int = None,
        status: str = None,
        task_id: str = None,
        task_type: str = None,
        word_count: int = None,
        work_space_id: str = None,
    ):
        self.base_task_id = base_task_id
        self.config = config
        self.cost_credits = cost_credits
        self.cost_time = cost_time
        self.error_message = error_message
        self.estimated_cost_credits = estimated_cost_credits
        self.estimated_time = estimated_time
        self.extracted_terms = extracted_terms
        self.file_format = file_format
        self.file_name = file_name
        self.finished_at = finished_at
        self.fonts = fonts
        self.org_id = org_id
        self.original_file_name = original_file_name
        self.page_count = page_count
        self.progress = progress
        self.status = status
        self.task_id = task_id
        self.task_type = task_type
        self.word_count = word_count
        self.work_space_id = work_space_id

    def validate(self):
        if self.config:
            self.config.validate()
        if self.extracted_terms:
            for v1 in self.extracted_terms:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.base_task_id is not None:
            result['BaseTaskId'] = self.base_task_id

        if self.config is not None:
            result['Config'] = self.config.to_map()

        if self.cost_credits is not None:
            result['CostCredits'] = self.cost_credits

        if self.cost_time is not None:
            result['CostTime'] = self.cost_time

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.estimated_cost_credits is not None:
            result['EstimatedCostCredits'] = self.estimated_cost_credits

        if self.estimated_time is not None:
            result['EstimatedTime'] = self.estimated_time

        result['ExtractedTerms'] = []
        if self.extracted_terms is not None:
            for k1 in self.extracted_terms:
                result['ExtractedTerms'].append(k1.to_map() if k1 else None)

        if self.file_format is not None:
            result['FileFormat'] = self.file_format

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.finished_at is not None:
            result['FinishedAt'] = self.finished_at

        if self.fonts is not None:
            result['Fonts'] = self.fonts

        if self.org_id is not None:
            result['OrgId'] = self.org_id

        if self.original_file_name is not None:
            result['OriginalFileName'] = self.original_file_name

        if self.page_count is not None:
            result['PageCount'] = self.page_count

        if self.progress is not None:
            result['Progress'] = self.progress

        if self.status is not None:
            result['Status'] = self.status

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        if self.word_count is not None:
            result['WordCount'] = self.word_count

        if self.work_space_id is not None:
            result['WorkSpaceId'] = self.work_space_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseTaskId') is not None:
            self.base_task_id = m.get('BaseTaskId')

        if m.get('Config') is not None:
            temp_model = main_models.GetTranslationTaskResponseBodyDataConfig()
            self.config = temp_model.from_map(m.get('Config'))

        if m.get('CostCredits') is not None:
            self.cost_credits = m.get('CostCredits')

        if m.get('CostTime') is not None:
            self.cost_time = m.get('CostTime')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('EstimatedCostCredits') is not None:
            self.estimated_cost_credits = m.get('EstimatedCostCredits')

        if m.get('EstimatedTime') is not None:
            self.estimated_time = m.get('EstimatedTime')

        self.extracted_terms = []
        if m.get('ExtractedTerms') is not None:
            for k1 in m.get('ExtractedTerms'):
                temp_model = main_models.GetTranslationTaskResponseBodyDataExtractedTerms()
                self.extracted_terms.append(temp_model.from_map(k1))

        if m.get('FileFormat') is not None:
            self.file_format = m.get('FileFormat')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('FinishedAt') is not None:
            self.finished_at = m.get('FinishedAt')

        if m.get('Fonts') is not None:
            self.fonts = m.get('Fonts')

        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')

        if m.get('OriginalFileName') is not None:
            self.original_file_name = m.get('OriginalFileName')

        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        if m.get('WordCount') is not None:
            self.word_count = m.get('WordCount')

        if m.get('WorkSpaceId') is not None:
            self.work_space_id = m.get('WorkSpaceId')

        return self

class GetTranslationTaskResponseBodyDataExtractedTerms(DaraModel):
    def __init__(
        self,
        source_term: str = None,
        target_term: str = None,
    ):
        self.source_term = source_term
        self.target_term = target_term

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.source_term is not None:
            result['SourceTerm'] = self.source_term

        if self.target_term is not None:
            result['TargetTerm'] = self.target_term

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceTerm') is not None:
            self.source_term = m.get('SourceTerm')

        if m.get('TargetTerm') is not None:
            self.target_term = m.get('TargetTerm')

        return self

class GetTranslationTaskResponseBodyDataConfig(DaraModel):
    def __init__(
        self,
        security_level: str = None,
        source_language: str = None,
        style: str = None,
        target_language: str = None,
        template: str = None,
    ):
        self.security_level = security_level
        self.source_language = source_language
        self.style = style
        self.target_language = target_language
        self.template = template

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.security_level is not None:
            result['SecurityLevel'] = self.security_level

        if self.source_language is not None:
            result['SourceLanguage'] = self.source_language

        if self.style is not None:
            result['Style'] = self.style

        if self.target_language is not None:
            result['TargetLanguage'] = self.target_language

        if self.template is not None:
            result['Template'] = self.template

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityLevel') is not None:
            self.security_level = m.get('SecurityLevel')

        if m.get('SourceLanguage') is not None:
            self.source_language = m.get('SourceLanguage')

        if m.get('Style') is not None:
            self.style = m.get('Style')

        if m.get('TargetLanguage') is not None:
            self.target_language = m.get('TargetLanguage')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        return self

