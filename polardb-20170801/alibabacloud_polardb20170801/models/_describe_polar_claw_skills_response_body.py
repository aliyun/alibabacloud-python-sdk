# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribePolarClawSkillsResponseBody(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        page_number: int = None,
        page_record_count: int = None,
        request_id: str = None,
        skill_list: List[main_models.DescribePolarClawSkillsResponseBodySkillList] = None,
        total_record_count: int = None,
    ):
        # The application ID.
        self.application_id = application_id
        # The page number.
        self.page_number = page_number
        # The number of entries on the current page.
        self.page_record_count = page_record_count
        # Id of the request
        self.request_id = request_id
        # The skill list.
        self.skill_list = skill_list
        # The total number of entries.
        self.total_record_count = total_record_count

    def validate(self):
        if self.skill_list:
            for v1 in self.skill_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SkillList'] = []
        if self.skill_list is not None:
            for k1 in self.skill_list:
                result['SkillList'].append(k1.to_map() if k1 else None)

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.skill_list = []
        if m.get('SkillList') is not None:
            for k1 in m.get('SkillList'):
                temp_model = main_models.DescribePolarClawSkillsResponseBodySkillList()
                self.skill_list.append(temp_model.from_map(k1))

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class DescribePolarClawSkillsResponseBodySkillList(DaraModel):
    def __init__(
        self,
        assessment_status: str = None,
        available_to_agent: bool = None,
        disabled: bool = None,
        evaluation_status: str = None,
        file_count: int = None,
        path: str = None,
        risk_detail: str = None,
        size: int = None,
        skill_name: str = None,
        skill_version: str = None,
        source: str = None,
        status: str = None,
        summary: str = None,
        title: str = None,
    ):
        # The assessment status.
        self.assessment_status = assessment_status
        # Indicates whether the skill is available to the agent. The value is false if the skill is not in the agent workspace or is excluded by the availability policy of the agent.
        self.available_to_agent = available_to_agent
        # Indicates whether the skill is disabled. If AgentId is not specified, the status of the default agent is returned.
        self.disabled = disabled
        # The evaluation status.
        self.evaluation_status = evaluation_status
        # The total number of files.
        self.file_count = file_count
        # The directory path.
        self.path = path
        # The baseline risk details.
        self.risk_detail = risk_detail
        # The size of the databases and tables. Unit: bytes.
        self.size = size
        # The skill name.
        self.skill_name = skill_name
        # The skill version.
        self.skill_version = skill_version
        # The skill source. Valid values:
        # - PUBLIC: public
        # - SELF: private
        # - OTHER: other
        self.source = source
        # The skill status.
        self.status = status
        # The OpenAPI summary.
        self.summary = summary
        # The title.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.assessment_status is not None:
            result['AssessmentStatus'] = self.assessment_status

        if self.available_to_agent is not None:
            result['AvailableToAgent'] = self.available_to_agent

        if self.disabled is not None:
            result['Disabled'] = self.disabled

        if self.evaluation_status is not None:
            result['EvaluationStatus'] = self.evaluation_status

        if self.file_count is not None:
            result['FileCount'] = self.file_count

        if self.path is not None:
            result['Path'] = self.path

        if self.risk_detail is not None:
            result['RiskDetail'] = self.risk_detail

        if self.size is not None:
            result['Size'] = self.size

        if self.skill_name is not None:
            result['SkillName'] = self.skill_name

        if self.skill_version is not None:
            result['SkillVersion'] = self.skill_version

        if self.source is not None:
            result['Source'] = self.source

        if self.status is not None:
            result['Status'] = self.status

        if self.summary is not None:
            result['Summary'] = self.summary

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssessmentStatus') is not None:
            self.assessment_status = m.get('AssessmentStatus')

        if m.get('AvailableToAgent') is not None:
            self.available_to_agent = m.get('AvailableToAgent')

        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')

        if m.get('EvaluationStatus') is not None:
            self.evaluation_status = m.get('EvaluationStatus')

        if m.get('FileCount') is not None:
            self.file_count = m.get('FileCount')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('RiskDetail') is not None:
            self.risk_detail = m.get('RiskDetail')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('SkillName') is not None:
            self.skill_name = m.get('SkillName')

        if m.get('SkillVersion') is not None:
            self.skill_version = m.get('SkillVersion')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

