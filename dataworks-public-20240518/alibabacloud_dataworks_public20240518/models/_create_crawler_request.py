# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class CreateCrawlerRequest(DaraModel):
    def __init__(
        self,
        data_source_id: int = None,
        enable_ai_comment: bool = None,
        name: str = None,
        options: Dict[str, str] = None,
        resource_group_id: str = None,
        schedule_config: main_models.CreateCrawlerRequestScheduleConfig = None,
        scope: main_models.CreateCrawlerRequestScope = None,
        type: str = None,
    ):
        # The ID of the data source associated with the crawler. The data source must be bound to a DataWorks workspace, and the data source type must match the Type value.
        # 
        # This parameter is required.
        self.data_source_id = data_source_id
        # Specifies whether to enable AI metadata descriptions. This parameter is supported only when the SupportAiComment value returned by GetCrawlerTypeCapabilities is true.
        self.enable_ai_comment = enable_ai_comment
        # The name of the metadata crawler. The name can be up to 128 characters in length.
        # 
        # This parameter is required.
        self.name = name
        # The extended configuration for the crawler type. The key names, value types, required fields, default values, and valid values are determined by the SupportedOptionKeys value returned by GetCrawlerTypeCapabilities.
        self.options = options
        # The ID of the Serverless 2.0 resource group used to run the collection task. Whether this parameter is required depends on the RequireResourceGroup value returned by GetCrawlerTypeCapabilities.
        self.resource_group_id = resource_group_id
        # The scheduling configuration. If this parameter is not specified, manual scheduling is used.
        self.schedule_config = schedule_config
        # The collection scope configuration. If this parameter is not specified, the DefaultScopeUnit value returned by GetCrawlerTypeCapabilities is used.
        self.scope = scope
        # The crawler type. Call GetCrawlerTypeCapabilities to query the valid values supported in the current region.
        # 
        # This parameter is required.
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
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id

        if self.enable_ai_comment is not None:
            result['EnableAiComment'] = self.enable_ai_comment

        if self.name is not None:
            result['Name'] = self.name

        if self.options is not None:
            result['Options'] = self.options

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.schedule_config is not None:
            result['ScheduleConfig'] = self.schedule_config.to_map()

        if self.scope is not None:
            result['Scope'] = self.scope.to_map()

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')

        if m.get('EnableAiComment') is not None:
            self.enable_ai_comment = m.get('EnableAiComment')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Options') is not None:
            self.options = m.get('Options')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ScheduleConfig') is not None:
            temp_model = main_models.CreateCrawlerRequestScheduleConfig()
            self.schedule_config = temp_model.from_map(m.get('ScheduleConfig'))

        if m.get('Scope') is not None:
            temp_model = main_models.CreateCrawlerRequestScope()
            self.scope = temp_model.from_map(m.get('Scope'))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class CreateCrawlerRequestScope(DaraModel):
    def __init__(
        self,
        exclude_regex: str = None,
        items: List[str] = None,
        unit: str = None,
    ):
        # The regular expression used to exclude objects from the collection scope. This parameter is supported only when the SupportExcludeRegex value returned by GetCrawlerTypeCapabilities is true.
        self.exclude_regex = exclude_regex
        # The list of database names. This parameter is supported only when Unit is set to DATABASE. A maximum of 1000 entries are allowed. Names cannot be empty or duplicated.
        self.items = items
        # The collection scope granularity. Valid values are determined by the SupportedScopeUnits value returned by GetCrawlerTypeCapabilities.
        # 
        # This parameter is required.
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

class CreateCrawlerRequestScheduleConfig(DaraModel):
    def __init__(
        self,
        cron_express: str = None,
        type: str = None,
    ):
        # The six-field cron expression for periodic scheduling. This parameter is required when Type is set to NORMAL. The seconds field must be 0, and the scheduling frequency cannot exceed once per hour.
        self.cron_express = cron_express
        # The scheduling type. MANUAL indicates manual execution, and NORMAL indicates periodic scheduling. Data sources in the development environment support only MANUAL. Whether NORMAL is available depends on the SupportSchedule value returned by GetCrawlerTypeCapabilities.
        # 
        # This parameter is required.
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

