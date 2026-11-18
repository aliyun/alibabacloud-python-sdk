# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class SendRuntimeQrCodeConfigChannelMessageResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.SendRuntimeQrCodeConfigChannelMessageResponseBodyData] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of sending results for each runtime. Each runtime corresponds to one result. The return order is not guaranteed to be the same as the order of RuntimeIds in the request. Match the results by RuntimeId.
        self.data = data
        # The request ID, which is a unique identifier for the request.
        self.request_id = request_id
        # The total number of returned sending results, which is the same as the number of results in Data.
        self.total_count = total_count

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.SendRuntimeQrCodeConfigChannelMessageResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class SendRuntimeQrCodeConfigChannelMessageResponseBodyData(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        qr_code_notify_url: str = None,
        runtime_id: str = None,
        success: bool = None,
    ):
        # The error code when the sending fails, such as Runtime.NotFound (the runtime does not exist) or Runtime.UserNotSupported (the runtime has no authorized user or has multiple authorized users). This parameter is not returned when the sending is successful.
        self.code = code
        # The error message when the sending fails. This parameter is not returned when the sending is successful.
        self.message = message
        # The access URL of the QR code configuration channel page. It carries the taskId, channel code, and region parameters for the current process, and has been sent to the authorized user of the runtime by email and SMS. This parameter is returned only when the sending is successful. The taskId is valid for 1 hour.
        self.qr_code_notify_url = qr_code_notify_url
        # The ID of the runtime resource.
        self.runtime_id = runtime_id
        # Indicates whether the QR code configuration channel message for the runtime was initiated successfully. If the value is false, you can check the Code and Message fields for the cause of the failure.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.qr_code_notify_url is not None:
            result['QrCodeNotifyUrl'] = self.qr_code_notify_url

        if self.runtime_id is not None:
            result['RuntimeId'] = self.runtime_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('QrCodeNotifyUrl') is not None:
            self.qr_code_notify_url = m.get('QrCodeNotifyUrl')

        if m.get('RuntimeId') is not None:
            self.runtime_id = m.get('RuntimeId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

