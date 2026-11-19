# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateServiceEndpointShrinkRequest(DaraModel):
    def __init__(
        self,
        body_shrink: str = None,
        client_token: str = None,
    ):
        # The service endpoint configurations to be modified in this request. Submit the supported modifiable name, bound version, invocation authentication configuration, elastic policy, or public network inbound switch based on the endpoint type. Router and hybrid ingress endpoints cannot be renamed. DEFAULT endpoints do not accept name or authentication configuration updates. When updating the elastic policy, you must specify both updateElasticity=true and clientToken.
        self.body_shrink = body_shrink
        # The client token. This parameter is required when updateElasticity is set to true and is verified by the server. Reuse the token and the original request for the same retry. Use a new token if the logical content changes. Passing different content with the same token returns InvalidParameter. The token must be 1 to 128 characters in length and can contain letters, digits, periods (.), underscores (_), colons (:), and hyphens (-). The scope is the tenant and workspace. The receipt is retained for 7 days from the time of successful acceptance. Replays do not extend the retention period. After expiration, it is verified again as a new submission.
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body_shrink is not None:
            result['body'] = self.body_shrink

        if self.client_token is not None:
            result['clientToken'] = self.client_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body_shrink = m.get('body')

        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        return self

