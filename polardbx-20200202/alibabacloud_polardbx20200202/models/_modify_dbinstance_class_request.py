# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDBInstanceClassRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        cn_class: str = None,
        dbinstance_name: str = None,
        dn_class: str = None,
        dn_storage_space: str = None,
        region_id: str = None,
        specified_dnscale: bool = None,
        specified_dnspec_map_json: str = None,
        switch_time: str = None,
        switch_time_mode: str = None,
        target_dbinstance_class: str = None,
    ):
        self.client_token = client_token
        self.cn_class = cn_class
        # This parameter is required.
        self.dbinstance_name = dbinstance_name
        self.dn_class = dn_class
        self.dn_storage_space = dn_storage_space
        # This parameter is required.
        self.region_id = region_id
        self.specified_dnscale = specified_dnscale
        self.specified_dnspec_map_json = specified_dnspec_map_json
        self.switch_time = switch_time
        self.switch_time_mode = switch_time_mode
        self.target_dbinstance_class = target_dbinstance_class

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.cn_class is not None:
            result['CnClass'] = self.cn_class

        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.dn_class is not None:
            result['DnClass'] = self.dn_class

        if self.dn_storage_space is not None:
            result['DnStorageSpace'] = self.dn_storage_space

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.specified_dnscale is not None:
            result['SpecifiedDNScale'] = self.specified_dnscale

        if self.specified_dnspec_map_json is not None:
            result['SpecifiedDNSpecMapJson'] = self.specified_dnspec_map_json

        if self.switch_time is not None:
            result['SwitchTime'] = self.switch_time

        if self.switch_time_mode is not None:
            result['SwitchTimeMode'] = self.switch_time_mode

        if self.target_dbinstance_class is not None:
            result['TargetDBInstanceClass'] = self.target_dbinstance_class

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('CnClass') is not None:
            self.cn_class = m.get('CnClass')

        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('DnClass') is not None:
            self.dn_class = m.get('DnClass')

        if m.get('DnStorageSpace') is not None:
            self.dn_storage_space = m.get('DnStorageSpace')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SpecifiedDNScale') is not None:
            self.specified_dnscale = m.get('SpecifiedDNScale')

        if m.get('SpecifiedDNSpecMapJson') is not None:
            self.specified_dnspec_map_json = m.get('SpecifiedDNSpecMapJson')

        if m.get('SwitchTime') is not None:
            self.switch_time = m.get('SwitchTime')

        if m.get('SwitchTimeMode') is not None:
            self.switch_time_mode = m.get('SwitchTimeMode')

        if m.get('TargetDBInstanceClass') is not None:
            self.target_dbinstance_class = m.get('TargetDBInstanceClass')

        return self

