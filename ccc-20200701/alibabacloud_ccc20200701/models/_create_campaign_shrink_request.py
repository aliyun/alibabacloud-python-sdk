# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateCampaignShrinkRequest(DaraModel):
    def __init__(
        self,
        callable_time: str = None,
        case_file_key: str = None,
        case_list_shrink: str = None,
        contact_flow_id: str = None,
        end_time: str = None,
        executing_until_timeout: bool = None,
        flash_sms_parameters: str = None,
        inst_group_id: str = None,
        instance_id: str = None,
        max_attempt_count: int = None,
        min_attempt_interval: int = None,
        name: str = None,
        number_list_shrink: str = None,
        queue_id: str = None,
        simulation: bool = None,
        simulation_parameters: str = None,
        start_time: str = None,
        strategy_parameters: str = None,
        strategy_type: str = None,
    ):
        # The callable time window for the predictive outbound dialing activity, formatted as a JSON object containing two properties: beginTime and endTime. Example: [{"beginTime":"00:00:00","endTime":"23:00:00"}].
        # 
        # This parameter is required.
        self.callable_time = callable_time
        # Predictive outbound dialing contact file, specified as the key of an OSS object. Obtain this key by calling the GetCaseFileUploadUrl API.
        self.case_file_key = case_file_key
        # List of predictive outbound dialing contacts. This parameter cannot be used together with CaseFileKey (import from file). You must choose either file import or list import.
        self.case_list_shrink = case_list_shrink
        # The contact flow ID associated with the predictive outbound dialing activity.
        # 
        # This parameter is required.
        self.contact_flow_id = contact_flow_id
        # The end time of the predictive outbound calling activity, formatted as a UNIX timestamp in milliseconds.
        # 
        # This parameter is required.
        self.end_time = end_time
        # Whether to keep the activity in the executing state until it expires. The default value is false. If false, the activity automatically transitions to the completed state after all contacts have been called. If true, the activity remains in the executing state even after all contacts have been called, allowing you to append additional contacts and continue dialing until the activity expires or is manually stopped.
        self.executing_until_timeout = executing_until_timeout
        # Flash SMS parameters
        self.flash_sms_parameters = flash_sms_parameters
        # Phone number collection ID
        self.inst_group_id = inst_group_id
        # Instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The maximum number of attempts for the predictive outbound calling activity. This specifies how many times a number can be redialed if the initial call fails.
        # 
        # This parameter is required.
        self.max_attempt_count = max_attempt_count
        # The minimum redial interval for the predictive outbound calling activity, which specifies the minimum time interval between redial attempts after a failed call, in minutes.
        # 
        # This parameter is required.
        self.min_attempt_interval = min_attempt_interval
        # Name of the predictive outbound dialing activity.
        # 
        # This parameter is required.
        self.name = name
        # List of caller numbers
        self.number_list_shrink = number_list_shrink
        # The skill group ID associated with the predictive outbound dialing activity.
        # 
        # This parameter is required.
        self.queue_id = queue_id
        # Indicates whether this is a simulation activity used for testing. Regular customers do not need to concern themselves with this.
        self.simulation = simulation
        # Simulation parameters used for testing. Regular customers do not need to concern themselves with this.
        self.simulation_parameters = simulation_parameters
        # The start time of the predictive outbound dialing activity, in Unix timestamp format with millisecond precision.
        # 
        # This parameter is required.
        self.start_time = start_time
        # Strategy parameters for the predictive outbound dialing activity. For PID strategy, an example format is: {"abandonRate":"5","historicalConnectedRate":"35"}. For PACING strategy, an example format is: {"ratio":1}. abandonRate represents the desired abandonment rate, historicalConnectedRate represents the historical reference connection rate, and ratio represents the fixed dialing ratio.
        # 
        # This parameter is required.
        self.strategy_parameters = strategy_parameters
        # The strategy pattern for the predictive outbound calling activity.
        # 
        # This parameter is required.
        self.strategy_type = strategy_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.callable_time is not None:
            result['CallableTime'] = self.callable_time

        if self.case_file_key is not None:
            result['CaseFileKey'] = self.case_file_key

        if self.case_list_shrink is not None:
            result['CaseList'] = self.case_list_shrink

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

        if self.number_list_shrink is not None:
            result['NumberList'] = self.number_list_shrink

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

        if m.get('CaseList') is not None:
            self.case_list_shrink = m.get('CaseList')

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
            self.number_list_shrink = m.get('NumberList')

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

