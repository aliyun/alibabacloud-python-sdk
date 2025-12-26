# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class DescribeWuyingServerEipInfoResponseBody(DaraModel):
    def __init__(
        self,
        eip_info_model: main_models.DescribeWuyingServerEipInfoResponseBodyEipInfoModel = None,
        request_id: str = None,
    ):
        # The information about the associated EIP.
        self.eip_info_model = eip_info_model
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.eip_info_model:
            self.eip_info_model.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.eip_info_model is not None:
            result['EipInfoModel'] = self.eip_info_model.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EipInfoModel') is not None:
            temp_model = main_models.DescribeWuyingServerEipInfoResponseBodyEipInfoModel()
            self.eip_info_model = temp_model.from_map(m.get('EipInfoModel'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeWuyingServerEipInfoResponseBodyEipInfoModel(DaraModel):
    def __init__(
        self,
        eip_id: str = None,
        ip_address: str = None,
        network_interface_id: str = None,
        server_port_range: str = None,
    ):
        self.eip_id = eip_id
        # The public IP address.
        self.ip_address = ip_address
        # The ID of the elastic network interface (ENI).
        self.network_interface_id = network_interface_id
        # The port range.
        self.server_port_range = server_port_range

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.eip_id is not None:
            result['EipId'] = self.eip_id

        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address

        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id

        if self.server_port_range is not None:
            result['ServerPortRange'] = self.server_port_range

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EipId') is not None:
            self.eip_id = m.get('EipId')

        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')

        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')

        if m.get('ServerPortRange') is not None:
            self.server_port_range = m.get('ServerPortRange')

        return self

