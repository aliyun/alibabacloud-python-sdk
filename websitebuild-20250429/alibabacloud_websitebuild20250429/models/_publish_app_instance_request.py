# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PublishAppInstanceRequest(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        deploy_channel: str = None,
        description: str = None,
        logical_number: int = None,
        publish_number: str = None,
        weapp_action: str = None,
    ):
        # Business ID
        self.biz_id = biz_id
        # Deployment channel
        self.deploy_channel = deploy_channel
        # Publish description
        self.description = description
        # Logical version number
        self.logical_number = logical_number
        # Publish number
        self.publish_number = publish_number
        # action
        self.weapp_action = weapp_action

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.deploy_channel is not None:
            result['DeployChannel'] = self.deploy_channel

        if self.description is not None:
            result['Description'] = self.description

        if self.logical_number is not None:
            result['LogicalNumber'] = self.logical_number

        if self.publish_number is not None:
            result['PublishNumber'] = self.publish_number

        if self.weapp_action is not None:
            result['WeappAction'] = self.weapp_action

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('DeployChannel') is not None:
            self.deploy_channel = m.get('DeployChannel')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('LogicalNumber') is not None:
            self.logical_number = m.get('LogicalNumber')

        if m.get('PublishNumber') is not None:
            self.publish_number = m.get('PublishNumber')

        if m.get('WeappAction') is not None:
            self.weapp_action = m.get('WeappAction')

        return self

