# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_push20160801 import models as main_models
from darabonba.model import DaraModel

class CheckCertificateResponseBody(DaraModel):
    def __init__(
        self,
        android: bool = None,
        development_cert_info: main_models.CheckCertificateResponseBodyDevelopmentCertInfo = None,
        ios: bool = None,
        production_cert_info: main_models.CheckCertificateResponseBodyProductionCertInfo = None,
        request_id: str = None,
    ):
        # Indicates whether the AppKey belongs to an Android app:
        # 
        # - true
        # 
        # - false
        self.android = android
        # The information about the certificate for the development or sandbox environment.
        self.development_cert_info = development_cert_info
        # Indicates whether the AppKey belongs to an iOS app:
        # 
        # - true
        # 
        # - false
        self.ios = ios
        # The information about the certificate for the production environment.
        self.production_cert_info = production_cert_info
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.development_cert_info:
            self.development_cert_info.validate()
        if self.production_cert_info:
            self.production_cert_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.android is not None:
            result['Android'] = self.android

        if self.development_cert_info is not None:
            result['DevelopmentCertInfo'] = self.development_cert_info.to_map()

        if self.ios is not None:
            result['IOS'] = self.ios

        if self.production_cert_info is not None:
            result['ProductionCertInfo'] = self.production_cert_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Android') is not None:
            self.android = m.get('Android')

        if m.get('DevelopmentCertInfo') is not None:
            temp_model = main_models.CheckCertificateResponseBodyDevelopmentCertInfo()
            self.development_cert_info = temp_model.from_map(m.get('DevelopmentCertInfo'))

        if m.get('IOS') is not None:
            self.ios = m.get('IOS')

        if m.get('ProductionCertInfo') is not None:
            temp_model = main_models.CheckCertificateResponseBodyProductionCertInfo()
            self.production_cert_info = temp_model.from_map(m.get('ProductionCertInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CheckCertificateResponseBodyProductionCertInfo(DaraModel):
    def __init__(
        self,
        exipre_time: int = None,
        status: str = None,
    ):
        # The expiration time of the certificate.
        self.exipre_time = exipre_time
        # The status of the certificate. Valid values:
        # 
        # - **EXPIRED**: The certificate is expired.
        # 
        # - **NOT_CONFIGURED**: The certificate is not configured.
        # 
        # - **NO_PASSWORD**: The password for the certificate is not configured.
        # 
        # - **OK**: The certificate is normal.
        # 
        # - **REVOKED**: The certificate is revoked.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.exipre_time is not None:
            result['ExipreTime'] = self.exipre_time

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExipreTime') is not None:
            self.exipre_time = m.get('ExipreTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class CheckCertificateResponseBodyDevelopmentCertInfo(DaraModel):
    def __init__(
        self,
        exipre_time: int = None,
        status: str = None,
    ):
        # The expiration time of the certificate.
        self.exipre_time = exipre_time
        # The status of the certificate. Valid values:
        # 
        # - **EXPIRED**: The certificate is expired.
        # 
        # - **NOT_CONFIGURED**: The certificate is not configured.
        # 
        # - **NO_PASSWORD**: The password for the certificate is not configured.
        # 
        # - **OK**: The certificate is normal.
        # 
        # - **REVOKED**: The certificate is revoked.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.exipre_time is not None:
            result['ExipreTime'] = self.exipre_time

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExipreTime') is not None:
            self.exipre_time = m.get('ExipreTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

