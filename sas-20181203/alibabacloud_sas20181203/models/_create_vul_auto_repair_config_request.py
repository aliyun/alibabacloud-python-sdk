# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class CreateVulAutoRepairConfigRequest(DaraModel):
    def __init__(
        self,
        reason: str = None,
        type: str = None,
        vul_auto_repair_config_list: List[main_models.CreateVulAutoRepairConfigRequestVulAutoRepairConfigList] = None,
    ):
        # The reason why the vulnerability can be automatically fixed.
        self.reason = reason
        # The type of the vulnerability. Valid values: -**cve**: Linux software vulnerability -**sys**: Windows system vulnerability
        # 
        # This parameter is required.
        self.type = type
        # The vulnerabilities that can be automatically fixed.
        # 
        # This parameter is required.
        self.vul_auto_repair_config_list = vul_auto_repair_config_list

    def validate(self):
        if self.vul_auto_repair_config_list:
            for v1 in self.vul_auto_repair_config_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.reason is not None:
            result['Reason'] = self.reason

        if self.type is not None:
            result['Type'] = self.type

        result['VulAutoRepairConfigList'] = []
        if self.vul_auto_repair_config_list is not None:
            for k1 in self.vul_auto_repair_config_list:
                result['VulAutoRepairConfigList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        self.vul_auto_repair_config_list = []
        if m.get('VulAutoRepairConfigList') is not None:
            for k1 in m.get('VulAutoRepairConfigList'):
                temp_model = main_models.CreateVulAutoRepairConfigRequestVulAutoRepairConfigList()
                self.vul_auto_repair_config_list.append(temp_model.from_map(k1))

        return self

class CreateVulAutoRepairConfigRequestVulAutoRepairConfigList(DaraModel):
    def __init__(
        self,
        alias_name: str = None,
        name: str = None,
    ):
        # The alias of the vulnerability.
        # 
        # This parameter is required.
        self.alias_name = alias_name
        # The name of the vulnerability.
        # 
        # This parameter is required.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

