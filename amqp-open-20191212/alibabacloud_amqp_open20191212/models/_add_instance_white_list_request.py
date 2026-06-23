# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class AddInstanceWhiteListRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        white_list_item: List[str] = None,
        white_list_type: int = None,
    ):
        # The ID of the instance receiving the whitelist entry.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The IP addresses or VPC IDs to add to the whitelist. Specify IP addresses as CIDR blocks.
        # 
        # This parameter is required.
        self.white_list_item = white_list_item
        # The type of the whitelist. Set this parameter to `2` if `WhiteListItem` contains IP addresses, or to `1` if it contains VPC IDs.
        # 
        # You can add a VPC whitelist only to instances that have an `anytunnel` VPC endpoint. Newer instances use the `privateLink` endpoint type, which does not support this feature.
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

        if self.white_list_item is not None:
            result['WhiteListItem'] = self.white_list_item

        if self.white_list_type is not None:
            result['WhiteListType'] = self.white_list_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('WhiteListItem') is not None:
            self.white_list_item = m.get('WhiteListItem')

        if m.get('WhiteListType') is not None:
            self.white_list_type = m.get('WhiteListType')

        return self

