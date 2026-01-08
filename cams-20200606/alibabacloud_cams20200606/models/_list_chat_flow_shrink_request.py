# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListChatFlowShrinkRequest(DaraModel):
    def __init__(
        self,
        biz_code: str = None,
        biz_extend_shrink: str = None,
        flow_trigger_type: str = None,
        keyword: str = None,
        owner_id: int = None,
        page_no: int = None,
        page_size: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        return_with_online_version: bool = None,
        status: str = None,
    ):
        # Business tenant code, default is “ALICOM_OPAAS”.
        self.biz_code = biz_code
        # Business extension information, default is “{}”.
        self.biz_extend_shrink = biz_extend_shrink
        # Flow trigger type, enum values:
        # - TriggeredManually
        # - TriggeredByWhatsApp
        # - TriggeredByInstagram
        # - TriggeredByViber
        # - TriggeredByMessenger
        self.flow_trigger_type = flow_trigger_type
        # Search keyword.
        self.keyword = keyword
        self.owner_id = owner_id
        # Page number
        self.page_no = page_no
        # Page size.
        self.page_size = page_size
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Whether to return the online status
        self.return_with_online_version = return_with_online_version
        # Flow status
        self.status = status

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

        if self.flow_trigger_type is not None:
            result['FlowTriggerType'] = self.flow_trigger_type

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.return_with_online_version is not None:
            result['ReturnWithOnlineVersion'] = self.return_with_online_version

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')

        if m.get('BizExtend') is not None:
            self.biz_extend_shrink = m.get('BizExtend')

        if m.get('FlowTriggerType') is not None:
            self.flow_trigger_type = m.get('FlowTriggerType')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('ReturnWithOnlineVersion') is not None:
            self.return_with_online_version = m.get('ReturnWithOnlineVersion')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

