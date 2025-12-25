# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class CreateDataCronClearOrderRequest(DaraModel):
    def __init__(
        self,
        attachment_key: str = None,
        comment: str = None,
        param: main_models.CreateDataCronClearOrderRequestParam = None,
        related_user_list: List[int] = None,
        tid: int = None,
    ):
        # The key of the attachment for the ticket. The attachment provides more instructions for this operation.
        # 
        # You can call the [GetUserUploadFileJob](https://help.aliyun.com/document_detail/206069.html) operation to query the key of the attachment.
        self.attachment_key = attachment_key
        # The purpose or objective of the data change. This reduces unnecessary communication.
        # 
        # This parameter is required.
        self.comment = comment
        # The parameters of the ticket.
        # 
        # This parameter is required.
        self.param = param
        # The stakeholders of this operation. All stakeholders can view the ticket details and assist in the approval process. Irrelevant users other than Data Management (DMS) administrators and database administrators (DBAs) are not allowed to view the ticket details.
        self.related_user_list = related_user_list
        # The ID of the tenant.
        # 
        # >  The ID of the tenant is displayed when you move the pointer over the profile picture in the upper-right corner of the DMS console. For more information, see the [View information about the current tenant](https://help.aliyun.com/document_detail/181330.html) section of the Manage DMS tenants topic.
        self.tid = tid

    def validate(self):
        if self.param:
            self.param.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attachment_key is not None:
            result['AttachmentKey'] = self.attachment_key

        if self.comment is not None:
            result['Comment'] = self.comment

        if self.param is not None:
            result['Param'] = self.param.to_map()

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

        if m.get('Param') is not None:
            temp_model = main_models.CreateDataCronClearOrderRequestParam()
            self.param = temp_model.from_map(m.get('Param'))

        if m.get('RelatedUserList') is not None:
            self.related_user_list = m.get('RelatedUserList')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

class CreateDataCronClearOrderRequestParam(DaraModel):
    def __init__(
        self,
        classify: str = None,
        cron_clear_item_list: List[main_models.CreateDataCronClearOrderRequestParamCronClearItemList] = None,
        cron_format: str = None,
        db_item_list: List[main_models.CreateDataCronClearOrderRequestParamDbItemList] = None,
        duration_hour: int = None,
        specify_duration: bool = None,
    ):
        # The reason for the data change.
        self.classify = classify
        # The tables for which you want to clear historical data.
        # 
        # This parameter is required.
        self.cron_clear_item_list = cron_clear_item_list
        # The crontab expression that you can use to run the task at a specified time. For more information, see [Crontab expression](https://help.aliyun.com/document_detail/206581.html).
        # 
        # This parameter is required.
        self.cron_format = cron_format
        # The databases for which you want to clear historical data.
        # 
        # This parameter is required.
        self.db_item_list = db_item_list
        # The amount of time taken to run the task. Unit: hours.
        # 
        # >  If the **specifyDuration** parameter is set to **true**, this parameter is required.
        self.duration_hour = duration_hour
        # Specifies whether to specify an end time for the task. Valid values:
        # 
        # *   **true**: specifies an end time for the task. The task is automatically suspended after this end time.
        # *   **false**: does not specify an end time for the task. The task is stopped after the historical data is cleared.
        # 
        # This parameter is required.
        self.specify_duration = specify_duration

    def validate(self):
        if self.cron_clear_item_list:
            for v1 in self.cron_clear_item_list:
                 if v1:
                    v1.validate()
        if self.db_item_list:
            for v1 in self.db_item_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.classify is not None:
            result['Classify'] = self.classify

        result['CronClearItemList'] = []
        if self.cron_clear_item_list is not None:
            for k1 in self.cron_clear_item_list:
                result['CronClearItemList'].append(k1.to_map() if k1 else None)

        if self.cron_format is not None:
            result['CronFormat'] = self.cron_format

        result['DbItemList'] = []
        if self.db_item_list is not None:
            for k1 in self.db_item_list:
                result['DbItemList'].append(k1.to_map() if k1 else None)

        if self.duration_hour is not None:
            result['DurationHour'] = self.duration_hour

        if self.specify_duration is not None:
            result['specifyDuration'] = self.specify_duration

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Classify') is not None:
            self.classify = m.get('Classify')

        self.cron_clear_item_list = []
        if m.get('CronClearItemList') is not None:
            for k1 in m.get('CronClearItemList'):
                temp_model = main_models.CreateDataCronClearOrderRequestParamCronClearItemList()
                self.cron_clear_item_list.append(temp_model.from_map(k1))

        if m.get('CronFormat') is not None:
            self.cron_format = m.get('CronFormat')

        self.db_item_list = []
        if m.get('DbItemList') is not None:
            for k1 in m.get('DbItemList'):
                temp_model = main_models.CreateDataCronClearOrderRequestParamDbItemList()
                self.db_item_list.append(temp_model.from_map(k1))

        if m.get('DurationHour') is not None:
            self.duration_hour = m.get('DurationHour')

        if m.get('specifyDuration') is not None:
            self.specify_duration = m.get('specifyDuration')

        return self

class CreateDataCronClearOrderRequestParamDbItemList(DaraModel):
    def __init__(
        self,
        db_id: int = None,
        logic: bool = None,
    ):
        # The ID of the database. You can call the [SearchDatabases](https://help.aliyun.com/document_detail/141876.html) operation to query the ID of the database.
        # 
        # This parameter is required.
        self.db_id = db_id
        # Indicates whether the database is a logical database. Valid values:
        # 
        # *   **true**: The database is a logical database.
        # *   **false**: The database is not a logical database.
        # 
        # This parameter is required.
        self.logic = logic

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.db_id is not None:
            result['DbId'] = self.db_id

        if self.logic is not None:
            result['Logic'] = self.logic

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')

        if m.get('Logic') is not None:
            self.logic = m.get('Logic')

        return self

class CreateDataCronClearOrderRequestParamCronClearItemList(DaraModel):
    def __init__(
        self,
        column_name: str = None,
        filter_sql: str = None,
        remain_days: int = None,
        table_name: str = None,
        time_unit: str = None,
    ):
        # The name of the field.
        # 
        # This parameter is required.
        self.column_name = column_name
        # The filter conditions.
        self.filter_sql = filter_sql
        # The retention period of the historical data. Unit: days. For example, if you set the parameter to 7, DMS deletes the data that is retained for more than seven days.
        # 
        # This parameter is required.
        self.remain_days = remain_days
        # The name of the table. You can call the [ListTables](https://help.aliyun.com/document_detail/141878.html) operation to query the name of the table.
        # 
        # This parameter is required.
        self.table_name = table_name
        # The type of time granularity. If the ColumnName parameter specifies a field of a time type, this parameter is required. Valid values:
        # 
        # *   **MILLISECONDS**: milliseconds
        # *   **SECONDS**: seconds
        self.time_unit = time_unit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.column_name is not None:
            result['ColumnName'] = self.column_name

        if self.filter_sql is not None:
            result['FilterSQL'] = self.filter_sql

        if self.remain_days is not None:
            result['RemainDays'] = self.remain_days

        if self.table_name is not None:
            result['TableName'] = self.table_name

        if self.time_unit is not None:
            result['TimeUnit'] = self.time_unit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColumnName') is not None:
            self.column_name = m.get('ColumnName')

        if m.get('FilterSQL') is not None:
            self.filter_sql = m.get('FilterSQL')

        if m.get('RemainDays') is not None:
            self.remain_days = m.get('RemainDays')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        if m.get('TimeUnit') is not None:
            self.time_unit = m.get('TimeUnit')

        return self

