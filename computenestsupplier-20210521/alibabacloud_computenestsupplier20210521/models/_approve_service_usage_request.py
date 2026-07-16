# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ApproveServiceUsageRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        comments: str = None,
        region_id: str = None,
        service_id: str = None,
        type: int = None,
        user_ali_uid: int = None,
    ):
        # A client token that ensures the idempotence of the request. Generate a unique value from your client for each request. The token can contain only ASCII characters.
        self.client_token = client_token
        # The approval comments.
        self.comments = comments
        # The region ID.
        self.region_id = region_id
        # The service ID.
        # 
        # This parameter is required.
        self.service_id = service_id
        # The service sharing type. The default value is SharedAccount. Valid values:
        # 
        # - SharedAccount: The regular sharing type.
        # 
        # - Reseller: The reseller sharing type.
        self.type = type
        # The UID of the user\\"s Alibaba Cloud account.
        # 
        # This parameter is required.
        self.user_ali_uid = user_ali_uid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.comments is not None:
            result['Comments'] = self.comments

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.service_id is not None:
            result['ServiceId'] = self.service_id

        if self.type is not None:
            result['Type'] = self.type

        if self.user_ali_uid is not None:
            result['UserAliUid'] = self.user_ali_uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Comments') is not None:
            self.comments = m.get('Comments')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UserAliUid') is not None:
            self.user_ali_uid = m.get('UserAliUid')

        return self

