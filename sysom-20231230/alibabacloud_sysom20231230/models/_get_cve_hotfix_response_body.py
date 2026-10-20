# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sysom20231230 import models as main_models
from darabonba.model import DaraModel

class GetCveHotfixResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.GetCveHotfixResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
    ):
        # The status code.
        # - If `code == Success`, the authorization is successful.
        # - Other status codes indicate that the authorization failed. If the authorization failed, check the `message` field for the detailed fault information.
        self.code = code
        # The returned data.
        self.data = data
        # The error message.
        # - If `code == Success`, this field is empty.
        # - Otherwise, this field contains the request error message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        result['data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['data'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.GetCveHotfixResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetCveHotfixResponseBodyData(DaraModel):
    def __init__(
        self,
        cve_id: str = None,
        hotfix: main_models.GetCveHotfixResponseBodyDataHotfix = None,
    ):
        # The CVE ID.
        self.cve_id = cve_id
        # The hotfix information for the CVE.
        self.hotfix = hotfix

    def validate(self):
        if self.hotfix:
            self.hotfix.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cve_id is not None:
            result['cveId'] = self.cve_id

        if self.hotfix is not None:
            result['hotfix'] = self.hotfix.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cveId') is not None:
            self.cve_id = m.get('cveId')

        if m.get('hotfix') is not None:
            temp_model = main_models.GetCveHotfixResponseBodyDataHotfix()
            self.hotfix = temp_model.from_map(m.get('hotfix'))

        return self

class GetCveHotfixResponseBodyDataHotfix(DaraModel):
    def __init__(
        self,
        description: str = None,
        hotfix_name: str = None,
        module_name: str = None,
        packages: List[main_models.GetCveHotfixResponseBodyDataHotfixPackages] = None,
        version: str = None,
    ):
        # The hotfix description.
        self.description = description
        # The hotfix name.
        self.hotfix_name = hotfix_name
        # The hotfix module name.
        self.module_name = module_name
        # The list of published packages that meet the kernel requirements.
        self.packages = packages
        # The hotfix version.
        self.version = version

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
        if self.description is not None:
            result['description'] = self.description

        if self.hotfix_name is not None:
            result['hotfixName'] = self.hotfix_name

        if self.module_name is not None:
            result['moduleName'] = self.module_name

        result['packages'] = []
        if self.packages is not None:
            for k1 in self.packages:
                result['packages'].append(k1.to_map() if k1 else None)

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('hotfixName') is not None:
            self.hotfix_name = m.get('hotfixName')

        if m.get('moduleName') is not None:
            self.module_name = m.get('moduleName')

        self.packages = []
        if m.get('packages') is not None:
            for k1 in m.get('packages'):
                temp_model = main_models.GetCveHotfixResponseBodyDataHotfixPackages()
                self.packages.append(temp_model.from_map(k1))

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

class GetCveHotfixResponseBodyDataHotfixPackages(DaraModel):
    def __init__(
        self,
        arch: str = None,
        distro: str = None,
        kernel_version: str = None,
        rpm_nevra: str = None,
    ):
        # The architecture.
        self.arch = arch
        # The distribution. This value is null if the distribution is not registered.
        self.distro = distro
        # The compatible full kernel version.
        self.kernel_version = kernel_version
        # The RPM package identifier.
        self.rpm_nevra = rpm_nevra

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arch is not None:
            result['arch'] = self.arch

        if self.distro is not None:
            result['distro'] = self.distro

        if self.kernel_version is not None:
            result['kernelVersion'] = self.kernel_version

        if self.rpm_nevra is not None:
            result['rpmNevra'] = self.rpm_nevra

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('arch') is not None:
            self.arch = m.get('arch')

        if m.get('distro') is not None:
            self.distro = m.get('distro')

        if m.get('kernelVersion') is not None:
            self.kernel_version = m.get('kernelVersion')

        if m.get('rpmNevra') is not None:
            self.rpm_nevra = m.get('rpmNevra')

        return self

