# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dyvmsapi20170525 import models as main_models
from darabonba.model import DaraModel

class IvrCallRequest(DaraModel):
    def __init__(
        self,
        bye_code: str = None,
        bye_tts_params: str = None,
        called_number: str = None,
        called_show_number: str = None,
        menu_key_map: List[main_models.IvrCallRequestMenuKeyMap] = None,
        out_id: str = None,
        owner_id: int = None,
        play_times: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        start_code: str = None,
        start_tts_params: str = None,
        timeout: int = None,
    ):
        # The end voice.
        # 
        # *   If you use a voice notification file, this parameter specifies the voice ID. You can log on to the [Voice Messaging Service console](https://dyvms.console.aliyun.com/overview/home), choose **Voice Messages** > **Voice Notifications**, and then click the **Voice Notification Files** tab to view the voice ID.
        # *   If you use a TTS template, this parameter specifies the template ID. You can log on to the [Voice Messaging Service console](https://dyvms.console.aliyun.com/overview/home), choose **Voice Messages** > **Voice Notifications**, and then click the **TTS Template** tab to view the template ID.
        # 
        # > The value of the ByeCode parameter must be of the same type as the value of the StartCode parameter. This means that both parameters must specify voice IDs or TTS template IDs.
        self.bye_code = bye_code
        # The variables in the TTS template, in the JSON format.
        # 
        # > This parameter is required when the ByeCode parameter is set to the ID of a TTS template that contains variables.
        self.bye_tts_params = bye_tts_params
        # The called number.
        # 
        # Only phone numbers in the Chinese mainland are supported. Each request supports only one called number.
        # 
        # This parameter is required.
        self.called_number = called_number
        # The calling number.
        # 
        # The value must be a number you purchased. Each request supports only one calling number. In most cases, a calling number is configured with the maximum number of concurrent requests. New requests fail if the maximum number of concurrent requests is reached. You can log on to the [Voice Messaging Service console](https://dyvms.console.aliyun.com/overview/home) and choose **Real Number Service > Real Number Management** to view the number you purchased.
        # 
        # This parameter is required.
        self.called_show_number = called_show_number
        # The information about the key pressed by the subscriber.
        self.menu_key_map = menu_key_map
        # The ID that is reserved for the caller of the operation. This ID is returned to the caller in a receipt message.
        # 
        # The value is of the STRING type and must be 1 to 15 bytes in length.
        self.out_id = out_id
        self.owner_id = owner_id
        # The number of replay times. Valid values: 1 to 3.
        self.play_times = play_times
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The voice that is played when the call begins.
        # 
        # *   If you use a voice notification file, this parameter specifies the voice ID. You can log on to the [Voice Messaging Service console](https://dyvms.console.aliyun.com/overview/home), choose **Voice Messages** > Voice Notifications, and then click the **Voice Notification Files** tab to view the voice ID.
        # *   If you use a text-to-speech (TTS) template, this parameter specifies the template ID. You can log on to the [Voice Messaging Service console](https://dyvms.console.aliyun.com/overview/home), choose **Voice Messages** > **Voice Notifications**, and then click the **TTS Template** tab to view the template ID.
        # 
        # This parameter is required.
        self.start_code = start_code
        # The variables in the TTS template, in the JSON format.
        # 
        # > This parameter is required when the StartCode parameter is set to the ID of a TTS template that contains variables.
        self.start_tts_params = start_tts_params
        # The timeout period for the subscriber to press a key. Unit: milliseconds.
        self.timeout = timeout

    def validate(self):
        if self.menu_key_map:
            for v1 in self.menu_key_map:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bye_code is not None:
            result['ByeCode'] = self.bye_code

        if self.bye_tts_params is not None:
            result['ByeTtsParams'] = self.bye_tts_params

        if self.called_number is not None:
            result['CalledNumber'] = self.called_number

        if self.called_show_number is not None:
            result['CalledShowNumber'] = self.called_show_number

        result['MenuKeyMap'] = []
        if self.menu_key_map is not None:
            for k1 in self.menu_key_map:
                result['MenuKeyMap'].append(k1.to_map() if k1 else None)

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

        if self.start_code is not None:
            result['StartCode'] = self.start_code

        if self.start_tts_params is not None:
            result['StartTtsParams'] = self.start_tts_params

        if self.timeout is not None:
            result['Timeout'] = self.timeout

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ByeCode') is not None:
            self.bye_code = m.get('ByeCode')

        if m.get('ByeTtsParams') is not None:
            self.bye_tts_params = m.get('ByeTtsParams')

        if m.get('CalledNumber') is not None:
            self.called_number = m.get('CalledNumber')

        if m.get('CalledShowNumber') is not None:
            self.called_show_number = m.get('CalledShowNumber')

        self.menu_key_map = []
        if m.get('MenuKeyMap') is not None:
            for k1 in m.get('MenuKeyMap'):
                temp_model = main_models.IvrCallRequestMenuKeyMap()
                self.menu_key_map.append(temp_model.from_map(k1))

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

        if m.get('StartCode') is not None:
            self.start_code = m.get('StartCode')

        if m.get('StartTtsParams') is not None:
            self.start_tts_params = m.get('StartTtsParams')

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        return self

class IvrCallRequestMenuKeyMap(DaraModel):
    def __init__(
        self,
        code: str = None,
        key: str = None,
        tts_params: str = None,
    ):
        # The voice that corresponds to the key specified by the **MenuKeyMap.N.Key** parameter.
        # 
        # *   If you use a voice notification file, this parameter specifies the voice ID. You can log on to the [Voice Messaging Service console](https://dyvms.console.aliyun.com/overview/home), choose **Voice Messages** > **Voice Notifications**, and then click the **Voice Notification Files** tab to view the voice ID.
        # *   If you use a TTS template, this parameter specifies the template ID. You can log on to the [Voice Messaging Service console](https://dyvms.console.aliyun.com/overview/home), choose **Voice Messages** > **Voice Notifications**, and then click the **TTS Template** tab to view the template ID.
        self.code = code
        # The key that can be pressed by the subscriber.
        self.key = key
        # The variables in the TTS template, in the JSON format.
        # 
        # > 
        # 
        # *   This parameter specifies the substitution relationship of the variables in the TTS template if the value of the **MenuKeyMap.N.Code** parameter is set to the ID of the TTS template.
        # 
        # *   This parameter is required if the value of the **MenuKeyMap.N.Code** parameter is set to the ID of a TTS template that contains variables.
        self.tts_params = tts_params

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.key is not None:
            result['Key'] = self.key

        if self.tts_params is not None:
            result['TtsParams'] = self.tts_params

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('TtsParams') is not None:
            self.tts_params = m.get('TtsParams')

        return self

