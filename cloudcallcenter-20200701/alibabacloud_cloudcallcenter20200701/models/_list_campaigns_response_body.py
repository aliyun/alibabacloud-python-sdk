# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudcallcenter20200701 import models as main_models
from darabonba.model import DaraModel

class ListCampaignsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListCampaignsResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
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

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

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
            temp_model = main_models.ListCampaignsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

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
        completed_rate: int = None,
        max_attempt_count: int = None,
        min_attempt_interval: int = None,
        name: str = None,
        planed_end_time: int = None,
        planed_start_time: int = None,
        queue_id: str = None,
        queue_name: str = None,
        simulation: bool = None,
        state: str = None,
        strategy_parameters: str = None,
        strategy_type: str = None,
        total_cases: int = None,
    ):
        self.actual_end_time = actual_end_time
        self.actual_start_time = actual_start_time
        self.campaign_id = campaign_id
        self.cases_aborted = cases_aborted
        self.cases_connected = cases_connected
        self.cases_uncompleted = cases_uncompleted
        self.completed_rate = completed_rate
        self.max_attempt_count = max_attempt_count
        self.min_attempt_interval = min_attempt_interval
        self.name = name
        self.planed_end_time = planed_end_time
        self.planed_start_time = planed_start_time
        self.queue_id = queue_id
        self.queue_name = queue_name
        self.simulation = simulation
        self.state = state
        self.strategy_parameters = strategy_parameters
        self.strategy_type = strategy_type
        self.total_cases = total_cases

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

        if self.completed_rate is not None:
            result['CompletedRate'] = self.completed_rate

        if self.max_attempt_count is not None:
            result['MaxAttemptCount'] = self.max_attempt_count

        if self.min_attempt_interval is not None:
            result['MinAttemptInterval'] = self.min_attempt_interval

        if self.name is not None:
            result['Name'] = self.name

        if self.planed_end_time is not None:
            result['PlanedEndTime'] = self.planed_end_time

        if self.planed_start_time is not None:
            result['PlanedStartTime'] = self.planed_start_time

        if self.queue_id is not None:
            result['QueueId'] = self.queue_id

        if self.queue_name is not None:
            result['QueueName'] = self.queue_name

        if self.simulation is not None:
            result['Simulation'] = self.simulation

        if self.state is not None:
            result['State'] = self.state

        if self.strategy_parameters is not None:
            result['StrategyParameters'] = self.strategy_parameters

        if self.strategy_type is not None:
            result['StrategyType'] = self.strategy_type

        if self.total_cases is not None:
            result['TotalCases'] = self.total_cases

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

        if m.get('CompletedRate') is not None:
            self.completed_rate = m.get('CompletedRate')

        if m.get('MaxAttemptCount') is not None:
            self.max_attempt_count = m.get('MaxAttemptCount')

        if m.get('MinAttemptInterval') is not None:
            self.min_attempt_interval = m.get('MinAttemptInterval')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PlanedEndTime') is not None:
            self.planed_end_time = m.get('PlanedEndTime')

        if m.get('PlanedStartTime') is not None:
            self.planed_start_time = m.get('PlanedStartTime')

        if m.get('QueueId') is not None:
            self.queue_id = m.get('QueueId')

        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')

        if m.get('Simulation') is not None:
            self.simulation = m.get('Simulation')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('StrategyParameters') is not None:
            self.strategy_parameters = m.get('StrategyParameters')

        if m.get('StrategyType') is not None:
            self.strategy_type = m.get('StrategyType')

        if m.get('TotalCases') is not None:
            self.total_cases = m.get('TotalCases')

        return self

