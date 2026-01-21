# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class NotificationStrategy(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        escalation_setting: main_models.NotificationStrategyEscalationSetting = None,
        filter_setting: main_models.NotificationStrategyFilterSetting = None,
        grouping_setting: main_models.NotificationStrategyGroupingSetting = None,
        name: str = None,
        product: str = None,
        pushing_setting: main_models.NotificationStrategyPushingSetting = None,
        route_setting: main_models.NotificationStrategyRouteSetting = None,
        update_time: str = None,
        user_id: str = None,
        uuid: str = None,
    ):
        self.create_time = create_time
        self.description = description
        self.escalation_setting = escalation_setting
        self.filter_setting = filter_setting
        self.grouping_setting = grouping_setting
        # This parameter is required.
        self.name = name
        self.product = product
        self.pushing_setting = pushing_setting
        self.route_setting = route_setting
        self.update_time = update_time
        self.user_id = user_id
        self.uuid = uuid

    def validate(self):
        if self.escalation_setting:
            self.escalation_setting.validate()
        if self.filter_setting:
            self.filter_setting.validate()
        if self.grouping_setting:
            self.grouping_setting.validate()
        if self.pushing_setting:
            self.pushing_setting.validate()
        if self.route_setting:
            self.route_setting.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.escalation_setting is not None:
            result['EscalationSetting'] = self.escalation_setting.to_map()

        if self.filter_setting is not None:
            result['FilterSetting'] = self.filter_setting.to_map()

        if self.grouping_setting is not None:
            result['GroupingSetting'] = self.grouping_setting.to_map()

        if self.name is not None:
            result['Name'] = self.name

        if self.product is not None:
            result['Product'] = self.product

        if self.pushing_setting is not None:
            result['PushingSetting'] = self.pushing_setting.to_map()

        if self.route_setting is not None:
            result['RouteSetting'] = self.route_setting.to_map()

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EscalationSetting') is not None:
            temp_model = main_models.NotificationStrategyEscalationSetting()
            self.escalation_setting = temp_model.from_map(m.get('EscalationSetting'))

        if m.get('FilterSetting') is not None:
            temp_model = main_models.NotificationStrategyFilterSetting()
            self.filter_setting = temp_model.from_map(m.get('FilterSetting'))

        if m.get('GroupingSetting') is not None:
            temp_model = main_models.NotificationStrategyGroupingSetting()
            self.grouping_setting = temp_model.from_map(m.get('GroupingSetting'))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Product') is not None:
            self.product = m.get('Product')

        if m.get('PushingSetting') is not None:
            temp_model = main_models.NotificationStrategyPushingSetting()
            self.pushing_setting = temp_model.from_map(m.get('PushingSetting'))

        if m.get('RouteSetting') is not None:
            temp_model = main_models.NotificationStrategyRouteSetting()
            self.route_setting = temp_model.from_map(m.get('RouteSetting'))

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

