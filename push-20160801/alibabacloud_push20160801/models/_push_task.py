# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_push20160801 import models as main_models
from darabonba.model import DaraModel

class PushTask(DaraModel):
    def __init__(
        self,
        action: str = None,
        message: main_models.PushTaskMessage = None,
        notification: main_models.PushTaskNotification = None,
        options: main_models.PushTaskOptions = None,
        target: main_models.PushTaskTarget = None,
    ):
        self.action = action
        self.message = message
        self.notification = notification
        self.options = options
        self.target = target

    def validate(self):
        if self.message:
            self.message.validate()
        if self.notification:
            self.notification.validate()
        if self.options:
            self.options.validate()
        if self.target:
            self.target.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        if self.message is not None:
            result['Message'] = self.message.to_map()

        if self.notification is not None:
            result['Notification'] = self.notification.to_map()

        if self.options is not None:
            result['Options'] = self.options.to_map()

        if self.target is not None:
            result['Target'] = self.target.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        if m.get('Message') is not None:
            temp_model = main_models.PushTaskMessage()
            self.message = temp_model.from_map(m.get('Message'))

        if m.get('Notification') is not None:
            temp_model = main_models.PushTaskNotification()
            self.notification = temp_model.from_map(m.get('Notification'))

        if m.get('Options') is not None:
            temp_model = main_models.PushTaskOptions()
            self.options = temp_model.from_map(m.get('Options'))

        if m.get('Target') is not None:
            temp_model = main_models.PushTaskTarget()
            self.target = temp_model.from_map(m.get('Target'))

        return self

class PushTaskTarget(DaraModel):
    def __init__(
        self,
        platform: str = None,
        type: str = None,
        value: str = None,
    ):
        self.platform = platform
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.platform is not None:
            result['Platform'] = self.platform

        if self.type is not None:
            result['Type'] = self.type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class PushTaskOptions(DaraModel):
    def __init__(
        self,
        expire_time: str = None,
        job_key: str = None,
        message_id: int = None,
        push_time: str = None,
        sms: main_models.PushTaskOptionsSms = None,
        trim: bool = None,
        use_channels: str = None,
    ):
        self.expire_time = expire_time
        self.job_key = job_key
        self.message_id = message_id
        self.push_time = push_time
        self.sms = sms
        self.trim = trim
        self.use_channels = use_channels

    def validate(self):
        if self.sms:
            self.sms.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.job_key is not None:
            result['JobKey'] = self.job_key

        if self.message_id is not None:
            result['MessageId'] = self.message_id

        if self.push_time is not None:
            result['PushTime'] = self.push_time

        if self.sms is not None:
            result['Sms'] = self.sms.to_map()

        if self.trim is not None:
            result['Trim'] = self.trim

        if self.use_channels is not None:
            result['UseChannels'] = self.use_channels

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('JobKey') is not None:
            self.job_key = m.get('JobKey')

        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')

        if m.get('PushTime') is not None:
            self.push_time = m.get('PushTime')

        if m.get('Sms') is not None:
            temp_model = main_models.PushTaskOptionsSms()
            self.sms = temp_model.from_map(m.get('Sms'))

        if m.get('Trim') is not None:
            self.trim = m.get('Trim')

        if m.get('UseChannels') is not None:
            self.use_channels = m.get('UseChannels')

        return self

class PushTaskOptionsSms(DaraModel):
    def __init__(
        self,
        delay_secs: int = None,
        params: str = None,
        send_policy: str = None,
        sign_name: str = None,
        template_name: str = None,
    ):
        self.delay_secs = delay_secs
        self.params = params
        self.send_policy = send_policy
        self.sign_name = sign_name
        self.template_name = template_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.delay_secs is not None:
            result['DelaySecs'] = self.delay_secs

        if self.params is not None:
            result['Params'] = self.params

        if self.send_policy is not None:
            result['SendPolicy'] = self.send_policy

        if self.sign_name is not None:
            result['SignName'] = self.sign_name

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DelaySecs') is not None:
            self.delay_secs = m.get('DelaySecs')

        if m.get('Params') is not None:
            self.params = m.get('Params')

        if m.get('SendPolicy') is not None:
            self.send_policy = m.get('SendPolicy')

        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        return self

