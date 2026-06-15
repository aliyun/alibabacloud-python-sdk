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
        # The push method. This is an optional parameter. The default value is `PUSH_IMMEDIATELY` (immediate push).
        # 
        # >Notice: 
        # 
        # The `MassPushV2` batch push API supports only the following push methods:
        # 
        # - `PUSH_IMMEDIATELY` (immediate push)
        # 
        # - `SCHEDULED_PUSH` (scheduled push)
        self.action = action
        # The pass-through message data sent to the device. The total length cannot exceed 4,000 bytes.
        # 
        # > Length calculation
        # >
        # > - The length is calculated based on the byte length of the UTF-8 encoded string after the Message object is serialized into JSON.
        # >
        # > - A Chinese character typically occupies 3 bytes in UTF-8 encoding.
        self.message = message
        # The vendor notification data sent to the device.
        # 
        # >Notice: 
        # 
        # If you set both `Message` and `Notification`, the device receives only one. The sending rules are as follows:
        # 
        # - If the device is online, pass-through message data is sent.
        # 
        # - If the device is offline, a system notification is sent.
        self.notification = notification
        # Push options
        self.options = options
        # The target object for the message push. This parameter is optional when the `Action` operation type is `CREATE_CONTINUOUS_PUSH` (create a continuous push task).
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
        # The platform type. This is an optional parameter.
        self.platform = platform
        # The push target type.
        # 
        # >Notice: 
        # 
        # The `MassPushV2` batch push API and `CONTINUOUS_PUSH` continuous push support only the following three target types:
        # 
        # - `DEVICE`
        # 
        # - `ACCOUNT`
        # 
        # - `ALIAS`
        self.type = type
        # Set the push target based on `Target.Type`. Separate multiple targets with commas. The target types and their values are described as follows:
        # 
        # > - `DEVICE`: Device ID, such as deviceid1,deviceid2. You can specify up to 1,000 device IDs.
        # >
        # > - `ACCOUNT`: Account ID, such as account1,account2. You can specify up to 1,000 account IDs.
        # >
        # > - `ALIAS`: Alias, such as alias1,alias2. You can specify up to 1,000 aliases.
        # >
        # > - `TAG`: Supports one or more tags. For more information about the format, see [Tag format specifications](https://help.aliyun.com/document_detail/434847.html).
        # >
        # > - `ALL`: Push to all devices. You do not need to set a value. Pushing to all devices may increase costs. Use this feature with caution.
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
        # Sets the expiration time of the message. After this time, the message will no longer be sent. The maximum retention period is 72 hours.
        # 
        # > - This uses the ISO 8601 standard and UTC time. The format is YYYY-MM-DDThh:mm:ssZ.
        # >
        # > - The expiration time must satisfy: ExpireTime > PushTime + 3 seconds (3 seconds is a buffer for network and system delays).
        # >
        # > - Recommendation: The expiration time for a single push should be at least 1 minute. For a push to all or a batch push, it should be at least 10 minutes.
        # 
        # >Notice: 
        # 
        # For pass-through messages, if you do not set an expiration time, the message is only sent to online devices. If the device is offline, the message is discarded.
        self.expire_time = expire_time
        # A custom identifier for the push task. If JobKey is not empty, this field will be included in the receipt log. To view receipt logs, see [Receipt logs](https://help.aliyun.com/document_detail/434651.html).
        self.job_key = job_key
        # A unique ID used to identify the message. This is only valid when the `Action` parameter is `CONTINUOUS_PUSH`.
        self.message_id = message_id
        # Specifies the sending time of the message, up to 7 days in the future. This is only valid when the `Action` parameter is `SCHEDULED_PUSH`.
        # 
        # > This uses the ISO 8601 standard and UTC time. The format is yyyy-MM-ddTHH:mm:ssZ.
        self.push_time = push_time
        # Resends the message as a text message.
        # 
        # > Currently, this is only supported for `Android` and `HarmonyOS` devices.
        self.sms = sms
        # Specifies whether to automatically truncate oversized titles and content.
        # 
        # > This is only supported for vendor channels that have explicit limits on title and content length. It does not apply to channels like APNs, Huawei, and Honor, which do not limit title and content length but only the total request body size.
        self.trim = trim
        # Specifies the sending channel. Valid values are:
        # 
        # - `accs`: Alibaba Cloud proprietary channel
        # 
        # - `huawei`: Huawei channel
        # 
        # - `honor`: Honor channel
        # 
        # - `xiaomi`: Xiaomi channel
        # 
        # - `oppo`: OPPO channel
        # 
        # - `vivo`: vivo channel
        # 
        # - `meizu`: Meizu channel
        # 
        # - `fcm`: Google Firebase channel (HTTP v1 API)
        # 
        # - `apns`: APNs channel
        # 
        # - `harmony`: HarmonyOS channel
        # 
        # > * If this parameter is not configured, all channels can be used.
        # >
        # > * If this parameter is configured, only the channels specified in the parameter are used.
        # >
        # > * If the configured channel conflicts with the sending policy (for example, iOS notifications only go through the APNs channel, but this parameter does not include \\`apns\\`), the message is not sent.
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
        # The delay time to trigger the text message, in seconds.
        # 
        # This must be set if you use SMS filter interaction. We recommend setting it to 15 seconds or more, with a maximum of 3 days, to avoid duplicate text messages and pushes.
        # 
        # > When you use SMS filter interaction, the ExpireTime parameter is invalid. The notification expiration time is calculated based on the DelaySecs parameter. The expiration time is the current time plus the DelaySecs time.
        self.delay_secs = delay_secs
        # Key-value pairs for the variables in the SMS template.
        self.params = params
        # The SMS sending policy.
        self.send_policy = send_policy
        # The SMS signature.
        self.sign_name = sign_name
        # The SMS template name. You can get this from the SMS template management interface. It is the name assigned by the system, not the name set by the developer.
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
        # Android notification configuration
        self.android = android
        # The content of the push notification.
        # 
        # > The length limits are as follows:
        # >
        # > - For iOS, HarmonyOS, and Android, the character length cannot exceed 200.
        self.body = body
        # HarmonyOS notification configuration.
        self.hmos = hmos
        # iOS notification configuration
        self.ios = ios
        # The title of the push notification.
        # 
        # > The length limits are as follows:
        # >
        # > - For iOS/HarmonyOS, the byte length cannot exceed 200.
        # >
        # > - For Android, the character length cannot exceed 50.
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
        # iOS notifications are sent through the Apple Push Notification service (APNs) center. You must specify the environment information. This is an optional parameter. The default is the production environment.
        # 
        # - DEV: Development environment, for applications installed and tested directly from Xcode.
        # 
        # - PRODUCT: Production environment, for applications distributed through the App Store, TestFlight, Ad Hoc, and enterprise channels.
        self.apns_env = apns_env
        # The iOS application badge.
        self.badge = badge
        # Specifies whether to enable the badge auto-increment feature. This is an optional parameter. The default value is false.
        # 
        # > - This parameter cannot be used with the badge setting parameter.
        # >
        # > - The badge auto-increment feature is maintained by the Alibaba Cloud push server, which counts the badges for each device. You must use SDK version 1.9.5 or later and actively sync the badge number to the server through the SDK.
        self.badge_auto_increment = badge_auto_increment
        # Specifies the category identifier for an iOS notification. This defines the notification\\"s interactive behavior and display style.
        # 
        # > - The category must be pre-registered in the app to take effect.
        # >
        # > - Different categories can define different sets of actions.
        self.category = category
        # A unique identifier that controls notification merging. Notifications with the same identifier are overwritten.
        self.collapse_id = collapse_id
        # Custom extension properties for iOS notifications.
        # 
        # > - The parameter must be passed in a standard JSON Map format. An incorrect format causes parsing to fail.
        self.ext_parameters = ext_parameters
        # The interruption level. This is an optional parameter. Valid values are:
        # 
        # - `passive`: The system adds the notification to the notification list without lighting up the screen or playing a sound.
        # 
        # - `active`: The system displays the notification immediately, lights up the screen, and can play a sound.
        # 
        # - `time-sensitive`: The system presents the notification immediately, lights up the screen, and can play a sound, but does not override system notification controls.
        # 
        # - `critical`: The system displays the notification immediately, lights up the screen, and plays a sound, bypassing the mute switch.
        self.interruption_level = interruption_level
        # Live Activities parameter object.
        # 
        # >Notice: 
        # 
        # - Live Activities push only supports pushing to a single device of the `DEVICE` type.
        # 
        # - When you push to Live Activities, you can leave the title and body parameters empty.
        self.live_activity = live_activity
        # The iOS notification sound. Specify the name of the audio file stored in the app bundle or the sandbox Library/Sounds directory. For more information, see [How to set the notification sound for iOS push](https://help.aliyun.com/document_detail/48906.html).
        # 
        # > - If you specify an empty string (""), the notification is silent.
        # >
        # > - If this parameter is not set, the default value is \\`default\\`, which is the system prompt sound.
        self.music = music
        # Enables extended notifications and controls whether iOS notifications support processing by the Notification Service Extension.
        # 
        # > - This must be set to true when you send a silent notification.
        # >
        # > - The extension processing time cannot exceed 30 seconds.
        # >
        # > - A timeout causes the notification to display the original content.
        # >
        # > - You must add a Notification Service Extension to your application.
        self.mutable = mutable
        # The relevance score of the notification message. It is used to control the priority and display policy of the notification.
        self.relevance_score = relevance_score
        # Controls whether to enable silent push mode.
        # 
        # > - When you send a silent notification, you can leave the `title` and `body` parameters empty.
        self.silent = silent
        # The subtitle of the iOS notification.
        self.subtitle = subtitle
        # The thread identifier for iOS notification grouping. It is used to classify and collapse related notifications.
        # 
        # > - Notifications with the same thread-id are automatically grouped.
        # >
        # > - Multiple related notifications are collapsed into one notification group.
        # >
        # > - Users can expand the group to view all notifications within it.
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
        # Static pass-through parameters for iOS Live Activities push. They are used to transmit immutable business identification information.
        # 
        # > This is required when `Event` is \\`start\\`.
        self.attributes = attributes
        # The type of Live Activity to start.
        # 
        # > This is required when `Event` is \\`start\\`.
        self.attributes_type = attributes_type
        # Dynamic pass-through parameters for a Live Activity. They contain real-time updatable status information and changing data.
        # 
        # > - Avoid overly frequent updates. An interval of 5 seconds or more is recommended.
        # >
        # > - Update multiple fields in a batch to reduce the number of pushes.
        # >
        # > - Consider the user experience and avoid screen flickering.
        # >
        # > - Must be a valid JSON string.
        self.content_state = content_state
        # Sets the retention period for a finished Live Activity on the lock screen. This lets users view information after the activity has ended. It is a Unix timestamp in seconds.
        self.dismissal_date = dismissal_date
        # Starts, updates, or ends a Live Activity.
        self.event = event
        # The unique identifier for a Live Activity. It associates the activity instance on the device with the push target on the server.
        # 
        # >Notice: 
        # 
        # - This `ID` must be the same as the `forActivityId` parameter of the `registerLiveActivityPushToken` method in the client SDK.
        # 
        # - The server uses this `ID` to locate the specific activity instance during a push.
        self.id = id
        # Sets the expiration timestamp for the content of an iOS Live Activity. It is a Unix timestamp in seconds.
        # 
        # > - After the specified time is reached, the system automatically marks the activity as expired.
        # >
        # > - Expired activities are removed from the Live Activity and the lock screen.
        # >
        # > - This prevents outdated information from occupying the user interface for a long time.
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
        # Specifies the action corresponding to the ability of an in-app page.
        # 
        # > For more information, see [ClickAction.action](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/push-scenariozed-api-request-param-V5#section152462191216) on the official HarmonyOS website.
        self.action = action
        # The HarmonyOS application badge cumulative number.
        # 
        # > - This is supported starting from HarmonyOS SDK 1.2.0.
        # >
        # > - See the description of the [addNum field](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/push-scenariozed-api-request-param-V5#section266310382145) for HarmonyOS badges.
        self.badge_add_num = badge_add_num
        # The HarmonyOS application badge number setting.
        # 
        # > - See the description of the [setNum field](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/push-scenariozed-api-request-param-V5#section266310382145) for HarmonyOS badges.
        # >
        # > - This is supported starting from HarmonyOS SDK 1.2.0.
        self.badge_set_num = badge_set_num
        # The notification message category. This is an optional parameter. The default category is `MARKETING`.
        # 
        # > After you apply for the right to self-classify notification messages, this parameter is used to identify the message type. Different notification message types affect how messages are displayed and how users are reminded. For more information, see [Notification.category](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/push-scenariozed-api-request-param-V5#section17371529101117) on the official HarmonyOS website.
        self.category = category
        # Sets custom extension properties for the notification message. This is used to pass additional business data.
        # 
        # > The parameter must be passed in a standard JSON Map format. An incorrect format causes parsing to fail.
        self.ext_parameters = ext_parameters
        # Extra data for the notification extension message.
        # 
        # > - This is valid when sending a HarmonyOS notification extension message.
        # >
        # > - It is conceptually equivalent to the extraData field of a HarmonyOS notification extension message. For a specific definition, see the HarmonyOS [ExtensionPayload](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/push-scenariozed-api-request-param-V5#section161192514234) description.
        # >
        # > - This is supported starting from HarmonyOS SDK 1.2.0.
        self.extension_extra_data = extension_extra_data
        # Enables the HarmonyOS notification extension.
        # 
        # > - You must first apply for permission on the official HarmonyOS website to send notification extension messages. For related content, see the [HarmonyOS documentation](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V5/push-send-extend-noti-V5) on sending notification extension messages.
        # >
        # > - This is supported starting from HarmonyOS SDK 1.2.0.
        self.extension_push = extension_push
        # The URL for the large icon on the right side of the notification. The URL must use the HTTPS protocol.
        # 
        # > - Supported image formats are png, jpg, jpeg, heif, gif, and bmp. The image dimensions (length × width) must be less than 25,000 pixels.
        # >
        # > - For more information, see [Notification.image](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/push-scenariozed-api-request-param-V5#section17371529101117) on the official HarmonyOS website.
        self.image_url = image_url
        # When `RenderStyle` is `MULTI_LINE`, you must fill in this field to define the content for the multi-line text style. It supports up to 3 lines of content.
        self.inbox_content = inbox_content
        # The JSON string of the HarmonyOS Live Window data structure [LiveViewPayload](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V13/push-scenariozed-api-request-param-V13#section66881469306). For developer integration, see the document [HarmonyOS Live Window Push Guide](https://help.aliyun.com/document_detail/2982112.html).
        self.live_view_payload = live_view_payload
        # Specifies the unique identifier (notifyId) for each message when it is displayed in the notification bar. If not provided, the push service automatically generates a unique identifier. Different notification messages can use the same notifyId to allow new messages to overwrite old ones. For more information, see [Notification.notifyId](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/push-scenariozed-api-request-param-V5#section17371529101117) on the official HarmonyOS website.
        self.notify_id = notify_id
        # The receipt ID for the HarmonyOS channel. This ID can be found in the receipt parameter settings on the HarmonyOS channel push operations platform.
        # 
        # > - If the default receipt configuration on the HarmonyOS channel push operations platform is the Alibaba Cloud receipt, you do not need to provide this. If not, we recommend that you first configure the default HarmonyOS channel receipt ID in the Alibaba Cloud EMAS Mobile Push console.
        # >
        # > - For more information, see [pushOptions.receiptId](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/push-scenariozed-api-request-param-V5#section418321011212) on the official HarmonyOS website.
        self.receipt_id = receipt_id
        # The notification message style. This is an optional parameter. The default is a normal notification.
        self.render_style = render_style
        # Uses the specified type of notification channel.
        # 
        # > - This is only valid for Alibaba Cloud\\"s proprietary channels.
        # >
        # > - For more information, see [SlotType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/js-apis-notificationmanager-V5#slottype) on the official HarmonyOS website.
        self.slot_type = slot_type
        # The HarmonyOS custom ringtone file name.
        self.sound = sound
        # The duration of the custom message notification ringtone in seconds. The range is [1, 60]. If the ringtone duration is too short, it will loop.
        self.sound_duration = sound_duration
        # Enables test messages.
        # 
        # > - For more information, see the HarmonyOS push parameter [TestMessage](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/push-scenariozed-api-request-param-V5#section418321011212).
        self.test_message = test_message
        # The URI corresponding to the ability of an in-app page.
        # 
        # > - If there are multiple abilities, specify the action and URI for each ability separately. The system prioritizes using the action to find the corresponding in-app page.
        # >
        # > - For more information, see [ClickAction.uri](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/push-scenariozed-api-request-param-V5#section152462191216) on the official HarmonyOS website.
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
        # The full class name of the application entry Activity for badge settings.
        # 
        # > This is only valid when pushing through the Huawei or Honor vendor channel.
        self.badge_activity = badge_activity
        # Sets a cumulative value for the badge, which is added to the original badge number.
        # 
        # > - This is supported by `Huawei` and `Honor` channels.
        # >
        # > - If both `BadgeAddNum` and `BadgeSetNum` are present, the latter takes precedence.
        self.badge_add_num = badge_add_num
        # Sets a fixed value for the badge number. The value range is [1, 99].
        # 
        # > - For vendor channel pushes, this is only effective for Huawei and Honor channels.
        # >
        # > - When pushing through Alibaba Cloud\\"s proprietary channel, this is only effective on Huawei, Honor, and vivo models.
        self.badge_set_num = badge_set_num
        # Sets the channelId for the Android app. It must correspond to the channelId in the vendor\\"s app.
        # 
        # > - Because the channel_id for OPPO\\"s private message notification channel is the same as the app\\"s channelId, the channel_id takes this value when pushing through the OPPO channel.
        # >
        # > - For pushes through Huawei, FCM, and Alibaba Cloud\\"s proprietary channels, the channel_id takes this value.
        # >
        # > - For specific uses, see the FAQ: [Notifications not received on Android 8.0 and later devices](https://help.aliyun.com/document_detail/67398.html).
        self.channel_id = channel_id
        # Custom extension properties for Android notifications.
        # 
        # > - The parameter must be passed in a standard JSON Map format. An incorrect format causes parsing to fail.
        self.ext_parameters = ext_parameters
        # Message grouping. For messages in the same group, only the latest one and the total number of messages received in that group are displayed in the notification bar. Not all messages are displayed, and they cannot be expanded. Currently supported by:
        # 
        # - Huawei vendor channel
        # 
        # - Honor vendor channel
        # 
        # - Proprietary channels with Android SDK 3.9.1 and earlier
        # 
        # > This parameter is no longer supported by proprietary channels in Android SDK 3.9.2 and later versions.
        self.group_id = group_id
        # The URL for the icon on the right. Currently supported by:
        # 
        # - `Huawei EMUI` (only applicable in long text mode and Inbox mode).
        # 
        # - `Honor Magic UI` (only applicable in long text mode).
        # 
        # - `Proprietary channels` (Android SDK 3.5.0 and later).
        self.image_url = image_url
        # The body text in Inbox mode. The content is a valid JSON Array with no more than 5 elements. Currently supported by:
        # 
        # - Huawei: EMUI 9 and later
        # 
        # - Honor: Magic UI 4.0 and later
        # 
        # - Xiaomi: MIUI 10 and later
        # 
        # - OPPO: ColorOS 5.0 and later
        # 
        # - Proprietary channels: Android SDK 3.6.0 and later
        self.inbox_content = inbox_content
        # The Huawei vendor channel notification sound. Specify the name of the audio file stored in the `app/src/main/res/raw/` directory of the client project, without the file format suffix. If not set, the default ringtone is used.
        self.music = music
        # The unique identifier for an Android notification bar message. It controls the overwriting and replacement behavior of notifications. A new notification with the same NotifyId automatically overwrites the old one.
        self.notify_id = notify_id
        # Detailed channel configuration.
        self.options = options
        # The image URL in large image mode. Currently supported by: proprietary channels with Android SDK 3.6.0 and later.
        self.picture_url = picture_url
        # The notification style. Valid values are:
        # 
        # - `0`: Standard mode (default)
        # 
        # - `1`: Long text mode (supported by Huawei, Honor, Xiaomi, OPPO, Meizu, and proprietary channels)
        # 
        # - `2`: Large image mode (supported by proprietary channels)
        # 
        # - `3`: List mode (supported by Huawei, Honor, Xiaomi, OPPO, and proprietary channels)
        self.render_style = render_style
        # Sets the vendor channel notification type:
        # 
        # - `false`: Formal notification (default).
        # 
        # - `true`: Test notification.
        # 
        # > Currently supported by: Huawei channel, Honor channel, vivo channel, and OPPO Fluid Cloud.
        self.test_message = test_message
        # Specifies the Activity to open after the notification is clicked.
        # 
        # >Warning: 
        # 
        # You must fill in this option when you use an Android vendor channel.
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
        # Alibaba Cloud proprietary configuration
        # 
        # > This is only valid when using Alibaba Cloud\\"s proprietary channel.
        self.accs = accs
        # Honor configuration
        self.honor = honor
        # Huawei configuration
        self.huawei = huawei
        # Meizu configuration
        self.meizu = meizu
        # OPPO configuration
        self.oppo = oppo
        # vivo configuration
        self.vivo = vivo
        # Xiaomi configuration
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
        focus_param: str = None,
        focus_pics: str = None,
        template_id: str = None,
        template_params: str = None,
    ):
        # Sets the channelId for the Xiaomi notification type. You must apply for this on the Xiaomi platform. For more information, see: [Application link](https://dev.mi.com/console/doc/detail?pId=2422#_4).
        # 
        # > A single application can apply for a maximum of 8 channels on the Xiaomi channel. Plan accordingly.
        self.channel = channel
        # The JSON string of the Xiaomi Super Island data structure [miui.focus.param](https://dev.mi.com/xiaomihyperos/documentation/detail?pId=2131). For developer integration, see the document [Xiaomi Super Island Push Guide](https://help.aliyun.com/zh/document_detail/3037956.html).
        self.focus_param = focus_param
        # The JSON string of the Xiaomi Super Island data image [miui.focus.pic_xxx](https://dev.mi.com/xiaomihyperos/documentation/detail?pId=2131). For developer integration, see the document [Xiaomi Super Island Push Guide](https://help.aliyun.com/zh/document_detail/3037956.html).
        self.focus_pics = focus_pics
        self.template_id = template_id
        self.template_params = template_params

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel is not None:
            result['Channel'] = self.channel

        if self.focus_param is not None:
            result['FocusParam'] = self.focus_param

        if self.focus_pics is not None:
            result['FocusPics'] = self.focus_pics

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_params is not None:
            result['TemplateParams'] = self.template_params

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')

        if m.get('FocusParam') is not None:
            self.focus_param = m.get('FocusParam')

        if m.get('FocusPics') is not None:
            self.focus_pics = m.get('FocusPics')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateParams') is not None:
            self.template_params = m.get('TemplateParams')

        return self

