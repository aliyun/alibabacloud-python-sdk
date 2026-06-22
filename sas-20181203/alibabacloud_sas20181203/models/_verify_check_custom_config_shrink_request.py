# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class VerifyCheckCustomConfigShrinkRequest(DaraModel):
    def __init__(
        self,
        check_id: int = None,
        custom_check_config_shrink: str = None,
        custom_configs: List[main_models.VerifyCheckCustomConfigShrinkRequestCustomConfigs] = None,
        repair_configs: List[main_models.VerifyCheckCustomConfigShrinkRequestRepairConfigs] = None,
        type: str = None,
    ):
        # The ID of the check item.
        self.check_id = check_id
        # The input parameters for custom check item validation.
        self.custom_check_config_shrink = custom_check_config_shrink
        # The list of custom parameter configuration items for the check item.
        self.custom_configs = custom_configs
        # The repair parameters supported by the repair feature of the check item.
        self.repair_configs = repair_configs
        # The validation type for Threat Detection Service parameters. Valid values:
        # - **REPAIR_CONFIG**: repair and custom parameter validation (default).
        # - **CHECK_ITEM_CONFIG**: custom check item validation.
        self.type = type

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

        if self.custom_check_config_shrink is not None:
            result['CustomCheckConfig'] = self.custom_check_config_shrink

        result['CustomConfigs'] = []
        if self.custom_configs is not None:
            for k1 in self.custom_configs:
                result['CustomConfigs'].append(k1.to_map() if k1 else None)

        result['RepairConfigs'] = []
        if self.repair_configs is not None:
            for k1 in self.repair_configs:
                result['RepairConfigs'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckId') is not None:
            self.check_id = m.get('CheckId')

        if m.get('CustomCheckConfig') is not None:
            self.custom_check_config_shrink = m.get('CustomCheckConfig')

        self.custom_configs = []
        if m.get('CustomConfigs') is not None:
            for k1 in m.get('CustomConfigs'):
                temp_model = main_models.VerifyCheckCustomConfigShrinkRequestCustomConfigs()
                self.custom_configs.append(temp_model.from_map(k1))

        self.repair_configs = []
        if m.get('RepairConfigs') is not None:
            for k1 in m.get('RepairConfigs'):
                temp_model = main_models.VerifyCheckCustomConfigShrinkRequestRepairConfigs()
                self.repair_configs.append(temp_model.from_map(k1))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class VerifyCheckCustomConfigShrinkRequestRepairConfigs(DaraModel):
    def __init__(
        self,
        flow_id: str = None,
        name: str = None,
        operation: str = None,
        value: str = None,
    ):
        # The ID of the repair flow that corresponds to the repair operation.
        self.flow_id = flow_id
        # The name of the repair parameter for the check item. The name is unique within the check item.
        self.name = name
        # The operation type of the custom configuration item for the check item. Set this parameter to DELETE only for deletion operations. You do not need to specify this parameter for creation or update operations.
        self.operation = operation
        # The user-configured value string of the repair configuration item for the check item.
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

class VerifyCheckCustomConfigShrinkRequestCustomConfigs(DaraModel):
    def __init__(
        self,
        name: str = None,
        operation: str = None,
        value: str = None,
    ):
        # The name of the custom configuration item for the check item. The name is unique within the check item.
        self.name = name
        # The operation type of the custom configuration item for the check item. Set this parameter to DELETE only for deletion operations. You do not need to specify this parameter for creation or update operations.
        self.operation = operation
        # The user-configured value string of the custom configuration item for the check item.
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

