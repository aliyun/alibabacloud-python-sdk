# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rtc20180111 import models as main_models
from darabonba.model import DaraModel

class ModifyAppRecordTemplateRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        client_token: str = None,
        record_template: main_models.ModifyAppRecordTemplateRequestRecordTemplate = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        self.client_token = client_token
        # This parameter is required.
        self.record_template = record_template

    def validate(self):
        if self.record_template:
            self.record_template.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.record_template is not None:
            result['RecordTemplate'] = self.record_template.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('RecordTemplate') is not None:
            temp_model = main_models.ModifyAppRecordTemplateRequestRecordTemplate()
            self.record_template = temp_model.from_map(m.get('RecordTemplate'))

        return self

class ModifyAppRecordTemplateRequestRecordTemplate(DaraModel):
    def __init__(
        self,
        delay_stop_time: int = None,
        file_prefix: str = None,
        file_split_interval: int = None,
        formats: List[str] = None,
        layout_ids: List[str] = None,
        media_encode: int = None,
        name: str = None,
        template_id: str = None,
    ):
        self.delay_stop_time = delay_stop_time
        # This parameter is required.
        self.file_prefix = file_prefix
        # This parameter is required.
        self.file_split_interval = file_split_interval
        # This parameter is required.
        self.formats = formats
        # This parameter is required.
        self.layout_ids = layout_ids
        # This parameter is required.
        self.media_encode = media_encode
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.delay_stop_time is not None:
            result['DelayStopTime'] = self.delay_stop_time

        if self.file_prefix is not None:
            result['FilePrefix'] = self.file_prefix

        if self.file_split_interval is not None:
            result['FileSplitInterval'] = self.file_split_interval

        if self.formats is not None:
            result['Formats'] = self.formats

        if self.layout_ids is not None:
            result['LayoutIds'] = self.layout_ids

        if self.media_encode is not None:
            result['MediaEncode'] = self.media_encode

        if self.name is not None:
            result['Name'] = self.name

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DelayStopTime') is not None:
            self.delay_stop_time = m.get('DelayStopTime')

        if m.get('FilePrefix') is not None:
            self.file_prefix = m.get('FilePrefix')

        if m.get('FileSplitInterval') is not None:
            self.file_split_interval = m.get('FileSplitInterval')

        if m.get('Formats') is not None:
            self.formats = m.get('Formats')

        if m.get('LayoutIds') is not None:
            self.layout_ids = m.get('LayoutIds')

        if m.get('MediaEncode') is not None:
            self.media_encode = m.get('MediaEncode')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

