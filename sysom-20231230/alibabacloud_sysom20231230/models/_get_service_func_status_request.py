# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sysom20231230 import models as main_models
from darabonba.model import DaraModel

class GetServiceFuncStatusRequest(DaraModel):
    def __init__(
        self,
        x_debug_id: str = None,
        channel: str = None,
        params: main_models.GetServiceFuncStatusRequestParams = None,
        service_name: str = None,
        x_sysom_invoke_source: str = None,
    ):
        self.x_debug_id = x_debug_id
        # The channel name.
        # 
        # This parameter is required.
        self.channel = channel
        # The diagnostic parameters. Different types of diagnostics require different diagnostic parameters. You can use this field to filter records whose parameters match the specified values.
        # 
        # This parameter is required.
        self.params = params
        # The service name.
        # 
        # This parameter is required.
        self.service_name = service_name
        self.x_sysom_invoke_source = x_sysom_invoke_source

    def validate(self):
        if self.params:
            self.params.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.x_debug_id is not None:
            result['X-Debug-Id'] = self.x_debug_id

        if self.channel is not None:
            result['channel'] = self.channel

        if self.params is not None:
            result['params'] = self.params.to_map()

        if self.service_name is not None:
            result['service_name'] = self.service_name

        if self.x_sysom_invoke_source is not None:
            result['x-sysom-invoke-source'] = self.x_sysom_invoke_source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X-Debug-Id') is not None:
            self.x_debug_id = m.get('X-Debug-Id')

        if m.get('channel') is not None:
            self.channel = m.get('channel')

        if m.get('params') is not None:
            temp_model = main_models.GetServiceFuncStatusRequestParams()
            self.params = temp_model.from_map(m.get('params'))

        if m.get('service_name') is not None:
            self.service_name = m.get('service_name')

        if m.get('x-sysom-invoke-source') is not None:
            self.x_sysom_invoke_source = m.get('x-sysom-invoke-source')

        return self

class GetServiceFuncStatusRequestParams(DaraModel):
    def __init__(
        self,
        function_name: str = None,
        instance: str = None,
        uid: str = None,
    ):
        # The feature name.
        # 
        # This parameter is required.
        self.function_name = function_name
        # The instance ID.
        self.instance = instance
        # The user ID.
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.function_name is not None:
            result['function_name'] = self.function_name

        if self.instance is not None:
            result['instance'] = self.instance

        if self.uid is not None:
            result['uid'] = self.uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('function_name') is not None:
            self.function_name = m.get('function_name')

        if m.get('instance') is not None:
            self.instance = m.get('instance')

        if m.get('uid') is not None:
            self.uid = m.get('uid')

        return self

