# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sddp20260120 import models as main_models
from darabonba.model import DaraModel

class ListMiniEngineVersionsResponseBody(DaraModel):
    def __init__(
        self,
        kernel_versions: List[main_models.ListMiniEngineVersionsResponseBodyKernelVersions] = None,
        request_id: str = None,
    ):
        self.kernel_versions = kernel_versions
        self.request_id = request_id

    def validate(self):
        if self.kernel_versions:
            for v1 in self.kernel_versions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['KernelVersions'] = []
        if self.kernel_versions is not None:
            for k1 in self.kernel_versions:
                result['KernelVersions'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.kernel_versions = []
        if m.get('KernelVersions') is not None:
            for k1 in m.get('KernelVersions'):
                temp_model = main_models.ListMiniEngineVersionsResponseBodyKernelVersions()
                self.kernel_versions.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListMiniEngineVersionsResponseBodyKernelVersions(DaraModel):
    def __init__(
        self,
        kernel_release_type: str = None,
        kernel_version: str = None,
        kernel_version_name: str = None,
    ):
        self.kernel_release_type = kernel_release_type
        self.kernel_version = kernel_version
        self.kernel_version_name = kernel_version_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.kernel_release_type is not None:
            result['KernelReleaseType'] = self.kernel_release_type

        if self.kernel_version is not None:
            result['KernelVersion'] = self.kernel_version

        if self.kernel_version_name is not None:
            result['KernelVersionName'] = self.kernel_version_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KernelReleaseType') is not None:
            self.kernel_release_type = m.get('KernelReleaseType')

        if m.get('KernelVersion') is not None:
            self.kernel_version = m.get('KernelVersion')

        if m.get('KernelVersionName') is not None:
            self.kernel_version_name = m.get('KernelVersionName')

        return self

