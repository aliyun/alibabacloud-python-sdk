# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eds_aic20230930 import models as main_models
from darabonba.model import DaraModel

class DescribeEdgeMobileAgentPackagesResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        packages: List[main_models.DescribeEdgeMobileAgentPackagesResponseBodyPackages] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The actual number of entries returned on the current page.
        self.max_results = max_results
        # The pagination token for the next page. An empty value indicates that no more data exists.
        self.next_token = next_token
        # The list of packages.
        self.packages = packages
        # The request ID.
        self.request_id = request_id
        # The total number of records.
        self.total_count = total_count

    def validate(self):
        if self.packages:
            for v1 in self.packages:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        result['Packages'] = []
        if self.packages is not None:
            for k1 in self.packages:
                result['Packages'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        self.packages = []
        if m.get('Packages') is not None:
            for k1 in m.get('Packages'):
                temp_model = main_models.DescribeEdgeMobileAgentPackagesResponseBodyPackages()
                self.packages.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeEdgeMobileAgentPackagesResponseBodyPackages(DaraModel):
    def __init__(
        self,
        device_class: str = None,
        expire_date: str = None,
        license_keys: List[str] = None,
        package_id: str = None,
        package_spec: str = None,
        status: str = None,
    ):
        # The device type.
        self.device_class = device_class
        # The expiration time.
        self.expire_date = expire_date
        # The list of license keys.
        self.license_keys = license_keys
        # The package ID.
        self.package_id = package_id
        # The package specification. Currently, only hardware is supported.
        self.package_spec = package_spec
        # The package status.
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

        if self.expire_date is not None:
            result['ExpireDate'] = self.expire_date

        if self.license_keys is not None:
            result['LicenseKeys'] = self.license_keys

        if self.package_id is not None:
            result['PackageId'] = self.package_id

        if self.package_spec is not None:
            result['PackageSpec'] = self.package_spec

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceClass') is not None:
            self.device_class = m.get('DeviceClass')

        if m.get('ExpireDate') is not None:
            self.expire_date = m.get('ExpireDate')

        if m.get('LicenseKeys') is not None:
            self.license_keys = m.get('LicenseKeys')

        if m.get('PackageId') is not None:
            self.package_id = m.get('PackageId')

        if m.get('PackageSpec') is not None:
            self.package_spec = m.get('PackageSpec')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

