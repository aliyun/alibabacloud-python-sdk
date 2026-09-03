# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ChannelProperties(DaraModel):
    def __init__(
        self,
        channel_activity: str = None,
        channel_fcm: str = None,
        harmony_channel_category: str = None,
        huawei_channel_category: str = None,
        huawei_channel_importance: str = None,
        huawei_message_urgency: str = None,
        main_activity: str = None,
        oppo_category: str = None,
        oppo_channel_id: str = None,
        oppo_notify_level: str = None,
        use_huawei_message: str = None,
        use_huawei_plain_message: str = None,
        vivo_add_badge: str = None,
        vivo_category: str = None,
        vivo_push_mode: str = None,
        xiaomi_channel_id: str = None,
    ):
        self.channel_activity = channel_activity
        self.channel_fcm = channel_fcm
        self.harmony_channel_category = harmony_channel_category
        self.huawei_channel_category = huawei_channel_category
        self.huawei_channel_importance = huawei_channel_importance
        self.huawei_message_urgency = huawei_message_urgency
        self.main_activity = main_activity
        self.oppo_category = oppo_category
        self.oppo_channel_id = oppo_channel_id
        self.oppo_notify_level = oppo_notify_level
        self.use_huawei_message = use_huawei_message
        self.use_huawei_plain_message = use_huawei_plain_message
        self.vivo_add_badge = vivo_add_badge
        self.vivo_category = vivo_category
        self.vivo_push_mode = vivo_push_mode
        self.xiaomi_channel_id = xiaomi_channel_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel_activity is not None:
            result['channelActivity'] = self.channel_activity

        if self.channel_fcm is not None:
            result['channelFcm'] = self.channel_fcm

        if self.harmony_channel_category is not None:
            result['harmonyChannelCategory'] = self.harmony_channel_category

        if self.huawei_channel_category is not None:
            result['huaweiChannelCategory'] = self.huawei_channel_category

        if self.huawei_channel_importance is not None:
            result['huaweiChannelImportance'] = self.huawei_channel_importance

        if self.huawei_message_urgency is not None:
            result['huaweiMessageUrgency'] = self.huawei_message_urgency

        if self.main_activity is not None:
            result['mainActivity'] = self.main_activity

        if self.oppo_category is not None:
            result['oppoCategory'] = self.oppo_category

        if self.oppo_channel_id is not None:
            result['oppoChannelId'] = self.oppo_channel_id

        if self.oppo_notify_level is not None:
            result['oppoNotifyLevel'] = self.oppo_notify_level

        if self.use_huawei_message is not None:
            result['useHuaweiMessage'] = self.use_huawei_message

        if self.use_huawei_plain_message is not None:
            result['useHuaweiPlainMessage'] = self.use_huawei_plain_message

        if self.vivo_add_badge is not None:
            result['vivoAddBadge'] = self.vivo_add_badge

        if self.vivo_category is not None:
            result['vivoCategory'] = self.vivo_category

        if self.vivo_push_mode is not None:
            result['vivoPushMode'] = self.vivo_push_mode

        if self.xiaomi_channel_id is not None:
            result['xiaomiChannelId'] = self.xiaomi_channel_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('channelActivity') is not None:
            self.channel_activity = m.get('channelActivity')

        if m.get('channelFcm') is not None:
            self.channel_fcm = m.get('channelFcm')

        if m.get('harmonyChannelCategory') is not None:
            self.harmony_channel_category = m.get('harmonyChannelCategory')

        if m.get('huaweiChannelCategory') is not None:
            self.huawei_channel_category = m.get('huaweiChannelCategory')

        if m.get('huaweiChannelImportance') is not None:
            self.huawei_channel_importance = m.get('huaweiChannelImportance')

        if m.get('huaweiMessageUrgency') is not None:
            self.huawei_message_urgency = m.get('huaweiMessageUrgency')

        if m.get('mainActivity') is not None:
            self.main_activity = m.get('mainActivity')

        if m.get('oppoCategory') is not None:
            self.oppo_category = m.get('oppoCategory')

        if m.get('oppoChannelId') is not None:
            self.oppo_channel_id = m.get('oppoChannelId')

        if m.get('oppoNotifyLevel') is not None:
            self.oppo_notify_level = m.get('oppoNotifyLevel')

        if m.get('useHuaweiMessage') is not None:
            self.use_huawei_message = m.get('useHuaweiMessage')

        if m.get('useHuaweiPlainMessage') is not None:
            self.use_huawei_plain_message = m.get('useHuaweiPlainMessage')

        if m.get('vivoAddBadge') is not None:
            self.vivo_add_badge = m.get('vivoAddBadge')

        if m.get('vivoCategory') is not None:
            self.vivo_category = m.get('vivoCategory')

        if m.get('vivoPushMode') is not None:
            self.vivo_push_mode = m.get('vivoPushMode')

        if m.get('xiaomiChannelId') is not None:
            self.xiaomi_channel_id = m.get('xiaomiChannelId')

        return self

