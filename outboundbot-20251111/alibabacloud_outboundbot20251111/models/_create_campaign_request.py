# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_outboundbot20251111 import models as main_models
from darabonba.model import DaraModel

class CreateCampaignRequest(DaraModel):
    def __init__(
        self,
        attempt_order: str = None,
        callable_time: str = None,
        case_file_key: str = None,
        cases: List[main_models.CreateCampaignRequestCases] = None,
        dialing_timeout_seconds: int = None,
        end_time: int = None,
        fixed_quota: int = None,
        flash_sms_parameters: str = None,
        holiday_restricted: bool = None,
        instance_id: str = None,
        max_attempt_count: int = None,
        min_attempt_interval: int = None,
        name: str = None,
        numbers: List[str] = None,
        redial_restrictions: str = None,
        run_until_end_time: bool = None,
        script_id: str = None,
        start_time: int = None,
        weight: int = None,
    ):
        # The call execution order. Default value: MIN_ATTEMPT_FIRST. Valid values:
        # - PRIORITY_FIRST: priority first.
        # - MIN_ATTEMPT_FIRST: minimum attempt count first.
        self.attempt_order = attempt_order
        # The callable time range for the task. The value is a JSON object that contains two properties: beginTime and EndTime.
        # 
        # This parameter is required.
        self.callable_time = callable_time
        # The task contact list, which is an OSS object key obtained through the GenerateFileUploadParams operation. You can also leave this parameter empty and append contacts later through the AppendCases operation.
        self.case_file_key = case_file_key
        # The contact list. You can also leave this parameter empty and append contacts later through the AppendCases operation.
        self.cases = cases
        # The dialing timeout period, in seconds. Default value: 25.
        self.dialing_timeout_seconds = dialing_timeout_seconds
        # The task end time.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The minimum concurrency for the task. A value of 0 indicates no guaranteed minimum, and resources are allocated by weight.
        # 
        # If multiple tasks have a minimum concurrency configured:
        # 
        # - If the total concurrency is less than the instance total concurrency, the minimum concurrency of each task is satisfied first, and the remaining resources are allocated proportionally by weight.
        # 
        # - If the total concurrency exceeds the instance total concurrency, the minimum concurrency no longer serves as a guaranteed minimum but is used as a weight factor in the calculation.
        self.fixed_quota = fixed_quota
        # The flash SMS parameters.
        self.flash_sms_parameters = flash_sms_parameters
        # Specifies whether to prohibit outbound calls on holidays.
        self.holiday_restricted = holiday_restricted
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The maximum number of attempts. This specifies the maximum number of times a number is called when the call fails.
        # 
        # This parameter is required.
        self.max_attempt_count = max_attempt_count
        # The interval between attempts.
        # 
        # This parameter is required.
        self.min_attempt_interval = min_attempt_interval
        # The task name.
        # 
        # This parameter is required.
        self.name = name
        # The list of caller numbers for the outbound task.
        self.numbers = numbers
        # The list of redial restriction conditions. If this parameter is not specified, no restrictions are applied. Valid values:
        # - CALLEE_NOT_EXISTS: Do not call nonexistent numbers.
        # - OUT_OF_SERVICE: Do not call numbers that are out of service.
        self.redial_restrictions = redial_restrictions
        # Specifies whether to keep the scheduling state until the task end time after all contacts are called. Default value: false. Valid values:
        # - true: The task remains in the scheduling state, and you can continue to append contacts.
        # - false: The task changes to completed, and you cannot append contacts.
        self.run_until_end_time = run_until_end_time
        # The scenario ID.
        # 
        # This parameter is required.
        self.script_id = script_id
        # The task start time.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The weight. The value is an integer in the range of 0 to 100. A larger value indicates more concurrency allocated during scheduling.
        self.weight = weight

    def validate(self):
        if self.cases:
            for v1 in self.cases:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attempt_order is not None:
            result['AttemptOrder'] = self.attempt_order

        if self.callable_time is not None:
            result['CallableTime'] = self.callable_time

        if self.case_file_key is not None:
            result['CaseFileKey'] = self.case_file_key

        result['Cases'] = []
        if self.cases is not None:
            for k1 in self.cases:
                result['Cases'].append(k1.to_map() if k1 else None)

        if self.dialing_timeout_seconds is not None:
            result['DialingTimeoutSeconds'] = self.dialing_timeout_seconds

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.fixed_quota is not None:
            result['FixedQuota'] = self.fixed_quota

        if self.flash_sms_parameters is not None:
            result['FlashSmsParameters'] = self.flash_sms_parameters

        if self.holiday_restricted is not None:
            result['HolidayRestricted'] = self.holiday_restricted

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.max_attempt_count is not None:
            result['MaxAttemptCount'] = self.max_attempt_count

        if self.min_attempt_interval is not None:
            result['MinAttemptInterval'] = self.min_attempt_interval

        if self.name is not None:
            result['Name'] = self.name

        if self.numbers is not None:
            result['Numbers'] = self.numbers

        if self.redial_restrictions is not None:
            result['RedialRestrictions'] = self.redial_restrictions

        if self.run_until_end_time is not None:
            result['RunUntilEndTime'] = self.run_until_end_time

        if self.script_id is not None:
            result['ScriptId'] = self.script_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.weight is not None:
            result['Weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttemptOrder') is not None:
            self.attempt_order = m.get('AttemptOrder')

        if m.get('CallableTime') is not None:
            self.callable_time = m.get('CallableTime')

        if m.get('CaseFileKey') is not None:
            self.case_file_key = m.get('CaseFileKey')

        self.cases = []
        if m.get('Cases') is not None:
            for k1 in m.get('Cases'):
                temp_model = main_models.CreateCampaignRequestCases()
                self.cases.append(temp_model.from_map(k1))

        if m.get('DialingTimeoutSeconds') is not None:
            self.dialing_timeout_seconds = m.get('DialingTimeoutSeconds')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('FixedQuota') is not None:
            self.fixed_quota = m.get('FixedQuota')

        if m.get('FlashSmsParameters') is not None:
            self.flash_sms_parameters = m.get('FlashSmsParameters')

        if m.get('HolidayRestricted') is not None:
            self.holiday_restricted = m.get('HolidayRestricted')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MaxAttemptCount') is not None:
            self.max_attempt_count = m.get('MaxAttemptCount')

        if m.get('MinAttemptInterval') is not None:
            self.min_attempt_interval = m.get('MinAttemptInterval')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Numbers') is not None:
            self.numbers = m.get('Numbers')

        if m.get('RedialRestrictions') is not None:
            self.redial_restrictions = m.get('RedialRestrictions')

        if m.get('RunUntilEndTime') is not None:
            self.run_until_end_time = m.get('RunUntilEndTime')

        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        return self

class CreateCampaignRequestCases(DaraModel):
    def __init__(
        self,
        custom_variables: str = None,
        phone_number: str = None,
        priority: str = None,
        reference_id: str = None,
    ):
        # The custom variables defined by the customer. The value is a JSON object that contains up to 10 properties. The name and value of each property are defined by the customer.
        self.custom_variables = custom_variables
        # The phone number of the contact.
        self.phone_number = phone_number
        # The priority of the contact. Default value: 1.
        self.priority = priority
        # The business ID of the contact.
        self.reference_id = reference_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_variables is not None:
            result['CustomVariables'] = self.custom_variables

        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.reference_id is not None:
            result['ReferenceId'] = self.reference_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomVariables') is not None:
            self.custom_variables = m.get('CustomVariables')

        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('ReferenceId') is not None:
            self.reference_id = m.get('ReferenceId')

        return self

