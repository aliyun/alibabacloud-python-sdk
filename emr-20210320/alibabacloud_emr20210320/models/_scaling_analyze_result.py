# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ScalingAnalyzeResult(DaraModel):
    def __init__(
        self,
        actual_usage: float = None,
        ideal_usage: float = None,
        release_cores: int = None,
        reserved_cores: int = None,
    ):
        # 实际资源利用率。
        self.actual_usage = actual_usage
        # 理想资源用量。
        self.ideal_usage = ideal_usage
        # 固定资源释放核数（非master）core。
        self.release_cores = release_cores
        # 固定资源保留核数（非master）core。
        self.reserved_cores = reserved_cores

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.actual_usage is not None:
            result['ActualUsage'] = self.actual_usage

        if self.ideal_usage is not None:
            result['IdealUsage'] = self.ideal_usage

        if self.release_cores is not None:
            result['ReleaseCores'] = self.release_cores

        if self.reserved_cores is not None:
            result['ReservedCores'] = self.reserved_cores

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActualUsage') is not None:
            self.actual_usage = m.get('ActualUsage')

        if m.get('IdealUsage') is not None:
            self.ideal_usage = m.get('IdealUsage')

        if m.get('ReleaseCores') is not None:
            self.release_cores = m.get('ReleaseCores')

        if m.get('ReservedCores') is not None:
            self.reserved_cores = m.get('ReservedCores')

        return self

