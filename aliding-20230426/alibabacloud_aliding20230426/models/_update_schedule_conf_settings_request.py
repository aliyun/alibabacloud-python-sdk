# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class UpdateScheduleConfSettingsRequest(DaraModel):
    def __init__(
        self,
        schedule_conf_setting_model: main_models.UpdateScheduleConfSettingsRequestScheduleConfSettingModel = None,
        schedule_conference_id: str = None,
        tenant_context: main_models.UpdateScheduleConfSettingsRequestTenantContext = None,
    ):
        self.schedule_conf_setting_model = schedule_conf_setting_model
        self.schedule_conference_id = schedule_conference_id
        self.tenant_context = tenant_context

    def validate(self):
        if self.schedule_conf_setting_model:
            self.schedule_conf_setting_model.validate()
        if self.tenant_context:
            self.tenant_context.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.schedule_conf_setting_model is not None:
            result['ScheduleConfSettingModel'] = self.schedule_conf_setting_model.to_map()

        if self.schedule_conference_id is not None:
            result['ScheduleConferenceId'] = self.schedule_conference_id

        if self.tenant_context is not None:
            result['TenantContext'] = self.tenant_context.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ScheduleConfSettingModel') is not None:
            temp_model = main_models.UpdateScheduleConfSettingsRequestScheduleConfSettingModel()
            self.schedule_conf_setting_model = temp_model.from_map(m.get('ScheduleConfSettingModel'))

        if m.get('ScheduleConferenceId') is not None:
            self.schedule_conference_id = m.get('ScheduleConferenceId')

        if m.get('TenantContext') is not None:
            temp_model = main_models.UpdateScheduleConfSettingsRequestTenantContext()
            self.tenant_context = temp_model.from_map(m.get('TenantContext'))

        return self

class UpdateScheduleConfSettingsRequestTenantContext(DaraModel):
    def __init__(
        self,
        tenant_id: str = None,
    ):
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

class UpdateScheduleConfSettingsRequestScheduleConfSettingModel(DaraModel):
    def __init__(
        self,
        cohost_user_ids: List[str] = None,
        conf_allowed_corp_id: str = None,
        host_user_id: str = None,
        lock_room: int = None,
        mozi_conf_open_record_setting: main_models.UpdateScheduleConfSettingsRequestScheduleConfSettingModelMoziConfOpenRecordSetting = None,
        mozi_conf_virtual_extra_setting: main_models.UpdateScheduleConfSettingsRequestScheduleConfSettingModelMoziConfVirtualExtraSetting = None,
        mute_on_join: int = None,
        screen_share_forbidden: int = None,
    ):
        self.cohost_user_ids = cohost_user_ids
        self.conf_allowed_corp_id = conf_allowed_corp_id
        self.host_user_id = host_user_id
        self.lock_room = lock_room
        self.mozi_conf_open_record_setting = mozi_conf_open_record_setting
        self.mozi_conf_virtual_extra_setting = mozi_conf_virtual_extra_setting
        self.mute_on_join = mute_on_join
        self.screen_share_forbidden = screen_share_forbidden

    def validate(self):
        if self.mozi_conf_open_record_setting:
            self.mozi_conf_open_record_setting.validate()
        if self.mozi_conf_virtual_extra_setting:
            self.mozi_conf_virtual_extra_setting.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cohost_user_ids is not None:
            result['CohostUserIds'] = self.cohost_user_ids

        if self.conf_allowed_corp_id is not None:
            result['ConfAllowedCorpId'] = self.conf_allowed_corp_id

        if self.host_user_id is not None:
            result['HostUserId'] = self.host_user_id

        if self.lock_room is not None:
            result['LockRoom'] = self.lock_room

        if self.mozi_conf_open_record_setting is not None:
            result['MoziConfOpenRecordSetting'] = self.mozi_conf_open_record_setting.to_map()

        if self.mozi_conf_virtual_extra_setting is not None:
            result['MoziConfVirtualExtraSetting'] = self.mozi_conf_virtual_extra_setting.to_map()

        if self.mute_on_join is not None:
            result['MuteOnJoin'] = self.mute_on_join

        if self.screen_share_forbidden is not None:
            result['ScreenShareForbidden'] = self.screen_share_forbidden

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CohostUserIds') is not None:
            self.cohost_user_ids = m.get('CohostUserIds')

        if m.get('ConfAllowedCorpId') is not None:
            self.conf_allowed_corp_id = m.get('ConfAllowedCorpId')

        if m.get('HostUserId') is not None:
            self.host_user_id = m.get('HostUserId')

        if m.get('LockRoom') is not None:
            self.lock_room = m.get('LockRoom')

        if m.get('MoziConfOpenRecordSetting') is not None:
            temp_model = main_models.UpdateScheduleConfSettingsRequestScheduleConfSettingModelMoziConfOpenRecordSetting()
            self.mozi_conf_open_record_setting = temp_model.from_map(m.get('MoziConfOpenRecordSetting'))

        if m.get('MoziConfVirtualExtraSetting') is not None:
            temp_model = main_models.UpdateScheduleConfSettingsRequestScheduleConfSettingModelMoziConfVirtualExtraSetting()
            self.mozi_conf_virtual_extra_setting = temp_model.from_map(m.get('MoziConfVirtualExtraSetting'))

        if m.get('MuteOnJoin') is not None:
            self.mute_on_join = m.get('MuteOnJoin')

        if m.get('ScreenShareForbidden') is not None:
            self.screen_share_forbidden = m.get('ScreenShareForbidden')

        return self

