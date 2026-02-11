# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_cloud_siem20220616 import models as main_models
from darabonba.model import DaraModel

class DescribeWhiteRuleListResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.DescribeWhiteRuleListResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code.
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
            temp_model = main_models.DescribeWhiteRuleListResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeWhiteRuleListResponseBodyData(DaraModel):
    def __init__(
        self,
        page_info: main_models.DescribeWhiteRuleListResponseBodyDataPageInfo = None,
        response_data: List[main_models.DescribeWhiteRuleListResponseBodyDataResponseData] = None,
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
            temp_model = main_models.DescribeWhiteRuleListResponseBodyDataPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        self.response_data = []
        if m.get('ResponseData') is not None:
            for k1 in m.get('ResponseData'):
                temp_model = main_models.DescribeWhiteRuleListResponseBodyDataResponseData()
                self.response_data.append(temp_model.from_map(k1))

        return self

class DescribeWhiteRuleListResponseBodyDataResponseData(DaraModel):
    def __init__(
        self,
        alert_name: str = None,
        alert_name_id: str = None,
        alert_type: str = None,
        alert_type_id: str = None,
        alert_uuid: str = None,
        aliuid: int = None,
        expression: main_models.DescribeWhiteRuleListResponseBodyDataResponseDataExpression = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        incident_uuid: str = None,
        status: int = None,
        sub_aliuid: int = None,
    ):
        # The alert name.
        self.alert_name = alert_name
        # The ID of the alert name.
        self.alert_name_id = alert_name_id
        # The alert type.
        self.alert_type = alert_type
        # The ID of the alert type.
        self.alert_type_id = alert_type_id
        # The UUID of the alert.
        self.alert_uuid = alert_uuid
        # The ID of the Alibaba Cloud account that is used to purchase the threat analysis feature.
        self.aliuid = aliuid
        # The conditions in the rule. The value is a JSON array.
        self.expression = expression
        # The time when the whitelist rule was created.
        self.gmt_create = gmt_create
        # The time when the whitelist rule was modified.
        self.gmt_modified = gmt_modified
        # The ID of the whitelist rule.
        self.id = id
        # The UUID of the event.
        self.incident_uuid = incident_uuid
        # The status of the whitelist rule. Valid values:
        # 
        # *   1: enabled.
        # *   0: disabled.
        self.status = status
        # The ID of the Alibaba Cloud account that is used to create the whitelist rule.
        self.sub_aliuid = sub_aliuid

    def validate(self):
        if self.expression:
            self.expression.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_name is not None:
            result['AlertName'] = self.alert_name

        if self.alert_name_id is not None:
            result['AlertNameId'] = self.alert_name_id

        if self.alert_type is not None:
            result['AlertType'] = self.alert_type

        if self.alert_type_id is not None:
            result['AlertTypeId'] = self.alert_type_id

        if self.alert_uuid is not None:
            result['AlertUuid'] = self.alert_uuid

        if self.aliuid is not None:
            result['Aliuid'] = self.aliuid

        if self.expression is not None:
            result['Expression'] = self.expression.to_map()

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid

        if self.status is not None:
            result['Status'] = self.status

        if self.sub_aliuid is not None:
            result['SubAliuid'] = self.sub_aliuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertName') is not None:
            self.alert_name = m.get('AlertName')

        if m.get('AlertNameId') is not None:
            self.alert_name_id = m.get('AlertNameId')

        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')

        if m.get('AlertTypeId') is not None:
            self.alert_type_id = m.get('AlertTypeId')

        if m.get('AlertUuid') is not None:
            self.alert_uuid = m.get('AlertUuid')

        if m.get('Aliuid') is not None:
            self.aliuid = m.get('Aliuid')

        if m.get('Expression') is not None:
            temp_model = main_models.DescribeWhiteRuleListResponseBodyDataResponseDataExpression()
            self.expression = temp_model.from_map(m.get('Expression'))

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SubAliuid') is not None:
            self.sub_aliuid = m.get('SubAliuid')

        return self

class DescribeWhiteRuleListResponseBodyDataResponseDataExpression(DaraModel):
    def __init__(
        self,
        conditions: List[main_models.DescribeWhiteRuleListResponseBodyDataResponseDataExpressionConditions] = None,
        logic: str = None,
    ):
        # The rule conditions.
        self.conditions = conditions
        # The logical relationships among the rule conditions.
        self.logic = logic

    def validate(self):
        if self.conditions:
            for v1 in self.conditions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Conditions'] = []
        if self.conditions is not None:
            for k1 in self.conditions:
                result['Conditions'].append(k1.to_map() if k1 else None)

        if self.logic is not None:
            result['Logic'] = self.logic

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.conditions = []
        if m.get('Conditions') is not None:
            for k1 in m.get('Conditions'):
                temp_model = main_models.DescribeWhiteRuleListResponseBodyDataResponseDataExpressionConditions()
                self.conditions.append(temp_model.from_map(k1))

        if m.get('Logic') is not None:
            self.logic = m.get('Logic')

        return self

class DescribeWhiteRuleListResponseBodyDataResponseDataExpressionConditions(DaraModel):
    def __init__(
        self,
        is_not: bool = None,
        item_id: int = None,
        left: main_models.DescribeWhiteRuleListResponseBodyDataResponseDataExpressionConditionsLeft = None,
        operator: str = None,
        right: main_models.DescribeWhiteRuleListResponseBodyDataResponseDataExpressionConditionsRight = None,
    ):
        # Indicates whether the result is inverted. Valid values:
        # 
        # *   true
        # *   false
        self.is_not = is_not
        # The ID of the rule condition.
        self.item_id = item_id
        # The left operand of the rule condition.
        self.left = left
        # The logical operator of the rule condition. Valid values:
        # 
        # *   `=`: equals to.
        # *   `<>`: does not equal to.
        # *   `in`: contains.
        # *   `not in`: does not contain.
        # *   `REGEXP`: matches a regular expression.
        # *   `NOT REGEXP`: does not match a regular expression.
        self.operator = operator
        # The right operand of the rule condition.
        self.right = right

    def validate(self):
        if self.left:
            self.left.validate()
        if self.right:
            self.right.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_not is not None:
            result['IsNot'] = self.is_not

        if self.item_id is not None:
            result['ItemId'] = self.item_id

        if self.left is not None:
            result['Left'] = self.left.to_map()

        if self.operator is not None:
            result['Operator'] = self.operator

        if self.right is not None:
            result['Right'] = self.right.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsNot') is not None:
            self.is_not = m.get('IsNot')

        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')

        if m.get('Left') is not None:
            temp_model = main_models.DescribeWhiteRuleListResponseBodyDataResponseDataExpressionConditionsLeft()
            self.left = temp_model.from_map(m.get('Left'))

        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        if m.get('Right') is not None:
            temp_model = main_models.DescribeWhiteRuleListResponseBodyDataResponseDataExpressionConditionsRight()
            self.right = temp_model.from_map(m.get('Right'))

        return self

class DescribeWhiteRuleListResponseBodyDataResponseDataExpressionConditionsRight(DaraModel):
    def __init__(
        self,
        is_var: bool = None,
        modifier: str = None,
        modifier_param: Dict[str, Any] = None,
        type: str = None,
        value: str = None,
    ):
        # Indicates whether the right operand is a constant or a runtime variable that is obtained from the runtime context. Valid values:
        # 
        # *   true: runtime variable.
        # *   false: constant.
        self.is_var = is_var
        # The remarks on the right operand.
        self.modifier = modifier
        # The key-value pair information of the remarks.
        self.modifier_param = modifier_param
        # The data type of the right operand.
        self.type = type
        # The right operand.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_var is not None:
            result['IsVar'] = self.is_var

        if self.modifier is not None:
            result['Modifier'] = self.modifier

        if self.modifier_param is not None:
            result['ModifierParam'] = self.modifier_param

        if self.type is not None:
            result['Type'] = self.type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsVar') is not None:
            self.is_var = m.get('IsVar')

        if m.get('Modifier') is not None:
            self.modifier = m.get('Modifier')

        if m.get('ModifierParam') is not None:
            self.modifier_param = m.get('ModifierParam')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeWhiteRuleListResponseBodyDataResponseDataExpressionConditionsLeft(DaraModel):
    def __init__(
        self,
        is_var: bool = None,
        modifier: str = None,
        modifier_param: Dict[str, Any] = None,
        type: str = None,
        value: str = None,
    ):
        # Indicates whether the left operand is a variable. Valid values:
        # 
        # *   true: variable.
        # *   false: constant.
        self.is_var = is_var
        # The remarks on the right operand.
        self.modifier = modifier
        # The key-value pair information of the remarks.
        self.modifier_param = modifier_param
        # Indicates whether the left operand is a constant. Valid values:
        # 
        # *   true
        # *   false
        self.type = type
        # The variable of the left operand.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_var is not None:
            result['IsVar'] = self.is_var

        if self.modifier is not None:
            result['Modifier'] = self.modifier

        if self.modifier_param is not None:
            result['ModifierParam'] = self.modifier_param

        if self.type is not None:
            result['Type'] = self.type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsVar') is not None:
            self.is_var = m.get('IsVar')

        if m.get('Modifier') is not None:
            self.modifier = m.get('Modifier')

        if m.get('ModifierParam') is not None:
            self.modifier_param = m.get('ModifierParam')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeWhiteRuleListResponseBodyDataPageInfo(DaraModel):
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

