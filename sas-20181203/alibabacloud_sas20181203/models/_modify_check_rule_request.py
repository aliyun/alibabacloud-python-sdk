# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ModifyCheckRuleRequest(DaraModel):
    def __init__(
        self,
        add_instance_list: List[main_models.ModifyCheckRuleRequestAddInstanceList] = None,
        delete_instance_list: List[main_models.ModifyCheckRuleRequestDeleteInstanceList] = None,
        remark: str = None,
        rule_id: int = None,
        rule_type: str = None,
        scope_type: str = None,
    ):
        # The list of instances to be added in this rule update. This parameter does not need to be passed if there are no instances to add.
        self.add_instance_list = add_instance_list
        # The list of instances to be removed in this rule update. This parameter does not need to be passed if there are no instances to remove.
        self.delete_instance_list = delete_instance_list
        # Remarks.
        self.remark = remark
        # Rule ID.
        # > You can obtain this parameter by calling the [ListCheckRule](https://help.aliyun.com/document_detail/2590599.html) API.
        # 
        # This parameter is required.
        self.rule_id = rule_id
        # Rule type. Default is **WHITE**. Values:
        # - **WHITE**: Add to whitelist
        self.rule_type = rule_type
        # The scope of effect for modifying the rule:
        # - **INSTANCE**: Instance
        # - **ITEM**: Check item
        self.scope_type = scope_type

    def validate(self):
        if self.add_instance_list:
            for v1 in self.add_instance_list:
                 if v1:
                    v1.validate()
        if self.delete_instance_list:
            for v1 in self.delete_instance_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AddInstanceList'] = []
        if self.add_instance_list is not None:
            for k1 in self.add_instance_list:
                result['AddInstanceList'].append(k1.to_map() if k1 else None)

        result['DeleteInstanceList'] = []
        if self.delete_instance_list is not None:
            for k1 in self.delete_instance_list:
                result['DeleteInstanceList'].append(k1.to_map() if k1 else None)

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_type is not None:
            result['RuleType'] = self.rule_type

        if self.scope_type is not None:
            result['ScopeType'] = self.scope_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.add_instance_list = []
        if m.get('AddInstanceList') is not None:
            for k1 in m.get('AddInstanceList'):
                temp_model = main_models.ModifyCheckRuleRequestAddInstanceList()
                self.add_instance_list.append(temp_model.from_map(k1))

        self.delete_instance_list = []
        if m.get('DeleteInstanceList') is not None:
            for k1 in m.get('DeleteInstanceList'):
                temp_model = main_models.ModifyCheckRuleRequestDeleteInstanceList()
                self.delete_instance_list.append(temp_model.from_map(k1))

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')

        if m.get('ScopeType') is not None:
            self.scope_type = m.get('ScopeType')

        return self

class ModifyCheckRuleRequestDeleteInstanceList(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
    ):
        # The instance ID of the asset.
        self.instance_id = instance_id
        # The region ID of the asset.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

class ModifyCheckRuleRequestAddInstanceList(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
    ):
        # The instance ID of the asset.
        self.instance_id = instance_id
        # The region ID of the asset.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

