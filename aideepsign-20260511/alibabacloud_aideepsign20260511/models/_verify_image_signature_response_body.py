# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aideepsign20260511 import models as main_models
from darabonba.model import DaraModel

class VerifyImageSignatureResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        issuer: main_models.VerifyImageSignatureResponseBodyIssuer = None,
        issuer_trusted: bool = None,
        manifest: main_models.VerifyImageSignatureResponseBodyManifest = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        verification_state: str = None,
    ):
        # The business error code. The value "OK" is returned if the request is successful.
        self.code = code
        # The HTTP status code. The value `200` is returned if the request is successful.
        self.http_status_code = http_status_code
        # The issuer information.
        self.issuer = issuer
        # Indicates whether the issuer is trusted. A value of true indicates that the issuer certificate is issued by a trusted CA.
        self.issuer_trusted = issuer_trusted
        # The content credentials manifest information. This parameter is returned only when the image contains a C2PA signature.
        self.manifest = manifest
        # The additional information. The value `success` is returned if the request is successful.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success
        # The signature verification status. Valid values:
        # - Valid: The signature is valid.
        # - Invalid: The signature is invalid or has been tampered with.
        # - Trusted: The signature is valid and trusted.
        self.verification_state = verification_state

    def validate(self):
        if self.issuer:
            self.issuer.validate()
        if self.manifest:
            self.manifest.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.issuer is not None:
            result['Issuer'] = self.issuer.to_map()

        if self.issuer_trusted is not None:
            result['IssuerTrusted'] = self.issuer_trusted

        if self.manifest is not None:
            result['Manifest'] = self.manifest.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.verification_state is not None:
            result['VerificationState'] = self.verification_state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Issuer') is not None:
            temp_model = main_models.VerifyImageSignatureResponseBodyIssuer()
            self.issuer = temp_model.from_map(m.get('Issuer'))

        if m.get('IssuerTrusted') is not None:
            self.issuer_trusted = m.get('IssuerTrusted')

        if m.get('Manifest') is not None:
            temp_model = main_models.VerifyImageSignatureResponseBodyManifest()
            self.manifest = temp_model.from_map(m.get('Manifest'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('VerificationState') is not None:
            self.verification_state = m.get('VerificationState')

        return self

class VerifyImageSignatureResponseBodyManifest(DaraModel):
    def __init__(
        self,
        assertions: List[main_models.VerifyImageSignatureResponseBodyManifestAssertions] = None,
        signature_info: main_models.VerifyImageSignatureResponseBodyManifestSignatureInfo = None,
    ):
        # The list of assertions, which contains metadata such as the origin and editing history of the image.
        self.assertions = assertions
        # The signature details.
        self.signature_info = signature_info

    def validate(self):
        if self.assertions:
            for v1 in self.assertions:
                 if v1:
                    v1.validate()
        if self.signature_info:
            self.signature_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Assertions'] = []
        if self.assertions is not None:
            for k1 in self.assertions:
                result['Assertions'].append(k1.to_map() if k1 else None)

        if self.signature_info is not None:
            result['SignatureInfo'] = self.signature_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.assertions = []
        if m.get('Assertions') is not None:
            for k1 in m.get('Assertions'):
                temp_model = main_models.VerifyImageSignatureResponseBodyManifestAssertions()
                self.assertions.append(temp_model.from_map(k1))

        if m.get('SignatureInfo') is not None:
            temp_model = main_models.VerifyImageSignatureResponseBodyManifestSignatureInfo()
            self.signature_info = temp_model.from_map(m.get('SignatureInfo'))

        return self

class VerifyImageSignatureResponseBodyManifestSignatureInfo(DaraModel):
    def __init__(
        self,
        alg: str = None,
        issuer: str = None,
        time: str = None,
    ):
        # The signature algorithm, such as `ps256` or `es256`.
        self.alg = alg
        # The distinguished name (DN) of the signing certificate issuer.
        self.issuer = issuer
        # The signing time in ISO 8601 format.
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alg is not None:
            result['Alg'] = self.alg

        if self.issuer is not None:
            result['Issuer'] = self.issuer

        if self.time is not None:
            result['Time'] = self.time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alg') is not None:
            self.alg = m.get('Alg')

        if m.get('Issuer') is not None:
            self.issuer = m.get('Issuer')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        return self

class VerifyImageSignatureResponseBodyManifestAssertions(DaraModel):
    def __init__(
        self,
        data: str = None,
        label: str = None,
    ):
        # The assertion data, which is detailed metadata in JSON format.
        self.data = data
        # The assertion label, such as c2pa.actions or stds.exif.
        self.label = label

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data

        if self.label is not None:
            result['Label'] = self.label

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        return self

class VerifyImageSignatureResponseBodyIssuer(DaraModel):
    def __init__(
        self,
        common_name: str = None,
        organization: str = None,
    ):
        # The common name (CN) of the issuer.
        self.common_name = common_name
        # The organization name (O) of the issuer.
        self.organization = organization

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.common_name is not None:
            result['CommonName'] = self.common_name

        if self.organization is not None:
            result['Organization'] = self.organization

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommonName') is not None:
            self.common_name = m.get('CommonName')

        if m.get('Organization') is not None:
            self.organization = m.get('Organization')

        return self

