# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class UpdateHoneypotResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.UpdateHoneypotResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code returned. The status code **200** indicates that the request was successful. Other status codes indicate that the request failed. You can identify the cause of the failure based on the status code.
        self.code = code
        # The information about the honeypot.
        self.data = data
        # The HTTP status code returned.
        self.http_status_code = http_status_code
        # The message returned.
        self.message = message
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: The request was successful.
        # *   **false**: The request failed.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.UpdateHoneypotResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class UpdateHoneypotResponseBodyData(DaraModel):
    def __init__(
        self,
        honeypot_id: str = None,
        honeypot_image_display_name: str = None,
        honeypot_image_name: str = None,
        honeypot_name: str = None,
        node_id: str = None,
        preset_id: str = None,
        state: List[str] = None,
    ):
        # The ID of the honeypot.
        self.honeypot_id = honeypot_id
        # The display name of the honeypot image.
        self.honeypot_image_display_name = honeypot_image_display_name
        # The name of the honeypot image.
        self.honeypot_image_name = honeypot_image_name
        # The custom name of the honeypot.
        self.honeypot_name = honeypot_name
        # The ID of the management node.
        self.node_id = node_id
        # The ID of the custom configuration for the honeypot.
        self.preset_id = preset_id
        # An array that consists of the status information about the honeypot.
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.honeypot_id is not None:
            result['HoneypotId'] = self.honeypot_id

        if self.honeypot_image_display_name is not None:
            result['HoneypotImageDisplayName'] = self.honeypot_image_display_name

        if self.honeypot_image_name is not None:
            result['HoneypotImageName'] = self.honeypot_image_name

        if self.honeypot_name is not None:
            result['HoneypotName'] = self.honeypot_name

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.preset_id is not None:
            result['PresetId'] = self.preset_id

        if self.state is not None:
            result['State'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HoneypotId') is not None:
            self.honeypot_id = m.get('HoneypotId')

        if m.get('HoneypotImageDisplayName') is not None:
            self.honeypot_image_display_name = m.get('HoneypotImageDisplayName')

        if m.get('HoneypotImageName') is not None:
            self.honeypot_image_name = m.get('HoneypotImageName')

        if m.get('HoneypotName') is not None:
            self.honeypot_name = m.get('HoneypotName')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('PresetId') is not None:
            self.preset_id = m.get('PresetId')

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

