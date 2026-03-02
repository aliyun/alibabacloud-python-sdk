# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_neuron20211115 import models as main_models
from darabonba.model import DaraModel

class StackInfo(DaraModel):
    def __init__(
        self,
        api: str = None,
        duration: int = None,
        exception: str = None,
        ext_info: main_models.StackInfoExtInfo = None,
        line: str = None,
        rpc_id: str = None,
        service_name: str = None,
        start_time: int = None,
    ):
        self.api = api
        self.duration = duration
        self.exception = exception
        self.ext_info = ext_info
        self.line = line
        self.rpc_id = rpc_id
        self.service_name = service_name
        self.start_time = start_time

    def validate(self):
        if self.ext_info:
            self.ext_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api is not None:
            result['api'] = self.api

        if self.duration is not None:
            result['duration'] = self.duration

        if self.exception is not None:
            result['exception'] = self.exception

        if self.ext_info is not None:
            result['extInfo'] = self.ext_info.to_map()

        if self.line is not None:
            result['line'] = self.line

        if self.rpc_id is not None:
            result['rpcId'] = self.rpc_id

        if self.service_name is not None:
            result['serviceName'] = self.service_name

        if self.start_time is not None:
            result['startTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('api') is not None:
            self.api = m.get('api')

        if m.get('duration') is not None:
            self.duration = m.get('duration')

        if m.get('exception') is not None:
            self.exception = m.get('exception')

        if m.get('extInfo') is not None:
            temp_model = main_models.StackInfoExtInfo()
            self.ext_info = temp_model.from_map(m.get('extInfo'))

        if m.get('line') is not None:
            self.line = m.get('line')

        if m.get('rpcId') is not None:
            self.rpc_id = m.get('rpcId')

        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        return self

