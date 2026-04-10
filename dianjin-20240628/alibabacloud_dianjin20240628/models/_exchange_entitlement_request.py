# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ExchangeEntitlementRequest(DaraModel):
    def __init__(
        self,
        external_user_id: str = None,
        key_hash: str = None,
        request_id: str = None,
        template_id: int = None,
        user_name: str = None,
    ):
        # This parameter is required.
        self.external_user_id = external_user_id
        self.key_hash = key_hash
        # This parameter is required.
        self.request_id = request_id
        # This parameter is required.
        self.template_id = template_id
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.external_user_id is not None:
            result['externalUserId'] = self.external_user_id

        if self.key_hash is not None:
            result['keyHash'] = self.key_hash

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.template_id is not None:
            result['templateId'] = self.template_id

        if self.user_name is not None:
            result['userName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('externalUserId') is not None:
            self.external_user_id = m.get('externalUserId')

        if m.get('keyHash') is not None:
            self.key_hash = m.get('keyHash')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('templateId') is not None:
            self.template_id = m.get('templateId')

        if m.get('userName') is not None:
            self.user_name = m.get('userName')

        return self

