# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class GetVpnGatewayDiagnoseResultResponseBody(DaraModel):
    def __init__(
        self,
        begin_time: str = None,
        diagnose_id: str = None,
        diagnose_result: List[main_models.GetVpnGatewayDiagnoseResultResponseBodyDiagnoseResult] = None,
        finish_time: str = None,
        finished_count: int = None,
        request_id: str = None,
        resource_instance_id: str = None,
        resource_type: str = None,
        total_count: int = None,
        vpn_gateway_id: str = None,
    ):
        # The time when the diagnostic started.
        # 
        # The time follows the ISO8601 standard in the `yyyy-MM-ddTHH:mm:ssZ` format. The time is displayed in UTC.
        self.begin_time = begin_time
        # The ID of the diagnostic.
        self.diagnose_id = diagnose_id
        # The information about the diagnostic items.
        self.diagnose_result = diagnose_result
        # The timestamp when the system finishes diagnosing the item.
        # 
        # The time follows the ISO8601 standard in the `yyyy-MM-ddTHH:mm:ssZ` format. The time is displayed in UTC.
        self.finish_time = finish_time
        # The number of diagnostic items that have been diagnosed.
        self.finished_count = finished_count
        # The request ID.
        self.request_id = request_id
        # The ID of the resource that is diagnosed.
        self.resource_instance_id = resource_instance_id
        # The type of the resource.
        # 
        # The value is set to **IPsec**, which indicates an IPsec-VPN connection.
        self.resource_type = resource_type
        # The total number of diagnostic items.
        self.total_count = total_count
        # The ID of the VPN gateway.
        self.vpn_gateway_id = vpn_gateway_id

    def validate(self):
        if self.diagnose_result:
            for v1 in self.diagnose_result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time

        if self.diagnose_id is not None:
            result['DiagnoseId'] = self.diagnose_id

        result['DiagnoseResult'] = []
        if self.diagnose_result is not None:
            for k1 in self.diagnose_result:
                result['DiagnoseResult'].append(k1.to_map() if k1 else None)

        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time

        if self.finished_count is not None:
            result['FinishedCount'] = self.finished_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_instance_id is not None:
            result['ResourceInstanceId'] = self.resource_instance_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.vpn_gateway_id is not None:
            result['VpnGatewayId'] = self.vpn_gateway_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')

        if m.get('DiagnoseId') is not None:
            self.diagnose_id = m.get('DiagnoseId')

        self.diagnose_result = []
        if m.get('DiagnoseResult') is not None:
            for k1 in m.get('DiagnoseResult'):
                temp_model = main_models.GetVpnGatewayDiagnoseResultResponseBodyDiagnoseResult()
                self.diagnose_result.append(temp_model.from_map(k1))

        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')

        if m.get('FinishedCount') is not None:
            self.finished_count = m.get('FinishedCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceInstanceId') is not None:
            self.resource_instance_id = m.get('ResourceInstanceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('VpnGatewayId') is not None:
            self.vpn_gateway_id = m.get('VpnGatewayId')

        return self

class GetVpnGatewayDiagnoseResultResponseBodyDiagnoseResult(DaraModel):
    def __init__(
        self,
        diagnose_name: str = None,
        diagnose_result_description: str = None,
        diagnose_result_level: str = None,
    ):
        # The diagnostic item.
        # 
        # *   **RouteEntryConflict**: route conflicts.
        # *   **VpnRouteQuota**: the quota of destination-based routes for the VPN gateway.
        # *   **VpnIPsecQuota**: the quota of IPsec-VPN connections for the VPN gateway.
        # *   **VpnPbrRouteQuota**: the quota of policy-based routes for the VPN gateway.
        # *   **VcoConfigConsistency**: the consistency of the IPsec-VPN connection.
        # *   **VcoUserInternetIpConnectivity**: Internet connectivity of the customer gateway.
        # *   **VcoPrivateConnectivity**: private network connectivity.
        # 
        # For more information about the diagnostic items, see [Background information about quick diagnostics](https://help.aliyun.com/document_detail/190330.html).
        self.diagnose_name = diagnose_name
        # The diagnostic result.
        # 
        # The system returns different results for each diagnostic item.
        # 
        # *   **RouteEntryConflict**: information about route conflicts.
        # 
        # *   **VpnRouteQuota**:
        # 
        #     *   **quotaName**: the quota ID of destination-based routes.
        #     *   **quantity**: the quota of destination-based routes for the VPN gateway.
        #     *   **used**: the number of destination-based routes created for the VPN gateway.
        # 
        # *   **VpnIPsecQuota**:
        # 
        #     *   **quotaName**: the quota ID of IPsec-VPN connections.
        #     *   **quantity**: the quota of IPsec-VPN connections for the VPN gateway.
        #     *   **used**: the number of IPsec-VPN connections created for the VPN gateway.
        # 
        # *   **VpnPbrRouteQuota**:
        # 
        #     *   **quotaName**: the quota ID of policy-based routes.
        #     *   **quantity**: the quota of policy-based routes for the VPN gateway.
        #     *   **used**: the number of policy-based routes created for the VPN gateway.
        # 
        # *   **VcoConfigConsistency**:
        # 
        #     *   **vcoLackConf**: The system cannot obtain the configuration of the peer of the IPsec-VPN connection.
        #     *   **vcoRunningConf**: the configurations that have been added to the peer of the IPsec-VPN connection.
        #     *   **vcoDiffConf**: the configurations that are inconsistent between the local end and the peer.
        #     *   **vcoConf**: the configurations that have been added to the local end.
        # 
        # *   **VcoUserInternetIpConnectivity**:
        # 
        #     *   **targetIp**: the public IP address of the customer gateway.
        #     *   **rtt**: the latency when the system accesses the public IP address of the customer gateway. Unit: milliseconds.
        #     *   **lossRate**: the packet loss when the system accesses the public IP address of the customer gateway.
        # 
        # *   **VcoPrivateConnectivity**:
        # 
        #     *   **targetIp**: the source IP address.
        #     *   **srcIp**: the destination IP address.
        #     *   **rtt**: the latency when the source IP address accesses the destination IP address. Unit: milliseconds.
        #     *   **lossRate**: the packet loss when the source IP address accesses the destination IP address.
        self.diagnose_result_description = diagnose_result_description
        # The diagnostic result level.
        # 
        # *   **normal**
        # *   **warning**
        # *   **error**
        # 
        # For more information, see [Background information about quick diagnostics](https://help.aliyun.com/document_detail/190330.html).
        self.diagnose_result_level = diagnose_result_level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.diagnose_name is not None:
            result['DiagnoseName'] = self.diagnose_name

        if self.diagnose_result_description is not None:
            result['DiagnoseResultDescription'] = self.diagnose_result_description

        if self.diagnose_result_level is not None:
            result['DiagnoseResultLevel'] = self.diagnose_result_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiagnoseName') is not None:
            self.diagnose_name = m.get('DiagnoseName')

        if m.get('DiagnoseResultDescription') is not None:
            self.diagnose_result_description = m.get('DiagnoseResultDescription')

        if m.get('DiagnoseResultLevel') is not None:
            self.diagnose_result_level = m.get('DiagnoseResultLevel')

        return self

