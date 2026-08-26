# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class AddLiveAppRecordConfigRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        delay_time: int = None,
        domain_name: str = None,
        end_time: str = None,
        on_demand: int = None,
        oss_bucket: str = None,
        oss_endpoint: str = None,
        owner_id: int = None,
        record_format: List[main_models.AddLiveAppRecordConfigRequestRecordFormat] = None,
        security_token: str = None,
        start_time: str = None,
        stream_name: str = None,
        transcode_record_format: List[main_models.AddLiveAppRecordConfigRequestTranscodeRecordFormat] = None,
        transcode_templates: List[str] = None,
    ):
        # The name of the application to which the stream belongs. The template takes effect only when the AppName value matches the AppName in the ingest URL. To match all application names, set this parameter to an asterisk (*).
        # 
        # This parameter is required.
        self.app_name = app_name
        # The stream discontinuity merging duration. If the live stream is disconnected for longer than the specified merging duration, a new file is generated. Valid values: 15 to 21600. Unit: seconds.
        self.delay_time = delay_time
        # The streaming domain of the streamer.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # The recording end time. Format: <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z (UTC).
        # 
        # > The difference between EndTime and StartTime cannot exceed 7 days. If it exceeds 7 days, the value is calculated as 7 days. This parameter is valid only for stream-level recording (when StreamName is not empty).
        self.end_time = end_time
        # The on-demand or manual recording mode. Valid values:
        # 
        # - **0** (default): disabled. Automatic recording is used.
        # - **1**: on-demand recording through HTTP callback. You must first configure OnDemandUrl by calling the [AddLiveRecordNotifyConfig](https://help.aliyun.com/document_detail/2847891.html) operation. Otherwise, recording is not performed by default.
        # - **2**: on-demand recording by parsing stream ingest parameters.
        # - **7**: manual recording. Recording is not performed by default. You can call the [RealTimeRecordCommand](https://help.aliyun.com/document_detail/2847882.html) operation to manually start or stop recording.
        self.on_demand = on_demand
        # The name of the OSS bucket.
        # 
        # To store live recordings in OSS, create an OSS bucket in advance. For more information, see [Configure OSS](https://help.aliyun.com/document_detail/84932.html).
        # 
        # This parameter is required.
        self.oss_bucket = oss_bucket
        # The endpoint of the OSS bucket.
        # 
        # To store live recordings in OSS, create an OSS bucket in advance. For more information, see [Configure OSS](https://help.aliyun.com/document_detail/84932.html).
        # 
        # This parameter is required.
        self.oss_endpoint = oss_endpoint
        self.owner_id = owner_id
        # The recording details.
        self.record_format = record_format
        self.security_token = security_token
        # The recording start time. Format: <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z (UTC).
        # 
        # > The specified time must be within 7 days of the actual stream ingest start time. This parameter is valid only for stream-level recording (when StreamName is not empty).
        self.start_time = start_time
        # The stream name. The template takes effect only when the StreamName value matches the StreamName in the ingest URL. To match all stream names under the specified AppName, set this parameter to an asterisk (*).
        self.stream_name = stream_name
        # The transcoded stream recording details.
        self.transcode_record_format = transcode_record_format
        # The transcoding template group for transcoded stream recording.
        self.transcode_templates = transcode_templates

    def validate(self):
        if self.record_format:
            for v1 in self.record_format:
                 if v1:
                    v1.validate()
        if self.transcode_record_format:
            for v1 in self.transcode_record_format:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.delay_time is not None:
            result['DelayTime'] = self.delay_time

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.on_demand is not None:
            result['OnDemand'] = self.on_demand

        if self.oss_bucket is not None:
            result['OssBucket'] = self.oss_bucket

        if self.oss_endpoint is not None:
            result['OssEndpoint'] = self.oss_endpoint

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        result['RecordFormat'] = []
        if self.record_format is not None:
            for k1 in self.record_format:
                result['RecordFormat'].append(k1.to_map() if k1 else None)

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.stream_name is not None:
            result['StreamName'] = self.stream_name

        result['TranscodeRecordFormat'] = []
        if self.transcode_record_format is not None:
            for k1 in self.transcode_record_format:
                result['TranscodeRecordFormat'].append(k1.to_map() if k1 else None)

        if self.transcode_templates is not None:
            result['TranscodeTemplates'] = self.transcode_templates

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('DelayTime') is not None:
            self.delay_time = m.get('DelayTime')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('OnDemand') is not None:
            self.on_demand = m.get('OnDemand')

        if m.get('OssBucket') is not None:
            self.oss_bucket = m.get('OssBucket')

        if m.get('OssEndpoint') is not None:
            self.oss_endpoint = m.get('OssEndpoint')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        self.record_format = []
        if m.get('RecordFormat') is not None:
            for k1 in m.get('RecordFormat'):
                temp_model = main_models.AddLiveAppRecordConfigRequestRecordFormat()
                self.record_format.append(temp_model.from_map(k1))

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')

        self.transcode_record_format = []
        if m.get('TranscodeRecordFormat') is not None:
            for k1 in m.get('TranscodeRecordFormat'):
                temp_model = main_models.AddLiveAppRecordConfigRequestTranscodeRecordFormat()
                self.transcode_record_format.append(temp_model.from_map(k1))

        if m.get('TranscodeTemplates') is not None:
            self.transcode_templates = m.get('TranscodeTemplates')

        return self

