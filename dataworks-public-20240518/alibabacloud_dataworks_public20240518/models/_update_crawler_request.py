# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class UpdateCrawlerRequest(DaraModel):
    def __init__(
        self,
        enable_ai_comment: bool = None,
        id: int = None,
        options: Dict[str, str] = None,
        resource_group_id: str = None,
        schedule_config: main_models.UpdateCrawlerRequestScheduleConfig = None,
        scope: main_models.UpdateCrawlerRequestScope = None,
    ):
        # Specifies whether to enable AI metadata description. This parameter is supported only when SupportAiComment returned by GetCrawlerTypeCapabilities is set to true. If this parameter is not specified, the existing value remains unchanged.
        self.enable_ai_comment = enable_ai_comment
        # The ID of the metadata crawler. You can call ListCrawlers to query crawler IDs.
        # 
        # This parameter is required.
        self.id = id
        # The extension configurations for the crawler type. Only the specified configuration items are updated. Unspecified configuration items remain unchanged. The supported keys and values are determined by the SupportedOptionKeys returned by GetCrawlerTypeCapabilities.
        self.options = options
        # The ID of the Serverless 2.0 resource group used to run the collection task. Whether this parameter is supported and whether it is required depend on the capabilities returned by GetCrawlerTypeCapabilities. If this parameter is not specified, the existing value remains unchanged.
        self.resource_group_id = resource_group_id
        # The scheduling configuration. If this parameter is specified, the scheduling method is updated. If this parameter is not specified, the existing value remains unchanged.
        self.schedule_config = schedule_config
        # The collection scope configuration. If this parameter is specified, the collection scope is updated. If this parameter is not specified, the existing value remains unchanged.
        self.scope = scope

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
        if self.enable_ai_comment is not None:
            result['EnableAiComment'] = self.enable_ai_comment

        if self.id is not None:
            result['Id'] = self.id

        if self.options is not None:
            result['Options'] = self.options

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.schedule_config is not None:
            result['ScheduleConfig'] = self.schedule_config.to_map()

        if self.scope is not None:
            result['Scope'] = self.scope.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableAiComment') is not None:
            self.enable_ai_comment = m.get('EnableAiComment')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Options') is not None:
            self.options = m.get('Options')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ScheduleConfig') is not None:
            temp_model = main_models.UpdateCrawlerRequestScheduleConfig()
            self.schedule_config = temp_model.from_map(m.get('ScheduleConfig'))

        if m.get('Scope') is not None:
            temp_model = main_models.UpdateCrawlerRequestScope()
            self.scope = temp_model.from_map(m.get('Scope'))

        return self

class UpdateCrawlerRequestScope(DaraModel):
    def __init__(
        self,
        exclude_regex: str = None,
        items: List[str] = None,
        unit: str = None,
    ):
        # The regular expression used to exclude objects from the collection scope. This parameter is supported only when SupportExcludeRegex returned by GetCrawlerTypeCapabilities is set to true.
        self.exclude_regex = exclude_regex
        # The list of database names. This parameter is supported only when Unit is set to DATABASE. A maximum of 1,000 entries are allowed. Names cannot be empty or duplicate.
        self.items = items
        # The collection scope granularity. Valid values are determined by the SupportedScopeUnits returned by GetCrawlerTypeCapabilities.
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

class UpdateCrawlerRequestScheduleConfig(DaraModel):
    def __init__(
        self,
        cron_express: str = None,
        type: str = None,
    ):
        # The six-field cron expression for periodic scheduling. This parameter is required when Type is set to NORMAL. The seconds field must be 0, and the scheduling frequency cannot exceed once per hour.
        self.cron_express = cron_express
        # The scheduling type. MANUAL indicates manual execution. NORMAL indicates periodic scheduling. Data sources in the development environment support only MANUAL. Whether NORMAL is available depends on the SupportSchedule value returned by GetCrawlerTypeCapabilities.
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

