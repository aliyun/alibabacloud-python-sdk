# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict


class AnalysisConfigTimeRange(TeaModel):
    def __init__(
        self,
        end: float = None,
        start: float = None,
    ):
        self.end = end
        self.start = start

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end is not None:
            result['end'] = self.end
        if self.start is not None:
            result['start'] = self.start
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('end') is not None:
            self.end = m.get('end')
        if m.get('start') is not None:
            self.start = m.get('start')
        return self


class AnalysisConfig(TeaModel):
    def __init__(
        self,
        bad_throughput_threshold: float = None,
        full_gcfrequent_interval_threshold: float = None,
        high_heap_usage_threshold: float = None,
        high_humongous_usage_threshold: float = None,
        high_metaspace_usage_threshold: float = None,
        high_old_usage_threshold: float = None,
        high_promotion_threshold: float = None,
        high_sys_threshold: float = None,
        long_concurrent_threshold: float = None,
        long_pause_threshold: float = None,
        low_usr_threshold: float = None,
        old_gcfrequent_interval_threshold: float = None,
        small_generation_threshold: float = None,
        time_range: AnalysisConfigTimeRange = None,
        too_many_old_gcthreshold: float = None,
        young_gcfrequent_interval_threshold: float = None,
    ):
        self.bad_throughput_threshold = bad_throughput_threshold
        self.full_gcfrequent_interval_threshold = full_gcfrequent_interval_threshold
        self.high_heap_usage_threshold = high_heap_usage_threshold
        self.high_humongous_usage_threshold = high_humongous_usage_threshold
        self.high_metaspace_usage_threshold = high_metaspace_usage_threshold
        self.high_old_usage_threshold = high_old_usage_threshold
        self.high_promotion_threshold = high_promotion_threshold
        self.high_sys_threshold = high_sys_threshold
        self.long_concurrent_threshold = long_concurrent_threshold
        self.long_pause_threshold = long_pause_threshold
        self.low_usr_threshold = low_usr_threshold
        self.old_gcfrequent_interval_threshold = old_gcfrequent_interval_threshold
        self.small_generation_threshold = small_generation_threshold
        self.time_range = time_range
        self.too_many_old_gcthreshold = too_many_old_gcthreshold
        self.young_gcfrequent_interval_threshold = young_gcfrequent_interval_threshold

    def validate(self):
        if self.time_range:
            self.time_range.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bad_throughput_threshold is not None:
            result['badThroughputThreshold'] = self.bad_throughput_threshold
        if self.full_gcfrequent_interval_threshold is not None:
            result['fullGCFrequentIntervalThreshold'] = self.full_gcfrequent_interval_threshold
        if self.high_heap_usage_threshold is not None:
            result['highHeapUsageThreshold'] = self.high_heap_usage_threshold
        if self.high_humongous_usage_threshold is not None:
            result['highHumongousUsageThreshold'] = self.high_humongous_usage_threshold
        if self.high_metaspace_usage_threshold is not None:
            result['highMetaspaceUsageThreshold'] = self.high_metaspace_usage_threshold
        if self.high_old_usage_threshold is not None:
            result['highOldUsageThreshold'] = self.high_old_usage_threshold
        if self.high_promotion_threshold is not None:
            result['highPromotionThreshold'] = self.high_promotion_threshold
        if self.high_sys_threshold is not None:
            result['highSysThreshold'] = self.high_sys_threshold
        if self.long_concurrent_threshold is not None:
            result['longConcurrentThreshold'] = self.long_concurrent_threshold
        if self.long_pause_threshold is not None:
            result['longPauseThreshold'] = self.long_pause_threshold
        if self.low_usr_threshold is not None:
            result['lowUsrThreshold'] = self.low_usr_threshold
        if self.old_gcfrequent_interval_threshold is not None:
            result['oldGCFrequentIntervalThreshold'] = self.old_gcfrequent_interval_threshold
        if self.small_generation_threshold is not None:
            result['smallGenerationThreshold'] = self.small_generation_threshold
        if self.time_range is not None:
            result['timeRange'] = self.time_range.to_map()
        if self.too_many_old_gcthreshold is not None:
            result['tooManyOldGCThreshold'] = self.too_many_old_gcthreshold
        if self.young_gcfrequent_interval_threshold is not None:
            result['youngGCFrequentIntervalThreshold'] = self.young_gcfrequent_interval_threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('badThroughputThreshold') is not None:
            self.bad_throughput_threshold = m.get('badThroughputThreshold')
        if m.get('fullGCFrequentIntervalThreshold') is not None:
            self.full_gcfrequent_interval_threshold = m.get('fullGCFrequentIntervalThreshold')
        if m.get('highHeapUsageThreshold') is not None:
            self.high_heap_usage_threshold = m.get('highHeapUsageThreshold')
        if m.get('highHumongousUsageThreshold') is not None:
            self.high_humongous_usage_threshold = m.get('highHumongousUsageThreshold')
        if m.get('highMetaspaceUsageThreshold') is not None:
            self.high_metaspace_usage_threshold = m.get('highMetaspaceUsageThreshold')
        if m.get('highOldUsageThreshold') is not None:
            self.high_old_usage_threshold = m.get('highOldUsageThreshold')
        if m.get('highPromotionThreshold') is not None:
            self.high_promotion_threshold = m.get('highPromotionThreshold')
        if m.get('highSysThreshold') is not None:
            self.high_sys_threshold = m.get('highSysThreshold')
        if m.get('longConcurrentThreshold') is not None:
            self.long_concurrent_threshold = m.get('longConcurrentThreshold')
        if m.get('longPauseThreshold') is not None:
            self.long_pause_threshold = m.get('longPauseThreshold')
        if m.get('lowUsrThreshold') is not None:
            self.low_usr_threshold = m.get('lowUsrThreshold')
        if m.get('oldGCFrequentIntervalThreshold') is not None:
            self.old_gcfrequent_interval_threshold = m.get('oldGCFrequentIntervalThreshold')
        if m.get('smallGenerationThreshold') is not None:
            self.small_generation_threshold = m.get('smallGenerationThreshold')
        if m.get('timeRange') is not None:
            temp_model = AnalysisConfigTimeRange()
            self.time_range = temp_model.from_map(m['timeRange'])
        if m.get('tooManyOldGCThreshold') is not None:
            self.too_many_old_gcthreshold = m.get('tooManyOldGCThreshold')
        if m.get('youngGCFrequentIntervalThreshold') is not None:
            self.young_gcfrequent_interval_threshold = m.get('youngGCFrequentIntervalThreshold')
        return self


