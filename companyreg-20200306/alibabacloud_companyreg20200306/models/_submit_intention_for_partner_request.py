# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitIntentionForPartnerRequest(DaraModel):
    def __init__(
        self,
        area: str = None,
        biz_type: str = None,
        channel: str = None,
        commodity_type: str = None,
        contact_name: str = None,
        description: str = None,
        ext_info: str = None,
        grade: int = None,
        mobile: str = None,
        user_id: str = None,
    ):
        self.area = area
        self.biz_type = biz_type
        self.channel = channel
        self.commodity_type = commodity_type
        self.contact_name = contact_name
        self.description = description
        self.ext_info = ext_info
        self.grade = grade
        self.mobile = mobile
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.area is not None:
            result['Area'] = self.area

        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.channel is not None:
            result['Channel'] = self.channel

        if self.commodity_type is not None:
            result['CommodityType'] = self.commodity_type

        if self.contact_name is not None:
            result['ContactName'] = self.contact_name

        if self.description is not None:
            result['Description'] = self.description

        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info

        if self.grade is not None:
            result['Grade'] = self.grade

        if self.mobile is not None:
            result['Mobile'] = self.mobile

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Area') is not None:
            self.area = m.get('Area')

        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('Channel') is not None:
            self.channel = m.get('Channel')

        if m.get('CommodityType') is not None:
            self.commodity_type = m.get('CommodityType')

        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')

        if m.get('Grade') is not None:
            self.grade = m.get('Grade')

        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

