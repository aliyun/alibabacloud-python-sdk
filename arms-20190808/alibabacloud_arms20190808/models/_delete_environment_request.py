# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteEnvironmentRequest(DaraModel):
    def __init__(
        self,
        delete_prom_instance: bool = None,
        environment_id: str = None,
        region_id: str = None,
    ):
        # Specifies whether to delete the related Prometheus instance.
        self.delete_prom_instance = delete_prom_instance
        # The ID of the environment instance.
        # 
        # This parameter is required.
        self.environment_id = environment_id
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.delete_prom_instance is not None:
            result['DeletePromInstance'] = self.delete_prom_instance

        if self.environment_id is not None:
            result['EnvironmentId'] = self.environment_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeletePromInstance') is not None:
            self.delete_prom_instance = m.get('DeletePromInstance')

        if m.get('EnvironmentId') is not None:
            self.environment_id = m.get('EnvironmentId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

