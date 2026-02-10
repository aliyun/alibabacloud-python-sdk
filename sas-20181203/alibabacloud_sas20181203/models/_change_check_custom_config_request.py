# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ChangeCheckCustomConfigRequest(DaraModel):
    def __init__(
        self,
        check_id: int = None,
        custom_configs: List[main_models.ChangeCheckCustomConfigRequestCustomConfigs] = None,
        region_id: str = None,
        repair_configs: List[main_models.ChangeCheckCustomConfigRequestRepairConfigs] = None,
    ):
        # The ID of the check item.
        # 
        # > You can call the [ListCheckResult](~~ListCheckResult~~) operation to query the IDs of check items.
        self.check_id = check_id
        # The custom configuration items of the check item.
        self.custom_configs = custom_configs
        # The region where the Security Center instance is deployed. Valid values:
        # 
        # *   **cn-hangzhou**: International
        # *   **ap-southeast-1**: Singapore
        self.region_id = region_id
        # The parameters required for fixing risk items.
        self.repair_configs = repair_configs

    def validate(self):
        if self.custom_configs:
            for v1 in self.custom_configs:
                 if v1:
                    v1.validate()
        if self.repair_configs:
            for v1 in self.repair_configs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_id is not None:
            result['CheckId'] = self.check_id

        result['CustomConfigs'] = []
        if self.custom_configs is not None:
            for k1 in self.custom_configs:
                result['CustomConfigs'].append(k1.to_map() if k1 else None)

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        result['RepairConfigs'] = []
        if self.repair_configs is not None:
            for k1 in self.repair_configs:
                result['RepairConfigs'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckId') is not None:
            self.check_id = m.get('CheckId')

        self.custom_configs = []
        if m.get('CustomConfigs') is not None:
            for k1 in m.get('CustomConfigs'):
                temp_model = main_models.ChangeCheckCustomConfigRequestCustomConfigs()
                self.custom_configs.append(temp_model.from_map(k1))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        self.repair_configs = []
        if m.get('RepairConfigs') is not None:
            for k1 in m.get('RepairConfigs'):
                temp_model = main_models.ChangeCheckCustomConfigRequestRepairConfigs()
                self.repair_configs.append(temp_model.from_map(k1))

        return self

class ChangeCheckCustomConfigRequestRepairConfigs(DaraModel):
    def __init__(
        self,
        flow_id: str = None,
        name: str = None,
        operation: str = None,
        value: str = None,
    ):
        # The ID of the fixing process.
        self.flow_id = flow_id
        # The name of the parameter required for fixing a risk item, which is unique in a check item.
        self.name = name
        # The operation that you want to perform on the custom configuration item. This parameter is required only if you want to delete the custom configuration item. To delete the custom configuration item, set the value to DELETE.
        self.operation = operation
        # The value of the parameter required for fixing a risk item. The value is a string.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id

        if self.name is not None:
            result['Name'] = self.name

        if self.operation is not None:
            result['Operation'] = self.operation

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Operation') is not None:
            self.operation = m.get('Operation')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ChangeCheckCustomConfigRequestCustomConfigs(DaraModel):
    def __init__(
        self,
        name: str = None,
        operation: str = None,
        value: str = None,
    ):
        # The name of the custom configuration item. The name of a custom configuration item is unique in a check item.
        self.name = name
        # The operation that you want to perform on the custom configuration item. This parameter is required only if you want to delete the custom configuration item. To delete the custom configuration item, set the value to DELETE.
        self.operation = operation
        # The value of the custom configuration item. The value is a string.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.operation is not None:
            result['Operation'] = self.operation

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Operation') is not None:
            self.operation = m.get('Operation')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

