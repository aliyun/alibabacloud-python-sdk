# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_smartag20180313 import models as main_models
from darabonba.model import DaraModel

class AddSmartAccessGatewayDnsForwardResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.AddSmartAccessGatewayDnsForwardResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code. A value of 200 indicates that the call is successful.
        self.code = code
        # The information returned for the request.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The response message.
        self.message = message
        # Id of the request
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.AddSmartAccessGatewayDnsForwardResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class AddSmartAccessGatewayDnsForwardResponseBodyData(DaraModel):
    def __init__(
        self,
        domain: str = None,
        instance_id: str = None,
        master_ip: str = None,
        mode: str = None,
        outbound_port_index: int = None,
        outbound_port_name: str = None,
        outbound_port_type: str = None,
        slave_ip: str = None,
    ):
        # The domain name.
        self.domain = domain
        # The ID of the instance.
        self.instance_id = instance_id
        # The primary DNS server.
        self.master_ip = master_ip
        # The forwarding mode.
        self.mode = mode
        # The number of the egress port.
        self.outbound_port_index = outbound_port_index
        # The egress port.
        self.outbound_port_name = outbound_port_name
        # The type of the egress port.
        self.outbound_port_type = outbound_port_type
        # The secondary DNS server.
        self.slave_ip = slave_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain is not None:
            result['Domain'] = self.domain

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.master_ip is not None:
            result['MasterIp'] = self.master_ip

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.outbound_port_index is not None:
            result['OutboundPortIndex'] = self.outbound_port_index

        if self.outbound_port_name is not None:
            result['OutboundPortName'] = self.outbound_port_name

        if self.outbound_port_type is not None:
            result['OutboundPortType'] = self.outbound_port_type

        if self.slave_ip is not None:
            result['SlaveIp'] = self.slave_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MasterIp') is not None:
            self.master_ip = m.get('MasterIp')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('OutboundPortIndex') is not None:
            self.outbound_port_index = m.get('OutboundPortIndex')

        if m.get('OutboundPortName') is not None:
            self.outbound_port_name = m.get('OutboundPortName')

        if m.get('OutboundPortType') is not None:
            self.outbound_port_type = m.get('OutboundPortType')

        if m.get('SlaveIp') is not None:
            self.slave_ip = m.get('SlaveIp')

        return self

