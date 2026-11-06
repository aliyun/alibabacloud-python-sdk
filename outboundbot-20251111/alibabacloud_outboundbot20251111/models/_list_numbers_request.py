# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListNumbersRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        number: str = None,
        page_number: int = None,
        page_size: int = None,
        sip_trunk_id: str = None,
        tenant_id: str = None,
    ):
        # The instance ID.
        self.instance_id = instance_id
        # The bound phone number.
        self.number = number
        # The page number.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The number of entries per page.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The SIP trunk ID.
        self.sip_trunk_id = sip_trunk_id
        # The tenant ID.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.number is not None:
            result['Number'] = self.number

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.sip_trunk_id is not None:
            result['SipTrunkId'] = self.sip_trunk_id

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Number') is not None:
            self.number = m.get('Number')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SipTrunkId') is not None:
            self.sip_trunk_id = m.get('SipTrunkId')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        return self

