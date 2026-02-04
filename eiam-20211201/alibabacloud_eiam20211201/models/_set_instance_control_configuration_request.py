# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class SetInstanceControlConfigurationRequest(DaraModel):
    def __init__(
        self,
        control_elements: List[main_models.SetInstanceControlConfigurationRequestControlElements] = None,
        instance_id: str = None,
    ):
        # 实例控制项。
        self.control_elements = control_elements
        # IDaaS EIAM实例的ID。
        # 
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        if self.control_elements:
            for v1 in self.control_elements:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ControlElements'] = []
        if self.control_elements is not None:
            for k1 in self.control_elements:
                result['ControlElements'].append(k1.to_map() if k1 else None)

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.control_elements = []
        if m.get('ControlElements') is not None:
            for k1 in m.get('ControlElements'):
                temp_model = main_models.SetInstanceControlConfigurationRequestControlElements()
                self.control_elements.append(temp_model.from_map(k1))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

class SetInstanceControlConfigurationRequestControlElements(DaraModel):
    def __init__(
        self,
        element_name: str = None,
        human_verification_config: main_models.SetInstanceControlConfigurationRequestControlElementsHumanVerificationConfig = None,
        status: str = None,
    ):
        # 实例控制项名称，如human_verification。
        self.element_name = element_name
        self.human_verification_config = human_verification_config
        # 实例控制项状态。
        self.status = status

    def validate(self):
        if self.human_verification_config:
            self.human_verification_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.element_name is not None:
            result['ElementName'] = self.element_name

        if self.human_verification_config is not None:
            result['HumanVerificationConfig'] = self.human_verification_config.to_map()

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ElementName') is not None:
            self.element_name = m.get('ElementName')

        if m.get('HumanVerificationConfig') is not None:
            temp_model = main_models.SetInstanceControlConfigurationRequestControlElementsHumanVerificationConfig()
            self.human_verification_config = temp_model.from_map(m.get('HumanVerificationConfig'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class SetInstanceControlConfigurationRequestControlElementsHumanVerificationConfig(DaraModel):
    def __init__(
        self,
        human_verification_type: str = None,
    ):
        self.human_verification_type = human_verification_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.human_verification_type is not None:
            result['HumanVerificationType'] = self.human_verification_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HumanVerificationType') is not None:
            self.human_verification_type = m.get('HumanVerificationType')

        return self