class PushTaskNotification(DaraModel):
    def __init__(
        self,
        android: main_models.PushTaskNotificationAndroid = None,
        body: str = None,
        hmos: main_models.PushTaskNotificationHmos = None,
        ios: main_models.PushTaskNotificationIos = None,
        title: str = None,
    ):
        self.android = android
        self.body = body
        self.hmos = hmos
        self.ios = ios
        self.title = title

    def validate(self):
        if self.android:
            self.android.validate()
        if self.hmos:
            self.hmos.validate()
        if self.ios:
            self.ios.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.android is not None:
            result['Android'] = self.android.to_map()

        if self.body is not None:
            result['Body'] = self.body

        if self.hmos is not None:
            result['Hmos'] = self.hmos.to_map()

        if self.ios is not None:
            result['Ios'] = self.ios.to_map()

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Android') is not None:
            temp_model = main_models.PushTaskNotificationAndroid()
            self.android = temp_model.from_map(m.get('Android'))

        if m.get('Body') is not None:
            self.body = m.get('Body')

        if m.get('Hmos') is not None:
            temp_model = main_models.PushTaskNotificationHmos()
            self.hmos = temp_model.from_map(m.get('Hmos'))

        if m.get('Ios') is not None:
            temp_model = main_models.PushTaskNotificationIos()
            self.ios = temp_model.from_map(m.get('Ios'))

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

class PushTaskNotificationIos(DaraModel):
    def __init__(
        self,
        apns_env: str = None,
        badge: int = None,
        badge_auto_increment: bool = None,
        category: str = None,
        collapse_id: str = None,
        ext_parameters: str = None,
        interruption_level: str = None,
        live_activity: main_models.PushTaskNotificationIosLiveActivity = None,
        music: str = None,
        mutable: bool = None,
        relevance_score: float = None,
        silent: bool = None,
        subtitle: str = None,
        thread_id: str = None,
    ):
        self.apns_env = apns_env
        self.badge = badge
        self.badge_auto_increment = badge_auto_increment
        self.category = category
        self.collapse_id = collapse_id
        self.ext_parameters = ext_parameters
        self.interruption_level = interruption_level
        self.live_activity = live_activity
        self.music = music
        self.mutable = mutable
        self.relevance_score = relevance_score
        self.silent = silent
        self.subtitle = subtitle
        self.thread_id = thread_id

    def validate(self):
        if self.live_activity:
            self.live_activity.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apns_env is not None:
            result['ApnsEnv'] = self.apns_env

        if self.badge is not None:
            result['Badge'] = self.badge

        if self.badge_auto_increment is not None:
            result['BadgeAutoIncrement'] = self.badge_auto_increment

        if self.category is not None:
            result['Category'] = self.category

        if self.collapse_id is not None:
            result['CollapseId'] = self.collapse_id

        if self.ext_parameters is not None:
            result['ExtParameters'] = self.ext_parameters

        if self.interruption_level is not None:
            result['InterruptionLevel'] = self.interruption_level

        if self.live_activity is not None:
            result['LiveActivity'] = self.live_activity.to_map()

        if self.music is not None:
            result['Music'] = self.music

        if self.mutable is not None:
            result['Mutable'] = self.mutable

        if self.relevance_score is not None:
            result['RelevanceScore'] = self.relevance_score

        if self.silent is not None:
            result['Silent'] = self.silent

        if self.subtitle is not None:
            result['Subtitle'] = self.subtitle

        if self.thread_id is not None:
            result['ThreadId'] = self.thread_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApnsEnv') is not None:
            self.apns_env = m.get('ApnsEnv')

        if m.get('Badge') is not None:
            self.badge = m.get('Badge')

        if m.get('BadgeAutoIncrement') is not None:
            self.badge_auto_increment = m.get('BadgeAutoIncrement')

        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('CollapseId') is not None:
            self.collapse_id = m.get('CollapseId')

        if m.get('ExtParameters') is not None:
            self.ext_parameters = m.get('ExtParameters')

        if m.get('InterruptionLevel') is not None:
            self.interruption_level = m.get('InterruptionLevel')

        if m.get('LiveActivity') is not None:
            temp_model = main_models.PushTaskNotificationIosLiveActivity()
            self.live_activity = temp_model.from_map(m.get('LiveActivity'))

        if m.get('Music') is not None:
            self.music = m.get('Music')

        if m.get('Mutable') is not None:
            self.mutable = m.get('Mutable')

        if m.get('RelevanceScore') is not None:
            self.relevance_score = m.get('RelevanceScore')

        if m.get('Silent') is not None:
            self.silent = m.get('Silent')

        if m.get('Subtitle') is not None:
            self.subtitle = m.get('Subtitle')

        if m.get('ThreadId') is not None:
            self.thread_id = m.get('ThreadId')

        return self

