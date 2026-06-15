# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class PushRequest(DaraModel):
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
        android_render_style: int = None,
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
        app_key: int = None,
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
        idempotent_token: str = None,
        job_key: str = None,
        push_time: str = None,
        push_type: str = None,
        send_channels: str = None,
        send_speed: int = None,
        sms_delay_secs: int = None,
        sms_params: str = None,
        sms_send_policy: int = None,
        sms_sign_name: str = None,
        sms_template_name: str = None,
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
        # This is required only when \\`AndroidOpenType\\` is \\`Activity\\`. For example: \\`com.alibaba.cloudpushdemo.bizactivity\\`.
        self.android_activity = android_activity
        # Sets the value to add to the badge number. This value is added to the original badge number. The value must be between 1 and 99.
        # 
        # > This is effective only for pushes through Huawei/Honor vendor channels. If both \\`AndroidBadgeAddNum\\` and \\`AndroidBadgeSetNum\\` are present, \\`AndroidBadgeSetNum\\` takes precedence.
        self.android_badge_add_num = android_badge_add_num
        # The fully qualified class name of the app\\"s entry Activity for badge setting.
        # 
        # > This is effective only for pushes through Huawei/Honor vendor channels.
        self.android_badge_class = android_badge_class
        # Sets a fixed number for the badge. The value must be between 0 and 99.
        # 
        # > For vendor channel pushes, this is effective only for Huawei and Honor channels. For pushes through Alibaba Cloud\\"s proprietary channel, this is effective only on Huawei, Honor, and vivo models.
        self.android_badge_set_num = android_badge_set_num
        # The body in long text mode. Length limit: 1,000 bytes (1 Chinese character is counted as 3 bytes). The actual limit depends on the specific vendor channel.
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
        # - Proprietary channel: Android SDK 3.6.0 and later
        # 
        # > If this parameter is not provided in long text mode, the system uses the first non-empty value from \\`Body\\` or \\`AndroidPopupBody\\`.
        self.android_big_body = android_big_body
        # The image URL for big picture mode. Currently supported by the proprietary channel on Android SDK 3.6.0 and later.
        self.android_big_picture_url = android_big_picture_url
        # The title in long text mode. Length limit: 200 bytes (1 Chinese character is counted as 3 bytes).
        # 
        # - Currently, this is only supported by Honor channels and Huawei channels on EMUI 11 and later.
        # 
        # - If this parameter is not provided in long text mode, the system uses the first non-empty value from \\`Title\\` or \\`AndroidPopupTitle\\`.
        self.android_big_title = android_big_title
        # Sets the extended properties of the notification. This property is not effective when \\`PushType\\` is \\`MESSAGE\\`.
        # 
        # This parameter must be in JSON map format to avoid parsing errors.
        self.android_ext_parameters = android_ext_parameters
        # Sets the Honor channel notification type:
        # 
        # - **0**: Formal notification (default).
        # 
        # - **1**: Test notification.
        # 
        # > Each app can send 1,000 test notifications per day. These are not subject to the daily push limit per device.
        self.android_honor_target_user_type = android_honor_target_user_type
        # Sets the Huawei quick notification parameter.
        # 
        # - **0**: Send a standard Huawei notification (default).
        # 
        # - **1**: Send a Huawei quick notification.
        self.android_huawei_business_type = android_huawei_business_type
        # A JSON string of the Huawei Android Live Notification data structure [LiveNotificationPayload](https://developer.huawei.com/consumer/cn/doc/HMSCore-References/rest-live-0000001562939968#ZH-CN_TOPIC_0000001700850537__p195121620102511). For development and integration, see [Huawei Live Notification Push Guide](https://help.aliyun.com/document_detail/2983768.html).
        self.android_huawei_live_notification_payload = android_huawei_live_notification_payload
        # The receipt ID for the Huawei channel. You can find this ID in the receipt parameter configuration on the Huawei Push service platform.
        # 
        # > If the default receipt configuration on the Huawei Push service platform is the Alibaba Cloud receipt, do not provide this. If not, first configure the default Huawei channel receipt ID in the Alibaba Cloud EMAS Mobile Push console.
        self.android_huawei_receipt_id = android_huawei_receipt_id
        # Sets the Huawei channel notification type:
        # 
        # - **0**: Formal notification (default).
        # 
        # - **1**: Test notification.
        # 
        # > Each app can send 500 test notifications per day. These are not subject to the daily push limit per device.
        self.android_huawei_target_user_type = android_huawei_target_user_type
        # The URL for the right-side icon.
        # Currently supported on:
        # 
        # - Huawei EMUI (only in long text and inbox modes).
        # 
        # - Honor Magic UI (only in long text mode).
        # 
        # - Proprietary channel: Android SDK 3.5.0 and later.
        self.android_image_url = android_image_url
        # The body content for inbox mode. The content must be a valid JSON array with no more than 5 elements. Currently supported on:
        # 
        # - Huawei: EMUI 9 and later
        # 
        # - Honor: Magic UI 4.0 and later
        # 
        # - Xiaomi: MIUI 10 and later
        # 
        # - OPPO: ColorOS 5.0 and later
        # 
        # - Proprietary channel: Android SDK 3.6.0 and later
        self.android_inbox_body = android_inbox_body
        # Meizu message type
        # 
        # - 0 Public message (default)
        # 
        # - 1 Private message
        self.android_meizu_notice_msg_type = android_meizu_notice_msg_type
        # Function 1: After applying for [self-classification rights](https://developer.huawei.com/consumer/cn/doc/development/HMSCore-Guides/message-classification-0000001149358835?#section3410731125514), this is used to identify the message type and determine the [message alert method](https://developer.huawei.com/consumer/cn/doc/development/HMSCore-Guides/message-classification-0000001149358835#ZH-CN_TOPIC_0000001149358835__p3850133955718). It accelerates the sending of specific message types. For valid values, refer to the [message classification standards](https://developer.huawei.com/consumer/cn/doc/development/HMSCore-Guides/message-classification-0000001149358835#section1076611477914) in the official Huawei Push documentation. Fill in the \\"Cloud notification category value\\" or \\"Local notification category value\\" from the document\\"s table.
        # 
        # Function 2: After applying for [special permissions](https://developer.huawei.com/consumer/cn/doc/development/HMSCore-Guides/faq-0000001050042183#section037425218509), this is used to identify high-priority pass-through scenarios. Valid values:
        # 
        # - VOIP: Voice and video calls
        # 
        # - PLAY_VOICE: Voice playback
        # 
        # > If the \\"Cloud notification category value\\" is \\"Not applicable\\", the push is sent through Alibaba Cloud\\"s proprietary channel. If the \\"Local notification category value\\" is \\"Not applicable\\", the push is sent through the Huawei channel.
        self.android_message_huawei_category = android_message_huawei_category
        # The delivery priority for notifications on the Huawei channel. Valid values:
        # 
        # - **HIGH**
        # 
        # - **NORMAL**
        # 
        # Apply for permission. For more information, see [Application link](https://developer.huawei.com/consumer/cn/doc/development/HMSCore-Guides/faq-0000001050042183#section037425218509).
        self.android_message_huawei_urgency = android_message_huawei_urgency
        # OPPO classifies and manages messages in two categories: Communication & Service, and Content & Marketing.
        # 
        # Communication & Service (requires permission):
        # 
        # - IM: Instant messaging, audio, and video calls
        # 
        # - ACCOUNT: Personal account and asset changes
        # 
        # - DEVICE_REMINDER: Personal device reminders
        # 
        # - ORDER: Personal order/logistics status changes
        # 
        # - TODO: Personal schedule/to-do items
        # 
        # - SUBSCRIPTION: Personal subscriptions
        # 
        # Content & Marketing:
        # 
        # - NEWS: News and information
        # 
        # - CONTENT: Content recommendations
        # 
        # - MARKETING: Platform activities
        # 
        # - SOCIAL: Social updates
        # 
        # For more information, see [OPUSH Message Classification Rules](https://open.oppomobile.com/new/developmentDoc/info?id=13189).
        self.android_message_oppo_category = android_message_oppo_category
        # The alert level for notification bar messages on the OPPO channel. Valid values:
        # 
        # - 1: Notification bar
        # 
        # - 2: Notification bar, lock screen, ringtone, vibration (default level for Communication & Service messages)
        # 
        # - 16: Notification bar, lock screen, ringtone, vibration, banner (requires permission)
        # 
        # > When using the \\`AndroidMessageOppoNotifyLevel\\` parameter, you must also pass the \\`AndroidMessageOppoCategory\\` parameter.
        self.android_message_oppo_notify_level = android_message_oppo_notify_level
        # vivo classifies and manages messages in two categories: System messages and Operational messages.
        # System messages:
        # 
        # - IM: Instant messages
        # 
        # - ACCOUNT: Account and assets
        # 
        # - TODO: Schedule and to-do
        # 
        # - DEVICE_REMINDER: Device information
        # 
        # - ORDER: Orders and logistics
        # 
        # - SUBSCRIPTION: Subscription reminders
        # 
        # Operational messages:
        # 
        # - NEWS: News
        # 
        # - CONTENT: Content recommendations
        # 
        # - MARKETING: Operational activities
        # 
        # - SOCIAL: Social updates
        # 
        # For more information, see [Classification description](https://dev.vivo.com.cn/documentCenter/doc/359#s-ef3qugc3).
        self.android_message_vivo_category = android_message_vivo_category
        # The notification sound for the Huawei vendor channel. Specify the name of the audio file located in the \\`app/src/main/res/raw/\\` directory of the client project. Do not include the file format suffix.
        # 
        # If this is not set, the default ringtone is used.
        self.android_music = android_music
        # The priority for arranging the Android notification in the notification bar. Valid values: -2, -1, 0, 1, 2.
        self.android_notification_bar_priority = android_notification_bar_priority
        # The custom Android notification bar style. Valid values: 1 to 100.
        self.android_notification_bar_type = android_notification_bar_type
        # The \\`channelId\\` for the Android app. This must correspond to a \\`channelId\\` in the app.
        # 
        # - Set the \\`NotificationChannel\\` parameter. For more information about its usage, see [FAQ: Why are notifications not received on devices running Android 8.0 or later?](https://help.aliyun.com/document_detail/67398.html).
        # 
        # - Because the \\`channel_id\\` for the OPPO private message channel is the same as the app\\"s \\`channelId\\`, this value is used for pushes through the OPPO channel.
        # 
        # - This value is used for pushes through Huawei, FCM, and Alibaba Cloud\\"s proprietary channels.
        self.android_notification_channel = android_notification_channel
        # Message grouping. For messages in the same group, the notification bar shows only the latest message and the total number of messages received for that group. It does not display all messages and cannot be expanded. Currently supported on:
        # 
        # - Huawei vendor channel
        # 
        # - Honor vendor channel
        # 
        # - Proprietary channel for Android SDK 3.9.1 and earlier
        # 
        # > This parameter is no longer supported by the proprietary channel for Android SDK 3.9.2 and later.
        self.android_notification_group = android_notification_group
        # Sets the \\`importance\\` parameter for Honor notification message classification. This determines the notification behavior on the user\\"s device. Valid values:
        # 
        # - **LOW**: For informational and marketing messages.
        # 
        # - **NORMAL**: For service and communication messages.
        # 
        # Apply for this on the Honor platform. [Application link](https://developer.honor.com/cn/docs/11002/guides/notification-class#%E8%87%AA%E5%88%86%E7%B1%BB%E6%9D%83%E7%9B%8A%E7%94%B3%E8%AF%B7).
        self.android_notification_honor_channel = android_notification_honor_channel
        # Sets the \\`importance\\` parameter for Huawei notification message classification. This determines the notification behavior on the user\\"s device. Valid values:
        # 
        # - LOW: For informational and marketing messages.
        # 
        # - NORMAL: For service and communication messages.
        # 
        # > * For the Huawei channel, use \\`AndroidMessageHuaweiCategory\\` for notification classification. You may no longer need to use \\`AndroidNotificationHuaweiChannel\\`.
        # >
        # > * Apply for this on the Huawei platform. [Application link](https://developer.huawei.com/consumer/cn/doc/development/HMSCore-Guides/message-classification-0000001149358835#section893184112272).
        self.android_notification_huawei_channel = android_notification_huawei_channel
        # A unique identifier for each message when it is displayed as a notification. Different notifications can have the same \\`NotifyId\\`, which allows a new notification to overwrite an old one.
        self.android_notification_notify_id = android_notification_notify_id
        # Message grouping. Messages in the same group are displayed in a collapsed state in the notification bar and can be expanded. Notifications from different groups are displayed separately. Currently supported on:
        # 
        # - Proprietary channel for Android SDK 3.9.2 and later
        self.android_notification_thread_id = android_notification_thread_id
        # Sets the classification for vivo notification messages. Valid values:
        # 
        # - 0: Operational messages (default)
        # 
        # - 1: System messages
        # 
        # > * For the vivo channel, use \\`AndroidMessageVivoCategory\\` for notification classification. You may no longer need to use \\`AndroidNotificationVivoChannel\\`.
        # >
        # > * Apply for this on the vivo platform. For more information, see [Application link](https://dev.vivo.com.cn/documentCenter/doc/359).
        self.android_notification_vivo_channel = android_notification_vivo_channel
        # Sets the \\`channelId\\` for the Xiaomi notification type. Apply for this on the Xiaomi platform. For more information, see [Application link](https://dev.mi.com/console/doc/detail?pId=2422#_4).
        # 
        # > - A single app can apply for a maximum of 8 channels through the Xiaomi channel. Plan accordingly.
        self.android_notification_xiaomi_channel = android_notification_xiaomi_channel
        # The notification alert type. Valid values:
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
        # - **APPLICATION**: Open the application (default).
        # 
        # - **ACTIVITY**: Open a specific Android Activity.
        # 
        # - **URL**: Open a URL.
        # 
        # - **NONE**: No action.
        self.android_open_type = android_open_type
        # The URL to open after the Android device receives the push.
        # 
        # This is required only when \\`AndroidOpenType\\` is \\`URL\\`.
        self.android_open_url = android_open_url
        # A JSON string of the OPPO Fluid Cloud intent deletion data structure [data](https://open.oppomobile.com/documentation/page/info?id=13578). This parameter is invalid if the \\`AndroidOppoIntelligentIntent\\` parameter is filled. For development and integration, see [OPPO Fluid Cloud Push Guide](https://help.aliyun.com/document_detail/2997310.html).
        self.android_oppo_delete_intent_data = android_oppo_delete_intent_data
        # A JSON string of the OPPO Fluid Cloud intent sharing data structure [IntelligentIntent](https://open.oppomobile.com/documentation/page/info?id=13565). For development and integration, see [OPPO Fluid Cloud Push Guide](https://help.aliyun.com/document_detail/2997310.html).
        self.android_oppo_intelligent_intent = android_oppo_intelligent_intent
        # Sets the OPPO Fluid Cloud push environment.
        # 
        # - **0**: Production environment (default).
        # 
        # - **1**: Staging environment.
        # 
        # > The OPPO Fluid Cloud staging environment must be set up on the client side. For more information, see [Environment setup](https://open.oppomobile.com/documentation/page/info?id=13590).
        self.android_oppo_intent_env = android_oppo_intent_env
        # OPPO private message template content parameters
        self.android_oppo_private_content_parameters = android_oppo_private_content_parameters
        # OPPO private message template ID
        self.android_oppo_private_msg_template_id = android_oppo_private_msg_template_id
        # OPPO private message template title parameters
        self.android_oppo_private_title_parameters = android_oppo_private_title_parameters
        # Specifies the Activity to launch after the notification is tapped.
        self.android_popup_activity = android_popup_activity
        # The body content in auxiliary pop-up mode. This parameter is required if \\`AndroidPopupActivity\\` is not empty.
        # 
        # Length limit: 200 characters. Both Chinese and English characters count as one.
        # 
        # If you use a vendor channel, comply with its restrictions. For more information, see [Limits on pushes through auxiliary channels on Android](https://help.aliyun.com/document_detail/165253.html).
        self.android_popup_body = android_popup_body
        # The title content in auxiliary pop-up mode. This parameter is required if \\`AndroidPopupActivity\\` is not empty.
        # 
        # Length limit: 50 characters. Both Chinese and English characters count as one.
        # 
        # If you use a vendor channel, comply with its restrictions. For more information, see [Limits on pushes through auxiliary channels on Android](https://help.aliyun.com/document_detail/165253.html).
        self.android_popup_title = android_popup_title
        # If the device is offline when a message is pushed, this push uses the auxiliary pop-up feature. The default value is \\`false\\`. This is effective only when \\`PushType\\` is \\`MESSAGE\\`.
        # 
        # If the message is successfully converted to a notification, the data displayed in the notification is the value of the \\`AndroidPopupTitle\\` and \\`AndroidPopupBody\\` parameters set on the server. When the notification is tapped, the data obtained in the \\`onSysNoticeOpened\\` method of the auxiliary pop-up is the value of the \\`Title\\` and \\`Body\\` parameters set on the server.
        self.android_remind = android_remind
        # The notification style. Valid values:
        # 
        # - **0**: Standard mode (default)
        # 
        # - **1**: Long text mode (supported by Huawei, Honor, Xiaomi, OPPO, Meizu, and proprietary channels)
        # 
        # - **2**: Big picture mode (supported by proprietary channels, but not by Xiaomi models)
        # 
        # - **3**: List mode (supported by Huawei, Honor, Xiaomi, OPPO, and proprietary channels)
        # 
        # > This parameter is required if you use a non-standard mode.
        self.android_render_style = android_render_style
        # Sets the vendor channel notification type:
        # 
        # - **0**: Formal notification (default).
        # 
        # - **1**: Test notification.
        # 
        # > * Configuring this parameter is equivalent to configuring \\`AndroidHuaweiTargetUserType\\`, \\`AndroidHonorTargetUserType\\`, \\`AndroidVivoPushMode\\`, and \\`AndroidOppoIntentEnv\\` simultaneously. Specific vendor channel parameters can override this setting.
        # >
        # > * Currently supported by: Huawei channel, Honor channel, vivo channel, and OPPO Fluid Cloud.
        self.android_target_user_type = android_target_user_type
        # A JSON string of the vivo Atomic Island data structure [liveMessage](https://dev.vivo.com.cn/documentCenter/doc/896#s-fdagzbd4). For development and integration, see [vivo Atomic Island Push Guide](https://help.aliyun.com/zh/document_detail/3030718.html).
        self.android_vivo_live_message = android_vivo_live_message
        # Sets the vivo channel notification type:
        # 
        # - **0**: Formal push (default).
        # 
        # - **1**: Test push.
        # 
        # > For test pushes, configure test devices in the vivo console beforehand. Find the test device\\"s \\`RegId\\` by searching for "onReceiveRegId regId" in the device startup logs.
        self.android_vivo_push_mode = android_vivo_push_mode
        # The receipt ID for the vivo channel. You can find this ID in the application information section of the vivo open platform\\"s push service.
        # 
        # > If the default receipt configuration on the vivo open platform is the Alibaba Cloud receipt, do not provide this. If not, first configure the default vivo channel receipt ID in the Alibaba Cloud EMAS Mobile Push console.
        self.android_vivo_receipt_id = android_vivo_receipt_id
        # This parameter is deprecated. All third-party auxiliary pop-ups are now supported by the new parameter **AndroidPopupActivity**.
        self.android_xiao_mi_activity = android_xiao_mi_activity
        # This parameter is deprecated. All third-party auxiliary pop-ups are now supported by the new parameter **AndroidPopupBody**.
        self.android_xiao_mi_notify_body = android_xiao_mi_notify_body
        # This parameter is deprecated. All third-party auxiliary pop-ups are now supported by the new parameter **AndroidPopupTitle**.
        self.android_xiao_mi_notify_title = android_xiao_mi_notify_title
        # This parameter is deprecated. Starting from August 2023, Xiaomi no longer supports dynamically setting small icons, right-side icons, or large pictures during pushes on new devices/systems.
        self.android_xiaomi_big_picture_url = android_xiaomi_big_picture_url
        # A JSON string of the Xiaomi Super Island data structure [miui.focus.param](https://dev.mi.com/xiaomihyperos/documentation/detail?pId=2131). For development and integration, see [Xiaomi Super Island Push Guide](https://help.aliyun.com/zh/document_detail/3037956.html).
        self.android_xiaomi_focus_param = android_xiaomi_focus_param
        # A JSON string of the Xiaomi Super Island data images [miui.focus.pic_xxx](https://dev.mi.com/xiaomihyperos/documentation/detail?pId=2131). For development and integration, see [Xiaomi Super Island Push Guide](https://help.aliyun.com/zh/document_detail/3037956.html).
        self.android_xiaomi_focus_pics = android_xiaomi_focus_pics
        # This parameter is deprecated. Starting from August 2023, Xiaomi no longer supports dynamically setting small icons, right-side icons, or large pictures during pushes on new devices/systems.
        self.android_xiaomi_image_url = android_xiaomi_image_url
        self.android_xiaomi_template_id = android_xiaomi_template_id
        self.android_xiaomi_template_params = android_xiaomi_template_params
        # The AppKey.
        # 
        # This parameter is required.
        self.app_key = app_key
        # The content of the notification or message for Android and HarmonyOS pushes. The content of the message or notification for iOS. The size of the push content is limited. For more information, see [Product limits](https://help.aliyun.com/document_detail/434629.html).
        self.body = body
        # The device type. Valid values:
        # 
        # - **HARMONY**: A HarmonyOS device.
        # 
        # - **iOS**: An iOS device.
        # 
        # - **ANDROID**: An Android device.
        # 
        # - **ALL**: For older dual-platform apps, this sends pushes to both Android and iOS devices. For newer single-platform apps, this has the same effect as specifying the device type for that app.
        # 
        # This parameter is required.
        self.device_type = device_type
        # The expiration time for offline messages or notifications. Use this with \\`StoreOffline\\`. The message is not sent after this time. The maximum retention period is 72 hours, which is also the default.
        # 
        # The time must be in ISO 8601 format and in UTC: \\`YYYY-MM-DDThh:mm:ssZ\\`. The expiration time must be at least 3 seconds after the current time or the scheduled push time (\\`ExpireTime\\` > \\`PushTime\\` + 3 seconds). The 3-second buffer accounts for network and system delays. For single pushes, use a value of at least 1 minute. For batch pushes or pushes to all devices, use a value of at least 10 minutes.
        self.expire_time = expire_time
        # The action corresponding to the in-app page ability.
        # 
        # >Notice: 
        # 
        # When \\`HarmonyActionType\\` is \\`APP_CUSTOM_PAGE\\`, fill in at least one of \\`HarmonyUri\\` or \\`HarmonyAction\\`.
        # 
        # 
        # 
        # For more information, see [ClickAction.action](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/push-scenariozed-api-request-param-V5#section152462191216) in the HarmonyOS documentation.
        self.harmony_action = harmony_action
        # The action to take after a notification is tapped. Valid values:
        # 
        # - APP_HOME_PAGE: Open the app\\"s home page.
        # 
        # - APP_CUSTOM_PAGE: Open a custom page in the app.
        self.harmony_action_type = harmony_action_type
        # The number to add to the HarmonyOS app badge. See the description of the [HarmonyOS badge addNum field](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/push-scenariozed-api-request-param-V5#section266310382145).<br>
        # Supported starting from HarmonyOS SDK version 1.2.0.<br>
        self.harmony_badge_add_num = harmony_badge_add_num
        # The number to set for the HarmonyOS app badge. See the description of the [HarmonyOS badge setNum field](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/push-scenariozed-api-request-param-V5#section266310382145).
        # Supported starting from HarmonyOS SDK version 1.2.0.
        self.harmony_badge_set_num = harmony_badge_set_num
        # The notification message category. After you apply for notification message self-classification rights, this is used to identify the message type. Different notification message types affect how messages are displayed and alerted. Valid values:
        # 
        # - IM: Instant messaging
        # 
        # - VOIP: Voice and video calls
        # 
        # - SUBSCRIPTION: Subscriptions
        # 
        # - TRAVEL: Travel
        # 
        # - HEALTH: Health
        # 
        # - WORK: Work reminders
        # 
        # - ACCOUNT: Account updates
        # 
        # - EXPRESS: Orders & logistics
        # 
        # - FINANCE: Finance
        # 
        # - DEVICE_REMINDER: Device reminders
        # 
        # - MAIL: Mail
        # 
        # - CUSTOMER_SERVICE: Customer service messages
        # 
        # - MARKETING: News, content recommendations, social updates, product promotions, financial updates, lifestyle information, surveys, feature recommendations, and operational activities. This only identifies the content and does not speed up message delivery. These are collectively known as informational and marketing messages.
        # 
        # For more information, see [Notification.category](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/push-scenariozed-api-request-param-V5#section17371529101117) in the HarmonyOS documentation.
        self.harmony_category = harmony_category
        # Sets the extended properties of the notification. This property is not effective when \\`PushType\\` is \\`MESSAGE\\`.
        # 
        # This parameter must be in JSON map format to avoid parsing errors.
        self.harmony_ext_parameters = harmony_ext_parameters
        # The extra data for the extended notification message.<br>
        # This is effective when sending a HarmonyOS extended notification message.<br>
        # Conceptually, this is equivalent to the \\`extraData\\` field of a HarmonyOS extended notification message. For the specific definition, see [HarmonyOS ExtensionPayload Description](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/push-scenariozed-api-request-param-V5#section161192514234).<br>
        # Supported starting from HarmonyOS SDK version 1.2.0.<br><br><br>
        self.harmony_extension_extra_data = harmony_extension_extra_data
        # When \\`PushType\\` is \\`NOTICE\\`, specifies whether this is a HarmonyOS extended notification message.
        # 
        # - true: Send an extended notification message.
        # 
        # - false: Send a normal notification (default).
        # 
        # Apply for permission on the HarmonyOS side before you can send extended notification messages. For more information, see [Send Extended Notification Messages](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V5/push-send-extend-noti-V5) in the HarmonyOS documentation.<br>
        # Supported starting from HarmonyOS SDK version 1.2.0.<br>
        self.harmony_extension_push = harmony_extension_push
        # The URL for the large icon on the right of the notification. The URL must use the HTTPS protocol.
        # 
        # > Supported image formats are PNG, JPG, JPEG, HEIF, GIF, and BMP. The image dimensions (height × width) must be less than 25,000 pixels.
        # 
        # For more information, see [Notification.image](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/push-scenariozed-api-request-param-V5#section17371529101117) in the HarmonyOS documentation.
        self.harmony_image_url = harmony_image_url
        # The content for the multi-line text style. This field is required when \\`HarmonyRenderStyle\\` is \\`MULTI_LINE\\`. It supports up to 3 lines of content.
        self.harmony_inbox_content = harmony_inbox_content
        # A JSON string of the HarmonyOS Live Window data structure [LiveViewPayload](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V13/push-scenariozed-api-request-param-V13#section66881469306). For development and integration, see [HarmonyOS Live Window Push Guide](https://help.aliyun.com/document_detail/2982112.html).
        self.harmony_live_view_payload = harmony_live_view_payload
        # Uses the specified type of notification channel. This is effective only when the Alibaba Cloud proprietary channel is online.
        # 
        # - SOCIAL_COMMUNICATION: Social communication.
        # 
        # - SERVICE_INFORMATION: Service reminders.
        # 
        # - CONTENT_INFORMATION: Content information.
        # 
        # - CUSTOMER_SERVICE: Customer service messages. This type is for messages between users and businesses and must be initiated by the user.
        # 
        # - OTHER_TYPES: Others.
        # 
        # For more information, see [SlotType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/js-apis-notificationmanager-V5#slottype) in the HarmonyOS documentation.
        self.harmony_notification_slot_type = harmony_notification_slot_type
        # A unique identifier for each message when it is displayed as a notification. If not provided, the push service automatically generates a unique ID for each message. Different notifications can have the same \\`notifyId\\`, which allows a new message to overwrite an old one.
        # 
        # For more information, see [Notification.notifyId](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/push-scenariozed-api-request-param-V5#section17371529101117) in the HarmonyOS documentation.
        self.harmony_notify_id = harmony_notify_id
        # The receipt ID for the HarmonyOS channel. You can find this ID in the receipt parameter configuration on the HarmonyOS Push service platform.
        # 
        # > If the default receipt configuration on the HarmonyOS Push service platform is the Alibaba Cloud receipt, do not provide this. If not, first configure the default HarmonyOS channel receipt ID in the Alibaba Cloud EMAS Mobile Push console.
        # 
        # For more information, see [pushOptions.receiptId](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/push-scenariozed-api-request-param-V5#section418321011212) in the HarmonyOS documentation.
        self.harmony_receipt_id = harmony_receipt_id
        # If the device is offline when a message is pushed, this push uses the auxiliary pop-up feature. The default value is \\`false\\`. This is effective only when \\`PushType\\` is \\`MESSAGE\\`.
        # 
        # If the message is successfully converted to a notification, the data displayed in the notification is the value of the \\`HarmonyRemindTitle\\` and \\`HarmonyRemindBody\\` parameters set on the server.
        self.harmony_remind = harmony_remind
        # The HarmonyOS notification content used when a message is converted to a notification. This is effective only when \\`HarmonyRemind\\` is \\`true\\`.
        self.harmony_remind_body = harmony_remind_body
        # The HarmonyOS notification title used when a message is converted to a notification. This is effective only when \\`HarmonyRemind\\` is \\`true\\`.
        self.harmony_remind_title = harmony_remind_title
        # The notification message style:
        # 
        # - NORMAL: Normal notification (default)
        # 
        # - MULTI_LINE: Multi-line text style
        self.harmony_render_style = harmony_render_style
        # Test message flag:
        # 
        # - false: Normal message (default)
        # 
        # - true: Test message
        # 
        # For more information, see [pushOptions.testMessage](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/push-scenariozed-api-request-param-V5#section418321011212) in the HarmonyOS documentation.
        self.harmony_test_message = harmony_test_message
        # The URI corresponding to the in-app page ability.
        # >Notice: When \\`HarmonyActionType\\` is \\`APP_CUSTOM_PAGE\\`, fill in at least one of \\`HarmonyUri\\` or \\`HarmonyAction\\`. If there are multiple abilities, fill in the action and URI for each. The action is used with priority to find the corresponding in-app page.
        # 
        # For more information, see [ClickAction.uri](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/push-scenariozed-api-request-param-V5#section152462191216) in the HarmonyOS documentation.
        self.harmony_uri = harmony_uri
        # An idempotent parameter to prevent duplicate pushes caused by API call retries. If you make a call with the same \\`IdempotentToken\\` within 15 minutes, only one push is sent. Subsequent calls return the result of the first successful push.
        # 
        # > - The parameter must be a standard 36-character UUID (8-4-4-4-12). Each valid character must be a hexadecimal digit from 0-9 or a-f, case-insensitive.
        # >
        # > - This parameter only prevents duplicate pushes from retries. It cannot prevent duplicate pushes from concurrent calls.
        self.idempotent_token = idempotent_token
        # A custom ID for the push task. If \\`JobKey\\` is not empty, this field is included in the receipt logs. For more information about receipt logs, see [Receipt logs](https://help.aliyun.com/document_detail/434651.html).
        # 
        # > The format must consist of letters, numbers, underscores (_), or hyphens (-). The length cannot exceed 32 characters.
        self.job_key = job_key
        # Used for scheduled sending. If you do not set this parameter, the push is sent immediately.
        # The scheduled time can be no more than 7 days in the future.
        # 
        # The time must be in ISO 8601 format and in UTC: \\`YYYY-MM-DDThh:mm:ssZ\\`.
        # 
        # > Scheduled sending is not supported when \\`Target\\` is \\`TBD\\` (continuous push).
        self.push_time = push_time
        # The push type. Valid values:
        # 
        # - **NOTICE**: A notification. Notifications are sent to devices through vendor channels, such as APNs, Huawei, Xiaomi, and HarmonyOS, and appear directly in the device\\"s notification bar. When an Android device is online (the app process is active), the notification is preferentially sent through Alibaba Cloud\\"s proprietary channel. The Push software development kit (SDK) then constructs and displays the notification. This improves push performance and can save on vendor channel message quotas in some scenarios.
        # 
        # - **MESSAGE**: A message. Messages are sent through Alibaba Cloud\\"s proprietary online channel. They do not appear in the notification bar by default. Instead, the app must be active to receive and process them. Your business logic determines whether to trigger any actions. If a device is offline (the app process is inactive), it cannot receive messages immediately. In this case, use the \\`iOSRemind\\` or \\`AndroidRemind\\` parameter to convert the message into a notification. Alternatively, set the \\`StoreOffline\\` parameter to have the push system save the message. The system then delivers the message automatically when the device comes back online.
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
        # > * If you do not set this parameter, all channels can be used.
        # >
        # > * If you set this parameter, only the specified channels are used.
        # >
        # > * If the specified channels conflict with the sending policy, the push is not sent. For example, if an iOS notification can only be sent through the APNs channel, but \\`apns\\` is not included in this parameter, the push will fail.
        # >
        # > * If you specify \\`gcm\\`, pushes can be sent through both Google GCM and FCM channels. If you specify \\`fcm\\`, pushes can only be sent through the Google FCM channel.
        self.send_channels = send_channels
        # This parameter is deprecated.
        self.send_speed = send_speed
        # The delay time in seconds before triggering the text message.
        # 
        # This must be set if using SMS filter interaction. Set it to 15 seconds or more, with a maximum of 3 days, to avoid duplicate pushes and text messages.
        # 
        # > When using SMS filter interaction, the \\`ExpireTime\\` parameter is invalid. The notification expiration time is calculated based on the \\`SmsDelaySecs\\` parameter. The expiration time is the current time plus the \\`SmsDelaySecs\\` time.
        self.sms_delay_secs = sms_delay_secs
        # The key-value pairs for the variables in the SMS template. Format: `key1=value1&key2=value2`.
        self.sms_params = sms_params
        # The condition for triggering the text message. Valid values:
        # 
        # - **0**: Triggered when the push is not received.
        # 
        # - **1**: Triggered when the user does not open the push.
        self.sms_send_policy = sms_send_policy
        # The signature for the supplementary text message.
        self.sms_sign_name = sms_sign_name
        # The name of the SMS template for supplementary sending. Get this from the SMS template management interface. This is the system-assigned name, not the name set by the developer.
        self.sms_template_name = sms_template_name
        # Specifies whether to save offline messages and notifications. The default value is **false**.
        # 
        # If set to true, and a user is offline, the message is sent again when the user comes online before the \\`ExpireTime\\`. The default \\`ExpireTime\\` is 72 hours. iOS notifications are sent through APNs and are not affected by this parameter.
        self.store_offline = store_offline
        # The push target. Valid values:
        # 
        # - **DEVICE**: Push to devices.
        # 
        # - **ACCOUNT**: Push to accounts.
        # 
        # - **ALIAS**: Push to aliases.
        # 
        # - **TAG**: Push to tags.
        # 
        # - **ALL**: Push to all devices. The interval between two consecutive pushes to all devices of the same \\`DeviceType\\` must be at least 1 second.
        # 
        # > When pushing to all iOS devices, the push is sent to devices that have been active in the last 24 months and have not uninstalled the app. A push is considered delivered once the Apple Push Notification service (APNs) receives the request and does not return an error. This can cause a sharp increase in the number of active devices and lead to significant costs. Use this feature with caution.
        # 
        # - **TBD**: Initializes a continuous push. The target is specified by a subsequent call to the [ContinuouslyPush](https://help.aliyun.com/document_detail/2249917.html) API.
        # 
        # This parameter is required.
        self.target = target
        # Set this based on the \\`Target\\` type. Use commas to separate multiple values. If you exceed the limit, send multiple pushes.
        # 
        # - If \\`Target\\` is \\`DEVICE\\`, provide device IDs, such as \\`deviceid1,deviceid2\\`. You can specify up to 1,000 device IDs.
        # 
        # - If \\`Target\\` is \\`ACCOUNT\\`, provide account IDs, such as \\`account1,account2\\`. You can specify up to 1,000 account IDs.
        # 
        # - If \\`Target\\` is \\`ALIAS\\`, provide aliases, such as \\`alias1,alias2\\`. You can specify up to 1,000 aliases.
        # 
        # - If \\`Target\\` is \\`TAG\\`, you can use single or multiple tags. For more information about the format, see [Tag format](https://help.aliyun.com/document_detail/434847.html).
        # 
        # - If \\`Target\\` is \\`ALL\\`, set the value to **ALL**. This is a fixed parameter combination for pushing to all devices.
        # 
        # - If \\`Target\\` is \\`TBD\\`, set the value to **TBD**. This is a fixed parameter combination for continuous pushes.
        # 
        # This parameter is required.
        self.target_value = target_value
        # The title of the notification or message. The maximum length is 200 bytes.
        # 
        # This is required for pushes to Android and HarmonyOS. It is optional for iOS notifications. If you provide a title for an iOS notification:
        # 
        # - For iOS 10 and later, the notification displays the title.
        # 
        # - For iOS 8.2 to iOS 9.x, the title replaces the app name in the notification.
        self.title = title
        # Specifies whether to automatically truncate titles and content that are too long.
        # 
        # > This only applies to vendor channels that have explicit limits on title and content length. It does not apply to channels like APNs, Huawei, and Honor, which only limit the total request body size.
        self.trim = trim
        # iOS notifications are sent through APNs. Specify the environment.
        # 
        # - **DEV**: The development environment. Use this for apps installed and debugged directly from Xcode.
        # 
        # - **PRODUCT**: The production environment. Use this for apps distributed through the App Store, TestFlight, Ad Hoc, or enterprise distribution.
        self.i_osapns_env = i_osapns_env
        # The badge number on the top-right corner of the app icon on iOS.
        # 
        # > If \\`iOSBadgeAutoIncrement\\` is set to \\`true\\`, this parameter must be empty.
        self.i_osbadge = i_osbadge
        # Specifies whether to enable the auto-increment feature for the badge number. The default value is \\`false\\`.
        # 
        # > When this is \\`true\\`, \\`iOSBadge\\` must be empty.
        # 
        # The auto-increment feature is managed by the push server, which maintains a badge count for each device. This requires SDK version 1.9.5 or later. The user must also actively sync the badge number to the server.
        self.i_osbadge_auto_increment = i_osbadge_auto_increment
        # The extended properties of the iOS notification.
        # 
        # For iOS 10 and later, specify the resource URL for a rich push notification, such as \\`{"attachment": "https\\://xxxx.xxx/notification_pic.png"}\\`. This parameter must be in JSON map format to avoid parsing errors.
        self.i_osext_parameters = i_osext_parameters
        # The interruption level. Valid values:
        # 
        # - **passive**: The system adds the notification to the notification list without lighting up the screen or playing a sound.
        # 
        # - **active**: The system displays the notification immediately, lights up the screen, and can play a sound.
        # 
        # - **time-sensitive**: The system presents the notification immediately, lights up the screen, and can play a sound, but it does not break through system notification controls.
        # 
        # - **critical**: The system displays the notification immediately, lights up the screen, and plays a sound, bypassing the mute switch.
        self.i_osinterruption_level = i_osinterruption_level
        # A JSON string containing static pass-through parameters for Dynamic Island pushes. It includes static, custom user information, such as product numbers and order details.
        # 
        # > This is required when \\`iOSLiveActivityEvent\\` is \\`start\\`.
        self.i_oslive_activity_attributes = i_oslive_activity_attributes
        # The type of Live Activity to start.
        # 
        # > This is required when \\`iOSLiveActivityEvent\\` is \\`start\\`.
        self.i_oslive_activity_attributes_type = i_oslive_activity_attributes_type
        # Dynamic pass-through parameters for Dynamic Island pushes. It includes real-time updates, such as price or inventory changes.
        self.i_oslive_activity_content_state = i_oslive_activity_content_state
        # A UNIX timestamp in seconds. The ended Live Activity remains on the lock screen until this specified time. The maximum duration is 4 hours.
        self.i_oslive_activity_dismissal_date = i_oslive_activity_dismissal_date
        # Starts, updates, or ends a Live Activity.
        # 
        # - Enumeration: start | update | end
        self.i_oslive_activity_event = i_oslive_activity_event
        # The Live Activity ID reported by the device to your server. This is the unique identifier for the Live Activity.
        self.i_oslive_activity_id = i_oslive_activity_id
        # A UNIX timestamp in seconds. Marks the time when the activity\\"s content becomes outdated.
        self.i_oslive_activity_stale_date = i_oslive_activity_stale_date
        # The sound for an iOS notification. Specify the name of an audio file located in the app bundle or the \\`Library/Sounds\\` directory of the sandbox. For more information, see [How to set notification sounds for iOS pushes](https://help.aliyun.com/document_detail/48906.html).
        # 
        # If you specify an empty string (""), the notification is silent. If you do not set this parameter, the default system sound is used.
        self.i_osmusic = i_osmusic
        # The flag for the iOS notification content extension (iOS 10+). If set to \\`true\\`, an APNs notification can be processed by the extension before it is displayed. This must be set to \\`true\\` for silent notifications.
        self.i_osmutable_content = i_osmutable_content
        # Specifies the iOS notification category (iOS 10+).
        self.i_osnotification_category = i_osnotification_category
        # If a device receives multiple notifications with the same \\`CollapseId\\`, they are merged into a single notification. If the device is offline and receives consecutive notifications with the same \\`CollapseId\\`, only one is shown in the notification bar. This parameter is supported on iOS 10 and later.
        self.i_osnotification_collapse_id = i_osnotification_collapse_id
        # Groups iOS remote notifications using this property. It marks the identifier for the collapsed group.
        # This is supported only on iOS 12.0 and later.
        self.i_osnotification_thread_id = i_osnotification_thread_id
        # The score for highlighting the summary. The value must be a floating-point number between 0 and 1.
        self.i_osrelevance_score = i_osrelevance_score
        # If a device is offline when a message is pushed (meaning the persistent connection to the Mobile Push server is down), the push is sent once as a notification through Apple\\"s APNs channel.
        # 
        # > Converting offline messages to notifications is only supported in the production environment.
        self.i_osremind = i_osremind
        # The content of the iOS notification used when a message is converted to a notification. This is valid only when \\`iOSApnsEnv\\` is \\`PRODUCT\\` and \\`iOSRemind\\` is \\`true\\`.
        self.i_osremind_body = i_osremind_body
        # Specifies whether to enable iOS silent notifications.
        self.i_ossilent_notification = i_ossilent_notification
        # The subtitle of the iOS notification (iOS 10+).
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

        if self.app_key is not None:
            result['AppKey'] = self.app_key

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

        if self.idempotent_token is not None:
            result['IdempotentToken'] = self.idempotent_token

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

        if self.sms_delay_secs is not None:
            result['SmsDelaySecs'] = self.sms_delay_secs

        if self.sms_params is not None:
            result['SmsParams'] = self.sms_params

        if self.sms_send_policy is not None:
            result['SmsSendPolicy'] = self.sms_send_policy

        if self.sms_sign_name is not None:
            result['SmsSignName'] = self.sms_sign_name

        if self.sms_template_name is not None:
            result['SmsTemplateName'] = self.sms_template_name

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

        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')

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

        if m.get('IdempotentToken') is not None:
            self.idempotent_token = m.get('IdempotentToken')

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

        if m.get('SmsDelaySecs') is not None:
            self.sms_delay_secs = m.get('SmsDelaySecs')

        if m.get('SmsParams') is not None:
            self.sms_params = m.get('SmsParams')

        if m.get('SmsSendPolicy') is not None:
            self.sms_send_policy = m.get('SmsSendPolicy')

        if m.get('SmsSignName') is not None:
            self.sms_sign_name = m.get('SmsSignName')

        if m.get('SmsTemplateName') is not None:
            self.sms_template_name = m.get('SmsTemplateName')

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

