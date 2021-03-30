# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class AttachDatasetResponseBodyResult(TeaModel):
    def __init__(
        self,
        version_id: str = None,
        state: str = None,
        gmt_modified: int = None,
        gmt_create: int = None,
        instance_id: str = None,
    ):
        self.version_id = version_id
        self.state = state
        self.gmt_modified = gmt_modified
        self.gmt_create = gmt_create
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.version_id is not None:
            result['versionId'] = self.version_id
        if self.state is not None:
            result['state'] = self.state
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('versionId') is not None:
            self.version_id = m.get('versionId')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        return self


class AttachDatasetResponseBody(TeaModel):
    def __init__(
        self,
        result: AttachDatasetResponseBodyResult = None,
        code: str = None,
        request_id: str = None,
        message: str = None,
    ):
        self.result = result
        self.code = code
        self.request_id = request_id
        self.message = message

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.code is not None:
            result['code'] = self.code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = AttachDatasetResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class AttachDatasetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AttachDatasetResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AttachDatasetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachIndexVersionResponseBody(TeaModel):
    def __init__(
        self,
        result: bool = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class AttachIndexVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AttachIndexVersionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AttachIndexVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckRankingModelReachableResponseBody(TeaModel):
    def __init__(
        self,
        result: bool = None,
        code: str = None,
        request_id: str = None,
        message: str = None,
    ):
        self.result = result
        self.code = code
        self.request_id = request_id
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result
        if self.code is not None:
            result['code'] = self.code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class CheckRankingModelReachableResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CheckRankingModelReachableResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CheckRankingModelReachableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CloneExperimentRequest(TeaModel):
    def __init__(
        self,
        dry_run: bool = None,
    ):
        self.dry_run = dry_run

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        return self


class CloneExperimentResponseBodyResultAlgorithmsConfig(TeaModel):
    def __init__(
        self,
        key: str = None,
        default_value: str = None,
        experiment_value: str = None,
        name: str = None,
    ):
        self.key = key
        self.default_value = default_value
        self.experiment_value = experiment_value
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.default_value is not None:
            result['defaultValue'] = self.default_value
        if self.experiment_value is not None:
            result['experimentValue'] = self.experiment_value
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('defaultValue') is not None:
            self.default_value = m.get('defaultValue')
        if m.get('experimentValue') is not None:
            self.experiment_value = m.get('experimentValue')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class CloneExperimentResponseBodyResultAlgorithms(TeaModel):
    def __init__(
        self,
        key: str = None,
        config: List[CloneExperimentResponseBodyResultAlgorithmsConfig] = None,
        default_value: str = None,
        type: str = None,
        experiment_value: str = None,
        has_config: bool = None,
        category: str = None,
        name: str = None,
    ):
        self.key = key
        self.config = config
        self.default_value = default_value
        self.type = type
        self.experiment_value = experiment_value
        self.has_config = has_config
        self.category = category
        self.name = name

    def validate(self):
        if self.config:
            for k in self.config:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        result['config'] = []
        if self.config is not None:
            for k in self.config:
                result['config'].append(k.to_map() if k else None)
        if self.default_value is not None:
            result['defaultValue'] = self.default_value
        if self.type is not None:
            result['type'] = self.type
        if self.experiment_value is not None:
            result['experimentValue'] = self.experiment_value
        if self.has_config is not None:
            result['hasConfig'] = self.has_config
        if self.category is not None:
            result['category'] = self.category
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        self.config = []
        if m.get('config') is not None:
            for k in m.get('config'):
                temp_model = CloneExperimentResponseBodyResultAlgorithmsConfig()
                self.config.append(temp_model.from_map(k))
        if m.get('defaultValue') is not None:
            self.default_value = m.get('defaultValue')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('experimentValue') is not None:
            self.experiment_value = m.get('experimentValue')
        if m.get('hasConfig') is not None:
            self.has_config = m.get('hasConfig')
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class CloneExperimentResponseBodyResult(TeaModel):
    def __init__(
        self,
        base: bool = None,
        online_time: str = None,
        offline_time: str = None,
        description: str = None,
        status: str = None,
        name: str = None,
        algorithms: List[CloneExperimentResponseBodyResultAlgorithms] = None,
        buckets: List[str] = None,
        experiment_id: str = None,
    ):
        self.base = base
        self.online_time = online_time
        self.offline_time = offline_time
        self.description = description
        self.status = status
        self.name = name
        self.algorithms = algorithms
        self.buckets = buckets
        self.experiment_id = experiment_id

    def validate(self):
        if self.algorithms:
            for k in self.algorithms:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base is not None:
            result['base'] = self.base
        if self.online_time is not None:
            result['onlineTime'] = self.online_time
        if self.offline_time is not None:
            result['offlineTime'] = self.offline_time
        if self.description is not None:
            result['description'] = self.description
        if self.status is not None:
            result['status'] = self.status
        if self.name is not None:
            result['name'] = self.name
        result['algorithms'] = []
        if self.algorithms is not None:
            for k in self.algorithms:
                result['algorithms'].append(k.to_map() if k else None)
        if self.buckets is not None:
            result['buckets'] = self.buckets
        if self.experiment_id is not None:
            result['experimentId'] = self.experiment_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('base') is not None:
            self.base = m.get('base')
        if m.get('onlineTime') is not None:
            self.online_time = m.get('onlineTime')
        if m.get('offlineTime') is not None:
            self.offline_time = m.get('offlineTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('name') is not None:
            self.name = m.get('name')
        self.algorithms = []
        if m.get('algorithms') is not None:
            for k in m.get('algorithms'):
                temp_model = CloneExperimentResponseBodyResultAlgorithms()
                self.algorithms.append(temp_model.from_map(k))
        if m.get('buckets') is not None:
            self.buckets = m.get('buckets')
        if m.get('experimentId') is not None:
            self.experiment_id = m.get('experimentId')
        return self


class CloneExperimentResponseBody(TeaModel):
    def __init__(
        self,
        result: CloneExperimentResponseBodyResult = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = CloneExperimentResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CloneExperimentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CloneExperimentResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CloneExperimentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFilteringAlgorithmRequest(TeaModel):
    def __init__(
        self,
        dry_run: str = None,
    ):
        self.dry_run = dry_run

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        return self


class CreateFilteringAlgorithmResponseBodyResultMetaThreshold(TeaModel):
    def __init__(
        self,
        source_data_size_threshold: int = None,
        source_data_record_threshold: int = None,
        index_size_threshold: int = None,
        index_loss_threshold: int = None,
    ):
        self.source_data_size_threshold = source_data_size_threshold
        self.source_data_record_threshold = source_data_record_threshold
        self.index_size_threshold = index_size_threshold
        self.index_loss_threshold = index_loss_threshold

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_data_size_threshold is not None:
            result['sourceDataSizeThreshold'] = self.source_data_size_threshold
        if self.source_data_record_threshold is not None:
            result['sourceDataRecordThreshold'] = self.source_data_record_threshold
        if self.index_size_threshold is not None:
            result['indexSizeThreshold'] = self.index_size_threshold
        if self.index_loss_threshold is not None:
            result['indexLossThreshold'] = self.index_loss_threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sourceDataSizeThreshold') is not None:
            self.source_data_size_threshold = m.get('sourceDataSizeThreshold')
        if m.get('sourceDataRecordThreshold') is not None:
            self.source_data_record_threshold = m.get('sourceDataRecordThreshold')
        if m.get('indexSizeThreshold') is not None:
            self.index_size_threshold = m.get('indexSizeThreshold')
        if m.get('indexLossThreshold') is not None:
            self.index_loss_threshold = m.get('indexLossThreshold')
        return self


class CreateFilteringAlgorithmResponseBodyResultMeta(TeaModel):
    def __init__(
        self,
        type: str = None,
        ext_info: Dict[str, Any] = None,
        category: str = None,
        threshold: CreateFilteringAlgorithmResponseBodyResultMetaThreshold = None,
        status: str = None,
        gmt_create: str = None,
        table_name: str = None,
        cron: str = None,
        description: str = None,
        gmt_modified: str = None,
        project_name: str = None,
        algorithm_name: str = None,
        cron_enabled: bool = None,
    ):
        self.type = type
        self.ext_info = ext_info
        self.category = category
        self.threshold = threshold
        self.status = status
        self.gmt_create = gmt_create
        self.table_name = table_name
        self.cron = cron
        self.description = description
        self.gmt_modified = gmt_modified
        self.project_name = project_name
        self.algorithm_name = algorithm_name
        self.cron_enabled = cron_enabled

    def validate(self):
        if self.threshold:
            self.threshold.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        if self.ext_info is not None:
            result['extInfo'] = self.ext_info
        if self.category is not None:
            result['category'] = self.category
        if self.threshold is not None:
            result['threshold'] = self.threshold.to_map()
        if self.status is not None:
            result['status'] = self.status
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.table_name is not None:
            result['tableName'] = self.table_name
        if self.cron is not None:
            result['cron'] = self.cron
        if self.description is not None:
            result['description'] = self.description
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.project_name is not None:
            result['projectName'] = self.project_name
        if self.algorithm_name is not None:
            result['algorithmName'] = self.algorithm_name
        if self.cron_enabled is not None:
            result['cronEnabled'] = self.cron_enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('extInfo') is not None:
            self.ext_info = m.get('extInfo')
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('threshold') is not None:
            temp_model = CreateFilteringAlgorithmResponseBodyResultMetaThreshold()
            self.threshold = temp_model.from_map(m['threshold'])
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('tableName') is not None:
            self.table_name = m.get('tableName')
        if m.get('cron') is not None:
            self.cron = m.get('cron')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')
        if m.get('algorithmName') is not None:
            self.algorithm_name = m.get('algorithmName')
        if m.get('cronEnabled') is not None:
            self.cron_enabled = m.get('cronEnabled')
        return self


class CreateFilteringAlgorithmResponseBodyResult(TeaModel):
    def __init__(
        self,
        gmt_modified: str = None,
        status: str = None,
        gmt_create: str = None,
        algorithm_id: str = None,
        meta: CreateFilteringAlgorithmResponseBodyResultMeta = None,
    ):
        self.gmt_modified = gmt_modified
        self.status = status
        self.gmt_create = gmt_create
        self.algorithm_id = algorithm_id
        self.meta = meta

    def validate(self):
        if self.meta:
            self.meta.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.status is not None:
            result['status'] = self.status
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.algorithm_id is not None:
            result['algorithmId'] = self.algorithm_id
        if self.meta is not None:
            result['meta'] = self.meta.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('algorithmId') is not None:
            self.algorithm_id = m.get('algorithmId')
        if m.get('meta') is not None:
            temp_model = CreateFilteringAlgorithmResponseBodyResultMeta()
            self.meta = temp_model.from_map(m['meta'])
        return self


class CreateFilteringAlgorithmResponseBody(TeaModel):
    def __init__(
        self,
        result: CreateFilteringAlgorithmResponseBodyResult = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = CreateFilteringAlgorithmResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateFilteringAlgorithmResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateFilteringAlgorithmResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateFilteringAlgorithmResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateInstanceResponseBodyResult(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        return self


class CreateInstanceResponseBody(TeaModel):
    def __init__(
        self,
        result: CreateInstanceResponseBodyResult = None,
        code: str = None,
        request_id: str = None,
        message: str = None,
    ):
        self.result = result
        self.code = code
        self.request_id = request_id
        self.message = message

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.code is not None:
            result['code'] = self.code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = CreateInstanceResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class CreateInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRankingModelRequest(TeaModel):
    def __init__(
        self,
        dry_run: bool = None,
    ):
        self.dry_run = dry_run

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        return self


class CreateRankingModelResponseBodyResult(TeaModel):
    def __init__(
        self,
        ranking_model_id: str = None,
        gmt_modified: str = None,
        gmt_create: str = None,
        meta: Dict[str, Any] = None,
    ):
        self.ranking_model_id = ranking_model_id
        self.gmt_modified = gmt_modified
        self.gmt_create = gmt_create
        self.meta = meta

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ranking_model_id is not None:
            result['rankingModelId'] = self.ranking_model_id
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.meta is not None:
            result['meta'] = self.meta
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('rankingModelId') is not None:
            self.ranking_model_id = m.get('rankingModelId')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('meta') is not None:
            self.meta = m.get('meta')
        return self


class CreateRankingModelResponseBody(TeaModel):
    def __init__(
        self,
        result: CreateRankingModelResponseBodyResult = None,
        code: str = None,
        request_id: str = None,
        message: str = None,
    ):
        self.result = result
        self.code = code
        self.request_id = request_id
        self.message = message

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.code is not None:
            result['code'] = self.code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = CreateRankingModelResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class CreateRankingModelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateRankingModelResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateRankingModelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRuleResponseBodyResult(TeaModel):
    def __init__(
        self,
        rule_id: str = None,
        gmt_modified: str = None,
        status: str = None,
        gmt_create: str = None,
    ):
        self.rule_id = rule_id
        self.gmt_modified = gmt_modified
        self.status = status
        self.gmt_create = gmt_create

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_id is not None:
            result['ruleId'] = self.rule_id
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.status is not None:
            result['status'] = self.status
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ruleId') is not None:
            self.rule_id = m.get('ruleId')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        return self


class CreateRuleResponseBody(TeaModel):
    def __init__(
        self,
        result: CreateRuleResponseBodyResult = None,
        code: str = None,
        request_id: str = None,
        message: str = None,
    ):
        self.result = result
        self.code = code
        self.request_id = request_id
        self.message = message

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.code is not None:
            result['code'] = self.code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = CreateRuleResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class CreateRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateRuleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSceneRequest(TeaModel):
    def __init__(
        self,
        dry_run: bool = None,
    ):
        self.dry_run = dry_run

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        return self


class CreateSceneResponseBodyResult(TeaModel):
    def __init__(
        self,
        scene_id: str = None,
        gmt_modified: str = None,
        status: str = None,
        gmt_create: str = None,
    ):
        self.scene_id = scene_id
        self.gmt_modified = gmt_modified
        self.status = status
        self.gmt_create = gmt_create

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene_id is not None:
            result['sceneId'] = self.scene_id
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.status is not None:
            result['status'] = self.status
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sceneId') is not None:
            self.scene_id = m.get('sceneId')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        return self


class CreateSceneResponseBody(TeaModel):
    def __init__(
        self,
        result: CreateSceneResponseBodyResult = None,
        code: str = None,
        request_id: str = None,
        message: str = None,
    ):
        self.result = result
        self.code = code
        self.request_id = request_id
        self.message = message

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.code is not None:
            result['code'] = self.code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = CreateSceneResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class CreateSceneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateSceneResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DecribeRankingModelResponseBodyResult(TeaModel):
    def __init__(
        self,
        ranking_model_id: str = None,
        gmt_modified: str = None,
        gmt_create: str = None,
        meta: Dict[str, Any] = None,
    ):
        self.ranking_model_id = ranking_model_id
        self.gmt_modified = gmt_modified
        self.gmt_create = gmt_create
        self.meta = meta

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ranking_model_id is not None:
            result['rankingModelId'] = self.ranking_model_id
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.meta is not None:
            result['meta'] = self.meta
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('rankingModelId') is not None:
            self.ranking_model_id = m.get('rankingModelId')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('meta') is not None:
            self.meta = m.get('meta')
        return self


class DecribeRankingModelResponseBody(TeaModel):
    def __init__(
        self,
        result: DecribeRankingModelResponseBodyResult = None,
        code: str = None,
        request_id: str = None,
        message: str = None,
    ):
        self.result = result
        self.code = code
        self.request_id = request_id
        self.message = message

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.code is not None:
            result['code'] = self.code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = DecribeRankingModelResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class DecribeRankingModelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DecribeRankingModelResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DecribeRankingModelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDataSetResponseBodyResult(TeaModel):
    def __init__(
        self,
        version_id: str = None,
        state: str = None,
        gmt_modified: int = None,
        gmt_create: int = None,
        instance_id: str = None,
    ):
        self.version_id = version_id
        self.state = state
        self.gmt_modified = gmt_modified
        self.gmt_create = gmt_create
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.version_id is not None:
            result['versionId'] = self.version_id
        if self.state is not None:
            result['state'] = self.state
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('versionId') is not None:
            self.version_id = m.get('versionId')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        return self


class DeleteDataSetResponseBody(TeaModel):
    def __init__(
        self,
        result: DeleteDataSetResponseBodyResult = None,
        code: str = None,
        request_id: str = None,
        message: str = None,
    ):
        self.result = result
        self.code = code
        self.request_id = request_id
        self.message = message

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.code is not None:
            result['code'] = self.code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = DeleteDataSetResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class DeleteDataSetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteDataSetResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteDataSetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteExperimentResponseBody(TeaModel):
    def __init__(
        self,
        result: bool = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteExperimentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteExperimentResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteExperimentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFilteringAlgorithmResponseBodyResultMetaExtInfo(TeaModel):
    def __init__(
        self,
        kv_separator: str = None,
        item_separator: str = None,
    ):
        self.kv_separator = kv_separator
        self.item_separator = item_separator

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.kv_separator is not None:
            result['kvSeparator'] = self.kv_separator
        if self.item_separator is not None:
            result['itemSeparator'] = self.item_separator
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('kvSeparator') is not None:
            self.kv_separator = m.get('kvSeparator')
        if m.get('itemSeparator') is not None:
            self.item_separator = m.get('itemSeparator')
        return self


class DeleteFilteringAlgorithmResponseBodyResultMetaThreshold(TeaModel):
    def __init__(
        self,
        source_data_size_threshold: int = None,
        source_data_record_threshold: int = None,
        index_size_threshold: int = None,
        index_loss_threshold: int = None,
    ):
        self.source_data_size_threshold = source_data_size_threshold
        self.source_data_record_threshold = source_data_record_threshold
        self.index_size_threshold = index_size_threshold
        self.index_loss_threshold = index_loss_threshold

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_data_size_threshold is not None:
            result['sourceDataSizeThreshold'] = self.source_data_size_threshold
        if self.source_data_record_threshold is not None:
            result['sourceDataRecordThreshold'] = self.source_data_record_threshold
        if self.index_size_threshold is not None:
            result['indexSizeThreshold'] = self.index_size_threshold
        if self.index_loss_threshold is not None:
            result['indexLossThreshold'] = self.index_loss_threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sourceDataSizeThreshold') is not None:
            self.source_data_size_threshold = m.get('sourceDataSizeThreshold')
        if m.get('sourceDataRecordThreshold') is not None:
            self.source_data_record_threshold = m.get('sourceDataRecordThreshold')
        if m.get('indexSizeThreshold') is not None:
            self.index_size_threshold = m.get('indexSizeThreshold')
        if m.get('indexLossThreshold') is not None:
            self.index_loss_threshold = m.get('indexLossThreshold')
        return self


class DeleteFilteringAlgorithmResponseBodyResultMeta(TeaModel):
    def __init__(
        self,
        task_id: str = None,
        meta_type: str = None,
        type: str = None,
        ext_info: DeleteFilteringAlgorithmResponseBodyResultMetaExtInfo = None,
        category: str = None,
        threshold: DeleteFilteringAlgorithmResponseBodyResultMetaThreshold = None,
        table_name: str = None,
        cluster_id: str = None,
        cron: str = None,
        description: str = None,
        project_name: str = None,
        algorithm_name: str = None,
        cron_enabled: bool = None,
    ):
        self.task_id = task_id
        self.meta_type = meta_type
        self.type = type
        self.ext_info = ext_info
        self.category = category
        self.threshold = threshold
        self.table_name = table_name
        self.cluster_id = cluster_id
        self.cron = cron
        self.description = description
        self.project_name = project_name
        self.algorithm_name = algorithm_name
        self.cron_enabled = cron_enabled

    def validate(self):
        if self.ext_info:
            self.ext_info.validate()
        if self.threshold:
            self.threshold.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['taskId'] = self.task_id
        if self.meta_type is not None:
            result['metaType'] = self.meta_type
        if self.type is not None:
            result['type'] = self.type
        if self.ext_info is not None:
            result['extInfo'] = self.ext_info.to_map()
        if self.category is not None:
            result['category'] = self.category
        if self.threshold is not None:
            result['threshold'] = self.threshold.to_map()
        if self.table_name is not None:
            result['tableName'] = self.table_name
        if self.cluster_id is not None:
            result['clusterId'] = self.cluster_id
        if self.cron is not None:
            result['cron'] = self.cron
        if self.description is not None:
            result['description'] = self.description
        if self.project_name is not None:
            result['projectName'] = self.project_name
        if self.algorithm_name is not None:
            result['algorithmName'] = self.algorithm_name
        if self.cron_enabled is not None:
            result['cronEnabled'] = self.cron_enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        if m.get('metaType') is not None:
            self.meta_type = m.get('metaType')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('extInfo') is not None:
            temp_model = DeleteFilteringAlgorithmResponseBodyResultMetaExtInfo()
            self.ext_info = temp_model.from_map(m['extInfo'])
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('threshold') is not None:
            temp_model = DeleteFilteringAlgorithmResponseBodyResultMetaThreshold()
            self.threshold = temp_model.from_map(m['threshold'])
        if m.get('tableName') is not None:
            self.table_name = m.get('tableName')
        if m.get('clusterId') is not None:
            self.cluster_id = m.get('clusterId')
        if m.get('cron') is not None:
            self.cron = m.get('cron')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')
        if m.get('algorithmName') is not None:
            self.algorithm_name = m.get('algorithmName')
        if m.get('cronEnabled') is not None:
            self.cron_enabled = m.get('cronEnabled')
        return self


class DeleteFilteringAlgorithmResponseBodyResult(TeaModel):
    def __init__(
        self,
        gmt_modified: str = None,
        status: str = None,
        gmt_create: str = None,
        algorithm_id: str = None,
        meta: DeleteFilteringAlgorithmResponseBodyResultMeta = None,
    ):
        self.gmt_modified = gmt_modified
        self.status = status
        self.gmt_create = gmt_create
        self.algorithm_id = algorithm_id
        self.meta = meta

    def validate(self):
        if self.meta:
            self.meta.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.status is not None:
            result['status'] = self.status
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.algorithm_id is not None:
            result['algorithmId'] = self.algorithm_id
        if self.meta is not None:
            result['meta'] = self.meta.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('algorithmId') is not None:
            self.algorithm_id = m.get('algorithmId')
        if m.get('meta') is not None:
            temp_model = DeleteFilteringAlgorithmResponseBodyResultMeta()
            self.meta = temp_model.from_map(m['meta'])
        return self


class DeleteFilteringAlgorithmResponseBody(TeaModel):
    def __init__(
        self,
        result: DeleteFilteringAlgorithmResponseBodyResult = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = DeleteFilteringAlgorithmResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteFilteringAlgorithmResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteFilteringAlgorithmResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteFilteringAlgorithmResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRankingModelResponseBodyResult(TeaModel):
    def __init__(
        self,
        ranking_model_id: str = None,
        meta: Dict[str, Any] = None,
    ):
        self.ranking_model_id = ranking_model_id
        self.meta = meta

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ranking_model_id is not None:
            result['rankingModelId'] = self.ranking_model_id
        if self.meta is not None:
            result['meta'] = self.meta
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('rankingModelId') is not None:
            self.ranking_model_id = m.get('rankingModelId')
        if m.get('meta') is not None:
            self.meta = m.get('meta')
        return self


class DeleteRankingModelResponseBody(TeaModel):
    def __init__(
        self,
        result: DeleteRankingModelResponseBodyResult = None,
        code: str = None,
        request_id: str = None,
        message: str = None,
    ):
        self.result = result
        self.code = code
        self.request_id = request_id
        self.message = message

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.code is not None:
            result['code'] = self.code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = DeleteRankingModelResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class DeleteRankingModelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteRankingModelResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteRankingModelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSceneResponseBodyResult(TeaModel):
    def __init__(
        self,
        scene_id: str = None,
    ):
        self.scene_id = scene_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene_id is not None:
            result['sceneId'] = self.scene_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sceneId') is not None:
            self.scene_id = m.get('sceneId')
        return self


class DeleteSceneResponseBody(TeaModel):
    def __init__(
        self,
        result: DeleteSceneResponseBodyResult = None,
        code: str = None,
        request_id: str = None,
        message: str = None,
    ):
        self.result = result
        self.code = code
        self.request_id = request_id
        self.message = message

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.code is not None:
            result['code'] = self.code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = DeleteSceneResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class DeleteSceneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteSceneResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBaseExperimentResponseBodyResultAlgorithmsConfig(TeaModel):
    def __init__(
        self,
        key: str = None,
        default_value: str = None,
        experiment_value: str = None,
        name: str = None,
    ):
        self.key = key
        self.default_value = default_value
        self.experiment_value = experiment_value
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.default_value is not None:
            result['defaultValue'] = self.default_value
        if self.experiment_value is not None:
            result['experimentValue'] = self.experiment_value
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('defaultValue') is not None:
            self.default_value = m.get('defaultValue')
        if m.get('experimentValue') is not None:
            self.experiment_value = m.get('experimentValue')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class DescribeBaseExperimentResponseBodyResultAlgorithms(TeaModel):
    def __init__(
        self,
        key: str = None,
        config: List[DescribeBaseExperimentResponseBodyResultAlgorithmsConfig] = None,
        default_value: str = None,
        type: str = None,
        experiment_value: str = None,
        has_config: bool = None,
        category: str = None,
        name: str = None,
    ):
        self.key = key
        self.config = config
        self.default_value = default_value
        self.type = type
        self.experiment_value = experiment_value
        self.has_config = has_config
        self.category = category
        self.name = name

    def validate(self):
        if self.config:
            for k in self.config:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        result['config'] = []
        if self.config is not None:
            for k in self.config:
                result['config'].append(k.to_map() if k else None)
        if self.default_value is not None:
            result['defaultValue'] = self.default_value
        if self.type is not None:
            result['type'] = self.type
        if self.experiment_value is not None:
            result['experimentValue'] = self.experiment_value
        if self.has_config is not None:
            result['hasConfig'] = self.has_config
        if self.category is not None:
            result['category'] = self.category
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        self.config = []
        if m.get('config') is not None:
            for k in m.get('config'):
                temp_model = DescribeBaseExperimentResponseBodyResultAlgorithmsConfig()
                self.config.append(temp_model.from_map(k))
        if m.get('defaultValue') is not None:
            self.default_value = m.get('defaultValue')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('experimentValue') is not None:
            self.experiment_value = m.get('experimentValue')
        if m.get('hasConfig') is not None:
            self.has_config = m.get('hasConfig')
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class DescribeBaseExperimentResponseBodyResult(TeaModel):
    def __init__(
        self,
        base: bool = None,
        online_time: str = None,
        offline_time: str = None,
        description: str = None,
        status: str = None,
        name: str = None,
        algorithms: List[DescribeBaseExperimentResponseBodyResultAlgorithms] = None,
        buckets: List[str] = None,
        experiment_id: str = None,
    ):
        self.base = base
        self.online_time = online_time
        self.offline_time = offline_time
        self.description = description
        self.status = status
        self.name = name
        self.algorithms = algorithms
        self.buckets = buckets
        self.experiment_id = experiment_id

    def validate(self):
        if self.algorithms:
            for k in self.algorithms:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base is not None:
            result['base'] = self.base
        if self.online_time is not None:
            result['onlineTime'] = self.online_time
        if self.offline_time is not None:
            result['offlineTime'] = self.offline_time
        if self.description is not None:
            result['description'] = self.description
        if self.status is not None:
            result['status'] = self.status
        if self.name is not None:
            result['name'] = self.name
        result['algorithms'] = []
        if self.algorithms is not None:
            for k in self.algorithms:
                result['algorithms'].append(k.to_map() if k else None)
        if self.buckets is not None:
            result['buckets'] = self.buckets
        if self.experiment_id is not None:
            result['experimentId'] = self.experiment_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('base') is not None:
            self.base = m.get('base')
        if m.get('onlineTime') is not None:
            self.online_time = m.get('onlineTime')
        if m.get('offlineTime') is not None:
            self.offline_time = m.get('offlineTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('name') is not None:
            self.name = m.get('name')
        self.algorithms = []
        if m.get('algorithms') is not None:
            for k in m.get('algorithms'):
                temp_model = DescribeBaseExperimentResponseBodyResultAlgorithms()
                self.algorithms.append(temp_model.from_map(k))
        if m.get('buckets') is not None:
            self.buckets = m.get('buckets')
        if m.get('experimentId') is not None:
            self.experiment_id = m.get('experimentId')
        return self


class DescribeBaseExperimentResponseBody(TeaModel):
    def __init__(
        self,
        result: DescribeBaseExperimentResponseBodyResult = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = DescribeBaseExperimentResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DescribeBaseExperimentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeBaseExperimentResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeBaseExperimentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDataSetMessageResponseBodyResult(TeaModel):
    def __init__(
        self,
        message: str = None,
        timestamp: str = None,
        error_level: str = None,
        error_type: str = None,
    ):
        self.message = message
        self.timestamp = timestamp
        self.error_level = error_level
        self.error_type = error_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['message'] = self.message
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.error_level is not None:
            result['errorLevel'] = self.error_level
        if self.error_type is not None:
            result['errorType'] = self.error_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('errorLevel') is not None:
            self.error_level = m.get('errorLevel')
        if m.get('errorType') is not None:
            self.error_type = m.get('errorType')
        return self


class DescribeDataSetMessageResponseBody(TeaModel):
    def __init__(
        self,
        result: List[DescribeDataSetMessageResponseBodyResult] = None,
        code: str = None,
        request_id: str = None,
        message: str = None,
    ):
        self.result = result
        self.code = code
        self.request_id = request_id
        self.message = message

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        if self.code is not None:
            result['code'] = self.code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = DescribeDataSetMessageResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class DescribeDataSetMessageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDataSetMessageResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDataSetMessageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDefaultAlgorithmsResponseBodyResultConfig(TeaModel):
    def __init__(
        self,
        key: str = None,
        default_value: str = None,
        experiment_value: str = None,
        name: str = None,
    ):
        self.key = key
        self.default_value = default_value
        self.experiment_value = experiment_value
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.default_value is not None:
            result['defaultValue'] = self.default_value
        if self.experiment_value is not None:
            result['experimentValue'] = self.experiment_value
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('defaultValue') is not None:
            self.default_value = m.get('defaultValue')
        if m.get('experimentValue') is not None:
            self.experiment_value = m.get('experimentValue')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class DescribeDefaultAlgorithmsResponseBodyResult(TeaModel):
    def __init__(
        self,
        key: str = None,
        config: List[DescribeDefaultAlgorithmsResponseBodyResultConfig] = None,
        default_value: str = None,
        type: str = None,
        experiment_value: str = None,
        has_config: bool = None,
        category: str = None,
        name: str = None,
    ):
        self.key = key
        self.config = config
        self.default_value = default_value
        self.type = type
        self.experiment_value = experiment_value
        self.has_config = has_config
        self.category = category
        self.name = name

    def validate(self):
        if self.config:
            for k in self.config:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        result['config'] = []
        if self.config is not None:
            for k in self.config:
                result['config'].append(k.to_map() if k else None)
        if self.default_value is not None:
            result['defaultValue'] = self.default_value
        if self.type is not None:
            result['type'] = self.type
        if self.experiment_value is not None:
            result['experimentValue'] = self.experiment_value
        if self.has_config is not None:
            result['hasConfig'] = self.has_config
        if self.category is not None:
            result['category'] = self.category
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        self.config = []
        if m.get('config') is not None:
            for k in m.get('config'):
                temp_model = DescribeDefaultAlgorithmsResponseBodyResultConfig()
                self.config.append(temp_model.from_map(k))
        if m.get('defaultValue') is not None:
            self.default_value = m.get('defaultValue')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('experimentValue') is not None:
            self.experiment_value = m.get('experimentValue')
        if m.get('hasConfig') is not None:
            self.has_config = m.get('hasConfig')
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class DescribeDefaultAlgorithmsResponseBody(TeaModel):
    def __init__(
        self,
        result: List[DescribeDefaultAlgorithmsResponseBodyResult] = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = DescribeDefaultAlgorithmsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DescribeDefaultAlgorithmsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDefaultAlgorithmsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDefaultAlgorithmsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeExperimentResponseBodyResultAlgorithmsConfig(TeaModel):
    def __init__(
        self,
        key: str = None,
        default_value: str = None,
        experiment_value: str = None,
        name: str = None,
    ):
        self.key = key
        self.default_value = default_value
        self.experiment_value = experiment_value
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.default_value is not None:
            result['defaultValue'] = self.default_value
        if self.experiment_value is not None:
            result['experimentValue'] = self.experiment_value
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('defaultValue') is not None:
            self.default_value = m.get('defaultValue')
        if m.get('experimentValue') is not None:
            self.experiment_value = m.get('experimentValue')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class DescribeExperimentResponseBodyResultAlgorithms(TeaModel):
    def __init__(
        self,
        key: str = None,
        config: List[DescribeExperimentResponseBodyResultAlgorithmsConfig] = None,
        default_value: str = None,
        type: str = None,
        experiment_value: str = None,
        has_config: bool = None,
        category: str = None,
        name: str = None,
    ):
        self.key = key
        self.config = config
        self.default_value = default_value
        self.type = type
        self.experiment_value = experiment_value
        self.has_config = has_config
        self.category = category
        self.name = name

    def validate(self):
        if self.config:
            for k in self.config:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        result['config'] = []
        if self.config is not None:
            for k in self.config:
                result['config'].append(k.to_map() if k else None)
        if self.default_value is not None:
            result['defaultValue'] = self.default_value
        if self.type is not None:
            result['type'] = self.type
        if self.experiment_value is not None:
            result['experimentValue'] = self.experiment_value
        if self.has_config is not None:
            result['hasConfig'] = self.has_config
        if self.category is not None:
            result['category'] = self.category
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        self.config = []
        if m.get('config') is not None:
            for k in m.get('config'):
                temp_model = DescribeExperimentResponseBodyResultAlgorithmsConfig()
                self.config.append(temp_model.from_map(k))
        if m.get('defaultValue') is not None:
            self.default_value = m.get('defaultValue')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('experimentValue') is not None:
            self.experiment_value = m.get('experimentValue')
        if m.get('hasConfig') is not None:
            self.has_config = m.get('hasConfig')
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class DescribeExperimentResponseBodyResult(TeaModel):
    def __init__(
        self,
        base: bool = None,
        online_time: str = None,
        offline_time: str = None,
        description: str = None,
        status: str = None,
        name: str = None,
        algorithms: List[DescribeExperimentResponseBodyResultAlgorithms] = None,
        buckets: List[str] = None,
        experiment_id: str = None,
    ):
        self.base = base
        self.online_time = online_time
        self.offline_time = offline_time
        self.description = description
        self.status = status
        self.name = name
        self.algorithms = algorithms
        self.buckets = buckets
        self.experiment_id = experiment_id

    def validate(self):
        if self.algorithms:
            for k in self.algorithms:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base is not None:
            result['base'] = self.base
        if self.online_time is not None:
            result['onlineTime'] = self.online_time
        if self.offline_time is not None:
            result['offlineTime'] = self.offline_time
        if self.description is not None:
            result['description'] = self.description
        if self.status is not None:
            result['status'] = self.status
        if self.name is not None:
            result['name'] = self.name
        result['algorithms'] = []
        if self.algorithms is not None:
            for k in self.algorithms:
                result['algorithms'].append(k.to_map() if k else None)
        if self.buckets is not None:
            result['buckets'] = self.buckets
        if self.experiment_id is not None:
            result['experimentId'] = self.experiment_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('base') is not None:
            self.base = m.get('base')
        if m.get('onlineTime') is not None:
            self.online_time = m.get('onlineTime')
        if m.get('offlineTime') is not None:
            self.offline_time = m.get('offlineTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('name') is not None:
            self.name = m.get('name')
        self.algorithms = []
        if m.get('algorithms') is not None:
            for k in m.get('algorithms'):
                temp_model = DescribeExperimentResponseBodyResultAlgorithms()
                self.algorithms.append(temp_model.from_map(k))
        if m.get('buckets') is not None:
            self.buckets = m.get('buckets')
        if m.get('experimentId') is not None:
            self.experiment_id = m.get('experimentId')
        return self


class DescribeExperimentResponseBody(TeaModel):
    def __init__(
        self,
        result: DescribeExperimentResponseBodyResult = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = DescribeExperimentResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DescribeExperimentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeExperimentResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeExperimentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeExperimentEnvResponseBodyResult(TeaModel):
    def __init__(
        self,
        bucket_count: int = None,
        divide_type: str = None,
    ):
        self.bucket_count = bucket_count
        self.divide_type = divide_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_count is not None:
            result['bucketCount'] = self.bucket_count
        if self.divide_type is not None:
            result['divideType'] = self.divide_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bucketCount') is not None:
            self.bucket_count = m.get('bucketCount')
        if m.get('divideType') is not None:
            self.divide_type = m.get('divideType')
        return self


class DescribeExperimentEnvResponseBody(TeaModel):
    def __init__(
        self,
        result: DescribeExperimentEnvResponseBodyResult = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = DescribeExperimentEnvResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DescribeExperimentEnvResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeExperimentEnvResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeExperimentEnvResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeExperimentEnvProgressResponseBodyResult(TeaModel):
    def __init__(
        self,
        status: str = None,
        progress: int = None,
    ):
        self.status = status
        self.progress = progress

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['status'] = self.status
        if self.progress is not None:
            result['progress'] = self.progress
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('progress') is not None:
            self.progress = m.get('progress')
        return self


class DescribeExperimentEnvProgressResponseBody(TeaModel):
    def __init__(
        self,
        result: DescribeExperimentEnvProgressResponseBodyResult = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = DescribeExperimentEnvProgressResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DescribeExperimentEnvProgressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeExperimentEnvProgressResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeExperimentEnvProgressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFilteringAlgorithmResponseBodyResultMetaExtInfo(TeaModel):
    def __init__(
        self,
        kv_separator: str = None,
        item_separator: str = None,
    ):
        self.kv_separator = kv_separator
        self.item_separator = item_separator

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.kv_separator is not None:
            result['kvSeparator'] = self.kv_separator
        if self.item_separator is not None:
            result['itemSeparator'] = self.item_separator
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('kvSeparator') is not None:
            self.kv_separator = m.get('kvSeparator')
        if m.get('itemSeparator') is not None:
            self.item_separator = m.get('itemSeparator')
        return self


class DescribeFilteringAlgorithmResponseBodyResultMetaThreshold(TeaModel):
    def __init__(
        self,
        source_data_size_threshold: int = None,
        source_data_record_threshold: int = None,
        index_size_threshold: int = None,
        index_loss_threshold: int = None,
    ):
        self.source_data_size_threshold = source_data_size_threshold
        self.source_data_record_threshold = source_data_record_threshold
        self.index_size_threshold = index_size_threshold
        self.index_loss_threshold = index_loss_threshold

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_data_size_threshold is not None:
            result['sourceDataSizeThreshold'] = self.source_data_size_threshold
        if self.source_data_record_threshold is not None:
            result['sourceDataRecordThreshold'] = self.source_data_record_threshold
        if self.index_size_threshold is not None:
            result['indexSizeThreshold'] = self.index_size_threshold
        if self.index_loss_threshold is not None:
            result['indexLossThreshold'] = self.index_loss_threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sourceDataSizeThreshold') is not None:
            self.source_data_size_threshold = m.get('sourceDataSizeThreshold')
        if m.get('sourceDataRecordThreshold') is not None:
            self.source_data_record_threshold = m.get('sourceDataRecordThreshold')
        if m.get('indexSizeThreshold') is not None:
            self.index_size_threshold = m.get('indexSizeThreshold')
        if m.get('indexLossThreshold') is not None:
            self.index_loss_threshold = m.get('indexLossThreshold')
        return self


class DescribeFilteringAlgorithmResponseBodyResultMeta(TeaModel):
    def __init__(
        self,
        task_id: str = None,
        meta_type: str = None,
        type: str = None,
        ext_info: DescribeFilteringAlgorithmResponseBodyResultMetaExtInfo = None,
        category: str = None,
        threshold: DescribeFilteringAlgorithmResponseBodyResultMetaThreshold = None,
        table_name: str = None,
        cluster_id: str = None,
        cron: str = None,
        description: str = None,
        project_name: str = None,
        algorithm_name: str = None,
        cron_enabled: bool = None,
    ):
        self.task_id = task_id
        self.meta_type = meta_type
        self.type = type
        self.ext_info = ext_info
        self.category = category
        self.threshold = threshold
        self.table_name = table_name
        self.cluster_id = cluster_id
        self.cron = cron
        self.description = description
        self.project_name = project_name
        self.algorithm_name = algorithm_name
        self.cron_enabled = cron_enabled

    def validate(self):
        if self.ext_info:
            self.ext_info.validate()
        if self.threshold:
            self.threshold.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['taskId'] = self.task_id
        if self.meta_type is not None:
            result['metaType'] = self.meta_type
        if self.type is not None:
            result['type'] = self.type
        if self.ext_info is not None:
            result['extInfo'] = self.ext_info.to_map()
        if self.category is not None:
            result['category'] = self.category
        if self.threshold is not None:
            result['threshold'] = self.threshold.to_map()
        if self.table_name is not None:
            result['tableName'] = self.table_name
        if self.cluster_id is not None:
            result['clusterId'] = self.cluster_id
        if self.cron is not None:
            result['cron'] = self.cron
        if self.description is not None:
            result['description'] = self.description
        if self.project_name is not None:
            result['projectName'] = self.project_name
        if self.algorithm_name is not None:
            result['algorithmName'] = self.algorithm_name
        if self.cron_enabled is not None:
            result['cronEnabled'] = self.cron_enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        if m.get('metaType') is not None:
            self.meta_type = m.get('metaType')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('extInfo') is not None:
            temp_model = DescribeFilteringAlgorithmResponseBodyResultMetaExtInfo()
            self.ext_info = temp_model.from_map(m['extInfo'])
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('threshold') is not None:
            temp_model = DescribeFilteringAlgorithmResponseBodyResultMetaThreshold()
            self.threshold = temp_model.from_map(m['threshold'])
        if m.get('tableName') is not None:
            self.table_name = m.get('tableName')
        if m.get('clusterId') is not None:
            self.cluster_id = m.get('clusterId')
        if m.get('cron') is not None:
            self.cron = m.get('cron')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')
        if m.get('algorithmName') is not None:
            self.algorithm_name = m.get('algorithmName')
        if m.get('cronEnabled') is not None:
            self.cron_enabled = m.get('cronEnabled')
        return self


class DescribeFilteringAlgorithmResponseBodyResult(TeaModel):
    def __init__(
        self,
        gmt_modified: str = None,
        status: str = None,
        gmt_create: str = None,
        algorithm_id: str = None,
        meta: DescribeFilteringAlgorithmResponseBodyResultMeta = None,
    ):
        self.gmt_modified = gmt_modified
        self.status = status
        self.gmt_create = gmt_create
        self.algorithm_id = algorithm_id
        self.meta = meta

    def validate(self):
        if self.meta:
            self.meta.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.status is not None:
            result['status'] = self.status
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.algorithm_id is not None:
            result['algorithmId'] = self.algorithm_id
        if self.meta is not None:
            result['meta'] = self.meta.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('algorithmId') is not None:
            self.algorithm_id = m.get('algorithmId')
        if m.get('meta') is not None:
            temp_model = DescribeFilteringAlgorithmResponseBodyResultMeta()
            self.meta = temp_model.from_map(m['meta'])
        return self


class DescribeFilteringAlgorithmResponseBody(TeaModel):
    def __init__(
        self,
        result: DescribeFilteringAlgorithmResponseBodyResult = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = DescribeFilteringAlgorithmResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DescribeFilteringAlgorithmResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeFilteringAlgorithmResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeFilteringAlgorithmResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceResponseBodyResult(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        type: str = None,
        lock_mode: str = None,
        expired_time: str = None,
        scene: str = None,
        status: str = None,
        gmt_create: str = None,
        charge_type: str = None,
        industry: str = None,
        commodity_code: str = None,
        gmt_modified: str = None,
        data_set_version: str = None,
        name: str = None,
        instance_id: str = None,
    ):
        self.region_id = region_id
        self.type = type
        self.lock_mode = lock_mode
        self.expired_time = expired_time
        self.scene = scene
        self.status = status
        self.gmt_create = gmt_create
        self.charge_type = charge_type
        self.industry = industry
        self.commodity_code = commodity_code
        self.gmt_modified = gmt_modified
        self.data_set_version = data_set_version
        self.name = name
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.type is not None:
            result['type'] = self.type
        if self.lock_mode is not None:
            result['lockMode'] = self.lock_mode
        if self.expired_time is not None:
            result['expiredTime'] = self.expired_time
        if self.scene is not None:
            result['scene'] = self.scene
        if self.status is not None:
            result['status'] = self.status
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.charge_type is not None:
            result['chargeType'] = self.charge_type
        if self.industry is not None:
            result['industry'] = self.industry
        if self.commodity_code is not None:
            result['commodityCode'] = self.commodity_code
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.data_set_version is not None:
            result['dataSetVersion'] = self.data_set_version
        if self.name is not None:
            result['name'] = self.name
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('lockMode') is not None:
            self.lock_mode = m.get('lockMode')
        if m.get('expiredTime') is not None:
            self.expired_time = m.get('expiredTime')
        if m.get('scene') is not None:
            self.scene = m.get('scene')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('chargeType') is not None:
            self.charge_type = m.get('chargeType')
        if m.get('industry') is not None:
            self.industry = m.get('industry')
        if m.get('commodityCode') is not None:
            self.commodity_code = m.get('commodityCode')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('dataSetVersion') is not None:
            self.data_set_version = m.get('dataSetVersion')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        return self


class DescribeInstanceResponseBody(TeaModel):
    def __init__(
        self,
        result: DescribeInstanceResponseBodyResult = None,
        code: str = None,
        request_id: str = None,
        message: str = None,
    ):
        self.result = result
        self.code = code
        self.request_id = request_id
        self.message = message

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.code is not None:
            result['code'] = self.code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = DescribeInstanceResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class DescribeInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeLatestTaskResponseBodyResult(TeaModel):
    def __init__(
        self,
        code: str = None,
        switched_time: str = None,
        rollback_enabled: bool = None,
        message: str = None,
        flow_type: str = None,
        cost_seconds: int = None,
        built_time: str = None,
        version_id: str = None,
        size: int = None,
        status: str = None,
        progress: int = None,
    ):
        self.code = code
        self.switched_time = switched_time
        self.rollback_enabled = rollback_enabled
        self.message = message
        self.flow_type = flow_type
        self.cost_seconds = cost_seconds
        self.built_time = built_time
        self.version_id = version_id
        self.size = size
        self.status = status
        self.progress = progress

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.switched_time is not None:
            result['switchedTime'] = self.switched_time
        if self.rollback_enabled is not None:
            result['rollbackEnabled'] = self.rollback_enabled
        if self.message is not None:
            result['message'] = self.message
        if self.flow_type is not None:
            result['flowType'] = self.flow_type
        if self.cost_seconds is not None:
            result['costSeconds'] = self.cost_seconds
        if self.built_time is not None:
            result['builtTime'] = self.built_time
        if self.version_id is not None:
            result['versionId'] = self.version_id
        if self.size is not None:
            result['size'] = self.size
        if self.status is not None:
            result['status'] = self.status
        if self.progress is not None:
            result['progress'] = self.progress
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('switchedTime') is not None:
            self.switched_time = m.get('switchedTime')
        if m.get('rollbackEnabled') is not None:
            self.rollback_enabled = m.get('rollbackEnabled')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('flowType') is not None:
            self.flow_type = m.get('flowType')
        if m.get('costSeconds') is not None:
            self.cost_seconds = m.get('costSeconds')
        if m.get('builtTime') is not None:
            self.built_time = m.get('builtTime')
        if m.get('versionId') is not None:
            self.version_id = m.get('versionId')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('progress') is not None:
            self.progress = m.get('progress')
        return self


class DescribeLatestTaskResponseBody(TeaModel):
    def __init__(
        self,
        result: List[DescribeLatestTaskResponseBodyResult] = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = DescribeLatestTaskResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DescribeLatestTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeLatestTaskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeLatestTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeQuotaResponseBodyResult(TeaModel):
    def __init__(
        self,
        item_count_used: int = None,
        item_count: int = None,
        user_count: int = None,
        user_count_used: int = None,
        qps: int = None,
        current_qps: int = None,
    ):
        self.item_count_used = item_count_used
        self.item_count = item_count
        self.user_count = user_count
        self.user_count_used = user_count_used
        self.qps = qps
        self.current_qps = current_qps

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.item_count_used is not None:
            result['itemCountUsed'] = self.item_count_used
        if self.item_count is not None:
            result['itemCount'] = self.item_count
        if self.user_count is not None:
            result['userCount'] = self.user_count
        if self.user_count_used is not None:
            result['userCountUsed'] = self.user_count_used
        if self.qps is not None:
            result['qps'] = self.qps
        if self.current_qps is not None:
            result['currentQps'] = self.current_qps
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('itemCountUsed') is not None:
            self.item_count_used = m.get('itemCountUsed')
        if m.get('itemCount') is not None:
            self.item_count = m.get('itemCount')
        if m.get('userCount') is not None:
            self.user_count = m.get('userCount')
        if m.get('userCountUsed') is not None:
            self.user_count_used = m.get('userCountUsed')
        if m.get('qps') is not None:
            self.qps = m.get('qps')
        if m.get('currentQps') is not None:
            self.current_qps = m.get('currentQps')
        return self


class DescribeQuotaResponseBody(TeaModel):
    def __init__(
        self,
        result: DescribeQuotaResponseBodyResult = None,
        code: str = None,
        request_id: str = None,
        message: str = None,
    ):
        self.result = result
        self.code = code
        self.request_id = request_id
        self.message = message

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.code is not None:
            result['code'] = self.code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = DescribeQuotaResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class DescribeQuotaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeQuotaResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeQuotaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
    ):
        self.accept_language = accept_language

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['acceptLanguage'] = self.accept_language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('acceptLanguage') is not None:
            self.accept_language = m.get('acceptLanguage')
        return self


class DescribeRegionsResponseBodyResult(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        endpoint: str = None,
        status: str = None,
        local_name: str = None,
        console_url: str = None,
    ):
        self.region_id = region_id
        self.endpoint = endpoint
        self.status = status
        self.local_name = local_name
        self.console_url = console_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint
        if self.status is not None:
            result['status'] = self.status
        if self.local_name is not None:
            result['localName'] = self.local_name
        if self.console_url is not None:
            result['consoleUrl'] = self.console_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('localName') is not None:
            self.local_name = m.get('localName')
        if m.get('consoleUrl') is not None:
            self.console_url = m.get('consoleUrl')
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(
        self,
        result: List[DescribeRegionsResponseBodyResult] = None,
        code: str = None,
        request_id: str = None,
        message: str = None,
    ):
        self.result = result
        self.code = code
        self.request_id = request_id
        self.message = message

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        if self.code is not None:
            result['code'] = self.code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = DescribeRegionsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRegionsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRuleRequest(TeaModel):
    def __init__(
        self,
        scene_id: str = None,
        rule_type: str = None,
    ):
        self.scene_id = scene_id
        self.rule_type = rule_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene_id is not None:
            result['sceneId'] = self.scene_id
        if self.rule_type is not None:
            result['ruleType'] = self.rule_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sceneId') is not None:
            self.scene_id = m.get('sceneId')
        if m.get('ruleType') is not None:
            self.rule_type = m.get('ruleType')
        return self


class DescribeRuleResponseBodyResult(TeaModel):
    def __init__(
        self,
        rule_id: str = None,
        gmt_modified: str = None,
        status: str = None,
        gmt_create: str = None,
    ):
        self.rule_id = rule_id
        self.gmt_modified = gmt_modified
        self.status = status
        self.gmt_create = gmt_create

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_id is not None:
            result['ruleId'] = self.rule_id
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.status is not None:
            result['status'] = self.status
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ruleId') is not None:
            self.rule_id = m.get('ruleId')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        return self


class DescribeRuleResponseBody(TeaModel):
    def __init__(
        self,
        result: DescribeRuleResponseBodyResult = None,
        code: str = None,
        request_id: str = None,
        message: str = None,
    ):
        self.result = result
        self.code = code
        self.request_id = request_id
        self.message = message

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.code is not None:
            result['code'] = self.code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = DescribeRuleResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class DescribeRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRuleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSceneResponseBodyResult(TeaModel):
    def __init__(
        self,
        scene_id: str = None,
        gmt_modified: str = None,
        status: str = None,
        gmt_create: str = None,
    ):
        self.scene_id = scene_id
        self.gmt_modified = gmt_modified
        self.status = status
        self.gmt_create = gmt_create

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene_id is not None:
            result['sceneId'] = self.scene_id
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.status is not None:
            result['status'] = self.status
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sceneId') is not None:
            self.scene_id = m.get('sceneId')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        return self


class DescribeSceneResponseBody(TeaModel):
    def __init__(
        self,
        result: DescribeSceneResponseBodyResult = None,
        code: str = None,
        request_id: str = None,
        message: str = None,
    ):
        self.result = result
        self.code = code
        self.request_id = request_id
        self.message = message

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.code is not None:
            result['code'] = self.code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = DescribeSceneResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class DescribeSceneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSceneResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSceneBucketResponseBodyResult(TeaModel):
    def __init__(
        self,
        num: int = None,
        in_use: str = None,
        detail: Dict[str, Any] = None,
    ):
        self.num = num
        self.in_use = in_use
        self.detail = detail

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.num is not None:
            result['num'] = self.num
        if self.in_use is not None:
            result['inUse'] = self.in_use
        if self.detail is not None:
            result['detail'] = self.detail
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('num') is not None:
            self.num = m.get('num')
        if m.get('inUse') is not None:
            self.in_use = m.get('inUse')
        if m.get('detail') is not None:
            self.detail = m.get('detail')
        return self


class DescribeSceneBucketResponseBody(TeaModel):
    def __init__(
        self,
        result: DescribeSceneBucketResponseBodyResult = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = DescribeSceneBucketResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DescribeSceneBucketResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSceneBucketResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeSceneBucketResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSceneThroughputResponseBodyResult(TeaModel):
    def __init__(
        self,
        pv_count: int = None,
    ):
        self.pv_count = pv_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pv_count is not None:
            result['pvCount'] = self.pv_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pvCount') is not None:
            self.pv_count = m.get('pvCount')
        return self


class DescribeSceneThroughputResponseBody(TeaModel):
    def __init__(
        self,
        result: DescribeSceneThroughputResponseBodyResult = None,
        code: str = None,
        request_id: str = None,
        message: str = None,
    ):
        self.result = result
        self.code = code
        self.request_id = request_id
        self.message = message

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.code is not None:
            result['code'] = self.code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = DescribeSceneThroughputResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class DescribeSceneThroughputResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSceneThroughputResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeSceneThroughputResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSyncReportDetailRequest(TeaModel):
    def __init__(
        self,
        start_time: int = None,
        end_time: int = None,
        type: str = None,
        level_type: str = None,
    ):
        self.start_time = start_time
        self.end_time = end_time
        self.type = type
        self.level_type = level_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.type is not None:
            result['type'] = self.type
        if self.level_type is not None:
            result['levelType'] = self.level_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('levelType') is not None:
            self.level_type = m.get('levelType')
        return self


class DescribeSyncReportDetailResponseBodyResultHistoryData(TeaModel):
    def __init__(
        self,
        error_percent: float = None,
        start_time: int = None,
        end_time: int = None,
    ):
        self.error_percent = error_percent
        self.start_time = start_time
        self.end_time = end_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_percent is not None:
            result['errorPercent'] = self.error_percent
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorPercent') is not None:
            self.error_percent = m.get('errorPercent')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        return self


class DescribeSyncReportDetailResponseBodyResult(TeaModel):
    def __init__(
        self,
        history_data: List[DescribeSyncReportDetailResponseBodyResultHistoryData] = None,
        sample_display: bool = None,
        type: str = None,
        error_count: int = None,
        error_percent: float = None,
        default_display: bool = None,
    ):
        self.history_data = history_data
        self.sample_display = sample_display
        self.type = type
        self.error_count = error_count
        self.error_percent = error_percent
        self.default_display = default_display

    def validate(self):
        if self.history_data:
            for k in self.history_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['historyData'] = []
        if self.history_data is not None:
            for k in self.history_data:
                result['historyData'].append(k.to_map() if k else None)
        if self.sample_display is not None:
            result['sampleDisplay'] = self.sample_display
        if self.type is not None:
            result['type'] = self.type
        if self.error_count is not None:
            result['errorCount'] = self.error_count
        if self.error_percent is not None:
            result['errorPercent'] = self.error_percent
        if self.default_display is not None:
            result['defaultDisplay'] = self.default_display
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.history_data = []
        if m.get('historyData') is not None:
            for k in m.get('historyData'):
                temp_model = DescribeSyncReportDetailResponseBodyResultHistoryData()
                self.history_data.append(temp_model.from_map(k))
        if m.get('sampleDisplay') is not None:
            self.sample_display = m.get('sampleDisplay')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('errorCount') is not None:
            self.error_count = m.get('errorCount')
        if m.get('errorPercent') is not None:
            self.error_percent = m.get('errorPercent')
        if m.get('defaultDisplay') is not None:
            self.default_display = m.get('defaultDisplay')
        return self


class DescribeSyncReportDetailResponseBody(TeaModel):
    def __init__(
        self,
        result: List[DescribeSyncReportDetailResponseBodyResult] = None,
        code: str = None,
        request_id: str = None,
        message: str = None,
    ):
        self.result = result
        self.code = code
        self.request_id = request_id
        self.message = message

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        if self.code is not None:
            result['code'] = self.code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = DescribeSyncReportDetailResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class DescribeSyncReportDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSyncReportDetailResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeSyncReportDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSyncReportOutliersRequest(TeaModel):
    def __init__(
        self,
        start_time: int = None,
        key: str = None,
        type: str = None,
        end_time: int = None,
        level_type: str = None,
    ):
        self.start_time = start_time
        self.key = key
        self.type = type
        self.end_time = end_time
        self.level_type = level_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.key is not None:
            result['key'] = self.key
        if self.type is not None:
            result['type'] = self.type
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.level_type is not None:
            result['levelType'] = self.level_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('levelType') is not None:
            self.level_type = m.get('levelType')
        return self


class DescribeSyncReportOutliersResponseBody(TeaModel):
    def __init__(
        self,
        result: Dict[str, Any] = None,
        code: str = None,
        request_id: str = None,
        message: str = None,
    ):
        self.result = result
        self.code = code
        self.request_id = request_id
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result
        if self.code is not None:
            result['code'] = self.code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class DescribeSyncReportOutliersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSyncReportOutliersResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeSyncReportOutliersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUserMetricsRequest(TeaModel):
    def __init__(
        self,
        start_time: int = None,
        end_time: int = None,
        metric_type: str = None,
    ):
        self.start_time = start_time
        self.end_time = end_time
        self.metric_type = metric_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.metric_type is not None:
            result['metricType'] = self.metric_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('metricType') is not None:
            self.metric_type = m.get('metricType')
        return self


class DescribeUserMetricsResponseBodyResultDataPoints(TeaModel):
    def __init__(
        self,
        val: float = None,
        start_time: int = None,
        end_time: int = None,
    ):
        self.val = val
        self.start_time = start_time
        self.end_time = end_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.val is not None:
            result['val'] = self.val
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('val') is not None:
            self.val = m.get('val')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        return self


class DescribeUserMetricsResponseBodyResult(TeaModel):
    def __init__(
        self,
        scene_id: str = None,
        data_points: List[DescribeUserMetricsResponseBodyResultDataPoints] = None,
    ):
        self.scene_id = scene_id
        self.data_points = data_points

    def validate(self):
        if self.data_points:
            for k in self.data_points:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene_id is not None:
            result['sceneId'] = self.scene_id
        result['dataPoints'] = []
        if self.data_points is not None:
            for k in self.data_points:
                result['dataPoints'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sceneId') is not None:
            self.scene_id = m.get('sceneId')
        self.data_points = []
        if m.get('dataPoints') is not None:
            for k in m.get('dataPoints'):
                temp_model = DescribeUserMetricsResponseBodyResultDataPoints()
                self.data_points.append(temp_model.from_map(k))
        return self


class DescribeUserMetricsResponseBody(TeaModel):
    def __init__(
        self,
        result: List[DescribeUserMetricsResponseBodyResult] = None,
        code: str = None,
        request_id: str = None,
        message: str = None,
    ):
        self.result = result
        self.code = code
        self.request_id = request_id
        self.message = message

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        if self.code is not None:
            result['code'] = self.code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = DescribeUserMetricsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class DescribeUserMetricsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeUserMetricsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeUserMetricsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DowngradeInstanceResponseBodyResult(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        return self


class DowngradeInstanceResponseBody(TeaModel):
    def __init__(
        self,
        result: DowngradeInstanceResponseBodyResult = None,
        code: str = None,
        request_id: str = None,
        message: str = None,
    ):
        self.result = result
        self.code = code
        self.request_id = request_id
        self.message = message

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.code is not None:
            result['code'] = self.code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = DowngradeInstanceResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class DowngradeInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DowngradeInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DowngradeInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableExperimentResponseBody(TeaModel):
    def __init__(
        self,
        result: bool = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class EnableExperimentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EnableExperimentResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = EnableExperimentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDashboardDetailsRequest(TeaModel):
    def __init__(
        self,
        start_time: int = None,
        end_time: int = None,
        trace_ids: str = None,
        scene_ids: str = None,
        metric_type: str = None,
        experiment_ids: str = None,
    ):
        self.start_time = start_time
        self.end_time = end_time
        self.trace_ids = trace_ids
        self.scene_ids = scene_ids
        self.metric_type = metric_type
        self.experiment_ids = experiment_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.trace_ids is not None:
            result['traceIds'] = self.trace_ids
        if self.scene_ids is not None:
            result['sceneIds'] = self.scene_ids
        if self.metric_type is not None:
            result['metricType'] = self.metric_type
        if self.experiment_ids is not None:
            result['experimentIds'] = self.experiment_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('traceIds') is not None:
            self.trace_ids = m.get('traceIds')
        if m.get('sceneIds') is not None:
            self.scene_ids = m.get('sceneIds')
        if m.get('metricType') is not None:
            self.metric_type = m.get('metricType')
        if m.get('experimentIds') is not None:
            self.experiment_ids = m.get('experimentIds')
        return self


class ListDashboardDetailsResponseBodyResultMetricRes(TeaModel):
    def __init__(
        self,
        total: Dict[str, Any] = None,
        detail: Dict[str, Any] = None,
    ):
        self.total = total
        self.detail = detail

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total is not None:
            result['total'] = self.total
        if self.detail is not None:
            result['detail'] = self.detail
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('total') is not None:
            self.total = m.get('total')
        if m.get('detail') is not None:
            self.detail = m.get('detail')
        return self


class ListDashboardDetailsResponseBodyResult(TeaModel):
    def __init__(
        self,
        trace_id: str = None,
        scene_id: str = None,
        metric_res: ListDashboardDetailsResponseBodyResultMetricRes = None,
    ):
        self.trace_id = trace_id
        self.scene_id = scene_id
        self.metric_res = metric_res

    def validate(self):
        if self.metric_res:
            self.metric_res.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.trace_id is not None:
            result['traceId'] = self.trace_id
        if self.scene_id is not None:
            result['sceneId'] = self.scene_id
        if self.metric_res is not None:
            result['metricRes'] = self.metric_res.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        if m.get('sceneId') is not None:
            self.scene_id = m.get('sceneId')
        if m.get('metricRes') is not None:
            temp_model = ListDashboardDetailsResponseBodyResultMetricRes()
            self.metric_res = temp_model.from_map(m['metricRes'])
        return self


class ListDashboardDetailsResponseBody(TeaModel):
    def __init__(
        self,
        result: List[ListDashboardDetailsResponseBodyResult] = None,
        code: str = None,
        request_id: str = None,
        message: str = None,
    ):
        self.result = result
        self.code = code
        self.request_id = request_id
        self.message = message

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        if self.code is not None:
            result['code'] = self.code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListDashboardDetailsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class ListDashboardDetailsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDashboardDetailsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListDashboardDetailsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDashboardDetailsFlowsRequest(TeaModel):
    def __init__(
        self,
        start_time: int = None,
        end_time: int = None,
        trace_ids: str = None,
        scene_ids: str = None,
        metric_type: str = None,
        experiment_ids: str = None,
    ):
        self.start_time = start_time
        self.end_time = end_time
        self.trace_ids = trace_ids
        self.scene_ids = scene_ids
        self.metric_type = metric_type
        self.experiment_ids = experiment_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.trace_ids is not None:
            result['traceIds'] = self.trace_ids
        if self.scene_ids is not None:
            result['sceneIds'] = self.scene_ids
        if self.metric_type is not None:
            result['metricType'] = self.metric_type
        if self.experiment_ids is not None:
            result['experimentIds'] = self.experiment_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('traceIds') is not None:
            self.trace_ids = m.get('traceIds')
        if m.get('sceneIds') is not None:
            self.scene_ids = m.get('sceneIds')
        if m.get('metricType') is not None:
            self.metric_type = m.get('metricType')
        if m.get('experimentIds') is not None:
            self.experiment_ids = m.get('experimentIds')
        return self


class ListDashboardDetailsFlowsResponseBodyResultMetricData(TeaModel):
    def __init__(
        self,
        trace_id: str = None,
        scene_id: str = None,
        metric_res: Dict[str, Any] = None,
    ):
        self.trace_id = trace_id
        self.scene_id = scene_id
        self.metric_res = metric_res

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.trace_id is not None:
            result['traceId'] = self.trace_id
        if self.scene_id is not None:
            result['sceneId'] = self.scene_id
        if self.metric_res is not None:
            result['metricRes'] = self.metric_res
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        if m.get('sceneId') is not None:
            self.scene_id = m.get('sceneId')
        if m.get('metricRes') is not None:
            self.metric_res = m.get('metricRes')
        return self


class ListDashboardDetailsFlowsResponseBodyResult(TeaModel):
    def __init__(
        self,
        metric_type: str = None,
        metric_data: List[ListDashboardDetailsFlowsResponseBodyResultMetricData] = None,
    ):
        self.metric_type = metric_type
        self.metric_data = metric_data

    def validate(self):
        if self.metric_data:
            for k in self.metric_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.metric_type is not None:
            result['metricType'] = self.metric_type
        result['metricData'] = []
        if self.metric_data is not None:
            for k in self.metric_data:
                result['metricData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('metricType') is not None:
            self.metric_type = m.get('metricType')
        self.metric_data = []
        if m.get('metricData') is not None:
            for k in m.get('metricData'):
                temp_model = ListDashboardDetailsFlowsResponseBodyResultMetricData()
                self.metric_data.append(temp_model.from_map(k))
        return self


class ListDashboardDetailsFlowsResponseBody(TeaModel):
    def __init__(
        self,
        result: ListDashboardDetailsFlowsResponseBodyResult = None,
        code: str = None,
        request_id: str = None,
        message: str = None,
    ):
        self.result = result
        self.code = code
        self.request_id = request_id
        self.message = message

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.code is not None:
            result['code'] = self.code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = ListDashboardDetailsFlowsResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class ListDashboardDetailsFlowsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDashboardDetailsFlowsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListDashboardDetailsFlowsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDashboardMetricsRequest(TeaModel):
    def __init__(
        self,
        start_time: int = None,
        end_time: int = None,
        metric_type: str = None,
    ):
        self.start_time = start_time
        self.end_time = end_time
        self.metric_type = metric_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.metric_type is not None:
            result['metricType'] = self.metric_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('metricType') is not None:
            self.metric_type = m.get('metricType')
        return self


class ListDashboardMetricsResponseBodyResultDetail(TeaModel):
    def __init__(
        self,
        val: str = None,
        start_time: str = None,
        end_time: str = None,
    ):
        self.val = val
        self.start_time = start_time
        self.end_time = end_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.val is not None:
            result['val'] = self.val
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('val') is not None:
            self.val = m.get('val')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        return self


class ListDashboardMetricsResponseBodyResult(TeaModel):
    def __init__(
        self,
        total: Dict[str, Any] = None,
        detail: List[ListDashboardMetricsResponseBodyResultDetail] = None,
    ):
        self.total = total
        self.detail = detail

    def validate(self):
        if self.detail:
            for k in self.detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total is not None:
            result['total'] = self.total
        result['detail'] = []
        if self.detail is not None:
            for k in self.detail:
                result['detail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('total') is not None:
            self.total = m.get('total')
        self.detail = []
        if m.get('detail') is not None:
            for k in m.get('detail'):
                temp_model = ListDashboardMetricsResponseBodyResultDetail()
                self.detail.append(temp_model.from_map(k))
        return self


class ListDashboardMetricsResponseBody(TeaModel):
    def __init__(
        self,
        result: List[ListDashboardMetricsResponseBodyResult] = None,
        code: str = None,
        request_id: str = None,
        message: str = None,
    ):
        self.result = result
        self.code = code
        self.request_id = request_id
        self.message = message

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        if self.code is not None:
            result['code'] = self.code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListDashboardMetricsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class ListDashboardMetricsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDashboardMetricsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListDashboardMetricsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDashboardMetricsFlowsRequest(TeaModel):
    def __init__(
        self,
        start_time: int = None,
        end_time: int = None,
        metric_type: str = None,
    ):
        self.start_time = start_time
        self.end_time = end_time
        self.metric_type = metric_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.metric_type is not None:
            result['metricType'] = self.metric_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('metricType') is not None:
            self.metric_type = m.get('metricType')
        return self


class ListDashboardMetricsFlowsResponseBodyResult(TeaModel):
    def __init__(
        self,
        metric_type: str = None,
        metric_data: Dict[str, Any] = None,
    ):
        self.metric_type = metric_type
        self.metric_data = metric_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.metric_type is not None:
            result['metricType'] = self.metric_type
        if self.metric_data is not None:
            result['metricData'] = self.metric_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('metricType') is not None:
            self.metric_type = m.get('metricType')
        if m.get('metricData') is not None:
            self.metric_data = m.get('metricData')
        return self


class ListDashboardMetricsFlowsResponseBody(TeaModel):
    def __init__(
        self,
        result: List[ListDashboardMetricsFlowsResponseBodyResult] = None,
        code: str = None,
        request_id: str = None,
        message: str = None,
    ):
        self.result = result
        self.code = code
        self.request_id = request_id
        self.message = message

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        if self.code is not None:
            result['code'] = self.code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListDashboardMetricsFlowsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class ListDashboardMetricsFlowsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDashboardMetricsFlowsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListDashboardMetricsFlowsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDataSetResponseBodyResult(TeaModel):
    def __init__(
        self,
        version_id: str = None,
        state: str = None,
        gmt_modified: int = None,
        gmt_create: int = None,
        instance_id: str = None,
    ):
        self.version_id = version_id
        self.state = state
        self.gmt_modified = gmt_modified
        self.gmt_create = gmt_create
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.version_id is not None:
            result['versionId'] = self.version_id
        if self.state is not None:
            result['state'] = self.state
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('versionId') is not None:
            self.version_id = m.get('versionId')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        return self


class ListDataSetResponseBody(TeaModel):
    def __init__(
        self,
        result: List[ListDataSetResponseBodyResult] = None,
        code: str = None,
        request_id: str = None,
        message: str = None,
    ):
        self.result = result
        self.code = code
        self.request_id = request_id
        self.message = message

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        if self.code is not None:
            result['code'] = self.code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListDataSetResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class ListDataSetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDataSetResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListDataSetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDataSourceResponseBodyResultMeta(TeaModel):
    def __init__(
        self,
        bucket_name: str = None,
        access_key_id: str = None,
        type: str = None,
        partition: str = None,
        timestamp: int = None,
        path: str = None,
        table_name: str = None,
        project_name: str = None,
    ):
        self.bucket_name = bucket_name
        self.access_key_id = access_key_id
        self.type = type
        self.partition = partition
        self.timestamp = timestamp
        self.path = path
        self.table_name = table_name
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_name is not None:
            result['bucketName'] = self.bucket_name
        if self.access_key_id is not None:
            result['accessKeyId'] = self.access_key_id
        if self.type is not None:
            result['type'] = self.type
        if self.partition is not None:
            result['partition'] = self.partition
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.path is not None:
            result['path'] = self.path
        if self.table_name is not None:
            result['tableName'] = self.table_name
        if self.project_name is not None:
            result['projectName'] = self.project_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bucketName') is not None:
            self.bucket_name = m.get('bucketName')
        if m.get('accessKeyId') is not None:
            self.access_key_id = m.get('accessKeyId')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('partition') is not None:
            self.partition = m.get('partition')
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('path') is not None:
            self.path = m.get('path')
        if m.get('tableName') is not None:
            self.table_name = m.get('tableName')
        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')
        return self


class ListDataSourceResponseBodyResult(TeaModel):
    def __init__(
        self,
        gmt_modified: str = None,
        gmt_create: str = None,
        table_name: str = None,
        meta: ListDataSourceResponseBodyResultMeta = None,
    ):
        self.gmt_modified = gmt_modified
        self.gmt_create = gmt_create
        self.table_name = table_name
        self.meta = meta

    def validate(self):
        if self.meta:
            self.meta.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.table_name is not None:
            result['tableName'] = self.table_name
        if self.meta is not None:
            result['meta'] = self.meta.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('tableName') is not None:
            self.table_name = m.get('tableName')
        if m.get('meta') is not None:
            temp_model = ListDataSourceResponseBodyResultMeta()
            self.meta = temp_model.from_map(m['meta'])
        return self


class ListDataSourceResponseBody(TeaModel):
    def __init__(
        self,
        result: List[ListDataSourceResponseBodyResult] = None,
        code: str = None,
        request_id: str = None,
        message: str = None,
    ):
        self.result = result
        self.code = code
        self.request_id = request_id
        self.message = message

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        if self.code is not None:
            result['code'] = self.code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListDataSourceResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class ListDataSourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDataSourceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListDataSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListExperimentsResponseBodyResult(TeaModel):
    def __init__(
        self,
        base: bool = None,
        online_time: str = None,
        offline_time: str = None,
        description: str = None,
        status: str = None,
        name: str = None,
        buckets: List[str] = None,
        experiment_id: str = None,
    ):
        self.base = base
        self.online_time = online_time
        self.offline_time = offline_time
        self.description = description
        self.status = status
        self.name = name
        self.buckets = buckets
        self.experiment_id = experiment_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base is not None:
            result['base'] = self.base
        if self.online_time is not None:
            result['onlineTime'] = self.online_time
        if self.offline_time is not None:
            result['offlineTime'] = self.offline_time
        if self.description is not None:
            result['description'] = self.description
        if self.status is not None:
            result['status'] = self.status
        if self.name is not None:
            result['name'] = self.name
        if self.buckets is not None:
            result['buckets'] = self.buckets
        if self.experiment_id is not None:
            result['experimentId'] = self.experiment_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('base') is not None:
            self.base = m.get('base')
        if m.get('onlineTime') is not None:
            self.online_time = m.get('onlineTime')
        if m.get('offlineTime') is not None:
            self.offline_time = m.get('offlineTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('buckets') is not None:
            self.buckets = m.get('buckets')
        if m.get('experimentId') is not None:
            self.experiment_id = m.get('experimentId')
        return self


class ListExperimentsResponseBody(TeaModel):
    def __init__(
        self,
        result: List[ListExperimentsResponseBodyResult] = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListExperimentsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListExperimentsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListExperimentsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListExperimentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFilteringAlgorithmsRequest(TeaModel):
    def __init__(
        self,
        status: str = None,
        algorithm_id: str = None,
        page: int = None,
        size: int = None,
    ):
        self.status = status
        self.algorithm_id = algorithm_id
        self.page = page
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['status'] = self.status
        if self.algorithm_id is not None:
            result['algorithmId'] = self.algorithm_id
        if self.page is not None:
            result['page'] = self.page
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('algorithmId') is not None:
            self.algorithm_id = m.get('algorithmId')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class ListFilteringAlgorithmsResponseBodyResultMetaExtInfo(TeaModel):
    def __init__(
        self,
        kv_separator: str = None,
        item_separator: str = None,
    ):
        self.kv_separator = kv_separator
        self.item_separator = item_separator

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.kv_separator is not None:
            result['kvSeparator'] = self.kv_separator
        if self.item_separator is not None:
            result['itemSeparator'] = self.item_separator
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('kvSeparator') is not None:
            self.kv_separator = m.get('kvSeparator')
        if m.get('itemSeparator') is not None:
            self.item_separator = m.get('itemSeparator')
        return self


class ListFilteringAlgorithmsResponseBodyResultMetaThreshold(TeaModel):
    def __init__(
        self,
        source_data_size_threshold: int = None,
        source_data_record_threshold: int = None,
        index_size_threshold: int = None,
        index_loss_threshold: int = None,
    ):
        self.source_data_size_threshold = source_data_size_threshold
        self.source_data_record_threshold = source_data_record_threshold
        self.index_size_threshold = index_size_threshold
        self.index_loss_threshold = index_loss_threshold

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_data_size_threshold is not None:
            result['sourceDataSizeThreshold'] = self.source_data_size_threshold
        if self.source_data_record_threshold is not None:
            result['sourceDataRecordThreshold'] = self.source_data_record_threshold
        if self.index_size_threshold is not None:
            result['indexSizeThreshold'] = self.index_size_threshold
        if self.index_loss_threshold is not None:
            result['indexLossThreshold'] = self.index_loss_threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sourceDataSizeThreshold') is not None:
            self.source_data_size_threshold = m.get('sourceDataSizeThreshold')
        if m.get('sourceDataRecordThreshold') is not None:
            self.source_data_record_threshold = m.get('sourceDataRecordThreshold')
        if m.get('indexSizeThreshold') is not None:
            self.index_size_threshold = m.get('indexSizeThreshold')
        if m.get('indexLossThreshold') is not None:
            self.index_loss_threshold = m.get('indexLossThreshold')
        return self


class ListFilteringAlgorithmsResponseBodyResultMeta(TeaModel):
    def __init__(
        self,
        task_id: str = None,
        meta_type: str = None,
        type: str = None,
        ext_info: ListFilteringAlgorithmsResponseBodyResultMetaExtInfo = None,
        category: str = None,
        threshold: ListFilteringAlgorithmsResponseBodyResultMetaThreshold = None,
        table_name: str = None,
        cluster_id: str = None,
        cron: str = None,
        description: str = None,
        project_name: str = None,
        algorithm_name: str = None,
        cron_enabled: bool = None,
    ):
        self.task_id = task_id
        self.meta_type = meta_type
        self.type = type
        self.ext_info = ext_info
        self.category = category
        self.threshold = threshold
        self.table_name = table_name
        self.cluster_id = cluster_id
        self.cron = cron
        self.description = description
        self.project_name = project_name
        self.algorithm_name = algorithm_name
        self.cron_enabled = cron_enabled

    def validate(self):
        if self.ext_info:
            self.ext_info.validate()
        if self.threshold:
            self.threshold.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['taskId'] = self.task_id
        if self.meta_type is not None:
            result['metaType'] = self.meta_type
        if self.type is not None:
            result['type'] = self.type
        if self.ext_info is not None:
            result['extInfo'] = self.ext_info.to_map()
        if self.category is not None:
            result['category'] = self.category
        if self.threshold is not None:
            result['threshold'] = self.threshold.to_map()
        if self.table_name is not None:
            result['tableName'] = self.table_name
        if self.cluster_id is not None:
            result['clusterId'] = self.cluster_id
        if self.cron is not None:
            result['cron'] = self.cron
        if self.description is not None:
            result['description'] = self.description
        if self.project_name is not None:
            result['projectName'] = self.project_name
        if self.algorithm_name is not None:
            result['algorithmName'] = self.algorithm_name
        if self.cron_enabled is not None:
            result['cronEnabled'] = self.cron_enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        if m.get('metaType') is not None:
            self.meta_type = m.get('metaType')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('extInfo') is not None:
            temp_model = ListFilteringAlgorithmsResponseBodyResultMetaExtInfo()
            self.ext_info = temp_model.from_map(m['extInfo'])
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('threshold') is not None:
            temp_model = ListFilteringAlgorithmsResponseBodyResultMetaThreshold()
            self.threshold = temp_model.from_map(m['threshold'])
        if m.get('tableName') is not None:
            self.table_name = m.get('tableName')
        if m.get('clusterId') is not None:
            self.cluster_id = m.get('clusterId')
        if m.get('cron') is not None:
            self.cron = m.get('cron')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')
        if m.get('algorithmName') is not None:
            self.algorithm_name = m.get('algorithmName')
        if m.get('cronEnabled') is not None:
            self.cron_enabled = m.get('cronEnabled')
        return self


class ListFilteringAlgorithmsResponseBodyResult(TeaModel):
    def __init__(
        self,
        gmt_modified: str = None,
        status: str = None,
        gmt_create: str = None,
        algorithm_id: str = None,
        meta: ListFilteringAlgorithmsResponseBodyResultMeta = None,
    ):
        self.gmt_modified = gmt_modified
        self.status = status
        self.gmt_create = gmt_create
        self.algorithm_id = algorithm_id
        self.meta = meta

    def validate(self):
        if self.meta:
            self.meta.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.status is not None:
            result['status'] = self.status
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.algorithm_id is not None:
            result['algorithmId'] = self.algorithm_id
        if self.meta is not None:
            result['meta'] = self.meta.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('algorithmId') is not None:
            self.algorithm_id = m.get('algorithmId')
        if m.get('meta') is not None:
            temp_model = ListFilteringAlgorithmsResponseBodyResultMeta()
            self.meta = temp_model.from_map(m['meta'])
        return self


class ListFilteringAlgorithmsResponseBodyHeaders(TeaModel):
    def __init__(
        self,
        x_total_count: int = None,
    ):
        self.x_total_count = x_total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.x_total_count is not None:
            result['X-Total-Count'] = self.x_total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X-Total-Count') is not None:
            self.x_total_count = m.get('X-Total-Count')
        return self


class ListFilteringAlgorithmsResponseBody(TeaModel):
    def __init__(
        self,
        result: List[ListFilteringAlgorithmsResponseBodyResult] = None,
        headers: ListFilteringAlgorithmsResponseBodyHeaders = None,
        request_id: str = None,
    ):
        self.result = result
        self.headers = headers
        self.request_id = request_id

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()
        if self.headers:
            self.headers.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        if self.headers is not None:
            result['headers'] = self.headers.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListFilteringAlgorithmsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('headers') is not None:
            temp_model = ListFilteringAlgorithmsResponseBodyHeaders()
            self.headers = temp_model.from_map(m['headers'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListFilteringAlgorithmsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListFilteringAlgorithmsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListFilteringAlgorithmsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListIndexVersionsResponseBodyResult(TeaModel):
    def __init__(
        self,
        code: str = None,
        switched_time: str = None,
        rollback_enabled: bool = None,
        message: str = None,
        flow_type: str = None,
        cost_seconds: int = None,
        built_time: str = None,
        version_id: str = None,
        size: int = None,
        status: str = None,
        progress: int = None,
    ):
        self.code = code
        self.switched_time = switched_time
        self.rollback_enabled = rollback_enabled
        self.message = message
        self.flow_type = flow_type
        self.cost_seconds = cost_seconds
        self.built_time = built_time
        self.version_id = version_id
        self.size = size
        self.status = status
        self.progress = progress

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.switched_time is not None:
            result['switchedTime'] = self.switched_time
        if self.rollback_enabled is not None:
            result['rollbackEnabled'] = self.rollback_enabled
        if self.message is not None:
            result['message'] = self.message
        if self.flow_type is not None:
            result['flowType'] = self.flow_type
        if self.cost_seconds is not None:
            result['costSeconds'] = self.cost_seconds
        if self.built_time is not None:
            result['builtTime'] = self.built_time
        if self.version_id is not None:
            result['versionId'] = self.version_id
        if self.size is not None:
            result['size'] = self.size
        if self.status is not None:
            result['status'] = self.status
        if self.progress is not None:
            result['progress'] = self.progress
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('switchedTime') is not None:
            self.switched_time = m.get('switchedTime')
        if m.get('rollbackEnabled') is not None:
            self.rollback_enabled = m.get('rollbackEnabled')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('flowType') is not None:
            self.flow_type = m.get('flowType')
        if m.get('costSeconds') is not None:
            self.cost_seconds = m.get('costSeconds')
        if m.get('builtTime') is not None:
            self.built_time = m.get('builtTime')
        if m.get('versionId') is not None:
            self.version_id = m.get('versionId')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('progress') is not None:
            self.progress = m.get('progress')
        return self


class ListIndexVersionsResponseBody(TeaModel):
    def __init__(
        self,
        result: List[ListIndexVersionsResponseBodyResult] = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListIndexVersionsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListIndexVersionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListIndexVersionsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListIndexVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstanceRequest(TeaModel):
    def __init__(
        self,
        page: int = None,
        size: int = None,
        status: str = None,
        name: str = None,
        expired_time: str = None,
        instance_id: str = None,
    ):
        self.page = page
        self.size = size
        self.status = status
        self.name = name
        self.expired_time = expired_time
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page is not None:
            result['page'] = self.page
        if self.size is not None:
            result['size'] = self.size
        if self.status is not None:
            result['status'] = self.status
        if self.name is not None:
            result['name'] = self.name
        if self.expired_time is not None:
            result['expiredTime'] = self.expired_time
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('expiredTime') is not None:
            self.expired_time = m.get('expiredTime')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        return self


class ListInstanceResponseBodyResult(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        type: str = None,
        lock_mode: str = None,
        expired_time: str = None,
        status: str = None,
        gmt_create: str = None,
        charge_type: str = None,
        industry: str = None,
        commodity_code: str = None,
        gmt_modified: str = None,
        data_set_version: str = None,
        name: str = None,
        instance_id: str = None,
    ):
        self.region_id = region_id
        self.type = type
        self.lock_mode = lock_mode
        self.expired_time = expired_time
        self.status = status
        self.gmt_create = gmt_create
        self.charge_type = charge_type
        self.industry = industry
        self.commodity_code = commodity_code
        self.gmt_modified = gmt_modified
        self.data_set_version = data_set_version
        self.name = name
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.type is not None:
            result['type'] = self.type
        if self.lock_mode is not None:
            result['lockMode'] = self.lock_mode
        if self.expired_time is not None:
            result['expiredTime'] = self.expired_time
        if self.status is not None:
            result['status'] = self.status
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.charge_type is not None:
            result['chargeType'] = self.charge_type
        if self.industry is not None:
            result['industry'] = self.industry
        if self.commodity_code is not None:
            result['commodityCode'] = self.commodity_code
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.data_set_version is not None:
            result['dataSetVersion'] = self.data_set_version
        if self.name is not None:
            result['name'] = self.name
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('lockMode') is not None:
            self.lock_mode = m.get('lockMode')
        if m.get('expiredTime') is not None:
            self.expired_time = m.get('expiredTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('chargeType') is not None:
            self.charge_type = m.get('chargeType')
        if m.get('industry') is not None:
            self.industry = m.get('industry')
        if m.get('commodityCode') is not None:
            self.commodity_code = m.get('commodityCode')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('dataSetVersion') is not None:
            self.data_set_version = m.get('dataSetVersion')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        return self


class ListInstanceResponseBody(TeaModel):
    def __init__(
        self,
        result: List[ListInstanceResponseBodyResult] = None,
        code: str = None,
        request_id: str = None,
        message: str = None,
    ):
        self.result = result
        self.code = code
        self.request_id = request_id
        self.message = message

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        if self.code is not None:
            result['code'] = self.code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListInstanceResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class ListInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstanceTaskResponseBodyResultSubProgressInfos(TeaModel):
    def __init__(
        self,
        type: str = None,
        detail: str = None,
        total_num: int = None,
        finished_num: int = None,
        progress: int = None,
    ):
        self.type = type
        self.detail = detail
        self.total_num = total_num
        self.finished_num = finished_num
        self.progress = progress

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        if self.detail is not None:
            result['detail'] = self.detail
        if self.total_num is not None:
            result['totalNum'] = self.total_num
        if self.finished_num is not None:
            result['finishedNum'] = self.finished_num
        if self.progress is not None:
            result['progress'] = self.progress
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('detail') is not None:
            self.detail = m.get('detail')
        if m.get('totalNum') is not None:
            self.total_num = m.get('totalNum')
        if m.get('finishedNum') is not None:
            self.finished_num = m.get('finishedNum')
        if m.get('progress') is not None:
            self.progress = m.get('progress')
        return self


class ListInstanceTaskResponseBodyResult(TeaModel):
    def __init__(
        self,
        sub_progress_infos: List[ListInstanceTaskResponseBodyResultSubProgressInfos] = None,
        total_progress: int = None,
        name: str = None,
    ):
        self.sub_progress_infos = sub_progress_infos
        self.total_progress = total_progress
        self.name = name

    def validate(self):
        if self.sub_progress_infos:
            for k in self.sub_progress_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['subProgressInfos'] = []
        if self.sub_progress_infos is not None:
            for k in self.sub_progress_infos:
                result['subProgressInfos'].append(k.to_map() if k else None)
        if self.total_progress is not None:
            result['totalProgress'] = self.total_progress
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.sub_progress_infos = []
        if m.get('subProgressInfos') is not None:
            for k in m.get('subProgressInfos'):
                temp_model = ListInstanceTaskResponseBodyResultSubProgressInfos()
                self.sub_progress_infos.append(temp_model.from_map(k))
        if m.get('totalProgress') is not None:
            self.total_progress = m.get('totalProgress')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class ListInstanceTaskResponseBody(TeaModel):
    def __init__(
        self,
        result: List[ListInstanceTaskResponseBodyResult] = None,
        code: str = None,
        request_id: str = None,
        message: str = None,
    ):
        self.result = result
        self.code = code
        self.request_id = request_id
        self.message = message

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        if self.code is not None:
            result['code'] = self.code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListInstanceTaskResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class ListInstanceTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListInstanceTaskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListInstanceTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListItemsRequest(TeaModel):
    def __init__(
        self,
        page: int = None,
        size: int = None,
    ):
        self.page = page
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page is not None:
            result['page'] = self.page
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class ListItemsResponseBodyResultTotal(TeaModel):
    def __init__(
        self,
        scene_weight_item: int = None,
        total_count: int = None,
        query_count: int = None,
        scene_recommend_item: int = None,
        weight_item: int = None,
        instance_recommend_item: int = None,
    ):
        self.scene_weight_item = scene_weight_item
        self.total_count = total_count
        self.query_count = query_count
        self.scene_recommend_item = scene_recommend_item
        self.weight_item = weight_item
        self.instance_recommend_item = instance_recommend_item

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene_weight_item is not None:
            result['sceneWeightItem'] = self.scene_weight_item
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        if self.query_count is not None:
            result['queryCount'] = self.query_count
        if self.scene_recommend_item is not None:
            result['sceneRecommendItem'] = self.scene_recommend_item
        if self.weight_item is not None:
            result['weightItem'] = self.weight_item
        if self.instance_recommend_item is not None:
            result['instanceRecommendItem'] = self.instance_recommend_item
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sceneWeightItem') is not None:
            self.scene_weight_item = m.get('sceneWeightItem')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        if m.get('queryCount') is not None:
            self.query_count = m.get('queryCount')
        if m.get('sceneRecommendItem') is not None:
            self.scene_recommend_item = m.get('sceneRecommendItem')
        if m.get('weightItem') is not None:
            self.weight_item = m.get('weightItem')
        if m.get('instanceRecommendItem') is not None:
            self.instance_recommend_item = m.get('instanceRecommendItem')
        return self


class ListItemsResponseBodyResultDetail(TeaModel):
    def __init__(
        self,
        title: str = None,
        category_path: str = None,
        item_id: str = None,
        item_type: str = None,
        status: str = None,
        brand_id: str = None,
        shop_id: str = None,
        pub_time: str = None,
        channel: str = None,
        duration: str = None,
        author: str = None,
        expire_time: str = None,
    ):
        self.title = title
        self.category_path = category_path
        self.item_id = item_id
        self.item_type = item_type
        self.status = status
        self.brand_id = brand_id
        self.shop_id = shop_id
        self.pub_time = pub_time
        self.channel = channel
        self.duration = duration
        self.author = author
        self.expire_time = expire_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.title is not None:
            result['title'] = self.title
        if self.category_path is not None:
            result['categoryPath'] = self.category_path
        if self.item_id is not None:
            result['itemId'] = self.item_id
        if self.item_type is not None:
            result['itemType'] = self.item_type
        if self.status is not None:
            result['status'] = self.status
        if self.brand_id is not None:
            result['brandId'] = self.brand_id
        if self.shop_id is not None:
            result['shopId'] = self.shop_id
        if self.pub_time is not None:
            result['pubTime'] = self.pub_time
        if self.channel is not None:
            result['channel'] = self.channel
        if self.duration is not None:
            result['duration'] = self.duration
        if self.author is not None:
            result['author'] = self.author
        if self.expire_time is not None:
            result['expireTime'] = self.expire_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('title') is not None:
            self.title = m.get('title')
        if m.get('categoryPath') is not None:
            self.category_path = m.get('categoryPath')
        if m.get('itemId') is not None:
            self.item_id = m.get('itemId')
        if m.get('itemType') is not None:
            self.item_type = m.get('itemType')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('brandId') is not None:
            self.brand_id = m.get('brandId')
        if m.get('shopId') is not None:
            self.shop_id = m.get('shopId')
        if m.get('pubTime') is not None:
            self.pub_time = m.get('pubTime')
        if m.get('channel') is not None:
            self.channel = m.get('channel')
        if m.get('duration') is not None:
            self.duration = m.get('duration')
        if m.get('author') is not None:
            self.author = m.get('author')
        if m.get('expireTime') is not None:
            self.expire_time = m.get('expireTime')
        return self


class ListItemsResponseBodyResult(TeaModel):
    def __init__(
        self,
        total: ListItemsResponseBodyResultTotal = None,
        detail: List[ListItemsResponseBodyResultDetail] = None,
    ):
        self.total = total
        self.detail = detail

    def validate(self):
        if self.total:
            self.total.validate()
        if self.detail:
            for k in self.detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total is not None:
            result['total'] = self.total.to_map()
        result['detail'] = []
        if self.detail is not None:
            for k in self.detail:
                result['detail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('total') is not None:
            temp_model = ListItemsResponseBodyResultTotal()
            self.total = temp_model.from_map(m['total'])
        self.detail = []
        if m.get('detail') is not None:
            for k in m.get('detail'):
                temp_model = ListItemsResponseBodyResultDetail()
                self.detail.append(temp_model.from_map(k))
        return self


class ListItemsResponseBody(TeaModel):
    def __init__(
        self,
        result: ListItemsResponseBodyResult = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = ListItemsResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListItemsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListItemsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListItemsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListLogsRequest(TeaModel):
    def __init__(
        self,
        query_params: str = None,
        start_time: int = None,
        end_time: int = None,
        page: int = None,
        size: int = None,
    ):
        self.query_params = query_params
        self.start_time = start_time
        self.end_time = end_time
        self.page = page
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.query_params is not None:
            result['queryParams'] = self.query_params
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.page is not None:
            result['page'] = self.page
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('queryParams') is not None:
            self.query_params = m.get('queryParams')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class ListLogsResponseBodyHeaders(TeaModel):
    def __init__(
        self,
        x_total_count: int = None,
    ):
        self.x_total_count = x_total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.x_total_count is not None:
            result['X-Total-Count'] = self.x_total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X-Total-Count') is not None:
            self.x_total_count = m.get('X-Total-Count')
        return self


class ListLogsResponseBody(TeaModel):
    def __init__(
        self,
        result: List[Dict[str, Any]] = None,
        headers: ListLogsResponseBodyHeaders = None,
        code: str = None,
        request_id: str = None,
        message: str = None,
    ):
        self.result = result
        self.headers = headers
        self.code = code
        self.request_id = request_id
        self.message = message

    def validate(self):
        if self.headers:
            self.headers.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result
        if self.headers is not None:
            result['headers'] = self.headers.to_map()
        if self.code is not None:
            result['code'] = self.code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('headers') is not None:
            temp_model = ListLogsResponseBodyHeaders()
            self.headers = temp_model.from_map(m['headers'])
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class ListLogsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListLogsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMixCategoriesResponseBodyResult(TeaModel):
    def __init__(
        self,
        categories: List[int] = None,
    ):
        self.categories = categories

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.categories is not None:
            result['categories'] = self.categories
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('categories') is not None:
            self.categories = m.get('categories')
        return self


class ListMixCategoriesResponseBody(TeaModel):
    def __init__(
        self,
        result: List[ListMixCategoriesResponseBodyResult] = None,
        code: str = None,
        request_id: str = None,
        message: str = None,
    ):
        self.result = result
        self.code = code
        self.request_id = request_id
        self.message = message

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        if self.code is not None:
            result['code'] = self.code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListMixCategoriesResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class ListMixCategoriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListMixCategoriesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListMixCategoriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRankingModelsRequest(TeaModel):
    def __init__(
        self,
        ranking_model_id: str = None,
        page: int = None,
        size: int = None,
    ):
        self.ranking_model_id = ranking_model_id
        self.page = page
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ranking_model_id is not None:
            result['rankingModelId'] = self.ranking_model_id
        if self.page is not None:
            result['page'] = self.page
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('rankingModelId') is not None:
            self.ranking_model_id = m.get('rankingModelId')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class ListRankingModelsResponseBodyResult(TeaModel):
    def __init__(
        self,
        ranking_model_id: str = None,
        gmt_modified: str = None,
        gmt_create: str = None,
        meta: Dict[str, Any] = None,
    ):
        self.ranking_model_id = ranking_model_id
        self.gmt_modified = gmt_modified
        self.gmt_create = gmt_create
        self.meta = meta

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ranking_model_id is not None:
            result['rankingModelId'] = self.ranking_model_id
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.meta is not None:
            result['meta'] = self.meta
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('rankingModelId') is not None:
            self.ranking_model_id = m.get('rankingModelId')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('meta') is not None:
            self.meta = m.get('meta')
        return self


class ListRankingModelsResponseBody(TeaModel):
    def __init__(
        self,
        result: List[ListRankingModelsResponseBodyResult] = None,
        code: str = None,
        request_id: str = None,
        message: str = None,
    ):
        self.result = result
        self.code = code
        self.request_id = request_id
        self.message = message

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        if self.code is not None:
            result['code'] = self.code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListRankingModelsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class ListRankingModelsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListRankingModelsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListRankingModelsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRuleConditionsResponseBodyResult(TeaModel):
    def __init__(
        self,
        select_type: str = None,
        select_value: str = None,
        selection_operation: str = None,
    ):
        self.select_type = select_type
        self.select_value = select_value
        self.selection_operation = selection_operation

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.select_type is not None:
            result['selectType'] = self.select_type
        if self.select_value is not None:
            result['selectValue'] = self.select_value
        if self.selection_operation is not None:
            result['selectionOperation'] = self.selection_operation
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('selectType') is not None:
            self.select_type = m.get('selectType')
        if m.get('selectValue') is not None:
            self.select_value = m.get('selectValue')
        if m.get('selectionOperation') is not None:
            self.selection_operation = m.get('selectionOperation')
        return self


class ListRuleConditionsResponseBody(TeaModel):
    def __init__(
        self,
        result: List[ListRuleConditionsResponseBodyResult] = None,
        code: str = None,
        request_id: str = None,
        message: str = None,
    ):
        self.result = result
        self.code = code
        self.request_id = request_id
        self.message = message

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        if self.code is not None:
            result['code'] = self.code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListRuleConditionsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class ListRuleConditionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListRuleConditionsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListRuleConditionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRulesRequest(TeaModel):
    def __init__(
        self,
        scene_id: str = None,
        rule_type: str = None,
        status: str = None,
        page: int = None,
        size: int = None,
        start_time: int = None,
        end_time: int = None,
    ):
        self.scene_id = scene_id
        self.rule_type = rule_type
        self.status = status
        self.page = page
        self.size = size
        self.start_time = start_time
        self.end_time = end_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene_id is not None:
            result['sceneId'] = self.scene_id
        if self.rule_type is not None:
            result['ruleType'] = self.rule_type
        if self.status is not None:
            result['status'] = self.status
        if self.page is not None:
            result['page'] = self.page
        if self.size is not None:
            result['size'] = self.size
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sceneId') is not None:
            self.scene_id = m.get('sceneId')
        if m.get('ruleType') is not None:
            self.rule_type = m.get('ruleType')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        return self


class ListRulesResponseBodyResult(TeaModel):
    def __init__(
        self,
        rule_id: str = None,
        gmt_modified: str = None,
        status: str = None,
        gmt_create: str = None,
    ):
        self.rule_id = rule_id
        self.gmt_modified = gmt_modified
        self.status = status
        self.gmt_create = gmt_create

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_id is not None:
            result['ruleId'] = self.rule_id
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.status is not None:
            result['status'] = self.status
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ruleId') is not None:
            self.rule_id = m.get('ruleId')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        return self


class ListRulesResponseBody(TeaModel):
    def __init__(
        self,
        result: List[ListRulesResponseBodyResult] = None,
        code: str = None,
        request_id: str = None,
        message: str = None,
    ):
        self.result = result
        self.code = code
        self.request_id = request_id
        self.message = message

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        if self.code is not None:
            result['code'] = self.code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListRulesResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class ListRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListRulesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRuleTasksRequest(TeaModel):
    def __init__(
        self,
        scene_id: str = None,
    ):
        self.scene_id = scene_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene_id is not None:
            result['sceneId'] = self.scene_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sceneId') is not None:
            self.scene_id = m.get('sceneId')
        return self


class ListRuleTasksResponseBodyResult(TeaModel):
    def __init__(
        self,
        finish_time: int = None,
        finish_rate: int = None,
    ):
        self.finish_time = finish_time
        self.finish_rate = finish_rate

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.finish_time is not None:
            result['finishTime'] = self.finish_time
        if self.finish_rate is not None:
            result['finishRate'] = self.finish_rate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('finishTime') is not None:
            self.finish_time = m.get('finishTime')
        if m.get('finishRate') is not None:
            self.finish_rate = m.get('finishRate')
        return self


class ListRuleTasksResponseBody(TeaModel):
    def __init__(
        self,
        result: ListRuleTasksResponseBodyResult = None,
        code: str = None,
        request_id: str = None,
        message: str = None,
    ):
        self.result = result
        self.code = code
        self.request_id = request_id
        self.message = message

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.code is not None:
            result['code'] = self.code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = ListRuleTasksResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class ListRuleTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListRuleTasksResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListRuleTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSceneItemsRequest(TeaModel):
    def __init__(
        self,
        operation_rule_id: str = None,
        selection_rule_id: str = None,
        page: int = None,
        size: int = None,
        preview_type: str = None,
        query_count: int = None,
    ):
        self.operation_rule_id = operation_rule_id
        self.selection_rule_id = selection_rule_id
        self.page = page
        self.size = size
        self.preview_type = preview_type
        self.query_count = query_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operation_rule_id is not None:
            result['operationRuleId'] = self.operation_rule_id
        if self.selection_rule_id is not None:
            result['selectionRuleId'] = self.selection_rule_id
        if self.page is not None:
            result['page'] = self.page
        if self.size is not None:
            result['size'] = self.size
        if self.preview_type is not None:
            result['previewType'] = self.preview_type
        if self.query_count is not None:
            result['queryCount'] = self.query_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('operationRuleId') is not None:
            self.operation_rule_id = m.get('operationRuleId')
        if m.get('selectionRuleId') is not None:
            self.selection_rule_id = m.get('selectionRuleId')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('previewType') is not None:
            self.preview_type = m.get('previewType')
        if m.get('queryCount') is not None:
            self.query_count = m.get('queryCount')
        return self


class ListSceneItemsResponseBodyResultTotal(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        scene_weight_item: int = None,
        scene_recommend_item: int = None,
        weight_item: int = None,
        instance_recommend_item: int = None,
    ):
        self.total_count = total_count
        self.scene_weight_item = scene_weight_item
        self.scene_recommend_item = scene_recommend_item
        self.weight_item = weight_item
        self.instance_recommend_item = instance_recommend_item

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        if self.scene_weight_item is not None:
            result['sceneWeightItem'] = self.scene_weight_item
        if self.scene_recommend_item is not None:
            result['sceneRecommendItem'] = self.scene_recommend_item
        if self.weight_item is not None:
            result['weightItem'] = self.weight_item
        if self.instance_recommend_item is not None:
            result['instanceRecommendItem'] = self.instance_recommend_item
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        if m.get('sceneWeightItem') is not None:
            self.scene_weight_item = m.get('sceneWeightItem')
        if m.get('sceneRecommendItem') is not None:
            self.scene_recommend_item = m.get('sceneRecommendItem')
        if m.get('weightItem') is not None:
            self.weight_item = m.get('weightItem')
        if m.get('instanceRecommendItem') is not None:
            self.instance_recommend_item = m.get('instanceRecommendItem')
        return self


class ListSceneItemsResponseBodyResultDetail(TeaModel):
    def __init__(
        self,
        title: str = None,
        category_path: str = None,
        item_id: str = None,
        item_type: str = None,
        status: str = None,
        brand_id: str = None,
        shop_id: str = None,
        pub_time: str = None,
        channel: str = None,
        duration: str = None,
        author: str = None,
        expire_time: str = None,
    ):
        self.title = title
        self.category_path = category_path
        self.item_id = item_id
        self.item_type = item_type
        self.status = status
        self.brand_id = brand_id
        self.shop_id = shop_id
        self.pub_time = pub_time
        self.channel = channel
        self.duration = duration
        self.author = author
        self.expire_time = expire_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.title is not None:
            result['title'] = self.title
        if self.category_path is not None:
            result['categoryPath'] = self.category_path
        if self.item_id is not None:
            result['itemId'] = self.item_id
        if self.item_type is not None:
            result['itemType'] = self.item_type
        if self.status is not None:
            result['status'] = self.status
        if self.brand_id is not None:
            result['brandId'] = self.brand_id
        if self.shop_id is not None:
            result['shopId'] = self.shop_id
        if self.pub_time is not None:
            result['pubTime'] = self.pub_time
        if self.channel is not None:
            result['channel'] = self.channel
        if self.duration is not None:
            result['duration'] = self.duration
        if self.author is not None:
            result['author'] = self.author
        if self.expire_time is not None:
            result['expireTime'] = self.expire_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('title') is not None:
            self.title = m.get('title')
        if m.get('categoryPath') is not None:
            self.category_path = m.get('categoryPath')
        if m.get('itemId') is not None:
            self.item_id = m.get('itemId')
        if m.get('itemType') is not None:
            self.item_type = m.get('itemType')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('brandId') is not None:
            self.brand_id = m.get('brandId')
        if m.get('shopId') is not None:
            self.shop_id = m.get('shopId')
        if m.get('pubTime') is not None:
            self.pub_time = m.get('pubTime')
        if m.get('channel') is not None:
            self.channel = m.get('channel')
        if m.get('duration') is not None:
            self.duration = m.get('duration')
        if m.get('author') is not None:
            self.author = m.get('author')
        if m.get('expireTime') is not None:
            self.expire_time = m.get('expireTime')
        return self


class ListSceneItemsResponseBodyResult(TeaModel):
    def __init__(
        self,
        total: ListSceneItemsResponseBodyResultTotal = None,
        detail: List[ListSceneItemsResponseBodyResultDetail] = None,
    ):
        self.total = total
        self.detail = detail

    def validate(self):
        if self.total:
            self.total.validate()
        if self.detail:
            for k in self.detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total is not None:
            result['total'] = self.total.to_map()
        result['detail'] = []
        if self.detail is not None:
            for k in self.detail:
                result['detail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('total') is not None:
            temp_model = ListSceneItemsResponseBodyResultTotal()
            self.total = temp_model.from_map(m['total'])
        self.detail = []
        if m.get('detail') is not None:
            for k in m.get('detail'):
                temp_model = ListSceneItemsResponseBodyResultDetail()
                self.detail.append(temp_model.from_map(k))
        return self


class ListSceneItemsResponseBody(TeaModel):
    def __init__(
        self,
        result: ListSceneItemsResponseBodyResult = None,
        code: str = None,
        request_id: str = None,
        message: str = None,
    ):
        self.result = result
        self.code = code
        self.request_id = request_id
        self.message = message

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.code is not None:
            result['code'] = self.code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = ListSceneItemsResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class ListSceneItemsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListSceneItemsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListSceneItemsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSceneParametersResponseBodyResult(TeaModel):
    def __init__(
        self,
        trace_id: List[str] = None,
        scene_id: List[str] = None,
    ):
        self.trace_id = trace_id
        self.scene_id = scene_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.trace_id is not None:
            result['traceId'] = self.trace_id
        if self.scene_id is not None:
            result['sceneId'] = self.scene_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        if m.get('sceneId') is not None:
            self.scene_id = m.get('sceneId')
        return self


class ListSceneParametersResponseBody(TeaModel):
    def __init__(
        self,
        result: ListSceneParametersResponseBodyResult = None,
        code: str = None,
        request_id: str = None,
        message: str = None,
    ):
        self.result = result
        self.code = code
        self.request_id = request_id
        self.message = message

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.code is not None:
            result['code'] = self.code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = ListSceneParametersResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class ListSceneParametersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListSceneParametersResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListSceneParametersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListScenesRequest(TeaModel):
    def __init__(
        self,
        status: str = None,
        scene_id: str = None,
        page: int = None,
        size: int = None,
    ):
        self.status = status
        self.scene_id = scene_id
        self.page = page
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['status'] = self.status
        if self.scene_id is not None:
            result['sceneId'] = self.scene_id
        if self.page is not None:
            result['page'] = self.page
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('sceneId') is not None:
            self.scene_id = m.get('sceneId')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class ListScenesResponseBodyResult(TeaModel):
    def __init__(
        self,
        scene_id: str = None,
        gmt_modified: str = None,
        status: str = None,
        gmt_create: str = None,
    ):
        self.scene_id = scene_id
        self.gmt_modified = gmt_modified
        self.status = status
        self.gmt_create = gmt_create

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene_id is not None:
            result['sceneId'] = self.scene_id
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.status is not None:
            result['status'] = self.status
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sceneId') is not None:
            self.scene_id = m.get('sceneId')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        return self


class ListScenesResponseBody(TeaModel):
    def __init__(
        self,
        result: List[ListScenesResponseBodyResult] = None,
        code: str = None,
        request_id: str = None,
        message: str = None,
    ):
        self.result = result
        self.code = code
        self.request_id = request_id
        self.message = message

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        if self.code is not None:
            result['code'] = self.code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListScenesResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class ListScenesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListScenesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListScenesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUmengAppkeysResponseBodyResult(TeaModel):
    def __init__(
        self,
        appkey: str = None,
        platform: str = None,
        name: str = None,
    ):
        self.appkey = appkey
        self.platform = platform
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.appkey is not None:
            result['appkey'] = self.appkey
        if self.platform is not None:
            result['platform'] = self.platform
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appkey') is not None:
            self.appkey = m.get('appkey')
        if m.get('platform') is not None:
            self.platform = m.get('platform')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class ListUmengAppkeysResponseBody(TeaModel):
    def __init__(
        self,
        result: List[ListUmengAppkeysResponseBodyResult] = None,
        code: str = None,
        request_id: str = None,
        message: str = None,
    ):
        self.result = result
        self.code = code
        self.request_id = request_id
        self.message = message

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        if self.code is not None:
            result['code'] = self.code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListUmengAppkeysResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class ListUmengAppkeysResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListUmengAppkeysResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListUmengAppkeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserClustersResponseBodyResultMeta(TeaModel):
    def __init__(
        self,
        meta_type: str = None,
        description: str = None,
    ):
        self.meta_type = meta_type
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.meta_type is not None:
            result['metaType'] = self.meta_type
        if self.description is not None:
            result['description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('metaType') is not None:
            self.meta_type = m.get('metaType')
        if m.get('description') is not None:
            self.description = m.get('description')
        return self


class ListUserClustersResponseBodyResult(TeaModel):
    def __init__(
        self,
        gmt_modified: str = None,
        status: str = None,
        gmt_create: str = None,
        name: str = None,
        meta: ListUserClustersResponseBodyResultMeta = None,
    ):
        self.gmt_modified = gmt_modified
        self.status = status
        self.gmt_create = gmt_create
        self.name = name
        self.meta = meta

    def validate(self):
        if self.meta:
            self.meta.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.status is not None:
            result['status'] = self.status
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.name is not None:
            result['name'] = self.name
        if self.meta is not None:
            result['meta'] = self.meta.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('meta') is not None:
            temp_model = ListUserClustersResponseBodyResultMeta()
            self.meta = temp_model.from_map(m['meta'])
        return self


class ListUserClustersResponseBodyHeaders(TeaModel):
    def __init__(
        self,
        x_total_count: int = None,
    ):
        self.x_total_count = x_total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.x_total_count is not None:
            result['X-Total-Count'] = self.x_total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X-Total-Count') is not None:
            self.x_total_count = m.get('X-Total-Count')
        return self


class ListUserClustersResponseBody(TeaModel):
    def __init__(
        self,
        result: List[ListUserClustersResponseBodyResult] = None,
        headers: ListUserClustersResponseBodyHeaders = None,
        request_id: str = None,
    ):
        self.result = result
        self.headers = headers
        self.request_id = request_id

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()
        if self.headers:
            self.headers.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        if self.headers is not None:
            result['headers'] = self.headers.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListUserClustersResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('headers') is not None:
            temp_model = ListUserClustersResponseBodyHeaders()
            self.headers = temp_model.from_map(m['headers'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListUserClustersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListUserClustersResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListUserClustersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDataSourceResponseBodyResultMeta(TeaModel):
    def __init__(
        self,
        bucket_name: str = None,
        access_key_id: str = None,
        type: str = None,
        partition: str = None,
        timestamp: int = None,
        path: str = None,
        table_name: str = None,
        project_name: str = None,
    ):
        self.bucket_name = bucket_name
        self.access_key_id = access_key_id
        self.type = type
        self.partition = partition
        self.timestamp = timestamp
        self.path = path
        self.table_name = table_name
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_name is not None:
            result['bucketName'] = self.bucket_name
        if self.access_key_id is not None:
            result['accessKeyId'] = self.access_key_id
        if self.type is not None:
            result['type'] = self.type
        if self.partition is not None:
            result['partition'] = self.partition
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.path is not None:
            result['path'] = self.path
        if self.table_name is not None:
            result['tableName'] = self.table_name
        if self.project_name is not None:
            result['projectName'] = self.project_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bucketName') is not None:
            self.bucket_name = m.get('bucketName')
        if m.get('accessKeyId') is not None:
            self.access_key_id = m.get('accessKeyId')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('partition') is not None:
            self.partition = m.get('partition')
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('path') is not None:
            self.path = m.get('path')
        if m.get('tableName') is not None:
            self.table_name = m.get('tableName')
        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')
        return self


class ModifyDataSourceResponseBodyResult(TeaModel):
    def __init__(
        self,
        gmt_modified: str = None,
        gmt_create: str = None,
        table_name: str = None,
        meta: ModifyDataSourceResponseBodyResultMeta = None,
    ):
        self.gmt_modified = gmt_modified
        self.gmt_create = gmt_create
        self.table_name = table_name
        self.meta = meta

    def validate(self):
        if self.meta:
            self.meta.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.table_name is not None:
            result['tableName'] = self.table_name
        if self.meta is not None:
            result['meta'] = self.meta.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('tableName') is not None:
            self.table_name = m.get('tableName')
        if m.get('meta') is not None:
            temp_model = ModifyDataSourceResponseBodyResultMeta()
            self.meta = temp_model.from_map(m['meta'])
        return self


class ModifyDataSourceResponseBody(TeaModel):
    def __init__(
        self,
        result: ModifyDataSourceResponseBodyResult = None,
        code: str = None,
        request_id: str = None,
        message: str = None,
    ):
        self.result = result
        self.code = code
        self.request_id = request_id
        self.message = message

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.code is not None:
            result['code'] = self.code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = ModifyDataSourceResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class ModifyDataSourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyDataSourceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyDataSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyFilteringAlgorithmMetaResponseBodyResultMetaExtInfo(TeaModel):
    def __init__(
        self,
        kv_separator: str = None,
        item_separator: str = None,
    ):
        self.kv_separator = kv_separator
        self.item_separator = item_separator

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.kv_separator is not None:
            result['kvSeparator'] = self.kv_separator
        if self.item_separator is not None:
            result['itemSeparator'] = self.item_separator
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('kvSeparator') is not None:
            self.kv_separator = m.get('kvSeparator')
        if m.get('itemSeparator') is not None:
            self.item_separator = m.get('itemSeparator')
        return self


class ModifyFilteringAlgorithmMetaResponseBodyResultMetaThreshold(TeaModel):
    def __init__(
        self,
        source_data_size_threshold: int = None,
        source_data_record_threshold: int = None,
        index_size_threshold: int = None,
        index_loss_threshold: int = None,
    ):
        self.source_data_size_threshold = source_data_size_threshold
        self.source_data_record_threshold = source_data_record_threshold
        self.index_size_threshold = index_size_threshold
        self.index_loss_threshold = index_loss_threshold

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_data_size_threshold is not None:
            result['sourceDataSizeThreshold'] = self.source_data_size_threshold
        if self.source_data_record_threshold is not None:
            result['sourceDataRecordThreshold'] = self.source_data_record_threshold
        if self.index_size_threshold is not None:
            result['indexSizeThreshold'] = self.index_size_threshold
        if self.index_loss_threshold is not None:
            result['indexLossThreshold'] = self.index_loss_threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sourceDataSizeThreshold') is not None:
            self.source_data_size_threshold = m.get('sourceDataSizeThreshold')
        if m.get('sourceDataRecordThreshold') is not None:
            self.source_data_record_threshold = m.get('sourceDataRecordThreshold')
        if m.get('indexSizeThreshold') is not None:
            self.index_size_threshold = m.get('indexSizeThreshold')
        if m.get('indexLossThreshold') is not None:
            self.index_loss_threshold = m.get('indexLossThreshold')
        return self


class ModifyFilteringAlgorithmMetaResponseBodyResultMeta(TeaModel):
    def __init__(
        self,
        task_id: str = None,
        meta_type: str = None,
        type: str = None,
        ext_info: ModifyFilteringAlgorithmMetaResponseBodyResultMetaExtInfo = None,
        category: str = None,
        threshold: ModifyFilteringAlgorithmMetaResponseBodyResultMetaThreshold = None,
        table_name: str = None,
        cluster_id: str = None,
        cron: str = None,
        description: str = None,
        project_name: str = None,
        algorithm_name: str = None,
        cron_enabled: bool = None,
    ):
        self.task_id = task_id
        self.meta_type = meta_type
        self.type = type
        self.ext_info = ext_info
        self.category = category
        self.threshold = threshold
        self.table_name = table_name
        self.cluster_id = cluster_id
        self.cron = cron
        self.description = description
        self.project_name = project_name
        self.algorithm_name = algorithm_name
        self.cron_enabled = cron_enabled

    def validate(self):
        if self.ext_info:
            self.ext_info.validate()
        if self.threshold:
            self.threshold.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['taskId'] = self.task_id
        if self.meta_type is not None:
            result['metaType'] = self.meta_type
        if self.type is not None:
            result['type'] = self.type
        if self.ext_info is not None:
            result['extInfo'] = self.ext_info.to_map()
        if self.category is not None:
            result['category'] = self.category
        if self.threshold is not None:
            result['threshold'] = self.threshold.to_map()
        if self.table_name is not None:
            result['tableName'] = self.table_name
        if self.cluster_id is not None:
            result['clusterId'] = self.cluster_id
        if self.cron is not None:
            result['cron'] = self.cron
        if self.description is not None:
            result['description'] = self.description
        if self.project_name is not None:
            result['projectName'] = self.project_name
        if self.algorithm_name is not None:
            result['algorithmName'] = self.algorithm_name
        if self.cron_enabled is not None:
            result['cronEnabled'] = self.cron_enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        if m.get('metaType') is not None:
            self.meta_type = m.get('metaType')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('extInfo') is not None:
            temp_model = ModifyFilteringAlgorithmMetaResponseBodyResultMetaExtInfo()
            self.ext_info = temp_model.from_map(m['extInfo'])
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('threshold') is not None:
            temp_model = ModifyFilteringAlgorithmMetaResponseBodyResultMetaThreshold()
            self.threshold = temp_model.from_map(m['threshold'])
        if m.get('tableName') is not None:
            self.table_name = m.get('tableName')
        if m.get('clusterId') is not None:
            self.cluster_id = m.get('clusterId')
        if m.get('cron') is not None:
            self.cron = m.get('cron')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')
        if m.get('algorithmName') is not None:
            self.algorithm_name = m.get('algorithmName')
        if m.get('cronEnabled') is not None:
            self.cron_enabled = m.get('cronEnabled')
        return self


class ModifyFilteringAlgorithmMetaResponseBodyResult(TeaModel):
    def __init__(
        self,
        gmt_modified: str = None,
        status: str = None,
        gmt_create: str = None,
        algorithm_id: str = None,
        meta: ModifyFilteringAlgorithmMetaResponseBodyResultMeta = None,
    ):
        self.gmt_modified = gmt_modified
        self.status = status
        self.gmt_create = gmt_create
        self.algorithm_id = algorithm_id
        self.meta = meta

    def validate(self):
        if self.meta:
            self.meta.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.status is not None:
            result['status'] = self.status
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.algorithm_id is not None:
            result['algorithmId'] = self.algorithm_id
        if self.meta is not None:
            result['meta'] = self.meta.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('algorithmId') is not None:
            self.algorithm_id = m.get('algorithmId')
        if m.get('meta') is not None:
            temp_model = ModifyFilteringAlgorithmMetaResponseBodyResultMeta()
            self.meta = temp_model.from_map(m['meta'])
        return self


class ModifyFilteringAlgorithmMetaResponseBody(TeaModel):
    def __init__(
        self,
        result: ModifyFilteringAlgorithmMetaResponseBodyResult = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = ModifyFilteringAlgorithmMetaResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ModifyFilteringAlgorithmMetaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyFilteringAlgorithmMetaResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyFilteringAlgorithmMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceResponseBodyResult(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        type: str = None,
        lock_mode: str = None,
        expired_time: str = None,
        status: str = None,
        gmt_create: str = None,
        charge_type: str = None,
        industry: str = None,
        commodity_code: str = None,
        gmt_modified: str = None,
        data_set_version: str = None,
        name: str = None,
        instance_id: str = None,
    ):
        self.region_id = region_id
        self.type = type
        self.lock_mode = lock_mode
        self.expired_time = expired_time
        self.status = status
        self.gmt_create = gmt_create
        self.charge_type = charge_type
        self.industry = industry
        self.commodity_code = commodity_code
        self.gmt_modified = gmt_modified
        self.data_set_version = data_set_version
        self.name = name
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.type is not None:
            result['type'] = self.type
        if self.lock_mode is not None:
            result['lockMode'] = self.lock_mode
        if self.expired_time is not None:
            result['expiredTime'] = self.expired_time
        if self.status is not None:
            result['status'] = self.status
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.charge_type is not None:
            result['chargeType'] = self.charge_type
        if self.industry is not None:
            result['industry'] = self.industry
        if self.commodity_code is not None:
            result['commodityCode'] = self.commodity_code
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.data_set_version is not None:
            result['dataSetVersion'] = self.data_set_version
        if self.name is not None:
            result['name'] = self.name
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('lockMode') is not None:
            self.lock_mode = m.get('lockMode')
        if m.get('expiredTime') is not None:
            self.expired_time = m.get('expiredTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('chargeType') is not None:
            self.charge_type = m.get('chargeType')
        if m.get('industry') is not None:
            self.industry = m.get('industry')
        if m.get('commodityCode') is not None:
            self.commodity_code = m.get('commodityCode')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('dataSetVersion') is not None:
            self.data_set_version = m.get('dataSetVersion')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        return self


class ModifyInstanceResponseBody(TeaModel):
    def __init__(
        self,
        result: ModifyInstanceResponseBodyResult = None,
        code: str = None,
        request_id: str = None,
        message: str = None,
    ):
        self.result = result
        self.code = code
        self.request_id = request_id
        self.message = message

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.code is not None:
            result['code'] = self.code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = ModifyInstanceResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class ModifyInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyItemsResponseBody(TeaModel):
    def __init__(
        self,
        result: bool = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ModifyItemsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyItemsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyItemsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyRankingModelResponseBodyResult(TeaModel):
    def __init__(
        self,
        ranking_model_id: str = None,
        gmt_modified: str = None,
        gmt_create: str = None,
        meta: Dict[str, Any] = None,
    ):
        self.ranking_model_id = ranking_model_id
        self.gmt_modified = gmt_modified
        self.gmt_create = gmt_create
        self.meta = meta

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ranking_model_id is not None:
            result['rankingModelId'] = self.ranking_model_id
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.meta is not None:
            result['meta'] = self.meta
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('rankingModelId') is not None:
            self.ranking_model_id = m.get('rankingModelId')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('meta') is not None:
            self.meta = m.get('meta')
        return self


class ModifyRankingModelResponseBody(TeaModel):
    def __init__(
        self,
        result: ModifyRankingModelResponseBodyResult = None,
        code: str = None,
        request_id: str = None,
        message: str = None,
    ):
        self.result = result
        self.code = code
        self.request_id = request_id
        self.message = message

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.code is not None:
            result['code'] = self.code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = ModifyRankingModelResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class ModifyRankingModelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyRankingModelResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyRankingModelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyRuleResponseBodyResult(TeaModel):
    def __init__(
        self,
        rule_id: str = None,
        rule_meta: Dict[str, Any] = None,
        gmt_modified: str = None,
        status: str = None,
        gmt_create: str = None,
    ):
        self.rule_id = rule_id
        self.rule_meta = rule_meta
        self.gmt_modified = gmt_modified
        self.status = status
        self.gmt_create = gmt_create

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_id is not None:
            result['ruleId'] = self.rule_id
        if self.rule_meta is not None:
            result['ruleMeta'] = self.rule_meta
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.status is not None:
            result['status'] = self.status
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ruleId') is not None:
            self.rule_id = m.get('ruleId')
        if m.get('ruleMeta') is not None:
            self.rule_meta = m.get('ruleMeta')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        return self


class ModifyRuleResponseBody(TeaModel):
    def __init__(
        self,
        result: ModifyRuleResponseBodyResult = None,
        code: str = None,
        request_id: str = None,
        message: str = None,
    ):
        self.result = result
        self.code = code
        self.request_id = request_id
        self.message = message

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.code is not None:
            result['code'] = self.code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = ModifyRuleResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class ModifyRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyRuleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifySceneResponseBodyResult(TeaModel):
    def __init__(
        self,
        scene_id: str = None,
        gmt_modified: str = None,
        status: str = None,
        gmt_create: str = None,
    ):
        self.scene_id = scene_id
        self.gmt_modified = gmt_modified
        self.status = status
        self.gmt_create = gmt_create

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene_id is not None:
            result['sceneId'] = self.scene_id
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.status is not None:
            result['status'] = self.status
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sceneId') is not None:
            self.scene_id = m.get('sceneId')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        return self


class ModifySceneResponseBody(TeaModel):
    def __init__(
        self,
        result: ModifySceneResponseBodyResult = None,
        code: str = None,
        request_id: str = None,
        message: str = None,
    ):
        self.result = result
        self.code = code
        self.request_id = request_id
        self.message = message

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.code is not None:
            result['code'] = self.code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = ModifySceneResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class ModifySceneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifySceneResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifySceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OfflineFilteringAlgorithmResponseBodyResultMetaExtInfo(TeaModel):
    def __init__(
        self,
        kv_separator: str = None,
        item_separator: str = None,
    ):
        self.kv_separator = kv_separator
        self.item_separator = item_separator

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.kv_separator is not None:
            result['kvSeparator'] = self.kv_separator
        if self.item_separator is not None:
            result['itemSeparator'] = self.item_separator
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('kvSeparator') is not None:
            self.kv_separator = m.get('kvSeparator')
        if m.get('itemSeparator') is not None:
            self.item_separator = m.get('itemSeparator')
        return self


class OfflineFilteringAlgorithmResponseBodyResultMetaThreshold(TeaModel):
    def __init__(
        self,
        source_data_size_threshold: int = None,
        source_data_record_threshold: int = None,
        index_size_threshold: int = None,
        index_loss_threshold: int = None,
    ):
        self.source_data_size_threshold = source_data_size_threshold
        self.source_data_record_threshold = source_data_record_threshold
        self.index_size_threshold = index_size_threshold
        self.index_loss_threshold = index_loss_threshold

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_data_size_threshold is not None:
            result['sourceDataSizeThreshold'] = self.source_data_size_threshold
        if self.source_data_record_threshold is not None:
            result['sourceDataRecordThreshold'] = self.source_data_record_threshold
        if self.index_size_threshold is not None:
            result['indexSizeThreshold'] = self.index_size_threshold
        if self.index_loss_threshold is not None:
            result['indexLossThreshold'] = self.index_loss_threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sourceDataSizeThreshold') is not None:
            self.source_data_size_threshold = m.get('sourceDataSizeThreshold')
        if m.get('sourceDataRecordThreshold') is not None:
            self.source_data_record_threshold = m.get('sourceDataRecordThreshold')
        if m.get('indexSizeThreshold') is not None:
            self.index_size_threshold = m.get('indexSizeThreshold')
        if m.get('indexLossThreshold') is not None:
            self.index_loss_threshold = m.get('indexLossThreshold')
        return self


class OfflineFilteringAlgorithmResponseBodyResultMeta(TeaModel):
    def __init__(
        self,
        task_id: str = None,
        meta_type: str = None,
        type: str = None,
        ext_info: OfflineFilteringAlgorithmResponseBodyResultMetaExtInfo = None,
        category: str = None,
        threshold: OfflineFilteringAlgorithmResponseBodyResultMetaThreshold = None,
        table_name: str = None,
        cluster_id: str = None,
        cron: str = None,
        description: str = None,
        project_name: str = None,
        algorithm_name: str = None,
        cron_enabled: bool = None,
    ):
        self.task_id = task_id
        self.meta_type = meta_type
        self.type = type
        self.ext_info = ext_info
        self.category = category
        self.threshold = threshold
        self.table_name = table_name
        self.cluster_id = cluster_id
        self.cron = cron
        self.description = description
        self.project_name = project_name
        self.algorithm_name = algorithm_name
        self.cron_enabled = cron_enabled

    def validate(self):
        if self.ext_info:
            self.ext_info.validate()
        if self.threshold:
            self.threshold.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['taskId'] = self.task_id
        if self.meta_type is not None:
            result['metaType'] = self.meta_type
        if self.type is not None:
            result['type'] = self.type
        if self.ext_info is not None:
            result['extInfo'] = self.ext_info.to_map()
        if self.category is not None:
            result['category'] = self.category
        if self.threshold is not None:
            result['threshold'] = self.threshold.to_map()
        if self.table_name is not None:
            result['tableName'] = self.table_name
        if self.cluster_id is not None:
            result['clusterId'] = self.cluster_id
        if self.cron is not None:
            result['cron'] = self.cron
        if self.description is not None:
            result['description'] = self.description
        if self.project_name is not None:
            result['projectName'] = self.project_name
        if self.algorithm_name is not None:
            result['algorithmName'] = self.algorithm_name
        if self.cron_enabled is not None:
            result['cronEnabled'] = self.cron_enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        if m.get('metaType') is not None:
            self.meta_type = m.get('metaType')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('extInfo') is not None:
            temp_model = OfflineFilteringAlgorithmResponseBodyResultMetaExtInfo()
            self.ext_info = temp_model.from_map(m['extInfo'])
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('threshold') is not None:
            temp_model = OfflineFilteringAlgorithmResponseBodyResultMetaThreshold()
            self.threshold = temp_model.from_map(m['threshold'])
        if m.get('tableName') is not None:
            self.table_name = m.get('tableName')
        if m.get('clusterId') is not None:
            self.cluster_id = m.get('clusterId')
        if m.get('cron') is not None:
            self.cron = m.get('cron')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')
        if m.get('algorithmName') is not None:
            self.algorithm_name = m.get('algorithmName')
        if m.get('cronEnabled') is not None:
            self.cron_enabled = m.get('cronEnabled')
        return self


class OfflineFilteringAlgorithmResponseBodyResult(TeaModel):
    def __init__(
        self,
        gmt_modified: str = None,
        status: str = None,
        gmt_create: str = None,
        algorithm_id: str = None,
        meta: OfflineFilteringAlgorithmResponseBodyResultMeta = None,
    ):
        self.gmt_modified = gmt_modified
        self.status = status
        self.gmt_create = gmt_create
        self.algorithm_id = algorithm_id
        self.meta = meta

    def validate(self):
        if self.meta:
            self.meta.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.status is not None:
            result['status'] = self.status
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.algorithm_id is not None:
            result['algorithmId'] = self.algorithm_id
        if self.meta is not None:
            result['meta'] = self.meta.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('algorithmId') is not None:
            self.algorithm_id = m.get('algorithmId')
        if m.get('meta') is not None:
            temp_model = OfflineFilteringAlgorithmResponseBodyResultMeta()
            self.meta = temp_model.from_map(m['meta'])
        return self


class OfflineFilteringAlgorithmResponseBody(TeaModel):
    def __init__(
        self,
        result: OfflineFilteringAlgorithmResponseBodyResult = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = OfflineFilteringAlgorithmResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class OfflineFilteringAlgorithmResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: OfflineFilteringAlgorithmResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = OfflineFilteringAlgorithmResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PublishRuleRequest(TeaModel):
    def __init__(
        self,
        rule_type: str = None,
        scene_id: str = None,
    ):
        self.rule_type = rule_type
        self.scene_id = scene_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_type is not None:
            result['ruleType'] = self.rule_type
        if self.scene_id is not None:
            result['sceneId'] = self.scene_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ruleType') is not None:
            self.rule_type = m.get('ruleType')
        if m.get('sceneId') is not None:
            self.scene_id = m.get('sceneId')
        return self


class PublishRuleResponseBodyResult(TeaModel):
    def __init__(
        self,
        rule_id: str = None,
    ):
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_id is not None:
            result['ruleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ruleId') is not None:
            self.rule_id = m.get('ruleId')
        return self


class PublishRuleResponseBody(TeaModel):
    def __init__(
        self,
        result: PublishRuleResponseBodyResult = None,
        code: str = None,
        request_id: str = None,
        message: str = None,
    ):
        self.result = result
        self.code = code
        self.request_id = request_id
        self.message = message

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.code is not None:
            result['code'] = self.code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = PublishRuleResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class PublishRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: PublishRuleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = PublishRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PushDocumentResponseBody(TeaModel):
    def __init__(
        self,
        result: bool = None,
        code: str = None,
        request_id: str = None,
        message: str = None,
    ):
        self.result = result
        self.code = code
        self.request_id = request_id
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result
        if self.code is not None:
            result['code'] = self.code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class PushDocumentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: PushDocumentResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = PushDocumentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PushInterventionResponseBody(TeaModel):
    def __init__(
        self,
        result: bool = None,
        code: str = None,
        request_id: str = None,
        message: str = None,
    ):
        self.result = result
        self.code = code
        self.request_id = request_id
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result
        if self.code is not None:
            result['code'] = self.code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class PushInterventionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: PushInterventionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = PushInterventionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDataMessageRequest(TeaModel):
    def __init__(
        self,
        start_time: int = None,
        end_time: int = None,
        cmd_type: str = None,
        item_id: str = None,
        item_type: str = None,
        user_id: str = None,
        user_type: str = None,
        page: int = None,
        size: int = None,
        trace_id: str = None,
        scene_id: str = None,
        bhv_type: str = None,
        message_source: str = None,
    ):
        self.start_time = start_time
        self.end_time = end_time
        self.cmd_type = cmd_type
        self.item_id = item_id
        self.item_type = item_type
        self.user_id = user_id
        self.user_type = user_type
        self.page = page
        self.size = size
        self.trace_id = trace_id
        self.scene_id = scene_id
        self.bhv_type = bhv_type
        self.message_source = message_source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.cmd_type is not None:
            result['cmdType'] = self.cmd_type
        if self.item_id is not None:
            result['itemId'] = self.item_id
        if self.item_type is not None:
            result['itemType'] = self.item_type
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.user_type is not None:
            result['userType'] = self.user_type
        if self.page is not None:
            result['page'] = self.page
        if self.size is not None:
            result['size'] = self.size
        if self.trace_id is not None:
            result['traceId'] = self.trace_id
        if self.scene_id is not None:
            result['sceneId'] = self.scene_id
        if self.bhv_type is not None:
            result['bhvType'] = self.bhv_type
        if self.message_source is not None:
            result['messageSource'] = self.message_source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('cmdType') is not None:
            self.cmd_type = m.get('cmdType')
        if m.get('itemId') is not None:
            self.item_id = m.get('itemId')
        if m.get('itemType') is not None:
            self.item_type = m.get('itemType')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('userType') is not None:
            self.user_type = m.get('userType')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        if m.get('sceneId') is not None:
            self.scene_id = m.get('sceneId')
        if m.get('bhvType') is not None:
            self.bhv_type = m.get('bhvType')
        if m.get('messageSource') is not None:
            self.message_source = m.get('messageSource')
        return self


class QueryDataMessageResponseBody(TeaModel):
    def __init__(
        self,
        result: Dict[str, Any] = None,
        code: str = None,
        request_id: str = None,
        message: str = None,
    ):
        self.result = result
        self.code = code
        self.request_id = request_id
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result
        if self.code is not None:
            result['code'] = self.code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class QueryDataMessageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryDataMessageResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryDataMessageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDataMessageStatisticsRequest(TeaModel):
    def __init__(
        self,
        start_time: int = None,
        end_time: int = None,
        cmd_type: str = None,
        item_id: str = None,
        item_type: str = None,
        user_id: str = None,
        user_type: str = None,
        trace_id: str = None,
        scene_id: str = None,
        bhv_type: str = None,
        message_source: str = None,
    ):
        self.start_time = start_time
        self.end_time = end_time
        self.cmd_type = cmd_type
        self.item_id = item_id
        self.item_type = item_type
        self.user_id = user_id
        self.user_type = user_type
        self.trace_id = trace_id
        self.scene_id = scene_id
        self.bhv_type = bhv_type
        self.message_source = message_source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.cmd_type is not None:
            result['cmdType'] = self.cmd_type
        if self.item_id is not None:
            result['itemId'] = self.item_id
        if self.item_type is not None:
            result['itemType'] = self.item_type
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.user_type is not None:
            result['userType'] = self.user_type
        if self.trace_id is not None:
            result['traceId'] = self.trace_id
        if self.scene_id is not None:
            result['sceneId'] = self.scene_id
        if self.bhv_type is not None:
            result['bhvType'] = self.bhv_type
        if self.message_source is not None:
            result['messageSource'] = self.message_source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('cmdType') is not None:
            self.cmd_type = m.get('cmdType')
        if m.get('itemId') is not None:
            self.item_id = m.get('itemId')
        if m.get('itemType') is not None:
            self.item_type = m.get('itemType')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('userType') is not None:
            self.user_type = m.get('userType')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        if m.get('sceneId') is not None:
            self.scene_id = m.get('sceneId')
        if m.get('bhvType') is not None:
            self.bhv_type = m.get('bhvType')
        if m.get('messageSource') is not None:
            self.message_source = m.get('messageSource')
        return self


class QueryDataMessageStatisticsResponseBody(TeaModel):
    def __init__(
        self,
        result: Dict[str, Any] = None,
        code: str = None,
        request_id: str = None,
        message: str = None,
    ):
        self.result = result
        self.code = code
        self.request_id = request_id
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result
        if self.code is not None:
            result['code'] = self.code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class QueryDataMessageStatisticsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryDataMessageStatisticsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryDataMessageStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryExceptionHistoryRequest(TeaModel):
    def __init__(
        self,
        start_time: int = None,
        end_time: int = None,
        type: str = None,
    ):
        self.start_time = start_time
        self.end_time = end_time
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class QueryExceptionHistoryResponseBody(TeaModel):
    def __init__(
        self,
        result: Dict[str, Any] = None,
        code: str = None,
        request_id: str = None,
        message: str = None,
    ):
        self.result = result
        self.code = code
        self.request_id = request_id
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result
        if self.code is not None:
            result['code'] = self.code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class QueryExceptionHistoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryExceptionHistoryResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryExceptionHistoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRawDataRequest(TeaModel):
    def __init__(
        self,
        item_id: str = None,
        item_type: str = None,
        user_id: str = None,
        user_type: str = None,
    ):
        self.item_id = item_id
        self.item_type = item_type
        self.user_id = user_id
        self.user_type = user_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.item_id is not None:
            result['itemId'] = self.item_id
        if self.item_type is not None:
            result['itemType'] = self.item_type
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.user_type is not None:
            result['userType'] = self.user_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('itemId') is not None:
            self.item_id = m.get('itemId')
        if m.get('itemType') is not None:
            self.item_type = m.get('itemType')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('userType') is not None:
            self.user_type = m.get('userType')
        return self


class QueryRawDataResponseBody(TeaModel):
    def __init__(
        self,
        result: Dict[str, Any] = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.result = result
        self.code = code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class QueryRawDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryRawDataResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryRawDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySingleAggregationReportResponseBody(TeaModel):
    def __init__(
        self,
        result: Dict[str, Any] = None,
        code: str = None,
        request_id: str = None,
        message: str = None,
    ):
        self.result = result
        self.code = code
        self.request_id = request_id
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result
        if self.code is not None:
            result['code'] = self.code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class QuerySingleAggregationReportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QuerySingleAggregationReportResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QuerySingleAggregationReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySingleReportRequest(TeaModel):
    def __init__(
        self,
        report_type: str = None,
    ):
        self.report_type = report_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.report_type is not None:
            result['reportType'] = self.report_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('reportType') is not None:
            self.report_type = m.get('reportType')
        return self


class QuerySingleReportResponseBody(TeaModel):
    def __init__(
        self,
        result: Dict[str, Any] = None,
        code: str = None,
        request_id: str = None,
        message: str = None,
    ):
        self.result = result
        self.code = code
        self.request_id = request_id
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result
        if self.code is not None:
            result['code'] = self.code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class QuerySingleReportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QuerySingleReportResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QuerySingleReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySyncReportAggregationRequest(TeaModel):
    def __init__(
        self,
        start_time: int = None,
        end_time: int = None,
    ):
        self.start_time = start_time
        self.end_time = end_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        return self


class QuerySyncReportAggregationResponseBody(TeaModel):
    def __init__(
        self,
        result: Dict[str, Any] = None,
        code: str = None,
        request_id: str = None,
        message: str = None,
    ):
        self.result = result
        self.code = code
        self.request_id = request_id
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result
        if self.code is not None:
            result['code'] = self.code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class QuerySyncReportAggregationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QuerySyncReportAggregationResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QuerySyncReportAggregationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RebuildIndexResponseBody(TeaModel):
    def __init__(
        self,
        result: str = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class RebuildIndexResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RebuildIndexResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RebuildIndexResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecommendRequest(TeaModel):
    def __init__(
        self,
        scene_id: str = None,
        user_id: str = None,
        ip: str = None,
        imei: str = None,
        return_count: int = None,
        items: str = None,
        service_type: str = None,
        user_info: str = None,
    ):
        self.scene_id = scene_id
        self.user_id = user_id
        self.ip = ip
        self.imei = imei
        self.return_count = return_count
        self.items = items
        self.service_type = service_type
        self.user_info = user_info

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene_id is not None:
            result['sceneId'] = self.scene_id
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.ip is not None:
            result['ip'] = self.ip
        if self.imei is not None:
            result['imei'] = self.imei
        if self.return_count is not None:
            result['returnCount'] = self.return_count
        if self.items is not None:
            result['items'] = self.items
        if self.service_type is not None:
            result['serviceType'] = self.service_type
        if self.user_info is not None:
            result['userInfo'] = self.user_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sceneId') is not None:
            self.scene_id = m.get('sceneId')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('imei') is not None:
            self.imei = m.get('imei')
        if m.get('returnCount') is not None:
            self.return_count = m.get('returnCount')
        if m.get('items') is not None:
            self.items = m.get('items')
        if m.get('serviceType') is not None:
            self.service_type = m.get('serviceType')
        if m.get('userInfo') is not None:
            self.user_info = m.get('userInfo')
        return self


class RecommendResponseBodyResult(TeaModel):
    def __init__(
        self,
        match_info: str = None,
        trace_id: str = None,
        position: int = None,
        item_id: str = None,
        item_type: str = None,
        trace_info: str = None,
        weight: float = None,
    ):
        self.match_info = match_info
        self.trace_id = trace_id
        self.position = position
        self.item_id = item_id
        self.item_type = item_type
        self.trace_info = trace_info
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_info is not None:
            result['matchInfo'] = self.match_info
        if self.trace_id is not None:
            result['traceId'] = self.trace_id
        if self.position is not None:
            result['position'] = self.position
        if self.item_id is not None:
            result['itemId'] = self.item_id
        if self.item_type is not None:
            result['itemType'] = self.item_type
        if self.trace_info is not None:
            result['traceInfo'] = self.trace_info
        if self.weight is not None:
            result['weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchInfo') is not None:
            self.match_info = m.get('matchInfo')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        if m.get('position') is not None:
            self.position = m.get('position')
        if m.get('itemId') is not None:
            self.item_id = m.get('itemId')
        if m.get('itemType') is not None:
            self.item_type = m.get('itemType')
        if m.get('traceInfo') is not None:
            self.trace_info = m.get('traceInfo')
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        return self


class RecommendResponseBody(TeaModel):
    def __init__(
        self,
        result: List[RecommendResponseBodyResult] = None,
        code: str = None,
        request_id: str = None,
        message: str = None,
    ):
        self.result = result
        self.code = code
        self.request_id = request_id
        self.message = message

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        if self.code is not None:
            result['code'] = self.code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = RecommendResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class RecommendResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RecommendResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RecommendResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RunInstanceResponseBody(TeaModel):
    def __init__(
        self,
        result: bool = None,
        code: str = None,
        request_id: str = None,
        message: str = None,
    ):
        self.result = result
        self.code = code
        self.request_id = request_id
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result
        if self.code is not None:
            result['code'] = self.code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class RunInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RunInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RunInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopDataSetResponseBodyResult(TeaModel):
    def __init__(
        self,
        version_id: str = None,
        state: str = None,
        gmt_modified: int = None,
        gmt_create: int = None,
        instance_id: str = None,
    ):
        self.version_id = version_id
        self.state = state
        self.gmt_modified = gmt_modified
        self.gmt_create = gmt_create
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.version_id is not None:
            result['versionId'] = self.version_id
        if self.state is not None:
            result['state'] = self.state
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('versionId') is not None:
            self.version_id = m.get('versionId')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        return self


class StopDataSetResponseBody(TeaModel):
    def __init__(
        self,
        result: StopDataSetResponseBodyResult = None,
        code: str = None,
        request_id: str = None,
        message: str = None,
    ):
        self.result = result
        self.code = code
        self.request_id = request_id
        self.message = message

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.code is not None:
            result['code'] = self.code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = StopDataSetResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class StopDataSetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StopDataSetResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StopDataSetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnLockIndexVersionResponseBody(TeaModel):
    def __init__(
        self,
        result: bool = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UnLockIndexVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UnLockIndexVersionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UnLockIndexVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateExperimentBasicInfoResponseBodyResultAlgorithmsConfig(TeaModel):
    def __init__(
        self,
        key: str = None,
        default_value: str = None,
        experiment_value: str = None,
        name: str = None,
    ):
        self.key = key
        self.default_value = default_value
        self.experiment_value = experiment_value
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.default_value is not None:
            result['defaultValue'] = self.default_value
        if self.experiment_value is not None:
            result['experimentValue'] = self.experiment_value
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('defaultValue') is not None:
            self.default_value = m.get('defaultValue')
        if m.get('experimentValue') is not None:
            self.experiment_value = m.get('experimentValue')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class UpdateExperimentBasicInfoResponseBodyResultAlgorithms(TeaModel):
    def __init__(
        self,
        key: str = None,
        config: List[UpdateExperimentBasicInfoResponseBodyResultAlgorithmsConfig] = None,
        default_value: str = None,
        type: str = None,
        experiment_value: str = None,
        has_config: bool = None,
        category: str = None,
        name: str = None,
    ):
        self.key = key
        self.config = config
        self.default_value = default_value
        self.type = type
        self.experiment_value = experiment_value
        self.has_config = has_config
        self.category = category
        self.name = name

    def validate(self):
        if self.config:
            for k in self.config:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        result['config'] = []
        if self.config is not None:
            for k in self.config:
                result['config'].append(k.to_map() if k else None)
        if self.default_value is not None:
            result['defaultValue'] = self.default_value
        if self.type is not None:
            result['type'] = self.type
        if self.experiment_value is not None:
            result['experimentValue'] = self.experiment_value
        if self.has_config is not None:
            result['hasConfig'] = self.has_config
        if self.category is not None:
            result['category'] = self.category
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        self.config = []
        if m.get('config') is not None:
            for k in m.get('config'):
                temp_model = UpdateExperimentBasicInfoResponseBodyResultAlgorithmsConfig()
                self.config.append(temp_model.from_map(k))
        if m.get('defaultValue') is not None:
            self.default_value = m.get('defaultValue')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('experimentValue') is not None:
            self.experiment_value = m.get('experimentValue')
        if m.get('hasConfig') is not None:
            self.has_config = m.get('hasConfig')
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class UpdateExperimentBasicInfoResponseBodyResult(TeaModel):
    def __init__(
        self,
        base: bool = None,
        online_time: str = None,
        offline_time: str = None,
        description: str = None,
        status: str = None,
        name: str = None,
        algorithms: List[UpdateExperimentBasicInfoResponseBodyResultAlgorithms] = None,
        buckets: List[str] = None,
        experiment_id: str = None,
    ):
        self.base = base
        self.online_time = online_time
        self.offline_time = offline_time
        self.description = description
        self.status = status
        self.name = name
        self.algorithms = algorithms
        self.buckets = buckets
        self.experiment_id = experiment_id

    def validate(self):
        if self.algorithms:
            for k in self.algorithms:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base is not None:
            result['base'] = self.base
        if self.online_time is not None:
            result['onlineTime'] = self.online_time
        if self.offline_time is not None:
            result['offlineTime'] = self.offline_time
        if self.description is not None:
            result['description'] = self.description
        if self.status is not None:
            result['status'] = self.status
        if self.name is not None:
            result['name'] = self.name
        result['algorithms'] = []
        if self.algorithms is not None:
            for k in self.algorithms:
                result['algorithms'].append(k.to_map() if k else None)
        if self.buckets is not None:
            result['buckets'] = self.buckets
        if self.experiment_id is not None:
            result['experimentId'] = self.experiment_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('base') is not None:
            self.base = m.get('base')
        if m.get('onlineTime') is not None:
            self.online_time = m.get('onlineTime')
        if m.get('offlineTime') is not None:
            self.offline_time = m.get('offlineTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('name') is not None:
            self.name = m.get('name')
        self.algorithms = []
        if m.get('algorithms') is not None:
            for k in m.get('algorithms'):
                temp_model = UpdateExperimentBasicInfoResponseBodyResultAlgorithms()
                self.algorithms.append(temp_model.from_map(k))
        if m.get('buckets') is not None:
            self.buckets = m.get('buckets')
        if m.get('experimentId') is not None:
            self.experiment_id = m.get('experimentId')
        return self


class UpdateExperimentBasicInfoResponseBody(TeaModel):
    def __init__(
        self,
        result: UpdateExperimentBasicInfoResponseBodyResult = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = UpdateExperimentBasicInfoResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateExperimentBasicInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateExperimentBasicInfoResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateExperimentBasicInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateExperimentConfigResponseBodyResultAlgorithmsConfig(TeaModel):
    def __init__(
        self,
        key: str = None,
        default_value: str = None,
        experiment_value: str = None,
        name: str = None,
    ):
        self.key = key
        self.default_value = default_value
        self.experiment_value = experiment_value
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.default_value is not None:
            result['defaultValue'] = self.default_value
        if self.experiment_value is not None:
            result['experimentValue'] = self.experiment_value
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('defaultValue') is not None:
            self.default_value = m.get('defaultValue')
        if m.get('experimentValue') is not None:
            self.experiment_value = m.get('experimentValue')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class UpdateExperimentConfigResponseBodyResultAlgorithms(TeaModel):
    def __init__(
        self,
        key: str = None,
        config: List[UpdateExperimentConfigResponseBodyResultAlgorithmsConfig] = None,
        default_value: str = None,
        type: str = None,
        experiment_value: str = None,
        has_config: bool = None,
        category: str = None,
        name: str = None,
    ):
        self.key = key
        self.config = config
        self.default_value = default_value
        self.type = type
        self.experiment_value = experiment_value
        self.has_config = has_config
        self.category = category
        self.name = name

    def validate(self):
        if self.config:
            for k in self.config:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        result['config'] = []
        if self.config is not None:
            for k in self.config:
                result['config'].append(k.to_map() if k else None)
        if self.default_value is not None:
            result['defaultValue'] = self.default_value
        if self.type is not None:
            result['type'] = self.type
        if self.experiment_value is not None:
            result['experimentValue'] = self.experiment_value
        if self.has_config is not None:
            result['hasConfig'] = self.has_config
        if self.category is not None:
            result['category'] = self.category
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        self.config = []
        if m.get('config') is not None:
            for k in m.get('config'):
                temp_model = UpdateExperimentConfigResponseBodyResultAlgorithmsConfig()
                self.config.append(temp_model.from_map(k))
        if m.get('defaultValue') is not None:
            self.default_value = m.get('defaultValue')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('experimentValue') is not None:
            self.experiment_value = m.get('experimentValue')
        if m.get('hasConfig') is not None:
            self.has_config = m.get('hasConfig')
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class UpdateExperimentConfigResponseBodyResult(TeaModel):
    def __init__(
        self,
        base: bool = None,
        online_time: str = None,
        offline_time: str = None,
        description: str = None,
        status: str = None,
        name: str = None,
        algorithms: List[UpdateExperimentConfigResponseBodyResultAlgorithms] = None,
        buckets: List[str] = None,
        experiment_id: str = None,
    ):
        self.base = base
        self.online_time = online_time
        self.offline_time = offline_time
        self.description = description
        self.status = status
        self.name = name
        self.algorithms = algorithms
        self.buckets = buckets
        self.experiment_id = experiment_id

    def validate(self):
        if self.algorithms:
            for k in self.algorithms:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base is not None:
            result['base'] = self.base
        if self.online_time is not None:
            result['onlineTime'] = self.online_time
        if self.offline_time is not None:
            result['offlineTime'] = self.offline_time
        if self.description is not None:
            result['description'] = self.description
        if self.status is not None:
            result['status'] = self.status
        if self.name is not None:
            result['name'] = self.name
        result['algorithms'] = []
        if self.algorithms is not None:
            for k in self.algorithms:
                result['algorithms'].append(k.to_map() if k else None)
        if self.buckets is not None:
            result['buckets'] = self.buckets
        if self.experiment_id is not None:
            result['experimentId'] = self.experiment_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('base') is not None:
            self.base = m.get('base')
        if m.get('onlineTime') is not None:
            self.online_time = m.get('onlineTime')
        if m.get('offlineTime') is not None:
            self.offline_time = m.get('offlineTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('name') is not None:
            self.name = m.get('name')
        self.algorithms = []
        if m.get('algorithms') is not None:
            for k in m.get('algorithms'):
                temp_model = UpdateExperimentConfigResponseBodyResultAlgorithms()
                self.algorithms.append(temp_model.from_map(k))
        if m.get('buckets') is not None:
            self.buckets = m.get('buckets')
        if m.get('experimentId') is not None:
            self.experiment_id = m.get('experimentId')
        return self


class UpdateExperimentConfigResponseBody(TeaModel):
    def __init__(
        self,
        result: UpdateExperimentConfigResponseBodyResult = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = UpdateExperimentConfigResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateExperimentConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateExperimentConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateExperimentConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateExperimentStatusResponseBodyResultAlgorithmsConfig(TeaModel):
    def __init__(
        self,
        key: str = None,
        default_value: str = None,
        experiment_value: str = None,
        name: str = None,
    ):
        self.key = key
        self.default_value = default_value
        self.experiment_value = experiment_value
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.default_value is not None:
            result['defaultValue'] = self.default_value
        if self.experiment_value is not None:
            result['experimentValue'] = self.experiment_value
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('defaultValue') is not None:
            self.default_value = m.get('defaultValue')
        if m.get('experimentValue') is not None:
            self.experiment_value = m.get('experimentValue')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class UpdateExperimentStatusResponseBodyResultAlgorithms(TeaModel):
    def __init__(
        self,
        key: str = None,
        config: List[UpdateExperimentStatusResponseBodyResultAlgorithmsConfig] = None,
        default_value: str = None,
        type: str = None,
        experiment_value: str = None,
        has_config: bool = None,
        category: str = None,
        name: str = None,
    ):
        self.key = key
        self.config = config
        self.default_value = default_value
        self.type = type
        self.experiment_value = experiment_value
        self.has_config = has_config
        self.category = category
        self.name = name

    def validate(self):
        if self.config:
            for k in self.config:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        result['config'] = []
        if self.config is not None:
            for k in self.config:
                result['config'].append(k.to_map() if k else None)
        if self.default_value is not None:
            result['defaultValue'] = self.default_value
        if self.type is not None:
            result['type'] = self.type
        if self.experiment_value is not None:
            result['experimentValue'] = self.experiment_value
        if self.has_config is not None:
            result['hasConfig'] = self.has_config
        if self.category is not None:
            result['category'] = self.category
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        self.config = []
        if m.get('config') is not None:
            for k in m.get('config'):
                temp_model = UpdateExperimentStatusResponseBodyResultAlgorithmsConfig()
                self.config.append(temp_model.from_map(k))
        if m.get('defaultValue') is not None:
            self.default_value = m.get('defaultValue')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('experimentValue') is not None:
            self.experiment_value = m.get('experimentValue')
        if m.get('hasConfig') is not None:
            self.has_config = m.get('hasConfig')
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class UpdateExperimentStatusResponseBodyResult(TeaModel):
    def __init__(
        self,
        base: bool = None,
        online_time: str = None,
        offline_time: str = None,
        description: str = None,
        status: str = None,
        name: str = None,
        algorithms: List[UpdateExperimentStatusResponseBodyResultAlgorithms] = None,
        buckets: List[str] = None,
        experiment_id: str = None,
    ):
        self.base = base
        self.online_time = online_time
        self.offline_time = offline_time
        self.description = description
        self.status = status
        self.name = name
        self.algorithms = algorithms
        self.buckets = buckets
        self.experiment_id = experiment_id

    def validate(self):
        if self.algorithms:
            for k in self.algorithms:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base is not None:
            result['base'] = self.base
        if self.online_time is not None:
            result['onlineTime'] = self.online_time
        if self.offline_time is not None:
            result['offlineTime'] = self.offline_time
        if self.description is not None:
            result['description'] = self.description
        if self.status is not None:
            result['status'] = self.status
        if self.name is not None:
            result['name'] = self.name
        result['algorithms'] = []
        if self.algorithms is not None:
            for k in self.algorithms:
                result['algorithms'].append(k.to_map() if k else None)
        if self.buckets is not None:
            result['buckets'] = self.buckets
        if self.experiment_id is not None:
            result['experimentId'] = self.experiment_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('base') is not None:
            self.base = m.get('base')
        if m.get('onlineTime') is not None:
            self.online_time = m.get('onlineTime')
        if m.get('offlineTime') is not None:
            self.offline_time = m.get('offlineTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('name') is not None:
            self.name = m.get('name')
        self.algorithms = []
        if m.get('algorithms') is not None:
            for k in m.get('algorithms'):
                temp_model = UpdateExperimentStatusResponseBodyResultAlgorithms()
                self.algorithms.append(temp_model.from_map(k))
        if m.get('buckets') is not None:
            self.buckets = m.get('buckets')
        if m.get('experimentId') is not None:
            self.experiment_id = m.get('experimentId')
        return self


class UpdateExperimentStatusResponseBody(TeaModel):
    def __init__(
        self,
        result: UpdateExperimentStatusResponseBodyResult = None,
        request_id: str = None,
    ):
        self.result = result
        self.request_id = request_id

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = UpdateExperimentStatusResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateExperimentStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateExperimentStatusResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateExperimentStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpgradeInstanceResponseBodyResult(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        return self


class UpgradeInstanceResponseBody(TeaModel):
    def __init__(
        self,
        result: UpgradeInstanceResponseBodyResult = None,
        code: str = None,
        request_id: str = None,
        message: str = None,
    ):
        self.result = result
        self.code = code
        self.request_id = request_id
        self.message = message

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.code is not None:
            result['code'] = self.code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = UpgradeInstanceResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class UpgradeInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpgradeInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpgradeInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ValidateInstanceResponseBody(TeaModel):
    def __init__(
        self,
        result: bool = None,
        code: str = None,
        request_id: str = None,
        message: str = None,
    ):
        self.result = result
        self.code = code
        self.request_id = request_id
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result
        if self.code is not None:
            result['code'] = self.code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class ValidateInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ValidateInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ValidateInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


