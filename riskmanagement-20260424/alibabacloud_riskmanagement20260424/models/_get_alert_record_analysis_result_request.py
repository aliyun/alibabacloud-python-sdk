# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_riskmanagement20260424 import models as main_models
from darabonba.model import DaraModel

class GetAlertRecordAnalysisResultRequest(DaraModel):
    def __init__(
        self,
        alarm_unique_info: str = None,
        aliyun_lang: str = None,
        unique_info: str = None,
        unique_tag_list: List[main_models.GetAlertRecordAnalysisResultRequestUniqueTagList] = None,
        uuid: str = None,
    ):
        self.alarm_unique_info = alarm_unique_info
        self.aliyun_lang = aliyun_lang
        self.unique_info = unique_info
        self.unique_tag_list = unique_tag_list
        self.uuid = uuid

    def validate(self):
        if self.unique_tag_list:
            for v1 in self.unique_tag_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alarm_unique_info is not None:
            result['AlarmUniqueInfo'] = self.alarm_unique_info

        if self.aliyun_lang is not None:
            result['AliyunLang'] = self.aliyun_lang

        if self.unique_info is not None:
            result['UniqueInfo'] = self.unique_info

        result['UniqueTagList'] = []
        if self.unique_tag_list is not None:
            for k1 in self.unique_tag_list:
                result['UniqueTagList'].append(k1.to_map() if k1 else None)

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmUniqueInfo') is not None:
            self.alarm_unique_info = m.get('AlarmUniqueInfo')

        if m.get('AliyunLang') is not None:
            self.aliyun_lang = m.get('AliyunLang')

        if m.get('UniqueInfo') is not None:
            self.unique_info = m.get('UniqueInfo')

        self.unique_tag_list = []
        if m.get('UniqueTagList') is not None:
            for k1 in m.get('UniqueTagList'):
                temp_model = main_models.GetAlertRecordAnalysisResultRequestUniqueTagList()
                self.unique_tag_list.append(temp_model.from_map(k1))

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

class GetAlertRecordAnalysisResultRequestUniqueTagList(DaraModel):
    def __init__(
        self,
        alarm_unique_info: str = None,
        choose_like: bool = None,
        ip: str = None,
        machine_instance_id: str = None,
        query_time: str = None,
        type: str = None,
        unique_info: str = None,
        uuid: str = None,
    ):
        self.alarm_unique_info = alarm_unique_info
        self.choose_like = choose_like
        self.ip = ip
        self.machine_instance_id = machine_instance_id
        self.query_time = query_time
        self.type = type
        self.unique_info = unique_info
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alarm_unique_info is not None:
            result['AlarmUniqueInfo'] = self.alarm_unique_info

        if self.choose_like is not None:
            result['ChooseLike'] = self.choose_like

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.machine_instance_id is not None:
            result['MachineInstanceId'] = self.machine_instance_id

        if self.query_time is not None:
            result['QueryTime'] = self.query_time

        if self.type is not None:
            result['Type'] = self.type

        if self.unique_info is not None:
            result['UniqueInfo'] = self.unique_info

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmUniqueInfo') is not None:
            self.alarm_unique_info = m.get('AlarmUniqueInfo')

        if m.get('ChooseLike') is not None:
            self.choose_like = m.get('ChooseLike')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('MachineInstanceId') is not None:
            self.machine_instance_id = m.get('MachineInstanceId')

        if m.get('QueryTime') is not None:
            self.query_time = m.get('QueryTime')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UniqueInfo') is not None:
            self.unique_info = m.get('UniqueInfo')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

