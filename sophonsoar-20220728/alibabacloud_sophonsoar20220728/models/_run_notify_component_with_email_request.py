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
        # The name of the component action.
        # 
        # This parameter is required.
        self.action_name = action_name
        # The ID of the asset that is used to send the email.
        # 
        # > Call the [DescribeComponentAssets](~~DescribeComponentAssets~~) operation to obtain this parameter.
        self.asset_id = asset_id
        # The name of the playbook component.
        # 
        # This parameter is required.
        self.component_name = component_name
        # The body of the email.
        # 
        # This parameter is required.
        self.content = content
        # The language of the request and response. Valid values:
        # 
        # - **zh** (default): Chinese
        # 
        # - **en**: English
        self.lang = lang
        # The name of the playbook node.
        # 
        # This parameter is required.
        self.node_name = node_name
        # The UUID of the playbook.
        # 
        # > Call the [DescribePlaybooks](~~DescribePlaybooks~~) operation to obtain this parameter.
        # 
        # This parameter is required.
        self.playbook_uuid = playbook_uuid
        # A list of email addresses.
        # 
        # This parameter is required.
        self.receivers = receivers
        # The UID of the member whose data an administrator wants to access.
        self.role_for = role_for
        # The view type. Valid values:
        # 
        # - 0: The view of the current Alibaba Cloud account.
        # 
        # - 1: The view of all accounts that belong to the enterprise.
        self.role_type = role_type
        # The title of the email.
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

