# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloud_siem20220616 import models as main_models
from darabonba.model import DaraModel

class ListAutomateResponseConfigsResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.ListAutomateResponseConfigsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code.
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
            temp_model = main_models.ListAutomateResponseConfigsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListAutomateResponseConfigsResponseBodyData(DaraModel):
    def __init__(
        self,
        page_info: main_models.ListAutomateResponseConfigsResponseBodyDataPageInfo = None,
        response_data: List[main_models.ListAutomateResponseConfigsResponseBodyDataResponseData] = None,
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
            temp_model = main_models.ListAutomateResponseConfigsResponseBodyDataPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        self.response_data = []
        if m.get('ResponseData') is not None:
            for k1 in m.get('ResponseData'):
                temp_model = main_models.ListAutomateResponseConfigsResponseBodyDataResponseData()
                self.response_data.append(temp_model.from_map(k1))

        return self

class ListAutomateResponseConfigsResponseBodyDataResponseData(DaraModel):
    def __init__(
        self,
        action_config: str = None,
        action_type: str = None,
        aliuid: int = None,
        auto_response_type: str = None,
        data_type: int = None,
        execution_condition: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        response_rule_type: str = None,
        rule_name: str = None,
        status: int = None,
        sub_user_id: int = None,
    ):
        # The configuration of the action that is performed after the automated response rule is hit. The value is in the JSON format.
        self.action_config = action_config
        # The type of the handling action. Multiple types are separated by commas (,). Valid values:
        # 
        # *   **doPlaybook**: runs the playbook.
        # *   **changeEventStatus**: changes the event status.
        # *   **changeThreatLevel**: changes the risk level of the event.
        self.action_type = action_type
        # The ID of the Alibaba Cloud account that is associated with the rule in SIEM.
        self.aliuid = aliuid
        # The type of the automated response rule. Valid values:
        # 
        # *   **event**
        # *   **alert**
        self.auto_response_type = auto_response_type
        # The type of the view. Valid values:
        # 
        # 0: the current Alibaba Cloud account
        # 1: the global account
        self.data_type = data_type
        # The trigger condition of the automated response rule. The value is in the JSON format.
        self.execution_condition = execution_condition
        # The creation time.
        self.gmt_create = gmt_create
        # The update time.
        self.gmt_modified = gmt_modified
        # The ID of the automated response rule.
        self.id = id
        self.response_rule_type = response_rule_type
        # The name of the automated response rule.
        self.rule_name = rule_name
        # The status of the rule. Valid values:
        # 
        # *   **0**: disabled.
        # *   **100**: enabled.
        self.status = status
        # The ID of the user who created the rule.
        self.sub_user_id = sub_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_config is not None:
            result['ActionConfig'] = self.action_config

        if self.action_type is not None:
            result['ActionType'] = self.action_type

        if self.aliuid is not None:
            result['Aliuid'] = self.aliuid

        if self.auto_response_type is not None:
            result['AutoResponseType'] = self.auto_response_type

        if self.data_type is not None:
            result['DataType'] = self.data_type

        if self.execution_condition is not None:
            result['ExecutionCondition'] = self.execution_condition

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.response_rule_type is not None:
            result['ResponseRuleType'] = self.response_rule_type

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.status is not None:
            result['Status'] = self.status

        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionConfig') is not None:
            self.action_config = m.get('ActionConfig')

        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')

        if m.get('Aliuid') is not None:
            self.aliuid = m.get('Aliuid')

        if m.get('AutoResponseType') is not None:
            self.auto_response_type = m.get('AutoResponseType')

        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')

        if m.get('ExecutionCondition') is not None:
            self.execution_condition = m.get('ExecutionCondition')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('ResponseRuleType') is not None:
            self.response_rule_type = m.get('ResponseRuleType')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')

        return self

class ListAutomateResponseConfigsResponseBodyDataPageInfo(DaraModel):
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

