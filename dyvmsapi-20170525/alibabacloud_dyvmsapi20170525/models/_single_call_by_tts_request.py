# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SingleCallByTtsRequest(DaraModel):
    def __init__(
        self,
        called_number: str = None,
        called_show_number: str = None,
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
        # The mobile phone number that receives voice notifications.
        # 
        # *   Number format in the Chinese mainland:
        # 
        #     *   Mobile phone number, for example, 159\\*\\*\\*\\*0000.
        #     *   Landline number, for example, 0571\\*\\*\\*\\*5678.
        # 
        # *   Number format outside the Chinese mainland: country code + phone number, for example, 85200\\*\\*\\*\\*00.
        # 
        # > 
        # 
        # *   Each request supports only one called number. For more information, see [How to use voice notifications in the Chinese mainland](https://help.aliyun.com/document_detail/150016.html) or [How to use voice verification codes in regions outside the Chinese mainland](https://help.aliyun.com/document_detail/270044.html).
        # 
        # *   Voice verification codes are sent to a called number at the following frequency: one time per minute, five times per hour, and 20 times per 24 hours.
        # 
        # This parameter is required.
        self.called_number = called_number
        # The number displayed to the called party.
        # 
        # *   You do not need to specify this parameter if you use the text-to-speech (TTS) notification template or voice verification code template for outbound calls in the common mode. For more information, see [FAQ about the common outbound call mode](https://help.aliyun.com/document_detail/172104.html).
        # *   If you use the TTS notification template or voice verification code template for outbound calls in the dedicated mode, you must specify a number you purchased and only one number can be specified. You can log on to the [Voice Messaging Service console](https://dyvms.console.aliyun.com/overview/home) and choose **Voice Numbers** > **Real Number Management** to view the number you purchased.
        self.called_show_number = called_show_number
        # The custom ID that is reserved for the caller of the operation when the request is initiated. This ID is returned to the caller in a receipt message.
        # 
        # The value is of the STRING type and must be 1 to 15 bytes in length.
        self.out_id = out_id
        self.owner_id = owner_id
        # The number of times a voice notification is played back in a call. Valid values: 1 to 3. Default value: 3.
        self.play_times = play_times
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The playback speed. Valid value: -500 to 500.
        self.speed = speed
        # The ID of the approved TTS notification template or voice verification code template.
        # 
        # You can log on to the [Voice Messaging Service console](https://dyvms.console.aliyun.com/overview/home), and choose **Voice Messages** > **Voice Verification Codes** or choose **Voice Messages** > **Voice Notifications** to view the **template ID**.
        # 
        # > The account to which the TTS template belongs must be the same as the account that is used to call the SingleCallByTts operation.
        # 
        # This parameter is required.
        self.tts_code = tts_code
        # The variables in the template, in the JSON format.
        # 
        # > The variables in the template must be less than 250 characters in length. The length of each single variable is not limited. These variables do not support URLs. The variables in the verification code template support only digits and letters.
        self.tts_param = tts_param
        # The playback volume of the voice notification. Valid values: 0 to 100. Default value: 100.
        self.volume = volume

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.called_number is not None:
            result['CalledNumber'] = self.called_number

        if self.called_show_number is not None:
            result['CalledShowNumber'] = self.called_show_number

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

        if m.get('CalledShowNumber') is not None:
            self.called_show_number = m.get('CalledShowNumber')

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

