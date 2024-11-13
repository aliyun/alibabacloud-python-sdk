# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, Any


class Alert(TeaModel):
    def __init__(
        self,
        body: str = None,
        subtitle: str = None,
        title: str = None,
    ):
        self.body = body
        self.subtitle = subtitle
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        if self.subtitle is not None:
            result['subtitle'] = self.subtitle
        if self.title is not None:
            result['title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        if m.get('subtitle') is not None:
            self.subtitle = m.get('subtitle')
        if m.get('title') is not None:
            self.title = m.get('title')
        return self


class Body(TeaModel):
    def __init__(
        self,
        activity: str = None,
        add_badge: int = None,
        after_open: str = None,
        builder_id: int = None,
        custom: str = None,
        expand_image: str = None,
        icon: str = None,
        img: str = None,
        play_lights: bool = None,
        play_sound: bool = None,
        play_vibrate: bool = None,
        re_pop: int = None,
        set_badge: int = None,
        sound: str = None,
        text: str = None,
        title: str = None,
        url: str = None,
    ):
        self.activity = activity
        self.add_badge = add_badge
        self.after_open = after_open
        self.builder_id = builder_id
        self.custom = custom
        self.expand_image = expand_image
        self.icon = icon
        self.img = img
        self.play_lights = play_lights
        self.play_sound = play_sound
        self.play_vibrate = play_vibrate
        self.re_pop = re_pop
        self.set_badge = set_badge
        self.sound = sound
        self.text = text
        self.title = title
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.activity is not None:
            result['activity'] = self.activity
        if self.add_badge is not None:
            result['addBadge'] = self.add_badge
        if self.after_open is not None:
            result['afterOpen'] = self.after_open
        if self.builder_id is not None:
            result['builderId'] = self.builder_id
        if self.custom is not None:
            result['custom'] = self.custom
        if self.expand_image is not None:
            result['expandImage'] = self.expand_image
        if self.icon is not None:
            result['icon'] = self.icon
        if self.img is not None:
            result['img'] = self.img
        if self.play_lights is not None:
            result['playLights'] = self.play_lights
        if self.play_sound is not None:
            result['playSound'] = self.play_sound
        if self.play_vibrate is not None:
            result['playVibrate'] = self.play_vibrate
        if self.re_pop is not None:
            result['rePop'] = self.re_pop
        if self.set_badge is not None:
            result['setBadge'] = self.set_badge
        if self.sound is not None:
            result['sound'] = self.sound
        if self.text is not None:
            result['text'] = self.text
        if self.title is not None:
            result['title'] = self.title
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('activity') is not None:
            self.activity = m.get('activity')
        if m.get('addBadge') is not None:
            self.add_badge = m.get('addBadge')
        if m.get('afterOpen') is not None:
            self.after_open = m.get('afterOpen')
        if m.get('builderId') is not None:
            self.builder_id = m.get('builderId')
        if m.get('custom') is not None:
            self.custom = m.get('custom')
        if m.get('expandImage') is not None:
            self.expand_image = m.get('expandImage')
        if m.get('icon') is not None:
            self.icon = m.get('icon')
        if m.get('img') is not None:
            self.img = m.get('img')
        if m.get('playLights') is not None:
            self.play_lights = m.get('playLights')
        if m.get('playSound') is not None:
            self.play_sound = m.get('playSound')
        if m.get('playVibrate') is not None:
            self.play_vibrate = m.get('playVibrate')
        if m.get('rePop') is not None:
            self.re_pop = m.get('rePop')
        if m.get('setBadge') is not None:
            self.set_badge = m.get('setBadge')
        if m.get('sound') is not None:
            self.sound = m.get('sound')
        if m.get('text') is not None:
            self.text = m.get('text')
        if m.get('title') is not None:
            self.title = m.get('title')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class Message2ThirdChannel(TeaModel):
    def __init__(
        self,
        set_badge: int = None,
        add_badge: int = None,
        big_body: str = None,
        big_title: str = None,
        expand_image: str = None,
        img: str = None,
        sound: str = None,
        text: str = None,
        title: str = None,
    ):
        self.set_badge = set_badge
        self.add_badge = add_badge
        self.big_body = big_body
        self.big_title = big_title
        self.expand_image = expand_image
        self.img = img
        self.sound = sound
        self.text = text
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.set_badge is not None:
            result['SetBadge'] = self.set_badge
        if self.add_badge is not None:
            result['addBadge'] = self.add_badge
        if self.big_body is not None:
            result['bigBody'] = self.big_body
        if self.big_title is not None:
            result['bigTitle'] = self.big_title
        if self.expand_image is not None:
            result['expandImage'] = self.expand_image
        if self.img is not None:
            result['img'] = self.img
        if self.sound is not None:
            result['sound'] = self.sound
        if self.text is not None:
            result['text'] = self.text
        if self.title is not None:
            result['title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SetBadge') is not None:
            self.set_badge = m.get('SetBadge')
        if m.get('addBadge') is not None:
            self.add_badge = m.get('addBadge')
        if m.get('bigBody') is not None:
            self.big_body = m.get('bigBody')
        if m.get('bigTitle') is not None:
            self.big_title = m.get('bigTitle')
        if m.get('expandImage') is not None:
            self.expand_image = m.get('expandImage')
        if m.get('img') is not None:
            self.img = m.get('img')
        if m.get('sound') is not None:
            self.sound = m.get('sound')
        if m.get('text') is not None:
            self.text = m.get('text')
        if m.get('title') is not None:
            self.title = m.get('title')
        return self


class AndroidPayload(TeaModel):
    def __init__(
        self,
        body: Body = None,
        display_type: str = None,
        extra: Dict[str, Any] = None,
        message_2third_channel: Message2ThirdChannel = None,
    ):
        self.body = body
        self.display_type = display_type
        self.extra = extra
        self.message_2third_channel = message_2third_channel

    def validate(self):
        if self.body:
            self.body.validate()
        if self.message_2third_channel:
            self.message_2third_channel.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        if self.display_type is not None:
            result['displayType'] = self.display_type
        if self.extra is not None:
            result['extra'] = self.extra
        if self.message_2third_channel is not None:
            result['message2ThirdChannel'] = self.message_2third_channel.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = Body()
            self.body = temp_model.from_map(m['body'])
        if m.get('displayType') is not None:
            self.display_type = m.get('displayType')
        if m.get('extra') is not None:
            self.extra = m.get('extra')
        if m.get('message2ThirdChannel') is not None:
            temp_model = Message2ThirdChannel()
            self.message_2third_channel = temp_model.from_map(m['message2ThirdChannel'])
        return self


class AndroidShortPayloadBody(TeaModel):
    def __init__(
        self,
        custom: str = None,
    ):
        self.custom = custom

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom is not None:
            result['custom'] = self.custom
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('custom') is not None:
            self.custom = m.get('custom')
        return self


class AndroidShortPayload(TeaModel):
    def __init__(
        self,
        body: AndroidShortPayloadBody = None,
        extra: Dict[str, Any] = None,
    ):
        self.body = body
        self.extra = extra

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        if self.extra is not None:
            result['extra'] = self.extra
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = AndroidShortPayloadBody()
            self.body = temp_model.from_map(m['body'])
        if m.get('extra') is not None:
            self.extra = m.get('extra')
        return self


class Aps(TeaModel):
    def __init__(
        self,
        alert: Alert = None,
        badge: str = None,
        category: str = None,
        content_available: int = None,
        interruption_level: str = None,
        sound: str = None,
        thread_id: str = None,
    ):
        self.alert = alert
        self.badge = badge
        self.category = category
        self.content_available = content_available
        self.interruption_level = interruption_level
        self.sound = sound
        self.thread_id = thread_id

    def validate(self):
        if self.alert:
            self.alert.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert is not None:
            result['alert'] = self.alert.to_map()
        if self.badge is not None:
            result['badge'] = self.badge
        if self.category is not None:
            result['category'] = self.category
        if self.content_available is not None:
            result['contentAvailable'] = self.content_available
        if self.interruption_level is not None:
            result['interruptionLevel'] = self.interruption_level
        if self.sound is not None:
            result['sound'] = self.sound
        if self.thread_id is not None:
            result['threadID'] = self.thread_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alert') is not None:
            temp_model = Alert()
            self.alert = temp_model.from_map(m['alert'])
        if m.get('badge') is not None:
            self.badge = m.get('badge')
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('contentAvailable') is not None:
            self.content_available = m.get('contentAvailable')
        if m.get('interruptionLevel') is not None:
            self.interruption_level = m.get('interruptionLevel')
        if m.get('sound') is not None:
            self.sound = m.get('sound')
        if m.get('threadID') is not None:
            self.thread_id = m.get('threadID')
        return self


class ChannelProperties(TeaModel):
    def __init__(
        self,
        channel_activity: str = None,
        channel_fcm: str = None,
        huawei_channel_category: str = None,
        huawei_channel_importance: str = None,
        huawei_message_urgency: str = None,
        main_activity: str = None,
        oppo_category: str = None,
        oppo_channel_id: str = None,
        oppo_notify_level: str = None,
        use_huawei_message: str = None,
        vivo_add_badge: str = None,
        vivo_category: str = None,
        vivo_push_mode: str = None,
        xiaomi_channel_id: str = None,
    ):
        self.channel_activity = channel_activity
        self.channel_fcm = channel_fcm
        self.huawei_channel_category = huawei_channel_category
        self.huawei_channel_importance = huawei_channel_importance
        self.huawei_message_urgency = huawei_message_urgency
        self.main_activity = main_activity
        self.oppo_category = oppo_category
        self.oppo_channel_id = oppo_channel_id
        self.oppo_notify_level = oppo_notify_level
        self.use_huawei_message = use_huawei_message
        self.vivo_add_badge = vivo_add_badge
        self.vivo_category = vivo_category
        self.vivo_push_mode = vivo_push_mode
        self.xiaomi_channel_id = xiaomi_channel_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_activity is not None:
            result['channelActivity'] = self.channel_activity
        if self.channel_fcm is not None:
            result['channelFcm'] = self.channel_fcm
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
        if m.get('vivoAddBadge') is not None:
            self.vivo_add_badge = m.get('vivoAddBadge')
        if m.get('vivoCategory') is not None:
            self.vivo_category = m.get('vivoCategory')
        if m.get('vivoPushMode') is not None:
            self.vivo_push_mode = m.get('vivoPushMode')
        if m.get('xiaomiChannelId') is not None:
            self.xiaomi_channel_id = m.get('xiaomiChannelId')
        return self


class IosPayload(TeaModel):
    def __init__(
        self,
        aps: Aps = None,
        extra: Dict[str, Any] = None,
    ):
        self.aps = aps
        self.extra = extra

    def validate(self):
        if self.aps:
            self.aps.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aps is not None:
            result['aps'] = self.aps.to_map()
        if self.extra is not None:
            result['extra'] = self.extra
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aps') is not None:
            temp_model = Aps()
            self.aps = temp_model.from_map(m['aps'])
        if m.get('extra') is not None:
            self.extra = m.get('extra')
        return self


class Policy(TeaModel):
    def __init__(
        self,
        expire_time: str = None,
        outer_biz_no: str = None,
        speed: int = None,
        start_time: str = None,
    ):
        self.expire_time = expire_time
        self.outer_biz_no = outer_biz_no
        self.speed = speed
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expire_time is not None:
            result['expireTime'] = self.expire_time
        if self.outer_biz_no is not None:
            result['outerBizNo'] = self.outer_biz_no
        if self.speed is not None:
            result['speed'] = self.speed
        if self.start_time is not None:
            result['startTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('expireTime') is not None:
            self.expire_time = m.get('expireTime')
        if m.get('outerBizNo') is not None:
            self.outer_biz_no = m.get('outerBizNo')
        if m.get('speed') is not None:
            self.speed = m.get('speed')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        return self


class CancelByMsgIdRequest(TeaModel):
    def __init__(
        self,
        msg_id: str = None,
    ):
        self.msg_id = msg_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.msg_id is not None:
            result['MsgId'] = self.msg_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')
        return self


class CancelByMsgIdResponseBodyData(TeaModel):
    def __init__(
        self,
        msg_id: str = None,
    ):
        self.msg_id = msg_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.msg_id is not None:
            result['MsgId'] = self.msg_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')
        return self


class CancelByMsgIdResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CancelByMsgIdResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = CancelByMsgIdResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CancelByMsgIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CancelByMsgIdResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CancelByMsgIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryMsgStatRequest(TeaModel):
    def __init__(
        self,
        msg_id: str = None,
    ):
        self.msg_id = msg_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.msg_id is not None:
            result['MsgId'] = self.msg_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')
        return self


class QueryMsgStatResponseBodyData(TeaModel):
    def __init__(
        self,
        accept: int = None,
        arrive: int = None,
        close_push: int = None,
        dismiss: int = None,
        msg_id: str = None,
        open: int = None,
        sent: int = None,
        status: int = None,
    ):
        self.accept = accept
        self.arrive = arrive
        self.close_push = close_push
        self.dismiss = dismiss
        self.msg_id = msg_id
        self.open = open
        self.sent = sent
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept is not None:
            result['Accept'] = self.accept
        if self.arrive is not None:
            result['Arrive'] = self.arrive
        if self.close_push is not None:
            result['ClosePush'] = self.close_push
        if self.dismiss is not None:
            result['Dismiss'] = self.dismiss
        if self.msg_id is not None:
            result['MsgId'] = self.msg_id
        if self.open is not None:
            result['Open'] = self.open
        if self.sent is not None:
            result['Sent'] = self.sent
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accept') is not None:
            self.accept = m.get('Accept')
        if m.get('Arrive') is not None:
            self.arrive = m.get('Arrive')
        if m.get('ClosePush') is not None:
            self.close_push = m.get('ClosePush')
        if m.get('Dismiss') is not None:
            self.dismiss = m.get('Dismiss')
        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')
        if m.get('Open') is not None:
            self.open = m.get('Open')
        if m.get('Sent') is not None:
            self.sent = m.get('Sent')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class QueryMsgStatResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryMsgStatResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = QueryMsgStatResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryMsgStatResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryMsgStatResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryMsgStatResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendByAliasRequest(TeaModel):
    def __init__(
        self,
        alias: str = None,
        alias_type: str = None,
        android_payload: AndroidPayload = None,
        android_short_payload: AndroidShortPayload = None,
        channel_properties: ChannelProperties = None,
        description: str = None,
        ios_payload: IosPayload = None,
        policy: Policy = None,
        production_mode: bool = None,
        receipt_type: int = None,
        receipt_url: str = None,
        third_party_id: str = None,
        callback_params: str = None,
    ):
        # This parameter is required.
        self.alias = alias
        self.alias_type = alias_type
        self.android_payload = android_payload
        self.android_short_payload = android_short_payload
        self.channel_properties = channel_properties
        self.description = description
        self.ios_payload = ios_payload
        self.policy = policy
        self.production_mode = production_mode
        self.receipt_type = receipt_type
        self.receipt_url = receipt_url
        self.third_party_id = third_party_id
        self.callback_params = callback_params

    def validate(self):
        if self.android_payload:
            self.android_payload.validate()
        if self.android_short_payload:
            self.android_short_payload.validate()
        if self.channel_properties:
            self.channel_properties.validate()
        if self.ios_payload:
            self.ios_payload.validate()
        if self.policy:
            self.policy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias is not None:
            result['Alias'] = self.alias
        if self.alias_type is not None:
            result['AliasType'] = self.alias_type
        if self.android_payload is not None:
            result['AndroidPayload'] = self.android_payload.to_map()
        if self.android_short_payload is not None:
            result['AndroidShortPayload'] = self.android_short_payload.to_map()
        if self.channel_properties is not None:
            result['ChannelProperties'] = self.channel_properties.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.ios_payload is not None:
            result['IosPayload'] = self.ios_payload.to_map()
        if self.policy is not None:
            result['Policy'] = self.policy.to_map()
        if self.production_mode is not None:
            result['ProductionMode'] = self.production_mode
        if self.receipt_type is not None:
            result['ReceiptType'] = self.receipt_type
        if self.receipt_url is not None:
            result['ReceiptUrl'] = self.receipt_url
        if self.third_party_id is not None:
            result['ThirdPartyId'] = self.third_party_id
        if self.callback_params is not None:
            result['callbackParams'] = self.callback_params
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')
        if m.get('AliasType') is not None:
            self.alias_type = m.get('AliasType')
        if m.get('AndroidPayload') is not None:
            temp_model = AndroidPayload()
            self.android_payload = temp_model.from_map(m['AndroidPayload'])
        if m.get('AndroidShortPayload') is not None:
            temp_model = AndroidShortPayload()
            self.android_short_payload = temp_model.from_map(m['AndroidShortPayload'])
        if m.get('ChannelProperties') is not None:
            temp_model = ChannelProperties()
            self.channel_properties = temp_model.from_map(m['ChannelProperties'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('IosPayload') is not None:
            temp_model = IosPayload()
            self.ios_payload = temp_model.from_map(m['IosPayload'])
        if m.get('Policy') is not None:
            temp_model = Policy()
            self.policy = temp_model.from_map(m['Policy'])
        if m.get('ProductionMode') is not None:
            self.production_mode = m.get('ProductionMode')
        if m.get('ReceiptType') is not None:
            self.receipt_type = m.get('ReceiptType')
        if m.get('ReceiptUrl') is not None:
            self.receipt_url = m.get('ReceiptUrl')
        if m.get('ThirdPartyId') is not None:
            self.third_party_id = m.get('ThirdPartyId')
        if m.get('callbackParams') is not None:
            self.callback_params = m.get('callbackParams')
        return self


class SendByAliasShrinkRequest(TeaModel):
    def __init__(
        self,
        alias: str = None,
        alias_type: str = None,
        android_payload_shrink: str = None,
        android_short_payload_shrink: str = None,
        channel_properties_shrink: str = None,
        description: str = None,
        ios_payload_shrink: str = None,
        policy_shrink: str = None,
        production_mode: bool = None,
        receipt_type: int = None,
        receipt_url: str = None,
        third_party_id: str = None,
        callback_params: str = None,
    ):
        # This parameter is required.
        self.alias = alias
        self.alias_type = alias_type
        self.android_payload_shrink = android_payload_shrink
        self.android_short_payload_shrink = android_short_payload_shrink
        self.channel_properties_shrink = channel_properties_shrink
        self.description = description
        self.ios_payload_shrink = ios_payload_shrink
        self.policy_shrink = policy_shrink
        self.production_mode = production_mode
        self.receipt_type = receipt_type
        self.receipt_url = receipt_url
        self.third_party_id = third_party_id
        self.callback_params = callback_params

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias is not None:
            result['Alias'] = self.alias
        if self.alias_type is not None:
            result['AliasType'] = self.alias_type
        if self.android_payload_shrink is not None:
            result['AndroidPayload'] = self.android_payload_shrink
        if self.android_short_payload_shrink is not None:
            result['AndroidShortPayload'] = self.android_short_payload_shrink
        if self.channel_properties_shrink is not None:
            result['ChannelProperties'] = self.channel_properties_shrink
        if self.description is not None:
            result['Description'] = self.description
        if self.ios_payload_shrink is not None:
            result['IosPayload'] = self.ios_payload_shrink
        if self.policy_shrink is not None:
            result['Policy'] = self.policy_shrink
        if self.production_mode is not None:
            result['ProductionMode'] = self.production_mode
        if self.receipt_type is not None:
            result['ReceiptType'] = self.receipt_type
        if self.receipt_url is not None:
            result['ReceiptUrl'] = self.receipt_url
        if self.third_party_id is not None:
            result['ThirdPartyId'] = self.third_party_id
        if self.callback_params is not None:
            result['callbackParams'] = self.callback_params
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')
        if m.get('AliasType') is not None:
            self.alias_type = m.get('AliasType')
        if m.get('AndroidPayload') is not None:
            self.android_payload_shrink = m.get('AndroidPayload')
        if m.get('AndroidShortPayload') is not None:
            self.android_short_payload_shrink = m.get('AndroidShortPayload')
        if m.get('ChannelProperties') is not None:
            self.channel_properties_shrink = m.get('ChannelProperties')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('IosPayload') is not None:
            self.ios_payload_shrink = m.get('IosPayload')
        if m.get('Policy') is not None:
            self.policy_shrink = m.get('Policy')
        if m.get('ProductionMode') is not None:
            self.production_mode = m.get('ProductionMode')
        if m.get('ReceiptType') is not None:
            self.receipt_type = m.get('ReceiptType')
        if m.get('ReceiptUrl') is not None:
            self.receipt_url = m.get('ReceiptUrl')
        if m.get('ThirdPartyId') is not None:
            self.third_party_id = m.get('ThirdPartyId')
        if m.get('callbackParams') is not None:
            self.callback_params = m.get('callbackParams')
        return self


class SendByAliasResponseBodyData(TeaModel):
    def __init__(
        self,
        msg_id: str = None,
    ):
        self.msg_id = msg_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.msg_id is not None:
            result['MsgId'] = self.msg_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')
        return self


class SendByAliasResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: SendByAliasResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = SendByAliasResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SendByAliasResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SendByAliasResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SendByAliasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendByAliasFileIdRequest(TeaModel):
    def __init__(
        self,
        alias_type: str = None,
        android_payload: AndroidPayload = None,
        android_short_payload: AndroidShortPayload = None,
        channel_properties: ChannelProperties = None,
        description: str = None,
        file_id: str = None,
        ios_payload: IosPayload = None,
        policy: Policy = None,
        production_mode: bool = None,
        receipt_type: int = None,
        receipt_url: str = None,
        third_party_id: str = None,
        callback_params: str = None,
    ):
        self.alias_type = alias_type
        self.android_payload = android_payload
        self.android_short_payload = android_short_payload
        self.channel_properties = channel_properties
        self.description = description
        # This parameter is required.
        self.file_id = file_id
        self.ios_payload = ios_payload
        self.policy = policy
        self.production_mode = production_mode
        self.receipt_type = receipt_type
        self.receipt_url = receipt_url
        self.third_party_id = third_party_id
        self.callback_params = callback_params

    def validate(self):
        if self.android_payload:
            self.android_payload.validate()
        if self.android_short_payload:
            self.android_short_payload.validate()
        if self.channel_properties:
            self.channel_properties.validate()
        if self.ios_payload:
            self.ios_payload.validate()
        if self.policy:
            self.policy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias_type is not None:
            result['AliasType'] = self.alias_type
        if self.android_payload is not None:
            result['AndroidPayload'] = self.android_payload.to_map()
        if self.android_short_payload is not None:
            result['AndroidShortPayload'] = self.android_short_payload.to_map()
        if self.channel_properties is not None:
            result['ChannelProperties'] = self.channel_properties.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.ios_payload is not None:
            result['IosPayload'] = self.ios_payload.to_map()
        if self.policy is not None:
            result['Policy'] = self.policy.to_map()
        if self.production_mode is not None:
            result['ProductionMode'] = self.production_mode
        if self.receipt_type is not None:
            result['ReceiptType'] = self.receipt_type
        if self.receipt_url is not None:
            result['ReceiptUrl'] = self.receipt_url
        if self.third_party_id is not None:
            result['ThirdPartyId'] = self.third_party_id
        if self.callback_params is not None:
            result['callbackParams'] = self.callback_params
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliasType') is not None:
            self.alias_type = m.get('AliasType')
        if m.get('AndroidPayload') is not None:
            temp_model = AndroidPayload()
            self.android_payload = temp_model.from_map(m['AndroidPayload'])
        if m.get('AndroidShortPayload') is not None:
            temp_model = AndroidShortPayload()
            self.android_short_payload = temp_model.from_map(m['AndroidShortPayload'])
        if m.get('ChannelProperties') is not None:
            temp_model = ChannelProperties()
            self.channel_properties = temp_model.from_map(m['ChannelProperties'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('IosPayload') is not None:
            temp_model = IosPayload()
            self.ios_payload = temp_model.from_map(m['IosPayload'])
        if m.get('Policy') is not None:
            temp_model = Policy()
            self.policy = temp_model.from_map(m['Policy'])
        if m.get('ProductionMode') is not None:
            self.production_mode = m.get('ProductionMode')
        if m.get('ReceiptType') is not None:
            self.receipt_type = m.get('ReceiptType')
        if m.get('ReceiptUrl') is not None:
            self.receipt_url = m.get('ReceiptUrl')
        if m.get('ThirdPartyId') is not None:
            self.third_party_id = m.get('ThirdPartyId')
        if m.get('callbackParams') is not None:
            self.callback_params = m.get('callbackParams')
        return self


class SendByAliasFileIdShrinkRequest(TeaModel):
    def __init__(
        self,
        alias_type: str = None,
        android_payload_shrink: str = None,
        android_short_payload_shrink: str = None,
        channel_properties_shrink: str = None,
        description: str = None,
        file_id: str = None,
        ios_payload_shrink: str = None,
        policy_shrink: str = None,
        production_mode: bool = None,
        receipt_type: int = None,
        receipt_url: str = None,
        third_party_id: str = None,
        callback_params: str = None,
    ):
        self.alias_type = alias_type
        self.android_payload_shrink = android_payload_shrink
        self.android_short_payload_shrink = android_short_payload_shrink
        self.channel_properties_shrink = channel_properties_shrink
        self.description = description
        # This parameter is required.
        self.file_id = file_id
        self.ios_payload_shrink = ios_payload_shrink
        self.policy_shrink = policy_shrink
        self.production_mode = production_mode
        self.receipt_type = receipt_type
        self.receipt_url = receipt_url
        self.third_party_id = third_party_id
        self.callback_params = callback_params

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias_type is not None:
            result['AliasType'] = self.alias_type
        if self.android_payload_shrink is not None:
            result['AndroidPayload'] = self.android_payload_shrink
        if self.android_short_payload_shrink is not None:
            result['AndroidShortPayload'] = self.android_short_payload_shrink
        if self.channel_properties_shrink is not None:
            result['ChannelProperties'] = self.channel_properties_shrink
        if self.description is not None:
            result['Description'] = self.description
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.ios_payload_shrink is not None:
            result['IosPayload'] = self.ios_payload_shrink
        if self.policy_shrink is not None:
            result['Policy'] = self.policy_shrink
        if self.production_mode is not None:
            result['ProductionMode'] = self.production_mode
        if self.receipt_type is not None:
            result['ReceiptType'] = self.receipt_type
        if self.receipt_url is not None:
            result['ReceiptUrl'] = self.receipt_url
        if self.third_party_id is not None:
            result['ThirdPartyId'] = self.third_party_id
        if self.callback_params is not None:
            result['callbackParams'] = self.callback_params
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliasType') is not None:
            self.alias_type = m.get('AliasType')
        if m.get('AndroidPayload') is not None:
            self.android_payload_shrink = m.get('AndroidPayload')
        if m.get('AndroidShortPayload') is not None:
            self.android_short_payload_shrink = m.get('AndroidShortPayload')
        if m.get('ChannelProperties') is not None:
            self.channel_properties_shrink = m.get('ChannelProperties')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('IosPayload') is not None:
            self.ios_payload_shrink = m.get('IosPayload')
        if m.get('Policy') is not None:
            self.policy_shrink = m.get('Policy')
        if m.get('ProductionMode') is not None:
            self.production_mode = m.get('ProductionMode')
        if m.get('ReceiptType') is not None:
            self.receipt_type = m.get('ReceiptType')
        if m.get('ReceiptUrl') is not None:
            self.receipt_url = m.get('ReceiptUrl')
        if m.get('ThirdPartyId') is not None:
            self.third_party_id = m.get('ThirdPartyId')
        if m.get('callbackParams') is not None:
            self.callback_params = m.get('callbackParams')
        return self


class SendByAliasFileIdResponseBodyData(TeaModel):
    def __init__(
        self,
        msg_id: str = None,
    ):
        self.msg_id = msg_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.msg_id is not None:
            result['MsgId'] = self.msg_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')
        return self


class SendByAliasFileIdResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: SendByAliasFileIdResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = SendByAliasFileIdResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SendByAliasFileIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SendByAliasFileIdResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SendByAliasFileIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendByAppRequest(TeaModel):
    def __init__(
        self,
        android_payload: AndroidPayload = None,
        android_short_payload: AndroidShortPayload = None,
        channel_properties: ChannelProperties = None,
        description: str = None,
        ios_payload: IosPayload = None,
        policy: Policy = None,
        production_mode: bool = None,
        receipt_type: int = None,
        receipt_url: str = None,
        third_party_id: str = None,
        callback_params: str = None,
    ):
        self.android_payload = android_payload
        self.android_short_payload = android_short_payload
        self.channel_properties = channel_properties
        self.description = description
        self.ios_payload = ios_payload
        self.policy = policy
        self.production_mode = production_mode
        self.receipt_type = receipt_type
        self.receipt_url = receipt_url
        self.third_party_id = third_party_id
        self.callback_params = callback_params

    def validate(self):
        if self.android_payload:
            self.android_payload.validate()
        if self.android_short_payload:
            self.android_short_payload.validate()
        if self.channel_properties:
            self.channel_properties.validate()
        if self.ios_payload:
            self.ios_payload.validate()
        if self.policy:
            self.policy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.android_payload is not None:
            result['AndroidPayload'] = self.android_payload.to_map()
        if self.android_short_payload is not None:
            result['AndroidShortPayload'] = self.android_short_payload.to_map()
        if self.channel_properties is not None:
            result['ChannelProperties'] = self.channel_properties.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.ios_payload is not None:
            result['IosPayload'] = self.ios_payload.to_map()
        if self.policy is not None:
            result['Policy'] = self.policy.to_map()
        if self.production_mode is not None:
            result['ProductionMode'] = self.production_mode
        if self.receipt_type is not None:
            result['ReceiptType'] = self.receipt_type
        if self.receipt_url is not None:
            result['ReceiptUrl'] = self.receipt_url
        if self.third_party_id is not None:
            result['ThirdPartyId'] = self.third_party_id
        if self.callback_params is not None:
            result['callbackParams'] = self.callback_params
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidPayload') is not None:
            temp_model = AndroidPayload()
            self.android_payload = temp_model.from_map(m['AndroidPayload'])
        if m.get('AndroidShortPayload') is not None:
            temp_model = AndroidShortPayload()
            self.android_short_payload = temp_model.from_map(m['AndroidShortPayload'])
        if m.get('ChannelProperties') is not None:
            temp_model = ChannelProperties()
            self.channel_properties = temp_model.from_map(m['ChannelProperties'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('IosPayload') is not None:
            temp_model = IosPayload()
            self.ios_payload = temp_model.from_map(m['IosPayload'])
        if m.get('Policy') is not None:
            temp_model = Policy()
            self.policy = temp_model.from_map(m['Policy'])
        if m.get('ProductionMode') is not None:
            self.production_mode = m.get('ProductionMode')
        if m.get('ReceiptType') is not None:
            self.receipt_type = m.get('ReceiptType')
        if m.get('ReceiptUrl') is not None:
            self.receipt_url = m.get('ReceiptUrl')
        if m.get('ThirdPartyId') is not None:
            self.third_party_id = m.get('ThirdPartyId')
        if m.get('callbackParams') is not None:
            self.callback_params = m.get('callbackParams')
        return self


class SendByAppShrinkRequest(TeaModel):
    def __init__(
        self,
        android_payload_shrink: str = None,
        android_short_payload_shrink: str = None,
        channel_properties_shrink: str = None,
        description: str = None,
        ios_payload_shrink: str = None,
        policy_shrink: str = None,
        production_mode: bool = None,
        receipt_type: int = None,
        receipt_url: str = None,
        third_party_id: str = None,
        callback_params: str = None,
    ):
        self.android_payload_shrink = android_payload_shrink
        self.android_short_payload_shrink = android_short_payload_shrink
        self.channel_properties_shrink = channel_properties_shrink
        self.description = description
        self.ios_payload_shrink = ios_payload_shrink
        self.policy_shrink = policy_shrink
        self.production_mode = production_mode
        self.receipt_type = receipt_type
        self.receipt_url = receipt_url
        self.third_party_id = third_party_id
        self.callback_params = callback_params

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.android_payload_shrink is not None:
            result['AndroidPayload'] = self.android_payload_shrink
        if self.android_short_payload_shrink is not None:
            result['AndroidShortPayload'] = self.android_short_payload_shrink
        if self.channel_properties_shrink is not None:
            result['ChannelProperties'] = self.channel_properties_shrink
        if self.description is not None:
            result['Description'] = self.description
        if self.ios_payload_shrink is not None:
            result['IosPayload'] = self.ios_payload_shrink
        if self.policy_shrink is not None:
            result['Policy'] = self.policy_shrink
        if self.production_mode is not None:
            result['ProductionMode'] = self.production_mode
        if self.receipt_type is not None:
            result['ReceiptType'] = self.receipt_type
        if self.receipt_url is not None:
            result['ReceiptUrl'] = self.receipt_url
        if self.third_party_id is not None:
            result['ThirdPartyId'] = self.third_party_id
        if self.callback_params is not None:
            result['callbackParams'] = self.callback_params
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidPayload') is not None:
            self.android_payload_shrink = m.get('AndroidPayload')
        if m.get('AndroidShortPayload') is not None:
            self.android_short_payload_shrink = m.get('AndroidShortPayload')
        if m.get('ChannelProperties') is not None:
            self.channel_properties_shrink = m.get('ChannelProperties')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('IosPayload') is not None:
            self.ios_payload_shrink = m.get('IosPayload')
        if m.get('Policy') is not None:
            self.policy_shrink = m.get('Policy')
        if m.get('ProductionMode') is not None:
            self.production_mode = m.get('ProductionMode')
        if m.get('ReceiptType') is not None:
            self.receipt_type = m.get('ReceiptType')
        if m.get('ReceiptUrl') is not None:
            self.receipt_url = m.get('ReceiptUrl')
        if m.get('ThirdPartyId') is not None:
            self.third_party_id = m.get('ThirdPartyId')
        if m.get('callbackParams') is not None:
            self.callback_params = m.get('callbackParams')
        return self


class SendByAppResponseBodyData(TeaModel):
    def __init__(
        self,
        msg_id: str = None,
    ):
        self.msg_id = msg_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.msg_id is not None:
            result['MsgId'] = self.msg_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')
        return self


class SendByAppResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: SendByAppResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = SendByAppResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SendByAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SendByAppResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SendByAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendByDeviceRequest(TeaModel):
    def __init__(
        self,
        android_payload: AndroidPayload = None,
        android_short_payload: AndroidShortPayload = None,
        channel_properties: ChannelProperties = None,
        description: str = None,
        device_tokens: str = None,
        ios_payload: IosPayload = None,
        policy: Policy = None,
        production_mode: bool = None,
        receipt_type: int = None,
        receipt_url: str = None,
        third_party_id: str = None,
        callback_params: str = None,
    ):
        self.android_payload = android_payload
        self.android_short_payload = android_short_payload
        self.channel_properties = channel_properties
        self.description = description
        # This parameter is required.
        self.device_tokens = device_tokens
        self.ios_payload = ios_payload
        self.policy = policy
        self.production_mode = production_mode
        self.receipt_type = receipt_type
        self.receipt_url = receipt_url
        self.third_party_id = third_party_id
        self.callback_params = callback_params

    def validate(self):
        if self.android_payload:
            self.android_payload.validate()
        if self.android_short_payload:
            self.android_short_payload.validate()
        if self.channel_properties:
            self.channel_properties.validate()
        if self.ios_payload:
            self.ios_payload.validate()
        if self.policy:
            self.policy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.android_payload is not None:
            result['AndroidPayload'] = self.android_payload.to_map()
        if self.android_short_payload is not None:
            result['AndroidShortPayload'] = self.android_short_payload.to_map()
        if self.channel_properties is not None:
            result['ChannelProperties'] = self.channel_properties.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.device_tokens is not None:
            result['DeviceTokens'] = self.device_tokens
        if self.ios_payload is not None:
            result['IosPayload'] = self.ios_payload.to_map()
        if self.policy is not None:
            result['Policy'] = self.policy.to_map()
        if self.production_mode is not None:
            result['ProductionMode'] = self.production_mode
        if self.receipt_type is not None:
            result['ReceiptType'] = self.receipt_type
        if self.receipt_url is not None:
            result['ReceiptUrl'] = self.receipt_url
        if self.third_party_id is not None:
            result['ThirdPartyId'] = self.third_party_id
        if self.callback_params is not None:
            result['callbackParams'] = self.callback_params
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidPayload') is not None:
            temp_model = AndroidPayload()
            self.android_payload = temp_model.from_map(m['AndroidPayload'])
        if m.get('AndroidShortPayload') is not None:
            temp_model = AndroidShortPayload()
            self.android_short_payload = temp_model.from_map(m['AndroidShortPayload'])
        if m.get('ChannelProperties') is not None:
            temp_model = ChannelProperties()
            self.channel_properties = temp_model.from_map(m['ChannelProperties'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DeviceTokens') is not None:
            self.device_tokens = m.get('DeviceTokens')
        if m.get('IosPayload') is not None:
            temp_model = IosPayload()
            self.ios_payload = temp_model.from_map(m['IosPayload'])
        if m.get('Policy') is not None:
            temp_model = Policy()
            self.policy = temp_model.from_map(m['Policy'])
        if m.get('ProductionMode') is not None:
            self.production_mode = m.get('ProductionMode')
        if m.get('ReceiptType') is not None:
            self.receipt_type = m.get('ReceiptType')
        if m.get('ReceiptUrl') is not None:
            self.receipt_url = m.get('ReceiptUrl')
        if m.get('ThirdPartyId') is not None:
            self.third_party_id = m.get('ThirdPartyId')
        if m.get('callbackParams') is not None:
            self.callback_params = m.get('callbackParams')
        return self


class SendByDeviceShrinkRequest(TeaModel):
    def __init__(
        self,
        android_payload_shrink: str = None,
        android_short_payload_shrink: str = None,
        channel_properties_shrink: str = None,
        description: str = None,
        device_tokens: str = None,
        ios_payload_shrink: str = None,
        policy_shrink: str = None,
        production_mode: bool = None,
        receipt_type: int = None,
        receipt_url: str = None,
        third_party_id: str = None,
        callback_params: str = None,
    ):
        self.android_payload_shrink = android_payload_shrink
        self.android_short_payload_shrink = android_short_payload_shrink
        self.channel_properties_shrink = channel_properties_shrink
        self.description = description
        # This parameter is required.
        self.device_tokens = device_tokens
        self.ios_payload_shrink = ios_payload_shrink
        self.policy_shrink = policy_shrink
        self.production_mode = production_mode
        self.receipt_type = receipt_type
        self.receipt_url = receipt_url
        self.third_party_id = third_party_id
        self.callback_params = callback_params

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.android_payload_shrink is not None:
            result['AndroidPayload'] = self.android_payload_shrink
        if self.android_short_payload_shrink is not None:
            result['AndroidShortPayload'] = self.android_short_payload_shrink
        if self.channel_properties_shrink is not None:
            result['ChannelProperties'] = self.channel_properties_shrink
        if self.description is not None:
            result['Description'] = self.description
        if self.device_tokens is not None:
            result['DeviceTokens'] = self.device_tokens
        if self.ios_payload_shrink is not None:
            result['IosPayload'] = self.ios_payload_shrink
        if self.policy_shrink is not None:
            result['Policy'] = self.policy_shrink
        if self.production_mode is not None:
            result['ProductionMode'] = self.production_mode
        if self.receipt_type is not None:
            result['ReceiptType'] = self.receipt_type
        if self.receipt_url is not None:
            result['ReceiptUrl'] = self.receipt_url
        if self.third_party_id is not None:
            result['ThirdPartyId'] = self.third_party_id
        if self.callback_params is not None:
            result['callbackParams'] = self.callback_params
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidPayload') is not None:
            self.android_payload_shrink = m.get('AndroidPayload')
        if m.get('AndroidShortPayload') is not None:
            self.android_short_payload_shrink = m.get('AndroidShortPayload')
        if m.get('ChannelProperties') is not None:
            self.channel_properties_shrink = m.get('ChannelProperties')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DeviceTokens') is not None:
            self.device_tokens = m.get('DeviceTokens')
        if m.get('IosPayload') is not None:
            self.ios_payload_shrink = m.get('IosPayload')
        if m.get('Policy') is not None:
            self.policy_shrink = m.get('Policy')
        if m.get('ProductionMode') is not None:
            self.production_mode = m.get('ProductionMode')
        if m.get('ReceiptType') is not None:
            self.receipt_type = m.get('ReceiptType')
        if m.get('ReceiptUrl') is not None:
            self.receipt_url = m.get('ReceiptUrl')
        if m.get('ThirdPartyId') is not None:
            self.third_party_id = m.get('ThirdPartyId')
        if m.get('callbackParams') is not None:
            self.callback_params = m.get('callbackParams')
        return self


class SendByDeviceResponseBodyData(TeaModel):
    def __init__(
        self,
        msg_id: str = None,
    ):
        self.msg_id = msg_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.msg_id is not None:
            result['MsgId'] = self.msg_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')
        return self


class SendByDeviceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: SendByDeviceResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = SendByDeviceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SendByDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SendByDeviceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SendByDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendByDeviceFileIdRequest(TeaModel):
    def __init__(
        self,
        android_payload: AndroidPayload = None,
        android_short_payload: AndroidShortPayload = None,
        channel_properties: ChannelProperties = None,
        description: str = None,
        file_id: str = None,
        ios_payload: IosPayload = None,
        policy: Policy = None,
        production_mode: bool = None,
        receipt_type: int = None,
        receipt_url: str = None,
        third_party_id: str = None,
        callback_params: str = None,
    ):
        self.android_payload = android_payload
        self.android_short_payload = android_short_payload
        self.channel_properties = channel_properties
        self.description = description
        # This parameter is required.
        self.file_id = file_id
        self.ios_payload = ios_payload
        self.policy = policy
        self.production_mode = production_mode
        self.receipt_type = receipt_type
        self.receipt_url = receipt_url
        self.third_party_id = third_party_id
        self.callback_params = callback_params

    def validate(self):
        if self.android_payload:
            self.android_payload.validate()
        if self.android_short_payload:
            self.android_short_payload.validate()
        if self.channel_properties:
            self.channel_properties.validate()
        if self.ios_payload:
            self.ios_payload.validate()
        if self.policy:
            self.policy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.android_payload is not None:
            result['AndroidPayload'] = self.android_payload.to_map()
        if self.android_short_payload is not None:
            result['AndroidShortPayload'] = self.android_short_payload.to_map()
        if self.channel_properties is not None:
            result['ChannelProperties'] = self.channel_properties.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.ios_payload is not None:
            result['IosPayload'] = self.ios_payload.to_map()
        if self.policy is not None:
            result['Policy'] = self.policy.to_map()
        if self.production_mode is not None:
            result['ProductionMode'] = self.production_mode
        if self.receipt_type is not None:
            result['ReceiptType'] = self.receipt_type
        if self.receipt_url is not None:
            result['ReceiptUrl'] = self.receipt_url
        if self.third_party_id is not None:
            result['ThirdPartyId'] = self.third_party_id
        if self.callback_params is not None:
            result['callbackParams'] = self.callback_params
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidPayload') is not None:
            temp_model = AndroidPayload()
            self.android_payload = temp_model.from_map(m['AndroidPayload'])
        if m.get('AndroidShortPayload') is not None:
            temp_model = AndroidShortPayload()
            self.android_short_payload = temp_model.from_map(m['AndroidShortPayload'])
        if m.get('ChannelProperties') is not None:
            temp_model = ChannelProperties()
            self.channel_properties = temp_model.from_map(m['ChannelProperties'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('IosPayload') is not None:
            temp_model = IosPayload()
            self.ios_payload = temp_model.from_map(m['IosPayload'])
        if m.get('Policy') is not None:
            temp_model = Policy()
            self.policy = temp_model.from_map(m['Policy'])
        if m.get('ProductionMode') is not None:
            self.production_mode = m.get('ProductionMode')
        if m.get('ReceiptType') is not None:
            self.receipt_type = m.get('ReceiptType')
        if m.get('ReceiptUrl') is not None:
            self.receipt_url = m.get('ReceiptUrl')
        if m.get('ThirdPartyId') is not None:
            self.third_party_id = m.get('ThirdPartyId')
        if m.get('callbackParams') is not None:
            self.callback_params = m.get('callbackParams')
        return self


class SendByDeviceFileIdShrinkRequest(TeaModel):
    def __init__(
        self,
        android_payload_shrink: str = None,
        android_short_payload_shrink: str = None,
        channel_properties_shrink: str = None,
        description: str = None,
        file_id: str = None,
        ios_payload_shrink: str = None,
        policy_shrink: str = None,
        production_mode: bool = None,
        receipt_type: int = None,
        receipt_url: str = None,
        third_party_id: str = None,
        callback_params: str = None,
    ):
        self.android_payload_shrink = android_payload_shrink
        self.android_short_payload_shrink = android_short_payload_shrink
        self.channel_properties_shrink = channel_properties_shrink
        self.description = description
        # This parameter is required.
        self.file_id = file_id
        self.ios_payload_shrink = ios_payload_shrink
        self.policy_shrink = policy_shrink
        self.production_mode = production_mode
        self.receipt_type = receipt_type
        self.receipt_url = receipt_url
        self.third_party_id = third_party_id
        self.callback_params = callback_params

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.android_payload_shrink is not None:
            result['AndroidPayload'] = self.android_payload_shrink
        if self.android_short_payload_shrink is not None:
            result['AndroidShortPayload'] = self.android_short_payload_shrink
        if self.channel_properties_shrink is not None:
            result['ChannelProperties'] = self.channel_properties_shrink
        if self.description is not None:
            result['Description'] = self.description
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.ios_payload_shrink is not None:
            result['IosPayload'] = self.ios_payload_shrink
        if self.policy_shrink is not None:
            result['Policy'] = self.policy_shrink
        if self.production_mode is not None:
            result['ProductionMode'] = self.production_mode
        if self.receipt_type is not None:
            result['ReceiptType'] = self.receipt_type
        if self.receipt_url is not None:
            result['ReceiptUrl'] = self.receipt_url
        if self.third_party_id is not None:
            result['ThirdPartyId'] = self.third_party_id
        if self.callback_params is not None:
            result['callbackParams'] = self.callback_params
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidPayload') is not None:
            self.android_payload_shrink = m.get('AndroidPayload')
        if m.get('AndroidShortPayload') is not None:
            self.android_short_payload_shrink = m.get('AndroidShortPayload')
        if m.get('ChannelProperties') is not None:
            self.channel_properties_shrink = m.get('ChannelProperties')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('IosPayload') is not None:
            self.ios_payload_shrink = m.get('IosPayload')
        if m.get('Policy') is not None:
            self.policy_shrink = m.get('Policy')
        if m.get('ProductionMode') is not None:
            self.production_mode = m.get('ProductionMode')
        if m.get('ReceiptType') is not None:
            self.receipt_type = m.get('ReceiptType')
        if m.get('ReceiptUrl') is not None:
            self.receipt_url = m.get('ReceiptUrl')
        if m.get('ThirdPartyId') is not None:
            self.third_party_id = m.get('ThirdPartyId')
        if m.get('callbackParams') is not None:
            self.callback_params = m.get('callbackParams')
        return self


class SendByDeviceFileIdResponseBodyData(TeaModel):
    def __init__(
        self,
        msg_id: str = None,
    ):
        self.msg_id = msg_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.msg_id is not None:
            result['MsgId'] = self.msg_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')
        return self


class SendByDeviceFileIdResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: SendByDeviceFileIdResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = SendByDeviceFileIdResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SendByDeviceFileIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SendByDeviceFileIdResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SendByDeviceFileIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendByFilterRequest(TeaModel):
    def __init__(
        self,
        android_payload: AndroidPayload = None,
        android_short_payload: AndroidShortPayload = None,
        channel_properties: ChannelProperties = None,
        description: str = None,
        filter: str = None,
        ios_payload: IosPayload = None,
        policy: Policy = None,
        production_mode: bool = None,
        receipt_type: int = None,
        receipt_url: str = None,
        third_party_id: str = None,
        callback_params: str = None,
    ):
        self.android_payload = android_payload
        self.android_short_payload = android_short_payload
        self.channel_properties = channel_properties
        self.description = description
        self.filter = filter
        self.ios_payload = ios_payload
        self.policy = policy
        self.production_mode = production_mode
        self.receipt_type = receipt_type
        self.receipt_url = receipt_url
        self.third_party_id = third_party_id
        self.callback_params = callback_params

    def validate(self):
        if self.android_payload:
            self.android_payload.validate()
        if self.android_short_payload:
            self.android_short_payload.validate()
        if self.channel_properties:
            self.channel_properties.validate()
        if self.ios_payload:
            self.ios_payload.validate()
        if self.policy:
            self.policy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.android_payload is not None:
            result['AndroidPayload'] = self.android_payload.to_map()
        if self.android_short_payload is not None:
            result['AndroidShortPayload'] = self.android_short_payload.to_map()
        if self.channel_properties is not None:
            result['ChannelProperties'] = self.channel_properties.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.ios_payload is not None:
            result['IosPayload'] = self.ios_payload.to_map()
        if self.policy is not None:
            result['Policy'] = self.policy.to_map()
        if self.production_mode is not None:
            result['ProductionMode'] = self.production_mode
        if self.receipt_type is not None:
            result['ReceiptType'] = self.receipt_type
        if self.receipt_url is not None:
            result['ReceiptUrl'] = self.receipt_url
        if self.third_party_id is not None:
            result['ThirdPartyId'] = self.third_party_id
        if self.callback_params is not None:
            result['callbackParams'] = self.callback_params
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidPayload') is not None:
            temp_model = AndroidPayload()
            self.android_payload = temp_model.from_map(m['AndroidPayload'])
        if m.get('AndroidShortPayload') is not None:
            temp_model = AndroidShortPayload()
            self.android_short_payload = temp_model.from_map(m['AndroidShortPayload'])
        if m.get('ChannelProperties') is not None:
            temp_model = ChannelProperties()
            self.channel_properties = temp_model.from_map(m['ChannelProperties'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('IosPayload') is not None:
            temp_model = IosPayload()
            self.ios_payload = temp_model.from_map(m['IosPayload'])
        if m.get('Policy') is not None:
            temp_model = Policy()
            self.policy = temp_model.from_map(m['Policy'])
        if m.get('ProductionMode') is not None:
            self.production_mode = m.get('ProductionMode')
        if m.get('ReceiptType') is not None:
            self.receipt_type = m.get('ReceiptType')
        if m.get('ReceiptUrl') is not None:
            self.receipt_url = m.get('ReceiptUrl')
        if m.get('ThirdPartyId') is not None:
            self.third_party_id = m.get('ThirdPartyId')
        if m.get('callbackParams') is not None:
            self.callback_params = m.get('callbackParams')
        return self


class SendByFilterShrinkRequest(TeaModel):
    def __init__(
        self,
        android_payload_shrink: str = None,
        android_short_payload: AndroidShortPayload = None,
        channel_properties_shrink: str = None,
        description: str = None,
        filter: str = None,
        ios_payload_shrink: str = None,
        policy_shrink: str = None,
        production_mode: bool = None,
        receipt_type: int = None,
        receipt_url: str = None,
        third_party_id: str = None,
        callback_params: str = None,
    ):
        self.android_payload_shrink = android_payload_shrink
        self.android_short_payload = android_short_payload
        self.channel_properties_shrink = channel_properties_shrink
        self.description = description
        self.filter = filter
        self.ios_payload_shrink = ios_payload_shrink
        self.policy_shrink = policy_shrink
        self.production_mode = production_mode
        self.receipt_type = receipt_type
        self.receipt_url = receipt_url
        self.third_party_id = third_party_id
        self.callback_params = callback_params

    def validate(self):
        if self.android_short_payload:
            self.android_short_payload.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.android_payload_shrink is not None:
            result['AndroidPayload'] = self.android_payload_shrink
        if self.android_short_payload is not None:
            result['AndroidShortPayload'] = self.android_short_payload.to_map()
        if self.channel_properties_shrink is not None:
            result['ChannelProperties'] = self.channel_properties_shrink
        if self.description is not None:
            result['Description'] = self.description
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.ios_payload_shrink is not None:
            result['IosPayload'] = self.ios_payload_shrink
        if self.policy_shrink is not None:
            result['Policy'] = self.policy_shrink
        if self.production_mode is not None:
            result['ProductionMode'] = self.production_mode
        if self.receipt_type is not None:
            result['ReceiptType'] = self.receipt_type
        if self.receipt_url is not None:
            result['ReceiptUrl'] = self.receipt_url
        if self.third_party_id is not None:
            result['ThirdPartyId'] = self.third_party_id
        if self.callback_params is not None:
            result['callbackParams'] = self.callback_params
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidPayload') is not None:
            self.android_payload_shrink = m.get('AndroidPayload')
        if m.get('AndroidShortPayload') is not None:
            temp_model = AndroidShortPayload()
            self.android_short_payload = temp_model.from_map(m['AndroidShortPayload'])
        if m.get('ChannelProperties') is not None:
            self.channel_properties_shrink = m.get('ChannelProperties')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('IosPayload') is not None:
            self.ios_payload_shrink = m.get('IosPayload')
        if m.get('Policy') is not None:
            self.policy_shrink = m.get('Policy')
        if m.get('ProductionMode') is not None:
            self.production_mode = m.get('ProductionMode')
        if m.get('ReceiptType') is not None:
            self.receipt_type = m.get('ReceiptType')
        if m.get('ReceiptUrl') is not None:
            self.receipt_url = m.get('ReceiptUrl')
        if m.get('ThirdPartyId') is not None:
            self.third_party_id = m.get('ThirdPartyId')
        if m.get('callbackParams') is not None:
            self.callback_params = m.get('callbackParams')
        return self


class SendByFilterResponseBodyData(TeaModel):
    def __init__(
        self,
        msg_id: str = None,
    ):
        self.msg_id = msg_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.msg_id is not None:
            result['MsgId'] = self.msg_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')
        return self


class SendByFilterResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: SendByFilterResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = SendByFilterResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SendByFilterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SendByFilterResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SendByFilterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UploadDeviceRequest(TeaModel):
    def __init__(
        self,
        device_tokens: str = None,
    ):
        self.device_tokens = device_tokens

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_tokens is not None:
            result['DeviceTokens'] = self.device_tokens
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceTokens') is not None:
            self.device_tokens = m.get('DeviceTokens')
        return self


class UploadDeviceResponseBodyData(TeaModel):
    def __init__(
        self,
        file_id: str = None,
    ):
        self.file_id = file_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_id is not None:
            result['FileId'] = self.file_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        return self


class UploadDeviceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: UploadDeviceResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = UploadDeviceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UploadDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UploadDeviceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UploadDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


