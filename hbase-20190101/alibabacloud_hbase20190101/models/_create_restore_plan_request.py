# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateRestorePlanRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        restore_all_table: bool = None,
        restore_by_copy: bool = None,
        restore_to_date: str = None,
        tables: str = None,
        target_cluster_id: str = None,
    ):
        # The ID of the ApsaraDB for HBase Performance-enhanced Edition cluster.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # Specifies whether to restore all tables. Valid values:
        # 
        # - **true**: Restores all tables in the ApsaraDB for HBase Performance-enhanced Edition cluster.
        # - **false**: Does not restore all tables in the ApsaraDB for HBase Performance-enhanced Edition cluster.
        # 
        # > If this parameter is set to **true**, the **Tables** parameter is invalid. If this parameter is set to **false**, the **Tables** parameter is required.
        # 
        # This parameter is required.
        self.restore_all_table = restore_all_table
        # Specifies whether to restore data by using the copy method. Set the value to **true**.
        # 
        # This parameter is required.
        self.restore_by_copy = restore_by_copy
        # The point in time to which you want to restore data. The point in time must be within the recoverable time range. You can call the [DescribeRecoverableTimeRange](https://help.aliyun.com/document_detail/188365.html) operation to query the recoverable time range.
        # 
        # This parameter is required.
        self.restore_to_date = restore_to_date
        # The table names. Specify one table name per line. Wildcards (*) are not supported.
        # 
        # - To restore to the current table, use the format: `namespace:table`. Example: `default:testTable`.
        # - To restore to a different table, use the format: `namespace:table/namespace:table2`. Example: `default:testTable/default:testTable2`.
        self.tables = tables
        # The ID of the ApsaraDB for HBase Performance-enhanced Edition cluster to which data is restored. You can also restore data to the cluster that is currently backed up.
        # 
        # > The specified ApsaraDB for HBase Performance-enhanced Edition cluster and the backed-up ApsaraDB for HBase Performance-enhanced Edition cluster must meet the following requirements:<ul>
        # <li>They are of the same version.</li>
        # <li>They are in the same region.</li>
        # <li>They are associated with the BDS cluster.</li></ul>.
        # 
        # This parameter is required.
        self.target_cluster_id = target_cluster_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.restore_all_table is not None:
            result['RestoreAllTable'] = self.restore_all_table

        if self.restore_by_copy is not None:
            result['RestoreByCopy'] = self.restore_by_copy

        if self.restore_to_date is not None:
            result['RestoreToDate'] = self.restore_to_date

        if self.tables is not None:
            result['Tables'] = self.tables

        if self.target_cluster_id is not None:
            result['TargetClusterId'] = self.target_cluster_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('RestoreAllTable') is not None:
            self.restore_all_table = m.get('RestoreAllTable')

        if m.get('RestoreByCopy') is not None:
            self.restore_by_copy = m.get('RestoreByCopy')

        if m.get('RestoreToDate') is not None:
            self.restore_to_date = m.get('RestoreToDate')

        if m.get('Tables') is not None:
            self.tables = m.get('Tables')

        if m.get('TargetClusterId') is not None:
            self.target_cluster_id = m.get('TargetClusterId')

        return self

