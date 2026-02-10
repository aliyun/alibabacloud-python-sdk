# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class GetCheckDetailResponseBody(DaraModel):
    def __init__(
        self,
        assist_info: main_models.GetCheckDetailResponseBodyAssistInfo = None,
        custom_configs: List[main_models.GetCheckDetailResponseBodyCustomConfigs] = None,
        description: main_models.GetCheckDetailResponseBodyDescription = None,
        repair_reset: str = None,
        repair_setting: main_models.GetCheckDetailResponseBodyRepairSetting = None,
        repair_support_type: int = None,
        request_id: str = None,
        solution: main_models.GetCheckDetailResponseBodySolution = None,
    ):
        # The help information about the check item.
        self.assist_info = assist_info
        # The custom configuration items of the check item.
        self.custom_configs = custom_configs
        # The description of the check item.
        self.description = description
        # >  This parameter is deprecated.
        self.repair_reset = repair_reset
        # The fixing parameter configurations of the check item.
        self.repair_setting = repair_setting
        # >  This parameter is deprecated.
        self.repair_support_type = repair_support_type
        # The request ID.
        self.request_id = request_id
        # The solution to handle the risk item.
        self.solution = solution

    def validate(self):
        if self.assist_info:
            self.assist_info.validate()
        if self.custom_configs:
            for v1 in self.custom_configs:
                 if v1:
                    v1.validate()
        if self.description:
            self.description.validate()
        if self.repair_setting:
            self.repair_setting.validate()
        if self.solution:
            self.solution.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.assist_info is not None:
            result['AssistInfo'] = self.assist_info.to_map()

        result['CustomConfigs'] = []
        if self.custom_configs is not None:
            for k1 in self.custom_configs:
                result['CustomConfigs'].append(k1.to_map() if k1 else None)

        if self.description is not None:
            result['Description'] = self.description.to_map()

        if self.repair_reset is not None:
            result['RepairReset'] = self.repair_reset

        if self.repair_setting is not None:
            result['RepairSetting'] = self.repair_setting.to_map()

        if self.repair_support_type is not None:
            result['RepairSupportType'] = self.repair_support_type

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.solution is not None:
            result['Solution'] = self.solution.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssistInfo') is not None:
            temp_model = main_models.GetCheckDetailResponseBodyAssistInfo()
            self.assist_info = temp_model.from_map(m.get('AssistInfo'))

        self.custom_configs = []
        if m.get('CustomConfigs') is not None:
            for k1 in m.get('CustomConfigs'):
                temp_model = main_models.GetCheckDetailResponseBodyCustomConfigs()
                self.custom_configs.append(temp_model.from_map(k1))

        if m.get('Description') is not None:
            temp_model = main_models.GetCheckDetailResponseBodyDescription()
            self.description = temp_model.from_map(m.get('Description'))

        if m.get('RepairReset') is not None:
            self.repair_reset = m.get('RepairReset')

        if m.get('RepairSetting') is not None:
            temp_model = main_models.GetCheckDetailResponseBodyRepairSetting()
            self.repair_setting = temp_model.from_map(m.get('RepairSetting'))

        if m.get('RepairSupportType') is not None:
            self.repair_support_type = m.get('RepairSupportType')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Solution') is not None:
            temp_model = main_models.GetCheckDetailResponseBodySolution()
            self.solution = temp_model.from_map(m.get('Solution'))

        return self

