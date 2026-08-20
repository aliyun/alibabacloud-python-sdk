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
        # The push method. Optional parameter. Default value: `PUSH_IMMEDIATELY` (push immediately).
        self.action = action
        # The pass-through message data sent to the device. The total length cannot exceed 4,000 bytes.
        # 
        # > Length calculation notes
        # > - The length is calculated based on the byte length of the UTF-8 encoded string after the Message object is serialized to JSON.
        # > - Chinese characters typically occupy 3 bytes in UTF-8 encoding.
        self.message = message
        # The vendor notification data sent to the device.
        # 
        # >Notice: 
        # 
        # When both `Message` and `Notification` are set, the device receives only one of them. The delivery rules are as follows:
        # 
        # - When the device is online, the pass-through message data is delivered.
        # - When the device is offline, the system notification is sent.
        self.notification = notification
        # The push options.
        self.options = options
        # Specifies the target object for message push. This parameter is optional when the operation type `Action` is set to `CREATE_CONTINUOUS_PUSH` (create a continuous push task).
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
        # The platform type. Optional parameter.
        self.platform = platform
        # The push target type.
        # 
        # >Notice: 
        # 
        # The batch push operation `MassPushV2` and continuous push `CONTINUOUS_PUSH` support only the following three target types:
        # 
        # - `DEVICE`
        # - `ACCOUNT`
        # - `ALIAS`
        self.type = type
        # The push target based on `Target.Type`. Separate multiple targets with commas. The following describes the target types and target values:
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
        # The expiration time of the message. The message will not be sent after it expires. Messages can be retained for up to 72 hours.
        # 
        # > * The time follows the ISO 8601 standard in UTC. Format: YYYY-MM-DDThh:mm:ssZ.
        # > * The expiration time must meet the following condition: ExpireTime > PushTime + 3 seconds (3 seconds is the redundancy for network and system latency).
        # > * Recommendation: Set the expiration time to at least 1 minute for single push notifications and at least 10 minutes for full push or batch push notifications.
        # 
        # 
        # >Notice: For pass-through messages, if no expiration time is set, the message is sent only to online devices. When the device is offline, the message is discarded.
        self.expire_time = expire_time
        # The custom identifier for the push task. When JobKey is not empty, this field is included in the receipt log. For more information about receipt logs, see [Receipt logs](https://help.aliyun.com/document_detail/434651.html).
        self.job_key = job_key
        # The unique ID used to identify the message. This parameter is valid only when the `Action` parameter is set to `CONTINUOUS_PUSH`.
        self.message_id = message_id
        # The scheduled time to send the message. The value cannot be later than 7 days from the current time. This parameter takes effect only when `Action` is set to `SCHEDULED_PUSH`.
        # 
        # > The time follows the ISO 8601 standard in UTC in the format of yyyy-MM-ddTHH:mm:ssZ.
        self.push_time = push_time
        # The supplementary SMS settings.
        self.sms = sms
        # Specifies whether to automatically truncate titles and content that exceed the length limit.
        # 
        # >This parameter applies only to vendor channels that explicitly limit the title and content length. It does not apply to channels such as APNs, Huawei, and Honor that do not limit the title or content length but only limit the total request body size.
        self.trim = trim
        # Specifies the delivery channels. Valid values:
        # 
        # - `accs`: Alibaba Cloud proprietary channel
        # - `huawei`: Huawei channel
        # - `honor`: Honor channel
        # - `xiaomi`: Xiaomi channel
        # - `oppo`: OPPO channel
        # - `vivo`: vivo channel
        # - `meizu`: Meizu channel
        # - `fcm`: Google Firebase channel (HTTP v1 API)
        # - `apns`: APNs channel
        # - `harmony`: HarmonyOS channel
        # 
        # > - If this parameter is not specified, all channels are available.
        # > - If this parameter is specified, only the specified channels are used.
        # > - If the specified channels conflict with the delivery policy (for example, iOS notifications can only be delivered through the APNs channel, but apns is not included in this parameter), the message is not delivered.
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
        # The delay before triggering the SMS message. Unit: seconds.
        # 
        # This parameter is required when SMS linkage is used. We recommend that you set this parameter to at least 15 seconds and no more than 3 days to avoid duplicate notifications from both SMS and push.
        # 
        # > When SMS linkage is used, the ExpireTime parameter does not take effect. The notification expiration time is calculated based on the DelaySecs parameter. The expiration time is the current time plus the DelaySecs value.
        self.delay_secs = delay_secs
        # The key-value pairs of variable names in the SMS template.
        self.params = params
        # The SMS sending policy.
        self.send_policy = send_policy
        # The SMS signature.
        self.sign_name = sign_name
        # The SMS template name. You can obtain this name from the SMS template management page. This is the system-assigned name, not the name set by the developer.
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
        # The body of the push notification.
        self.body = body
        # The HarmonyOS notification configuration.
        self.hmos = hmos
        # The iOS notification configuration.
        self.ios = ios
        # The title of the push notification.
        # 
        # > Length limits:
        # > - iOS/Harmony: The **byte length** cannot exceed 200.
        # > - Android: The **character length** cannot exceed 50.
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
        # iOS notifications are sent through the APNs center. You need to specify the corresponding environment information. Optional parameter. Default value: production environment.
        self.apns_env = apns_env
        # The iOS application badge number.
        self.badge = badge
        # Specifies whether to enable the badge auto-increment feature. Optional parameter. Default value: false.
        self.badge_auto_increment = badge_auto_increment
        # The category identifier for the iOS notification, which defines the interaction behavior and display style of the notification.
        # 
        # > - The category must be pre-registered in the app to take effect.
        # > - Different categories can define different sets of actions.
        self.category = category
        # The unique identifier for notification collapsing. Notifications with the same identifier are overwritten and displayed as one.
        self.collapse_id = collapse_id
        # The custom extension attributes of the iOS notification.
        self.ext_parameters = ext_parameters
        # The interruption level. Optional parameter. Valid values:
        self.interruption_level = interruption_level
        # The Live Activity parameter object.
        # 
        # >Notice: 
        # 
        # - Live Activity push notifications can only be sent to a **single device** by specifying the `DEVICE` type.
        # - When pushing Live Activity notifications, the title and body parameters are optional.
        self.live_activity = live_activity
        # The notification sound for iOS. Specify the name of an audio file stored in the app bundle or the Library/Sounds directory of the sandbox. For more information, see [How to set notification sounds for iOS push](https://help.aliyun.com/document_detail/48906.html).
        # 
        # > - If set to an empty string (""), the notification is silent.
        # > - If not specified, the value defaults to "default", which plays the system alert sound.
        self.music = music
        # Specifies whether to enable the notification extension, which controls whether iOS notifications support processing by Notification Service Extension.
        # > - When sending silent notifications, this parameter must be set to true.
        # > - The Extension processing time cannot exceed 30 seconds.
        # > - A timeout causes the notification to display the original content.
        # > - You must add a Notification Service Extension to your application.
        self.mutable = mutable
        # The relevance score of the notification message, used to control the priority and display strategy of the notification.
        self.relevance_score = relevance_score
        # Specifies whether to enable silent push mode.
        self.silent = silent
        # The subtitle content of the iOS notification.
        self.subtitle = subtitle
        # The thread identifier for iOS notification grouping, which is used to categorize and collapse related notifications.
        # 
        # > - Notifications with the same thread-id are automatically grouped together.
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
        # The static pass-through parameter for iOS Live Activities push notifications, used to pass immutable business identifier information.
        # 
        # > Required when `Event` is set to start.
        self.attributes = attributes
        # The type of the Live Activity to start.
        self.attributes_type = attributes_type
        # The dynamic pass-through parameters of the Live Activity, containing real-time updatable status information and changing data.
        self.content_state = content_state
        # The retention time of an ended Live Activity on the lock screen, allowing users to view information after the activity ends. The value is a UNIX timestamp in seconds.
        self.dismissal_date = dismissal_date
        # Starts, updates, or ends a Live Activity.
        self.event = event
        # The unique identifier of the Live Activity, used to associate the device-side activity instance with the server-side push target.
        self.id = id
        # The expiration timestamp for the iOS Live Activity content, specified as a Unix timestamp in seconds.
        # 
        # > - After the specified time is reached, the system automatically marks the activity as expired.
        # > - Expired activities are removed from the Dynamic Island and Lock Screen.
        # > - This prevents outdated information from occupying the user interface for an extended period.
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
        # The action that corresponds to the ability of the in-app page.
        # 
        # > For more information, refer to [ClickAction.action](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/push-scenariozed-api-request-param-V5#section152462191216) on the HarmonyOS official website.
        self.action = action
        # The incremental badge number for HarmonyOS applications.
        # 
        # > - Supported since HarmonyOS SDK 1.2.0.
        # > - Refer to the HarmonyOS badge [addNum field description](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/push-scenariozed-api-request-param-V5#section266310382145).
        self.badge_add_num = badge_add_num
        # The number to set for the HarmonyOS app badge.
        # 
        # > - Refer to the HarmonyOS badge [setNum field](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/push-scenariozed-api-request-param-V5#section266310382145) description.
        # > - Supported since HarmonyOS SDK version 1.2.0.
        self.badge_set_num = badge_set_num
        # The category of the notification message. This is an optional parameter. Default value: `MARKETING`.
        # 
        # > After you complete the application for the notification message self-classification privilege, this parameter identifies the message type. Different notification message types affect how messages are displayed and how reminders are triggered. For more information, refer to [Notification.category](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/push-scenariozed-api-request-param-V5#section17371529101117) on the HarmonyOS official website.
        self.category = category
        # The custom extension attributes of the notification message, used to pass additional business data.
        self.ext_parameters = ext_parameters
        # The extra data of the notification extension message.
        # 
        # > - Valid when sending HarmonyOS notification extension messages.
        # > - Conceptually equivalent to the extraData field of HarmonyOS notification extension messages. For the specific definition, refer to the HarmonyOS [ExtensionPayload](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/push-scenariozed-api-request-param-V5#section161192514234) documentation.
        # > - Supported since HarmonyOS SDK 1.2.0.
        self.extension_extra_data = extension_extra_data
        # Enables HarmonyOS notification extension.
        # 
        # > - To send notification extension messages, you must first apply for permissions on the HarmonyOS official website. For more information, refer to [HarmonyOS documentation](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V5/push-send-extend-noti-V5) on sending notification extension messages.
        # > - Supported starting from HarmonyOS SDK 1.2.0.
        self.extension_push = extension_push
        # The URL of the large icon displayed on the right side of the notification. The URL must use the HTTPS protocol.
        # 
        # > - Supported image formats include png, jpg, jpeg, heif, gif, and bmp. The image length × width must be less than 25000 pixels.
        # > - For more information, refer to the HarmonyOS official documentation [Notification.image](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/push-scenariozed-api-request-param-V5#section17371529101117).
        self.image_url = image_url
        # When `RenderStyle` is set to `MULTI_LINE`, this field is required to define the content in multi-line text style. A maximum of 3 items are supported.
        self.inbox_content = inbox_content
        # The JSON string of the HarmonyOS Live View data structure [LiveViewPayload](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V13/push-scenariozed-api-request-param-V13#section66881469306). For development and integration, refer to [HarmonyOS Live View Push Guide](https://help.aliyun.com/document_detail/2982112.html).
        self.live_view_payload = live_view_payload
        # The unique identifier (notifyId) for each message displayed in the notification bar. If not provided, the push service automatically generates a unique identifier. Different notification messages can use the same notifyId to enable new messages to overwrite old messages. For more information, see [Notification.notifyId](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/push-scenariozed-api-request-param-V5#section17371529101117) on the HarmonyOS official website.
        self.notify_id = notify_id
        # The receipt ID of the HarmonyOS channel. You can view this receipt ID in the receipt parameter settings on the HarmonyOS channel push operation platform.
        self.receipt_id = receipt_id
        # The notification message style. This is an optional parameter. Default value: normal notification.
        self.render_style = render_style
        # Specifies the notification channel type to use.
        # 
        # > - Valid only for the Alibaba Cloud proprietary channel.
        # > - For more information, refer to the HarmonyOS official documentation [SlotType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/js-apis-notificationmanager-V5#slottype).
        self.slot_type = slot_type
        # The HarmonyOS custom ringtone file name.
        self.sound = sound
        # The custom notification ringtone duration in seconds. Valid values: 1 to 60. The ringtone loops if its duration is shorter than the specified value.
        self.sound_duration = sound_duration
        # Enables the test message.
        # 
        # > - For more information, refer to the HarmonyOS push parameter [TestMessage](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/push-scenariozed-api-request-param-V5#section418321011212).
        self.test_message = test_message
        # The URI that corresponds to the in-app page ability.
        # 
        # > - When multiple Abilities exist, specify the action and URI for each Ability separately. The action is used first to find the corresponding in-app page.
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
        # The full class name of the Activity for the badge setting application entry.
        self.badge_activity = badge_activity
        # The incremental badge count value, which is added to the current badge count.
        # 
        # > - Supported on `Huawei` and `Honor` channels.
        # > - If both `BadgeAddNum` and `BadgeSetNum` are specified, `BadgeSetNum` takes precedence.
        self.badge_add_num = badge_add_num
        # The fixed badge number. Valid values: 1 to 99.
        self.badge_set_num = badge_set_num
        # The channelId of the Android app. This must match the channelId configured in the vendor app.
        self.channel_id = channel_id
        # The custom extension attributes of the Android notification.
        self.ext_parameters = ext_parameters
        # The message group. Only the latest message and the total number of messages received in the group are displayed in the notification bar. All messages are not displayed and cannot be expanded. Currently supported channels:
        # 
        # - Huawei channel
        # - Honor channel
        # - Chinese domestic channel with Android SDK 3.9.1 and earlier
        # 
        # > The Chinese domestic channel no longer supports this parameter in Android SDK 3.9.2 and later.
        self.group_id = group_id
        # The URL of the right-side icon. Currently supported:
        # 
        # - `Huawei EMUI` (applicable only in long text mode and Inbox mode).
        # - `Honor Magic UI` (applicable only in long text mode).
        # - `Custom channel` (Android SDK 3.5.0 and later).
        self.image_url = image_url
        # The body content in Inbox mode. The value must be a valid JSON array with no more than 5 elements. Currently supported on:
        # 
        # - Huawei: EMUI 9 and later
        # - Honor: Magic UI 4.0 and later
        # - Xiaomi: MIUI 10 and later
        # - OPPO: ColorOS later than 5.0
        # - Custom channel: Android SDK 3.6.0 and later
        self.inbox_content = inbox_content
        # The notification sound for the Huawei vendor channel. Specify the audio file name stored in the client project directory `app/src/main/res/raw/` without the file format extension. If not set, the default ringtone is used.
        self.music = music
        # The unique identifier of the Android notification bar message, used to control notification override and replacement behavior. A new notification with the same NotifyId automatically overrides the old notification.
        self.notify_id = notify_id
        # The detailed channel configuration.
        self.options = options
        # The image URL in big picture mode. Currently supported: proprietary channel: Android SDK 3.6.0 and later.
        self.picture_url = picture_url
        # The notification style. Valid values:
        self.render_style = render_style
        # Specifies the notification type for the manufacturer channel. Valid values:
        # 
        # - `false`: Production notification. This is the default value.
        # - `true`: Test notification.
        # 
        # > Currently supported: Huawei channel, Honor channel, vivo channel, and OPPO Fluid Cloud.
        self.test_message = test_message
        # The Activity to open when the notification is tapped.
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
        # The Alibaba Cloud proprietary channel configuration.
        self.accs = accs
        # The Honor channel configuration.
        self.honor = honor
        # The Huawei channel configuration.
        self.huawei = huawei
        # The Meizu channel configuration.
        self.meizu = meizu
        # The OPPO channel configuration.
        self.oppo = oppo
        # The vivo channel configuration.
        self.vivo = vivo
        # The Xiaomi channel configuration.
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
        # The channel ID for Xiaomi notification types. You must apply for this on the Xiaomi platform. For more information, see [Application link](https://dev.mi.com/console/doc/detail?pId=2422#_4).
        # 
        # > A single application can apply for a maximum of 8 channels on the Xiaomi channel. Plan ahead.
        self.channel = channel
        # The JSON character string of the Xiaomi Super Island data structure [miui.focus.param](https://dev.mi.com/xiaomihyperos/documentation/detail?pId=2131). References: [Xiaomi Super Island Push Guide](https://www.alibabacloud.com/help/en/document_detail/3037956.html).
        self.focus_param = focus_param
        # The JSON character string of the Xiaomi Super Island image data [miui.focus.pic_xxx](https://dev.mi.com/xiaomihyperos/documentation/detail?pId=2131). References: [Xiaomi Super Island Push Guide](https://www.alibabacloud.com/help/en/document_detail/3037956.html).
        self.focus_pics = focus_pics
        # The Xiaomi private message template ID.
        self.template_id = template_id
        # The Xiaomi private message template parameters in JSON string format.
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
    ):
        self.add_badge = add_badge
        # vivo categorizes messages into two types: system messages and operational messages.
        # 
        # **System messages:**
        # 
        # - IM: instant messaging
        # - ACCOUNT: accounts and assets
        # - TODO: schedules and to-do items
        # - DEVICE_REMINDER: device information
        # - ORDER: orders and logistics
        # - SUBSCRIPTION: subscription reminders
        # 
        # **Operational messages:**
        # 
        # - NEWS: news
        # - CONTENT: content recommendation
        # - MARKETING: operational activity
        # - SOCIAL: social updates
        # 
        # For more information, refer to [vivo category description](https://dev.vivo.com.cn/documentCenter/doc/359#s-ef3qugc3).
        self.category = category
        # Specifies the vivo notification message category. Valid values:
        # 
        # - `0`: Operational message (default).
        # - `1`: System message.
        # 
        # > Use `Category` for notification classification. You need to apply on the vivo platform. For more information, see [Application link](https://dev.vivo.com.cn/documentCenter/doc/359).
        self.importance = importance
        # The JSON character string of the vivo Atomic Island data structure [liveMessage](https://dev.vivo.com.cn/documentCenter/doc/896#s-fdagzbd4). References: [vivo Atomic Island Push Guide](https://www.alibabacloud.com/help/en/document_detail/3030718.html).
        self.live_message = live_message
        # The message receipt identifier for the vivo vendor push channel, used to receive push result callback notifications.
        self.receipt_id = receipt_id

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
        # OPPO categorizes messages into two types for management: Communication & Service, and Content & Marketing.
        self.category = category
        # The JSON character string of the OPPO Fluid Cloud intent delete data structure [data](https://open.oppomobile.com/documentation/page/info?id=13578). This parameter is invalid when the AndroidOppoIntelligentIntent parameter is already specified. References: [OPPO Fluid Cloud Push Guide](https://help.aliyun.com/document_detail/2997310.html).
        self.delete_intent_data = delete_intent_data
        # The JSON character string of the OPPO Fluid Cloud intent sharing data structure [IntelligentIntent](https://open.oppomobile.com/documentation/page/info?id=13565). References: [OPPO Fluid Cloud Push Guide](https://help.aliyun.com/document_detail/2997310.html).
        self.intelligent_intent = intelligent_intent
        # The notification bar message alert level for the OPPO channel. Valid values:
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
        # The Huawei quick notification parameter.
        self.business_type = business_type
        # Purpose 1: After completing the [self-classification privilege](https://developer.huawei.com/consumer/cn/doc/development/HMSCore-Guides/message-classification-0000001149358835?#section3410731125514) application, this parameter identifies the message type, determines the [notification method](https://developer.huawei.com/consumer/cn/doc/development/HMSCore-Guides/message-classification-0000001149358835#ZH-CN_TOPIC_0000001149358835__p3850133955718), and accelerates delivery for specific message types. For valid values, refer to the [message classification standard](https://developer.huawei.com/consumer/cn/doc/development/HMSCore-Guides/message-classification-0000001149358835#section1076611477914) in the official Huawei Push documentation. Use the value from the "Cloud notification category value" or "Local notification category value" column in the table.
        # 
        # Purpose 2: After [applying for special permissions](https://developer.huawei.com/consumer/cn/doc/development/HMSCore-Guides/faq-0000001050042183#section037425218509), this parameter identifies high-priority pass-through scenarios. Valid values:
        # 
        # - `VOIP`: audio and video calls
        # - `PLAY_VOICE`: voice broadcast
        # 
        # > - For messages where the "Cloud notification category value" is "Not applicable", messages are sent through the Alibaba Cloud proprietary channel.
        # > - For messages where the "Local notification category value" is "Not applicable", messages are sent through the Huawei channel.
        self.category = category
        # The importance parameter for Huawei notification message classification, which determines the notification behavior on the user device. Valid values:
        self.importance = importance
        # The JSON string of the Huawei Android Live Notification data structure [LiveNotificationPayload](https://developer.huawei.com/consumer/cn/doc/HMSCore-References/rest-live-0000001562939968#ZH-CN_TOPIC_0000001700850537__p195121620102511). For development and integration, refer to [Huawei Live Notification Push Guide](https://help.aliyun.com/document_detail/2983768.html).
        self.live_notification_payload = live_notification_payload
        # The receipt ID of the Huawei channel. You can view this receipt ID in the receipt parameter configuration on the Huawei channel push operation platform.
        # 
        # > If the default receipt configuration on the Huawei channel push operation platform is set to Alibaba Cloud receipt, you do not need to provide this parameter. If not, configure the default Huawei channel receipt ID in the Alibaba Cloud EMAS Mobile Push console first.
        self.receipt_id = receipt_id
        # The delivery priority of the Huawei channel notification. Valid values:
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
        # Specifies the importance parameter for Honor notification message classification, which determines the notification behavior on the user\\"s device. Valid values:
        # 
        # - `0`: informational and marketing messages
        # - `1`: service and communication messages
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
        # The custom notification bar style for Android. Valid values: 1 to 100.
        # 
        # > The style preset must be configured on the client. For more information, see [Custom notification style API](https://help.aliyun.com/document_detail/2834944.html).
        self.custom_style = custom_style
        # The notification alert type. Valid values:
        # 
        # - `VIBRATE`: vibration (default)
        # - `SOUND`: sound
        # - `BOTH`: sound and vibration
        # - `NONE`: silent
        self.notify_type = notify_type
        # The activity to open when the notification is tapped. This parameter takes effect only when `OpenType` is set to `ACTIVITY`.
        self.open_activity = open_activity
        # The action after tapping the notification. Valid values:
        self.open_type = open_type
        # The URL to open when the notification is tapped on Android. This is valid when `OpenType` is set to `URL`.
        self.open_url = open_url
        # The priority of the Android notification position in the notification bar. Valid values: -2, -1, 0, 1, 2.
        self.priority = priority
        # The message group. Messages in the same group are collapsed in the notification bar and can be expanded. Messages in different groups are displayed separately.
        # 
        # > Android SDK 3.9.2 and later
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
        # The body of the message to send.
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

