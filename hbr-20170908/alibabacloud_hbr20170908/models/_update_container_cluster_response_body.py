# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateContainerClusterResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        token: str = None,
        token_updated: bool = None,
    ):
        # Return code, 200 indicates success.
        self.code = code
        # Return information.
        self.message = message
        # Request ID.
        self.request_id = request_id
        # Indicates if the request was successful.
        # 
        # - true: Success
        # - false: Failure
        self.success = success
        # Cluster token, used for registering HBR clients within the cluster.
        self.token = token
        # Indicates whether the cluster token has been updated.
        self.token_updated = token_updated

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.token is not None:
            result['Token'] = self.token

        if self.token_updated is not None:
            result['TokenUpdated'] = self.token_updated

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Token') is not None:
            self.token = m.get('Token')

        if m.get('TokenUpdated') is not None:
            self.token_updated = m.get('TokenUpdated')

        return self

