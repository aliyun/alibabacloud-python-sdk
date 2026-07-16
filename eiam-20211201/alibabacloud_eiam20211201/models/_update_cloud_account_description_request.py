# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateCloudAccountDescriptionRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        cloud_account_id: str = None,
        description: str = None,
        instance_id: str = None,
    ):
        # A client token to ensure the idempotence of the request. Generate a unique value for this parameter from your client for each request. The ClientToken can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://www.alibabacloud.com/help/zh/ecs/developer-reference/how-to-ensure-idempotence).
        # 
        # This parameter is required.
        self.client_token = client_token
        # The ID of the Alibaba Cloud account.
        # 
        # This parameter is required.
        self.cloud_account_id = cloud_account_id
        # The description of the Alibaba Cloud account.
        self.description = description
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.cloud_account_id is not None:
            result['CloudAccountId'] = self.cloud_account_id

        if self.description is not None:
            result['Description'] = self.description

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('CloudAccountId') is not None:
            self.cloud_account_id = m.get('CloudAccountId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

