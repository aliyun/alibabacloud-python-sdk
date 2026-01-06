# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class DescribeKernelVersionResponseBody(DaraModel):
    def __init__(
        self,
        available_kernel_versions: List[main_models.DescribeKernelVersionResponseBodyAvailableKernelVersions] = None,
        expire_date: str = None,
        kernel_version: str = None,
        request_id: str = None,
    ):
        # The minor versions to which you can update the current minor version of the cluster.
        self.available_kernel_versions = available_kernel_versions
        # The maintenance expiration time of the version. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC. After the time arrives, the system no longer maintains the version. If any issues occur, update the minor version of the cluster to a later version.
        self.expire_date = expire_date
        # The minor version of the cluster. Example: **3.1.8**.
        self.kernel_version = kernel_version
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.available_kernel_versions:
            for v1 in self.available_kernel_versions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AvailableKernelVersions'] = []
        if self.available_kernel_versions is not None:
            for k1 in self.available_kernel_versions:
                result['AvailableKernelVersions'].append(k1.to_map() if k1 else None)

        if self.expire_date is not None:
            result['ExpireDate'] = self.expire_date

        if self.kernel_version is not None:
            result['KernelVersion'] = self.kernel_version

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.available_kernel_versions = []
        if m.get('AvailableKernelVersions') is not None:
            for k1 in m.get('AvailableKernelVersions'):
                temp_model = main_models.DescribeKernelVersionResponseBodyAvailableKernelVersions()
                self.available_kernel_versions.append(temp_model.from_map(k1))

        if m.get('ExpireDate') is not None:
            self.expire_date = m.get('ExpireDate')

        if m.get('KernelVersion') is not None:
            self.kernel_version = m.get('KernelVersion')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeKernelVersionResponseBodyAvailableKernelVersions(DaraModel):
    def __init__(
        self,
        expire_date: str = None,
        kernel_version: str = None,
        release_date: str = None,
    ):
        # The maintenance expiration time of the version. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC. After the time arrives, the system no longer maintains the version. If any issues occur, update the minor version of the cluster to a later version.
        self.expire_date = expire_date
        # The minor version. Example: **3.1.9**.
        self.kernel_version = kernel_version
        # The time when the minor version was released. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.release_date = release_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expire_date is not None:
            result['ExpireDate'] = self.expire_date

        if self.kernel_version is not None:
            result['KernelVersion'] = self.kernel_version

        if self.release_date is not None:
            result['ReleaseDate'] = self.release_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpireDate') is not None:
            self.expire_date = m.get('ExpireDate')

        if m.get('KernelVersion') is not None:
            self.kernel_version = m.get('KernelVersion')

        if m.get('ReleaseDate') is not None:
            self.release_date = m.get('ReleaseDate')

        return self

