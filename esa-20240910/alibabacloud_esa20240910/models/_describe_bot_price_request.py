# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeBotPriceRequest(DaraModel):
    def __init__(
        self,
        bot_instance_level: str = None,
    ):
        # The bot instance type.
        # 
        # This parameter is required.
        self.bot_instance_level = bot_instance_level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bot_instance_level is not None:
            result['BotInstanceLevel'] = self.bot_instance_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BotInstanceLevel') is not None:
            self.bot_instance_level = m.get('BotInstanceLevel')

        return self

