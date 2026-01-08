# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetDownloadExcelListShrinkRequest(DaraModel):
    def __init__(
        self,
        biz_code: str = None,
        biz_extend_shrink: str = None,
        condition: str = None,
        country_names_shrink: str = None,
        end_date: str = None,
        group_id: str = None,
        group_ids_shrink: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        start_date: str = None,
    ):
        self.biz_code = biz_code
        self.biz_extend_shrink = biz_extend_shrink
        self.condition = condition
        self.country_names_shrink = country_names_shrink
        self.end_date = end_date
        self.group_id = group_id
        self.group_ids_shrink = group_ids_shrink
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.start_date = start_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code

        if self.biz_extend_shrink is not None:
            result['BizExtend'] = self.biz_extend_shrink

        if self.condition is not None:
            result['Condition'] = self.condition

        if self.country_names_shrink is not None:
            result['CountryNames'] = self.country_names_shrink

        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_ids_shrink is not None:
            result['GroupIds'] = self.group_ids_shrink

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')

        if m.get('BizExtend') is not None:
            self.biz_extend_shrink = m.get('BizExtend')

        if m.get('Condition') is not None:
            self.condition = m.get('Condition')

        if m.get('CountryNames') is not None:
            self.country_names_shrink = m.get('CountryNames')

        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupIds') is not None:
            self.group_ids_shrink = m.get('GroupIds')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        return self

