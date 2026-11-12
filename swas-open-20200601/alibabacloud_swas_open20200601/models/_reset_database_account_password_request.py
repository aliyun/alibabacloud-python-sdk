# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ResetDatabaseAccountPasswordRequest(DaraModel):
    def __init__(
        self,
        account_password: str = None,
        client_token: str = None,
        database_instance_id: str = None,
        region_id: str = None,
    ):
        # The password of the administrator account for the database.
        # 
        # This parameter is required.
        self.account_password = account_password
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, and you must ensure that the value is unique among different requests. The client token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The instance ID of the simple application server database.
        # 
        # This parameter is required.
        self.database_instance_id = database_instance_id
        # The region ID of the simple application server database instance. You can call the [ListRegions](https://help.aliyun.com/document_detail/189315.html) operation to query the supported Alibaba Cloud regions.
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
        if self.account_password is not None:
            result['AccountPassword'] = self.account_password

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.database_instance_id is not None:
            result['DatabaseInstanceId'] = self.database_instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountPassword') is not None:
            self.account_password = m.get('AccountPassword')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DatabaseInstanceId') is not None:
            self.database_instance_id = m.get('DatabaseInstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

