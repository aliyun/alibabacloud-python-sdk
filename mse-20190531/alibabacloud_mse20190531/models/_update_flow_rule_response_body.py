# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class UpdateFlowRuleResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.UpdateFlowRuleResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code.
        self.code = code
        # The data of the node.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        # 
        # Valid values:
        # 
        # *   true
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     The request was successful.
        # 
        #     <!-- -->
        # 
        # *   false
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     The request failed.
        # 
        #     <!-- -->
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
            temp_model = main_models.UpdateFlowRuleResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class UpdateFlowRuleResponseBodyData(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        control_behavior: int = None,
        enable: bool = None,
        id: int = None,
        limit_app: str = None,
        max_queueing_time_ms: int = None,
        namespace: str = None,
        resource: str = None,
        threshold: float = None,
    ):
        # The application ID.
        self.app_id = app_id
        # The application name.
        self.app_name = app_name
        # The throttling effect.
        # 
        # Valid values:
        # 
        # *   0
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     fast failure
        # 
        #     <!-- -->
        # 
        # *   2
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     in queue
        # 
        #     <!-- -->
        self.control_behavior = control_behavior
        # Indicates whether the rule was enabled.
        # 
        # Valid value:
        # 
        # *   true
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   false
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.enable = enable
        # The rule ID.
        self.id = id
        self.limit_app = limit_app
        # The timeout period for queuing when the value of ControlBehavior is set to 2. Unit: milliseconds.
        self.max_queueing_time_ms = max_queueing_time_ms
        # The namespace.
        self.namespace = namespace
        # The name of the API resource.
        self.resource = resource
        # The throttling threshold.
        self.threshold = threshold

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.control_behavior is not None:
            result['ControlBehavior'] = self.control_behavior

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.id is not None:
            result['Id'] = self.id

        if self.limit_app is not None:
            result['LimitApp'] = self.limit_app

        if self.max_queueing_time_ms is not None:
            result['MaxQueueingTimeMs'] = self.max_queueing_time_ms

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.resource is not None:
            result['Resource'] = self.resource

        if self.threshold is not None:
            result['Threshold'] = self.threshold

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('ControlBehavior') is not None:
            self.control_behavior = m.get('ControlBehavior')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('LimitApp') is not None:
            self.limit_app = m.get('LimitApp')

        if m.get('MaxQueueingTimeMs') is not None:
            self.max_queueing_time_ms = m.get('MaxQueueingTimeMs')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('Resource') is not None:
            self.resource = m.get('Resource')

        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')

        return self

