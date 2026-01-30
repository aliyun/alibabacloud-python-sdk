# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_vs20181212 import models as main_models
from darabonba.model import DaraModel

class RefreshRenderingInstanceStreamingRequest(DaraModel):
    def __init__(
        self,
        client_info: main_models.RefreshRenderingInstanceStreamingRequestClientInfo = None,
        rendering_instance_id: str = None,
    ):
        self.client_info = client_info
        # This parameter is required.
        self.rendering_instance_id = rendering_instance_id

    def validate(self):
        if self.client_info:
            self.client_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_info is not None:
            result['ClientInfo'] = self.client_info.to_map()

        if self.rendering_instance_id is not None:
            result['RenderingInstanceId'] = self.rendering_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientInfo') is not None:
            temp_model = main_models.RefreshRenderingInstanceStreamingRequestClientInfo()
            self.client_info = temp_model.from_map(m.get('ClientInfo'))

        if m.get('RenderingInstanceId') is not None:
            self.rendering_instance_id = m.get('RenderingInstanceId')

        return self

class RefreshRenderingInstanceStreamingRequestClientInfo(DaraModel):
    def __init__(
        self,
        client_ip: str = None,
        new_client: bool = None,
    ):
        self.client_ip = client_ip
        self.new_client = new_client

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip

        if self.new_client is not None:
            result['NewClient'] = self.new_client

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')

        if m.get('NewClient') is not None:
            self.new_client = m.get('NewClient')

        return self

