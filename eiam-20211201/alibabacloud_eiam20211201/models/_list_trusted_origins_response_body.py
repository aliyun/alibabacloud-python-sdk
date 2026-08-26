# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class ListTrustedOriginsResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
        trusted_origins: List[main_models.ListTrustedOriginsResponseBodyTrustedOrigins] = None,
    ):
        # The number of entries per page that takes effect for this request.
        self.max_results = max_results
        # The token for the next page query.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries.
        self.total_count = total_count
        # The list of trusted origins.
        self.trusted_origins = trusted_origins

    def validate(self):
        if self.trusted_origins:
            for v1 in self.trusted_origins:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        result['TrustedOrigins'] = []
        if self.trusted_origins is not None:
            for k1 in self.trusted_origins:
                result['TrustedOrigins'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.trusted_origins = []
        if m.get('TrustedOrigins') is not None:
            for k1 in m.get('TrustedOrigins'):
                temp_model = main_models.ListTrustedOriginsResponseBodyTrustedOrigins()
                self.trusted_origins.append(temp_model.from_map(k1))

        return self

class ListTrustedOriginsResponseBodyTrustedOrigins(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        instance_id: str = None,
        origin: str = None,
        status: str = None,
        trust_origin_name: str = None,
        trusted_origin_id: str = None,
        trusted_origin_scene: List[str] = None,
        update_time: str = None,
    ):
        # The creation time.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.create_time = create_time
        # The instance ID.
        self.instance_id = instance_id
        # The browser origin.
        self.origin = origin
        # The status.
        self.status = status
        # The trusted origin name.
        self.trust_origin_name = trust_origin_name
        # The trusted origin ID.
        self.trusted_origin_id = trusted_origin_id
        # The trusted origin scene.
        self.trusted_origin_scene = trusted_origin_scene
        # The update time.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.origin is not None:
            result['Origin'] = self.origin

        if self.status is not None:
            result['Status'] = self.status

        if self.trust_origin_name is not None:
            result['TrustOriginName'] = self.trust_origin_name

        if self.trusted_origin_id is not None:
            result['TrustedOriginId'] = self.trusted_origin_id

        if self.trusted_origin_scene is not None:
            result['TrustedOriginScene'] = self.trusted_origin_scene

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Origin') is not None:
            self.origin = m.get('Origin')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TrustOriginName') is not None:
            self.trust_origin_name = m.get('TrustOriginName')

        if m.get('TrustedOriginId') is not None:
            self.trusted_origin_id = m.get('TrustedOriginId')

        if m.get('TrustedOriginScene') is not None:
            self.trusted_origin_scene = m.get('TrustedOriginScene')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

