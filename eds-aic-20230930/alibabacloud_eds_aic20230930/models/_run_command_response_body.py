# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eds_aic20230930 import models as main_models
from darabonba.model import DaraModel

class RunCommandResponseBody(DaraModel):
    def __init__(
        self,
        invoke_id: str = None,
        request_id: str = None,
        run_command_infos: List[main_models.RunCommandResponseBodyRunCommandInfos] = None,
    ):
        # The ID of the command execution. You can use the command execution ID to query the output of a command.
        self.invoke_id = invoke_id
        # The ID of the request.
        self.request_id = request_id
        self.run_command_infos = run_command_infos

    def validate(self):
        if self.run_command_infos:
            for v1 in self.run_command_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.invoke_id is not None:
            result['InvokeId'] = self.invoke_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['RunCommandInfos'] = []
        if self.run_command_infos is not None:
            for k1 in self.run_command_infos:
                result['RunCommandInfos'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InvokeId') is not None:
            self.invoke_id = m.get('InvokeId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.run_command_infos = []
        if m.get('RunCommandInfos') is not None:
            for k1 in m.get('RunCommandInfos'):
                temp_model = main_models.RunCommandResponseBodyRunCommandInfos()
                self.run_command_infos.append(temp_model.from_map(k1))

        return self

class RunCommandResponseBodyRunCommandInfos(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        invoke_id: str = None,
    ):
        self.instance_id = instance_id
        self.invoke_id = invoke_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.invoke_id is not None:
            result['InvokeId'] = self.invoke_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InvokeId') is not None:
            self.invoke_id = m.get('InvokeId')

        return self

