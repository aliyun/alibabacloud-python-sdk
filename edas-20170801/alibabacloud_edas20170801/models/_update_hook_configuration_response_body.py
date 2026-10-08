# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_edas20170801 import models as main_models
from darabonba.model import DaraModel

class UpdateHookConfigurationResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        hooks_configuration: List[main_models.UpdateHookConfigurationResponseBodyHooksConfiguration] = None,
        message: str = None,
        request_id: str = None,
    ):
        # The HTTP status code that is returned.
        self.code = code
        # The information about the mounted script.
        self.hooks_configuration = hooks_configuration
        # The message that is returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.hooks_configuration:
            for v1 in self.hooks_configuration:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['HooksConfiguration'] = []
        if self.hooks_configuration is not None:
            for k1 in self.hooks_configuration:
                result['HooksConfiguration'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.hooks_configuration = []
        if m.get('HooksConfiguration') is not None:
            for k1 in m.get('HooksConfiguration'):
                temp_model = main_models.UpdateHookConfigurationResponseBodyHooksConfiguration()
                self.hooks_configuration.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class UpdateHookConfigurationResponseBodyHooksConfiguration(DaraModel):
    def __init__(
        self,
        ignore_fail: bool = None,
        name: str = None,
        script: str = None,
    ):
        # Indicates whether a mount failure is ignored. Valid values:
        # 
        # - **true**: A mount failure is ignored.
        # 
        # - **false**: A mount failure is not ignored.
        self.ignore_fail = ignore_fail
        # The name of the mounted script.
        self.name = name
        # The content of the mounted script.
        self.script = script

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ignore_fail is not None:
            result['IgnoreFail'] = self.ignore_fail

        if self.name is not None:
            result['Name'] = self.name

        if self.script is not None:
            result['Script'] = self.script

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IgnoreFail') is not None:
            self.ignore_fail = m.get('IgnoreFail')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Script') is not None:
            self.script = m.get('Script')

        return self

