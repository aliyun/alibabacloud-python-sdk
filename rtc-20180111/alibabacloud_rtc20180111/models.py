# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class AddRecordTemplateRequestBackgrounds(TeaModel):
    def __init__(
        self,
        width: float = None,
        height: float = None,
        y: float = None,
        url: str = None,
        display: int = None,
        zorder: int = None,
        x: float = None,
    ):
        self.width = width
        self.height = height
        self.y = y
        self.url = url
        self.display = display
        self.zorder = zorder
        self.x = x

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        if self.y is not None:
            result['Y'] = self.y
        if self.url is not None:
            result['Url'] = self.url
        if self.display is not None:
            result['Display'] = self.display
        if self.zorder is not None:
            result['ZOrder'] = self.zorder
        if self.x is not None:
            result['X'] = self.x
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Display') is not None:
            self.display = m.get('Display')
        if m.get('ZOrder') is not None:
            self.zorder = m.get('ZOrder')
        if m.get('X') is not None:
            self.x = m.get('X')
        return self


class AddRecordTemplateRequestWatermarks(TeaModel):
    def __init__(
        self,
        alpha: float = None,
        width: float = None,
        height: float = None,
        y: float = None,
        url: str = None,
        display: int = None,
        zorder: int = None,
        x: float = None,
    ):
        self.alpha = alpha
        self.width = width
        self.height = height
        self.y = y
        self.url = url
        self.display = display
        self.zorder = zorder
        self.x = x

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.alpha is not None:
            result['Alpha'] = self.alpha
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        if self.y is not None:
            result['Y'] = self.y
        if self.url is not None:
            result['Url'] = self.url
        if self.display is not None:
            result['Display'] = self.display
        if self.zorder is not None:
            result['ZOrder'] = self.zorder
        if self.x is not None:
            result['X'] = self.x
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alpha') is not None:
            self.alpha = m.get('Alpha')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Display') is not None:
            self.display = m.get('Display')
        if m.get('ZOrder') is not None:
            self.zorder = m.get('ZOrder')
        if m.get('X') is not None:
            self.x = m.get('X')
        return self


class AddRecordTemplateRequestClockWidgets(TeaModel):
    def __init__(
        self,
        font_type: int = None,
        font_color: int = None,
        y: float = None,
        zorder: int = None,
        x: float = None,
        font_size: int = None,
    ):
        self.font_type = font_type
        self.font_color = font_color
        self.y = y
        self.zorder = zorder
        self.x = x
        self.font_size = font_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.font_type is not None:
            result['FontType'] = self.font_type
        if self.font_color is not None:
            result['FontColor'] = self.font_color
        if self.y is not None:
            result['Y'] = self.y
        if self.zorder is not None:
            result['ZOrder'] = self.zorder
        if self.x is not None:
            result['X'] = self.x
        if self.font_size is not None:
            result['FontSize'] = self.font_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FontType') is not None:
            self.font_type = m.get('FontType')
        if m.get('FontColor') is not None:
            self.font_color = m.get('FontColor')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        if m.get('ZOrder') is not None:
            self.zorder = m.get('ZOrder')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('FontSize') is not None:
            self.font_size = m.get('FontSize')
        return self


class AddRecordTemplateRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        show_log: str = None,
        app_id: str = None,
        name: str = None,
        task_profile: str = None,
        media_encode: int = None,
        background_color: int = None,
        oss_bucket: str = None,
        oss_file_prefix: str = None,
        file_split_interval: int = None,
        delay_stop_time: int = None,
        mns_queue: str = None,
        http_callback_url: str = None,
        layout_ids: List[int] = None,
        formats: List[str] = None,
        backgrounds: List[AddRecordTemplateRequestBackgrounds] = None,
        watermarks: List[AddRecordTemplateRequestWatermarks] = None,
        clock_widgets: List[AddRecordTemplateRequestClockWidgets] = None,
    ):
        self.owner_id = owner_id
        self.show_log = show_log
        self.app_id = app_id
        self.name = name
        self.task_profile = task_profile
        self.media_encode = media_encode
        self.background_color = background_color
        self.oss_bucket = oss_bucket
        self.oss_file_prefix = oss_file_prefix
        self.file_split_interval = file_split_interval
        self.delay_stop_time = delay_stop_time
        self.mns_queue = mns_queue
        self.http_callback_url = http_callback_url
        self.layout_ids = layout_ids
        self.formats = formats
        self.backgrounds = backgrounds
        self.watermarks = watermarks
        self.clock_widgets = clock_widgets

    def validate(self):
        if self.backgrounds:
            for k in self.backgrounds:
                if k:
                    k.validate()
        if self.watermarks:
            for k in self.watermarks:
                if k:
                    k.validate()
        if self.clock_widgets:
            for k in self.clock_widgets:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.show_log is not None:
            result['ShowLog'] = self.show_log
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.name is not None:
            result['Name'] = self.name
        if self.task_profile is not None:
            result['TaskProfile'] = self.task_profile
        if self.media_encode is not None:
            result['MediaEncode'] = self.media_encode
        if self.background_color is not None:
            result['BackgroundColor'] = self.background_color
        if self.oss_bucket is not None:
            result['OssBucket'] = self.oss_bucket
        if self.oss_file_prefix is not None:
            result['OssFilePrefix'] = self.oss_file_prefix
        if self.file_split_interval is not None:
            result['FileSplitInterval'] = self.file_split_interval
        if self.delay_stop_time is not None:
            result['DelayStopTime'] = self.delay_stop_time
        if self.mns_queue is not None:
            result['MnsQueue'] = self.mns_queue
        if self.http_callback_url is not None:
            result['HttpCallbackUrl'] = self.http_callback_url
        if self.layout_ids is not None:
            result['LayoutIds'] = self.layout_ids
        if self.formats is not None:
            result['Formats'] = self.formats
        result['Backgrounds'] = []
        if self.backgrounds is not None:
            for k in self.backgrounds:
                result['Backgrounds'].append(k.to_map() if k else None)
        result['Watermarks'] = []
        if self.watermarks is not None:
            for k in self.watermarks:
                result['Watermarks'].append(k.to_map() if k else None)
        result['ClockWidgets'] = []
        if self.clock_widgets is not None:
            for k in self.clock_widgets:
                result['ClockWidgets'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ShowLog') is not None:
            self.show_log = m.get('ShowLog')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TaskProfile') is not None:
            self.task_profile = m.get('TaskProfile')
        if m.get('MediaEncode') is not None:
            self.media_encode = m.get('MediaEncode')
        if m.get('BackgroundColor') is not None:
            self.background_color = m.get('BackgroundColor')
        if m.get('OssBucket') is not None:
            self.oss_bucket = m.get('OssBucket')
        if m.get('OssFilePrefix') is not None:
            self.oss_file_prefix = m.get('OssFilePrefix')
        if m.get('FileSplitInterval') is not None:
            self.file_split_interval = m.get('FileSplitInterval')
        if m.get('DelayStopTime') is not None:
            self.delay_stop_time = m.get('DelayStopTime')
        if m.get('MnsQueue') is not None:
            self.mns_queue = m.get('MnsQueue')
        if m.get('HttpCallbackUrl') is not None:
            self.http_callback_url = m.get('HttpCallbackUrl')
        if m.get('LayoutIds') is not None:
            self.layout_ids = m.get('LayoutIds')
        if m.get('Formats') is not None:
            self.formats = m.get('Formats')
        self.backgrounds = []
        if m.get('Backgrounds') is not None:
            for k in m.get('Backgrounds'):
                temp_model = AddRecordTemplateRequestBackgrounds()
                self.backgrounds.append(temp_model.from_map(k))
        self.watermarks = []
        if m.get('Watermarks') is not None:
            for k in m.get('Watermarks'):
                temp_model = AddRecordTemplateRequestWatermarks()
                self.watermarks.append(temp_model.from_map(k))
        self.clock_widgets = []
        if m.get('ClockWidgets') is not None:
            for k in m.get('ClockWidgets'):
                temp_model = AddRecordTemplateRequestClockWidgets()
                self.clock_widgets.append(temp_model.from_map(k))
        return self


class AddRecordTemplateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        template_id: str = None,
    ):
        self.request_id = request_id
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class AddRecordTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddRecordTemplateResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddRecordTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAutoLiveStreamRuleRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        show_log: str = None,
        app_id: str = None,
        play_domain: str = None,
        rule_name: str = None,
        call_back: str = None,
    ):
        self.owner_id = owner_id
        self.show_log = show_log
        self.app_id = app_id
        self.play_domain = play_domain
        self.rule_name = rule_name
        self.call_back = call_back

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.show_log is not None:
            result['ShowLog'] = self.show_log
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.play_domain is not None:
            result['PlayDomain'] = self.play_domain
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.call_back is not None:
            result['CallBack'] = self.call_back
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ShowLog') is not None:
            self.show_log = m.get('ShowLog')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('PlayDomain') is not None:
            self.play_domain = m.get('PlayDomain')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('CallBack') is not None:
            self.call_back = m.get('CallBack')
        return self


class CreateAutoLiveStreamRuleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        rule_id: int = None,
    ):
        self.request_id = request_id
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class CreateAutoLiveStreamRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateAutoLiveStreamRuleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateAutoLiveStreamRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateChannelRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        show_log: str = None,
        app_id: str = None,
        channel_id: str = None,
    ):
        self.owner_id = owner_id
        self.show_log = show_log
        self.app_id = app_id
        self.channel_id = channel_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.show_log is not None:
            result['ShowLog'] = self.show_log
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ShowLog') is not None:
            self.show_log = m.get('ShowLog')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        return self


class CreateChannelResponseBody(TeaModel):
    def __init__(
        self,
        nonce: str = None,
        request_id: str = None,
        channel_key: str = None,
        timestamp: int = None,
    ):
        self.nonce = nonce
        self.request_id = request_id
        self.channel_key = channel_key
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.nonce is not None:
            result['Nonce'] = self.nonce
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.channel_key is not None:
            result['ChannelKey'] = self.channel_key
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Nonce') is not None:
            self.nonce = m.get('Nonce')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ChannelKey') is not None:
            self.channel_key = m.get('ChannelKey')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class CreateChannelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateChannelResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateChannelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateConferenceRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        show_log: str = None,
        app_id: str = None,
        conference_name: str = None,
        client_token: str = None,
        start_time: str = None,
        type: str = None,
        remind_notice: int = None,
    ):
        self.owner_id = owner_id
        self.show_log = show_log
        self.app_id = app_id
        self.conference_name = conference_name
        self.client_token = client_token
        self.start_time = start_time
        self.type = type
        self.remind_notice = remind_notice

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.show_log is not None:
            result['ShowLog'] = self.show_log
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.conference_name is not None:
            result['ConferenceName'] = self.conference_name
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.type is not None:
            result['Type'] = self.type
        if self.remind_notice is not None:
            result['RemindNotice'] = self.remind_notice
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ShowLog') is not None:
            self.show_log = m.get('ShowLog')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ConferenceName') is not None:
            self.conference_name = m.get('ConferenceName')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('RemindNotice') is not None:
            self.remind_notice = m.get('RemindNotice')
        return self


class CreateConferenceResponseBodyAuthInfo(TeaModel):
    def __init__(
        self,
        key: str = None,
        nonce: str = None,
        timestamp: int = None,
    ):
        self.key = key
        self.nonce = nonce
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.nonce is not None:
            result['Nonce'] = self.nonce
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Nonce') is not None:
            self.nonce = m.get('Nonce')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class CreateConferenceResponseBody(TeaModel):
    def __init__(
        self,
        auth_info: CreateConferenceResponseBodyAuthInfo = None,
        request_id: str = None,
        conference_id: str = None,
    ):
        self.auth_info = auth_info
        self.request_id = request_id
        self.conference_id = conference_id

    def validate(self):
        if self.auth_info:
            self.auth_info.validate()

    def to_map(self):
        result = dict()
        if self.auth_info is not None:
            result['AuthInfo'] = self.auth_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.conference_id is not None:
            result['ConferenceId'] = self.conference_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthInfo') is not None:
            temp_model = CreateConferenceResponseBodyAuthInfo()
            self.auth_info = temp_model.from_map(m['AuthInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ConferenceId') is not None:
            self.conference_id = m.get('ConferenceId')
        return self


class CreateConferenceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateConferenceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateConferenceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateEventSubscribeRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        show_log: str = None,
        app_id: str = None,
        channel_id: str = None,
        callback_url: str = None,
        client_token: str = None,
        users: List[str] = None,
        events: List[str] = None,
    ):
        self.owner_id = owner_id
        self.show_log = show_log
        self.app_id = app_id
        self.channel_id = channel_id
        self.callback_url = callback_url
        self.client_token = client_token
        self.users = users
        self.events = events

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.show_log is not None:
            result['ShowLog'] = self.show_log
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.users is not None:
            result['Users'] = self.users
        if self.events is not None:
            result['Events'] = self.events
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ShowLog') is not None:
            self.show_log = m.get('ShowLog')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Users') is not None:
            self.users = m.get('Users')
        if m.get('Events') is not None:
            self.events = m.get('Events')
        return self


class CreateEventSubscribeResponseBody(TeaModel):
    def __init__(
        self,
        subscribe_id: str = None,
        request_id: str = None,
    ):
        self.subscribe_id = subscribe_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.subscribe_id is not None:
            result['SubscribeId'] = self.subscribe_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SubscribeId') is not None:
            self.subscribe_id = m.get('SubscribeId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateEventSubscribeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateEventSubscribeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateEventSubscribeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateMPULayoutRequestPanes(TeaModel):
    def __init__(
        self,
        major_pane: int = None,
        width: float = None,
        height: float = None,
        y: float = None,
        pane_id: int = None,
        zorder: int = None,
        x: float = None,
    ):
        self.major_pane = major_pane
        self.width = width
        self.height = height
        self.y = y
        self.pane_id = pane_id
        self.zorder = zorder
        self.x = x

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.major_pane is not None:
            result['MajorPane'] = self.major_pane
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        if self.y is not None:
            result['Y'] = self.y
        if self.pane_id is not None:
            result['PaneId'] = self.pane_id
        if self.zorder is not None:
            result['ZOrder'] = self.zorder
        if self.x is not None:
            result['X'] = self.x
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MajorPane') is not None:
            self.major_pane = m.get('MajorPane')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        if m.get('PaneId') is not None:
            self.pane_id = m.get('PaneId')
        if m.get('ZOrder') is not None:
            self.zorder = m.get('ZOrder')
        if m.get('X') is not None:
            self.x = m.get('X')
        return self


class CreateMPULayoutRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        show_log: str = None,
        app_id: str = None,
        name: str = None,
        audio_mix_count: int = None,
        panes: List[CreateMPULayoutRequestPanes] = None,
    ):
        self.owner_id = owner_id
        self.show_log = show_log
        self.app_id = app_id
        self.name = name
        self.audio_mix_count = audio_mix_count
        self.panes = panes

    def validate(self):
        if self.panes:
            for k in self.panes:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.show_log is not None:
            result['ShowLog'] = self.show_log
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.name is not None:
            result['Name'] = self.name
        if self.audio_mix_count is not None:
            result['AudioMixCount'] = self.audio_mix_count
        result['Panes'] = []
        if self.panes is not None:
            for k in self.panes:
                result['Panes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ShowLog') is not None:
            self.show_log = m.get('ShowLog')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('AudioMixCount') is not None:
            self.audio_mix_count = m.get('AudioMixCount')
        self.panes = []
        if m.get('Panes') is not None:
            for k in m.get('Panes'):
                temp_model = CreateMPULayoutRequestPanes()
                self.panes.append(temp_model.from_map(k))
        return self


class CreateMPULayoutResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        layout_id: int = None,
    ):
        self.request_id = request_id
        self.layout_id = layout_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.layout_id is not None:
            result['LayoutId'] = self.layout_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('LayoutId') is not None:
            self.layout_id = m.get('LayoutId')
        return self


class CreateMPULayoutResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateMPULayoutResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateMPULayoutResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateMPURuleRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        show_log: str = None,
        app_id: str = None,
        channel_prefix: str = None,
        media_encode: int = None,
        background_color: int = None,
        crop_mode: int = None,
        task_profile: str = None,
        play_domain: str = None,
        call_back: str = None,
        layout_ids: List[int] = None,
    ):
        self.owner_id = owner_id
        self.show_log = show_log
        self.app_id = app_id
        self.channel_prefix = channel_prefix
        self.media_encode = media_encode
        self.background_color = background_color
        self.crop_mode = crop_mode
        self.task_profile = task_profile
        self.play_domain = play_domain
        self.call_back = call_back
        self.layout_ids = layout_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.show_log is not None:
            result['ShowLog'] = self.show_log
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_prefix is not None:
            result['ChannelPrefix'] = self.channel_prefix
        if self.media_encode is not None:
            result['MediaEncode'] = self.media_encode
        if self.background_color is not None:
            result['BackgroundColor'] = self.background_color
        if self.crop_mode is not None:
            result['CropMode'] = self.crop_mode
        if self.task_profile is not None:
            result['TaskProfile'] = self.task_profile
        if self.play_domain is not None:
            result['PlayDomain'] = self.play_domain
        if self.call_back is not None:
            result['CallBack'] = self.call_back
        if self.layout_ids is not None:
            result['LayoutIds'] = self.layout_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ShowLog') is not None:
            self.show_log = m.get('ShowLog')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelPrefix') is not None:
            self.channel_prefix = m.get('ChannelPrefix')
        if m.get('MediaEncode') is not None:
            self.media_encode = m.get('MediaEncode')
        if m.get('BackgroundColor') is not None:
            self.background_color = m.get('BackgroundColor')
        if m.get('CropMode') is not None:
            self.crop_mode = m.get('CropMode')
        if m.get('TaskProfile') is not None:
            self.task_profile = m.get('TaskProfile')
        if m.get('PlayDomain') is not None:
            self.play_domain = m.get('PlayDomain')
        if m.get('CallBack') is not None:
            self.call_back = m.get('CallBack')
        if m.get('LayoutIds') is not None:
            self.layout_ids = m.get('LayoutIds')
        return self


class CreateMPURuleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        rule_id: int = None,
    ):
        self.request_id = request_id
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class CreateMPURuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateMPURuleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateMPURuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateServiceLinkedRoleForRtcRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        show_log: str = None,
    ):
        self.owner_id = owner_id
        self.show_log = show_log

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.show_log is not None:
            result['ShowLog'] = self.show_log
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ShowLog') is not None:
            self.show_log = m.get('ShowLog')
        return self


class CreateServiceLinkedRoleForRtcResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateServiceLinkedRoleForRtcResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateServiceLinkedRoleForRtcResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateServiceLinkedRoleForRtcResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSubscribeRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        show_log: str = None,
        app_id: str = None,
        channel_id: str = None,
        callback_url: str = None,
        client_token: str = None,
        users: List[str] = None,
        events: List[str] = None,
    ):
        self.owner_id = owner_id
        self.show_log = show_log
        self.app_id = app_id
        self.channel_id = channel_id
        self.callback_url = callback_url
        self.client_token = client_token
        self.users = users
        self.events = events

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.show_log is not None:
            result['ShowLog'] = self.show_log
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.users is not None:
            result['Users'] = self.users
        if self.events is not None:
            result['Events'] = self.events
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ShowLog') is not None:
            self.show_log = m.get('ShowLog')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Users') is not None:
            self.users = m.get('Users')
        if m.get('Events') is not None:
            self.events = m.get('Events')
        return self


class CreateSubscribeResponseBody(TeaModel):
    def __init__(
        self,
        subscribe_id: str = None,
        request_id: str = None,
    ):
        self.subscribe_id = subscribe_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.subscribe_id is not None:
            result['SubscribeId'] = self.subscribe_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SubscribeId') is not None:
            self.subscribe_id = m.get('SubscribeId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateSubscribeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateSubscribeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateSubscribeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAutoLiveStreamRuleRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        show_log: str = None,
        app_id: str = None,
        rule_id: int = None,
    ):
        self.owner_id = owner_id
        self.show_log = show_log
        self.app_id = app_id
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.show_log is not None:
            result['ShowLog'] = self.show_log
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ShowLog') is not None:
            self.show_log = m.get('ShowLog')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class DeleteAutoLiveStreamRuleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteAutoLiveStreamRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteAutoLiveStreamRuleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteAutoLiveStreamRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteChannelRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        show_log: str = None,
        app_id: str = None,
        channel_id: str = None,
    ):
        self.owner_id = owner_id
        self.show_log = show_log
        self.app_id = app_id
        self.channel_id = channel_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.show_log is not None:
            result['ShowLog'] = self.show_log
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ShowLog') is not None:
            self.show_log = m.get('ShowLog')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        return self


class DeleteChannelResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteChannelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteChannelResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteChannelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteConferenceRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        show_log: str = None,
        app_id: str = None,
        conference_id: str = None,
    ):
        self.owner_id = owner_id
        self.show_log = show_log
        self.app_id = app_id
        self.conference_id = conference_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.show_log is not None:
            result['ShowLog'] = self.show_log
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.conference_id is not None:
            result['ConferenceId'] = self.conference_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ShowLog') is not None:
            self.show_log = m.get('ShowLog')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ConferenceId') is not None:
            self.conference_id = m.get('ConferenceId')
        return self


class DeleteConferenceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteConferenceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteConferenceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteConferenceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteEventSubscribeRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        show_log: str = None,
        app_id: str = None,
        subscribe_id: str = None,
    ):
        self.owner_id = owner_id
        self.show_log = show_log
        self.app_id = app_id
        self.subscribe_id = subscribe_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.show_log is not None:
            result['ShowLog'] = self.show_log
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.subscribe_id is not None:
            result['SubscribeId'] = self.subscribe_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ShowLog') is not None:
            self.show_log = m.get('ShowLog')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('SubscribeId') is not None:
            self.subscribe_id = m.get('SubscribeId')
        return self


class DeleteEventSubscribeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteEventSubscribeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteEventSubscribeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteEventSubscribeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteMPULayoutRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        show_log: str = None,
        app_id: str = None,
        layout_id: int = None,
    ):
        self.owner_id = owner_id
        self.show_log = show_log
        self.app_id = app_id
        self.layout_id = layout_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.show_log is not None:
            result['ShowLog'] = self.show_log
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.layout_id is not None:
            result['LayoutId'] = self.layout_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ShowLog') is not None:
            self.show_log = m.get('ShowLog')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('LayoutId') is not None:
            self.layout_id = m.get('LayoutId')
        return self


class DeleteMPULayoutResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteMPULayoutResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteMPULayoutResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteMPULayoutResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteMPURuleRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        show_log: str = None,
        app_id: str = None,
        rule_id: int = None,
    ):
        self.owner_id = owner_id
        self.show_log = show_log
        self.app_id = app_id
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.show_log is not None:
            result['ShowLog'] = self.show_log
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ShowLog') is not None:
            self.show_log = m.get('ShowLog')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class DeleteMPURuleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteMPURuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteMPURuleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteMPURuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRecordTemplateRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        show_log: str = None,
        app_id: str = None,
        template_id: str = None,
    ):
        self.owner_id = owner_id
        self.show_log = show_log
        self.app_id = app_id
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.show_log is not None:
            result['ShowLog'] = self.show_log
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ShowLog') is not None:
            self.show_log = m.get('ShowLog')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class DeleteRecordTemplateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteRecordTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteRecordTemplateResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteRecordTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSubscribeRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        show_log: str = None,
        app_id: str = None,
        subscribe_id: str = None,
    ):
        self.owner_id = owner_id
        self.show_log = show_log
        self.app_id = app_id
        self.subscribe_id = subscribe_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.show_log is not None:
            result['ShowLog'] = self.show_log
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.subscribe_id is not None:
            result['SubscribeId'] = self.subscribe_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ShowLog') is not None:
            self.show_log = m.get('ShowLog')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('SubscribeId') is not None:
            self.subscribe_id = m.get('SubscribeId')
        return self


class DeleteSubscribeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteSubscribeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteSubscribeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteSubscribeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAppsRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        show_log: str = None,
        app_id: str = None,
        status: str = None,
        order: str = None,
        page_num: int = None,
        page_size: int = None,
    ):
        self.owner_id = owner_id
        self.show_log = show_log
        self.app_id = app_id
        self.status = status
        self.order = order
        self.page_num = page_num
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.show_log is not None:
            result['ShowLog'] = self.show_log
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.status is not None:
            result['Status'] = self.status
        if self.order is not None:
            result['Order'] = self.order
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ShowLog') is not None:
            self.show_log = m.get('ShowLog')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeAppsResponseBodyAppListAppServiceAreas(TeaModel):
    def __init__(
        self,
        service_area: List[str] = None,
    ):
        self.service_area = service_area

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.service_area is not None:
            result['ServiceArea'] = self.service_area
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceArea') is not None:
            self.service_area = m.get('ServiceArea')
        return self


class DescribeAppsResponseBodyAppListApp(TeaModel):
    def __init__(
        self,
        status: int = None,
        app_name: str = None,
        service_areas: DescribeAppsResponseBodyAppListAppServiceAreas = None,
        app_id: str = None,
        create_time: str = None,
        bill_type: str = None,
        app_type: str = None,
    ):
        self.status = status
        self.app_name = app_name
        self.service_areas = service_areas
        self.app_id = app_id
        self.create_time = create_time
        self.bill_type = bill_type
        self.app_type = app_type

    def validate(self):
        if self.service_areas:
            self.service_areas.validate()

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.service_areas is not None:
            result['ServiceAreas'] = self.service_areas.to_map()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.bill_type is not None:
            result['BillType'] = self.bill_type
        if self.app_type is not None:
            result['AppType'] = self.app_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('ServiceAreas') is not None:
            temp_model = DescribeAppsResponseBodyAppListAppServiceAreas()
            self.service_areas = temp_model.from_map(m['ServiceAreas'])
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('BillType') is not None:
            self.bill_type = m.get('BillType')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        return self


class DescribeAppsResponseBodyAppList(TeaModel):
    def __init__(
        self,
        app: List[DescribeAppsResponseBodyAppListApp] = None,
    ):
        self.app = app

    def validate(self):
        if self.app:
            for k in self.app:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['App'] = []
        if self.app is not None:
            for k in self.app:
                result['App'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.app = []
        if m.get('App') is not None:
            for k in m.get('App'):
                temp_model = DescribeAppsResponseBodyAppListApp()
                self.app.append(temp_model.from_map(k))
        return self


class DescribeAppsResponseBody(TeaModel):
    def __init__(
        self,
        total_num: int = None,
        total_page: int = None,
        request_id: str = None,
        app_list: DescribeAppsResponseBodyAppList = None,
    ):
        self.total_num = total_num
        self.total_page = total_page
        self.request_id = request_id
        self.app_list = app_list

    def validate(self):
        if self.app_list:
            self.app_list.validate()

    def to_map(self):
        result = dict()
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.app_list is not None:
            result['AppList'] = self.app_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AppList') is not None:
            temp_model = DescribeAppsResponseBodyAppList()
            self.app_list = temp_model.from_map(m['AppList'])
        return self


class DescribeAppsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAppsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeAppsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAutoLiveStreamRuleRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        show_log: str = None,
        app_id: str = None,
    ):
        self.owner_id = owner_id
        self.show_log = show_log
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.show_log is not None:
            result['ShowLog'] = self.show_log
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ShowLog') is not None:
            self.show_log = m.get('ShowLog')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class DescribeAutoLiveStreamRuleResponseBodyRules(TeaModel):
    def __init__(
        self,
        call_back: str = None,
        play_domain: str = None,
        create_time: str = None,
        rule_name: str = None,
        rule_id: int = None,
    ):
        self.call_back = call_back
        self.play_domain = play_domain
        self.create_time = create_time
        self.rule_name = rule_name
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.call_back is not None:
            result['CallBack'] = self.call_back
        if self.play_domain is not None:
            result['PlayDomain'] = self.play_domain
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallBack') is not None:
            self.call_back = m.get('CallBack')
        if m.get('PlayDomain') is not None:
            self.play_domain = m.get('PlayDomain')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class DescribeAutoLiveStreamRuleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        rules: List[DescribeAutoLiveStreamRuleResponseBodyRules] = None,
    ):
        self.request_id = request_id
        self.rules = rules

    def validate(self):
        if self.rules:
            for k in self.rules:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['Rules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.rules = []
        if m.get('Rules') is not None:
            for k in m.get('Rules'):
                temp_model = DescribeAutoLiveStreamRuleResponseBodyRules()
                self.rules.append(temp_model.from_map(k))
        return self


class DescribeAutoLiveStreamRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAutoLiveStreamRuleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeAutoLiveStreamRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeChannelParticipantsRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        show_log: str = None,
        app_id: str = None,
        channel_id: str = None,
        order: str = None,
        page_num: int = None,
        page_size: int = None,
    ):
        self.owner_id = owner_id
        self.show_log = show_log
        self.app_id = app_id
        self.channel_id = channel_id
        self.order = order
        self.page_num = page_num
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.show_log is not None:
            result['ShowLog'] = self.show_log
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.order is not None:
            result['Order'] = self.order
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ShowLog') is not None:
            self.show_log = m.get('ShowLog')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeChannelParticipantsResponseBodyUserList(TeaModel):
    def __init__(
        self,
        user: List[str] = None,
    ):
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.user is not None:
            result['User'] = self.user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('User') is not None:
            self.user = m.get('User')
        return self


class DescribeChannelParticipantsResponseBody(TeaModel):
    def __init__(
        self,
        total_num: int = None,
        total_page: int = None,
        request_id: str = None,
        timestamp: int = None,
        user_list: DescribeChannelParticipantsResponseBodyUserList = None,
    ):
        self.total_num = total_num
        self.total_page = total_page
        self.request_id = request_id
        self.timestamp = timestamp
        self.user_list = user_list

    def validate(self):
        if self.user_list:
            self.user_list.validate()

    def to_map(self):
        result = dict()
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.user_list is not None:
            result['UserList'] = self.user_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('UserList') is not None:
            temp_model = DescribeChannelParticipantsResponseBodyUserList()
            self.user_list = temp_model.from_map(m['UserList'])
        return self


class DescribeChannelParticipantsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeChannelParticipantsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeChannelParticipantsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeChannelUsersRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        show_log: str = None,
        app_id: str = None,
        channel_id: str = None,
    ):
        self.owner_id = owner_id
        self.show_log = show_log
        self.app_id = app_id
        self.channel_id = channel_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.show_log is not None:
            result['ShowLog'] = self.show_log
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ShowLog') is not None:
            self.show_log = m.get('ShowLog')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        return self


class DescribeChannelUsersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        interactive_user_list: List[str] = None,
        live_user_num: int = None,
        channel_profile: int = None,
        interactive_user_num: int = None,
        is_channel_exist: bool = None,
        timestamp: int = None,
        user_list: List[str] = None,
        live_user_list: List[str] = None,
        comm_total_num: int = None,
    ):
        self.request_id = request_id
        self.interactive_user_list = interactive_user_list
        self.live_user_num = live_user_num
        self.channel_profile = channel_profile
        self.interactive_user_num = interactive_user_num
        self.is_channel_exist = is_channel_exist
        self.timestamp = timestamp
        self.user_list = user_list
        self.live_user_list = live_user_list
        self.comm_total_num = comm_total_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.interactive_user_list is not None:
            result['InteractiveUserList'] = self.interactive_user_list
        if self.live_user_num is not None:
            result['LiveUserNum'] = self.live_user_num
        if self.channel_profile is not None:
            result['ChannelProfile'] = self.channel_profile
        if self.interactive_user_num is not None:
            result['InteractiveUserNum'] = self.interactive_user_num
        if self.is_channel_exist is not None:
            result['IsChannelExist'] = self.is_channel_exist
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.user_list is not None:
            result['UserList'] = self.user_list
        if self.live_user_list is not None:
            result['LiveUserList'] = self.live_user_list
        if self.comm_total_num is not None:
            result['CommTotalNum'] = self.comm_total_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InteractiveUserList') is not None:
            self.interactive_user_list = m.get('InteractiveUserList')
        if m.get('LiveUserNum') is not None:
            self.live_user_num = m.get('LiveUserNum')
        if m.get('ChannelProfile') is not None:
            self.channel_profile = m.get('ChannelProfile')
        if m.get('InteractiveUserNum') is not None:
            self.interactive_user_num = m.get('InteractiveUserNum')
        if m.get('IsChannelExist') is not None:
            self.is_channel_exist = m.get('IsChannelExist')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('UserList') is not None:
            self.user_list = m.get('UserList')
        if m.get('LiveUserList') is not None:
            self.live_user_list = m.get('LiveUserList')
        if m.get('CommTotalNum') is not None:
            self.comm_total_num = m.get('CommTotalNum')
        return self


class DescribeChannelUsersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeChannelUsersResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeChannelUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeConferenceAuthInfoRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        show_log: str = None,
        app_id: str = None,
        conference_id: str = None,
    ):
        self.owner_id = owner_id
        self.show_log = show_log
        self.app_id = app_id
        self.conference_id = conference_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.show_log is not None:
            result['ShowLog'] = self.show_log
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.conference_id is not None:
            result['ConferenceId'] = self.conference_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ShowLog') is not None:
            self.show_log = m.get('ShowLog')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ConferenceId') is not None:
            self.conference_id = m.get('ConferenceId')
        return self


class DescribeConferenceAuthInfoResponseBodyAuthInfo(TeaModel):
    def __init__(
        self,
        key: str = None,
        nonce: str = None,
        timestamp: int = None,
    ):
        self.key = key
        self.nonce = nonce
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.nonce is not None:
            result['Nonce'] = self.nonce
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Nonce') is not None:
            self.nonce = m.get('Nonce')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class DescribeConferenceAuthInfoResponseBody(TeaModel):
    def __init__(
        self,
        auth_info: DescribeConferenceAuthInfoResponseBodyAuthInfo = None,
        request_id: str = None,
        conference_id: str = None,
    ):
        self.auth_info = auth_info
        self.request_id = request_id
        self.conference_id = conference_id

    def validate(self):
        if self.auth_info:
            self.auth_info.validate()

    def to_map(self):
        result = dict()
        if self.auth_info is not None:
            result['AuthInfo'] = self.auth_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.conference_id is not None:
            result['ConferenceId'] = self.conference_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthInfo') is not None:
            temp_model = DescribeConferenceAuthInfoResponseBodyAuthInfo()
            self.auth_info = temp_model.from_map(m['AuthInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ConferenceId') is not None:
            self.conference_id = m.get('ConferenceId')
        return self


class DescribeConferenceAuthInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeConferenceAuthInfoResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeConferenceAuthInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMPULayoutInfoRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        show_log: str = None,
        app_id: str = None,
        layout_id: int = None,
    ):
        self.owner_id = owner_id
        self.show_log = show_log
        self.app_id = app_id
        self.layout_id = layout_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.show_log is not None:
            result['ShowLog'] = self.show_log
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.layout_id is not None:
            result['LayoutId'] = self.layout_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ShowLog') is not None:
            self.show_log = m.get('ShowLog')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('LayoutId') is not None:
            self.layout_id = m.get('LayoutId')
        return self


class DescribeMPULayoutInfoResponseBodyLayoutPanesPanes(TeaModel):
    def __init__(
        self,
        major_pane: int = None,
        width: float = None,
        height: float = None,
        y: float = None,
        pane_id: int = None,
        zorder: int = None,
        x: float = None,
    ):
        self.major_pane = major_pane
        self.width = width
        self.height = height
        self.y = y
        self.pane_id = pane_id
        self.zorder = zorder
        self.x = x

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.major_pane is not None:
            result['MajorPane'] = self.major_pane
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        if self.y is not None:
            result['Y'] = self.y
        if self.pane_id is not None:
            result['PaneId'] = self.pane_id
        if self.zorder is not None:
            result['ZOrder'] = self.zorder
        if self.x is not None:
            result['X'] = self.x
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MajorPane') is not None:
            self.major_pane = m.get('MajorPane')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        if m.get('PaneId') is not None:
            self.pane_id = m.get('PaneId')
        if m.get('ZOrder') is not None:
            self.zorder = m.get('ZOrder')
        if m.get('X') is not None:
            self.x = m.get('X')
        return self


