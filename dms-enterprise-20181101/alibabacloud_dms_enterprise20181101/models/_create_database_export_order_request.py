# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class CreateDatabaseExportOrderRequest(DaraModel):
    def __init__(
        self,
        attachment_key: str = None,
        comment: str = None,
        parent_id: int = None,
        plugin_param: main_models.CreateDatabaseExportOrderRequestPluginParam = None,
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
            temp_model = main_models.CreateDatabaseExportOrderRequestPluginParam()
            self.plugin_param = temp_model.from_map(m.get('PluginParam'))

        if m.get('RelatedUserList') is not None:
            self.related_user_list = m.get('RelatedUserList')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

class CreateDatabaseExportOrderRequestPluginParam(DaraModel):
    def __init__(
        self,
        classify: str = None,
        config: main_models.CreateDatabaseExportOrderRequestPluginParamConfig = None,
        db_id: int = None,
        instance_id: int = None,
        logic: bool = None,
        search_name: str = None,
    ):
        # The reason for the database export.
        # 
        # This parameter is required.
        self.classify = classify
        # The configurations for database export.
        # 
        # This parameter is required.
        self.config = config
        # The database ID.
        # 
        # This parameter is required.
        self.db_id = db_id
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Specifies whether the database is a logical database. Valid values:
        # 
        # *   **true**
        # *   **false**
        # 
        # This parameter is required.
        self.logic = logic
        # The name that is used to search for the database.
        # 
        # This parameter is required.
        self.search_name = search_name

    def validate(self):
        if self.config:
            self.config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.classify is not None:
            result['Classify'] = self.classify

        if self.config is not None:
            result['Config'] = self.config.to_map()

        if self.db_id is not None:
            result['DbId'] = self.db_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.logic is not None:
            result['Logic'] = self.logic

        if self.search_name is not None:
            result['SearchName'] = self.search_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Classify') is not None:
            self.classify = m.get('Classify')

        if m.get('Config') is not None:
            temp_model = main_models.CreateDatabaseExportOrderRequestPluginParamConfig()
            self.config = temp_model.from_map(m.get('Config'))

        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Logic') is not None:
            self.logic = m.get('Logic')

        if m.get('SearchName') is not None:
            self.search_name = m.get('SearchName')

        return self

class CreateDatabaseExportOrderRequestPluginParamConfig(DaraModel):
    def __init__(
        self,
        data_option: List[str] = None,
        export_content: str = None,
        export_types: List[str] = None,
        sqlext_option: List[str] = None,
        selected_tables: List[str] = None,
        tables: Dict[str, str] = None,
        target_option: str = None,
    ):
        # The export options for big data. The options are used to filter the big data to be exported. You can leave this parameter empty.
        # 
        # This parameter is required.
        self.data_option = data_option
        # The type of data that you want to export. Valid values:
        # 
        # *   **DATA**: The data of the database is exported.
        # *   **STRUCT**: The schema of the database is exported.
        # *   **DATA_STRUCT**: The data and schema of the database are exported.
        # 
        # This parameter is required.
        self.export_content = export_content
        # The types of schemas that you want to export.
        self.export_types = export_types
        # The extension options of the SQL script. You can leave this parameter empty.
        # 
        # This parameter is required.
        self.sqlext_option = sqlext_option
        # The tables that you want to export.
        self.selected_tables = selected_tables
        # The conditions used to filter the tables to be exported.
        self.tables = tables
        # The format in which the database is exported. Valid values:
        # 
        # *   **SQL**
        # *   **CSV**
        # *   **XLSX**
        # 
        # This parameter is required.
        self.target_option = target_option

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_option is not None:
            result['DataOption'] = self.data_option

        if self.export_content is not None:
            result['ExportContent'] = self.export_content

        if self.export_types is not None:
            result['ExportTypes'] = self.export_types

        if self.sqlext_option is not None:
            result['SQLExtOption'] = self.sqlext_option

        if self.selected_tables is not None:
            result['SelectedTables'] = self.selected_tables

        if self.tables is not None:
            result['Tables'] = self.tables

        if self.target_option is not None:
            result['TargetOption'] = self.target_option

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataOption') is not None:
            self.data_option = m.get('DataOption')

        if m.get('ExportContent') is not None:
            self.export_content = m.get('ExportContent')

        if m.get('ExportTypes') is not None:
            self.export_types = m.get('ExportTypes')

        if m.get('SQLExtOption') is not None:
            self.sqlext_option = m.get('SQLExtOption')

        if m.get('SelectedTables') is not None:
            self.selected_tables = m.get('SelectedTables')

        if m.get('Tables') is not None:
            self.tables = m.get('Tables')

        if m.get('TargetOption') is not None:
            self.target_option = m.get('TargetOption')

        return self

