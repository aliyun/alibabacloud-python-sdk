# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class ListSmartVoiceGroupsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        voice_groups: List[main_models.ListSmartVoiceGroupsResponseBodyVoiceGroups] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The queried speaker groups.
        self.voice_groups = voice_groups

    def validate(self):
        if self.voice_groups:
            for v1 in self.voice_groups:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['VoiceGroups'] = []
        if self.voice_groups is not None:
            for k1 in self.voice_groups:
                result['VoiceGroups'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.voice_groups = []
        if m.get('VoiceGroups') is not None:
            for k1 in m.get('VoiceGroups'):
                temp_model = main_models.ListSmartVoiceGroupsResponseBodyVoiceGroups()
                self.voice_groups.append(temp_model.from_map(k1))

        return self

class ListSmartVoiceGroupsResponseBodyVoiceGroups(DaraModel):
    def __init__(
        self,
        type: str = None,
        voice_list: List[main_models.ListSmartVoiceGroupsResponseBodyVoiceGroupsVoiceList] = None,
    ):
        # The name of the speaker group.
        self.type = type
        # The speakers.
        self.voice_list = voice_list

    def validate(self):
        if self.voice_list:
            for v1 in self.voice_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.type is not None:
            result['Type'] = self.type

        result['VoiceList'] = []
        if self.voice_list is not None:
            for k1 in self.voice_list:
                result['VoiceList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')

        self.voice_list = []
        if m.get('VoiceList') is not None:
            for k1 in m.get('VoiceList'):
                temp_model = main_models.ListSmartVoiceGroupsResponseBodyVoiceGroupsVoiceList()
                self.voice_list.append(temp_model.from_map(k1))

        return self

class ListSmartVoiceGroupsResponseBodyVoiceGroupsVoiceList(DaraModel):
    def __init__(
        self,
        desc: str = None,
        name: str = None,
        remark: str = None,
        support_sample_rate: str = None,
        tag: str = None,
        voice: str = None,
        voice_source: str = None,
        voice_type: str = None,
        voice_url: str = None,
    ):
        # The speaker description.
        self.desc = desc
        # The speaker name.
        self.name = name
        # The remarks of the speaker.
        self.remark = remark
        self.support_sample_rate = support_sample_rate
        # The tag of the speaker type.
        self.tag = tag
        # The speaker ID.
        self.voice = voice
        self.voice_source = voice_source
        # The speaker type.
        # 
        # Valid values:
        # 
        # *   Male
        # *   Female
        # *   Boy
        # *   Girl
        self.voice_type = voice_type
        # The URL of the sample audio file.
        self.voice_url = voice_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desc is not None:
            result['Desc'] = self.desc

        if self.name is not None:
            result['Name'] = self.name

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.support_sample_rate is not None:
            result['SupportSampleRate'] = self.support_sample_rate

        if self.tag is not None:
            result['Tag'] = self.tag

        if self.voice is not None:
            result['Voice'] = self.voice

        if self.voice_source is not None:
            result['VoiceSource'] = self.voice_source

        if self.voice_type is not None:
            result['VoiceType'] = self.voice_type

        if self.voice_url is not None:
            result['VoiceUrl'] = self.voice_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('SupportSampleRate') is not None:
            self.support_sample_rate = m.get('SupportSampleRate')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        if m.get('Voice') is not None:
            self.voice = m.get('Voice')

        if m.get('VoiceSource') is not None:
            self.voice_source = m.get('VoiceSource')

        if m.get('VoiceType') is not None:
            self.voice_type = m.get('VoiceType')

        if m.get('VoiceUrl') is not None:
            self.voice_url = m.get('VoiceUrl')

        return self

