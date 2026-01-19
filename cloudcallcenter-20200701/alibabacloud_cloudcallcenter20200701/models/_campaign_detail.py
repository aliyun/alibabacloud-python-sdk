# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CampaignDetail(DaraModel):
    def __init__(
        self,
        actual_end_time: int = None,
        actual_start_time: int = None,
        cases_aborted: int = None,
        cases_connected: int = None,
        cases_uncompleted: int = None,
        completed_rate: int = None,
        create_time: int = None,
        id: str = None,
        max_attempt_count: int = None,
        min_attempt_interval: int = None,
        name: str = None,
        planed_end_time: int = None,
        planed_start_time: int = None,
        queue_name: str = None,
        state: str = None,
        total_cases: int = None,
        update_time: int = None,
    ):
        self.actual_end_time = actual_end_time
        self.actual_start_time = actual_start_time
        self.cases_aborted = cases_aborted
        self.cases_connected = cases_connected
        self.cases_uncompleted = cases_uncompleted
        self.completed_rate = completed_rate
        self.create_time = create_time
        self.id = id
        self.max_attempt_count = max_attempt_count
        self.min_attempt_interval = min_attempt_interval
        self.name = name
        self.planed_end_time = planed_end_time
        self.planed_start_time = planed_start_time
        self.queue_name = queue_name
        self.state = state
        self.total_cases = total_cases
        self.update_time = update_time

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

        if self.cases_aborted is not None:
            result['CasesAborted'] = self.cases_aborted

        if self.cases_connected is not None:
            result['CasesConnected'] = self.cases_connected

        if self.cases_uncompleted is not None:
            result['CasesUncompleted'] = self.cases_uncompleted

        if self.completed_rate is not None:
            result['CompletedRate'] = self.completed_rate

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.id is not None:
            result['Id'] = self.id

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

        if self.queue_name is not None:
            result['QueueName'] = self.queue_name

        if self.state is not None:
            result['State'] = self.state

        if self.total_cases is not None:
            result['TotalCases'] = self.total_cases

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActualEndTime') is not None:
            self.actual_end_time = m.get('ActualEndTime')

        if m.get('ActualStartTime') is not None:
            self.actual_start_time = m.get('ActualStartTime')

        if m.get('CasesAborted') is not None:
            self.cases_aborted = m.get('CasesAborted')

        if m.get('CasesConnected') is not None:
            self.cases_connected = m.get('CasesConnected')

        if m.get('CasesUncompleted') is not None:
            self.cases_uncompleted = m.get('CasesUncompleted')

        if m.get('CompletedRate') is not None:
            self.completed_rate = m.get('CompletedRate')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Id') is not None:
            self.id = m.get('Id')

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

        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('TotalCases') is not None:
            self.total_cases = m.get('TotalCases')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

