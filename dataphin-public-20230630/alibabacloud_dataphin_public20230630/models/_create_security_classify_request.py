# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class CreateSecurityClassifyRequest(DaraModel):
    def __init__(
        self,
        create_command: main_models.CreateSecurityClassifyRequestCreateCommand = None,
        op_tenant_id: int = None,
    ):
        # This parameter is required.
        self.create_command = create_command
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        if self.create_command:
            self.create_command.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_command is not None:
            result['CreateCommand'] = self.create_command.to_map()

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateCommand') is not None:
            temp_model = main_models.CreateSecurityClassifyRequestCreateCommand()
            self.create_command = temp_model.from_map(m.get('CreateCommand'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        return self

class CreateSecurityClassifyRequestCreateCommand(DaraModel):
    def __init__(
        self,
        abbreviation: str = None,
        advanced_condition_list: List[main_models.CreateSecurityClassifyRequestCreateCommandAdvancedConditionList] = None,
        description: str = None,
        feature_name_list: List[str] = None,
        level_name: str = None,
        name: str = None,
        parent_path: str = None,
        priority: int = None,
        status: str = None,
    ):
        self.abbreviation = abbreviation
        self.advanced_condition_list = advanced_condition_list
        self.description = description
        self.feature_name_list = feature_name_list
        # This parameter is required.
        self.level_name = level_name
        # This parameter is required.
        self.name = name
        self.parent_path = parent_path
        self.priority = priority
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
                temp_model = main_models.CreateSecurityClassifyRequestCreateCommandAdvancedConditionList()
                self.advanced_condition_list.append(temp_model.from_map(k1))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FeatureNameList') is not None:
            self.feature_name_list = m.get('FeatureNameList')

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

class CreateSecurityClassifyRequestCreateCommandAdvancedConditionList(DaraModel):
    def __init__(
        self,
        id: str = None,
        operate: str = None,
        option_list: List[main_models.CreateSecurityClassifyRequestCreateCommandAdvancedConditionListOptionList] = None,
        parent_id: str = None,
        property: str = None,
        relation: str = None,
        value_list: List[str] = None,
    ):
        # This parameter is required.
        self.id = id
        # This parameter is required.
        self.operate = operate
        self.option_list = option_list
        self.parent_id = parent_id
        self.property = property
        # This parameter is required.
        self.relation = relation
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
                temp_model = main_models.CreateSecurityClassifyRequestCreateCommandAdvancedConditionListOptionList()
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

class CreateSecurityClassifyRequestCreateCommandAdvancedConditionListOptionList(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # This parameter is required.
        self.key = key
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

