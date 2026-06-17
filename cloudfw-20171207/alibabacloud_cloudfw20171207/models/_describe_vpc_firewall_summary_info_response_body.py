# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeVpcFirewallSummaryInfoResponseBody(DaraModel):
    def __init__(
        self,
        available_vpc_firewall_quota: int = None,
        cen_express_connect_vpc_count: int = None,
        cen_firewall_vpc_count: int = None,
        cen_tr_vpc_count: int = None,
        closed_cen_firewall_count: int = None,
        closed_express_connect_firewall_count: int = None,
        closed_vpc_firewall_count: int = None,
        configured_cen_firewall_count: int = None,
        configured_cen_firewall_region_count: int = None,
        configured_cen_firewall_vpc_count: int = None,
        configured_cen_tr_firewall_count: int = None,
        configured_express_connect_firewall_count: int = None,
        configured_express_connect_vpc_count: int = None,
        configured_vpc_firewall_count: int = None,
        configured_vpc_firewall_vpc_count: int = None,
        express_connect_vpc_count: int = None,
        not_configured_cen_firewall_count: int = None,
        not_configured_cen_tr_firewall_count: int = None,
        not_configured_express_connect_firewall_count: int = None,
        not_configured_vpc_firewall_count: int = None,
        opened_cen_express_connect_vpc_count: int = None,
        opened_cen_firewall_count: int = None,
        opened_cen_firewall_vpc_count: int = None,
        opened_cen_tr_firewall_vpc_count: int = None,
        opened_ecr_count: int = None,
        opened_express_connect_firewall_count: int = None,
        opened_express_connect_vpc_count: int = None,
        opened_peer_tr_count: int = None,
        opened_vbr_count: int = None,
        opened_vpc_count: int = None,
        opened_vpc_firewall_count: int = None,
        opened_vpn_count: int = None,
        request_id: str = None,
        total_ecr_count: int = None,
        total_peer_tr_count: int = None,
        total_vbr_count: int = None,
        total_vpc_count: int = None,
        total_vpc_firewall_quota: int = None,
        total_vpn_count: int = None,
    ):
        # The remaining quota for VPC firewalls.
        self.available_vpc_firewall_quota = available_vpc_firewall_quota
        # The number of VPCs connected using Cloud Enterprise Network (CEN) and Express Connect.
        self.cen_express_connect_vpc_count = cen_express_connect_vpc_count
        # The number of CEN VPCs.
        self.cen_firewall_vpc_count = cen_firewall_vpc_count
        # The number of VPCs on the CEN transit router.
        self.cen_tr_vpc_count = cen_tr_vpc_count
        # The number of configured CEN firewalls that are disabled.
        self.closed_cen_firewall_count = closed_cen_firewall_count
        # The number of configured Express Connect firewalls that are disabled.
        self.closed_express_connect_firewall_count = closed_express_connect_firewall_count
        # The number of configured VPC firewalls that are disabled.
        self.closed_vpc_firewall_count = closed_vpc_firewall_count
        # The number of configured CEN firewall instances of the Basic Edition.
        self.configured_cen_firewall_count = configured_cen_firewall_count
        # The number of regions where CEN firewalls are configured.
        self.configured_cen_firewall_region_count = configured_cen_firewall_region_count
        # The number of VPCs for which CEN firewalls are configured.
        self.configured_cen_firewall_vpc_count = configured_cen_firewall_vpc_count
        # The number of configured CEN transit router firewall instances.
        self.configured_cen_tr_firewall_count = configured_cen_tr_firewall_count
        # The number of configured Express Connect circuits.
        self.configured_express_connect_firewall_count = configured_express_connect_firewall_count
        # The number of VPCs for which Express Connect firewalls are configured.
        self.configured_express_connect_vpc_count = configured_express_connect_vpc_count
        # The number of configured VPC firewalls.
        self.configured_vpc_firewall_count = configured_vpc_firewall_count
        # The number of VPCs for which VPC firewalls are configured.
        self.configured_vpc_firewall_vpc_count = configured_vpc_firewall_vpc_count
        # The number of Express Connect VPCs.
        self.express_connect_vpc_count = express_connect_vpc_count
        # The number of CEN firewalls that are not configured.
        self.not_configured_cen_firewall_count = not_configured_cen_firewall_count
        # The number of CEN transit router firewall instances that are not configured.
        self.not_configured_cen_tr_firewall_count = not_configured_cen_tr_firewall_count
        # The number of Express Connect firewalls that are not configured.
        self.not_configured_express_connect_firewall_count = not_configured_express_connect_firewall_count
        # The number of VPC firewalls that are not configured.
        self.not_configured_vpc_firewall_count = not_configured_vpc_firewall_count
        # The number of VPCs that are connected using CEN and Express Connect and have the firewall enabled.
        self.opened_cen_express_connect_vpc_count = opened_cen_express_connect_vpc_count
        # The number of enabled CEN firewalls.
        self.opened_cen_firewall_count = opened_cen_firewall_count
        # The number of VPCs protected by CEN firewalls.
        self.opened_cen_firewall_vpc_count = opened_cen_firewall_vpc_count
        # The number of VPCs protected by the CEN transit router firewall.
        self.opened_cen_tr_firewall_vpc_count = opened_cen_tr_firewall_vpc_count
        # The number of enabled CEN Express Connect Routers (ECRs).
        self.opened_ecr_count = opened_ecr_count
        # The number of enabled Express Connect firewalls.
        self.opened_express_connect_firewall_count = opened_express_connect_firewall_count
        # The number of VPCs protected by Express Connect firewalls.
        self.opened_express_connect_vpc_count = opened_express_connect_vpc_count
        # The number of inter-region connections protected by the CEN transit router firewall.
        self.opened_peer_tr_count = opened_peer_tr_count
        # The number of Virtual Border Routers (VBRs) protected by the CEN transit router firewall.
        self.opened_vbr_count = opened_vbr_count
        # The number of protected VPCs.
        self.opened_vpc_count = opened_vpc_count
        # The number of enabled VPC firewalls.
        self.opened_vpc_firewall_count = opened_vpc_firewall_count
        # The number of VPN gateways protected by the CEN transit router firewall.
        self.opened_vpn_count = opened_vpn_count
        # The ID of the request.
        self.request_id = request_id
        # The number of ECRs.
        self.total_ecr_count = total_ecr_count
        # The number of inter-region connections on the CEN transit router.
        self.total_peer_tr_count = total_peer_tr_count
        # The number of VBRs on the CEN transit router.
        self.total_vbr_count = total_vbr_count
        # The number of interconnected VPCs.
        self.total_vpc_count = total_vpc_count
        # The total quota for VPC firewalls.
        self.total_vpc_firewall_quota = total_vpc_firewall_quota
        # The number of VPN gateways on the CEN transit router.
        self.total_vpn_count = total_vpn_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.available_vpc_firewall_quota is not None:
            result['AvailableVpcFirewallQuota'] = self.available_vpc_firewall_quota

        if self.cen_express_connect_vpc_count is not None:
            result['CenExpressConnectVpcCount'] = self.cen_express_connect_vpc_count

        if self.cen_firewall_vpc_count is not None:
            result['CenFirewallVpcCount'] = self.cen_firewall_vpc_count

        if self.cen_tr_vpc_count is not None:
            result['CenTrVpcCount'] = self.cen_tr_vpc_count

        if self.closed_cen_firewall_count is not None:
            result['ClosedCenFirewallCount'] = self.closed_cen_firewall_count

        if self.closed_express_connect_firewall_count is not None:
            result['ClosedExpressConnectFirewallCount'] = self.closed_express_connect_firewall_count

        if self.closed_vpc_firewall_count is not None:
            result['ClosedVpcFirewallCount'] = self.closed_vpc_firewall_count

        if self.configured_cen_firewall_count is not None:
            result['ConfiguredCenFirewallCount'] = self.configured_cen_firewall_count

        if self.configured_cen_firewall_region_count is not None:
            result['ConfiguredCenFirewallRegionCount'] = self.configured_cen_firewall_region_count

        if self.configured_cen_firewall_vpc_count is not None:
            result['ConfiguredCenFirewallVpcCount'] = self.configured_cen_firewall_vpc_count

        if self.configured_cen_tr_firewall_count is not None:
            result['ConfiguredCenTrFirewallCount'] = self.configured_cen_tr_firewall_count

        if self.configured_express_connect_firewall_count is not None:
            result['ConfiguredExpressConnectFirewallCount'] = self.configured_express_connect_firewall_count

        if self.configured_express_connect_vpc_count is not None:
            result['ConfiguredExpressConnectVpcCount'] = self.configured_express_connect_vpc_count

        if self.configured_vpc_firewall_count is not None:
            result['ConfiguredVpcFirewallCount'] = self.configured_vpc_firewall_count

        if self.configured_vpc_firewall_vpc_count is not None:
            result['ConfiguredVpcFirewallVpcCount'] = self.configured_vpc_firewall_vpc_count

        if self.express_connect_vpc_count is not None:
            result['ExpressConnectVpcCount'] = self.express_connect_vpc_count

        if self.not_configured_cen_firewall_count is not None:
            result['NotConfiguredCenFirewallCount'] = self.not_configured_cen_firewall_count

        if self.not_configured_cen_tr_firewall_count is not None:
            result['NotConfiguredCenTrFirewallCount'] = self.not_configured_cen_tr_firewall_count

        if self.not_configured_express_connect_firewall_count is not None:
            result['NotConfiguredExpressConnectFirewallCount'] = self.not_configured_express_connect_firewall_count

        if self.not_configured_vpc_firewall_count is not None:
            result['NotConfiguredVpcFirewallCount'] = self.not_configured_vpc_firewall_count

        if self.opened_cen_express_connect_vpc_count is not None:
            result['OpenedCenExpressConnectVpcCount'] = self.opened_cen_express_connect_vpc_count

        if self.opened_cen_firewall_count is not None:
            result['OpenedCenFirewallCount'] = self.opened_cen_firewall_count

        if self.opened_cen_firewall_vpc_count is not None:
            result['OpenedCenFirewallVpcCount'] = self.opened_cen_firewall_vpc_count

        if self.opened_cen_tr_firewall_vpc_count is not None:
            result['OpenedCenTrFirewallVpcCount'] = self.opened_cen_tr_firewall_vpc_count

        if self.opened_ecr_count is not None:
            result['OpenedEcrCount'] = self.opened_ecr_count

        if self.opened_express_connect_firewall_count is not None:
            result['OpenedExpressConnectFirewallCount'] = self.opened_express_connect_firewall_count

        if self.opened_express_connect_vpc_count is not None:
            result['OpenedExpressConnectVpcCount'] = self.opened_express_connect_vpc_count

        if self.opened_peer_tr_count is not None:
            result['OpenedPeerTrCount'] = self.opened_peer_tr_count

        if self.opened_vbr_count is not None:
            result['OpenedVbrCount'] = self.opened_vbr_count

        if self.opened_vpc_count is not None:
            result['OpenedVpcCount'] = self.opened_vpc_count

        if self.opened_vpc_firewall_count is not None:
            result['OpenedVpcFirewallCount'] = self.opened_vpc_firewall_count

        if self.opened_vpn_count is not None:
            result['OpenedVpnCount'] = self.opened_vpn_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_ecr_count is not None:
            result['TotalEcrCount'] = self.total_ecr_count

        if self.total_peer_tr_count is not None:
            result['TotalPeerTrCount'] = self.total_peer_tr_count

        if self.total_vbr_count is not None:
            result['TotalVbrCount'] = self.total_vbr_count

        if self.total_vpc_count is not None:
            result['TotalVpcCount'] = self.total_vpc_count

        if self.total_vpc_firewall_quota is not None:
            result['TotalVpcFirewallQuota'] = self.total_vpc_firewall_quota

        if self.total_vpn_count is not None:
            result['TotalVpnCount'] = self.total_vpn_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableVpcFirewallQuota') is not None:
            self.available_vpc_firewall_quota = m.get('AvailableVpcFirewallQuota')

        if m.get('CenExpressConnectVpcCount') is not None:
            self.cen_express_connect_vpc_count = m.get('CenExpressConnectVpcCount')

        if m.get('CenFirewallVpcCount') is not None:
            self.cen_firewall_vpc_count = m.get('CenFirewallVpcCount')

        if m.get('CenTrVpcCount') is not None:
            self.cen_tr_vpc_count = m.get('CenTrVpcCount')

        if m.get('ClosedCenFirewallCount') is not None:
            self.closed_cen_firewall_count = m.get('ClosedCenFirewallCount')

        if m.get('ClosedExpressConnectFirewallCount') is not None:
            self.closed_express_connect_firewall_count = m.get('ClosedExpressConnectFirewallCount')

        if m.get('ClosedVpcFirewallCount') is not None:
            self.closed_vpc_firewall_count = m.get('ClosedVpcFirewallCount')

        if m.get('ConfiguredCenFirewallCount') is not None:
            self.configured_cen_firewall_count = m.get('ConfiguredCenFirewallCount')

        if m.get('ConfiguredCenFirewallRegionCount') is not None:
            self.configured_cen_firewall_region_count = m.get('ConfiguredCenFirewallRegionCount')

        if m.get('ConfiguredCenFirewallVpcCount') is not None:
            self.configured_cen_firewall_vpc_count = m.get('ConfiguredCenFirewallVpcCount')

        if m.get('ConfiguredCenTrFirewallCount') is not None:
            self.configured_cen_tr_firewall_count = m.get('ConfiguredCenTrFirewallCount')

        if m.get('ConfiguredExpressConnectFirewallCount') is not None:
            self.configured_express_connect_firewall_count = m.get('ConfiguredExpressConnectFirewallCount')

        if m.get('ConfiguredExpressConnectVpcCount') is not None:
            self.configured_express_connect_vpc_count = m.get('ConfiguredExpressConnectVpcCount')

        if m.get('ConfiguredVpcFirewallCount') is not None:
            self.configured_vpc_firewall_count = m.get('ConfiguredVpcFirewallCount')

        if m.get('ConfiguredVpcFirewallVpcCount') is not None:
            self.configured_vpc_firewall_vpc_count = m.get('ConfiguredVpcFirewallVpcCount')

        if m.get('ExpressConnectVpcCount') is not None:
            self.express_connect_vpc_count = m.get('ExpressConnectVpcCount')

        if m.get('NotConfiguredCenFirewallCount') is not None:
            self.not_configured_cen_firewall_count = m.get('NotConfiguredCenFirewallCount')

        if m.get('NotConfiguredCenTrFirewallCount') is not None:
            self.not_configured_cen_tr_firewall_count = m.get('NotConfiguredCenTrFirewallCount')

        if m.get('NotConfiguredExpressConnectFirewallCount') is not None:
            self.not_configured_express_connect_firewall_count = m.get('NotConfiguredExpressConnectFirewallCount')

        if m.get('NotConfiguredVpcFirewallCount') is not None:
            self.not_configured_vpc_firewall_count = m.get('NotConfiguredVpcFirewallCount')

        if m.get('OpenedCenExpressConnectVpcCount') is not None:
            self.opened_cen_express_connect_vpc_count = m.get('OpenedCenExpressConnectVpcCount')

        if m.get('OpenedCenFirewallCount') is not None:
            self.opened_cen_firewall_count = m.get('OpenedCenFirewallCount')

        if m.get('OpenedCenFirewallVpcCount') is not None:
            self.opened_cen_firewall_vpc_count = m.get('OpenedCenFirewallVpcCount')

        if m.get('OpenedCenTrFirewallVpcCount') is not None:
            self.opened_cen_tr_firewall_vpc_count = m.get('OpenedCenTrFirewallVpcCount')

        if m.get('OpenedEcrCount') is not None:
            self.opened_ecr_count = m.get('OpenedEcrCount')

        if m.get('OpenedExpressConnectFirewallCount') is not None:
            self.opened_express_connect_firewall_count = m.get('OpenedExpressConnectFirewallCount')

        if m.get('OpenedExpressConnectVpcCount') is not None:
            self.opened_express_connect_vpc_count = m.get('OpenedExpressConnectVpcCount')

        if m.get('OpenedPeerTrCount') is not None:
            self.opened_peer_tr_count = m.get('OpenedPeerTrCount')

        if m.get('OpenedVbrCount') is not None:
            self.opened_vbr_count = m.get('OpenedVbrCount')

        if m.get('OpenedVpcCount') is not None:
            self.opened_vpc_count = m.get('OpenedVpcCount')

        if m.get('OpenedVpcFirewallCount') is not None:
            self.opened_vpc_firewall_count = m.get('OpenedVpcFirewallCount')

        if m.get('OpenedVpnCount') is not None:
            self.opened_vpn_count = m.get('OpenedVpnCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalEcrCount') is not None:
            self.total_ecr_count = m.get('TotalEcrCount')

        if m.get('TotalPeerTrCount') is not None:
            self.total_peer_tr_count = m.get('TotalPeerTrCount')

        if m.get('TotalVbrCount') is not None:
            self.total_vbr_count = m.get('TotalVbrCount')

        if m.get('TotalVpcCount') is not None:
            self.total_vpc_count = m.get('TotalVpcCount')

        if m.get('TotalVpcFirewallQuota') is not None:
            self.total_vpc_firewall_quota = m.get('TotalVpcFirewallQuota')

        if m.get('TotalVpnCount') is not None:
            self.total_vpn_count = m.get('TotalVpnCount')

        return self

