# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePostpayTrafficTotalResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        total_assets: int = None,
        total_bill_traffic: int = None,
        total_internet_assets: int = None,
        total_internet_traffic: int = None,
        total_nat_assets: int = None,
        total_nat_traffic: int = None,
        total_sdl_bill_traffic: int = None,
        total_sdl_free_traffic: int = None,
        total_traffic: int = None,
        total_vpc_assets: int = None,
        total_vpc_traffic: int = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The total number of assets that are protected by border firewalls.
        self.total_assets = total_assets
        # For the subscription edition, this is the total billed elastic traffic after deductions are applied. Unit: bytes.
        self.total_bill_traffic = total_bill_traffic
        # The total number of assets that are protected by Internet Border firewalls.
        self.total_internet_assets = total_internet_assets
        # The total traffic of the Internet Border. For the subscription edition, this is the total elastic traffic of the Internet Border. Unit: bytes.
        self.total_internet_traffic = total_internet_traffic
        # The total number of assets that are protected by NAT border firewalls.
        self.total_nat_assets = total_nat_assets
        # The total traffic of the NAT border. For the subscription edition, this is the total elastic traffic of the NAT border. Unit: bytes.
        self.total_nat_traffic = total_nat_traffic
        # The total billed traffic for data leakage detection.
        self.total_sdl_bill_traffic = total_sdl_bill_traffic
        # The total free traffic for data leakage detection.
        self.total_sdl_free_traffic = total_sdl_free_traffic
        # The total traffic. For the subscription edition, this is the total elastic traffic. Unit: bytes.
        self.total_traffic = total_traffic
        # The total number of assets that are protected by VPC border firewalls.
        self.total_vpc_assets = total_vpc_assets
        # The total traffic of the VPC border. For the subscription edition, this is the total elastic traffic of the VPC border. Unit: bytes.
        self.total_vpc_traffic = total_vpc_traffic

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_assets is not None:
            result['TotalAssets'] = self.total_assets

        if self.total_bill_traffic is not None:
            result['TotalBillTraffic'] = self.total_bill_traffic

        if self.total_internet_assets is not None:
            result['TotalInternetAssets'] = self.total_internet_assets

        if self.total_internet_traffic is not None:
            result['TotalInternetTraffic'] = self.total_internet_traffic

        if self.total_nat_assets is not None:
            result['TotalNatAssets'] = self.total_nat_assets

        if self.total_nat_traffic is not None:
            result['TotalNatTraffic'] = self.total_nat_traffic

        if self.total_sdl_bill_traffic is not None:
            result['TotalSdlBillTraffic'] = self.total_sdl_bill_traffic

        if self.total_sdl_free_traffic is not None:
            result['TotalSdlFreeTraffic'] = self.total_sdl_free_traffic

        if self.total_traffic is not None:
            result['TotalTraffic'] = self.total_traffic

        if self.total_vpc_assets is not None:
            result['TotalVpcAssets'] = self.total_vpc_assets

        if self.total_vpc_traffic is not None:
            result['TotalVpcTraffic'] = self.total_vpc_traffic

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalAssets') is not None:
            self.total_assets = m.get('TotalAssets')

        if m.get('TotalBillTraffic') is not None:
            self.total_bill_traffic = m.get('TotalBillTraffic')

        if m.get('TotalInternetAssets') is not None:
            self.total_internet_assets = m.get('TotalInternetAssets')

        if m.get('TotalInternetTraffic') is not None:
            self.total_internet_traffic = m.get('TotalInternetTraffic')

        if m.get('TotalNatAssets') is not None:
            self.total_nat_assets = m.get('TotalNatAssets')

        if m.get('TotalNatTraffic') is not None:
            self.total_nat_traffic = m.get('TotalNatTraffic')

        if m.get('TotalSdlBillTraffic') is not None:
            self.total_sdl_bill_traffic = m.get('TotalSdlBillTraffic')

        if m.get('TotalSdlFreeTraffic') is not None:
            self.total_sdl_free_traffic = m.get('TotalSdlFreeTraffic')

        if m.get('TotalTraffic') is not None:
            self.total_traffic = m.get('TotalTraffic')

        if m.get('TotalVpcAssets') is not None:
            self.total_vpc_assets = m.get('TotalVpcAssets')

        if m.get('TotalVpcTraffic') is not None:
            self.total_vpc_traffic = m.get('TotalVpcTraffic')

        return self

