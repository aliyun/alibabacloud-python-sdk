# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDasInstanceConfigRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dbinstance_id: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        storage_auto_scale: str = None,
        storage_threshold: int = None,
        storage_upper_bound: int = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the generated token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The instance ID. You can call the DescribeDBInstances operation to query the instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Specifies whether to enable automatic storage expansion. Valid values:
        # 
        # *   **Enable**
        # *   **Disable**
        # 
        # This parameter is required.
        self.storage_auto_scale = storage_auto_scale
        # The threshold in percentage based on which an automatic storage expansion is triggered. If the available storage reaches the threshold, ApsaraDB RDS increases the storage capacity of the instance. Valid values:
        # 
        # *   **10**
        # *   **20**
        # *   **30**
        # *   **40**
        # *   **50**
        # 
        # >  If you set the StorageAutoScale parameter to **Enable**, you must specify this parameter.
        self.storage_threshold = storage_threshold
        # The maximum storage capacity that is allowed for an automatic storage expansion. The value of this parameter must be greater than or equal to the current storage capacity of the RDS instance.
        # 
        # *   If the RDS instance uses ESSDs, the maximum value of this parameter can be set to 32000 GB.
        # *   If the RDS instance uses standard SSDs, the maximum value of this parameter can be set to 6000 GB.
        # 
        # >  If you set the **StorageAutoScale** parameter to **Enable**, you must specify this parameter.
        self.storage_upper_bound = storage_upper_bound

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.storage_auto_scale is not None:
            result['StorageAutoScale'] = self.storage_auto_scale

        if self.storage_threshold is not None:
            result['StorageThreshold'] = self.storage_threshold

        if self.storage_upper_bound is not None:
            result['StorageUpperBound'] = self.storage_upper_bound

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('StorageAutoScale') is not None:
            self.storage_auto_scale = m.get('StorageAutoScale')

        if m.get('StorageThreshold') is not None:
            self.storage_threshold = m.get('StorageThreshold')

        if m.get('StorageUpperBound') is not None:
            self.storage_upper_bound = m.get('StorageUpperBound')

        return self

