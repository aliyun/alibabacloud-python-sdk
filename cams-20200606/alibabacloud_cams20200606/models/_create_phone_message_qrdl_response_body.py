# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cams20200606 import models as main_models
from darabonba.model import DaraModel

class CreatePhoneMessageQrdlResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: main_models.CreatePhoneMessageQrdlResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        # If OK is returned, the request was successful.
        self.code = code
        # The returned data.
        self.data = data
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.CreatePhoneMessageQrdlResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreatePhoneMessageQrdlResponseBodyData(DaraModel):
    def __init__(
        self,
        deep_link_url: str = None,
        generate_qr_image: str = None,
        phone_number: str = None,
        prefilled_message: str = None,
        qr_image_url: str = None,
        qrdl_code: str = None,
    ):
        # The URL of the deep link.
        self.deep_link_url = deep_link_url
        # The format of the generated image.
        self.generate_qr_image = generate_qr_image
        # The phone number.
        self.phone_number = phone_number
        # The message content.
        self.prefilled_message = prefilled_message
        # The URL of the QR code.
        self.qr_image_url = qr_image_url
        # The mode of the quick-response (QR) code.
        self.qrdl_code = qrdl_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.deep_link_url is not None:
            result['DeepLinkUrl'] = self.deep_link_url

        if self.generate_qr_image is not None:
            result['GenerateQrImage'] = self.generate_qr_image

        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number

        if self.prefilled_message is not None:
            result['PrefilledMessage'] = self.prefilled_message

        if self.qr_image_url is not None:
            result['QrImageUrl'] = self.qr_image_url

        if self.qrdl_code is not None:
            result['QrdlCode'] = self.qrdl_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeepLinkUrl') is not None:
            self.deep_link_url = m.get('DeepLinkUrl')

        if m.get('GenerateQrImage') is not None:
            self.generate_qr_image = m.get('GenerateQrImage')

        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')

        if m.get('PrefilledMessage') is not None:
            self.prefilled_message = m.get('PrefilledMessage')

        if m.get('QrImageUrl') is not None:
            self.qr_image_url = m.get('QrImageUrl')

        if m.get('QrdlCode') is not None:
            self.qrdl_code = m.get('QrdlCode')

        return self

