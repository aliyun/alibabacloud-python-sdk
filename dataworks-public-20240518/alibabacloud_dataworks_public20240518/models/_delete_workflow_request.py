# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteWorkflowRequest(DaraModel):
    def __init__(
        self,
        client_unique_code: str = None,
        env_type: str = None,
        id: int = None,
    ):
        # The unique code of the client. This parameter is used to create a workflow asynchronously and implement the idempotence of the workflow. If you do not specify this parameter when you create the workflow, the system automatically generates a unique code. The unique code is uniquely associated with the workflow ID. If you specify this parameter when you update or delete the workflow, the value of this parameter must be the unique code that is used to create the workflow.
        self.client_unique_code = client_unique_code
        # The environment of the workspace. Valid values:
        # 
        # *   Prod: production environment
        # *   Dev: development environment
        self.env_type = env_type
        # The workflow ID.
        # 
        # This parameter is required.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_unique_code is not None:
            result['ClientUniqueCode'] = self.client_unique_code

        if self.env_type is not None:
            result['EnvType'] = self.env_type

        if self.id is not None:
            result['Id'] = self.id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientUniqueCode') is not None:
            self.client_unique_code = m.get('ClientUniqueCode')

        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        return self

