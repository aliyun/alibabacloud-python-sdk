# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class CreateDataExportOrderRequest(DaraModel):
    def __init__(
        self,
        attachment_key: str = None,
        comment: str = None,
        parent_id: int = None,
        plugin_param: main_models.CreateDataExportOrderRequestPluginParam = None,
        real_login_user_uid: str = None,
        related_user_list: List[int] = None,
        tid: int = None,
    ):
        # The key of the attachment that provides more instructions for the ticket. You can call the [GetUserUploadFileJob](https://help.aliyun.com/document_detail/206069.html) operation to obtain the attachment key.
        self.attachment_key = attachment_key
        # The purpose or objective of the ticket. This parameter helps reduce unnecessary communication.
        # 
        # This parameter is required.
        self.comment = comment
        # The ID of the parent ticket.
        self.parent_id = parent_id
        # The parameters of the ticket.
        # 
        # This parameter is required.
        self.plugin_param = plugin_param
        # The UID of the Alibaba Cloud account that actually calls the API.
        self.real_login_user_uid = real_login_user_uid
        # The stakeholders involved in this operation.
        self.related_user_list = related_user_list
        # The tenant ID.
        # 
        # > To view the ID of the tenant, move the pointer over the profile picture in the upper-right corner of the DMS console. For more information, see the [View information about the current tenant](https://help.aliyun.com/document_detail/181330.html) section of the "Manage DMS tenants" topic.
        self.tid = tid

    def validate(self):
        if self.plugin_param:
            self.plugin_param.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attachment_key is not None:
            result['AttachmentKey'] = self.attachment_key

        if self.comment is not None:
            result['Comment'] = self.comment

        if self.parent_id is not None:
            result['ParentId'] = self.parent_id

        if self.plugin_param is not None:
            result['PluginParam'] = self.plugin_param.to_map()

        if self.real_login_user_uid is not None:
            result['RealLoginUserUid'] = self.real_login_user_uid

        if self.related_user_list is not None:
            result['RelatedUserList'] = self.related_user_list

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttachmentKey') is not None:
            self.attachment_key = m.get('AttachmentKey')

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')

        if m.get('PluginParam') is not None:
            temp_model = main_models.CreateDataExportOrderRequestPluginParam()
            self.plugin_param = temp_model.from_map(m.get('PluginParam'))

        if m.get('RealLoginUserUid') is not None:
            self.real_login_user_uid = m.get('RealLoginUserUid')

        if m.get('RelatedUserList') is not None:
            self.related_user_list = m.get('RelatedUserList')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

class CreateDataExportOrderRequestPluginParam(DaraModel):
    def __init__(
        self,
        affect_rows: int = None,
        classify: str = None,
        db_id: int = None,
        exe_sql: str = None,
        ignore_affect_rows: bool = None,
        ignore_affect_rows_reason: str = None,
        instance_id: int = None,
        logic: bool = None,
        watermark: main_models.CreateDataExportOrderRequestPluginParamWatermark = None,
    ):
        # The estimated number of data rows to be affected.
        # 
        # This parameter is required.
        self.affect_rows = affect_rows
        # The reason for the export ticket.
        # 
        # This parameter is required.
        self.classify = classify
        # The database ID.
        # 
        # This parameter is required.
        self.db_id = db_id
        # The SQL statements that can be executed.
        # 
        # This parameter is required.
        self.exe_sql = exe_sql
        # Specifies whether to skip verification. Valid values:
        # 
        # *   **true**
        # *   **false**
        # 
        # This parameter is required.
        self.ignore_affect_rows = ignore_affect_rows
        # The reason for skipping verification. This parameter is required if you set IgnoreAffectRows to true.
        self.ignore_affect_rows_reason = ignore_affect_rows_reason
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Specifies whether the database is a logical database. Valid values:
        # 
        # *   **true**
        # *   **false**
        # 
        # > If you set this parameter to **true**, the database that you specify must be a logical database.
        # 
        # This parameter is required.
        self.logic = logic
        # The information about the watermarks.
        self.watermark = watermark

    def validate(self):
        if self.watermark:
            self.watermark.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.affect_rows is not None:
            result['AffectRows'] = self.affect_rows

        if self.classify is not None:
            result['Classify'] = self.classify

        if self.db_id is not None:
            result['DbId'] = self.db_id

        if self.exe_sql is not None:
            result['ExeSQL'] = self.exe_sql

        if self.ignore_affect_rows is not None:
            result['IgnoreAffectRows'] = self.ignore_affect_rows

        if self.ignore_affect_rows_reason is not None:
            result['IgnoreAffectRowsReason'] = self.ignore_affect_rows_reason

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.logic is not None:
            result['Logic'] = self.logic

        if self.watermark is not None:
            result['Watermark'] = self.watermark.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AffectRows') is not None:
            self.affect_rows = m.get('AffectRows')

        if m.get('Classify') is not None:
            self.classify = m.get('Classify')

        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')

        if m.get('ExeSQL') is not None:
            self.exe_sql = m.get('ExeSQL')

        if m.get('IgnoreAffectRows') is not None:
            self.ignore_affect_rows = m.get('IgnoreAffectRows')

        if m.get('IgnoreAffectRowsReason') is not None:
            self.ignore_affect_rows_reason = m.get('IgnoreAffectRowsReason')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Logic') is not None:
            self.logic = m.get('Logic')

        if m.get('Watermark') is not None:
            temp_model = main_models.CreateDataExportOrderRequestPluginParamWatermark()
            self.watermark = temp_model.from_map(m.get('Watermark'))

        return self

class CreateDataExportOrderRequestPluginParamWatermark(DaraModel):
    def __init__(
        self,
        column_name: str = None,
        data_watermark: str = None,
        file_watermark: str = None,
        keys: List[str] = None,
        watermark_types: List[str] = None,
    ):
        # The field into which the watermark is to be embedded.
        self.column_name = column_name
        # The information to be embedded as a watermark into data.
        self.data_watermark = data_watermark
        # The information to be embedded as a watermark into files.
        self.file_watermark = file_watermark
        # One or more primary keys or unique keys.
        self.keys = keys
        # The methods in which the watermark is embedded.
        self.watermark_types = watermark_types

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.column_name is not None:
            result['ColumnName'] = self.column_name

        if self.data_watermark is not None:
            result['DataWatermark'] = self.data_watermark

        if self.file_watermark is not None:
            result['FileWatermark'] = self.file_watermark

        if self.keys is not None:
            result['Keys'] = self.keys

        if self.watermark_types is not None:
            result['WatermarkTypes'] = self.watermark_types

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColumnName') is not None:
            self.column_name = m.get('ColumnName')

        if m.get('DataWatermark') is not None:
            self.data_watermark = m.get('DataWatermark')

        if m.get('FileWatermark') is not None:
            self.file_watermark = m.get('FileWatermark')

        if m.get('Keys') is not None:
            self.keys = m.get('Keys')

        if m.get('WatermarkTypes') is not None:
            self.watermark_types = m.get('WatermarkTypes')

        return self