class PushTaskNotificationIosLiveActivity(DaraModel):
    def __init__(
        self,
        attributes: str = None,
        attributes_type: str = None,
        content_state: str = None,
        dismissal_date: int = None,
        event: str = None,
        id: str = None,
        stale_date: int = None,
    ):
        self.attributes = attributes
        self.attributes_type = attributes_type
        self.content_state = content_state
        self.dismissal_date = dismissal_date
        self.event = event
        self.id = id
        self.stale_date = stale_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attributes is not None:
            result['Attributes'] = self.attributes

        if self.attributes_type is not None:
            result['AttributesType'] = self.attributes_type

        if self.content_state is not None:
            result['ContentState'] = self.content_state

        if self.dismissal_date is not None:
            result['DismissalDate'] = self.dismissal_date

        if self.event is not None:
            result['Event'] = self.event

        if self.id is not None:
            result['Id'] = self.id

        if self.stale_date is not None:
            result['StaleDate'] = self.stale_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')

        if m.get('AttributesType') is not None:
            self.attributes_type = m.get('AttributesType')

        if m.get('ContentState') is not None:
            self.content_state = m.get('ContentState')

        if m.get('DismissalDate') is not None:
            self.dismissal_date = m.get('DismissalDate')

        if m.get('Event') is not None:
            self.event = m.get('Event')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('StaleDate') is not None:
            self.stale_date = m.get('StaleDate')

        return self

