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
        # Request ID.
        self.request_id = request_id
        # Service instance ID.
        self.service_instance_id = service_instance_id
        # The deployment status of the service instance. Possible values:
        # 
        # - Created: Created
        # 
        # - Deploying: Deploying
        # 
        # - DeployedFailed: Deployment Failed
        # 
        # - Deployed: Deployed
        # 
        # - Upgrading: Upgrading
        # 
        # - UpgradeRollbacking: Rolling Back
        # 
        # - Deleting: Deleting
        # 
        # - Deleted: Deleted
        # 
        # - DeletedFailed: Deletion Failed
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

