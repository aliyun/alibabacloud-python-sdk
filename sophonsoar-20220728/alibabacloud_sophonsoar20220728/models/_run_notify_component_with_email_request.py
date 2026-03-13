# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class RunNotifyComponentWithEmailRequest(DaraModel):
    def __init__(
        self,
        action_name: str = None,
        asset_id: str = None,
        component_name: str = None,
        content: str = None,
        lang: str = None,
        node_name: str = None,
        playbook_uuid: str = None,
        receivers: List[str] = None,
        role_for: int = None,
        role_type: str = None,
        subject: str = None,
    ):
        # The action name of the component.
        # 
        # This parameter is required.
        self.action_name = action_name
        # The resource instance ID of the email sender.
        # 
        # >  You can call the [DescribeComponentAssets](~~DescribeComponentAssets~~) operation to query the ID.
        self.asset_id = asset_id
        # The name of component in the playbook.
        # 
        # This parameter is required.
        self.component_name = component_name
        # The body of the email.
        # 
        # This parameter is required.
        self.content = content
        # The language of the content within the request and the response. Valid value:
        # 
        # *   **zh** (default): Chinese.
        # *   **en**: English.
        self.lang = lang
        # The name of the node in the playbook.
        # 
        # This parameter is required.
        self.node_name = node_name
        # The UUID of the playbook.
        # 
        # >  You can call the [DescribePlaybooks](~~DescribePlaybooks~~) operation to query the UUIDs of playbooks.
        # 
        # This parameter is required.
        self.playbook_uuid = playbook_uuid
        # The email addresses.
        # 
        # This parameter is required.
        self.receivers = receivers
        # The ID of the user who switches from the current view to the destination view by using the management account.
        self.role_for = role_for
        # The type of the view. Valid values:
        # 
        # *   0: the view of the current Alibaba Cloud account.
        # *   1: the view of all accounts for the enterprise.
        self.role_type = role_type
        # The subject of the email.
        # 
        # This parameter is required.
        self.subject = subject

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

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid

        if self.receivers is not None:
            result['Receivers'] = self.receivers

        if self.role_for is not None:
            result['RoleFor'] = self.role_for

        if self.role_type is not None:
            result['RoleType'] = self.role_type

        if self.subject is not None:
            result['Subject'] = self.subject

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

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')

        if m.get('Receivers') is not None:
            self.receivers = m.get('Receivers')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')

        if m.get('Subject') is not None:
            self.subject = m.get('Subject')

        return self

