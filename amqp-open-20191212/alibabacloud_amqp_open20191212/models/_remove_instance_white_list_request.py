# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RemoveInstanceWhiteListRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        white_list_item_id: int = None,
        white_list_type: int = None,
    ):
        # The ID of the instance from which to remove a whitelist entry.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Call the ListInstanceWhiteList operation to obtain this ID.
        # 
        # This parameter is required.
        self.white_list_item_id = white_list_item_id
        # The type of the whitelist item. Specify 2 for an IP address or 1 for a VPC ID.
        # 
        # A VPC whitelist only applies to instances with the anytunnel VPC endpoint type. Newer instances use PrivateLink for their VPC endpoints and do not support VPC whitelists.
        # 
        # This parameter is required.
        self.white_list_type = white_list_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.white_list_item_id is not None:
            result['whiteListItemId'] = self.white_list_item_id

        if self.white_list_type is not None:
            result['whiteListType'] = self.white_list_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('whiteListItemId') is not None:
            self.white_list_item_id = m.get('whiteListItemId')

        if m.get('whiteListType') is not None:
            self.white_list_type = m.get('whiteListType')

        return self

