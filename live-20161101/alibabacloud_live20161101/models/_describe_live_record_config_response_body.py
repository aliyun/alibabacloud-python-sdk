# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeLiveRecordConfigResponseBody(DaraModel):
    def __init__(
        self,
        live_app_record_list: main_models.DescribeLiveRecordConfigResponseBodyLiveAppRecordList = None,
        order: str = None,
        page_num: int = None,
        page_size: int = None,
        request_id: str = None,
        total_num: int = None,
        total_page: int = None,
    ):
        # The list of recording configurations.
        self.live_app_record_list = live_app_record_list
        # The sorting order of recording configurations by creation time.
        self.order = order
        # The page number.
        self.page_num = page_num
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of recording configurations that meet the specified conditions.
        self.total_num = total_num
        # The total number of pages.
        self.total_page = total_page

    def validate(self):
        if self.live_app_record_list:
            self.live_app_record_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.live_app_record_list is not None:
            result['LiveAppRecordList'] = self.live_app_record_list.to_map()

        if self.order is not None:
            result['Order'] = self.order

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_num is not None:
            result['TotalNum'] = self.total_num

        if self.total_page is not None:
            result['TotalPage'] = self.total_page

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LiveAppRecordList') is not None:
            temp_model = main_models.DescribeLiveRecordConfigResponseBodyLiveAppRecordList()
            self.live_app_record_list = temp_model.from_map(m.get('LiveAppRecordList'))

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')

        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')

        return self