class NotificationStrategyRouteSetting(DaraModel):
    def __init__(
        self,
        routes: List[main_models.NotificationStrategyRouteSettingRoutes] = None,
    ):
        self.routes = routes

    def validate(self):
        if self.routes:
            for v1 in self.routes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Routes'] = []
        if self.routes is not None:
            for k1 in self.routes:
                result['Routes'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.routes = []
        if m.get('Routes') is not None:
            for k1 in m.get('Routes'):
                temp_model = main_models.NotificationStrategyRouteSettingRoutes()
                self.routes.append(temp_model.from_map(k1))

        return self

class NotificationStrategyRouteSettingRoutes(DaraModel):
    def __init__(
        self,
        conditions: List[main_models.NotificationStrategyRouteSettingRoutesConditions] = None,
        escalation_uuid: str = None,
    ):
        self.conditions = conditions
        self.escalation_uuid = escalation_uuid

    def validate(self):
        if self.conditions:
            for v1 in self.conditions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Conditions'] = []
        if self.conditions is not None:
            for k1 in self.conditions:
                result['Conditions'].append(k1.to_map() if k1 else None)

        if self.escalation_uuid is not None:
            result['EscalationUuid'] = self.escalation_uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.conditions = []
        if m.get('Conditions') is not None:
            for k1 in m.get('Conditions'):
                temp_model = main_models.NotificationStrategyRouteSettingRoutesConditions()
                self.conditions.append(temp_model.from_map(k1))

        if m.get('EscalationUuid') is not None:
            self.escalation_uuid = m.get('EscalationUuid')

        return self

class NotificationStrategyRouteSettingRoutesConditions(DaraModel):
    def __init__(
        self,
        field: str = None,
        op: str = None,
        value: str = None,
    ):
        self.field = field
        self.op = op
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.field is not None:
            result['Field'] = self.field

        if self.op is not None:
            result['Op'] = self.op

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Field') is not None:
            self.field = m.get('Field')

        if m.get('Op') is not None:
            self.op = m.get('Op')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class NotificationStrategyPushingSetting(DaraModel):
    def __init__(
        self,
        pushing_data_format: str = None,
        range: str = None,
        target_uuids: List[str] = None,
        template_uuid: str = None,
    ):
        self.pushing_data_format = pushing_data_format
        self.range = range
        self.target_uuids = target_uuids
        self.template_uuid = template_uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.pushing_data_format is not None:
            result['PushingDataFormat'] = self.pushing_data_format

        if self.range is not None:
            result['Range'] = self.range

        if self.target_uuids is not None:
            result['TargetUuids'] = self.target_uuids

        if self.template_uuid is not None:
            result['TemplateUuid'] = self.template_uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PushingDataFormat') is not None:
            self.pushing_data_format = m.get('PushingDataFormat')

        if m.get('Range') is not None:
            self.range = m.get('Range')

        if m.get('TargetUuids') is not None:
            self.target_uuids = m.get('TargetUuids')

        if m.get('TemplateUuid') is not None:
            self.template_uuid = m.get('TemplateUuid')

        return self

class NotificationStrategyGroupingSetting(DaraModel):
    def __init__(
        self,
        enable_raw_alert_dispatching: bool = None,
        grouping_items: List[main_models.NotificationStrategyGroupingSettingGroupingItems] = None,
        period_min: int = None,
        silence_sec: int = None,
        times: int = None,
    ):
        self.enable_raw_alert_dispatching = enable_raw_alert_dispatching
        self.grouping_items = grouping_items
        self.period_min = period_min
        self.silence_sec = silence_sec
        self.times = times

    def validate(self):
        if self.grouping_items:
            for v1 in self.grouping_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_raw_alert_dispatching is not None:
            result['EnableRawAlertDispatching'] = self.enable_raw_alert_dispatching

        result['GroupingItems'] = []
        if self.grouping_items is not None:
            for k1 in self.grouping_items:
                result['GroupingItems'].append(k1.to_map() if k1 else None)

        if self.period_min is not None:
            result['PeriodMin'] = self.period_min

        if self.silence_sec is not None:
            result['SilenceSec'] = self.silence_sec

        if self.times is not None:
            result['Times'] = self.times

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableRawAlertDispatching') is not None:
            self.enable_raw_alert_dispatching = m.get('EnableRawAlertDispatching')

        self.grouping_items = []
        if m.get('GroupingItems') is not None:
            for k1 in m.get('GroupingItems'):
                temp_model = main_models.NotificationStrategyGroupingSettingGroupingItems()
                self.grouping_items.append(temp_model.from_map(k1))

        if m.get('PeriodMin') is not None:
            self.period_min = m.get('PeriodMin')

        if m.get('SilenceSec') is not None:
            self.silence_sec = m.get('SilenceSec')

        if m.get('Times') is not None:
            self.times = m.get('Times')

        return self

class NotificationStrategyGroupingSettingGroupingItems(DaraModel):
    def __init__(
        self,
        keys: List[str] = None,
        type: str = None,
    ):
        self.keys = keys
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.keys is not None:
            result['Keys'] = self.keys

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keys') is not None:
            self.keys = m.get('Keys')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class NotificationStrategyFilterSetting(DaraModel):
    def __init__(
        self,
        black_list: List[List[main_models.NotificationStrategyFilterSettingBlackList]] = None,
        white_list: List[List[main_models.NotificationStrategyFilterSettingWhiteList]] = None,
    ):
        self.black_list = black_list
        self.white_list = white_list

    def validate(self):
        if self.black_list:
            for v1 in self.black_list:
                for v2 in v1:
                     if v2:
                        v2.validate()
        if self.white_list:
            for v1 in self.white_list:
                for v2 in v1:
                     if v2:
                        v2.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BlackList'] = []
        if self.black_list is not None:
            for k1 in self.black_list:
                l1 = []
                for k2 in k1:
                    l1.append(k2.to_map() if k2 else None)
                result['BlackList'].append(l1)

        result['WhiteList'] = []
        if self.white_list is not None:
            for k1 in self.white_list:
                l1 = []
                for k2 in k1:
                    l1.append(k2.to_map() if k2 else None)
                result['WhiteList'].append(l1)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.black_list = []
        if m.get('BlackList') is not None:
            for k1 in m.get('BlackList'):
                l1 = []
                for k2 in k1:
                    temp_model = main_models.NotificationStrategyFilterSettingBlackList()
                    l1.append(temp_model.from_map(k2))
                self.black_list.append(l1)

        self.white_list = []
        if m.get('WhiteList') is not None:
            for k1 in m.get('WhiteList'):
                l1 = []
                for k2 in k1:
                    temp_model = main_models.NotificationStrategyFilterSettingWhiteList()
                    l1.append(temp_model.from_map(k2))
                self.white_list.append(l1)

        return self

class NotificationStrategyFilterSettingWhiteList(DaraModel):
    def __init__(
        self,
        field: str = None,
        op: str = None,
        value: str = None,
    ):
        # This parameter is required.
        self.field = field
        # This parameter is required.
        self.op = op
        # This parameter is required.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.field is not None:
            result['Field'] = self.field

        if self.op is not None:
            result['Op'] = self.op

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Field') is not None:
            self.field = m.get('Field')

        if m.get('Op') is not None:
            self.op = m.get('Op')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class NotificationStrategyFilterSettingBlackList(DaraModel):
    def __init__(
        self,
        field: str = None,
        op: str = None,
        value: str = None,
    ):
        # This parameter is required.
        self.field = field
        # This parameter is required.
        self.op = op
        # This parameter is required.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.field is not None:
            result['Field'] = self.field

        if self.op is not None:
            result['Op'] = self.op

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Field') is not None:
            self.field = m.get('Field')

        if m.get('Op') is not None:
            self.op = m.get('Op')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class NotificationStrategyEscalationSetting(DaraModel):
    def __init__(
        self,
        auto_resolve_min: int = None,
        custom_channels: List[main_models.NotificationStrategyEscalationSettingCustomChannels] = None,
        escalation_level: str = None,
        escalation_uuid: str = None,
        range: str = None,
        retrigger_min: int = None,
    ):
        self.auto_resolve_min = auto_resolve_min
        self.custom_channels = custom_channels
        self.escalation_level = escalation_level
        self.escalation_uuid = escalation_uuid
        self.range = range
        self.retrigger_min = retrigger_min

    def validate(self):
        if self.custom_channels:
            for v1 in self.custom_channels:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_resolve_min is not None:
            result['AutoResolveMin'] = self.auto_resolve_min

        result['CustomChannels'] = []
        if self.custom_channels is not None:
            for k1 in self.custom_channels:
                result['CustomChannels'].append(k1.to_map() if k1 else None)

        if self.escalation_level is not None:
            result['EscalationLevel'] = self.escalation_level

        if self.escalation_uuid is not None:
            result['EscalationUuid'] = self.escalation_uuid

        if self.range is not None:
            result['Range'] = self.range

        if self.retrigger_min is not None:
            result['RetriggerMin'] = self.retrigger_min

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoResolveMin') is not None:
            self.auto_resolve_min = m.get('AutoResolveMin')

        self.custom_channels = []
        if m.get('CustomChannels') is not None:
            for k1 in m.get('CustomChannels'):
                temp_model = main_models.NotificationStrategyEscalationSettingCustomChannels()
                self.custom_channels.append(temp_model.from_map(k1))

        if m.get('EscalationLevel') is not None:
            self.escalation_level = m.get('EscalationLevel')

        if m.get('EscalationUuid') is not None:
            self.escalation_uuid = m.get('EscalationUuid')

        if m.get('Range') is not None:
            self.range = m.get('Range')

        if m.get('RetriggerMin') is not None:
            self.retrigger_min = m.get('RetriggerMin')

        return self

class NotificationStrategyEscalationSettingCustomChannels(DaraModel):
    def __init__(
        self,
        channel_type: str = None,
        severities: List[str] = None,
        template_uuid: str = None,
    ):
        # This parameter is required.
        self.channel_type = channel_type
        self.severities = severities
        self.template_uuid = template_uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type

        if self.severities is not None:
            result['Severities'] = self.severities

        if self.template_uuid is not None:
            result['TemplateUuid'] = self.template_uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')

        if m.get('Severities') is not None:
            self.severities = m.get('Severities')

        if m.get('TemplateUuid') is not None:
            self.template_uuid = m.get('TemplateUuid')

        return self

