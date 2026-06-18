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
        # The client token. It can be any unique string.
        self.client_token = client_token
        # **Target specifications for Enterprise Edition compute node specification changes**
        # 
        # **Primary instance compute node specifications (Enterprise Edition CN) general-purpose**	
        # - polarx.x4.medium.2e	2 cores, 8 GB (general-purpose)
        # - polarx.x4.large.2e	4 cores, 16 GB (general-purpose)
        # - polarx.x4.xlarge.2e	8 cores, 32 GB (general-purpose)
        # - polarx.x4.2xlarge.2e 16 cores, 64 GB (general-purpose)
        # 
        # **Primary instance compute node specifications (Enterprise Edition CN) dedicated**	
        # - polarx.x8.large.2e	4 cores, 32 GB (dedicated)
        # - polarx.x8.xlarge.2e	8 cores, 64 GB (dedicated)
        # - polarx.x8.2xlarge.2e	16 cores, 128 GB (dedicated)
        # - polarx.x4.4xlarge.2e	32 cores, 128 GB (dedicated)
        # - polarx.x8.4xlarge.2e	32 cores, 256 GB (dedicated)
        # - polarx.st.8xlarge.2e	60 cores, 470 GB (dedicated)
        # - polarx.st.12xlarge.2e	90 cores, 720 GB (dedicated)
        # 
        # **Read-only instance compute node specifications (Enterprise Edition CN) general-purpose**	
        # 
        # - polarxro.x4.medium.2e	2 cores, 8 GB (general-purpose)
        # - polarxro.x4.large.2e	4 cores, 16 GB (general-purpose)
        # - polarxro.x4.xlarge.2e	8 cores, 32 GB (general-purpose)
        # - polarxro.x4.2xlarge.2e	16 cores, 64 GB (general-purpose)
        # 
        # **Read-only instance compute node specifications (Enterprise Edition CN) dedicated**	
        # 
        # - polarxro.x8.large.2e	4 cores, 32 GB (dedicated)
        # - polarxro.x8.xlarge.2e	8 cores, 64 GB (dedicated)
        # - polarxro.x8.2xlarge.2e	16 cores, 128 GB (dedicated)
        # - polarxro.x4.4xlarge.2e	32 cores, 128 GB (dedicated)
        # - polarxro.x8.4xlarge.2e	32 cores, 256 GB (dedicated)
        # - polarxro.st.8xlarge.2e	60 cores, 470 GB (dedicated physical machine)
        # - polarxro.st.12xlarge.2e	90 cores, 720 GB (dedicated physical machine).
        self.cn_class = cn_class
        # The instance ID.
        # 
        # This parameter is required.
        self.dbinstance_name = dbinstance_name
        # **Target specifications for Enterprise Edition storage node specification changes**
        # 
        # **Storage node specifications (Enterprise Edition DN) general-purpose**	
        # 
        # - mysql.n4.medium.25	2 cores, 8 GB (general-purpose)
        # - mysql.n4.large.25	4 cores, 16 GB (general-purpose)
        # - mysql.n4.xlarge.25	8 cores, 32 GB (general-purpose)
        # - mysql.n4.2xlarge.25	16 cores, 64 GB (general-purpose)
        # 
        # **Storage node specifications (Enterprise Edition DN) dedicated**	
        # 
        # - mysql.x8.large.25	4 cores, 32 GB (dedicated)
        # - mysql.x8.xlarge.25	8 cores, 64 GB (dedicated)
        # - mysql.x8.2xlarge.25	16 cores, 128 GB (dedicated)
        # - mysql.x4.4xlarge.25	32 cores, 128 GB (dedicated)
        # - mysql.x8.4xlarge.25	32 cores, 256 GB (dedicated)
        # - mysql.st.8xlarge.25	60 cores, 470 GB (dedicated)
        # - mysql.st.12xlarge.25	90 cores, 720 GB (dedicated)
        # 
        # **Read-only instance storage node specifications (Enterprise Edition DN) general-purpose**	
        # 
        # - rds.mysql.s2.xlarge	2 cores, 8 GB (general-purpose)
        # - mysqlro.x4.large.1	4 cores, 16 GB (general-purpose)
        # - mysqlro.x4.xlarge.1	8 cores, 32 GB (general-purpose)
        # - mysqlro.x4.2xlarge.1	16 cores, 64 GB (general-purpose)
        # 
        # **Read-only instance storage node specifications (Enterprise Edition DN) dedicated**	
        # 
        # - mysqlro.x8.large.1	4 cores, 32 GB (dedicated)
        # - mysqlro.x8.xlarge.1	8 cores, 64 GB (dedicated)
        # - mysqlro.x8.2xlarge.1	16 cores, 128 GB (dedicated)
        # - mysqlro.x4.4xlarge.1	32 cores, 128 GB (dedicated)
        # - mysqlro.x8.4xlarge.1	32 cores, 256 GB (dedicated)
        # - rds.mysql.st.h43	60 cores, 470 GB (dedicated physical machine)
        # - rds.mysql.st.v52	90 cores, 720 GB (dedicated physical machine).
        self.dn_class = dn_class
        # The target disk size for the specification change.
        # 
        # - If the instance uses a fixed-size disk, the disk cannot be changed. In this case, do not specify DnStorageSpace.
        # - Valid values of DnStorageSpace: [20, 3072].
        self.dn_storage_space = dn_storage_space
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # Specifies whether to change specifications for multiple DNs.
        self.specified_dnscale = specified_dnscale
        # The target specifications for each DN when changing specifications for multiple DNs.
        self.specified_dnspec_map_json = specified_dnspec_map_json
        # The start time of the switch. The switch time range is [start time T, T+30m]. This parameter is not yet available.
        self.switch_time = switch_time
        # The switch time. Valid values:
        # - 0: immediately
        # - 1: within the O&M window.
        self.switch_time_mode = switch_time_mode
        # **Target specifications for Standard Edition specification changes**
        # 
        # **Primary instance node specifications (for Standard Edition) (general-purpose):**
        # - mysql.n2.medium.25	2 cores, 4 GB (general-purpose)
        # - mysql.n4.medium.25	2 cores, 8 GB (general-purpose)
        # - mysql.n8.medium.25	2 cores, 16 GB (general-purpose)
        # - mysql.n2.large.25	4 cores, 8 GB (general-purpose)
        # - mysql.n4.large.25	4 cores, 16 GB (general-purpose)
        # - mysql.n8.large.25	4 cores, 32 GB (general-purpose)
        # - mysql.n2.xlarge.25	8 cores, 16 GB (general-purpose)
        # - mysql.n4.xlarge.25	8 cores, 32 GB (general-purpose)
        # - mysql.n8.xlarge.25	8 cores, 64 GB (general-purpose)
        # - mysql.n2.2xlarge.25	16 cores, 32 GB (general-purpose)
        # - mysql.n4.2xlarge.25	16 cores, 64 GB (general-purpose)
        # - mysql.n8.2xlarge.25	16 cores, 128 GB (general-purpose)
        # 
        # **Primary instance node specifications (for Standard Edition) (dedicated):**
        # - mysql.x2.medium.25	2 cores, 4 GB (dedicated)
        # - mysql.x4.medium.25	2 cores, 8 GB (dedicated)
        # - mysql.x8.medium.25	2 cores, 16 GB (dedicated)
        # - mysql.x2.large.25	4 cores, 8 GB (dedicated)
        # - mysql.x4.large.25	4 cores, 16 GB (dedicated)
        # - mysql.x8.large.25	4 cores, 32 GB (dedicated)
        # - mysql.x2.xlarge.25	8 cores, 16 GB (dedicated)
        # - mysql.x4.xlarge.25	8 cores, 32 GB (dedicated)
        # - mysql.x8.xlarge.25	8 cores, 64 GB (dedicated)
        # - mysql.x2.2xlarge.25	16 cores, 32 GB (dedicated)
        # - mysql.x4.2xlarge.25	16 cores, 64 GB (dedicated)
        # - mysql.x8.2xlarge.25	16 cores, 128 GB (dedicated)
        # 
        # **Read-only instance node specifications (for Standard Edition) general-purpose**	
        # 
        # - rds.mysql.s2.xlarge 	2 cores, 8 GB (general-purpose)
        # - mysqlro.x4.large.1 	4 cores, 16 GB (general-purpose)
        # - mysqlro.x4.xlarge.1 	8 cores, 32 GB (general-purpose)
        # - mysqlro.x4.2xlarge.1 	16 cores, 64 GB (general-purpose) 
        # 
        # **Read-only instance node specifications (for Standard Edition) dedicated**	
        # 
        # - mysqlro.x8.large.1 	4 cores, 32 GB (dedicated) 
        # - mysqlro.x8.xlarge.1 	8 cores, 64 GB (dedicated) 
        # - mysqlro.x8.2xlarge.1 	16 cores, 128 GB (dedicated) 
        # - mysqlro.x4.4xlarge.1 	32 cores, 128 GB (dedicated) 
        # - mysqlro.x8.4xlarge.1	32 cores, 256 GB (dedicated).
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

