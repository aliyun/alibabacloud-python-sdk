# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeEdgeMobileAgentPackagesRequest(DaraModel):
    def __init__(
        self,
        device_class: str = None,
        license_keys: str = None,
        max_results: int = None,
        next_token: str = None,
        package_ids: str = None,
        status: str = None,
    ):
        # The device type filter. Valid values: BOX, PHONE, PAD, and OTHER.
        self.device_class = device_class
        # The list of license keys. Separate multiple keys with commas.
        self.license_keys = license_keys
        # The maximum number of entries per page. Valid values: 1 to 100. Default value: 20.
        self.max_results = max_results
        # The pagination token. Leave this parameter empty for the first query. For subsequent queries, use the value returned in the previous response.
        self.next_token = next_token
        # The list of package IDs. Separate multiple IDs with commas.
        self.package_ids = package_ids
        # The package status filter.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_class is not None:
            result['DeviceClass'] = self.device_class

        if self.license_keys is not None:
            result['LicenseKeys'] = self.license_keys

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.package_ids is not None:
            result['PackageIds'] = self.package_ids

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceClass') is not None:
            self.device_class = m.get('DeviceClass')

        if m.get('LicenseKeys') is not None:
            self.license_keys = m.get('LicenseKeys')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PackageIds') is not None:
            self.package_ids = m.get('PackageIds')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