class FileInfoAnalyzeProgress(TeaModel):
    def __init__(
        self,
        message: str = None,
        percent: float = None,
        state: str = None,
    ):
        self.message = message
        self.percent = percent
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['message'] = self.message
        if self.percent is not None:
            result['percent'] = self.percent
        if self.state is not None:
            result['state'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('percent') is not None:
            self.percent = m.get('percent')
        if m.get('state') is not None:
            self.state = m.get('state')
        return self


class FileInfoTransferProgress(TeaModel):
    def __init__(
        self,
        total_size: int = None,
        transferred_size: int = None,
    ):
        self.total_size = total_size
        self.transferred_size = transferred_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_size is not None:
            result['totalSize'] = self.total_size
        if self.transferred_size is not None:
            result['transferredSize'] = self.transferred_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('totalSize') is not None:
            self.total_size = m.get('totalSize')
        if m.get('transferredSize') is not None:
            self.transferred_size = m.get('transferredSize')
        return self


class FileInfo(TeaModel):
    def __init__(
        self,
        analyze_progress: FileInfoAnalyzeProgress = None,
        creation_time: int = None,
        display_name: str = None,
        labels: str = None,
        name: str = None,
        request_id: str = None,
        shared: bool = None,
        size: int = None,
        transfer_progress: FileInfoTransferProgress = None,
        transfer_state: str = None,
        type: str = None,
    ):
        self.analyze_progress = analyze_progress
        self.creation_time = creation_time
        self.display_name = display_name
        self.labels = labels
        self.name = name
        self.request_id = request_id
        self.shared = shared
        self.size = size
        self.transfer_progress = transfer_progress
        self.transfer_state = transfer_state
        self.type = type

    def validate(self):
        if self.analyze_progress:
            self.analyze_progress.validate()
        if self.transfer_progress:
            self.transfer_progress.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.analyze_progress is not None:
            result['analyzeProgress'] = self.analyze_progress.to_map()
        if self.creation_time is not None:
            result['creationTime'] = self.creation_time
        if self.display_name is not None:
            result['displayName'] = self.display_name
        if self.labels is not None:
            result['labels'] = self.labels
        if self.name is not None:
            result['name'] = self.name
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.shared is not None:
            result['shared'] = self.shared
        if self.size is not None:
            result['size'] = self.size
        if self.transfer_progress is not None:
            result['transferProgress'] = self.transfer_progress.to_map()
        if self.transfer_state is not None:
            result['transferState'] = self.transfer_state
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('analyzeProgress') is not None:
            temp_model = FileInfoAnalyzeProgress()
            self.analyze_progress = temp_model.from_map(m['analyzeProgress'])
        if m.get('creationTime') is not None:
            self.creation_time = m.get('creationTime')
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        if m.get('labels') is not None:
            self.labels = m.get('labels')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('shared') is not None:
            self.shared = m.get('shared')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('transferProgress') is not None:
            temp_model = FileInfoTransferProgress()
            self.transfer_progress = temp_model.from_map(m['transferProgress'])
        if m.get('transferState') is not None:
            self.transfer_state = m.get('transferState')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class PhaseStatisticItem(TeaModel):
    def __init__(
        self,
        count: int = None,
        duration_avg: float = None,
        duration_max: float = None,
        duration_total: float = None,
        interval_avg: float = None,
        interval_min: float = None,
        name: str = None,
    ):
        self.count = count
        self.duration_avg = duration_avg
        self.duration_max = duration_max
        self.duration_total = duration_total
        self.interval_avg = interval_avg
        self.interval_min = interval_min
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['count'] = self.count
        if self.duration_avg is not None:
            result['durationAvg'] = self.duration_avg
        if self.duration_max is not None:
            result['durationMax'] = self.duration_max
        if self.duration_total is not None:
            result['durationTotal'] = self.duration_total
        if self.interval_avg is not None:
            result['intervalAvg'] = self.interval_avg
        if self.interval_min is not None:
            result['intervalMin'] = self.interval_min
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('durationAvg') is not None:
            self.duration_avg = m.get('durationAvg')
        if m.get('durationMax') is not None:
            self.duration_max = m.get('durationMax')
        if m.get('durationTotal') is not None:
            self.duration_total = m.get('durationTotal')
        if m.get('intervalAvg') is not None:
            self.interval_avg = m.get('intervalAvg')
        if m.get('intervalMin') is not None:
            self.interval_min = m.get('intervalMin')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class AnalyzeFileRequest(TeaModel):
    def __init__(
        self,
        keep_unreachable_objects: bool = None,
        name: str = None,
        token: str = None,
    ):
        self.keep_unreachable_objects = keep_unreachable_objects
        self.name = name
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keep_unreachable_objects is not None:
            result['keepUnreachableObjects'] = self.keep_unreachable_objects
        if self.name is not None:
            result['name'] = self.name
        if self.token is not None:
            result['token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keepUnreachableObjects') is not None:
            self.keep_unreachable_objects = m.get('keepUnreachableObjects')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('token') is not None:
            self.token = m.get('token')
        return self


class AnalyzeFileResponseBody(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        request_id: str = None,
    ):
        self.file_name = file_name
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class AnalyzeFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AnalyzeFileResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AnalyzeFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFileRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        token: str = None,
    ):
        self.name = name
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.token is not None:
            result['token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('token') is not None:
            self.token = m.get('token')
        return self


class GetFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: FileInfo = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = FileInfo()
            self.body = temp_model.from_map(m['body'])
        return self


class UploadFileByOSSRequest(TeaModel):
    def __init__(
        self,
        bucket_name: str = None,
        display_name: str = None,
        endpoint: str = None,
        object_name: str = None,
        type: str = None,
    ):
        self.bucket_name = bucket_name
        self.display_name = display_name
        # oss endpoint
        self.endpoint = endpoint
        self.object_name = object_name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_name is not None:
            result['bucketName'] = self.bucket_name
        if self.display_name is not None:
            result['displayName'] = self.display_name
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint
        if self.object_name is not None:
            result['objectName'] = self.object_name
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bucketName') is not None:
            self.bucket_name = m.get('bucketName')
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')
        if m.get('objectName') is not None:
            self.object_name = m.get('objectName')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class UploadFileByOSSResponseBody(TeaModel):
    def __init__(
        self,
        name: str = None,
        request_id: str = None,
    ):
        self.name = name
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UploadFileByOSSResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UploadFileByOSSResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UploadFileByOSSResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UploadFileByURLRequest(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        type: str = None,
        url: str = None,
    ):
        self.display_name = display_name
        self.type = type
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['displayName'] = self.display_name
        if self.type is not None:
            result['type'] = self.type
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class UploadFileByURLResponseBody(TeaModel):
    def __init__(
        self,
        name: str = None,
        request_id: str = None,
    ):
        self.name = name
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UploadFileByURLResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UploadFileByURLResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UploadFileByURLResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


