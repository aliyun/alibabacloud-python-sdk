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
        # The name of the application to which the live stream belongs. The value of this parameter must be the same as the application name in the ingest URL. Otherwise, the configuration does not take effect. If you want to match all applications, specify an asterisk (\\*) as the value.
        # 
        # This parameter is required.
        self.app_name = app_name
        # Duration for stream concatenation. If the live streaming interruption exceeds the set concatenation duration, a new file will be generated. The concatenation duration can be set between 15 to 21600 seconds.
        self.delay_time = delay_time
        # The main streaming domain.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # Recording end time. Format: <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z (UTC time).
        # > The difference between EndTime and StartTime should not exceed 7 days; if it does, it will be calculated as 7 days. This is only valid for stream-level recording (when StreamName is not empty).
        self.end_time = end_time
        # Specifies whether to enable on-demand recording. Valid values:
        # 
        # *   **0**: disables on-demand recording.
        # *   **1**: enables on-demand recording by using the HTTP callback method.
        # *   **2**: enables on-demand recording by parsing the stream ingest parameters.
        # *   **7**: By default, ApsaraVideo Live does not automatically record live streams. You can call the [RealTimeRecordCommand](https://help.aliyun.com/document_detail/2847882.html) operation to manually start or stop recording.
        # 
        # >  If you set the OnDemand parameter to **1**, you need to call the [AddLiveRecordNotifyConfig](https://help.aliyun.com/document_detail/2847891.html) operation to configure the OnDemandUrl parameter. Otherwise, ApsaraVideo Live does not perform on-demand recording.
        self.on_demand = on_demand
        # The name of the OSS bucket where live streaming recording files are stored. To store recorded files in OSS, you need to create an OSS bucket in advance. For creation method, please refer to [Configure OSS](https://help.aliyun.com/document_detail/84932.html).
        # 
        # This parameter is required.
        self.oss_bucket = oss_bucket
        # The endpoint of the OSS bucket. 
        # To store live stream recordings in OSS, you need to create an OSS bucket in advance. For more information, see Configure OSS.
        # 
        # This parameter is required.
        self.oss_endpoint = oss_endpoint
        self.owner_id = owner_id
        # The recording details.
        self.record_format = record_format
        self.security_token = security_token
        # Start time of the recording. Format: <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z (UTC time).
        # > The set time must be within 7 days of the actual streaming start time, and is only valid for stream-level recording (when StreamName is not empty).
        self.start_time = start_time
        # Stream broadcast name.
        self.stream_name = stream_name
        # The transcoded stream recording details.
        self.transcode_record_format = transcode_record_format
        # Transcoding stream recording template group.
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
        # The transcoded stream recording cycle. Unit: seconds. If you do not specify this parameter, the default value 6 hours is used.
        self.cycle_duration = cycle_duration
        # The transcoded stream recording format. Supported formats include M3U8, FLV, MP4, and CMAF. Valid values:
        # 
        # >  If you set this parameter to m3u8 or cmaf, you must also specify the TranscodeRecordFormat.N.SliceOssObjectPrefix and TranscodeRecordFormat.N.SliceDuration parameters.
        # 
        # *   m3u8
        # *   flv
        # *   mp4
        # *   cmaf
        self.format = format
        # The naming format of a transcoded stream recording to store in OSS.
        # 
        # *   The name must be less than 256 bytes in length and can contain the {AppName}, {StreamName}, {Sequence}, {StartTime}, {EndTime}, {EscapedStartTime}, and {EscapedEndTime} variables.
        # *   The name must contain the {StartTime} and {EndTime} variables or the {EscapedStartTime} and {EscapedEndTime} variables.
        self.oss_object_prefix = oss_object_prefix
        # The duration of a single segment in a transcoded stream recording. Unit: seconds.
        # 
        # >  This parameter takes effect only if you set the TranscodeRecordFormat.N.Format parameter to m3u8 or cmaf.
        # 
        # If you do not specify this parameter, the default value 30 seconds is used. Valid values: 5 to 30.
        self.slice_duration = slice_duration
        # The naming format of a segment in a transcoded stream recording.
        # 
        # >  This parameter is required only if you set the TranscodeRecordFormat.N.Format parameter to m3u8 or cmaf.
        # 
        # *   By default, the duration of a segment is 30 seconds. The segment name must be less than 256 bytes in length and can contain the {AppName}, {StreamName}, {UnixTimestamp}, and {Sequence} variables.
        # *   The segment name must contain the {UnixTimestamp} and {Sequence} variables.
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
        # The recording cycle. Unit: seconds. If you do not specify this parameter, the default value 6 hours is used.
        # 
        # > 
        # 
        # *   If a live stream is interrupted during a recording cycle but is resumed within the interruption duration threshold, the stream is recorded in the same recording before and after the interruption.
        # 
        # *   If a live stream is interrupted for longer than the interruption duration threshold, a new recording is generated.
        self.cycle_duration = cycle_duration
        # The recording format. Supported formats include M3U8, FLV, MP4, and CMAF. Valid values:
        # 
        # >  You need to specify at lease one of the RecordFormat and TranscodeRecordFormat parameters. If you set this parameter to m3u8 or cmaf, you must also specify the RecordFormat.N.SliceOssObjectPrefix and RecordFormat.N.SliceDuration parameters.
        # 
        # *   m3u8
        # *   flv
        # *   mp4
        # *   cmaf
        self.format = format
        # The naming format of a recording to store in OSS.
        # 
        # *   The name must be less than 256 bytes in length and can contain the {AppName}, {StreamName}, {Sequence}, {StartTime}, {EndTime}, {EscapedStartTime}, and {EscapedEndTime} variables.
        # *   The name must contain the {StartTime} and {EndTime} variables or the {EscapedStartTime} and {EscapedEndTime} variables.
        self.oss_object_prefix = oss_object_prefix
        # The duration of a single segment. Unit: seconds.
        # 
        # >  This parameter takes effect only if you set the RecordFormat.N.Format parameter to m3u8 or cmaf.
        # 
        # If you do not specify this parameter, the default value 30 seconds is used. Valid values: 5 to 30.
        self.slice_duration = slice_duration
        # The naming format of a segment.
        # 
        # >  This parameter is required only if you set the RecordFormat.N.Format parameter to m3u8 or cmaf.
        # 
        # *   By default, the duration of a segment is 30 seconds. The segment name must be less than 256 bytes in length and can contain the {AppName}, {StreamName}, {UnixTimestamp}, and {Sequence} variables.
        # *   The segment name must contain the {UnixTimestamp} and {Sequence} variables.
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

