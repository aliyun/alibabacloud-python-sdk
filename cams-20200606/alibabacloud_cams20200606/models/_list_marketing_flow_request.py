# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class ListMarketingFlowRequest(DaraModel):
    def __init__(
        self,
        activity_code: str = None,
        activity_name: str = None,
        activity_status: str = None,
        biz_code: str = None,
        biz_extend: Dict[str, Any] = None,
        owner_id: int = None,
        page_index: str = None,
        page_size: str = None,
        related_flow_code: str = None,
        related_group_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.activity_code = activity_code
        self.activity_name = activity_name
        self.activity_status = activity_status
        self.biz_code = biz_code
        self.biz_extend = biz_extend
        self.owner_id = owner_id
        self.page_index = page_index
        self.page_size = page_size
        self.related_flow_code = related_flow_code
        self.related_group_id = related_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.activity_code is not None:
            result['ActivityCode'] = self.activity_code

        if self.activity_name is not None:
            result['ActivityName'] = self.activity_name

        if self.activity_status is not None:
            result['ActivityStatus'] = self.activity_status

        if self.biz_code is not None:
            result['BizCode'] = self.biz_code

        if self.biz_extend is not None:
            result['BizExtend'] = self.biz_extend

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_index is not None:
            result['PageIndex'] = self.page_index

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.related_flow_code is not None:
            result['RelatedFlowCode'] = self.related_flow_code

        if self.related_group_id is not None:
            result['RelatedGroupId'] = self.related_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivityCode') is not None:
            self.activity_code = m.get('ActivityCode')

        if m.get('ActivityName') is not None:
            self.activity_name = m.get('ActivityName')

        if m.get('ActivityStatus') is not None:
            self.activity_status = m.get('ActivityStatus')

        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')

        if m.get('BizExtend') is not None:
            self.biz_extend = m.get('BizExtend')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RelatedFlowCode') is not None:
            self.related_flow_code = m.get('RelatedFlowCode')

        if m.get('RelatedGroupId') is not None:
            self.related_group_id = m.get('RelatedGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

