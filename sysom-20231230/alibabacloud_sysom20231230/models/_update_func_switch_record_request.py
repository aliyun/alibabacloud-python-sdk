# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sysom20231230 import models as main_models
from darabonba.model import DaraModel

class UpdateFuncSwitchRecordRequest(DaraModel):
    def __init__(
        self,
        channel: str = None,
        params: main_models.UpdateFuncSwitchRecordRequestParams = None,
        service_name: str = None,
    ):
        # This parameter is required.
        self.channel = channel
        # This parameter is required.
        self.params = params
        # This parameter is required.
        self.service_name = service_name

    def validate(self):
        if self.params:
            self.params.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel is not None:
            result['channel'] = self.channel

        if self.params is not None:
            result['params'] = self.params.to_map()

        if self.service_name is not None:
            result['service_name'] = self.service_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('channel') is not None:
            self.channel = m.get('channel')

        if m.get('params') is not None:
            temp_model = main_models.UpdateFuncSwitchRecordRequestParams()
            self.params = temp_model.from_map(m.get('params'))

        if m.get('service_name') is not None:
            self.service_name = m.get('service_name')

        return self

class UpdateFuncSwitchRecordRequestParams(DaraModel):
    def __init__(
        self,
        args: main_models.UpdateFuncSwitchRecordRequestParamsArgs = None,
        function_name: str = None,
        instance: str = None,
        op: str = None,
        region: str = None,
        uid: str = None,
    ):
        self.args = args
        # This parameter is required.
        self.function_name = function_name
        self.instance = instance
        self.op = op
        self.region = region
        self.uid = uid

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

        if self.function_name is not None:
            result['function_name'] = self.function_name

        if self.instance is not None:
            result['instance'] = self.instance

        if self.op is not None:
            result['op'] = self.op

        if self.region is not None:
            result['region'] = self.region

        if self.uid is not None:
            result['uid'] = self.uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('args') is not None:
            temp_model = main_models.UpdateFuncSwitchRecordRequestParamsArgs()
            self.args = temp_model.from_map(m.get('args'))

        if m.get('function_name') is not None:
            self.function_name = m.get('function_name')

        if m.get('instance') is not None:
            self.instance = m.get('instance')

        if m.get('op') is not None:
            self.op = m.get('op')

        if m.get('region') is not None:
            self.region = m.get('region')

        if m.get('uid') is not None:
            self.uid = m.get('uid')

        return self

class UpdateFuncSwitchRecordRequestParamsArgs(DaraModel):
    def __init__(
        self,
        add_cmd: str = None,
        cpu: str = None,
        duration: int = None,
        java_store_path: str = None,
        locks: str = None,
        loop: int = None,
        mem: str = None,
        pid: int = None,
        system_profiling: str = None,
    ):
        self.add_cmd = add_cmd
        self.cpu = cpu
        self.duration = duration
        self.java_store_path = java_store_path
        self.locks = locks
        self.loop = loop
        self.mem = mem
        self.pid = pid
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

        if self.duration is not None:
            result['duration'] = self.duration

        if self.java_store_path is not None:
            result['java_store_path'] = self.java_store_path

        if self.locks is not None:
            result['locks'] = self.locks

        if self.loop is not None:
            result['loop'] = self.loop

        if self.mem is not None:
            result['mem'] = self.mem

        if self.pid is not None:
            result['pid'] = self.pid

        if self.system_profiling is not None:
            result['system_profiling'] = self.system_profiling

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('add_cmd') is not None:
            self.add_cmd = m.get('add_cmd')

        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')

        if m.get('duration') is not None:
            self.duration = m.get('duration')

        if m.get('java_store_path') is not None:
            self.java_store_path = m.get('java_store_path')

        if m.get('locks') is not None:
            self.locks = m.get('locks')

        if m.get('loop') is not None:
            self.loop = m.get('loop')

        if m.get('mem') is not None:
            self.mem = m.get('mem')

        if m.get('pid') is not None:
            self.pid = m.get('pid')

        if m.get('system_profiling') is not None:
            self.system_profiling = m.get('system_profiling')

        return self

