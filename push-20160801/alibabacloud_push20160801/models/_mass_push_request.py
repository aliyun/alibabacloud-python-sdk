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
        # The AppKey.
        # 
        # This parameter is required.
        self.app_key = app_key
        # The idempotent parameter used to prevent duplicate pushes caused by API client retries. If the same IdempotentToken is used within 15 minutes, only one push is performed, and subsequent calls return the result of the first successful push.
        # 
        # > 
        # > - The parameter format is a standard 36-character UUID (8-4-4-4-12). Each valid character is a hexadecimal digit in the range of 0-9 or a-f, and it is case-insensitive.
        # > - This parameter is only used to prevent duplicate pushes caused by retries. It cannot prevent duplicate pushes caused by concurrent calls.
        self.idempotent_token = idempotent_token
        # The array of independent push tasks.
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
        android_vivo_template_id: str = None,
        android_vivo_template_params: str = None,
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
        # The activity to be opened by the notification.
        # 
        # This parameter is valid only when PushTask.N.AndroidOpenType is set to ACTIVITY. Example: `com.alibaba.cloudpushdemo.bizactivity`.
        self.android_activity = android_activity
        # Specifies the increment value for the badge. The value is added to the existing badge number. Valid values: 1 to 99.
        # > This parameter is valid only for push notifications sent through Huawei or Honor vendor channels. If both AndroidBadgeAddNum and AndroidBadgeSetNum are specified, AndroidBadgeSetNum takes precedence.
        self.android_badge_add_num = android_badge_add_num
        # The fully qualified class name of the entry Activity for badge settings.
        # > This parameter is valid only for push notifications sent through Huawei or Honor vendor channels.
        self.android_badge_class = android_badge_class
        # Specifies the fixed number for the badge. Valid values: 0 to 99.
        # > This parameter takes effect only on Huawei and Honor channels when push notifications are sent through vendor channels. When push notifications are sent through the Alibaba Cloud proprietary channel, this parameter takes effect only on Huawei, Honor, and vivo devices.
        self.android_badge_set_num = android_badge_set_num
        # The body in long text mode. Maximum length: 1,000 bytes. One Chinese character counts as 3 bytes. The actual limit is subject to the specific vendor channel during sending.
        # 
        # Currently supported by:
        # - Huawei: EMUI 10 or later
        # - Honor: Magic UI 4.0 or later
        # - Xiaomi: MIUI 10 or later
        # - OPPO: ColorOS 5.0 or later
        # - Meizu: Flyme
        # - Proprietary channel: Android SDK 3.6.0 or later
        # 
        # If this parameter is not provided in long text mode, the first non-empty value from Body and AndroidPopupBody is used.
        self.android_big_body = android_big_body
        # The image URL in big image mode. Currently supported by the proprietary channel with Android SDK 3.6.0 or later.
        self.android_big_picture_url = android_big_picture_url
        # The title in long text mode. Maximum length: 200 bytes. One Chinese character counts as 3 bytes.
        # 
        # - This parameter is currently supported only by the Honor channel and the Huawei channel with EMUI 11 or later.
        # 
        # - If this parameter is not provided in long text mode, the first non-empty value from Title and AndroidPopupTitle is used.
        self.android_big_title = android_big_title
        # The extended properties of the notification. This parameter does not take effect when the push type PushType is set to MESSAGE.
        # 
        # This parameter must be passed in JSON map format. Otherwise, a parsing error occurs.
        self.android_ext_parameters = android_ext_parameters
        # The notification type for the Honor channel. Valid values:
        # - **0**: Formal notification. This is the default value.
        # - **1**: Test notification.
        # 
        # > Each application can send 1,000 test notifications per day, which is not subject to the daily push limit per device.
        self.android_honor_target_user_type = android_honor_target_user_type
        # The Huawei quick notification parameter. Valid values:
        # - **0**: Send a standard Huawei notification. This is the default value.
        # - **1**: Send a Huawei quick notification.
        self.android_huawei_business_type = android_huawei_business_type
        # The JSON string of the Huawei Android Live Notification data structure [LiveNotificationPayload](https://developer.huawei.com/consumer/cn/doc/HMSCore-References/rest-live-0000001562939968#ZH-CN_TOPIC_0000001700850537__p195121620102511). For development integration, refer to [Huawei Live Notification push guide](https://help.aliyun.com/document_detail/2983768.html).
        self.android_huawei_live_notification_payload = android_huawei_live_notification_payload
        # The receipt ID for the Huawei channel. You can view this receipt ID in the receipt parameter settings of the Huawei channel push operations platform.
        # 
        # > If the default receipt configuration on the Huawei channel push operations platform is set to Alibaba Cloud receipt, you do not need to provide this parameter. Otherwise, configure the default receipt ID for the Huawei channel in the Alibaba Cloud EMAS Mobile Push console first.
        self.android_huawei_receipt_id = android_huawei_receipt_id
        # The notification type for the Huawei channel. Valid values:
        # - **0**: Formal notification. This is the default value.
        # - **1**: Test notification.
        # 
        # > Each application can send 500 test notifications per day, which is not subject to the daily push limit per device.
        self.android_huawei_target_user_type = android_huawei_target_user_type
        # The URL of the right-side icon. Currently supported by:
        # - Huawei EMUI: Applicable only in long text mode and inbox mode.
        # - Honor Magic UI: Applicable only in long text mode.
        # - Proprietary channel: Android SDK 3.5.0 or later.
        self.android_image_url = android_image_url
        # The body in inbox mode. The content must be a valid JSON array with no more than five elements. Currently supported by:
        # 
        # - Huawei: EMUI 9 or later
        # - Honor: Magic UI 4.0 or later
        # - Xiaomi: MIUI 10 or later
        # - OPPO: ColorOS 5.0 or later
        # - Proprietary channel: Android SDK 3.6.0 or later
        self.android_inbox_body = android_inbox_body
        # The Meizu message type. Valid values:
        # 
        # - 0: Public message. This is the default value.
        # - 1: Private message.
        self.android_meizu_notice_msg_type = android_meizu_notice_msg_type
        # Purpose 1: After you complete the [self-classification permission application](https://developer.huawei.com/consumer/cn/doc/development/HMSCore-Guides/message-classification-0000001149358835?#section3410731125514), this parameter is used to identify the message type, determine the [message reminder method](https://developer.huawei.com/consumer/cn/doc/development/HMSCore-Guides/message-classification-0000001149358835#ZH-CN_TOPIC_0000001149358835__p3850133955718), and accelerate the sending of specific types of messages. For valid values, refer to the [Message classification standards](https://developer.huawei.com/consumer/cn/doc/development/HMSCore-Guides/message-classification-0000001149358835#section1076611477914) in the official Huawei push documentation, and fill in the "Cloud notification category value" or "Local notification category value" in the document table.
        # 
        # Purpose 2: After you [apply for special permissions](https://developer.huawei.com/consumer/cn/doc/development/HMSCore-Guides/faq-0000001050042183#section037425218509), this parameter is used to identify high-priority pass-through scenarios. Valid values:
        # - VOIP: Audio and video calls.
        # - PLAY_VOICE: Voice broadcast.
        # 
        # > If the "Cloud notification category value" is "Not applicable", the message is sent through the Alibaba Cloud proprietary channel. If the "Local notification category value" is "Not applicable", the message is sent through the Huawei channel.
        self.android_message_huawei_category = android_message_huawei_category
        # The delivery priority for Huawei channel notifications. Valid values:
        # 
        # - HIGH
        # 
        # - NORMAL
        # 
        # You must apply for this permission. For more information, see [Application link](https://developer.huawei.com/consumer/cn/doc/development/HMSCore-Guides/faq-0000001050042183#section037425218509).
        self.android_message_huawei_urgency = android_message_huawei_urgency
        # OPPO message categorization includes two categories for management: Communication and Service, and Content and Marketing.
        # 
        # Communication and Service (requires permission application):
        # - IM: Instant chat, audio calls, and video calls.
        # - ACCOUNT: Individual account and asset changes.
        # - DEVICE_REMINDER: Personal device reminders.
        # - ORDER: Personal order and logistics status changes.
        # - TODO: Personal schedules and to-do lists.
        # - SUBSCRIPTION: Personal subscriptions.
        # 
        # Content and Marketing:
        # - NEWS: News and information.
        # - CONTENT: Content recommendations.
        # - MARKETING: Platform activities.
        # - SOCIAL: Social updates.
        # 
        # For more information, see [OPUSH message classification rules](https://open.oppomobile.com/new/developmentDoc/info?id=13189).
        self.android_message_oppo_category = android_message_oppo_category
        # The notification bar message reminder level for the OPPO channel. Valid values:
        # - 1: Notification bar.
        # - 2: Notification bar, lock screen, ringtone, and vibration. This is the default notification level for communication and service messages.
        # - 16: Notification bar, lock screen, ringtone, vibration, and banner. Requires permission application.
        # 
        # > When you use the AndroidMessageOppoNotifyLevel parameter, you must also pass the AndroidMessageOppoCategory parameter.
        self.android_message_oppo_notify_level = android_message_oppo_notify_level
        # vivo message categorization includes two categories for management: System messages and Operational messages. 
        # 
        # System messages:
        # - IM: Instant messages.
        # - ACCOUNT: Accounts and assets.
        # - TODO: Schedules and to-do lists.
        # - DEVICE_REMINDER: Device information.
        # - ORDER: Orders and logistics.
        # - SUBSCRIPTION: Subscription reminders.
        # 
        # Operational messages:
        # - NEWS: News.
        # - CONTENT: Content recommendations.
        # - MARKETING: Operational activities.
        # - SOCIAL: Social updates.
        # > For more information, see [Classification description](https://dev.vivo.com.cn/documentCenter/doc/359#s-ef3qugc3).
        self.android_message_vivo_category = android_message_vivo_category
        # The notification sound for the Huawei vendor channel. Specify the name of the audio file stored in the app/src/main/res/raw/ directory of the client project. Do not include the file extension.
        # 
        # If this parameter is not specified, the default ringtone is used.
        self.android_music = android_music
        # The priority of the Android notification display position in the notification bar. Valid values: -2, -1, 0, 1, and 2.
        self.android_notification_bar_priority = android_notification_bar_priority
        # The custom notification bar style for Android. Valid values: 1 to 100.
        self.android_notification_bar_type = android_notification_bar_type
        # The channel ID of the Android application. This value must match the channel ID in the application.
        # - For more information about the NotificationChannel parameter, see [FAQ: Notifications are not received on devices running Android 8.0 or later](https://help.aliyun.com/document_detail/67398.html).
        # - Because the channel_id of the OPPO private message channel is the same as the channel ID of the application, this value is used as the channel_id for OPPO channel pushes.
        # - This value is used as the channel_id for Huawei, FCM, and Alibaba Cloud proprietary channel pushes.
        self.android_notification_channel = android_notification_channel
        # The message group. For messages in the same group, only the latest message and the total number of received messages in the group are displayed in the notification bar. All messages are not displayed and cannot be expanded. Currently supported by:
        # 
        # - Huawei vendor channel
        # - Honor vendor channel
        # - Proprietary channel with Android SDK 3.9.1 or earlier
        # 
        # > The proprietary channel no longer supports this parameter in Android SDK 3.9.2 or later.
        self.android_notification_group = android_notification_group
        # The importance parameter for Honor notification message classification, which determines the notification behavior on user devices. Valid values:
        # 
        # - LOW: Information and marketing messages.
        # 
        # - NORMAL: Service and communication messages.
        # 
        # You must apply for this permission on the Honor platform. For more information, see [Application link](https://developer.honor.com/cn/docs/11002/guides/notification-class#%E8%87%AA%E5%88%86%E7%B1%BB%E6%9D%83%E7%9B%8A%E7%94%B3%E8%AF%B7).
        self.android_notification_honor_channel = android_notification_honor_channel
        # The importance parameter for Huawei notification message classification, which determines the notification behavior on user devices. Valid values:
        # 
        # - LOW: Information and marketing messages.
        # - NORMAL: Service and communication messages.
        # 
        # > - For the Huawei channel, use AndroidMessageHuaweiCategory for notification classification instead of AndroidNotificationHuaweiChannel.
        # > - You must apply for this permission on the Huawei platform. For more information, see [Application link](https://developer.huawei.com/consumer/cn/doc/development/HMSCore-Guides/message-classification-0000001149358835#section893184112272).
        self.android_notification_huawei_channel = android_notification_huawei_channel
        # The unique identifier for each message when displayed in the notification bar. Different notification bar messages can share the same NotifyId, allowing new notification bar messages to overwrite old ones.
        self.android_notification_notify_id = android_notification_notify_id
        # The message thread ID. Messages in the same group are collapsed and can be expanded in the notification bar. Notifications in different groups are displayed separately. Currently supported by:
        # 
        # - Proprietary channel with Android SDK 3.9.2 or later
        self.android_notification_thread_id = android_notification_thread_id
        # The vivo notification message classification. Valid values:
        # 
        # - 0: Operational messages. This is the default value.
        # - 1: System messages.
        # 
        # > - For the vivo channel, use AndroidMessageVivoCategory for notification classification instead of AndroidNotificationVivoChannel.
        # > - You must apply for this permission on the vivo platform. For more information, see [Application link](https://dev.vivo.com.cn/documentCenter/doc/359).
        self.android_notification_vivo_channel = android_notification_vivo_channel
        # The channel ID for Xiaomi notification types. You must apply for this permission on the Xiaomi platform. For more information, see [Application link](https://dev.mi.com/console/doc/detail?pId=2422#_4).
        # > - A single application can apply for a maximum of eight channels on the Xiaomi channel. Plan ahead.
        self.android_notification_xiaomi_channel = android_notification_xiaomi_channel
        # The reminder method for the notification. Valid values:
        # 
        # - **VIBRATE**: Vibration. This is the default value.
        # - **SOUND**: Sound.
        # - **BOTH**: Sound and vibration.
        # - **NONE**: Silent.
        self.android_notify_type = android_notify_type
        # The action to perform after the notification is clicked. Valid values:
        # 
        # - APPLICATION: Open the application. This is the default value.
        # - ACTIVITY: Open the specified Android activity.
        # - URL: Open the specified URL.
        # - NONE: Perform no action.
        self.android_open_type = android_open_type
        # The URL to be opened after the Android device receives the push. This parameter is valid only when PushTask.N.AndroidOpenType is set to URL.
        self.android_open_url = android_open_url
        # The JSON character string of the OPPO Fluid Cloud intent delete data structure [data](https://open.oppomobile.com/documentation/page/info?id=13578). This parameter is invalid if the AndroidOppoIntelligentIntent parameter is already specified. For development integration, see References: [OPPO Fluid Cloud push guide](https://help.aliyun.com/document_detail/2997310.html).
        self.android_oppo_delete_intent_data = android_oppo_delete_intent_data
        # The JSON character string of the OPPO Fluid Cloud intent sharing data structure [IntelligentIntent](https://open.oppomobile.com/documentation/page/info?id=13565). For development integration, see References: [OPPO Fluid Cloud push guide](https://help.aliyun.com/document_detail/2997310.html).
        self.android_oppo_intelligent_intent = android_oppo_intelligent_intent
        # The push environment for OPPO Fluid Cloud. Valid values:
        # - **0**: Formal environment. This is the default value.
        # - **1**: Test environment.
        # 
        # > To use the OPPO Fluid Cloud test environment, you must build it on the client side by referring to [Environment setup](https://open.oppomobile.com/documentation/page/info?id=13590).
        self.android_oppo_intent_env = android_oppo_intent_env
        # The content parameter of the OPPO private message template.
        self.android_oppo_private_content_parameters = android_oppo_private_content_parameters
        # The OPPO private message template ID.
        # 
        # >Warning: The OPPO private message template feature is no longer supported by MaasPush. To use this feature, call the Push, PushV2, or MassPushV2 operation.
        self.android_oppo_private_msg_template_id = android_oppo_private_msg_template_id
        # The title parameter of the OPPO private message template.
        self.android_oppo_private_title_parameters = android_oppo_private_title_parameters
        # The activity to navigate to after the notification is clicked.
        self.android_popup_activity = android_popup_activity
        # The body content in auxiliary pop-up window mode. This parameter is required when the AndroidPopupActivity parameter is not empty.
        # 
        # Maximum length: 200 characters. Both Chinese and English characters count as one character.
        # 
        # If a vendor channel is used, the body must also meet the limits of the vendor channel. For more information, see [Limits on auxiliary channel pushes for Android](https://help.aliyun.com/document_detail/165253.html).
        self.android_popup_body = android_popup_body
        # The title content in auxiliary pop-up window mode. This parameter is required when the AndroidPopupActivity parameter is not empty. 
        # 
        # Maximum length: 50 characters. Both Chinese and English characters count as one character.
        # 
        # If a vendor channel is used, the title must also meet the limits of the vendor channel. For more information, see [Limits on auxiliary channel pushes for Android](https://help.aliyun.com/document_detail/165253.html).
        self.android_popup_title = android_popup_title
        # Specifies whether to use the auxiliary pop-up window feature when the device is offline during a message push. Default value: false. This parameter takes effect only when PushType is set to MESSAGE.
        # 
        # If the message-to-notification push is successful, the data displayed in the received notification is the value of the AndroidPopupTitle and AndroidPopupBody parameters set on the server. When you click the notification, the data obtained in the onSysNoticeOpened method of the auxiliary pop-up window is the value of the Title and Body parameters set on the server.
        self.android_remind = android_remind
        # The notification style. Valid values:
        # - **0**: Standard mode. This is the default value.
        # - **1**: Long text mode. Supported by Huawei, Honor, Xiaomi, OPPO, Meizu, and the proprietary channel.
        # - **2**: Big image mode. Supported by the proprietary channel, but not supported by Xiaomi devices.
        # - **3**: Inbox mode. Supported by Huawei, Honor, Xiaomi, OPPO, and the proprietary channel.
        # > This parameter is required if a non-standard mode is used.
        self.android_render_style = android_render_style
        # Settings for the vendor channel notification type. Valid values:
        # - **0**: Formal notification. This is the default value.
        # - **1**: Test notification.
        # 
        # > - The parameter settings are equivalent to configuring the AndroidHuaweiTargetUserType, AndroidHonorTargetUserType, AndroidVivoPushMode, and AndroidOppoIntentEnv parameters at the same time. The corresponding parameters for specific vendor channels can overwrite this parameter.
        # > - Currently supported by: Huawei channel, Honor channel, vivo channel, and OPPO Fluid Cloud.
        self.android_target_user_type = android_target_user_type
        # The JSON character string of the vivo Atomic Island data structure [liveMessage](https://dev.vivo.com.cn/documentCenter/doc/896#s-fdagzbd4). For development integration, see References: [vivo Atomic Island push guide](https://www.alibabacloud.com/help/en/document_detail/3030718.html).
        self.android_vivo_live_message = android_vivo_live_message
        # The notification type for the vivo channel. Valid values:
        # - **0**: Formal push. This is the default value.
        # - **1**: Test push.
        # 
        # > For test pushes, configure the test devices in the vivo console in advance. You can obtain the RegId of the test device by searching for "onReceiveRegId regId" in the device startup log.
        self.android_vivo_push_mode = android_vivo_push_mode
        # The receipt ID for the vivo channel. You can view this receipt ID in the application information of the push service on the vivo open platform.
        # 
        # > If the default receipt configuration on the vivo open platform is set to Alibaba Cloud receipt, you do not need to provide this parameter. Otherwise, configure the default receipt ID for the vivo channel in the Alibaba Cloud EMAS Mobile Push console first.
        self.android_vivo_receipt_id = android_vivo_receipt_id
        # The vivo template ID.
        self.android_vivo_template_id = android_vivo_template_id
        # The parameters of the vivo template. The value is a JSON object string.
        self.android_vivo_template_params = android_vivo_template_params
        # **[Deprecated]** This parameter is deprecated. All third-party auxiliary pop-up windows are uniformly supported by the new **AndroidPopupActivity** parameter.
        self.android_xiao_mi_activity = android_xiao_mi_activity
        # **[Deprecated]** This parameter is deprecated. All third-party auxiliary pop-up windows are uniformly supported by the new **AndroidPopupBody** parameter.
        self.android_xiao_mi_notify_body = android_xiao_mi_notify_body
        # **[Deprecated]** This parameter is deprecated. All third-party auxiliary pop-up windows are uniformly supported by the new **AndroidPopupTitle** parameter.
        self.android_xiao_mi_notify_title = android_xiao_mi_notify_title
        # **[Deprecated]** This parameter is deprecated. Since August 2023, Xiaomi no longer supports dynamically setting small icons, right-side icons, and big images during pushes on new devices or systems.
        self.android_xiaomi_big_picture_url = android_xiaomi_big_picture_url
        # The JSON character string of the Xiaomi Super Island data structure [miui.focus.param](https://dev.mi.com/xiaomihyperos/documentation/detail?pId=2131). For development integration, see References: [Xiaomi Super Island push guide](https://www.alibabacloud.com/help/en/document_detail/3037956.html).
        self.android_xiaomi_focus_param = android_xiaomi_focus_param
        # The JSON character string of the Xiaomi Super Island data images [miui.focus.pic_xxx](https://dev.mi.com/xiaomihyperos/documentation/detail?pId=2131). For development integration, see References: [Xiaomi Super Island push guide](https://www.alibabacloud.com/help/en/document_detail/3037956.html).
        self.android_xiaomi_focus_pics = android_xiaomi_focus_pics
        # **[Deprecated]** This parameter is deprecated. Since August 2023, Xiaomi no longer supports dynamically setting small icons, right-side icons, and big images during pushes on new devices or systems.
        self.android_xiaomi_image_url = android_xiaomi_image_url
        # The Xiaomi private message template ID.
        self.android_xiaomi_template_id = android_xiaomi_template_id
        # The parameters of the Xiaomi private message template. The value is a JSON string.
        self.android_xiaomi_template_params = android_xiaomi_template_params
        # The content of the notification or message for Android and HarmonyOS pushes, or the content of the message or notification for iOS pushes. The content size is limited. For more information, see [Limits](https://help.aliyun.com/document_detail/92832.html).
        self.body = body
        # The device type. Valid values:
        # 
        # - HARMONY: HarmonyOS device
        # - iOS: iOS device
        # - ANDROID: Android device
        # - ALL: If the AppKey belongs to a legacy dual-platform application, this value indicates that the message is pushed to both Android and iOS devices. If the AppKey belongs to a new single-platform application, this value has the same effect as specifying the device type corresponding to the application type.
        # 
        # This parameter is required.
        self.device_type = device_type
        # The expiration time of the offline message or notification. This parameter is used together with StoreOffline. An expired message or notification is not sent. The maximum retention period is 72 hours. Default value: 72 hours.
        # 
        # Specify the time in the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time must be in UTC. The expiration time cannot be earlier than the current time or 3 seconds after the scheduled sending time (ExpireTime > PushTime + 3 seconds). The 3-second buffer is used to compensate for network and system latency. Set the expiration time to at least 1 minute for single pushes and at least 10 minutes for full pushes and batch pushes.
        self.expire_time = expire_time
        # The action corresponding to the ability of the built-in page in the app.
        # 
        # >Notice: When HarmonyActionType is set to APP_CUSTOM_PAGE, you must specify at least one of the HarmonyUri and HarmonyAction fields.
        # 
        # For more information, see [ClickAction.action](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/push-scenariozed-api-request-param-V5#section152462191216) on the HarmonyOS official website.
        self.harmony_action = harmony_action
        # The action to perform after the notification is clicked. Valid values:
        # 
        # - APP_HOME_PAGE: Opens the app home page.
        # - APP_CUSTOM_PAGE: Opens a custom page in the app.
        self.harmony_action_type = harmony_action_type
        # The increment value for the badge of the HarmonyOS app. For more information, see [Description of the addNum field for HarmonyOS badges](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/push-scenariozed-api-request-param-V5#section266310382145).</br>
        # This parameter is supported in HarmonyOS SDK 1.2.0 and later.
        self.harmony_badge_add_num = harmony_badge_add_num
        # The fixed number for the badge of the HarmonyOS app. For more information, see [Description of the setNum field for HarmonyOS badges](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/push-scenariozed-api-request-param-V5#section266310382145).</br>
        # This parameter is supported in HarmonyOS SDK 1.2.0 and later.
        self.harmony_badge_set_num = harmony_badge_set_num
        # The category of the notification message. After you apply for the notification message self-categorization permission, this parameter is used as the identity of the message type. Different notification message types affect the display and reminder methods of messages. Valid values:
        # 
        # - IM: Instant chat.
        # - VOIP: Audio and video calls.
        # - SUBSCRIPTION: subscribe.
        # - TRAVEL: Travel.
        # - HEALTH: Health.
        # - WORK: Work reminders.
        # - ACCOUNT: Account updates.
        # - EXPRESS: Orders and logistics.
        # - FINANCE: Finance.
        # - DEVICE_REMINDER: Device reminders.
        # - MAIL: Emails.
        # - CUSTOMER_SERVICE: Customer service messages.
        # - MARKETING: News, content recommendations, social updates, product promotions, financial updates, lifestyle information, surveys, feature recommendations, and operational activity. This category only identifies the content and does not accelerate message sending. These are collectively referred to as information and marketing messages.
        # 
        # For details, see [Notification.category](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/push-scenariozed-api-request-param-V5#section17371529101117) on the HarmonyOS official website.
        self.harmony_category = harmony_category
        # The extended properties of the notification. This parameter does not take effect when the push type PushType is set to MESSAGE.
        # 
        # This parameter must be passed in JSON map format. Otherwise, a parsing error occurs.
        self.harmony_ext_parameters = harmony_ext_parameters
        # The extra data of the extended notification message.</br>
        # This parameter is valid when you send HarmonyOS extended notification messages.</br>
        # This parameter is conceptually equivalent to the extraData field of a HarmonyOS extended notification message. For the specific definition, see [HarmonyOS ExtensionPayload description](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/push-scenariozed-api-request-param-V5#section161192514234).</br>
        # This parameter is supported in HarmonyOS SDK 1.2.0 and later.
        self.harmony_extension_extra_data = harmony_extension_extra_data
        # Specifies whether to send a HarmonyOS extended notification message when PushType is set to NOTICE. Valid values:
        # 
        # - true: Sends an extended notification message.
        # - false: Sends a normal notification. This is the default value.
        # 
        # You must apply for permissions on the HarmonyOS side before you can send extended notification messages. For more information, see [Send extended notification messages](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V5/push-send-extend-noti-V5) in the HarmonyOS documentation.</br>
        # This parameter is supported in HarmonyOS SDK 1.2.0 and later.
        self.harmony_extension_push = harmony_extension_push
        # The URL of the large icon on the right side of the notification. The URL must use the HTTPS protocol.
        # 
        # > Supported image formats include PNG, JPG, JPEG, HEIF, GIF, and BMP. The product of the image width and height must be less than 25,000 pixels.
        # 
        # For more information, see [Notification.image](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/push-scenariozed-api-request-param-V5#section17371529101117) on the HarmonyOS official website.
        self.harmony_image_url = harmony_image_url
        # The content in the multi-line text style. This field is required when HarmonyRenderStyle is set to MULTI_LINE. A maximum of three content items are supported.
        self.harmony_inbox_content = harmony_inbox_content
        # The JSON string of the HarmonyOS Live View data structure [LiveViewPayload](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V13/push-scenariozed-api-request-param-V13#section66881469306). For development integration, refer to [HarmonyOS Live View push guide](https://help.aliyun.com/document_detail/2982112.html).
        self.harmony_live_view_payload = harmony_live_view_payload
        # The type of the notification channel to use. This parameter is valid only when the Alibaba Cloud proprietary channel is online. Valid values:
        # 
        # - SOCIAL_COMMUNICATION: Social communication.
        # - SERVICE_INFORMATION: Service reminders.
        # - CONTENT_INFORMATION: Content information.
        # - CUSTOMER_SERVICE: Customer service messages. This type is used for customer service messages between users and merchants and must be initiated by the user.
        # - OTHER_TYPES: Other types.
        # 
        # For more information, see [SlotType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/js-apis-notificationmanager-V5#slottype) on the HarmonyOS official website.
        self.harmony_notification_slot_type = harmony_notification_slot_type
        # The unique identifier of each message when the notification is displayed. If this parameter is not specified, the push service automatically generates a unique identifier for each message. Different notification messages can have the same notifyId to allow new messages to overwrite old ones.
        # 
        # For more information, see [Notification.notifyId](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/push-scenariozed-api-request-param-V5#section17371529101117) on the HarmonyOS official website.
        self.harmony_notify_id = harmony_notify_id
        # The receipt ID for the HarmonyOS channel. You can view this receipt ID in the receipt parameter settings of the HarmonyOS channel push operations platform.
        # 
        # > If the default receipt configured on the HarmonyOS channel push operations platform is the Alibaba Cloud receipt, you do not need to provide this parameter. Otherwise, we recommend that you configure the default receipt ID for the HarmonyOS channel in the Alibaba Cloud EMAS shift Push console first.
        # 
        # For details, see [pushOptions.receiptId](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/push-scenariozed-api-request-param-V5#section418321011212) on the HarmonyOS official website.
        self.harmony_receipt_id = harmony_receipt_id
        # Specifies whether to use the auxiliary pop-up window feature when a push notification of the message type is sent to an offline device. Default value: false. This parameter takes effect only when PushType is set to MESSAGE.
        # 
        # If the message is successfully converted to a notification and pushed, the received notification displays the data specified by the HarmonyRemindTitle and HarmonyRemindBody parameters on the server.
        self.harmony_remind = harmony_remind
        # The HarmonyOS notification content used when a message is converted to a notification. This parameter is valid only when HarmonyRemind is set to true.
        self.harmony_remind_body = harmony_remind_body
        # The HarmonyOS notification title used when a message is converted to a notification. This parameter is valid only when HarmonyRemind is set to true.
        self.harmony_remind_title = harmony_remind_title
        # The style of the notification message. Valid values:
        # - NORMAL: Normal notification. This is the default value.
        # - MULTI_LINE: Multi-line text style.
        self.harmony_render_style = harmony_render_style
        # Specifies whether the message is a test message. Valid values:
        # 
        # - false: Normal message. This is the default value.
        # - true: Test message.
        # 
        # For more information, see [pushOptions.testMessage](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/push-scenariozed-api-request-param-V5#section418321011212) on the HarmonyOS official website.
        self.harmony_test_message = harmony_test_message
        # The URI corresponding to the ability of the built-in page in the app.
        # >Notice: When HarmonyActionType is set to APP_CUSTOM_PAGE, you must specify at least one of the HarmonyUri and HarmonyAction fields. If multiple abilities exist, specify the action and URI for each ability. The action is preferentially used to find the corresponding built-in page in the app.
        # 
        # For more information, see [ClickAction.uri](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/push-scenariozed-api-request-param-V5#section152462191216) on the HarmonyOS official website.
        self.harmony_uri = harmony_uri
        # The custom identifier of the push task. If JobKey is not empty, this field is included in the receipt log. For more information, see [Receipt logs](https://help.aliyun.com/document_detail/434651.html).
        self.job_key = job_key
        # The scheduled sending time. If this parameter is not specified, the message is sent immediately.
        # 
        # Specify the time in the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time must be in UTC.
        self.push_time = push_time
        # The push type. Valid values:
        # 
        # - MESSAGE: message
        # - NOTICE: notification
        # 
        # This parameter is required.
        self.push_type = push_type
        # The sending channels. Valid values:
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
        # > - If this parameter is not configured, all channels are available.
        # > - If this parameter is configured, only the specified channels are used.
        # > - If the configured channels conflict with the sending policy (for example, iOS notifications can only be sent through the APNs channel, but apns is not included in this parameter), the message is not sent.
        # > - If gcm is configured, both Google GCM and FCM channels can be used. If fcm is configured, only the Google FCM channel can be used.
        self.send_channels = send_channels
        # **[Deprecated]** This parameter is deprecated.
        self.send_speed = send_speed
        # Specifies whether to save offline messages or notifications. Default value: false.
        # 
        # If this parameter is set to true and the user is offline during the push, the message or notification is sent again when the user comes online within the expiration time specified by ExpireTime. The default value of ExpireTime is 72 hours. iOS notifications are sent through the APNs channel and are not affected by the StoreOffline parameter.
        self.store_offline = store_offline
        # The push target. Valid values:
        # 
        # - DEVICE: device
        # - ACCOUNT: account
        # - ALIAS: alias
        # 
        # This parameter is required.
        self.target = target
        # The target value, which is specified based on the Target parameter. Separate multiple values with commas. If the number of values exceeds the limit, you must push the message in multiple batches.
        # 
        # - If Target is set to DEVICE, the value is in the format of `deviceid1,deviceid2`. A maximum of 1,000 devices are supported.
        # - If Target is set to ACCOUNT, the value is in the format of `account1,account2`. A maximum of 1,000 accounts are supported.
        # - If Target is set to ALIAS, the value is in the format of `alias1,alias2`. A maximum of 1,000 aliases are supported.
        # 
        # This parameter is required.
        self.target_value = target_value
        # The title of the notification or message. Maximum length: 200 bytes.
        # This parameter is required for Android and HarmonyOS pushes. This parameter is optional for iOS notification pushes. If you specify this parameter for iOS:
        # * For iOS 10 and later, the title is displayed in the notification.
        # * For iOS 8.2 to iOS 9.x, the title replaces the application name in the notification.
        self.title = title
        # Specifies whether to automatically truncate excessively long titles and content.
        # Note: This parameter applies only to vendor channels that explicitly limit the length of titles and content. It does not apply to channels such as APNs, Huawei, and Honor, which do not limit the length of titles and content but only limit the total request body size.
        self.trim = trim
        # To send iOS notifications through the APNs center, you must specify the corresponding environment context. Valid values:
        # 
        # - DEV: The development environment. This value applies to applications that are directly installed and debugged by using Xcode.
        # - PRODUCT: The production environment. This value applies to applications distributed through the App Store, TestFlight, Ad Hoc, and enterprise distribution.
        self.i_osapns_env = i_osapns_env
        # The badge number displayed in the upper-right corner of the iOS application icon.
        # 
        # > If iOSBadgeAutoIncrement is set to true, this parameter must be left empty.
        self.i_osbadge = i_osbadge
        # Specifies whether to enable the automatic badge increment feature. Default value: false.
        # 
        # > When this parameter is set to true, iOSBadge must be left empty.
        # 
        # The automatic badge increment feature maintains the badge count for each device on the push server. This feature requires SDK V1.9.5 or later, and users must actively synchronize the badge number to the server.
        self.i_osbadge_auto_increment = i_osbadge_auto_increment
        # The extension property of the iOS notification.
        # 
        # For iOS 10 and later, you can specify the resource URL for rich media push notifications in this parameter: `{"attachment": "https://www.example.com/notification_pic.png"}`. This parameter must be passed in JSON map format. Otherwise, a parse error occurs.
        self.i_osext_parameters = i_osext_parameters
        # The interruption level. Valid values:
        # 
        # - passive: The system adds the notification to the notification list without turning on the screen or playing a sound.
        # 
        # - active: The system displays the notification immediately, turns on the screen, and can play a sound.
        # 
        # - time-sensitive: The system displays the notification immediately, turns on the screen, and can play a sound, but does not break through the system notification controls.
        # 
        # - critical: The system displays the notification immediately, turns on the screen, and plays a sound bypassing the silent switch.
        self.i_osinterruption_level = i_osinterruption_level
        # The JSON string that contains the static pass-through parameters for Dynamic Island pushes. Static parameter includes static user-defined information, such as product IDs and order information.
        # 
        # > Static parameter is required when iOSLiveActivityEvent is set to start.
        self.i_oslive_activity_attributes = i_oslive_activity_attributes
        # The type of the Live Activity to be started.
        # > This parameter is required when iOSLiveActivityEvent is set to start.
        self.i_oslive_activity_attributes_type = i_oslive_activity_attributes_type
        # The pass-through dynamic parameter for Dynamic Island pushes. This parameter includes real-time update information, such as price and inventory changes.
        self.i_oslive_activity_content_state = i_oslive_activity_content_state
        # The time until which the ended Live Activity remains on the Lock Screen. The maximum retention period is 4 hours.
        self.i_oslive_activity_dismissal_date = i_oslive_activity_dismissal_date
        # The event to start, update, or end a Live Activity. Valid values: start, update, and end.
        self.i_oslive_activity_event = i_oslive_activity_event
        # The Live Activity ID reported by the device to the user server. This is the unique identifier of the Live Activity.
        self.i_oslive_activity_id = i_oslive_activity_id
        # The second-level timestamp that marks the expiration time of the activity content.
        self.i_oslive_activity_stale_date = i_oslive_activity_stale_date
        # The sound of the iOS notification. Specify the name of the audio file stored in the app bundle or the sandbox Library/Sounds directory. For more information, see How to set the notification sound for iOS pushes.
        # 
        # If this parameter is set to an empty string (""), the notification is silent. If this parameter is not specified, the default value "default" is used, which indicates the system prompt sound.
        self.i_osmusic = i_osmusic
        # The iOS notification processing extension flag (iOS 10 and later). If this parameter is set to true, the notification pushed by APNs can be processed by the extension before it is displayed. This parameter must be set to true for silent notifications.
        self.i_osmutable_content = i_osmutable_content
        # The category of the iOS notification (iOS 10 and later).
        self.i_osnotification_category = i_osnotification_category
        # The collapse ID. If a device receives messages with the same CollapseId, the messages are merged into one. If the device is offline and continuously receives messages with the same CollapseId, only one notification is displayed in the notification bar. This parameter is supported in iOS 10 and later.
        self.i_osnotification_collapse_id = i_osnotification_collapse_id
        # The thread ID used to group iOS remote notifications and mark the identifier of the collapsed group. This parameter is supported only in iOS 12.0 and later.
        self.i_osnotification_thread_id = i_osnotification_thread_id
        # The relevance score for summary highlighting. Valid values: a floating-point number in the range of [0,1].
        self.i_osrelevance_score = i_osrelevance_score
        # If the device is offline during a message push (that is, the persistent connection to the Mobile Push server is disconnected), the message is delivered once as a notification through the Apple APNs channel.
        # 
        # > Offline message-to-notification conversion applies only to the production environment.
        self.i_osremind = i_osremind
        # The iOS notification content used when an iOS message is converted to a notification. This parameter is valid only when iOSApnsEnv is set to PRODUCT and iOSRemind is set to true.
        self.i_osremind_body = i_osremind_body
        # Specifies whether to enable iOS silent notifications.
        self.i_ossilent_notification = i_ossilent_notification
        # The subtitle of the iOS notification (iOS 10 and later).
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

        if self.android_vivo_template_id is not None:
            result['AndroidVivoTemplateId'] = self.android_vivo_template_id

        if self.android_vivo_template_params is not None:
            result['AndroidVivoTemplateParams'] = self.android_vivo_template_params

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

        if m.get('AndroidVivoTemplateId') is not None:
            self.android_vivo_template_id = m.get('AndroidVivoTemplateId')

        if m.get('AndroidVivoTemplateParams') is not None:
            self.android_vivo_template_params = m.get('AndroidVivoTemplateParams')

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