class PushTaskNotificationHmos(DaraModel):
    def __init__(
        self,
        action: str = None,
        badge_add_num: int = None,
        badge_set_num: int = None,
        category: str = None,
        ext_parameters: str = None,
        extension_extra_data: str = None,
        extension_push: bool = None,
        image_url: str = None,
        inbox_content: List[str] = None,
        live_view_payload: str = None,
        notify_id: int = None,
        receipt_id: str = None,
        render_style: str = None,
        slot_type: str = None,
        sound: str = None,
        sound_duration: int = None,
        test_message: bool = None,
        uri: str = None,
    ):
        self.action = action
        self.badge_add_num = badge_add_num
        self.badge_set_num = badge_set_num
        self.category = category
        self.ext_parameters = ext_parameters
        self.extension_extra_data = extension_extra_data
        self.extension_push = extension_push
        self.image_url = image_url
        self.inbox_content = inbox_content
        self.live_view_payload = live_view_payload
        self.notify_id = notify_id
        self.receipt_id = receipt_id
        self.render_style = render_style
        self.slot_type = slot_type
        self.sound = sound
        self.sound_duration = sound_duration
        self.test_message = test_message
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        if self.badge_add_num is not None:
            result['BadgeAddNum'] = self.badge_add_num

        if self.badge_set_num is not None:
            result['BadgeSetNum'] = self.badge_set_num

        if self.category is not None:
            result['Category'] = self.category

        if self.ext_parameters is not None:
            result['ExtParameters'] = self.ext_parameters

        if self.extension_extra_data is not None:
            result['ExtensionExtraData'] = self.extension_extra_data

        if self.extension_push is not None:
            result['ExtensionPush'] = self.extension_push

        if self.image_url is not None:
            result['ImageUrl'] = self.image_url

        if self.inbox_content is not None:
            result['InboxContent'] = self.inbox_content

        if self.live_view_payload is not None:
            result['LiveViewPayload'] = self.live_view_payload

        if self.notify_id is not None:
            result['NotifyId'] = self.notify_id

        if self.receipt_id is not None:
            result['ReceiptId'] = self.receipt_id

        if self.render_style is not None:
            result['RenderStyle'] = self.render_style

        if self.slot_type is not None:
            result['SlotType'] = self.slot_type

        if self.sound is not None:
            result['Sound'] = self.sound

        if self.sound_duration is not None:
            result['SoundDuration'] = self.sound_duration

        if self.test_message is not None:
            result['TestMessage'] = self.test_message

        if self.uri is not None:
            result['Uri'] = self.uri

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        if m.get('BadgeAddNum') is not None:
            self.badge_add_num = m.get('BadgeAddNum')

        if m.get('BadgeSetNum') is not None:
            self.badge_set_num = m.get('BadgeSetNum')

        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('ExtParameters') is not None:
            self.ext_parameters = m.get('ExtParameters')

        if m.get('ExtensionExtraData') is not None:
            self.extension_extra_data = m.get('ExtensionExtraData')

        if m.get('ExtensionPush') is not None:
            self.extension_push = m.get('ExtensionPush')

        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')

        if m.get('InboxContent') is not None:
            self.inbox_content = m.get('InboxContent')

        if m.get('LiveViewPayload') is not None:
            self.live_view_payload = m.get('LiveViewPayload')

        if m.get('NotifyId') is not None:
            self.notify_id = m.get('NotifyId')

        if m.get('ReceiptId') is not None:
            self.receipt_id = m.get('ReceiptId')

        if m.get('RenderStyle') is not None:
            self.render_style = m.get('RenderStyle')

        if m.get('SlotType') is not None:
            self.slot_type = m.get('SlotType')

        if m.get('Sound') is not None:
            self.sound = m.get('Sound')

        if m.get('SoundDuration') is not None:
            self.sound_duration = m.get('SoundDuration')

        if m.get('TestMessage') is not None:
            self.test_message = m.get('TestMessage')

        if m.get('Uri') is not None:
            self.uri = m.get('Uri')

        return self

