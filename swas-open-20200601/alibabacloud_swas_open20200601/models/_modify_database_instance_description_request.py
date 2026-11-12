# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDatabaseInstanceDescriptionRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        database_instance_description: str = None,
        database_instance_id: str = None,
        region_id: str = None,
    ):
        # Ensures the idempotence of the request. You can generate the value from your client to ensure that the value is unique across different requests. The ClientToken parameter supports only ASCII characters and can be up to 64 characters in length. For more information, see [Ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The description of the lightweight database instance.
        # 
        # This parameter is required.
        self.database_instance_description = database_instance_description
        # The instance ID of the lightweight database instance.
        # 
        # This parameter is required.
        self.database_instance_id = database_instance_id
        # The region ID of the lightweight database instance. You can call the [ListRegions](https://help.aliyun.com/document_detail/189315.html) operation to query the list of supported Alibaba Cloud regions.
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
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.database_instance_description is not None:
            result['DatabaseInstanceDescription'] = self.database_instance_description

        if self.database_instance_id is not None:
            result['DatabaseInstanceId'] = self.database_instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DatabaseInstanceDescription') is not None:
            self.database_instance_description = m.get('DatabaseInstanceDescription')

        if m.get('DatabaseInstanceId') is not None:
            self.database_instance_id = m.get('DatabaseInstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

