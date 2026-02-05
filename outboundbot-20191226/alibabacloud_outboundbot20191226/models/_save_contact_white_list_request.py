# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class SaveContactWhiteListRequest(DaraModel):
    def __init__(
        self,
        contact_white_list_list: List[str] = None,
        contact_white_lists_json: str = None,
        instance_id: str = None,
    ):
        self.contact_white_list_list = contact_white_list_list
        self.contact_white_lists_json = contact_white_lists_json
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_white_list_list is not None:
            result['ContactWhiteListList'] = self.contact_white_list_list

        if self.contact_white_lists_json is not None:
            result['ContactWhiteListsJson'] = self.contact_white_lists_json

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactWhiteListList') is not None:
            self.contact_white_list_list = m.get('ContactWhiteListList')

        if m.get('ContactWhiteListsJson') is not None:
            self.contact_white_lists_json = m.get('ContactWhiteListsJson')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

