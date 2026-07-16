# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeMobileAgentPackageRequest(DaraModel):
    def __init__(
        self,
        instance_ids: List[str] = None,
        package_ids: List[str] = None,
        package_spec: str = None,
        package_status: str = None,
        page_num: int = None,
        page_size: int = None,
    ):
        # An array of node instance IDs.
        self.instance_ids = instance_ids
        # An array of package IDs.
        self.package_ids = package_ids
        # The package specification.
        self.package_spec = package_spec
        # The package status.
        self.package_status = package_status
        # The page number. Default value: 1.
        self.page_num = page_num
        # The number of entries per page.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.package_ids is not None:
            result['PackageIds'] = self.package_ids

        if self.package_spec is not None:
            result['PackageSpec'] = self.package_spec

        if self.package_status is not None:
            result['PackageStatus'] = self.package_status

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('PackageIds') is not None:
            self.package_ids = m.get('PackageIds')

        if m.get('PackageSpec') is not None:
            self.package_spec = m.get('PackageSpec')

        if m.get('PackageStatus') is not None:
            self.package_status = m.get('PackageStatus')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

