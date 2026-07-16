# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RollbackServiceInstanceResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        service_instance_id: str = None,
        status: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The service instance ID.
        self.service_instance_id = service_instance_id
        # The deployment status of the service instance. Valid values:
        # 
        # - Created: The service instance is created.
        # 
        # - Deploying: The service instance is being deployed.
        # 
        # - DeployedFailed: The deployment of the service instance failed.
        # 
        # - Deployed: The service instance is deployed.
        # 
        # - Upgrading: The service instance is being upgraded.
        # 
        # - UpgradeRollbacking: The service instance is being rolled back.
        # 
        # - Deleting: The service instance is being deleted.
        # 
        # - Deleted: The service instance is deleted.
        # 
        # - DeletedFailed: The deletion of the service instance failed.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

