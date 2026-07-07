# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PurchaseBotInstanceRequest(DaraModel):
    def __init__(
        self,
        bot_instance_level: str = None,
        site_instance_id: str = None,
    ):
        # The bot instance specifications.
        # 
        # This parameter is required.
        self.bot_instance_level = bot_instance_level
        # The site instance.
        # 
        # This parameter is required.
        self.site_instance_id = site_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bot_instance_level is not None:
            result['BotInstanceLevel'] = self.bot_instance_level

        if self.site_instance_id is not None:
            result['SiteInstanceId'] = self.site_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BotInstanceLevel') is not None:
            self.bot_instance_level = m.get('BotInstanceLevel')

        if m.get('SiteInstanceId') is not None:
            self.site_instance_id = m.get('SiteInstanceId')

        return self

