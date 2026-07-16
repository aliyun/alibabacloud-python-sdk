# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_outboundbot20191226 import models as main_models
from darabonba.model import DaraModel

class QueryJobsWithResultResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        jobs: main_models.QueryJobsWithResultResponseBodyJobs = None,
        labels: List[main_models.QueryJobsWithResultResponseBodyLabels] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        variable_names: List[str] = None,
    ):
        # The response code. The value `OK` indicates that the request was successful.
        self.code = code
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The paginated list of jobs.
        self.jobs = jobs
        # The tag information that can be used as filter criteria.
        # 
        # > Displays information for all tags in the job group that have enumerated values.
        self.labels = labels
        # The response message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success
        # The names of tags to be collected.
        self.variable_names = variable_names

    def validate(self):
        if self.jobs:
            self.jobs.validate()
        if self.labels:
            for v1 in self.labels:
                 if v1:
                    v1.validate()

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

        result['Labels'] = []
        if self.labels is not None:
            for k1 in self.labels:
                result['Labels'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.variable_names is not None:
            result['VariableNames'] = self.variable_names

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Jobs') is not None:
            temp_model = main_models.QueryJobsWithResultResponseBodyJobs()
            self.jobs = temp_model.from_map(m.get('Jobs'))

        self.labels = []
        if m.get('Labels') is not None:
            for k1 in m.get('Labels'):
                temp_model = main_models.QueryJobsWithResultResponseBodyLabels()
                self.labels.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('VariableNames') is not None:
            self.variable_names = m.get('VariableNames')

        return self

class QueryJobsWithResultResponseBodyLabels(DaraModel):
    def __init__(
        self,
        name: str = None,
        value_list: List[str] = None,
    ):
        # Tag Name
        self.name = name
        # Tag value list.
        self.value_list = value_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.value_list is not None:
            result['ValueList'] = self.value_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ValueList') is not None:
            self.value_list = m.get('ValueList')

        return self

class QueryJobsWithResultResponseBodyJobs(DaraModel):
    def __init__(
        self,
        list: List[main_models.QueryJobsWithResultResponseBodyJobsList] = None,
        page_count: int = None,
        page_number: int = None,
        page_size: int = None,
        row_count: int = None,
    ):
        # A list of jobs.
        self.list = list
        # The total number of pages.
        self.page_count = page_count
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries.
        self.row_count = row_count

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

        if self.page_count is not None:
            result['PageCount'] = self.page_count

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.row_count is not None:
            result['RowCount'] = self.row_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k1 in m.get('List'):
                temp_model = main_models.QueryJobsWithResultResponseBodyJobsList()
                self.list.append(temp_model.from_map(k1))

        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RowCount') is not None:
            self.row_count = m.get('RowCount')

        return self

class QueryJobsWithResultResponseBodyJobsList(DaraModel):
    def __init__(
        self,
        id: str = None,
        job_failure_reason: str = None,
        latest_task: main_models.QueryJobsWithResultResponseBodyJobsListLatestTask = None,
        status: str = None,
        status_name: str = None,
    ):
        # The job ID.
        self.id = id
        # The reason the job failed.
        self.job_failure_reason = job_failure_reason
        # The most recent call.
        self.latest_task = latest_task
        # The job status. Valid values:
        # 
        # - `Scheduling`: The job is being scheduled.
        # 
        # - `Executing`: The job is in progress.
        # 
        # - `Succeeded`: The job succeeded, and the contact was reached.
        # 
        # - `Paused`: The job is paused.
        # 
        # - `Failed`: The job failed because the contact was not reached.
        # 
        # - `Cancelled`: The job was cancelled by a user.
        # 
        # - `Drafted`: The job is a draft.
        self.status = status
        # The name of the job status.
        self.status_name = status_name

    def validate(self):
        if self.latest_task:
            self.latest_task.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.job_failure_reason is not None:
            result['JobFailureReason'] = self.job_failure_reason

        if self.latest_task is not None:
            result['LatestTask'] = self.latest_task.to_map()

        if self.status is not None:
            result['Status'] = self.status

        if self.status_name is not None:
            result['StatusName'] = self.status_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('JobFailureReason') is not None:
            self.job_failure_reason = m.get('JobFailureReason')

        if m.get('LatestTask') is not None:
            temp_model = main_models.QueryJobsWithResultResponseBodyJobsListLatestTask()
            self.latest_task = temp_model.from_map(m.get('LatestTask'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StatusName') is not None:
            self.status_name = m.get('StatusName')

        return self

class QueryJobsWithResultResponseBodyJobsListLatestTask(DaraModel):
    def __init__(
        self,
        call_duration: int = None,
        call_duration_display: str = None,
        call_time: int = None,
        contact: main_models.QueryJobsWithResultResponseBodyJobsListLatestTaskContact = None,
        dial_exception_codes: List[main_models.QueryJobsWithResultResponseBodyJobsListLatestTaskDialExceptionCodes] = None,
        extras: List[main_models.QueryJobsWithResultResponseBodyJobsListLatestTaskExtras] = None,
        hang_up_direction: str = None,
        has_answered: bool = None,
        has_hang_up_by_rejection: bool = None,
        has_last_playback_completed: bool = None,
        has_reached_end_of_flow: bool = None,
        status: str = None,
        status_name: str = None,
        tag_hits: List[main_models.QueryJobsWithResultResponseBodyJobsListLatestTaskTagHits] = None,
        task_end_reason: str = None,
    ):
        # The call duration, in milliseconds.
        self.call_duration = call_duration
        # The call duration, formatted for display.
        self.call_duration_display = call_duration_display
        # The time when the call was made. This value is a UNIX timestamp in milliseconds.
        self.call_time = call_time
        # The contact.
        self.contact = contact
        # The error codes for the call.
        self.dial_exception_codes = dial_exception_codes
        # The custom tags (key-value pairs) associated with the call.
        self.extras = extras
        self.hang_up_direction = hang_up_direction
        # Indicates whether the call was answered.
        self.has_answered = has_answered
        # Indicates whether the call was hung up due to rejection.
        self.has_hang_up_by_rejection = has_hang_up_by_rejection
        # Indicates whether the last voice playback was completed before the call was hung up.
        self.has_last_playback_completed = has_last_playback_completed
        # Indicates whether the call flow was completed.
        self.has_reached_end_of_flow = has_reached_end_of_flow
        # The call status.
        self.status = status
        # The name of the call status.
        self.status_name = status_name
        # Information about tags that were matched. This parameter is returned for flows created using the legacy canvas.
        self.tag_hits = tag_hits
        # The call end reason.
        self.task_end_reason = task_end_reason

    def validate(self):
        if self.contact:
            self.contact.validate()
        if self.dial_exception_codes:
            for v1 in self.dial_exception_codes:
                 if v1:
                    v1.validate()
        if self.extras:
            for v1 in self.extras:
                 if v1:
                    v1.validate()
        if self.tag_hits:
            for v1 in self.tag_hits:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.call_duration is not None:
            result['CallDuration'] = self.call_duration

        if self.call_duration_display is not None:
            result['CallDurationDisplay'] = self.call_duration_display

        if self.call_time is not None:
            result['CallTime'] = self.call_time

        if self.contact is not None:
            result['Contact'] = self.contact.to_map()

        result['DialExceptionCodes'] = []
        if self.dial_exception_codes is not None:
            for k1 in self.dial_exception_codes:
                result['DialExceptionCodes'].append(k1.to_map() if k1 else None)

        result['Extras'] = []
        if self.extras is not None:
            for k1 in self.extras:
                result['Extras'].append(k1.to_map() if k1 else None)

        if self.hang_up_direction is not None:
            result['HangUpDirection'] = self.hang_up_direction

        if self.has_answered is not None:
            result['HasAnswered'] = self.has_answered

        if self.has_hang_up_by_rejection is not None:
            result['HasHangUpByRejection'] = self.has_hang_up_by_rejection

        if self.has_last_playback_completed is not None:
            result['HasLastPlaybackCompleted'] = self.has_last_playback_completed

        if self.has_reached_end_of_flow is not None:
            result['HasReachedEndOfFlow'] = self.has_reached_end_of_flow

        if self.status is not None:
            result['Status'] = self.status

        if self.status_name is not None:
            result['StatusName'] = self.status_name

        result['TagHits'] = []
        if self.tag_hits is not None:
            for k1 in self.tag_hits:
                result['TagHits'].append(k1.to_map() if k1 else None)

        if self.task_end_reason is not None:
            result['TaskEndReason'] = self.task_end_reason

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallDuration') is not None:
            self.call_duration = m.get('CallDuration')

        if m.get('CallDurationDisplay') is not None:
            self.call_duration_display = m.get('CallDurationDisplay')

        if m.get('CallTime') is not None:
            self.call_time = m.get('CallTime')

        if m.get('Contact') is not None:
            temp_model = main_models.QueryJobsWithResultResponseBodyJobsListLatestTaskContact()
            self.contact = temp_model.from_map(m.get('Contact'))

        self.dial_exception_codes = []
        if m.get('DialExceptionCodes') is not None:
            for k1 in m.get('DialExceptionCodes'):
                temp_model = main_models.QueryJobsWithResultResponseBodyJobsListLatestTaskDialExceptionCodes()
                self.dial_exception_codes.append(temp_model.from_map(k1))

        self.extras = []
        if m.get('Extras') is not None:
            for k1 in m.get('Extras'):
                temp_model = main_models.QueryJobsWithResultResponseBodyJobsListLatestTaskExtras()
                self.extras.append(temp_model.from_map(k1))

        if m.get('HangUpDirection') is not None:
            self.hang_up_direction = m.get('HangUpDirection')

        if m.get('HasAnswered') is not None:
            self.has_answered = m.get('HasAnswered')

        if m.get('HasHangUpByRejection') is not None:
            self.has_hang_up_by_rejection = m.get('HasHangUpByRejection')

        if m.get('HasLastPlaybackCompleted') is not None:
            self.has_last_playback_completed = m.get('HasLastPlaybackCompleted')

        if m.get('HasReachedEndOfFlow') is not None:
            self.has_reached_end_of_flow = m.get('HasReachedEndOfFlow')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StatusName') is not None:
            self.status_name = m.get('StatusName')

        self.tag_hits = []
        if m.get('TagHits') is not None:
            for k1 in m.get('TagHits'):
                temp_model = main_models.QueryJobsWithResultResponseBodyJobsListLatestTaskTagHits()
                self.tag_hits.append(temp_model.from_map(k1))

        if m.get('TaskEndReason') is not None:
            self.task_end_reason = m.get('TaskEndReason')

        return self

class QueryJobsWithResultResponseBodyJobsListLatestTaskTagHits(DaraModel):
    def __init__(
        self,
        tag_group: str = None,
        tag_name: str = None,
    ):
        # The tag group to which the tag belongs.
        self.tag_group = tag_group
        # The tag name.
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

class QueryJobsWithResultResponseBodyJobsListLatestTaskExtras(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
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

class QueryJobsWithResultResponseBodyJobsListLatestTaskDialExceptionCodes(DaraModel):
    def __init__(
        self,
        code: str = None,
        hint: str = None,
    ):
        # The error code.
        self.code = code
        # Error message
        self.hint = hint

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.hint is not None:
            result['Hint'] = self.hint

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Hint') is not None:
            self.hint = m.get('Hint')

        return self

class QueryJobsWithResultResponseBodyJobsListLatestTaskContact(DaraModel):
    def __init__(
        self,
        honorific: str = None,
        id: str = None,
        job_uuid: str = None,
        name: str = None,
        phone_number: str = None,
        preferred_phone_number: str = None,
        reference_id: str = None,
        role: str = None,
        round: int = None,
        state: str = None,
    ):
        # The honorific for the contact, such as Mr. or Ms. If not provided, it defaults to the value of the `Name` parameter.
        # 
        # > This is a custom parameter. You can specify it in the JSON object when you start an outbound job.
        self.honorific = honorific
        # The unique ID of the contact, generated by the system when the contact list is uploaded.
        self.id = id
        # The job ID.
        self.job_uuid = job_uuid
        # The name of the contact. For example, John Smith.
        self.name = name
        # The phone number of the contact.
        self.phone_number = phone_number
        # The phone number specified by the callee during the conversation. If provided, Outbound Bot calls this number.
        # 
        # > This is a custom parameter. You can specify it in the JSON object when you start an outbound job.
        self.preferred_phone_number = preferred_phone_number
        # Your custom ID for the contact. This ID helps you uniquely identify the contact and prevent issues caused by duplicate names.
        self.reference_id = reference_id
        # The role of the contact in the outbound calling scenario. This parameter is optional. For example, in a debt collection scenario, roles can include `borrower`, `co-borrower`, or `guarantor`.
        # 
        # > This is a custom parameter. You can specify it in the JSON object when starting a job.
        self.role = role
        # The call attempt number.
        self.round = round
        # The status of the contact. For example, `Available` (the contact is available), `WrongNumber` (the phone number is incorrect), or `DoesNotExist` (the phone number does not exist).
        # 
        # > This is a custom parameter. You can specify it in the JSON object when you start an outbound job.
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.honorific is not None:
            result['Honorific'] = self.honorific

        if self.id is not None:
            result['Id'] = self.id

        if self.job_uuid is not None:
            result['JobUuid'] = self.job_uuid

        if self.name is not None:
            result['Name'] = self.name

        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number

        if self.preferred_phone_number is not None:
            result['PreferredPhoneNumber'] = self.preferred_phone_number

        if self.reference_id is not None:
            result['ReferenceId'] = self.reference_id

        if self.role is not None:
            result['Role'] = self.role

        if self.round is not None:
            result['Round'] = self.round

        if self.state is not None:
            result['State'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Honorific') is not None:
            self.honorific = m.get('Honorific')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('JobUuid') is not None:
            self.job_uuid = m.get('JobUuid')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')

        if m.get('PreferredPhoneNumber') is not None:
            self.preferred_phone_number = m.get('PreferredPhoneNumber')

        if m.get('ReferenceId') is not None:
            self.reference_id = m.get('ReferenceId')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('Round') is not None:
            self.round = m.get('Round')

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

