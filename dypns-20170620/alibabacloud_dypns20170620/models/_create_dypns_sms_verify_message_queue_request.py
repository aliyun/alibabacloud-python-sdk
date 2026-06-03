# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDypnsSmsVerifyMessageQueueRequest(DaraModel):
    def __init__(
        self,
        owner_id: int = None,
        query_queue_types: str = None,
        queue_type: str = None,
        region: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.owner_id = owner_id
        self.query_queue_types = query_queue_types
        self.queue_type = queue_type
        self.region = region
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.query_queue_types is not None:
            result['QueryQueueTypes'] = self.query_queue_types

        if self.queue_type is not None:
            result['QueueType'] = self.queue_type

        if self.region is not None:
            result['Region'] = self.region

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('QueryQueueTypes') is not None:
            self.query_queue_types = m.get('QueryQueueTypes')

        if m.get('QueueType') is not None:
            self.queue_type = m.get('QueueType')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

