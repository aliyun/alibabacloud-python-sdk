# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict, Any


class BackendCallGroupRequest(TeaModel):
    def __init__(
        self,
        called_number: List[str] = None,
        caller_id_number: str = None,
        country_id: str = None,
        out_id: str = None,
        owner_id: int = None,
        play_times: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        send_type: int = None,
        speed: int = None,
        task_name: str = None,
        timing_start: str = None,
        tts_code: str = None,
        voice_code: str = None,
        volume: int = None,
    ):
        # The called numbers. You can specify up to 50,000 phone numbers.
        self.called_number = called_number
        # The calling number.
        # 
        # If you do not specify this parameter, the system uses a local random number as the display number. If you use a dedicated number for outbound calls, you must specify the purchased number. You can specify only one number. You can log on to the VMS console and choose Number Management to view the purchased phone numbers.
        self.caller_id_number = caller_id_number
        # The ISO2 country code.
        self.country_id = country_id
        # The ID reserved for the caller. This ID is returned to the caller in a receipt message.
        # 
        # The value must be of the STRING type and 1 to 15 bytes in length.
        self.out_id = out_id
        self.owner_id = owner_id
        # The number of times the audio file is played. Valid values: 1 to 3.
        self.play_times = play_times
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The delivery type. Valid values: 1 and 2.
        # 
        # 1: The audio file is delivered immediately.
        # 
        # 2: The audio file is delivered at a scheduled time. If you specify SendType as 2, you must specify TimingStart.
        self.send_type = send_type
        # The playback speed. Valid values: -500 to 500.
        # 
        # You must specify this parameter when the audio type is text-to-speech (TTS). You do not need to specify this parameter when you use recordings.
        self.speed = speed
        # The task name.
        self.task_name = task_name
        # The time when the audio file is scheduled to be delivered.
        self.timing_start = timing_start
        # The voice template ID of the audio file.
        # 
        # You can log on to the VMS console and choose Voice Call Template > Audio File to view the template ID.
        # 
        # You must specify either TtsCode or VoiceCode. You can specify TtsCode to use the audio file as the call content. Alternatively, you can specify VoiceCode to use preset text as the call content.
        self.tts_code = tts_code
        # The TTS template ID.
        # 
        # You can log on to the VMS console and choose Voice Call Template > TTS Template to view the template ID.
        # 
        # You must specify either TtsCode or VoiceCode. You can specify TtsCode to use the audio file as the call content. Alternatively, you can specify VoiceCode to use preset text as the call content.
        self.voice_code = voice_code
        # The playback volume of the audio file. Valid values: 0 to 100. Default value: 100.
        self.volume = volume

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.called_number is not None:
            result['CalledNumber'] = self.called_number
        if self.caller_id_number is not None:
            result['CallerIdNumber'] = self.caller_id_number
        if self.country_id is not None:
            result['CountryId'] = self.country_id
        if self.out_id is not None:
            result['OutId'] = self.out_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.play_times is not None:
            result['PlayTimes'] = self.play_times
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.send_type is not None:
            result['SendType'] = self.send_type
        if self.speed is not None:
            result['Speed'] = self.speed
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.timing_start is not None:
            result['TimingStart'] = self.timing_start
        if self.tts_code is not None:
            result['TtsCode'] = self.tts_code
        if self.voice_code is not None:
            result['VoiceCode'] = self.voice_code
        if self.volume is not None:
            result['Volume'] = self.volume
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CalledNumber') is not None:
            self.called_number = m.get('CalledNumber')
        if m.get('CallerIdNumber') is not None:
            self.caller_id_number = m.get('CallerIdNumber')
        if m.get('CountryId') is not None:
            self.country_id = m.get('CountryId')
        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PlayTimes') is not None:
            self.play_times = m.get('PlayTimes')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SendType') is not None:
            self.send_type = m.get('SendType')
        if m.get('Speed') is not None:
            self.speed = m.get('Speed')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TimingStart') is not None:
            self.timing_start = m.get('TimingStart')
        if m.get('TtsCode') is not None:
            self.tts_code = m.get('TtsCode')
        if m.get('VoiceCode') is not None:
            self.voice_code = m.get('VoiceCode')
        if m.get('Volume') is not None:
            self.volume = m.get('Volume')
        return self


