# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetLatestThirdAppAccessTokenShrinkRequest(DaraModel):
    def __init__(
        self,
        authorizer_id: str = None,
        business_channel: str = None,
        resource_shrink: str = None,
    ):
        # The WyId of the user used when the token was created. It must correspond to the current account and the target cloud desktop, and cannot be replaced by a username.
        # 
        # This parameter is required.
        self.authorizer_id = authorizer_id
        # The business channel. Valid values: Enterprise and Business. The value is case-insensitive. If omitted, the default value is Enterprise. If an empty string or other value is explicitly passed, a parameter error is returned. This parameter does not replace user identity verification.
        self.business_channel = business_channel
        # The target single cloud desktop resource. You must provide this object along with ResourceType and ResourceId when calling this operation. Pass it as a JSON object to specify only one cloud desktop. Wildcards or authorization for all cloud desktops are not supported.
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

        if self.resource_shrink is not None:
            result['Resource'] = self.resource_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizerId') is not None:
            self.authorizer_id = m.get('AuthorizerId')

        if m.get('BusinessChannel') is not None:
            self.business_channel = m.get('BusinessChannel')

        if m.get('Resource') is not None:
            self.resource_shrink = m.get('Resource')

        return self

