# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_onsmqtt20200420 import models as main_models
from darabonba.model import DaraModel

class GetCaCertificateResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetCaCertificateResponseBodyData = None,
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
            temp_model = main_models.GetCaCertificateResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetCaCertificateResponseBodyData(DaraModel):
    def __init__(
        self,
        ca_content: str = None,
        ca_name: str = None,
        registration_code: str = None,
        sn: str = None,
        status: str = None,
        valid_begin: str = None,
        valid_end: str = None,
        verification_content: str = None,
    ):
        # Content of the CA certificate.
        # > \\n represents a new line.
        self.ca_content = ca_content
        # Name of the CA certificate
        self.ca_name = ca_name
        # Registration code of the CA certificate
        self.registration_code = registration_code
        # The SN serial number of the CA certificate, used to uniquely identify a CA certificate. Value range: no more than 128 bytes.
        self.sn = sn
        # The status of the CA certificate. The values are as follows:
        # - **0**: Indicates that the certificate is in an inactive state. - **1**: Indicates that the certificate is in an active state.
        # > After the CA certificate is registered, it is in an active state by default.
        self.status = status
        # The start time when the CA certificate becomes effective. The format is a Unix timestamp in milliseconds.
        self.valid_begin = valid_begin
        # The end time when the CA certificate becomes effective. The format is a Unix timestamp in milliseconds.
        self.valid_end = valid_end
        # Content of the Verification certificate.
        # > \\n represents a new line.
        self.verification_content = verification_content

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ca_content is not None:
            result['CaContent'] = self.ca_content

        if self.ca_name is not None:
            result['CaName'] = self.ca_name

        if self.registration_code is not None:
            result['RegistrationCode'] = self.registration_code

        if self.sn is not None:
            result['Sn'] = self.sn

        if self.status is not None:
            result['Status'] = self.status

        if self.valid_begin is not None:
            result['ValidBegin'] = self.valid_begin

        if self.valid_end is not None:
            result['ValidEnd'] = self.valid_end

        if self.verification_content is not None:
            result['VerificationContent'] = self.verification_content

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CaContent') is not None:
            self.ca_content = m.get('CaContent')

        if m.get('CaName') is not None:
            self.ca_name = m.get('CaName')

        if m.get('RegistrationCode') is not None:
            self.registration_code = m.get('RegistrationCode')

        if m.get('Sn') is not None:
            self.sn = m.get('Sn')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('ValidBegin') is not None:
            self.valid_begin = m.get('ValidBegin')

        if m.get('ValidEnd') is not None:
            self.valid_end = m.get('ValidEnd')

        if m.get('VerificationContent') is not None:
            self.verification_content = m.get('VerificationContent')

        return self

