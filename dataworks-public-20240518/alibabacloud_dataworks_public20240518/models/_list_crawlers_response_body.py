# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class ListCrawlersResponseBody(DaraModel):
    def __init__(
        self,
        paging_info: main_models.ListCrawlersResponseBodyPagingInfo = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The pagination information.
        self.paging_info = paging_info
        # The request ID. Used to locate logs and troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the request succeeded.
        self.success = success

    def validate(self):
        if self.paging_info:
            self.paging_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.paging_info is not None:
            result['PagingInfo'] = self.paging_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PagingInfo') is not None:
            temp_model = main_models.ListCrawlersResponseBodyPagingInfo()
            self.paging_info = temp_model.from_map(m.get('PagingInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListCrawlersResponseBodyPagingInfo(DaraModel):
    def __init__(
        self,
        crawlers: List[main_models.ListCrawlersResponseBodyPagingInfoCrawlers] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The list of metadata crawlers.
        self.crawlers = crawlers
        # The current page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The total number of records that match the query conditions.
        self.total_count = total_count

    def validate(self):
        if self.crawlers:
            for v1 in self.crawlers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Crawlers'] = []
        if self.crawlers is not None:
            for k1 in self.crawlers:
                result['Crawlers'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.crawlers = []
        if m.get('Crawlers') is not None:
            for k1 in m.get('Crawlers'):
                temp_model = main_models.ListCrawlersResponseBodyPagingInfoCrawlers()
                self.crawlers.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListCrawlersResponseBodyPagingInfoCrawlers(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        data_source_id: int = None,
        env_type: str = None,
        id: int = None,
        last_run_status: str = None,
        meta_entity_id: str = None,
        modify_time: int = None,
        name: str = None,
        owner: str = None,
        project_id: int = None,
        resource_group_id: str = None,
        schedule_config: main_models.ListCrawlersResponseBodyPagingInfoCrawlersScheduleConfig = None,
        status: str = None,
        task_id: int = None,
        type: str = None,
    ):
        # The creation time, expressed as a millisecond-precision UNIX timestamp.
        self.create_time = create_time
        # The data source ID.
        self.data_source_id = data_source_id
        # The DataWorks environment type. Valid values: Dev, Prod.
        self.env_type = env_type
        # The crawler ID.
        self.id = id
        # The most recent run status. Valid values: WAITING, RUNNING, SUCCESS, ERROR, SHUTDOWN. This field may be empty if the crawler has not run yet.
        self.last_run_status = last_run_status
        # The meta entity ID associated with the crawler. You can use this ID to connect to metadata query APIs.
        self.meta_entity_id = meta_entity_id
        # The modification time, expressed as a millisecond-precision UNIX timestamp.
        self.modify_time = modify_time
        # The crawler name.
        self.name = name
        # The DataWorks user ID of the crawler owner.
        self.owner = owner
        # The DataWorks workspace ID.
        self.project_id = project_id
        # The ID of the Serverless 2.0 resource group used to run the crawl task.
        self.resource_group_id = resource_group_id
        # The schedule configuration.
        self.schedule_config = schedule_config
        # The crawler status. The value is VALID when the crawler configuration is valid and the associated data source exists. Otherwise, the value is INVALID.
        self.status = status
        # The DataWorks scheduling node ID associated with the crawler. You can use this ID to call GetTask to query the node definition.
        self.task_id = task_id
        # The crawler type.
        self.type = type

    def validate(self):
        if self.schedule_config:
            self.schedule_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id

        if self.env_type is not None:
            result['EnvType'] = self.env_type

        if self.id is not None:
            result['Id'] = self.id

        if self.last_run_status is not None:
            result['LastRunStatus'] = self.last_run_status

        if self.meta_entity_id is not None:
            result['MetaEntityId'] = self.meta_entity_id

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.name is not None:
            result['Name'] = self.name

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.schedule_config is not None:
            result['ScheduleConfig'] = self.schedule_config.to_map()

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

        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('LastRunStatus') is not None:
            self.last_run_status = m.get('LastRunStatus')

        if m.get('MetaEntityId') is not None:
            self.meta_entity_id = m.get('MetaEntityId')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ScheduleConfig') is not None:
            temp_model = main_models.ListCrawlersResponseBodyPagingInfoCrawlersScheduleConfig()
            self.schedule_config = temp_model.from_map(m.get('ScheduleConfig'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListCrawlersResponseBodyPagingInfoCrawlersScheduleConfig(DaraModel):
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

