# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class SubscriptionForSNSView(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        enable: bool = None,
        filter_setting: main_models.FilterSetting = None,
        mode: str = None,
        name: str = None,
        notify_strategy_uuid: str = None,
        region_id: str = None,
        subscribe_legacy_event: bool = None,
        subscription_type: str = None,
        sync_from_type: str = None,
        update_time: str = None,
        user_id: str = None,
        uuid: str = None,
        workspace: str = None,
        workspace_filter_setting: main_models.WorkspaceFilterSetting = None,
    ):
        # The time when the subscription was created.
        self.create_time = create_time
        # Indicates whether the subscription is enabled.
        self.enable = enable
        # The filter configuration.
        self.filter_setting = filter_setting
        # The lifecycle mode.
        self.mode = mode
        # The subscription name.
        self.name = name
        # The reverse association to the SNS (= snsUuid).
        self.notify_strategy_uuid = notify_strategy_uuid
        # The region ID.
        self.region_id = region_id
        # Indicates whether the subscription includes legacy product events (CMS 1.0, ARMS, or SLS events where workspace is null). Valid values: true: Subscribed. false or null: Not subscribed.
        self.subscribe_legacy_event = subscribe_legacy_event
        # The subscription type.
        self.subscription_type = subscription_type
        # The sync source type.
        self.sync_from_type = sync_from_type
        # The time when the subscription was last updated.
        self.update_time = update_time
        # The user ID of the owner.
        self.user_id = user_id
        # The subscription UUID.
        self.uuid = uuid
        # The workspace.
        self.workspace = workspace
        # The workspace filter configuration.
        self.workspace_filter_setting = workspace_filter_setting

    def validate(self):
        if self.filter_setting:
            self.filter_setting.validate()
        if self.workspace_filter_setting:
            self.workspace_filter_setting.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.enable is not None:
            result['enable'] = self.enable

        if self.filter_setting is not None:
            result['filterSetting'] = self.filter_setting.to_map()

        if self.mode is not None:
            result['mode'] = self.mode

        if self.name is not None:
            result['name'] = self.name

        if self.notify_strategy_uuid is not None:
            result['notifyStrategyUuid'] = self.notify_strategy_uuid

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.subscribe_legacy_event is not None:
            result['subscribeLegacyEvent'] = self.subscribe_legacy_event

        if self.subscription_type is not None:
            result['subscriptionType'] = self.subscription_type

        if self.sync_from_type is not None:
            result['syncFromType'] = self.sync_from_type

        if self.update_time is not None:
            result['updateTime'] = self.update_time

        if self.user_id is not None:
            result['userId'] = self.user_id

        if self.uuid is not None:
            result['uuid'] = self.uuid

        if self.workspace is not None:
            result['workspace'] = self.workspace

        if self.workspace_filter_setting is not None:
            result['workspaceFilterSetting'] = self.workspace_filter_setting.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('enable') is not None:
            self.enable = m.get('enable')

        if m.get('filterSetting') is not None:
            temp_model = main_models.FilterSetting()
            self.filter_setting = temp_model.from_map(m.get('filterSetting'))

        if m.get('mode') is not None:
            self.mode = m.get('mode')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('notifyStrategyUuid') is not None:
            self.notify_strategy_uuid = m.get('notifyStrategyUuid')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('subscribeLegacyEvent') is not None:
            self.subscribe_legacy_event = m.get('subscribeLegacyEvent')

        if m.get('subscriptionType') is not None:
            self.subscription_type = m.get('subscriptionType')

        if m.get('syncFromType') is not None:
            self.sync_from_type = m.get('syncFromType')

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        if m.get('uuid') is not None:
            self.uuid = m.get('uuid')

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        if m.get('workspaceFilterSetting') is not None:
            temp_model = main_models.WorkspaceFilterSetting()
            self.workspace_filter_setting = temp_model.from_map(m.get('workspaceFilterSetting'))

        return self

