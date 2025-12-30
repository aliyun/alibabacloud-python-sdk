# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class GetDemonstrationForCustomizedVoiceJobResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetDemonstrationForCustomizedVoiceJobResponseBodyData = None,
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
            temp_model = main_models.GetDemonstrationForCustomizedVoiceJobResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetDemonstrationForCustomizedVoiceJobResponseBodyData(DaraModel):
    def __init__(
        self,
        demonstration_list: List[main_models.GetDemonstrationForCustomizedVoiceJobResponseBodyDataDemonstrationList] = None,
    ):
        # A list of 20 text entries to be read and the corresponding sample audio.
        self.demonstration_list = demonstration_list

    def validate(self):
        if self.demonstration_list:
            for v1 in self.demonstration_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DemonstrationList'] = []
        if self.demonstration_list is not None:
            for k1 in self.demonstration_list:
                result['DemonstrationList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.demonstration_list = []
        if m.get('DemonstrationList') is not None:
            for k1 in m.get('DemonstrationList'):
                temp_model = main_models.GetDemonstrationForCustomizedVoiceJobResponseBodyDataDemonstrationList()
                self.demonstration_list.append(temp_model.from_map(k1))

        return self

class GetDemonstrationForCustomizedVoiceJobResponseBodyDataDemonstrationList(DaraModel):
    def __init__(
        self,
        audio_id: int = None,
        demo_audio: str = None,
        text: str = None,
    ):
        # The sequence number of the text, which corresponds to the AduioRecordId parameter to be passed during audio check.
        self.audio_id = audio_id
        # The URL of the sample audio.
        # 
        # *   The value is an Object Storage Service (OSS) URL.
        # 
        #     **
        # 
        #     **Note**: The URL expires in 12 hours.
        self.demo_audio = demo_audio
        # The text content to be read.
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audio_id is not None:
            result['AudioId'] = self.audio_id

        if self.demo_audio is not None:
            result['DemoAudio'] = self.demo_audio

        if self.text is not None:
            result['Text'] = self.text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AudioId') is not None:
            self.audio_id = m.get('AudioId')

        if m.get('DemoAudio') is not None:
            self.demo_audio = m.get('DemoAudio')

        if m.get('Text') is not None:
            self.text = m.get('Text')

        return self

