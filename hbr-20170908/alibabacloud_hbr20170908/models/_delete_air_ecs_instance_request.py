# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DeleteAirEcsInstanceRequest(DaraModel):
    def __init__(
        self,
        ecs_instance_id: str = None,
        uninstall_client_source_types: List[str] = None,
    ):
        # The ID of the Elastic Compute Service (ECS) instance.
        self.ecs_instance_id = ecs_instance_id
        # The data sources for which the client needs to be uninstalled.
        self.uninstall_client_source_types = uninstall_client_source_types

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ecs_instance_id is not None:
            result['EcsInstanceId'] = self.ecs_instance_id

        if self.uninstall_client_source_types is not None:
            result['UninstallClientSourceTypes'] = self.uninstall_client_source_types

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EcsInstanceId') is not None:
            self.ecs_instance_id = m.get('EcsInstanceId')

        if m.get('UninstallClientSourceTypes') is not None:
            self.uninstall_client_source_types = m.get('UninstallClientSourceTypes')

        return self

