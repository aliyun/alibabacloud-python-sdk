# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_outboundbot20191226 import models as main_models
from darabonba.model import DaraModel

class ListJobsByGroupResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        jobs: main_models.ListJobsByGroupResponseBodyJobs = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.jobs = jobs
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.jobs:
            self.jobs.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.jobs is not None:
            result['Jobs'] = self.jobs.to_map()

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

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Jobs') is not None:
            temp_model = main_models.ListJobsByGroupResponseBodyJobs()
            self.jobs = temp_model.from_map(m.get('Jobs'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListJobsByGroupResponseBodyJobs(DaraModel):
    def __init__(
        self,
        list: List[main_models.ListJobsByGroupResponseBodyJobsList] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.list = list
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.list:
            for v1 in self.list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['List'] = []
        if self.list is not None:
            for k1 in self.list:
                result['List'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k1 in m.get('List'):
                temp_model = main_models.ListJobsByGroupResponseBodyJobsList()
                self.list.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListJobsByGroupResponseBodyJobsList(DaraModel):
    def __init__(
        self,
        calling_numbers: List[str] = None,
        contacts: List[main_models.ListJobsByGroupResponseBodyJobsListContacts] = None,
        extras: List[main_models.ListJobsByGroupResponseBodyJobsListExtras] = None,
        failure_reason: str = None,
        job_group_id: str = None,
        job_id: str = None,
        priority: int = None,
        reference_id: str = None,
        scenario_id: str = None,
        status: str = None,
        strategy_id: str = None,
        summary: List[main_models.ListJobsByGroupResponseBodyJobsListSummary] = None,
        system_priority: int = None,
    ):
        self.calling_numbers = calling_numbers
        self.contacts = contacts
        self.extras = extras
        self.failure_reason = failure_reason
        self.job_group_id = job_group_id
        self.job_id = job_id
        self.priority = priority
        self.reference_id = reference_id
        self.scenario_id = scenario_id
        self.status = status
        self.strategy_id = strategy_id
        self.summary = summary
        self.system_priority = system_priority

    def validate(self):
        if self.contacts:
            for v1 in self.contacts:
                 if v1:
                    v1.validate()
        if self.extras:
            for v1 in self.extras:
                 if v1:
                    v1.validate()
        if self.summary:
            for v1 in self.summary:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.calling_numbers is not None:
            result['CallingNumbers'] = self.calling_numbers

        result['Contacts'] = []
        if self.contacts is not None:
            for k1 in self.contacts:
                result['Contacts'].append(k1.to_map() if k1 else None)

        result['Extras'] = []
        if self.extras is not None:
            for k1 in self.extras:
                result['Extras'].append(k1.to_map() if k1 else None)

        if self.failure_reason is not None:
            result['FailureReason'] = self.failure_reason

        if self.job_group_id is not None:
            result['JobGroupId'] = self.job_group_id

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.reference_id is not None:
            result['ReferenceId'] = self.reference_id

        if self.scenario_id is not None:
            result['ScenarioId'] = self.scenario_id

        if self.status is not None:
            result['Status'] = self.status

        if self.strategy_id is not None:
            result['StrategyId'] = self.strategy_id

        result['Summary'] = []
        if self.summary is not None:
            for k1 in self.summary:
                result['Summary'].append(k1.to_map() if k1 else None)

        if self.system_priority is not None:
            result['SystemPriority'] = self.system_priority

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallingNumbers') is not None:
            self.calling_numbers = m.get('CallingNumbers')

        self.contacts = []
        if m.get('Contacts') is not None:
            for k1 in m.get('Contacts'):
                temp_model = main_models.ListJobsByGroupResponseBodyJobsListContacts()
                self.contacts.append(temp_model.from_map(k1))

        self.extras = []
        if m.get('Extras') is not None:
            for k1 in m.get('Extras'):
                temp_model = main_models.ListJobsByGroupResponseBodyJobsListExtras()
                self.extras.append(temp_model.from_map(k1))

        if m.get('FailureReason') is not None:
            self.failure_reason = m.get('FailureReason')

        if m.get('JobGroupId') is not None:
            self.job_group_id = m.get('JobGroupId')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('ReferenceId') is not None:
            self.reference_id = m.get('ReferenceId')

        if m.get('ScenarioId') is not None:
            self.scenario_id = m.get('ScenarioId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StrategyId') is not None:
            self.strategy_id = m.get('StrategyId')

        self.summary = []
        if m.get('Summary') is not None:
            for k1 in m.get('Summary'):
                temp_model = main_models.ListJobsByGroupResponseBodyJobsListSummary()
                self.summary.append(temp_model.from_map(k1))

        if m.get('SystemPriority') is not None:
            self.system_priority = m.get('SystemPriority')

        return self

class ListJobsByGroupResponseBodyJobsListSummary(DaraModel):
    def __init__(
        self,
        category: str = None,
        content: str = None,
        conversation_detail_id: str = None,
        job_group_id: str = None,
        job_id: str = None,
        summary_id: str = None,
        summary_name: str = None,
        task_id: str = None,
    ):
        self.category = category
        self.content = content
        self.conversation_detail_id = conversation_detail_id
        self.job_group_id = job_group_id
        self.job_id = job_id
        self.summary_id = summary_id
        self.summary_name = summary_name
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.content is not None:
            result['Content'] = self.content

        if self.conversation_detail_id is not None:
            result['ConversationDetailId'] = self.conversation_detail_id

        if self.job_group_id is not None:
            result['JobGroupId'] = self.job_group_id

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.summary_id is not None:
            result['SummaryId'] = self.summary_id

        if self.summary_name is not None:
            result['SummaryName'] = self.summary_name

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('ConversationDetailId') is not None:
            self.conversation_detail_id = m.get('ConversationDetailId')

        if m.get('JobGroupId') is not None:
            self.job_group_id = m.get('JobGroupId')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('SummaryId') is not None:
            self.summary_id = m.get('SummaryId')

        if m.get('SummaryName') is not None:
            self.summary_name = m.get('SummaryName')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

class ListJobsByGroupResponseBodyJobsListExtras(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListJobsByGroupResponseBodyJobsListContacts(DaraModel):
    def __init__(
        self,
        contact_id: str = None,
        contact_name: str = None,
        honorific: str = None,
        job_id: str = None,
        phone_number: str = None,
        reference_id: str = None,
        role: str = None,
        state: str = None,
    ):
        self.contact_id = contact_id
        self.contact_name = contact_name
        self.honorific = honorific
        self.job_id = job_id
        self.phone_number = phone_number
        self.reference_id = reference_id
        self.role = role
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id

        if self.contact_name is not None:
            result['ContactName'] = self.contact_name

        if self.honorific is not None:
            result['Honorific'] = self.honorific

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number

        if self.reference_id is not None:
            result['ReferenceId'] = self.reference_id

        if self.role is not None:
            result['Role'] = self.role

        if self.state is not None:
            result['State'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')

        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')

        if m.get('Honorific') is not None:
            self.honorific = m.get('Honorific')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')

        if m.get('ReferenceId') is not None:
            self.reference_id = m.get('ReferenceId')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

