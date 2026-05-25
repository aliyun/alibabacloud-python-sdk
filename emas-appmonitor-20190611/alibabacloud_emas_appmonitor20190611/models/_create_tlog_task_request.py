# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateTlogTaskRequest(DaraModel):
    def __init__(
        self,
        ali_yun_current_pk: str = None,
        ali_yun_main_pk: str = None,
        ali_yun_name: str = None,
        app_key: int = None,
        app_version: str = None,
        begin_date: int = None,
        brand: str = None,
        city: str = None,
        cluster_id: str = None,
        collection_nums: int = None,
        days: str = None,
        device_json: str = None,
        end_date: int = None,
        error_type: str = None,
        model: str = None,
        notify_setting_json: str = None,
        os: str = None,
        os_version: str = None,
        source_type: str = None,
        task_name: str = None,
    ):
        self.ali_yun_current_pk = ali_yun_current_pk
        self.ali_yun_main_pk = ali_yun_main_pk
        # This parameter is required.
        self.ali_yun_name = ali_yun_name
        # This parameter is required.
        self.app_key = app_key
        self.app_version = app_version
        self.begin_date = begin_date
        self.brand = brand
        self.city = city
        self.cluster_id = cluster_id
        self.collection_nums = collection_nums
        self.days = days
        self.device_json = device_json
        self.end_date = end_date
        self.error_type = error_type
        self.model = model
        self.notify_setting_json = notify_setting_json
        # This parameter is required.
        self.os = os
        self.os_version = os_version
        self.source_type = source_type
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ali_yun_current_pk is not None:
            result['AliYunCurrentPk'] = self.ali_yun_current_pk

        if self.ali_yun_main_pk is not None:
            result['AliYunMainPk'] = self.ali_yun_main_pk

        if self.ali_yun_name is not None:
            result['AliYunName'] = self.ali_yun_name

        if self.app_key is not None:
            result['AppKey'] = self.app_key

        if self.app_version is not None:
            result['AppVersion'] = self.app_version

        if self.begin_date is not None:
            result['BeginDate'] = self.begin_date

        if self.brand is not None:
            result['Brand'] = self.brand

        if self.city is not None:
            result['City'] = self.city

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.collection_nums is not None:
            result['CollectionNums'] = self.collection_nums

        if self.days is not None:
            result['Days'] = self.days

        if self.device_json is not None:
            result['DeviceJson'] = self.device_json

        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.error_type is not None:
            result['ErrorType'] = self.error_type

        if self.model is not None:
            result['Model'] = self.model

        if self.notify_setting_json is not None:
            result['NotifySettingJson'] = self.notify_setting_json

        if self.os is not None:
            result['Os'] = self.os

        if self.os_version is not None:
            result['OsVersion'] = self.os_version

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliYunCurrentPk') is not None:
            self.ali_yun_current_pk = m.get('AliYunCurrentPk')

        if m.get('AliYunMainPk') is not None:
            self.ali_yun_main_pk = m.get('AliYunMainPk')

        if m.get('AliYunName') is not None:
            self.ali_yun_name = m.get('AliYunName')

        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')

        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')

        if m.get('BeginDate') is not None:
            self.begin_date = m.get('BeginDate')

        if m.get('Brand') is not None:
            self.brand = m.get('Brand')

        if m.get('City') is not None:
            self.city = m.get('City')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('CollectionNums') is not None:
            self.collection_nums = m.get('CollectionNums')

        if m.get('Days') is not None:
            self.days = m.get('Days')

        if m.get('DeviceJson') is not None:
            self.device_json = m.get('DeviceJson')

        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('ErrorType') is not None:
            self.error_type = m.get('ErrorType')

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('NotifySettingJson') is not None:
            self.notify_setting_json = m.get('NotifySettingJson')

        if m.get('Os') is not None:
            self.os = m.get('Os')

        if m.get('OsVersion') is not None:
            self.os_version = m.get('OsVersion')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        return self

