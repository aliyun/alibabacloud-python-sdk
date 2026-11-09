# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_onsmqtt20200420 import models as main_models
from darabonba.model import DaraModel

class ListDeviceCertificateResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListDeviceCertificateResponseBodyData = None,
        request_id: str = None,
    ):
        # Query result.
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
            temp_model = main_models.ListDeviceCertificateResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListDeviceCertificateResponseBodyData(DaraModel):
    def __init__(
        self,
        device_certificate_vos: List[main_models.ListDeviceCertificateResponseBodyDataDeviceCertificateVOS] = None,
        page_no: int = None,
        page_size: int = None,
        total: int = None,
    ):
        # Details of the device certificate.
        self.device_certificate_vos = device_certificate_vos
        # The current page number of the returned query records.
        self.page_no = page_no
        # The maximum number of results to display per page.
        self.page_size = page_size
        # Maximum number of pages in the query result.
        self.total = total

    def validate(self):
        if self.device_certificate_vos:
            for v1 in self.device_certificate_vos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DeviceCertificateVOS'] = []
        if self.device_certificate_vos is not None:
            for k1 in self.device_certificate_vos:
                result['DeviceCertificateVOS'].append(k1.to_map() if k1 else None)

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.device_certificate_vos = []
        if m.get('DeviceCertificateVOS') is not None:
            for k1 in m.get('DeviceCertificateVOS'):
                temp_model = main_models.ListDeviceCertificateResponseBodyDataDeviceCertificateVOS()
                self.device_certificate_vos.append(temp_model.from_map(k1))

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListDeviceCertificateResponseBodyDataDeviceCertificateVOS(DaraModel):
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
        # - 0: indicates that the certificate is in an inactive state. - 1: indicates that the certificate is in an active state.
        # After the device certificate is registered, it defaults to the active state.
        self.status = status
        # The start time when the device certificate becomes effective. The format is a Unix timestamp in milliseconds.
        self.valid_begin = valid_begin
        # The end time when the device certificate becomes effective. Formatted as a Unix timestamp in milliseconds.
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

