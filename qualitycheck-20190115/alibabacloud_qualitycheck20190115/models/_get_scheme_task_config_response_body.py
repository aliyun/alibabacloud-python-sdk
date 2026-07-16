# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_qualitycheck20190115 import models as main_models
from darabonba.model import DaraModel

class GetSchemeTaskConfigResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetSchemeTaskConfigResponseBodyData = None,
        http_status_code: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        # Result code. **200** means success.
        # 
        # > Any other value means failure. The caller can use this field to identify the cause.
        self.code = code
        # Response data. See the additional notes below.
        self.data = data
        # HTTP status code
        self.http_status_code = http_status_code
        # Error details if the request failed. Returns successful if the request succeeded.
        self.message = message
        # Request ID
        self.request_id = request_id
        # Indicates whether the request succeeded. Use this field to check the result: true means success, false or null means failure.
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

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

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
            temp_model = main_models.GetSchemeTaskConfigResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetSchemeTaskConfigResponseBodyData(DaraModel):
    def __init__(
        self,
        asr_task_priority: int = None,
        assign_type: int = None,
        data_config: main_models.GetSchemeTaskConfigResponseBodyDataDataConfig = None,
        id: int = None,
        manual_review: int = None,
        mode_customization_id: str = None,
        model_name: str = None,
        name: str = None,
        scheme_id_list: List[int] = None,
        scheme_list: List[main_models.GetSchemeTaskConfigResponseBodyDataSchemeList] = None,
        scheme_task_config_id: int = None,
        source_data_type: str = None,
        status: str = None,
    ):
        # Task priority:
        # 
        # - 0 (low)
        # 
        # - 1 (medium)
        # 
        # - 2 (high)
        self.asr_task_priority = asr_task_priority
        # Assignment type
        self.assign_type = assign_type
        # Data configuration
        self.data_config = data_config
        # Quality inspection task ID
        self.id = id
        # Manual review
        self.manual_review = manual_review
        # Language model ID
        self.mode_customization_id = mode_customization_id
        # Language model name
        self.model_name = model_name
        # Quality inspection task name
        self.name = name
        # Quality inspection scheme IDs
        self.scheme_id_list = scheme_id_list
        # Quality inspection schemes
        self.scheme_list = scheme_list
        # Quality inspection task ID
        self.scheme_task_config_id = scheme_task_config_id
        # Quality inspection result type:
        # 
        # - 1: offline voice
        # 
        # - 2: offline text
        # 
        # - 3: real-time voice
        # 
        # - 4: real-time text
        # 
        # - 5: contact center secondary quality inspection
        # 
        # - 51: call center voice secondary quality inspection
        # 
        # - 52: call center text secondary quality inspection
        # 
        # - 11: dataset voice
        # 
        # - 12: dataset text
        self.source_data_type = source_data_type
        # Enable status. Valid values: 0 (disabled) or 1 (enabled)
        self.status = status

    def validate(self):
        if self.data_config:
            self.data_config.validate()
        if self.scheme_list:
            for v1 in self.scheme_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asr_task_priority is not None:
            result['AsrTaskPriority'] = self.asr_task_priority

        if self.assign_type is not None:
            result['AssignType'] = self.assign_type

        if self.data_config is not None:
            result['DataConfig'] = self.data_config.to_map()

        if self.id is not None:
            result['Id'] = self.id

        if self.manual_review is not None:
            result['ManualReview'] = self.manual_review

        if self.mode_customization_id is not None:
            result['ModeCustomizationId'] = self.mode_customization_id

        if self.model_name is not None:
            result['ModelName'] = self.model_name

        if self.name is not None:
            result['Name'] = self.name

        if self.scheme_id_list is not None:
            result['SchemeIdList'] = self.scheme_id_list

        result['SchemeList'] = []
        if self.scheme_list is not None:
            for k1 in self.scheme_list:
                result['SchemeList'].append(k1.to_map() if k1 else None)

        if self.scheme_task_config_id is not None:
            result['SchemeTaskConfigId'] = self.scheme_task_config_id

        if self.source_data_type is not None:
            result['SourceDataType'] = self.source_data_type

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AsrTaskPriority') is not None:
            self.asr_task_priority = m.get('AsrTaskPriority')

        if m.get('AssignType') is not None:
            self.assign_type = m.get('AssignType')

        if m.get('DataConfig') is not None:
            temp_model = main_models.GetSchemeTaskConfigResponseBodyDataDataConfig()
            self.data_config = temp_model.from_map(m.get('DataConfig'))

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('ManualReview') is not None:
            self.manual_review = m.get('ManualReview')

        if m.get('ModeCustomizationId') is not None:
            self.mode_customization_id = m.get('ModeCustomizationId')

        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SchemeIdList') is not None:
            self.scheme_id_list = m.get('SchemeIdList')

        self.scheme_list = []
        if m.get('SchemeList') is not None:
            for k1 in m.get('SchemeList'):
                temp_model = main_models.GetSchemeTaskConfigResponseBodyDataSchemeList()
                self.scheme_list.append(temp_model.from_map(k1))

        if m.get('SchemeTaskConfigId') is not None:
            self.scheme_task_config_id = m.get('SchemeTaskConfigId')

        if m.get('SourceDataType') is not None:
            self.source_data_type = m.get('SourceDataType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class GetSchemeTaskConfigResponseBodyDataSchemeList(DaraModel):
    def __init__(
        self,
        name: str = None,
        scheme_id: int = None,
    ):
        # Quality inspection scheme name
        self.name = name
        # Quality inspection scheme ID
        self.scheme_id = scheme_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.scheme_id is not None:
            result['SchemeId'] = self.scheme_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SchemeId') is not None:
            self.scheme_id = m.get('SchemeId')

        return self

class GetSchemeTaskConfigResponseBodyDataDataConfig(DaraModel):
    def __init__(
        self,
        assign_configs: List[main_models.GetSchemeTaskConfigResponseBodyDataDataConfigAssignConfigs] = None,
        data_sets: str = None,
        index: int = None,
        result_param: str = None,
    ):
        # Data screening items for on-the-fly recording
        self.assign_configs = assign_configs
        # Dataset task. Manage datasets.
        self.data_sets = data_sets
        # Index number
        self.index = index
        # JSON text for filtering conditions used in secondary quality inspection. For details, see the request parameters of the GetResult API.
        self.result_param = result_param

    def validate(self):
        if self.assign_configs:
            for v1 in self.assign_configs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AssignConfigs'] = []
        if self.assign_configs is not None:
            for k1 in self.assign_configs:
                result['AssignConfigs'].append(k1.to_map() if k1 else None)

        if self.data_sets is not None:
            result['DataSets'] = self.data_sets

        if self.index is not None:
            result['Index'] = self.index

        if self.result_param is not None:
            result['ResultParam'] = self.result_param

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.assign_configs = []
        if m.get('AssignConfigs') is not None:
            for k1 in m.get('AssignConfigs'):
                temp_model = main_models.GetSchemeTaskConfigResponseBodyDataDataConfigAssignConfigs()
                self.assign_configs.append(temp_model.from_map(k1))

        if m.get('DataSets') is not None:
            self.data_sets = m.get('DataSets')

        if m.get('Index') is not None:
            self.index = m.get('Index')

        if m.get('ResultParam') is not None:
            self.result_param = m.get('ResultParam')

        return self

class GetSchemeTaskConfigResponseBodyDataDataConfigAssignConfigs(DaraModel):
    def __init__(
        self,
        assign_config_contests: List[main_models.GetSchemeTaskConfigResponseBodyDataDataConfigAssignConfigsAssignConfigContests] = None,
    ):
        # Parameter matching configurations for on-the-fly recording
        self.assign_config_contests = assign_config_contests

    def validate(self):
        if self.assign_config_contests:
            for v1 in self.assign_config_contests:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AssignConfigContests'] = []
        if self.assign_config_contests is not None:
            for k1 in self.assign_config_contests:
                result['AssignConfigContests'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.assign_config_contests = []
        if m.get('AssignConfigContests') is not None:
            for k1 in m.get('AssignConfigContests'):
                temp_model = main_models.GetSchemeTaskConfigResponseBodyDataDataConfigAssignConfigsAssignConfigContests()
                self.assign_config_contests.append(temp_model.from_map(k1))

        return self

class GetSchemeTaskConfigResponseBodyDataDataConfigAssignConfigsAssignConfigContests(DaraModel):
    def __init__(
        self,
        data_type: int = None,
        list_object: List[Any] = None,
        name: str = None,
        symbol: int = None,
        value: str = None,
    ):
        # Type of the value
        # 
        # - 0: String
        # 
        # - 1: Number
        # 
        # - 2: List (use list type for all parameter values when using =)
        # 
        # - 3: Date
        # 
        # - 4: List_Json
        self.data_type = data_type
        # List of on-the-fly recording data
        self.list_object = list_object
        # Check item name
        self.name = name
        # Operator
        # 
        # - 1: ==
        # 
        # - 2: >
        # 
        # - 3: <
        # 
        # - 4: range
        # 
        # - 5: >=
        # 
        # - 6: <=
        # 
        # - 7: !=
        # 
        # - 8: null
        # 
        # - 9: not null
        # 
        # - 10: contains
        # 
        # - 11: does not contain
        self.symbol = symbol
        # Matching value for on-the-fly recording data
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_type is not None:
            result['DataType'] = self.data_type

        if self.list_object is not None:
            result['ListObject'] = self.list_object

        if self.name is not None:
            result['Name'] = self.name

        if self.symbol is not None:
            result['Symbol'] = self.symbol

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')

        if m.get('ListObject') is not None:
            self.list_object = m.get('ListObject')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Symbol') is not None:
            self.symbol = m.get('Symbol')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

