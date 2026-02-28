# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_ccc20200701 import models as main_models
from darabonba.model import DaraModel

class ListIvrTrackingDetailsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListIvrTrackingDetailsResponseBodyData = None,
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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.ListIvrTrackingDetailsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListIvrTrackingDetailsResponseBodyData(DaraModel):
    def __init__(
        self,
        list: List[main_models.ListIvrTrackingDetailsResponseBodyDataList] = None,
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
                temp_model = main_models.ListIvrTrackingDetailsResponseBodyDataList()
                self.list.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListIvrTrackingDetailsResponseBodyDataList(DaraModel):
    def __init__(
        self,
        callee: str = None,
        caller: str = None,
        channel_id: str = None,
        channel_variables: str = None,
        contact_id: str = None,
        enter_time: int = None,
        flow_id: str = None,
        flow_name: str = None,
        instance: str = None,
        leave_time: int = None,
        node_exit_code: str = None,
        node_id: str = None,
        node_name: str = None,
        node_properties: Dict[str, Any] = None,
        node_type: str = None,
        node_variables: Dict[str, Any] = None,
    ):
        self.callee = callee
        self.caller = caller
        self.channel_id = channel_id
        self.channel_variables = channel_variables
        self.contact_id = contact_id
        self.enter_time = enter_time
        self.flow_id = flow_id
        self.flow_name = flow_name
        self.instance = instance
        self.leave_time = leave_time
        self.node_exit_code = node_exit_code
        self.node_id = node_id
        self.node_name = node_name
        self.node_properties = node_properties
        self.node_type = node_type
        self.node_variables = node_variables

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.callee is not None:
            result['Callee'] = self.callee

        if self.caller is not None:
            result['Caller'] = self.caller

        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id

        if self.channel_variables is not None:
            result['ChannelVariables'] = self.channel_variables

        if self.contact_id is not None:
            result['ContactId'] = self.contact_id

        if self.enter_time is not None:
            result['EnterTime'] = self.enter_time

        if self.flow_id is not None:
            result['FlowId'] = self.flow_id

        if self.flow_name is not None:
            result['FlowName'] = self.flow_name

        if self.instance is not None:
            result['Instance'] = self.instance

        if self.leave_time is not None:
            result['LeaveTime'] = self.leave_time

        if self.node_exit_code is not None:
            result['NodeExitCode'] = self.node_exit_code

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        if self.node_properties is not None:
            result['NodeProperties'] = self.node_properties

        if self.node_type is not None:
            result['NodeType'] = self.node_type

        if self.node_variables is not None:
            result['NodeVariables'] = self.node_variables

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Callee') is not None:
            self.callee = m.get('Callee')

        if m.get('Caller') is not None:
            self.caller = m.get('Caller')

        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        if m.get('ChannelVariables') is not None:
            self.channel_variables = m.get('ChannelVariables')

        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')

        if m.get('EnterTime') is not None:
            self.enter_time = m.get('EnterTime')

        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')

        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')

        if m.get('Instance') is not None:
            self.instance = m.get('Instance')

        if m.get('LeaveTime') is not None:
            self.leave_time = m.get('LeaveTime')

        if m.get('NodeExitCode') is not None:
            self.node_exit_code = m.get('NodeExitCode')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        if m.get('NodeProperties') is not None:
            self.node_properties = m.get('NodeProperties')

        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')

        if m.get('NodeVariables') is not None:
            self.node_variables = m.get('NodeVariables')

        return self

