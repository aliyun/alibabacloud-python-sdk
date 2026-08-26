# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class GetTrustedOriginResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        trusted_origin: main_models.GetTrustedOriginResponseBodyTrustedOrigin = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The trusted origin.
        self.trusted_origin = trusted_origin

    def validate(self):
        if self.trusted_origin:
            self.trusted_origin.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.trusted_origin is not None:
            result['TrustedOrigin'] = self.trusted_origin.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TrustedOrigin') is not None:
            temp_model = main_models.GetTrustedOriginResponseBodyTrustedOrigin()
            self.trusted_origin = temp_model.from_map(m.get('TrustedOrigin'))

        return self

class GetTrustedOriginResponseBodyTrustedOrigin(DaraModel):
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
        # The name of the trusted origin.
        self.trust_origin_name = trust_origin_name
        # The ID of the trusted origin.
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

