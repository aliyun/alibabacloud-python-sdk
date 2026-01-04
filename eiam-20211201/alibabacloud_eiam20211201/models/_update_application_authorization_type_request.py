# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateApplicationAuthorizationTypeRequest(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        authorization_type: str = None,
        instance_id: str = None,
    ):
        # The ID of the application that you want to modify.
        # 
        # This parameter is required.
        self.application_id = application_id
        # The authorization type of the application. Valid values:
        # 
        # *   authorize_required: Only the user with explicit authorization can access the application.
        # *   default_all: By default, all users can access the application.
        # 
        # This parameter is required.
        self.authorization_type = authorization_type
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.authorization_type is not None:
            result['AuthorizationType'] = self.authorization_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('AuthorizationType') is not None:
            self.authorization_type = m.get('AuthorizationType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

