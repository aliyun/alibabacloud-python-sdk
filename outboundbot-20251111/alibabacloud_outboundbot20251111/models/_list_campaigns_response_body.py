# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_outboundbot20251111 import models as main_models
from darabonba.model import DaraModel

class ListCampaignsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListCampaignsResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        params: List[str] = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The result code.
        self.code = code
        # The paged query result.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The error message.
        self.message = message
        # The list of error message parameters.
        self.params = params
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
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

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.params is not None:
            result['Params'] = self.params

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
            temp_model = main_models.ListCampaignsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Params') is not None:
            self.params = m.get('Params')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListCampaignsResponseBodyData(DaraModel):
    def __init__(
        self,
        list: List[main_models.ListCampaignsResponseBodyDataList] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The list of outbound campaigns.
        self.list = list
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The total number of records.
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
                temp_model = main_models.ListCampaignsResponseBodyDataList()
                self.list.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListCampaignsResponseBodyDataList(DaraModel):
    def __init__(
        self,
        actual_end_time: int = None,
        actual_start_time: int = None,
        campaign_id: str = None,
        cases_aborted: int = None,
        cases_connected: int = None,
        cases_uncompleted: int = None,
        cases_uncompleted_after_attempted: int = None,
        completed_rate: float = None,
        created_time: int = None,
        fixed_quota: int = None,
        max_attempt_count: int = None,
        min_attempt_interval: int = None,
        name: str = None,
        planned_end_time: int = None,
        planned_start_time: int = None,
        run_until_end_time: bool = None,
        script_id: str = None,
        state: str = None,
        total_cases: int = None,
        updated_time: int = None,
        weight: int = None,
    ):
        # The actual end time.
        self.actual_end_time = actual_end_time
        # The actual start time.
        self.actual_start_time = actual_start_time
        # The campaign ID.
        self.campaign_id = campaign_id
        # The number of aborted cases.
        self.cases_aborted = cases_aborted
        # The number of connected cases.
        self.cases_connected = cases_connected
        # The number of uncompleted cases.
        self.cases_uncompleted = cases_uncompleted
        # The number of cases that were attempted but not completed.
        self.cases_uncompleted_after_attempted = cases_uncompleted_after_attempted
        # The completion rate.
        self.completed_rate = completed_rate
        # The time when the campaign was created.
        self.created_time = created_time
        # The fixed number of concurrent calls.
        self.fixed_quota = fixed_quota
        # The maximum number of retries.
        self.max_attempt_count = max_attempt_count
        # The minimum retry interval.
        self.min_attempt_interval = min_attempt_interval
        # The campaign name.
        self.name = name
        # The planned end time.
        self.planned_end_time = planned_end_time
        # The planned start time.
        self.planned_start_time = planned_start_time
        # Indicates whether the campaign continues to run until the planned end time after all contacts have been called.
        self.run_until_end_time = run_until_end_time
        # The IVR flow ID.
        self.script_id = script_id
        # The campaign status.
        self.state = state
        # The total number of cases.
        self.total_cases = total_cases
        # The time when the campaign was last updated.
        self.updated_time = updated_time
        # The weight of the campaign.
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.actual_end_time is not None:
            result['ActualEndTime'] = self.actual_end_time

        if self.actual_start_time is not None:
            result['ActualStartTime'] = self.actual_start_time

        if self.campaign_id is not None:
            result['CampaignId'] = self.campaign_id

        if self.cases_aborted is not None:
            result['CasesAborted'] = self.cases_aborted

        if self.cases_connected is not None:
            result['CasesConnected'] = self.cases_connected

        if self.cases_uncompleted is not None:
            result['CasesUncompleted'] = self.cases_uncompleted

        if self.cases_uncompleted_after_attempted is not None:
            result['CasesUncompletedAfterAttempted'] = self.cases_uncompleted_after_attempted

        if self.completed_rate is not None:
            result['CompletedRate'] = self.completed_rate

        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.fixed_quota is not None:
            result['FixedQuota'] = self.fixed_quota

        if self.max_attempt_count is not None:
            result['MaxAttemptCount'] = self.max_attempt_count

        if self.min_attempt_interval is not None:
            result['MinAttemptInterval'] = self.min_attempt_interval

        if self.name is not None:
            result['Name'] = self.name

        if self.planned_end_time is not None:
            result['PlannedEndTime'] = self.planned_end_time

        if self.planned_start_time is not None:
            result['PlannedStartTime'] = self.planned_start_time

        if self.run_until_end_time is not None:
            result['RunUntilEndTime'] = self.run_until_end_time

        if self.script_id is not None:
            result['ScriptId'] = self.script_id

        if self.state is not None:
            result['State'] = self.state

        if self.total_cases is not None:
            result['TotalCases'] = self.total_cases

        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time

        if self.weight is not None:
            result['Weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActualEndTime') is not None:
            self.actual_end_time = m.get('ActualEndTime')

        if m.get('ActualStartTime') is not None:
            self.actual_start_time = m.get('ActualStartTime')

        if m.get('CampaignId') is not None:
            self.campaign_id = m.get('CampaignId')

        if m.get('CasesAborted') is not None:
            self.cases_aborted = m.get('CasesAborted')

        if m.get('CasesConnected') is not None:
            self.cases_connected = m.get('CasesConnected')

        if m.get('CasesUncompleted') is not None:
            self.cases_uncompleted = m.get('CasesUncompleted')

        if m.get('CasesUncompletedAfterAttempted') is not None:
            self.cases_uncompleted_after_attempted = m.get('CasesUncompletedAfterAttempted')

        if m.get('CompletedRate') is not None:
            self.completed_rate = m.get('CompletedRate')

        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('FixedQuota') is not None:
            self.fixed_quota = m.get('FixedQuota')

        if m.get('MaxAttemptCount') is not None:
            self.max_attempt_count = m.get('MaxAttemptCount')

        if m.get('MinAttemptInterval') is not None:
            self.min_attempt_interval = m.get('MinAttemptInterval')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PlannedEndTime') is not None:
            self.planned_end_time = m.get('PlannedEndTime')

        if m.get('PlannedStartTime') is not None:
            self.planned_start_time = m.get('PlannedStartTime')

        if m.get('RunUntilEndTime') is not None:
            self.run_until_end_time = m.get('RunUntilEndTime')

        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('TotalCases') is not None:
            self.total_cases = m.get('TotalCases')

        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        return self