class BackendCallGroupShrinkRequest(TeaModel):
    def __init__(
        self,
        called_number_shrink: str = None,
        caller_id_number: str = None,
        country_id: str = None,
        out_id: str = None,
        owner_id: int = None,
        play_times: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        send_type: int = None,
        speed: int = None,
        task_name: str = None,
        timing_start: str = None,
        tts_code: str = None,
        voice_code: str = None,
        volume: int = None,
    ):
        # The called numbers. You can specify up to 50,000 phone numbers.
        self.called_number_shrink = called_number_shrink
        # The calling number.
        # 
        # If you do not specify this parameter, the system uses a local random number as the display number. If you use a dedicated number for outbound calls, you must specify the purchased number. You can specify only one number. You can log on to the VMS console and choose Number Management to view the purchased phone numbers.
        self.caller_id_number = caller_id_number
        # The ISO2 country code.
        self.country_id = country_id
        # The ID reserved for the caller. This ID is returned to the caller in a receipt message.
        # 
        # The value must be of the STRING type and 1 to 15 bytes in length.
        self.out_id = out_id
        self.owner_id = owner_id
        # The number of times the audio file is played. Valid values: 1 to 3.
        self.play_times = play_times
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The delivery type. Valid values: 1 and 2.
        # 
        # 1: The audio file is delivered immediately.
        # 
        # 2: The audio file is delivered at a scheduled time. If you specify SendType as 2, you must specify TimingStart.
        self.send_type = send_type
        # The playback speed. Valid values: -500 to 500.
        # 
        # You must specify this parameter when the audio type is text-to-speech (TTS). You do not need to specify this parameter when you use recordings.
        self.speed = speed
        # The task name.
        self.task_name = task_name
        # The time when the audio file is scheduled to be delivered.
        self.timing_start = timing_start
        # The voice template ID of the audio file.
        # 
        # You can log on to the VMS console and choose Voice Call Template > Audio File to view the template ID.
        # 
        # You must specify either TtsCode or VoiceCode. You can specify TtsCode to use the audio file as the call content. Alternatively, you can specify VoiceCode to use preset text as the call content.
        self.tts_code = tts_code
        # The TTS template ID.
        # 
        # You can log on to the VMS console and choose Voice Call Template > TTS Template to view the template ID.
        # 
        # You must specify either TtsCode or VoiceCode. You can specify TtsCode to use the audio file as the call content. Alternatively, you can specify VoiceCode to use preset text as the call content.
        self.voice_code = voice_code
        # The playback volume of the audio file. Valid values: 0 to 100. Default value: 100.
        self.volume = volume

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.called_number_shrink is not None:
            result['CalledNumber'] = self.called_number_shrink
        if self.caller_id_number is not None:
            result['CallerIdNumber'] = self.caller_id_number
        if self.country_id is not None:
            result['CountryId'] = self.country_id
        if self.out_id is not None:
            result['OutId'] = self.out_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.play_times is not None:
            result['PlayTimes'] = self.play_times
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.send_type is not None:
            result['SendType'] = self.send_type
        if self.speed is not None:
            result['Speed'] = self.speed
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.timing_start is not None:
            result['TimingStart'] = self.timing_start
        if self.tts_code is not None:
            result['TtsCode'] = self.tts_code
        if self.voice_code is not None:
            result['VoiceCode'] = self.voice_code
        if self.volume is not None:
            result['Volume'] = self.volume
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CalledNumber') is not None:
            self.called_number_shrink = m.get('CalledNumber')
        if m.get('CallerIdNumber') is not None:
            self.caller_id_number = m.get('CallerIdNumber')
        if m.get('CountryId') is not None:
            self.country_id = m.get('CountryId')
        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PlayTimes') is not None:
            self.play_times = m.get('PlayTimes')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SendType') is not None:
            self.send_type = m.get('SendType')
        if m.get('Speed') is not None:
            self.speed = m.get('Speed')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TimingStart') is not None:
            self.timing_start = m.get('TimingStart')
        if m.get('TtsCode') is not None:
            self.tts_code = m.get('TtsCode')
        if m.get('VoiceCode') is not None:
            self.voice_code = m.get('VoiceCode')
        if m.get('Volume') is not None:
            self.volume = m.get('Volume')
        return self


class BackendCallGroupResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        task_id: str = None,
    ):
        # The response code.
        # 
        # The value OK indicates that the request was successful. Other values indicate that the request failed. For more information, see Error codes.
        self.code = code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The task ID. You can use this ID to query the details of the task.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class BackendCallGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BackendCallGroupResponseBody = None,
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
            temp_model = BackendCallGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BackendCallSignalRequest(TeaModel):
    def __init__(
        self,
        called_number: str = None,
        caller_id_number: str = None,
        country_id: str = None,
        out_id: str = None,
        owner_id: int = None,
        play_times: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        speed: int = None,
        tts_code: str = None,
        tts_param: str = None,
        volume: int = None,
    ):
        # The phone number that receives the voice notification.
        # 
        # You must add the country code to the beginning of the phone number. Example: 85200\\*\\*\\*\\*00.
        self.called_number = called_number
        # The calling number.
        # 
        # If you do not specify this parameter, the system uses a local random number as the display number. If you use a dedicated number for outbound calls, you must specify the purchased number. You can specify only one number. You can log on to the VMS console and choose Number Management to view the purchased phone numbers.
        self.caller_id_number = caller_id_number
        # The ISO2 country code.
        self.country_id = country_id
        # The ID reserved for the caller. This ID is returned to the caller in a receipt message.
        # 
        # The value must be of the STRING type and 1 to 15 bytes in length.
        self.out_id = out_id
        self.owner_id = owner_id
        # The number of times the voice notification is played back in a call. Valid values: 1 to 3. Default value: 3.
        self.play_times = play_times
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The playback speed. Valid values: -500 to 500.
        self.speed = speed
        # The ID of the approved voice verification code template.
        # 
        # You can log on to the VMS console and choose Voice Call Template to view the template ID.
        self.tts_code = tts_code
        # The variables in the template, in the JSON format.
        self.tts_param = tts_param
        # The playback volume of the voice notification. Valid values: 0 to 100. Default value: 100.
        self.volume = volume

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.called_number is not None:
            result['CalledNumber'] = self.called_number
        if self.caller_id_number is not None:
            result['CallerIdNumber'] = self.caller_id_number
        if self.country_id is not None:
            result['CountryId'] = self.country_id
        if self.out_id is not None:
            result['OutId'] = self.out_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.play_times is not None:
            result['PlayTimes'] = self.play_times
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.speed is not None:
            result['Speed'] = self.speed
        if self.tts_code is not None:
            result['TtsCode'] = self.tts_code
        if self.tts_param is not None:
            result['TtsParam'] = self.tts_param
        if self.volume is not None:
            result['Volume'] = self.volume
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CalledNumber') is not None:
            self.called_number = m.get('CalledNumber')
        if m.get('CallerIdNumber') is not None:
            self.caller_id_number = m.get('CallerIdNumber')
        if m.get('CountryId') is not None:
            self.country_id = m.get('CountryId')
        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PlayTimes') is not None:
            self.play_times = m.get('PlayTimes')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Speed') is not None:
            self.speed = m.get('Speed')
        if m.get('TtsCode') is not None:
            self.tts_code = m.get('TtsCode')
        if m.get('TtsParam') is not None:
            self.tts_param = m.get('TtsParam')
        if m.get('Volume') is not None:
            self.volume = m.get('Volume')
        return self


