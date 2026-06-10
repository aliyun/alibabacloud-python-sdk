# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RollbackAppInstancePublishRequest(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        deploy_channel: str = None,
        publish_number: str = None,
        quick_rollback: str = None,
    ):
        # Business ID
        self.biz_id = biz_id
        # Deployment channel
        self.deploy_channel = deploy_channel
        # Publish number
        self.publish_number = publish_number
        # Quick rollback.
        self.quick_rollback = quick_rollback

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

        if self.publish_number is not None:
            result['PublishNumber'] = self.publish_number

        if self.quick_rollback is not None:
            result['QuickRollback'] = self.quick_rollback

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('DeployChannel') is not None:
            self.deploy_channel = m.get('DeployChannel')

        if m.get('PublishNumber') is not None:
            self.publish_number = m.get('PublishNumber')

        if m.get('QuickRollback') is not None:
            self.quick_rollback = m.get('QuickRollback')

        return self

