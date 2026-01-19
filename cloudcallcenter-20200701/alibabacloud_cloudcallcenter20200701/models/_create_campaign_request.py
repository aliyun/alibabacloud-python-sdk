# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudcallcenter20200701 import models as main_models
from darabonba.model import DaraModel

class CreateCampaignRequest(DaraModel):
    def __init__(
        self,
        callable_time: str = None,
        case_file_key: str = None,
        case_list: List[main_models.CreateCampaignRequestCaseList] = None,
        contact_flow_id: str = None,
        end_time: str = None,
        executing_until_timeout: bool = None,
        flash_sms_parameters: str = None,
        inst_group_id: str = None,
        instance_id: str = None,
        max_attempt_count: int = None,
        min_attempt_interval: int = None,
        name: str = None,
        number_list: List[str] = None,
        queue_id: str = None,
        simulation: bool = None,
        simulation_parameters: str = None,
        start_time: str = None,
        strategy_parameters: str = None,
        strategy_type: str = None,
    ):
        self.callable_time = callable_time
        self.case_file_key = case_file_key
        self.case_list = case_list
        self.contact_flow_id = contact_flow_id
        self.end_time = end_time
        self.executing_until_timeout = executing_until_timeout
        self.flash_sms_parameters = flash_sms_parameters
        self.inst_group_id = inst_group_id
        self.instance_id = instance_id
        self.max_attempt_count = max_attempt_count
        self.min_attempt_interval = min_attempt_interval
        self.name = name
        self.number_list = number_list
        self.queue_id = queue_id
        self.simulation = simulation
        self.simulation_parameters = simulation_parameters
        self.start_time = start_time
        self.strategy_parameters = strategy_parameters
        self.strategy_type = strategy_type

    def validate(self):
        if self.case_list:
            for v1 in self.case_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.callable_time is not None:
            result['CallableTime'] = self.callable_time

        if self.case_file_key is not None:
            result['CaseFileKey'] = self.case_file_key

        result['CaseList'] = []
        if self.case_list is not None:
            for k1 in self.case_list:
                result['CaseList'].append(k1.to_map() if k1 else None)

        if self.contact_flow_id is not None:
            result['ContactFlowId'] = self.contact_flow_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.executing_until_timeout is not None:
            result['ExecutingUntilTimeout'] = self.executing_until_timeout

        if self.flash_sms_parameters is not None:
            result['FlashSmsParameters'] = self.flash_sms_parameters

        if self.inst_group_id is not None:
            result['InstGroupId'] = self.inst_group_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.max_attempt_count is not None:
            result['MaxAttemptCount'] = self.max_attempt_count

        if self.min_attempt_interval is not None:
            result['MinAttemptInterval'] = self.min_attempt_interval

        if self.name is not None:
            result['Name'] = self.name

        if self.number_list is not None:
            result['NumberList'] = self.number_list

        if self.queue_id is not None:
            result['QueueId'] = self.queue_id

        if self.simulation is not None:
            result['Simulation'] = self.simulation

        if self.simulation_parameters is not None:
            result['SimulationParameters'] = self.simulation_parameters

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.strategy_parameters is not None:
            result['StrategyParameters'] = self.strategy_parameters

        if self.strategy_type is not None:
            result['StrategyType'] = self.strategy_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallableTime') is not None:
            self.callable_time = m.get('CallableTime')

        if m.get('CaseFileKey') is not None:
            self.case_file_key = m.get('CaseFileKey')

        self.case_list = []
        if m.get('CaseList') is not None:
            for k1 in m.get('CaseList'):
                temp_model = main_models.CreateCampaignRequestCaseList()
                self.case_list.append(temp_model.from_map(k1))

        if m.get('ContactFlowId') is not None:
            self.contact_flow_id = m.get('ContactFlowId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('ExecutingUntilTimeout') is not None:
            self.executing_until_timeout = m.get('ExecutingUntilTimeout')

        if m.get('FlashSmsParameters') is not None:
            self.flash_sms_parameters = m.get('FlashSmsParameters')

        if m.get('InstGroupId') is not None:
            self.inst_group_id = m.get('InstGroupId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MaxAttemptCount') is not None:
            self.max_attempt_count = m.get('MaxAttemptCount')

        if m.get('MinAttemptInterval') is not None:
            self.min_attempt_interval = m.get('MinAttemptInterval')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NumberList') is not None:
            self.number_list = m.get('NumberList')

        if m.get('QueueId') is not None:
            self.queue_id = m.get('QueueId')

        if m.get('Simulation') is not None:
            self.simulation = m.get('Simulation')

        if m.get('SimulationParameters') is not None:
            self.simulation_parameters = m.get('SimulationParameters')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('StrategyParameters') is not None:
            self.strategy_parameters = m.get('StrategyParameters')

        if m.get('StrategyType') is not None:
            self.strategy_type = m.get('StrategyType')

        return self



class CreateCampaignRequestCaseList(DaraModel):
    def __init__(
        self,
        custom_variables: str = None,
        phone_number: str = None,
        reference_id: str = None,
    ):
        self.custom_variables = custom_variables
        self.phone_number = phone_number
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

        if self.reference_id is not None:
            result['ReferenceId'] = self.reference_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomVariables') is not None:
            self.custom_variables = m.get('CustomVariables')

        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')

        if m.get('ReferenceId') is not None:
            self.reference_id = m.get('ReferenceId')

        return self

