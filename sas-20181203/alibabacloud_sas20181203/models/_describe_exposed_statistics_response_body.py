# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeExposedStatisticsResponseBody(DaraModel):
    def __init__(
        self,
        exposed_asap_vul_count: int = None,
        exposed_component_count: int = None,
        exposed_dds_count: int = None,
        exposed_ecs_count: int = None,
        exposed_instance_count: int = None,
        exposed_ip_count: int = None,
        exposed_kvstore_count: int = None,
        exposed_later_vul_count: int = None,
        exposed_nntf_vul_count: int = None,
        exposed_port_count: int = None,
        exposed_rds_count: int = None,
        exposed_week_password_machine_count: int = None,
        gateway_asset_count: int = None,
        request_id: str = None,
    ):
        # The total number of high-risk vulnerabilities that are exposed on the Internet and can be exploited by attackers.
        self.exposed_asap_vul_count = exposed_asap_vul_count
        # The total number of system components that are exposed on the Internet. The components include OpenSSL and OpenSSH.
        self.exposed_component_count = exposed_component_count
        # The number of ApsaraDB for MongoDB instances that are exposed on the Internet.
        self.exposed_dds_count = exposed_dds_count
        # The number of Elastic Compute Service (ECS) instances that are exposed on the Internet.
        self.exposed_ecs_count = exposed_ecs_count
        # The total number of assets that are exposed on the Internet.
        self.exposed_instance_count = exposed_instance_count
        # The total number of IP addresses that are exposed on the Internet.
        self.exposed_ip_count = exposed_ip_count
        # The number of ApsaraDB for Redis instances that are exposed on the Internet.
        self.exposed_kvstore_count = exposed_kvstore_count
        # The total number of medium-risk vulnerabilities that are exposed on the Internet and can be exploited by attackers.
        self.exposed_later_vul_count = exposed_later_vul_count
        # The total number of low-risk vulnerabilities that are exposed on the Internet and can be exploited by attackers.
        self.exposed_nntf_vul_count = exposed_nntf_vul_count
        # The total number of ports that are exposed on the Internet.
        self.exposed_port_count = exposed_port_count
        # The number of ApsaraDB RDS instances that are exposed on the Internet.
        self.exposed_rds_count = exposed_rds_count
        # The total number of system keys that are detected on your servers and are exposed on the Internet.
        self.exposed_week_password_machine_count = exposed_week_password_machine_count
        # The total number of gateway assets that are exposed on the Internet. The gateway assets include NAT gateways and Server Load Balancer (SLB) instances.
        self.gateway_asset_count = gateway_asset_count
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.exposed_asap_vul_count is not None:
            result['ExposedAsapVulCount'] = self.exposed_asap_vul_count

        if self.exposed_component_count is not None:
            result['ExposedComponentCount'] = self.exposed_component_count

        if self.exposed_dds_count is not None:
            result['ExposedDdsCount'] = self.exposed_dds_count

        if self.exposed_ecs_count is not None:
            result['ExposedEcsCount'] = self.exposed_ecs_count

        if self.exposed_instance_count is not None:
            result['ExposedInstanceCount'] = self.exposed_instance_count

        if self.exposed_ip_count is not None:
            result['ExposedIpCount'] = self.exposed_ip_count

        if self.exposed_kvstore_count is not None:
            result['ExposedKvstoreCount'] = self.exposed_kvstore_count

        if self.exposed_later_vul_count is not None:
            result['ExposedLaterVulCount'] = self.exposed_later_vul_count

        if self.exposed_nntf_vul_count is not None:
            result['ExposedNntfVulCount'] = self.exposed_nntf_vul_count

        if self.exposed_port_count is not None:
            result['ExposedPortCount'] = self.exposed_port_count

        if self.exposed_rds_count is not None:
            result['ExposedRdsCount'] = self.exposed_rds_count

        if self.exposed_week_password_machine_count is not None:
            result['ExposedWeekPasswordMachineCount'] = self.exposed_week_password_machine_count

        if self.gateway_asset_count is not None:
            result['GatewayAssetCount'] = self.gateway_asset_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExposedAsapVulCount') is not None:
            self.exposed_asap_vul_count = m.get('ExposedAsapVulCount')

        if m.get('ExposedComponentCount') is not None:
            self.exposed_component_count = m.get('ExposedComponentCount')

        if m.get('ExposedDdsCount') is not None:
            self.exposed_dds_count = m.get('ExposedDdsCount')

        if m.get('ExposedEcsCount') is not None:
            self.exposed_ecs_count = m.get('ExposedEcsCount')

        if m.get('ExposedInstanceCount') is not None:
            self.exposed_instance_count = m.get('ExposedInstanceCount')

        if m.get('ExposedIpCount') is not None:
            self.exposed_ip_count = m.get('ExposedIpCount')

        if m.get('ExposedKvstoreCount') is not None:
            self.exposed_kvstore_count = m.get('ExposedKvstoreCount')

        if m.get('ExposedLaterVulCount') is not None:
            self.exposed_later_vul_count = m.get('ExposedLaterVulCount')

        if m.get('ExposedNntfVulCount') is not None:
            self.exposed_nntf_vul_count = m.get('ExposedNntfVulCount')

        if m.get('ExposedPortCount') is not None:
            self.exposed_port_count = m.get('ExposedPortCount')

        if m.get('ExposedRdsCount') is not None:
            self.exposed_rds_count = m.get('ExposedRdsCount')

        if m.get('ExposedWeekPasswordMachineCount') is not None:
            self.exposed_week_password_machine_count = m.get('ExposedWeekPasswordMachineCount')

        if m.get('GatewayAssetCount') is not None:
            self.gateway_asset_count = m.get('GatewayAssetCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

