# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DeleteVulAutoRepairConfigRequest(DaraModel):
    def __init__(
        self,
        alias_name: str = None,
        config_id_list: List[int] = None,
        type: str = None,
    ):
        # The alias of the vulnerability.
        self.alias_name = alias_name
        # The IDs of the configurations.
        # 
        # >  You can call the [ListVulAutoRepairConfig](~~ListVulAutoRepairConfig~~) operation to query the IDs.
        self.config_id_list = config_id_list
        # The type of the vulnerability. Valid values:
        # 
        # *   cve: Linux software vulnerability
        # *   sys: Windows system vulnerability
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name

        if self.config_id_list is not None:
            result['ConfigIdList'] = self.config_id_list

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')

        if m.get('ConfigIdList') is not None:
            self.config_id_list = m.get('ConfigIdList')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

