# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeGtmInstanceAddressPoolsRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        lang: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The ID of the GTM instance that you want to query.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The language used by the user.
        self.lang = lang
        # The number of the page to return. Pages start from page **1**. Default value: **1**.
        self.page_number = page_number
        # The number of entries to return per page. Maximum value: **100**. Default value: **20**.
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

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

