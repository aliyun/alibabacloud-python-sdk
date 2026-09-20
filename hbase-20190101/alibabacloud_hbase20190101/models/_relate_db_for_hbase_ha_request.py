# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RelateDbForHBaseHaRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        ha_active: str = None,
        ha_active_cluster_key: str = None,
        ha_active_dbtype: str = None,
        ha_active_hbase_fs_dir: str = None,
        ha_active_hdfs_uri: str = None,
        ha_active_password: str = None,
        ha_active_user: str = None,
        ha_active_version: str = None,
        ha_migrate_type: str = None,
        ha_standby: str = None,
        ha_standby_cluster_key: str = None,
        ha_standby_dbtype: str = None,
        ha_standby_hbase_fs_dir: str = None,
        ha_standby_hdfs_uri: str = None,
        ha_standby_password: str = None,
        ha_standby_user: str = None,
        ha_standby_version: str = None,
        ha_tables: str = None,
        is_active_standard: bool = None,
        is_standby_standard: bool = None,
    ):
        # The ID of the BDS cluster. You can call the [DescribeInstances](https://help.aliyun.com/document_detail/144595.html) operation to obtain the cluster ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The instance ID of the primary instance.
        # 
        # This parameter is required.
        self.ha_active = ha_active
        # The ZooKeeper address of the primary instance. This parameter is required when the primary instance is a non-standard instance (IsActiveStandard is set to false).
        self.ha_active_cluster_key = ha_active_cluster_key
        # The cluster type of the primary instance. Valid values: **HBase** and **HBaseue**.
        # 
        # This parameter is required.
        self.ha_active_dbtype = ha_active_dbtype
        # The HDFS directory of the primary instance. This parameter is required when the primary instance is a non-standard instance (IsActiveStandard is set to false).
        self.ha_active_hbase_fs_dir = ha_active_hbase_fs_dir
        # The HDFS URI of the primary instance. This parameter is required when the primary instance is a non-standard instance (IsActiveStandard is set to false).
        self.ha_active_hdfs_uri = ha_active_hdfs_uri
        # The password that corresponds to the username of the primary instance. This parameter is required when the primary instance is **HBaseue**.
        self.ha_active_password = ha_active_password
        # The username of the primary instance. This parameter is required when the primary instance is **HBaseue**.
        self.ha_active_user = ha_active_user
        # The database engine version of the primary instance. This parameter is required when the primary instance is a non-standard instance (IsActiveStandard is set to false). Valid values:
        # - **HBase1x**: HBase 1.x.
        # - **HBase2x**: HBase 2.x.
        # - **HBaseUE**: HBaseue.
        self.ha_active_version = ha_active_version
        # The synchronization type. Valid values:
        # - **CLUSTER**: instance-level synchronization.
        # - **TABLE**: table-level synchronization.
        # - **SKIP**: no synchronization required.
        # 
        # This parameter is required.
        self.ha_migrate_type = ha_migrate_type
        # The ID of the secondary instance cluster.
        # 
        # This parameter is required.
        self.ha_standby = ha_standby
        # The ZooKeeper address of the secondary instance. This parameter is required when the secondary instance is a non-standard instance (IsStandbyStandard is set to false).
        self.ha_standby_cluster_key = ha_standby_cluster_key
        # The cluster type of the secondary instance. Valid values: **HBase** and **HBaseue**.
        # 
        # This parameter is required.
        self.ha_standby_dbtype = ha_standby_dbtype
        # The HDFS directory of the secondary instance. This parameter is required when the secondary instance is a non-standard instance (IsStandbyStandard is set to false).
        self.ha_standby_hbase_fs_dir = ha_standby_hbase_fs_dir
        # The HDFS URI of the secondary instance. This parameter is required when the secondary instance is a non-standard instance (IsStandbyStandard is set to false).
        self.ha_standby_hdfs_uri = ha_standby_hdfs_uri
        # The password that corresponds to the username of the secondary instance. This parameter is required when the secondary instance is **hbaseue**.
        self.ha_standby_password = ha_standby_password
        # The username of the secondary instance. This parameter is required when the secondary instance is **hbaseue**.
        self.ha_standby_user = ha_standby_user
        # The database engine version of the secondary instance. This parameter is required when the secondary instance is a non-standard instance (IsStandbyStandard is set to false). Valid values:
        # - **HBase1x**: HBase 1.x.
        # - **HBase2x**: HBase 2.x.
        # - **HBaseUE**: HBaseue.
        self.ha_standby_version = ha_standby_version
        # The tables to synchronize. This parameter is required when HaMigrateType is set to TABLE. Separate multiple tables with commas (,).
        self.ha_tables = ha_tables
        # Specifies whether the primary instance is a standard instance. Set this parameter to **true** for a standard instance.
        # 
        # This parameter is required.
        self.is_active_standard = is_active_standard
        # Specifies whether the secondary instance is a standard instance. Set this parameter to **true** for a standard instance.
        # 
        # This parameter is required.
        self.is_standby_standard = is_standby_standard

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.ha_active is not None:
            result['HaActive'] = self.ha_active

        if self.ha_active_cluster_key is not None:
            result['HaActiveClusterKey'] = self.ha_active_cluster_key

        if self.ha_active_dbtype is not None:
            result['HaActiveDBType'] = self.ha_active_dbtype

        if self.ha_active_hbase_fs_dir is not None:
            result['HaActiveHbaseFsDir'] = self.ha_active_hbase_fs_dir

        if self.ha_active_hdfs_uri is not None:
            result['HaActiveHdfsUri'] = self.ha_active_hdfs_uri

        if self.ha_active_password is not None:
            result['HaActivePassword'] = self.ha_active_password

        if self.ha_active_user is not None:
            result['HaActiveUser'] = self.ha_active_user

        if self.ha_active_version is not None:
            result['HaActiveVersion'] = self.ha_active_version

        if self.ha_migrate_type is not None:
            result['HaMigrateType'] = self.ha_migrate_type

        if self.ha_standby is not None:
            result['HaStandby'] = self.ha_standby

        if self.ha_standby_cluster_key is not None:
            result['HaStandbyClusterKey'] = self.ha_standby_cluster_key

        if self.ha_standby_dbtype is not None:
            result['HaStandbyDBType'] = self.ha_standby_dbtype

        if self.ha_standby_hbase_fs_dir is not None:
            result['HaStandbyHbaseFsDir'] = self.ha_standby_hbase_fs_dir

        if self.ha_standby_hdfs_uri is not None:
            result['HaStandbyHdfsUri'] = self.ha_standby_hdfs_uri

        if self.ha_standby_password is not None:
            result['HaStandbyPassword'] = self.ha_standby_password

        if self.ha_standby_user is not None:
            result['HaStandbyUser'] = self.ha_standby_user

        if self.ha_standby_version is not None:
            result['HaStandbyVersion'] = self.ha_standby_version

        if self.ha_tables is not None:
            result['HaTables'] = self.ha_tables

        if self.is_active_standard is not None:
            result['IsActiveStandard'] = self.is_active_standard

        if self.is_standby_standard is not None:
            result['IsStandbyStandard'] = self.is_standby_standard

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('HaActive') is not None:
            self.ha_active = m.get('HaActive')

        if m.get('HaActiveClusterKey') is not None:
            self.ha_active_cluster_key = m.get('HaActiveClusterKey')

        if m.get('HaActiveDBType') is not None:
            self.ha_active_dbtype = m.get('HaActiveDBType')

        if m.get('HaActiveHbaseFsDir') is not None:
            self.ha_active_hbase_fs_dir = m.get('HaActiveHbaseFsDir')

        if m.get('HaActiveHdfsUri') is not None:
            self.ha_active_hdfs_uri = m.get('HaActiveHdfsUri')

        if m.get('HaActivePassword') is not None:
            self.ha_active_password = m.get('HaActivePassword')

        if m.get('HaActiveUser') is not None:
            self.ha_active_user = m.get('HaActiveUser')

        if m.get('HaActiveVersion') is not None:
            self.ha_active_version = m.get('HaActiveVersion')

        if m.get('HaMigrateType') is not None:
            self.ha_migrate_type = m.get('HaMigrateType')

        if m.get('HaStandby') is not None:
            self.ha_standby = m.get('HaStandby')

        if m.get('HaStandbyClusterKey') is not None:
            self.ha_standby_cluster_key = m.get('HaStandbyClusterKey')

        if m.get('HaStandbyDBType') is not None:
            self.ha_standby_dbtype = m.get('HaStandbyDBType')

        if m.get('HaStandbyHbaseFsDir') is not None:
            self.ha_standby_hbase_fs_dir = m.get('HaStandbyHbaseFsDir')

        if m.get('HaStandbyHdfsUri') is not None:
            self.ha_standby_hdfs_uri = m.get('HaStandbyHdfsUri')

        if m.get('HaStandbyPassword') is not None:
            self.ha_standby_password = m.get('HaStandbyPassword')

        if m.get('HaStandbyUser') is not None:
            self.ha_standby_user = m.get('HaStandbyUser')

        if m.get('HaStandbyVersion') is not None:
            self.ha_standby_version = m.get('HaStandbyVersion')

        if m.get('HaTables') is not None:
            self.ha_tables = m.get('HaTables')

        if m.get('IsActiveStandard') is not None:
            self.is_active_standard = m.get('IsActiveStandard')

        if m.get('IsStandbyStandard') is not None:
            self.is_standby_standard = m.get('IsStandbyStandard')

        return self

