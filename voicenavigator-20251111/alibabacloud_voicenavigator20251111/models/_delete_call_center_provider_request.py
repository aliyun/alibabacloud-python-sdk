# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteCallCenterProviderRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        provider_id: str = None,
    ):
        self.instance_id = instance_id
        self.provider_id = provider_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.provider_id is not None:
            result['ProviderId'] = self.provider_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ProviderId') is not None:
            self.provider_id = m.get('ProviderId')

        return self

