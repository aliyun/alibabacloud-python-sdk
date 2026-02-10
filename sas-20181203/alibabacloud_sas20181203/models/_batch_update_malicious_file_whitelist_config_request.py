# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class BatchUpdateMaliciousFileWhitelistConfigRequest(DaraModel):
    def __init__(
        self,
        config_list: List[main_models.BatchUpdateMaliciousFileWhitelistConfigRequestConfigList] = None,
    ):
        # The whitelist rules.
        self.config_list = config_list

    def validate(self):
        if self.config_list:
            for v1 in self.config_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ConfigList'] = []
        if self.config_list is not None:
            for k1 in self.config_list:
                result['ConfigList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.config_list = []
        if m.get('ConfigList') is not None:
            for k1 in m.get('ConfigList'):
                temp_model = main_models.BatchUpdateMaliciousFileWhitelistConfigRequestConfigList()
                self.config_list.append(temp_model.from_map(k1))

        return self

class BatchUpdateMaliciousFileWhitelistConfigRequestConfigList(DaraModel):
    def __init__(
        self,
        config_id: int = None,
        event_name: str = None,
        field: str = None,
        field_value: str = None,
        operator: str = None,
        source: str = None,
        target_type: str = None,
        target_value: str = None,
    ):
        # The ID of the whitelist rule. If you do not specify this parameter, a whitelist rule is created.
        self.config_id = config_id
        # The name of the alert.
        # 
        # *   Set the value to **ALL**, which indicates all alert types.
        self.event_name = event_name
        # The field that you want to use in the whitelist rule.
        self.field = field
        # The value of the field that you want to use in the whitelist rule.
        self.field_value = field_value
        # The logical operator that you want to use in the whitelist rule.
        # 
        # *   Set the value to strEqual, which indicates the equality operator (=).
        self.operator = operator
        # The feature to which this operation belongs.
        # 
        # *   Set the value to agentless, which indicates the agentless detection feature.
        self.source = source
        # The type of the assets on which you want the whitelist rule to take effect. Valid values:
        # 
        # *   ALL: all assets
        # *   SELECTION_KEY: selected assets
        self.target_type = target_type
        # The assets on which you want the whitelist rule to take effect. Valid values:
        # 
        # *   ALL: all assets
        # *   Others: selected assets
        self.target_value = target_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_id is not None:
            result['ConfigId'] = self.config_id

        if self.event_name is not None:
            result['EventName'] = self.event_name

        if self.field is not None:
            result['Field'] = self.field

        if self.field_value is not None:
            result['FieldValue'] = self.field_value

        if self.operator is not None:
            result['Operator'] = self.operator

        if self.source is not None:
            result['Source'] = self.source

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        if self.target_value is not None:
            result['TargetValue'] = self.target_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')

        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')

        if m.get('Field') is not None:
            self.field = m.get('Field')

        if m.get('FieldValue') is not None:
            self.field_value = m.get('FieldValue')

        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        if m.get('TargetValue') is not None:
            self.target_value = m.get('TargetValue')

        return self

