# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDcdnUserConfigsRequest(DaraModel):
    def __init__(
        self,
        function_name: str = None,
    ):
        # The configuration that you want to query. Valid values:
        # 
        # *   domain_business_control: user configurations
        # *   bot_basic: the basic edition of bot traffic management, which supports authorized crawlers and provides threat intelligence
        # *   bot_Advance: the advanced edition of bot traffic management, which supports authorized crawlers and AI intelligent protection and provides threat intelligence
        # 
        # This parameter is required.
        self.function_name = function_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.function_name is not None:
            result['FunctionName'] = self.function_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')

        return self

