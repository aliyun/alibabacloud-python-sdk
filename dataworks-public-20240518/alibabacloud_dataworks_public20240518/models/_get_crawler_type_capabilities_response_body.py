# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class GetCrawlerTypeCapabilitiesResponseBody(DaraModel):
    def __init__(
        self,
        crawler_types: List[main_models.GetCrawlerTypeCapabilitiesResponseBodyCrawlerTypes] = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.crawler_types = crawler_types
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.crawler_types:
            for v1 in self.crawler_types:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CrawlerTypes'] = []
        if self.crawler_types is not None:
            for k1 in self.crawler_types:
                result['CrawlerTypes'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.crawler_types = []
        if m.get('CrawlerTypes') is not None:
            for k1 in m.get('CrawlerTypes'):
                temp_model = main_models.GetCrawlerTypeCapabilitiesResponseBodyCrawlerTypes()
                self.crawler_types.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetCrawlerTypeCapabilitiesResponseBodyCrawlerTypes(DaraModel):
    def __init__(
        self,
        default_scope_unit: str = None,
        display_name: str = None,
        require_resource_group: bool = None,
        support_ai_comment: bool = None,
        support_exclude_regex: bool = None,
        support_schedule: bool = None,
        supported_datasource_types: List[str] = None,
        supported_entity_types: List[main_models.GetCrawlerTypeCapabilitiesResponseBodyCrawlerTypesSupportedEntityTypes] = None,
        supported_option_keys: List[main_models.GetCrawlerTypeCapabilitiesResponseBodyCrawlerTypesSupportedOptionKeys] = None,
        supported_scope_units: List[str] = None,
        type: str = None,
    ):
        self.default_scope_unit = default_scope_unit
        self.display_name = display_name
        self.require_resource_group = require_resource_group
        self.support_ai_comment = support_ai_comment
        self.support_exclude_regex = support_exclude_regex
        self.support_schedule = support_schedule
        self.supported_datasource_types = supported_datasource_types
        self.supported_entity_types = supported_entity_types
        self.supported_option_keys = supported_option_keys
        self.supported_scope_units = supported_scope_units
        self.type = type

    def validate(self):
        if self.supported_entity_types:
            for v1 in self.supported_entity_types:
                 if v1:
                    v1.validate()
        if self.supported_option_keys:
            for v1 in self.supported_option_keys:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_scope_unit is not None:
            result['DefaultScopeUnit'] = self.default_scope_unit

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.require_resource_group is not None:
            result['RequireResourceGroup'] = self.require_resource_group

        if self.support_ai_comment is not None:
            result['SupportAiComment'] = self.support_ai_comment

        if self.support_exclude_regex is not None:
            result['SupportExcludeRegex'] = self.support_exclude_regex

        if self.support_schedule is not None:
            result['SupportSchedule'] = self.support_schedule

        if self.supported_datasource_types is not None:
            result['SupportedDatasourceTypes'] = self.supported_datasource_types

        result['SupportedEntityTypes'] = []
        if self.supported_entity_types is not None:
            for k1 in self.supported_entity_types:
                result['SupportedEntityTypes'].append(k1.to_map() if k1 else None)

        result['SupportedOptionKeys'] = []
        if self.supported_option_keys is not None:
            for k1 in self.supported_option_keys:
                result['SupportedOptionKeys'].append(k1.to_map() if k1 else None)

        if self.supported_scope_units is not None:
            result['SupportedScopeUnits'] = self.supported_scope_units

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultScopeUnit') is not None:
            self.default_scope_unit = m.get('DefaultScopeUnit')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('RequireResourceGroup') is not None:
            self.require_resource_group = m.get('RequireResourceGroup')

        if m.get('SupportAiComment') is not None:
            self.support_ai_comment = m.get('SupportAiComment')

        if m.get('SupportExcludeRegex') is not None:
            self.support_exclude_regex = m.get('SupportExcludeRegex')

        if m.get('SupportSchedule') is not None:
            self.support_schedule = m.get('SupportSchedule')

        if m.get('SupportedDatasourceTypes') is not None:
            self.supported_datasource_types = m.get('SupportedDatasourceTypes')

        self.supported_entity_types = []
        if m.get('SupportedEntityTypes') is not None:
            for k1 in m.get('SupportedEntityTypes'):
                temp_model = main_models.GetCrawlerTypeCapabilitiesResponseBodyCrawlerTypesSupportedEntityTypes()
                self.supported_entity_types.append(temp_model.from_map(k1))

        self.supported_option_keys = []
        if m.get('SupportedOptionKeys') is not None:
            for k1 in m.get('SupportedOptionKeys'):
                temp_model = main_models.GetCrawlerTypeCapabilitiesResponseBodyCrawlerTypesSupportedOptionKeys()
                self.supported_option_keys.append(temp_model.from_map(k1))

        if m.get('SupportedScopeUnits') is not None:
            self.supported_scope_units = m.get('SupportedScopeUnits')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class GetCrawlerTypeCapabilitiesResponseBodyCrawlerTypesSupportedOptionKeys(DaraModel):
    def __init__(
        self,
        allowed_values: List[str] = None,
        default_value: str = None,
        key: str = None,
        required: bool = None,
        value_type: str = None,
    ):
        self.allowed_values = allowed_values
        self.default_value = default_value
        self.key = key
        self.required = required
        self.value_type = value_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allowed_values is not None:
            result['AllowedValues'] = self.allowed_values

        if self.default_value is not None:
            result['DefaultValue'] = self.default_value

        if self.key is not None:
            result['Key'] = self.key

        if self.required is not None:
            result['Required'] = self.required

        if self.value_type is not None:
            result['ValueType'] = self.value_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowedValues') is not None:
            self.allowed_values = m.get('AllowedValues')

        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Required') is not None:
            self.required = m.get('Required')

        if m.get('ValueType') is not None:
            self.value_type = m.get('ValueType')

        return self

class GetCrawlerTypeCapabilitiesResponseBodyCrawlerTypesSupportedEntityTypes(DaraModel):
    def __init__(
        self,
        optional: bool = None,
        parent_sub_type: str = None,
        sub_type: str = None,
        type: str = None,
    ):
        self.optional = optional
        self.parent_sub_type = parent_sub_type
        self.sub_type = sub_type
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.optional is not None:
            result['Optional'] = self.optional

        if self.parent_sub_type is not None:
            result['ParentSubType'] = self.parent_sub_type

        if self.sub_type is not None:
            result['SubType'] = self.sub_type

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Optional') is not None:
            self.optional = m.get('Optional')

        if m.get('ParentSubType') is not None:
            self.parent_sub_type = m.get('ParentSubType')

        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

