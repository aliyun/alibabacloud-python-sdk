# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_push20160801 import models as main_models
from darabonba.model import DaraModel

class MassPushRequest(DaraModel):
    def __init__(
        self,
        app_key: int = None,
        idempotent_token: str = None,
        push_task: List[main_models.MassPushRequestPushTask] = None,
    ):
        # The AppKey of the application.
        # 
        # This parameter is required.
        self.app_key = app_key
        # An idempotency parameter that prevents duplicate pushes caused by API client retries. If you make a call with the same IdempotentToken within 15 minutes, only one push is performed, and subsequent calls return the result of the first successful push.
        # 
        # > - The parameter format is a standard 36-character UUID (8-4-4-4-12). Each valid character is a hexadecimal digit from 0-9 or a-f, case-insensitive.
        # >
        # > - This parameter only prevents duplicate pushes caused by retries. It cannot prevent duplicate pushes caused by concurrent calls.
        self.idempotent_token = idempotent_token
        # An array of independent push tasks.
        # 
        # This parameter is required.
        self.push_task = push_task

    def validate(self):
        if self.push_task:
            for v1 in self.push_task:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_key is not None:
            result['AppKey'] = self.app_key

        if self.idempotent_token is not None:
            result['IdempotentToken'] = self.idempotent_token

        result['PushTask'] = []
        if self.push_task is not None:
            for k1 in self.push_task:
                result['PushTask'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')

        if m.get('IdempotentToken') is not None:
            self.idempotent_token = m.get('IdempotentToken')

        self.push_task = []
        if m.get('PushTask') is not None:
            for k1 in m.get('PushTask'):
                temp_model = main_models.MassPushRequestPushTask()
                self.push_task.append(temp_model.from_map(k1))

        return self

class MassPushRequestPushTask(DaraModel):
    def __init__(
        self,
        android_activity: str = None,
        android_badge_add_num: int = None,
        android_badge_class: str = None,
        android_badge_set_num: int = None,
        android_big_body: str = None,
        android_big_picture_url: str = None,
        android_big_title: str = None,
        android_ext_parameters: str = None,
        android_honor_target_user_type: int = None,
        android_huawei_business_type: int = None,
        android_huawei_live_notification_payload: str = None,
        android_huawei_receipt_id: str = None,
        android_huawei_target_user_type: int = None,
        android_image_url: str = None,
        android_inbox_body: str = None,
        android_meizu_notice_msg_type: int = None,
        android_message_huawei_category: str = None,
        android_message_huawei_urgency: str = None,
        android_message_oppo_category: str = None,
        android_message_oppo_notify_level: int = None,
        android_message_vivo_category: str = None,
        android_music: str = None,
        android_notification_bar_priority: int = None,
        android_notification_bar_type: int = None,
        android_notification_channel: str = None,
        android_notification_group: str = None,
        android_notification_honor_channel: str = None,
        android_notification_huawei_channel: str = None,
        android_notification_notify_id: int = None,
        android_notification_thread_id: str = None,
        android_notification_vivo_channel: str = None,
        android_notification_xiaomi_channel: str = None,
        android_notify_type: str = None,
        android_open_type: str = None,
        android_open_url: str = None,
        android_oppo_delete_intent_data: str = None,
        android_oppo_intelligent_intent: str = None,
        android_oppo_intent_env: int = None,
        android_oppo_private_content_parameters: Dict[str, str] = None,
        android_oppo_private_msg_template_id: str = None,
        android_oppo_private_title_parameters: Dict[str, str] = None,
        android_popup_activity: str = None,
        android_popup_body: str = None,
        android_popup_title: str = None,
        android_remind: bool = None,
        android_render_style: str = None,
        android_target_user_type: int = None,
        android_vivo_live_message: str = None,
        android_vivo_push_mode: int = None,
        android_vivo_receipt_id: str = None,
        android_xiao_mi_activity: str = None,
        android_xiao_mi_notify_body: str = None,
        android_xiao_mi_notify_title: str = None,
        android_xiaomi_big_picture_url: str = None,
        android_xiaomi_focus_param: str = None,
        android_xiaomi_focus_pics: str = None,
        android_xiaomi_image_url: str = None,
        android_xiaomi_template_id: str = None,
        android_xiaomi_template_params: str = None,
        body: str = None,
        device_type: str = None,
        expire_time: str = None,
        harmony_action: str = None,
        harmony_action_type: str = None,
        harmony_badge_add_num: int = None,
        harmony_badge_set_num: int = None,
        harmony_category: str = None,
        harmony_ext_parameters: str = None,
        harmony_extension_extra_data: str = None,
        harmony_extension_push: bool = None,
        harmony_image_url: str = None,
        harmony_inbox_content: str = None,
        harmony_live_view_payload: str = None,
        harmony_notification_slot_type: str = None,
        harmony_notify_id: int = None,
        harmony_receipt_id: str = None,
        harmony_remind: bool = None,
        harmony_remind_body: str = None,
        harmony_remind_title: str = None,
        harmony_render_style: str = None,
        harmony_test_message: bool = None,
        harmony_uri: str = None,
        job_key: str = None,
        push_time: str = None,
        push_type: str = None,
        send_channels: str = None,
        send_speed: int = None,
        store_offline: bool = None,
        target: str = None,
        target_value: str = None,
        title: str = None,
        trim: bool = None,
        i_osapns_env: str = None,
        i_osbadge: int = None,
        i_osbadge_auto_increment: bool = None,
        i_osext_parameters: str = None,
        i_osinterruption_level: str = None,
        i_oslive_activity_attributes: str = None,
        i_oslive_activity_attributes_type: str = None,
        i_oslive_activity_content_state: str = None,
        i_oslive_activity_dismissal_date: int = None,
        i_oslive_activity_event: str = None,
        i_oslive_activity_id: str = None,
        i_oslive_activity_stale_date: int = None,
        i_osmusic: str = None,
        i_osmutable_content: bool = None,
        i_osnotification_category: str = None,
        i_osnotification_collapse_id: str = None,
        i_osnotification_thread_id: str = None,
        i_osrelevance_score: float = None,
        i_osremind: bool = None,
        i_osremind_body: str = None,
        i_ossilent_notification: bool = None,
        i_ossubtitle: str = None,
    ):
        # Specifies the activity to open when the notification is tapped.
        # 
        # This is required only when PushTask.N.AndroidOpenType is set to "Activity". For example: `com.alibaba.cloudpushdemo.bizactivity`.
        self.android_activity = android_activity
        # Sets the value to add to the badge number. The value is added to the original badge number. The value range is [1, 99].
        # 
        # > This is effective only for pushes through Huawei or Honor vendor channels. If both AndroidBadgeAddNum and AndroidBadgeSetNum are present, AndroidBadgeSetNum takes precedence.
        self.android_badge_add_num = android_badge_add_num
        # The full class name of the entry Activity of the application for badge settings.
        # 
        # > This is effective only for pushes through Huawei or Honor vendor channels.
        self.android_badge_class = android_badge_class
        # Sets a fixed number for the badge. The value range is [0, 99].
        # 
        # > For vendor channel pushes, this is effective only for Huawei and Honor channels. For pushes through Alibaba Cloud\\"s proprietary channel, this is effective only on Huawei, Honor, and vivo models.
        self.android_badge_set_num = android_badge_set_num
        # The body in long text mode. Length limit: 1,000 bytes (one Chinese character is counted as 3 bytes). The actual limit depends on the specific vendor channel.
        # 
        # Currently supported on:
        # 
        # - Huawei: EMUI 10 and later
        # 
        # - Honor: Magic UI 4.0 and later
        # 
        # - Xiaomi: MIUI 10 and later
        # 
        # - OPPO: ColorOS 5.0 and later
        # 
        # - Meizu: Flyme
        # 
        # - Alibaba Cloud\\"s proprietary channel: Android SDK 3.6.0 and later
        # 
        # If this parameter is not provided in long text mode, the first non-empty value from Body or AndroidPopupBody is used.
        self.android_big_body = android_big_body
        # The image URL in big picture mode. Currently supported on: Alibaba Cloud\\"s proprietary channel with Android SDK 3.6.0 or later.
        self.android_big_picture_url = android_big_picture_url
        # The title in long text mode. Length limit: 200 bytes (one Chinese character is counted as 3 bytes).
        # 
        # - Currently, this is only supported by Honor channels and Huawei channels on EMUI 11 and later.
        # 
        # - If this parameter is not provided in long text mode, the first non-empty value from Title or AndroidPopupTitle is used.
        self.android_big_title = android_big_title
        # Sets the extended properties of the notification. This parameter does not take effect when the push type PushType is set to MESSAGE.
        # 
        # This parameter must be passed in JSON map format, or it will fail to parse.
        self.android_ext_parameters = android_ext_parameters
        # Sets the Honor channel notification type:
        # 
        # - **0**: Formal notification (default).
        # 
        # - **1**: Test notification.
        # 
        # > Each application can send 1,000 test notifications per day, and these are not subject to the daily push limit per device.
        self.android_honor_target_user_type = android_honor_target_user_type
        # Sets the parameters for Huawei quick notifications
        # 
        # - **0**: Send a normal Huawei notification (default).
        # 
        # - **1**: Send a Huawei quick notification.
        self.android_huawei_business_type = android_huawei_business_type
        # A JSON string of the Huawei Android Live Notification data structure [LiveNotificationPayload](https://developer.huawei.com/consumer/cn/doc/HMSCore-References/rest-live-0000001562939968#ZH-CN_TOPIC_0000001700850537__p195121620102511). For development and integration, see the [Huawei Live Notification Push Guide](https://help.aliyun.com/document_detail/2983768.html).
        self.android_huawei_live_notification_payload = android_huawei_live_notification_payload
        # The receipt ID for the Huawei channel. View this receipt ID in the receipt parameter configuration on the Huawei Push operations platform.
        # 
        # > If the default receipt configuration on the Huawei Push operations platform is the Alibaba Cloud receipt, you do not need to provide this. If not, we recommend that you first configure the default receipt ID for the Huawei channel in the Alibaba Cloud EMAS Mobile Push console.
        self.android_huawei_receipt_id = android_huawei_receipt_id
        # Sets the Huawei channel notification type:
        # 
        # - **0**: Formal notification (default).
        # 
        # - **1**: Test notification.
        # 
        # > Each application can send 500 test notifications per day, and these are not subject to the daily push limit per device.
        self.android_huawei_target_user_type = android_huawei_target_user_type
        # The URL for the right-side icon. Currently supported on:
        # 
        # - Huawei EMUI (applicable only in long text mode and inbox mode)
        # 
        # - Honor Magic UI (applicable only in long text mode)
        # 
        # - Alibaba Cloud\\"s proprietary channel: Android SDK 3.5.0 and later
        self.android_image_url = android_image_url
        # The body in inbox mode. The content must be a valid JSON array with no more than 5 elements. Currently supported on:
        # 
        # - Huawei: EMUI 9 and later
        # 
        # - Honor: Magic UI 4.0 and later
        # 
        # - Xiaomi: MIUI 10 and later
        # 
        # - OPPO: ColorOS 5.0 and later
        # 
        # - Alibaba Cloud\\"s proprietary channel: Android SDK 3.6.0 and later
        self.android_inbox_body = android_inbox_body
        # Meizu message type
        # 
        # - 0 Public message (default)
        # 
        # - 1 Private message
        self.android_meizu_notice_msg_type = android_meizu_notice_msg_type
        # Function 1: After applying for [self-classification permissions](https://developer.huawei.com/consumer/cn/doc/development/HMSCore-Guides/message-classification-0000001149358835?#section3410731125514), use this parameter to identify the message type, determine the [message reminder method](https://developer.huawei.com/consumer/cn/doc/development/HMSCore-Guides/message-classification-0000001149358835#ZH-CN_TOPIC_0000001149358835__p3850133955718), and expedite the sending of specific message types. For valid values, see the [message classification standards](https://developer.huawei.com/consumer/cn/doc/development/HMSCore-Guides/message-classification-0000001149358835#section1076611477914) in the official Huawei Push documentation. Fill in the "Cloud-side notification category value" or "Local notification category value" from the documentation table.
        # 
        # Function 2: After applying for [special permissions](https://developer.huawei.com/consumer/cn/doc/development/HMSCore-Guides/faq-0000001050042183#section037425218509), use this parameter to identify high-priority pass-through scenarios. Valid values:
        # 
        # - VOIP: Video calls
        # 
        # - PLAY_VOICE: Voice playback
        # 
        # > For "Cloud-side notification category values" that are "Not applicable", all pushes go through Alibaba Cloud\\"s proprietary channel. For "Local notification category values" that are "Not applicable", all pushes go through the Huawei channel.
        self.android_message_huawei_category = android_message_huawei_category
        # The delivery priority for Huawei channel notifications. Valid values:
        # 
        # - HIGH
        # 
        # - NORMAL
        # 
        # You must apply for permissions. For more information, see [Application Link](https://developer.huawei.com/consumer/cn/doc/development/HMSCore-Guides/faq-0000001050042183#section037425218509).
        self.android_message_huawei_urgency = android_message_huawei_urgency
        # OPPO manages messages in two categories: Communication and Services, and Content and Marketing.
        # 
        # Communication and Services (requires permission application):
        # 
        # - IM: Instant messaging, audio, and video calls
        # 
        # - ACCOUNT: Changes in personal accounts and assets
        # 
        # - DEVICE_REMINDER: Personal device reminders
        # 
        # - ORDER: Changes in personal order or logistics status
        # 
        # - TODO: Personal schedules or to-do items
        # 
        # - SUBSCRIPTION: Personal subscriptions
        # 
        # Content and Marketing:
        # 
        # - NEWS: News and information
        # 
        # - CONTENT: Content recommendations
        # 
        # - MARKETING: Platform activities
        # 
        # - SOCIAL: Social updates
        # 
        # For more information, see [OPUSH Message Classification Rules](https://open.oppomobile.com/new/developmentDoc/info?id=13189)
        self.android_message_oppo_category = android_message_oppo_category
        # The reminder level for OPPO channel notification bar messages. Valid values:
        # 
        # - 1: Notification bar
        # 
        # - 2: Notification bar, lock screen, ringtone, vibration (default notification level for Communication and Services messages)
        # 
        # - 16: Notification bar, lock screen, ringtone, vibration, banner (requires permission application)
        # 
        # > When using the AndroidMessageOppoNotifyLevel parameter, you must also pass the AndroidMessageOppoCategory parameter.
        self.android_message_oppo_notify_level = android_message_oppo_notify_level
        # vivo manages messages in two categories: system messages and operational messages.
        # 
        # System messages:
        # 
        # - IM: Instant messages
        # 
        # - ACCOUNT: Account and asset
        # 
        # - TODO: Schedule and to-do
        # 
        # - DEVICE_REMINDER: Device information
        # 
        # - ORDER: Order and logistics
        # 
        # - SUBSCRIPTION: Subscription reminder
        # 
        # Operational messages:
        # 
        # - NEWS: News
        # 
        # - CONTENT: Content recommendation
        # 
        # - MARKETING: Operational activity
        # 
        # - SOCIAL: Social updates
        # 
        # > For more information, see [Classification Description](https://dev.vivo.com.cn/documentCenter/doc/359#s-ef3qugc3)
        self.android_message_vivo_category = android_message_vivo_category
        # The notification sound for the Huawei vendor channel. Specify the name of the audio file stored in the app/src/main/res/raw/ directory of the client project. Do not include the file format suffix.
        # 
        # If you do not set this parameter, the default ringtone is used.
        self.android_music = android_music
        # The priority that determines the position of the Android notification in the notification bar. Valid values: -2, -1, 0, 1, and 2.
        self.android_notification_bar_priority = android_notification_bar_priority
        # The custom Android notification bar style. Valid values: 1 to 100.
        self.android_notification_bar_type = android_notification_bar_type
        # The channel ID for the Android app. It must correspond to a channel ID in the app.
        # 
        # - Set the NotificationChannel parameter. For more information about its use, see [FAQ: Why are notifications not received on devices with Android 8.0 or later?](https://help.aliyun.com/document_detail/67398.html).
        # 
        # - Because the channel_id for the OPPO private message channel is the same as the app\\"s channelId, this value is used for the channel_id when pushing through the OPPO channel.
        # 
        # - For pushes through Huawei, FCM, and Alibaba Cloud\\"s proprietary channels, this value is used for the channel_id.
        self.android_notification_channel = android_notification_channel
        # Message grouping. For messages in the same group, the notification bar displays only the latest message and the total number of messages received for that group. It does not display all messages and cannot be expanded. Currently supported on:
        # 
        # - Huawei vendor channel
        # 
        # - Honor vendor channel
        # 
        # - Alibaba Cloud\\"s proprietary channel with Android SDK 3.9.1 and earlier
        # 
        # > This parameter is not supported by Alibaba Cloud\\"s proprietary channel on Android SDK 3.9.2 and later.
        self.android_notification_group = android_notification_group
        # Sets the importance parameter for Honor notification message classification, which determines the notification behavior on the user\\"s device. Valid values:
        # 
        # - LOW: Marketing messages
        # 
        # - NORMAL: Service and communication messages
        # 
        # Apply for this on the Honor platform. [Application Link](https://developer.honor.com/cn/docs/11002/guides/notification-class#%E8%87%AA%E5%88%86%E7%B1%BB%E6%9D%83%E7%9B%8A%E7%94%B3%E8%AF%B7).
        self.android_notification_honor_channel = android_notification_honor_channel
        # Sets the importance parameter for Huawei notification message classification, which determines the notification behavior on the user\\"s device. Valid values:
        # 
        # - LOW: Marketing messages
        # 
        # - NORMAL: Service and communication messages
        # 
        # > * For the Huawei channel, use AndroidMessageHuaweiCategory for notification classification. AndroidNotificationHuaweiChannel is no longer required.
        # >
        # > * You must apply for this on the Huawei platform. [Application Link](https://developer.huawei.com/consumer/cn/doc/development/HMSCore-Guides/message-classification-0000001149358835#section893184112272).
        self.android_notification_huawei_channel = android_notification_huawei_channel
        # The unique ID for each message when it is displayed as a notification. Different notification messages can have the same NotifyId to allow new notifications to overwrite old ones.
        self.android_notification_notify_id = android_notification_notify_id
        # Message grouping. Messages in the same group are displayed collapsed in the notification bar and can be expanded. Notifications from different groups are displayed separately. Currently supported on:
        # 
        # - Alibaba Cloud\\"s proprietary channel with Android SDK 3.9.2 and later
        self.android_notification_thread_id = android_notification_thread_id
        # Sets the vivo notification message classification. Valid values:
        # 
        # - 0: Operational messages (default)
        # 
        # - 1: System messages
        # 
        # > * For the vivo channel, use AndroidMessageVivoCategory for notification classification. AndroidNotificationVivoChannel is no longer required.
        # >
        # > * Apply for this on the vivo platform. For more information, see [Application Link](https://dev.vivo.com.cn/documentCenter/doc/359).
        self.android_notification_vivo_channel = android_notification_vivo_channel
        # Sets the channel ID for the Xiaomi notification type. Apply for it on the Xiaomi platform. For more information, see [Application Link](https://dev.mi.com/console/doc/detail?pId=2422#_4).
        # 
        # > - A single application can apply for a maximum of 8 channels on the Xiaomi platform. Plan accordingly.
        self.android_notification_xiaomi_channel = android_notification_xiaomi_channel
        # The notification reminder method. Valid values:
        # 
        # - **VIBRATE**: Vibrate (default)
        # 
        # - **SOUND**: Sound
        # 
        # - **BOTH**: Sound and vibrate
        # 
        # - **NONE**: Silent
        self.android_notify_type = android_notify_type
        # The action to take after a notification is tapped. Valid values:
        # 
        # - APPLICATION: Open the application (default)
        # 
        # - ACTIVITY: Open the application\\"s AndroidActivity
        # 
        # - URL: Open a URL
        # 
        # - NONE: No action
        self.android_open_type = android_open_type
        # The URL to open after the Android device receives the push. This is required only when PushTask.N.AndroidOpenType is set to "URL".
        self.android_open_url = android_open_url
        # A JSON string of the OPPO Fluid Cloud intent deletion data structure [data](https://open.oppomobile.com/documentation/page/info?id=13578). This parameter is invalid if the AndroidOppoIntelligentIntent parameter is already filled. For development and integration, see the [OPPO Fluid Cloud Push Guide](https://help.aliyun.com/document_detail/2997310.html).
        self.android_oppo_delete_intent_data = android_oppo_delete_intent_data
        # A JSON string of the OPPO Fluid Cloud intent sharing data structure [IntelligentIntent](https://open.oppomobile.com/documentation/page/info?id=13565). For development and integration, see the [OPPO Fluid Cloud Push Guide](https://help.aliyun.com/document_detail/2997310.html).
        self.android_oppo_intelligent_intent = android_oppo_intelligent_intent
        # Sets the OPPO Fluid Cloud push environment
        # 
        # - **0**: Production environment (default).
        # 
        # - **1**: Staging environment.
        # 
        # > The OPPO Fluid Cloud staging environment needs to be set up on the client side. For more information, see [Environment Setup](https://open.oppomobile.com/documentation/page/info?id=13590).
        self.android_oppo_intent_env = android_oppo_intent_env
        # OPPO private message template content parameters
        self.android_oppo_private_content_parameters = android_oppo_private_content_parameters
        # OPPO private message template ID
        # 
        # >Warning: 
        # 
        # The OPPO private message template feature is no longer supported by MaasPush. To use this feature, use the Push, PushV2, or MassPushV2 API instead.
        self.android_oppo_private_msg_template_id = android_oppo_private_msg_template_id
        # OPPO private message template title parameters
        self.android_oppo_private_title_parameters = android_oppo_private_title_parameters
        # Specifies the Activity to which the user is redirected after tapping the notification.
        self.android_popup_activity = android_popup_activity
        # The body content in auxiliary pop-up mode. This parameter is required if the AndroidPopupActivity parameter is not empty.
        # 
        # Length limit: 200 characters. Both Chinese and English characters count as one.
        # 
        # If you use a vendor channel, comply with the vendor channel\\"s restrictions. For more information, see [Limits on auxiliary channel pushes for Android](https://help.aliyun.com/document_detail/165253.html).
        self.android_popup_body = android_popup_body
        # The title content in auxiliary pop-up mode. This parameter is required if the AndroidPopupActivity parameter is not empty.
        # 
        # Length limit: 50 characters. Both Chinese and English characters count as one.
        # 
        # If you use a vendor channel, comply with the vendor channel\\"s restrictions. For more information, see [Limits on auxiliary channel pushes for Android](https://help.aliyun.com/document_detail/165253.html).
        self.android_popup_title = android_popup_title
        # If the push type is MESSAGE and the device is offline, this push uses the auxiliary pop-up feature. The default value is false. This parameter takes effect only when PushType is MESSAGE.
        # 
        # If a message is successfully converted to a notification, the displayed notification uses the values of the AndroidPopupTitle and AndroidPopupBody parameters. When the user taps the notification, the data retrieved by the onSysNoticeOpened method of the auxiliary pop-up uses the values of the Title and Body parameters.
        self.android_remind = android_remind
        # The notification style. Valid values:
        # 
        # - **0**: Standard mode (default)
        # 
        # - **1**: Long text mode (supported by Huawei, Honor, Xiaomi, OPPO, Meizu, and Alibaba Cloud\\"s proprietary channel)
        # 
        # - **2**: Big picture mode (supported by Alibaba Cloud\\"s proprietary channel, not supported on Xiaomi models)
        # 
        # - **3**: List mode (supported by Huawei, Honor, Xiaomi, OPPO, and Alibaba Cloud\\"s proprietary channel)
        # 
        # > This parameter is required for non-standard modes.
        self.android_render_style = android_render_style
        # Sets the vendor channel notification type:
        # 
        # - **0**: Formal notification (default).
        # 
        # - **1**: Test notification.
        # 
        # > * Configuring this parameter is equivalent to configuring the AndroidHuaweiTargetUserType, AndroidHonorTargetUserType, AndroidVivoPushMode, and AndroidOppoIntentEnv parameters at the same time. A specific vendor channel parameter can override this parameter.
        # >
        # > * Currently supported: Huawei channel, Honor channel, vivo channel, OPPO Fluid Cloud.
        self.android_target_user_type = android_target_user_type
        # A JSON string of the vivo Atomic Island data structure [liveMessage](https://dev.vivo.com.cn/documentCenter/doc/896#s-fdagzbd4). For development and integration, see the [vivo Atomic Island Push Guide](https://help.aliyun.com/zh/document_detail/3030718.html).
        self.android_vivo_live_message = android_vivo_live_message
        # Sets the vivo channel notification type:
        # 
        # - **0**: Formal push (default).
        # 
        # - **1**: Test push.
        # 
        # > For test pushes, configure the test devices in the vivo console beforehand. You can obtain the test device\\"s RegId by searching for "onReceiveRegId regId" in the device startup logs.
        self.android_vivo_push_mode = android_vivo_push_mode
        # The receipt ID for the vivo channel. View this receipt ID in the application information of the push service on the vivo open platform.
        # 
        # > If the default receipt configuration on the vivo open platform is the Alibaba Cloud receipt, you do not need to provide this. If not, we recommend that you first configure the default receipt ID for the vivo channel in the Alibaba Cloud EMAS Mobile Push console.
        self.android_vivo_receipt_id = android_vivo_receipt_id
        # This parameter is deprecated. All third-party auxiliary pop-ups are now supported by the new **AndroidPopupActivity** parameter.
        self.android_xiao_mi_activity = android_xiao_mi_activity
        # This parameter is deprecated. All third-party auxiliary pop-ups are now supported by the new **AndroidPopupBody** parameter.
        self.android_xiao_mi_notify_body = android_xiao_mi_notify_body
        # This parameter is deprecated. All third-party auxiliary pop-ups are now supported by the new **AndroidPopupTitle** parameter.
        self.android_xiao_mi_notify_title = android_xiao_mi_notify_title
        # This parameter is deprecated. Since August 2023, Xiaomi no longer supports dynamically setting small icons, right-side icons, or large pictures during pushes on new devices or systems.
        self.android_xiaomi_big_picture_url = android_xiaomi_big_picture_url
        # A JSON string of the Xiaomi HyperOS Island data structure [miui.focus.param](https://dev.mi.com/xiaomihyperos/documentation/detail?pId=2131). For development and integration, see the [Xiaomi HyperOS Island Push Guide](https://help.aliyun.com/zh/document_detail/3037956.html).
        self.android_xiaomi_focus_param = android_xiaomi_focus_param
        # A JSON string of the Xiaomi HyperOS Island data image [miui.focus.pic_xxx](https://dev.mi.com/xiaomihyperos/documentation/detail?pId=2131). For development and integration, see the [Xiaomi HyperOS Island Push Guide](https://help.aliyun.com/zh/document_detail/3037956.html).
        self.android_xiaomi_focus_pics = android_xiaomi_focus_pics
        # This parameter is deprecated. Since August 2023, Xiaomi no longer supports dynamically setting small icons, right-side icons, or large pictures during pushes on new devices or systems.
        self.android_xiaomi_image_url = android_xiaomi_image_url
        self.android_xiaomi_template_id = android_xiaomi_template_id
        self.android_xiaomi_template_params = android_xiaomi_template_params
        # The content of the notification or message for Android and HarmonyOS pushes. The content of the message or notification for iOS. The content size is limited. For more information, see [Product limits](https://help.aliyun.com/document_detail/92832.html).
        self.body = body
        # The device type. Valid values:
        # 
        # - HARMONY: HarmonyOS devices
        # 
        # - iOS: iOS devices
        # 
        # - ANDROID: Android devices
        # 
        # - ALL: If the AppKey is for an old version of a dual-platform application, this value indicates that pushes are sent to both Android and iOS devices. If the AppKey is for a new version of a single-platform application, the effect is the same as specifying the device type corresponding to that application type.
        # 
        # This parameter is required.
        self.device_type = device_type
        # The time-to-live (TTL) for offline messages or notifications. Use this with StoreOffline. After the TTL expires, the message or notification is no longer sent. The maximum TTL is 72 hours. The default is 72 hours.
        # 
        # The time must be in ISO 8601 format and in UTC: YYYY-MM-DDThh:mm:ssZ. The expiration time must be at least 3 seconds later than the current time or the scheduled push time (`ExpireTime > PushTime + 3 seconds`). The 3-second buffer accounts for potential network and system latency. Set the TTL to at least 1 minute for individual pushes and at least 10 minutes for full or batch pushes.
        self.expire_time = expire_time
        # The action corresponding to the in-app page ability.
        # 
        # >Notice: 
        # 
        # When HarmonyActionType is APP_CUSTOM_PAGE, at least one of HarmonyUri and HarmonyAction must be filled in.
        # 
        # 
        # 
        # For more information, see [ClickAction.action](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/push-scenariozed-api-request-param-V5#section152462191216) on the HarmonyOS website.
        self.harmony_action = harmony_action
        # The action to take after a notification is tapped. Valid values:
        # 
        # - APP_HOME_PAGE: Open the application home page
        # 
        # - APP_CUSTOM_PAGE: Open a custom application page
        self.harmony_action_type = harmony_action_type
        # The number to add to the HarmonyOS application badge. See the [HarmonyOS badge addNum field description](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/push-scenariozed-api-request-param-V5#section266310382145).<br>
        # Supported starting from HarmonyOS SDK version 1.2.0.<br>
        self.harmony_badge_add_num = harmony_badge_add_num
        # The number to set for the HarmonyOS application badge. See the [HarmonyOS badge setNum field description](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/push-scenariozed-api-request-param-V5#section266310382145).<br>
        # Supported starting from HarmonyOS SDK version 1.2.0.<br>
        self.harmony_badge_set_num = harmony_badge_set_num
        # The notification message category. After applying for notification message self-classification permissions, use this to identify the message type. Different notification message types affect how messages are displayed and reminded. Valid values:
        # 
        # - IM: Instant messaging
        # 
        # - VOIP: Video call
        # 
        # - SUBSCRIPTION: Subscription
        # 
        # - TRAVEL: Travel
        # 
        # - HEALTH: Health
        # 
        # - WORK: Work item reminder
        # 
        # - ACCOUNT: Account updates
        # 
        # - EXPRESS: Order & logistics
        # 
        # - FINANCE: Finance
        # 
        # - DEVICE_REMINDER: Device reminder
        # 
        # - MAIL: Email
        # 
        # - CUSTOMER_SERVICE: Customer service message
        # 
        # - MARKETING: News, content recommendations, social updates, product promotions, financial updates, lifestyle information, surveys, feature recommendations, and operational activities (only identifies content, does not expedite message sending), collectively referred to as marketing messages.
        # 
        # For more information, see [Notification.category](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/push-scenariozed-api-request-param-V5#section17371529101117) on the HarmonyOS website.
        self.harmony_category = harmony_category
        # Sets the extended properties of the notification. This parameter does not take effect when the push type PushType is set to MESSAGE.
        # 
        # This parameter must be passed in JSON map format, or it will fail to parse.
        self.harmony_ext_parameters = harmony_ext_parameters
        # Extra data for the extended notification message.<br>
        # Effective when sending HarmonyOS extended notification messages.<br>
        # Conceptually equivalent to the extraData field of a HarmonyOS extended notification message. For a detailed definition, see [HarmonyOS ExtensionPayload Description](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/push-scenariozed-api-request-param-V5#section161192514234).<br>
        # Supported starting from HarmonyOS SDK version 1.2.0.<br><br><br>
        self.harmony_extension_extra_data = harmony_extension_extra_data
        # When PushType is NOTICE, specifies whether it is a HarmonyOS extended notification message.
        # 
        # - true: Send an extended notification message
        # 
        # - false: Send a normal notification (default)
        # 
        # You must apply for permission on the HarmonyOS side before sending extended notification messages. For more information, see [Send Extended Notification Messages](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V5/push-send-extend-noti-V5) in the HarmonyOS documentation.<br>
        # Supported starting from HarmonyOS SDK version 1.2.0.<br>
        self.harmony_extension_push = harmony_extension_push
        # The URL for the large icon on the right of the notification. The URL must use the HTTPS protocol.
        # 
        # > Supported image formats are png, jpg, jpeg, heif, gif, and bmp. The image length × width must be less than 25,000 pixels.
        # 
        # For more information, see [Notification.image](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/push-scenariozed-api-request-param-V5#section17371529101117) on the HarmonyOS website.
        self.harmony_image_url = harmony_image_url
        # The content for the multi-line text style. This field is required when HarmonyRenderStyle is MULTI_LINE. A maximum of 3 content entries are supported.
        self.harmony_inbox_content = harmony_inbox_content
        # A JSON string of the HarmonyOS Live Window data structure [LiveViewPayload](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V13/push-scenariozed-api-request-param-V13#section66881469306). For development and integration, see the [HarmonyOS Live Window Push Guide](https://help.aliyun.com/document_detail/2982112.html).
        self.harmony_live_view_payload = harmony_live_view_payload
        # Uses the specified type of notification channel. This is effective only when the Alibaba Cloud proprietary channel is online.
        # 
        # - SOCIAL_COMMUNICATION: Social communication.
        # 
        # - SERVICE_INFORMATION: Service reminder.
        # 
        # - CONTENT_INFORMATION: Content information.
        # 
        # - CUSTOMER_SERVICE: Customer service message. This type is used for customer service messages between users and businesses and must be initiated by the user.
        # 
        # - OTHER_TYPES: Other.
        # 
        # For more information, see [SlotType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/js-apis-notificationmanager-V5#slottype) on the HarmonyOS website.
        self.harmony_notification_slot_type = harmony_notification_slot_type
        # The unique ID for each message when it is displayed as a notification. If not included, the push service automatically generates a unique ID for each message. Different notification messages can have the same notifyId to allow new messages to overwrite old ones.
        # 
        # For more information, see [Notification.notifyId](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/push-scenariozed-api-request-param-V5#section17371529101117) on the HarmonyOS website.
        self.harmony_notify_id = harmony_notify_id
        # The receipt ID for the HarmonyOS channel. View this receipt ID in the receipt parameter configuration on the HarmonyOS Push operations platform.
        # 
        # > If the default receipt configuration on the HarmonyOS Push operations platform is the Alibaba Cloud receipt, you do not need to provide this. If not, we recommend that you first configure the default receipt ID for the HarmonyOS channel in the Alibaba Cloud EMAS Mobile Push console.
        # 
        # For more information, see [pushOptions.receiptId](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/push-scenariozed-api-request-param-V5#section418321011212) on the HarmonyOS website.
        self.harmony_receipt_id = harmony_receipt_id
        # If the push type is MESSAGE and the device is offline, this push uses the auxiliary pop-up feature. The default value is false. This parameter is effective only when PushType is set to MESSAGE.
        # 
        # If a message is successfully converted to a notification, the data displayed in the notification is the value of the server-side HarmonyRemindTitle and HarmonyRemindBody parameters.
        self.harmony_remind = harmony_remind
        # The HarmonyOS notification content used when a message is converted to a notification. This is effective only when HarmonyRemind is set to true.
        self.harmony_remind_body = harmony_remind_body
        # The HarmonyOS notification title used when a message is converted to a notification. This is effective only when HarmonyRemind is set to true.
        self.harmony_remind_title = harmony_remind_title
        # The notification message style:
        # 
        # - NORMAL: Normal notification (default)
        # 
        # - MULTI_LINE: Multi-line text style
        self.harmony_render_style = harmony_render_style
        # The test message flag:
        # 
        # - false: Normal message (default)
        # 
        # - true: Test message
        # 
        # For more information, see [pushOptions.testMessage](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/push-scenariozed-api-request-param-V5#section418321011212) on the HarmonyOS website.
        self.harmony_test_message = harmony_test_message
        # The URI corresponding to the in-app page ability.
        # >Notice: When HarmonyActionType is APP_CUSTOM_PAGE, at least one of HarmonyUri and HarmonyAction must be filled in. When there are multiple Abilities, fill in the action and URI for each Ability separately. The action is used with priority to find the corresponding in-app page.
        # 
        # For more information, see [ClickAction.uri](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/push-scenariozed-api-request-param-V5#section152462191216) on the HarmonyOS website.
        self.harmony_uri = harmony_uri
        # A custom ID for the push task. If JobKey is not empty, this field is included in the receipt logs. For more information about how to view receipt logs, see [Receipt logs](https://help.aliyun.com/document_detail/434651.html).
        self.job_key = job_key
        # Specifies the time for a scheduled push. If you do not set this parameter, the push is sent immediately.
        # 
        # The time must be in ISO 8601 format and in UTC: YYYY-MM-DDThh:mm:ssZ.
        self.push_time = push_time
        # The push type. Valid values:
        # 
        # - MESSAGE: a message.
        # 
        # - NOTICE: a notification.
        # 
        # This parameter is required.
        self.push_type = push_type
        # Specifies the sending channels. Valid values:
        # 
        # - accs: Alibaba Cloud\\"s proprietary channel
        # 
        # - huawei: Huawei channel
        # 
        # - honor: Honor channel
        # 
        # - xiaomi: Xiaomi channel
        # 
        # - oppo: OPPO channel
        # 
        # - vivo: vivo channel
        # 
        # - meizu: Meizu channel
        # 
        # - gcm: Google GCM channel (legacy HTTP)
        # 
        # - fcm: Google Firebase channel (HTTP v1 API)
        # 
        # - apns: APNs channel
        # 
        # - harmony: HarmonyOS channel
        # 
        # > * If you do not configure this parameter, all channels can be used.
        # >
        # > * If you configure this parameter, only the specified channels are used.
        # >
        # > * If the configured channels conflict with the sending policy (for example, iOS notifications are sent only through the APNs channel, but this parameter does not include apns), the push is not sent.
        # >
        # > * If you configure gcm, both Google GCM and FCM channels can be used. If you configure fcm, only the Google FCM channel can be used.
        self.send_channels = send_channels
        # This parameter is deprecated.
        self.send_speed = send_speed
        # Specifies whether to save offline messages or notifications. The default value is false.
        # 
        # If you save them, and a user is offline, the message or notification is resent when the user comes online before the time-to-live (TTL) specified by ExpireTime expires. The default TTL is 72 hours. iOS notifications are sent through the APNs channel and are not affected by this parameter.
        self.store_offline = store_offline
        # The push target. Valid values:
        # 
        # - DEVICE: Push by device.
        # 
        # - ACCOUNT: Push by account.
        # 
        # - ALIAS: Push by alias.
        # 
        # This parameter is required.
        self.target = target
        # Set this parameter based on the value of Target. To specify multiple values, separate them with commas. If you exceed the limit, send multiple pushes.
        # 
        # - If you set Target to DEVICE, specify device IDs, such as `deviceid1,deviceid2`. You can specify up to 1,000 device IDs.
        # 
        # - If you set Target to ACCOUNT, specify accounts, such as `account1,account2`. You can specify up to 1,000 accounts.
        # 
        # - If you set Target to ALIAS, specify aliases, such as `alias1,alias2`. You can specify up to 1,000 aliases.
        # 
        # This parameter is required.
        self.target_value = target_value
        # The title of the notification or message. The length is limited to 200 bytes.
        # This parameter is required for Android and HarmonyOS pushes. It is optional for iOS notification pushes. If you specify it for iOS:
        # 
        # - For iOS 10 and later, the notification title is displayed.
        # 
        # - For iOS versions from 8.2 to 10, it replaces the application name in the notification.
        self.title = title
        # Specifies whether to automatically truncate titles and content that are too long.
        # Note: This applies only to vendor channels that have explicit limits on title and content length. It does not apply to channels such as APNs, Huawei, and Honor, which limit the total request body size instead of the title and content length.
        self.trim = trim
        # iOS notifications are sent through APNs. Specify the environment information.
        # 
        # - DEV: The development environment. This applies to applications installed and debugged directly from Xcode.
        # 
        # - PRODUCT: The production environment. This applies to applications distributed through the App Store, TestFlight, Ad Hoc, or enterprise distribution.
        self.i_osapns_env = i_osapns_env
        # The badge number on the top-right corner of the iOS application icon.
        # 
        # > If iOSBadgeAutoIncrement is set to true, this parameter must be empty.
        self.i_osbadge = i_osbadge
        # Specifies whether to enable the auto-increment badge feature. The default value is false.
        # 
        # > When this is set to true, iOSBadge must be empty.
        # 
        # The auto-increment badge feature is maintained by the push server, which keeps a badge count for each device. To use this feature, use SDK version 1.9.5 or later and actively sync the badge number to the server.
        self.i_osbadge_auto_increment = i_osbadge_auto_increment
        # The extended properties for iOS notifications.
        # 
        # For iOS 10 and later, specify the resource URL for a rich push notification, such as `{"attachment": "https://xxxx.xxx/notification_pic.png"}`. This parameter must be passed in JSON map format, or it will fail to parse.
        self.i_osext_parameters = i_osext_parameters
        # The interruption level. Valid values:
        # 
        # - passive: The system adds the notification to the notification list without lighting up the screen or playing a sound.
        # 
        # - active: The system immediately displays the notification, lights up the screen, and can play a sound.
        # 
        # - time-sensitive: The system immediately presents the notification, lights up the screen, and can play a sound, but does not break through system notification controls.
        # 
        # - critical: The system immediately displays the notification, lights up the screen, and plays a sound, bypassing the mute switch.
        self.i_osinterruption_level = i_osinterruption_level
        # A JSON string for the static pass-through parameters of a Dynamic Island push. It contains static, user-defined information, such as product numbers and order information.
        # 
        # > Required when iOSLiveActivityEvent is set to start.
        self.i_oslive_activity_attributes = i_oslive_activity_attributes
        # The type of Live Activity to start.
        # 
        # > Required when iOSLiveActivityEvent is set to start.
        self.i_oslive_activity_attributes_type = i_oslive_activity_attributes_type
        # The dynamic pass-through parameters for a Dynamic Island push. It contains real-time updated information, such as price or inventory changes.
        self.i_oslive_activity_content_state = i_oslive_activity_content_state
        # The time until which an ended Live Activity remains on the lock screen. The maximum duration is 4 hours.
        self.i_oslive_activity_dismissal_date = i_oslive_activity_dismissal_date
        # Starts, updates, or ends a Live Activity.
        # 
        # - Enumeration: start | update | end
        self.i_oslive_activity_event = i_oslive_activity_event
        # The Live Activity ID reported by the device to your server. This is the unique identifier for a Live Activity.
        self.i_oslive_activity_id = i_oslive_activity_id
        # A UNIX timestamp in seconds that marks the content of the activity as outdated.
        self.i_oslive_activity_stale_date = i_oslive_activity_stale_date
        # The sound for the iOS notification. Specify the name of the audio file stored in the app bundle or the Library/Sounds directory of the sandbox. For more information, see How to set notification sounds for iOS pushes.
        # 
        # If you specify an empty string (""), the notification is silent. If you do not set this parameter, the default value is \\"default\\", which is the system alert sound.
        self.i_osmusic = i_osmusic
        # The mutable content flag for iOS notifications (for iOS 10 and later). If set to true, notifications pushed through APNs can be processed by an extension before being displayed. For silent notifications, this must be set to true.
        self.i_osmutable_content = i_osmutable_content
        # Specifies the iOS notification category (for iOS 10 and later).
        self.i_osnotification_category = i_osnotification_category
        # If a device receives messages with the same CollapseId, they are merged into one. If the device is offline and receives multiple messages with the same CollapseId, only one is displayed in the notification bar. This parameter is supported on iOS 10 and later.
        self.i_osnotification_collapse_id = i_osnotification_collapse_id
        # Groups iOS remote notifications using this property. It marks the identifier for a collapsed group. This is supported only on iOS 12.0 and later.
        self.i_osnotification_thread_id = i_osnotification_thread_id
        # The score for highlighting the summary. The value must be a floating-point number from 0 to 1.
        self.i_osrelevance_score = i_osrelevance_score
        # If a device is offline when a message is pushed (meaning the persistent connection to the Mobile Push server is unavailable), this push is sent once as a notification through the Apple APNs channel.
        # 
        # > Converting offline messages to notifications is only applicable to the production environment.
        self.i_osremind = i_osremind
        # The content of the iOS notification when an iOS message is converted to a notification. This parameter is valid only when iOSApnsEnv is set to PRODUCT and iOSRemind is set to true.
        self.i_osremind_body = i_osremind_body
        # Specifies whether to enable iOS silent notifications.
        self.i_ossilent_notification = i_ossilent_notification
        # The subtitle of the iOS notification (for iOS 10 and later).
        self.i_ossubtitle = i_ossubtitle

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.android_activity is not None:
            result['AndroidActivity'] = self.android_activity

        if self.android_badge_add_num is not None:
            result['AndroidBadgeAddNum'] = self.android_badge_add_num

        if self.android_badge_class is not None:
            result['AndroidBadgeClass'] = self.android_badge_class

        if self.android_badge_set_num is not None:
            result['AndroidBadgeSetNum'] = self.android_badge_set_num

        if self.android_big_body is not None:
            result['AndroidBigBody'] = self.android_big_body

        if self.android_big_picture_url is not None:
            result['AndroidBigPictureUrl'] = self.android_big_picture_url

        if self.android_big_title is not None:
            result['AndroidBigTitle'] = self.android_big_title

        if self.android_ext_parameters is not None:
            result['AndroidExtParameters'] = self.android_ext_parameters

        if self.android_honor_target_user_type is not None:
            result['AndroidHonorTargetUserType'] = self.android_honor_target_user_type

        if self.android_huawei_business_type is not None:
            result['AndroidHuaweiBusinessType'] = self.android_huawei_business_type

        if self.android_huawei_live_notification_payload is not None:
            result['AndroidHuaweiLiveNotificationPayload'] = self.android_huawei_live_notification_payload

        if self.android_huawei_receipt_id is not None:
            result['AndroidHuaweiReceiptId'] = self.android_huawei_receipt_id

        if self.android_huawei_target_user_type is not None:
            result['AndroidHuaweiTargetUserType'] = self.android_huawei_target_user_type

        if self.android_image_url is not None:
            result['AndroidImageUrl'] = self.android_image_url

        if self.android_inbox_body is not None:
            result['AndroidInboxBody'] = self.android_inbox_body

        if self.android_meizu_notice_msg_type is not None:
            result['AndroidMeizuNoticeMsgType'] = self.android_meizu_notice_msg_type

        if self.android_message_huawei_category is not None:
            result['AndroidMessageHuaweiCategory'] = self.android_message_huawei_category

        if self.android_message_huawei_urgency is not None:
            result['AndroidMessageHuaweiUrgency'] = self.android_message_huawei_urgency

        if self.android_message_oppo_category is not None:
            result['AndroidMessageOppoCategory'] = self.android_message_oppo_category

        if self.android_message_oppo_notify_level is not None:
            result['AndroidMessageOppoNotifyLevel'] = self.android_message_oppo_notify_level

        if self.android_message_vivo_category is not None:
            result['AndroidMessageVivoCategory'] = self.android_message_vivo_category

        if self.android_music is not None:
            result['AndroidMusic'] = self.android_music

        if self.android_notification_bar_priority is not None:
            result['AndroidNotificationBarPriority'] = self.android_notification_bar_priority

        if self.android_notification_bar_type is not None:
            result['AndroidNotificationBarType'] = self.android_notification_bar_type

        if self.android_notification_channel is not None:
            result['AndroidNotificationChannel'] = self.android_notification_channel

        if self.android_notification_group is not None:
            result['AndroidNotificationGroup'] = self.android_notification_group

        if self.android_notification_honor_channel is not None:
            result['AndroidNotificationHonorChannel'] = self.android_notification_honor_channel

        if self.android_notification_huawei_channel is not None:
            result['AndroidNotificationHuaweiChannel'] = self.android_notification_huawei_channel

        if self.android_notification_notify_id is not None:
            result['AndroidNotificationNotifyId'] = self.android_notification_notify_id

        if self.android_notification_thread_id is not None:
            result['AndroidNotificationThreadId'] = self.android_notification_thread_id

        if self.android_notification_vivo_channel is not None:
            result['AndroidNotificationVivoChannel'] = self.android_notification_vivo_channel

        if self.android_notification_xiaomi_channel is not None:
            result['AndroidNotificationXiaomiChannel'] = self.android_notification_xiaomi_channel

        if self.android_notify_type is not None:
            result['AndroidNotifyType'] = self.android_notify_type

        if self.android_open_type is not None:
            result['AndroidOpenType'] = self.android_open_type

        if self.android_open_url is not None:
            result['AndroidOpenUrl'] = self.android_open_url

        if self.android_oppo_delete_intent_data is not None:
            result['AndroidOppoDeleteIntentData'] = self.android_oppo_delete_intent_data

        if self.android_oppo_intelligent_intent is not None:
            result['AndroidOppoIntelligentIntent'] = self.android_oppo_intelligent_intent

        if self.android_oppo_intent_env is not None:
            result['AndroidOppoIntentEnv'] = self.android_oppo_intent_env

        if self.android_oppo_private_content_parameters is not None:
            result['AndroidOppoPrivateContentParameters'] = self.android_oppo_private_content_parameters

        if self.android_oppo_private_msg_template_id is not None:
            result['AndroidOppoPrivateMsgTemplateId'] = self.android_oppo_private_msg_template_id

        if self.android_oppo_private_title_parameters is not None:
            result['AndroidOppoPrivateTitleParameters'] = self.android_oppo_private_title_parameters

        if self.android_popup_activity is not None:
            result['AndroidPopupActivity'] = self.android_popup_activity

        if self.android_popup_body is not None:
            result['AndroidPopupBody'] = self.android_popup_body

        if self.android_popup_title is not None:
            result['AndroidPopupTitle'] = self.android_popup_title

        if self.android_remind is not None:
            result['AndroidRemind'] = self.android_remind

        if self.android_render_style is not None:
            result['AndroidRenderStyle'] = self.android_render_style

        if self.android_target_user_type is not None:
            result['AndroidTargetUserType'] = self.android_target_user_type

        if self.android_vivo_live_message is not None:
            result['AndroidVivoLiveMessage'] = self.android_vivo_live_message

        if self.android_vivo_push_mode is not None:
            result['AndroidVivoPushMode'] = self.android_vivo_push_mode

        if self.android_vivo_receipt_id is not None:
            result['AndroidVivoReceiptId'] = self.android_vivo_receipt_id

        if self.android_xiao_mi_activity is not None:
            result['AndroidXiaoMiActivity'] = self.android_xiao_mi_activity

        if self.android_xiao_mi_notify_body is not None:
            result['AndroidXiaoMiNotifyBody'] = self.android_xiao_mi_notify_body

        if self.android_xiao_mi_notify_title is not None:
            result['AndroidXiaoMiNotifyTitle'] = self.android_xiao_mi_notify_title

        if self.android_xiaomi_big_picture_url is not None:
            result['AndroidXiaomiBigPictureUrl'] = self.android_xiaomi_big_picture_url

        if self.android_xiaomi_focus_param is not None:
            result['AndroidXiaomiFocusParam'] = self.android_xiaomi_focus_param

        if self.android_xiaomi_focus_pics is not None:
            result['AndroidXiaomiFocusPics'] = self.android_xiaomi_focus_pics

        if self.android_xiaomi_image_url is not None:
            result['AndroidXiaomiImageUrl'] = self.android_xiaomi_image_url

        if self.android_xiaomi_template_id is not None:
            result['AndroidXiaomiTemplateId'] = self.android_xiaomi_template_id

        if self.android_xiaomi_template_params is not None:
            result['AndroidXiaomiTemplateParams'] = self.android_xiaomi_template_params

        if self.body is not None:
            result['Body'] = self.body

        if self.device_type is not None:
            result['DeviceType'] = self.device_type

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.harmony_action is not None:
            result['HarmonyAction'] = self.harmony_action

        if self.harmony_action_type is not None:
            result['HarmonyActionType'] = self.harmony_action_type

        if self.harmony_badge_add_num is not None:
            result['HarmonyBadgeAddNum'] = self.harmony_badge_add_num

        if self.harmony_badge_set_num is not None:
            result['HarmonyBadgeSetNum'] = self.harmony_badge_set_num

        if self.harmony_category is not None:
            result['HarmonyCategory'] = self.harmony_category

        if self.harmony_ext_parameters is not None:
            result['HarmonyExtParameters'] = self.harmony_ext_parameters

        if self.harmony_extension_extra_data is not None:
            result['HarmonyExtensionExtraData'] = self.harmony_extension_extra_data

        if self.harmony_extension_push is not None:
            result['HarmonyExtensionPush'] = self.harmony_extension_push

        if self.harmony_image_url is not None:
            result['HarmonyImageUrl'] = self.harmony_image_url

        if self.harmony_inbox_content is not None:
            result['HarmonyInboxContent'] = self.harmony_inbox_content

        if self.harmony_live_view_payload is not None:
            result['HarmonyLiveViewPayload'] = self.harmony_live_view_payload

        if self.harmony_notification_slot_type is not None:
            result['HarmonyNotificationSlotType'] = self.harmony_notification_slot_type

        if self.harmony_notify_id is not None:
            result['HarmonyNotifyId'] = self.harmony_notify_id

        if self.harmony_receipt_id is not None:
            result['HarmonyReceiptId'] = self.harmony_receipt_id

        if self.harmony_remind is not None:
            result['HarmonyRemind'] = self.harmony_remind

        if self.harmony_remind_body is not None:
            result['HarmonyRemindBody'] = self.harmony_remind_body

        if self.harmony_remind_title is not None:
            result['HarmonyRemindTitle'] = self.harmony_remind_title

        if self.harmony_render_style is not None:
            result['HarmonyRenderStyle'] = self.harmony_render_style

        if self.harmony_test_message is not None:
            result['HarmonyTestMessage'] = self.harmony_test_message

        if self.harmony_uri is not None:
            result['HarmonyUri'] = self.harmony_uri

        if self.job_key is not None:
            result['JobKey'] = self.job_key

        if self.push_time is not None:
            result['PushTime'] = self.push_time

        if self.push_type is not None:
            result['PushType'] = self.push_type

        if self.send_channels is not None:
            result['SendChannels'] = self.send_channels

        if self.send_speed is not None:
            result['SendSpeed'] = self.send_speed

        if self.store_offline is not None:
            result['StoreOffline'] = self.store_offline

        if self.target is not None:
            result['Target'] = self.target

        if self.target_value is not None:
            result['TargetValue'] = self.target_value

        if self.title is not None:
            result['Title'] = self.title

        if self.trim is not None:
            result['Trim'] = self.trim

        if self.i_osapns_env is not None:
            result['iOSApnsEnv'] = self.i_osapns_env

        if self.i_osbadge is not None:
            result['iOSBadge'] = self.i_osbadge

        if self.i_osbadge_auto_increment is not None:
            result['iOSBadgeAutoIncrement'] = self.i_osbadge_auto_increment

        if self.i_osext_parameters is not None:
            result['iOSExtParameters'] = self.i_osext_parameters

        if self.i_osinterruption_level is not None:
            result['iOSInterruptionLevel'] = self.i_osinterruption_level

        if self.i_oslive_activity_attributes is not None:
            result['iOSLiveActivityAttributes'] = self.i_oslive_activity_attributes

        if self.i_oslive_activity_attributes_type is not None:
            result['iOSLiveActivityAttributesType'] = self.i_oslive_activity_attributes_type

        if self.i_oslive_activity_content_state is not None:
            result['iOSLiveActivityContentState'] = self.i_oslive_activity_content_state

        if self.i_oslive_activity_dismissal_date is not None:
            result['iOSLiveActivityDismissalDate'] = self.i_oslive_activity_dismissal_date

        if self.i_oslive_activity_event is not None:
            result['iOSLiveActivityEvent'] = self.i_oslive_activity_event

        if self.i_oslive_activity_id is not None:
            result['iOSLiveActivityId'] = self.i_oslive_activity_id

        if self.i_oslive_activity_stale_date is not None:
            result['iOSLiveActivityStaleDate'] = self.i_oslive_activity_stale_date

        if self.i_osmusic is not None:
            result['iOSMusic'] = self.i_osmusic

        if self.i_osmutable_content is not None:
            result['iOSMutableContent'] = self.i_osmutable_content

        if self.i_osnotification_category is not None:
            result['iOSNotificationCategory'] = self.i_osnotification_category

        if self.i_osnotification_collapse_id is not None:
            result['iOSNotificationCollapseId'] = self.i_osnotification_collapse_id

        if self.i_osnotification_thread_id is not None:
            result['iOSNotificationThreadId'] = self.i_osnotification_thread_id

        if self.i_osrelevance_score is not None:
            result['iOSRelevanceScore'] = self.i_osrelevance_score

        if self.i_osremind is not None:
            result['iOSRemind'] = self.i_osremind

        if self.i_osremind_body is not None:
            result['iOSRemindBody'] = self.i_osremind_body

        if self.i_ossilent_notification is not None:
            result['iOSSilentNotification'] = self.i_ossilent_notification

        if self.i_ossubtitle is not None:
            result['iOSSubtitle'] = self.i_ossubtitle

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidActivity') is not None:
            self.android_activity = m.get('AndroidActivity')

        if m.get('AndroidBadgeAddNum') is not None:
            self.android_badge_add_num = m.get('AndroidBadgeAddNum')

        if m.get('AndroidBadgeClass') is not None:
            self.android_badge_class = m.get('AndroidBadgeClass')

        if m.get('AndroidBadgeSetNum') is not None:
            self.android_badge_set_num = m.get('AndroidBadgeSetNum')

        if m.get('AndroidBigBody') is not None:
            self.android_big_body = m.get('AndroidBigBody')

        if m.get('AndroidBigPictureUrl') is not None:
            self.android_big_picture_url = m.get('AndroidBigPictureUrl')

        if m.get('AndroidBigTitle') is not None:
            self.android_big_title = m.get('AndroidBigTitle')

        if m.get('AndroidExtParameters') is not None:
            self.android_ext_parameters = m.get('AndroidExtParameters')

        if m.get('AndroidHonorTargetUserType') is not None:
            self.android_honor_target_user_type = m.get('AndroidHonorTargetUserType')

        if m.get('AndroidHuaweiBusinessType') is not None:
            self.android_huawei_business_type = m.get('AndroidHuaweiBusinessType')

        if m.get('AndroidHuaweiLiveNotificationPayload') is not None:
            self.android_huawei_live_notification_payload = m.get('AndroidHuaweiLiveNotificationPayload')

        if m.get('AndroidHuaweiReceiptId') is not None:
            self.android_huawei_receipt_id = m.get('AndroidHuaweiReceiptId')

        if m.get('AndroidHuaweiTargetUserType') is not None:
            self.android_huawei_target_user_type = m.get('AndroidHuaweiTargetUserType')

        if m.get('AndroidImageUrl') is not None:
            self.android_image_url = m.get('AndroidImageUrl')

        if m.get('AndroidInboxBody') is not None:
            self.android_inbox_body = m.get('AndroidInboxBody')

        if m.get('AndroidMeizuNoticeMsgType') is not None:
            self.android_meizu_notice_msg_type = m.get('AndroidMeizuNoticeMsgType')

        if m.get('AndroidMessageHuaweiCategory') is not None:
            self.android_message_huawei_category = m.get('AndroidMessageHuaweiCategory')

        if m.get('AndroidMessageHuaweiUrgency') is not None:
            self.android_message_huawei_urgency = m.get('AndroidMessageHuaweiUrgency')

        if m.get('AndroidMessageOppoCategory') is not None:
            self.android_message_oppo_category = m.get('AndroidMessageOppoCategory')

        if m.get('AndroidMessageOppoNotifyLevel') is not None:
            self.android_message_oppo_notify_level = m.get('AndroidMessageOppoNotifyLevel')

        if m.get('AndroidMessageVivoCategory') is not None:
            self.android_message_vivo_category = m.get('AndroidMessageVivoCategory')

        if m.get('AndroidMusic') is not None:
            self.android_music = m.get('AndroidMusic')

        if m.get('AndroidNotificationBarPriority') is not None:
            self.android_notification_bar_priority = m.get('AndroidNotificationBarPriority')

        if m.get('AndroidNotificationBarType') is not None:
            self.android_notification_bar_type = m.get('AndroidNotificationBarType')

        if m.get('AndroidNotificationChannel') is not None:
            self.android_notification_channel = m.get('AndroidNotificationChannel')

        if m.get('AndroidNotificationGroup') is not None:
            self.android_notification_group = m.get('AndroidNotificationGroup')

        if m.get('AndroidNotificationHonorChannel') is not None:
            self.android_notification_honor_channel = m.get('AndroidNotificationHonorChannel')

        if m.get('AndroidNotificationHuaweiChannel') is not None:
            self.android_notification_huawei_channel = m.get('AndroidNotificationHuaweiChannel')

        if m.get('AndroidNotificationNotifyId') is not None:
            self.android_notification_notify_id = m.get('AndroidNotificationNotifyId')

        if m.get('AndroidNotificationThreadId') is not None:
            self.android_notification_thread_id = m.get('AndroidNotificationThreadId')

        if m.get('AndroidNotificationVivoChannel') is not None:
            self.android_notification_vivo_channel = m.get('AndroidNotificationVivoChannel')

        if m.get('AndroidNotificationXiaomiChannel') is not None:
            self.android_notification_xiaomi_channel = m.get('AndroidNotificationXiaomiChannel')

        if m.get('AndroidNotifyType') is not None:
            self.android_notify_type = m.get('AndroidNotifyType')

        if m.get('AndroidOpenType') is not None:
            self.android_open_type = m.get('AndroidOpenType')

        if m.get('AndroidOpenUrl') is not None:
            self.android_open_url = m.get('AndroidOpenUrl')

        if m.get('AndroidOppoDeleteIntentData') is not None:
            self.android_oppo_delete_intent_data = m.get('AndroidOppoDeleteIntentData')

        if m.get('AndroidOppoIntelligentIntent') is not None:
            self.android_oppo_intelligent_intent = m.get('AndroidOppoIntelligentIntent')

        if m.get('AndroidOppoIntentEnv') is not None:
            self.android_oppo_intent_env = m.get('AndroidOppoIntentEnv')

        if m.get('AndroidOppoPrivateContentParameters') is not None:
            self.android_oppo_private_content_parameters = m.get('AndroidOppoPrivateContentParameters')

        if m.get('AndroidOppoPrivateMsgTemplateId') is not None:
            self.android_oppo_private_msg_template_id = m.get('AndroidOppoPrivateMsgTemplateId')

        if m.get('AndroidOppoPrivateTitleParameters') is not None:
            self.android_oppo_private_title_parameters = m.get('AndroidOppoPrivateTitleParameters')

        if m.get('AndroidPopupActivity') is not None:
            self.android_popup_activity = m.get('AndroidPopupActivity')

        if m.get('AndroidPopupBody') is not None:
            self.android_popup_body = m.get('AndroidPopupBody')

        if m.get('AndroidPopupTitle') is not None:
            self.android_popup_title = m.get('AndroidPopupTitle')

        if m.get('AndroidRemind') is not None:
            self.android_remind = m.get('AndroidRemind')

        if m.get('AndroidRenderStyle') is not None:
            self.android_render_style = m.get('AndroidRenderStyle')

        if m.get('AndroidTargetUserType') is not None:
            self.android_target_user_type = m.get('AndroidTargetUserType')

        if m.get('AndroidVivoLiveMessage') is not None:
            self.android_vivo_live_message = m.get('AndroidVivoLiveMessage')

        if m.get('AndroidVivoPushMode') is not None:
            self.android_vivo_push_mode = m.get('AndroidVivoPushMode')

        if m.get('AndroidVivoReceiptId') is not None:
            self.android_vivo_receipt_id = m.get('AndroidVivoReceiptId')

        if m.get('AndroidXiaoMiActivity') is not None:
            self.android_xiao_mi_activity = m.get('AndroidXiaoMiActivity')

        if m.get('AndroidXiaoMiNotifyBody') is not None:
            self.android_xiao_mi_notify_body = m.get('AndroidXiaoMiNotifyBody')

        if m.get('AndroidXiaoMiNotifyTitle') is not None:
            self.android_xiao_mi_notify_title = m.get('AndroidXiaoMiNotifyTitle')

        if m.get('AndroidXiaomiBigPictureUrl') is not None:
            self.android_xiaomi_big_picture_url = m.get('AndroidXiaomiBigPictureUrl')

        if m.get('AndroidXiaomiFocusParam') is not None:
            self.android_xiaomi_focus_param = m.get('AndroidXiaomiFocusParam')

        if m.get('AndroidXiaomiFocusPics') is not None:
            self.android_xiaomi_focus_pics = m.get('AndroidXiaomiFocusPics')

        if m.get('AndroidXiaomiImageUrl') is not None:
            self.android_xiaomi_image_url = m.get('AndroidXiaomiImageUrl')

        if m.get('AndroidXiaomiTemplateId') is not None:
            self.android_xiaomi_template_id = m.get('AndroidXiaomiTemplateId')

        if m.get('AndroidXiaomiTemplateParams') is not None:
            self.android_xiaomi_template_params = m.get('AndroidXiaomiTemplateParams')

        if m.get('Body') is not None:
            self.body = m.get('Body')

        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('HarmonyAction') is not None:
            self.harmony_action = m.get('HarmonyAction')

        if m.get('HarmonyActionType') is not None:
            self.harmony_action_type = m.get('HarmonyActionType')

        if m.get('HarmonyBadgeAddNum') is not None:
            self.harmony_badge_add_num = m.get('HarmonyBadgeAddNum')

        if m.get('HarmonyBadgeSetNum') is not None:
            self.harmony_badge_set_num = m.get('HarmonyBadgeSetNum')

        if m.get('HarmonyCategory') is not None:
            self.harmony_category = m.get('HarmonyCategory')

        if m.get('HarmonyExtParameters') is not None:
            self.harmony_ext_parameters = m.get('HarmonyExtParameters')

        if m.get('HarmonyExtensionExtraData') is not None:
            self.harmony_extension_extra_data = m.get('HarmonyExtensionExtraData')

        if m.get('HarmonyExtensionPush') is not None:
            self.harmony_extension_push = m.get('HarmonyExtensionPush')

        if m.get('HarmonyImageUrl') is not None:
            self.harmony_image_url = m.get('HarmonyImageUrl')

        if m.get('HarmonyInboxContent') is not None:
            self.harmony_inbox_content = m.get('HarmonyInboxContent')

        if m.get('HarmonyLiveViewPayload') is not None:
            self.harmony_live_view_payload = m.get('HarmonyLiveViewPayload')

        if m.get('HarmonyNotificationSlotType') is not None:
            self.harmony_notification_slot_type = m.get('HarmonyNotificationSlotType')

        if m.get('HarmonyNotifyId') is not None:
            self.harmony_notify_id = m.get('HarmonyNotifyId')

        if m.get('HarmonyReceiptId') is not None:
            self.harmony_receipt_id = m.get('HarmonyReceiptId')

        if m.get('HarmonyRemind') is not None:
            self.harmony_remind = m.get('HarmonyRemind')

        if m.get('HarmonyRemindBody') is not None:
            self.harmony_remind_body = m.get('HarmonyRemindBody')

        if m.get('HarmonyRemindTitle') is not None:
            self.harmony_remind_title = m.get('HarmonyRemindTitle')

        if m.get('HarmonyRenderStyle') is not None:
            self.harmony_render_style = m.get('HarmonyRenderStyle')

        if m.get('HarmonyTestMessage') is not None:
            self.harmony_test_message = m.get('HarmonyTestMessage')

        if m.get('HarmonyUri') is not None:
            self.harmony_uri = m.get('HarmonyUri')

        if m.get('JobKey') is not None:
            self.job_key = m.get('JobKey')

        if m.get('PushTime') is not None:
            self.push_time = m.get('PushTime')

        if m.get('PushType') is not None:
            self.push_type = m.get('PushType')

        if m.get('SendChannels') is not None:
            self.send_channels = m.get('SendChannels')

        if m.get('SendSpeed') is not None:
            self.send_speed = m.get('SendSpeed')

        if m.get('StoreOffline') is not None:
            self.store_offline = m.get('StoreOffline')

        if m.get('Target') is not None:
            self.target = m.get('Target')

        if m.get('TargetValue') is not None:
            self.target_value = m.get('TargetValue')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('Trim') is not None:
            self.trim = m.get('Trim')

        if m.get('iOSApnsEnv') is not None:
            self.i_osapns_env = m.get('iOSApnsEnv')

        if m.get('iOSBadge') is not None:
            self.i_osbadge = m.get('iOSBadge')

        if m.get('iOSBadgeAutoIncrement') is not None:
            self.i_osbadge_auto_increment = m.get('iOSBadgeAutoIncrement')

        if m.get('iOSExtParameters') is not None:
            self.i_osext_parameters = m.get('iOSExtParameters')

        if m.get('iOSInterruptionLevel') is not None:
            self.i_osinterruption_level = m.get('iOSInterruptionLevel')

        if m.get('iOSLiveActivityAttributes') is not None:
            self.i_oslive_activity_attributes = m.get('iOSLiveActivityAttributes')

        if m.get('iOSLiveActivityAttributesType') is not None:
            self.i_oslive_activity_attributes_type = m.get('iOSLiveActivityAttributesType')

        if m.get('iOSLiveActivityContentState') is not None:
            self.i_oslive_activity_content_state = m.get('iOSLiveActivityContentState')

        if m.get('iOSLiveActivityDismissalDate') is not None:
            self.i_oslive_activity_dismissal_date = m.get('iOSLiveActivityDismissalDate')

        if m.get('iOSLiveActivityEvent') is not None:
            self.i_oslive_activity_event = m.get('iOSLiveActivityEvent')

        if m.get('iOSLiveActivityId') is not None:
            self.i_oslive_activity_id = m.get('iOSLiveActivityId')

        if m.get('iOSLiveActivityStaleDate') is not None:
            self.i_oslive_activity_stale_date = m.get('iOSLiveActivityStaleDate')

        if m.get('iOSMusic') is not None:
            self.i_osmusic = m.get('iOSMusic')

        if m.get('iOSMutableContent') is not None:
            self.i_osmutable_content = m.get('iOSMutableContent')

        if m.get('iOSNotificationCategory') is not None:
            self.i_osnotification_category = m.get('iOSNotificationCategory')

        if m.get('iOSNotificationCollapseId') is not None:
            self.i_osnotification_collapse_id = m.get('iOSNotificationCollapseId')

        if m.get('iOSNotificationThreadId') is not None:
            self.i_osnotification_thread_id = m.get('iOSNotificationThreadId')

        if m.get('iOSRelevanceScore') is not None:
            self.i_osrelevance_score = m.get('iOSRelevanceScore')

        if m.get('iOSRemind') is not None:
            self.i_osremind = m.get('iOSRemind')

        if m.get('iOSRemindBody') is not None:
            self.i_osremind_body = m.get('iOSRemindBody')

        if m.get('iOSSilentNotification') is not None:
            self.i_ossilent_notification = m.get('iOSSilentNotification')

        if m.get('iOSSubtitle') is not None:
            self.i_ossubtitle = m.get('iOSSubtitle')

        return self