class DescribeMPULayoutInfoResponseBodyLayoutPanes(TeaModel):
    def __init__(
        self,
        panes: List[DescribeMPULayoutInfoResponseBodyLayoutPanesPanes] = None,
    ):
        self.panes = panes

    def validate(self):
        if self.panes:
            for k in self.panes:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Panes'] = []
        if self.panes is not None:
            for k in self.panes:
                result['Panes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.panes = []
        if m.get('Panes') is not None:
            for k in m.get('Panes'):
                temp_model = DescribeMPULayoutInfoResponseBodyLayoutPanesPanes()
                self.panes.append(temp_model.from_map(k))
        return self


class DescribeMPULayoutInfoResponseBodyLayout(TeaModel):
    def __init__(
        self,
        layout_id: int = None,
        panes: DescribeMPULayoutInfoResponseBodyLayoutPanes = None,
        name: str = None,
        audio_mix_count: int = None,
    ):
        self.layout_id = layout_id
        self.panes = panes
        self.name = name
        self.audio_mix_count = audio_mix_count

    def validate(self):
        if self.panes:
            self.panes.validate()

    def to_map(self):
        result = dict()
        if self.layout_id is not None:
            result['LayoutId'] = self.layout_id
        if self.panes is not None:
            result['Panes'] = self.panes.to_map()
        if self.name is not None:
            result['Name'] = self.name
        if self.audio_mix_count is not None:
            result['AudioMixCount'] = self.audio_mix_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LayoutId') is not None:
            self.layout_id = m.get('LayoutId')
        if m.get('Panes') is not None:
            temp_model = DescribeMPULayoutInfoResponseBodyLayoutPanes()
            self.panes = temp_model.from_map(m['Panes'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('AudioMixCount') is not None:
            self.audio_mix_count = m.get('AudioMixCount')
        return self


class DescribeMPULayoutInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        layout: DescribeMPULayoutInfoResponseBodyLayout = None,
    ):
        self.request_id = request_id
        self.layout = layout

    def validate(self):
        if self.layout:
            self.layout.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.layout is not None:
            result['Layout'] = self.layout.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Layout') is not None:
            temp_model = DescribeMPULayoutInfoResponseBodyLayout()
            self.layout = temp_model.from_map(m['Layout'])
        return self


class DescribeMPULayoutInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeMPULayoutInfoResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeMPULayoutInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMPULayoutInfoListRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        show_log: str = None,
        app_id: str = None,
        layout_id: int = None,
        name: str = None,
        page_num: int = None,
        page_size: int = None,
    ):
        self.owner_id = owner_id
        self.show_log = show_log
        self.app_id = app_id
        self.layout_id = layout_id
        self.name = name
        self.page_num = page_num
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.show_log is not None:
            result['ShowLog'] = self.show_log
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.layout_id is not None:
            result['LayoutId'] = self.layout_id
        if self.name is not None:
            result['Name'] = self.name
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ShowLog') is not None:
            self.show_log = m.get('ShowLog')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('LayoutId') is not None:
            self.layout_id = m.get('LayoutId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeMPULayoutInfoListResponseBodyLayoutsLayoutPanesPanes(TeaModel):
    def __init__(
        self,
        major_pane: int = None,
        width: float = None,
        height: float = None,
        y: float = None,
        pane_id: int = None,
        zorder: int = None,
        x: float = None,
    ):
        self.major_pane = major_pane
        self.width = width
        self.height = height
        self.y = y
        self.pane_id = pane_id
        self.zorder = zorder
        self.x = x

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.major_pane is not None:
            result['MajorPane'] = self.major_pane
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        if self.y is not None:
            result['Y'] = self.y
        if self.pane_id is not None:
            result['PaneId'] = self.pane_id
        if self.zorder is not None:
            result['ZOrder'] = self.zorder
        if self.x is not None:
            result['X'] = self.x
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MajorPane') is not None:
            self.major_pane = m.get('MajorPane')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        if m.get('PaneId') is not None:
            self.pane_id = m.get('PaneId')
        if m.get('ZOrder') is not None:
            self.zorder = m.get('ZOrder')
        if m.get('X') is not None:
            self.x = m.get('X')
        return self


class DescribeMPULayoutInfoListResponseBodyLayoutsLayoutPanes(TeaModel):
    def __init__(
        self,
        panes: List[DescribeMPULayoutInfoListResponseBodyLayoutsLayoutPanesPanes] = None,
    ):
        self.panes = panes

    def validate(self):
        if self.panes:
            for k in self.panes:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Panes'] = []
        if self.panes is not None:
            for k in self.panes:
                result['Panes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.panes = []
        if m.get('Panes') is not None:
            for k in m.get('Panes'):
                temp_model = DescribeMPULayoutInfoListResponseBodyLayoutsLayoutPanesPanes()
                self.panes.append(temp_model.from_map(k))
        return self


class DescribeMPULayoutInfoListResponseBodyLayoutsLayout(TeaModel):
    def __init__(
        self,
        layout_id: int = None,
        panes: DescribeMPULayoutInfoListResponseBodyLayoutsLayoutPanes = None,
        name: str = None,
        audio_mix_count: int = None,
    ):
        self.layout_id = layout_id
        self.panes = panes
        self.name = name
        self.audio_mix_count = audio_mix_count

    def validate(self):
        if self.panes:
            self.panes.validate()

    def to_map(self):
        result = dict()
        if self.layout_id is not None:
            result['LayoutId'] = self.layout_id
        if self.panes is not None:
            result['Panes'] = self.panes.to_map()
        if self.name is not None:
            result['Name'] = self.name
        if self.audio_mix_count is not None:
            result['AudioMixCount'] = self.audio_mix_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LayoutId') is not None:
            self.layout_id = m.get('LayoutId')
        if m.get('Panes') is not None:
            temp_model = DescribeMPULayoutInfoListResponseBodyLayoutsLayoutPanes()
            self.panes = temp_model.from_map(m['Panes'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('AudioMixCount') is not None:
            self.audio_mix_count = m.get('AudioMixCount')
        return self


class DescribeMPULayoutInfoListResponseBodyLayouts(TeaModel):
    def __init__(
        self,
        layout: List[DescribeMPULayoutInfoListResponseBodyLayoutsLayout] = None,
    ):
        self.layout = layout

    def validate(self):
        if self.layout:
            for k in self.layout:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Layout'] = []
        if self.layout is not None:
            for k in self.layout:
                result['Layout'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.layout = []
        if m.get('Layout') is not None:
            for k in m.get('Layout'):
                temp_model = DescribeMPULayoutInfoListResponseBodyLayoutsLayout()
                self.layout.append(temp_model.from_map(k))
        return self


class DescribeMPULayoutInfoListResponseBody(TeaModel):
    def __init__(
        self,
        total_num: int = None,
        total_page: int = None,
        request_id: str = None,
        layouts: DescribeMPULayoutInfoListResponseBodyLayouts = None,
    ):
        self.total_num = total_num
        self.total_page = total_page
        self.request_id = request_id
        self.layouts = layouts

    def validate(self):
        if self.layouts:
            self.layouts.validate()

    def to_map(self):
        result = dict()
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.layouts is not None:
            result['Layouts'] = self.layouts.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Layouts') is not None:
            temp_model = DescribeMPULayoutInfoListResponseBodyLayouts()
            self.layouts = temp_model.from_map(m['Layouts'])
        return self


class DescribeMPULayoutInfoListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeMPULayoutInfoListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeMPULayoutInfoListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMPULayoutListRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        show_log: str = None,
        app_id: str = None,
    ):
        self.owner_id = owner_id
        self.show_log = show_log
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.show_log is not None:
            result['ShowLog'] = self.show_log
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ShowLog') is not None:
            self.show_log = m.get('ShowLog')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class DescribeMPULayoutListResponseBodyLayoutIds(TeaModel):
    def __init__(
        self,
        layout_id: List[str] = None,
    ):
        self.layout_id = layout_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.layout_id is not None:
            result['LayoutId'] = self.layout_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LayoutId') is not None:
            self.layout_id = m.get('LayoutId')
        return self


class DescribeMPULayoutListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        layout_ids: DescribeMPULayoutListResponseBodyLayoutIds = None,
    ):
        self.request_id = request_id
        self.layout_ids = layout_ids

    def validate(self):
        if self.layout_ids:
            self.layout_ids.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.layout_ids is not None:
            result['LayoutIds'] = self.layout_ids.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('LayoutIds') is not None:
            temp_model = DescribeMPULayoutListResponseBodyLayoutIds()
            self.layout_ids = temp_model.from_map(m['LayoutIds'])
        return self


class DescribeMPULayoutListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeMPULayoutListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeMPULayoutListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMPURuleRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        show_log: str = None,
        app_id: str = None,
    ):
        self.owner_id = owner_id
        self.show_log = show_log
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.show_log is not None:
            result['ShowLog'] = self.show_log
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ShowLog') is not None:
            self.show_log = m.get('ShowLog')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class DescribeMPURuleResponseBodyRules(TeaModel):
    def __init__(
        self,
        media_encode: int = None,
        crop_mode: int = None,
        call_back: str = None,
        play_domain: str = None,
        channel_prefix: str = None,
        backgroud_color: int = None,
        is_enable: int = None,
        layout_ids: List[str] = None,
        task_profile: str = None,
        rule_id: int = None,
    ):
        self.media_encode = media_encode
        self.crop_mode = crop_mode
        self.call_back = call_back
        self.play_domain = play_domain
        self.channel_prefix = channel_prefix
        self.backgroud_color = backgroud_color
        self.is_enable = is_enable
        self.layout_ids = layout_ids
        self.task_profile = task_profile
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.media_encode is not None:
            result['MediaEncode'] = self.media_encode
        if self.crop_mode is not None:
            result['CropMode'] = self.crop_mode
        if self.call_back is not None:
            result['CallBack'] = self.call_back
        if self.play_domain is not None:
            result['PlayDomain'] = self.play_domain
        if self.channel_prefix is not None:
            result['ChannelPrefix'] = self.channel_prefix
        if self.backgroud_color is not None:
            result['BackgroudColor'] = self.backgroud_color
        if self.is_enable is not None:
            result['IsEnable'] = self.is_enable
        if self.layout_ids is not None:
            result['LayoutIds'] = self.layout_ids
        if self.task_profile is not None:
            result['TaskProfile'] = self.task_profile
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MediaEncode') is not None:
            self.media_encode = m.get('MediaEncode')
        if m.get('CropMode') is not None:
            self.crop_mode = m.get('CropMode')
        if m.get('CallBack') is not None:
            self.call_back = m.get('CallBack')
        if m.get('PlayDomain') is not None:
            self.play_domain = m.get('PlayDomain')
        if m.get('ChannelPrefix') is not None:
            self.channel_prefix = m.get('ChannelPrefix')
        if m.get('BackgroudColor') is not None:
            self.backgroud_color = m.get('BackgroudColor')
        if m.get('IsEnable') is not None:
            self.is_enable = m.get('IsEnable')
        if m.get('LayoutIds') is not None:
            self.layout_ids = m.get('LayoutIds')
        if m.get('TaskProfile') is not None:
            self.task_profile = m.get('TaskProfile')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class DescribeMPURuleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        rules: List[DescribeMPURuleResponseBodyRules] = None,
    ):
        self.request_id = request_id
        self.rules = rules

    def validate(self):
        if self.rules:
            for k in self.rules:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['Rules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.rules = []
        if m.get('Rules') is not None:
            for k in m.get('Rules'):
                temp_model = DescribeMPURuleResponseBodyRules()
                self.rules.append(temp_model.from_map(k))
        return self


class DescribeMPURuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeMPURuleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeMPURuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRecordFilesRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        show_log: str = None,
        app_id: str = None,
        channel_id: str = None,
        page_size: int = None,
        page_num: int = None,
        start_time: str = None,
        end_time: str = None,
        task_ids: List[str] = None,
    ):
        self.owner_id = owner_id
        self.show_log = show_log
        self.app_id = app_id
        self.channel_id = channel_id
        self.page_size = page_size
        self.page_num = page_num
        self.start_time = start_time
        self.end_time = end_time
        self.task_ids = task_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.show_log is not None:
            result['ShowLog'] = self.show_log
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.task_ids is not None:
            result['TaskIds'] = self.task_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ShowLog') is not None:
            self.show_log = m.get('ShowLog')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('TaskIds') is not None:
            self.task_ids = m.get('TaskIds')
        return self


class DescribeRecordFilesResponseBodyRecordFiles(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        create_time: str = None,
        app_id: str = None,
        channel_id: str = None,
        url: str = None,
        duration: float = None,
        task_id: str = None,
        stop_time: str = None,
    ):
        self.start_time = start_time
        self.create_time = create_time
        self.app_id = app_id
        self.channel_id = channel_id
        self.url = url
        self.duration = duration
        self.task_id = task_id
        self.stop_time = stop_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.url is not None:
            result['Url'] = self.url
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.stop_time is not None:
            result['StopTime'] = self.stop_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('StopTime') is not None:
            self.stop_time = m.get('StopTime')
        return self


class DescribeRecordFilesResponseBody(TeaModel):
    def __init__(
        self,
        total_num: int = None,
        total_page: int = None,
        request_id: str = None,
        record_files: List[DescribeRecordFilesResponseBodyRecordFiles] = None,
    ):
        self.total_num = total_num
        self.total_page = total_page
        self.request_id = request_id
        self.record_files = record_files

    def validate(self):
        if self.record_files:
            for k in self.record_files:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['RecordFiles'] = []
        if self.record_files is not None:
            for k in self.record_files:
                result['RecordFiles'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.record_files = []
        if m.get('RecordFiles') is not None:
            for k in m.get('RecordFiles'):
                temp_model = DescribeRecordFilesResponseBodyRecordFiles()
                self.record_files.append(temp_model.from_map(k))
        return self


class DescribeRecordFilesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRecordFilesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeRecordFilesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRecordTasksRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        show_log: str = None,
        app_id: str = None,
        channel_id: str = None,
        status: str = None,
        start_time: str = None,
        end_time: str = None,
        page_size: int = None,
        page_num: int = None,
        task_ids: List[str] = None,
    ):
        self.owner_id = owner_id
        self.show_log = show_log
        self.app_id = app_id
        self.channel_id = channel_id
        self.status = status
        self.start_time = start_time
        self.end_time = end_time
        self.page_size = page_size
        self.page_num = page_num
        self.task_ids = task_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.show_log is not None:
            result['ShowLog'] = self.show_log
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.status is not None:
            result['Status'] = self.status
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.task_ids is not None:
            result['TaskIds'] = self.task_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ShowLog') is not None:
            self.show_log = m.get('ShowLog')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('TaskIds') is not None:
            self.task_ids = m.get('TaskIds')
        return self


class DescribeRecordTasksResponseBodyRecordTasksUserPanes(TeaModel):
    def __init__(
        self,
        user_id: str = None,
        pane_id: int = None,
        source: str = None,
    ):
        self.user_id = user_id
        self.pane_id = pane_id
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.pane_id is not None:
            result['PaneId'] = self.pane_id
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('PaneId') is not None:
            self.pane_id = m.get('PaneId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class DescribeRecordTasksResponseBodyRecordTasks(TeaModel):
    def __init__(
        self,
        status: int = None,
        sub_spec_users: List[str] = None,
        user_panes: List[DescribeRecordTasksResponseBodyRecordTasksUserPanes] = None,
        create_time: str = None,
        app_id: str = None,
        channel_id: str = None,
        task_id: str = None,
        template_id: str = None,
    ):
        self.status = status
        self.sub_spec_users = sub_spec_users
        self.user_panes = user_panes
        self.create_time = create_time
        self.app_id = app_id
        self.channel_id = channel_id
        self.task_id = task_id
        self.template_id = template_id

    def validate(self):
        if self.user_panes:
            for k in self.user_panes:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.sub_spec_users is not None:
            result['SubSpecUsers'] = self.sub_spec_users
        result['UserPanes'] = []
        if self.user_panes is not None:
            for k in self.user_panes:
                result['UserPanes'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubSpecUsers') is not None:
            self.sub_spec_users = m.get('SubSpecUsers')
        self.user_panes = []
        if m.get('UserPanes') is not None:
            for k in m.get('UserPanes'):
                temp_model = DescribeRecordTasksResponseBodyRecordTasksUserPanes()
                self.user_panes.append(temp_model.from_map(k))
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class DescribeRecordTasksResponseBody(TeaModel):
    def __init__(
        self,
        record_tasks: List[DescribeRecordTasksResponseBodyRecordTasks] = None,
        total_num: int = None,
        total_page: int = None,
        request_id: str = None,
    ):
        self.record_tasks = record_tasks
        self.total_num = total_num
        self.total_page = total_page
        self.request_id = request_id

    def validate(self):
        if self.record_tasks:
            for k in self.record_tasks:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['RecordTasks'] = []
        if self.record_tasks is not None:
            for k in self.record_tasks:
                result['RecordTasks'].append(k.to_map() if k else None)
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.record_tasks = []
        if m.get('RecordTasks') is not None:
            for k in m.get('RecordTasks'):
                temp_model = DescribeRecordTasksResponseBodyRecordTasks()
                self.record_tasks.append(temp_model.from_map(k))
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeRecordTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRecordTasksResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeRecordTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRecordTemplatesRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        show_log: str = None,
        app_id: str = None,
        page_size: int = None,
        page_num: int = None,
        template_ids: List[str] = None,
    ):
        self.owner_id = owner_id
        self.show_log = show_log
        self.app_id = app_id
        self.page_size = page_size
        self.page_num = page_num
        self.template_ids = template_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.show_log is not None:
            result['ShowLog'] = self.show_log
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.template_ids is not None:
            result['TemplateIds'] = self.template_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ShowLog') is not None:
            self.show_log = m.get('ShowLog')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('TemplateIds') is not None:
            self.template_ids = m.get('TemplateIds')
        return self


class DescribeRecordTemplatesResponseBodyTemplatesClockWidgets(TeaModel):
    def __init__(
        self,
        font_type: int = None,
        font_color: int = None,
        y: float = None,
        zorder: int = None,
        x: float = None,
        font_size: int = None,
    ):
        self.font_type = font_type
        self.font_color = font_color
        self.y = y
        self.zorder = zorder
        self.x = x
        self.font_size = font_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.font_type is not None:
            result['FontType'] = self.font_type
        if self.font_color is not None:
            result['FontColor'] = self.font_color
        if self.y is not None:
            result['Y'] = self.y
        if self.zorder is not None:
            result['ZOrder'] = self.zorder
        if self.x is not None:
            result['X'] = self.x
        if self.font_size is not None:
            result['FontSize'] = self.font_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FontType') is not None:
            self.font_type = m.get('FontType')
        if m.get('FontColor') is not None:
            self.font_color = m.get('FontColor')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        if m.get('ZOrder') is not None:
            self.zorder = m.get('ZOrder')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('FontSize') is not None:
            self.font_size = m.get('FontSize')
        return self


class DescribeRecordTemplatesResponseBodyTemplatesBackgrounds(TeaModel):
    def __init__(
        self,
        width: float = None,
        height: float = None,
        y: float = None,
        url: str = None,
        display: int = None,
        zorder: int = None,
        x: float = None,
    ):
        self.width = width
        self.height = height
        self.y = y
        self.url = url
        self.display = display
        self.zorder = zorder
        self.x = x

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        if self.y is not None:
            result['Y'] = self.y
        if self.url is not None:
            result['Url'] = self.url
        if self.display is not None:
            result['Display'] = self.display
        if self.zorder is not None:
            result['ZOrder'] = self.zorder
        if self.x is not None:
            result['X'] = self.x
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Display') is not None:
            self.display = m.get('Display')
        if m.get('ZOrder') is not None:
            self.zorder = m.get('ZOrder')
        if m.get('X') is not None:
            self.x = m.get('X')
        return self


class DescribeRecordTemplatesResponseBodyTemplatesWatermarks(TeaModel):
    def __init__(
        self,
        alpha: float = None,
        width: float = None,
        height: float = None,
        y: float = None,
        url: str = None,
        display: int = None,
        zorder: int = None,
        x: float = None,
    ):
        self.alpha = alpha
        self.width = width
        self.height = height
        self.y = y
        self.url = url
        self.display = display
        self.zorder = zorder
        self.x = x

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.alpha is not None:
            result['Alpha'] = self.alpha
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        if self.y is not None:
            result['Y'] = self.y
        if self.url is not None:
            result['Url'] = self.url
        if self.display is not None:
            result['Display'] = self.display
        if self.zorder is not None:
            result['ZOrder'] = self.zorder
        if self.x is not None:
            result['X'] = self.x
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alpha') is not None:
            self.alpha = m.get('Alpha')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Display') is not None:
            self.display = m.get('Display')
        if m.get('ZOrder') is not None:
            self.zorder = m.get('ZOrder')
        if m.get('X') is not None:
            self.x = m.get('X')
        return self


class DescribeRecordTemplatesResponseBodyTemplates(TeaModel):
    def __init__(
        self,
        mns_queue: str = None,
        oss_file_prefix: str = None,
        create_time: str = None,
        clock_widgets: List[DescribeRecordTemplatesResponseBodyTemplatesClockWidgets] = None,
        oss_bucket: str = None,
        delay_stop_time: str = None,
        layout_ids: List[int] = None,
        media_encode: int = None,
        file_split_interval: int = None,
        http_callback_url: str = None,
        formats: List[str] = None,
        background_color: int = None,
        backgrounds: List[DescribeRecordTemplatesResponseBodyTemplatesBackgrounds] = None,
        watermarks: List[DescribeRecordTemplatesResponseBodyTemplatesWatermarks] = None,
        name: str = None,
        template_id: str = None,
        task_profile: str = None,
    ):
        self.mns_queue = mns_queue
        self.oss_file_prefix = oss_file_prefix
        self.create_time = create_time
        self.clock_widgets = clock_widgets
        self.oss_bucket = oss_bucket
        self.delay_stop_time = delay_stop_time
        self.layout_ids = layout_ids
        self.media_encode = media_encode
        self.file_split_interval = file_split_interval
        self.http_callback_url = http_callback_url
        self.formats = formats
        self.background_color = background_color
        self.backgrounds = backgrounds
        self.watermarks = watermarks
        self.name = name
        self.template_id = template_id
        self.task_profile = task_profile

    def validate(self):
        if self.clock_widgets:
            for k in self.clock_widgets:
                if k:
                    k.validate()
        if self.backgrounds:
            for k in self.backgrounds:
                if k:
                    k.validate()
        if self.watermarks:
            for k in self.watermarks:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.mns_queue is not None:
            result['MnsQueue'] = self.mns_queue
        if self.oss_file_prefix is not None:
            result['OssFilePrefix'] = self.oss_file_prefix
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        result['ClockWidgets'] = []
        if self.clock_widgets is not None:
            for k in self.clock_widgets:
                result['ClockWidgets'].append(k.to_map() if k else None)
        if self.oss_bucket is not None:
            result['OssBucket'] = self.oss_bucket
        if self.delay_stop_time is not None:
            result['DelayStopTime'] = self.delay_stop_time
        if self.layout_ids is not None:
            result['LayoutIds'] = self.layout_ids
        if self.media_encode is not None:
            result['MediaEncode'] = self.media_encode
        if self.file_split_interval is not None:
            result['FileSplitInterval'] = self.file_split_interval
        if self.http_callback_url is not None:
            result['HttpCallbackUrl'] = self.http_callback_url
        if self.formats is not None:
            result['Formats'] = self.formats
        if self.background_color is not None:
            result['BackgroundColor'] = self.background_color
        result['Backgrounds'] = []
        if self.backgrounds is not None:
            for k in self.backgrounds:
                result['Backgrounds'].append(k.to_map() if k else None)
        result['Watermarks'] = []
        if self.watermarks is not None:
            for k in self.watermarks:
                result['Watermarks'].append(k.to_map() if k else None)
        if self.name is not None:
            result['Name'] = self.name
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.task_profile is not None:
            result['TaskProfile'] = self.task_profile
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MnsQueue') is not None:
            self.mns_queue = m.get('MnsQueue')
        if m.get('OssFilePrefix') is not None:
            self.oss_file_prefix = m.get('OssFilePrefix')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        self.clock_widgets = []
        if m.get('ClockWidgets') is not None:
            for k in m.get('ClockWidgets'):
                temp_model = DescribeRecordTemplatesResponseBodyTemplatesClockWidgets()
                self.clock_widgets.append(temp_model.from_map(k))
        if m.get('OssBucket') is not None:
            self.oss_bucket = m.get('OssBucket')
        if m.get('DelayStopTime') is not None:
            self.delay_stop_time = m.get('DelayStopTime')
        if m.get('LayoutIds') is not None:
            self.layout_ids = m.get('LayoutIds')
        if m.get('MediaEncode') is not None:
            self.media_encode = m.get('MediaEncode')
        if m.get('FileSplitInterval') is not None:
            self.file_split_interval = m.get('FileSplitInterval')
        if m.get('HttpCallbackUrl') is not None:
            self.http_callback_url = m.get('HttpCallbackUrl')
        if m.get('Formats') is not None:
            self.formats = m.get('Formats')
        if m.get('BackgroundColor') is not None:
            self.background_color = m.get('BackgroundColor')
        self.backgrounds = []
        if m.get('Backgrounds') is not None:
            for k in m.get('Backgrounds'):
                temp_model = DescribeRecordTemplatesResponseBodyTemplatesBackgrounds()
                self.backgrounds.append(temp_model.from_map(k))
        self.watermarks = []
        if m.get('Watermarks') is not None:
            for k in m.get('Watermarks'):
                temp_model = DescribeRecordTemplatesResponseBodyTemplatesWatermarks()
                self.watermarks.append(temp_model.from_map(k))
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TaskProfile') is not None:
            self.task_profile = m.get('TaskProfile')
        return self


class DescribeRecordTemplatesResponseBody(TeaModel):
    def __init__(
        self,
        total_num: int = None,
        total_page: int = None,
        request_id: str = None,
        templates: List[DescribeRecordTemplatesResponseBodyTemplates] = None,
    ):
        self.total_num = total_num
        self.total_page = total_page
        self.request_id = request_id
        self.templates = templates

    def validate(self):
        if self.templates:
            for k in self.templates:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Templates'] = []
        if self.templates is not None:
            for k in self.templates:
                result['Templates'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.templates = []
        if m.get('Templates') is not None:
            for k in m.get('Templates'):
                temp_model = DescribeRecordTemplatesResponseBodyTemplates()
                self.templates.append(temp_model.from_map(k))
        return self


class DescribeRecordTemplatesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRecordTemplatesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeRecordTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRTCAppKeyRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        show_log: str = None,
        app_id: str = None,
    ):
        self.owner_id = owner_id
        self.show_log = show_log
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.show_log is not None:
            result['ShowLog'] = self.show_log
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ShowLog') is not None:
            self.show_log = m.get('ShowLog')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class DescribeRTCAppKeyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        app_key: str = None,
    ):
        self.request_id = request_id
        self.app_key = app_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        return self


class DescribeRTCAppKeyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRTCAppKeyResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeRTCAppKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRtcChannelCntDataRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        show_log: str = None,
        start_time: str = None,
        end_time: str = None,
        app_id: str = None,
        service_area: str = None,
        interval: str = None,
    ):
        self.owner_id = owner_id
        self.show_log = show_log
        self.start_time = start_time
        self.end_time = end_time
        self.app_id = app_id
        self.service_area = service_area
        self.interval = interval

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.show_log is not None:
            result['ShowLog'] = self.show_log
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.service_area is not None:
            result['ServiceArea'] = self.service_area
        if self.interval is not None:
            result['Interval'] = self.interval
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ShowLog') is not None:
            self.show_log = m.get('ShowLog')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ServiceArea') is not None:
            self.service_area = m.get('ServiceArea')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        return self


class DescribeRtcChannelCntDataResponseBodyChannelCntDataPerIntervalChannelCntModule(TeaModel):
    def __init__(
        self,
        active_channel_cnt: int = None,
        time_stamp: str = None,
    ):
        self.active_channel_cnt = active_channel_cnt
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.active_channel_cnt is not None:
            result['ActiveChannelCnt'] = self.active_channel_cnt
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveChannelCnt') is not None:
            self.active_channel_cnt = m.get('ActiveChannelCnt')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class DescribeRtcChannelCntDataResponseBodyChannelCntDataPerInterval(TeaModel):
    def __init__(
        self,
        channel_cnt_module: List[DescribeRtcChannelCntDataResponseBodyChannelCntDataPerIntervalChannelCntModule] = None,
    ):
        self.channel_cnt_module = channel_cnt_module

    def validate(self):
        if self.channel_cnt_module:
            for k in self.channel_cnt_module:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['ChannelCntModule'] = []
        if self.channel_cnt_module is not None:
            for k in self.channel_cnt_module:
                result['ChannelCntModule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.channel_cnt_module = []
        if m.get('ChannelCntModule') is not None:
            for k in m.get('ChannelCntModule'):
                temp_model = DescribeRtcChannelCntDataResponseBodyChannelCntDataPerIntervalChannelCntModule()
                self.channel_cnt_module.append(temp_model.from_map(k))
        return self


class DescribeRtcChannelCntDataResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        channel_cnt_data_per_interval: DescribeRtcChannelCntDataResponseBodyChannelCntDataPerInterval = None,
    ):
        self.request_id = request_id
        self.channel_cnt_data_per_interval = channel_cnt_data_per_interval

    def validate(self):
        if self.channel_cnt_data_per_interval:
            self.channel_cnt_data_per_interval.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.channel_cnt_data_per_interval is not None:
            result['ChannelCntDataPerInterval'] = self.channel_cnt_data_per_interval.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ChannelCntDataPerInterval') is not None:
            temp_model = DescribeRtcChannelCntDataResponseBodyChannelCntDataPerInterval()
            self.channel_cnt_data_per_interval = temp_model.from_map(m['ChannelCntDataPerInterval'])
        return self


class DescribeRtcChannelCntDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRtcChannelCntDataResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeRtcChannelCntDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRtcChannelDetailRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        show_log: str = None,
        app_id: str = None,
        channel_id: str = None,
        start_time: str = None,
        end_time: str = None,
        page_no: int = None,
        page_size: int = None,
    ):
        self.owner_id = owner_id
        self.show_log = show_log
        self.app_id = app_id
        self.channel_id = channel_id
        self.start_time = start_time
        self.end_time = end_time
        self.page_no = page_no
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.show_log is not None:
            result['ShowLog'] = self.show_log
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ShowLog') is not None:
            self.show_log = m.get('ShowLog')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeRtcChannelDetailResponseBodyChannelInfo(TeaModel):
    def __init__(
        self,
        sid: str = None,
        device_type: str = None,
        os: str = None,
        leave_time: str = None,
        join_time: str = None,
        platform: str = None,
        sdk_version: str = None,
        uid: str = None,
    ):
        self.sid = sid
        self.device_type = device_type
        self.os = os
        self.leave_time = leave_time
        self.join_time = join_time
        self.platform = platform
        self.sdk_version = sdk_version
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.sid is not None:
            result['Sid'] = self.sid
        if self.device_type is not None:
            result['DeviceType'] = self.device_type
        if self.os is not None:
            result['OS'] = self.os
        if self.leave_time is not None:
            result['LeaveTime'] = self.leave_time
        if self.join_time is not None:
            result['JoinTime'] = self.join_time
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.sdk_version is not None:
            result['SdkVersion'] = self.sdk_version
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Sid') is not None:
            self.sid = m.get('Sid')
        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')
        if m.get('OS') is not None:
            self.os = m.get('OS')
        if m.get('LeaveTime') is not None:
            self.leave_time = m.get('LeaveTime')
        if m.get('JoinTime') is not None:
            self.join_time = m.get('JoinTime')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('SdkVersion') is not None:
            self.sdk_version = m.get('SdkVersion')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class DescribeRtcChannelDetailResponseBody(TeaModel):
    def __init__(
        self,
        total_cnt: int = None,
        page_size: int = None,
        request_id: str = None,
        page_no: int = None,
        channel_info: List[DescribeRtcChannelDetailResponseBodyChannelInfo] = None,
        channel_id: str = None,
    ):
        self.total_cnt = total_cnt
        self.page_size = page_size
        self.request_id = request_id
        self.page_no = page_no
        self.channel_info = channel_info
        self.channel_id = channel_id

    def validate(self):
        if self.channel_info:
            for k in self.channel_info:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_cnt is not None:
            result['TotalCnt'] = self.total_cnt
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        result['ChannelInfo'] = []
        if self.channel_info is not None:
            for k in self.channel_info:
                result['ChannelInfo'].append(k.to_map() if k else None)
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCnt') is not None:
            self.total_cnt = m.get('TotalCnt')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        self.channel_info = []
        if m.get('ChannelInfo') is not None:
            for k in m.get('ChannelInfo'):
                temp_model = DescribeRtcChannelDetailResponseBodyChannelInfo()
                self.channel_info.append(temp_model.from_map(k))
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        return self


class DescribeRtcChannelDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRtcChannelDetailResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeRtcChannelDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRtcChannelListRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        show_log: str = None,
        app_id: str = None,
        time_point: str = None,
        sort_type: str = None,
        service_area: str = None,
        user_id: str = None,
        channel_id: str = None,
        page_no: int = None,
        page_size: int = None,
    ):
        self.owner_id = owner_id
        self.show_log = show_log
        self.app_id = app_id
        self.time_point = time_point
        self.sort_type = sort_type
        self.service_area = service_area
        self.user_id = user_id
        self.channel_id = channel_id
        self.page_no = page_no
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.show_log is not None:
            result['ShowLog'] = self.show_log
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.time_point is not None:
            result['TimePoint'] = self.time_point
        if self.sort_type is not None:
            result['SortType'] = self.sort_type
        if self.service_area is not None:
            result['ServiceArea'] = self.service_area
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ShowLog') is not None:
            self.show_log = m.get('ShowLog')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('TimePoint') is not None:
            self.time_point = m.get('TimePoint')
        if m.get('SortType') is not None:
            self.sort_type = m.get('SortType')
        if m.get('ServiceArea') is not None:
            self.service_area = m.get('ServiceArea')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeRtcChannelListResponseBodyChannelListChannelListCallArea(TeaModel):
    def __init__(
        self,
        call_area: List[str] = None,
    ):
        self.call_area = call_area

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.call_area is not None:
            result['CallArea'] = self.call_area
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallArea') is not None:
            self.call_area = m.get('CallArea')
        return self


class DescribeRtcChannelListResponseBodyChannelListChannelList(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        total_user_cnt: int = None,
        start_time: str = None,
        call_area: DescribeRtcChannelListResponseBodyChannelListChannelListCallArea = None,
        channel_id: str = None,
    ):
        self.end_time = end_time
        self.total_user_cnt = total_user_cnt
        self.start_time = start_time
        self.call_area = call_area
        self.channel_id = channel_id

    def validate(self):
        if self.call_area:
            self.call_area.validate()

    def to_map(self):
        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.total_user_cnt is not None:
            result['TotalUserCnt'] = self.total_user_cnt
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.call_area is not None:
            result['CallArea'] = self.call_area.to_map()
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('TotalUserCnt') is not None:
            self.total_user_cnt = m.get('TotalUserCnt')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('CallArea') is not None:
            temp_model = DescribeRtcChannelListResponseBodyChannelListChannelListCallArea()
            self.call_area = temp_model.from_map(m['CallArea'])
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        return self


class DescribeRtcChannelListResponseBodyChannelList(TeaModel):
    def __init__(
        self,
        channel_list: List[DescribeRtcChannelListResponseBodyChannelListChannelList] = None,
    ):
        self.channel_list = channel_list

    def validate(self):
        if self.channel_list:
            for k in self.channel_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['ChannelList'] = []
        if self.channel_list is not None:
            for k in self.channel_list:
                result['ChannelList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.channel_list = []
        if m.get('ChannelList') is not None:
            for k in m.get('ChannelList'):
                temp_model = DescribeRtcChannelListResponseBodyChannelListChannelList()
                self.channel_list.append(temp_model.from_map(k))
        return self


class DescribeRtcChannelListResponseBody(TeaModel):
    def __init__(
        self,
        total_cnt: int = None,
        request_id: str = None,
        page_size: int = None,
        page_no: int = None,
        channel_list: DescribeRtcChannelListResponseBodyChannelList = None,
    ):
        self.total_cnt = total_cnt
        self.request_id = request_id
        self.page_size = page_size
        self.page_no = page_no
        self.channel_list = channel_list

    def validate(self):
        if self.channel_list:
            self.channel_list.validate()

    def to_map(self):
        result = dict()
        if self.total_cnt is not None:
            result['TotalCnt'] = self.total_cnt
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.channel_list is not None:
            result['ChannelList'] = self.channel_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCnt') is not None:
            self.total_cnt = m.get('TotalCnt')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('ChannelList') is not None:
            temp_model = DescribeRtcChannelListResponseBodyChannelList()
            self.channel_list = temp_model.from_map(m['ChannelList'])
        return self


class DescribeRtcChannelListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRtcChannelListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeRtcChannelListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRtcChannelMetricRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        show_log: str = None,
        time_point: str = None,
        app_id: str = None,
        channel_id: str = None,
    ):
        self.owner_id = owner_id
        self.show_log = show_log
        self.time_point = time_point
        self.app_id = app_id
        self.channel_id = channel_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.show_log is not None:
            result['ShowLog'] = self.show_log
        if self.time_point is not None:
            result['TimePoint'] = self.time_point
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ShowLog') is not None:
            self.show_log = m.get('ShowLog')
        if m.get('TimePoint') is not None:
            self.time_point = m.get('TimePoint')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        return self


class DescribeRtcChannelMetricResponseBodyChannelMetricInfoDurationSubDuration(TeaModel):
    def __init__(
        self,
        video_720: int = None,
        video_1080: int = None,
        video_360: int = None,
        content: int = None,
        audio: int = None,
    ):
        self.video_720 = video_720
        self.video_1080 = video_1080
        self.video_360 = video_360
        self.content = content
        self.audio = audio

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.video_720 is not None:
            result['Video720'] = self.video_720
        if self.video_1080 is not None:
            result['Video1080'] = self.video_1080
        if self.video_360 is not None:
            result['Video360'] = self.video_360
        if self.content is not None:
            result['Content'] = self.content
        if self.audio is not None:
            result['Audio'] = self.audio
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Video720') is not None:
            self.video_720 = m.get('Video720')
        if m.get('Video1080') is not None:
            self.video_1080 = m.get('Video1080')
        if m.get('Video360') is not None:
            self.video_360 = m.get('Video360')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Audio') is not None:
            self.audio = m.get('Audio')
        return self


class DescribeRtcChannelMetricResponseBodyChannelMetricInfoDurationPubDuration(TeaModel):
    def __init__(
        self,
        video_720: int = None,
        video_1080: int = None,
        video_360: int = None,
        content: int = None,
        audio: int = None,
    ):
        self.video_720 = video_720
        self.video_1080 = video_1080
        self.video_360 = video_360
        self.content = content
        self.audio = audio

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.video_720 is not None:
            result['Video720'] = self.video_720
        if self.video_1080 is not None:
            result['Video1080'] = self.video_1080
        if self.video_360 is not None:
            result['Video360'] = self.video_360
        if self.content is not None:
            result['Content'] = self.content
        if self.audio is not None:
            result['Audio'] = self.audio
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Video720') is not None:
            self.video_720 = m.get('Video720')
        if m.get('Video1080') is not None:
            self.video_1080 = m.get('Video1080')
        if m.get('Video360') is not None:
            self.video_360 = m.get('Video360')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Audio') is not None:
            self.audio = m.get('Audio')
        return self


class DescribeRtcChannelMetricResponseBodyChannelMetricInfoDuration(TeaModel):
    def __init__(
        self,
        sub_duration: DescribeRtcChannelMetricResponseBodyChannelMetricInfoDurationSubDuration = None,
        pub_duration: DescribeRtcChannelMetricResponseBodyChannelMetricInfoDurationPubDuration = None,
    ):
        self.sub_duration = sub_duration
        self.pub_duration = pub_duration

    def validate(self):
        if self.sub_duration:
            self.sub_duration.validate()
        if self.pub_duration:
            self.pub_duration.validate()

    def to_map(self):
        result = dict()
        if self.sub_duration is not None:
            result['SubDuration'] = self.sub_duration.to_map()
        if self.pub_duration is not None:
            result['PubDuration'] = self.pub_duration.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SubDuration') is not None:
            temp_model = DescribeRtcChannelMetricResponseBodyChannelMetricInfoDurationSubDuration()
            self.sub_duration = temp_model.from_map(m['SubDuration'])
        if m.get('PubDuration') is not None:
            temp_model = DescribeRtcChannelMetricResponseBodyChannelMetricInfoDurationPubDuration()
            self.pub_duration = temp_model.from_map(m['PubDuration'])
        return self


class DescribeRtcChannelMetricResponseBodyChannelMetricInfoChannelMetric(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        start_time: str = None,
        sub_user_count: int = None,
        channel_id: str = None,
        user_count: int = None,
        pub_user_count: int = None,
    ):
        self.end_time = end_time
        self.start_time = start_time
        self.sub_user_count = sub_user_count
        self.channel_id = channel_id
        self.user_count = user_count
        self.pub_user_count = pub_user_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.sub_user_count is not None:
            result['SubUserCount'] = self.sub_user_count
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.user_count is not None:
            result['UserCount'] = self.user_count
        if self.pub_user_count is not None:
            result['PubUserCount'] = self.pub_user_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('SubUserCount') is not None:
            self.sub_user_count = m.get('SubUserCount')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('UserCount') is not None:
            self.user_count = m.get('UserCount')
        if m.get('PubUserCount') is not None:
            self.pub_user_count = m.get('PubUserCount')
        return self


class DescribeRtcChannelMetricResponseBodyChannelMetricInfo(TeaModel):
    def __init__(
        self,
        duration: DescribeRtcChannelMetricResponseBodyChannelMetricInfoDuration = None,
        channel_metric: DescribeRtcChannelMetricResponseBodyChannelMetricInfoChannelMetric = None,
    ):
        self.duration = duration
        self.channel_metric = channel_metric

    def validate(self):
        if self.duration:
            self.duration.validate()
        if self.channel_metric:
            self.channel_metric.validate()

    def to_map(self):
        result = dict()
        if self.duration is not None:
            result['Duration'] = self.duration.to_map()
        if self.channel_metric is not None:
            result['ChannelMetric'] = self.channel_metric.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            temp_model = DescribeRtcChannelMetricResponseBodyChannelMetricInfoDuration()
            self.duration = temp_model.from_map(m['Duration'])
        if m.get('ChannelMetric') is not None:
            temp_model = DescribeRtcChannelMetricResponseBodyChannelMetricInfoChannelMetric()
            self.channel_metric = temp_model.from_map(m['ChannelMetric'])
        return self


class DescribeRtcChannelMetricResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        channel_metric_info: DescribeRtcChannelMetricResponseBodyChannelMetricInfo = None,
    ):
        self.request_id = request_id
        self.channel_metric_info = channel_metric_info

    def validate(self):
        if self.channel_metric_info:
            self.channel_metric_info.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.channel_metric_info is not None:
            result['ChannelMetricInfo'] = self.channel_metric_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ChannelMetricInfo') is not None:
            temp_model = DescribeRtcChannelMetricResponseBodyChannelMetricInfo()
            self.channel_metric_info = temp_model.from_map(m['ChannelMetricInfo'])
        return self


class DescribeRtcChannelMetricResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRtcChannelMetricResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeRtcChannelMetricResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRtcChannelMetricsRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        show_log: str = None,
        app_id: str = None,
        channel_id: str = None,
        pub_uid: str = None,
        sub_uid: str = None,
        start_time: str = None,
        end_time: str = None,
    ):
        self.owner_id = owner_id
        self.show_log = show_log
        self.app_id = app_id
        self.channel_id = channel_id
        self.pub_uid = pub_uid
        self.sub_uid = sub_uid
        self.start_time = start_time
        self.end_time = end_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.show_log is not None:
            result['ShowLog'] = self.show_log
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.pub_uid is not None:
            result['PubUid'] = self.pub_uid
        if self.sub_uid is not None:
            result['SubUid'] = self.sub_uid
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ShowLog') is not None:
            self.show_log = m.get('ShowLog')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('PubUid') is not None:
            self.pub_uid = m.get('PubUid')
        if m.get('SubUid') is not None:
            self.sub_uid = m.get('SubUid')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class DescribeRtcChannelMetricsResponseBodyMetrics(TeaModel):
    def __init__(
        self,
        mid: str = None,
        kvs: List[str] = None,
        uid: str = None,
    ):
        self.mid = mid
        self.kvs = kvs
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.mid is not None:
            result['Mid'] = self.mid
        if self.kvs is not None:
            result['KVs'] = self.kvs
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Mid') is not None:
            self.mid = m.get('Mid')
        if m.get('KVs') is not None:
            self.kvs = m.get('KVs')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class DescribeRtcChannelMetricsResponseBody(TeaModel):
    def __init__(
        self,
        metrics: List[DescribeRtcChannelMetricsResponseBodyMetrics] = None,
        request_id: str = None,
    ):
        self.metrics = metrics
        self.request_id = request_id

    def validate(self):
        if self.metrics:
            for k in self.metrics:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Metrics'] = []
        if self.metrics is not None:
            for k in self.metrics:
                result['Metrics'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.metrics = []
        if m.get('Metrics') is not None:
            for k in m.get('Metrics'):
                temp_model = DescribeRtcChannelMetricsResponseBodyMetrics()
                self.metrics.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeRtcChannelMetricsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRtcChannelMetricsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeRtcChannelMetricsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRtcChannelsRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        show_log: str = None,
        app_id: str = None,
        start_time: str = None,
        end_time: str = None,
        channel_id: str = None,
        page_no: int = None,
        page_size: int = None,
    ):
        self.owner_id = owner_id
        self.show_log = show_log
        self.app_id = app_id
        self.start_time = start_time
        self.end_time = end_time
        self.channel_id = channel_id
        self.page_no = page_no
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.show_log is not None:
            result['ShowLog'] = self.show_log
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ShowLog') is not None:
            self.show_log = m.get('ShowLog')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeRtcChannelsResponseBodyChannels(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        start_time: str = None,
        channel_id: str = None,
        finished: bool = None,
    ):
        self.end_time = end_time
        self.start_time = start_time
        self.channel_id = channel_id
        self.finished = finished

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.finished is not None:
            result['Finished'] = self.finished
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('Finished') is not None:
            self.finished = m.get('Finished')
        return self


class DescribeRtcChannelsResponseBody(TeaModel):
    def __init__(
        self,
        total_cnt: int = None,
        request_id: str = None,
        page_size: int = None,
        page_no: int = None,
        channels: List[DescribeRtcChannelsResponseBodyChannels] = None,
    ):
        self.total_cnt = total_cnt
        self.request_id = request_id
        self.page_size = page_size
        self.page_no = page_no
        self.channels = channels

    def validate(self):
        if self.channels:
            for k in self.channels:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_cnt is not None:
            result['TotalCnt'] = self.total_cnt
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        result['Channels'] = []
        if self.channels is not None:
            for k in self.channels:
                result['Channels'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCnt') is not None:
            self.total_cnt = m.get('TotalCnt')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        self.channels = []
        if m.get('Channels') is not None:
            for k in m.get('Channels'):
                temp_model = DescribeRtcChannelsResponseBodyChannels()
                self.channels.append(temp_model.from_map(k))
        return self


class DescribeRtcChannelsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRtcChannelsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeRtcChannelsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRtcChannelUserListRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        show_log: str = None,
        app_id: str = None,
        channel_id: str = None,
        page_no: int = None,
        page_size: int = None,
        time_point: str = None,
    ):
        self.owner_id = owner_id
        self.show_log = show_log
        self.app_id = app_id
        self.channel_id = channel_id
        self.page_no = page_no
        self.page_size = page_size
        self.time_point = time_point

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.show_log is not None:
            result['ShowLog'] = self.show_log
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.time_point is not None:
            result['TimePoint'] = self.time_point
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ShowLog') is not None:
            self.show_log = m.get('ShowLog')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TimePoint') is not None:
            self.time_point = m.get('TimePoint')
        return self


class DescribeRtcChannelUserListResponseBodyUserListUserList(TeaModel):
    def __init__(
        self,
        sub_video_720: int = None,
        sub_video_1080: int = None,
        sub_content: int = None,
        user_id: str = None,
        pub_video_360: int = None,
        sub_video_360: int = None,
        service_area: str = None,
        end_time: str = None,
        start_time: str = None,
        pub_content: int = None,
        channel_id: str = None,
        pub_video_1080: int = None,
        pub_audio: int = None,
        pub_video_720: int = None,
        sub_audio: int = None,
    ):
        self.sub_video_720 = sub_video_720
        self.sub_video_1080 = sub_video_1080
        self.sub_content = sub_content
        self.user_id = user_id
        self.pub_video_360 = pub_video_360
        self.sub_video_360 = sub_video_360
        self.service_area = service_area
        self.end_time = end_time
        self.start_time = start_time
        self.pub_content = pub_content
        self.channel_id = channel_id
        self.pub_video_1080 = pub_video_1080
        self.pub_audio = pub_audio
        self.pub_video_720 = pub_video_720
        self.sub_audio = sub_audio

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.sub_video_720 is not None:
            result['SubVideo720'] = self.sub_video_720
        if self.sub_video_1080 is not None:
            result['SubVideo1080'] = self.sub_video_1080
        if self.sub_content is not None:
            result['SubContent'] = self.sub_content
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.pub_video_360 is not None:
            result['PubVideo360'] = self.pub_video_360
        if self.sub_video_360 is not None:
            result['SubVideo360'] = self.sub_video_360
        if self.service_area is not None:
            result['ServiceArea'] = self.service_area
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.pub_content is not None:
            result['PubContent'] = self.pub_content
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.pub_video_1080 is not None:
            result['PubVideo1080'] = self.pub_video_1080
        if self.pub_audio is not None:
            result['PubAudio'] = self.pub_audio
        if self.pub_video_720 is not None:
            result['PubVideo720'] = self.pub_video_720
        if self.sub_audio is not None:
            result['SubAudio'] = self.sub_audio
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SubVideo720') is not None:
            self.sub_video_720 = m.get('SubVideo720')
        if m.get('SubVideo1080') is not None:
            self.sub_video_1080 = m.get('SubVideo1080')
        if m.get('SubContent') is not None:
            self.sub_content = m.get('SubContent')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('PubVideo360') is not None:
            self.pub_video_360 = m.get('PubVideo360')
        if m.get('SubVideo360') is not None:
            self.sub_video_360 = m.get('SubVideo360')
        if m.get('ServiceArea') is not None:
            self.service_area = m.get('ServiceArea')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('PubContent') is not None:
            self.pub_content = m.get('PubContent')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('PubVideo1080') is not None:
            self.pub_video_1080 = m.get('PubVideo1080')
        if m.get('PubAudio') is not None:
            self.pub_audio = m.get('PubAudio')
        if m.get('PubVideo720') is not None:
            self.pub_video_720 = m.get('PubVideo720')
        if m.get('SubAudio') is not None:
            self.sub_audio = m.get('SubAudio')
        return self


