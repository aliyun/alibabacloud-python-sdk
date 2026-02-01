# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sysom20231230 import models as main_models
from darabonba.model import DaraModel

class ListAgentsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: List[main_models.ListAgentsResponseBodyData] = None,
        message: str = None,
        total: int = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data
        self.message = message
        self.total = total

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.code is not None:
            result['code'] = self.code

        result['data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['data'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['message'] = self.message

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('code') is not None:
            self.code = m.get('code')

        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.ListAgentsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

class ListAgentsResponseBodyData(DaraModel):
    def __init__(
        self,
        created_at: str = None,
        description: str = None,
        id: str = None,
        name: str = None,
        support_arch: str = None,
        type: str = None,
        updated_at: str = None,
        versions: List[main_models.ListAgentsResponseBodyDataVersions] = None,
    ):
        self.created_at = created_at
        self.description = description
        self.id = id
        self.name = name
        self.support_arch = support_arch
        self.type = type
        self.updated_at = updated_at
        self.versions = versions

    def validate(self):
        if self.versions:
            for v1 in self.versions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_at is not None:
            result['created_at'] = self.created_at

        if self.description is not None:
            result['description'] = self.description

        if self.id is not None:
            result['id'] = self.id

        if self.name is not None:
            result['name'] = self.name

        if self.support_arch is not None:
            result['support_arch'] = self.support_arch

        if self.type is not None:
            result['type'] = self.type

        if self.updated_at is not None:
            result['updated_at'] = self.updated_at

        result['versions'] = []
        if self.versions is not None:
            for k1 in self.versions:
                result['versions'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('support_arch') is not None:
            self.support_arch = m.get('support_arch')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')

        self.versions = []
        if m.get('versions') is not None:
            for k1 in m.get('versions'):
                temp_model = main_models.ListAgentsResponseBodyDataVersions()
                self.versions.append(temp_model.from_map(k1))

        return self

class ListAgentsResponseBodyDataVersions(DaraModel):
    def __init__(
        self,
        created_at: str = None,
        install_script: str = None,
        uninstall_script: str = None,
        updated_at: str = None,
        upgrade_script: str = None,
        version: str = None,
    ):
        self.created_at = created_at
        self.install_script = install_script
        self.uninstall_script = uninstall_script
        self.updated_at = updated_at
        self.upgrade_script = upgrade_script
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_at is not None:
            result['created_at'] = self.created_at

        if self.install_script is not None:
            result['install_script'] = self.install_script

        if self.uninstall_script is not None:
            result['uninstall_script'] = self.uninstall_script

        if self.updated_at is not None:
            result['updated_at'] = self.updated_at

        if self.upgrade_script is not None:
            result['upgrade_script'] = self.upgrade_script

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')

        if m.get('install_script') is not None:
            self.install_script = m.get('install_script')

        if m.get('uninstall_script') is not None:
            self.uninstall_script = m.get('uninstall_script')

        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')

        if m.get('upgrade_script') is not None:
            self.upgrade_script = m.get('upgrade_script')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

