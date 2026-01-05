# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CheckKMSAuthorizedResponseBody(DaraModel):
    def __init__(
        self,
        authorization_state: int = None,
        dbcluster_id: str = None,
        request_id: str = None,
        role_arn: str = None,
    ):
        # Indicates whether the cluster is authorized to use KMS. Valid values:
        # 
        # *   **0**: no.
        # *   **1**: yes.
        self.authorization_state = authorization_state
        # The cluster ID.
        self.dbcluster_id = dbcluster_id
        # The request ID.
        self.request_id = request_id
        # The Alibaba Cloud Resource Name (ARN) of the RAM role. A RAM role is a virtual identity that you can create within your Alibaba Cloud account. For more information, see [RAM role overview](https://help.aliyun.com/document_detail/93689.html).
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

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizationState') is not None:
            self.authorization_state = m.get('AuthorizationState')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')

        return self

