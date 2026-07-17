# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpgradeLindormInstanceRequest(DaraModel):
    def __init__(
        self,
        cluster_storage: int = None,
        cold_storage: int = None,
        core_single_storage: int = None,
        filestore_num: int = None,
        filestore_spec: str = None,
        instance_id: str = None,
        lindorm_num: int = None,
        lindorm_spec: str = None,
        log_num: int = None,
        log_single_storage: int = None,
        log_spec: str = None,
        lts_core_num: int = None,
        lts_core_spec: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
        solr_num: int = None,
        solr_spec: str = None,
        stream_num: int = None,
        stream_spec: str = None,
        tsdb_num: int = None,
        tsdb_spec: str = None,
        upgrade_type: str = None,
        zone_id: str = None,
    ):
        # The new storage capacity of the instance. Unit: GB. Valid values: **480** to **1017600**.
        self.cluster_storage = cluster_storage
        # The new cold storage capacity of the instance. Unit: GB. Valid values: **800** to **1000000**.
        self.cold_storage = cold_storage
        # The new storage capacity of a single core node in a multi-zone instance. Unit: GB. Valid values: 400 to 64000. **This parameter is optional.**
        self.core_single_storage = core_single_storage
        # The new number of file engine nodes. Valid values: **0** to **60**.
        self.filestore_num = filestore_num
        # The new specification of the file engine nodes. Valid value:
        # 
        # **lindorm.c.xlarge**: 4 CPU cores, 8 GB of memory (standard specification).
        self.filestore_spec = filestore_spec
        # The ID of the instance. You can call the [GetLindormInstanceList](https://help.aliyun.com/document_detail/426069.html) operation to obtain this ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The new number of wide table engine nodes. Valid values: **0** to **90**.
        # 
        # > If you specify this parameter, the LindormSpec parameter is also required.
        self.lindorm_num = lindorm_num
        # The new specification of the wide table engine nodes. Valid values:
        # 
        # - **lindorm.c.xlarge**: 4 CPU cores, 8 GB of memory (dedicated specification).
        # 
        # - **lindorm.c.2xlarge**: 8 CPU cores, 16 GB of memory (dedicated specification).
        # 
        # - **lindorm.c.4xlarge**: 16 CPU cores, 32 GB of memory (dedicated specification).
        # 
        # - **lindorm.c.8xlarge**: 32 CPU cores, 64 GB of memory (dedicated specification).
        self.lindorm_spec = lindorm_spec
        # The new number of log nodes for a multi-zone instance. Valid values: 4 to 400. **This parameter is optional.**
        self.log_num = log_num
        # The new disk capacity of a single log node for a multi-zone instance. Unit: GB. Valid values: 400 to 64000. **This parameter is optional.**
        self.log_single_storage = log_single_storage
        # The new specification of the log nodes for a multi-zone instance. Valid values:
        # 
        # - **lindorm.sn1.large**: 4 CPU cores, 8 GB of memory (dedicated specification).
        # 
        # - **lindorm.sn1.2xlarge**: 8 CPU cores, 16 GB of memory (dedicated specification).
        # 
        # **This parameter is optional.**
        self.log_spec = log_spec
        # The new number of LTS nodes. Valid values: **0** to **50**.
        self.lts_core_num = lts_core_num
        # The new specification of the LTS nodes. Valid values:
        # 
        # - **lindorm.g.xlarge**: 4 CPU cores, 16 GB of memory (dedicated specification).
        # 
        # - **lindorm.g.2xlarge**: 8 CPU cores, 32 GB of memory (dedicated specification).
        self.lts_core_spec = lts_core_spec
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the region where the instance is located. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/426062.html) operation to obtain the latest region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token
        # The new number of search engine nodes. Valid values: **0** to **60**.
        self.solr_num = solr_num
        # The new specification of the search engine nodes. Valid values:
        # 
        # - **lindorm.g.xlarge**: 4 CPU cores, 16 GB of memory (dedicated specification).
        # 
        # - **lindorm.g.2xlarge**: 8 CPU cores, 32 GB of memory (dedicated specification).
        # 
        # - **lindorm.g.4xlarge**: 16 CPU cores, 64 GB of memory (dedicated specification).
        # 
        # - **lindorm.g.8xlarg**e: 32 CPU cores, 128 GB of memory (dedicated specification).
        self.solr_spec = solr_spec
        # The new number of stream engine nodes. Valid values: **0** to **90**.
        self.stream_num = stream_num
        # The new specification of the stream engine nodes. Valid values:
        # 
        # - **lindorm.c.2xlarge**: 8 CPU cores, 16 GB of memory (dedicated specification).
        # 
        # - **lindorm.c.4xlarge**: 16 CPU cores, 32 GB of memory (dedicated specification).
        # 
        # - **lindorm.c.8xlarge**: 32 CPU cores, 64 GB of memory (dedicated specification).
        self.stream_spec = stream_spec
        # The new number of time series engine nodes. Valid values: **0** to **24**.
        self.tsdb_num = tsdb_num
        # The new specification of the time series engine nodes. Valid values:
        # 
        # - **lindorm.g.xlarge**: 4 CPU cores, 16 GB of memory (dedicated specification).
        # 
        # - **lindorm.g.2xlarge**: 8 CPU cores, 32 GB of memory (dedicated specification).
        # 
        # - **lindorm.g.4xlarge**: 16 CPU cores, 64 GB of memory (dedicated specification).
        # 
        # - **lindorm.g.8xlarge**: 32 CPU cores, 128 GB of memory (dedicated specification).
        self.tsdb_spec = tsdb_spec
        # The type of the upgrade. For details about the supported types, see the description of the UpgradeType parameter in the "Additional information about request parameters" section.
        # 
        # This parameter is required.
        self.upgrade_type = upgrade_type
        # The ID of the availability zone. You can call the [GetLindormInstance](https://help.aliyun.com/document_detail/426067.html) operation to obtain this ID.
        # 
        # This parameter is required.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_storage is not None:
            result['ClusterStorage'] = self.cluster_storage

        if self.cold_storage is not None:
            result['ColdStorage'] = self.cold_storage

        if self.core_single_storage is not None:
            result['CoreSingleStorage'] = self.core_single_storage

        if self.filestore_num is not None:
            result['FilestoreNum'] = self.filestore_num

        if self.filestore_spec is not None:
            result['FilestoreSpec'] = self.filestore_spec

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.lindorm_num is not None:
            result['LindormNum'] = self.lindorm_num

        if self.lindorm_spec is not None:
            result['LindormSpec'] = self.lindorm_spec

        if self.log_num is not None:
            result['LogNum'] = self.log_num

        if self.log_single_storage is not None:
            result['LogSingleStorage'] = self.log_single_storage

        if self.log_spec is not None:
            result['LogSpec'] = self.log_spec

        if self.lts_core_num is not None:
            result['LtsCoreNum'] = self.lts_core_num

        if self.lts_core_spec is not None:
            result['LtsCoreSpec'] = self.lts_core_spec

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.solr_num is not None:
            result['SolrNum'] = self.solr_num

        if self.solr_spec is not None:
            result['SolrSpec'] = self.solr_spec

        if self.stream_num is not None:
            result['StreamNum'] = self.stream_num

        if self.stream_spec is not None:
            result['StreamSpec'] = self.stream_spec

        if self.tsdb_num is not None:
            result['TsdbNum'] = self.tsdb_num

        if self.tsdb_spec is not None:
            result['TsdbSpec'] = self.tsdb_spec

        if self.upgrade_type is not None:
            result['UpgradeType'] = self.upgrade_type

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterStorage') is not None:
            self.cluster_storage = m.get('ClusterStorage')

        if m.get('ColdStorage') is not None:
            self.cold_storage = m.get('ColdStorage')

        if m.get('CoreSingleStorage') is not None:
            self.core_single_storage = m.get('CoreSingleStorage')

        if m.get('FilestoreNum') is not None:
            self.filestore_num = m.get('FilestoreNum')

        if m.get('FilestoreSpec') is not None:
            self.filestore_spec = m.get('FilestoreSpec')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LindormNum') is not None:
            self.lindorm_num = m.get('LindormNum')

        if m.get('LindormSpec') is not None:
            self.lindorm_spec = m.get('LindormSpec')

        if m.get('LogNum') is not None:
            self.log_num = m.get('LogNum')

        if m.get('LogSingleStorage') is not None:
            self.log_single_storage = m.get('LogSingleStorage')

        if m.get('LogSpec') is not None:
            self.log_spec = m.get('LogSpec')

        if m.get('LtsCoreNum') is not None:
            self.lts_core_num = m.get('LtsCoreNum')

        if m.get('LtsCoreSpec') is not None:
            self.lts_core_spec = m.get('LtsCoreSpec')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('SolrNum') is not None:
            self.solr_num = m.get('SolrNum')

        if m.get('SolrSpec') is not None:
            self.solr_spec = m.get('SolrSpec')

        if m.get('StreamNum') is not None:
            self.stream_num = m.get('StreamNum')

        if m.get('StreamSpec') is not None:
            self.stream_spec = m.get('StreamSpec')

        if m.get('TsdbNum') is not None:
            self.tsdb_num = m.get('TsdbNum')

        if m.get('TsdbSpec') is not None:
            self.tsdb_spec = m.get('TsdbSpec')

        if m.get('UpgradeType') is not None:
            self.upgrade_type = m.get('UpgradeType')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

