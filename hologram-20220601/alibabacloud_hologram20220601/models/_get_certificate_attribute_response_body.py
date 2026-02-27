# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_hologram20220601 import models as main_models
from darabonba.model import DaraModel

class GetCertificateAttributeResponseBody(DaraModel):
    def __init__(
        self,
        certificate_attribute_dto: main_models.GetCertificateAttributeResponseBodyCertificateAttributeDto = None,
        error_code: str = None,
        error_message: str = None,
        http_status_code: str = None,
        success: bool = None,
        request_id: str = None,
    ):
        self.certificate_attribute_dto = certificate_attribute_dto
        self.error_code = error_code
        self.error_message = error_message
        self.http_status_code = http_status_code
        self.success = success
        self.request_id = request_id

    def validate(self):
        if self.certificate_attribute_dto:
            self.certificate_attribute_dto.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.certificate_attribute_dto is not None:
            result['CertificateAttributeDto'] = self.certificate_attribute_dto.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.success is not None:
            result['Success'] = self.success

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertificateAttributeDto') is not None:
            temp_model = main_models.GetCertificateAttributeResponseBodyCertificateAttributeDto()
            self.certificate_attribute_dto = temp_model.from_map(m.get('CertificateAttributeDto'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetCertificateAttributeResponseBodyCertificateAttributeDto(DaraModel):
    def __init__(
        self,
        enable_ssl: bool = None,
        expiration_time: int = None,
        status: str = None,
    ):
        self.enable_ssl = enable_ssl
        self.expiration_time = expiration_time
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_ssl is not None:
            result['enableSSL'] = self.enable_ssl

        if self.expiration_time is not None:
            result['expirationTime'] = self.expiration_time

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enableSSL') is not None:
            self.enable_ssl = m.get('enableSSL')

        if m.get('expirationTime') is not None:
            self.expiration_time = m.get('expirationTime')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

