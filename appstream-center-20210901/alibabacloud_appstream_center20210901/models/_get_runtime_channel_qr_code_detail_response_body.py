# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class GetRuntimeChannelQrCodeDetailResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetRuntimeChannelQrCodeDetailResponseBodyData = None,
        request_id: str = None,
    ):
        # The QR code configuration details of the channel. If no QR code configuration process exists for the channel under the specified runtime, this field is empty.
        self.data = data
        # The request ID, which uniquely identifies the request.
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
            temp_model = main_models.GetRuntimeChannelQrCodeDetailResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetRuntimeChannelQrCodeDetailResponseBodyData(DaraModel):
    def __init__(
        self,
        qr_code: str = None,
        qr_code_notify_url: str = None,
        qr_code_status: str = None,
        status: str = None,
    ):
        # The URL or content of the QR code. If the QR code is not yet generated or the content is empty, this field is empty.
        self.qr_code = qr_code
        # The access URL of the QR code configuration channel page. This URL is generated and sent to the user when the QR code configuration is initiated, and carries the taskId, channel code, and region parameters of the current process. If the URL is not recorded, this field is empty.
        self.qr_code_notify_url = qr_code_notify_url
        # The scan status. Valid values: Generating (generating), Generated (generated), GenerateFailed (generation failed), Scanned (scanned), Configuring (configuring), Success (success), Failed (failed), and Expired (expired).
        self.qr_code_status = qr_code_status
        # The status of the QR code configuration process. The valid values are the same as those of QrCodeStatus. Valid values: Generating (generating), Generated (generated), GenerateFailed (generation failed), Scanned (scanned), Configuring (configuring), Success (success), Failed (failed), and Expired (expired).
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.qr_code is not None:
            result['QrCode'] = self.qr_code

        if self.qr_code_notify_url is not None:
            result['QrCodeNotifyUrl'] = self.qr_code_notify_url

        if self.qr_code_status is not None:
            result['QrCodeStatus'] = self.qr_code_status

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QrCode') is not None:
            self.qr_code = m.get('QrCode')

        if m.get('QrCodeNotifyUrl') is not None:
            self.qr_code_notify_url = m.get('QrCodeNotifyUrl')

        if m.get('QrCodeStatus') is not None:
            self.qr_code_status = m.get('QrCodeStatus')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

