# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class DsgDesensPlanAddOrUpdateRequest(DaraModel):
    def __init__(
        self,
        desens_rules: List[main_models.DsgDesensPlanAddOrUpdateRequestDesensRules] = None,
    ):
        # A collection of data masking rules that you want to add or modify.
        # 
        # This parameter is required.
        self.desens_rules = desens_rules

    def validate(self):
        if self.desens_rules:
            for v1 in self.desens_rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DesensRules'] = []
        if self.desens_rules is not None:
            for k1 in self.desens_rules:
                result['DesensRules'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.desens_rules = []
        if m.get('DesensRules') is not None:
            for k1 in m.get('DesensRules'):
                temp_model = main_models.DsgDesensPlanAddOrUpdateRequestDesensRules()
                self.desens_rules.append(temp_model.from_map(k1))

        return self

class DsgDesensPlanAddOrUpdateRequestDesensRules(DaraModel):
    def __init__(
        self,
        check_watermark: bool = None,
        data_type: str = None,
        desens_plan: main_models.DsgDesensPlanAddOrUpdateRequestDesensRulesDesensPlan = None,
        id: int = None,
        owner: str = None,
        rule_name: str = None,
        scene_ids: List[int] = None,
        status: int = None,
        columns: List[main_models.DsgDesensPlanAddOrUpdateRequestDesensRulesColumns] = None,
        empty_not_desesn: bool = None,
    ):
        # Specifies whether to add a watermark. Valid values:
        # 
        # *   true
        # *   false
        self.check_watermark = check_watermark
        # The sensitive field type.
        self.data_type = data_type
        # The data masking rule.
        # 
        # This parameter is required.
        self.desens_plan = desens_plan
        # The ID of the data masking rule. You can call the [DsgDesensPlanQueryList](https://help.aliyun.com/document_detail/2786578.html) operation to query the ID of the data masking rule.
        self.id = id
        # The owner of the data masking rule.
        # 
        # This parameter is required.
        self.owner = owner
        # The name of the data masking rule.
        # 
        # This parameter is required.
        self.rule_name = rule_name
        # The level-2 data masking scenario.
        # 
        # This parameter is required.
        self.scene_ids = scene_ids
        # The status of the data masking rule. Valid values:
        # 
        # *   0: expired
        # *   1: effective
        self.status = status
        self.columns = columns
        self.empty_not_desesn = empty_not_desesn

    def validate(self):
        if self.desens_plan:
            self.desens_plan.validate()
        if self.columns:
            for v1 in self.columns:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_watermark is not None:
            result['CheckWatermark'] = self.check_watermark

        if self.data_type is not None:
            result['DataType'] = self.data_type

        if self.desens_plan is not None:
            result['DesensPlan'] = self.desens_plan.to_map()

        if self.id is not None:
            result['Id'] = self.id

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.scene_ids is not None:
            result['SceneIds'] = self.scene_ids

        if self.status is not None:
            result['Status'] = self.status

        result['columns'] = []
        if self.columns is not None:
            for k1 in self.columns:
                result['columns'].append(k1.to_map() if k1 else None)

        if self.empty_not_desesn is not None:
            result['emptyNotDesesn'] = self.empty_not_desesn

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckWatermark') is not None:
            self.check_watermark = m.get('CheckWatermark')

        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')

        if m.get('DesensPlan') is not None:
            temp_model = main_models.DsgDesensPlanAddOrUpdateRequestDesensRulesDesensPlan()
            self.desens_plan = temp_model.from_map(m.get('DesensPlan'))

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('SceneIds') is not None:
            self.scene_ids = m.get('SceneIds')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.columns = []
        if m.get('columns') is not None:
            for k1 in m.get('columns'):
                temp_model = main_models.DsgDesensPlanAddOrUpdateRequestDesensRulesColumns()
                self.columns.append(temp_model.from_map(k1))

        if m.get('emptyNotDesesn') is not None:
            self.empty_not_desesn = m.get('emptyNotDesesn')

        return self

class DsgDesensPlanAddOrUpdateRequestDesensRulesColumns(DaraModel):
    def __init__(
        self,
        column: str = None,
        db_type: str = None,
        project: str = None,
        table: str = None,
    ):
        # This parameter is required.
        self.column = column
        # This parameter is required.
        self.db_type = db_type
        # This parameter is required.
        self.project = project
        # This parameter is required.
        self.table = table

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.column is not None:
            result['column'] = self.column

        if self.db_type is not None:
            result['dbType'] = self.db_type

        if self.project is not None:
            result['project'] = self.project

        if self.table is not None:
            result['table'] = self.table

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('column') is not None:
            self.column = m.get('column')

        if m.get('dbType') is not None:
            self.db_type = m.get('dbType')

        if m.get('project') is not None:
            self.project = m.get('project')

        if m.get('table') is not None:
            self.table = m.get('table')

        return self

class DsgDesensPlanAddOrUpdateRequestDesensRulesDesensPlan(DaraModel):
    def __init__(
        self,
        desens_plan_type: str = None,
        ext_param: Dict[str, Any] = None,
    ):
        # The masking method configured in the data masking rule. Valid values:
        # 
        # *   hash
        # *   mapping
        # *   mask
        # *   charreplacement
        # *   intervalselect
        # *   decimalpoint
        # *   emptydesens
        # 
        # This parameter is required.
        self.desens_plan_type = desens_plan_type
        # The parameters for the data masking rule.
        self.ext_param = ext_param

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desens_plan_type is not None:
            result['DesensPlanType'] = self.desens_plan_type

        if self.ext_param is not None:
            result['ExtParam'] = self.ext_param

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesensPlanType') is not None:
            self.desens_plan_type = m.get('DesensPlanType')

        if m.get('ExtParam') is not None:
            self.ext_param = m.get('ExtParam')

        return self

