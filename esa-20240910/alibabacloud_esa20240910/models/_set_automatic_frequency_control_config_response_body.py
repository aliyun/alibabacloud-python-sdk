# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetAutomaticFrequencyControlConfigResponseBody(DaraModel):
    def __init__(
        self,
        action_type: str = None,
        enable: str = None,
        level: str = None,
        request_id: str = None,
    ):
        # The action to perform. Valid values:
        # - **observe**: Monitor.
        # - **deny**: Block.
        # - **js**: JavaScript Challenge.
        self.action_type = action_type
        # Specifies whether to enable the feature. Valid values:
        # 
        #  - **on**: Enabled.
        # 
        #  - **off**: Disabled.
        self.enable = enable
        # The protection level. Valid values:
        # - **loose**: Loose.
        # - **normal**: Medium.
        # - **strict**: Strict.
        self.level = level
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_type is not None:
            result['ActionType'] = self.action_type

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.level is not None:
            result['Level'] = self.level

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

