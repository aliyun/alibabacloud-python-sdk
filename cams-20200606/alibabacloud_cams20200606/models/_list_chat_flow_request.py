# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class ListChatFlowRequest(DaraModel):
    def __init__(
        self,
        biz_code: str = None,
        biz_extend: Dict[str, Any] = None,
        flow_code: str = None,
        flow_status: str = None,
        flow_trigger_type: str = None,
        keyword: str = None,
        owner_id: int = None,
        page_no: int = None,
        page_size: int = None,
        phone_number: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        return_with_online_version: bool = None,
        status: str = None,
        title: str = None,
    ):
        # The business tenant code. Default value: ALICOM_OPAAS.
        self.biz_code = biz_code
        # The business extension information. Default value: an empty collection.
        self.biz_extend = biz_extend
        # flowCode
        self.flow_code = flow_code
        # The flow status.
        self.flow_status = flow_status
        # The flow trigger type. Valid values:
        # - TriggeredManually
        # - TriggeredByWhatsApp
        # - TriggeredByInstagram
        # - TriggeredByViber
        # - TriggeredByMessenger
        self.flow_trigger_type = flow_trigger_type
        # The search keyword. This parameter is used for fuzzy match of flow names.
        self.keyword = keyword
        self.owner_id = owner_id
        # The page number.
        self.page_no = page_no
        # The number of entries per page.
        self.page_size = page_size
        # The phone number.
        self.phone_number = phone_number
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Specifies whether to return the online status. Valid values:
        # 
        # - true: Yes.
        # 
        # - false: No.
        self.return_with_online_version = return_with_online_version
        # The flow status. Default value: NORMAL.
        self.status = status
        # The title.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code

        if self.biz_extend is not None:
            result['BizExtend'] = self.biz_extend

        if self.flow_code is not None:
            result['FlowCode'] = self.flow_code

        if self.flow_status is not None:
            result['FlowStatus'] = self.flow_status

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

        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.return_with_online_version is not None:
            result['ReturnWithOnlineVersion'] = self.return_with_online_version

        if self.status is not None:
            result['Status'] = self.status

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')

        if m.get('BizExtend') is not None:
            self.biz_extend = m.get('BizExtend')

        if m.get('FlowCode') is not None:
            self.flow_code = m.get('FlowCode')

        if m.get('FlowStatus') is not None:
            self.flow_status = m.get('FlowStatus')

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

        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('ReturnWithOnlineVersion') is not None:
            self.return_with_online_version = m.get('ReturnWithOnlineVersion')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

