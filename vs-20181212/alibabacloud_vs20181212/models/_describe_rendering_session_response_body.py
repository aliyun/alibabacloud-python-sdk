# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vs20181212 import models as main_models
from darabonba.model import DaraModel

class DescribeRenderingSessionResponseBody(DaraModel):
    def __init__(
        self,
        additional_ingresses: List[main_models.DescribeRenderingSessionResponseBodyAdditionalIngresses] = None,
        app_id: str = None,
        client_id: str = None,
        hostname: str = None,
        isp: str = None,
        location: main_models.DescribeRenderingSessionResponseBodyLocation = None,
        patch_id: str = None,
        port_mappings: List[main_models.DescribeRenderingSessionResponseBodyPortMappings] = None,
        rendering_instance_id: str = None,
        request_id: str = None,
        session_id: str = None,
        start_time: str = None,
        state_info: main_models.DescribeRenderingSessionResponseBodyStateInfo = None,
    ):
        self.additional_ingresses = additional_ingresses
        self.app_id = app_id
        self.client_id = client_id
        self.hostname = hostname
        self.isp = isp
        self.location = location
        self.patch_id = patch_id
        self.port_mappings = port_mappings
        self.rendering_instance_id = rendering_instance_id
        self.request_id = request_id
        self.session_id = session_id
        self.start_time = start_time
        self.state_info = state_info

    def validate(self):
        if self.additional_ingresses:
            for v1 in self.additional_ingresses:
                 if v1:
                    v1.validate()
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
        result['AdditionalIngresses'] = []
        if self.additional_ingresses is not None:
            for k1 in self.additional_ingresses:
                result['AdditionalIngresses'].append(k1.to_map() if k1 else None)

        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.client_id is not None:
            result['ClientId'] = self.client_id

        if self.hostname is not None:
            result['Hostname'] = self.hostname

        if self.isp is not None:
            result['Isp'] = self.isp

        if self.location is not None:
            result['Location'] = self.location.to_map()

        if self.patch_id is not None:
            result['PatchId'] = self.patch_id

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

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.state_info is not None:
            result['StateInfo'] = self.state_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.additional_ingresses = []
        if m.get('AdditionalIngresses') is not None:
            for k1 in m.get('AdditionalIngresses'):
                temp_model = main_models.DescribeRenderingSessionResponseBodyAdditionalIngresses()
                self.additional_ingresses.append(temp_model.from_map(k1))

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')

        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')

        if m.get('Isp') is not None:
            self.isp = m.get('Isp')

        if m.get('Location') is not None:
            temp_model = main_models.DescribeRenderingSessionResponseBodyLocation()
            self.location = temp_model.from_map(m.get('Location'))

        if m.get('PatchId') is not None:
            self.patch_id = m.get('PatchId')

        self.port_mappings = []
        if m.get('PortMappings') is not None:
            for k1 in m.get('PortMappings'):
                temp_model = main_models.DescribeRenderingSessionResponseBodyPortMappings()
                self.port_mappings.append(temp_model.from_map(k1))

        if m.get('RenderingInstanceId') is not None:
            self.rendering_instance_id = m.get('RenderingInstanceId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('StateInfo') is not None:
            temp_model = main_models.DescribeRenderingSessionResponseBodyStateInfo()
            self.state_info = temp_model.from_map(m.get('StateInfo'))

        return self

class DescribeRenderingSessionResponseBodyStateInfo(DaraModel):
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

class DescribeRenderingSessionResponseBodyPortMappings(DaraModel):
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

class DescribeRenderingSessionResponseBodyLocation(DaraModel):
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

class DescribeRenderingSessionResponseBodyAdditionalIngresses(DaraModel):
    def __init__(
        self,
        hostname: str = None,
        isp: str = None,
        port_mappings: List[main_models.DescribeRenderingSessionResponseBodyAdditionalIngressesPortMappings] = None,
    ):
        self.hostname = hostname
        self.isp = isp
        self.port_mappings = port_mappings

    def validate(self):
        if self.port_mappings:
            for v1 in self.port_mappings:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hostname is not None:
            result['Hostname'] = self.hostname

        if self.isp is not None:
            result['Isp'] = self.isp

        result['PortMappings'] = []
        if self.port_mappings is not None:
            for k1 in self.port_mappings:
                result['PortMappings'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')

        if m.get('Isp') is not None:
            self.isp = m.get('Isp')

        self.port_mappings = []
        if m.get('PortMappings') is not None:
            for k1 in m.get('PortMappings'):
                temp_model = main_models.DescribeRenderingSessionResponseBodyAdditionalIngressesPortMappings()
                self.port_mappings.append(temp_model.from_map(k1))

        return self

class DescribeRenderingSessionResponseBodyAdditionalIngressesPortMappings(DaraModel):
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

