# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class ListCustomizedVoicesResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListCustomizedVoicesResponseBodyData = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The data returned.
        self.data = data
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.ListCustomizedVoicesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListCustomizedVoicesResponseBodyData(DaraModel):
    def __init__(
        self,
        customized_voice_list: List[main_models.ListCustomizedVoicesResponseBodyDataCustomizedVoiceList] = None,
        total_count: int = None,
    ):
        # The queried personalized human voices.
        self.customized_voice_list = customized_voice_list
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.customized_voice_list:
            for v1 in self.customized_voice_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CustomizedVoiceList'] = []
        if self.customized_voice_list is not None:
            for k1 in self.customized_voice_list:
                result['CustomizedVoiceList'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.customized_voice_list = []
        if m.get('CustomizedVoiceList') is not None:
            for k1 in m.get('CustomizedVoiceList'):
                temp_model = main_models.ListCustomizedVoicesResponseBodyDataCustomizedVoiceList()
                self.customized_voice_list.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListCustomizedVoicesResponseBodyDataCustomizedVoiceList(DaraModel):
    def __init__(
        self,
        demo_audio_media_id: str = None,
        gender: str = None,
        scenario: str = None,
        type: str = None,
        voice_desc: str = None,
        voice_id: str = None,
        voice_name: str = None,
    ):
        # The media asset ID of the sample audio file.
        self.demo_audio_media_id = demo_audio_media_id
        # The gender. Valid values:
        # 
        # *   female
        # *   male
        self.gender = gender
        # The scenario. Valid values:
        # 
        # *   story
        # *   interaction
        # *   navigation
        self.scenario = scenario
        # *   The voice type. Valid values:
        # 
        #     *   Basic
        #     *   Standard
        self.type = type
        # The voice description.
        self.voice_desc = voice_desc
        # The voice ID.
        self.voice_id = voice_id
        # The voice name.
        self.voice_name = voice_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.demo_audio_media_id is not None:
            result['DemoAudioMediaId'] = self.demo_audio_media_id

        if self.gender is not None:
            result['Gender'] = self.gender

        if self.scenario is not None:
            result['Scenario'] = self.scenario

        if self.type is not None:
            result['Type'] = self.type

        if self.voice_desc is not None:
            result['VoiceDesc'] = self.voice_desc

        if self.voice_id is not None:
            result['VoiceId'] = self.voice_id

        if self.voice_name is not None:
            result['VoiceName'] = self.voice_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DemoAudioMediaId') is not None:
            self.demo_audio_media_id = m.get('DemoAudioMediaId')

        if m.get('Gender') is not None:
            self.gender = m.get('Gender')

        if m.get('Scenario') is not None:
            self.scenario = m.get('Scenario')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('VoiceDesc') is not None:
            self.voice_desc = m.get('VoiceDesc')

        if m.get('VoiceId') is not None:
            self.voice_id = m.get('VoiceId')

        if m.get('VoiceName') is not None:
            self.voice_name = m.get('VoiceName')

        return self

