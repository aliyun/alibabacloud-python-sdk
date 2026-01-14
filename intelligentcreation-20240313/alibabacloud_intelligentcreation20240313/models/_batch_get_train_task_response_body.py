# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_intelligentcreation20240313 import models as main_models
from darabonba.model import DaraModel

class BatchGetTrainTaskResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        voice_list: List[main_models.BatchGetTrainTaskResponseBodyVoiceList] = None,
    ):
        self.request_id = request_id
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
        if self.request_id is not None:
            result['requestId'] = self.request_id

        result['voiceList'] = []
        if self.voice_list is not None:
            for k1 in self.voice_list:
                result['voiceList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.voice_list = []
        if m.get('voiceList') is not None:
            for k1 in m.get('voiceList'):
                temp_model = main_models.BatchGetTrainTaskResponseBodyVoiceList()
                self.voice_list.append(temp_model.from_map(k1))

        return self

class BatchGetTrainTaskResponseBodyVoiceList(DaraModel):
    def __init__(
        self,
        aliyun_sub_id: str = None,
        audit_fail_message: str = None,
        audit_status: str = None,
        create_time: str = None,
        gender: str = None,
        name: str = None,
        res_spec_type: str = None,
        task_id: str = None,
        task_type: str = None,
        train_fail_message: str = None,
        train_status: str = None,
        use_scene: str = None,
        voice_material: main_models.BatchGetTrainTaskResponseBodyVoiceListVoiceMaterial = None,
    ):
        self.aliyun_sub_id = aliyun_sub_id
        self.audit_fail_message = audit_fail_message
        self.audit_status = audit_status
        self.create_time = create_time
        self.gender = gender
        self.name = name
        self.res_spec_type = res_spec_type
        self.task_id = task_id
        self.task_type = task_type
        self.train_fail_message = train_fail_message
        self.train_status = train_status
        self.use_scene = use_scene
        self.voice_material = voice_material

    def validate(self):
        if self.voice_material:
            self.voice_material.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliyun_sub_id is not None:
            result['aliyunSubId'] = self.aliyun_sub_id

        if self.audit_fail_message is not None:
            result['auditFailMessage'] = self.audit_fail_message

        if self.audit_status is not None:
            result['auditStatus'] = self.audit_status

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.gender is not None:
            result['gender'] = self.gender

        if self.name is not None:
            result['name'] = self.name

        if self.res_spec_type is not None:
            result['resSpecType'] = self.res_spec_type

        if self.task_id is not None:
            result['taskId'] = self.task_id

        if self.task_type is not None:
            result['taskType'] = self.task_type

        if self.train_fail_message is not None:
            result['trainFailMessage'] = self.train_fail_message

        if self.train_status is not None:
            result['trainStatus'] = self.train_status

        if self.use_scene is not None:
            result['useScene'] = self.use_scene

        if self.voice_material is not None:
            result['voiceMaterial'] = self.voice_material.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aliyunSubId') is not None:
            self.aliyun_sub_id = m.get('aliyunSubId')

        if m.get('auditFailMessage') is not None:
            self.audit_fail_message = m.get('auditFailMessage')

        if m.get('auditStatus') is not None:
            self.audit_status = m.get('auditStatus')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('gender') is not None:
            self.gender = m.get('gender')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('resSpecType') is not None:
            self.res_spec_type = m.get('resSpecType')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        if m.get('taskType') is not None:
            self.task_type = m.get('taskType')

        if m.get('trainFailMessage') is not None:
            self.train_fail_message = m.get('trainFailMessage')

        if m.get('trainStatus') is not None:
            self.train_status = m.get('trainStatus')

        if m.get('useScene') is not None:
            self.use_scene = m.get('useScene')

        if m.get('voiceMaterial') is not None:
            temp_model = main_models.BatchGetTrainTaskResponseBodyVoiceListVoiceMaterial()
            self.voice_material = temp_model.from_map(m.get('voiceMaterial'))

        return self

class BatchGetTrainTaskResponseBodyVoiceListVoiceMaterial(DaraModel):
    def __init__(
        self,
        voice_id: int = None,
        voice_language: str = None,
        voice_url: str = None,
    ):
        self.voice_id = voice_id
        self.voice_language = voice_language
        self.voice_url = voice_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.voice_id is not None:
            result['voiceId'] = self.voice_id

        if self.voice_language is not None:
            result['voiceLanguage'] = self.voice_language

        if self.voice_url is not None:
            result['voiceUrl'] = self.voice_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('voiceId') is not None:
            self.voice_id = m.get('voiceId')

        if m.get('voiceLanguage') is not None:
            self.voice_language = m.get('voiceLanguage')

        if m.get('voiceUrl') is not None:
            self.voice_url = m.get('voiceUrl')

        return self

