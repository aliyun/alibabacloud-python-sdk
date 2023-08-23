# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class CampaignDetail(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class AbortCampaignRequest(TeaModel):
    def __init__(
        self,
        campaign_id: str = None,
        instance_id: str = None,
    ):
        self.campaign_id = campaign_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.campaign_id is not None:
            result['CampaignId'] = self.campaign_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CampaignId') is not None:
            self.campaign_id = m.get('CampaignId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class AbortCampaignResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AbortCampaignResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AbortCampaignResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AbortCampaignResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AbortCasesRequest(TeaModel):
    def __init__(
        self,
        campaign_id: str = None,
        instance_id: str = None,
        phone_number_list: List[str] = None,
    ):
        self.campaign_id = campaign_id
        self.instance_id = instance_id
        self.phone_number_list = phone_number_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.campaign_id is not None:
            result['CampaignId'] = self.campaign_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.phone_number_list is not None:
            result['PhoneNumberList'] = self.phone_number_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CampaignId') is not None:
            self.campaign_id = m.get('CampaignId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PhoneNumberList') is not None:
            self.phone_number_list = m.get('PhoneNumberList')
        return self


class AbortCasesShrinkRequest(TeaModel):
    def __init__(
        self,
        campaign_id: str = None,
        instance_id: str = None,
        phone_number_list_shrink: str = None,
    ):
        self.campaign_id = campaign_id
        self.instance_id = instance_id
        self.phone_number_list_shrink = phone_number_list_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.campaign_id is not None:
            result['CampaignId'] = self.campaign_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.phone_number_list_shrink is not None:
            result['PhoneNumberList'] = self.phone_number_list_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CampaignId') is not None:
            self.campaign_id = m.get('CampaignId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PhoneNumberList') is not None:
            self.phone_number_list_shrink = m.get('PhoneNumberList')
        return self


class AbortCasesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AbortCasesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AbortCasesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AbortCasesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckDemoInstanceExistsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        http_status_code: int = None,
        message: str = None,
        params: List[str] = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.params = params
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.params is not None:
            result['Params'] = self.params
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CheckDemoInstanceExistsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckDemoInstanceExistsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CheckDemoInstanceExistsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckMQRoleAssumptionAuthorityResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        params: List[str] = None,
        request_id: str = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.params = params
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.params is not None:
            result['Params'] = self.params
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CheckMQRoleAssumptionAuthorityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckMQRoleAssumptionAuthorityResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CheckMQRoleAssumptionAuthorityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCampaignRequestCaseList(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateCampaignRequest(TeaModel):
    def __init__(
        self,
        callable_time: str = None,
        case_file_key: str = None,
        case_list: List[CreateCampaignRequestCaseList] = None,
        contact_flow_id: str = None,
        end_time: str = None,
        executing_until_timeout: bool = None,
        instance_id: str = None,
        max_attempt_count: int = None,
        min_attempt_interval: int = None,
        name: str = None,
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
        self.instance_id = instance_id
        self.max_attempt_count = max_attempt_count
        self.min_attempt_interval = min_attempt_interval
        self.name = name
        self.queue_id = queue_id
        self.simulation = simulation
        self.simulation_parameters = simulation_parameters
        self.start_time = start_time
        self.strategy_parameters = strategy_parameters
        self.strategy_type = strategy_type

    def validate(self):
        if self.case_list:
            for k in self.case_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.callable_time is not None:
            result['CallableTime'] = self.callable_time
        if self.case_file_key is not None:
            result['CaseFileKey'] = self.case_file_key
        result['CaseList'] = []
        if self.case_list is not None:
            for k in self.case_list:
                result['CaseList'].append(k.to_map() if k else None)
        if self.contact_flow_id is not None:
            result['ContactFlowId'] = self.contact_flow_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.executing_until_timeout is not None:
            result['ExecutingUntilTimeout'] = self.executing_until_timeout
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.max_attempt_count is not None:
            result['MaxAttemptCount'] = self.max_attempt_count
        if self.min_attempt_interval is not None:
            result['MinAttemptInterval'] = self.min_attempt_interval
        if self.name is not None:
            result['Name'] = self.name
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
            for k in m.get('CaseList'):
                temp_model = CreateCampaignRequestCaseList()
                self.case_list.append(temp_model.from_map(k))
        if m.get('ContactFlowId') is not None:
            self.contact_flow_id = m.get('ContactFlowId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ExecutingUntilTimeout') is not None:
            self.executing_until_timeout = m.get('ExecutingUntilTimeout')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MaxAttemptCount') is not None:
            self.max_attempt_count = m.get('MaxAttemptCount')
        if m.get('MinAttemptInterval') is not None:
            self.min_attempt_interval = m.get('MinAttemptInterval')
        if m.get('Name') is not None:
            self.name = m.get('Name')
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


class CreateCampaignShrinkRequest(TeaModel):
    def __init__(
        self,
        callable_time: str = None,
        case_file_key: str = None,
        case_list_shrink: str = None,
        contact_flow_id: str = None,
        end_time: str = None,
        executing_until_timeout: bool = None,
        instance_id: str = None,
        max_attempt_count: int = None,
        min_attempt_interval: int = None,
        name: str = None,
        queue_id: str = None,
        simulation: bool = None,
        simulation_parameters: str = None,
        start_time: str = None,
        strategy_parameters: str = None,
        strategy_type: str = None,
    ):
        self.callable_time = callable_time
        self.case_file_key = case_file_key
        self.case_list_shrink = case_list_shrink
        self.contact_flow_id = contact_flow_id
        self.end_time = end_time
        self.executing_until_timeout = executing_until_timeout
        self.instance_id = instance_id
        self.max_attempt_count = max_attempt_count
        self.min_attempt_interval = min_attempt_interval
        self.name = name
        self.queue_id = queue_id
        self.simulation = simulation
        self.simulation_parameters = simulation_parameters
        self.start_time = start_time
        self.strategy_parameters = strategy_parameters
        self.strategy_type = strategy_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.max_attempt_count is not None:
            result['MaxAttemptCount'] = self.max_attempt_count
        if self.min_attempt_interval is not None:
            result['MinAttemptInterval'] = self.min_attempt_interval
        if self.name is not None:
            result['Name'] = self.name
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
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MaxAttemptCount') is not None:
            self.max_attempt_count = m.get('MaxAttemptCount')
        if m.get('MinAttemptInterval') is not None:
            self.min_attempt_interval = m.get('MinAttemptInterval')
        if m.get('Name') is not None:
            self.name = m.get('Name')
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


class CreateCampaignResponseBody(TeaModel):
    def __init__(
        self,
        campaign_id: str = None,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
    ):
        self.campaign_id = campaign_id
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.campaign_id is not None:
            result['CampaignId'] = self.campaign_id
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CampaignId') is not None:
            self.campaign_id = m.get('CampaignId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateCampaignResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateCampaignResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateCampaignResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCorpNumberGroupRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
    ):
        self.description = description
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class CreateCorpNumberGroupResponseBodyData(TeaModel):
    def __init__(
        self,
        aliyun_uid: str = None,
        description: str = None,
        number_count: str = None,
        number_group_id: str = None,
        number_group_name: str = None,
    ):
        self.aliyun_uid = aliyun_uid
        self.description = description
        self.number_count = number_count
        self.number_group_id = number_group_id
        self.number_group_name = number_group_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyun_uid is not None:
            result['AliyunUid'] = self.aliyun_uid
        if self.description is not None:
            result['Description'] = self.description
        if self.number_count is not None:
            result['NumberCount'] = self.number_count
        if self.number_group_id is not None:
            result['NumberGroupId'] = self.number_group_id
        if self.number_group_name is not None:
            result['NumberGroupName'] = self.number_group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunUid') is not None:
            self.aliyun_uid = m.get('AliyunUid')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('NumberCount') is not None:
            self.number_count = m.get('NumberCount')
        if m.get('NumberGroupId') is not None:
            self.number_group_id = m.get('NumberGroupId')
        if m.get('NumberGroupName') is not None:
            self.number_group_name = m.get('NumberGroupName')
        return self


class CreateCorpNumberGroupResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateCorpNumberGroupResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = CreateCorpNumberGroupResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateCorpNumberGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateCorpNumberGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateCorpNumberGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDemoInstanceRequest(TeaModel):
    def __init__(
        self,
        outbound_call_whitelist: str = None,
    ):
        self.outbound_call_whitelist = outbound_call_whitelist

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.outbound_call_whitelist is not None:
            result['OutboundCallWhitelist'] = self.outbound_call_whitelist
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OutboundCallWhitelist') is not None:
            self.outbound_call_whitelist = m.get('OutboundCallWhitelist')
        return self


class CreateDemoInstanceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        http_status_code: int = None,
        message: str = None,
        params: List[str] = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.params = params
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.params is not None:
            result['Params'] = self.params
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDemoInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDemoInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateDemoInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCampaignRequest(TeaModel):
    def __init__(
        self,
        campaign_id: str = None,
        instance_id: str = None,
    ):
        self.campaign_id = campaign_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.campaign_id is not None:
            result['CampaignId'] = self.campaign_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CampaignId') is not None:
            self.campaign_id = m.get('CampaignId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetCampaignResponseBodyData(TeaModel):
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
        simulation_parameters: str = None,
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
        self.simulation_parameters = simulation_parameters
        self.state = state
        self.strategy_parameters = strategy_parameters
        self.strategy_type = strategy_type
        self.total_cases = total_cases

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if self.simulation_parameters is not None:
            result['SimulationParameters'] = self.simulation_parameters
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
        if m.get('SimulationParameters') is not None:
            self.simulation_parameters = m.get('SimulationParameters')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('StrategyParameters') is not None:
            self.strategy_parameters = m.get('StrategyParameters')
        if m.get('StrategyType') is not None:
            self.strategy_type = m.get('StrategyType')
        if m.get('TotalCases') is not None:
            self.total_cases = m.get('TotalCases')
        return self


class GetCampaignResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetCampaignResponseBodyData = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
            temp_model = GetCampaignResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetCampaignResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetCampaignResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetCampaignResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHistoricalCampaignReportRequest(TeaModel):
    def __init__(
        self,
        campaign_id: str = None,
        instance_id: str = None,
    ):
        self.campaign_id = campaign_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.campaign_id is not None:
            result['CampaignId'] = self.campaign_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CampaignId') is not None:
            self.campaign_id = m.get('CampaignId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetHistoricalCampaignReportResponseBodyData(TeaModel):
    def __init__(
        self,
        abandoned_rate: float = None,
        calls_abandoned: int = None,
        calls_connected: int = None,
        calls_dialed: int = None,
        connected_rate: float = None,
        occupancy_rate: float = None,
    ):
        self.abandoned_rate = abandoned_rate
        self.calls_abandoned = calls_abandoned
        self.calls_connected = calls_connected
        self.calls_dialed = calls_dialed
        self.connected_rate = connected_rate
        self.occupancy_rate = occupancy_rate

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.abandoned_rate is not None:
            result['AbandonedRate'] = self.abandoned_rate
        if self.calls_abandoned is not None:
            result['CallsAbandoned'] = self.calls_abandoned
        if self.calls_connected is not None:
            result['CallsConnected'] = self.calls_connected
        if self.calls_dialed is not None:
            result['CallsDialed'] = self.calls_dialed
        if self.connected_rate is not None:
            result['ConnectedRate'] = self.connected_rate
        if self.occupancy_rate is not None:
            result['OccupancyRate'] = self.occupancy_rate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AbandonedRate') is not None:
            self.abandoned_rate = m.get('AbandonedRate')
        if m.get('CallsAbandoned') is not None:
            self.calls_abandoned = m.get('CallsAbandoned')
        if m.get('CallsConnected') is not None:
            self.calls_connected = m.get('CallsConnected')
        if m.get('CallsDialed') is not None:
            self.calls_dialed = m.get('CallsDialed')
        if m.get('ConnectedRate') is not None:
            self.connected_rate = m.get('ConnectedRate')
        if m.get('OccupancyRate') is not None:
            self.occupancy_rate = m.get('OccupancyRate')
        return self


class GetHistoricalCampaignReportResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetHistoricalCampaignReportResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetHistoricalCampaignReportResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetHistoricalCampaignReportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetHistoricalCampaignReportResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetHistoricalCampaignReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstanceIdsByAliyunUidV2Request(TeaModel):
    def __init__(
        self,
        aliyun_uid: str = None,
    ):
        self.aliyun_uid = aliyun_uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyun_uid is not None:
            result['AliyunUid'] = self.aliyun_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunUid') is not None:
            self.aliyun_uid = m.get('AliyunUid')
        return self


class GetInstanceIdsByAliyunUidV2ResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        instance_ids: List[str] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.instance_ids = instance_ids
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
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
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetInstanceIdsByAliyunUidV2Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetInstanceIdsByAliyunUidV2ResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetInstanceIdsByAliyunUidV2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRealtimeCampaignStatsRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        queue_id: str = None,
    ):
        self.instance_id = instance_id
        self.queue_id = queue_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.queue_id is not None:
            result['QueueId'] = self.queue_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('QueueId') is not None:
            self.queue_id = m.get('QueueId')
        return self


class GetRealtimeCampaignStatsResponseBodyData(TeaModel):
    def __init__(
        self,
        breaking_agents: int = None,
        caps: int = None,
        logged_in_agents: int = None,
        outbound_scenario_breaking_agents: int = None,
        outbound_scenario_ready_agents: int = None,
        outbound_scenario_talking_agents: int = None,
        outbound_scenario_working_agents: int = None,
        ready_agents: int = None,
        talking_agents: int = None,
        total_agents: int = None,
        working_agents: int = None,
    ):
        self.breaking_agents = breaking_agents
        self.caps = caps
        self.logged_in_agents = logged_in_agents
        self.outbound_scenario_breaking_agents = outbound_scenario_breaking_agents
        self.outbound_scenario_ready_agents = outbound_scenario_ready_agents
        self.outbound_scenario_talking_agents = outbound_scenario_talking_agents
        self.outbound_scenario_working_agents = outbound_scenario_working_agents
        self.ready_agents = ready_agents
        self.talking_agents = talking_agents
        self.total_agents = total_agents
        self.working_agents = working_agents

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.breaking_agents is not None:
            result['BreakingAgents'] = self.breaking_agents
        if self.caps is not None:
            result['Caps'] = self.caps
        if self.logged_in_agents is not None:
            result['LoggedInAgents'] = self.logged_in_agents
        if self.outbound_scenario_breaking_agents is not None:
            result['OutboundScenarioBreakingAgents'] = self.outbound_scenario_breaking_agents
        if self.outbound_scenario_ready_agents is not None:
            result['OutboundScenarioReadyAgents'] = self.outbound_scenario_ready_agents
        if self.outbound_scenario_talking_agents is not None:
            result['OutboundScenarioTalkingAgents'] = self.outbound_scenario_talking_agents
        if self.outbound_scenario_working_agents is not None:
            result['OutboundScenarioWorkingAgents'] = self.outbound_scenario_working_agents
        if self.ready_agents is not None:
            result['ReadyAgents'] = self.ready_agents
        if self.talking_agents is not None:
            result['TalkingAgents'] = self.talking_agents
        if self.total_agents is not None:
            result['TotalAgents'] = self.total_agents
        if self.working_agents is not None:
            result['WorkingAgents'] = self.working_agents
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BreakingAgents') is not None:
            self.breaking_agents = m.get('BreakingAgents')
        if m.get('Caps') is not None:
            self.caps = m.get('Caps')
        if m.get('LoggedInAgents') is not None:
            self.logged_in_agents = m.get('LoggedInAgents')
        if m.get('OutboundScenarioBreakingAgents') is not None:
            self.outbound_scenario_breaking_agents = m.get('OutboundScenarioBreakingAgents')
        if m.get('OutboundScenarioReadyAgents') is not None:
            self.outbound_scenario_ready_agents = m.get('OutboundScenarioReadyAgents')
        if m.get('OutboundScenarioTalkingAgents') is not None:
            self.outbound_scenario_talking_agents = m.get('OutboundScenarioTalkingAgents')
        if m.get('OutboundScenarioWorkingAgents') is not None:
            self.outbound_scenario_working_agents = m.get('OutboundScenarioWorkingAgents')
        if m.get('ReadyAgents') is not None:
            self.ready_agents = m.get('ReadyAgents')
        if m.get('TalkingAgents') is not None:
            self.talking_agents = m.get('TalkingAgents')
        if m.get('TotalAgents') is not None:
            self.total_agents = m.get('TotalAgents')
        if m.get('WorkingAgents') is not None:
            self.working_agents = m.get('WorkingAgents')
        return self


class GetRealtimeCampaignStatsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetRealtimeCampaignStatsResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetRealtimeCampaignStatsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetRealtimeCampaignStatsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetRealtimeCampaignStatsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetRealtimeCampaignStatsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImportAdminsRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        ram_id_list: str = None,
    ):
        self.instance_id = instance_id
        self.ram_id_list = ram_id_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ram_id_list is not None:
            result['RamIdList'] = self.ram_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RamIdList') is not None:
            self.ram_id_list = m.get('RamIdList')
        return self


class ImportAdminsResponseBodyData(TeaModel):
    def __init__(
        self,
        extension: str = None,
        instance_id: str = None,
        ram_id: str = None,
        role_id: str = None,
        user_id: str = None,
    ):
        self.extension = extension
        self.instance_id = instance_id
        self.ram_id = ram_id
        self.role_id = role_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extension is not None:
            result['Extension'] = self.extension
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ram_id is not None:
            result['RamId'] = self.ram_id
        if self.role_id is not None:
            result['RoleId'] = self.role_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Extension') is not None:
            self.extension = m.get('Extension')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RamId') is not None:
            self.ram_id = m.get('RamId')
        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ImportAdminsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ImportAdminsResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ImportAdminsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ImportAdminsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ImportAdminsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ImportAdminsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class IssueSoftphoneCommandRequest(TeaModel):
    def __init__(
        self,
        data: str = None,
    ):
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class IssueSoftphoneCommandResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class IssueSoftphoneCommandResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: IssueSoftphoneCommandResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = IssueSoftphoneCommandResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAttemptsRequest(TeaModel):
    def __init__(
        self,
        agent_id: str = None,
        attempt_id: str = None,
        callee: str = None,
        caller: str = None,
        campaign_id: str = None,
        case_id: str = None,
        contact_id: str = None,
        end_time: int = None,
        instance_id: str = None,
        page_number: int = None,
        page_size: int = None,
        queue_id: str = None,
        start_time: int = None,
    ):
        self.agent_id = agent_id
        self.attempt_id = attempt_id
        self.callee = callee
        self.caller = caller
        self.campaign_id = campaign_id
        self.case_id = case_id
        self.contact_id = contact_id
        self.end_time = end_time
        self.instance_id = instance_id
        self.page_number = page_number
        self.page_size = page_size
        self.queue_id = queue_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id
        if self.attempt_id is not None:
            result['AttemptId'] = self.attempt_id
        if self.callee is not None:
            result['Callee'] = self.callee
        if self.caller is not None:
            result['Caller'] = self.caller
        if self.campaign_id is not None:
            result['CampaignId'] = self.campaign_id
        if self.case_id is not None:
            result['CaseId'] = self.case_id
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.queue_id is not None:
            result['QueueId'] = self.queue_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')
        if m.get('AttemptId') is not None:
            self.attempt_id = m.get('AttemptId')
        if m.get('Callee') is not None:
            self.callee = m.get('Callee')
        if m.get('Caller') is not None:
            self.caller = m.get('Caller')
        if m.get('CampaignId') is not None:
            self.campaign_id = m.get('CampaignId')
        if m.get('CaseId') is not None:
            self.case_id = m.get('CaseId')
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('QueueId') is not None:
            self.queue_id = m.get('QueueId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class ListAttemptsResponseBodyDataList(TeaModel):
    def __init__(
        self,
        agent_established_time: int = None,
        agent_id: str = None,
        agent_ring_duration: int = None,
        assign_agent_time: int = None,
        attempt_id: str = None,
        callee: str = None,
        caller: str = None,
        campaign_id: str = None,
        case_id: str = None,
        contact_id: str = None,
        customer_established_time: int = None,
        customer_released_time: int = None,
        dial_duration: int = None,
        dial_time: int = None,
        enqueue_time: int = None,
        enter_ivr_time: int = None,
        instance_id: str = None,
        ivr_duration: int = None,
        queue_duration: int = None,
        queue_id: str = None,
    ):
        self.agent_established_time = agent_established_time
        self.agent_id = agent_id
        self.agent_ring_duration = agent_ring_duration
        self.assign_agent_time = assign_agent_time
        self.attempt_id = attempt_id
        self.callee = callee
        self.caller = caller
        self.campaign_id = campaign_id
        self.case_id = case_id
        self.contact_id = contact_id
        self.customer_established_time = customer_established_time
        self.customer_released_time = customer_released_time
        self.dial_duration = dial_duration
        self.dial_time = dial_time
        self.enqueue_time = enqueue_time
        self.enter_ivr_time = enter_ivr_time
        self.instance_id = instance_id
        self.ivr_duration = ivr_duration
        self.queue_duration = queue_duration
        self.queue_id = queue_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_established_time is not None:
            result['AgentEstablishedTime'] = self.agent_established_time
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id
        if self.agent_ring_duration is not None:
            result['AgentRingDuration'] = self.agent_ring_duration
        if self.assign_agent_time is not None:
            result['AssignAgentTime'] = self.assign_agent_time
        if self.attempt_id is not None:
            result['AttemptId'] = self.attempt_id
        if self.callee is not None:
            result['Callee'] = self.callee
        if self.caller is not None:
            result['Caller'] = self.caller
        if self.campaign_id is not None:
            result['CampaignId'] = self.campaign_id
        if self.case_id is not None:
            result['CaseId'] = self.case_id
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id
        if self.customer_established_time is not None:
            result['CustomerEstablishedTime'] = self.customer_established_time
        if self.customer_released_time is not None:
            result['CustomerReleasedTime'] = self.customer_released_time
        if self.dial_duration is not None:
            result['DialDuration'] = self.dial_duration
        if self.dial_time is not None:
            result['DialTime'] = self.dial_time
        if self.enqueue_time is not None:
            result['EnqueueTime'] = self.enqueue_time
        if self.enter_ivr_time is not None:
            result['EnterIvrTime'] = self.enter_ivr_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ivr_duration is not None:
            result['IvrDuration'] = self.ivr_duration
        if self.queue_duration is not None:
            result['QueueDuration'] = self.queue_duration
        if self.queue_id is not None:
            result['QueueId'] = self.queue_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentEstablishedTime') is not None:
            self.agent_established_time = m.get('AgentEstablishedTime')
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')
        if m.get('AgentRingDuration') is not None:
            self.agent_ring_duration = m.get('AgentRingDuration')
        if m.get('AssignAgentTime') is not None:
            self.assign_agent_time = m.get('AssignAgentTime')
        if m.get('AttemptId') is not None:
            self.attempt_id = m.get('AttemptId')
        if m.get('Callee') is not None:
            self.callee = m.get('Callee')
        if m.get('Caller') is not None:
            self.caller = m.get('Caller')
        if m.get('CampaignId') is not None:
            self.campaign_id = m.get('CampaignId')
        if m.get('CaseId') is not None:
            self.case_id = m.get('CaseId')
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')
        if m.get('CustomerEstablishedTime') is not None:
            self.customer_established_time = m.get('CustomerEstablishedTime')
        if m.get('CustomerReleasedTime') is not None:
            self.customer_released_time = m.get('CustomerReleasedTime')
        if m.get('DialDuration') is not None:
            self.dial_duration = m.get('DialDuration')
        if m.get('DialTime') is not None:
            self.dial_time = m.get('DialTime')
        if m.get('EnqueueTime') is not None:
            self.enqueue_time = m.get('EnqueueTime')
        if m.get('EnterIvrTime') is not None:
            self.enter_ivr_time = m.get('EnterIvrTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IvrDuration') is not None:
            self.ivr_duration = m.get('IvrDuration')
        if m.get('QueueDuration') is not None:
            self.queue_duration = m.get('QueueDuration')
        if m.get('QueueId') is not None:
            self.queue_id = m.get('QueueId')
        return self


class ListAttemptsResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[ListAttemptsResponseBodyDataList] = None,
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
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
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
            for k in m.get('List'):
                temp_model = ListAttemptsResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAttemptsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListAttemptsResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ListAttemptsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListAttemptsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAttemptsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListAttemptsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCampaignTrendingReportRequest(TeaModel):
    def __init__(
        self,
        campaign_id: str = None,
        end_time: int = None,
        instance_id: str = None,
        start_time: int = None,
    ):
        self.campaign_id = campaign_id
        self.end_time = end_time
        self.instance_id = instance_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.campaign_id is not None:
            result['CampaignId'] = self.campaign_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CampaignId') is not None:
            self.campaign_id = m.get('CampaignId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class ListCampaignTrendingReportResponseBodyData(TeaModel):
    def __init__(
        self,
        break_agents: int = None,
        concurrency: int = None,
        datetime: int = None,
        logged_in_agents: int = None,
        outbound_scenario_breaking_agents: str = None,
        outbound_scenario_ready_agents: str = None,
        outbound_scenario_talking_agents: str = None,
        outbound_scenario_working_agents: str = None,
        ready_agents: int = None,
        talk_agents: int = None,
        work_agents: int = None,
    ):
        self.break_agents = break_agents
        self.concurrency = concurrency
        self.datetime = datetime
        self.logged_in_agents = logged_in_agents
        self.outbound_scenario_breaking_agents = outbound_scenario_breaking_agents
        self.outbound_scenario_ready_agents = outbound_scenario_ready_agents
        self.outbound_scenario_talking_agents = outbound_scenario_talking_agents
        self.outbound_scenario_working_agents = outbound_scenario_working_agents
        self.ready_agents = ready_agents
        self.talk_agents = talk_agents
        self.work_agents = work_agents

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.break_agents is not None:
            result['BreakAgents'] = self.break_agents
        if self.concurrency is not None:
            result['Concurrency'] = self.concurrency
        if self.datetime is not None:
            result['Datetime'] = self.datetime
        if self.logged_in_agents is not None:
            result['LoggedInAgents'] = self.logged_in_agents
        if self.outbound_scenario_breaking_agents is not None:
            result['OutboundScenarioBreakingAgents'] = self.outbound_scenario_breaking_agents
        if self.outbound_scenario_ready_agents is not None:
            result['OutboundScenarioReadyAgents'] = self.outbound_scenario_ready_agents
        if self.outbound_scenario_talking_agents is not None:
            result['OutboundScenarioTalkingAgents'] = self.outbound_scenario_talking_agents
        if self.outbound_scenario_working_agents is not None:
            result['OutboundScenarioWorkingAgents'] = self.outbound_scenario_working_agents
        if self.ready_agents is not None:
            result['ReadyAgents'] = self.ready_agents
        if self.talk_agents is not None:
            result['TalkAgents'] = self.talk_agents
        if self.work_agents is not None:
            result['WorkAgents'] = self.work_agents
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BreakAgents') is not None:
            self.break_agents = m.get('BreakAgents')
        if m.get('Concurrency') is not None:
            self.concurrency = m.get('Concurrency')
        if m.get('Datetime') is not None:
            self.datetime = m.get('Datetime')
        if m.get('LoggedInAgents') is not None:
            self.logged_in_agents = m.get('LoggedInAgents')
        if m.get('OutboundScenarioBreakingAgents') is not None:
            self.outbound_scenario_breaking_agents = m.get('OutboundScenarioBreakingAgents')
        if m.get('OutboundScenarioReadyAgents') is not None:
            self.outbound_scenario_ready_agents = m.get('OutboundScenarioReadyAgents')
        if m.get('OutboundScenarioTalkingAgents') is not None:
            self.outbound_scenario_talking_agents = m.get('OutboundScenarioTalkingAgents')
        if m.get('OutboundScenarioWorkingAgents') is not None:
            self.outbound_scenario_working_agents = m.get('OutboundScenarioWorkingAgents')
        if m.get('ReadyAgents') is not None:
            self.ready_agents = m.get('ReadyAgents')
        if m.get('TalkAgents') is not None:
            self.talk_agents = m.get('TalkAgents')
        if m.get('WorkAgents') is not None:
            self.work_agents = m.get('WorkAgents')
        return self


class ListCampaignTrendingReportResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ListCampaignTrendingReportResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListCampaignTrendingReportResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListCampaignTrendingReportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListCampaignTrendingReportResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListCampaignTrendingReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCampaignsRequest(TeaModel):
    def __init__(
        self,
        actual_start_time_from: str = None,
        actual_start_time_to: str = None,
        instance_id: str = None,
        name: str = None,
        page_number: int = None,
        page_size: int = None,
        planed_start_time_from: str = None,
        planed_start_time_to: str = None,
        queue_id: str = None,
        state: str = None,
    ):
        self.actual_start_time_from = actual_start_time_from
        self.actual_start_time_to = actual_start_time_to
        self.instance_id = instance_id
        self.name = name
        self.page_number = page_number
        self.page_size = page_size
        self.planed_start_time_from = planed_start_time_from
        self.planed_start_time_to = planed_start_time_to
        self.queue_id = queue_id
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actual_start_time_from is not None:
            result['ActualStartTimeFrom'] = self.actual_start_time_from
        if self.actual_start_time_to is not None:
            result['ActualStartTimeTo'] = self.actual_start_time_to
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.planed_start_time_from is not None:
            result['PlanedStartTimeFrom'] = self.planed_start_time_from
        if self.planed_start_time_to is not None:
            result['PlanedStartTimeTo'] = self.planed_start_time_to
        if self.queue_id is not None:
            result['QueueId'] = self.queue_id
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActualStartTimeFrom') is not None:
            self.actual_start_time_from = m.get('ActualStartTimeFrom')
        if m.get('ActualStartTimeTo') is not None:
            self.actual_start_time_to = m.get('ActualStartTimeTo')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PlanedStartTimeFrom') is not None:
            self.planed_start_time_from = m.get('PlanedStartTimeFrom')
        if m.get('PlanedStartTimeTo') is not None:
            self.planed_start_time_to = m.get('PlanedStartTimeTo')
        if m.get('QueueId') is not None:
            self.queue_id = m.get('QueueId')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class ListCampaignsResponseBodyDataList(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListCampaignsResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[ListCampaignsResponseBodyDataList] = None,
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
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
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
            for k in m.get('List'):
                temp_model = ListCampaignsResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListCampaignsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListCampaignsResponseBodyData = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = ListCampaignsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListCampaignsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListCampaignsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListCampaignsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCasesRequest(TeaModel):
    def __init__(
        self,
        campaign_id: str = None,
        instance_id: str = None,
        page_number: int = None,
        page_size: int = None,
        phone_number: str = None,
    ):
        self.campaign_id = campaign_id
        self.instance_id = instance_id
        self.page_number = page_number
        self.page_size = page_size
        self.phone_number = phone_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.campaign_id is not None:
            result['CampaignId'] = self.campaign_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CampaignId') is not None:
            self.campaign_id = m.get('CampaignId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        return self


class ListCasesResponseBodyDataList(TeaModel):
    def __init__(
        self,
        abandon_type: str = None,
        attempt_count: int = None,
        case_id: str = None,
        custom_variables: str = None,
        expand_info: str = None,
        failure_reason: str = None,
        phone_number: str = None,
        state: str = None,
    ):
        self.abandon_type = abandon_type
        self.attempt_count = attempt_count
        self.case_id = case_id
        self.custom_variables = custom_variables
        self.expand_info = expand_info
        self.failure_reason = failure_reason
        self.phone_number = phone_number
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.abandon_type is not None:
            result['AbandonType'] = self.abandon_type
        if self.attempt_count is not None:
            result['AttemptCount'] = self.attempt_count
        if self.case_id is not None:
            result['CaseId'] = self.case_id
        if self.custom_variables is not None:
            result['CustomVariables'] = self.custom_variables
        if self.expand_info is not None:
            result['ExpandInfo'] = self.expand_info
        if self.failure_reason is not None:
            result['FailureReason'] = self.failure_reason
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AbandonType') is not None:
            self.abandon_type = m.get('AbandonType')
        if m.get('AttemptCount') is not None:
            self.attempt_count = m.get('AttemptCount')
        if m.get('CaseId') is not None:
            self.case_id = m.get('CaseId')
        if m.get('CustomVariables') is not None:
            self.custom_variables = m.get('CustomVariables')
        if m.get('ExpandInfo') is not None:
            self.expand_info = m.get('ExpandInfo')
        if m.get('FailureReason') is not None:
            self.failure_reason = m.get('FailureReason')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class ListCasesResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[ListCasesResponseBodyDataList] = None,
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
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
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
            for k in m.get('List'):
                temp_model = ListCasesResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListCasesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListCasesResponseBodyData = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = ListCasesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListCasesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListCasesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListCasesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHistoricalAgentSkillGroupReportRequest(TeaModel):
    def __init__(
        self,
        agent_id_list: str = None,
        end_time: int = None,
        instance_id: str = None,
        media_type: str = None,
        page_number: int = None,
        page_size: int = None,
        skill_group_id_list: str = None,
        start_time: int = None,
    ):
        self.agent_id_list = agent_id_list
        self.end_time = end_time
        self.instance_id = instance_id
        self.media_type = media_type
        self.page_number = page_number
        self.page_size = page_size
        self.skill_group_id_list = skill_group_id_list
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_id_list is not None:
            result['AgentIdList'] = self.agent_id_list
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.media_type is not None:
            result['MediaType'] = self.media_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.skill_group_id_list is not None:
            result['SkillGroupIdList'] = self.skill_group_id_list
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentIdList') is not None:
            self.agent_id_list = m.get('AgentIdList')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SkillGroupIdList') is not None:
            self.skill_group_id_list = m.get('SkillGroupIdList')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class ListHistoricalAgentSkillGroupReportResponseBodyDataListBack2Back(TeaModel):
    def __init__(
        self,
        agent_answer_rate: float = None,
        answer_rate: float = None,
        average_customer_ring_time: float = None,
        average_ring_time: float = None,
        average_talk_time: int = None,
        calls_answered: int = None,
        calls_customer_handled: int = None,
        calls_dialed: int = None,
        customer_handle_rate: float = None,
        max_customer_ring_time: int = None,
        max_ring_time: int = None,
        max_talk_time: int = None,
        total_customer_ring_time: int = None,
        total_ring_time: int = None,
        total_talk_time: int = None,
    ):
        self.agent_answer_rate = agent_answer_rate
        self.answer_rate = answer_rate
        self.average_customer_ring_time = average_customer_ring_time
        self.average_ring_time = average_ring_time
        self.average_talk_time = average_talk_time
        self.calls_answered = calls_answered
        self.calls_customer_handled = calls_customer_handled
        self.calls_dialed = calls_dialed
        self.customer_handle_rate = customer_handle_rate
        self.max_customer_ring_time = max_customer_ring_time
        self.max_ring_time = max_ring_time
        self.max_talk_time = max_talk_time
        self.total_customer_ring_time = total_customer_ring_time
        self.total_ring_time = total_ring_time
        self.total_talk_time = total_talk_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_answer_rate is not None:
            result['AgentAnswerRate'] = self.agent_answer_rate
        if self.answer_rate is not None:
            result['AnswerRate'] = self.answer_rate
        if self.average_customer_ring_time is not None:
            result['AverageCustomerRingTime'] = self.average_customer_ring_time
        if self.average_ring_time is not None:
            result['AverageRingTime'] = self.average_ring_time
        if self.average_talk_time is not None:
            result['AverageTalkTime'] = self.average_talk_time
        if self.calls_answered is not None:
            result['CallsAnswered'] = self.calls_answered
        if self.calls_customer_handled is not None:
            result['CallsCustomerHandled'] = self.calls_customer_handled
        if self.calls_dialed is not None:
            result['CallsDialed'] = self.calls_dialed
        if self.customer_handle_rate is not None:
            result['CustomerHandleRate'] = self.customer_handle_rate
        if self.max_customer_ring_time is not None:
            result['MaxCustomerRingTime'] = self.max_customer_ring_time
        if self.max_ring_time is not None:
            result['MaxRingTime'] = self.max_ring_time
        if self.max_talk_time is not None:
            result['MaxTalkTime'] = self.max_talk_time
        if self.total_customer_ring_time is not None:
            result['TotalCustomerRingTime'] = self.total_customer_ring_time
        if self.total_ring_time is not None:
            result['TotalRingTime'] = self.total_ring_time
        if self.total_talk_time is not None:
            result['TotalTalkTime'] = self.total_talk_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentAnswerRate') is not None:
            self.agent_answer_rate = m.get('AgentAnswerRate')
        if m.get('AnswerRate') is not None:
            self.answer_rate = m.get('AnswerRate')
        if m.get('AverageCustomerRingTime') is not None:
            self.average_customer_ring_time = m.get('AverageCustomerRingTime')
        if m.get('AverageRingTime') is not None:
            self.average_ring_time = m.get('AverageRingTime')
        if m.get('AverageTalkTime') is not None:
            self.average_talk_time = m.get('AverageTalkTime')
        if m.get('CallsAnswered') is not None:
            self.calls_answered = m.get('CallsAnswered')
        if m.get('CallsCustomerHandled') is not None:
            self.calls_customer_handled = m.get('CallsCustomerHandled')
        if m.get('CallsDialed') is not None:
            self.calls_dialed = m.get('CallsDialed')
        if m.get('CustomerHandleRate') is not None:
            self.customer_handle_rate = m.get('CustomerHandleRate')
        if m.get('MaxCustomerRingTime') is not None:
            self.max_customer_ring_time = m.get('MaxCustomerRingTime')
        if m.get('MaxRingTime') is not None:
            self.max_ring_time = m.get('MaxRingTime')
        if m.get('MaxTalkTime') is not None:
            self.max_talk_time = m.get('MaxTalkTime')
        if m.get('TotalCustomerRingTime') is not None:
            self.total_customer_ring_time = m.get('TotalCustomerRingTime')
        if m.get('TotalRingTime') is not None:
            self.total_ring_time = m.get('TotalRingTime')
        if m.get('TotalTalkTime') is not None:
            self.total_talk_time = m.get('TotalTalkTime')
        return self


class ListHistoricalAgentSkillGroupReportResponseBodyDataListInbound(TeaModel):
    def __init__(
        self,
        average_first_response_time: float = None,
        average_hold_time: float = None,
        average_response_time: float = None,
        average_ring_time: float = None,
        average_talk_time: float = None,
        average_work_time: float = None,
        calls_attended_transfer_in: int = None,
        calls_attended_transfer_out: int = None,
        calls_blind_transfer_in: int = None,
        calls_blind_transfer_out: int = None,
        calls_handled: int = None,
        calls_hold: int = None,
        calls_offered: int = None,
        calls_ringed: int = None,
        handle_rate: float = None,
        max_hold_time: int = None,
        max_ring_time: int = None,
        max_talk_time: int = None,
        max_work_time: int = None,
        satisfaction_index: float = None,
        satisfaction_rate: float = None,
        satisfaction_surveys_offered: int = None,
        satisfaction_surveys_responded: int = None,
        total_hold_time: int = None,
        total_messages_sent: int = None,
        total_messages_sent_by_agent: int = None,
        total_messages_sent_by_customer: int = None,
        total_ring_time: int = None,
        total_talk_time: int = None,
        total_work_time: int = None,
    ):
        self.average_first_response_time = average_first_response_time
        self.average_hold_time = average_hold_time
        self.average_response_time = average_response_time
        self.average_ring_time = average_ring_time
        self.average_talk_time = average_talk_time
        self.average_work_time = average_work_time
        self.calls_attended_transfer_in = calls_attended_transfer_in
        self.calls_attended_transfer_out = calls_attended_transfer_out
        self.calls_blind_transfer_in = calls_blind_transfer_in
        self.calls_blind_transfer_out = calls_blind_transfer_out
        self.calls_handled = calls_handled
        self.calls_hold = calls_hold
        self.calls_offered = calls_offered
        self.calls_ringed = calls_ringed
        self.handle_rate = handle_rate
        self.max_hold_time = max_hold_time
        self.max_ring_time = max_ring_time
        self.max_talk_time = max_talk_time
        self.max_work_time = max_work_time
        self.satisfaction_index = satisfaction_index
        self.satisfaction_rate = satisfaction_rate
        self.satisfaction_surveys_offered = satisfaction_surveys_offered
        self.satisfaction_surveys_responded = satisfaction_surveys_responded
        self.total_hold_time = total_hold_time
        self.total_messages_sent = total_messages_sent
        self.total_messages_sent_by_agent = total_messages_sent_by_agent
        self.total_messages_sent_by_customer = total_messages_sent_by_customer
        self.total_ring_time = total_ring_time
        self.total_talk_time = total_talk_time
        self.total_work_time = total_work_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.average_first_response_time is not None:
            result['AverageFirstResponseTime'] = self.average_first_response_time
        if self.average_hold_time is not None:
            result['AverageHoldTime'] = self.average_hold_time
        if self.average_response_time is not None:
            result['AverageResponseTime'] = self.average_response_time
        if self.average_ring_time is not None:
            result['AverageRingTime'] = self.average_ring_time
        if self.average_talk_time is not None:
            result['AverageTalkTime'] = self.average_talk_time
        if self.average_work_time is not None:
            result['AverageWorkTime'] = self.average_work_time
        if self.calls_attended_transfer_in is not None:
            result['CallsAttendedTransferIn'] = self.calls_attended_transfer_in
        if self.calls_attended_transfer_out is not None:
            result['CallsAttendedTransferOut'] = self.calls_attended_transfer_out
        if self.calls_blind_transfer_in is not None:
            result['CallsBlindTransferIn'] = self.calls_blind_transfer_in
        if self.calls_blind_transfer_out is not None:
            result['CallsBlindTransferOut'] = self.calls_blind_transfer_out
        if self.calls_handled is not None:
            result['CallsHandled'] = self.calls_handled
        if self.calls_hold is not None:
            result['CallsHold'] = self.calls_hold
        if self.calls_offered is not None:
            result['CallsOffered'] = self.calls_offered
        if self.calls_ringed is not None:
            result['CallsRinged'] = self.calls_ringed
        if self.handle_rate is not None:
            result['HandleRate'] = self.handle_rate
        if self.max_hold_time is not None:
            result['MaxHoldTime'] = self.max_hold_time
        if self.max_ring_time is not None:
            result['MaxRingTime'] = self.max_ring_time
        if self.max_talk_time is not None:
            result['MaxTalkTime'] = self.max_talk_time
        if self.max_work_time is not None:
            result['MaxWorkTime'] = self.max_work_time
        if self.satisfaction_index is not None:
            result['SatisfactionIndex'] = self.satisfaction_index
        if self.satisfaction_rate is not None:
            result['SatisfactionRate'] = self.satisfaction_rate
        if self.satisfaction_surveys_offered is not None:
            result['SatisfactionSurveysOffered'] = self.satisfaction_surveys_offered
        if self.satisfaction_surveys_responded is not None:
            result['SatisfactionSurveysResponded'] = self.satisfaction_surveys_responded
        if self.total_hold_time is not None:
            result['TotalHoldTime'] = self.total_hold_time
        if self.total_messages_sent is not None:
            result['TotalMessagesSent'] = self.total_messages_sent
        if self.total_messages_sent_by_agent is not None:
            result['TotalMessagesSentByAgent'] = self.total_messages_sent_by_agent
        if self.total_messages_sent_by_customer is not None:
            result['TotalMessagesSentByCustomer'] = self.total_messages_sent_by_customer
        if self.total_ring_time is not None:
            result['TotalRingTime'] = self.total_ring_time
        if self.total_talk_time is not None:
            result['TotalTalkTime'] = self.total_talk_time
        if self.total_work_time is not None:
            result['TotalWorkTime'] = self.total_work_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AverageFirstResponseTime') is not None:
            self.average_first_response_time = m.get('AverageFirstResponseTime')
        if m.get('AverageHoldTime') is not None:
            self.average_hold_time = m.get('AverageHoldTime')
        if m.get('AverageResponseTime') is not None:
            self.average_response_time = m.get('AverageResponseTime')
        if m.get('AverageRingTime') is not None:
            self.average_ring_time = m.get('AverageRingTime')
        if m.get('AverageTalkTime') is not None:
            self.average_talk_time = m.get('AverageTalkTime')
        if m.get('AverageWorkTime') is not None:
            self.average_work_time = m.get('AverageWorkTime')
        if m.get('CallsAttendedTransferIn') is not None:
            self.calls_attended_transfer_in = m.get('CallsAttendedTransferIn')
        if m.get('CallsAttendedTransferOut') is not None:
            self.calls_attended_transfer_out = m.get('CallsAttendedTransferOut')
        if m.get('CallsBlindTransferIn') is not None:
            self.calls_blind_transfer_in = m.get('CallsBlindTransferIn')
        if m.get('CallsBlindTransferOut') is not None:
            self.calls_blind_transfer_out = m.get('CallsBlindTransferOut')
        if m.get('CallsHandled') is not None:
            self.calls_handled = m.get('CallsHandled')
        if m.get('CallsHold') is not None:
            self.calls_hold = m.get('CallsHold')
        if m.get('CallsOffered') is not None:
            self.calls_offered = m.get('CallsOffered')
        if m.get('CallsRinged') is not None:
            self.calls_ringed = m.get('CallsRinged')
        if m.get('HandleRate') is not None:
            self.handle_rate = m.get('HandleRate')
        if m.get('MaxHoldTime') is not None:
            self.max_hold_time = m.get('MaxHoldTime')
        if m.get('MaxRingTime') is not None:
            self.max_ring_time = m.get('MaxRingTime')
        if m.get('MaxTalkTime') is not None:
            self.max_talk_time = m.get('MaxTalkTime')
        if m.get('MaxWorkTime') is not None:
            self.max_work_time = m.get('MaxWorkTime')
        if m.get('SatisfactionIndex') is not None:
            self.satisfaction_index = m.get('SatisfactionIndex')
        if m.get('SatisfactionRate') is not None:
            self.satisfaction_rate = m.get('SatisfactionRate')
        if m.get('SatisfactionSurveysOffered') is not None:
            self.satisfaction_surveys_offered = m.get('SatisfactionSurveysOffered')
        if m.get('SatisfactionSurveysResponded') is not None:
            self.satisfaction_surveys_responded = m.get('SatisfactionSurveysResponded')
        if m.get('TotalHoldTime') is not None:
            self.total_hold_time = m.get('TotalHoldTime')
        if m.get('TotalMessagesSent') is not None:
            self.total_messages_sent = m.get('TotalMessagesSent')
        if m.get('TotalMessagesSentByAgent') is not None:
            self.total_messages_sent_by_agent = m.get('TotalMessagesSentByAgent')
        if m.get('TotalMessagesSentByCustomer') is not None:
            self.total_messages_sent_by_customer = m.get('TotalMessagesSentByCustomer')
        if m.get('TotalRingTime') is not None:
            self.total_ring_time = m.get('TotalRingTime')
        if m.get('TotalTalkTime') is not None:
            self.total_talk_time = m.get('TotalTalkTime')
        if m.get('TotalWorkTime') is not None:
            self.total_work_time = m.get('TotalWorkTime')
        return self


class ListHistoricalAgentSkillGroupReportResponseBodyDataListInternal(TeaModel):
    def __init__(
        self,
        average_talk_time: int = None,
        calls_answered: int = None,
        calls_dialed: int = None,
        calls_handled: int = None,
        calls_offered: int = None,
        calls_talk: int = None,
        max_talk_time: int = None,
        total_talk_time: int = None,
    ):
        self.average_talk_time = average_talk_time
        self.calls_answered = calls_answered
        self.calls_dialed = calls_dialed
        self.calls_handled = calls_handled
        self.calls_offered = calls_offered
        self.calls_talk = calls_talk
        self.max_talk_time = max_talk_time
        self.total_talk_time = total_talk_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.average_talk_time is not None:
            result['AverageTalkTime'] = self.average_talk_time
        if self.calls_answered is not None:
            result['CallsAnswered'] = self.calls_answered
        if self.calls_dialed is not None:
            result['CallsDialed'] = self.calls_dialed
        if self.calls_handled is not None:
            result['CallsHandled'] = self.calls_handled
        if self.calls_offered is not None:
            result['CallsOffered'] = self.calls_offered
        if self.calls_talk is not None:
            result['CallsTalk'] = self.calls_talk
        if self.max_talk_time is not None:
            result['MaxTalkTime'] = self.max_talk_time
        if self.total_talk_time is not None:
            result['TotalTalkTime'] = self.total_talk_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AverageTalkTime') is not None:
            self.average_talk_time = m.get('AverageTalkTime')
        if m.get('CallsAnswered') is not None:
            self.calls_answered = m.get('CallsAnswered')
        if m.get('CallsDialed') is not None:
            self.calls_dialed = m.get('CallsDialed')
        if m.get('CallsHandled') is not None:
            self.calls_handled = m.get('CallsHandled')
        if m.get('CallsOffered') is not None:
            self.calls_offered = m.get('CallsOffered')
        if m.get('CallsTalk') is not None:
            self.calls_talk = m.get('CallsTalk')
        if m.get('MaxTalkTime') is not None:
            self.max_talk_time = m.get('MaxTalkTime')
        if m.get('TotalTalkTime') is not None:
            self.total_talk_time = m.get('TotalTalkTime')
        return self


class ListHistoricalAgentSkillGroupReportResponseBodyDataListOutbound(TeaModel):
    def __init__(
        self,
        answer_rate: float = None,
        average_dialing_time: float = None,
        average_hold_time: float = None,
        average_ring_time: float = None,
        average_talk_time: float = None,
        average_work_time: float = None,
        calls_answered: int = None,
        calls_attended_transfer_in: int = None,
        calls_attended_transfer_out: int = None,
        calls_blind_transfer_in: int = None,
        calls_blind_transfer_out: int = None,
        calls_dialed: int = None,
        calls_hold: int = None,
        calls_ringed: int = None,
        max_dialing_time: int = None,
        max_hold_time: int = None,
        max_ring_time: int = None,
        max_talk_time: int = None,
        max_work_time: int = None,
        satisfaction_index: float = None,
        satisfaction_rate: float = None,
        satisfaction_surveys_offered: int = None,
        satisfaction_surveys_responded: int = None,
        total_dialing_time: int = None,
        total_hold_time: int = None,
        total_ring_time: int = None,
        total_talk_time: int = None,
        total_work_time: int = None,
    ):
        self.answer_rate = answer_rate
        self.average_dialing_time = average_dialing_time
        self.average_hold_time = average_hold_time
        self.average_ring_time = average_ring_time
        self.average_talk_time = average_talk_time
        self.average_work_time = average_work_time
        self.calls_answered = calls_answered
        self.calls_attended_transfer_in = calls_attended_transfer_in
        self.calls_attended_transfer_out = calls_attended_transfer_out
        self.calls_blind_transfer_in = calls_blind_transfer_in
        self.calls_blind_transfer_out = calls_blind_transfer_out
        self.calls_dialed = calls_dialed
        self.calls_hold = calls_hold
        self.calls_ringed = calls_ringed
        self.max_dialing_time = max_dialing_time
        self.max_hold_time = max_hold_time
        self.max_ring_time = max_ring_time
        self.max_talk_time = max_talk_time
        self.max_work_time = max_work_time
        self.satisfaction_index = satisfaction_index
        self.satisfaction_rate = satisfaction_rate
        self.satisfaction_surveys_offered = satisfaction_surveys_offered
        self.satisfaction_surveys_responded = satisfaction_surveys_responded
        self.total_dialing_time = total_dialing_time
        self.total_hold_time = total_hold_time
        self.total_ring_time = total_ring_time
        self.total_talk_time = total_talk_time
        self.total_work_time = total_work_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.answer_rate is not None:
            result['AnswerRate'] = self.answer_rate
        if self.average_dialing_time is not None:
            result['AverageDialingTime'] = self.average_dialing_time
        if self.average_hold_time is not None:
            result['AverageHoldTime'] = self.average_hold_time
        if self.average_ring_time is not None:
            result['AverageRingTime'] = self.average_ring_time
        if self.average_talk_time is not None:
            result['AverageTalkTime'] = self.average_talk_time
        if self.average_work_time is not None:
            result['AverageWorkTime'] = self.average_work_time
        if self.calls_answered is not None:
            result['CallsAnswered'] = self.calls_answered
        if self.calls_attended_transfer_in is not None:
            result['CallsAttendedTransferIn'] = self.calls_attended_transfer_in
        if self.calls_attended_transfer_out is not None:
            result['CallsAttendedTransferOut'] = self.calls_attended_transfer_out
        if self.calls_blind_transfer_in is not None:
            result['CallsBlindTransferIn'] = self.calls_blind_transfer_in
        if self.calls_blind_transfer_out is not None:
            result['CallsBlindTransferOut'] = self.calls_blind_transfer_out
        if self.calls_dialed is not None:
            result['CallsDialed'] = self.calls_dialed
        if self.calls_hold is not None:
            result['CallsHold'] = self.calls_hold
        if self.calls_ringed is not None:
            result['CallsRinged'] = self.calls_ringed
        if self.max_dialing_time is not None:
            result['MaxDialingTime'] = self.max_dialing_time
        if self.max_hold_time is not None:
            result['MaxHoldTime'] = self.max_hold_time
        if self.max_ring_time is not None:
            result['MaxRingTime'] = self.max_ring_time
        if self.max_talk_time is not None:
            result['MaxTalkTime'] = self.max_talk_time
        if self.max_work_time is not None:
            result['MaxWorkTime'] = self.max_work_time
        if self.satisfaction_index is not None:
            result['SatisfactionIndex'] = self.satisfaction_index
        if self.satisfaction_rate is not None:
            result['SatisfactionRate'] = self.satisfaction_rate
        if self.satisfaction_surveys_offered is not None:
            result['SatisfactionSurveysOffered'] = self.satisfaction_surveys_offered
        if self.satisfaction_surveys_responded is not None:
            result['SatisfactionSurveysResponded'] = self.satisfaction_surveys_responded
        if self.total_dialing_time is not None:
            result['TotalDialingTime'] = self.total_dialing_time
        if self.total_hold_time is not None:
            result['TotalHoldTime'] = self.total_hold_time
        if self.total_ring_time is not None:
            result['TotalRingTime'] = self.total_ring_time
        if self.total_talk_time is not None:
            result['TotalTalkTime'] = self.total_talk_time
        if self.total_work_time is not None:
            result['TotalWorkTime'] = self.total_work_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnswerRate') is not None:
            self.answer_rate = m.get('AnswerRate')
        if m.get('AverageDialingTime') is not None:
            self.average_dialing_time = m.get('AverageDialingTime')
        if m.get('AverageHoldTime') is not None:
            self.average_hold_time = m.get('AverageHoldTime')
        if m.get('AverageRingTime') is not None:
            self.average_ring_time = m.get('AverageRingTime')
        if m.get('AverageTalkTime') is not None:
            self.average_talk_time = m.get('AverageTalkTime')
        if m.get('AverageWorkTime') is not None:
            self.average_work_time = m.get('AverageWorkTime')
        if m.get('CallsAnswered') is not None:
            self.calls_answered = m.get('CallsAnswered')
        if m.get('CallsAttendedTransferIn') is not None:
            self.calls_attended_transfer_in = m.get('CallsAttendedTransferIn')
        if m.get('CallsAttendedTransferOut') is not None:
            self.calls_attended_transfer_out = m.get('CallsAttendedTransferOut')
        if m.get('CallsBlindTransferIn') is not None:
            self.calls_blind_transfer_in = m.get('CallsBlindTransferIn')
        if m.get('CallsBlindTransferOut') is not None:
            self.calls_blind_transfer_out = m.get('CallsBlindTransferOut')
        if m.get('CallsDialed') is not None:
            self.calls_dialed = m.get('CallsDialed')
        if m.get('CallsHold') is not None:
            self.calls_hold = m.get('CallsHold')
        if m.get('CallsRinged') is not None:
            self.calls_ringed = m.get('CallsRinged')
        if m.get('MaxDialingTime') is not None:
            self.max_dialing_time = m.get('MaxDialingTime')
        if m.get('MaxHoldTime') is not None:
            self.max_hold_time = m.get('MaxHoldTime')
        if m.get('MaxRingTime') is not None:
            self.max_ring_time = m.get('MaxRingTime')
        if m.get('MaxTalkTime') is not None:
            self.max_talk_time = m.get('MaxTalkTime')
        if m.get('MaxWorkTime') is not None:
            self.max_work_time = m.get('MaxWorkTime')
        if m.get('SatisfactionIndex') is not None:
            self.satisfaction_index = m.get('SatisfactionIndex')
        if m.get('SatisfactionRate') is not None:
            self.satisfaction_rate = m.get('SatisfactionRate')
        if m.get('SatisfactionSurveysOffered') is not None:
            self.satisfaction_surveys_offered = m.get('SatisfactionSurveysOffered')
        if m.get('SatisfactionSurveysResponded') is not None:
            self.satisfaction_surveys_responded = m.get('SatisfactionSurveysResponded')
        if m.get('TotalDialingTime') is not None:
            self.total_dialing_time = m.get('TotalDialingTime')
        if m.get('TotalHoldTime') is not None:
            self.total_hold_time = m.get('TotalHoldTime')
        if m.get('TotalRingTime') is not None:
            self.total_ring_time = m.get('TotalRingTime')
        if m.get('TotalTalkTime') is not None:
            self.total_talk_time = m.get('TotalTalkTime')
        if m.get('TotalWorkTime') is not None:
            self.total_work_time = m.get('TotalWorkTime')
        return self


class ListHistoricalAgentSkillGroupReportResponseBodyDataListOverallBreakCodeDetailList(TeaModel):
    def __init__(
        self,
        break_code: str = None,
        count: int = None,
        duration: int = None,
    ):
        self.break_code = break_code
        self.count = count
        self.duration = duration

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.break_code is not None:
            result['BreakCode'] = self.break_code
        if self.count is not None:
            result['Count'] = self.count
        if self.duration is not None:
            result['Duration'] = self.duration
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BreakCode') is not None:
            self.break_code = m.get('BreakCode')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        return self


class ListHistoricalAgentSkillGroupReportResponseBodyDataListOverall(TeaModel):
    def __init__(
        self,
        average_break_time: float = None,
        average_hold_time: float = None,
        average_ready_time: float = None,
        average_talk_time: float = None,
        average_work_time: float = None,
        break_code_detail_list: List[ListHistoricalAgentSkillGroupReportResponseBodyDataListOverallBreakCodeDetailList] = None,
        first_check_in_time: int = None,
        last_check_out_time: int = None,
        max_break_time: int = None,
        max_hold_time: int = None,
        max_ready_time: int = None,
        max_talk_time: int = None,
        max_work_time: int = None,
        occupancy_rate: float = None,
        satisfaction_index: float = None,
        satisfaction_rate: float = None,
        satisfaction_surveys_offered: int = None,
        satisfaction_surveys_responded: int = None,
        total_break_time: int = None,
        total_calls: int = None,
        total_hold_time: int = None,
        total_logged_in_time: int = None,
        total_off_site_online_time: int = None,
        total_office_phone_online_time: int = None,
        total_on_site_online_time: int = None,
        total_outbound_scenario_ready_time: int = None,
        total_outbound_scenario_time: int = None,
        total_ready_time: int = None,
        total_talk_time: int = None,
        total_work_time: int = None,
    ):
        self.average_break_time = average_break_time
        self.average_hold_time = average_hold_time
        self.average_ready_time = average_ready_time
        self.average_talk_time = average_talk_time
        self.average_work_time = average_work_time
        self.break_code_detail_list = break_code_detail_list
        self.first_check_in_time = first_check_in_time
        self.last_check_out_time = last_check_out_time
        self.max_break_time = max_break_time
        self.max_hold_time = max_hold_time
        self.max_ready_time = max_ready_time
        self.max_talk_time = max_talk_time
        self.max_work_time = max_work_time
        self.occupancy_rate = occupancy_rate
        self.satisfaction_index = satisfaction_index
        self.satisfaction_rate = satisfaction_rate
        self.satisfaction_surveys_offered = satisfaction_surveys_offered
        self.satisfaction_surveys_responded = satisfaction_surveys_responded
        self.total_break_time = total_break_time
        self.total_calls = total_calls
        self.total_hold_time = total_hold_time
        self.total_logged_in_time = total_logged_in_time
        self.total_off_site_online_time = total_off_site_online_time
        self.total_office_phone_online_time = total_office_phone_online_time
        self.total_on_site_online_time = total_on_site_online_time
        self.total_outbound_scenario_ready_time = total_outbound_scenario_ready_time
        self.total_outbound_scenario_time = total_outbound_scenario_time
        self.total_ready_time = total_ready_time
        self.total_talk_time = total_talk_time
        self.total_work_time = total_work_time

    def validate(self):
        if self.break_code_detail_list:
            for k in self.break_code_detail_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.average_break_time is not None:
            result['AverageBreakTime'] = self.average_break_time
        if self.average_hold_time is not None:
            result['AverageHoldTime'] = self.average_hold_time
        if self.average_ready_time is not None:
            result['AverageReadyTime'] = self.average_ready_time
        if self.average_talk_time is not None:
            result['AverageTalkTime'] = self.average_talk_time
        if self.average_work_time is not None:
            result['AverageWorkTime'] = self.average_work_time
        result['BreakCodeDetailList'] = []
        if self.break_code_detail_list is not None:
            for k in self.break_code_detail_list:
                result['BreakCodeDetailList'].append(k.to_map() if k else None)
        if self.first_check_in_time is not None:
            result['FirstCheckInTime'] = self.first_check_in_time
        if self.last_check_out_time is not None:
            result['LastCheckOutTime'] = self.last_check_out_time
        if self.max_break_time is not None:
            result['MaxBreakTime'] = self.max_break_time
        if self.max_hold_time is not None:
            result['MaxHoldTime'] = self.max_hold_time
        if self.max_ready_time is not None:
            result['MaxReadyTime'] = self.max_ready_time
        if self.max_talk_time is not None:
            result['MaxTalkTime'] = self.max_talk_time
        if self.max_work_time is not None:
            result['MaxWorkTime'] = self.max_work_time
        if self.occupancy_rate is not None:
            result['OccupancyRate'] = self.occupancy_rate
        if self.satisfaction_index is not None:
            result['SatisfactionIndex'] = self.satisfaction_index
        if self.satisfaction_rate is not None:
            result['SatisfactionRate'] = self.satisfaction_rate
        if self.satisfaction_surveys_offered is not None:
            result['SatisfactionSurveysOffered'] = self.satisfaction_surveys_offered
        if self.satisfaction_surveys_responded is not None:
            result['SatisfactionSurveysResponded'] = self.satisfaction_surveys_responded
        if self.total_break_time is not None:
            result['TotalBreakTime'] = self.total_break_time
        if self.total_calls is not None:
            result['TotalCalls'] = self.total_calls
        if self.total_hold_time is not None:
            result['TotalHoldTime'] = self.total_hold_time
        if self.total_logged_in_time is not None:
            result['TotalLoggedInTime'] = self.total_logged_in_time
        if self.total_off_site_online_time is not None:
            result['TotalOffSiteOnlineTime'] = self.total_off_site_online_time
        if self.total_office_phone_online_time is not None:
            result['TotalOfficePhoneOnlineTime'] = self.total_office_phone_online_time
        if self.total_on_site_online_time is not None:
            result['TotalOnSiteOnlineTime'] = self.total_on_site_online_time
        if self.total_outbound_scenario_ready_time is not None:
            result['TotalOutboundScenarioReadyTime'] = self.total_outbound_scenario_ready_time
        if self.total_outbound_scenario_time is not None:
            result['TotalOutboundScenarioTime'] = self.total_outbound_scenario_time
        if self.total_ready_time is not None:
            result['TotalReadyTime'] = self.total_ready_time
        if self.total_talk_time is not None:
            result['TotalTalkTime'] = self.total_talk_time
        if self.total_work_time is not None:
            result['TotalWorkTime'] = self.total_work_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AverageBreakTime') is not None:
            self.average_break_time = m.get('AverageBreakTime')
        if m.get('AverageHoldTime') is not None:
            self.average_hold_time = m.get('AverageHoldTime')
        if m.get('AverageReadyTime') is not None:
            self.average_ready_time = m.get('AverageReadyTime')
        if m.get('AverageTalkTime') is not None:
            self.average_talk_time = m.get('AverageTalkTime')
        if m.get('AverageWorkTime') is not None:
            self.average_work_time = m.get('AverageWorkTime')
        self.break_code_detail_list = []
        if m.get('BreakCodeDetailList') is not None:
            for k in m.get('BreakCodeDetailList'):
                temp_model = ListHistoricalAgentSkillGroupReportResponseBodyDataListOverallBreakCodeDetailList()
                self.break_code_detail_list.append(temp_model.from_map(k))
        if m.get('FirstCheckInTime') is not None:
            self.first_check_in_time = m.get('FirstCheckInTime')
        if m.get('LastCheckOutTime') is not None:
            self.last_check_out_time = m.get('LastCheckOutTime')
        if m.get('MaxBreakTime') is not None:
            self.max_break_time = m.get('MaxBreakTime')
        if m.get('MaxHoldTime') is not None:
            self.max_hold_time = m.get('MaxHoldTime')
        if m.get('MaxReadyTime') is not None:
            self.max_ready_time = m.get('MaxReadyTime')
        if m.get('MaxTalkTime') is not None:
            self.max_talk_time = m.get('MaxTalkTime')
        if m.get('MaxWorkTime') is not None:
            self.max_work_time = m.get('MaxWorkTime')
        if m.get('OccupancyRate') is not None:
            self.occupancy_rate = m.get('OccupancyRate')
        if m.get('SatisfactionIndex') is not None:
            self.satisfaction_index = m.get('SatisfactionIndex')
        if m.get('SatisfactionRate') is not None:
            self.satisfaction_rate = m.get('SatisfactionRate')
        if m.get('SatisfactionSurveysOffered') is not None:
            self.satisfaction_surveys_offered = m.get('SatisfactionSurveysOffered')
        if m.get('SatisfactionSurveysResponded') is not None:
            self.satisfaction_surveys_responded = m.get('SatisfactionSurveysResponded')
        if m.get('TotalBreakTime') is not None:
            self.total_break_time = m.get('TotalBreakTime')
        if m.get('TotalCalls') is not None:
            self.total_calls = m.get('TotalCalls')
        if m.get('TotalHoldTime') is not None:
            self.total_hold_time = m.get('TotalHoldTime')
        if m.get('TotalLoggedInTime') is not None:
            self.total_logged_in_time = m.get('TotalLoggedInTime')
        if m.get('TotalOffSiteOnlineTime') is not None:
            self.total_off_site_online_time = m.get('TotalOffSiteOnlineTime')
        if m.get('TotalOfficePhoneOnlineTime') is not None:
            self.total_office_phone_online_time = m.get('TotalOfficePhoneOnlineTime')
        if m.get('TotalOnSiteOnlineTime') is not None:
            self.total_on_site_online_time = m.get('TotalOnSiteOnlineTime')
        if m.get('TotalOutboundScenarioReadyTime') is not None:
            self.total_outbound_scenario_ready_time = m.get('TotalOutboundScenarioReadyTime')
        if m.get('TotalOutboundScenarioTime') is not None:
            self.total_outbound_scenario_time = m.get('TotalOutboundScenarioTime')
        if m.get('TotalReadyTime') is not None:
            self.total_ready_time = m.get('TotalReadyTime')
        if m.get('TotalTalkTime') is not None:
            self.total_talk_time = m.get('TotalTalkTime')
        if m.get('TotalWorkTime') is not None:
            self.total_work_time = m.get('TotalWorkTime')
        return self


class ListHistoricalAgentSkillGroupReportResponseBodyDataList(TeaModel):
    def __init__(
        self,
        agent_id: str = None,
        agent_name: str = None,
        back_2back: ListHistoricalAgentSkillGroupReportResponseBodyDataListBack2Back = None,
        display_id: str = None,
        inbound: ListHistoricalAgentSkillGroupReportResponseBodyDataListInbound = None,
        internal: ListHistoricalAgentSkillGroupReportResponseBodyDataListInternal = None,
        outbound: ListHistoricalAgentSkillGroupReportResponseBodyDataListOutbound = None,
        overall: ListHistoricalAgentSkillGroupReportResponseBodyDataListOverall = None,
        skill_group_id: str = None,
        skill_group_name: str = None,
    ):
        self.agent_id = agent_id
        self.agent_name = agent_name
        self.back_2back = back_2back
        self.display_id = display_id
        self.inbound = inbound
        self.internal = internal
        self.outbound = outbound
        self.overall = overall
        self.skill_group_id = skill_group_id
        self.skill_group_name = skill_group_name

    def validate(self):
        if self.back_2back:
            self.back_2back.validate()
        if self.inbound:
            self.inbound.validate()
        if self.internal:
            self.internal.validate()
        if self.outbound:
            self.outbound.validate()
        if self.overall:
            self.overall.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id
        if self.agent_name is not None:
            result['AgentName'] = self.agent_name
        if self.back_2back is not None:
            result['Back2Back'] = self.back_2back.to_map()
        if self.display_id is not None:
            result['DisplayId'] = self.display_id
        if self.inbound is not None:
            result['Inbound'] = self.inbound.to_map()
        if self.internal is not None:
            result['Internal'] = self.internal.to_map()
        if self.outbound is not None:
            result['Outbound'] = self.outbound.to_map()
        if self.overall is not None:
            result['Overall'] = self.overall.to_map()
        if self.skill_group_id is not None:
            result['SkillGroupId'] = self.skill_group_id
        if self.skill_group_name is not None:
            result['SkillGroupName'] = self.skill_group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')
        if m.get('AgentName') is not None:
            self.agent_name = m.get('AgentName')
        if m.get('Back2Back') is not None:
            temp_model = ListHistoricalAgentSkillGroupReportResponseBodyDataListBack2Back()
            self.back_2back = temp_model.from_map(m['Back2Back'])
        if m.get('DisplayId') is not None:
            self.display_id = m.get('DisplayId')
        if m.get('Inbound') is not None:
            temp_model = ListHistoricalAgentSkillGroupReportResponseBodyDataListInbound()
            self.inbound = temp_model.from_map(m['Inbound'])
        if m.get('Internal') is not None:
            temp_model = ListHistoricalAgentSkillGroupReportResponseBodyDataListInternal()
            self.internal = temp_model.from_map(m['Internal'])
        if m.get('Outbound') is not None:
            temp_model = ListHistoricalAgentSkillGroupReportResponseBodyDataListOutbound()
            self.outbound = temp_model.from_map(m['Outbound'])
        if m.get('Overall') is not None:
            temp_model = ListHistoricalAgentSkillGroupReportResponseBodyDataListOverall()
            self.overall = temp_model.from_map(m['Overall'])
        if m.get('SkillGroupId') is not None:
            self.skill_group_id = m.get('SkillGroupId')
        if m.get('SkillGroupName') is not None:
            self.skill_group_name = m.get('SkillGroupName')
        return self


class ListHistoricalAgentSkillGroupReportResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[ListHistoricalAgentSkillGroupReportResponseBodyDataList] = None,
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
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
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
            for k in m.get('List'):
                temp_model = ListHistoricalAgentSkillGroupReportResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListHistoricalAgentSkillGroupReportResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListHistoricalAgentSkillGroupReportResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ListHistoricalAgentSkillGroupReportResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListHistoricalAgentSkillGroupReportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListHistoricalAgentSkillGroupReportResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListHistoricalAgentSkillGroupReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListIntervalAgentSkillGroupReportRequest(TeaModel):
    def __init__(
        self,
        agent_id: str = None,
        end_time: int = None,
        instance_id: str = None,
        interval: str = None,
        media_type: str = None,
        skill_group_id: str = None,
        start_time: int = None,
    ):
        self.agent_id = agent_id
        self.end_time = end_time
        self.instance_id = instance_id
        self.interval = interval
        self.media_type = media_type
        self.skill_group_id = skill_group_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.media_type is not None:
            result['MediaType'] = self.media_type
        if self.skill_group_id is not None:
            result['SkillGroupId'] = self.skill_group_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')
        if m.get('SkillGroupId') is not None:
            self.skill_group_id = m.get('SkillGroupId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class ListIntervalAgentSkillGroupReportResponseBodyDataBack2Back(TeaModel):
    def __init__(
        self,
        agent_answer_rate: float = None,
        answer_rate: float = None,
        average_customer_ring_time: float = None,
        average_ring_time: float = None,
        average_talk_time: int = None,
        calls_answered: int = None,
        calls_customer_handled: int = None,
        calls_dialed: int = None,
        customer_handle_rate: float = None,
        max_customer_ring_time: int = None,
        max_ring_time: int = None,
        max_talk_time: int = None,
        total_customer_ring_time: int = None,
        total_ring_time: int = None,
        total_talk_time: int = None,
    ):
        self.agent_answer_rate = agent_answer_rate
        self.answer_rate = answer_rate
        self.average_customer_ring_time = average_customer_ring_time
        self.average_ring_time = average_ring_time
        self.average_talk_time = average_talk_time
        self.calls_answered = calls_answered
        self.calls_customer_handled = calls_customer_handled
        self.calls_dialed = calls_dialed
        self.customer_handle_rate = customer_handle_rate
        self.max_customer_ring_time = max_customer_ring_time
        self.max_ring_time = max_ring_time
        self.max_talk_time = max_talk_time
        self.total_customer_ring_time = total_customer_ring_time
        self.total_ring_time = total_ring_time
        self.total_talk_time = total_talk_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_answer_rate is not None:
            result['AgentAnswerRate'] = self.agent_answer_rate
        if self.answer_rate is not None:
            result['AnswerRate'] = self.answer_rate
        if self.average_customer_ring_time is not None:
            result['AverageCustomerRingTime'] = self.average_customer_ring_time
        if self.average_ring_time is not None:
            result['AverageRingTime'] = self.average_ring_time
        if self.average_talk_time is not None:
            result['AverageTalkTime'] = self.average_talk_time
        if self.calls_answered is not None:
            result['CallsAnswered'] = self.calls_answered
        if self.calls_customer_handled is not None:
            result['CallsCustomerHandled'] = self.calls_customer_handled
        if self.calls_dialed is not None:
            result['CallsDialed'] = self.calls_dialed
        if self.customer_handle_rate is not None:
            result['CustomerHandleRate'] = self.customer_handle_rate
        if self.max_customer_ring_time is not None:
            result['MaxCustomerRingTime'] = self.max_customer_ring_time
        if self.max_ring_time is not None:
            result['MaxRingTime'] = self.max_ring_time
        if self.max_talk_time is not None:
            result['MaxTalkTime'] = self.max_talk_time
        if self.total_customer_ring_time is not None:
            result['TotalCustomerRingTime'] = self.total_customer_ring_time
        if self.total_ring_time is not None:
            result['TotalRingTime'] = self.total_ring_time
        if self.total_talk_time is not None:
            result['TotalTalkTime'] = self.total_talk_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentAnswerRate') is not None:
            self.agent_answer_rate = m.get('AgentAnswerRate')
        if m.get('AnswerRate') is not None:
            self.answer_rate = m.get('AnswerRate')
        if m.get('AverageCustomerRingTime') is not None:
            self.average_customer_ring_time = m.get('AverageCustomerRingTime')
        if m.get('AverageRingTime') is not None:
            self.average_ring_time = m.get('AverageRingTime')
        if m.get('AverageTalkTime') is not None:
            self.average_talk_time = m.get('AverageTalkTime')
        if m.get('CallsAnswered') is not None:
            self.calls_answered = m.get('CallsAnswered')
        if m.get('CallsCustomerHandled') is not None:
            self.calls_customer_handled = m.get('CallsCustomerHandled')
        if m.get('CallsDialed') is not None:
            self.calls_dialed = m.get('CallsDialed')
        if m.get('CustomerHandleRate') is not None:
            self.customer_handle_rate = m.get('CustomerHandleRate')
        if m.get('MaxCustomerRingTime') is not None:
            self.max_customer_ring_time = m.get('MaxCustomerRingTime')
        if m.get('MaxRingTime') is not None:
            self.max_ring_time = m.get('MaxRingTime')
        if m.get('MaxTalkTime') is not None:
            self.max_talk_time = m.get('MaxTalkTime')
        if m.get('TotalCustomerRingTime') is not None:
            self.total_customer_ring_time = m.get('TotalCustomerRingTime')
        if m.get('TotalRingTime') is not None:
            self.total_ring_time = m.get('TotalRingTime')
        if m.get('TotalTalkTime') is not None:
            self.total_talk_time = m.get('TotalTalkTime')
        return self


class ListIntervalAgentSkillGroupReportResponseBodyDataInbound(TeaModel):
    def __init__(
        self,
        average_first_response_time: float = None,
        average_hold_time: float = None,
        average_response_time: float = None,
        average_ring_time: float = None,
        average_talk_time: float = None,
        average_work_time: float = None,
        calls_attended_transfer_in: int = None,
        calls_attended_transfer_out: int = None,
        calls_blind_transfer_in: int = None,
        calls_blind_transfer_out: int = None,
        calls_handled: int = None,
        calls_hold: int = None,
        calls_offered: int = None,
        calls_ringed: int = None,
        handle_rate: float = None,
        max_hold_time: int = None,
        max_ring_time: int = None,
        max_talk_time: int = None,
        max_work_time: int = None,
        satisfaction_index: float = None,
        satisfaction_rate: float = None,
        satisfaction_surveys_offered: int = None,
        satisfaction_surveys_responded: int = None,
        total_hold_time: int = None,
        total_messages_sent: int = None,
        total_messages_sent_by_agent: int = None,
        total_messages_sent_by_customer: int = None,
        total_ring_time: int = None,
        total_talk_time: int = None,
        total_work_time: int = None,
    ):
        self.average_first_response_time = average_first_response_time
        self.average_hold_time = average_hold_time
        self.average_response_time = average_response_time
        self.average_ring_time = average_ring_time
        self.average_talk_time = average_talk_time
        self.average_work_time = average_work_time
        self.calls_attended_transfer_in = calls_attended_transfer_in
        self.calls_attended_transfer_out = calls_attended_transfer_out
        self.calls_blind_transfer_in = calls_blind_transfer_in
        self.calls_blind_transfer_out = calls_blind_transfer_out
        self.calls_handled = calls_handled
        self.calls_hold = calls_hold
        self.calls_offered = calls_offered
        self.calls_ringed = calls_ringed
        self.handle_rate = handle_rate
        self.max_hold_time = max_hold_time
        self.max_ring_time = max_ring_time
        self.max_talk_time = max_talk_time
        self.max_work_time = max_work_time
        self.satisfaction_index = satisfaction_index
        self.satisfaction_rate = satisfaction_rate
        self.satisfaction_surveys_offered = satisfaction_surveys_offered
        self.satisfaction_surveys_responded = satisfaction_surveys_responded
        self.total_hold_time = total_hold_time
        self.total_messages_sent = total_messages_sent
        self.total_messages_sent_by_agent = total_messages_sent_by_agent
        self.total_messages_sent_by_customer = total_messages_sent_by_customer
        self.total_ring_time = total_ring_time
        self.total_talk_time = total_talk_time
        self.total_work_time = total_work_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.average_first_response_time is not None:
            result['AverageFirstResponseTime'] = self.average_first_response_time
        if self.average_hold_time is not None:
            result['AverageHoldTime'] = self.average_hold_time
        if self.average_response_time is not None:
            result['AverageResponseTime'] = self.average_response_time
        if self.average_ring_time is not None:
            result['AverageRingTime'] = self.average_ring_time
        if self.average_talk_time is not None:
            result['AverageTalkTime'] = self.average_talk_time
        if self.average_work_time is not None:
            result['AverageWorkTime'] = self.average_work_time
        if self.calls_attended_transfer_in is not None:
            result['CallsAttendedTransferIn'] = self.calls_attended_transfer_in
        if self.calls_attended_transfer_out is not None:
            result['CallsAttendedTransferOut'] = self.calls_attended_transfer_out
        if self.calls_blind_transfer_in is not None:
            result['CallsBlindTransferIn'] = self.calls_blind_transfer_in
        if self.calls_blind_transfer_out is not None:
            result['CallsBlindTransferOut'] = self.calls_blind_transfer_out
        if self.calls_handled is not None:
            result['CallsHandled'] = self.calls_handled
        if self.calls_hold is not None:
            result['CallsHold'] = self.calls_hold
        if self.calls_offered is not None:
            result['CallsOffered'] = self.calls_offered
        if self.calls_ringed is not None:
            result['CallsRinged'] = self.calls_ringed
        if self.handle_rate is not None:
            result['HandleRate'] = self.handle_rate
        if self.max_hold_time is not None:
            result['MaxHoldTime'] = self.max_hold_time
        if self.max_ring_time is not None:
            result['MaxRingTime'] = self.max_ring_time
        if self.max_talk_time is not None:
            result['MaxTalkTime'] = self.max_talk_time
        if self.max_work_time is not None:
            result['MaxWorkTime'] = self.max_work_time
        if self.satisfaction_index is not None:
            result['SatisfactionIndex'] = self.satisfaction_index
        if self.satisfaction_rate is not None:
            result['SatisfactionRate'] = self.satisfaction_rate
        if self.satisfaction_surveys_offered is not None:
            result['SatisfactionSurveysOffered'] = self.satisfaction_surveys_offered
        if self.satisfaction_surveys_responded is not None:
            result['SatisfactionSurveysResponded'] = self.satisfaction_surveys_responded
        if self.total_hold_time is not None:
            result['TotalHoldTime'] = self.total_hold_time
        if self.total_messages_sent is not None:
            result['TotalMessagesSent'] = self.total_messages_sent
        if self.total_messages_sent_by_agent is not None:
            result['TotalMessagesSentByAgent'] = self.total_messages_sent_by_agent
        if self.total_messages_sent_by_customer is not None:
            result['TotalMessagesSentByCustomer'] = self.total_messages_sent_by_customer
        if self.total_ring_time is not None:
            result['TotalRingTime'] = self.total_ring_time
        if self.total_talk_time is not None:
            result['TotalTalkTime'] = self.total_talk_time
        if self.total_work_time is not None:
            result['TotalWorkTime'] = self.total_work_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AverageFirstResponseTime') is not None:
            self.average_first_response_time = m.get('AverageFirstResponseTime')
        if m.get('AverageHoldTime') is not None:
            self.average_hold_time = m.get('AverageHoldTime')
        if m.get('AverageResponseTime') is not None:
            self.average_response_time = m.get('AverageResponseTime')
        if m.get('AverageRingTime') is not None:
            self.average_ring_time = m.get('AverageRingTime')
        if m.get('AverageTalkTime') is not None:
            self.average_talk_time = m.get('AverageTalkTime')
        if m.get('AverageWorkTime') is not None:
            self.average_work_time = m.get('AverageWorkTime')
        if m.get('CallsAttendedTransferIn') is not None:
            self.calls_attended_transfer_in = m.get('CallsAttendedTransferIn')
        if m.get('CallsAttendedTransferOut') is not None:
            self.calls_attended_transfer_out = m.get('CallsAttendedTransferOut')
        if m.get('CallsBlindTransferIn') is not None:
            self.calls_blind_transfer_in = m.get('CallsBlindTransferIn')
        if m.get('CallsBlindTransferOut') is not None:
            self.calls_blind_transfer_out = m.get('CallsBlindTransferOut')
        if m.get('CallsHandled') is not None:
            self.calls_handled = m.get('CallsHandled')
        if m.get('CallsHold') is not None:
            self.calls_hold = m.get('CallsHold')
        if m.get('CallsOffered') is not None:
            self.calls_offered = m.get('CallsOffered')
        if m.get('CallsRinged') is not None:
            self.calls_ringed = m.get('CallsRinged')
        if m.get('HandleRate') is not None:
            self.handle_rate = m.get('HandleRate')
        if m.get('MaxHoldTime') is not None:
            self.max_hold_time = m.get('MaxHoldTime')
        if m.get('MaxRingTime') is not None:
            self.max_ring_time = m.get('MaxRingTime')
        if m.get('MaxTalkTime') is not None:
            self.max_talk_time = m.get('MaxTalkTime')
        if m.get('MaxWorkTime') is not None:
            self.max_work_time = m.get('MaxWorkTime')
        if m.get('SatisfactionIndex') is not None:
            self.satisfaction_index = m.get('SatisfactionIndex')
        if m.get('SatisfactionRate') is not None:
            self.satisfaction_rate = m.get('SatisfactionRate')
        if m.get('SatisfactionSurveysOffered') is not None:
            self.satisfaction_surveys_offered = m.get('SatisfactionSurveysOffered')
        if m.get('SatisfactionSurveysResponded') is not None:
            self.satisfaction_surveys_responded = m.get('SatisfactionSurveysResponded')
        if m.get('TotalHoldTime') is not None:
            self.total_hold_time = m.get('TotalHoldTime')
        if m.get('TotalMessagesSent') is not None:
            self.total_messages_sent = m.get('TotalMessagesSent')
        if m.get('TotalMessagesSentByAgent') is not None:
            self.total_messages_sent_by_agent = m.get('TotalMessagesSentByAgent')
        if m.get('TotalMessagesSentByCustomer') is not None:
            self.total_messages_sent_by_customer = m.get('TotalMessagesSentByCustomer')
        if m.get('TotalRingTime') is not None:
            self.total_ring_time = m.get('TotalRingTime')
        if m.get('TotalTalkTime') is not None:
            self.total_talk_time = m.get('TotalTalkTime')
        if m.get('TotalWorkTime') is not None:
            self.total_work_time = m.get('TotalWorkTime')
        return self


class ListIntervalAgentSkillGroupReportResponseBodyDataInternal(TeaModel):
    def __init__(
        self,
        average_talk_time: float = None,
        calls_answered: int = None,
        calls_dialed: int = None,
        calls_handled: int = None,
        calls_offered: int = None,
        calls_talk: int = None,
        max_talk_time: int = None,
        total_talk_time: int = None,
    ):
        self.average_talk_time = average_talk_time
        self.calls_answered = calls_answered
        self.calls_dialed = calls_dialed
        self.calls_handled = calls_handled
        self.calls_offered = calls_offered
        self.calls_talk = calls_talk
        self.max_talk_time = max_talk_time
        self.total_talk_time = total_talk_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.average_talk_time is not None:
            result['AverageTalkTime'] = self.average_talk_time
        if self.calls_answered is not None:
            result['CallsAnswered'] = self.calls_answered
        if self.calls_dialed is not None:
            result['CallsDialed'] = self.calls_dialed
        if self.calls_handled is not None:
            result['CallsHandled'] = self.calls_handled
        if self.calls_offered is not None:
            result['CallsOffered'] = self.calls_offered
        if self.calls_talk is not None:
            result['CallsTalk'] = self.calls_talk
        if self.max_talk_time is not None:
            result['MaxTalkTime'] = self.max_talk_time
        if self.total_talk_time is not None:
            result['TotalTalkTime'] = self.total_talk_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AverageTalkTime') is not None:
            self.average_talk_time = m.get('AverageTalkTime')
        if m.get('CallsAnswered') is not None:
            self.calls_answered = m.get('CallsAnswered')
        if m.get('CallsDialed') is not None:
            self.calls_dialed = m.get('CallsDialed')
        if m.get('CallsHandled') is not None:
            self.calls_handled = m.get('CallsHandled')
        if m.get('CallsOffered') is not None:
            self.calls_offered = m.get('CallsOffered')
        if m.get('CallsTalk') is not None:
            self.calls_talk = m.get('CallsTalk')
        if m.get('MaxTalkTime') is not None:
            self.max_talk_time = m.get('MaxTalkTime')
        if m.get('TotalTalkTime') is not None:
            self.total_talk_time = m.get('TotalTalkTime')
        return self


class ListIntervalAgentSkillGroupReportResponseBodyDataOutbound(TeaModel):
    def __init__(
        self,
        answer_rate: float = None,
        average_dialing_time: float = None,
        average_hold_time: float = None,
        average_ring_time: float = None,
        average_talk_time: float = None,
        average_work_time: float = None,
        calls_answered: int = None,
        calls_attended_transfer_in: int = None,
        calls_attended_transfer_out: int = None,
        calls_blind_transfer_in: int = None,
        calls_blind_transfer_out: int = None,
        calls_dialed: int = None,
        calls_hold: int = None,
        calls_ringed: int = None,
        max_dialing_time: int = None,
        max_hold_time: int = None,
        max_ring_time: int = None,
        max_talk_time: int = None,
        max_work_time: int = None,
        satisfaction_index: float = None,
        satisfaction_rate: float = None,
        satisfaction_surveys_offered: int = None,
        satisfaction_surveys_responded: int = None,
        total_dialing_time: int = None,
        total_hold_time: int = None,
        total_ring_time: int = None,
        total_talk_time: int = None,
        total_work_time: int = None,
    ):
        self.answer_rate = answer_rate
        self.average_dialing_time = average_dialing_time
        self.average_hold_time = average_hold_time
        self.average_ring_time = average_ring_time
        self.average_talk_time = average_talk_time
        self.average_work_time = average_work_time
        self.calls_answered = calls_answered
        self.calls_attended_transfer_in = calls_attended_transfer_in
        self.calls_attended_transfer_out = calls_attended_transfer_out
        self.calls_blind_transfer_in = calls_blind_transfer_in
        self.calls_blind_transfer_out = calls_blind_transfer_out
        self.calls_dialed = calls_dialed
        self.calls_hold = calls_hold
        self.calls_ringed = calls_ringed
        self.max_dialing_time = max_dialing_time
        self.max_hold_time = max_hold_time
        self.max_ring_time = max_ring_time
        self.max_talk_time = max_talk_time
        self.max_work_time = max_work_time
        self.satisfaction_index = satisfaction_index
        self.satisfaction_rate = satisfaction_rate
        self.satisfaction_surveys_offered = satisfaction_surveys_offered
        self.satisfaction_surveys_responded = satisfaction_surveys_responded
        self.total_dialing_time = total_dialing_time
        self.total_hold_time = total_hold_time
        self.total_ring_time = total_ring_time
        self.total_talk_time = total_talk_time
        self.total_work_time = total_work_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.answer_rate is not None:
            result['AnswerRate'] = self.answer_rate
        if self.average_dialing_time is not None:
            result['AverageDialingTime'] = self.average_dialing_time
        if self.average_hold_time is not None:
            result['AverageHoldTime'] = self.average_hold_time
        if self.average_ring_time is not None:
            result['AverageRingTime'] = self.average_ring_time
        if self.average_talk_time is not None:
            result['AverageTalkTime'] = self.average_talk_time
        if self.average_work_time is not None:
            result['AverageWorkTime'] = self.average_work_time
        if self.calls_answered is not None:
            result['CallsAnswered'] = self.calls_answered
        if self.calls_attended_transfer_in is not None:
            result['CallsAttendedTransferIn'] = self.calls_attended_transfer_in
        if self.calls_attended_transfer_out is not None:
            result['CallsAttendedTransferOut'] = self.calls_attended_transfer_out
        if self.calls_blind_transfer_in is not None:
            result['CallsBlindTransferIn'] = self.calls_blind_transfer_in
        if self.calls_blind_transfer_out is not None:
            result['CallsBlindTransferOut'] = self.calls_blind_transfer_out
        if self.calls_dialed is not None:
            result['CallsDialed'] = self.calls_dialed
        if self.calls_hold is not None:
            result['CallsHold'] = self.calls_hold
        if self.calls_ringed is not None:
            result['CallsRinged'] = self.calls_ringed
        if self.max_dialing_time is not None:
            result['MaxDialingTime'] = self.max_dialing_time
        if self.max_hold_time is not None:
            result['MaxHoldTime'] = self.max_hold_time
        if self.max_ring_time is not None:
            result['MaxRingTime'] = self.max_ring_time
        if self.max_talk_time is not None:
            result['MaxTalkTime'] = self.max_talk_time
        if self.max_work_time is not None:
            result['MaxWorkTime'] = self.max_work_time
        if self.satisfaction_index is not None:
            result['SatisfactionIndex'] = self.satisfaction_index
        if self.satisfaction_rate is not None:
            result['SatisfactionRate'] = self.satisfaction_rate
        if self.satisfaction_surveys_offered is not None:
            result['SatisfactionSurveysOffered'] = self.satisfaction_surveys_offered
        if self.satisfaction_surveys_responded is not None:
            result['SatisfactionSurveysResponded'] = self.satisfaction_surveys_responded
        if self.total_dialing_time is not None:
            result['TotalDialingTime'] = self.total_dialing_time
        if self.total_hold_time is not None:
            result['TotalHoldTime'] = self.total_hold_time
        if self.total_ring_time is not None:
            result['TotalRingTime'] = self.total_ring_time
        if self.total_talk_time is not None:
            result['TotalTalkTime'] = self.total_talk_time
        if self.total_work_time is not None:
            result['TotalWorkTime'] = self.total_work_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnswerRate') is not None:
            self.answer_rate = m.get('AnswerRate')
        if m.get('AverageDialingTime') is not None:
            self.average_dialing_time = m.get('AverageDialingTime')
        if m.get('AverageHoldTime') is not None:
            self.average_hold_time = m.get('AverageHoldTime')
        if m.get('AverageRingTime') is not None:
            self.average_ring_time = m.get('AverageRingTime')
        if m.get('AverageTalkTime') is not None:
            self.average_talk_time = m.get('AverageTalkTime')
        if m.get('AverageWorkTime') is not None:
            self.average_work_time = m.get('AverageWorkTime')
        if m.get('CallsAnswered') is not None:
            self.calls_answered = m.get('CallsAnswered')
        if m.get('CallsAttendedTransferIn') is not None:
            self.calls_attended_transfer_in = m.get('CallsAttendedTransferIn')
        if m.get('CallsAttendedTransferOut') is not None:
            self.calls_attended_transfer_out = m.get('CallsAttendedTransferOut')
        if m.get('CallsBlindTransferIn') is not None:
            self.calls_blind_transfer_in = m.get('CallsBlindTransferIn')
        if m.get('CallsBlindTransferOut') is not None:
            self.calls_blind_transfer_out = m.get('CallsBlindTransferOut')
        if m.get('CallsDialed') is not None:
            self.calls_dialed = m.get('CallsDialed')
        if m.get('CallsHold') is not None:
            self.calls_hold = m.get('CallsHold')
        if m.get('CallsRinged') is not None:
            self.calls_ringed = m.get('CallsRinged')
        if m.get('MaxDialingTime') is not None:
            self.max_dialing_time = m.get('MaxDialingTime')
        if m.get('MaxHoldTime') is not None:
            self.max_hold_time = m.get('MaxHoldTime')
        if m.get('MaxRingTime') is not None:
            self.max_ring_time = m.get('MaxRingTime')
        if m.get('MaxTalkTime') is not None:
            self.max_talk_time = m.get('MaxTalkTime')
        if m.get('MaxWorkTime') is not None:
            self.max_work_time = m.get('MaxWorkTime')
        if m.get('SatisfactionIndex') is not None:
            self.satisfaction_index = m.get('SatisfactionIndex')
        if m.get('SatisfactionRate') is not None:
            self.satisfaction_rate = m.get('SatisfactionRate')
        if m.get('SatisfactionSurveysOffered') is not None:
            self.satisfaction_surveys_offered = m.get('SatisfactionSurveysOffered')
        if m.get('SatisfactionSurveysResponded') is not None:
            self.satisfaction_surveys_responded = m.get('SatisfactionSurveysResponded')
        if m.get('TotalDialingTime') is not None:
            self.total_dialing_time = m.get('TotalDialingTime')
        if m.get('TotalHoldTime') is not None:
            self.total_hold_time = m.get('TotalHoldTime')
        if m.get('TotalRingTime') is not None:
            self.total_ring_time = m.get('TotalRingTime')
        if m.get('TotalTalkTime') is not None:
            self.total_talk_time = m.get('TotalTalkTime')
        if m.get('TotalWorkTime') is not None:
            self.total_work_time = m.get('TotalWorkTime')
        return self


class ListIntervalAgentSkillGroupReportResponseBodyDataOverallBreakCodeDetailList(TeaModel):
    def __init__(
        self,
        break_code: str = None,
        count: int = None,
        duration: int = None,
    ):
        self.break_code = break_code
        self.count = count
        self.duration = duration

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.break_code is not None:
            result['BreakCode'] = self.break_code
        if self.count is not None:
            result['Count'] = self.count
        if self.duration is not None:
            result['Duration'] = self.duration
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BreakCode') is not None:
            self.break_code = m.get('BreakCode')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        return self


class ListIntervalAgentSkillGroupReportResponseBodyDataOverall(TeaModel):
    def __init__(
        self,
        average_break_time: float = None,
        average_hold_time: float = None,
        average_ready_time: float = None,
        average_talk_time: float = None,
        average_work_time: float = None,
        break_code_detail_list: List[ListIntervalAgentSkillGroupReportResponseBodyDataOverallBreakCodeDetailList] = None,
        first_check_in_time: int = None,
        last_checkout_time: int = None,
        max_break_time: int = None,
        max_hold_time: int = None,
        max_ready_time: int = None,
        max_talk_time: int = None,
        max_work_time: int = None,
        occupancy_rate: float = None,
        satisfaction_index: float = None,
        satisfaction_rate: float = None,
        satisfaction_surveys_offered: int = None,
        satisfaction_surveys_responded: int = None,
        total_break_time: int = None,
        total_calls: int = None,
        total_hold_time: int = None,
        total_logged_in_time: int = None,
        total_off_site_online_time: int = None,
        total_office_phone_online_time: int = None,
        total_on_site_online_time: int = None,
        total_outbound_scenario_ready_time: int = None,
        total_outbound_scenario_time: int = None,
        total_ready_time: int = None,
        total_talk_time: int = None,
        total_work_time: int = None,
    ):
        self.average_break_time = average_break_time
        self.average_hold_time = average_hold_time
        self.average_ready_time = average_ready_time
        self.average_talk_time = average_talk_time
        self.average_work_time = average_work_time
        self.break_code_detail_list = break_code_detail_list
        self.first_check_in_time = first_check_in_time
        self.last_checkout_time = last_checkout_time
        self.max_break_time = max_break_time
        self.max_hold_time = max_hold_time
        self.max_ready_time = max_ready_time
        self.max_talk_time = max_talk_time
        self.max_work_time = max_work_time
        self.occupancy_rate = occupancy_rate
        self.satisfaction_index = satisfaction_index
        self.satisfaction_rate = satisfaction_rate
        self.satisfaction_surveys_offered = satisfaction_surveys_offered
        self.satisfaction_surveys_responded = satisfaction_surveys_responded
        self.total_break_time = total_break_time
        self.total_calls = total_calls
        self.total_hold_time = total_hold_time
        self.total_logged_in_time = total_logged_in_time
        self.total_off_site_online_time = total_off_site_online_time
        self.total_office_phone_online_time = total_office_phone_online_time
        self.total_on_site_online_time = total_on_site_online_time
        self.total_outbound_scenario_ready_time = total_outbound_scenario_ready_time
        self.total_outbound_scenario_time = total_outbound_scenario_time
        self.total_ready_time = total_ready_time
        self.total_talk_time = total_talk_time
        self.total_work_time = total_work_time

    def validate(self):
        if self.break_code_detail_list:
            for k in self.break_code_detail_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.average_break_time is not None:
            result['AverageBreakTime'] = self.average_break_time
        if self.average_hold_time is not None:
            result['AverageHoldTime'] = self.average_hold_time
        if self.average_ready_time is not None:
            result['AverageReadyTime'] = self.average_ready_time
        if self.average_talk_time is not None:
            result['AverageTalkTime'] = self.average_talk_time
        if self.average_work_time is not None:
            result['AverageWorkTime'] = self.average_work_time
        result['BreakCodeDetailList'] = []
        if self.break_code_detail_list is not None:
            for k in self.break_code_detail_list:
                result['BreakCodeDetailList'].append(k.to_map() if k else None)
        if self.first_check_in_time is not None:
            result['FirstCheckInTime'] = self.first_check_in_time
        if self.last_checkout_time is not None:
            result['LastCheckoutTime'] = self.last_checkout_time
        if self.max_break_time is not None:
            result['MaxBreakTime'] = self.max_break_time
        if self.max_hold_time is not None:
            result['MaxHoldTime'] = self.max_hold_time
        if self.max_ready_time is not None:
            result['MaxReadyTime'] = self.max_ready_time
        if self.max_talk_time is not None:
            result['MaxTalkTime'] = self.max_talk_time
        if self.max_work_time is not None:
            result['MaxWorkTime'] = self.max_work_time
        if self.occupancy_rate is not None:
            result['OccupancyRate'] = self.occupancy_rate
        if self.satisfaction_index is not None:
            result['SatisfactionIndex'] = self.satisfaction_index
        if self.satisfaction_rate is not None:
            result['SatisfactionRate'] = self.satisfaction_rate
        if self.satisfaction_surveys_offered is not None:
            result['SatisfactionSurveysOffered'] = self.satisfaction_surveys_offered
        if self.satisfaction_surveys_responded is not None:
            result['SatisfactionSurveysResponded'] = self.satisfaction_surveys_responded
        if self.total_break_time is not None:
            result['TotalBreakTime'] = self.total_break_time
        if self.total_calls is not None:
            result['TotalCalls'] = self.total_calls
        if self.total_hold_time is not None:
            result['TotalHoldTime'] = self.total_hold_time
        if self.total_logged_in_time is not None:
            result['TotalLoggedInTime'] = self.total_logged_in_time
        if self.total_off_site_online_time is not None:
            result['TotalOffSiteOnlineTime'] = self.total_off_site_online_time
        if self.total_office_phone_online_time is not None:
            result['TotalOfficePhoneOnlineTime'] = self.total_office_phone_online_time
        if self.total_on_site_online_time is not None:
            result['TotalOnSiteOnlineTime'] = self.total_on_site_online_time
        if self.total_outbound_scenario_ready_time is not None:
            result['TotalOutboundScenarioReadyTime'] = self.total_outbound_scenario_ready_time
        if self.total_outbound_scenario_time is not None:
            result['TotalOutboundScenarioTime'] = self.total_outbound_scenario_time
        if self.total_ready_time is not None:
            result['TotalReadyTime'] = self.total_ready_time
        if self.total_talk_time is not None:
            result['TotalTalkTime'] = self.total_talk_time
        if self.total_work_time is not None:
            result['TotalWorkTime'] = self.total_work_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AverageBreakTime') is not None:
            self.average_break_time = m.get('AverageBreakTime')
        if m.get('AverageHoldTime') is not None:
            self.average_hold_time = m.get('AverageHoldTime')
        if m.get('AverageReadyTime') is not None:
            self.average_ready_time = m.get('AverageReadyTime')
        if m.get('AverageTalkTime') is not None:
            self.average_talk_time = m.get('AverageTalkTime')
        if m.get('AverageWorkTime') is not None:
            self.average_work_time = m.get('AverageWorkTime')
        self.break_code_detail_list = []
        if m.get('BreakCodeDetailList') is not None:
            for k in m.get('BreakCodeDetailList'):
                temp_model = ListIntervalAgentSkillGroupReportResponseBodyDataOverallBreakCodeDetailList()
                self.break_code_detail_list.append(temp_model.from_map(k))
        if m.get('FirstCheckInTime') is not None:
            self.first_check_in_time = m.get('FirstCheckInTime')
        if m.get('LastCheckoutTime') is not None:
            self.last_checkout_time = m.get('LastCheckoutTime')
        if m.get('MaxBreakTime') is not None:
            self.max_break_time = m.get('MaxBreakTime')
        if m.get('MaxHoldTime') is not None:
            self.max_hold_time = m.get('MaxHoldTime')
        if m.get('MaxReadyTime') is not None:
            self.max_ready_time = m.get('MaxReadyTime')
        if m.get('MaxTalkTime') is not None:
            self.max_talk_time = m.get('MaxTalkTime')
        if m.get('MaxWorkTime') is not None:
            self.max_work_time = m.get('MaxWorkTime')
        if m.get('OccupancyRate') is not None:
            self.occupancy_rate = m.get('OccupancyRate')
        if m.get('SatisfactionIndex') is not None:
            self.satisfaction_index = m.get('SatisfactionIndex')
        if m.get('SatisfactionRate') is not None:
            self.satisfaction_rate = m.get('SatisfactionRate')
        if m.get('SatisfactionSurveysOffered') is not None:
            self.satisfaction_surveys_offered = m.get('SatisfactionSurveysOffered')
        if m.get('SatisfactionSurveysResponded') is not None:
            self.satisfaction_surveys_responded = m.get('SatisfactionSurveysResponded')
        if m.get('TotalBreakTime') is not None:
            self.total_break_time = m.get('TotalBreakTime')
        if m.get('TotalCalls') is not None:
            self.total_calls = m.get('TotalCalls')
        if m.get('TotalHoldTime') is not None:
            self.total_hold_time = m.get('TotalHoldTime')
        if m.get('TotalLoggedInTime') is not None:
            self.total_logged_in_time = m.get('TotalLoggedInTime')
        if m.get('TotalOffSiteOnlineTime') is not None:
            self.total_off_site_online_time = m.get('TotalOffSiteOnlineTime')
        if m.get('TotalOfficePhoneOnlineTime') is not None:
            self.total_office_phone_online_time = m.get('TotalOfficePhoneOnlineTime')
        if m.get('TotalOnSiteOnlineTime') is not None:
            self.total_on_site_online_time = m.get('TotalOnSiteOnlineTime')
        if m.get('TotalOutboundScenarioReadyTime') is not None:
            self.total_outbound_scenario_ready_time = m.get('TotalOutboundScenarioReadyTime')
        if m.get('TotalOutboundScenarioTime') is not None:
            self.total_outbound_scenario_time = m.get('TotalOutboundScenarioTime')
        if m.get('TotalReadyTime') is not None:
            self.total_ready_time = m.get('TotalReadyTime')
        if m.get('TotalTalkTime') is not None:
            self.total_talk_time = m.get('TotalTalkTime')
        if m.get('TotalWorkTime') is not None:
            self.total_work_time = m.get('TotalWorkTime')
        return self


class ListIntervalAgentSkillGroupReportResponseBodyData(TeaModel):
    def __init__(
        self,
        back_2back: ListIntervalAgentSkillGroupReportResponseBodyDataBack2Back = None,
        inbound: ListIntervalAgentSkillGroupReportResponseBodyDataInbound = None,
        internal: ListIntervalAgentSkillGroupReportResponseBodyDataInternal = None,
        outbound: ListIntervalAgentSkillGroupReportResponseBodyDataOutbound = None,
        overall: ListIntervalAgentSkillGroupReportResponseBodyDataOverall = None,
        stats_time: int = None,
    ):
        self.back_2back = back_2back
        self.inbound = inbound
        self.internal = internal
        self.outbound = outbound
        self.overall = overall
        self.stats_time = stats_time

    def validate(self):
        if self.back_2back:
            self.back_2back.validate()
        if self.inbound:
            self.inbound.validate()
        if self.internal:
            self.internal.validate()
        if self.outbound:
            self.outbound.validate()
        if self.overall:
            self.overall.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.back_2back is not None:
            result['Back2Back'] = self.back_2back.to_map()
        if self.inbound is not None:
            result['Inbound'] = self.inbound.to_map()
        if self.internal is not None:
            result['Internal'] = self.internal.to_map()
        if self.outbound is not None:
            result['Outbound'] = self.outbound.to_map()
        if self.overall is not None:
            result['Overall'] = self.overall.to_map()
        if self.stats_time is not None:
            result['StatsTime'] = self.stats_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Back2Back') is not None:
            temp_model = ListIntervalAgentSkillGroupReportResponseBodyDataBack2Back()
            self.back_2back = temp_model.from_map(m['Back2Back'])
        if m.get('Inbound') is not None:
            temp_model = ListIntervalAgentSkillGroupReportResponseBodyDataInbound()
            self.inbound = temp_model.from_map(m['Inbound'])
        if m.get('Internal') is not None:
            temp_model = ListIntervalAgentSkillGroupReportResponseBodyDataInternal()
            self.internal = temp_model.from_map(m['Internal'])
        if m.get('Outbound') is not None:
            temp_model = ListIntervalAgentSkillGroupReportResponseBodyDataOutbound()
            self.outbound = temp_model.from_map(m['Outbound'])
        if m.get('Overall') is not None:
            temp_model = ListIntervalAgentSkillGroupReportResponseBodyDataOverall()
            self.overall = temp_model.from_map(m['Overall'])
        if m.get('StatsTime') is not None:
            self.stats_time = m.get('StatsTime')
        return self


class ListIntervalAgentSkillGroupReportResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ListIntervalAgentSkillGroupReportResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListIntervalAgentSkillGroupReportResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListIntervalAgentSkillGroupReportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListIntervalAgentSkillGroupReportResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListIntervalAgentSkillGroupReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMonoRecordingsRequest(TeaModel):
    def __init__(
        self,
        contact_id: str = None,
        instance_id: str = None,
    ):
        self.contact_id = contact_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ListMonoRecordingsResponseBodyData(TeaModel):
    def __init__(
        self,
        agent_id: str = None,
        agent_name: str = None,
        contact_id: str = None,
        duration: str = None,
        file_name: str = None,
        file_url: str = None,
        ram_id: str = None,
        skill_group_id: str = None,
        start_time: str = None,
    ):
        self.agent_id = agent_id
        self.agent_name = agent_name
        self.contact_id = contact_id
        self.duration = duration
        self.file_name = file_name
        self.file_url = file_url
        self.ram_id = ram_id
        self.skill_group_id = skill_group_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id
        if self.agent_name is not None:
            result['AgentName'] = self.agent_name
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.ram_id is not None:
            result['RamId'] = self.ram_id
        if self.skill_group_id is not None:
            result['SkillGroupId'] = self.skill_group_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')
        if m.get('AgentName') is not None:
            self.agent_name = m.get('AgentName')
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('RamId') is not None:
            self.ram_id = m.get('RamId')
        if m.get('SkillGroupId') is not None:
            self.skill_group_id = m.get('SkillGroupId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class ListMonoRecordingsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ListMonoRecordingsResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListMonoRecordingsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListMonoRecordingsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListMonoRecordingsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListMonoRecordingsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PauseCampaignRequest(TeaModel):
    def __init__(
        self,
        campaign_id: str = None,
        instance_id: str = None,
    ):
        self.campaign_id = campaign_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.campaign_id is not None:
            result['CampaignId'] = self.campaign_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CampaignId') is not None:
            self.campaign_id = m.get('CampaignId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class PauseCampaignResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class PauseCampaignResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PauseCampaignResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = PauseCampaignResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReplaceMigrationAvailableNumbersRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        operator_name: str = None,
        operator_uid: int = None,
        v_1numbers: str = None,
        v_2numbers: str = None,
    ):
        self.instance_id = instance_id
        self.operator_name = operator_name
        self.operator_uid = operator_uid
        self.v_1numbers = v_1numbers
        self.v_2numbers = v_2numbers

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.operator_name is not None:
            result['OperatorName'] = self.operator_name
        if self.operator_uid is not None:
            result['OperatorUid'] = self.operator_uid
        if self.v_1numbers is not None:
            result['V1Numbers'] = self.v_1numbers
        if self.v_2numbers is not None:
            result['V2Numbers'] = self.v_2numbers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OperatorName') is not None:
            self.operator_name = m.get('OperatorName')
        if m.get('OperatorUid') is not None:
            self.operator_uid = m.get('OperatorUid')
        if m.get('V1Numbers') is not None:
            self.v_1numbers = m.get('V1Numbers')
        if m.get('V2Numbers') is not None:
            self.v_2numbers = m.get('V2Numbers')
        return self


class ReplaceMigrationAvailableNumbersResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ReplaceMigrationAvailableNumbersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReplaceMigrationAvailableNumbersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ReplaceMigrationAvailableNumbersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResumeCampaignRequest(TeaModel):
    def __init__(
        self,
        campaign_id: str = None,
        instance_id: str = None,
    ):
        self.campaign_id = campaign_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.campaign_id is not None:
            result['CampaignId'] = self.campaign_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CampaignId') is not None:
            self.campaign_id = m.get('CampaignId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ResumeCampaignResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ResumeCampaignResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ResumeCampaignResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ResumeCampaignResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveRTCStatsV2Request(TeaModel):
    def __init__(
        self,
        call_id: str = None,
        general_info: str = None,
        goog_address: str = None,
        instance_id: str = None,
        receiver_report: str = None,
        sender_report: str = None,
    ):
        self.call_id = call_id
        self.general_info = general_info
        self.goog_address = goog_address
        self.instance_id = instance_id
        self.receiver_report = receiver_report
        self.sender_report = sender_report

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_id is not None:
            result['CallId'] = self.call_id
        if self.general_info is not None:
            result['GeneralInfo'] = self.general_info
        if self.goog_address is not None:
            result['GoogAddress'] = self.goog_address
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.receiver_report is not None:
            result['ReceiverReport'] = self.receiver_report
        if self.sender_report is not None:
            result['SenderReport'] = self.sender_report
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')
        if m.get('GeneralInfo') is not None:
            self.general_info = m.get('GeneralInfo')
        if m.get('GoogAddress') is not None:
            self.goog_address = m.get('GoogAddress')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ReceiverReport') is not None:
            self.receiver_report = m.get('ReceiverReport')
        if m.get('SenderReport') is not None:
            self.sender_report = m.get('SenderReport')
        return self


class SaveRTCStatsV2ResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        row_count: int = None,
        success: bool = None,
        time_stamp: int = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.row_count = row_count
        self.success = success
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.row_count is not None:
            result['RowCount'] = self.row_count
        if self.success is not None:
            result['Success'] = self.success
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RowCount') is not None:
            self.row_count = m.get('RowCount')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class SaveRTCStatsV2Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SaveRTCStatsV2ResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SaveRTCStatsV2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveTerminalLogRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        call_id: str = None,
        content: str = None,
        data_type: int = None,
        instance_id: str = None,
        job_id: str = None,
        method_name: str = None,
        status: str = None,
        unique_request_id: str = None,
    ):
        self.app_name = app_name
        self.call_id = call_id
        self.content = content
        self.data_type = data_type
        self.instance_id = instance_id
        self.job_id = job_id
        self.method_name = method_name
        self.status = status
        self.unique_request_id = unique_request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.call_id is not None:
            result['CallId'] = self.call_id
        if self.content is not None:
            result['Content'] = self.content
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.method_name is not None:
            result['MethodName'] = self.method_name
        if self.status is not None:
            result['Status'] = self.status
        if self.unique_request_id is not None:
            result['UniqueRequestId'] = self.unique_request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('MethodName') is not None:
            self.method_name = m.get('MethodName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UniqueRequestId') is not None:
            self.unique_request_id = m.get('UniqueRequestId')
        return self


class SaveTerminalLogResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        time_stamp: int = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class SaveTerminalLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SaveTerminalLogResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SaveTerminalLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveWebRtcInfoRequest(TeaModel):
    def __init__(
        self,
        call_id: str = None,
        content: str = None,
        content_type: str = None,
        instance_id: str = None,
        job_id: str = None,
    ):
        self.call_id = call_id
        self.content = content
        self.content_type = content_type
        self.instance_id = instance_id
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_id is not None:
            result['CallId'] = self.call_id
        if self.content is not None:
            result['Content'] = self.content
        if self.content_type is not None:
            result['ContentType'] = self.content_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class SaveWebRtcInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        row_count: int = None,
        success: bool = None,
        time_stamp: int = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.row_count = row_count
        self.success = success
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.row_count is not None:
            result['RowCount'] = self.row_count
        if self.success is not None:
            result['Success'] = self.success
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RowCount') is not None:
            self.row_count = m.get('RowCount')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class SaveWebRtcInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SaveWebRtcInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SaveWebRtcInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitCampaignRequest(TeaModel):
    def __init__(
        self,
        campaign_id: str = None,
        instance_id: str = None,
    ):
        self.campaign_id = campaign_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.campaign_id is not None:
            result['CampaignId'] = self.campaign_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CampaignId') is not None:
            self.campaign_id = m.get('CampaignId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class SubmitCampaignResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SubmitCampaignResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitCampaignResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SubmitCampaignResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnregisterDeviceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        user_id: str = None,
    ):
        self.instance_id = instance_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class UnregisterDeviceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UnregisterDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UnregisterDeviceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UnregisterDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


