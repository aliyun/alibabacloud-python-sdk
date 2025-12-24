# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateResourceResponseBody(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        instance_ids: List[str] = None,
        owner_uid: str = None,
        request_id: str = None,
        resource_id: str = None,
        resource_name: str = None,
    ):
        # The ID of the cluster to which the resource group belongs.
        self.cluster_id = cluster_id
        # The instance IDs.
        self.instance_ids = instance_ids
        # The user ID (UID) of the resource group owner.
        self.owner_uid = owner_uid
        # The request ID.
        self.request_id = request_id
        # The ID of the resource group.
        self.resource_id = resource_id
        # The name of the resource group.
        self.resource_name = resource_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.owner_uid is not None:
            result['OwnerUid'] = self.owner_uid

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('OwnerUid') is not None:
            self.owner_uid = m.get('OwnerUid')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')

        return self

