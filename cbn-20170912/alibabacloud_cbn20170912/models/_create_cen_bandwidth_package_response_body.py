# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateCenBandwidthPackageResponseBody(DaraModel):
    def __init__(
        self,
        cen_bandwidth_package_id: str = None,
        cen_bandwidth_package_order_id: str = None,
        request_id: str = None,
    ):
        # The ID of the bandwidth plan.
        self.cen_bandwidth_package_id = cen_bandwidth_package_id
        # The ID of the order for the bandwidth plan.
        self.cen_bandwidth_package_order_id = cen_bandwidth_package_order_id
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cen_bandwidth_package_id is not None:
            result['CenBandwidthPackageId'] = self.cen_bandwidth_package_id

        if self.cen_bandwidth_package_order_id is not None:
            result['CenBandwidthPackageOrderId'] = self.cen_bandwidth_package_order_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CenBandwidthPackageId') is not None:
            self.cen_bandwidth_package_id = m.get('CenBandwidthPackageId')

        if m.get('CenBandwidthPackageOrderId') is not None:
            self.cen_bandwidth_package_order_id = m.get('CenBandwidthPackageOrderId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

