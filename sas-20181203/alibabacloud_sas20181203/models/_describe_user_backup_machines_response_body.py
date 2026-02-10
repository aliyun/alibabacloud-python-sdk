# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeUserBackupMachinesResponseBody(DaraModel):
    def __init__(
        self,
        machines: List[main_models.DescribeUserBackupMachinesResponseBodyMachines] = None,
        request_id: str = None,
    ):
        # An array consisting of the servers to which the anti-ransomware policy is applied.
        self.machines = machines
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.machines:
            for v1 in self.machines:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Machines'] = []
        if self.machines is not None:
            for k1 in self.machines:
                result['Machines'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.machines = []
        if m.get('Machines') is not None:
            for k1 in m.get('Machines'):
                temp_model = main_models.DescribeUserBackupMachinesResponseBodyMachines()
                self.machines.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeUserBackupMachinesResponseBodyMachines(DaraModel):
    def __init__(
        self,
        id: int = None,
        policy_name: str = None,
        uuid: str = None,
    ):
        # The ID of the anti-ransomware policy that is applied to the server.
        self.id = id
        # The name of the anti-ransomware policy that is applied to the server.
        self.policy_name = policy_name
        # The UUID of the server to which the anti-ransomware policy is applied.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

