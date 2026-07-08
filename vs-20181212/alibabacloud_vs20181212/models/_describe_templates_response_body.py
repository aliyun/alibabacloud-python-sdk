# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vs20181212 import models as main_models
from darabonba.model import DaraModel

class DescribeTemplatesResponseBody(DaraModel):
    def __init__(
        self,
        page_count: int = None,
        page_num: int = None,
        page_size: int = None,
        request_id: str = None,
        templates: List[main_models.DescribeTemplatesResponseBodyTemplates] = None,
        total_count: int = None,
    ):
        # Total number of pages.
        self.page_count = page_count
        # Page number.
        self.page_num = page_num
        # Number of entries per page.
        self.page_size = page_size
        # Request ID.
        self.request_id = request_id
        # Template list.
        self.templates = templates
        # Total number of templates.
        self.total_count = total_count

    def validate(self):
        if self.templates:
            for v1 in self.templates:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_count is not None:
            result['PageCount'] = self.page_count

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Templates'] = []
        if self.templates is not None:
            for k1 in self.templates:
                result['Templates'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.templates = []
        if m.get('Templates') is not None:
            for k1 in m.get('Templates'):
                temp_model = main_models.DescribeTemplatesResponseBodyTemplates()
                self.templates.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeTemplatesResponseBodyTemplates(DaraModel):
    def __init__(
        self,
        callback: str = None,
        created_time: str = None,
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
        region: str = None,
        retention: int = None,
        trans_configs: List[main_models.DescribeTemplatesResponseBodyTemplatesTransConfigs] = None,
        trigger: str = None,
        type: str = None,
    ):
        # Callback URL after template execution.
        self.callback = callback
        # Template creation time.
        self.created_time = created_time
        # Template description.
        self.description = description
        # Storage file format. Separate multiple values with commas. Valid values: mp4, flv, hls, jpg.
        self.file_format = file_format
        # FLV storage path.
        # 
        # > This applies only to recording templates.
        self.flv = flv
        # HLS storage path for M3U8 files.
        # 
        # > This applies only to recording templates.
        self.hls_m3u_8 = hls_m3u_8
        # HLS storage path for TS files.
        # 
        # > This applies only to recording templates.
        self.hls_ts = hls_ts
        # Template ID.
        self.id = id
        # Operation interval in seconds.
        self.interval = interval
        # JPG storage path for on-demand snapshots.
        # 
        # > This applies only to snapshot templates.
        self.jpg_on_demand = jpg_on_demand
        # JPG storage path for overwrite snapshots.
        # 
        # > This applies only to snapshot templates.
        self.jpg_overwrite = jpg_overwrite
        # JPG storage path for sequential snapshots.
        # 
        # > This applies only to snapshot templates.
        self.jpg_sequence = jpg_sequence
        # MP4 storage path.
        # 
        # > This applies only to recording templates.
        self.mp_4 = mp_4
        # Template name.
        self.name = name
        # The OSS bucket.
        self.oss_bucket = oss_bucket
        # OSS domain name.
        self.oss_endpoint = oss_endpoint
        # OSS file prefix.
        self.oss_file_prefix = oss_file_prefix
        # OSS region, also known as service center.
        self.region = region
        # Time-shifting retention period in days.
        # 
        # > This applies only to time-shifting templates.
        self.retention = retention
        # Transcoding configuration list.
        # 
        # > This applies only to transcoding templates.
        self.trans_configs = trans_configs
        # Template trigger type. Valid values:
        # 
        # - auto (automatic)
        # 
        # - ondemand (on demand)
        # 
        # > This applies only to recording templates.
        self.trigger = trigger
        # Template type. Valid values:
        # 
        # - record (recording)
        # 
        # - snapshot (snapshot)
        # 
        # - transcode (transcoding)
        # 
        # - timeshift (time shifting)
        self.type = type

    def validate(self):
        if self.trans_configs:
            for v1 in self.trans_configs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.callback is not None:
            result['Callback'] = self.callback

        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

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

        if self.region is not None:
            result['Region'] = self.region

        if self.retention is not None:
            result['Retention'] = self.retention

        result['TransConfigs'] = []
        if self.trans_configs is not None:
            for k1 in self.trans_configs:
                result['TransConfigs'].append(k1.to_map() if k1 else None)

        if self.trigger is not None:
            result['Trigger'] = self.trigger

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Callback') is not None:
            self.callback = m.get('Callback')

        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

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

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('Retention') is not None:
            self.retention = m.get('Retention')

        self.trans_configs = []
        if m.get('TransConfigs') is not None:
            for k1 in m.get('TransConfigs'):
                temp_model = main_models.DescribeTemplatesResponseBodyTemplatesTransConfigs()
                self.trans_configs.append(temp_model.from_map(k1))

        if m.get('Trigger') is not None:
            self.trigger = m.get('Trigger')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class DescribeTemplatesResponseBodyTemplatesTransConfigs(DaraModel):
    def __init__(
        self,
        fps: int = None,
        gop: int = None,
        height: int = None,
        name: str = None,
        video_bitrate: int = None,
        video_codec: str = None,
        width: int = None,
        id: str = None,
    ):
        # Video frame rate in fps.
        self.fps = fps
        # Video GOP in frames.
        self.gop = gop
        # Video height.
        self.height = height
        # Transcoding rule name. This name becomes the suffix of the transcoded stream. Use a descriptive suffix such as sd or 200k. Only letters and numbers are allowed.
        self.name = name
        # Video bitrate in kbps.
        self.video_bitrate = video_bitrate
        # Video encoding.
        self.video_codec = video_codec
        # Video width.
        self.width = width
        # Transcoding configuration ID.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fps is not None:
            result['Fps'] = self.fps

        if self.gop is not None:
            result['Gop'] = self.gop

        if self.height is not None:
            result['Height'] = self.height

        if self.name is not None:
            result['Name'] = self.name

        if self.video_bitrate is not None:
            result['VideoBitrate'] = self.video_bitrate

        if self.video_codec is not None:
            result['VideoCodec'] = self.video_codec

        if self.width is not None:
            result['Width'] = self.width

        if self.id is not None:
            result['id'] = self.id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Fps') is not None:
            self.fps = m.get('Fps')

        if m.get('Gop') is not None:
            self.gop = m.get('Gop')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('VideoBitrate') is not None:
            self.video_bitrate = m.get('VideoBitrate')

        if m.get('VideoCodec') is not None:
            self.video_codec = m.get('VideoCodec')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        if m.get('id') is not None:
            self.id = m.get('id')

        return self