class PushTaskNotificationAndroid(DaraModel):
    def __init__(
        self,
        badge_activity: str = None,
        badge_add_num: int = None,
        badge_set_num: int = None,
        channel_id: str = None,
        ext_parameters: str = None,
        group_id: str = None,
        image_url: str = None,
        inbox_content: List[str] = None,
        music: str = None,
        notify_id: int = None,
        options: main_models.PushTaskNotificationAndroidOptions = None,
        picture_url: str = None,
        render_style: str = None,
        test_message: bool = None,
        vendor_channel_activity: str = None,
    ):
        self.badge_activity = badge_activity
        self.badge_add_num = badge_add_num
        self.badge_set_num = badge_set_num
        self.channel_id = channel_id
        self.ext_parameters = ext_parameters
        self.group_id = group_id
        self.image_url = image_url
        self.inbox_content = inbox_content
        self.music = music
        self.notify_id = notify_id
        self.options = options
        self.picture_url = picture_url
        self.render_style = render_style
        self.test_message = test_message
        self.vendor_channel_activity = vendor_channel_activity

    def validate(self):
        if self.options:
            self.options.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.badge_activity is not None:
            result['BadgeActivity'] = self.badge_activity

        if self.badge_add_num is not None:
            result['BadgeAddNum'] = self.badge_add_num

        if self.badge_set_num is not None:
            result['BadgeSetNum'] = self.badge_set_num

        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id

        if self.ext_parameters is not None:
            result['ExtParameters'] = self.ext_parameters

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.image_url is not None:
            result['ImageUrl'] = self.image_url

        if self.inbox_content is not None:
            result['InboxContent'] = self.inbox_content

        if self.music is not None:
            result['Music'] = self.music

        if self.notify_id is not None:
            result['NotifyId'] = self.notify_id

        if self.options is not None:
            result['Options'] = self.options.to_map()

        if self.picture_url is not None:
            result['PictureUrl'] = self.picture_url

        if self.render_style is not None:
            result['RenderStyle'] = self.render_style

        if self.test_message is not None:
            result['TestMessage'] = self.test_message

        if self.vendor_channel_activity is not None:
            result['VendorChannelActivity'] = self.vendor_channel_activity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BadgeActivity') is not None:
            self.badge_activity = m.get('BadgeActivity')

        if m.get('BadgeAddNum') is not None:
            self.badge_add_num = m.get('BadgeAddNum')

        if m.get('BadgeSetNum') is not None:
            self.badge_set_num = m.get('BadgeSetNum')

        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        if m.get('ExtParameters') is not None:
            self.ext_parameters = m.get('ExtParameters')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')

        if m.get('InboxContent') is not None:
            self.inbox_content = m.get('InboxContent')

        if m.get('Music') is not None:
            self.music = m.get('Music')

        if m.get('NotifyId') is not None:
            self.notify_id = m.get('NotifyId')

        if m.get('Options') is not None:
            temp_model = main_models.PushTaskNotificationAndroidOptions()
            self.options = temp_model.from_map(m.get('Options'))

        if m.get('PictureUrl') is not None:
            self.picture_url = m.get('PictureUrl')

        if m.get('RenderStyle') is not None:
            self.render_style = m.get('RenderStyle')

        if m.get('TestMessage') is not None:
            self.test_message = m.get('TestMessage')

        if m.get('VendorChannelActivity') is not None:
            self.vendor_channel_activity = m.get('VendorChannelActivity')

        return self

class PushTaskNotificationAndroidOptions(DaraModel):
    def __init__(
        self,
        accs: main_models.PushTaskNotificationAndroidOptionsAccs = None,
        honor: main_models.PushTaskNotificationAndroidOptionsHonor = None,
        huawei: main_models.PushTaskNotificationAndroidOptionsHuawei = None,
        meizu: main_models.PushTaskNotificationAndroidOptionsMeizu = None,
        oppo: main_models.PushTaskNotificationAndroidOptionsOppo = None,
        vivo: main_models.PushTaskNotificationAndroidOptionsVivo = None,
        xiaomi: main_models.PushTaskNotificationAndroidOptionsXiaomi = None,
    ):
        self.accs = accs
        self.honor = honor
        self.huawei = huawei
        self.meizu = meizu
        self.oppo = oppo
        self.vivo = vivo
        self.xiaomi = xiaomi

    def validate(self):
        if self.accs:
            self.accs.validate()
        if self.honor:
            self.honor.validate()
        if self.huawei:
            self.huawei.validate()
        if self.meizu:
            self.meizu.validate()
        if self.oppo:
            self.oppo.validate()
        if self.vivo:
            self.vivo.validate()
        if self.xiaomi:
            self.xiaomi.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accs is not None:
            result['Accs'] = self.accs.to_map()

        if self.honor is not None:
            result['Honor'] = self.honor.to_map()

        if self.huawei is not None:
            result['Huawei'] = self.huawei.to_map()

        if self.meizu is not None:
            result['Meizu'] = self.meizu.to_map()

        if self.oppo is not None:
            result['Oppo'] = self.oppo.to_map()

        if self.vivo is not None:
            result['Vivo'] = self.vivo.to_map()

        if self.xiaomi is not None:
            result['Xiaomi'] = self.xiaomi.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accs') is not None:
            temp_model = main_models.PushTaskNotificationAndroidOptionsAccs()
            self.accs = temp_model.from_map(m.get('Accs'))

        if m.get('Honor') is not None:
            temp_model = main_models.PushTaskNotificationAndroidOptionsHonor()
            self.honor = temp_model.from_map(m.get('Honor'))

        if m.get('Huawei') is not None:
            temp_model = main_models.PushTaskNotificationAndroidOptionsHuawei()
            self.huawei = temp_model.from_map(m.get('Huawei'))

        if m.get('Meizu') is not None:
            temp_model = main_models.PushTaskNotificationAndroidOptionsMeizu()
            self.meizu = temp_model.from_map(m.get('Meizu'))

        if m.get('Oppo') is not None:
            temp_model = main_models.PushTaskNotificationAndroidOptionsOppo()
            self.oppo = temp_model.from_map(m.get('Oppo'))

        if m.get('Vivo') is not None:
            temp_model = main_models.PushTaskNotificationAndroidOptionsVivo()
            self.vivo = temp_model.from_map(m.get('Vivo'))

        if m.get('Xiaomi') is not None:
            temp_model = main_models.PushTaskNotificationAndroidOptionsXiaomi()
            self.xiaomi = temp_model.from_map(m.get('Xiaomi'))

        return self

