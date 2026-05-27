# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddInboundNumberShrinkRequest(DaraModel):
    def __init__(
        self,
        application_code: str = None,
        inbound_numbers_shrink: str = None,
        inbound_type: int = None,
        line_code: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # This parameter is required.
        self.application_code = application_code
        # This parameter is required.
        self.inbound_numbers_shrink = inbound_numbers_shrink
        # This parameter is required.
        self.inbound_type = inbound_type
        self.line_code = line_code
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_code is not None:
            result['ApplicationCode'] = self.application_code

        if self.inbound_numbers_shrink is not None:
            result['InboundNumbers'] = self.inbound_numbers_shrink

        if self.inbound_type is not None:
            result['InboundType'] = self.inbound_type

        if self.line_code is not None:
            result['LineCode'] = self.line_code

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationCode') is not None:
            self.application_code = m.get('ApplicationCode')

        if m.get('InboundNumbers') is not None:
            self.inbound_numbers_shrink = m.get('InboundNumbers')

        if m.get('InboundType') is not None:
            self.inbound_type = m.get('InboundType')

        if m.get('LineCode') is not None:
            self.line_code = m.get('LineCode')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

