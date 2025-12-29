# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SingleCallByVoiceRequest(DaraModel):
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
        voice_code: str = None,
        volume: int = None,
    ):
        # The number for receiving voice notifications.
        # 
        # Number format:
        # 
        # *   In the Chinese mainland:
        # 
        #     *   Mobile phone number, for example, 159\\*\\*\\*\\*0000.
        #     *   Landline number, for example, 0571\\*\\*\\*\\*5678.
        # 
        # *   Outside the Chinese mainland: country code + phone number, for example, 85200\\*\\*\\*\\*00.
        # 
        # > 
        # 
        # *   You can specify only one called number for a request. For more information, see [How to use voice notifications in the Chinese mainland](https://help.aliyun.com/document_detail/150016.html) or [How to use voice notifications in regions outside the Chinese mainland](https://help.aliyun.com/document_detail/268810.html).
        # 
        # *   Voice notifications are sent to a called number at the following frequency: one time per minute, five times per hour, and 20 times per 24 hours.
        # 
        # This parameter is required.
        self.called_number = called_number
        # The number displayed to the called party.
        # 
        # *   You do not need to specify this parameter if you use a voice notification file that uses the common outbound call mode. For more information, see [FAQ about the common outbound call mode](https://help.aliyun.com/document_detail/172104.html).
        # *   If you use a voice notification file that uses the dedicated outbound call mode, you must specify a number that you purchased. You can specify only one number. You can log on to the [Voice Messaging Service console](https://dyvms.console.aliyun.com/overview/home) and choose **Real Number Service** > **Real Number Management** to view the number that you purchased.
        self.called_show_number = called_show_number
        # The ID reserved for the caller. This ID is returned to the caller in a receipt message.
        # 
        # The value must be of the STRING type and 1 to 15 bytes in length.
        self.out_id = out_id
        self.owner_id = owner_id
        # The number of times the voice notification file is played. Valid values: 1 to 3.
        self.play_times = play_times
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The playback speed of the voice notification file. Valid values: -500 to 500.
        self.speed = speed
        # The voice ID of the voice notification file.
        # 
        # You can log on to the [Voice Messaging Service console](https://dyvms.console.aliyun.com/overview/home), choose **Voice Messages** > **Voice Notifications** or **Voice File Management**, and then click the **Voice Notification Files** tab to view the **voice ID**.
        # 
        # This parameter is required.
        self.voice_code = voice_code
        # The playback volume of the voice notification file. Valid values: 0 to 100. Default value: 100.
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

        if self.voice_code is not None:
            result['VoiceCode'] = self.voice_code

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

        if m.get('VoiceCode') is not None:
            self.voice_code = m.get('VoiceCode')

        if m.get('Volume') is not None:
            self.volume = m.get('Volume')

        return self

