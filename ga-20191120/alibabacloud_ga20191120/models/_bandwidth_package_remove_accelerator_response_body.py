# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class BandwidthPackageRemoveAcceleratorResponseBody(DaraModel):
    def __init__(
        self,
        accelerators: List[str] = None,
        bandwidth_package_id: str = None,
        request_id: str = None,
    ):
        # The ID of the GA instance.
        self.accelerators = accelerators
        # The ID of the bandwidth plan.
        self.bandwidth_package_id = bandwidth_package_id
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accelerators is not None:
            result['Accelerators'] = self.accelerators

        if self.bandwidth_package_id is not None:
            result['BandwidthPackageId'] = self.bandwidth_package_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accelerators') is not None:
            self.accelerators = m.get('Accelerators')

        if m.get('BandwidthPackageId') is not None:
            self.bandwidth_package_id = m.get('BandwidthPackageId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