class PushTaskNotificationAndroidOptionsXiaomi(DaraModel):
    def __init__(
        self,
        channel: str = None,
    ):
        self.channel = channel

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel is not None:
            result['Channel'] = self.channel

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')

        return self

class PushTaskNotificationAndroidOptionsVivo(DaraModel):
    def __init__(
        self,
        category: str = None,
        importance: int = None,
        receipt_id: str = None,
    ):
        self.category = category
        self.importance = importance
        self.receipt_id = receipt_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.importance is not None:
            result['Importance'] = self.importance

        if self.receipt_id is not None:
            result['ReceiptId'] = self.receipt_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('Importance') is not None:
            self.importance = m.get('Importance')

        if m.get('ReceiptId') is not None:
            self.receipt_id = m.get('ReceiptId')

        return self

class PushTaskNotificationAndroidOptionsOppo(DaraModel):
    def __init__(
        self,
        category: str = None,
        delete_intent_data: str = None,
        intelligent_intent: str = None,
        notify_level: int = None,
        private_content_parameters: str = None,
        private_msg_template_id: str = None,
        private_title_parameters: str = None,
    ):
        self.category = category
        self.delete_intent_data = delete_intent_data
        self.intelligent_intent = intelligent_intent
        self.notify_level = notify_level
        self.private_content_parameters = private_content_parameters
        self.private_msg_template_id = private_msg_template_id
        self.private_title_parameters = private_title_parameters

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.delete_intent_data is not None:
            result['DeleteIntentData'] = self.delete_intent_data

        if self.intelligent_intent is not None:
            result['IntelligentIntent'] = self.intelligent_intent

        if self.notify_level is not None:
            result['NotifyLevel'] = self.notify_level

        if self.private_content_parameters is not None:
            result['PrivateContentParameters'] = self.private_content_parameters

        if self.private_msg_template_id is not None:
            result['PrivateMsgTemplateId'] = self.private_msg_template_id

        if self.private_title_parameters is not None:
            result['PrivateTitleParameters'] = self.private_title_parameters

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('DeleteIntentData') is not None:
            self.delete_intent_data = m.get('DeleteIntentData')

        if m.get('IntelligentIntent') is not None:
            self.intelligent_intent = m.get('IntelligentIntent')

        if m.get('NotifyLevel') is not None:
            self.notify_level = m.get('NotifyLevel')

        if m.get('PrivateContentParameters') is not None:
            self.private_content_parameters = m.get('PrivateContentParameters')

        if m.get('PrivateMsgTemplateId') is not None:
            self.private_msg_template_id = m.get('PrivateMsgTemplateId')

        if m.get('PrivateTitleParameters') is not None:
            self.private_title_parameters = m.get('PrivateTitleParameters')

        return self