class GetCheckDetailResponseBodySolution(DaraModel):
    def __init__(
        self,
        link: str = None,
        type: str = None,
        value: str = None,
    ):
        # The link to the solution to handle the risk item when the Type parameter is set to link.
        self.link = link
        # The type of the solution to handle the risk item. Valid values:
        # 
        # *   **text**
        # *   **link**
        self.type = type
        # The content of the solution to handle the risk item when the Type parameter is set to text.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.link is not None:
            result['Link'] = self.link

        if self.type is not None:
            result['Type'] = self.type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Link') is not None:
            self.link = m.get('Link')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetCheckDetailResponseBodyRepairSetting(DaraModel):
    def __init__(
        self,
        flow_step: List[main_models.GetCheckDetailResponseBodyRepairSettingFlowStep] = None,
        repair_configs: List[main_models.GetCheckDetailResponseBodyRepairSettingRepairConfigs] = None,
        repair_reset: bool = None,
        repair_support: bool = None,
        repair_support_type: int = None,
    ):
        # The description of the fixing workflow.
        self.flow_step = flow_step
        # The configurations of the fixing parameters.
        self.repair_configs = repair_configs
        # Indicates whether a restart is required after the fixing. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.repair_reset = repair_reset
        # Indicates whether the check item supports the quick fix feature. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.repair_support = repair_support
        # The fixing type that is supported. Valid values:
        # 
        # *   **1**: The fixing and rollback are supported.
        # *   **2**: The fixing is supported, but the rollback is not supported.
        # *   **3**: The fixing must be performed on a third-party platform.
        self.repair_support_type = repair_support_type

    def validate(self):
        if self.flow_step:
            for v1 in self.flow_step:
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
        result['FlowStep'] = []
        if self.flow_step is not None:
            for k1 in self.flow_step:
                result['FlowStep'].append(k1.to_map() if k1 else None)

        result['RepairConfigs'] = []
        if self.repair_configs is not None:
            for k1 in self.repair_configs:
                result['RepairConfigs'].append(k1.to_map() if k1 else None)

        if self.repair_reset is not None:
            result['RepairReset'] = self.repair_reset

        if self.repair_support is not None:
            result['RepairSupport'] = self.repair_support

        if self.repair_support_type is not None:
            result['RepairSupportType'] = self.repair_support_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.flow_step = []
        if m.get('FlowStep') is not None:
            for k1 in m.get('FlowStep'):
                temp_model = main_models.GetCheckDetailResponseBodyRepairSettingFlowStep()
                self.flow_step.append(temp_model.from_map(k1))

        self.repair_configs = []
        if m.get('RepairConfigs') is not None:
            for k1 in m.get('RepairConfigs'):
                temp_model = main_models.GetCheckDetailResponseBodyRepairSettingRepairConfigs()
                self.repair_configs.append(temp_model.from_map(k1))

        if m.get('RepairReset') is not None:
            self.repair_reset = m.get('RepairReset')

        if m.get('RepairSupport') is not None:
            self.repair_support = m.get('RepairSupport')

        if m.get('RepairSupportType') is not None:
            self.repair_support_type = m.get('RepairSupportType')

        return self