class DescribeRtcChannelUserListResponseBodyUserList(TeaModel):
    def __init__(
        self,
        user_list: List[DescribeRtcChannelUserListResponseBodyUserListUserList] = None,
    ):
        self.user_list = user_list

    def validate(self):
        if self.user_list:
            for k in self.user_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['UserList'] = []
        if self.user_list is not None:
            for k in self.user_list:
                result['UserList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.user_list = []
        if m.get('UserList') is not None:
            for k in m.get('UserList'):
                temp_model = DescribeRtcChannelUserListResponseBodyUserListUserList()
                self.user_list.append(temp_model.from_map(k))
        return self


class DescribeRtcChannelUserListResponseBody(TeaModel):
    def __init__(
        self,
        total_cnt: int = None,
        request_id: str = None,
        page_size: int = None,
        page_no: int = None,
        user_list: DescribeRtcChannelUserListResponseBodyUserList = None,
    ):
        self.total_cnt = total_cnt
        self.request_id = request_id
        self.page_size = page_size
        self.page_no = page_no
        self.user_list = user_list

    def validate(self):
        if self.user_list:
            self.user_list.validate()

    def to_map(self):
        result = dict()
        if self.total_cnt is not None:
            result['TotalCnt'] = self.total_cnt
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.user_list is not None:
            result['UserList'] = self.user_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCnt') is not None:
            self.total_cnt = m.get('TotalCnt')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('UserList') is not None:
            temp_model = DescribeRtcChannelUserListResponseBodyUserList()
            self.user_list = temp_model.from_map(m['UserList'])
        return self


class DescribeRtcChannelUserListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRtcChannelUserListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeRtcChannelUserListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRtcDurationDataRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        show_log: str = None,
        start_time: str = None,
        end_time: str = None,
        app_id: str = None,
        service_area: str = None,
        interval: str = None,
    ):
        self.owner_id = owner_id
        self.show_log = show_log
        self.start_time = start_time
        self.end_time = end_time
        self.app_id = app_id
        self.service_area = service_area
        self.interval = interval

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.show_log is not None:
            result['ShowLog'] = self.show_log
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.service_area is not None:
            result['ServiceArea'] = self.service_area
        if self.interval is not None:
            result['Interval'] = self.interval
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ShowLog') is not None:
            self.show_log = m.get('ShowLog')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ServiceArea') is not None:
            self.service_area = m.get('ServiceArea')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        return self


class DescribeRtcDurationDataResponseBodyDurationDataPerIntervalDurationModule(TeaModel):
    def __init__(
        self,
        content_duration: int = None,
        v_720duration: int = None,
        v_360duration: int = None,
        audio_duration: int = None,
        time_stamp: str = None,
        v_1080duration: int = None,
        total_duration: int = None,
    ):
        self.content_duration = content_duration
        self.v_720duration = v_720duration
        self.v_360duration = v_360duration
        self.audio_duration = audio_duration
        self.time_stamp = time_stamp
        self.v_1080duration = v_1080duration
        self.total_duration = total_duration

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.content_duration is not None:
            result['ContentDuration'] = self.content_duration
        if self.v_720duration is not None:
            result['V720Duration'] = self.v_720duration
        if self.v_360duration is not None:
            result['V360Duration'] = self.v_360duration
        if self.audio_duration is not None:
            result['AudioDuration'] = self.audio_duration
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.v_1080duration is not None:
            result['V1080Duration'] = self.v_1080duration
        if self.total_duration is not None:
            result['TotalDuration'] = self.total_duration
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContentDuration') is not None:
            self.content_duration = m.get('ContentDuration')
        if m.get('V720Duration') is not None:
            self.v_720duration = m.get('V720Duration')
        if m.get('V360Duration') is not None:
            self.v_360duration = m.get('V360Duration')
        if m.get('AudioDuration') is not None:
            self.audio_duration = m.get('AudioDuration')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('V1080Duration') is not None:
            self.v_1080duration = m.get('V1080Duration')
        if m.get('TotalDuration') is not None:
            self.total_duration = m.get('TotalDuration')
        return self


class DescribeRtcDurationDataResponseBodyDurationDataPerInterval(TeaModel):
    def __init__(
        self,
        duration_module: List[DescribeRtcDurationDataResponseBodyDurationDataPerIntervalDurationModule] = None,
    ):
        self.duration_module = duration_module

    def validate(self):
        if self.duration_module:
            for k in self.duration_module:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['DurationModule'] = []
        if self.duration_module is not None:
            for k in self.duration_module:
                result['DurationModule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.duration_module = []
        if m.get('DurationModule') is not None:
            for k in m.get('DurationModule'):
                temp_model = DescribeRtcDurationDataResponseBodyDurationDataPerIntervalDurationModule()
                self.duration_module.append(temp_model.from_map(k))
        return self


class DescribeRtcDurationDataResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        duration_data_per_interval: DescribeRtcDurationDataResponseBodyDurationDataPerInterval = None,
    ):
        self.request_id = request_id
        self.duration_data_per_interval = duration_data_per_interval

    def validate(self):
        if self.duration_data_per_interval:
            self.duration_data_per_interval.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.duration_data_per_interval is not None:
            result['DurationDataPerInterval'] = self.duration_data_per_interval.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DurationDataPerInterval') is not None:
            temp_model = DescribeRtcDurationDataResponseBodyDurationDataPerInterval()
            self.duration_data_per_interval = temp_model.from_map(m['DurationDataPerInterval'])
        return self


class DescribeRtcDurationDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRtcDurationDataResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeRtcDurationDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRtcPeakChannelCntDataRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        show_log: str = None,
        start_time: str = None,
        end_time: str = None,
        app_id: str = None,
        service_area: str = None,
        interval: str = None,
    ):
        self.owner_id = owner_id
        self.show_log = show_log
        self.start_time = start_time
        self.end_time = end_time
        self.app_id = app_id
        self.service_area = service_area
        self.interval = interval

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.show_log is not None:
            result['ShowLog'] = self.show_log
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.service_area is not None:
            result['ServiceArea'] = self.service_area
        if self.interval is not None:
            result['Interval'] = self.interval
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ShowLog') is not None:
            self.show_log = m.get('ShowLog')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ServiceArea') is not None:
            self.service_area = m.get('ServiceArea')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        return self


class DescribeRtcPeakChannelCntDataResponseBodyPeakChannelCntDataPerIntervalPeakChannelCntModule(TeaModel):
    def __init__(
        self,
        active_channel_peak_time: str = None,
        time_stamp: str = None,
        active_channel_peak: int = None,
    ):
        self.active_channel_peak_time = active_channel_peak_time
        self.time_stamp = time_stamp
        self.active_channel_peak = active_channel_peak

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.active_channel_peak_time is not None:
            result['ActiveChannelPeakTime'] = self.active_channel_peak_time
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.active_channel_peak is not None:
            result['ActiveChannelPeak'] = self.active_channel_peak
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveChannelPeakTime') is not None:
            self.active_channel_peak_time = m.get('ActiveChannelPeakTime')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('ActiveChannelPeak') is not None:
            self.active_channel_peak = m.get('ActiveChannelPeak')
        return self


class DescribeRtcPeakChannelCntDataResponseBodyPeakChannelCntDataPerInterval(TeaModel):
    def __init__(
        self,
        peak_channel_cnt_module: List[DescribeRtcPeakChannelCntDataResponseBodyPeakChannelCntDataPerIntervalPeakChannelCntModule] = None,
    ):
        self.peak_channel_cnt_module = peak_channel_cnt_module

    def validate(self):
        if self.peak_channel_cnt_module:
            for k in self.peak_channel_cnt_module:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['PeakChannelCntModule'] = []
        if self.peak_channel_cnt_module is not None:
            for k in self.peak_channel_cnt_module:
                result['PeakChannelCntModule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.peak_channel_cnt_module = []
        if m.get('PeakChannelCntModule') is not None:
            for k in m.get('PeakChannelCntModule'):
                temp_model = DescribeRtcPeakChannelCntDataResponseBodyPeakChannelCntDataPerIntervalPeakChannelCntModule()
                self.peak_channel_cnt_module.append(temp_model.from_map(k))
        return self


class DescribeRtcPeakChannelCntDataResponseBody(TeaModel):
    def __init__(
        self,
        peak_channel_cnt_data_per_interval: DescribeRtcPeakChannelCntDataResponseBodyPeakChannelCntDataPerInterval = None,
        request_id: str = None,
    ):
        self.peak_channel_cnt_data_per_interval = peak_channel_cnt_data_per_interval
        self.request_id = request_id

    def validate(self):
        if self.peak_channel_cnt_data_per_interval:
            self.peak_channel_cnt_data_per_interval.validate()

    def to_map(self):
        result = dict()
        if self.peak_channel_cnt_data_per_interval is not None:
            result['PeakChannelCntDataPerInterval'] = self.peak_channel_cnt_data_per_interval.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PeakChannelCntDataPerInterval') is not None:
            temp_model = DescribeRtcPeakChannelCntDataResponseBodyPeakChannelCntDataPerInterval()
            self.peak_channel_cnt_data_per_interval = temp_model.from_map(m['PeakChannelCntDataPerInterval'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeRtcPeakChannelCntDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRtcPeakChannelCntDataResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeRtcPeakChannelCntDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRtcPeakUserCntDataRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        show_log: str = None,
        start_time: str = None,
        end_time: str = None,
        app_id: str = None,
        service_area: str = None,
        interval: str = None,
    ):
        self.owner_id = owner_id
        self.show_log = show_log
        self.start_time = start_time
        self.end_time = end_time
        self.app_id = app_id
        self.service_area = service_area
        self.interval = interval

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.show_log is not None:
            result['ShowLog'] = self.show_log
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.service_area is not None:
            result['ServiceArea'] = self.service_area
        if self.interval is not None:
            result['Interval'] = self.interval
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ShowLog') is not None:
            self.show_log = m.get('ShowLog')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ServiceArea') is not None:
            self.service_area = m.get('ServiceArea')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        return self


class DescribeRtcPeakUserCntDataResponseBodyPeakUserCntDataPerIntervalPeakUserCntModule(TeaModel):
    def __init__(
        self,
        active_user_peak_time: str = None,
        time_stamp: str = None,
        active_user_peak: int = None,
    ):
        self.active_user_peak_time = active_user_peak_time
        self.time_stamp = time_stamp
        self.active_user_peak = active_user_peak

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.active_user_peak_time is not None:
            result['ActiveUserPeakTime'] = self.active_user_peak_time
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.active_user_peak is not None:
            result['ActiveUserPeak'] = self.active_user_peak
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveUserPeakTime') is not None:
            self.active_user_peak_time = m.get('ActiveUserPeakTime')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('ActiveUserPeak') is not None:
            self.active_user_peak = m.get('ActiveUserPeak')
        return self


class DescribeRtcPeakUserCntDataResponseBodyPeakUserCntDataPerInterval(TeaModel):
    def __init__(
        self,
        peak_user_cnt_module: List[DescribeRtcPeakUserCntDataResponseBodyPeakUserCntDataPerIntervalPeakUserCntModule] = None,
    ):
        self.peak_user_cnt_module = peak_user_cnt_module

    def validate(self):
        if self.peak_user_cnt_module:
            for k in self.peak_user_cnt_module:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['PeakUserCntModule'] = []
        if self.peak_user_cnt_module is not None:
            for k in self.peak_user_cnt_module:
                result['PeakUserCntModule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.peak_user_cnt_module = []
        if m.get('PeakUserCntModule') is not None:
            for k in m.get('PeakUserCntModule'):
                temp_model = DescribeRtcPeakUserCntDataResponseBodyPeakUserCntDataPerIntervalPeakUserCntModule()
                self.peak_user_cnt_module.append(temp_model.from_map(k))
        return self


class DescribeRtcPeakUserCntDataResponseBody(TeaModel):
    def __init__(
        self,
        peak_user_cnt_data_per_interval: DescribeRtcPeakUserCntDataResponseBodyPeakUserCntDataPerInterval = None,
        request_id: str = None,
    ):
        self.peak_user_cnt_data_per_interval = peak_user_cnt_data_per_interval
        self.request_id = request_id

    def validate(self):
        if self.peak_user_cnt_data_per_interval:
            self.peak_user_cnt_data_per_interval.validate()

    def to_map(self):
        result = dict()
        if self.peak_user_cnt_data_per_interval is not None:
            result['PeakUserCntDataPerInterval'] = self.peak_user_cnt_data_per_interval.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PeakUserCntDataPerInterval') is not None:
            temp_model = DescribeRtcPeakUserCntDataResponseBodyPeakUserCntDataPerInterval()
            self.peak_user_cnt_data_per_interval = temp_model.from_map(m['PeakUserCntDataPerInterval'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeRtcPeakUserCntDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRtcPeakUserCntDataResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeRtcPeakUserCntDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRtcScaleRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        show_log: str = None,
        app_id: str = None,
        start_time: str = None,
        end_time: str = None,
    ):
        self.owner_id = owner_id
        self.show_log = show_log
        self.app_id = app_id
        self.start_time = start_time
        self.end_time = end_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.show_log is not None:
            result['ShowLog'] = self.show_log
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ShowLog') is not None:
            self.show_log = m.get('ShowLog')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class DescribeRtcScaleResponseBodyScale(TeaModel):
    def __init__(
        self,
        session_count: int = None,
        time: str = None,
        channel_count: int = None,
        audio_duration: int = None,
        user_count: int = None,
        video_duration: int = None,
    ):
        self.session_count = session_count
        self.time = time
        self.channel_count = channel_count
        self.audio_duration = audio_duration
        self.user_count = user_count
        self.video_duration = video_duration

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.session_count is not None:
            result['SessionCount'] = self.session_count
        if self.time is not None:
            result['Time'] = self.time
        if self.channel_count is not None:
            result['ChannelCount'] = self.channel_count
        if self.audio_duration is not None:
            result['AudioDuration'] = self.audio_duration
        if self.user_count is not None:
            result['UserCount'] = self.user_count
        if self.video_duration is not None:
            result['VideoDuration'] = self.video_duration
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SessionCount') is not None:
            self.session_count = m.get('SessionCount')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('ChannelCount') is not None:
            self.channel_count = m.get('ChannelCount')
        if m.get('AudioDuration') is not None:
            self.audio_duration = m.get('AudioDuration')
        if m.get('UserCount') is not None:
            self.user_count = m.get('UserCount')
        if m.get('VideoDuration') is not None:
            self.video_duration = m.get('VideoDuration')
        return self


class DescribeRtcScaleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        scale: List[DescribeRtcScaleResponseBodyScale] = None,
    ):
        self.request_id = request_id
        self.scale = scale

    def validate(self):
        if self.scale:
            for k in self.scale:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Scale'] = []
        if self.scale is not None:
            for k in self.scale:
                result['Scale'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.scale = []
        if m.get('Scale') is not None:
            for k in m.get('Scale'):
                temp_model = DescribeRtcScaleResponseBodyScale()
                self.scale.append(temp_model.from_map(k))
        return self


class DescribeRtcScaleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRtcScaleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeRtcScaleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRtcScaleDetailRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        show_log: str = None,
        app_id: str = None,
        start_time: str = None,
        end_time: str = None,
    ):
        self.owner_id = owner_id
        self.show_log = show_log
        self.app_id = app_id
        self.start_time = start_time
        self.end_time = end_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.show_log is not None:
            result['ShowLog'] = self.show_log
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ShowLog') is not None:
            self.show_log = m.get('ShowLog')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class DescribeRtcScaleDetailResponseBodyScale(TeaModel):
    def __init__(
        self,
        cc: int = None,
        ts: str = None,
        uc: int = None,
    ):
        self.cc = cc
        self.ts = ts
        self.uc = uc

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cc is not None:
            result['CC'] = self.cc
        if self.ts is not None:
            result['TS'] = self.ts
        if self.uc is not None:
            result['UC'] = self.uc
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CC') is not None:
            self.cc = m.get('CC')
        if m.get('TS') is not None:
            self.ts = m.get('TS')
        if m.get('UC') is not None:
            self.uc = m.get('UC')
        return self


class DescribeRtcScaleDetailResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        scale: List[DescribeRtcScaleDetailResponseBodyScale] = None,
    ):
        self.request_id = request_id
        self.scale = scale

    def validate(self):
        if self.scale:
            for k in self.scale:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Scale'] = []
        if self.scale is not None:
            for k in self.scale:
                result['Scale'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.scale = []
        if m.get('Scale') is not None:
            for k in m.get('Scale'):
                temp_model = DescribeRtcScaleDetailResponseBodyScale()
                self.scale.append(temp_model.from_map(k))
        return self


class DescribeRtcScaleDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRtcScaleDetailResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeRtcScaleDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRtcUserCntDataRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        show_log: str = None,
        start_time: str = None,
        end_time: str = None,
        app_id: str = None,
        service_area: str = None,
        interval: str = None,
    ):
        self.owner_id = owner_id
        self.show_log = show_log
        self.start_time = start_time
        self.end_time = end_time
        self.app_id = app_id
        self.service_area = service_area
        self.interval = interval

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.show_log is not None:
            result['ShowLog'] = self.show_log
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.service_area is not None:
            result['ServiceArea'] = self.service_area
        if self.interval is not None:
            result['Interval'] = self.interval
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ShowLog') is not None:
            self.show_log = m.get('ShowLog')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ServiceArea') is not None:
            self.service_area = m.get('ServiceArea')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        return self


class DescribeRtcUserCntDataResponseBodyUserCntDataPerIntervalUserCntModule(TeaModel):
    def __init__(
        self,
        active_user_cnt: int = None,
        time_stamp: str = None,
    ):
        self.active_user_cnt = active_user_cnt
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.active_user_cnt is not None:
            result['ActiveUserCnt'] = self.active_user_cnt
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveUserCnt') is not None:
            self.active_user_cnt = m.get('ActiveUserCnt')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class DescribeRtcUserCntDataResponseBodyUserCntDataPerInterval(TeaModel):
    def __init__(
        self,
        user_cnt_module: List[DescribeRtcUserCntDataResponseBodyUserCntDataPerIntervalUserCntModule] = None,
    ):
        self.user_cnt_module = user_cnt_module

    def validate(self):
        if self.user_cnt_module:
            for k in self.user_cnt_module:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['UserCntModule'] = []
        if self.user_cnt_module is not None:
            for k in self.user_cnt_module:
                result['UserCntModule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.user_cnt_module = []
        if m.get('UserCntModule') is not None:
            for k in m.get('UserCntModule'):
                temp_model = DescribeRtcUserCntDataResponseBodyUserCntDataPerIntervalUserCntModule()
                self.user_cnt_module.append(temp_model.from_map(k))
        return self


class DescribeRtcUserCntDataResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        user_cnt_data_per_interval: DescribeRtcUserCntDataResponseBodyUserCntDataPerInterval = None,
    ):
        self.request_id = request_id
        self.user_cnt_data_per_interval = user_cnt_data_per_interval

    def validate(self):
        if self.user_cnt_data_per_interval:
            self.user_cnt_data_per_interval.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.user_cnt_data_per_interval is not None:
            result['UserCntDataPerInterval'] = self.user_cnt_data_per_interval.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UserCntDataPerInterval') is not None:
            temp_model = DescribeRtcUserCntDataResponseBodyUserCntDataPerInterval()
            self.user_cnt_data_per_interval = temp_model.from_map(m['UserCntDataPerInterval'])
        return self


class DescribeRtcUserCntDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRtcUserCntDataResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeRtcUserCntDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRtcUserEventsRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        show_log: str = None,
        app_id: str = None,
        uid: str = None,
        channel_id: str = None,
        start_time: str = None,
        end_time: str = None,
    ):
        self.owner_id = owner_id
        self.show_log = show_log
        self.app_id = app_id
        self.uid = uid
        self.channel_id = channel_id
        self.start_time = start_time
        self.end_time = end_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.show_log is not None:
            result['ShowLog'] = self.show_log
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ShowLog') is not None:
            self.show_log = m.get('ShowLog')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class DescribeRtcUserEventsResponseBodyEvents(TeaModel):
    def __init__(
        self,
        event_id: str = None,
        event_time: int = None,
        category: str = None,
    ):
        self.event_id = event_id
        self.event_time = event_time
        self.category = category

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.event_time is not None:
            result['EventTime'] = self.event_time
        if self.category is not None:
            result['Category'] = self.category
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('EventTime') is not None:
            self.event_time = m.get('EventTime')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        return self


class DescribeRtcUserEventsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        events: List[DescribeRtcUserEventsResponseBodyEvents] = None,
    ):
        self.request_id = request_id
        self.events = events

    def validate(self):
        if self.events:
            for k in self.events:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Events'] = []
        if self.events is not None:
            for k in self.events:
                result['Events'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.events = []
        if m.get('Events') is not None:
            for k in m.get('Events'):
                temp_model = DescribeRtcUserEventsResponseBodyEvents()
                self.events.append(temp_model.from_map(k))
        return self


class DescribeRtcUserEventsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRtcUserEventsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeRtcUserEventsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRtcUserListRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        show_log: str = None,
        start_time: str = None,
        end_time: str = None,
        app_id: str = None,
        channel_id: str = None,
        pub_user: str = None,
        sub_user: str = None,
    ):
        self.owner_id = owner_id
        self.show_log = show_log
        self.start_time = start_time
        self.end_time = end_time
        self.app_id = app_id
        self.channel_id = channel_id
        self.pub_user = pub_user
        self.sub_user = sub_user

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.show_log is not None:
            result['ShowLog'] = self.show_log
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.pub_user is not None:
            result['PubUser'] = self.pub_user
        if self.sub_user is not None:
            result['SubUser'] = self.sub_user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ShowLog') is not None:
            self.show_log = m.get('ShowLog')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('PubUser') is not None:
            self.pub_user = m.get('PubUser')
        if m.get('SubUser') is not None:
            self.sub_user = m.get('SubUser')
        return self


class DescribeRtcUserListResponseBodyUserListUserList(TeaModel):
    def __init__(
        self,
        user: str = None,
    ):
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.user is not None:
            result['User'] = self.user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('User') is not None:
            self.user = m.get('User')
        return self


class DescribeRtcUserListResponseBodyUserList(TeaModel):
    def __init__(
        self,
        user_list: List[DescribeRtcUserListResponseBodyUserListUserList] = None,
    ):
        self.user_list = user_list

    def validate(self):
        if self.user_list:
            for k in self.user_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['UserList'] = []
        if self.user_list is not None:
            for k in self.user_list:
                result['UserList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.user_list = []
        if m.get('UserList') is not None:
            for k in m.get('UserList'):
                temp_model = DescribeRtcUserListResponseBodyUserListUserList()
                self.user_list.append(temp_model.from_map(k))
        return self


class DescribeRtcUserListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        user_list: DescribeRtcUserListResponseBodyUserList = None,
    ):
        self.request_id = request_id
        self.user_list = user_list

    def validate(self):
        if self.user_list:
            self.user_list.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.user_list is not None:
            result['UserList'] = self.user_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UserList') is not None:
            temp_model = DescribeRtcUserListResponseBodyUserList()
            self.user_list = temp_model.from_map(m['UserList'])
        return self


class DescribeRtcUserListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRtcUserListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeRtcUserListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUserInfoInChannelRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        show_log: str = None,
        app_id: str = None,
        channel_id: str = None,
        user_id: str = None,
    ):
        self.owner_id = owner_id
        self.show_log = show_log
        self.app_id = app_id
        self.channel_id = channel_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.show_log is not None:
            result['ShowLog'] = self.show_log
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ShowLog') is not None:
            self.show_log = m.get('ShowLog')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DescribeUserInfoInChannelResponseBodyProperty(TeaModel):
    def __init__(
        self,
        session: str = None,
        join: int = None,
        role: int = None,
    ):
        self.session = session
        self.join = join
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.session is not None:
            result['Session'] = self.session
        if self.join is not None:
            result['Join'] = self.join
        if self.role is not None:
            result['Role'] = self.role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Session') is not None:
            self.session = m.get('Session')
        if m.get('Join') is not None:
            self.join = m.get('Join')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        return self


class DescribeUserInfoInChannelResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        is_in_channel: bool = None,
        timestamp: int = None,
        is_channel_exist: bool = None,
        property: List[DescribeUserInfoInChannelResponseBodyProperty] = None,
    ):
        self.request_id = request_id
        self.is_in_channel = is_in_channel
        self.timestamp = timestamp
        self.is_channel_exist = is_channel_exist
        self.property = property

    def validate(self):
        if self.property:
            for k in self.property:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.is_in_channel is not None:
            result['IsInChannel'] = self.is_in_channel
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.is_channel_exist is not None:
            result['IsChannelExist'] = self.is_channel_exist
        result['Property'] = []
        if self.property is not None:
            for k in self.property:
                result['Property'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('IsInChannel') is not None:
            self.is_in_channel = m.get('IsInChannel')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('IsChannelExist') is not None:
            self.is_channel_exist = m.get('IsChannelExist')
        self.property = []
        if m.get('Property') is not None:
            for k in m.get('Property'):
                temp_model = DescribeUserInfoInChannelResponseBodyProperty()
                self.property.append(temp_model.from_map(k))
        return self


class DescribeUserInfoInChannelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeUserInfoInChannelResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeUserInfoInChannelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableMPURuleRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        show_log: str = None,
        app_id: str = None,
        rule_id: int = None,
    ):
        self.owner_id = owner_id
        self.show_log = show_log
        self.app_id = app_id
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.show_log is not None:
            result['ShowLog'] = self.show_log
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ShowLog') is not None:
            self.show_log = m.get('ShowLog')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class DisableMPURuleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DisableMPURuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DisableMPURuleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DisableMPURuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableMPURuleRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        show_log: str = None,
        app_id: str = None,
        rule_id: int = None,
    ):
        self.owner_id = owner_id
        self.show_log = show_log
        self.app_id = app_id
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.show_log is not None:
            result['ShowLog'] = self.show_log
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ShowLog') is not None:
            self.show_log = m.get('ShowLog')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class EnableMPURuleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class EnableMPURuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EnableMPURuleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = EnableMPURuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMPUTaskStatusRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        show_log: str = None,
        app_id: str = None,
        task_id: str = None,
    ):
        self.owner_id = owner_id
        self.show_log = show_log
        self.app_id = app_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.show_log is not None:
            result['ShowLog'] = self.show_log
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ShowLog') is not None:
            self.show_log = m.get('ShowLog')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetMPUTaskStatusResponseBody(TeaModel):
    def __init__(
        self,
        status: int = None,
        request_id: str = None,
    ):
        self.status = status
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetMPUTaskStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetMPUTaskStatusResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetMPUTaskStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAppRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        show_log: str = None,
        app_id: str = None,
        app_name: str = None,
    ):
        self.owner_id = owner_id
        self.show_log = show_log
        self.app_id = app_id
        self.app_name = app_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.show_log is not None:
            result['ShowLog'] = self.show_log
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ShowLog') is not None:
            self.show_log = m.get('ShowLog')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        return self


class ModifyAppResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyAppResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyConferenceRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        show_log: str = None,
        app_id: str = None,
        conference_id: str = None,
        conference_name: str = None,
        start_time: str = None,
        type: str = None,
        remind_notice: int = None,
    ):
        self.owner_id = owner_id
        self.show_log = show_log
        self.app_id = app_id
        self.conference_id = conference_id
        self.conference_name = conference_name
        self.start_time = start_time
        self.type = type
        self.remind_notice = remind_notice

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.show_log is not None:
            result['ShowLog'] = self.show_log
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.conference_id is not None:
            result['ConferenceId'] = self.conference_id
        if self.conference_name is not None:
            result['ConferenceName'] = self.conference_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.type is not None:
            result['Type'] = self.type
        if self.remind_notice is not None:
            result['RemindNotice'] = self.remind_notice
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ShowLog') is not None:
            self.show_log = m.get('ShowLog')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ConferenceId') is not None:
            self.conference_id = m.get('ConferenceId')
        if m.get('ConferenceName') is not None:
            self.conference_name = m.get('ConferenceName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('RemindNotice') is not None:
            self.remind_notice = m.get('RemindNotice')
        return self


class ModifyConferenceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        conference_id: str = None,
    ):
        self.request_id = request_id
        self.conference_id = conference_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.conference_id is not None:
            result['ConferenceId'] = self.conference_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ConferenceId') is not None:
            self.conference_id = m.get('ConferenceId')
        return self


class ModifyConferenceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyConferenceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyConferenceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyMPULayoutRequestPanes(TeaModel):
    def __init__(
        self,
        major_pane: int = None,
        width: float = None,
        height: float = None,
        y: float = None,
        pane_id: int = None,
        zorder: int = None,
        x: float = None,
    ):
        self.major_pane = major_pane
        self.width = width
        self.height = height
        self.y = y
        self.pane_id = pane_id
        self.zorder = zorder
        self.x = x

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.major_pane is not None:
            result['MajorPane'] = self.major_pane
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        if self.y is not None:
            result['Y'] = self.y
        if self.pane_id is not None:
            result['PaneId'] = self.pane_id
        if self.zorder is not None:
            result['ZOrder'] = self.zorder
        if self.x is not None:
            result['X'] = self.x
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MajorPane') is not None:
            self.major_pane = m.get('MajorPane')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        if m.get('PaneId') is not None:
            self.pane_id = m.get('PaneId')
        if m.get('ZOrder') is not None:
            self.zorder = m.get('ZOrder')
        if m.get('X') is not None:
            self.x = m.get('X')
        return self


class ModifyMPULayoutRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        show_log: str = None,
        app_id: str = None,
        name: str = None,
        layout_id: int = None,
        audio_mix_count: int = None,
        panes: List[ModifyMPULayoutRequestPanes] = None,
    ):
        self.owner_id = owner_id
        self.show_log = show_log
        self.app_id = app_id
        self.name = name
        self.layout_id = layout_id
        self.audio_mix_count = audio_mix_count
        self.panes = panes

    def validate(self):
        if self.panes:
            for k in self.panes:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.show_log is not None:
            result['ShowLog'] = self.show_log
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.name is not None:
            result['Name'] = self.name
        if self.layout_id is not None:
            result['LayoutId'] = self.layout_id
        if self.audio_mix_count is not None:
            result['AudioMixCount'] = self.audio_mix_count
        result['Panes'] = []
        if self.panes is not None:
            for k in self.panes:
                result['Panes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ShowLog') is not None:
            self.show_log = m.get('ShowLog')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('LayoutId') is not None:
            self.layout_id = m.get('LayoutId')
        if m.get('AudioMixCount') is not None:
            self.audio_mix_count = m.get('AudioMixCount')
        self.panes = []
        if m.get('Panes') is not None:
            for k in m.get('Panes'):
                temp_model = ModifyMPULayoutRequestPanes()
                self.panes.append(temp_model.from_map(k))
        return self


class ModifyMPULayoutResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyMPULayoutResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyMPULayoutResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyMPULayoutResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MuteAudioRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        show_log: str = None,
        app_id: str = None,
        conference_id: str = None,
        participant_ids: List[str] = None,
    ):
        self.owner_id = owner_id
        self.show_log = show_log
        self.app_id = app_id
        self.conference_id = conference_id
        self.participant_ids = participant_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.show_log is not None:
            result['ShowLog'] = self.show_log
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.conference_id is not None:
            result['ConferenceId'] = self.conference_id
        if self.participant_ids is not None:
            result['ParticipantIds'] = self.participant_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ShowLog') is not None:
            self.show_log = m.get('ShowLog')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ConferenceId') is not None:
            self.conference_id = m.get('ConferenceId')
        if m.get('ParticipantIds') is not None:
            self.participant_ids = m.get('ParticipantIds')
        return self


class MuteAudioResponseBodyParticipantsParticipant(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        id: str = None,
    ):
        self.code = code
        self.message = message
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class MuteAudioResponseBodyParticipants(TeaModel):
    def __init__(
        self,
        participant: List[MuteAudioResponseBodyParticipantsParticipant] = None,
    ):
        self.participant = participant

    def validate(self):
        if self.participant:
            for k in self.participant:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Participant'] = []
        if self.participant is not None:
            for k in self.participant:
                result['Participant'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.participant = []
        if m.get('Participant') is not None:
            for k in m.get('Participant'):
                temp_model = MuteAudioResponseBodyParticipantsParticipant()
                self.participant.append(temp_model.from_map(k))
        return self


class MuteAudioResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        conference_id: str = None,
        participants: MuteAudioResponseBodyParticipants = None,
    ):
        self.request_id = request_id
        self.conference_id = conference_id
        self.participants = participants

    def validate(self):
        if self.participants:
            self.participants.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.conference_id is not None:
            result['ConferenceId'] = self.conference_id
        if self.participants is not None:
            result['Participants'] = self.participants.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ConferenceId') is not None:
            self.conference_id = m.get('ConferenceId')
        if m.get('Participants') is not None:
            temp_model = MuteAudioResponseBodyParticipants()
            self.participants = temp_model.from_map(m['Participants'])
        return self


class MuteAudioResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: MuteAudioResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = MuteAudioResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MuteAudioAllRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        show_log: str = None,
        app_id: str = None,
        conference_id: str = None,
        participant_id: str = None,
    ):
        self.owner_id = owner_id
        self.show_log = show_log
        self.app_id = app_id
        self.conference_id = conference_id
        self.participant_id = participant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.show_log is not None:
            result['ShowLog'] = self.show_log
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.conference_id is not None:
            result['ConferenceId'] = self.conference_id
        if self.participant_id is not None:
            result['ParticipantId'] = self.participant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ShowLog') is not None:
            self.show_log = m.get('ShowLog')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ConferenceId') is not None:
            self.conference_id = m.get('ConferenceId')
        if m.get('ParticipantId') is not None:
            self.participant_id = m.get('ParticipantId')
        return self


class MuteAudioAllResponseBodyParticipantsParticipant(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        id: str = None,
    ):
        self.code = code
        self.message = message
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class MuteAudioAllResponseBodyParticipants(TeaModel):
    def __init__(
        self,
        participant: List[MuteAudioAllResponseBodyParticipantsParticipant] = None,
    ):
        self.participant = participant

    def validate(self):
        if self.participant:
            for k in self.participant:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Participant'] = []
        if self.participant is not None:
            for k in self.participant:
                result['Participant'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.participant = []
        if m.get('Participant') is not None:
            for k in m.get('Participant'):
                temp_model = MuteAudioAllResponseBodyParticipantsParticipant()
                self.participant.append(temp_model.from_map(k))
        return self


class MuteAudioAllResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        conference_id: str = None,
        participants: MuteAudioAllResponseBodyParticipants = None,
    ):
        self.request_id = request_id
        self.conference_id = conference_id
        self.participants = participants

    def validate(self):
        if self.participants:
            self.participants.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.conference_id is not None:
            result['ConferenceId'] = self.conference_id
        if self.participants is not None:
            result['Participants'] = self.participants.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ConferenceId') is not None:
            self.conference_id = m.get('ConferenceId')
        if m.get('Participants') is not None:
            temp_model = MuteAudioAllResponseBodyParticipants()
            self.participants = temp_model.from_map(m['Participants'])
        return self


class MuteAudioAllResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: MuteAudioAllResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = MuteAudioAllResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReceiveNotifyRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        show_log: str = None,
        trace_id: str = None,
        biz_id: str = None,
        event: str = None,
        content_type: str = None,
        content: str = None,
    ):
        self.owner_id = owner_id
        self.show_log = show_log
        self.trace_id = trace_id
        self.biz_id = biz_id
        self.event = event
        self.content_type = content_type
        self.content = content

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.show_log is not None:
            result['ShowLog'] = self.show_log
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.event is not None:
            result['Event'] = self.event
        if self.content_type is not None:
            result['ContentType'] = self.content_type
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ShowLog') is not None:
            self.show_log = m.get('ShowLog')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Event') is not None:
            self.event = m.get('Event')
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class ReceiveNotifyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        trace_id: str = None,
    ):
        self.request_id = request_id
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class ReceiveNotifyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ReceiveNotifyResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ReceiveNotifyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveParticipantsRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        show_log: str = None,
        app_id: str = None,
        conference_id: str = None,
        participant_ids: List[str] = None,
    ):
        self.owner_id = owner_id
        self.show_log = show_log
        self.app_id = app_id
        self.conference_id = conference_id
        self.participant_ids = participant_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.show_log is not None:
            result['ShowLog'] = self.show_log
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.conference_id is not None:
            result['ConferenceId'] = self.conference_id
        if self.participant_ids is not None:
            result['ParticipantIds'] = self.participant_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ShowLog') is not None:
            self.show_log = m.get('ShowLog')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ConferenceId') is not None:
            self.conference_id = m.get('ConferenceId')
        if m.get('ParticipantIds') is not None:
            self.participant_ids = m.get('ParticipantIds')
        return self


class RemoveParticipantsResponseBodyParticipantsParticipant(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        id: str = None,
    ):
        self.code = code
        self.message = message
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class RemoveParticipantsResponseBodyParticipants(TeaModel):
    def __init__(
        self,
        participant: List[RemoveParticipantsResponseBodyParticipantsParticipant] = None,
    ):
        self.participant = participant

    def validate(self):
        if self.participant:
            for k in self.participant:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Participant'] = []
        if self.participant is not None:
            for k in self.participant:
                result['Participant'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.participant = []
        if m.get('Participant') is not None:
            for k in m.get('Participant'):
                temp_model = RemoveParticipantsResponseBodyParticipantsParticipant()
                self.participant.append(temp_model.from_map(k))
        return self


class RemoveParticipantsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        conference_id: str = None,
        participants: RemoveParticipantsResponseBodyParticipants = None,
    ):
        self.request_id = request_id
        self.conference_id = conference_id
        self.participants = participants

    def validate(self):
        if self.participants:
            self.participants.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.conference_id is not None:
            result['ConferenceId'] = self.conference_id
        if self.participants is not None:
            result['Participants'] = self.participants.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ConferenceId') is not None:
            self.conference_id = m.get('ConferenceId')
        if m.get('Participants') is not None:
            temp_model = RemoveParticipantsResponseBodyParticipants()
            self.participants = temp_model.from_map(m['Participants'])
        return self


class RemoveParticipantsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RemoveParticipantsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RemoveParticipantsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveTerminalsRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        show_log: str = None,
        app_id: str = None,
        channel_id: str = None,
        terminal_ids: List[str] = None,
    ):
        self.owner_id = owner_id
        self.show_log = show_log
        self.app_id = app_id
        self.channel_id = channel_id
        self.terminal_ids = terminal_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.show_log is not None:
            result['ShowLog'] = self.show_log
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.terminal_ids is not None:
            result['TerminalIds'] = self.terminal_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ShowLog') is not None:
            self.show_log = m.get('ShowLog')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('TerminalIds') is not None:
            self.terminal_ids = m.get('TerminalIds')
        return self


class RemoveTerminalsResponseBodyTerminalsTerminal(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        id: str = None,
    ):
        self.code = code
        self.message = message
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class RemoveTerminalsResponseBodyTerminals(TeaModel):
    def __init__(
        self,
        terminal: List[RemoveTerminalsResponseBodyTerminalsTerminal] = None,
    ):
        self.terminal = terminal

    def validate(self):
        if self.terminal:
            for k in self.terminal:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Terminal'] = []
        if self.terminal is not None:
            for k in self.terminal:
                result['Terminal'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.terminal = []
        if m.get('Terminal') is not None:
            for k in m.get('Terminal'):
                temp_model = RemoveTerminalsResponseBodyTerminalsTerminal()
                self.terminal.append(temp_model.from_map(k))
        return self


class RemoveTerminalsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        terminals: RemoveTerminalsResponseBodyTerminals = None,
    ):
        self.request_id = request_id
        self.terminals = terminals

    def validate(self):
        if self.terminals:
            self.terminals.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.terminals is not None:
            result['Terminals'] = self.terminals.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Terminals') is not None:
            temp_model = RemoveTerminalsResponseBodyTerminals()
            self.terminals = temp_model.from_map(m['Terminals'])
        return self


class RemoveTerminalsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RemoveTerminalsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RemoveTerminalsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetChannelPropertyRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        show_log: str = None,
        app_id: str = None,
        channel_id: str = None,
        max_user_num: int = None,
        start_time: int = None,
        duration: int = None,
        priority: str = None,
        topics: str = None,
    ):
        self.owner_id = owner_id
        self.show_log = show_log
        self.app_id = app_id
        self.channel_id = channel_id
        self.max_user_num = max_user_num
        self.start_time = start_time
        self.duration = duration
        self.priority = priority
        self.topics = topics

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.show_log is not None:
            result['ShowLog'] = self.show_log
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.max_user_num is not None:
            result['MaxUserNum'] = self.max_user_num
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.topics is not None:
            result['Topics'] = self.topics
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ShowLog') is not None:
            self.show_log = m.get('ShowLog')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('MaxUserNum') is not None:
            self.max_user_num = m.get('MaxUserNum')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Topics') is not None:
            self.topics = m.get('Topics')
        return self


class SetChannelPropertyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetChannelPropertyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetChannelPropertyResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SetChannelPropertyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartMPUTaskRequestUserPanesImages(TeaModel):
    def __init__(
        self,
        width: float = None,
        height: float = None,
        y: float = None,
        url: str = None,
        display: int = None,
        zorder: int = None,
        x: float = None,
    ):
        self.width = width
        self.height = height
        self.y = y
        self.url = url
        self.display = display
        self.zorder = zorder
        self.x = x

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        if self.y is not None:
            result['Y'] = self.y
        if self.url is not None:
            result['Url'] = self.url
        if self.display is not None:
            result['Display'] = self.display
        if self.zorder is not None:
            result['ZOrder'] = self.zorder
        if self.x is not None:
            result['X'] = self.x
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Display') is not None:
            self.display = m.get('Display')
        if m.get('ZOrder') is not None:
            self.zorder = m.get('ZOrder')
        if m.get('X') is not None:
            self.x = m.get('X')
        return self


class StartMPUTaskRequestUserPanesTexts(TeaModel):
    def __init__(
        self,
        font_type: int = None,
        font_color: int = None,
        y: float = None,
        text: str = None,
        zorder: int = None,
        font_size: int = None,
        x: float = None,
    ):
        self.font_type = font_type
        self.font_color = font_color
        self.y = y
        self.text = text
        self.zorder = zorder
        self.font_size = font_size
        self.x = x

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.font_type is not None:
            result['FontType'] = self.font_type
        if self.font_color is not None:
            result['FontColor'] = self.font_color
        if self.y is not None:
            result['Y'] = self.y
        if self.text is not None:
            result['Text'] = self.text
        if self.zorder is not None:
            result['ZOrder'] = self.zorder
        if self.font_size is not None:
            result['FontSize'] = self.font_size
        if self.x is not None:
            result['X'] = self.x
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FontType') is not None:
            self.font_type = m.get('FontType')
        if m.get('FontColor') is not None:
            self.font_color = m.get('FontColor')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('ZOrder') is not None:
            self.zorder = m.get('ZOrder')
        if m.get('FontSize') is not None:
            self.font_size = m.get('FontSize')
        if m.get('X') is not None:
            self.x = m.get('X')
        return self


class StartMPUTaskRequestUserPanes(TeaModel):
    def __init__(
        self,
        images: List[StartMPUTaskRequestUserPanesImages] = None,
        segment_type: int = None,
        user_id: str = None,
        texts: List[StartMPUTaskRequestUserPanesTexts] = None,
        source_type: str = None,
        pane_id: int = None,
    ):
        self.images = images
        self.segment_type = segment_type
        self.user_id = user_id
        self.texts = texts
        self.source_type = source_type
        self.pane_id = pane_id

    def validate(self):
        if self.images:
            for k in self.images:
                if k:
                    k.validate()
        if self.texts:
            for k in self.texts:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Images'] = []
        if self.images is not None:
            for k in self.images:
                result['Images'].append(k.to_map() if k else None)
        if self.segment_type is not None:
            result['SegmentType'] = self.segment_type
        if self.user_id is not None:
            result['UserId'] = self.user_id
        result['Texts'] = []
        if self.texts is not None:
            for k in self.texts:
                result['Texts'].append(k.to_map() if k else None)
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.pane_id is not None:
            result['PaneId'] = self.pane_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.images = []
        if m.get('Images') is not None:
            for k in m.get('Images'):
                temp_model = StartMPUTaskRequestUserPanesImages()
                self.images.append(temp_model.from_map(k))
        if m.get('SegmentType') is not None:
            self.segment_type = m.get('SegmentType')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        self.texts = []
        if m.get('Texts') is not None:
            for k in m.get('Texts'):
                temp_model = StartMPUTaskRequestUserPanesTexts()
                self.texts.append(temp_model.from_map(k))
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('PaneId') is not None:
            self.pane_id = m.get('PaneId')
        return self


class StartMPUTaskRequestBackgrounds(TeaModel):
    def __init__(
        self,
        width: float = None,
        height: float = None,
        y: float = None,
        url: str = None,
        display: int = None,
        zorder: int = None,
        x: float = None,
    ):
        self.width = width
        self.height = height
        self.y = y
        self.url = url
        self.display = display
        self.zorder = zorder
        self.x = x

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        if self.y is not None:
            result['Y'] = self.y
        if self.url is not None:
            result['Url'] = self.url
        if self.display is not None:
            result['Display'] = self.display
        if self.zorder is not None:
            result['ZOrder'] = self.zorder
        if self.x is not None:
            result['X'] = self.x
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Display') is not None:
            self.display = m.get('Display')
        if m.get('ZOrder') is not None:
            self.zorder = m.get('ZOrder')
        if m.get('X') is not None:
            self.x = m.get('X')
        return self


