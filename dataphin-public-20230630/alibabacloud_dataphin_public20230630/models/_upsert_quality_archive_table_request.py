# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class UpsertQualityArchiveTableRequest(DaraModel):
    def __init__(
        self,
        op_tenant_id: int = None,
        op_user_id: str = None,
        upsert_command: main_models.UpsertQualityArchiveTableRequestUpsertCommand = None,
    ):
        # The tenant ID.
        # 
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # The ID of the operator.
        self.op_user_id = op_user_id
        # The upsert command.
        # 
        # This parameter is required.
        self.upsert_command = upsert_command

    def validate(self):
        if self.upsert_command:
            self.upsert_command.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.op_user_id is not None:
            result['OpUserId'] = self.op_user_id

        if self.upsert_command is not None:
            result['UpsertCommand'] = self.upsert_command.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('OpUserId') is not None:
            self.op_user_id = m.get('OpUserId')

        if m.get('UpsertCommand') is not None:
            temp_model = main_models.UpsertQualityArchiveTableRequestUpsertCommand()
            self.upsert_command = temp_model.from_map(m.get('UpsertCommand'))

        return self

class UpsertQualityArchiveTableRequestUpsertCommand(DaraModel):
    def __init__(
        self,
        add_mode: str = None,
        archive_table_id: int = None,
        exist_table_name: str = None,
        lifecycle: int = None,
        max_archive_count: int = None,
        new_table_name_prefix: str = None,
        set_active: bool = None,
        watch_id: int = None,
    ):
        # The mode for adding the archived table. Valid values:
        # 
        # - CREATE_NEW_TABLE: creates a new table.
        # - BIND_EXIST_TABLE: binds an existing table.
        self.add_mode = add_mode
        # The ID of the archived table. If this parameter is specified, the operation runs in update mode, and you cannot specify AddMode or NewTableNamePrefix. If this parameter is not specified, the operation runs in create mode.
        self.archive_table_id = archive_table_id
        # The name of the existing table. This parameter is required when AddMode is set to BIND_EXIST_TABLE. For Dataphin tables, use the format "project_name.table_name" (for example, dataphin03.ads_region_order_summary). For datasource tables, use the format "database/schema.table_name" (for example, order_db.order_exception_data). The table must belong to the same project or datasource as the monitored object, and the table schema must contain system fields with the dataphin_quality_ prefix.
        self.exist_table_name = exist_table_name
        # The lifecycle of the table, in days. The value must be a positive integer. If this parameter is not specified, no lifecycle is set. This parameter is valid only when creating a new table or in edit pattern, and only when the table belongs to MaxCompute, Hadoop series, or Hive. This parameter cannot be specified when AddMode is set to BIND_EXIST_TABLE.
        self.lifecycle = lifecycle
        # The maximum number of archived rows. A positive integer specifies the limit on the number of archived rows. The console provides options of 10,000, 100,000, and 500,000. A value of -1 indicates full archiving. Default value: 10000. This parameter is supported only for MaxCompute, Hadoop series, or Hive.
        self.max_archive_count = max_archive_count
        # The table name prefix for the new archived table. This parameter is required when AddMode is set to CREATE_NEW_TABLE. The system automatically appends the _exception_data suffix. For example, if you specify vip_user_tips112, the actual table name is vip_user_tips112_exception_data.
        self.new_table_name_prefix = new_table_name_prefix
        # Specifies whether to set the archived table as the active table. Only the value true is supported. After the table is set as active, the previously active table under the same monitored object is automatically deactivated (only one active table is allowed at a time). If you set this parameter to false, an InvalidParameter error is returned. If this parameter is not specified, the default value true is used. If this parameter is left empty, the active status remains unchanged.
        self.set_active = set_active
        # The ID of the monitored object to which the archived table belongs.
        # 
        # This parameter is required.
        self.watch_id = watch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.add_mode is not None:
            result['AddMode'] = self.add_mode

        if self.archive_table_id is not None:
            result['ArchiveTableId'] = self.archive_table_id

        if self.exist_table_name is not None:
            result['ExistTableName'] = self.exist_table_name

        if self.lifecycle is not None:
            result['Lifecycle'] = self.lifecycle

        if self.max_archive_count is not None:
            result['MaxArchiveCount'] = self.max_archive_count

        if self.new_table_name_prefix is not None:
            result['NewTableNamePrefix'] = self.new_table_name_prefix

        if self.set_active is not None:
            result['SetActive'] = self.set_active

        if self.watch_id is not None:
            result['WatchId'] = self.watch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddMode') is not None:
            self.add_mode = m.get('AddMode')

        if m.get('ArchiveTableId') is not None:
            self.archive_table_id = m.get('ArchiveTableId')

        if m.get('ExistTableName') is not None:
            self.exist_table_name = m.get('ExistTableName')

        if m.get('Lifecycle') is not None:
            self.lifecycle = m.get('Lifecycle')

        if m.get('MaxArchiveCount') is not None:
            self.max_archive_count = m.get('MaxArchiveCount')

        if m.get('NewTableNamePrefix') is not None:
            self.new_table_name_prefix = m.get('NewTableNamePrefix')

        if m.get('SetActive') is not None:
            self.set_active = m.get('SetActive')

        if m.get('WatchId') is not None:
            self.watch_id = m.get('WatchId')

        return self

