# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeResourceConstraintsRequest(DaraModel):
    def __init__(
        self,
        architecture: str = None,
        package_type: str = None,
        run_mode: str = None,
    ):
        # Specifies the instance architecture. Valid values:
        # 
        # - onEci: The instance is deployed on ECI.
        # 
        # - onEcs: The instance is deployed on ECS.
        # 
        # - onBareMetal: The instance is deployed on a bare metal resource pool.
        self.architecture = architecture
        # Specifies the instance edition. Valid values:
        # 
        # - trial: The entry-level edition.
        # 
        # - official: The Standard Edition.
        self.package_type = package_type
        # Specifies the run mode of the cluster. Valid values:
        # 
        # - shared_nothing: The shared-nothing mode.
        # 
        # - shared_data: The shared-data mode.
        # 
        # - lakehouse: The data lake analytics mode.
        self.run_mode = run_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.architecture is not None:
            result['Architecture'] = self.architecture

        if self.package_type is not None:
            result['PackageType'] = self.package_type

        if self.run_mode is not None:
            result['RunMode'] = self.run_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Architecture') is not None:
            self.architecture = m.get('Architecture')

        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')

        if m.get('RunMode') is not None:
            self.run_mode = m.get('RunMode')

        return self

