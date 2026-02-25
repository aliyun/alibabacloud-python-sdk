# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddMediaWorkflowRequest(DaraModel):
    def __init__(
        self,
        name: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        topology: str = None,
        trigger_mode: str = None,
    ):
        # The name of the media workflow.
        # 
        # *   The value cannot be empty.
        # *   The name cannot be the same as that of an existing media workflow within the current Alibaba Cloud account.
        # *   The name can be up to 64 characters in length.
        # *   The value must be encoded in the UTF-8 format.
        # 
        # This parameter is required.
        self.name = name
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The topology of the media workflow. The value must be a JSON object that contains the activities and activity dependencies. For more information, see the **Sample topology** section of this topic.
        # 
        # >  The Object Storage Service (OSS) bucket must reside in the same region as your MPS service.
        # 
        # This parameter is required.
        self.topology = topology
        # The triggering mode of the media workflow. Valid values:
        # 
        # *   **OssAutoTrigger**: The media workflow is automatically triggered.
        # *   **NotInAuto**: The media workflow is not automatically triggered.
        self.trigger_mode = trigger_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.topology is not None:
            result['Topology'] = self.topology

        if self.trigger_mode is not None:
            result['TriggerMode'] = self.trigger_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('Topology') is not None:
            self.topology = m.get('Topology')

        if m.get('TriggerMode') is not None:
            self.trigger_mode = m.get('TriggerMode')

        return self

