# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateTemplateRequest(DaraModel):
    def __init__(
        self,
        callback: str = None,
        description: str = None,
        file_format: str = None,
        flv: str = None,
        hls_m3u_8: str = None,
        hls_ts: str = None,
        interval: int = None,
        jpg_on_demand: str = None,
        jpg_overwrite: str = None,
        jpg_sequence: str = None,
        mp_4: str = None,
        name: str = None,
        oss_bucket: str = None,
        oss_endpoint: str = None,
        oss_file_prefix: str = None,
        owner_id: int = None,
        region: str = None,
        retention: int = None,
        trans_configs_json: str = None,
        trigger: str = None,
        type: str = None,
    ):
        self.callback = callback
        self.description = description
        self.file_format = file_format
        self.flv = flv
        self.hls_m3u_8 = hls_m3u_8
        self.hls_ts = hls_ts
        self.interval = interval
        self.jpg_on_demand = jpg_on_demand
        self.jpg_overwrite = jpg_overwrite
        self.jpg_sequence = jpg_sequence
        self.mp_4 = mp_4
        # This parameter is required.
        self.name = name
        self.oss_bucket = oss_bucket
        self.oss_endpoint = oss_endpoint
        self.oss_file_prefix = oss_file_prefix
        self.owner_id = owner_id
        self.region = region
        self.retention = retention
        self.trans_configs_json = trans_configs_json
        self.trigger = trigger
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.callback is not None:
            result['Callback'] = self.callback

        if self.description is not None:
            result['Description'] = self.description

        if self.file_format is not None:
            result['FileFormat'] = self.file_format

        if self.flv is not None:
            result['Flv'] = self.flv

        if self.hls_m3u_8 is not None:
            result['HlsM3u8'] = self.hls_m3u_8

        if self.hls_ts is not None:
            result['HlsTs'] = self.hls_ts

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.jpg_on_demand is not None:
            result['JpgOnDemand'] = self.jpg_on_demand

        if self.jpg_overwrite is not None:
            result['JpgOverwrite'] = self.jpg_overwrite

        if self.jpg_sequence is not None:
            result['JpgSequence'] = self.jpg_sequence

        if self.mp_4 is not None:
            result['Mp4'] = self.mp_4

        if self.name is not None:
            result['Name'] = self.name

        if self.oss_bucket is not None:
            result['OssBucket'] = self.oss_bucket

        if self.oss_endpoint is not None:
            result['OssEndpoint'] = self.oss_endpoint

        if self.oss_file_prefix is not None:
            result['OssFilePrefix'] = self.oss_file_prefix

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region is not None:
            result['Region'] = self.region

        if self.retention is not None:
            result['Retention'] = self.retention

        if self.trans_configs_json is not None:
            result['TransConfigsJSON'] = self.trans_configs_json

        if self.trigger is not None:
            result['Trigger'] = self.trigger

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Callback') is not None:
            self.callback = m.get('Callback')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FileFormat') is not None:
            self.file_format = m.get('FileFormat')

        if m.get('Flv') is not None:
            self.flv = m.get('Flv')

        if m.get('HlsM3u8') is not None:
            self.hls_m3u_8 = m.get('HlsM3u8')

        if m.get('HlsTs') is not None:
            self.hls_ts = m.get('HlsTs')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('JpgOnDemand') is not None:
            self.jpg_on_demand = m.get('JpgOnDemand')

        if m.get('JpgOverwrite') is not None:
            self.jpg_overwrite = m.get('JpgOverwrite')

        if m.get('JpgSequence') is not None:
            self.jpg_sequence = m.get('JpgSequence')

        if m.get('Mp4') is not None:
            self.mp_4 = m.get('Mp4')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OssBucket') is not None:
            self.oss_bucket = m.get('OssBucket')

        if m.get('OssEndpoint') is not None:
            self.oss_endpoint = m.get('OssEndpoint')

        if m.get('OssFilePrefix') is not None:
            self.oss_file_prefix = m.get('OssFilePrefix')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('Retention') is not None:
            self.retention = m.get('Retention')

        if m.get('TransConfigsJSON') is not None:
            self.trans_configs_json = m.get('TransConfigsJSON')

        if m.get('Trigger') is not None:
            self.trigger = m.get('Trigger')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

