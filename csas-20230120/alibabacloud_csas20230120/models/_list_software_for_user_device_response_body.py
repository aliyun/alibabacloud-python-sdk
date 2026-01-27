# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class ListSoftwareForUserDeviceResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        software: List[main_models.ListSoftwareForUserDeviceResponseBodySoftware] = None,
        total_num: int = None,
    ):
        self.request_id = request_id
        self.software = software
        self.total_num = total_num

    def validate(self):
        if self.software:
            for v1 in self.software:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Software'] = []
        if self.software is not None:
            for k1 in self.software:
                result['Software'].append(k1.to_map() if k1 else None)

        if self.total_num is not None:
            result['TotalNum'] = self.total_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.software = []
        if m.get('Software') is not None:
            for k1 in m.get('Software'):
                temp_model = main_models.ListSoftwareForUserDeviceResponseBodySoftware()
                self.software.append(temp_model.from_map(k1))

        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')

        return self

class ListSoftwareForUserDeviceResponseBodySoftware(DaraModel):
    def __init__(
        self,
        inc: str = None,
        install_time: str = None,
        name: str = None,
        versions: List[str] = None,
    ):
        self.inc = inc
        self.install_time = install_time
        self.name = name
        self.versions = versions

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.inc is not None:
            result['Inc'] = self.inc

        if self.install_time is not None:
            result['InstallTime'] = self.install_time

        if self.name is not None:
            result['Name'] = self.name

        if self.versions is not None:
            result['Versions'] = self.versions

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Inc') is not None:
            self.inc = m.get('Inc')

        if m.get('InstallTime') is not None:
            self.install_time = m.get('InstallTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Versions') is not None:
            self.versions = m.get('Versions')

        return self