class UpdateScheduleConfSettingsRequestScheduleConfSettingModelMoziConfVirtualExtraSetting(DaraModel):
    def __init__(
        self,
        cloud_record_owner_user_id: str = None,
        enable_chat: int = None,
        enable_web_anonymous_join: bool = None,
        join_before_host: int = None,
        lock_media_status_mic_mute: int = None,
        lock_nick: int = None,
        minutes_owner_user_id: str = None,
        mozi_conf_extension_app_settings: List[main_models.UpdateScheduleConfSettingsRequestScheduleConfSettingModelMoziConfVirtualExtraSettingMoziConfExtensionAppSettings] = None,
        push_all_meeting_records: bool = None,
        push_cloud_record_card: bool = None,
        push_minutes_card: bool = None,
        waiting_room: int = None,
    ):
        self.cloud_record_owner_user_id = cloud_record_owner_user_id
        self.enable_chat = enable_chat
        self.enable_web_anonymous_join = enable_web_anonymous_join
        self.join_before_host = join_before_host
        self.lock_media_status_mic_mute = lock_media_status_mic_mute
        self.lock_nick = lock_nick
        self.minutes_owner_user_id = minutes_owner_user_id
        self.mozi_conf_extension_app_settings = mozi_conf_extension_app_settings
        self.push_all_meeting_records = push_all_meeting_records
        self.push_cloud_record_card = push_cloud_record_card
        self.push_minutes_card = push_minutes_card
        self.waiting_room = waiting_room

    def validate(self):
        if self.mozi_conf_extension_app_settings:
            for v1 in self.mozi_conf_extension_app_settings:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cloud_record_owner_user_id is not None:
            result['CloudRecordOwnerUserId'] = self.cloud_record_owner_user_id

        if self.enable_chat is not None:
            result['EnableChat'] = self.enable_chat

        if self.enable_web_anonymous_join is not None:
            result['EnableWebAnonymousJoin'] = self.enable_web_anonymous_join

        if self.join_before_host is not None:
            result['JoinBeforeHost'] = self.join_before_host

        if self.lock_media_status_mic_mute is not None:
            result['LockMediaStatusMicMute'] = self.lock_media_status_mic_mute

        if self.lock_nick is not None:
            result['LockNick'] = self.lock_nick

        if self.minutes_owner_user_id is not None:
            result['MinutesOwnerUserId'] = self.minutes_owner_user_id

        result['MoziConfExtensionAppSettings'] = []
        if self.mozi_conf_extension_app_settings is not None:
            for k1 in self.mozi_conf_extension_app_settings:
                result['MoziConfExtensionAppSettings'].append(k1.to_map() if k1 else None)

        if self.push_all_meeting_records is not None:
            result['PushAllMeetingRecords'] = self.push_all_meeting_records

        if self.push_cloud_record_card is not None:
            result['PushCloudRecordCard'] = self.push_cloud_record_card

        if self.push_minutes_card is not None:
            result['PushMinutesCard'] = self.push_minutes_card

        if self.waiting_room is not None:
            result['WaitingRoom'] = self.waiting_room

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CloudRecordOwnerUserId') is not None:
            self.cloud_record_owner_user_id = m.get('CloudRecordOwnerUserId')

        if m.get('EnableChat') is not None:
            self.enable_chat = m.get('EnableChat')

        if m.get('EnableWebAnonymousJoin') is not None:
            self.enable_web_anonymous_join = m.get('EnableWebAnonymousJoin')

        if m.get('JoinBeforeHost') is not None:
            self.join_before_host = m.get('JoinBeforeHost')

        if m.get('LockMediaStatusMicMute') is not None:
            self.lock_media_status_mic_mute = m.get('LockMediaStatusMicMute')

        if m.get('LockNick') is not None:
            self.lock_nick = m.get('LockNick')

        if m.get('MinutesOwnerUserId') is not None:
            self.minutes_owner_user_id = m.get('MinutesOwnerUserId')

        self.mozi_conf_extension_app_settings = []
        if m.get('MoziConfExtensionAppSettings') is not None:
            for k1 in m.get('MoziConfExtensionAppSettings'):
                temp_model = main_models.UpdateScheduleConfSettingsRequestScheduleConfSettingModelMoziConfVirtualExtraSettingMoziConfExtensionAppSettings()
                self.mozi_conf_extension_app_settings.append(temp_model.from_map(k1))

        if m.get('PushAllMeetingRecords') is not None:
            self.push_all_meeting_records = m.get('PushAllMeetingRecords')

        if m.get('PushCloudRecordCard') is not None:
            self.push_cloud_record_card = m.get('PushCloudRecordCard')

        if m.get('PushMinutesCard') is not None:
            self.push_minutes_card = m.get('PushMinutesCard')

        if m.get('WaitingRoom') is not None:
            self.waiting_room = m.get('WaitingRoom')

        return self

