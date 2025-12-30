# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ehpc20240730 import models as main_models
from darabonba.model import DaraModel

class InstallSoftwaresRequest(DaraModel):
    def __init__(
        self,
        additional_packages: List[main_models.InstallSoftwaresRequestAdditionalPackages] = None,
        cluster_id: str = None,
    ):
        # The information about the software systems that you want to install.
        self.additional_packages = additional_packages
        # The cluster ID.
        self.cluster_id = cluster_id

    def validate(self):
        if self.additional_packages:
            for v1 in self.additional_packages:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AdditionalPackages'] = []
        if self.additional_packages is not None:
            for k1 in self.additional_packages:
                result['AdditionalPackages'].append(k1.to_map() if k1 else None)

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.additional_packages = []
        if m.get('AdditionalPackages') is not None:
            for k1 in m.get('AdditionalPackages'):
                temp_model = main_models.InstallSoftwaresRequestAdditionalPackages()
                self.additional_packages.append(temp_model.from_map(k1))

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        return self

class InstallSoftwaresRequestAdditionalPackages(DaraModel):
    def __init__(
        self,
        name: str = None,
        version: str = None,
    ):
        # The software name.
        self.name = name
        # The software version.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

