# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class ApprovePolarClawDevicePairResponseBody(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        code: int = None,
        device: main_models.ApprovePolarClawDevicePairResponseBodyDevice = None,
        message: str = None,
        pair_request_id: str = None,
        request_id: str = None,
    ):
        # The application ID.
        self.application_id = application_id
        # The response status code.
        self.code = code
        # The paired device information.
        self.device = device
        # The response message.
        self.message = message
        # The pairing request ID.
        self.pair_request_id = pair_request_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.device:
            self.device.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.code is not None:
            result['Code'] = self.code

        if self.device is not None:
            result['Device'] = self.device.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.pair_request_id is not None:
            result['PairRequestId'] = self.pair_request_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Device') is not None:
            temp_model = main_models.ApprovePolarClawDevicePairResponseBodyDevice()
            self.device = temp_model.from_map(m.get('Device'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PairRequestId') is not None:
            self.pair_request_id = m.get('PairRequestId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ApprovePolarClawDevicePairResponseBodyDevice(DaraModel):
    def __init__(
        self,
        created_at_ms: int = None,
        device_family: str = None,
        device_id: str = None,
        display_name: str = None,
        platform: str = None,
        role: str = None,
        scopes: List[str] = None,
    ):
        # The creation time of the device pairing, in Unix milliseconds.
        self.created_at_ms = created_at_ms
        # The device family.
        self.device_family = device_family
        # The unique ID of the device.
        self.device_id = device_id
        # The display name of the device.
        self.display_name = display_name
        # The operating system of the device.
        self.platform = platform
        # The role of the device.
        self.role = role
        # A list of permission scopes.
        self.scopes = scopes

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_at_ms is not None:
            result['CreatedAtMs'] = self.created_at_ms

        if self.device_family is not None:
            result['DeviceFamily'] = self.device_family

        if self.device_id is not None:
            result['DeviceId'] = self.device_id

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.platform is not None:
            result['Platform'] = self.platform

        if self.role is not None:
            result['Role'] = self.role

        if self.scopes is not None:
            result['Scopes'] = self.scopes

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedAtMs') is not None:
            self.created_at_ms = m.get('CreatedAtMs')

        if m.get('DeviceFamily') is not None:
            self.device_family = m.get('DeviceFamily')

        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Platform') is not None:
            self.platform = m.get('Platform')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('Scopes') is not None:
            self.scopes = m.get('Scopes')

        return self

