# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class UpsertQualityWatchAlertRequest(DaraModel):
    def __init__(
        self,
        op_tenant_id: int = None,
        upsert_command: main_models.UpsertQualityWatchAlertRequestUpsertCommand = None,
    ):
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # This parameter is required.
        self.upsert_command = upsert_command

    def validate(self):
        if self.upsert_command:
            self.upsert_command.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.upsert_command is not None:
            result['UpsertCommand'] = self.upsert_command.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('UpsertCommand') is not None:
            temp_model = main_models.UpsertQualityWatchAlertRequestUpsertCommand()
            self.upsert_command = temp_model.from_map(m.get('UpsertCommand'))

        return self

class UpsertQualityWatchAlertRequestUpsertCommand(DaraModel):
    def __init__(
        self,
        quality_alert_info: main_models.UpsertQualityWatchAlertRequestUpsertCommandQualityAlertInfo = None,
        watch_id: int = None,
    ):
        # This parameter is required.
        self.quality_alert_info = quality_alert_info
        # This parameter is required.
        self.watch_id = watch_id

    def validate(self):
        if self.quality_alert_info:
            self.quality_alert_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.quality_alert_info is not None:
            result['QualityAlertInfo'] = self.quality_alert_info.to_map()

        if self.watch_id is not None:
            result['WatchId'] = self.watch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QualityAlertInfo') is not None:
            temp_model = main_models.UpsertQualityWatchAlertRequestUpsertCommandQualityAlertInfo()
            self.quality_alert_info = temp_model.from_map(m.get('QualityAlertInfo'))

        if m.get('WatchId') is not None:
            self.watch_id = m.get('WatchId')

        return self

class UpsertQualityWatchAlertRequestUpsertCommandQualityAlertInfo(DaraModel):
    def __init__(
        self,
        alert_duty_channel_list: List[str] = None,
        alert_duty_list: List[main_models.UpsertQualityWatchAlertRequestUpsertCommandQualityAlertInfoAlertDutyList] = None,
        alert_quality_owner_channel_list: List[str] = None,
        alert_user_channel_list: List[str] = None,
        alert_user_list: List[main_models.UpsertQualityWatchAlertRequestUpsertCommandQualityAlertInfoAlertUserList] = None,
        enable_alert_quality_owner: bool = None,
    ):
        self.alert_duty_channel_list = alert_duty_channel_list
        self.alert_duty_list = alert_duty_list
        self.alert_quality_owner_channel_list = alert_quality_owner_channel_list
        self.alert_user_channel_list = alert_user_channel_list
        self.alert_user_list = alert_user_list
        self.enable_alert_quality_owner = enable_alert_quality_owner

    def validate(self):
        if self.alert_duty_list:
            for v1 in self.alert_duty_list:
                 if v1:
                    v1.validate()
        if self.alert_user_list:
            for v1 in self.alert_user_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_duty_channel_list is not None:
            result['AlertDutyChannelList'] = self.alert_duty_channel_list

        result['AlertDutyList'] = []
        if self.alert_duty_list is not None:
            for k1 in self.alert_duty_list:
                result['AlertDutyList'].append(k1.to_map() if k1 else None)

        if self.alert_quality_owner_channel_list is not None:
            result['AlertQualityOwnerChannelList'] = self.alert_quality_owner_channel_list

        if self.alert_user_channel_list is not None:
            result['AlertUserChannelList'] = self.alert_user_channel_list

        result['AlertUserList'] = []
        if self.alert_user_list is not None:
            for k1 in self.alert_user_list:
                result['AlertUserList'].append(k1.to_map() if k1 else None)

        if self.enable_alert_quality_owner is not None:
            result['EnableAlertQualityOwner'] = self.enable_alert_quality_owner

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertDutyChannelList') is not None:
            self.alert_duty_channel_list = m.get('AlertDutyChannelList')

        self.alert_duty_list = []
        if m.get('AlertDutyList') is not None:
            for k1 in m.get('AlertDutyList'):
                temp_model = main_models.UpsertQualityWatchAlertRequestUpsertCommandQualityAlertInfoAlertDutyList()
                self.alert_duty_list.append(temp_model.from_map(k1))

        if m.get('AlertQualityOwnerChannelList') is not None:
            self.alert_quality_owner_channel_list = m.get('AlertQualityOwnerChannelList')

        if m.get('AlertUserChannelList') is not None:
            self.alert_user_channel_list = m.get('AlertUserChannelList')

        self.alert_user_list = []
        if m.get('AlertUserList') is not None:
            for k1 in m.get('AlertUserList'):
                temp_model = main_models.UpsertQualityWatchAlertRequestUpsertCommandQualityAlertInfoAlertUserList()
                self.alert_user_list.append(temp_model.from_map(k1))

        if m.get('EnableAlertQualityOwner') is not None:
            self.enable_alert_quality_owner = m.get('EnableAlertQualityOwner')

        return self

class UpsertQualityWatchAlertRequestUpsertCommandQualityAlertInfoAlertUserList(DaraModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
    ):
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class UpsertQualityWatchAlertRequestUpsertCommandQualityAlertInfoAlertDutyList(DaraModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
    ):
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

