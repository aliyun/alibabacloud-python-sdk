# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ccc20200701 import models as main_models
from darabonba.model import DaraModel

class ListLegacyAgentStatusLogsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListLegacyAgentStatusLogsResponseBodyData = None,
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
            temp_model = main_models.ListLegacyAgentStatusLogsResponseBodyData()
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

class ListLegacyAgentStatusLogsResponseBodyData(DaraModel):
    def __init__(
        self,
        list: List[main_models.ListLegacyAgentStatusLogsResponseBodyDataList] = None,
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
                temp_model = main_models.ListLegacyAgentStatusLogsResponseBodyDataList()
                self.list.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListLegacyAgentStatusLogsResponseBodyDataList(DaraModel):
    def __init__(
        self,
        agent_drop_call: str = None,
        agent_no: str = None,
        ali_hangup_cause: str = None,
        call_dir: str = None,
        call_id: str = None,
        call_type: str = None,
        callee_id: str = None,
        caller_id: str = None,
        conn_id: str = None,
        extend_1: str = None,
        extend_2: str = None,
        extend_3: str = None,
        extend_4: str = None,
        group_no: str = None,
        monited_agent_no: str = None,
        monited_agent_phone_no: str = None,
        outbound_scenario: bool = None,
        phone_no: str = None,
        statistic_date: str = None,
        statistic_time: int = None,
        status: str = None,
        target_request: str = None,
        target_select: str = None,
        tenant_id: str = None,
        transfer_no: str = None,
        transfer_number: str = None,
    ):
        self.agent_drop_call = agent_drop_call
        self.agent_no = agent_no
        self.ali_hangup_cause = ali_hangup_cause
        self.call_dir = call_dir
        self.call_id = call_id
        self.call_type = call_type
        self.callee_id = callee_id
        self.caller_id = caller_id
        self.conn_id = conn_id
        self.extend_1 = extend_1
        self.extend_2 = extend_2
        self.extend_3 = extend_3
        self.extend_4 = extend_4
        self.group_no = group_no
        self.monited_agent_no = monited_agent_no
        self.monited_agent_phone_no = monited_agent_phone_no
        self.outbound_scenario = outbound_scenario
        self.phone_no = phone_no
        self.statistic_date = statistic_date
        self.statistic_time = statistic_time
        self.status = status
        self.target_request = target_request
        self.target_select = target_select
        self.tenant_id = tenant_id
        self.transfer_no = transfer_no
        self.transfer_number = transfer_number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_drop_call is not None:
            result['AgentDropCall'] = self.agent_drop_call

        if self.agent_no is not None:
            result['AgentNo'] = self.agent_no

        if self.ali_hangup_cause is not None:
            result['AliHangupCause'] = self.ali_hangup_cause

        if self.call_dir is not None:
            result['CallDir'] = self.call_dir

        if self.call_id is not None:
            result['CallId'] = self.call_id

        if self.call_type is not None:
            result['CallType'] = self.call_type

        if self.callee_id is not None:
            result['CalleeId'] = self.callee_id

        if self.caller_id is not None:
            result['CallerId'] = self.caller_id

        if self.conn_id is not None:
            result['ConnId'] = self.conn_id

        if self.extend_1 is not None:
            result['Extend1'] = self.extend_1

        if self.extend_2 is not None:
            result['Extend2'] = self.extend_2

        if self.extend_3 is not None:
            result['Extend3'] = self.extend_3

        if self.extend_4 is not None:
            result['Extend4'] = self.extend_4

        if self.group_no is not None:
            result['GroupNo'] = self.group_no

        if self.monited_agent_no is not None:
            result['MonitedAgentNo'] = self.monited_agent_no

        if self.monited_agent_phone_no is not None:
            result['MonitedAgentPhoneNo'] = self.monited_agent_phone_no

        if self.outbound_scenario is not None:
            result['OutboundScenario'] = self.outbound_scenario

        if self.phone_no is not None:
            result['PhoneNo'] = self.phone_no

        if self.statistic_date is not None:
            result['StatisticDate'] = self.statistic_date

        if self.statistic_time is not None:
            result['StatisticTime'] = self.statistic_time

        if self.status is not None:
            result['Status'] = self.status

        if self.target_request is not None:
            result['TargetRequest'] = self.target_request

        if self.target_select is not None:
            result['TargetSelect'] = self.target_select

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.transfer_no is not None:
            result['TransferNo'] = self.transfer_no

        if self.transfer_number is not None:
            result['TransferNumber'] = self.transfer_number

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentDropCall') is not None:
            self.agent_drop_call = m.get('AgentDropCall')

        if m.get('AgentNo') is not None:
            self.agent_no = m.get('AgentNo')

        if m.get('AliHangupCause') is not None:
            self.ali_hangup_cause = m.get('AliHangupCause')

        if m.get('CallDir') is not None:
            self.call_dir = m.get('CallDir')

        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')

        if m.get('CallType') is not None:
            self.call_type = m.get('CallType')

        if m.get('CalleeId') is not None:
            self.callee_id = m.get('CalleeId')

        if m.get('CallerId') is not None:
            self.caller_id = m.get('CallerId')

        if m.get('ConnId') is not None:
            self.conn_id = m.get('ConnId')

        if m.get('Extend1') is not None:
            self.extend_1 = m.get('Extend1')

        if m.get('Extend2') is not None:
            self.extend_2 = m.get('Extend2')

        if m.get('Extend3') is not None:
            self.extend_3 = m.get('Extend3')

        if m.get('Extend4') is not None:
            self.extend_4 = m.get('Extend4')

        if m.get('GroupNo') is not None:
            self.group_no = m.get('GroupNo')

        if m.get('MonitedAgentNo') is not None:
            self.monited_agent_no = m.get('MonitedAgentNo')

        if m.get('MonitedAgentPhoneNo') is not None:
            self.monited_agent_phone_no = m.get('MonitedAgentPhoneNo')

        if m.get('OutboundScenario') is not None:
            self.outbound_scenario = m.get('OutboundScenario')

        if m.get('PhoneNo') is not None:
            self.phone_no = m.get('PhoneNo')

        if m.get('StatisticDate') is not None:
            self.statistic_date = m.get('StatisticDate')

        if m.get('StatisticTime') is not None:
            self.statistic_time = m.get('StatisticTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TargetRequest') is not None:
            self.target_request = m.get('TargetRequest')

        if m.get('TargetSelect') is not None:
            self.target_select = m.get('TargetSelect')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('TransferNo') is not None:
            self.transfer_no = m.get('TransferNo')

        if m.get('TransferNumber') is not None:
            self.transfer_number = m.get('TransferNumber')

        return self

