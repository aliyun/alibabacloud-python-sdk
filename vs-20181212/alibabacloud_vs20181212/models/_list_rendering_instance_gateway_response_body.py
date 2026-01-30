# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vs20181212 import models as main_models
from darabonba.model import DaraModel

class ListRenderingInstanceGatewayResponseBody(DaraModel):
    def __init__(
        self,
        gateway_configuration_infos: List[main_models.ListRenderingInstanceGatewayResponseBodyGatewayConfigurationInfos] = None,
        page_number: str = None,
        page_size: str = None,
        request_id: str = None,
        total_count: str = None,
    ):
        self.gateway_configuration_infos = gateway_configuration_infos
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.gateway_configuration_infos:
            for v1 in self.gateway_configuration_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['GatewayConfigurationInfos'] = []
        if self.gateway_configuration_infos is not None:
            for k1 in self.gateway_configuration_infos:
                result['GatewayConfigurationInfos'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.gateway_configuration_infos = []
        if m.get('GatewayConfigurationInfos') is not None:
            for k1 in m.get('GatewayConfigurationInfos'):
                temp_model = main_models.ListRenderingInstanceGatewayResponseBodyGatewayConfigurationInfos()
                self.gateway_configuration_infos.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListRenderingInstanceGatewayResponseBodyGatewayConfigurationInfos(DaraModel):
    def __init__(
        self,
        creation_time: str = None,
        gateway_instance_id: str = None,
        rendering_instance_id: str = None,
        status: str = None,
        update_time: str = None,
    ):
        self.creation_time = creation_time
        self.gateway_instance_id = gateway_instance_id
        self.rendering_instance_id = rendering_instance_id
        self.status = status
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.gateway_instance_id is not None:
            result['GatewayInstanceId'] = self.gateway_instance_id

        if self.rendering_instance_id is not None:
            result['RenderingInstanceId'] = self.rendering_instance_id

        if self.status is not None:
            result['Status'] = self.status

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('GatewayInstanceId') is not None:
            self.gateway_instance_id = m.get('GatewayInstanceId')

        if m.get('RenderingInstanceId') is not None:
            self.rendering_instance_id = m.get('RenderingInstanceId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

