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
        # AppKey information.
        # 
        # This parameter is required.
        self.app_key = app_key
        # An idempotency parameter used to prevent duplicate pushes caused by API caller retries. When calls are made with the same IdempotentToken within 15 minutes, only one push is performed, and subsequent calls return the result of the first successful push.
        # 
        # > 
        # > - The parameter format is a standard 36-character UUID (8-4-4-4-12). Each valid character is a hexadecimal digit in the range 0-9 or a-f, case-insensitive.
        # > - This parameter is only used to prevent duplicate pushes caused by retries and cannot prevent duplicate pushes caused by concurrent calls.
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
        # Specify the Activity to open from the notification.
        # 
        # Only applicable when PushTask.N.AndroidOpenType="Activity", e.g., `com.alibaba.cloudpushdemo.bizactivity`.
        self.android_activity = android_activity
        # Set the badge increment value. The value is added to the existing badge count. Value range: [1-99].
        # > Only valid for Huawei/Honor vendor channel pushes. When both AndroidBadgeAddNum and AndroidBadgeSetNum are present, AndroidBadgeSetNum takes precedence.
        self.android_badge_add_num = android_badge_add_num
        # Full class name of the app entry Activity for badge settings.
        # 
        # > Only valid for Huawei/Honor vendor channel pushes.
        self.android_badge_class = android_badge_class
        # Set the badge to a fixed number. Value range: [0-99].
        # 
        # > For vendor channel pushes, this only takes effect on Huawei and Honor channels. For Alibaba Cloud proprietary channel pushes, this only takes effect on Huawei, Honor, and vivo devices.
        self.android_badge_set_num = android_badge_set_num
        # Body in long text mode. Length limit: 1,000 bytes (1 Chinese character counts as 3 bytes). Subject to specific vendor channel restrictions when sending.
        # 
        # Currently supported:
        # - Huawei: EMUI 10 and later
        # - Honor: Magic UI 4.0 and later
        # - Xiaomi: MIUI 10 and later
        # - OPPO: ColorOS 5.0 and later
        # - Meizu: Flyme
        # - Proprietary channel: Android SDK 3.6.0 and later
        # 
        # If this parameter is not provided in long text mode, the first non-empty value from Body and AndroidPopupBody is used.
        self.android_big_body = android_big_body
        # Image URL in big picture mode. Currently supported: Proprietary channel: Android SDK 3.6.0 and later.
        self.android_big_picture_url = android_big_picture_url
        # Title in long text mode. Length limit: 200 bytes (1 Chinese character counts as 3 bytes).
        # 
        # - Currently only supported by the Honor channel and Huawei channel EMUI 11 and later.
        # 
        # - If this parameter is not provided in long text mode, the first non-empty value from Title and AndroidPopupTitle is used.
        self.android_big_title = android_big_title
        # Set notification extended properties. This property does not take effect when the push type PushType is set to MESSAGE.
        # 
        # This parameter must be passed in JSON map format; otherwise, parsing errors will occur.
        self.android_ext_parameters = android_ext_parameters
        # Set the Honor channel notification type:
        # - **0**: Production notification (default).
        # - **1**: Test notification.
        # 
        # > Each application can send up to 1,000 test notifications per day, and this is not subject to the daily per-device push limit.
        self.android_honor_target_user_type = android_honor_target_user_type
        # Set the Huawei instant notification parameter:
        # - **0**: Send a regular Huawei notification (default).
        # - **1**: Send a Huawei instant notification.
        self.android_huawei_business_type = android_huawei_business_type
        # JSON string of the Huawei Android Live Notification data structure [LiveNotificationPayload](https://developer.huawei.com/consumer/cn/doc/HMSCore-References/rest-live-0000001562939968#ZH-CN_TOPIC_0000001700850537__p195121620102511). For development integration, see [Huawei Live Notification Push Guide](https://help.aliyun.com/document_detail/2983768.html)
        self.android_huawei_live_notification_payload = android_huawei_live_notification_payload
        # Huawei channel receipt ID. This receipt ID can be found in the receipt parameter configuration on the Huawei channel push operations platform.
        # 
        # > If the default receipt configuration on the Huawei channel push operations platform is set to Alibaba Cloud receipt, this is not required. If not, we recommend configuring the default Huawei channel receipt ID in the Alibaba Cloud EMAS Mobile Push console first.
        self.android_huawei_receipt_id = android_huawei_receipt_id
        # Set the Huawei channel notification type:
        # - **0**: Production notification (default).
        # - **1**: Test notification.
        # 
        # > Each application can send up to 500 test notifications per day, and this is not subject to the daily per-device push limit.
        self.android_huawei_target_user_type = android_huawei_target_user_type
        # Right-side icon URL. Currently supported:
        # - Huawei EMUI (only applicable in long text mode and Inbox mode)
        # - Honor Magic UI (only applicable in long text mode)
        # - Proprietary channel: Android SDK 3.5.0 and later
        self.android_image_url = android_image_url
        # Body content in Inbox mode. The content must be a valid JSON Array with no more than 5 elements. Currently supported:
        # 
        # - Huawei: EMUI 9 and later
        # - Honor: Magic UI 4.0 and later
        # - Xiaomi: MIUI 10 and later
        # - OPPO: ColorOS 5.0 and later
        # - Proprietary channel: Android SDK 3.6.0 and later
        self.android_inbox_body = android_inbox_body
        # Meizu message type
        # 
        # - 0: Public message (default)
        # - 1: Private message
        self.android_meizu_notice_msg_type = android_meizu_notice_msg_type
        # Purpose 1: After completing the [self-classification privilege application](https://developer.huawei.com/consumer/cn/doc/development/HMSCore-Guides/message-classification-0000001149358835?#section3410731125514), this is used to identify the message type, determine the [notification alert method](https://developer.huawei.com/consumer/cn/doc/development/HMSCore-Guides/message-classification-0000001149358835#ZH-CN_TOPIC_0000001149358835__p3850133955718), and speed up delivery for specific message types. For valid values, refer to the Huawei Push official documentation\\"s [Message Classification Standard](https://developer.huawei.com/consumer/cn/doc/development/HMSCore-Guides/message-classification-0000001149358835#section1076611477914). Use the "Cloud notification category value" or "Local notification category value" from the documentation table.
        # 
        # Purpose 2: After [applying for special permissions](https://developer.huawei.com/consumer/cn/doc/development/HMSCore-Guides/faq-0000001050042183#section037425218509), this is used to identify high-priority pass-through scenarios. Valid values:
        # - VOIP: Audio/video calls
        # - PLAY_VOICE: Voice playback
        # 
        # > For "Cloud notification category values" marked as "Not applicable", the Alibaba Cloud proprietary channel is used. For "Local notification category values" marked as "Not applicable", the Huawei channel is used.
        self.android_message_huawei_category = android_message_huawei_category
        # Huawei channel notification delivery priority. Valid values:
        # 
        # - HIGH
        # 
        # - NORMAL
        # 
        # Permission application is required. See: [Application link](https://developer.huawei.com/consumer/cn/doc/development/HMSCore-Guides/faq-0000001050042183#section037425218509).
        self.android_message_huawei_urgency = android_message_huawei_urgency
        # OPPO classifies messages into two categories: Communication & Service, and Content & Marketing.
        # 
        # Communication & Service (permission application required):
        # - IM: Instant messaging, audio, and video calls
        # - ACCOUNT: Personal account and asset changes
        # - DEVICE_REMINDER: Personal device reminders
        # - ORDER: Personal order/logistics status changes
        # - TODO: Personal schedule/to-do items
        # - SUBSCRIPTION: Personal subscriptions
        # 
        # Content & Marketing:
        # - NEWS: News and information
        # - CONTENT: Content recommendations
        # - MARKETING: Platform promotions
        # - SOCIAL: Social updates
        # 
        # For details, see [OPUSH Message Classification Rules](https://open.oppomobile.com/new/developmentDoc/info?id=13189)
        self.android_message_oppo_category = android_message_oppo_category
        # OPPO channel notification bar message alert level. Valid values:
        # - 1: Notification bar
        # - 2: Notification bar, lock screen, ringtone, and vibration (default notification level for Communication & Service messages)
        # - 16: Notification bar, lock screen, ringtone, vibration, and banner (permission application required)
        # 
        # > When using the AndroidMessageOppoNotifyLevel parameter, the AndroidMessageOppoCategory parameter must also be provided.
        self.android_message_oppo_notify_level = android_message_oppo_notify_level
        # vivo classifies messages into two categories: System messages and Operational messages.
        # 
        # System messages:
        # - IM: Instant messages
        # - ACCOUNT: Account and assets
        # - TODO: Schedule and to-do items
        # - DEVICE_REMINDER: Device information
        # - ORDER: Orders and logistics
        # - SUBSCRIPTION: Subscription reminders
        # 
        # Operational messages:
        # - NEWS: News
        # - CONTENT: Content recommendations
        # - MARKETING: Operational campaigns
        # - SOCIAL: Social updates
        # > For details, see [Classification Description](https://dev.vivo.com.cn/documentCenter/doc/359#s-ef3qugc3)
        self.android_message_vivo_category = android_message_vivo_category
        # Huawei vendor channel notification sound. Specify the name of an audio file stored in the client project\\"s app/src/main/res/raw/ directory. The file extension is not required.
        # 
        # If not set, the default ringtone is used.
        self.android_music = android_music
        # Priority of the notification position in the Android notification bar. Valid values: -2, -1, 0, 1, 2.
        self.android_notification_bar_priority = android_notification_bar_priority
        # Android custom notification bar style. Value range: 1-100.
        self.android_notification_bar_type = android_notification_bar_type
        # The channelId of the Android app. Must match the channelId configured in the app.
        # - Set the NotificationChannel parameter. For specific usage, see [FAQ: Notifications not received on Android 8.0+ devices](https://help.aliyun.com/document_detail/67398.html).
        # - Since the OPPO notification private channel\\"s channel_id is the same as the app\\"s channelId, the channel_id takes this value when pushing through the OPPO channel.
        # - For Huawei, FCM, and Alibaba Cloud proprietary channel pushes, the channel_id takes this value.
        self.android_notification_channel = android_notification_channel
        # Message grouping. Messages in the same group display only the latest one and the total count of messages received in that group in the notification bar. All messages are not displayed and cannot be expanded. Currently supported:
        # 
        # - Huawei vendor channel
        # - Honor vendor channel
        # - Proprietary channel: Android SDK 3.9.1 and earlier
        # 
        # > The proprietary channel no longer supports this parameter on Android SDK 3.9.2 and later.
        self.android_notification_group = android_notification_group
        # Set the Honor notification message classification importance parameter, which determines the notification behavior on user devices. Valid values:
        # 
        # - LOW: Information and marketing messages
        # 
        # - NORMAL: Service and communication messages
        # 
        # Application is required on the Honor platform. [Application link](https://developer.honor.com/cn/docs/11002/guides/notification-class#%E8%87%AA%E5%88%86%E7%B1%BB%E6%9D%83%E7%9B%8A%E7%94%B3%E8%AF%B7).
        self.android_notification_honor_channel = android_notification_honor_channel
        # Set the Huawei notification message classification importance parameter, which determines the notification behavior on user devices. Valid values:
        # 
        # - LOW: Information and marketing messages
        # - NORMAL: Service and communication messages
        # 
        # >- The Huawei channel now recommends using AndroidMessageHuaweiCategory for notification classification. AndroidNotificationHuaweiChannel is no longer required.
        # >- Application is required on the Huawei platform. [Application link](https://developer.huawei.com/consumer/cn/doc/development/HMSCore-Guides/message-classification-0000001149358835#section893184112272).
        self.android_notification_huawei_channel = android_notification_huawei_channel
        # Unique identifier for each message displayed in the notification bar. Different notification bar messages can share the same NotifyId, allowing new notifications to replace old ones.
        self.android_notification_notify_id = android_notification_notify_id
        # Message grouping. Messages in the same group are displayed collapsed in the notification bar and can be expanded. Notifications from different groups are displayed separately. Currently supported:
        # 
        # - Proprietary channel: Android SDK 3.9.2 and later
        self.android_notification_thread_id = android_notification_thread_id
        # Set the vivo notification message classification. Valid values:
        # 
        # - 0: Operational messages (default)
        # - 1: System messages
        # 
        # >- The vivo channel now recommends using AndroidMessageVivoCategory for notification classification. AndroidNotificationVivoChannel is no longer required.
        # >- Application is required on the vivo platform. See: [Application link](https://dev.vivo.com.cn/documentCenter/doc/359).
        self.android_notification_vivo_channel = android_notification_vivo_channel
        # Set the channelId for Xiaomi notification types. Application is required on the Xiaomi platform. See: [Application link](https://dev.mi.com/console/doc/detail?pId=2422#_4).
        # >- A single application on the Xiaomi channel can apply for up to 8 channels. Please plan ahead.
        self.android_notification_xiaomi_channel = android_notification_xiaomi_channel
        # Notification alert type. Valid values:
        # 
        # - **VIBRATE**: Vibration (default)
        # - **SOUND**: Sound
        # - **BOTH**: Sound and vibration
        # - **NONE**: Silent
        self.android_notify_type = android_notify_type
        # Action after clicking the notification. Valid values:
        # 
        # - APPLICATION: Open the app (default)
        # - ACTIVITY: Open an Android Activity
        # - URL: Open a URL
        # - NONE: No navigation
        self.android_open_type = android_open_type
        # The URL to open after Android receives the push. Only applicable when PushTask.N.AndroidOpenType="URL".
        self.android_open_url = android_open_url
        # JSON string of the OPPO Fluid Cloud intent deletion data structure [data](https://open.oppomobile.com/documentation/page/info?id=13578). This parameter is ignored when the AndroidOppoIntelligentIntent parameter is already provided. For development integration, see [OPPO Fluid Cloud Push Guide](https://help.aliyun.com/document_detail/2997310.html)
        self.android_oppo_delete_intent_data = android_oppo_delete_intent_data
        # JSON string of the OPPO Fluid Cloud intent sharing data structure [IntelligentIntent](https://open.oppomobile.com/documentation/page/info?id=13565). For development integration, see [OPPO Fluid Cloud Push Guide](https://help.aliyun.com/document_detail/2997310.html)
        self.android_oppo_intelligent_intent = android_oppo_intelligent_intent
        # Set the OPPO Fluid Cloud push environment:
        # - **0**: Production environment (default).
        # - **1**: Test environment.
        # 
        # > The OPPO Fluid Cloud test environment requires client-side setup. See [Environment Setup](https://open.oppomobile.com/documentation/page/info?id=13590).
        self.android_oppo_intent_env = android_oppo_intent_env
        # OPPO private message template content parameters
        self.android_oppo_private_content_parameters = android_oppo_private_content_parameters
        # OPPO private message template ID
        # 
        # >Warning: The OPPO private message template feature is no longer supported by MaasPush. To use this feature, please use the Push, PushV2, or MassPushV2 API instead.
        self.android_oppo_private_msg_template_id = android_oppo_private_msg_template_id
        # OPPO private message template title parameters
        self.android_oppo_private_title_parameters = android_oppo_private_title_parameters
        # Specify the Activity to navigate to when the notification is clicked.
        self.android_popup_activity = android_popup_activity
        # Body content in auxiliary popup mode. Required when the AndroidPopupActivity parameter is not empty.
        # 
        # Length limit: 200 characters (both Chinese and English characters count as one character each).
        # 
        # When using vendor channels, you must also comply with the vendor channel restrictions. For details, see [Android Auxiliary Channel Push Limits](https://help.aliyun.com/document_detail/165253.html).
        self.android_popup_body = android_popup_body
        # Title content in auxiliary popup mode. Required when the AndroidPopupActivity parameter is not empty.
        # 
        # Length limit: 50 characters (both Chinese and English characters count as one character each).
        # 
        # When using vendor channels, you must also comply with the vendor channel restrictions. For details, see [Android Auxiliary Channel Push Limits](https://help.aliyun.com/document_detail/165253.html).
        self.android_popup_title = android_popup_title
        # When the push type is message and the device is offline, this push will use the auxiliary popup feature. Defaults to false. Only takes effect when PushType=MESSAGE.
        # 
        # If the message-to-notification conversion push is successful, the notification displays the data set by the server\\"s AndroidPopupTitle and AndroidPopupBody parameter values. The data obtained when clicking the notification in the auxiliary popup\\"s onSysNoticeOpened method is the server-set Title and Body parameter values.
        self.android_remind = android_remind
        # Notification style. Valid values:
        # - **0**: Standard mode (default)
        # - **1**: Long text mode (supported by Huawei, Honor, Xiaomi, OPPO, Meizu, and proprietary channels)
        # - **2**: Big picture mode (supported by proprietary channel, not supported on Xiaomi devices)
        # - **3**: List mode (supported by Huawei, Honor, Xiaomi, OPPO, and proprietary channels)
        # > This parameter is required when using non-standard modes.
        self.android_render_style = android_render_style
        # Set the vendor channel notification type:
        # - **0**: Production notification (default).
        # - **1**: Test notification.
        # 
        # >- Configuring this parameter is equivalent to simultaneously configuring the AndroidHuaweiTargetUserType, AndroidHonorTargetUserType, AndroidVivoPushMode, and AndroidOppoIntentEnv parameters. The corresponding parameter for a specific vendor channel can override this parameter.
        # >- Currently supported: Huawei channel, Honor channel, vivo channel, and OPPO Fluid Cloud.
        self.android_target_user_type = android_target_user_type
        # JSON string of the vivo Atomic Island data structure [liveMessage](https://dev.vivo.com.cn/documentCenter/doc/896#s-fdagzbd4). For development integration, see [vivo Atomic Island Push Guide](https://help.aliyun.com/zh/document_detail/3030718.html)
        self.android_vivo_live_message = android_vivo_live_message
        # Set the vivo channel notification type:
        # - **0**: Production push (default).
        # - **1**: Test push.
        # 
        # > For test pushes, configure test devices in the vivo console in advance. The test device RegId can be obtained by searching for "onReceiveRegId regId" in the device startup logs.
        self.android_vivo_push_mode = android_vivo_push_mode
        # vivo channel receipt ID. This receipt ID can be found in the app information section of the push service on the vivo open platform.
        # 
        # > If the default receipt configuration on the vivo open platform is set to Alibaba Cloud receipt, this is not required. If not, we recommend configuring the default vivo channel receipt ID in the Alibaba Cloud EMAS Mobile Push console first.
        self.android_vivo_receipt_id = android_vivo_receipt_id
        # This parameter has been deprecated. All third-party auxiliary popups are now supported by the new parameter **AndroidPopupActivity**.
        self.android_xiao_mi_activity = android_xiao_mi_activity
        # This parameter has been deprecated. All third-party auxiliary popups are now supported by the new parameter **AndroidPopupBody**.
        self.android_xiao_mi_notify_body = android_xiao_mi_notify_body
        # This parameter has been deprecated. All third-party auxiliary popups are now supported by the new parameter **AndroidPopupTitle**.
        self.android_xiao_mi_notify_title = android_xiao_mi_notify_title
        # This parameter has been deprecated. Since August 2023, Xiaomi has officially discontinued support for dynamically setting small icons, right-side icons, and big pictures during push on new devices/systems.
        self.android_xiaomi_big_picture_url = android_xiaomi_big_picture_url
        # JSON string of the Xiaomi Super Island data structure [miui.focus.param](https://dev.mi.com/xiaomihyperos/documentation/detail?pId=2131). For development integration, see [Xiaomi Super Island Push Guide](https://help.aliyun.com/zh/document_detail/3037956.html)
        self.android_xiaomi_focus_param = android_xiaomi_focus_param
        # JSON string of the Xiaomi Super Island images [miui.focus.pic_xxx](https://dev.mi.com/xiaomihyperos/documentation/detail?pId=2131). For development integration, see [Xiaomi Super Island Push Guide](https://help.aliyun.com/zh/document_detail/3037956.html)
        self.android_xiaomi_focus_pics = android_xiaomi_focus_pics
        # This parameter has been deprecated. Since August 2023, Xiaomi has officially discontinued support for dynamically setting small icons, right-side icons, and big pictures during push on new devices/systems.
        self.android_xiaomi_image_url = android_xiaomi_image_url
        # Xiaomi private message template ID
        self.android_xiaomi_template_id = android_xiaomi_template_id
        # Xiaomi private message template parameters, JSON string
        self.android_xiaomi_template_params = android_xiaomi_template_params
        # Content of the notification/message for Android and HarmonyOS pushes; iOS message/notification content. The push content size is limited. See [Product Limits](https://help.aliyun.com/document_detail/92832.html).
        self.body = body
        # Device type. Valid values:
        # 
        # - HARMONY: HarmonyOS device
        # - iOS: iOS device
        # - ANDROID: Android device
        # - ALL: When the AppKey is for a legacy dual-platform app, this pushes to both Android and iOS devices simultaneously. When the AppKey is for a new single-platform app, the effect is the same as specifying the device type corresponding to the app type.
        # 
        # This parameter is required.
        self.device_type = device_type
        # Expiration time of offline messages/notifications. Used together with StoreOffline. Expired messages will no longer be sent. The maximum retention period is 72 hours. The default is 72 hours.
        # 
        # The time format follows the ISO 8601 standard and must use UTC time in the format YYYY-MM-DDThh:mm:ssZ. The expiration time cannot be earlier than the current time or the scheduled push time plus 3 seconds (`ExpireTime > PushTime + 3 seconds`). The 3-second buffer accounts for network and system latency. We recommend at least 1 minute for unicast pushes and at least 10 minutes for broadcast and batch pushes.
        self.expire_time = expire_time
        # The action corresponding to the built-in page ability of the app.
        # 
        # >Notice: When HarmonyActionType is APP_CUSTOM_PAGE, at least one of HarmonyUri and HarmonyAction must be provided.
        # 
        # For details, see HarmonyOS official documentation [ClickAction.action](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/push-scenariozed-api-request-param-V5#section152462191216)
        self.harmony_action = harmony_action
        # Action after clicking the notification. Valid values:
        # 
        # - APP_HOME_PAGE: Open the app home page
        # - APP_CUSTOM_PAGE: Open a custom app page
        self.harmony_action_type = harmony_action_type
        # HarmonyOS app badge increment number. See [HarmonyOS badge addNum field description](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/push-scenariozed-api-request-param-V5#section266310382145).</br>
        # Supported from HarmonyOS SDK 1.2.0.
        self.harmony_badge_add_num = harmony_badge_add_num
        # HarmonyOS app badge set number. See [HarmonyOS badge setNum field description](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/push-scenariozed-api-request-param-V5#section266310382145).</br>
        # Supported from HarmonyOS SDK 1.2.0.
        self.harmony_badge_set_num = harmony_badge_set_num
        # Notification message category. After completing the notification message self-classification privilege application, this is used to identify the message type. Different notification message types affect the display and alert methods. Valid values:
        # 
        # - IM: Instant messaging
        # - VOIP: Audio/video calls
        # - SUBSCRIPTION: Subscriptions
        # - TRAVEL: Travel
        # - HEALTH: Health
        # - WORK: Work task reminders
        # - ACCOUNT: Account updates
        # - EXPRESS: Orders & logistics
        # - FINANCE: Finance
        # - DEVICE_REMINDER: Device reminders
        # - MAIL: Email
        # - CUSTOMER_SERVICE: Customer service messages
        # - MARKETING: News, content recommendations, social updates, product promotions, financial updates, lifestyle information, surveys, feature recommendations, and operational campaigns (only marks the content, does not speed up message delivery), collectively referred to as information and marketing messages
        # 
        # For details, see HarmonyOS official documentation [Notification.category](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/push-scenariozed-api-request-param-V5#section17371529101117)
        self.harmony_category = harmony_category
        # Set notification extended properties. This property does not take effect when the push type PushType is set to MESSAGE.
        # 
        # This parameter must be passed in JSON map format; otherwise, parsing errors will occur.
        self.harmony_ext_parameters = harmony_ext_parameters
        # Extra data for notification extension messages.</br>
        # Valid when sending HarmonyOS notification extension messages.</br>
        # Conceptually equivalent to the extraData field of HarmonyOS notification extension messages. For the specific definition, see [HarmonyOS ExtensionPayload Description](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/push-scenariozed-api-request-param-V5#section161192514234).</br>
        # Supported from HarmonyOS SDK 1.2.0.
        self.harmony_extension_extra_data = harmony_extension_extra_data
        # When PushType is NOTICE, whether this is a HarmonyOS notification extension message.
        # 
        # - true: Send a notification extension message
        # - false: Send a regular notification (default)
        # 
        # Notification extension messages require permission to be applied for on the HarmonyOS side before sending. For details, see the HarmonyOS documentation [Send Notification Extension Messages](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V5/push-send-extend-noti-V5).</br>
        # Supported from HarmonyOS SDK 1.2.0.
        self.harmony_extension_push = harmony_extension_push
        # URL for the large icon on the right side of the notification. The URL must use the HTTPS protocol.
        # 
        # > Supported image formats: png, jpg, jpeg, heif, gif, bmp. Image dimensions must satisfy height × width < 25,000 pixels.
        # 
        # For details, see HarmonyOS official documentation [Notification.image](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/push-scenariozed-api-request-param-V5#section17371529101117)
        self.harmony_image_url = harmony_image_url
        # Content for multi-line text style. Required when HarmonyRenderStyle is MULTI_LINE. Up to 3 content items are supported.
        self.harmony_inbox_content = harmony_inbox_content
        # JSON string of the HarmonyOS Live View data structure [LiveViewPayload](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V13/push-scenariozed-api-request-param-V13#section66881469306). For development integration, see [HarmonyOS Live View Push Guide](https://help.aliyun.com/document_detail/2982112.html)
        self.harmony_live_view_payload = harmony_live_view_payload
        # Use the specified type of notification slot. Only valid when the Alibaba Cloud proprietary channel is online.
        # 
        # - SOCIAL_COMMUNICATION: Social communication.
        # - SERVICE_INFORMATION: Service reminders.
        # - CONTENT_INFORMATION: Content information.
        # - CUSTOMER_SERVICE: Customer service messages. This type is used for customer service messages between users and merchants, and must be initiated by the user.
        # - OTHER_TYPES: Others.
        # 
        # For details, see HarmonyOS official documentation [SlotType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/js-apis-notificationmanager-V5#slottype)
        self.harmony_notification_slot_type = harmony_notification_slot_type
        # Unique identifier for each message displayed in the notification. When not provided, the push service automatically generates a unique identifier for each message. Different notification messages can share the same notifyId, enabling new messages to replace old ones.
        # 
        # For details, see HarmonyOS official documentation [Notification.notifyId](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/push-scenariozed-api-request-param-V5#section17371529101117)
        self.harmony_notify_id = harmony_notify_id
        # HarmonyOS channel receipt ID. This receipt ID can be found in the receipt parameter configuration on the HarmonyOS channel push operations platform.
        # 
        # > If the default receipt configuration on the HarmonyOS channel push operations platform is set to Alibaba Cloud receipt, this is not required. If not, we recommend configuring the default HarmonyOS channel receipt ID in the Alibaba Cloud EMAS Mobile Push console first.
        # 
        # For details, see HarmonyOS official documentation [pushOptions.receiptId](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/push-scenariozed-api-request-param-V5#section418321011212)
        self.harmony_receipt_id = harmony_receipt_id
        # When the push type is message and the device is offline, this push will use the auxiliary popup feature. Defaults to false. Only takes effect when PushType=MESSAGE.
        # 
        # If the message-to-notification conversion push is successful, the notification displays the data set by the server\\"s HarmonyRemindTitle and HarmonyRemindBody parameter values.
        self.harmony_remind = harmony_remind
        # HarmonyOS notification content used when converting HarmonyOS messages to notifications. Only valid when HarmonyRemind is true.
        self.harmony_remind_body = harmony_remind_body
        # HarmonyOS notification title used when converting HarmonyOS messages to notifications. Only valid when HarmonyRemind is true.
        self.harmony_remind_title = harmony_remind_title
        # Notification message style:
        # - NORMAL: Standard notification (default)
        # - MULTI_LINE: Multi-line text style
        self.harmony_render_style = harmony_render_style
        # Test message flag:
        # 
        # - false: Normal message (default)
        # - true: Test message
        # 
        # For details, see HarmonyOS official documentation [pushOptions.testMessage](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/push-scenariozed-api-request-param-V5#section418321011212)
        self.harmony_test_message = harmony_test_message
        # The URI corresponding to the built-in page ability of the app.
        # >Notice: When HarmonyActionType is APP_CUSTOM_PAGE, at least one of HarmonyUri and HarmonyAction must be provided. When multiple Abilities exist, provide different action and URI values for each Ability. The action is prioritized when looking up the corresponding built-in app page.
        # 
        # For details, see HarmonyOS official documentation [ClickAction.uri](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/push-scenariozed-api-request-param-V5#section152462191216)
        self.harmony_uri = harmony_uri
        # Custom identifier for the push task. When JobKey is not empty, this field will be included in the receipt logs. For receipt log details, see [Receipt Logs](https://help.aliyun.com/document_detail/434651.html).
        self.job_key = job_key
        # Used for scheduled sending. If not set, the default is immediate sending.
        # 
        # The time format follows the ISO 8601 standard and must use UTC time in the format YYYY-MM-DDThh:mm:ssZ.
        self.push_time = push_time
        # Push type. Valid values:
        # 
        # - MESSAGE: indicates a message.
        # - NOTICE: indicates a notification.
        # 
        # This parameter is required.
        self.push_type = push_type
        # Specify sending channels. Valid values:
        # 
        # - accs: Alibaba Cloud proprietary channel
        # - huawei: Huawei channel
        # - honor: Honor channel
        # - xiaomi: Xiaomi channel
        # - oppo: OPPO channel
        # - vivo: vivo channel
        # - meizu: Meizu channel
        # - gcm: Google GCM channel (legacy HTTP)
        # - fcm: Google Firebase channel (HTTP v1 API)
        # - apns: APNs channel
        # - harmony: HarmonyOS channel
        # 
        # >- If this parameter is not configured, all channels are available.
        # >- If this parameter is configured, only the specified channels are used.
        # >- If the configured channels conflict with the sending strategy (e.g., iOS notifications only go through the APNs channel, but this parameter does not include apns), the push will not be sent.
        # >- If gcm is configured, both Google GCM and FCM channels can be used. If fcm is configured, only the Google FCM channel can be used.
        self.send_channels = send_channels
        # This parameter has been deprecated.
        self.send_speed = send_speed
        # Whether to store offline messages/notifications. StoreOffline defaults to false.
        # 
        # If stored, when the user is offline during push, the message will be resent when the user comes online within the expiration time (ExpireTime). ExpireTime defaults to 72 hours. iOS notifications are delivered through the APNs channel and are not affected by StoreOffline.
        self.store_offline = store_offline
        # Push target. Valid values:
        # 
        # - DEVICE: push by device.
        # - ACCOUNT: push by account.
        # - ALIAS: push by alias.
        # 
        # This parameter is required.
        self.target = target
        # Set based on Target. Multiple values are separated by commas. If the limit is exceeded, you need to split the push into multiple calls.
        # 
        # - Target=DEVICE: values such as `deviceid1,deviceid2` (up to 1,000 supported).
        # - Target=ACCOUNT: values such as `account1,account2` (up to 1,000 supported).
        # - Target=ALIAS: values such as `alias1,alias2` (up to 1,000 supported).
        # 
        # This parameter is required.
        self.target_value = target_value
        # Title of the notification/message during push. Length limit: 200 bytes.
        # Required for Android and HarmonyOS pushes. Optional for iOS push notifications. If provided:
        # * iOS 10+: the notification displays the title.
        # * iOS 8.2 <= iOS version < iOS 10: replaces the notification app name.
        self.title = title
        # Whether to automatically truncate titles and content that are too long.
        # Note: This only applies to vendor channels that explicitly limit title and content length. It does not apply to channels like APNs, Huawei, and Honor that do not limit title and content individually but only limit the total request body size.
        self.trim = trim
        # iOS notifications are sent through the APNs center. You need to specify the corresponding environment information.
        # 
        # - DEV: Development environment, applicable to apps installed and debugged directly via Xcode.
        # - PRODUCT: Production environment, applicable to apps distributed through App Store, TestFlight, Ad Hoc, and enterprise distribution.
        self.i_osapns_env = i_osapns_env
        # iOS app icon badge number in the upper-right corner.
        # 
        # > If iOSBadgeAutoIncrement is set to True, this field must be empty.
        self.i_osbadge = i_osbadge
        # Whether to enable badge auto-increment. Defaults to false.
        # 
        # > When this is set to true, iOSBadge must be empty.
        # 
        # The badge auto-increment feature is maintained by the push server for each device\\"s badge count. Users must use SDK version V1.9.5 or later and actively sync the badge number to the server.
        self.i_osbadge_auto_increment = i_osbadge_auto_increment
        # Extended properties of iOS notifications.
        # 
        # On iOS 10+, you can specify the resource URL for rich media push notifications here: `{"attachment": "https://xxxx.xxx/notification_pic.png"} `. This parameter must be passed in JSON map format; otherwise, parsing errors will occur.
        self.i_osext_parameters = i_osext_parameters
        # Interruption level. Valid values:
        # 
        # - passive: The system adds the notification to the notification list without lighting up the screen or playing sound.
        # 
        # - active: The system immediately displays the notification, lights up the screen, and can play sound.
        # 
        # - time-sensitive: The system immediately presents the notification, lights up the screen, and can play sound, but does not break through system notification controls.
        # 
        # - critical: The system immediately displays the notification, lights up the screen, and plays sound bypassing the mute switch.
        self.i_osinterruption_level = i_osinterruption_level
        # JSON string. Static pass-through parameters for Dynamic Island push. Contains static user-defined information such as product ID and order information.
        # 
        # > Required when iOSLiveActivityEvent is start.
        self.i_oslive_activity_attributes = i_oslive_activity_attributes
        # The type of Live Activity to start.
        # > Required when iOSLiveActivityEvent is start.
        self.i_oslive_activity_attributes_type = i_oslive_activity_attributes_type
        # Dynamic pass-through parameters for Dynamic Island push. Contains real-time update information such as price and inventory changes.
        self.i_oslive_activity_content_state = i_oslive_activity_content_state
        # The ended Live Activity will remain on the lock screen until the specified time, up to a maximum of 4 hours.
        self.i_oslive_activity_dismissal_date = i_oslive_activity_dismissal_date
        # Start, update, or end a Live Activity.
        # 
        # - Enum: start | update | end
        self.i_oslive_activity_event = i_oslive_activity_event
        # The Live Activity ID reported by the device to the user\\"s server. A unique identifier for the Live Activity.
        self.i_oslive_activity_id = i_oslive_activity_id
        # Timestamp in seconds, marking the expiration time of the activity content.
        self.i_oslive_activity_stale_date = i_oslive_activity_stale_date
        # iOS notification sound. Specify the name of an audio file stored in the app bundle or the sandbox Library/Sounds directory. See: How to set notification sound for iOS push.
        # 
        # If set to an empty string (""), the notification is silent. If not set, the default system alert sound is used.
        self.i_osmusic = i_osmusic
        # iOS notification processing extension flag (iOS 10+). If set to true, APNs push notifications can reach the Extension for processing before being displayed. Must be set to true for silent notifications.
        self.i_osmutable_content = i_osmutable_content
        # Specify the iOS notification Category (iOS 10+).
        self.i_osnotification_category = i_osnotification_category
        # When a device receives messages with the same CollapseId, they are merged into one. When the device is offline, consecutive messages with the same CollapseId will show only one notification in the notification bar. Supported on iOS 10+.
        self.i_osnotification_collapse_id = i_osnotification_collapse_id
        # Groups iOS remote notifications using this property, marking the group identifier for collapsed notifications. Only supported on iOS 12.0+.
        self.i_osnotification_thread_id = i_osnotification_thread_id
        # Summary highlight score. Value range: a floating-point number in [0,1\\].
        self.i_osrelevance_score = i_osrelevance_score
        # When the device is offline during message push (i.e., the persistent connection channel to the Mobile Push server is disconnected), this push will be delivered as a notification through Apple\\"s APNs channel once.
        # 
        # > Offline message-to-notification conversion only applies to the production environment.
        self.i_osremind = i_osremind
        # iOS notification content used when converting iOS messages to notifications. Only valid when iOSApnsEnv=PRODUCT and iOSRemind is true.
        self.i_osremind_body = i_osremind_body
        # Whether to enable iOS silent notification.
        self.i_ossilent_notification = i_ossilent_notification
        # iOS notification subtitle content (iOS 10+).
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

