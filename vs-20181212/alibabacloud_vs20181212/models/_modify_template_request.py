# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyTemplateRequest(DaraModel):
    def __init__(
        self,
        callback: str = None,
        description: str = None,
        file_format: str = None,
        flv: str = None,
        hls_m3u_8: str = None,
        hls_ts: str = None,
        id: str = None,
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
    ):
        # The callback URL that is used after the template is executed.
        self.callback = callback
        # The description of the template.
        self.description = description
        # The file format for storage. Separate multiple values with commas. Valid values:
        # 
        # - mp4
        # 
        # - flv
        # 
        # - hls
        # 
        # > Recording in FLV and MP4 formats is not supported in the China (Qingdao) region.
        self.file_format = file_format
        # The storage path for FLV files. For information about the format, see the description of the Mp4 parameter.
        self.flv = flv
        # The storage path for HLS M3U8 files. For information about the format, see the description of the Mp4 parameter.
        self.hls_m3u_8 = hls_m3u_8
        # The storage path for HLS TS files.
        # 
        # - The path supports variables such as {AppName}, {StreamName}, {UnixTimestamp}, and {Sequence}.
        # 
        # - You must include the {UnixTimestamp} and {Sequence} variables.
        self.hls_ts = hls_ts
        # The ID of the template.
        # 
        # This parameter is required.
        self.id = id
        # The operation interval, in seconds.
        self.interval = interval
        # The storage path for JPG files. This path is used for on-demand snapshots.
        # 
        # - Only JPG images are supported.
        # 
        # - The path supports variables such as {AppName}, {StreamName}, {UnixTimestamp}, and {Sequence}.
        # 
        # - You must include either {UnixTimestamp} or {Sequence}.
        self.jpg_on_demand = jpg_on_demand
        # The storage path for JPG files. This path is used to overwrite snapshots.
        # 
        # - Only JPG images are supported.
        # 
        # - The path supports variables such as {AppName} and {StreamName}.
        self.jpg_overwrite = jpg_overwrite
        # The storage path for JPG files. This path is used for sequence snapshots.
        # 
        # - Only JPG images are supported.
        # 
        # - The path supports variables such as {AppName}, {StreamName}, {UnixTimestamp}, and {Sequence}.
        # 
        # - You must include either {UnixTimestamp} or {Sequence}.
        self.jpg_sequence = jpg_sequence
        # The storage path for MP4 files.
        # 
        # - The path supports variables such as {AppName}, {StreamName}, {Sequence}, {EscapedStartTime}, and {EscapedEndTime}.
        # 
        # - You must include {EscapedStartTime} and {EscapedEndTime}.
        self.mp_4 = mp_4
        # The name of the template.
        self.name = name
        # The OSS bucket.
        self.oss_bucket = oss_bucket
        # The domain name of the OSS bucket.
        self.oss_endpoint = oss_endpoint
        # The prefix of the OSS file.
        self.oss_file_prefix = oss_file_prefix
        self.owner_id = owner_id
        # The region where the Object Storage Service (OSS) bucket is located.
        self.region = region
        # The retention period for time shifting, in days.
        self.retention = retention
        # An array of transcoding configurations of the TransConfig type, in a JSON-formatted string.
        self.trans_configs_json = trans_configs_json
        # The trigger type of the template. The default value is auto. Valid values:
        # 
        # - auto (automatic)
        # 
        # - ondemand (on-demand)
        self.trigger = trigger

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

        if self.id is not None:
            result['Id'] = self.id

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

        if m.get('Id') is not None:
            self.id = m.get('Id')

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

        return self