class StartMPUTaskRequestWatermarks(TeaModel):
    def __init__(
        self,
        alpha: float = None,
        width: float = None,
        height: float = None,
        y: float = None,
        url: str = None,
        display: int = None,
        zorder: int = None,
        x: float = None,
    ):
        self.alpha = alpha
        self.width = width
        self.height = height
        self.y = y
        self.url = url
        self.display = display
        self.zorder = zorder
        self.x = x

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.alpha is not None:
            result['Alpha'] = self.alpha
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        if self.y is not None:
            result['Y'] = self.y
        if self.url is not None:
            result['Url'] = self.url
        if self.display is not None:
            result['Display'] = self.display
        if self.zorder is not None:
            result['ZOrder'] = self.zorder
        if self.x is not None:
            result['X'] = self.x
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alpha') is not None:
            self.alpha = m.get('Alpha')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Display') is not None:
            self.display = m.get('Display')
        if m.get('ZOrder') is not None:
            self.zorder = m.get('ZOrder')
        if m.get('X') is not None:
            self.x = m.get('X')
        return self


class StartMPUTaskRequestClockWidgets(TeaModel):
    def __init__(
        self,
        font_type: int = None,
        font_color: int = None,
        y: float = None,
        zorder: int = None,
        x: float = None,
        font_size: int = None,
    ):
        self.font_type = font_type
        self.font_color = font_color
        self.y = y
        self.zorder = zorder
        self.x = x
        self.font_size = font_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.font_type is not None:
            result['FontType'] = self.font_type
        if self.font_color is not None:
            result['FontColor'] = self.font_color
        if self.y is not None:
            result['Y'] = self.y
        if self.zorder is not None:
            result['ZOrder'] = self.zorder
        if self.x is not None:
            result['X'] = self.x
        if self.font_size is not None:
            result['FontSize'] = self.font_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FontType') is not None:
            self.font_type = m.get('FontType')
        if m.get('FontColor') is not None:
            self.font_color = m.get('FontColor')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        if m.get('ZOrder') is not None:
            self.zorder = m.get('ZOrder')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('FontSize') is not None:
            self.font_size = m.get('FontSize')
        return self


class StartMPUTaskRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        show_log: str = None,
        app_id: str = None,
        channel_id: str = None,
        task_id: str = None,
        task_profile: str = None,
        task_mode: int = None,
        mix_mode: int = None,
        crop_mode: int = None,
        media_encode: int = None,
        source_type: str = None,
        stream_type: int = None,
        background_color: int = None,
        stream_url: str = None,
        payload_type: int = None,
        report_vad: int = None,
        rtp_ext_info: int = None,
        time_stamp_ref: int = None,
        vad_interval: int = None,
        sub_spec_users: List[str] = None,
        sub_spec_audio_users: List[str] = None,
        layout_ids: List[int] = None,
        user_panes: List[StartMPUTaskRequestUserPanes] = None,
        backgrounds: List[StartMPUTaskRequestBackgrounds] = None,
        watermarks: List[StartMPUTaskRequestWatermarks] = None,
        clock_widgets: List[StartMPUTaskRequestClockWidgets] = None,
    ):
        self.owner_id = owner_id
        self.show_log = show_log
        self.app_id = app_id
        self.channel_id = channel_id
        self.task_id = task_id
        self.task_profile = task_profile
        self.task_mode = task_mode
        self.mix_mode = mix_mode
        self.crop_mode = crop_mode
        self.media_encode = media_encode
        self.source_type = source_type
        self.stream_type = stream_type
        self.background_color = background_color
        self.stream_url = stream_url
        self.payload_type = payload_type
        self.report_vad = report_vad
        self.rtp_ext_info = rtp_ext_info
        self.time_stamp_ref = time_stamp_ref
        self.vad_interval = vad_interval
        self.sub_spec_users = sub_spec_users
        self.sub_spec_audio_users = sub_spec_audio_users
        self.layout_ids = layout_ids
        self.user_panes = user_panes
        self.backgrounds = backgrounds
        self.watermarks = watermarks
        self.clock_widgets = clock_widgets

    def validate(self):
        if self.user_panes:
            for k in self.user_panes:
                if k:
                    k.validate()
        if self.backgrounds:
            for k in self.backgrounds:
                if k:
                    k.validate()
        if self.watermarks:
            for k in self.watermarks:
                if k:
                    k.validate()
        if self.clock_widgets:
            for k in self.clock_widgets:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.show_log is not None:
            result['ShowLog'] = self.show_log
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_profile is not None:
            result['TaskProfile'] = self.task_profile
        if self.task_mode is not None:
            result['TaskMode'] = self.task_mode
        if self.mix_mode is not None:
            result['MixMode'] = self.mix_mode
        if self.crop_mode is not None:
            result['CropMode'] = self.crop_mode
        if self.media_encode is not None:
            result['MediaEncode'] = self.media_encode
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.stream_type is not None:
            result['StreamType'] = self.stream_type
        if self.background_color is not None:
            result['BackgroundColor'] = self.background_color
        if self.stream_url is not None:
            result['StreamURL'] = self.stream_url
        if self.payload_type is not None:
            result['PayloadType'] = self.payload_type
        if self.report_vad is not None:
            result['ReportVad'] = self.report_vad
        if self.rtp_ext_info is not None:
            result['RtpExtInfo'] = self.rtp_ext_info
        if self.time_stamp_ref is not None:
            result['TimeStampRef'] = self.time_stamp_ref
        if self.vad_interval is not None:
            result['VadInterval'] = self.vad_interval
        if self.sub_spec_users is not None:
            result['SubSpecUsers'] = self.sub_spec_users
        if self.sub_spec_audio_users is not None:
            result['SubSpecAudioUsers'] = self.sub_spec_audio_users
        if self.layout_ids is not None:
            result['LayoutIds'] = self.layout_ids
        result['UserPanes'] = []
        if self.user_panes is not None:
            for k in self.user_panes:
                result['UserPanes'].append(k.to_map() if k else None)
        result['Backgrounds'] = []
        if self.backgrounds is not None:
            for k in self.backgrounds:
                result['Backgrounds'].append(k.to_map() if k else None)
        result['Watermarks'] = []
        if self.watermarks is not None:
            for k in self.watermarks:
                result['Watermarks'].append(k.to_map() if k else None)
        result['ClockWidgets'] = []
        if self.clock_widgets is not None:
            for k in self.clock_widgets:
                result['ClockWidgets'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ShowLog') is not None:
            self.show_log = m.get('ShowLog')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskProfile') is not None:
            self.task_profile = m.get('TaskProfile')
        if m.get('TaskMode') is not None:
            self.task_mode = m.get('TaskMode')
        if m.get('MixMode') is not None:
            self.mix_mode = m.get('MixMode')
        if m.get('CropMode') is not None:
            self.crop_mode = m.get('CropMode')
        if m.get('MediaEncode') is not None:
            self.media_encode = m.get('MediaEncode')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')
        if m.get('BackgroundColor') is not None:
            self.background_color = m.get('BackgroundColor')
        if m.get('StreamURL') is not None:
            self.stream_url = m.get('StreamURL')
        if m.get('PayloadType') is not None:
            self.payload_type = m.get('PayloadType')
        if m.get('ReportVad') is not None:
            self.report_vad = m.get('ReportVad')
        if m.get('RtpExtInfo') is not None:
            self.rtp_ext_info = m.get('RtpExtInfo')
        if m.get('TimeStampRef') is not None:
            self.time_stamp_ref = m.get('TimeStampRef')
        if m.get('VadInterval') is not None:
            self.vad_interval = m.get('VadInterval')
        if m.get('SubSpecUsers') is not None:
            self.sub_spec_users = m.get('SubSpecUsers')
        if m.get('SubSpecAudioUsers') is not None:
            self.sub_spec_audio_users = m.get('SubSpecAudioUsers')
        if m.get('LayoutIds') is not None:
            self.layout_ids = m.get('LayoutIds')
        self.user_panes = []
        if m.get('UserPanes') is not None:
            for k in m.get('UserPanes'):
                temp_model = StartMPUTaskRequestUserPanes()
                self.user_panes.append(temp_model.from_map(k))
        self.backgrounds = []
        if m.get('Backgrounds') is not None:
            for k in m.get('Backgrounds'):
                temp_model = StartMPUTaskRequestBackgrounds()
                self.backgrounds.append(temp_model.from_map(k))
        self.watermarks = []
        if m.get('Watermarks') is not None:
            for k in m.get('Watermarks'):
                temp_model = StartMPUTaskRequestWatermarks()
                self.watermarks.append(temp_model.from_map(k))
        self.clock_widgets = []
        if m.get('ClockWidgets') is not None:
            for k in m.get('ClockWidgets'):
                temp_model = StartMPUTaskRequestClockWidgets()
                self.clock_widgets.append(temp_model.from_map(k))
        return self


class StartMPUTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StartMPUTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StartMPUTaskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StartMPUTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartRecordTaskRequestUserPanesImages(TeaModel):
    def __init__(
        self,
        width: float = None,
        height: float = None,
        y: float = None,
        url: str = None,
        display: int = None,
        zorder: int = None,
        x: float = None,
    ):
        self.width = width
        self.height = height
        self.y = y
        self.url = url
        self.display = display
        self.zorder = zorder
        self.x = x

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        if self.y is not None:
            result['Y'] = self.y
        if self.url is not None:
            result['Url'] = self.url
        if self.display is not None:
            result['Display'] = self.display
        if self.zorder is not None:
            result['ZOrder'] = self.zorder
        if self.x is not None:
            result['X'] = self.x
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Display') is not None:
            self.display = m.get('Display')
        if m.get('ZOrder') is not None:
            self.zorder = m.get('ZOrder')
        if m.get('X') is not None:
            self.x = m.get('X')
        return self


class StartRecordTaskRequestUserPanesTexts(TeaModel):
    def __init__(
        self,
        font_type: int = None,
        font_color: int = None,
        y: float = None,
        text: str = None,
        zorder: int = None,
        font_size: int = None,
        x: float = None,
    ):
        self.font_type = font_type
        self.font_color = font_color
        self.y = y
        self.text = text
        self.zorder = zorder
        self.font_size = font_size
        self.x = x

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.font_type is not None:
            result['FontType'] = self.font_type
        if self.font_color is not None:
            result['FontColor'] = self.font_color
        if self.y is not None:
            result['Y'] = self.y
        if self.text is not None:
            result['Text'] = self.text
        if self.zorder is not None:
            result['ZOrder'] = self.zorder
        if self.font_size is not None:
            result['FontSize'] = self.font_size
        if self.x is not None:
            result['X'] = self.x
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FontType') is not None:
            self.font_type = m.get('FontType')
        if m.get('FontColor') is not None:
            self.font_color = m.get('FontColor')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('ZOrder') is not None:
            self.zorder = m.get('ZOrder')
        if m.get('FontSize') is not None:
            self.font_size = m.get('FontSize')
        if m.get('X') is not None:
            self.x = m.get('X')
        return self


class StartRecordTaskRequestUserPanes(TeaModel):
    def __init__(
        self,
        images: List[StartRecordTaskRequestUserPanesImages] = None,
        user_id: str = None,
        texts: List[StartRecordTaskRequestUserPanesTexts] = None,
        source_type: str = None,
        pane_id: int = None,
    ):
        self.images = images
        self.user_id = user_id
        self.texts = texts
        self.source_type = source_type
        self.pane_id = pane_id

    def validate(self):
        if self.images:
            for k in self.images:
                if k:
                    k.validate()
        if self.texts:
            for k in self.texts:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Images'] = []
        if self.images is not None:
            for k in self.images:
                result['Images'].append(k.to_map() if k else None)
        if self.user_id is not None:
            result['UserId'] = self.user_id
        result['Texts'] = []
        if self.texts is not None:
            for k in self.texts:
                result['Texts'].append(k.to_map() if k else None)
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.pane_id is not None:
            result['PaneId'] = self.pane_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.images = []
        if m.get('Images') is not None:
            for k in m.get('Images'):
                temp_model = StartRecordTaskRequestUserPanesImages()
                self.images.append(temp_model.from_map(k))
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        self.texts = []
        if m.get('Texts') is not None:
            for k in m.get('Texts'):
                temp_model = StartRecordTaskRequestUserPanesTexts()
                self.texts.append(temp_model.from_map(k))
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('PaneId') is not None:
            self.pane_id = m.get('PaneId')
        return self


class StartRecordTaskRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        show_log: str = None,
        app_id: str = None,
        channel_id: str = None,
        task_id: str = None,
        task_profile: str = None,
        media_encode: int = None,
        template_id: str = None,
        sub_spec_users: List[str] = None,
        user_panes: List[StartRecordTaskRequestUserPanes] = None,
    ):
        self.owner_id = owner_id
        self.show_log = show_log
        self.app_id = app_id
        self.channel_id = channel_id
        self.task_id = task_id
        self.task_profile = task_profile
        self.media_encode = media_encode
        self.template_id = template_id
        self.sub_spec_users = sub_spec_users
        self.user_panes = user_panes

    def validate(self):
        if self.user_panes:
            for k in self.user_panes:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.show_log is not None:
            result['ShowLog'] = self.show_log
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_profile is not None:
            result['TaskProfile'] = self.task_profile
        if self.media_encode is not None:
            result['MediaEncode'] = self.media_encode
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.sub_spec_users is not None:
            result['SubSpecUsers'] = self.sub_spec_users
        result['UserPanes'] = []
        if self.user_panes is not None:
            for k in self.user_panes:
                result['UserPanes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ShowLog') is not None:
            self.show_log = m.get('ShowLog')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskProfile') is not None:
            self.task_profile = m.get('TaskProfile')
        if m.get('MediaEncode') is not None:
            self.media_encode = m.get('MediaEncode')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('SubSpecUsers') is not None:
            self.sub_spec_users = m.get('SubSpecUsers')
        self.user_panes = []
        if m.get('UserPanes') is not None:
            for k in m.get('UserPanes'):
                temp_model = StartRecordTaskRequestUserPanes()
                self.user_panes.append(temp_model.from_map(k))
        return self


class StartRecordTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StartRecordTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StartRecordTaskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StartRecordTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopChannelUserPublishRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        show_log: str = None,
        app_id: str = None,
        channel_id: str = None,
        user_id: str = None,
    ):
        self.owner_id = owner_id
        self.show_log = show_log
        self.app_id = app_id
        self.channel_id = channel_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.show_log is not None:
            result['ShowLog'] = self.show_log
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ShowLog') is not None:
            self.show_log = m.get('ShowLog')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class StopChannelUserPublishResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StopChannelUserPublishResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StopChannelUserPublishResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StopChannelUserPublishResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopMPUTaskRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        show_log: str = None,
        app_id: str = None,
        task_id: str = None,
    ):
        self.owner_id = owner_id
        self.show_log = show_log
        self.app_id = app_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.show_log is not None:
            result['ShowLog'] = self.show_log
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ShowLog') is not None:
            self.show_log = m.get('ShowLog')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class StopMPUTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StopMPUTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StopMPUTaskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StopMPUTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopRecordTaskRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        show_log: str = None,
        app_id: str = None,
        task_id: str = None,
    ):
        self.owner_id = owner_id
        self.show_log = show_log
        self.app_id = app_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.show_log is not None:
            result['ShowLog'] = self.show_log
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ShowLog') is not None:
            self.show_log = m.get('ShowLog')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class StopRecordTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StopRecordTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StopRecordTaskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StopRecordTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnmuteAudioRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        show_log: str = None,
        app_id: str = None,
        conference_id: str = None,
        participant_ids: List[str] = None,
    ):
        self.owner_id = owner_id
        self.show_log = show_log
        self.app_id = app_id
        self.conference_id = conference_id
        self.participant_ids = participant_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.show_log is not None:
            result['ShowLog'] = self.show_log
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.conference_id is not None:
            result['ConferenceId'] = self.conference_id
        if self.participant_ids is not None:
            result['ParticipantIds'] = self.participant_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ShowLog') is not None:
            self.show_log = m.get('ShowLog')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ConferenceId') is not None:
            self.conference_id = m.get('ConferenceId')
        if m.get('ParticipantIds') is not None:
            self.participant_ids = m.get('ParticipantIds')
        return self


class UnmuteAudioResponseBodyParticipantsParticipant(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        id: str = None,
    ):
        self.code = code
        self.message = message
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class UnmuteAudioResponseBodyParticipants(TeaModel):
    def __init__(
        self,
        participant: List[UnmuteAudioResponseBodyParticipantsParticipant] = None,
    ):
        self.participant = participant

    def validate(self):
        if self.participant:
            for k in self.participant:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Participant'] = []
        if self.participant is not None:
            for k in self.participant:
                result['Participant'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.participant = []
        if m.get('Participant') is not None:
            for k in m.get('Participant'):
                temp_model = UnmuteAudioResponseBodyParticipantsParticipant()
                self.participant.append(temp_model.from_map(k))
        return self


class UnmuteAudioResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        conference_id: str = None,
        participants: UnmuteAudioResponseBodyParticipants = None,
    ):
        self.request_id = request_id
        self.conference_id = conference_id
        self.participants = participants

    def validate(self):
        if self.participants:
            self.participants.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.conference_id is not None:
            result['ConferenceId'] = self.conference_id
        if self.participants is not None:
            result['Participants'] = self.participants.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ConferenceId') is not None:
            self.conference_id = m.get('ConferenceId')
        if m.get('Participants') is not None:
            temp_model = UnmuteAudioResponseBodyParticipants()
            self.participants = temp_model.from_map(m['Participants'])
        return self


class UnmuteAudioResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UnmuteAudioResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UnmuteAudioResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnmuteAudioAllRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        show_log: str = None,
        app_id: str = None,
        conference_id: str = None,
        participant_id: str = None,
    ):
        self.owner_id = owner_id
        self.show_log = show_log
        self.app_id = app_id
        self.conference_id = conference_id
        self.participant_id = participant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.show_log is not None:
            result['ShowLog'] = self.show_log
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.conference_id is not None:
            result['ConferenceId'] = self.conference_id
        if self.participant_id is not None:
            result['ParticipantId'] = self.participant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ShowLog') is not None:
            self.show_log = m.get('ShowLog')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ConferenceId') is not None:
            self.conference_id = m.get('ConferenceId')
        if m.get('ParticipantId') is not None:
            self.participant_id = m.get('ParticipantId')
        return self


class UnmuteAudioAllResponseBodyParticipantsParticipant(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        id: str = None,
    ):
        self.code = code
        self.message = message
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class UnmuteAudioAllResponseBodyParticipants(TeaModel):
    def __init__(
        self,
        participant: List[UnmuteAudioAllResponseBodyParticipantsParticipant] = None,
    ):
        self.participant = participant

    def validate(self):
        if self.participant:
            for k in self.participant:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Participant'] = []
        if self.participant is not None:
            for k in self.participant:
                result['Participant'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.participant = []
        if m.get('Participant') is not None:
            for k in m.get('Participant'):
                temp_model = UnmuteAudioAllResponseBodyParticipantsParticipant()
                self.participant.append(temp_model.from_map(k))
        return self


class UnmuteAudioAllResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        conference_id: str = None,
        participants: UnmuteAudioAllResponseBodyParticipants = None,
    ):
        self.request_id = request_id
        self.conference_id = conference_id
        self.participants = participants

    def validate(self):
        if self.participants:
            self.participants.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.conference_id is not None:
            result['ConferenceId'] = self.conference_id
        if self.participants is not None:
            result['Participants'] = self.participants.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ConferenceId') is not None:
            self.conference_id = m.get('ConferenceId')
        if m.get('Participants') is not None:
            temp_model = UnmuteAudioAllResponseBodyParticipants()
            self.participants = temp_model.from_map(m['Participants'])
        return self


class UnmuteAudioAllResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UnmuteAudioAllResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UnmuteAudioAllResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateChannelRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        show_log: str = None,
        app_id: str = None,
        channel_id: str = None,
        nonce: str = None,
    ):
        self.owner_id = owner_id
        self.show_log = show_log
        self.app_id = app_id
        self.channel_id = channel_id
        self.nonce = nonce

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.show_log is not None:
            result['ShowLog'] = self.show_log
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.nonce is not None:
            result['Nonce'] = self.nonce
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ShowLog') is not None:
            self.show_log = m.get('ShowLog')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('Nonce') is not None:
            self.nonce = m.get('Nonce')
        return self


class UpdateChannelResponseBody(TeaModel):
    def __init__(
        self,
        nonce: str = None,
        request_id: str = None,
        timestamp: int = None,
    ):
        self.nonce = nonce
        self.request_id = request_id
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.nonce is not None:
            result['Nonce'] = self.nonce
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Nonce') is not None:
            self.nonce = m.get('Nonce')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class UpdateChannelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateChannelResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateChannelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateMPULayoutRequestUserPanesImages(TeaModel):
    def __init__(
        self,
        width: float = None,
        height: float = None,
        y: float = None,
        url: str = None,
        display: int = None,
        zorder: int = None,
        x: float = None,
    ):
        self.width = width
        self.height = height
        self.y = y
        self.url = url
        self.display = display
        self.zorder = zorder
        self.x = x

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        if self.y is not None:
            result['Y'] = self.y
        if self.url is not None:
            result['Url'] = self.url
        if self.display is not None:
            result['Display'] = self.display
        if self.zorder is not None:
            result['ZOrder'] = self.zorder
        if self.x is not None:
            result['X'] = self.x
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Display') is not None:
            self.display = m.get('Display')
        if m.get('ZOrder') is not None:
            self.zorder = m.get('ZOrder')
        if m.get('X') is not None:
            self.x = m.get('X')
        return self


