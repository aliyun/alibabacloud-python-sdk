# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class GetInstanceControlConfigurationResponseBody(DaraModel):
    def __init__(
        self,
        instance_control_configuration: main_models.GetInstanceControlConfigurationResponseBodyInstanceControlConfiguration = None,
        request_id: str = None,
    ):
        self.instance_control_configuration = instance_control_configuration
        self.request_id = request_id

    def validate(self):
        if self.instance_control_configuration:
            self.instance_control_configuration.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_control_configuration is not None:
            result['InstanceControlConfiguration'] = self.instance_control_configuration.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceControlConfiguration') is not None:
            temp_model = main_models.GetInstanceControlConfigurationResponseBodyInstanceControlConfiguration()
            self.instance_control_configuration = temp_model.from_map(m.get('InstanceControlConfiguration'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetInstanceControlConfigurationResponseBodyInstanceControlConfiguration(DaraModel):
    def __init__(
        self,
        control_elements: List[main_models.GetInstanceControlConfigurationResponseBodyInstanceControlConfigurationControlElements] = None,
    ):
        # 实例控制配置项
        self.control_elements = control_elements

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.control_elements = []
        if m.get('ControlElements') is not None:
            for k1 in m.get('ControlElements'):
                temp_model = main_models.GetInstanceControlConfigurationResponseBodyInstanceControlConfigurationControlElements()
                self.control_elements.append(temp_model.from_map(k1))

        return self

class GetInstanceControlConfigurationResponseBodyInstanceControlConfigurationControlElements(DaraModel):
    def __init__(
        self,
        element_name: str = None,
        human_verification_config: main_models.GetInstanceControlConfigurationResponseBodyInstanceControlConfigurationControlElementsHumanVerificationConfig = None,
        status: str = None,
    ):
        # 实例控制项名称，如human_verification。
        self.element_name = element_name
        self.human_verification_config = human_verification_config
        # 实例控制项状态，enabled或者disabled。
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
            temp_model = main_models.GetInstanceControlConfigurationResponseBodyInstanceControlConfigurationControlElementsHumanVerificationConfig()
            self.human_verification_config = temp_model.from_map(m.get('HumanVerificationConfig'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class GetInstanceControlConfigurationResponseBodyInstanceControlConfigurationControlElementsHumanVerificationConfig(DaraModel):
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

