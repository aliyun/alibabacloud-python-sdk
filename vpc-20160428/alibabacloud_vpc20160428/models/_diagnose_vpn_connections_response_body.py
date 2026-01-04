# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class DiagnoseVpnConnectionsResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        vpn_connections: List[main_models.DiagnoseVpnConnectionsResponseBodyVpnConnections] = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The number of entries returned.
        self.total_count = total_count
        # The diagnostic information.
        self.vpn_connections = vpn_connections

    def validate(self):
        if self.vpn_connections:
            for v1 in self.vpn_connections:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        result['VpnConnections'] = []
        if self.vpn_connections is not None:
            for k1 in self.vpn_connections:
                result['VpnConnections'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.vpn_connections = []
        if m.get('VpnConnections') is not None:
            for k1 in m.get('VpnConnections'):
                temp_model = main_models.DiagnoseVpnConnectionsResponseBodyVpnConnections()
                self.vpn_connections.append(temp_model.from_map(k1))

        return self

class DiagnoseVpnConnectionsResponseBodyVpnConnections(DaraModel):
    def __init__(
        self,
        failed_reason: str = None,
        failed_reason_code: str = None,
        failed_time: int = None,
        mismatch_local_param: str = None,
        mismatch_remote_param: str = None,
        severity: str = None,
        source_log: str = None,
        tunnel_id: str = None,
        vpn_connection_id: str = None,
    ):
        # The cause of the error.
        self.failed_reason = failed_reason
        # The error code.
        self.failed_reason_code = failed_reason_code
        # The timestamp when the current error occurred on the IPsec-VPN connection. Unit: millisecond.
        # 
        # This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.failed_time = failed_time
        # If the values of the parameters configured for the IPsec-VPN connection and the peer gateway device do not match, this parameter indicates the value of the parameters configured for the IPsec-VPN connection.
        self.mismatch_local_param = mismatch_local_param
        # If the parameter values configured for the IPsec-VPN connection and the peer gateway device do not match, this parameter indicates the value of the parameter configured for the peer gateway device.
        self.mismatch_remote_param = mismatch_remote_param
        # The error level. Valid values:
        # 
        # *   **Critical**
        # *   **Warn**
        # *   **Normal**
        self.severity = severity
        # The log information about the error.
        self.source_log = source_log
        # The tunnel ID.
        self.tunnel_id = tunnel_id
        # The ID of the IPsec-VPN connection.
        self.vpn_connection_id = vpn_connection_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failed_reason is not None:
            result['FailedReason'] = self.failed_reason

        if self.failed_reason_code is not None:
            result['FailedReasonCode'] = self.failed_reason_code

        if self.failed_time is not None:
            result['FailedTime'] = self.failed_time

        if self.mismatch_local_param is not None:
            result['MismatchLocalParam'] = self.mismatch_local_param

        if self.mismatch_remote_param is not None:
            result['MismatchRemoteParam'] = self.mismatch_remote_param

        if self.severity is not None:
            result['Severity'] = self.severity

        if self.source_log is not None:
            result['SourceLog'] = self.source_log

        if self.tunnel_id is not None:
            result['TunnelId'] = self.tunnel_id

        if self.vpn_connection_id is not None:
            result['VpnConnectionId'] = self.vpn_connection_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailedReason') is not None:
            self.failed_reason = m.get('FailedReason')

        if m.get('FailedReasonCode') is not None:
            self.failed_reason_code = m.get('FailedReasonCode')

        if m.get('FailedTime') is not None:
            self.failed_time = m.get('FailedTime')

        if m.get('MismatchLocalParam') is not None:
            self.mismatch_local_param = m.get('MismatchLocalParam')

        if m.get('MismatchRemoteParam') is not None:
            self.mismatch_remote_param = m.get('MismatchRemoteParam')

        if m.get('Severity') is not None:
            self.severity = m.get('Severity')

        if m.get('SourceLog') is not None:
            self.source_log = m.get('SourceLog')

        if m.get('TunnelId') is not None:
            self.tunnel_id = m.get('TunnelId')

        if m.get('VpnConnectionId') is not None:
            self.vpn_connection_id = m.get('VpnConnectionId')

        return self