class PushTaskNotificationAndroidOptionsMeizu(DaraModel):
    def __init__(
        self,
        notice_msg_type: int = None,
    ):
        self.notice_msg_type = notice_msg_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.notice_msg_type is not None:
            result['NoticeMsgType'] = self.notice_msg_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NoticeMsgType') is not None:
            self.notice_msg_type = m.get('NoticeMsgType')

        return self

class PushTaskNotificationAndroidOptionsHuawei(DaraModel):
    def __init__(
        self,
        category: str = None,
        importance: int = None,
        live_notification_payload: str = None,
        receipt_id: str = None,
        urgency: str = None,
    ):
        self.category = category
        self.importance = importance
        self.live_notification_payload = live_notification_payload
        self.receipt_id = receipt_id
        self.urgency = urgency

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.importance is not None:
            result['Importance'] = self.importance

        if self.live_notification_payload is not None:
            result['LiveNotificationPayload'] = self.live_notification_payload

        if self.receipt_id is not None:
            result['ReceiptId'] = self.receipt_id

        if self.urgency is not None:
            result['Urgency'] = self.urgency

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('Importance') is not None:
            self.importance = m.get('Importance')

        if m.get('LiveNotificationPayload') is not None:
            self.live_notification_payload = m.get('LiveNotificationPayload')

        if m.get('ReceiptId') is not None:
            self.receipt_id = m.get('ReceiptId')

        if m.get('Urgency') is not None:
            self.urgency = m.get('Urgency')

        return self

class PushTaskNotificationAndroidOptionsHonor(DaraModel):
    def __init__(
        self,
        importance: int = None,
    ):
        self.importance = importance

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.importance is not None:
            result['Importance'] = self.importance

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Importance') is not None:
            self.importance = m.get('Importance')

        return self

class PushTaskNotificationAndroidOptionsAccs(DaraModel):
    def __init__(
        self,
        custom_style: int = None,
        notify_type: str = None,
        open_activity: str = None,
        open_type: str = None,
        open_url: str = None,
        priority: int = None,
        thread_id: str = None,
    ):
        self.custom_style = custom_style
        self.notify_type = notify_type
        self.open_activity = open_activity
        self.open_type = open_type
        self.open_url = open_url
        self.priority = priority
        self.thread_id = thread_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_style is not None:
            result['CustomStyle'] = self.custom_style

        if self.notify_type is not None:
            result['NotifyType'] = self.notify_type

        if self.open_activity is not None:
            result['OpenActivity'] = self.open_activity

        if self.open_type is not None:
            result['OpenType'] = self.open_type

        if self.open_url is not None:
            result['OpenUrl'] = self.open_url

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.thread_id is not None:
            result['ThreadId'] = self.thread_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomStyle') is not None:
            self.custom_style = m.get('CustomStyle')

        if m.get('NotifyType') is not None:
            self.notify_type = m.get('NotifyType')

        if m.get('OpenActivity') is not None:
            self.open_activity = m.get('OpenActivity')

        if m.get('OpenType') is not None:
            self.open_type = m.get('OpenType')

        if m.get('OpenUrl') is not None:
            self.open_url = m.get('OpenUrl')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('ThreadId') is not None:
            self.thread_id = m.get('ThreadId')

        return self



class PushTaskMessage(DaraModel):
    def __init__(
        self,
        body: str = None,
        title: str = None,
    ):
        self.body = body
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body is not None:
            result['Body'] = self.body

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Body') is not None:
            self.body = m.get('Body')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

