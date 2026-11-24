# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateThirdAppAccessTokenShrinkRequest(DaraModel):
    def __init__(
        self,
        authorizer_id: str = None,
        business_channel: str = None,
        expiration: int = None,
        resource_shrink: str = None,
    ):
        # The WyId of the authorized user. The user must belong to the current calling account. This parameter is not the username.
        # 
        # This parameter is required.
        self.authorizer_id = authorizer_id
        # The business channel. Valid values: Enterprise and Business. The value is case-insensitive. If omitted, the default value is Enterprise. If an empty string or other values are explicitly passed, a parameter error is returned. This parameter does not replace user identity verification.
        self.business_channel = business_channel
        # The validity period of the token, in seconds. Valid values: 1 to 15552000. If omitted, the default value is 15552000, which equals 180 days. Permanent validity is not supported, and 0 cannot be passed.
        self.expiration = expiration
        # The target single cloud desktop resource. You must provide this object along with ResourceType and ResourceId when you call this operation. Pass this parameter as a JSON object and specify only one cloud desktop. Wildcards or authorization for all cloud desktops are not supported.
        self.resource_shrink = resource_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authorizer_id is not None:
            result['AuthorizerId'] = self.authorizer_id

        if self.business_channel is not None:
            result['BusinessChannel'] = self.business_channel

        if self.expiration is not None:
            result['Expiration'] = self.expiration

        if self.resource_shrink is not None:
            result['Resource'] = self.resource_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizerId') is not None:
            self.authorizer_id = m.get('AuthorizerId')

        if m.get('BusinessChannel') is not None:
            self.business_channel = m.get('BusinessChannel')

        if m.get('Expiration') is not None:
            self.expiration = m.get('Expiration')

        if m.get('Resource') is not None:
            self.resource_shrink = m.get('Resource')

        return self