class AddLiveAppRecordConfigRequestTranscodeRecordFormat(DaraModel):
    def __init__(
        self,
        cycle_duration: int = None,
        format: str = None,
        oss_object_prefix: str = None,
        slice_duration: int = None,
        slice_oss_object_prefix: str = None,
    ):
        # The recording length per epoch for transcoding stream recording. Unit: seconds.
        # > If this parameter is not specified, the default value varies by recording format: 6 hours for m3u8 and cmaf formats, and 1 hour for flv and mp4 formats.
        self.cycle_duration = cycle_duration
        # The transcoding stream recording format. M3U8, FLV, MP4, and CMAF are supported. Valid values:
        # >Notice: If you select m3u8 or cmaf, you must also set the request parameters TranscodeRecordFormat.N.SliceOssObjectPrefix and TranscodeRecordFormat.N.SliceDuration.
        # 
        # 
        # - m3u8.
        # - flv.
        # - mp4.
        # - cmaf.
        # 
        # > Settings: if you select m3u8 or cmaf format, the corresponding slice parameters must also be configured.
        self.format = format
        # The name of the transcoded stream recording file stored in OSS.
        # - The file name must be less than 256 bytes and supports variable matching, including {AppName}, {StreamName}, {Sequence}, {StartTime}, {EndTime}, {EscapedStartTime}, and {EscapedEndTime}.
        # - The value must contain {StartTime} or {EscapedStartTime} and {EndTime} or {EscapedEndTime}.
        self.oss_object_prefix = oss_object_prefix
        # The segment length of a single segment for transcoding stream recording. Unit: seconds.
        # 
        # >Notice: This parameter takes effect only when TranscodeRecordFormat.N.Format (transcoding stream recording format) is set to m3u8 or cmaf.
        # 
        # 
        # If this parameter is not specified, the default value is 30 seconds. Valid values: 5 to 30.
        self.slice_duration = slice_duration
        # The segment name for transcoded stream recording.
        # 
        # >Notice: This parameter is required only when TranscodeRecordFormat.N.Format is set to m3u8 or cmaf.
        # 
        # 
        # - The default segment length is 30 seconds. The value must be less than 256 bytes and supports variable matching, including {AppName}, {StreamName}, {UnixTimestamp}, and {Sequence}.
        # - The value must contain the {UnixTimestamp} and {Sequence} variables.
        self.slice_oss_object_prefix = slice_oss_object_prefix

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cycle_duration is not None:
            result['CycleDuration'] = self.cycle_duration

        if self.format is not None:
            result['Format'] = self.format

        if self.oss_object_prefix is not None:
            result['OssObjectPrefix'] = self.oss_object_prefix

        if self.slice_duration is not None:
            result['SliceDuration'] = self.slice_duration

        if self.slice_oss_object_prefix is not None:
            result['SliceOssObjectPrefix'] = self.slice_oss_object_prefix

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CycleDuration') is not None:
            self.cycle_duration = m.get('CycleDuration')

        if m.get('Format') is not None:
            self.format = m.get('Format')

        if m.get('OssObjectPrefix') is not None:
            self.oss_object_prefix = m.get('OssObjectPrefix')

        if m.get('SliceDuration') is not None:
            self.slice_duration = m.get('SliceDuration')

        if m.get('SliceOssObjectPrefix') is not None:
            self.slice_oss_object_prefix = m.get('SliceOssObjectPrefix')

        return self

