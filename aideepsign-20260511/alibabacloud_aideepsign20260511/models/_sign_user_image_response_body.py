# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SignUserImageResponseBody(DaraModel):
    def __init__(
        self,
        algorithm: str = None,
        certificate_subject: str = None,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        object_key: str = None,
        request_id: str = None,
        sign_time: str = None,
        signed_image_url: str = None,
        success: bool = None,
    ):
        # The algorithm used for signing, such as ps256 or es256.
        self.algorithm = algorithm
        # The subject information of the signing certificate.
        self.certificate_subject = certificate_subject
        # The business error code. The value "OK" is returned if the request succeeds.
        self.code = code
        # The HTTP status code. The value 200 is returned if the request succeeds.
        self.http_status_code = http_status_code
        # The additional information. The value "success" is returned if the request succeeds.
        self.message = message
        # The ObjectKey of the signed image in OSS. You can use this value for subsequent API calls.
        self.object_key = object_key
        # The request ID.
        self.request_id = request_id
        # The signing time in ISO 8601 format, such as `2026-01-15T08:30:00Z`.
        self.sign_time = sign_time
        # The pre-signed download URL of the signed image.
        self.signed_image_url = signed_image_url
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm

        if self.certificate_subject is not None:
            result['CertificateSubject'] = self.certificate_subject

        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.object_key is not None:
            result['ObjectKey'] = self.object_key

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.sign_time is not None:
            result['SignTime'] = self.sign_time

        if self.signed_image_url is not None:
            result['SignedImageUrl'] = self.signed_image_url

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')

        if m.get('CertificateSubject') is not None:
            self.certificate_subject = m.get('CertificateSubject')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('ObjectKey') is not None:
            self.object_key = m.get('ObjectKey')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SignTime') is not None:
            self.sign_time = m.get('SignTime')

        if m.get('SignedImageUrl') is not None:
            self.signed_image_url = m.get('SignedImageUrl')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

