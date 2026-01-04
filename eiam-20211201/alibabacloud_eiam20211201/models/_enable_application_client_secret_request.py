# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EnableApplicationClientSecretRequest(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        instance_id: str = None,
        secret_id: str = None,
    ):
        # The ID of the application.
        # 
        # This parameter is required.
        self.application_id = application_id
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The client key ID of the application.
        # 
        # This parameter is required.
        self.secret_id = secret_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.secret_id is not None:
            result['SecretId'] = self.secret_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('SecretId') is not None:
            self.secret_id = m.get('SecretId')

        return self

