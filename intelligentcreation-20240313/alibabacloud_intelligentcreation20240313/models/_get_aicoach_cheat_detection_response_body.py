# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_intelligentcreation20240313 import models as main_models
from darabonba.model import DaraModel

class GetAICoachCheatDetectionResponseBody(DaraModel):
    def __init__(
        self,
        cheat_id: str = None,
        error_code: str = None,
        error_message: str = None,
        gmt_create: str = None,
        image_cheat: main_models.GetAICoachCheatDetectionResponseBodyImageCheat = None,
        request_id: str = None,
        status: int = None,
        success: bool = None,
        voice_cheat: main_models.GetAICoachCheatDetectionResponseBodyVoiceCheat = None,
    ):
        self.cheat_id = cheat_id
        self.error_code = error_code
        self.error_message = error_message
        self.gmt_create = gmt_create
        self.image_cheat = image_cheat
        # Id of the request
        self.request_id = request_id
        self.status = status
        # true
        self.success = success
        self.voice_cheat = voice_cheat

    def validate(self):
        if self.image_cheat:
            self.image_cheat.validate()
        if self.voice_cheat:
            self.voice_cheat.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cheat_id is not None:
            result['cheatId'] = self.cheat_id

        if self.error_code is not None:
            result['errorCode'] = self.error_code

        if self.error_message is not None:
            result['errorMessage'] = self.error_message

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.image_cheat is not None:
            result['imageCheat'] = self.image_cheat.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.status is not None:
            result['status'] = self.status

        if self.success is not None:
            result['success'] = self.success

        if self.voice_cheat is not None:
            result['voiceCheat'] = self.voice_cheat.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cheatId') is not None:
            self.cheat_id = m.get('cheatId')

        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')

        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('imageCheat') is not None:
            temp_model = main_models.GetAICoachCheatDetectionResponseBodyImageCheat()
            self.image_cheat = temp_model.from_map(m.get('imageCheat'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('voiceCheat') is not None:
            temp_model = main_models.GetAICoachCheatDetectionResponseBodyVoiceCheat()
            self.voice_cheat = temp_model.from_map(m.get('voiceCheat'))

        return self

class GetAICoachCheatDetectionResponseBodyVoiceCheat(DaraModel):
    def __init__(
        self,
        comparison_list: List[main_models.GetAICoachCheatDetectionResponseBodyVoiceCheatComparisonList] = None,
        desc: str = None,
        original_list: List[main_models.GetAICoachCheatDetectionResponseBodyVoiceCheatOriginalList] = None,
        status: int = None,
    ):
        self.comparison_list = comparison_list
        self.desc = desc
        self.original_list = original_list
        self.status = status

    def validate(self):
        if self.comparison_list:
            for v1 in self.comparison_list:
                 if v1:
                    v1.validate()
        if self.original_list:
            for v1 in self.original_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['comparisonList'] = []
        if self.comparison_list is not None:
            for k1 in self.comparison_list:
                result['comparisonList'].append(k1.to_map() if k1 else None)

        if self.desc is not None:
            result['desc'] = self.desc

        result['originalList'] = []
        if self.original_list is not None:
            for k1 in self.original_list:
                result['originalList'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.comparison_list = []
        if m.get('comparisonList') is not None:
            for k1 in m.get('comparisonList'):
                temp_model = main_models.GetAICoachCheatDetectionResponseBodyVoiceCheatComparisonList()
                self.comparison_list.append(temp_model.from_map(k1))

        if m.get('desc') is not None:
            self.desc = m.get('desc')

        self.original_list = []
        if m.get('originalList') is not None:
            for k1 in m.get('originalList'):
                temp_model = main_models.GetAICoachCheatDetectionResponseBodyVoiceCheatOriginalList()
                self.original_list.append(temp_model.from_map(k1))

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

class GetAICoachCheatDetectionResponseBodyVoiceCheatOriginalList(DaraModel):
    def __init__(
        self,
        url: str = None,
    ):
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('url') is not None:
            self.url = m.get('url')

        return self

class GetAICoachCheatDetectionResponseBodyVoiceCheatComparisonList(DaraModel):
    def __init__(
        self,
        time: str = None,
        url: str = None,
    ):
        self.time = time
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.time is not None:
            result['time'] = self.time

        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('time') is not None:
            self.time = m.get('time')

        if m.get('url') is not None:
            self.url = m.get('url')

        return self

class GetAICoachCheatDetectionResponseBodyImageCheat(DaraModel):
    def __init__(
        self,
        desc: str = None,
        list: List[main_models.GetAICoachCheatDetectionResponseBodyImageCheatList] = None,
        status: int = None,
    ):
        self.desc = desc
        self.list = list
        self.status = status

    def validate(self):
        if self.list:
            for v1 in self.list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desc is not None:
            result['desc'] = self.desc

        result['list'] = []
        if self.list is not None:
            for k1 in self.list:
                result['list'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('desc') is not None:
            self.desc = m.get('desc')

        self.list = []
        if m.get('list') is not None:
            for k1 in m.get('list'):
                temp_model = main_models.GetAICoachCheatDetectionResponseBodyImageCheatList()
                self.list.append(temp_model.from_map(k1))

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

class GetAICoachCheatDetectionResponseBodyImageCheatList(DaraModel):
    def __init__(
        self,
        time: str = None,
        url: str = None,
    ):
        self.time = time
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.time is not None:
            result['time'] = self.time

        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('time') is not None:
            self.time = m.get('time')

        if m.get('url') is not None:
            self.url = m.get('url')

        return self

