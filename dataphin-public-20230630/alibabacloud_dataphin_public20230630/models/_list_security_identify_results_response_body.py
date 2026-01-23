# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ListSecurityIdentifyResultsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        page_result: main_models.ListSecurityIdentifyResultsResponseBodyPageResult = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.page_result = page_result
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.page_result:
            self.page_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.page_result is not None:
            result['PageResult'] = self.page_result.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageResult') is not None:
            temp_model = main_models.ListSecurityIdentifyResultsResponseBodyPageResult()
            self.page_result = temp_model.from_map(m.get('PageResult'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListSecurityIdentifyResultsResponseBodyPageResult(DaraModel):
    def __init__(
        self,
        security_identify_result_list: List[main_models.ListSecurityIdentifyResultsResponseBodyPageResultSecurityIdentifyResultList] = None,
        total_count: int = None,
    ):
        self.security_identify_result_list = security_identify_result_list
        self.total_count = total_count

    def validate(self):
        if self.security_identify_result_list:
            for v1 in self.security_identify_result_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SecurityIdentifyResultList'] = []
        if self.security_identify_result_list is not None:
            for k1 in self.security_identify_result_list:
                result['SecurityIdentifyResultList'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.security_identify_result_list = []
        if m.get('SecurityIdentifyResultList') is not None:
            for k1 in m.get('SecurityIdentifyResultList'):
                temp_model = main_models.ListSecurityIdentifyResultsResponseBodyPageResultSecurityIdentifyResultList()
                self.security_identify_result_list.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListSecurityIdentifyResultsResponseBodyPageResultSecurityIdentifyResultList(DaraModel):
    def __init__(
        self,
        biz_date: str = None,
        biz_unit_display_name: str = None,
        biz_unit_id: int = None,
        biz_unit_name: str = None,
        classify_abbreviation: str = None,
        classify_id: int = None,
        classify_name: str = None,
        create_time: str = None,
        creator: str = None,
        datasource_id: int = None,
        datasource_name: str = None,
        field_description: str = None,
        field_id: str = None,
        field_name: str = None,
        has_better_rule: bool = None,
        id: int = None,
        identify_record_id: int = None,
        is_custom_identify: bool = None,
        is_locked: bool = None,
        level_abbreviation: str = None,
        level_color: int = None,
        level_index: int = None,
        level_name: str = None,
        modifier: str = None,
        modify_time: str = None,
        project_display_name: str = None,
        project_id: int = None,
        project_name: str = None,
        scan_task_id: int = None,
        status: str = None,
        table_catalog: str = None,
        table_description: str = None,
        table_env: str = None,
        table_id: str = None,
        table_name: str = None,
        table_task_id: int = None,
        table_type: str = None,
    ):
        self.biz_date = biz_date
        self.biz_unit_display_name = biz_unit_display_name
        self.biz_unit_id = biz_unit_id
        self.biz_unit_name = biz_unit_name
        self.classify_abbreviation = classify_abbreviation
        self.classify_id = classify_id
        self.classify_name = classify_name
        self.create_time = create_time
        self.creator = creator
        self.datasource_id = datasource_id
        self.datasource_name = datasource_name
        self.field_description = field_description
        self.field_id = field_id
        self.field_name = field_name
        self.has_better_rule = has_better_rule
        self.id = id
        self.identify_record_id = identify_record_id
        self.is_custom_identify = is_custom_identify
        self.is_locked = is_locked
        self.level_abbreviation = level_abbreviation
        self.level_color = level_color
        self.level_index = level_index
        self.level_name = level_name
        self.modifier = modifier
        self.modify_time = modify_time
        self.project_display_name = project_display_name
        self.project_id = project_id
        self.project_name = project_name
        self.scan_task_id = scan_task_id
        self.status = status
        self.table_catalog = table_catalog
        self.table_description = table_description
        self.table_env = table_env
        self.table_id = table_id
        self.table_name = table_name
        self.table_task_id = table_task_id
        self.table_type = table_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_date is not None:
            result['BizDate'] = self.biz_date

        if self.biz_unit_display_name is not None:
            result['BizUnitDisplayName'] = self.biz_unit_display_name

        if self.biz_unit_id is not None:
            result['BizUnitId'] = self.biz_unit_id

        if self.biz_unit_name is not None:
            result['BizUnitName'] = self.biz_unit_name

        if self.classify_abbreviation is not None:
            result['ClassifyAbbreviation'] = self.classify_abbreviation

        if self.classify_id is not None:
            result['ClassifyId'] = self.classify_id

        if self.classify_name is not None:
            result['ClassifyName'] = self.classify_name

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.datasource_id is not None:
            result['DatasourceId'] = self.datasource_id

        if self.datasource_name is not None:
            result['DatasourceName'] = self.datasource_name

        if self.field_description is not None:
            result['FieldDescription'] = self.field_description

        if self.field_id is not None:
            result['FieldId'] = self.field_id

        if self.field_name is not None:
            result['FieldName'] = self.field_name

        if self.has_better_rule is not None:
            result['HasBetterRule'] = self.has_better_rule

        if self.id is not None:
            result['Id'] = self.id

        if self.identify_record_id is not None:
            result['IdentifyRecordId'] = self.identify_record_id

        if self.is_custom_identify is not None:
            result['IsCustomIdentify'] = self.is_custom_identify

        if self.is_locked is not None:
            result['IsLocked'] = self.is_locked

        if self.level_abbreviation is not None:
            result['LevelAbbreviation'] = self.level_abbreviation

        if self.level_color is not None:
            result['LevelColor'] = self.level_color

        if self.level_index is not None:
            result['LevelIndex'] = self.level_index

        if self.level_name is not None:
            result['LevelName'] = self.level_name

        if self.modifier is not None:
            result['Modifier'] = self.modifier

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.project_display_name is not None:
            result['ProjectDisplayName'] = self.project_display_name

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.scan_task_id is not None:
            result['ScanTaskId'] = self.scan_task_id

        if self.status is not None:
            result['Status'] = self.status

        if self.table_catalog is not None:
            result['TableCatalog'] = self.table_catalog

        if self.table_description is not None:
            result['TableDescription'] = self.table_description

        if self.table_env is not None:
            result['TableEnv'] = self.table_env

        if self.table_id is not None:
            result['TableId'] = self.table_id

        if self.table_name is not None:
            result['TableName'] = self.table_name

        if self.table_task_id is not None:
            result['TableTaskId'] = self.table_task_id

        if self.table_type is not None:
            result['TableType'] = self.table_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizDate') is not None:
            self.biz_date = m.get('BizDate')

        if m.get('BizUnitDisplayName') is not None:
            self.biz_unit_display_name = m.get('BizUnitDisplayName')

        if m.get('BizUnitId') is not None:
            self.biz_unit_id = m.get('BizUnitId')

        if m.get('BizUnitName') is not None:
            self.biz_unit_name = m.get('BizUnitName')

        if m.get('ClassifyAbbreviation') is not None:
            self.classify_abbreviation = m.get('ClassifyAbbreviation')

        if m.get('ClassifyId') is not None:
            self.classify_id = m.get('ClassifyId')

        if m.get('ClassifyName') is not None:
            self.classify_name = m.get('ClassifyName')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('DatasourceId') is not None:
            self.datasource_id = m.get('DatasourceId')

        if m.get('DatasourceName') is not None:
            self.datasource_name = m.get('DatasourceName')

        if m.get('FieldDescription') is not None:
            self.field_description = m.get('FieldDescription')

        if m.get('FieldId') is not None:
            self.field_id = m.get('FieldId')

        if m.get('FieldName') is not None:
            self.field_name = m.get('FieldName')

        if m.get('HasBetterRule') is not None:
            self.has_better_rule = m.get('HasBetterRule')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IdentifyRecordId') is not None:
            self.identify_record_id = m.get('IdentifyRecordId')

        if m.get('IsCustomIdentify') is not None:
            self.is_custom_identify = m.get('IsCustomIdentify')

        if m.get('IsLocked') is not None:
            self.is_locked = m.get('IsLocked')

        if m.get('LevelAbbreviation') is not None:
            self.level_abbreviation = m.get('LevelAbbreviation')

        if m.get('LevelColor') is not None:
            self.level_color = m.get('LevelColor')

        if m.get('LevelIndex') is not None:
            self.level_index = m.get('LevelIndex')

        if m.get('LevelName') is not None:
            self.level_name = m.get('LevelName')

        if m.get('Modifier') is not None:
            self.modifier = m.get('Modifier')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('ProjectDisplayName') is not None:
            self.project_display_name = m.get('ProjectDisplayName')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('ScanTaskId') is not None:
            self.scan_task_id = m.get('ScanTaskId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TableCatalog') is not None:
            self.table_catalog = m.get('TableCatalog')

        if m.get('TableDescription') is not None:
            self.table_description = m.get('TableDescription')

        if m.get('TableEnv') is not None:
            self.table_env = m.get('TableEnv')

        if m.get('TableId') is not None:
            self.table_id = m.get('TableId')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        if m.get('TableTaskId') is not None:
            self.table_task_id = m.get('TableTaskId')

        if m.get('TableType') is not None:
            self.table_type = m.get('TableType')

        return self