class AddLiveAppRecordConfigRequestRecordFormat(DaraModel):
    def __init__(
        self,
        cycle_duration: int = None,
        format: str = None,
        oss_object_prefix: str = None,
        slice_duration: int = None,
        slice_oss_object_prefix: str = None,
    ):
        # The recording length per epoch. Unit: seconds.
        # 
        # > - If this parameter is not specified, the default value varies by recording format: 6 hours for m3u8 and cmaf formats, and 1 hour for flv and mp4 formats.
        # > - If a live stream is disconnected within a recording epoch but resumes stream ingest within the stream discontinuity merging duration, recording continues in the same file. This is Normal behavior.
        # > - A recording file is generated only after the live stream is disconnected for longer than the stream discontinuity merging duration.
        self.cycle_duration = cycle_duration
        # The format. M3U8, FLV, MP4, and CMAF are supported. Valid values:
        # 
        # >Notice: At least one of RecordFormat and TranscodeRecordFormat must be set. If you select m3u8 or cmaf, you must also set the request parameters RecordFormat.N.SliceOssObjectPrefix and RecordFormat.N.SliceDuration.
        # 
        # 
        # - m3u8.
        # - flv.
        # - mp4.
        # - cmaf.
        # 
        # > Settings for RecordFormat and TranscodeRecordFormat: at least one must be specified.
        self.format = format
        # The name of the recording file stored in OSS.
        # 
        # - The file name must be less than 256 bytes and supports variable matching, including {AppName}, {StreamName}, {Sequence}, {StartTime}, {EndTime}, {EscapedStartTime}, and {EscapedEndTime}.
        # - The value must contain {StartTime} or {EscapedStartTime} and {EndTime} or {EscapedEndTime}.
        self.oss_object_prefix = oss_object_prefix
        # The segment length of a single segment. Unit: seconds.
        # 
        # >Notice: This parameter takes effect only when RecordFormat.N.Format is set to m3u8 or cmaf.
        # 
        # 
        # If this parameter is not specified, the default value is 30 seconds. Valid values: 5 to 30.
        self.slice_duration = slice_duration
        # The segment name.
        # 
        # >Notice: This parameter is required only when RecordFormat.N.Format is set to m3u8 or cmaf.
        # 
        # 
        # - The default segment length is 30 seconds. The value must be less than 256 bytes and supports variable matching, including {AppName}, {StreamName}, {UnixTimestamp}, and {Sequence}.
        # - The value must contain the {UnixTimestamp} and {Sequence} variables.
        self.slice_oss_object_prefix = slice_oss_object_prefix

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cycle_duration is not None:
            result['CycleDuration'] = self.cycle_duration

        if self.format is not None:
            result['Format'] = self.format

        if self.oss_object_prefix is not None:
            result['OssObjectPrefix'] = self.oss_object_prefix

        if self.slice_duration is not None:
            result['SliceDuration'] = self.slice_duration

        if self.slice_oss_object_prefix is not None:
            result['SliceOssObjectPrefix'] = self.slice_oss_object_prefix

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CycleDuration') is not None:
            self.cycle_duration = m.get('CycleDuration')

        if m.get('Format') is not None:
            self.format = m.get('Format')

        if m.get('OssObjectPrefix') is not None:
            self.oss_object_prefix = m.get('OssObjectPrefix')

        if m.get('SliceDuration') is not None:
            self.slice_duration = m.get('SliceDuration')

        if m.get('SliceOssObjectPrefix') is not None:
            self.slice_oss_object_prefix = m.get('SliceOssObjectPrefix')

        return self

