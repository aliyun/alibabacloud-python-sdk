# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class GetCrawlerResponseBody(DaraModel):
    def __init__(
        self,
        crawler: main_models.GetCrawlerResponseBodyCrawler = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The metadata crawler details.
        self.crawler = crawler
        # The request ID. Used for locating logs and troubleshooting issues.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.crawler:
            self.crawler.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.crawler is not None:
            result['Crawler'] = self.crawler.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Crawler') is not None:
            temp_model = main_models.GetCrawlerResponseBodyCrawler()
            self.crawler = temp_model.from_map(m.get('Crawler'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetCrawlerResponseBodyCrawler(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        data_source_id: int = None,
        enable_ai_comment: bool = None,
        env_type: str = None,
        id: int = None,
        last_run_status: str = None,
        last_run_task_instance_id: int = None,
        meta_entity_id: str = None,
        modify_time: int = None,
        name: str = None,
        options: Dict[str, str] = None,
        owner: str = None,
        project_id: int = None,
        resource_group_id: str = None,
        schedule_config: main_models.GetCrawlerResponseBodyCrawlerScheduleConfig = None,
        scope: main_models.GetCrawlerResponseBodyCrawlerScope = None,
        status: str = None,
        task_id: int = None,
        type: str = None,
    ):
        # The creation time, in millisecond-level UNIX timestamp.
        self.create_time = create_time
        # The data source ID.
        self.data_source_id = data_source_id
        # Indicates whether AI metadata description is enabled.
        self.enable_ai_comment = enable_ai_comment
        # The DataWorks environment type. Valid values: Dev, Prod.
        self.env_type = env_type
        # The crawler ID.
        self.id = id
        # The latest run status. Valid values: WAITING, RUNNING, SUCCESS, ERROR, SHUTDOWN. This value may be empty if the crawler has not been run.
        self.last_run_status = last_run_status
        # The DataWorks task instance ID associated with the latest run. This value may be empty if the crawler has not been run.
        self.last_run_task_instance_id = last_run_task_instance_id
        # The meta entity ID associated with the crawler, which can be used to connect to metadata query APIs.
        self.meta_entity_id = meta_entity_id
        # The modification time, in millisecond-level UNIX timestamp.
        self.modify_time = modify_time
        # The crawler name.
        self.name = name
        # The extended configuration for the crawler type.
        self.options = options
        # The DataWorks user ID of the crawler owner.
        self.owner = owner
        # The DataWorks workspace ID.
        self.project_id = project_id
        # The Serverless 2.0 resource group ID used to run the collection task.
        self.resource_group_id = resource_group_id
        # The schedule configuration.
        self.schedule_config = schedule_config
        # The collection scope configuration.
        self.scope = scope
        # The crawler status. The value is VALID if the crawler configuration is valid and the associated data source exists. Otherwise, the value is INVALID.
        self.status = status
        # The DataWorks scheduling task ID associated with the crawler, which can be used to call GetTask to query the task definition.
        self.task_id = task_id
        # The crawler type.
        self.type = type

    def validate(self):
        if self.schedule_config:
            self.schedule_config.validate()
        if self.scope:
            self.scope.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id

        if self.enable_ai_comment is not None:
            result['EnableAiComment'] = self.enable_ai_comment

        if self.env_type is not None:
            result['EnvType'] = self.env_type

        if self.id is not None:
            result['Id'] = self.id

        if self.last_run_status is not None:
            result['LastRunStatus'] = self.last_run_status

        if self.last_run_task_instance_id is not None:
            result['LastRunTaskInstanceId'] = self.last_run_task_instance_id

        if self.meta_entity_id is not None:
            result['MetaEntityId'] = self.meta_entity_id

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.name is not None:
            result['Name'] = self.name

        if self.options is not None:
            result['Options'] = self.options

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.schedule_config is not None:
            result['ScheduleConfig'] = self.schedule_config.to_map()

        if self.scope is not None:
            result['Scope'] = self.scope.to_map()

        if self.status is not None:
            result['Status'] = self.status

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')

        if m.get('EnableAiComment') is not None:
            self.enable_ai_comment = m.get('EnableAiComment')

        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('LastRunStatus') is not None:
            self.last_run_status = m.get('LastRunStatus')

        if m.get('LastRunTaskInstanceId') is not None:
            self.last_run_task_instance_id = m.get('LastRunTaskInstanceId')

        if m.get('MetaEntityId') is not None:
            self.meta_entity_id = m.get('MetaEntityId')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Options') is not None:
            self.options = m.get('Options')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ScheduleConfig') is not None:
            temp_model = main_models.GetCrawlerResponseBodyCrawlerScheduleConfig()
            self.schedule_config = temp_model.from_map(m.get('ScheduleConfig'))

        if m.get('Scope') is not None:
            temp_model = main_models.GetCrawlerResponseBodyCrawlerScope()
            self.scope = temp_model.from_map(m.get('Scope'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class GetCrawlerResponseBodyCrawlerScope(DaraModel):
    def __init__(
        self,
        exclude_regex: str = None,
        items: List[str] = None,
        unit: str = None,
    ):
        # The exclusion regular expression for the collection scope.
        self.exclude_regex = exclude_regex
        # The collection scope entries.
        self.items = items
        # The collection scope granularity. Valid values: PROJECT, DATABASE, INSTANCE, CATALOG.
        self.unit = unit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.exclude_regex is not None:
            result['ExcludeRegex'] = self.exclude_regex

        if self.items is not None:
            result['Items'] = self.items

        if self.unit is not None:
            result['Unit'] = self.unit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExcludeRegex') is not None:
            self.exclude_regex = m.get('ExcludeRegex')

        if m.get('Items') is not None:
            self.items = m.get('Items')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        return self

class GetCrawlerResponseBodyCrawlerScheduleConfig(DaraModel):
    def __init__(
        self,
        cron_express: str = None,
        type: str = None,
    ):
        # The cron expression.
        self.cron_express = cron_express
        # The schedule type. Valid values: MANUAL, NORMAL.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cron_express is not None:
            result['CronExpress'] = self.cron_express

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CronExpress') is not None:
            self.cron_express = m.get('CronExpress')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

