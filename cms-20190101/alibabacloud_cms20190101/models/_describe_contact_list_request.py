# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeContactListRequest(DaraModel):
    def __init__(
        self,
        chanel_type: str = None,
        chanel_value: str = None,
        contact_name: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
    ):
        # The alert notification method. Valid values:
        # 
        # *   Mail: emails
        # *   DingWebHook: DingTalk chatbots
        self.chanel_type = chanel_type
        # The value specified for the alert notification method.
        # 
        # >  This parameter is required only if you set the `ChanelType` parameter to `Mail`.
        self.chanel_value = chanel_value
        # The name of the alert contact.
        self.contact_name = contact_name
        # The page number.
        # 
        # Default value: 1.
        self.page_number = page_number
        # The number of entries per page.
        # 
        # Default value: 100.
        self.page_size = page_size
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.chanel_type is not None:
            result['ChanelType'] = self.chanel_type

        if self.chanel_value is not None:
            result['ChanelValue'] = self.chanel_value

        if self.contact_name is not None:
            result['ContactName'] = self.contact_name

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChanelType') is not None:
            self.chanel_type = m.get('ChanelType')

        if m.get('ChanelValue') is not None:
            self.chanel_value = m.get('ChanelValue')

        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

