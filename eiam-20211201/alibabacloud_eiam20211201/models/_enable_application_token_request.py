# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EnableApplicationTokenRequest(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        application_token_id: str = None,
        instance_id: str = None,
    ):
        # IDaaS的应用资源ID。
        # 
        # This parameter is required.
        self.application_id = application_id
        # IDaaS的应用资源TokenID。
        # 
        # This parameter is required.
        self.application_token_id = application_token_id
        # IDaaS EIAM实例的ID。
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

        if self.application_token_id is not None:
            result['ApplicationTokenId'] = self.application_token_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('ApplicationTokenId') is not None:
            self.application_token_id = m.get('ApplicationTokenId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

