# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class ListPrivateAccessApplicationL7SwitchesResponseBody(DaraModel):
    def __init__(
        self,
        l_7switches: List[main_models.ListPrivateAccessApplicationL7SwitchesResponseBodyL7Switches] = None,
        request_id: str = None,
    ):
        # The Layer 7 application configurations.
        self.l_7switches = l_7switches
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.l_7switches:
            for v1 in self.l_7switches:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['L7Switches'] = []
        if self.l_7switches is not None:
            for k1 in self.l_7switches:
                result['L7Switches'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.l_7switches = []
        if m.get('L7Switches') is not None:
            for k1 in m.get('L7Switches'):
                temp_model = main_models.ListPrivateAccessApplicationL7SwitchesResponseBodyL7Switches()
                self.l_7switches.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListPrivateAccessApplicationL7SwitchesResponseBodyL7Switches(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        dev_tag_mark_status: str = None,
        download_audit_status: str = None,
        port_ranges: List[main_models.ListPrivateAccessApplicationL7SwitchesResponseBodyL7SwitchesPortRanges] = None,
        src_ip_mark_status: str = None,
        status: str = None,
        timeout_sec: int = None,
        user_mark_status: str = None,
        zero_trust_status: str = None,
    ):
        # The ID of the internal-facing application.
        self.application_id = application_id
        # The device tag mark switch. Valid values:
        # - **Enabled**: Enabled.
        # - **Disabled**: Disabled.
        self.dev_tag_mark_status = dev_tag_mark_status
        # The download audit switch for sensitive applications. Valid values:
        # - **Enabled**: Enabled.
        # - **Disabled**: Disabled.
        self.download_audit_status = download_audit_status
        # The port ranges.
        self.port_ranges = port_ranges
        # The source IP mark switch. Valid values:
        # - **Enabled**: Enabled.
        # - **Disabled**: Disabled.
        self.src_ip_mark_status = src_ip_mark_status
        # The status of the internal-facing access policy. Valid values:
        # - **Enabled**: Enabled.
        # - **Disabled**: Disabled.
        self.status = status
        # The request timeout period.
        self.timeout_sec = timeout_sec
        # The user mark switch. Valid values:
        # - **Enabled**: Enabled.
        # - **Disabled**: Disabled.
        self.user_mark_status = user_mark_status
        # The host bypass prevention switch. Valid values:
        # - **Enabled**: Enabled.
        # - **Disabled**: Disabled.
        self.zero_trust_status = zero_trust_status

    def validate(self):
        if self.port_ranges:
            for v1 in self.port_ranges:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.dev_tag_mark_status is not None:
            result['DevTagMarkStatus'] = self.dev_tag_mark_status

        if self.download_audit_status is not None:
            result['DownloadAuditStatus'] = self.download_audit_status

        result['PortRanges'] = []
        if self.port_ranges is not None:
            for k1 in self.port_ranges:
                result['PortRanges'].append(k1.to_map() if k1 else None)

        if self.src_ip_mark_status is not None:
            result['SrcIpMarkStatus'] = self.src_ip_mark_status

        if self.status is not None:
            result['Status'] = self.status

        if self.timeout_sec is not None:
            result['TimeoutSec'] = self.timeout_sec

        if self.user_mark_status is not None:
            result['UserMarkStatus'] = self.user_mark_status

        if self.zero_trust_status is not None:
            result['ZeroTrustStatus'] = self.zero_trust_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('DevTagMarkStatus') is not None:
            self.dev_tag_mark_status = m.get('DevTagMarkStatus')

        if m.get('DownloadAuditStatus') is not None:
            self.download_audit_status = m.get('DownloadAuditStatus')

        self.port_ranges = []
        if m.get('PortRanges') is not None:
            for k1 in m.get('PortRanges'):
                temp_model = main_models.ListPrivateAccessApplicationL7SwitchesResponseBodyL7SwitchesPortRanges()
                self.port_ranges.append(temp_model.from_map(k1))

        if m.get('SrcIpMarkStatus') is not None:
            self.src_ip_mark_status = m.get('SrcIpMarkStatus')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TimeoutSec') is not None:
            self.timeout_sec = m.get('TimeoutSec')

        if m.get('UserMarkStatus') is not None:
            self.user_mark_status = m.get('UserMarkStatus')

        if m.get('ZeroTrustStatus') is not None:
            self.zero_trust_status = m.get('ZeroTrustStatus')

        return self

class ListPrivateAccessApplicationL7SwitchesResponseBodyL7SwitchesPortRanges(DaraModel):
    def __init__(
        self,
        begin: int = None,
        end: int = None,
    ):
        # The start port.
        self.begin = begin
        # The end port. The value must be greater than or equal to the start port.
        self.end = end

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin is not None:
            result['Begin'] = self.begin

        if self.end is not None:
            result['End'] = self.end

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Begin') is not None:
            self.begin = m.get('Begin')

        if m.get('End') is not None:
            self.end = m.get('End')

        return self

