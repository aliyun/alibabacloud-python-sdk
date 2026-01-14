# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateUserTagValueRequest(DaraModel):
    def __init__(
        self,
        tag_id: str = None,
        tag_value: str = None,
        user_id: str = None,
    ):
        # The ID of the tag to be modified.
        # 
        # This parameter is required.
        self.tag_id = tag_id
        # The tag value to be modified.
        # 
        # - To clear this tag, set the tag value to ($NULL$).
        # - For multiple values, use English commas to separate them.
        # - Format validation, maximum length: 3000 characters
        # 
        # This parameter is required.
        self.tag_value = tag_value
        # The user ID for which the tag value is to be modified. This user ID refers to the Quick BI UserID, not the Alibaba Cloud UID.
        # 
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_id is not None:
            result['TagId'] = self.tag_id

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