class PushTaskNotificationAndroidOptionsVivo(DaraModel):
    def __init__(
        self,
        category: str = None,
        importance: int = None,
        live_message: str = None,
        receipt_id: str = None,
    ):
        # vivo classifies messages into two categories for management: system messages and operational messages.
        # 
        # **System messages:**
        # 
        # - IM: Instant messages
        # 
        # - ACCOUNT: Account and asset
        # 
        # - TODO: To-do list
        # 
        # - DEVICE_REMINDER: Device information
        # 
        # - ORDER: Order and logistics
        # 
        # - SUBSCRIPTION: Subscription reminder
        # 
        # **Operational messages:**
        # 
        # - NEWS: News
        # 
        # - CONTENT: Content recommendation
        # 
        # - MARKETING: Operational activity
        # 
        # - SOCIAL: Social dynamics
        # 
        # For more information, see [vivo classification description](https://dev.vivo.com.cn/documentCenter/doc/359#s-ef3qugc3).
        self.category = category
        # Sets the vivo notification message classification. Valid values are:
        # 
        # - `0`: Operational message (default)
        # 
        # - `1`: System message
        # 
        # > We recommend using `Category` for notification classification. You must apply for this on the vivo platform. For more information, see: [Application link](https://dev.vivo.com.cn/documentCenter/doc/359).
        self.importance = importance
        # The JSON string of the vivo Atomic Island data structure [liveMessage](https://dev.vivo.com.cn/documentCenter/doc/896#s-fdagzbd4). For developer integration, see the document [vivo Atomic Island Push Guide](https://help.aliyun.com/zh/document_detail/3030718.html).
        self.live_message = live_message
        # The message receipt identifier for the vivo vendor push channel. It is used to receive push result callback notifications.
        # 
        # > - Location: vivo Open Platform → Push Service → Application Information → Receipt Configuration
        # >
        # > - Recommendation: First, configure the default receipt ID in the Alibaba Cloud EMAS console.
        # >
        # > - Condition: This must be configured only if the default receipt on the vivo platform is not the Alibaba Cloud receipt.
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

        if self.live_message is not None:
            result['LiveMessage'] = self.live_message

        if self.receipt_id is not None:
            result['ReceiptId'] = self.receipt_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('Importance') is not None:
            self.importance = m.get('Importance')

        if m.get('LiveMessage') is not None:
            self.live_message = m.get('LiveMessage')

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
        # OPPO classifies messages into two categories for management: communication and services, and content and marketing.
        # 
        # **Communication and services (requires permission application):**
        # 
        # - IM: Instant messages
        # 
        # - ACCOUNT: Account and asset
        # 
        # - TODO: To-do list
        # 
        # - DEVICE_REMINDER: Device information
        # 
        # - ORDER: Order and logistics
        # 
        # - SUBSCRIPTION: Subscription reminder
        # 
        # **Content and marketing:**
        # 
        # - NEWS: News
        # 
        # - CONTENT: Content recommendation
        # 
        # - MARKETING: Operational activity
        # 
        # - SOCIAL: Social dynamics
        # 
        # For more information, see [vivo classification description](https://open.oppomobile.com/new/developmentDoc/info?id=13189).
        self.category = category
        # The JSON string of the OPPO Fluid Cloud\\"s intent deletion data structure [data](https://open.oppomobile.com/documentation/page/info?id=13578). This parameter is invalid if the AndroidOppoIntelligentIntent parameter is already filled. For developer integration, see the document [OPPO Fluid Cloud Push Guide](https://help.aliyun.com/document_detail/2997310.html).
        self.delete_intent_data = delete_intent_data
        # The JSON string of the OPPO Fluid Cloud\\"s intent sharing data structure [IntelligentIntent](https://open.oppomobile.com/documentation/page/info?id=13565). For developer integration, see the document [OPPO Fluid Cloud Push Guide](https://help.aliyun.com/document_detail/2997310.html).
        self.intelligent_intent = intelligent_intent
        # The OPPO channel notification bar message reminder level. Valid values are:
        # 
        # - `1`: Notification bar
        # 
        # - `2`: Notification bar, lock screen, ringtone, vibration (default notification level for communication and service messages)
        # 
        # - `16`: Notification bar, lock screen, ringtone, vibration, banner (requires permission application)
        # 
        # > When you use the `NotifyLevel` parameter, you must also pass the `Category` parameter.
        self.notify_level = notify_level
        # The OPPO private message template content parameters.
        self.private_content_parameters = private_content_parameters
        # The OPPO private message template ID.
        self.private_msg_template_id = private_msg_template_id
        # The OPPO private message template title parameters.
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
        # The Meizu message type.
        # 
        # - 0 Public message (default)
        # 
        # - 1 Private message
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
        business_type: int = None,
        category: str = None,
        importance: int = None,
        live_notification_payload: str = None,
        receipt_id: str = None,
        urgency: str = None,
    ):
        # Sets the Huawei quick notification parameters.
        # 
        # - **0**: Send a normal Huawei notification (default).
        # 
        # - **1**: Send a Huawei quick notification.
        self.business_type = business_type
        # Function 1: After you apply for [self-classification rights](https://developer.huawei.com/consumer/cn/doc/development/HMSCore-Guides/message-classification-0000001149358835?#section3410731125514), this is used to identify the message type and determine the [message reminder method](https://developer.huawei.com/consumer/cn/doc/development/HMSCore-Guides/message-classification-0000001149358835#ZH-CN_TOPIC_0000001149358835__p3850133955718). It speeds up the sending of specific types of messages. For valid values, see the [message classification standards](https://developer.huawei.com/consumer/cn/doc/development/HMSCore-Guides/message-classification-0000001149358835#section1076611477914) in the official Huawei Push documentation. Fill in the "Cloud notification category value" or "Local notification category value" from the document\\"s table.
        # 
        # Function 2: After [applying for special permissions](https://developer.huawei.com/consumer/cn/doc/development/HMSCore-Guides/faq-0000001050042183#section037425218509), this is used to identify high-priority pass-through scenarios. Valid values are:
        # 
        # - `VOIP`: Video call
        # 
        # - `PLAY_VOICE`: Voice playback
        # 
        # > * For "Cloud notification category value" that is "Not applicable," all messages go through Alibaba Cloud\\"s proprietary channel.
        # >
        # > * For "Local notification category value" that is "Not applicable," all messages go through the Huawei channel.
        self.category = category
        # Sets the importance parameter for Huawei notification message classification, which determines the notification behavior on the user\\"s device. Valid values are:
        # 
        # - `0`: Marketing message
        # 
        # - `1`: Service and communication message
        # 
        # > We recommend using `Category` for notification classification. You must apply for this on the Huawei platform. [Application link](https://developer.huawei.com/consumer/cn/doc/development/HMSCore-Guides/message-classification-0000001149358835#section893184112272).
        self.importance = importance
        # The JSON string of the Huawei Android Live Window data structure [LiveNotificationPayload](https://developer.huawei.com/consumer/cn/doc/HMSCore-References/rest-live-0000001562939968#ZH-CN_TOPIC_0000001700850537__p195121620102511). For developer integration, see the document [Huawei Live Window Push Guide](https://help.aliyun.com/document_detail/2983768.html).
        self.live_notification_payload = live_notification_payload
        # The receipt ID for the Huawei channel. This ID can be found in the receipt parameter settings on the Huawei channel push operations platform.
        # 
        # > If the default receipt configuration on the Huawei channel push operations platform is the Alibaba Cloud receipt, you do not need to provide this. If not, we recommend that you first configure the default Huawei channel receipt ID in the Alibaba Cloud EMAS Mobile Push console.
        self.receipt_id = receipt_id
        # The Huawei channel notification delivery priority. Valid values are:
        # 
        # - `HIGH`
        # 
        # - `NORMAL`
        # 
        # You must apply for permission. For more information, see: [Application link](https://developer.huawei.com/consumer/cn/doc/development/HMSCore-Guides/faq-0000001050042183#section037425218509).
        self.urgency = urgency

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_type is not None:
            result['BusinessType'] = self.business_type

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
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')

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
        # Sets the importance parameter for Honor notification message classification, which determines the notification behavior on the user\\"s device. Valid values are:
        # 
        # - `0`: Marketing message
        # 
        # - `1`: Service and communication message
        # 
        # You must apply for this on the Honor platform. [Application link](https://developer.honor.com/cn/docs/11002/guides/notification-class#%E8%87%AA%E5%88%86%E7%B1%BB%E6%9D%83%E7%9B%8A%E7%94%B3%E8%AF%B7).
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
        # The custom Android notification bar style. The value can be from 1 to 100.
        # 
        # > The client must complete the style preset configuration. For more information, see the [Custom Notification Style API](https://help.aliyun.com/document_detail/2834944.html) document.
        self.custom_style = custom_style
        # The notification reminder method. Valid values:
        # 
        # - `VIBRATE`: Vibrate (default)
        # 
        # - `SOUND`: Sound
        # 
        # - `BOTH`: Sound and vibration
        # 
        # - `NONE`: Silent
        self.notify_type = notify_type
        # Sets the activity to open when the notification is clicked. This is valid when `OpenType` is `ACTIVITY`.
        self.open_activity = open_activity
        # The action to take after the notification is clicked. Valid values:
        # 
        # - `APPLICATION`: Open the application (default).
        # 
        # - `ACTIVITY`: Open the specified page `OpenActivity`.
        # 
        # - `URL`: Open a URL.
        # 
        # - `NONE`: No action.
        self.open_type = open_type
        # After an Android device receives a push, clicking the notification opens the corresponding URL. This is valid when `OpenType` is `URL`.
        self.open_url = open_url
        # The priority of the Android notification\\"s position in the notification bar. Valid values: -2, -1, 0, 1, 2.
        self.priority = priority
        # Message grouping. Messages in the same group are displayed collapsed in the notification bar and can be expanded. Different groups of notifications are displayed separately.
        # 
        # > This is for Android SDK 3.9.2 and later.
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
        # The content of the message to send.
        self.body = body
        # The title of the message to send.
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