class GetCheckDetailResponseBodyRepairSettingRepairConfigs(DaraModel):
    def __init__(
        self,
        console_param_type: str = None,
        custom_flag: bool = None,
        data_transform_type: str = None,
        default_value: str = None,
        empty_param_switch: str = None,
        exclusive_name: List[str] = None,
        flow_id: str = None,
        name: str = None,
        show_name: str = None,
        type_define: str = None,
        usage_type: str = None,
        value: str = None,
    ):
        # Indicates whether the value of the parameter is displayed in the console. Valid values:
        # 
        # *   0: The historical value and real-time value of the parameter are displayed.
        # *   1: Only the real-time value of the parameter is displayed.
        # *   2: The value of the parameter is not displayed in the console.
        self.console_param_type = console_param_type
        # Indicates whether custom configurations of the fixing parameters are supported. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.custom_flag = custom_flag
        # Indicates whether data needs to be encrypted during transmission. Valid values:
        # 
        # *   0: Data does not need to be encrypted during transmission.
        # *   1: Data needs to be encrypted during transmission.
        # *   2: Data needs to be encrypted during transmission, and the user must perform secondary confirmation.
        self.data_transform_type = data_transform_type
        # The default value of the parameter. The value is a string.
        self.default_value = default_value
        # Indicates whether this parameter is specified by the user. Valid values:
        # 
        # *   0: The default value is used.
        # *   1: This parameter is required, and no default value is specified.
        # *   2: This parameter can be left empty.
        self.empty_param_switch = empty_param_switch
        # The fixing parameters that are not compatible with this parameter.
        self.exclusive_name = exclusive_name
        # The ID of the fixing workflow.
        self.flow_id = flow_id
        # The name of the parameter. The name must be unique within the check item.
        self.name = name
        # The display name of the parameter.
        self.show_name = show_name
        # The type of the parameter. The value is a JSON string.
        self.type_define = type_define
        # The type of the parameter. Valid values:
        # 
        # *   1: asset parameters that are required during fixing.
        # *   2: user-provided parameters that are required during fixing.
        # *   3: parameters that are temporarily provided by the user.
        self.usage_type = usage_type
        # The user-configured value of the parameter. The value is a string.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.console_param_type is not None:
            result['ConsoleParamType'] = self.console_param_type

        if self.custom_flag is not None:
            result['CustomFlag'] = self.custom_flag

        if self.data_transform_type is not None:
            result['DataTransformType'] = self.data_transform_type

        if self.default_value is not None:
            result['DefaultValue'] = self.default_value

        if self.empty_param_switch is not None:
            result['EmptyParamSwitch'] = self.empty_param_switch

        if self.exclusive_name is not None:
            result['ExclusiveName'] = self.exclusive_name

        if self.flow_id is not None:
            result['FlowId'] = self.flow_id

        if self.name is not None:
            result['Name'] = self.name

        if self.show_name is not None:
            result['ShowName'] = self.show_name

        if self.type_define is not None:
            result['TypeDefine'] = self.type_define

        if self.usage_type is not None:
            result['UsageType'] = self.usage_type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleParamType') is not None:
            self.console_param_type = m.get('ConsoleParamType')

        if m.get('CustomFlag') is not None:
            self.custom_flag = m.get('CustomFlag')

        if m.get('DataTransformType') is not None:
            self.data_transform_type = m.get('DataTransformType')

        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')

        if m.get('EmptyParamSwitch') is not None:
            self.empty_param_switch = m.get('EmptyParamSwitch')

        if m.get('ExclusiveName') is not None:
            self.exclusive_name = m.get('ExclusiveName')

        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ShowName') is not None:
            self.show_name = m.get('ShowName')

        if m.get('TypeDefine') is not None:
            self.type_define = m.get('TypeDefine')

        if m.get('UsageType') is not None:
            self.usage_type = m.get('UsageType')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetCheckDetailResponseBodyRepairSettingFlowStep(DaraModel):
    def __init__(
        self,
        show_text: str = None,
        step: str = None,
    ):
        # The text description of the fixing step.
        self.show_text = show_text
        # The sequence number of the fixing step.
        self.step = step

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.show_text is not None:
            result['ShowText'] = self.show_text

        if self.step is not None:
            result['Step'] = self.step

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ShowText') is not None:
            self.show_text = m.get('ShowText')

        if m.get('Step') is not None:
            self.step = m.get('Step')

        return self

class GetCheckDetailResponseBodyDescription(DaraModel):
    def __init__(
        self,
        link: str = None,
        type: str = None,
        value: str = None,
    ):
        # The link to the description of the check item.
        self.link = link
        # The description type of the check item. The value is fixed as text.
        self.type = type
        # The content in the description of the check item.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.link is not None:
            result['Link'] = self.link

        if self.type is not None:
            result['Type'] = self.type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Link') is not None:
            self.link = m.get('Link')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetCheckDetailResponseBodyCustomConfigs(DaraModel):
    def __init__(
        self,
        default_value: str = None,
        name: str = None,
        show_name: str = None,
        type_define: str = None,
        value: str = None,
    ):
        # The default value of the custom configuration item. The value is a string.
        self.default_value = default_value
        # The name of the custom configuration item, which is unique in a check item.
        self.name = name
        # The display name of the custom configuration item for internationalization.
        self.show_name = show_name
        # The type of the custom configuration item. The value is a JSON string.
        self.type_define = type_define
        # The value of the custom configuration item. The value is a string.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value

        if self.name is not None:
            result['Name'] = self.name

        if self.show_name is not None:
            result['ShowName'] = self.show_name

        if self.type_define is not None:
            result['TypeDefine'] = self.type_define

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ShowName') is not None:
            self.show_name = m.get('ShowName')

        if m.get('TypeDefine') is not None:
            self.type_define = m.get('TypeDefine')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetCheckDetailResponseBodyAssistInfo(DaraModel):
    def __init__(
        self,
        link: str = None,
        type: str = None,
        value: str = None,
    ):
        # The link to the help information about the risk item when the Type parameter is set to link.
        self.link = link
        # The type of the help information about the risk item. Valid values:
        # 
        # *   **text**
        # *   **link**
        self.type = type
        # The content in the help information about the risk item when the Type parameter is set to text.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.link is not None:
            result['Link'] = self.link

        if self.type is not None:
            result['Type'] = self.type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Link') is not None:
            self.link = m.get('Link')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

