# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDBInstanceClassRequest(DaraModel):
    def __init__(
        self,
        align_storage_primary_azone: bool = None,
        client_token: str = None,
        cn_class: str = None,
        dbinstance_name: str = None,
        dn_class: str = None,
        dn_storage_space: str = None,
        region_id: str = None,
        specified_dnscale: bool = None,
        specified_dnspec_map_json: str = None,
        storage_type: str = None,
        switch_time: str = None,
        switch_time_mode: str = None,
        target_dbinstance_class: str = None,
    ):
        self.align_storage_primary_azone = align_storage_primary_azone
        # The client token. It is an arbitrary unique string used to ensure the idempotence of the request.
        self.client_token = client_token
        # **Target specifications for Enterprise Edition compute nodes**
        # 
        # **Primary instance compute node specifications (Enterprise Edition CN) (General-purpose)**	
        # - polarx.x4.medium.2e 2 vCPUs, 8 GB (General-purpose)
        # - polarx.x4.large.2e 4 vCPUs, 16 GB (General-purpose)
        # - polarx.x4.xlarge.2e 8 vCPUs, 32 GB (General-purpose)
        # - polarx.x4.2xlarge.2e 16 vCPUs, 64 GB (General-purpose)
        # 
        # **Primary instance compute node specifications (Enterprise Edition CN) (Dedicated)**	
        # - polarx.x8.large.2e 4 vCPUs, 32 GB (Dedicated)
        # - polarx.x8.xlarge.2e 8 vCPUs, 64 GB (Dedicated)
        # - polarx.x8.2xlarge.2e 16 vCPUs, 128 GB (Dedicated)
        # - polarx.x4.4xlarge.2e 32 vCPUs, 128 GB (Dedicated)
        # - polarx.x8.4xlarge.2e 32 vCPUs, 256 GB (Dedicated)
        # - polarx.st.8xlarge.2e 60 vCPUs, 470 GB (Dedicated)
        # - polarx.st.12xlarge.2e 90 vCPUs, 720 GB (Dedicated)
        # 
        # **Read-only instance compute node specifications (Enterprise Edition CN) (General-purpose)**	
        # 
        # - polarxro.x4.medium.2e 2 vCPUs, 8 GB (General-purpose)
        # - polarxro.x4.large.2e 4 vCPUs, 16 GB (General-purpose)
        # - polarxro.x4.xlarge.2e 8 vCPUs, 32 GB (General-purpose)
        # - polarxro.x4.2xlarge.2e 16 vCPUs, 64 GB (General-purpose)
        # 
        # **Read-only instance compute node specifications (Enterprise Edition CN) (Dedicated)**	
        # 
        # - polarxro.x8.large.2e 4 vCPUs, 32 GB (Dedicated)
        # - polarxro.x8.xlarge.2e 8 vCPUs, 64 GB (Dedicated)
        # - polarxro.x8.2xlarge.2e 16 vCPUs, 128 GB (Dedicated)
        # - polarxro.x4.4xlarge.2e 32 vCPUs, 128 GB (Dedicated)
        # - polarxro.x8.4xlarge.2e 32 vCPUs, 256 GB (Dedicated)
        # - polarxro.st.8xlarge.2e 60 vCPUs, 470 GB (Dedicated physical host)
        # - polarxro.st.12xlarge.2e 90 vCPUs, 720 GB (Dedicated physical host)
        self.cn_class = cn_class
        # The instance ID.
        # 
        # This parameter is required.
        self.dbinstance_name = dbinstance_name
        # **Target specifications for Enterprise Edition storage nodes**
        # 
        # **Storage node specifications (Enterprise Edition DN) (General-purpose)**	
        # 
        # - mysql.n4.medium.25 2 vCPUs, 8 GB (General-purpose)
        # - mysql.n4.large.25 4 vCPUs, 16 GB (General-purpose)
        # - mysql.n4.xlarge.25 8 vCPUs, 32 GB (General-purpose)
        # - mysql.n4.2xlarge.25 16 vCPUs, 64 GB (General-purpose)
        # 
        # **Storage node specifications (Enterprise Edition DN) (Dedicated)**	
        # 
        # - mysql.x8.large.25 4 vCPUs, 32 GB (Dedicated)
        # - mysql.x8.xlarge.25 8 vCPUs, 64 GB (Dedicated)
        # - mysql.x8.2xlarge.25 16 vCPUs, 128 GB (Dedicated)
        # - mysql.x4.4xlarge.25 32 vCPUs, 128 GB (Dedicated)
        # - mysql.x8.4xlarge.25 32 vCPUs, 256 GB (Dedicated)
        # - mysql.st.8xlarge.25 60 vCPUs, 470 GB (Dedicated)
        # - mysql.st.12xlarge.25 90 vCPUs, 720 GB (Dedicated)
        # 
        # **Read-only instance storage node specifications (Enterprise Edition DN) (General-purpose)**	
        # 
        # - rds.mysql.s2.xlarge 2 vCPUs, 8 GB (General-purpose)
        # - mysqlro.x4.large.1 4 vCPUs, 16 GB (General-purpose)
        # - mysqlro.x4.xlarge.1 8 vCPUs, 32 GB (General-purpose)
        # - mysqlro.x4.2xlarge.1 16 vCPUs, 64 GB (General-purpose)
        # 
        # **Read-only instance storage node specifications (Enterprise Edition DN) (Dedicated)**	
        # 
        # - mysqlro.x8.large.1 4 vCPUs, 32 GB (Dedicated)
        # - mysqlro.x8.xlarge.1 8 vCPUs, 64 GB (Dedicated)
        # - mysqlro.x8.2xlarge.1 16 vCPUs, 128 GB (Dedicated)
        # - mysqlro.x4.4xlarge.1 32 vCPUs, 128 GB (Dedicated)
        # - mysqlro.x8.4xlarge.1 32 vCPUs, 256 GB (Dedicated)
        # - rds.mysql.st.h43 60 vCPUs, 470 GB (Dedicated physical host)
        # - rds.mysql.st.v52 90 vCPUs, 720 GB (Dedicated physical host)
        self.dn_class = dn_class
        # The target cloud disk size after the specification change.
        # 
        # - If the instance uses a fixed-size cloud disk, you cannot change the cloud disk size. In this case, do not specify DnStorageSpace.
        # - Valid values of DnStorageSpace: 20 to 3072.
        self.dn_storage_space = dn_storage_space
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # Specifies whether to change the DN nodes to different specifications.
        self.specified_dnscale = specified_dnscale
        # The target specification for each DN node when DN nodes are changed to different specifications.
        self.specified_dnspec_map_json = specified_dnspec_map_json
        # The target storage type.
        self.storage_type = storage_type
        # The start time of the switchover. The switchover is performed within the period from the start time T to T+30 minutes. This parameter is not available.
        self.switch_time = switch_time
        # The switching time. Valid values:
        # - 0: Immediately.
        # - 1: Within the O&M window.
        self.switch_time_mode = switch_time_mode
        # **Target specifications for Standard Edition**
        # 
        # **Primary instance node specifications (Standard Edition) (General-purpose):**
        # - mysql.n2.medium.25 2 vCPUs, 4 GB (General-purpose)
        # - mysql.n4.medium.25 2 vCPUs, 8 GB (General-purpose)
        # - mysql.n8.medium.25 2 vCPUs, 16 GB (General-purpose)
        # - mysql.n2.large.25 4 vCPUs, 8 GB (General-purpose)
        # - mysql.n4.large.25 4 vCPUs, 16 GB (General-purpose)
        # - mysql.n8.large.25 4 vCPUs, 32 GB (General-purpose)
        # - mysql.n2.xlarge.25 8 vCPUs, 16 GB (General-purpose)
        # - mysql.n4.xlarge.25 8 vCPUs, 32 GB (General-purpose)
        # - mysql.n8.xlarge.25 8 vCPUs, 64 GB (General-purpose)
        # - mysql.n2.2xlarge.25 16 vCPUs, 32 GB (General-purpose)
        # - mysql.n4.2xlarge.25 16 vCPUs, 64 GB (General-purpose)
        # - mysql.n8.2xlarge.25 16 vCPUs, 128 GB (General-purpose)
        # 
        # **Primary instance node specifications (Standard Edition) (Dedicated):**
        # - mysql.x2.medium.25 2 vCPUs, 4 GB (Dedicated)
        # - mysql.x4.medium.25 2 vCPUs, 8 GB (Dedicated)
        # - mysql.x8.medium.25 2 vCPUs, 16 GB (Dedicated)
        # - mysql.x2.large.25 4 vCPUs, 8 GB (Dedicated)
        # - mysql.x4.large.25 4 vCPUs, 16 GB (Dedicated)
        # - mysql.x8.large.25 4 vCPUs, 32 GB (Dedicated)
        # - mysql.x2.xlarge.25 8 vCPUs, 16 GB (Dedicated)
        # - mysql.x4.xlarge.25 8 vCPUs, 32 GB (Dedicated)
        # - mysql.x8.xlarge.25 8 vCPUs, 64 GB (Dedicated)
        # - mysql.x2.2xlarge.25 16 vCPUs, 32 GB (Dedicated)
        # - mysql.x4.2xlarge.25 16 vCPUs, 64 GB (Dedicated)
        # - mysql.x8.2xlarge.25 16 vCPUs, 128 GB (Dedicated)
        # 
        # **Read-only instance node specifications (Standard Edition) (General-purpose)**	
        # 
        # - rds.mysql.s2.xlarge 2 vCPUs, 8 GB (General-purpose)
        # - mysqlro.x4.large.1 4 vCPUs, 16 GB (General-purpose)
        # - mysqlro.x4.xlarge.1 8 vCPUs, 32 GB (General-purpose)
        # - mysqlro.x4.2xlarge.1 16 vCPUs, 64 GB (General-purpose) 
        # 
        # **Read-only instance node specifications (Standard Edition) (Dedicated)**	
        # 
        # - mysqlro.x8.large.1 4 vCPUs, 32 GB (Dedicated) 
        # - mysqlro.x8.xlarge.1 8 vCPUs, 64 GB (Dedicated) 
        # - mysqlro.x8.2xlarge.1 16 vCPUs, 128 GB (Dedicated) 
        # - mysqlro.x4.4xlarge.1 32 vCPUs, 128 GB (Dedicated) 
        # - mysqlro.x8.4xlarge.1 32 vCPUs, 256 GB (Dedicated)
        self.target_dbinstance_class = target_dbinstance_class

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.align_storage_primary_azone is not None:
            result['AlignStoragePrimaryAzone'] = self.align_storage_primary_azone

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

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        if self.switch_time is not None:
            result['SwitchTime'] = self.switch_time

        if self.switch_time_mode is not None:
            result['SwitchTimeMode'] = self.switch_time_mode

        if self.target_dbinstance_class is not None:
            result['TargetDBInstanceClass'] = self.target_dbinstance_class

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlignStoragePrimaryAzone') is not None:
            self.align_storage_primary_azone = m.get('AlignStoragePrimaryAzone')

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

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        if m.get('SwitchTime') is not None:
            self.switch_time = m.get('SwitchTime')

        if m.get('SwitchTimeMode') is not None:
            self.switch_time_mode = m.get('SwitchTimeMode')

        if m.get('TargetDBInstanceClass') is not None:
            self.target_dbinstance_class = m.get('TargetDBInstanceClass')

        return self

