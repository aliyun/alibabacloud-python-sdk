# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_starrocks20221019 import models as main_models
from darabonba.model import DaraModel

class ModifyHostAliasRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        host_aliases: List[main_models.ModifyHostAliasRequestHostAliases] = None,
    ):
        self.instance_id = instance_id
        self.host_aliases = host_aliases

    def validate(self):
        if self.host_aliases:
            for v1 in self.host_aliases:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        result['hostAliases'] = []
        if self.host_aliases is not None:
            for k1 in self.host_aliases:
                result['hostAliases'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        self.host_aliases = []
        if m.get('hostAliases') is not None:
            for k1 in m.get('hostAliases'):
                temp_model = main_models.ModifyHostAliasRequestHostAliases()
                self.host_aliases.append(temp_model.from_map(k1))

        return self

class ModifyHostAliasRequestHostAliases(DaraModel):
    def __init__(
        self,
        hostnames: List[str] = None,
        ip: str = None,
    ):
        self.hostnames = hostnames
        self.ip = ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hostnames is not None:
            result['hostnames'] = self.hostnames

        if self.ip is not None:
            result['ip'] = self.ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hostnames') is not None:
            self.hostnames = m.get('hostnames')

        if m.get('ip') is not None:
            self.ip = m.get('ip')

        return self

