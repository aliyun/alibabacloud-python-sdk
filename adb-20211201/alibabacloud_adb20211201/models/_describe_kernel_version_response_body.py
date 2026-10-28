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
        # The list of target versions to which the current version can be upgraded.
        self.available_kernel_versions = available_kernel_versions
        # The end-of-support date of the version. The time is in the yyyy-MM-DD HH:mm:ss format. After this date, the system no longer maintains this version. If any issues occur, upgrade to a later version.
        self.expire_date = expire_date
        # The kernel version number of the cluster. Example: **3.1.8**.
        self.kernel_version = kernel_version
        # The ID of the request.
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
        # The end-of-support date of the version. The time is in the yyyy-MM-DD HH:mm:ss format. After this date, the system no longer maintains this version. If any issues occur, upgrade to a later version.
        self.expire_date = expire_date
        # The kernel version number of the cluster. Example: **3.1.9**.
        self.kernel_version = kernel_version
        # The release time of the kernel version. The time format is yyyy-MM-DD HH:mm:ss.
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

