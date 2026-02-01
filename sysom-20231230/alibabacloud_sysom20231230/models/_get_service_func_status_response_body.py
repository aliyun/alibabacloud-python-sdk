# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sysom20231230 import models as main_models
from darabonba.model import DaraModel

class GetServiceFuncStatusResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetServiceFuncStatusResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.GetServiceFuncStatusResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetServiceFuncStatusResponseBodyData(DaraModel):
    def __init__(
        self,
        args: main_models.GetServiceFuncStatusResponseBodyDataArgs = None,
    ):
        self.args = args

    def validate(self):
        if self.args:
            self.args.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.args is not None:
            result['args'] = self.args.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('args') is not None:
            temp_model = main_models.GetServiceFuncStatusResponseBodyDataArgs()
            self.args = temp_model.from_map(m.get('args'))

        return self

class GetServiceFuncStatusResponseBodyDataArgs(DaraModel):
    def __init__(
        self,
        add_cmd: str = None,
        cpu: str = None,
        java_store_path: str = None,
        locks: str = None,
        loop: int = None,
        mem: str = None,
        system_profiling: str = None,
    ):
        self.add_cmd = add_cmd
        self.cpu = cpu
        self.java_store_path = java_store_path
        self.locks = locks
        self.loop = loop
        self.mem = mem
        self.system_profiling = system_profiling

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.add_cmd is not None:
            result['add_cmd'] = self.add_cmd

        if self.cpu is not None:
            result['cpu'] = self.cpu

        if self.java_store_path is not None:
            result['java_store_path'] = self.java_store_path

        if self.locks is not None:
            result['locks'] = self.locks

        if self.loop is not None:
            result['loop'] = self.loop

        if self.mem is not None:
            result['mem'] = self.mem

        if self.system_profiling is not None:
            result['system_profiling'] = self.system_profiling

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('add_cmd') is not None:
            self.add_cmd = m.get('add_cmd')

        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')

        if m.get('java_store_path') is not None:
            self.java_store_path = m.get('java_store_path')

        if m.get('locks') is not None:
            self.locks = m.get('locks')

        if m.get('loop') is not None:
            self.loop = m.get('loop')

        if m.get('mem') is not None:
            self.mem = m.get('mem')

        if m.get('system_profiling') is not None:
            self.system_profiling = m.get('system_profiling')

        return self

