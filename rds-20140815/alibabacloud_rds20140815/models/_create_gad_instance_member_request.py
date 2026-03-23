# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class CreateGadInstanceMemberRequest(DaraModel):
    def __init__(
        self,
        central_dbinstance_id: str = None,
        central_rds_dts_admin_account: str = None,
        central_rds_dts_admin_password: str = None,
        central_region_id: str = None,
        dblist: str = None,
        gad_instance_id: str = None,
        unit_node: List[main_models.CreateGadInstanceMemberRequestUnitNode] = None,
    ):
        # This parameter is required.
        self.central_dbinstance_id = central_dbinstance_id
        # This parameter is required.
        self.central_rds_dts_admin_account = central_rds_dts_admin_account
        # This parameter is required.
        self.central_rds_dts_admin_password = central_rds_dts_admin_password
        # This parameter is required.
        self.central_region_id = central_region_id
        # This parameter is required.
        self.dblist = dblist
        # This parameter is required.
        self.gad_instance_id = gad_instance_id
        # This parameter is required.
        self.unit_node = unit_node

    def validate(self):
        if self.unit_node:
            for v1 in self.unit_node:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.central_dbinstance_id is not None:
            result['CentralDBInstanceId'] = self.central_dbinstance_id

        if self.central_rds_dts_admin_account is not None:
            result['CentralRdsDtsAdminAccount'] = self.central_rds_dts_admin_account

        if self.central_rds_dts_admin_password is not None:
            result['CentralRdsDtsAdminPassword'] = self.central_rds_dts_admin_password

        if self.central_region_id is not None:
            result['CentralRegionId'] = self.central_region_id

        if self.dblist is not None:
            result['DBList'] = self.dblist

        if self.gad_instance_id is not None:
            result['GadInstanceId'] = self.gad_instance_id

        result['UnitNode'] = []
        if self.unit_node is not None:
            for k1 in self.unit_node:
                result['UnitNode'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CentralDBInstanceId') is not None:
            self.central_dbinstance_id = m.get('CentralDBInstanceId')

        if m.get('CentralRdsDtsAdminAccount') is not None:
            self.central_rds_dts_admin_account = m.get('CentralRdsDtsAdminAccount')

        if m.get('CentralRdsDtsAdminPassword') is not None:
            self.central_rds_dts_admin_password = m.get('CentralRdsDtsAdminPassword')

        if m.get('CentralRegionId') is not None:
            self.central_region_id = m.get('CentralRegionId')

        if m.get('DBList') is not None:
            self.dblist = m.get('DBList')

        if m.get('GadInstanceId') is not None:
            self.gad_instance_id = m.get('GadInstanceId')

        self.unit_node = []
        if m.get('UnitNode') is not None:
            for k1 in m.get('UnitNode'):
                temp_model = main_models.CreateGadInstanceMemberRequestUnitNode()
                self.unit_node.append(temp_model.from_map(k1))

        return self

class CreateGadInstanceMemberRequestUnitNode(DaraModel):
    def __init__(
        self,
        dbinstance_description: str = None,
        dbinstance_storage: int = None,
        dbinstance_storage_type: str = None,
        db_instance_class: str = None,
        dts_conflict: str = None,
        dts_instance_class: str = None,
        engine: str = None,
        engine_version: str = None,
        region_id: str = None,
        security_iplist: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        zone_id: str = None,
        zone_idslave_1: str = None,
        zone_idslave_2: str = None,
    ):
        self.dbinstance_description = dbinstance_description
        self.dbinstance_storage = dbinstance_storage
        self.dbinstance_storage_type = dbinstance_storage_type
        self.db_instance_class = db_instance_class
        # This parameter is required.
        self.dts_conflict = dts_conflict
        # This parameter is required.
        self.dts_instance_class = dts_instance_class
        self.engine = engine
        self.engine_version = engine_version
        # This parameter is required.
        self.region_id = region_id
        self.security_iplist = security_iplist
        # This parameter is required.
        self.v_switch_id = v_switch_id
        # This parameter is required.
        self.vpc_id = vpc_id
        self.zone_id = zone_id
        self.zone_idslave_1 = zone_idslave_1
        self.zone_idslave_2 = zone_idslave_2

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description

        if self.dbinstance_storage is not None:
            result['DBInstanceStorage'] = self.dbinstance_storage

        if self.dbinstance_storage_type is not None:
            result['DBInstanceStorageType'] = self.dbinstance_storage_type

        if self.db_instance_class is not None:
            result['DbInstanceClass'] = self.db_instance_class

        if self.dts_conflict is not None:
            result['DtsConflict'] = self.dts_conflict

        if self.dts_instance_class is not None:
            result['DtsInstanceClass'] = self.dts_instance_class

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        if self.region_id is not None:
            result['RegionID'] = self.region_id

        if self.security_iplist is not None:
            result['SecurityIPList'] = self.security_iplist

        if self.v_switch_id is not None:
            result['VSwitchID'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcID'] = self.vpc_id

        if self.zone_id is not None:
            result['ZoneID'] = self.zone_id

        if self.zone_idslave_1 is not None:
            result['ZoneIDSlave1'] = self.zone_idslave_1

        if self.zone_idslave_2 is not None:
            result['ZoneIDSlave2'] = self.zone_idslave_2

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')

        if m.get('DBInstanceStorage') is not None:
            self.dbinstance_storage = m.get('DBInstanceStorage')

        if m.get('DBInstanceStorageType') is not None:
            self.dbinstance_storage_type = m.get('DBInstanceStorageType')

        if m.get('DbInstanceClass') is not None:
            self.db_instance_class = m.get('DbInstanceClass')

        if m.get('DtsConflict') is not None:
            self.dts_conflict = m.get('DtsConflict')

        if m.get('DtsInstanceClass') is not None:
            self.dts_instance_class = m.get('DtsInstanceClass')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        if m.get('RegionID') is not None:
            self.region_id = m.get('RegionID')

        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')

        if m.get('VSwitchID') is not None:
            self.v_switch_id = m.get('VSwitchID')

        if m.get('VpcID') is not None:
            self.vpc_id = m.get('VpcID')

        if m.get('ZoneID') is not None:
            self.zone_id = m.get('ZoneID')

        if m.get('ZoneIDSlave1') is not None:
            self.zone_idslave_1 = m.get('ZoneIDSlave1')

        if m.get('ZoneIDSlave2') is not None:
            self.zone_idslave_2 = m.get('ZoneIDSlave2')

        return self

