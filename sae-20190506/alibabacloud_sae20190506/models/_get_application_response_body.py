# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class GetApplicationResponseBody(DaraModel):
    def __init__(
        self,
        application: main_models.GetApplicationResponseBodyApplication = None,
        message: str = None,
        request_id: str = None,
        trace_id: str = None,
    ):
        # The details of the application.
        self.application = application
        # The additional information returned. Valid values:
        # 
        # *   When a request is successful, **success**is returned.
        # *   An error code is returned when a request failed.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # The ID of the trace. The ID is used to query the details of a request.
        self.trace_id = trace_id

    def validate(self):
        if self.application:
            self.application.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application is not None:
            result['Application'] = self.application.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.trace_id is not None:
            result['TraceId'] = self.trace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Application') is not None:
            temp_model = main_models.GetApplicationResponseBodyApplication()
            self.application = temp_model.from_map(m.get('Application'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')

        return self

class GetApplicationResponseBodyApplication(DaraModel):
    def __init__(
        self,
        app_description: str = None,
        app_id: str = None,
        app_name: str = None,
        base_app_id: str = None,
        cpu: int = None,
        instances: int = None,
        is_stateful: bool = None,
        mem: int = None,
        mse_enabled: bool = None,
        mse_namespace_id: str = None,
        namespace_id: str = None,
        programming_language: str = None,
        running_instances: int = None,
        scale_rule_enabled: str = None,
        scale_rule_type: str = None,
    ):
        # The description of the application.
        self.app_description = app_description
        # The application ID.
        self.app_id = app_id
        # The application name.
        self.app_name = app_name
        # The ID of the basic application.
        self.base_app_id = base_app_id
        # The CPU specifications that are required for each instance. Unit: millicores. This parameter cannot be set to 0. Valid values:
        # 
        # *   **500**
        # *   **1000**
        # *   **2000**
        # *   **4000**
        # *   **8000**
        # *   **12000**
        # *   **16000**
        # *   **32000**
        self.cpu = cpu
        # The number of application instances.
        self.instances = instances
        self.is_stateful = is_stateful
        # The memory size that is required by each instance. Unit: MB. This parameter cannot be set to 0. The values of this parameter correspond to the values of the Cpu parameter:
        # 
        # *   This parameter is set to **1024** if the Cpu parameter is set to 500 or 1000.
        # *   This parameter is set to **2048** if the Cpu parameter is set to 500, 1000, or 2000.
        # *   This parameter is set to **4096** if the Cpu parameter is set to 1000, 2000, or 4000.
        # *   This parameter is set to **8192** if the Cpu parameter is set to 2000, 4000, or 8000.
        # *   This parameter is set to **12288** if the Cpu parameter is set to 12000.
        # *   This parameter is set to **16384** if the Cpu parameter is set to 4000, 8000, or 16000.
        # *   This parameter is set to **24576** if the Cpu parameter is set to 12000.
        # *   This parameter is set to **32768** if the Cpu parameter is set to 16000.
        # *   This parameter is set to **65536** if the Cpu parameter is set to 8000, 16000, or 32000.
        # *   This parameter is set to **131072** if the Cpu parameter is set to 32000.
        self.mem = mem
        # Specifies whether to enable WebAssembly Filter. Valid values:
        # 
        # *   true: enables this parameter.
        # *   false: disables this parameter.
        self.mse_enabled = mse_enabled
        # The ID of the namespace to which the MSE instance belongs.
        self.mse_namespace_id = mse_namespace_id
        # The namespace ID.
        self.namespace_id = namespace_id
        # The programming language that is used to create the application. Valid values:
        # 
        # *   **java** :Java.
        # *   **php**: PHP.
        # *   **other**: other programming languages, such as Python, C++, Go, .NET, and Node.js
        self.programming_language = programming_language
        # The number of application instances that are running.
        self.running_instances = running_instances
        # Indicates whether the auto scaling policy is enabled. Valid values:
        # 
        # *   **true**: The auto scaling policy is enabled.
        # *   **false**: The auto scaling policy is disabled.
        self.scale_rule_enabled = scale_rule_enabled
        # The type of the auto scaling policy. Valid values:
        # 
        # *   **timing**: a scheduled auto scaling policy.
        # *   **metric**: a metric-based auto scaling policy.
        # *   **mix**: a hybrid auto scaling policy.
        self.scale_rule_type = scale_rule_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_description is not None:
            result['AppDescription'] = self.app_description

        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.base_app_id is not None:
            result['BaseAppId'] = self.base_app_id

        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.instances is not None:
            result['Instances'] = self.instances

        if self.is_stateful is not None:
            result['IsStateful'] = self.is_stateful

        if self.mem is not None:
            result['Mem'] = self.mem

        if self.mse_enabled is not None:
            result['MseEnabled'] = self.mse_enabled

        if self.mse_namespace_id is not None:
            result['MseNamespaceId'] = self.mse_namespace_id

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        if self.programming_language is not None:
            result['ProgrammingLanguage'] = self.programming_language

        if self.running_instances is not None:
            result['RunningInstances'] = self.running_instances

        if self.scale_rule_enabled is not None:
            result['ScaleRuleEnabled'] = self.scale_rule_enabled

        if self.scale_rule_type is not None:
            result['ScaleRuleType'] = self.scale_rule_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppDescription') is not None:
            self.app_description = m.get('AppDescription')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('BaseAppId') is not None:
            self.base_app_id = m.get('BaseAppId')

        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('Instances') is not None:
            self.instances = m.get('Instances')

        if m.get('IsStateful') is not None:
            self.is_stateful = m.get('IsStateful')

        if m.get('Mem') is not None:
            self.mem = m.get('Mem')

        if m.get('MseEnabled') is not None:
            self.mse_enabled = m.get('MseEnabled')

        if m.get('MseNamespaceId') is not None:
            self.mse_namespace_id = m.get('MseNamespaceId')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        if m.get('ProgrammingLanguage') is not None:
            self.programming_language = m.get('ProgrammingLanguage')

        if m.get('RunningInstances') is not None:
            self.running_instances = m.get('RunningInstances')

        if m.get('ScaleRuleEnabled') is not None:
            self.scale_rule_enabled = m.get('ScaleRuleEnabled')

        if m.get('ScaleRuleType') is not None:
            self.scale_rule_type = m.get('ScaleRuleType')

        return self