class UpdateScheduleConfSettingsRequestScheduleConfSettingModelMoziConfVirtualExtraSettingMoziConfExtensionAppSettings(DaraModel):
    def __init__(
        self,
        auto_open_mode: int = None,
        cool_app_code: str = None,
        extension_app_biz_data: str = None,
    ):
        self.auto_open_mode = auto_open_mode
        self.cool_app_code = cool_app_code
        self.extension_app_biz_data = extension_app_biz_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_open_mode is not None:
            result['AutoOpenMode'] = self.auto_open_mode

        if self.cool_app_code is not None:
            result['CoolAppCode'] = self.cool_app_code

        if self.extension_app_biz_data is not None:
            result['ExtensionAppBizData'] = self.extension_app_biz_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoOpenMode') is not None:
            self.auto_open_mode = m.get('AutoOpenMode')

        if m.get('CoolAppCode') is not None:
            self.cool_app_code = m.get('CoolAppCode')

        if m.get('ExtensionAppBizData') is not None:
            self.extension_app_biz_data = m.get('ExtensionAppBizData')

        return self

class UpdateScheduleConfSettingsRequestScheduleConfSettingModelMoziConfOpenRecordSetting(DaraModel):
    def __init__(
        self,
        is_follow_host: bool = None,
        mode: str = None,
        record_auto_start: int = None,
        record_auto_start_type: int = None,
    ):
        self.is_follow_host = is_follow_host
        self.mode = mode
        self.record_auto_start = record_auto_start
        self.record_auto_start_type = record_auto_start_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_follow_host is not None:
            result['IsFollowHost'] = self.is_follow_host

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.record_auto_start is not None:
            result['RecordAutoStart'] = self.record_auto_start

        if self.record_auto_start_type is not None:
            result['RecordAutoStartType'] = self.record_auto_start_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsFollowHost') is not None:
            self.is_follow_host = m.get('IsFollowHost')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('RecordAutoStart') is not None:
            self.record_auto_start = m.get('RecordAutoStart')

        if m.get('RecordAutoStartType') is not None:
            self.record_auto_start_type = m.get('RecordAutoStartType')

        return self

