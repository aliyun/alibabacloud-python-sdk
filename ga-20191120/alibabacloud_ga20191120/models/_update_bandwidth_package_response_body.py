# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateBandwidthPackageResponseBody(DaraModel):
    def __init__(
        self,
        bandwidth_package: str = None,
        description: str = None,
        name: str = None,
        request_id: str = None,
    ):
        # The bandwidth plan ID.
        self.bandwidth_package = bandwidth_package
        # The description of the bandwidth plan.
        self.description = description
        # The name of the bandwidth plan.
        self.name = name
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bandwidth_package is not None:
            result['BandwidthPackage'] = self.bandwidth_package

        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BandwidthPackage') is not None:
            self.bandwidth_package = m.get('BandwidthPackage')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

