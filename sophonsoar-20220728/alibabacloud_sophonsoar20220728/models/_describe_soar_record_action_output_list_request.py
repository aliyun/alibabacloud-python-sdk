# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSoarRecordActionOutputListRequest(DaraModel):
    def __init__(
        self,
        action_uuid: str = None,
        lang: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The UUID of the component action.
        # 
        # >  You can call the [DescribeSoarTaskAndActions](~~DescribeSoarTaskAndActions~~) operation to query the UUID.
        # 
        # This parameter is required.
        self.action_uuid = action_uuid
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The page number. Default value: 1. Pages start from page 1.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The number of entries per page. Default value: 10. If you leave this parameter empty, 10 entries are returned on each page.
        # 
        # >  We recommend that you do not leave this parameter empty.
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
        if self.action_uuid is not None:
            result['ActionUuid'] = self.action_uuid

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionUuid') is not None:
            self.action_uuid = m.get('ActionUuid')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

