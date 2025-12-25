# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_qualitycheck20190115 import models as main_models
from darabonba.model import DaraModel

class GetCustomizationConfigListResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetCustomizationConfigListResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
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
            temp_model = main_models.GetCustomizationConfigListResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetCustomizationConfigListResponseBodyData(DaraModel):
    def __init__(
        self,
        model_customization_data_set_po: List[main_models.GetCustomizationConfigListResponseBodyDataModelCustomizationDataSetPo] = None,
    ):
        self.model_customization_data_set_po = model_customization_data_set_po

    def validate(self):
        if self.model_customization_data_set_po:
            for v1 in self.model_customization_data_set_po:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ModelCustomizationDataSetPo'] = []
        if self.model_customization_data_set_po is not None:
            for k1 in self.model_customization_data_set_po:
                result['ModelCustomizationDataSetPo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.model_customization_data_set_po = []
        if m.get('ModelCustomizationDataSetPo') is not None:
            for k1 in m.get('ModelCustomizationDataSetPo'):
                temp_model = main_models.GetCustomizationConfigListResponseBodyDataModelCustomizationDataSetPo()
                self.model_customization_data_set_po.append(temp_model.from_map(k1))

        return self

class GetCustomizationConfigListResponseBodyDataModelCustomizationDataSetPo(DaraModel):
    def __init__(
        self,
        asr_version: int = None,
        create_time: str = None,
        mode_customization_id: str = None,
        model_id: int = None,
        model_name: str = None,
        model_status: int = None,
        task_type: int = None,
    ):
        self.asr_version = asr_version
        self.create_time = create_time
        self.mode_customization_id = mode_customization_id
        self.model_id = model_id
        self.model_name = model_name
        self.model_status = model_status
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asr_version is not None:
            result['AsrVersion'] = self.asr_version

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.mode_customization_id is not None:
            result['ModeCustomizationId'] = self.mode_customization_id

        if self.model_id is not None:
            result['ModelId'] = self.model_id

        if self.model_name is not None:
            result['ModelName'] = self.model_name

        if self.model_status is not None:
            result['ModelStatus'] = self.model_status

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AsrVersion') is not None:
            self.asr_version = m.get('AsrVersion')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('ModeCustomizationId') is not None:
            self.mode_customization_id = m.get('ModeCustomizationId')

        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')

        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')

        if m.get('ModelStatus') is not None:
            self.model_status = m.get('ModelStatus')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self

