# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class CreateHoneypotProbeResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        honeypot_probe: main_models.CreateHoneypotProbeResponseBodyHoneypotProbe = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code returned. The status code **200** indicates that the request was successful. Other status codes indicate that the request failed. You can identify the cause of the failure based on the status code.
        self.code = code
        # The information about the probe.
        self.honeypot_probe = honeypot_probe
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
        if self.honeypot_probe:
            self.honeypot_probe.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.honeypot_probe is not None:
            result['HoneypotProbe'] = self.honeypot_probe.to_map()

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

        if m.get('HoneypotProbe') is not None:
            temp_model = main_models.CreateHoneypotProbeResponseBodyHoneypotProbe()
            self.honeypot_probe = temp_model.from_map(m.get('HoneypotProbe'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class CreateHoneypotProbeResponseBodyHoneypotProbe(DaraModel):
    def __init__(
        self,
        probe_id: str = None,
    ):
        # The ID of the probe.
        self.probe_id = probe_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.probe_id is not None:
            result['ProbeId'] = self.probe_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProbeId') is not None:
            self.probe_id = m.get('ProbeId')

        return self