class UpdateMPULayoutRequestUserPanesTexts(TeaModel):
    def __init__(
        self,
        font_type: int = None,
        font_color: int = None,
        y: float = None,
        text: str = None,
        zorder: int = None,
        font_size: int = None,
        x: float = None,
    ):
        self.font_type = font_type
        self.font_color = font_color
        self.y = y
        self.text = text
        self.zorder = zorder
        self.font_size = font_size
        self.x = x

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.font_type is not None:
            result['FontType'] = self.font_type
        if self.font_color is not None:
            result['FontColor'] = self.font_color
        if self.y is not None:
            result['Y'] = self.y
        if self.text is not None:
            result['Text'] = self.text
        if self.zorder is not None:
            result['ZOrder'] = self.zorder
        if self.font_size is not None:
            result['FontSize'] = self.font_size
        if self.x is not None:
            result['X'] = self.x
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FontType') is not None:
            self.font_type = m.get('FontType')
        if m.get('FontColor') is not None:
            self.font_color = m.get('FontColor')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('ZOrder') is not None:
            self.zorder = m.get('ZOrder')
        if m.get('FontSize') is not None:
            self.font_size = m.get('FontSize')
        if m.get('X') is not None:
            self.x = m.get('X')
        return self


class UpdateMPULayoutRequestUserPanes(TeaModel):
    def __init__(
        self,
        images: List[UpdateMPULayoutRequestUserPanesImages] = None,
        segment_type: int = None,
        user_id: str = None,
        texts: List[UpdateMPULayoutRequestUserPanesTexts] = None,
        source_type: str = None,
        pane_id: int = None,
    ):
        self.images = images
        self.segment_type = segment_type
        self.user_id = user_id
        self.texts = texts
        self.source_type = source_type
        self.pane_id = pane_id

    def validate(self):
        if self.images:
            for k in self.images:
                if k:
                    k.validate()
        if self.texts:
            for k in self.texts:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Images'] = []
        if self.images is not None:
            for k in self.images:
                result['Images'].append(k.to_map() if k else None)
        if self.segment_type is not None:
            result['SegmentType'] = self.segment_type
        if self.user_id is not None:
            result['UserId'] = self.user_id
        result['Texts'] = []
        if self.texts is not None:
            for k in self.texts:
                result['Texts'].append(k.to_map() if k else None)
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.pane_id is not None:
            result['PaneId'] = self.pane_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.images = []
        if m.get('Images') is not None:
            for k in m.get('Images'):
                temp_model = UpdateMPULayoutRequestUserPanesImages()
                self.images.append(temp_model.from_map(k))
        if m.get('SegmentType') is not None:
            self.segment_type = m.get('SegmentType')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        self.texts = []
        if m.get('Texts') is not None:
            for k in m.get('Texts'):
                temp_model = UpdateMPULayoutRequestUserPanesTexts()
                self.texts.append(temp_model.from_map(k))
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('PaneId') is not None:
            self.pane_id = m.get('PaneId')
        return self


class UpdateMPULayoutRequestBackgrounds(TeaModel):
    def __init__(
        self,
        width: float = None,
        height: float = None,
        y: float = None,
        url: str = None,
        display: int = None,
        zorder: int = None,
        x: float = None,
    ):
        self.width = width
        self.height = height
        self.y = y
        self.url = url
        self.display = display
        self.zorder = zorder
        self.x = x

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        if self.y is not None:
            result['Y'] = self.y
        if self.url is not None:
            result['Url'] = self.url
        if self.display is not None:
            result['Display'] = self.display
        if self.zorder is not None:
            result['ZOrder'] = self.zorder
        if self.x is not None:
            result['X'] = self.x
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Display') is not None:
            self.display = m.get('Display')
        if m.get('ZOrder') is not None:
            self.zorder = m.get('ZOrder')
        if m.get('X') is not None:
            self.x = m.get('X')
        return self


class UpdateMPULayoutRequestWatermarks(TeaModel):
    def __init__(
        self,
        alpha: float = None,
        width: float = None,
        height: float = None,
        y: float = None,
        url: str = None,
        display: int = None,
        zorder: int = None,
        x: float = None,
    ):
        self.alpha = alpha
        self.width = width
        self.height = height
        self.y = y
        self.url = url
        self.display = display
        self.zorder = zorder
        self.x = x

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.alpha is not None:
            result['Alpha'] = self.alpha
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        if self.y is not None:
            result['Y'] = self.y
        if self.url is not None:
            result['Url'] = self.url
        if self.display is not None:
            result['Display'] = self.display
        if self.zorder is not None:
            result['ZOrder'] = self.zorder
        if self.x is not None:
            result['X'] = self.x
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alpha') is not None:
            self.alpha = m.get('Alpha')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Display') is not None:
            self.display = m.get('Display')
        if m.get('ZOrder') is not None:
            self.zorder = m.get('ZOrder')
        if m.get('X') is not None:
            self.x = m.get('X')
        return self


class UpdateMPULayoutRequestClockWidgets(TeaModel):
    def __init__(
        self,
        font_type: int = None,
        font_color: int = None,
        y: float = None,
        zorder: int = None,
        x: float = None,
        font_size: int = None,
    ):
        self.font_type = font_type
        self.font_color = font_color
        self.y = y
        self.zorder = zorder
        self.x = x
        self.font_size = font_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.font_type is not None:
            result['FontType'] = self.font_type
        if self.font_color is not None:
            result['FontColor'] = self.font_color
        if self.y is not None:
            result['Y'] = self.y
        if self.zorder is not None:
            result['ZOrder'] = self.zorder
        if self.x is not None:
            result['X'] = self.x
        if self.font_size is not None:
            result['FontSize'] = self.font_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FontType') is not None:
            self.font_type = m.get('FontType')
        if m.get('FontColor') is not None:
            self.font_color = m.get('FontColor')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        if m.get('ZOrder') is not None:
            self.zorder = m.get('ZOrder')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('FontSize') is not None:
            self.font_size = m.get('FontSize')
        return self


class UpdateMPULayoutRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        show_log: str = None,
        app_id: str = None,
        task_id: str = None,
        crop_mode: int = None,
        background_color: int = None,
        layout_ids: List[int] = None,
        sub_spec_users: List[str] = None,
        user_panes: List[UpdateMPULayoutRequestUserPanes] = None,
        backgrounds: List[UpdateMPULayoutRequestBackgrounds] = None,
        watermarks: List[UpdateMPULayoutRequestWatermarks] = None,
        clock_widgets: List[UpdateMPULayoutRequestClockWidgets] = None,
    ):
        self.owner_id = owner_id
        self.show_log = show_log
        self.app_id = app_id
        self.task_id = task_id
        self.crop_mode = crop_mode
        self.background_color = background_color
        self.layout_ids = layout_ids
        self.sub_spec_users = sub_spec_users
        self.user_panes = user_panes
        self.backgrounds = backgrounds
        self.watermarks = watermarks
        self.clock_widgets = clock_widgets

    def validate(self):
        if self.user_panes:
            for k in self.user_panes:
                if k:
                    k.validate()
        if self.backgrounds:
            for k in self.backgrounds:
                if k:
                    k.validate()
        if self.watermarks:
            for k in self.watermarks:
                if k:
                    k.validate()
        if self.clock_widgets:
            for k in self.clock_widgets:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.show_log is not None:
            result['ShowLog'] = self.show_log
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.crop_mode is not None:
            result['CropMode'] = self.crop_mode
        if self.background_color is not None:
            result['BackgroundColor'] = self.background_color
        if self.layout_ids is not None:
            result['LayoutIds'] = self.layout_ids
        if self.sub_spec_users is not None:
            result['SubSpecUsers'] = self.sub_spec_users
        result['UserPanes'] = []
        if self.user_panes is not None:
            for k in self.user_panes:
                result['UserPanes'].append(k.to_map() if k else None)
        result['Backgrounds'] = []
        if self.backgrounds is not None:
            for k in self.backgrounds:
                result['Backgrounds'].append(k.to_map() if k else None)
        result['Watermarks'] = []
        if self.watermarks is not None:
            for k in self.watermarks:
                result['Watermarks'].append(k.to_map() if k else None)
        result['ClockWidgets'] = []
        if self.clock_widgets is not None:
            for k in self.clock_widgets:
                result['ClockWidgets'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ShowLog') is not None:
            self.show_log = m.get('ShowLog')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('CropMode') is not None:
            self.crop_mode = m.get('CropMode')
        if m.get('BackgroundColor') is not None:
            self.background_color = m.get('BackgroundColor')
        if m.get('LayoutIds') is not None:
            self.layout_ids = m.get('LayoutIds')
        if m.get('SubSpecUsers') is not None:
            self.sub_spec_users = m.get('SubSpecUsers')
        self.user_panes = []
        if m.get('UserPanes') is not None:
            for k in m.get('UserPanes'):
                temp_model = UpdateMPULayoutRequestUserPanes()
                self.user_panes.append(temp_model.from_map(k))
        self.backgrounds = []
        if m.get('Backgrounds') is not None:
            for k in m.get('Backgrounds'):
                temp_model = UpdateMPULayoutRequestBackgrounds()
                self.backgrounds.append(temp_model.from_map(k))
        self.watermarks = []
        if m.get('Watermarks') is not None:
            for k in m.get('Watermarks'):
                temp_model = UpdateMPULayoutRequestWatermarks()
                self.watermarks.append(temp_model.from_map(k))
        self.clock_widgets = []
        if m.get('ClockWidgets') is not None:
            for k in m.get('ClockWidgets'):
                temp_model = UpdateMPULayoutRequestClockWidgets()
                self.clock_widgets.append(temp_model.from_map(k))
        return self


class UpdateMPULayoutResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateMPULayoutResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateMPULayoutResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateMPULayoutResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateRecordTaskRequestUserPanesImages(TeaModel):
    def __init__(
        self,
        width: float = None,
        height: float = None,
        y: float = None,
        url: str = None,
        display: int = None,
        zorder: int = None,
        x: float = None,
    ):
        self.width = width
        self.height = height
        self.y = y
        self.url = url
        self.display = display
        self.zorder = zorder
        self.x = x

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        if self.y is not None:
            result['Y'] = self.y
        if self.url is not None:
            result['Url'] = self.url
        if self.display is not None:
            result['Display'] = self.display
        if self.zorder is not None:
            result['ZOrder'] = self.zorder
        if self.x is not None:
            result['X'] = self.x
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Display') is not None:
            self.display = m.get('Display')
        if m.get('ZOrder') is not None:
            self.zorder = m.get('ZOrder')
        if m.get('X') is not None:
            self.x = m.get('X')
        return self


class UpdateRecordTaskRequestUserPanesTexts(TeaModel):
    def __init__(
        self,
        font_type: int = None,
        font_color: int = None,
        y: float = None,
        text: str = None,
        zorder: int = None,
        font_size: int = None,
        x: float = None,
    ):
        self.font_type = font_type
        self.font_color = font_color
        self.y = y
        self.text = text
        self.zorder = zorder
        self.font_size = font_size
        self.x = x

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.font_type is not None:
            result['FontType'] = self.font_type
        if self.font_color is not None:
            result['FontColor'] = self.font_color
        if self.y is not None:
            result['Y'] = self.y
        if self.text is not None:
            result['Text'] = self.text
        if self.zorder is not None:
            result['ZOrder'] = self.zorder
        if self.font_size is not None:
            result['FontSize'] = self.font_size
        if self.x is not None:
            result['X'] = self.x
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FontType') is not None:
            self.font_type = m.get('FontType')
        if m.get('FontColor') is not None:
            self.font_color = m.get('FontColor')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('ZOrder') is not None:
            self.zorder = m.get('ZOrder')
        if m.get('FontSize') is not None:
            self.font_size = m.get('FontSize')
        if m.get('X') is not None:
            self.x = m.get('X')
        return self


class UpdateRecordTaskRequestUserPanes(TeaModel):
    def __init__(
        self,
        images: List[UpdateRecordTaskRequestUserPanesImages] = None,
        user_id: str = None,
        texts: List[UpdateRecordTaskRequestUserPanesTexts] = None,
        source_type: str = None,
        pane_id: int = None,
    ):
        self.images = images
        self.user_id = user_id
        self.texts = texts
        self.source_type = source_type
        self.pane_id = pane_id

    def validate(self):
        if self.images:
            for k in self.images:
                if k:
                    k.validate()
        if self.texts:
            for k in self.texts:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Images'] = []
        if self.images is not None:
            for k in self.images:
                result['Images'].append(k.to_map() if k else None)
        if self.user_id is not None:
            result['UserId'] = self.user_id
        result['Texts'] = []
        if self.texts is not None:
            for k in self.texts:
                result['Texts'].append(k.to_map() if k else None)
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.pane_id is not None:
            result['PaneId'] = self.pane_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.images = []
        if m.get('Images') is not None:
            for k in m.get('Images'):
                temp_model = UpdateRecordTaskRequestUserPanesImages()
                self.images.append(temp_model.from_map(k))
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        self.texts = []
        if m.get('Texts') is not None:
            for k in m.get('Texts'):
                temp_model = UpdateRecordTaskRequestUserPanesTexts()
                self.texts.append(temp_model.from_map(k))
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('PaneId') is not None:
            self.pane_id = m.get('PaneId')
        return self


class UpdateRecordTaskRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        show_log: str = None,
        app_id: str = None,
        channel_id: str = None,
        task_id: str = None,
        template_id: str = None,
        sub_spec_users: List[str] = None,
        user_panes: List[UpdateRecordTaskRequestUserPanes] = None,
    ):
        self.owner_id = owner_id
        self.show_log = show_log
        self.app_id = app_id
        self.channel_id = channel_id
        self.task_id = task_id
        self.template_id = template_id
        self.sub_spec_users = sub_spec_users
        self.user_panes = user_panes

    def validate(self):
        if self.user_panes:
            for k in self.user_panes:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.show_log is not None:
            result['ShowLog'] = self.show_log
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.sub_spec_users is not None:
            result['SubSpecUsers'] = self.sub_spec_users
        result['UserPanes'] = []
        if self.user_panes is not None:
            for k in self.user_panes:
                result['UserPanes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ShowLog') is not None:
            self.show_log = m.get('ShowLog')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('SubSpecUsers') is not None:
            self.sub_spec_users = m.get('SubSpecUsers')
        self.user_panes = []
        if m.get('UserPanes') is not None:
            for k in m.get('UserPanes'):
                temp_model = UpdateRecordTaskRequestUserPanes()
                self.user_panes.append(temp_model.from_map(k))
        return self


class UpdateRecordTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateRecordTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateRecordTaskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateRecordTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateRecordTemplateRequestBackgrounds(TeaModel):
    def __init__(
        self,
        width: float = None,
        height: float = None,
        y: float = None,
        url: str = None,
        display: int = None,
        zorder: int = None,
        x: float = None,
    ):
        self.width = width
        self.height = height
        self.y = y
        self.url = url
        self.display = display
        self.zorder = zorder
        self.x = x

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        if self.y is not None:
            result['Y'] = self.y
        if self.url is not None:
            result['Url'] = self.url
        if self.display is not None:
            result['Display'] = self.display
        if self.zorder is not None:
            result['ZOrder'] = self.zorder
        if self.x is not None:
            result['X'] = self.x
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Display') is not None:
            self.display = m.get('Display')
        if m.get('ZOrder') is not None:
            self.zorder = m.get('ZOrder')
        if m.get('X') is not None:
            self.x = m.get('X')
        return self


class UpdateRecordTemplateRequestWatermarks(TeaModel):
    def __init__(
        self,
        alpha: float = None,
        width: float = None,
        height: float = None,
        y: float = None,
        url: str = None,
        display: int = None,
        zorder: int = None,
        x: float = None,
    ):
        self.alpha = alpha
        self.width = width
        self.height = height
        self.y = y
        self.url = url
        self.display = display
        self.zorder = zorder
        self.x = x

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.alpha is not None:
            result['Alpha'] = self.alpha
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        if self.y is not None:
            result['Y'] = self.y
        if self.url is not None:
            result['Url'] = self.url
        if self.display is not None:
            result['Display'] = self.display
        if self.zorder is not None:
            result['ZOrder'] = self.zorder
        if self.x is not None:
            result['X'] = self.x
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alpha') is not None:
            self.alpha = m.get('Alpha')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Display') is not None:
            self.display = m.get('Display')
        if m.get('ZOrder') is not None:
            self.zorder = m.get('ZOrder')
        if m.get('X') is not None:
            self.x = m.get('X')
        return self


class UpdateRecordTemplateRequestClockWidgets(TeaModel):
    def __init__(
        self,
        font_type: int = None,
        font_color: int = None,
        y: float = None,
        zorder: int = None,
        x: float = None,
        font_size: int = None,
    ):
        self.font_type = font_type
        self.font_color = font_color
        self.y = y
        self.zorder = zorder
        self.x = x
        self.font_size = font_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.font_type is not None:
            result['FontType'] = self.font_type
        if self.font_color is not None:
            result['FontColor'] = self.font_color
        if self.y is not None:
            result['Y'] = self.y
        if self.zorder is not None:
            result['ZOrder'] = self.zorder
        if self.x is not None:
            result['X'] = self.x
        if self.font_size is not None:
            result['FontSize'] = self.font_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FontType') is not None:
            self.font_type = m.get('FontType')
        if m.get('FontColor') is not None:
            self.font_color = m.get('FontColor')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        if m.get('ZOrder') is not None:
            self.zorder = m.get('ZOrder')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('FontSize') is not None:
            self.font_size = m.get('FontSize')
        return self


class UpdateRecordTemplateRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        show_log: str = None,
        app_id: str = None,
        name: str = None,
        template_id: str = None,
        task_profile: str = None,
        media_encode: int = None,
        background_color: int = None,
        oss_bucket: str = None,
        oss_file_prefix: str = None,
        mns_queue: str = None,
        http_callback_url: str = None,
        file_split_interval: int = None,
        delay_stop_time: int = None,
        layout_ids: List[int] = None,
        formats: List[str] = None,
        backgrounds: List[UpdateRecordTemplateRequestBackgrounds] = None,
        watermarks: List[UpdateRecordTemplateRequestWatermarks] = None,
        clock_widgets: List[UpdateRecordTemplateRequestClockWidgets] = None,
    ):
        self.owner_id = owner_id
        self.show_log = show_log
        self.app_id = app_id
        self.name = name
        self.template_id = template_id
        self.task_profile = task_profile
        self.media_encode = media_encode
        self.background_color = background_color
        self.oss_bucket = oss_bucket
        self.oss_file_prefix = oss_file_prefix
        self.mns_queue = mns_queue
        self.http_callback_url = http_callback_url
        self.file_split_interval = file_split_interval
        self.delay_stop_time = delay_stop_time
        self.layout_ids = layout_ids
        self.formats = formats
        self.backgrounds = backgrounds
        self.watermarks = watermarks
        self.clock_widgets = clock_widgets

    def validate(self):
        if self.backgrounds:
            for k in self.backgrounds:
                if k:
                    k.validate()
        if self.watermarks:
            for k in self.watermarks:
                if k:
                    k.validate()
        if self.clock_widgets:
            for k in self.clock_widgets:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.show_log is not None:
            result['ShowLog'] = self.show_log
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.name is not None:
            result['Name'] = self.name
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.task_profile is not None:
            result['TaskProfile'] = self.task_profile
        if self.media_encode is not None:
            result['MediaEncode'] = self.media_encode
        if self.background_color is not None:
            result['BackgroundColor'] = self.background_color
        if self.oss_bucket is not None:
            result['OssBucket'] = self.oss_bucket
        if self.oss_file_prefix is not None:
            result['OssFilePrefix'] = self.oss_file_prefix
        if self.mns_queue is not None:
            result['MnsQueue'] = self.mns_queue
        if self.http_callback_url is not None:
            result['HttpCallbackUrl'] = self.http_callback_url
        if self.file_split_interval is not None:
            result['FileSplitInterval'] = self.file_split_interval
        if self.delay_stop_time is not None:
            result['DelayStopTime'] = self.delay_stop_time
        if self.layout_ids is not None:
            result['LayoutIds'] = self.layout_ids
        if self.formats is not None:
            result['Formats'] = self.formats
        result['Backgrounds'] = []
        if self.backgrounds is not None:
            for k in self.backgrounds:
                result['Backgrounds'].append(k.to_map() if k else None)
        result['Watermarks'] = []
        if self.watermarks is not None:
            for k in self.watermarks:
                result['Watermarks'].append(k.to_map() if k else None)
        result['ClockWidgets'] = []
        if self.clock_widgets is not None:
            for k in self.clock_widgets:
                result['ClockWidgets'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ShowLog') is not None:
            self.show_log = m.get('ShowLog')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TaskProfile') is not None:
            self.task_profile = m.get('TaskProfile')
        if m.get('MediaEncode') is not None:
            self.media_encode = m.get('MediaEncode')
        if m.get('BackgroundColor') is not None:
            self.background_color = m.get('BackgroundColor')
        if m.get('OssBucket') is not None:
            self.oss_bucket = m.get('OssBucket')
        if m.get('OssFilePrefix') is not None:
            self.oss_file_prefix = m.get('OssFilePrefix')
        if m.get('MnsQueue') is not None:
            self.mns_queue = m.get('MnsQueue')
        if m.get('HttpCallbackUrl') is not None:
            self.http_callback_url = m.get('HttpCallbackUrl')
        if m.get('FileSplitInterval') is not None:
            self.file_split_interval = m.get('FileSplitInterval')
        if m.get('DelayStopTime') is not None:
            self.delay_stop_time = m.get('DelayStopTime')
        if m.get('LayoutIds') is not None:
            self.layout_ids = m.get('LayoutIds')
        if m.get('Formats') is not None:
            self.formats = m.get('Formats')
        self.backgrounds = []
        if m.get('Backgrounds') is not None:
            for k in m.get('Backgrounds'):
                temp_model = UpdateRecordTemplateRequestBackgrounds()
                self.backgrounds.append(temp_model.from_map(k))
        self.watermarks = []
        if m.get('Watermarks') is not None:
            for k in m.get('Watermarks'):
                temp_model = UpdateRecordTemplateRequestWatermarks()
                self.watermarks.append(temp_model.from_map(k))
        self.clock_widgets = []
        if m.get('ClockWidgets') is not None:
            for k in m.get('ClockWidgets'):
                temp_model = UpdateRecordTemplateRequestClockWidgets()
                self.clock_widgets.append(temp_model.from_map(k))
        return self


class UpdateRecordTemplateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        template_id: str = None,
    ):
        self.request_id = request_id
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class UpdateRecordTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateRecordTemplateResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateRecordTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


