# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteAppInstanceRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        delete_dbinstance: bool = None,
        instance_name: str = None,
        region_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. The client generates the value of this parameter to prevent duplicate requests from being submitted.
        self.client_token = client_token
        # Specifies whether to delete the corresponding database instance.
        self.delete_dbinstance = delete_dbinstance
        # The instance ID of the AI application.
        self.instance_name = instance_name
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.delete_dbinstance is not None:
            result['DeleteDBInstance'] = self.delete_dbinstance

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DeleteDBInstance') is not None:
            self.delete_dbinstance = m.get('DeleteDBInstance')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

