# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyServiceInstanceResourcesRequest(DaraModel):
    def __init__(
        self,
        resources: str = None,
        service_instance_id: str = None,
        service_instance_resources_action: str = None,
    ):
        # The imported resources.
        self.resources = resources
        # The ID of the service instance.
        # 
        # This parameter is required.
        self.service_instance_id = service_instance_id
        # The type of operation performed on the service instance resource. Valid values:
        # 
        # *   Import: The resource is imported.
        # *   UnImport: The resource import is canceled.
        self.service_instance_resources_action = service_instance_resources_action

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resources is not None:
            result['Resources'] = self.resources

        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id

        if self.service_instance_resources_action is not None:
            result['ServiceInstanceResourcesAction'] = self.service_instance_resources_action

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Resources') is not None:
            self.resources = m.get('Resources')

        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')

        if m.get('ServiceInstanceResourcesAction') is not None:
            self.service_instance_resources_action = m.get('ServiceInstanceResourcesAction')

        return self

