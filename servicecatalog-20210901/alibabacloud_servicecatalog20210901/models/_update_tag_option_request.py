# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateTagOptionRequest(DaraModel):
    def __init__(
        self,
        active: bool = None,
        tag_option_id: str = None,
        value: str = None,
    ):
        # Specifies whether to enable the tag option. Valid values:
        # 
        # *   true (default)
        # *   false
        self.active = active
        # The ID of the tag option.
        # 
        # This parameter is required.
        self.tag_option_id = tag_option_id
        # The value of the tag option.
        # 
        # The value can be up to 128 characters in length. It cannot start with `acs:` and cannot contain `http://` or `https://`.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active is not None:
            result['Active'] = self.active

        if self.tag_option_id is not None:
            result['TagOptionId'] = self.tag_option_id

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Active') is not None:
            self.active = m.get('Active')

        if m.get('TagOptionId') is not None:
            self.tag_option_id = m.get('TagOptionId')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