class BackendCallSignalResponseBody(TeaModel):
    def __init__(
        self,
        call_id: str = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # The unique receipt ID for the call. You can use this ID to query the details of a single call.
        self.call_id = call_id
        # The response code.
        # 
        # The value OK indicates that the request was successful. Other values indicate that the request failed. For more information, see Error codes.
        self.code = code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_id is not None:
            result['CallId'] = self.call_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BackendCallSignalResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BackendCallSignalResponseBody = None,
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
            temp_model = BackendCallSignalResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GroupCallRequest(TeaModel):
    def __init__(
        self,
        called_number: List[str] = None,
        caller_id_number: str = None,
        country_id: str = None,
        out_id: str = None,
        owner_id: int = None,
        play_times: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        send_type: int = None,
        signature: str = None,
        signature_nonce: str = None,
        speed: int = None,
        task_name: str = None,
        timestamp: str = None,
        timing_start: str = None,
        tts_code: str = None,
        tts_param: str = None,
        voice_code: str = None,
        volume: int = None,
    ):
        # 被叫号码。上限为5万个。
        self.called_number = called_number
        # 主叫号码。  若您不填该参数，系统将会使用当地随机号码作为外显号码。 若您专属号码外呼，则必须传入已购买的号码，仅支持一个号码。您可以登录国际语音服务控制台，选择"号码管理"查看已购买的号码。
        self.caller_id_number = caller_id_number
        # 国家/地区二字码，ISO2。
        self.country_id = country_id
        # 预留给调用方使用的ID，最终会通过在回执消息中将此ID带回给调用方。  字符串类型，长度为1~15个字节。
        self.out_id = out_id
        self.owner_id = owner_id
        # 语音文件的播放次数。取值范围：1~3。
        self.play_times = play_times
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # 发送类型：取值[1,2]。  1： 立即开始发送任务，不等待。  2： 定时开始发送任务。如果传该类型，TimingStart为必选字段。
        self.send_type = send_type
        self.signature = signature
        self.signature_nonce = signature_nonce
        # 语速控制，取值范围：-500~500。  音频类型为TTS时必传。录音文件可不传。
        self.speed = speed
        # 任务名称。
        self.task_name = task_name
        self.timestamp = timestamp
        # 2022-05-01T08:00:00+08:00
        self.timing_start = timing_start
        # 文本转语音的模板ID。  您可以登录国际语音服务控制台，选择"语音模板管理"-"文本转语音模板"，查看模板ID。  此参数与VoiceCode二选一必填。分别代表使用语音文件作为呼叫内容呼叫或者使用固定模板文字作为呼叫内容。
        self.tts_code = tts_code
        # 模板中的变量参数，JSON格式。
        self.tts_param = tts_param
        # 语音文件的模板ID。  您可以登录国际语音服务控制台，选择"语音模板管理"-"语音文件"，查看模板ID。  此参数与TtsCode二选一必填。分别代表使用语音文件作为呼叫内容呼叫或者使用固定模板文字作为呼叫内容。
        self.voice_code = voice_code
        # 语音文件播放的音量。取值范围：0~100，默认取值100。
        self.volume = volume

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.called_number is not None:
            result['CalledNumber'] = self.called_number
        if self.caller_id_number is not None:
            result['CallerIdNumber'] = self.caller_id_number
        if self.country_id is not None:
            result['CountryId'] = self.country_id
        if self.out_id is not None:
            result['OutId'] = self.out_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.play_times is not None:
            result['PlayTimes'] = self.play_times
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.send_type is not None:
            result['SendType'] = self.send_type
        if self.signature is not None:
            result['Signature'] = self.signature
        if self.signature_nonce is not None:
            result['SignatureNonce'] = self.signature_nonce
        if self.speed is not None:
            result['Speed'] = self.speed
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.timing_start is not None:
            result['TimingStart'] = self.timing_start
        if self.tts_code is not None:
            result['TtsCode'] = self.tts_code
        if self.tts_param is not None:
            result['TtsParam'] = self.tts_param
        if self.voice_code is not None:
            result['VoiceCode'] = self.voice_code
        if self.volume is not None:
            result['Volume'] = self.volume
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CalledNumber') is not None:
            self.called_number = m.get('CalledNumber')
        if m.get('CallerIdNumber') is not None:
            self.caller_id_number = m.get('CallerIdNumber')
        if m.get('CountryId') is not None:
            self.country_id = m.get('CountryId')
        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PlayTimes') is not None:
            self.play_times = m.get('PlayTimes')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SendType') is not None:
            self.send_type = m.get('SendType')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        if m.get('SignatureNonce') is not None:
            self.signature_nonce = m.get('SignatureNonce')
        if m.get('Speed') is not None:
            self.speed = m.get('Speed')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('TimingStart') is not None:
            self.timing_start = m.get('TimingStart')
        if m.get('TtsCode') is not None:
            self.tts_code = m.get('TtsCode')
        if m.get('TtsParam') is not None:
            self.tts_param = m.get('TtsParam')
        if m.get('VoiceCode') is not None:
            self.voice_code = m.get('VoiceCode')
        if m.get('Volume') is not None:
            self.volume = m.get('Volume')
        return self


class GroupCallShrinkRequest(TeaModel):
    def __init__(
        self,
        called_number_shrink: str = None,
        caller_id_number: str = None,
        country_id: str = None,
        out_id: str = None,
        owner_id: int = None,
        play_times: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        send_type: int = None,
        signature: str = None,
        signature_nonce: str = None,
        speed: int = None,
        task_name: str = None,
        timestamp: str = None,
        timing_start: str = None,
        tts_code: str = None,
        tts_param: str = None,
        voice_code: str = None,
        volume: int = None,
    ):
        # 被叫号码。上限为5万个。
        self.called_number_shrink = called_number_shrink
        # 主叫号码。  若您不填该参数，系统将会使用当地随机号码作为外显号码。 若您专属号码外呼，则必须传入已购买的号码，仅支持一个号码。您可以登录国际语音服务控制台，选择"号码管理"查看已购买的号码。
        self.caller_id_number = caller_id_number
        # 国家/地区二字码，ISO2。
        self.country_id = country_id
        # 预留给调用方使用的ID，最终会通过在回执消息中将此ID带回给调用方。  字符串类型，长度为1~15个字节。
        self.out_id = out_id
        self.owner_id = owner_id
        # 语音文件的播放次数。取值范围：1~3。
        self.play_times = play_times
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # 发送类型：取值[1,2]。  1： 立即开始发送任务，不等待。  2： 定时开始发送任务。如果传该类型，TimingStart为必选字段。
        self.send_type = send_type
        self.signature = signature
        self.signature_nonce = signature_nonce
        # 语速控制，取值范围：-500~500。  音频类型为TTS时必传。录音文件可不传。
        self.speed = speed
        # 任务名称。
        self.task_name = task_name
        self.timestamp = timestamp
        # 2022-05-01T08:00:00+08:00
        self.timing_start = timing_start
        # 文本转语音的模板ID。  您可以登录国际语音服务控制台，选择"语音模板管理"-"文本转语音模板"，查看模板ID。  此参数与VoiceCode二选一必填。分别代表使用语音文件作为呼叫内容呼叫或者使用固定模板文字作为呼叫内容。
        self.tts_code = tts_code
        # 模板中的变量参数，JSON格式。
        self.tts_param = tts_param
        # 语音文件的模板ID。  您可以登录国际语音服务控制台，选择"语音模板管理"-"语音文件"，查看模板ID。  此参数与TtsCode二选一必填。分别代表使用语音文件作为呼叫内容呼叫或者使用固定模板文字作为呼叫内容。
        self.voice_code = voice_code
        # 语音文件播放的音量。取值范围：0~100，默认取值100。
        self.volume = volume

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.called_number_shrink is not None:
            result['CalledNumber'] = self.called_number_shrink
        if self.caller_id_number is not None:
            result['CallerIdNumber'] = self.caller_id_number
        if self.country_id is not None:
            result['CountryId'] = self.country_id
        if self.out_id is not None:
            result['OutId'] = self.out_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.play_times is not None:
            result['PlayTimes'] = self.play_times
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.send_type is not None:
            result['SendType'] = self.send_type
        if self.signature is not None:
            result['Signature'] = self.signature
        if self.signature_nonce is not None:
            result['SignatureNonce'] = self.signature_nonce
        if self.speed is not None:
            result['Speed'] = self.speed
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.timing_start is not None:
            result['TimingStart'] = self.timing_start
        if self.tts_code is not None:
            result['TtsCode'] = self.tts_code
        if self.tts_param is not None:
            result['TtsParam'] = self.tts_param
        if self.voice_code is not None:
            result['VoiceCode'] = self.voice_code
        if self.volume is not None:
            result['Volume'] = self.volume
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CalledNumber') is not None:
            self.called_number_shrink = m.get('CalledNumber')
        if m.get('CallerIdNumber') is not None:
            self.caller_id_number = m.get('CallerIdNumber')
        if m.get('CountryId') is not None:
            self.country_id = m.get('CountryId')
        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PlayTimes') is not None:
            self.play_times = m.get('PlayTimes')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SendType') is not None:
            self.send_type = m.get('SendType')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        if m.get('SignatureNonce') is not None:
            self.signature_nonce = m.get('SignatureNonce')
        if m.get('Speed') is not None:
            self.speed = m.get('Speed')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('TimingStart') is not None:
            self.timing_start = m.get('TimingStart')
        if m.get('TtsCode') is not None:
            self.tts_code = m.get('TtsCode')
        if m.get('TtsParam') is not None:
            self.tts_param = m.get('TtsParam')
        if m.get('VoiceCode') is not None:
            self.voice_code = m.get('VoiceCode')
        if m.get('Volume') is not None:
            self.volume = m.get('Volume')
        return self


class GroupCallResponseBodyModel(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        # 任务ID，可以通过此ID查询任务的详情。
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GroupCallResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        message: str = None,
        model: GroupCallResponseBodyModel = None,
        request_id: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        # 请求状态码。  返回OK代表请求成功。 其他错误码，请参见API错误码。
        self.code = code
        # 返回信息描述
        self.message = message
        self.model = model
        # 请求ID
        self.request_id = request_id

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.model is not None:
            result['Model'] = self.model.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Model') is not None:
            temp_model = GroupCallResponseBodyModel()
            self.model = temp_model.from_map(m['Model'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GroupCallResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GroupCallResponseBody = None,
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
            temp_model = GroupCallResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SignalCallRequest(TeaModel):
    def __init__(
        self,
        called_number: str = None,
        caller_id_number: str = None,
        country_id: str = None,
        out_id: str = None,
        owner_id: int = None,
        play_times: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        send_type: int = None,
        signature: str = None,
        signature_nonce: str = None,
        speed: int = None,
        task_name: str = None,
        timestamp: str = None,
        timing_start: str = None,
        tts_code: str = None,
        tts_param: str = None,
        voice_code: str = None,
        volume: int = None,
    ):
        # 接收语音通知的手机号码。  号码格式：国际码+号码： 示例：85200****00。
        self.called_number = called_number
        # 主叫号码。  若您不填该参数，系统将会使用当地随机号码作为外显号码。 若您专属号码外呼，则必须传入已购买的号码，仅支持一个号码。您可以登录国际语音服务控制台，选择"号码管理"查看已购买的号码。
        self.caller_id_number = caller_id_number
        # 国家/地区二字码，ISO2。
        self.country_id = country_id
        # 预留给调用方使用的ID，最终会通过在回执消息中将此ID带回给调用方。  字符串类型，长度为1~15个字节。
        self.out_id = out_id
        self.owner_id = owner_id
        # 一通电话内语音通知内容的播放次数。取值范围：1~3，默认取值3。
        self.play_times = play_times
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # 发送类型：取值[1,2]。  1： 立即开始发送任务，不等待。  2： 定时开始发送任务。如果传该类型，TimingStart为必选字段。
        self.send_type = send_type
        self.signature = signature
        self.signature_nonce = signature_nonce
        # 语速控制。取值范围为：-500~500。
        self.speed = speed
        # 任务名称。
        self.task_name = task_name
        self.timestamp = timestamp
        # 定时发送的时间。
        self.timing_start = timing_start
        # 文本转语音模板的语音ID。  您可以登录国际语音服务控制台，选择"语音模板管理"-"文本转语音模板"，查看模板ID。  此参数与VoiceCode二选一必填。分别代表使用语音文件作为呼叫内容呼叫或者使用固定模板文字作为呼叫内容。
        self.tts_code = tts_code
        # 模板中的变量参数，JSON格式。
        self.tts_param = tts_param
        # 语音文件的模板ID。  您可以登录国际语音服务控制台，选择"语音模板管理"-"语音文件"，查看模板ID。  此参数与TtsCode二选一必填。分别代表使用语音文件作为呼叫内容呼叫或者使用固定模板文字作为呼叫内容。
        self.voice_code = voice_code
        # 语音通知的播放音量。取值范围：0~100，默认取值100。
        self.volume = volume

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.called_number is not None:
            result['CalledNumber'] = self.called_number
        if self.caller_id_number is not None:
            result['CallerIdNumber'] = self.caller_id_number
        if self.country_id is not None:
            result['CountryId'] = self.country_id
        if self.out_id is not None:
            result['OutId'] = self.out_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.play_times is not None:
            result['PlayTimes'] = self.play_times
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.send_type is not None:
            result['SendType'] = self.send_type
        if self.signature is not None:
            result['Signature'] = self.signature
        if self.signature_nonce is not None:
            result['SignatureNonce'] = self.signature_nonce
        if self.speed is not None:
            result['Speed'] = self.speed
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.timing_start is not None:
            result['TimingStart'] = self.timing_start
        if self.tts_code is not None:
            result['TtsCode'] = self.tts_code
        if self.tts_param is not None:
            result['TtsParam'] = self.tts_param
        if self.voice_code is not None:
            result['VoiceCode'] = self.voice_code
        if self.volume is not None:
            result['Volume'] = self.volume
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CalledNumber') is not None:
            self.called_number = m.get('CalledNumber')
        if m.get('CallerIdNumber') is not None:
            self.caller_id_number = m.get('CallerIdNumber')
        if m.get('CountryId') is not None:
            self.country_id = m.get('CountryId')
        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PlayTimes') is not None:
            self.play_times = m.get('PlayTimes')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SendType') is not None:
            self.send_type = m.get('SendType')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        if m.get('SignatureNonce') is not None:
            self.signature_nonce = m.get('SignatureNonce')
        if m.get('Speed') is not None:
            self.speed = m.get('Speed')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('TimingStart') is not None:
            self.timing_start = m.get('TimingStart')
        if m.get('TtsCode') is not None:
            self.tts_code = m.get('TtsCode')
        if m.get('TtsParam') is not None:
            self.tts_param = m.get('TtsParam')
        if m.get('VoiceCode') is not None:
            self.voice_code = m.get('VoiceCode')
        if m.get('Volume') is not None:
            self.volume = m.get('Volume')
        return self


class SignalCallResponseBodyModel(TeaModel):
    def __init__(
        self,
        call_id: str = None,
    ):
        # 任务ID，可以通过此ID查询任务的详情。
        self.call_id = call_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_id is not None:
            result['CallId'] = self.call_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')
        return self


class SignalCallResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        message: str = None,
        model: SignalCallResponseBodyModel = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        # 请求状态码。  返回OK代表请求成功。 其他错误码，请参见API错误码。
        self.code = code
        # 返回信息描述。
        self.message = message
        self.model = model
        # 请求ID。
        self.request_id = request_id
        # 请求是否成功，成功：true，失败：false。
        self.success = success

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.model is not None:
            result['Model'] = self.model.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Model') is not None:
            temp_model = SignalCallResponseBodyModel()
            self.model = temp_model.from_map(m['Model'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SignalCallResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SignalCallResponseBody = None,
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
            temp_model = SignalCallResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VoiceGroupCallRequest(TeaModel):
    def __init__(
        self,
        called_number: List[str] = None,
        caller_id_number: str = None,
        country_id: str = None,
        out_id: str = None,
        owner_id: int = None,
        play_times: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        send_type: int = None,
        speed: int = None,
        task_name: str = None,
        timing_start: str = None,
        tts_code: str = None,
        tts_param: str = None,
        voice_code: str = None,
        volume: int = None,
    ):
        self.called_number = called_number
        self.caller_id_number = caller_id_number
        self.country_id = country_id
        self.out_id = out_id
        self.owner_id = owner_id
        self.play_times = play_times
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.send_type = send_type
        self.speed = speed
        self.task_name = task_name
        self.timing_start = timing_start
        self.tts_code = tts_code
        self.tts_param = tts_param
        self.voice_code = voice_code
        self.volume = volume

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.called_number is not None:
            result['CalledNumber'] = self.called_number
        if self.caller_id_number is not None:
            result['CallerIdNumber'] = self.caller_id_number
        if self.country_id is not None:
            result['CountryId'] = self.country_id
        if self.out_id is not None:
            result['OutId'] = self.out_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.play_times is not None:
            result['PlayTimes'] = self.play_times
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.send_type is not None:
            result['SendType'] = self.send_type
        if self.speed is not None:
            result['Speed'] = self.speed
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.timing_start is not None:
            result['TimingStart'] = self.timing_start
        if self.tts_code is not None:
            result['TtsCode'] = self.tts_code
        if self.tts_param is not None:
            result['TtsParam'] = self.tts_param
        if self.voice_code is not None:
            result['VoiceCode'] = self.voice_code
        if self.volume is not None:
            result['Volume'] = self.volume
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CalledNumber') is not None:
            self.called_number = m.get('CalledNumber')
        if m.get('CallerIdNumber') is not None:
            self.caller_id_number = m.get('CallerIdNumber')
        if m.get('CountryId') is not None:
            self.country_id = m.get('CountryId')
        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PlayTimes') is not None:
            self.play_times = m.get('PlayTimes')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SendType') is not None:
            self.send_type = m.get('SendType')
        if m.get('Speed') is not None:
            self.speed = m.get('Speed')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TimingStart') is not None:
            self.timing_start = m.get('TimingStart')
        if m.get('TtsCode') is not None:
            self.tts_code = m.get('TtsCode')
        if m.get('TtsParam') is not None:
            self.tts_param = m.get('TtsParam')
        if m.get('VoiceCode') is not None:
            self.voice_code = m.get('VoiceCode')
        if m.get('Volume') is not None:
            self.volume = m.get('Volume')
        return self


class VoiceGroupCallShrinkRequest(TeaModel):
    def __init__(
        self,
        called_number_shrink: str = None,
        caller_id_number: str = None,
        country_id: str = None,
        out_id: str = None,
        owner_id: int = None,
        play_times: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        send_type: int = None,
        speed: int = None,
        task_name: str = None,
        timing_start: str = None,
        tts_code: str = None,
        tts_param: str = None,
        voice_code: str = None,
        volume: int = None,
    ):
        self.called_number_shrink = called_number_shrink
        self.caller_id_number = caller_id_number
        self.country_id = country_id
        self.out_id = out_id
        self.owner_id = owner_id
        self.play_times = play_times
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.send_type = send_type
        self.speed = speed
        self.task_name = task_name
        self.timing_start = timing_start
        self.tts_code = tts_code
        self.tts_param = tts_param
        self.voice_code = voice_code
        self.volume = volume

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.called_number_shrink is not None:
            result['CalledNumber'] = self.called_number_shrink
        if self.caller_id_number is not None:
            result['CallerIdNumber'] = self.caller_id_number
        if self.country_id is not None:
            result['CountryId'] = self.country_id
        if self.out_id is not None:
            result['OutId'] = self.out_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.play_times is not None:
            result['PlayTimes'] = self.play_times
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.send_type is not None:
            result['SendType'] = self.send_type
        if self.speed is not None:
            result['Speed'] = self.speed
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.timing_start is not None:
            result['TimingStart'] = self.timing_start
        if self.tts_code is not None:
            result['TtsCode'] = self.tts_code
        if self.tts_param is not None:
            result['TtsParam'] = self.tts_param
        if self.voice_code is not None:
            result['VoiceCode'] = self.voice_code
        if self.volume is not None:
            result['Volume'] = self.volume
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CalledNumber') is not None:
            self.called_number_shrink = m.get('CalledNumber')
        if m.get('CallerIdNumber') is not None:
            self.caller_id_number = m.get('CallerIdNumber')
        if m.get('CountryId') is not None:
            self.country_id = m.get('CountryId')
        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PlayTimes') is not None:
            self.play_times = m.get('PlayTimes')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SendType') is not None:
            self.send_type = m.get('SendType')
        if m.get('Speed') is not None:
            self.speed = m.get('Speed')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TimingStart') is not None:
            self.timing_start = m.get('TimingStart')
        if m.get('TtsCode') is not None:
            self.tts_code = m.get('TtsCode')
        if m.get('TtsParam') is not None:
            self.tts_param = m.get('TtsParam')
        if m.get('VoiceCode') is not None:
            self.voice_code = m.get('VoiceCode')
        if m.get('Volume') is not None:
            self.volume = m.get('Volume')
        return self


class VoiceGroupCallResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        message: str = None,
        model: Dict[str, Any] = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.message = message
        self.model = model
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.model is not None:
            result['Model'] = self.model
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class VoiceGroupCallResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: VoiceGroupCallResponseBody = None,
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
            temp_model = VoiceGroupCallResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VoiceSingleCallRequest(TeaModel):
    def __init__(
        self,
        called_number: str = None,
        caller_id_number: str = None,
        country_id: str = None,
        out_id: str = None,
        owner_id: int = None,
        play_times: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        send_type: int = None,
        speed: int = None,
        task_name: str = None,
        timing_start: str = None,
        tts_code: str = None,
        tts_param: str = None,
        voice_code: str = None,
        volume: int = None,
    ):
        self.called_number = called_number
        self.caller_id_number = caller_id_number
        self.country_id = country_id
        self.out_id = out_id
        self.owner_id = owner_id
        self.play_times = play_times
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.send_type = send_type
        self.speed = speed
        self.task_name = task_name
        self.timing_start = timing_start
        self.tts_code = tts_code
        self.tts_param = tts_param
        self.voice_code = voice_code
        self.volume = volume

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.called_number is not None:
            result['CalledNumber'] = self.called_number
        if self.caller_id_number is not None:
            result['CallerIdNumber'] = self.caller_id_number
        if self.country_id is not None:
            result['CountryId'] = self.country_id
        if self.out_id is not None:
            result['OutId'] = self.out_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.play_times is not None:
            result['PlayTimes'] = self.play_times
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.send_type is not None:
            result['SendType'] = self.send_type
        if self.speed is not None:
            result['Speed'] = self.speed
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.timing_start is not None:
            result['TimingStart'] = self.timing_start
        if self.tts_code is not None:
            result['TtsCode'] = self.tts_code
        if self.tts_param is not None:
            result['TtsParam'] = self.tts_param
        if self.voice_code is not None:
            result['VoiceCode'] = self.voice_code
        if self.volume is not None:
            result['Volume'] = self.volume
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CalledNumber') is not None:
            self.called_number = m.get('CalledNumber')
        if m.get('CallerIdNumber') is not None:
            self.caller_id_number = m.get('CallerIdNumber')
        if m.get('CountryId') is not None:
            self.country_id = m.get('CountryId')
        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PlayTimes') is not None:
            self.play_times = m.get('PlayTimes')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SendType') is not None:
            self.send_type = m.get('SendType')
        if m.get('Speed') is not None:
            self.speed = m.get('Speed')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TimingStart') is not None:
            self.timing_start = m.get('TimingStart')
        if m.get('TtsCode') is not None:
            self.tts_code = m.get('TtsCode')
        if m.get('TtsParam') is not None:
            self.tts_param = m.get('TtsParam')
        if m.get('VoiceCode') is not None:
            self.voice_code = m.get('VoiceCode')
        if m.get('Volume') is not None:
            self.volume = m.get('Volume')
        return self


class VoiceSingleCallResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        message: str = None,
        model: Dict[str, Any] = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.message = message
        self.model = model
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.model is not None:
            result['Model'] = self.model
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class VoiceSingleCallResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: VoiceSingleCallResponseBody = None,
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
            temp_model = VoiceSingleCallResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


