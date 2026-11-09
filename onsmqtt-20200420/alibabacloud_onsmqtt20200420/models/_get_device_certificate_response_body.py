# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_onsmqtt20200420 import models as main_models
from darabonba.model import DaraModel

class GetDeviceCertificateResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetDeviceCertificateResponseBodyData = None,
        request_id: str = None,
    ):
        # Certificate details.
        self.data = data
        # Public parameters, each request ID is unique and can be used for troubleshooting and problem localization.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetDeviceCertificateResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetDeviceCertificateResponseBodyData(DaraModel):
    def __init__(
        self,
        ca_sn: str = None,
        device_content: str = None,
        device_name: str = None,
        device_sn: str = None,
        status: str = None,
        valid_begin: str = None,
        valid_end: str = None,
    ):
        # The SN serial number of the CA certificate to which the device certificate belongs, used to uniquely identify a CA certificate.
        self.ca_sn = ca_sn
        # Content of the device certificate.
        # 
        #  represents a new line.
        self.device_content = device_content
        # Name of the device certificate.
        self.device_name = device_name
        # The SN serial number of the device certificate, used to uniquely identify a device certificate.
        self.device_sn = device_sn
        # The status of the device certificate. The values are as follows:
        # - **0**: Indicates that the certificate is in an inactive state. - **1**: Indicates that the certificate is in an active state.
        # > After the device certificate is registered, it is in an active state by default.
        self.status = status
        # The start time when the device certificate becomes effective. The format is a Unix timestamp in milliseconds.
        self.valid_begin = valid_begin
        # The end time when the device certificate becomes effective. The format is a Unix timestamp in milliseconds.
        self.valid_end = valid_end

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ca_sn is not None:
            result['CaSn'] = self.ca_sn

        if self.device_content is not None:
            result['DeviceContent'] = self.device_content

        if self.device_name is not None:
            result['DeviceName'] = self.device_name

        if self.device_sn is not None:
            result['DeviceSn'] = self.device_sn

        if self.status is not None:
            result['Status'] = self.status

        if self.valid_begin is not None:
            result['ValidBegin'] = self.valid_begin

        if self.valid_end is not None:
            result['ValidEnd'] = self.valid_end

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CaSn') is not None:
            self.ca_sn = m.get('CaSn')

        if m.get('DeviceContent') is not None:
            self.device_content = m.get('DeviceContent')

        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')

        if m.get('DeviceSn') is not None:
            self.device_sn = m.get('DeviceSn')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('ValidBegin') is not None:
            self.valid_begin = m.get('ValidBegin')

        if m.get('ValidEnd') is not None:
            self.valid_end = m.get('ValidEnd')

        return self

