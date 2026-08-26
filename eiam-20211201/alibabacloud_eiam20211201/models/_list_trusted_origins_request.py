# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListTrustedOriginsRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        max_results: int = None,
        next_token: str = None,
        origin: str = None,
        status: str = None,
        trust_origin_name: str = None,
        trusted_origin_scene: List[str] = None,
    ):
        # The ID of the IDaaS EIAM instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The number of entries per page. Default value: 20. Maximum value: 100. If you set this parameter to 0, the default value is used.
        self.max_results = max_results
        # The NextToken returned by the previous call.
        self.next_token = next_token
        # Filters by the exact normalized origin.
        self.origin = origin
        # Filters by exact status. Valid values: Enabled or Disabled.
        self.status = status
        # Filters by exact name.
        self.trust_origin_name = trust_origin_name
        # Filters by exact trusted origin scene. You can specify at most one value.
        self.trusted_origin_scene = trusted_origin_scene

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.origin is not None:
            result['Origin'] = self.origin

        if self.status is not None:
            result['Status'] = self.status

        if self.trust_origin_name is not None:
            result['TrustOriginName'] = self.trust_origin_name

        if self.trusted_origin_scene is not None:
            result['TrustedOriginScene'] = self.trusted_origin_scene

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('Origin') is not None:
            self.origin = m.get('Origin')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TrustOriginName') is not None:
            self.trust_origin_name = m.get('TrustOriginName')

        if m.get('TrustedOriginScene') is not None:
            self.trusted_origin_scene = m.get('TrustedOriginScene')

        return self

