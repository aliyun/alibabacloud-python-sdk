# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RunNotifyComponentWithWebhookRequest(DaraModel):
    def __init__(
        self,
        action_name: str = None,
        asset_id: str = None,
        component_name: str = None,
        content: str = None,
        lang: str = None,
        msg_type: str = None,
        node_name: str = None,
        playbook_uuid: str = None,
        role_for: int = None,
        role_type: str = None,
        secret: str = None,
        webhook: str = None,
    ):
        # The name of the playbook action.
        # 
        # This parameter is required.
        self.action_name = action_name
        # The ID of the resource. This parameter is deprecated and no longer used.
        self.asset_id = asset_id
        # The name of the playbook component.
        # 
        # This parameter is required.
        self.component_name = component_name
        # The content of the message sent by the webhook of the DingTalk group robot.
        # 
        # This parameter is required.
        self.content = content
        # The language of the request and response. Valid values:
        # 
        # - **zh** (default): Chinese.
        # 
        # - **en**: English.
        self.lang = lang
        # The message type of the webhook. Valid values:
        # 
        # - text
        # 
        # - markdown
        # 
        # - actionCard
        # 
        # This parameter is required.
        self.msg_type = msg_type
        # The name of the playbook node.
        # 
        # This parameter is required.
        self.node_name = node_name
        # The UUID of the playbook.
        # 
        # > Call the [DescribePlaybooks](https://help.aliyun.com/document_detail/3000306.html) operation to obtain this parameter.
        # 
        # This parameter is required.
        self.playbook_uuid = playbook_uuid
        # The UID of the member that the administrator wants to switch to.
        self.role_for = role_for
        # The view type. Valid values:
        # 
        # - 0 (default): the view of the current Alibaba Cloud account.
        # 
        # - 1: the view of all accounts that belong to the enterprise.
        self.role_type = role_type
        # The secret key for the webhook of the DingTalk group robot. This parameter is deprecated and no longer used.
        self.secret = secret
        # The IDs of the DingTalk robots. Obtain the IDs on the robot management page in Message Center.
        # 
        # This parameter is required.
        self.webhook = webhook

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_name is not None:
            result['ActionName'] = self.action_name

        if self.asset_id is not None:
            result['AssetId'] = self.asset_id

        if self.component_name is not None:
            result['ComponentName'] = self.component_name

        if self.content is not None:
            result['Content'] = self.content

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.msg_type is not None:
            result['MsgType'] = self.msg_type

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid

        if self.role_for is not None:
            result['RoleFor'] = self.role_for

        if self.role_type is not None:
            result['RoleType'] = self.role_type

        if self.secret is not None:
            result['Secret'] = self.secret

        if self.webhook is not None:
            result['Webhook'] = self.webhook

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionName') is not None:
            self.action_name = m.get('ActionName')

        if m.get('AssetId') is not None:
            self.asset_id = m.get('AssetId')

        if m.get('ComponentName') is not None:
            self.component_name = m.get('ComponentName')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('MsgType') is not None:
            self.msg_type = m.get('MsgType')

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')

        if m.get('Secret') is not None:
            self.secret = m.get('Secret')

        if m.get('Webhook') is not None:
            self.webhook = m.get('Webhook')

        return self

