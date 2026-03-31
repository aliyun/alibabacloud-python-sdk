# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_cloud_siem20220616 import models as main_models
from darabonba.model import DaraModel

class DescribeDisposeAndPlaybookResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.DescribeDisposeAndPlaybookResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code that is returned.
        self.code = code
        # The data returned.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
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
            temp_model = main_models.DescribeDisposeAndPlaybookResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeDisposeAndPlaybookResponseBodyData(DaraModel):
    def __init__(
        self,
        page_info: main_models.DescribeDisposeAndPlaybookResponseBodyDataPageInfo = None,
        response_data: List[main_models.DescribeDisposeAndPlaybookResponseBodyDataResponseData] = None,
    ):
        # The pagination information.
        self.page_info = page_info
        # The detailed data.
        self.response_data = response_data

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.response_data:
            for v1 in self.response_data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        result['ResponseData'] = []
        if self.response_data is not None:
            for k1 in self.response_data:
                result['ResponseData'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageInfo') is not None:
            temp_model = main_models.DescribeDisposeAndPlaybookResponseBodyDataPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        self.response_data = []
        if m.get('ResponseData') is not None:
            for k1 in m.get('ResponseData'):
                temp_model = main_models.DescribeDisposeAndPlaybookResponseBodyDataResponseData()
                self.response_data.append(temp_model.from_map(k1))

        return self

class DescribeDisposeAndPlaybookResponseBodyDataResponseData(DaraModel):
    def __init__(
        self,
        alert_num: int = None,
        dispose: str = None,
        entity_id: int = None,
        entity_info: Dict[str, Any] = None,
        entity_type: str = None,
        opcode_map: Dict[str, str] = None,
        opcode_set: List[str] = None,
        playbook_list: List[main_models.DescribeDisposeAndPlaybookResponseBodyDataResponseDataPlaybookList] = None,
        scope: List[Any] = None,
    ):
        # The number of alerts that are associated with the entity.
        self.alert_num = alert_num
        # The object for handling.
        self.dispose = dispose
        # The entity ID
        self.entity_id = entity_id
        # The entity information.
        self.entity_info = entity_info
        self.entity_type = entity_type
        # The key-value pairs each of which consists of opcode and oplevel.
        self.opcode_map = opcode_map
        # The codes of the playbooks that are recommended for entity handling.
        self.opcode_set = opcode_set
        # The playbooks that can handle the entity.
        self.playbook_list = playbook_list
        # The IDs of the users who can handle objects.
        self.scope = scope

    def validate(self):
        if self.playbook_list:
            for v1 in self.playbook_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_num is not None:
            result['AlertNum'] = self.alert_num

        if self.dispose is not None:
            result['Dispose'] = self.dispose

        if self.entity_id is not None:
            result['EntityId'] = self.entity_id

        if self.entity_info is not None:
            result['EntityInfo'] = self.entity_info

        if self.entity_type is not None:
            result['EntityType'] = self.entity_type

        if self.opcode_map is not None:
            result['OpcodeMap'] = self.opcode_map

        if self.opcode_set is not None:
            result['OpcodeSet'] = self.opcode_set

        result['PlaybookList'] = []
        if self.playbook_list is not None:
            for k1 in self.playbook_list:
                result['PlaybookList'].append(k1.to_map() if k1 else None)

        if self.scope is not None:
            result['Scope'] = self.scope

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertNum') is not None:
            self.alert_num = m.get('AlertNum')

        if m.get('Dispose') is not None:
            self.dispose = m.get('Dispose')

        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')

        if m.get('EntityInfo') is not None:
            self.entity_info = m.get('EntityInfo')

        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')

        if m.get('OpcodeMap') is not None:
            self.opcode_map = m.get('OpcodeMap')

        if m.get('OpcodeSet') is not None:
            self.opcode_set = m.get('OpcodeSet')

        self.playbook_list = []
        if m.get('PlaybookList') is not None:
            for k1 in m.get('PlaybookList'):
                temp_model = main_models.DescribeDisposeAndPlaybookResponseBodyDataResponseDataPlaybookList()
                self.playbook_list.append(temp_model.from_map(k1))

        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        return self

class DescribeDisposeAndPlaybookResponseBodyDataResponseDataPlaybookList(DaraModel):
    def __init__(
        self,
        available: str = None,
        description: str = None,
        display_name: str = None,
        name: str = None,
        op_code: str = None,
        op_level: str = None,
        param_config: List[Any] = None,
        task_config: str = None,
        un_available_code: str = None,
        uuid: str = None,
        waf_playbook: bool = None,
    ):
        self.available = available
        # The playbook description.
        self.description = description
        # The display name of the playbook.
        self.display_name = display_name
        # The playbook name, which is the unique identifier of the playbook.
        self.name = name
        # The opcode of the playbook, which corresponds to the opcode of the playbook recommended for entity handling.
        self.op_code = op_code
        # Indicates whether quick event handling is selected by default. Valid values:
        # 
        # *   2: Quick event handling is selected.
        # *   1: Quick event handling is displayed but not selected.
        self.op_level = op_level
        # The playbook parameters and the corresponding properties.
        self.param_config = param_config
        # The opcode configuration.
        self.task_config = task_config
        self.un_available_code = un_available_code
        self.uuid = uuid
        # Indicates whether the playbook is intended for Web Application Firewall (WAF). Valid values:
        # 
        # *   true
        # *   false
        self.waf_playbook = waf_playbook

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.available is not None:
            result['Available'] = self.available

        if self.description is not None:
            result['Description'] = self.description

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.name is not None:
            result['Name'] = self.name

        if self.op_code is not None:
            result['OpCode'] = self.op_code

        if self.op_level is not None:
            result['OpLevel'] = self.op_level

        if self.param_config is not None:
            result['ParamConfig'] = self.param_config

        if self.task_config is not None:
            result['TaskConfig'] = self.task_config

        if self.un_available_code is not None:
            result['UnAvailableCode'] = self.un_available_code

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        if self.waf_playbook is not None:
            result['WafPlaybook'] = self.waf_playbook

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Available') is not None:
            self.available = m.get('Available')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OpCode') is not None:
            self.op_code = m.get('OpCode')

        if m.get('OpLevel') is not None:
            self.op_level = m.get('OpLevel')

        if m.get('ParamConfig') is not None:
            self.param_config = m.get('ParamConfig')

        if m.get('TaskConfig') is not None:
            self.task_config = m.get('TaskConfig')

        if m.get('UnAvailableCode') is not None:
            self.un_available_code = m.get('UnAvailableCode')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        if m.get('WafPlaybook') is not None:
            self.waf_playbook = m.get('WafPlaybook')

        return self

class DescribeDisposeAndPlaybookResponseBodyDataPageInfo(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The current page number.
        self.current_page = current_page
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

