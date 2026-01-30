# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vs20181212 import models as main_models
from darabonba.model import DaraModel

class StartRenderingSessionResponseBody(DaraModel):
    def __init__(
        self,
        hostname: str = None,
        is_repeated_request: bool = None,
        location: main_models.StartRenderingSessionResponseBodyLocation = None,
        port_mappings: List[main_models.StartRenderingSessionResponseBodyPortMappings] = None,
        rendering_instance_id: str = None,
        request_id: str = None,
        session_id: str = None,
        state_info: main_models.StartRenderingSessionResponseBodyStateInfo = None,
    ):
        self.hostname = hostname
        self.is_repeated_request = is_repeated_request
        self.location = location
        self.port_mappings = port_mappings
        self.rendering_instance_id = rendering_instance_id
        self.request_id = request_id
        self.session_id = session_id
        self.state_info = state_info

    def validate(self):
        if self.location:
            self.location.validate()
        if self.port_mappings:
            for v1 in self.port_mappings:
                 if v1:
                    v1.validate()
        if self.state_info:
            self.state_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hostname is not None:
            result['Hostname'] = self.hostname

        if self.is_repeated_request is not None:
            result['IsRepeatedRequest'] = self.is_repeated_request

        if self.location is not None:
            result['Location'] = self.location.to_map()

        result['PortMappings'] = []
        if self.port_mappings is not None:
            for k1 in self.port_mappings:
                result['PortMappings'].append(k1.to_map() if k1 else None)

        if self.rendering_instance_id is not None:
            result['RenderingInstanceId'] = self.rendering_instance_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.state_info is not None:
            result['StateInfo'] = self.state_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')

        if m.get('IsRepeatedRequest') is not None:
            self.is_repeated_request = m.get('IsRepeatedRequest')

        if m.get('Location') is not None:
            temp_model = main_models.StartRenderingSessionResponseBodyLocation()
            self.location = temp_model.from_map(m.get('Location'))

        self.port_mappings = []
        if m.get('PortMappings') is not None:
            for k1 in m.get('PortMappings'):
                temp_model = main_models.StartRenderingSessionResponseBodyPortMappings()
                self.port_mappings.append(temp_model.from_map(k1))

        if m.get('RenderingInstanceId') is not None:
            self.rendering_instance_id = m.get('RenderingInstanceId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('StateInfo') is not None:
            temp_model = main_models.StartRenderingSessionResponseBodyStateInfo()
            self.state_info = temp_model.from_map(m.get('StateInfo'))

        return self

class StartRenderingSessionResponseBodyStateInfo(DaraModel):
    def __init__(
        self,
        comment: str = None,
        state: str = None,
        update_time: str = None,
    ):
        self.comment = comment
        self.state = state
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment

        if self.state is not None:
            result['State'] = self.state

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class StartRenderingSessionResponseBodyPortMappings(DaraModel):
    def __init__(
        self,
        external_port: str = None,
        internal_port: str = None,
    ):
        self.external_port = external_port
        self.internal_port = internal_port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.external_port is not None:
            result['ExternalPort'] = self.external_port

        if self.internal_port is not None:
            result['InternalPort'] = self.internal_port

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExternalPort') is not None:
            self.external_port = m.get('ExternalPort')

        if m.get('InternalPort') is not None:
            self.internal_port = m.get('InternalPort')

        return self

class StartRenderingSessionResponseBodyLocation(DaraModel):
    def __init__(
        self,
        province_code: str = None,
    ):
        self.province_code = province_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.province_code is not None:
            result['ProvinceCode'] = self.province_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProvinceCode') is not None:
            self.province_code = m.get('ProvinceCode')

        return self

