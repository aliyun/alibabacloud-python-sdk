# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdatePipelineRequest(DaraModel):
    def __init__(
        self,
        extend_config: str = None,
        name: str = None,
        notify_config: str = None,
        owner_account: str = None,
        owner_id: int = None,
        pipeline_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        role: str = None,
        state: str = None,
    ):
        self.extend_config = extend_config
        # The new name of the MPS queue. The value can contain letters, digits, and special characters such as hyphens (-) and can be up to 128 bytes in size. The value cannot start with a special character.
        # 
        # This parameter is required.
        self.name = name
        # The Message Service (MNS) configuration, such as the information about the MNS queue or topic. For more information, see the "NotifyConfig" section of the [Parameter details](https://help.aliyun.com/document_detail/29253.html) topic.
        self.notify_config = notify_config
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the MPS queue that you want to update. To view the MPS queue ID, log on to the **MPS console** and choose **Global Settings** > **Pipelines** in the left-side navigation pane.
        # 
        # This parameter is required.
        self.pipeline_id = pipeline_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The role that is assigned to the current RAM user. To obtain the role, you can log on to the **Resource Access Management (RAM) console** and choose **Identities** > **Roles** in the left-side navigation pane.
        self.role = role
        # The new state of the MPS queue.
        # 
        # *   **Active**: The MPS queue is active. Jobs in the MPS queue can be scheduled and run by MPS.
        # *   **Paused**: The MPS queue is paused. Jobs in the MPS queue cannot be scheduled or run by MPS, and all jobs remain in the Submitted state. Jobs that are running will not be affected.
        # 
        # This parameter is required.
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.extend_config is not None:
            result['ExtendConfig'] = self.extend_config

        if self.name is not None:
            result['Name'] = self.name

        if self.notify_config is not None:
            result['NotifyConfig'] = self.notify_config

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.role is not None:
            result['Role'] = self.role

        if self.state is not None:
            result['State'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtendConfig') is not None:
            self.extend_config = m.get('ExtendConfig')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NotifyConfig') is not None:
            self.notify_config = m.get('NotifyConfig')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

