# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CheckPolarFsQuotaConsistencyRequest(DaraModel):
    def __init__(
        self,
        enable_repair: bool = None,
        enable_strict_calculate: bool = None,
        path: str = None,
        polar_fs_instance_id: str = None,
    ):
        self.enable_repair = enable_repair
        self.enable_strict_calculate = enable_strict_calculate
        self.path = path
        # This parameter is required.
        self.polar_fs_instance_id = polar_fs_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_repair is not None:
            result['EnableRepair'] = self.enable_repair

        if self.enable_strict_calculate is not None:
            result['EnableStrictCalculate'] = self.enable_strict_calculate

        if self.path is not None:
            result['Path'] = self.path

        if self.polar_fs_instance_id is not None:
            result['PolarFsInstanceId'] = self.polar_fs_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableRepair') is not None:
            self.enable_repair = m.get('EnableRepair')

        if m.get('EnableStrictCalculate') is not None:
            self.enable_strict_calculate = m.get('EnableStrictCalculate')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('PolarFsInstanceId') is not None:
            self.polar_fs_instance_id = m.get('PolarFsInstanceId')

        return self

