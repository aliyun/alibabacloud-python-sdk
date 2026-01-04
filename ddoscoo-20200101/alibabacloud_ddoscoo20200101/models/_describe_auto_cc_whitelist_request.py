# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAutoCcWhitelistRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        key_word: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The ID of the instance.
        # 
        # > You can call the [DescribeInstanceIds](https://help.aliyun.com/document_detail/157459.html) operation to query the IDs of all instances.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The keyword for the query. This keyword is used to specify the prefix of the source IP address that you want to query.
        # 
        # > The keyword must be greater than three characters in length.
        self.key_word = key_word
        # The number of the page to return. For example, to query the returned results on the first page, set the value to **1**.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The number of entries to return on each page.
        # 
        # This parameter is required.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.key_word is not None:
            result['KeyWord'] = self.key_word

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('KeyWord') is not None:
            self.key_word = m.get('KeyWord')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

