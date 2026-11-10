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
        # The push method. This parameter is optional. Default value: PUSH_IMMEDIATELY (push immediately).
        # 
        # >Notice: 
        # 
        # The MassPushV2 batch push API supports only the following push methods:
        # 
        # - PUSH_IMMEDIATELY (push immediately)
        # - SCHEDULED_PUSH (scheduled push)
        self.action = action
        # The pass-through message data sent to the device. The total length cannot exceed 4,000 bytes.
        # 
        # > Length calculation rules
        # > - The length is calculated based on the byte length of the UTF-8 encoded string after the Message object is serialized into JSON.
        # > - A Chinese character typically occupies 3 bytes in UTF-8 encoding.
        self.message = message
        # The vendor notification data sent to the device.
        # 
        # >Notice: 
        # 
        # If both Message and Notification are configured, the device receives only one of them based on the following rules:
        # 
        # - If the device is online, the pass-through message data is sent.
        # - If the device is offline, the system notification is sent.
        self.notification = notification
        # The push options.
        self.options = options
        # The target object for the message push. This parameter is optional when the Action parameter is set to CREATE_CONTINUOUS_PUSH (create a continuous push task).
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
        # The platform type. This parameter is optional.
        self.platform = platform
        # The type of the push target.
        # 
        # >Notice: 
        # 
        # The MassPushV2 batch push API and the CONTINUOUS_PUSH continuous push support only the following three target types:
        # 
        # - DEVICE (device)
        # - ACCOUNT (account)
        # - ALIAS (alias)
        self.type = type
        # The push targets based on Target.Type. Separate multiple targets with commas. The following section describes the target types and target values in detail:
        # 
        # >* DEVICE: device IDs, such as deviceid1,deviceid2. Maximum of 1,000.
        # >* ACCOUNT: account IDs, such as account1,account2. Maximum of 1,000.
        # >* ALIAS: aliases, such as alias1,alias2. Maximum of 1,000.
        # >* TAG: one or more tags. For the format, see [Tag format specifications](https://help.aliyun.com/document_detail/434847.html).
        # >* ALL: all targets. No value is required. Pushing to all targets may increase costs. Use this option with caution.
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
        # The expiration time of the message. The message is not sent after it expires. The maximum retention period is 72 hours.
        # 
        # > * The time must follow the ISO 8601 standard and use UTC time in the YYYY-MM-DDThh:mm:ssZ format.
        # > * The expiration time must meet the following condition: ExpireTime > PushTime + 3 seconds. The 3 seconds are reserved for network and system latency.
        # > * Set the expiration time to at least 1 minute for single-target push tasks and at least 10 minutes for full or batch push tasks.
        # 
        # 
        # >Notice: For pass-through messages, if the expiration time is not set, the message is sent only to online devices. If the device is offline, the message is discarded.</notice>
        self.expire_time = expire_time
        # The custom identifier of the push task. If JobKey is not empty, this field is included in the receipt log. For more information, see [Receipt logs](https://help.aliyun.com/document_detail/434651.html).
        self.job_key = job_key
        # The unique identity of the message. This parameter is valid only when the Action parameter is set to CONTINUOUS_PUSH.
        self.message_id = message_id
        # Specifies the sending time of the message, which can be up to seven days later. Valid only when the Action parameter is set to SCHEDULED_PUSH.
        # 
        # > The time must follow the ISO 8601 standard and use UTC time in the yyyy-MM-ddTHH:mm:ssZ format.
        self.push_time = push_time
        # The fallback SMS message configuration.
        # 
        # > Currently, only Android and HarmonyOS devices are supported.
        self.sms = sms
        # Specifies whether to automatically truncate excessively long titles and content.
        # 
        # >This parameter applies only to vendor channels that explicitly limit the title and content length. It does not apply to channels such as APNs, Huawei, and Honor, which do not limit the title and content length but only limit the total request body size.
        self.trim = trim
        # Specifies the sending channels. Valid values:
        # 
        # - accs: Alibaba Cloud proprietary channel.
        # - huawei: Huawei channel.
        # - honor: Honor channel.
        # - xiaomi: Xiaomi channel.
        # - oppo: OPPO channel.
        # - vivo: vivo channel.
        # - meizu: Meizu channel.
        # - fcm: Google Firebase channel (HTTP v1 API).
        # - apns: APNs channel.
        # - harmony: HarmonyOS channel.
        # 
        # > - If this parameter is not configured, all channels are available.
        # > - If this parameter is configured, only the specified channels are used.
        # > - If the configured channels conflict with the sending policy (for example, iOS notifications only use the APNs channel, but apns is not included in this parameter), the message is not sent.
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
        # The delay time before the SMS message is triggered. Unit: seconds.
        # 
        # If you use SMS linkage, this parameter is required. Set this parameter to at least 15 seconds and no more than 3 days to avoid duplicate SMS and push messages.
        # 
        # > When SMS linkage is used, the ExpireTime parameter becomes invalid. The expiration time of the notification is calculated based on the DelaySecs parameter. The expiration time is the current time plus the DelaySecs value.
        self.delay_secs = delay_secs
        # The key-value pairs of the variables in the SMS template.
        self.params = params
        # The SMS sending policy.
        self.send_policy = send_policy
        # The SMS signature.
        self.sign_name = sign_name
        # The name of the SMS template. You can obtain the name from the SMS template management page. The name is assigned by the system, not specified by the developer.
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
        # The Android notification configuration.
        self.android = android
        # The body of the notification to be pushed.
        # 
        # > Length limits:
        # > - iOS/HarmonyOS/Android: the **character length** cannot exceed 200.
        self.body = body
        # HarmonyOS notification configuration.
        self.hmos = hmos
        # iOS notification configuration.
        self.ios = ios
        # The title of the notification to be pushed.
        # 
        # > Length limits:
        # > - iOS/HarmonyOS: the **byte length** cannot exceed 200.
        # > - Android: the **character length** cannot exceed 50.
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
        # To send iOS notifications through the APNs center, you must specify the corresponding environment context. This parameter is optional. Default value: production environment.
        # 
        # - DEV: the development environment, which applies to applications directly installed and debugged by using Xcode.
        # - PRODUCT: the production environment, which applies to applications distributed through the App Store, TestFlight, Ad Hoc, and enterprise distribution.
        self.apns_env = apns_env
        # The badge of the iOS application.
        self.badge = badge
        # Specifies whether to enable the automatic badge increment feature. This parameter is optional. Default value: false.
        # 
        # > - This parameter cannot be used together with the badge setting parameter.
        # > - The automatic badge increment feature maintains the badge count for each device on the Alibaba Cloud push server. You must use SDK version 1.9.5 or later to actively synchronize the badge count to the server.
        self.badge_auto_increment = badge_auto_increment
        # The category identifier of the iOS notification, which is used to define the interactive behavior and display style of the notification.
        # 
        # > - The category must be pre-registered in the application to take effect.
        # > - Different categories can define different sets of actions.
        self.category = category
        # The unique identifier used to control notification grouping. Notifications with the same identifier are overwritten.
        self.collapse_id = collapse_id
        # The custom extension attributes of the iOS notification.
        # 
        # > - The parameter must be passed in standard JSON map format. Incorrect formats cause parsing failures.
        self.ext_parameters = ext_parameters
        # The interruption level. This parameter is optional. Valid values:
        # 
        # - passive: The system adds the notification to the notification list without lighting up the screen or playing a sound.
        # - active: The system displays the notification immediately, lights up the screen, and may play a sound.
        # - time-sensitive: The system presents the notification immediately, lights up the screen, and may play a sound, but does not bypass the system notification controls.
        # - critical: The system displays the notification immediately, lights up the screen, and plays a sound bypassing the silent switch.
        self.interruption_level = interruption_level
        # The Live Activity parameter object.
        # 
        # >Notice: 
        # 
        # - Live Activity push supports pushing to a **single device** only by using the DEVICE type.
        # - When pushing to a Live Activity, you do not need to specify the title and body parameters.
        self.live_activity = live_activity
        # The sound of the iOS notification. Specify the name of the audio file stored in the app bundle or the Library/Sounds directory of the sandbox. For more information, see [How to set the notification sound for iOS push](https://help.aliyun.com/document_detail/48906.html).
        # 
        # > - If an empty string ("") is specified, the notification is silent.
        # > - If this parameter is not set, the default value default is used, which indicates the system prompt sound.
        self.music = music
        # Specifies whether to enable extended notifications and allow iOS notifications to be processed by the Notification Service Extension.
        # > - This parameter must be set to true when sending silent notifications.
        # > - The processing time of the extension cannot exceed 30 seconds.
        # > - A timeout causes the notification to display the original content.
        # > - You must add the Notification Service Extension to your application.
        self.mutable = mutable
        # The relevance score of the notification message, which is used to control the priority and display strategy of the notification.
        self.relevance_score = relevance_score
        # Specifies whether to enable the silent push mode.
        # 
        # > - When sending a silent notification, you do not need to specify the title and body parameters.
        self.silent = silent
        # The subtitle of the iOS notification.
        self.subtitle = subtitle
        # The thread identifier for iOS notification grouping, which is used to group and collapse related notifications.
        # 
        # > - Notifications with the same thread ID are automatically grouped.
        # > - Multiple related notifications are collapsed into a single notification group.
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
        # The static pass-through parameters for iOS Live Activity push, which are used to pass unchanged business identification information.
        # 
        # > This parameter is required when Event is set to start.
        self.attributes = attributes
        # The type of the Live Activity to be started.
        # 
        # > This parameter is required when Event is set to start.
        self.attributes_type = attributes_type
        # The dynamic pass-through parameters for the Live Activity, which contain status information and changing data that can be updated in real time.
        # 
        # > - Avoid excessively frequent updates. An interval of 5 seconds or more is recommended.
        # > - Update multiple fields in batches to reduce the number of pushes.
        # > - Consider the user experience and avoid interface flickering.
        # > - Must be a valid JSON string.
        self.content_state = content_state
        # The retention time of a completed Live Activity on the Lock Screen, which allows users to view the information after the activity ends. The value is a UNIX timestamp in seconds.
        self.dismissal_date = dismissal_date
        # Starts, updates, or ends a live activity.
        self.event = event
        # The unique identifier of the Live Activity, which is used to associate the activity instance on the device with the push target on the server.
        # 
        # >Notice: 
        # 
        # - The ID must be the same as the forActivityId parameter in the registerLiveActivityPushToken method of the client SDK.
        # 
        # - The server uses this ID to locate the specific activity instance during a push.
        self.id = id
        # The expiration timestamp for the content of the iOS Live Activity. The value is a UNIX timestamp in seconds.
        # 
        # > - After the specified time is reached, the system automatically marks the activity as stale.
        # > - Stale activities are removed from the Dynamic Island and the Lock Screen.
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
        # The action corresponding to the ability of the in-app page.
        # 
        # > For more information, see [ClickAction.action](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/push-scenariozed-api-request-param-V5#section152462191216) on the HarmonyOS official website.
        self.action = action
        # The number to add to the HarmonyOS application badge.
        # 
        # > - Supported by HarmonyOS SDK 1.2.0 and later.
        # > - For more information, see the [addNum field description](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/push-scenariozed-api-request-param-V5#section266310382145) for HarmonyOS badges.
        self.badge_add_num = badge_add_num
        # The number to set for the HarmonyOS application badge.
        # 
        # > - For more information, see the [setNum field](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/push-scenariozed-api-request-param-V5#section266310382145) description for HarmonyOS badges.
        # > - Supported by HarmonyOS SDK 1.2.0 and later.
        self.badge_set_num = badge_set_num
        # The category of the notification message. This parameter is optional. Default value: MARKETING.
        # 
        # > After you apply for the notification message auto-classification permission, this parameter is used to identify the message type. Different notification message types affect the message display and reminder methods. For more information, see [Notification.category](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/push-scenariozed-api-request-param-V5#section17371529101117) on the HarmonyOS official website.
        self.category = category
        # Sets the custom extension attributes of the notification message to pass additional business data.
        # 
        # > The parameter must be passed in standard JSON map format. Incorrect formats will cause parsing failures.
        self.ext_parameters = ext_parameters
        # The additional data for notification extension messages.
        # 
        # > - Valid only when sending HarmonyOS notification extension messages.
        # > - Conceptually equivalent to the extraData field of HarmonyOS notification extension messages. For specific definitions, see the [ExtensionPayload](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/push-scenariozed-api-request-param-V5#section161192514234) description in HarmonyOS.
        # > - Supported by HarmonyOS SDK 1.2.0 and later.
        self.extension_extra_data = extension_extra_data
        # Enables HarmonyOS notification extensions.
        # 
        # > - To send notification extension messages, you must first apply for permissions on the HarmonyOS official website. For more information, see [HarmonyOS documentation](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V5/push-send-extend-noti-V5).
        # > - Supported by HarmonyOS SDK 1.2.0 and later.
        self.extension_push = extension_push
        # The URL of the large icon on the right side of the notification. The URL must use the HTTPS protocol.
        # 
        # > - Supported image formats: PNG, JPG, JPEG, HEIF, GIF, and BMP. The total number of pixels (width × height) must be less than 25,000.
        # > - For more information, see [Notification.image](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/push-scenariozed-api-request-param-V5#section17371529101117) on the HarmonyOS official website.
        self.image_url = image_url
        # When RenderStyle is set to MULTI_LINE, this field is required to define the content for the multi-line text style. A maximum of three content items are supported.
        self.inbox_content = inbox_content
        # The JSON string of the HarmonyOS Live View data structure [LiveViewPayload](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V13/push-scenariozed-api-request-param-V13#section66881469306). For development and integration, refer to the [HarmonyOS Live View push guide](https://help.aliyun.com/document_detail/2982112.html).
        self.live_view_payload = live_view_payload
        # The unique identifier (notifyId) for each message displayed in the notification bar. If this parameter is not provided, the push service automatically generates a unique identifier. Different notification messages can use the same notifyId to allow new messages to overwrite old ones. For more information, see [Notification.notifyId](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/push-scenariozed-api-request-param-V5#section17371529101117) on the HarmonyOS official website.
        self.notify_id = notify_id
        # The receipt ID of the HarmonyOS channel. You can view this receipt ID in the receipt parameter settings of the HarmonyOS channel push operations platform.
        # 
        # > - If the default receipt configuration on the HarmonyOS channel push operations platform is set to Alibaba Cloud receipt, you do not need to provide this parameter. Otherwise, we recommend that you configure the default receipt ID for the HarmonyOS channel in the Alibaba Cloud EMAS shift push console first.
        # > - For details, see [pushOptions.receiptId](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/push-scenariozed-api-request-param-V5#section418321011212) on the HarmonyOS official website.
        self.receipt_id = receipt_id
        # The notification message style. This parameter is optional. Default value: NORMAL.
        self.render_style = render_style
        # Uses a notification channel of the specified type.
        # 
        # > - This parameter is valid only for Alibaba Cloud proprietary channels.
        # > - For more information, see [SlotType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/js-apis-notificationmanager-V5#slottype) on the HarmonyOS official website.
        self.slot_type = slot_type
        # The custom ringtone file name for HarmonyOS.
        self.sound = sound
        # The duration of the custom message notification ringtone, in seconds. Valid values: 1 to 60. If the ringtone duration is shorter than the notification display time, the ringtone loops.
        self.sound_duration = sound_duration
        # Enables test messages.
        # 
        # > - For more information, see [TestMessage](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/push-scenariozed-api-request-param-V5#section418321011212) in the HarmonyOS push parameters.
        self.test_message = test_message
        # The URI corresponding to the ability of the built-in app page.
        # 
        # > - If multiple abilities exist, specify the action and URI for each ability. The action is prioritized when searching for the corresponding built-in app page.
        # > - For more information, see [ClickAction.uri](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/push-scenariozed-api-request-param-V5#section152462191216) on the HarmonyOS official website.
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
        # The fully qualified class name of the application entry activity for badge settings.
        # 
        # > Valid only for Huawei and Honor vendor channel pushes.
        self.badge_activity = badge_activity
        # Sets the increment value for the badge, which is added to the original badge number.
        # 
        # > - Supported by Huawei and Honor channels.
        # > - If both BadgeAddNum and BadgeSetNum are specified, BadgeSetNum takes precedence.
        self.badge_add_num = badge_add_num
        # Sets a fixed value for the badge number. Valid values: 1 to 99.
        # 
        # > - This parameter takes effect only for Huawei and Honor vendor channel pushes. 
        # > - For Alibaba Cloud proprietary channel pushes, this parameter takes effect only on Huawei, Honor, and vivo devices.
        self.badge_set_num = badge_set_num
        # Sets the channel ID of the Android application. The channel ID must match the channel ID in the vendor application.
        # 
        # > - Because the channel_id of the OPPO private message channel is the same as the channel ID of the application, this value is used as the channel_id when pushing through the OPPO channel.
        # > - This value is also used as the channel_id for Huawei, FCM, and Alibaba Cloud proprietary channel pushes.
        # > - For specific use cases, see the FAQ: [Notifications are not received on devices running Android 8.0 or later](https://help.aliyun.com/document_detail/67398.html).
        self.channel_id = channel_id
        # The custom extension attributes for Android notifications.
        # 
        # > - The parameter must be passed in standard JSON map format. Incorrect formats will cause parsing failures.
        self.ext_parameters = ext_parameters
        # The message group. For messages in the same group, only the latest message and the total number of received messages in the group are displayed in the notification bar. All messages are not displayed and cannot be expanded. Currently supported by:
        # 
        # - Huawei vendor channel.
        # - Honor vendor channel.
        # - Proprietary channels with Android SDK 3.9.1 or earlier.
        # 
        # > Proprietary channels no longer support this parameter in Android SDK 3.9.2 or later.
        self.group_id = group_id
        # The URL of the icon on the right side. Currently supported by:
        # 
        # - Huawei EMUI (applicable only in long text mode and Inbox mode).
        # - Honor Magic UI (applicable only in long text mode).
        # - Proprietary channels (Android SDK 3.5.0 or later).
        self.image_url = image_url
        # The body text in Inbox mode. The content must be a valid JSON array with a maximum of five elements. Currently supported by:
        # 
        # - Huawei: EMUI 9 or later.
        # - Honor: Magic UI 4.0 or later.
        # - Xiaomi: MIUI 10 or later.
        # - OPPO: ColorOS 5.0 or later.
        # - Proprietary channels: Android SDK 3.6.0 or later.
        self.inbox_content = inbox_content
        # The notification sound for the Huawei vendor channel. Specify the audio file name stored in the `app/src/main/res/raw/` directory of the client project. Do not include the file format extension. If not set, the default ringtone is used.
        self.music = music
        # The unique identifier of the Android notification bar message, used to control the override and replacement behavior of notifications. A new notification with the same NotifyId automatically overrides the old notification.
        self.notify_id = notify_id
        # The detailed channel configuration.
        self.options = options
        # The image URL in large image mode. Currently supported by proprietary channels with Android SDK 3.6.0 or later.
        self.picture_url = picture_url
        # The notification style. Valid values:
        # 
        # - 0: Standard mode (default).
        # - 1: Long text mode (supported by Huawei, Honor, Xiaomi, OPPO, Meizu, and proprietary channels).
        # - 2: Large image mode (supported by proprietary channels).
        # - 3: List mode (supported by Huawei, Honor, Xiaomi, OPPO, and proprietary channels).
        self.render_style = render_style
        # Sets the notification type for vendor channels. Valid values:
        # 
        # - false: Formal notification (default).
        # - true: Test notification.
        # 
        # > Currently supported by Huawei channel, Honor channel, vivo channel, and OPPO Fluid Cloud.
        self.test_message = test_message
        # Specifies the activity to open when the notification is clicked.
        # 
        # >Warning: This parameter is required when you use Android vendor channels.</warning>
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
        # The Alibaba Cloud proprietary configuration.
        # 
        # > Valid only when the Alibaba Cloud proprietary channel is used.
        self.accs = accs
        # The Honor configuration.
        self.honor = honor
        # The Huawei configuration.
        self.huawei = huawei
        # The Meizu configuration.
        self.meizu = meizu
        # The OPPO configuration.
        self.oppo = oppo
        # The vivo configuration.
        self.vivo = vivo
        # The Xiaomi configuration.
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
        # Sets the channel ID for the Xiaomi notification type. You must apply on the Xiaomi platform. For more information, see [Application link](https://dev.mi.com/console/doc/detail?pId=2422#_4).
        # 
        # > A single application can apply for a maximum of eight channels on the Xiaomi channel. Plan accordingly in advance.
        self.channel = channel
        # The JSON character string of the Xiaomi Super Island data structure [miui.focus.param](https://dev.mi.com/xiaomihyperos/documentation/detail?pId=2131). For development and integration, References: [Xiaomi Super Island push guide](https://www.alibabacloud.com/help/en/document_detail/3037956.html).
        self.focus_param = focus_param
        # The JSON character string of the Xiaomi Super Island data images [miui.focus.pic_xxx](https://dev.mi.com/xiaomihyperos/documentation/detail?pId=2131). For development and integration, References: [Xiaomi Super Island push guide](https://www.alibabacloud.com/help/en/document_detail/3037956.html).
        self.focus_pics = focus_pics
        # The Xiaomi private message template ID.
        self.template_id = template_id
        # The Xiaomi private message template parameters, as a JSON string.
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
        add_badge: bool = None,
        category: str = None,
        importance: int = None,
        live_message: str = None,
        receipt_id: str = None,
        template_id: str = None,
        template_params: str = None,
    ):
        # Sets the increment value for the vivo channel badge.
        self.add_badge = add_badge
        # vivo message categorization includes two categories for management: system messages and operation messages. 
        # 
        # **System messages:**
        # 
        # - IM: Instant messages.
        # - ACCOUNT: Accounts and assets.
        # - TODO: Schedules and to-do lists.
        # - DEVICE_REMINDER: Device information.
        # - ORDER: Orders and logistics.
        # - SUBSCRIPTION: subscribe reminders.
        # 
        # **Operation messages:**
        # 
        # - NEWS: News.
        # - CONTENT: Content recommendations.
        # - MARKETING: operational activity.
        # - SOCIAL: Social updates.
        # 
        # For more information, see [vivo categorization description](https://dev.vivo.com.cn/documentCenter/doc/359#s-ef3qugc3).
        self.category = category
        # Sets the vivo notification message classification. Valid values:
        # 
        # - 0: Operation messages (default).
        # - 1: System messages.
        # 
        # > We recommend that you use Category for notification classification. You must apply on the vivo platform. For more information, see [Application link](https://dev.vivo.com.cn/documentCenter/doc/359).
        self.importance = importance
        # The JSON character string of the vivo Atomic Island data structure [liveMessage](https://dev.vivo.com.cn/documentCenter/doc/896#s-fdagzbd4). For development and integration, References: [vivo Atomic Island push guide](https://www.alibabacloud.com/help/en/document_detail/3030718.html).
        self.live_message = live_message
        # The message receipt identifier for the vivo vendor push channel, used to receive callback notifications for push results.
        # 
        # > - Location: vivo Open Platform > Push Service > Application Information > Receipt Configuration.
        # > - Configuration recommendation: Configure the default receipt ID in the Alibaba Cloud EMAS console first.
        # > - Usage condition: Required only when the default receipt on the vivo platform is not the Alibaba Cloud receipt.
        self.receipt_id = receipt_id
        self.template_id = template_id
        self.template_params = template_params

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.add_badge is not None:
            result['AddBadge'] = self.add_badge

        if self.category is not None:
            result['Category'] = self.category

        if self.importance is not None:
            result['Importance'] = self.importance

        if self.live_message is not None:
            result['LiveMessage'] = self.live_message

        if self.receipt_id is not None:
            result['ReceiptId'] = self.receipt_id

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_params is not None:
            result['TemplateParams'] = self.template_params

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddBadge') is not None:
            self.add_badge = m.get('AddBadge')

        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('Importance') is not None:
            self.importance = m.get('Importance')

        if m.get('LiveMessage') is not None:
            self.live_message = m.get('LiveMessage')

        if m.get('ReceiptId') is not None:
            self.receipt_id = m.get('ReceiptId')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateParams') is not None:
            self.template_params = m.get('TemplateParams')

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
        # OPPO message categorization includes two categories for management: communication and service, and content and marketing. 
        # 
        # **Communication and service (requires permission application):**
        # 
        # - IM: Instant messages.
        # - ACCOUNT: Accounts and assets.
        # - TODO: Schedules and to-do lists.
        # - DEVICE_REMINDER: Device information.
        # - ORDER: Orders and logistics.
        # - SUBSCRIPTION: subscribe reminders.
        # 
        # **Content and marketing:**
        # 
        # - NEWS: News.
        # - CONTENT: Content recommendations.
        # - MARKETING: operational activity.
        # - SOCIAL: Social updates.
        # 
        # For more information, see the [OPPO categorization description](https://open.oppomobile.com/new/developmentDoc/info?id=13189).
        self.category = category
        # The JSON character string of the OPPO Fluid Cloud intent delete data structure [data](https://open.oppomobile.com/documentation/page/info?id=13578). This parameter is invalid if the AndroidOppoIntelligentIntent parameter is already specified. For development and integration, References: [OPPO Fluid Cloud push guide](https://help.aliyun.com/document_detail/2997310.html).
        self.delete_intent_data = delete_intent_data
        # The JSON character string of the OPPO Fluid Cloud intent sharing data structure [IntelligentIntent](https://open.oppomobile.com/documentation/page/info?id=13565). For development and integration, References: [OPPO Fluid Cloud push guide](https://help.aliyun.com/document_detail/2997310.html).
        self.intelligent_intent = intelligent_intent
        # The reminder level for OPPO channel notification bar messages. Valid values:
        # 
        # - 1: Notification bar.
        # - 2: Notification bar, lock screen, ringtone, and vibration (default notification level for communication and service messages).
        # - 16: Notification bar, lock screen, ringtone, vibration, and banner (requires permission application).
        # 
        # > When you use the NotifyLevel parameter, you must also pass the Category parameter.
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
        # The Meizu message type. Valid values:
        # 
        # - 0: Public message (default).
        # - 1: Private message.
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
        # Sets the Huawei fast notification parameter. Valid values:
        # - **0**: Send standard Huawei notifications (default).
        # - **1**: Send Huawei fast notifications.
        self.business_type = business_type
        # Purpose 1: After applying for [self-classification benefits](https://developer.huawei.com/consumer/cn/doc/development/HMSCore-Guides/message-classification-0000001149358835?#section3410731125514), this parameter is used to identify the message type, determine the [message reminder method](https://developer.huawei.com/consumer/cn/doc/development/HMSCore-Guides/message-classification-0000001149358835#ZH-CN_TOPIC_0000001149358835__p3850133955718), and accelerate the delivery of specific types of messages. For valid values, refer to the [message classification standards](https://developer.huawei.com/consumer/cn/doc/development/HMSCore-Guides/message-classification-0000001149358835#section1076611477914) in the official Huawei push documentation, and fill in the "Cloud notification category value" or "Local notification category value" from the documentation table.
        # 
        # Purpose 2: After [applying for special permissions](https://developer.huawei.com/consumer/cn/doc/development/HMSCore-Guides/faq-0000001050042183#section037425218509), this parameter is used to identify high-priority pass-through scenarios. Valid values:
        # 
        # - VOIP: Audio and video calls.
        # - PLAY_VOICE: Voice broadcast.
        # 
        # > - If the "Cloud notification category value" is "Not applicable", the message is sent through the Alibaba Cloud proprietary channel.
        # > - If the "Local notification category value" is "Not applicable", the message is sent through the Huawei channel.
        self.category = category
        # Sets the importance parameter for Huawei notification message classification, which determines the notification behavior on user devices. Valid values:
        # 
        # - 0: Information and marketing messages.
        # - 1: Service and communication messages.
        # 
        # > We recommend that you use Category for notification classification. You must apply on the Huawei platform. See [Application link](https://developer.huawei.com/consumer/cn/doc/development/HMSCore-Guides/message-classification-0000001149358835#section893184112272).
        self.importance = importance
        # The JSON string of the Huawei Android Live Window data structure [LiveNotificationPayload](https://developer.huawei.com/consumer/cn/doc/HMSCore-References/rest-live-0000001562939968#ZH-CN_TOPIC_0000001700850537__p195121620102511). For development and integration, refer to the [Huawei Live Window push guide](https://help.aliyun.com/document_detail/2983768.html).
        self.live_notification_payload = live_notification_payload
        # The receipt ID of the Huawei channel. You can view this receipt ID in the receipt parameter settings of the Huawei channel push operations platform.
        # 
        # > If the default receipt configuration on the Huawei channel push operations platform is set to Alibaba Cloud receipt, you do not need to provide this parameter. Otherwise, we recommend that you configure the default receipt ID for the Huawei channel in the Alibaba Cloud EMAS shift push console first.
        self.receipt_id = receipt_id
        # The delivery priority for Huawei channel notifications. Valid values:
        # 
        # - HIGH
        # - NORMAL
        # 
        # You must apply for permissions. For more information, see [Application link](https://developer.huawei.com/consumer/cn/doc/development/HMSCore-Guides/faq-0000001050042183#section037425218509).
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
        # Sets the importance parameter for Honor notification message classification, which determines the notification behavior on user devices. Valid values:
        # 
        # - 0: Information and marketing messages.
        # - 1: Service and communication messages.
        # 
        # You must apply on the Honor platform. See [Application link](https://developer.honor.com/cn/docs/11002/guides/notification-class#%E8%87%AA%E5%88%86%E7%B1%BB%E6%9D%83%E7%9B%8A%E7%94%B3%E8%AF%B7).
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
        # The custom notification bar style for Android. Valid values: 1 to 100.
        # 
        # > The client must complete the style preset configuration. References: [Custom notification style API](https://help.aliyun.com/document_detail/2834944.html).
        self.custom_style = custom_style
        # The reminder method for the notification. Valid values:
        # 
        # - VIBRATE: Vibration (default).
        # - SOUND: Sound.
        # - BOTH: Sound and vibration.
        # - NONE: Silent.
        self.notify_type = notify_type
        # Specifies the activity to open when the notification is clicked. Valid only when OpenType is set to ACTIVITY.
        self.open_activity = open_activity
        # The action to perform when the notification is clicked. Valid values:
        # 
        # - APPLICATION: Open the application (default).
        # - ACTIVITY: Open the specified activity OpenActivity.
        # - URL: Open a URL.
        # - NONE: No redirection.
        self.open_type = open_type
        # The URL to open when the notification is clicked after an Android device receives the push message. Valid only when OpenType is set to URL.
        self.open_url = open_url
        # The priority of the display position for Android notifications in the notification bar. Valid values: -2, -1, 0, 1, and 2.
        self.priority = priority
        # The message group. Messages in the same group are collapsed and can be expanded in the notification bar. Notifications from different groups are displayed separately.
        # 
        # > Supported by Android SDK 3.9.2 or later.
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
        # The body of the message to be sent.
        self.body = body
        # The title of the message to be sent.
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

