# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CheckCloudResourceAuthorizedResponseBody(DaraModel):
    def __init__(
        self,
        authorization_state: int = None,
        request_id: str = None,
        role_arn: str = None,
    ):
        # The authorization status. Valid values:
        # - **1**: Authorized.
        # - **0**: Not authorized.
        self.authorization_state = authorization_state
        # The request ID.
        self.request_id = request_id
        # The global resource descriptor of the role, which is used to specify a specific role. For details, see [RAM role overview](https://help.aliyun.com/document_detail/93689.html).
        self.role_arn = role_arn

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authorization_state is not None:
            result['AuthorizationState'] = self.authorization_state

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizationState') is not None:
            self.authorization_state = m.get('AuthorizationState')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')

        return self

