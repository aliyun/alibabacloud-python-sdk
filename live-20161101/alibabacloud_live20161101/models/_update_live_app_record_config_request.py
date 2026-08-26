# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class UpdateLiveAppRecordConfigRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        delay_time: int = None,
        domain_name: str = None,
        end_time: str = None,
        on_demand: int = None,
        oss_endpoint: str = None,
        owner_id: int = None,
        record_format: List[main_models.UpdateLiveAppRecordConfigRequestRecordFormat] = None,
        security_token: str = None,
        start_time: str = None,
        stream_name: str = None,
        transcode_record_format: List[main_models.UpdateLiveAppRecordConfigRequestTranscodeRecordFormat] = None,
        transcode_templates: List[str] = None,
    ):
        # The AppName of the live stream.
        # 
        # This parameter is required.
        self.app_name = app_name
        # The window in seconds for merging fragmented recording after an interruption. If a stream disconnects and reconnects within this window, the recording will continue in the same file. Valid values: 15 to 21600.
        self.delay_time = delay_time
        # The main streaming domain.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # The recording end time. Format: *yyyy-MM-dd*T*HH:mm:ss*Z (UTC time).
        # 
        # > This parameter is only effective for stream-level recordings. The interval between EndTime and StartTime cannot exceed 7 days.
        self.end_time = end_time
        # Specifies the recording mode. Valid values:
        # 
        # - **0**: disables on-demand recording.
        # 
        # - **1**: On-demand recording via HTTP callback.
        # 
        # - **2**: On-demand recording by parsing parameters in the ingest URL.
        # 
        # - **7**: Manual recording. You can call the [RealTimeRecordCommand](https://help.aliyun.com/document_detail/2847882.html) API to manually start or stop recording.
        # 
        # > If you set OnDemand to **1**, you need to call the [AddLiveRecordNotifyConfig](https://help.aliyun.com/document_detail/2847891.html) API to configure the OnDemandUrl parameter. Otherwise, ApsaraVideo Live does not perform on-demand recording.
        self.on_demand = on_demand
        # The endpoint for OSS storage. You must create an OSS bucket before using this feature. See [Configure OSS](https://help.aliyun.com/document_detail/84932.html).
        # 
        # This parameter is required.
        self.oss_endpoint = oss_endpoint
        self.owner_id = owner_id
        # The recording details.
        self.record_format = record_format
        self.security_token = security_token
        # The recording start time. Format: *yyyy-MM-dd*T*HH:mm:ss*Z (UTC time).
        # 
        # > This parameter is only effective for stream-level recordings (i.e., when `StreamName` is specified). The time must be within 7 days of the actual stream start time.
        self.start_time = start_time
        # The name of the live stream.
        self.stream_name = stream_name
        # The transcoded stream recording configuration.
        self.transcode_record_format = transcode_record_format
        # The transcoding template group details.
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

        if m.get('OssEndpoint') is not None:
            self.oss_endpoint = m.get('OssEndpoint')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        self.record_format = []
        if m.get('RecordFormat') is not None:
            for k1 in m.get('RecordFormat'):
                temp_model = main_models.UpdateLiveAppRecordConfigRequestRecordFormat()
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
                temp_model = main_models.UpdateLiveAppRecordConfigRequestTranscodeRecordFormat()
                self.transcode_record_format.append(temp_model.from_map(k1))

        if m.get('TranscodeTemplates') is not None:
            self.transcode_templates = m.get('TranscodeTemplates')

        return self

class UpdateLiveAppRecordConfigRequestTranscodeRecordFormat(DaraModel):
    def __init__(
        self,
        cycle_duration: int = None,
        format: str = None,
        slice_duration: int = None,
    ):
        # The transcoded stream recording cycle. Unit: seconds. If you do not specify this parameter, the default value 6 hours is used.
        self.cycle_duration = cycle_duration
        # The format of the transcoded stream recording. Valid values:
        # 
        # > If you choose m3u8 or cmaf, you must specify the TranscodeRecordFormat.N.SliceOssObjectPrefix and TranscodeRecordFormat.N.SliceDuration parameters.
        # 
        # - m3u8
        # 
        # - flv
        # 
        # - mp4
        # 
        # - cmaf
        self.format = format
        # The duration of a single segment for transcoded stream recording. Unit: seconds.
        # 
        # > This parameter takes effect only if you set the TranscodeRecordFormat.N.Format parameter to m3u8 or cmaf.
        # 
        # If you do not specify this parameter, the default value 30 seconds is used. Valid values: 5 to 30.
        self.slice_duration = slice_duration

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

        if self.slice_duration is not None:
            result['SliceDuration'] = self.slice_duration

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CycleDuration') is not None:
            self.cycle_duration = m.get('CycleDuration')

        if m.get('Format') is not None:
            self.format = m.get('Format')

        if m.get('SliceDuration') is not None:
            self.slice_duration = m.get('SliceDuration')

        return self

class UpdateLiveAppRecordConfigRequestRecordFormat(DaraModel):
    def __init__(
        self,
        cycle_duration: int = None,
        format: str = None,
        slice_duration: int = None,
    ):
        # The duration of a single recording cycle in seconds. If not specified, the default value is 6 hours
        # 
        # > If a live stream is interrupted during a recording cycle but resumes normal streaming within the merge window, recording will continue in the same file. A recording file is generated only when a live stream is interrupted for longer than the merge window.
        self.cycle_duration = cycle_duration
        # The recording format. Valid values:
        # 
        # >Notice: 
        # 
        # If you choose m3u8 or cmaf, you must also set SliceOssObjectPrefix and SliceDuration. At least one of RecordFormat or TranscodeRecordFormat must be specified.
        # 
        # 
        # 
        # - m3u8
        # 
        # - flv
        # 
        # - mp4
        # 
        # - cmaf
        self.format = format
        # The duration of a single segment. Unit: seconds
        # 
        # > This parameter takes effect only if you set the RecordFormat.N.Format parameter to m3u8 or cmaf.
        # 
        # If you do not specify this parameter, the default value 30 seconds is used. Valid values: 5 to 30.
        self.slice_duration = slice_duration

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

        if self.slice_duration is not None:
            result['SliceDuration'] = self.slice_duration

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CycleDuration') is not None:
            self.cycle_duration = m.get('CycleDuration')

        if m.get('Format') is not None:
            self.format = m.get('Format')

        if m.get('SliceDuration') is not None:
            self.slice_duration = m.get('SliceDuration')

        return self

