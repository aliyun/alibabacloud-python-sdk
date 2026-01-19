# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ReplaceMigrationAvailableNumbersRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        operator_name: str = None,
        operator_uid: int = None,
        v_1numbers: str = None,
        v_2numbers: str = None,
    ):
        self.instance_id = instance_id
        self.operator_name = operator_name
        self.operator_uid = operator_uid
        self.v_1numbers = v_1numbers
        self.v_2numbers = v_2numbers

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.operator_name is not None:
            result['OperatorName'] = self.operator_name

        if self.operator_uid is not None:
            result['OperatorUid'] = self.operator_uid

        if self.v_1numbers is not None:
            result['V1Numbers'] = self.v_1numbers

        if self.v_2numbers is not None:
            result['V2Numbers'] = self.v_2numbers

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OperatorName') is not None:
            self.operator_name = m.get('OperatorName')

        if m.get('OperatorUid') is not None:
            self.operator_uid = m.get('OperatorUid')

        if m.get('V1Numbers') is not None:
            self.v_1numbers = m.get('V1Numbers')

        if m.get('V2Numbers') is not None:
            self.v_2numbers = m.get('V2Numbers')

        return self

