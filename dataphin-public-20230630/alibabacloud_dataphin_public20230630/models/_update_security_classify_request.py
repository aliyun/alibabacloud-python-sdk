# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class UpdateSecurityClassifyRequest(DaraModel):
    def __init__(
        self,
        op_tenant_id: int = None,
        update_command: main_models.UpdateSecurityClassifyRequestUpdateCommand = None,
    ):
        # The tenant ID.
        # 
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # The update command.
        # 
        # This parameter is required.
        self.update_command = update_command

    def validate(self):
        if self.update_command:
            self.update_command.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.update_command is not None:
            result['UpdateCommand'] = self.update_command.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('UpdateCommand') is not None:
            temp_model = main_models.UpdateSecurityClassifyRequestUpdateCommand()
            self.update_command = temp_model.from_map(m.get('UpdateCommand'))

        return self

class UpdateSecurityClassifyRequestUpdateCommand(DaraModel):
    def __init__(
        self,
        abbreviation: str = None,
        advanced_condition_list: List[main_models.UpdateSecurityClassifyRequestUpdateCommandAdvancedConditionList] = None,
        description: str = None,
        feature_name_list: List[str] = None,
        id: int = None,
        level_name: str = None,
        name: str = None,
        parent_path: str = None,
        priority: int = None,
        status: str = None,
    ):
        # The abbreviation of the classification.
        self.abbreviation = abbreviation
        # The advanced configurations.
        self.advanced_condition_list = advanced_condition_list
        # The description of the classification.
        self.description = description
        # The feature names.
        self.feature_name_list = feature_name_list
        # The classification ID. If this parameter is not specified, the classification is matched and updated based on the classification name and parent path.
        self.id = id
        # The data level name.
        # 
        # This parameter is required.
        self.level_name = level_name
        # The classification name.
        self.name = name
        # The parent path of the classification.
        self.parent_path = parent_path
        # The priority. Default value: 5.
        self.priority = priority
        # The classification status. Valid values:
        # - ENABLE: enabled.
        # - DISABLE: disabled.
        self.status = status

    def validate(self):
        if self.advanced_condition_list:
            for v1 in self.advanced_condition_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.abbreviation is not None:
            result['Abbreviation'] = self.abbreviation

        result['AdvancedConditionList'] = []
        if self.advanced_condition_list is not None:
            for k1 in self.advanced_condition_list:
                result['AdvancedConditionList'].append(k1.to_map() if k1 else None)

        if self.description is not None:
            result['Description'] = self.description

        if self.feature_name_list is not None:
            result['FeatureNameList'] = self.feature_name_list

        if self.id is not None:
            result['Id'] = self.id

        if self.level_name is not None:
            result['LevelName'] = self.level_name

        if self.name is not None:
            result['Name'] = self.name

        if self.parent_path is not None:
            result['ParentPath'] = self.parent_path

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Abbreviation') is not None:
            self.abbreviation = m.get('Abbreviation')

        self.advanced_condition_list = []
        if m.get('AdvancedConditionList') is not None:
            for k1 in m.get('AdvancedConditionList'):
                temp_model = main_models.UpdateSecurityClassifyRequestUpdateCommandAdvancedConditionList()
                self.advanced_condition_list.append(temp_model.from_map(k1))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FeatureNameList') is not None:
            self.feature_name_list = m.get('FeatureNameList')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('LevelName') is not None:
            self.level_name = m.get('LevelName')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ParentPath') is not None:
            self.parent_path = m.get('ParentPath')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class UpdateSecurityClassifyRequestUpdateCommandAdvancedConditionList(DaraModel):
    def __init__(
        self,
        id: str = None,
        operate: str = None,
        option_list: List[main_models.UpdateSecurityClassifyRequestUpdateCommandAdvancedConditionListOptionList] = None,
        parent_id: str = None,
        property: str = None,
        relation: str = None,
        value_list: List[str] = None,
    ):
        # The ID of the feature condition node. The ID is randomly generated by the application and must be unique.
        # 
        # This parameter is required.
        self.id = id
        # The condition operator. Valid values:
        # - AND
        # - OR
        # - BUILT_IN_EXPRESSION: built-in expression.
        # - IGNORE_CASE_EXPRESSION: regular expression with case-insensitive matching.
        # - EXPRESSION: regular expression.
        # - NOT_BELONG: does not belong to.
        # - CONTAINS: contains.
        # - NOT_CONTAINS: does not contain.
        # - EQUAL
        # - NOT_EQUAL.
        # 
        # This parameter is required.
        self.operate = operate
        # The additional properties, such as field content.
        self.option_list = option_list
        # The parent node of the feature condition.
        self.parent_id = parent_id
        # The feature property. Valid values:
        # - TABLE_NAME: table name.
        # - TABLE_DESC: table description.
        # - FIELD_CONTENT: field content.
        # - FIELD_NAME: field name.
        # - FIELD_DESC: field description.
        # - FIELD_TYPE: field type.
        self.property = property
        # The condition relation. Valid values:
        # - EXPRESSION: expression.
        # - RELATION: relation.
        # 
        # This parameter is required.
        self.relation = relation
        # The condition values.
        self.value_list = value_list

    def validate(self):
        if self.option_list:
            for v1 in self.option_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.operate is not None:
            result['Operate'] = self.operate

        result['OptionList'] = []
        if self.option_list is not None:
            for k1 in self.option_list:
                result['OptionList'].append(k1.to_map() if k1 else None)

        if self.parent_id is not None:
            result['ParentId'] = self.parent_id

        if self.property is not None:
            result['Property'] = self.property

        if self.relation is not None:
            result['Relation'] = self.relation

        if self.value_list is not None:
            result['ValueList'] = self.value_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Operate') is not None:
            self.operate = m.get('Operate')

        self.option_list = []
        if m.get('OptionList') is not None:
            for k1 in m.get('OptionList'):
                temp_model = main_models.UpdateSecurityClassifyRequestUpdateCommandAdvancedConditionListOptionList()
                self.option_list.append(temp_model.from_map(k1))

        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')

        if m.get('Property') is not None:
            self.property = m.get('Property')

        if m.get('Relation') is not None:
            self.relation = m.get('Relation')

        if m.get('ValueList') is not None:
            self.value_list = m.get('ValueList')

        return self

class UpdateSecurityClassifyRequestUpdateCommandAdvancedConditionListOptionList(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The configuration item.
        # 
        # This parameter is required.
        self.key = key
        # The configuration item value.
        # 
        # This parameter is required.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