class DescribeLiveRecordConfigResponseBodyLiveAppRecordList(DaraModel):
    def __init__(
        self,
        live_app_record: List[main_models.DescribeLiveRecordConfigResponseBodyLiveAppRecordListLiveAppRecord] = None,
    ):
        self.live_app_record = live_app_record

    def validate(self):
        if self.live_app_record:
            for v1 in self.live_app_record:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LiveAppRecord'] = []
        if self.live_app_record is not None:
            for k1 in self.live_app_record:
                result['LiveAppRecord'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.live_app_record = []
        if m.get('LiveAppRecord') is not None:
            for k1 in m.get('LiveAppRecord'):
                temp_model = main_models.DescribeLiveRecordConfigResponseBodyLiveAppRecordListLiveAppRecord()
                self.live_app_record.append(temp_model.from_map(k1))

        return self

class DescribeLiveRecordConfigResponseBodyLiveAppRecordListLiveAppRecord(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        create_time: str = None,
        delay_time: int = None,
        domain_name: str = None,
        end_time: str = None,
        on_demond: int = None,
        oss_bucket: str = None,
        oss_endpoint: str = None,
        record_format_list: main_models.DescribeLiveRecordConfigResponseBodyLiveAppRecordListLiveAppRecordRecordFormatList = None,
        start_time: str = None,
        stream_name: str = None,
        transcode_record_format_list: main_models.DescribeLiveRecordConfigResponseBodyLiveAppRecordListLiveAppRecordTranscodeRecordFormatList = None,
        transcode_templates: main_models.DescribeLiveRecordConfigResponseBodyLiveAppRecordListLiveAppRecordTranscodeTemplates = None,
    ):
        # The name of the application to which the live stream belongs.
        self.app_name = app_name
        # The time when the recording configuration was created. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.create_time = create_time
        # The maximum interruption duration of the live stream. If the actual interruption duration exceeds the threshold, a new recording is generated. Valid values: 15 to 21600. Unit: seconds.
        self.delay_time = delay_time
        # The name of the main streaming domain.
        self.domain_name = domain_name
        # The end time of the recording. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.end_time = end_time
        # The configuration of on-demand recording. Valid values:
        # 
        # *   **0**: disables on-demand recording.
        # *   **1**: enables on-demand recording that is triggered by HTTP callbacks.
        # *   **2**: enables on-demand recording that is triggered by stream ingest parameters.
        # *   **7**: enables on-demand recording by calling the [RealTimeRecordCommand](https://help.aliyun.com/document_detail/85907.html) operation to manually start or stop recording.
        # 
        # >  If you set OnDemand to **1**, you must call the [AddLiveRecordNotifyConfig](https://help.aliyun.com/document_detail/51831.html) operation to configure OnDemandUrl. Otherwise, the configuration of on-demand recording is invalid.
        self.on_demond = on_demond
        # The name of the Object Storage Service (OSS) bucket in which the recordings are stored.
        self.oss_bucket = oss_bucket
        # The endpoint of the OSS bucket.
        self.oss_endpoint = oss_endpoint
        # The recording formats of original streams.
        self.record_format_list = record_format_list
        # The start time of the recording. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.start_time = start_time
        # The name of the live stream.
        self.stream_name = stream_name
        # The recording formats of transcoded streams.
        self.transcode_record_format_list = transcode_record_format_list
        # The transcoding templates.
        self.transcode_templates = transcode_templates

    def validate(self):
        if self.record_format_list:
            self.record_format_list.validate()
        if self.transcode_record_format_list:
            self.transcode_record_format_list.validate()
        if self.transcode_templates:
            self.transcode_templates.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.delay_time is not None:
            result['DelayTime'] = self.delay_time

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.on_demond is not None:
            result['OnDemond'] = self.on_demond

        if self.oss_bucket is not None:
            result['OssBucket'] = self.oss_bucket

        if self.oss_endpoint is not None:
            result['OssEndpoint'] = self.oss_endpoint

        if self.record_format_list is not None:
            result['RecordFormatList'] = self.record_format_list.to_map()

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.stream_name is not None:
            result['StreamName'] = self.stream_name

        if self.transcode_record_format_list is not None:
            result['TranscodeRecordFormatList'] = self.transcode_record_format_list.to_map()

        if self.transcode_templates is not None:
            result['TranscodeTemplates'] = self.transcode_templates.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DelayTime') is not None:
            self.delay_time = m.get('DelayTime')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('OnDemond') is not None:
            self.on_demond = m.get('OnDemond')

        if m.get('OssBucket') is not None:
            self.oss_bucket = m.get('OssBucket')

        if m.get('OssEndpoint') is not None:
            self.oss_endpoint = m.get('OssEndpoint')

        if m.get('RecordFormatList') is not None:
            temp_model = main_models.DescribeLiveRecordConfigResponseBodyLiveAppRecordListLiveAppRecordRecordFormatList()
            self.record_format_list = temp_model.from_map(m.get('RecordFormatList'))

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')

        if m.get('TranscodeRecordFormatList') is not None:
            temp_model = main_models.DescribeLiveRecordConfigResponseBodyLiveAppRecordListLiveAppRecordTranscodeRecordFormatList()
            self.transcode_record_format_list = temp_model.from_map(m.get('TranscodeRecordFormatList'))

        if m.get('TranscodeTemplates') is not None:
            temp_model = main_models.DescribeLiveRecordConfigResponseBodyLiveAppRecordListLiveAppRecordTranscodeTemplates()
            self.transcode_templates = temp_model.from_map(m.get('TranscodeTemplates'))

        return self

class DescribeLiveRecordConfigResponseBodyLiveAppRecordListLiveAppRecordTranscodeTemplates(DaraModel):
    def __init__(
        self,
        templates: List[str] = None,
    ):
        self.templates = templates

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.templates is not None:
            result['Templates'] = self.templates

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Templates') is not None:
            self.templates = m.get('Templates')

        return self

class DescribeLiveRecordConfigResponseBodyLiveAppRecordListLiveAppRecordTranscodeRecordFormatList(DaraModel):
    def __init__(
        self,
        record_format: List[main_models.DescribeLiveRecordConfigResponseBodyLiveAppRecordListLiveAppRecordTranscodeRecordFormatListRecordFormat] = None,
    ):
        self.record_format = record_format

    def validate(self):
        if self.record_format:
            for v1 in self.record_format:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RecordFormat'] = []
        if self.record_format is not None:
            for k1 in self.record_format:
                result['RecordFormat'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.record_format = []
        if m.get('RecordFormat') is not None:
            for k1 in m.get('RecordFormat'):
                temp_model = main_models.DescribeLiveRecordConfigResponseBodyLiveAppRecordListLiveAppRecordTranscodeRecordFormatListRecordFormat()
                self.record_format.append(temp_model.from_map(k1))

        return self

class DescribeLiveRecordConfigResponseBodyLiveAppRecordListLiveAppRecordTranscodeRecordFormatListRecordFormat(DaraModel):
    def __init__(
        self,
        cycle_duration: int = None,
        format: str = None,
        oss_object_prefix: str = None,
        slice_duration: int = None,
        slice_oss_object_prefix: str = None,
    ):
        # The duration of a recording file. Unit: seconds.
        self.cycle_duration = cycle_duration
        # The format of recording files.
        self.format = format
        # The naming format of a recording file.
        self.oss_object_prefix = oss_object_prefix
        # The duration of a segment file. Unit: seconds.
        self.slice_duration = slice_duration
        # The naming format of a segment file.
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

class DescribeLiveRecordConfigResponseBodyLiveAppRecordListLiveAppRecordRecordFormatList(DaraModel):
    def __init__(
        self,
        record_format: List[main_models.DescribeLiveRecordConfigResponseBodyLiveAppRecordListLiveAppRecordRecordFormatListRecordFormat] = None,
    ):
        self.record_format = record_format

    def validate(self):
        if self.record_format:
            for v1 in self.record_format:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RecordFormat'] = []
        if self.record_format is not None:
            for k1 in self.record_format:
                result['RecordFormat'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.record_format = []
        if m.get('RecordFormat') is not None:
            for k1 in m.get('RecordFormat'):
                temp_model = main_models.DescribeLiveRecordConfigResponseBodyLiveAppRecordListLiveAppRecordRecordFormatListRecordFormat()
                self.record_format.append(temp_model.from_map(k1))

        return self

class DescribeLiveRecordConfigResponseBodyLiveAppRecordListLiveAppRecordRecordFormatListRecordFormat(DaraModel):
    def __init__(
        self,
        cycle_duration: int = None,
        format: str = None,
        oss_object_prefix: str = None,
        slice_duration: int = None,
        slice_oss_object_prefix: str = None,
    ):
        # The duration of a recording file. Unit: seconds.
        self.cycle_duration = cycle_duration
        # The format of recording files.
        self.format = format
        # The naming format of a recording file.
        self.oss_object_prefix = oss_object_prefix
        # The duration of a segment file. Unit: seconds.
        self.slice_duration = slice_duration
        # The naming format of a segment file.
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

