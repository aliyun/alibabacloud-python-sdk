# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_outboundbot20191226 import models as main_models
from darabonba.model import DaraModel

class QueryJobsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        jobs: main_models.QueryJobsResponseBodyJobs = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # HTTP status code.
        self.code = code
        # HTTP status code.
        self.http_status_code = http_status_code
        # Job data.
        self.jobs = jobs
        # Response message.
        self.message = message
        # Request ID.
        self.request_id = request_id
        # Indicates whether the call succeeded.
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
            temp_model = main_models.QueryJobsResponseBodyJobs()
            self.jobs = temp_model.from_map(m.get('Jobs'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryJobsResponseBodyJobs(DaraModel):
    def __init__(
        self,
        list: List[main_models.QueryJobsResponseBodyJobsList] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # Job array.
        self.list = list
        # Page number.
        self.page_number = page_number
        # Page size.
        self.page_size = page_size
        # Total number of records.
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
                temp_model = main_models.QueryJobsResponseBodyJobsList()
                self.list.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class QueryJobsResponseBodyJobsList(DaraModel):
    def __init__(
        self,
        calling_numbers: List[str] = None,
        contacts: List[main_models.QueryJobsResponseBodyJobsListContacts] = None,
        extras: List[main_models.QueryJobsResponseBodyJobsListExtras] = None,
        failure_reason: str = None,
        job_group_id: str = None,
        job_id: str = None,
        priority: int = None,
        reference_id: str = None,
        scenario_id: str = None,
        status: str = None,
        strategy_id: str = None,
        summary: List[main_models.QueryJobsResponseBodyJobsListSummary] = None,
        tag_hits: List[main_models.QueryJobsResponseBodyJobsListTagHits] = None,
        tasks: List[main_models.QueryJobsResponseBodyJobsListTasks] = None,
    ):
        # Caller number list.
        self.calling_numbers = calling_numbers
        # Contact information. This parameter is deprecated.
        # 
        # > Use the DescribeJob operation instead.
        self.contacts = contacts
        # Business data. Shows tag collection status for Large Language Model (LLM) scenarios.
        # 
        # > Keys TenantId and ServiceId are system parameters.
        self.extras = extras
        # Failure reason.
        # 
        # - Unknown
        # 
        # - NoAnswer
        # 
        # - InvalidStrategy
        # 
        # - TimeUp
        # 
        # - NoStrategy
        # 
        # - CallFailed
        # 
        # - PerDayCallCountLimit
        # 
        # - ContactBlockList
        # 
        # - EmptyNumber
        # 
        # - JobPerDayCallCountLimit
        # 
        # - VerificationCancelled
        # 
        # - ContactSuspended
        # 
        # - InArrears
        # 
        # - OutOfService
        self.failure_reason = failure_reason
        # Task ID.
        self.job_group_id = job_group_id
        # Job ID.
        self.job_id = job_id
        # Priority.
        self.priority = priority
        # Associated business ID.
        self.reference_id = reference_id
        # Scenario ID. This parameter is deprecated.
        self.scenario_id = scenario_id
        # Job status.
        # 
        # - Scheduling (0)
        # 
        # - Executing (1)
        # 
        # - Succeeded (2)
        # 
        # - Paused (3)
        # 
        # - Failed (4)
        # 
        # - Cancelled (5)
        # 
        # - Drafted (6)
        self.status = status
        # Strategy ID.
        self.strategy_id = strategy_id
        # Conversation summary. This field is deprecated.
        self.summary = summary
        # Tags hit in small model scenarios.
        self.tag_hits = tag_hits
        # Call list. This parameter is deprecated.
        # 
        # > Use the searchTask operation instead.
        self.tasks = tasks

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
        if self.tag_hits:
            for v1 in self.tag_hits:
                 if v1:
                    v1.validate()
        if self.tasks:
            for v1 in self.tasks:
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

        result['TagHits'] = []
        if self.tag_hits is not None:
            for k1 in self.tag_hits:
                result['TagHits'].append(k1.to_map() if k1 else None)

        result['Tasks'] = []
        if self.tasks is not None:
            for k1 in self.tasks:
                result['Tasks'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallingNumbers') is not None:
            self.calling_numbers = m.get('CallingNumbers')

        self.contacts = []
        if m.get('Contacts') is not None:
            for k1 in m.get('Contacts'):
                temp_model = main_models.QueryJobsResponseBodyJobsListContacts()
                self.contacts.append(temp_model.from_map(k1))

        self.extras = []
        if m.get('Extras') is not None:
            for k1 in m.get('Extras'):
                temp_model = main_models.QueryJobsResponseBodyJobsListExtras()
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
                temp_model = main_models.QueryJobsResponseBodyJobsListSummary()
                self.summary.append(temp_model.from_map(k1))

        self.tag_hits = []
        if m.get('TagHits') is not None:
            for k1 in m.get('TagHits'):
                temp_model = main_models.QueryJobsResponseBodyJobsListTagHits()
                self.tag_hits.append(temp_model.from_map(k1))

        self.tasks = []
        if m.get('Tasks') is not None:
            for k1 in m.get('Tasks'):
                temp_model = main_models.QueryJobsResponseBodyJobsListTasks()
                self.tasks.append(temp_model.from_map(k1))

        return self

class QueryJobsResponseBodyJobsListTasks(DaraModel):
    def __init__(
        self,
        actual_time: int = None,
        brief: str = None,
        call_id: str = None,
        called_number: str = None,
        calling_number: str = None,
        chatbot_id: str = None,
        contact: main_models.QueryJobsResponseBodyJobsListTasksContact = None,
        duration: int = None,
        job_id: str = None,
        planed_time: int = None,
        scenario_id: str = None,
        status: str = None,
        task_id: str = None,
    ):
        # Actual call time.
        self.actual_time = actual_time
        # Summary. This field is deprecated.
        self.brief = brief
        # SIP call ID.
        self.call_id = call_id
        # Callee number.
        self.called_number = called_number
        # Caller number.
        self.calling_number = calling_number
        # Chatbot ID.
        self.chatbot_id = chatbot_id
        # Contact information.
        self.contact = contact
        # Call duration in seconds.
        self.duration = duration
        # Job ID.
        self.job_id = job_id
        # Scheduled call time.
        self.planed_time = planed_time
        # Scenario ID.
        self.scenario_id = scenario_id
        # The status of the task. Valid values are described below. Note that the Succeeded status is subdivided by reason. The generic Succeeded: 1 (Connected) status is no longer returned, and a specific success reason is provided instead.
        # 
        # - Executing: 0 (Calling).
        # 
        # - Succeeded: 1 (Connected).
        # 
        # - NoAnswer: 2 (Not connected – No answer).
        # 
        # - NotExist: 3 (Not connected – Nonexistent number).
        # 
        # - Busy: 4 (Not connected – Line busy).
        # 
        # - Cancelled: 5 (Not dialed – Task stopped).
        # 
        # - Failed: 6 (Failed).
        # 
        # - NotConnected: 7 (Not connected – Unreachable).
        # 
        # - PoweredOff: 8 (Not connected – Powered off).
        # 
        # - OutOfService: 9 (Not connected – Service suspended).
        # 
        # - InArrears: 10 (Not connected – Account has an overdue payment).
        # 
        # - EmptyNumber: 11 (Not dialed – Invalid number).
        # 
        # - PerDayCallCountLimit: 12 (Not dialed – Daily call limit exceeded).
        # 
        # - ContactBlockList: 13 (Not dialed – Number on blocklist).
        # 
        # - CallerNotRegistered: 14 (Not dialed – Caller ID not registered).
        # 
        # - Terminated: 15 (Not dialed – Terminated).
        # 
        # - VerificationCancelled: 16 (Not dialed – Canceled due to pre-call validation failure).
        # 
        # - OutOfServiceNoCall: 17 (Not dialed – Service suspended).
        # 
        # - InArrearsNoCall: 18 (Not dialed – Account has an overdue payment).
        # 
        # - CallingNumberNotExist: 19 (Not dialed – Caller ID does not exist).
        # 
        # - SucceededFinish: 20 (Connected – Completed normally).
        # 
        # - SucceededChatbotHangUpAfterNoAnswer: 21 (Connected – Bot hung up due to unrecognized input).
        # 
        # - SucceededChatbotHangUpAfterSilence: 22 (Connected – Bot hung up due to a silence timeout).
        # 
        # - SucceededClientHangUpAfterNoAnswer: 23 (Connected – User hung up due to unrecognized input).
        # 
        # - SucceededClientHangUp: 24 (Connected – User hung up).
        # 
        # - SucceededTransferByIntent: 25 (Connected – Transferred to an agent based on an intent match).
        # 
        # - SucceededTransferAfterNoAnswer: 26 (Connected – Transferred to an agent due to unrecognized input).
        # 
        # - SucceededInoInterAction: 27 (Connected – No user interaction).
        # 
        # - SucceededError: 28 (Connected – Call interrupted by a system error).
        # 
        # - SucceededSpecialInterceptVoiceAssistant: 29 (Connected – Intercepted by a voice assistant).
        # 
        # - SucceededSpecialInterceptExtensionNumberTransfer: 30 (Connected – Intercepted due to an extension transfer).
        # 
        # - SucceededSpecialInterceptCustomSpecialIntercept: 31 (Connected – Intercepted by a custom rule).
        # 
        # - HighRiskSipCode: 32 (Not dialed – High-risk number).
        self.status = status
        # Call ID.
        self.task_id = task_id

    def validate(self):
        if self.contact:
            self.contact.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.actual_time is not None:
            result['ActualTime'] = self.actual_time

        if self.brief is not None:
            result['Brief'] = self.brief

        if self.call_id is not None:
            result['CallId'] = self.call_id

        if self.called_number is not None:
            result['CalledNumber'] = self.called_number

        if self.calling_number is not None:
            result['CallingNumber'] = self.calling_number

        if self.chatbot_id is not None:
            result['ChatbotId'] = self.chatbot_id

        if self.contact is not None:
            result['Contact'] = self.contact.to_map()

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.planed_time is not None:
            result['PlanedTime'] = self.planed_time

        if self.scenario_id is not None:
            result['ScenarioId'] = self.scenario_id

        if self.status is not None:
            result['Status'] = self.status

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActualTime') is not None:
            self.actual_time = m.get('ActualTime')

        if m.get('Brief') is not None:
            self.brief = m.get('Brief')

        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')

        if m.get('CalledNumber') is not None:
            self.called_number = m.get('CalledNumber')

        if m.get('CallingNumber') is not None:
            self.calling_number = m.get('CallingNumber')

        if m.get('ChatbotId') is not None:
            self.chatbot_id = m.get('ChatbotId')

        if m.get('Contact') is not None:
            temp_model = main_models.QueryJobsResponseBodyJobsListTasksContact()
            self.contact = temp_model.from_map(m.get('Contact'))

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('PlanedTime') is not None:
            self.planed_time = m.get('PlanedTime')

        if m.get('ScenarioId') is not None:
            self.scenario_id = m.get('ScenarioId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

class QueryJobsResponseBodyJobsListTasksContact(DaraModel):
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
        # Contact ID.
        self.contact_id = contact_id
        # Contact name.
        self.contact_name = contact_name
        # Honorific.
        self.honorific = honorific
        # Job ID.
        self.job_id = job_id
        # Contact phone number.
        self.phone_number = phone_number
        # Business association ID.
        self.reference_id = reference_id
        # Role.
        self.role = role
        # Status.
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

class QueryJobsResponseBodyJobsListTagHits(DaraModel):
    def __init__(
        self,
        tag_group: str = None,
        tag_name: str = None,
    ):
        # Tag group name.
        self.tag_group = tag_group
        # Tag name.
        self.tag_name = tag_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_group is not None:
            result['TagGroup'] = self.tag_group

        if self.tag_name is not None:
            result['TagName'] = self.tag_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagGroup') is not None:
            self.tag_group = m.get('TagGroup')

        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')

        return self

class QueryJobsResponseBodyJobsListSummary(DaraModel):
    def __init__(
        self,
        category: str = None,
        content: str = None,
        conversation_detail_id: str = None,
        group_id: str = None,
        job_id: str = None,
        summary_id: str = None,
        summary_name: str = None,
        task_id: str = None,
    ):
        # Category.
        self.category = category
        # Content.
        self.content = content
        # Call record ID.
        self.conversation_detail_id = conversation_detail_id
        # Task ID.
        self.group_id = group_id
        # Job ID.
        self.job_id = job_id
        # Summary ID.
        self.summary_id = summary_id
        # Summary name.
        self.summary_name = summary_name
        # Call ID.
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

        if self.group_id is not None:
            result['GroupId'] = self.group_id

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

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('SummaryId') is not None:
            self.summary_id = m.get('SummaryId')

        if m.get('SummaryName') is not None:
            self.summary_name = m.get('SummaryName')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

class QueryJobsResponseBodyJobsListExtras(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # Business data key.
        self.key = key
        # Business data value.
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

class QueryJobsResponseBodyJobsListContacts(DaraModel):
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
        # Contact ID.
        self.contact_id = contact_id
        # Contact name.
        self.contact_name = contact_name
        # Honorific.
        self.honorific = honorific
        # Job ID.
        self.job_id = job_id
        # Phone number.
        self.phone_number = phone_number
        # Associated business ID.
        self.reference_id = reference_id
        # Role.
        self.role = role
        # Status.
        # 
        # - Available
        # 
        # - WrongNumber
        # 
        # - DoesNotExist
        # 
        # - Suspended
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

