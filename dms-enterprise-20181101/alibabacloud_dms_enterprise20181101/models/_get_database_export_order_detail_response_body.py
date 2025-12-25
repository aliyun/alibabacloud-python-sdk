# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class GetDatabaseExportOrderDetailResponseBody(DaraModel):
    def __init__(
        self,
        database_export_order_detail: main_models.GetDatabaseExportOrderDetailResponseBodyDatabaseExportOrderDetail = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details of the database export ticket.
        self.database_export_order_detail = database_export_order_detail
        # The error code.
        self.error_code = error_code
        # The error message returned if the request failed.
        self.error_message = error_message
        # The request ID. You can use the ID to query logs and troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.success = success

    def validate(self):
        if self.database_export_order_detail:
            self.database_export_order_detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.database_export_order_detail is not None:
            result['DatabaseExportOrderDetail'] = self.database_export_order_detail.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseExportOrderDetail') is not None:
            temp_model = main_models.GetDatabaseExportOrderDetailResponseBodyDatabaseExportOrderDetail()
            self.database_export_order_detail = temp_model.from_map(m.get('DatabaseExportOrderDetail'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetDatabaseExportOrderDetailResponseBodyDatabaseExportOrderDetail(DaraModel):
    def __init__(
        self,
        comment: str = None,
        committer: str = None,
        committer_id: str = None,
        id: int = None,
        key_info: main_models.GetDatabaseExportOrderDetailResponseBodyDatabaseExportOrderDetailKeyInfo = None,
        log: str = None,
        search_name: str = None,
        status_desc: str = None,
        workflow_status_desc: str = None,
    ):
        # The business background information of the database export ticket.
        self.comment = comment
        # The user who submitted the ticket.
        self.committer = committer
        # The ID of the user who submitted the ticket. This ID is a user ID and is not the ID of an Alibaba Cloud account.
        self.committer_id = committer_id
        # The ticket ID.
        self.id = id
        # The key information about the ticket.
        self.key_info = key_info
        # The execution logs.
        self.log = log
        # The name that is used to search for the database.
        self.search_name = search_name
        # The status description of the ticket.
        self.status_desc = status_desc
        # The status description of the workflow.
        self.workflow_status_desc = workflow_status_desc

    def validate(self):
        if self.key_info:
            self.key_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment

        if self.committer is not None:
            result['Committer'] = self.committer

        if self.committer_id is not None:
            result['CommitterId'] = self.committer_id

        if self.id is not None:
            result['Id'] = self.id

        if self.key_info is not None:
            result['KeyInfo'] = self.key_info.to_map()

        if self.log is not None:
            result['Log'] = self.log

        if self.search_name is not None:
            result['SearchName'] = self.search_name

        if self.status_desc is not None:
            result['StatusDesc'] = self.status_desc

        if self.workflow_status_desc is not None:
            result['WorkflowStatusDesc'] = self.workflow_status_desc

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('Committer') is not None:
            self.committer = m.get('Committer')

        if m.get('CommitterId') is not None:
            self.committer_id = m.get('CommitterId')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('KeyInfo') is not None:
            temp_model = main_models.GetDatabaseExportOrderDetailResponseBodyDatabaseExportOrderDetailKeyInfo()
            self.key_info = temp_model.from_map(m.get('KeyInfo'))

        if m.get('Log') is not None:
            self.log = m.get('Log')

        if m.get('SearchName') is not None:
            self.search_name = m.get('SearchName')

        if m.get('StatusDesc') is not None:
            self.status_desc = m.get('StatusDesc')

        if m.get('WorkflowStatusDesc') is not None:
            self.workflow_status_desc = m.get('WorkflowStatusDesc')

        return self

class GetDatabaseExportOrderDetailResponseBodyDatabaseExportOrderDetailKeyInfo(DaraModel):
    def __init__(
        self,
        audit_date: str = None,
        config: main_models.GetDatabaseExportOrderDetailResponseBodyDatabaseExportOrderDetailKeyInfoConfig = None,
        db_id: int = None,
        download_url: str = None,
    ):
        # The time when the ticket was submitted.
        self.audit_date = audit_date
        # The configuration information about the ticket.
        self.config = config
        # The database ID.
        self.db_id = db_id
        # The URL that is used to download the export result.
        self.download_url = download_url

    def validate(self):
        if self.config:
            self.config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audit_date is not None:
            result['AuditDate'] = self.audit_date

        if self.config is not None:
            result['Config'] = self.config.to_map()

        if self.db_id is not None:
            result['DbId'] = self.db_id

        if self.download_url is not None:
            result['DownloadURL'] = self.download_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditDate') is not None:
            self.audit_date = m.get('AuditDate')

        if m.get('Config') is not None:
            temp_model = main_models.GetDatabaseExportOrderDetailResponseBodyDatabaseExportOrderDetailKeyInfoConfig()
            self.config = temp_model.from_map(m.get('Config'))

        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')

        if m.get('DownloadURL') is not None:
            self.download_url = m.get('DownloadURL')

        return self

class GetDatabaseExportOrderDetailResponseBodyDatabaseExportOrderDetailKeyInfoConfig(DaraModel):
    def __init__(
        self,
        db_name: str = None,
        export_content: str = None,
        export_types: main_models.GetDatabaseExportOrderDetailResponseBodyDatabaseExportOrderDetailKeyInfoConfigExportTypes = None,
        sqlext_option: main_models.GetDatabaseExportOrderDetailResponseBodyDatabaseExportOrderDetailKeyInfoConfigSQLExtOption = None,
        selected_tables: main_models.GetDatabaseExportOrderDetailResponseBodyDatabaseExportOrderDetailKeyInfoConfigSelectedTables = None,
        target_option: str = None,
    ):
        # The database name.
        self.db_name = db_name
        # The type of data that was exported. Valid values:
        # 
        # *   **DATA**: The data of the database was exported.
        # *   **STRUCT**: The schema of the database was exported.
        # *   **DATA_STRUCT**: The data and schema of the database were exported.
        self.export_content = export_content
        # The type of schema that was exported.
        self.export_types = export_types
        # The extension options of the SQL script.
        self.sqlext_option = sqlext_option
        # The tables that were exported from the database.
        self.selected_tables = selected_tables
        # The format in which the database was exported. Valid values:
        # 
        # *   **SQL**
        # *   **CSV**
        # *   **XLSX**
        self.target_option = target_option

    def validate(self):
        if self.export_types:
            self.export_types.validate()
        if self.sqlext_option:
            self.sqlext_option.validate()
        if self.selected_tables:
            self.selected_tables.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.db_name is not None:
            result['DbName'] = self.db_name

        if self.export_content is not None:
            result['ExportContent'] = self.export_content

        if self.export_types is not None:
            result['ExportTypes'] = self.export_types.to_map()

        if self.sqlext_option is not None:
            result['SQLExtOption'] = self.sqlext_option.to_map()

        if self.selected_tables is not None:
            result['SelectedTables'] = self.selected_tables.to_map()

        if self.target_option is not None:
            result['TargetOption'] = self.target_option

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')

        if m.get('ExportContent') is not None:
            self.export_content = m.get('ExportContent')

        if m.get('ExportTypes') is not None:
            temp_model = main_models.GetDatabaseExportOrderDetailResponseBodyDatabaseExportOrderDetailKeyInfoConfigExportTypes()
            self.export_types = temp_model.from_map(m.get('ExportTypes'))

        if m.get('SQLExtOption') is not None:
            temp_model = main_models.GetDatabaseExportOrderDetailResponseBodyDatabaseExportOrderDetailKeyInfoConfigSQLExtOption()
            self.sqlext_option = temp_model.from_map(m.get('SQLExtOption'))

        if m.get('SelectedTables') is not None:
            temp_model = main_models.GetDatabaseExportOrderDetailResponseBodyDatabaseExportOrderDetailKeyInfoConfigSelectedTables()
            self.selected_tables = temp_model.from_map(m.get('SelectedTables'))

        if m.get('TargetOption') is not None:
            self.target_option = m.get('TargetOption')

        return self

class GetDatabaseExportOrderDetailResponseBodyDatabaseExportOrderDetailKeyInfoConfigSelectedTables(DaraModel):
    def __init__(
        self,
        selected_tables: List[str] = None,
    ):
        self.selected_tables = selected_tables

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.selected_tables is not None:
            result['SelectedTables'] = self.selected_tables

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SelectedTables') is not None:
            self.selected_tables = m.get('SelectedTables')

        return self

class GetDatabaseExportOrderDetailResponseBodyDatabaseExportOrderDetailKeyInfoConfigSQLExtOption(DaraModel):
    def __init__(
        self,
        sqlext_option: List[str] = None,
    ):
        self.sqlext_option = sqlext_option

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.sqlext_option is not None:
            result['SQLExtOption'] = self.sqlext_option

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SQLExtOption') is not None:
            self.sqlext_option = m.get('SQLExtOption')

        return self

class GetDatabaseExportOrderDetailResponseBodyDatabaseExportOrderDetailKeyInfoConfigExportTypes(DaraModel):
    def __init__(
        self,
        export_types: List[str] = None,
    ):
        self.export_types = export_types

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.export_types is not None:
            result['ExportTypes'] = self.export_types

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExportTypes') is not None:
            self.export_types = m.get('ExportTypes')

        return self

