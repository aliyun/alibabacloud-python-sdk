# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, BinaryIO


class AccelerationInfo(TeaModel):
    def __init__(
        self,
        status: str = None,
    ):
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class Alias(TeaModel):
    def __init__(
        self,
        additional_version_weight: Dict[str, float] = None,
        alias_name: str = None,
        created_time: str = None,
        description: str = None,
        last_modified_time: str = None,
        version_id: str = None,
    ):
        self.additional_version_weight = additional_version_weight
        self.alias_name = alias_name
        self.created_time = created_time
        self.description = description
        self.last_modified_time = last_modified_time
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.additional_version_weight is not None:
            result['additionalVersionWeight'] = self.additional_version_weight
        if self.alias_name is not None:
            result['aliasName'] = self.alias_name
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.description is not None:
            result['description'] = self.description
        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time
        if self.version_id is not None:
            result['versionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('additionalVersionWeight') is not None:
            self.additional_version_weight = m.get('additionalVersionWeight')
        if m.get('aliasName') is not None:
            self.alias_name = m.get('aliasName')
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')
        if m.get('versionId') is not None:
            self.version_id = m.get('versionId')
        return self


class Destination(TeaModel):
    def __init__(
        self,
        destination: str = None,
    ):
        self.destination = destination

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination is not None:
            result['destination'] = self.destination
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('destination') is not None:
            self.destination = m.get('destination')
        return self


class DestinationConfig(TeaModel):
    def __init__(
        self,
        on_failure: Destination = None,
        on_success: Destination = None,
    ):
        self.on_failure = on_failure
        self.on_success = on_success

    def validate(self):
        if self.on_failure:
            self.on_failure.validate()
        if self.on_success:
            self.on_success.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.on_failure is not None:
            result['onFailure'] = self.on_failure.to_map()
        if self.on_success is not None:
            result['onSuccess'] = self.on_success.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('onFailure') is not None:
            temp_model = Destination()
            self.on_failure = temp_model.from_map(m['onFailure'])
        if m.get('onSuccess') is not None:
            temp_model = Destination()
            self.on_success = temp_model.from_map(m['onSuccess'])
        return self


class AsyncConfig(TeaModel):
    def __init__(
        self,
        async_task: bool = None,
        created_time: str = None,
        destination_config: DestinationConfig = None,
        function_arn: str = None,
        last_modified_time: str = None,
        max_async_event_age_in_seconds: int = None,
        max_async_retry_attempts: int = None,
    ):
        self.async_task = async_task
        self.created_time = created_time
        self.destination_config = destination_config
        self.function_arn = function_arn
        self.last_modified_time = last_modified_time
        self.max_async_event_age_in_seconds = max_async_event_age_in_seconds
        self.max_async_retry_attempts = max_async_retry_attempts

    def validate(self):
        if self.destination_config:
            self.destination_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.async_task is not None:
            result['asyncTask'] = self.async_task
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.destination_config is not None:
            result['destinationConfig'] = self.destination_config.to_map()
        if self.function_arn is not None:
            result['functionArn'] = self.function_arn
        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time
        if self.max_async_event_age_in_seconds is not None:
            result['maxAsyncEventAgeInSeconds'] = self.max_async_event_age_in_seconds
        if self.max_async_retry_attempts is not None:
            result['maxAsyncRetryAttempts'] = self.max_async_retry_attempts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('asyncTask') is not None:
            self.async_task = m.get('asyncTask')
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('destinationConfig') is not None:
            temp_model = DestinationConfig()
            self.destination_config = temp_model.from_map(m['destinationConfig'])
        if m.get('functionArn') is not None:
            self.function_arn = m.get('functionArn')
        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')
        if m.get('maxAsyncEventAgeInSeconds') is not None:
            self.max_async_event_age_in_seconds = m.get('maxAsyncEventAgeInSeconds')
        if m.get('maxAsyncRetryAttempts') is not None:
            self.max_async_retry_attempts = m.get('maxAsyncRetryAttempts')
        return self


class AsyncTaskEvent(TeaModel):
    def __init__(
        self,
        event_detail: str = None,
        event_id: int = None,
        status: str = None,
        timestamp: int = None,
    ):
        self.event_detail = event_detail
        self.event_id = event_id
        self.status = status
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_detail is not None:
            result['eventDetail'] = self.event_detail
        if self.event_id is not None:
            result['eventId'] = self.event_id
        if self.status is not None:
            result['status'] = self.status
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('eventDetail') is not None:
            self.event_detail = m.get('eventDetail')
        if m.get('eventId') is not None:
            self.event_id = m.get('eventId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        return self


class AsyncTask(TeaModel):
    def __init__(
        self,
        already_retried_times: int = None,
        destination_status: str = None,
        duration_ms: int = None,
        end_time: int = None,
        events: List[AsyncTaskEvent] = None,
        function_arn: str = None,
        instance_id: str = None,
        qualifier: str = None,
        request_id: str = None,
        return_payload: str = None,
        started_time: int = None,
        status: str = None,
        task_error_message: str = None,
        task_id: str = None,
        task_payload: str = None,
    ):
        self.already_retried_times = already_retried_times
        self.destination_status = destination_status
        self.duration_ms = duration_ms
        self.end_time = end_time
        self.events = events
        self.function_arn = function_arn
        self.instance_id = instance_id
        self.qualifier = qualifier
        self.request_id = request_id
        self.return_payload = return_payload
        self.started_time = started_time
        self.status = status
        self.task_error_message = task_error_message
        self.task_id = task_id
        self.task_payload = task_payload

    def validate(self):
        if self.events:
            for k in self.events:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.already_retried_times is not None:
            result['alreadyRetriedTimes'] = self.already_retried_times
        if self.destination_status is not None:
            result['destinationStatus'] = self.destination_status
        if self.duration_ms is not None:
            result['durationMs'] = self.duration_ms
        if self.end_time is not None:
            result['endTime'] = self.end_time
        result['events'] = []
        if self.events is not None:
            for k in self.events:
                result['events'].append(k.to_map() if k else None)
        if self.function_arn is not None:
            result['functionArn'] = self.function_arn
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.return_payload is not None:
            result['returnPayload'] = self.return_payload
        if self.started_time is not None:
            result['startedTime'] = self.started_time
        if self.status is not None:
            result['status'] = self.status
        if self.task_error_message is not None:
            result['taskErrorMessage'] = self.task_error_message
        if self.task_id is not None:
            result['taskId'] = self.task_id
        if self.task_payload is not None:
            result['taskPayload'] = self.task_payload
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alreadyRetriedTimes') is not None:
            self.already_retried_times = m.get('alreadyRetriedTimes')
        if m.get('destinationStatus') is not None:
            self.destination_status = m.get('destinationStatus')
        if m.get('durationMs') is not None:
            self.duration_ms = m.get('durationMs')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        self.events = []
        if m.get('events') is not None:
            for k in m.get('events'):
                temp_model = AsyncTaskEvent()
                self.events.append(temp_model.from_map(k))
        if m.get('functionArn') is not None:
            self.function_arn = m.get('functionArn')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('returnPayload') is not None:
            self.return_payload = m.get('returnPayload')
        if m.get('startedTime') is not None:
            self.started_time = m.get('startedTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('taskErrorMessage') is not None:
            self.task_error_message = m.get('taskErrorMessage')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        if m.get('taskPayload') is not None:
            self.task_payload = m.get('taskPayload')
        return self


class AuthConfig(TeaModel):
    def __init__(
        self,
        auth_info: str = None,
        auth_type: str = None,
    ):
        self.auth_info = auth_info
        self.auth_type = auth_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_info is not None:
            result['authInfo'] = self.auth_info
        if self.auth_type is not None:
            result['authType'] = self.auth_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authInfo') is not None:
            self.auth_info = m.get('authInfo')
        if m.get('authType') is not None:
            self.auth_type = m.get('authType')
        return self


class BatchWindow(TeaModel):
    def __init__(
        self,
        count_based_window: int = None,
        time_based_window: int = None,
    ):
        self.count_based_window = count_based_window
        self.time_based_window = time_based_window

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count_based_window is not None:
            result['CountBasedWindow'] = self.count_based_window
        if self.time_based_window is not None:
            result['TimeBasedWindow'] = self.time_based_window
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CountBasedWindow') is not None:
            self.count_based_window = m.get('CountBasedWindow')
        if m.get('TimeBasedWindow') is not None:
            self.time_based_window = m.get('TimeBasedWindow')
        return self


class CDNTriggerConfig(TeaModel):
    def __init__(
        self,
        event_name: str = None,
        event_version: str = None,
        filter: Dict[str, List[str]] = None,
        notes: str = None,
    ):
        self.event_name = event_name
        self.event_version = event_version
        self.filter = filter
        self.notes = notes

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_name is not None:
            result['eventName'] = self.event_name
        if self.event_version is not None:
            result['eventVersion'] = self.event_version
        if self.filter is not None:
            result['filter'] = self.filter
        if self.notes is not None:
            result['notes'] = self.notes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('eventName') is not None:
            self.event_name = m.get('eventName')
        if m.get('eventVersion') is not None:
            self.event_version = m.get('eventVersion')
        if m.get('filter') is not None:
            self.filter = m.get('filter')
        if m.get('notes') is not None:
            self.notes = m.get('notes')
        return self


class CertConfig(TeaModel):
    def __init__(
        self,
        cert_name: str = None,
        certificate: str = None,
        private_key: str = None,
    ):
        # This parameter is required.
        self.cert_name = cert_name
        # This parameter is required.
        self.certificate = certificate
        # This parameter is required.
        self.private_key = private_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_name is not None:
            result['certName'] = self.cert_name
        if self.certificate is not None:
            result['certificate'] = self.certificate
        if self.private_key is not None:
            result['privateKey'] = self.private_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('certName') is not None:
            self.cert_name = m.get('certName')
        if m.get('certificate') is not None:
            self.certificate = m.get('certificate')
        if m.get('privateKey') is not None:
            self.private_key = m.get('privateKey')
        return self


class ConcurrencyConfig(TeaModel):
    def __init__(
        self,
        function_arn: str = None,
        reserved_concurrency: int = None,
    ):
        self.function_arn = function_arn
        self.reserved_concurrency = reserved_concurrency

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.function_arn is not None:
            result['functionArn'] = self.function_arn
        if self.reserved_concurrency is not None:
            result['reservedConcurrency'] = self.reserved_concurrency
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('functionArn') is not None:
            self.function_arn = m.get('functionArn')
        if m.get('reservedConcurrency') is not None:
            self.reserved_concurrency = m.get('reservedConcurrency')
        return self


class CreateAliasInput(TeaModel):
    def __init__(
        self,
        additional_version_weight: Dict[str, float] = None,
        alias_name: str = None,
        description: str = None,
        version_id: str = None,
    ):
        self.additional_version_weight = additional_version_weight
        # This parameter is required.
        self.alias_name = alias_name
        self.description = description
        # This parameter is required.
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.additional_version_weight is not None:
            result['additionalVersionWeight'] = self.additional_version_weight
        if self.alias_name is not None:
            result['aliasName'] = self.alias_name
        if self.description is not None:
            result['description'] = self.description
        if self.version_id is not None:
            result['versionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('additionalVersionWeight') is not None:
            self.additional_version_weight = m.get('additionalVersionWeight')
        if m.get('aliasName') is not None:
            self.alias_name = m.get('aliasName')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('versionId') is not None:
            self.version_id = m.get('versionId')
        return self


class EqualRule(TeaModel):
    def __init__(
        self,
        match: str = None,
        replacement: str = None,
    ):
        # This parameter is required.
        self.match = match
        # This parameter is required.
        self.replacement = replacement

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match is not None:
            result['match'] = self.match
        if self.replacement is not None:
            result['replacement'] = self.replacement
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('match') is not None:
            self.match = m.get('match')
        if m.get('replacement') is not None:
            self.replacement = m.get('replacement')
        return self


class RegexRule(TeaModel):
    def __init__(
        self,
        match: str = None,
        replacement: str = None,
    ):
        # This parameter is required.
        self.match = match
        # This parameter is required.
        self.replacement = replacement

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match is not None:
            result['match'] = self.match
        if self.replacement is not None:
            result['replacement'] = self.replacement
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('match') is not None:
            self.match = m.get('match')
        if m.get('replacement') is not None:
            self.replacement = m.get('replacement')
        return self


class WildcardRule(TeaModel):
    def __init__(
        self,
        match: str = None,
        replacement: str = None,
    ):
        # This parameter is required.
        self.match = match
        # This parameter is required.
        self.replacement = replacement

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match is not None:
            result['match'] = self.match
        if self.replacement is not None:
            result['replacement'] = self.replacement
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('match') is not None:
            self.match = m.get('match')
        if m.get('replacement') is not None:
            self.replacement = m.get('replacement')
        return self


class RewriteConfig(TeaModel):
    def __init__(
        self,
        equal_rules: List[EqualRule] = None,
        regex_rules: List[RegexRule] = None,
        wildcard_rules: List[WildcardRule] = None,
    ):
        self.equal_rules = equal_rules
        self.regex_rules = regex_rules
        self.wildcard_rules = wildcard_rules

    def validate(self):
        if self.equal_rules:
            for k in self.equal_rules:
                if k:
                    k.validate()
        if self.regex_rules:
            for k in self.regex_rules:
                if k:
                    k.validate()
        if self.wildcard_rules:
            for k in self.wildcard_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['equalRules'] = []
        if self.equal_rules is not None:
            for k in self.equal_rules:
                result['equalRules'].append(k.to_map() if k else None)
        result['regexRules'] = []
        if self.regex_rules is not None:
            for k in self.regex_rules:
                result['regexRules'].append(k.to_map() if k else None)
        result['wildcardRules'] = []
        if self.wildcard_rules is not None:
            for k in self.wildcard_rules:
                result['wildcardRules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.equal_rules = []
        if m.get('equalRules') is not None:
            for k in m.get('equalRules'):
                temp_model = EqualRule()
                self.equal_rules.append(temp_model.from_map(k))
        self.regex_rules = []
        if m.get('regexRules') is not None:
            for k in m.get('regexRules'):
                temp_model = RegexRule()
                self.regex_rules.append(temp_model.from_map(k))
        self.wildcard_rules = []
        if m.get('wildcardRules') is not None:
            for k in m.get('wildcardRules'):
                temp_model = WildcardRule()
                self.wildcard_rules.append(temp_model.from_map(k))
        return self


class PathConfig(TeaModel):
    def __init__(
        self,
        function_name: str = None,
        methods: List[str] = None,
        path: str = None,
        qualifier: str = None,
        rewrite_config: RewriteConfig = None,
    ):
        # This parameter is required.
        self.function_name = function_name
        self.methods = methods
        # This parameter is required.
        self.path = path
        self.qualifier = qualifier
        self.rewrite_config = rewrite_config

    def validate(self):
        if self.rewrite_config:
            self.rewrite_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.function_name is not None:
            result['functionName'] = self.function_name
        if self.methods is not None:
            result['methods'] = self.methods
        if self.path is not None:
            result['path'] = self.path
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        if self.rewrite_config is not None:
            result['rewriteConfig'] = self.rewrite_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('functionName') is not None:
            self.function_name = m.get('functionName')
        if m.get('methods') is not None:
            self.methods = m.get('methods')
        if m.get('path') is not None:
            self.path = m.get('path')
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        if m.get('rewriteConfig') is not None:
            temp_model = RewriteConfig()
            self.rewrite_config = temp_model.from_map(m['rewriteConfig'])
        return self


class RouteConfig(TeaModel):
    def __init__(
        self,
        routes: List[PathConfig] = None,
    ):
        self.routes = routes

    def validate(self):
        if self.routes:
            for k in self.routes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['routes'] = []
        if self.routes is not None:
            for k in self.routes:
                result['routes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.routes = []
        if m.get('routes') is not None:
            for k in m.get('routes'):
                temp_model = PathConfig()
                self.routes.append(temp_model.from_map(k))
        return self


class TLSConfig(TeaModel):
    def __init__(
        self,
        cipher_suites: List[str] = None,
        max_version: str = None,
        min_version: str = None,
    ):
        # This parameter is required.
        self.cipher_suites = cipher_suites
        self.max_version = max_version
        # This parameter is required.
        self.min_version = min_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cipher_suites is not None:
            result['cipherSuites'] = self.cipher_suites
        if self.max_version is not None:
            result['maxVersion'] = self.max_version
        if self.min_version is not None:
            result['minVersion'] = self.min_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cipherSuites') is not None:
            self.cipher_suites = m.get('cipherSuites')
        if m.get('maxVersion') is not None:
            self.max_version = m.get('maxVersion')
        if m.get('minVersion') is not None:
            self.min_version = m.get('minVersion')
        return self


class WAFConfig(TeaModel):
    def __init__(
        self,
        enable_waf: bool = None,
    ):
        self.enable_waf = enable_waf

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_waf is not None:
            result['enableWAF'] = self.enable_waf
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enableWAF') is not None:
            self.enable_waf = m.get('enableWAF')
        return self


class CreateCustomDomainInput(TeaModel):
    def __init__(
        self,
        auth_config: AuthConfig = None,
        cert_config: CertConfig = None,
        domain_name: str = None,
        protocol: str = None,
        route_config: RouteConfig = None,
        tls_config: TLSConfig = None,
        waf_config: WAFConfig = None,
    ):
        self.auth_config = auth_config
        self.cert_config = cert_config
        # This parameter is required.
        self.domain_name = domain_name
        self.protocol = protocol
        self.route_config = route_config
        self.tls_config = tls_config
        self.waf_config = waf_config

    def validate(self):
        if self.auth_config:
            self.auth_config.validate()
        if self.cert_config:
            self.cert_config.validate()
        if self.route_config:
            self.route_config.validate()
        if self.tls_config:
            self.tls_config.validate()
        if self.waf_config:
            self.waf_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_config is not None:
            result['authConfig'] = self.auth_config.to_map()
        if self.cert_config is not None:
            result['certConfig'] = self.cert_config.to_map()
        if self.domain_name is not None:
            result['domainName'] = self.domain_name
        if self.protocol is not None:
            result['protocol'] = self.protocol
        if self.route_config is not None:
            result['routeConfig'] = self.route_config.to_map()
        if self.tls_config is not None:
            result['tlsConfig'] = self.tls_config.to_map()
        if self.waf_config is not None:
            result['wafConfig'] = self.waf_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authConfig') is not None:
            temp_model = AuthConfig()
            self.auth_config = temp_model.from_map(m['authConfig'])
        if m.get('certConfig') is not None:
            temp_model = CertConfig()
            self.cert_config = temp_model.from_map(m['certConfig'])
        if m.get('domainName') is not None:
            self.domain_name = m.get('domainName')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('routeConfig') is not None:
            temp_model = RouteConfig()
            self.route_config = temp_model.from_map(m['routeConfig'])
        if m.get('tlsConfig') is not None:
            temp_model = TLSConfig()
            self.tls_config = temp_model.from_map(m['tlsConfig'])
        if m.get('wafConfig') is not None:
            temp_model = WAFConfig()
            self.waf_config = temp_model.from_map(m['wafConfig'])
        return self


class InputCodeLocation(TeaModel):
    def __init__(
        self,
        checksum: str = None,
        oss_bucket_name: str = None,
        oss_object_name: str = None,
        zip_file: str = None,
    ):
        self.checksum = checksum
        self.oss_bucket_name = oss_bucket_name
        self.oss_object_name = oss_object_name
        self.zip_file = zip_file

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.checksum is not None:
            result['checksum'] = self.checksum
        if self.oss_bucket_name is not None:
            result['ossBucketName'] = self.oss_bucket_name
        if self.oss_object_name is not None:
            result['ossObjectName'] = self.oss_object_name
        if self.zip_file is not None:
            result['zipFile'] = self.zip_file
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('checksum') is not None:
            self.checksum = m.get('checksum')
        if m.get('ossBucketName') is not None:
            self.oss_bucket_name = m.get('ossBucketName')
        if m.get('ossObjectName') is not None:
            self.oss_object_name = m.get('ossObjectName')
        if m.get('zipFile') is not None:
            self.zip_file = m.get('zipFile')
        return self


class CustomHealthCheckConfig(TeaModel):
    def __init__(
        self,
        failure_threshold: int = None,
        http_get_url: str = None,
        initial_delay_seconds: int = None,
        period_seconds: int = None,
        success_threshold: int = None,
        timeout_seconds: int = None,
    ):
        self.failure_threshold = failure_threshold
        self.http_get_url = http_get_url
        self.initial_delay_seconds = initial_delay_seconds
        self.period_seconds = period_seconds
        self.success_threshold = success_threshold
        self.timeout_seconds = timeout_seconds

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.failure_threshold is not None:
            result['failureThreshold'] = self.failure_threshold
        if self.http_get_url is not None:
            result['httpGetUrl'] = self.http_get_url
        if self.initial_delay_seconds is not None:
            result['initialDelaySeconds'] = self.initial_delay_seconds
        if self.period_seconds is not None:
            result['periodSeconds'] = self.period_seconds
        if self.success_threshold is not None:
            result['successThreshold'] = self.success_threshold
        if self.timeout_seconds is not None:
            result['timeoutSeconds'] = self.timeout_seconds
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('failureThreshold') is not None:
            self.failure_threshold = m.get('failureThreshold')
        if m.get('httpGetUrl') is not None:
            self.http_get_url = m.get('httpGetUrl')
        if m.get('initialDelaySeconds') is not None:
            self.initial_delay_seconds = m.get('initialDelaySeconds')
        if m.get('periodSeconds') is not None:
            self.period_seconds = m.get('periodSeconds')
        if m.get('successThreshold') is not None:
            self.success_threshold = m.get('successThreshold')
        if m.get('timeoutSeconds') is not None:
            self.timeout_seconds = m.get('timeoutSeconds')
        return self


class CustomContainerConfig(TeaModel):
    def __init__(
        self,
        acceleration_info: AccelerationInfo = None,
        acceleration_type: str = None,
        acr_instance_id: str = None,
        command: List[str] = None,
        entrypoint: List[str] = None,
        health_check_config: CustomHealthCheckConfig = None,
        image: str = None,
        port: int = None,
        resolved_image_uri: str = None,
    ):
        self.acceleration_info = acceleration_info
        self.acceleration_type = acceleration_type
        self.acr_instance_id = acr_instance_id
        self.command = command
        self.entrypoint = entrypoint
        self.health_check_config = health_check_config
        self.image = image
        self.port = port
        self.resolved_image_uri = resolved_image_uri

    def validate(self):
        if self.acceleration_info:
            self.acceleration_info.validate()
        if self.health_check_config:
            self.health_check_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acceleration_info is not None:
            result['accelerationInfo'] = self.acceleration_info.to_map()
        if self.acceleration_type is not None:
            result['accelerationType'] = self.acceleration_type
        if self.acr_instance_id is not None:
            result['acrInstanceId'] = self.acr_instance_id
        if self.command is not None:
            result['command'] = self.command
        if self.entrypoint is not None:
            result['entrypoint'] = self.entrypoint
        if self.health_check_config is not None:
            result['healthCheckConfig'] = self.health_check_config.to_map()
        if self.image is not None:
            result['image'] = self.image
        if self.port is not None:
            result['port'] = self.port
        if self.resolved_image_uri is not None:
            result['resolvedImageUri'] = self.resolved_image_uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accelerationInfo') is not None:
            temp_model = AccelerationInfo()
            self.acceleration_info = temp_model.from_map(m['accelerationInfo'])
        if m.get('accelerationType') is not None:
            self.acceleration_type = m.get('accelerationType')
        if m.get('acrInstanceId') is not None:
            self.acr_instance_id = m.get('acrInstanceId')
        if m.get('command') is not None:
            self.command = m.get('command')
        if m.get('entrypoint') is not None:
            self.entrypoint = m.get('entrypoint')
        if m.get('healthCheckConfig') is not None:
            temp_model = CustomHealthCheckConfig()
            self.health_check_config = temp_model.from_map(m['healthCheckConfig'])
        if m.get('image') is not None:
            self.image = m.get('image')
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('resolvedImageUri') is not None:
            self.resolved_image_uri = m.get('resolvedImageUri')
        return self


class DNSOption(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        self.name = name
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class CustomDNS(TeaModel):
    def __init__(
        self,
        dns_options: List[DNSOption] = None,
        name_servers: List[str] = None,
        searches: List[str] = None,
    ):
        self.dns_options = dns_options
        self.name_servers = name_servers
        self.searches = searches

    def validate(self):
        if self.dns_options:
            for k in self.dns_options:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['dnsOptions'] = []
        if self.dns_options is not None:
            for k in self.dns_options:
                result['dnsOptions'].append(k.to_map() if k else None)
        if self.name_servers is not None:
            result['nameServers'] = self.name_servers
        if self.searches is not None:
            result['searches'] = self.searches
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dns_options = []
        if m.get('dnsOptions') is not None:
            for k in m.get('dnsOptions'):
                temp_model = DNSOption()
                self.dns_options.append(temp_model.from_map(k))
        if m.get('nameServers') is not None:
            self.name_servers = m.get('nameServers')
        if m.get('searches') is not None:
            self.searches = m.get('searches')
        return self


class CustomRuntimeConfig(TeaModel):
    def __init__(
        self,
        args: List[str] = None,
        command: List[str] = None,
        health_check_config: CustomHealthCheckConfig = None,
        port: int = None,
    ):
        self.args = args
        self.command = command
        self.health_check_config = health_check_config
        self.port = port

    def validate(self):
        if self.health_check_config:
            self.health_check_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.args is not None:
            result['args'] = self.args
        if self.command is not None:
            result['command'] = self.command
        if self.health_check_config is not None:
            result['healthCheckConfig'] = self.health_check_config.to_map()
        if self.port is not None:
            result['port'] = self.port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('args') is not None:
            self.args = m.get('args')
        if m.get('command') is not None:
            self.command = m.get('command')
        if m.get('healthCheckConfig') is not None:
            temp_model = CustomHealthCheckConfig()
            self.health_check_config = temp_model.from_map(m['healthCheckConfig'])
        if m.get('port') is not None:
            self.port = m.get('port')
        return self


class GPUConfig(TeaModel):
    def __init__(
        self,
        gpu_memory_size: int = None,
        gpu_type: str = None,
    ):
        self.gpu_memory_size = gpu_memory_size
        self.gpu_type = gpu_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gpu_memory_size is not None:
            result['gpuMemorySize'] = self.gpu_memory_size
        if self.gpu_type is not None:
            result['gpuType'] = self.gpu_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gpuMemorySize') is not None:
            self.gpu_memory_size = m.get('gpuMemorySize')
        if m.get('gpuType') is not None:
            self.gpu_type = m.get('gpuType')
        return self


class LifecycleHook(TeaModel):
    def __init__(
        self,
        handler: str = None,
        timeout: int = None,
    ):
        self.handler = handler
        self.timeout = timeout

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.handler is not None:
            result['handler'] = self.handler
        if self.timeout is not None:
            result['timeout'] = self.timeout
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('handler') is not None:
            self.handler = m.get('handler')
        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')
        return self


class InstanceLifecycleConfig(TeaModel):
    def __init__(
        self,
        initializer: LifecycleHook = None,
        pre_stop: LifecycleHook = None,
    ):
        self.initializer = initializer
        self.pre_stop = pre_stop

    def validate(self):
        if self.initializer:
            self.initializer.validate()
        if self.pre_stop:
            self.pre_stop.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.initializer is not None:
            result['initializer'] = self.initializer.to_map()
        if self.pre_stop is not None:
            result['preStop'] = self.pre_stop.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('initializer') is not None:
            temp_model = LifecycleHook()
            self.initializer = temp_model.from_map(m['initializer'])
        if m.get('preStop') is not None:
            temp_model = LifecycleHook()
            self.pre_stop = temp_model.from_map(m['preStop'])
        return self


class LogConfig(TeaModel):
    def __init__(
        self,
        enable_instance_metrics: bool = None,
        enable_request_metrics: bool = None,
        log_begin_rule: str = None,
        logstore: str = None,
        project: str = None,
    ):
        self.enable_instance_metrics = enable_instance_metrics
        self.enable_request_metrics = enable_request_metrics
        self.log_begin_rule = log_begin_rule
        self.logstore = logstore
        self.project = project

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_instance_metrics is not None:
            result['enableInstanceMetrics'] = self.enable_instance_metrics
        if self.enable_request_metrics is not None:
            result['enableRequestMetrics'] = self.enable_request_metrics
        if self.log_begin_rule is not None:
            result['logBeginRule'] = self.log_begin_rule
        if self.logstore is not None:
            result['logstore'] = self.logstore
        if self.project is not None:
            result['project'] = self.project
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enableInstanceMetrics') is not None:
            self.enable_instance_metrics = m.get('enableInstanceMetrics')
        if m.get('enableRequestMetrics') is not None:
            self.enable_request_metrics = m.get('enableRequestMetrics')
        if m.get('logBeginRule') is not None:
            self.log_begin_rule = m.get('logBeginRule')
        if m.get('logstore') is not None:
            self.logstore = m.get('logstore')
        if m.get('project') is not None:
            self.project = m.get('project')
        return self


class NASMountConfig(TeaModel):
    def __init__(
        self,
        enable_tls: bool = None,
        mount_dir: str = None,
        server_addr: str = None,
    ):
        self.enable_tls = enable_tls
        self.mount_dir = mount_dir
        self.server_addr = server_addr

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_tls is not None:
            result['enableTLS'] = self.enable_tls
        if self.mount_dir is not None:
            result['mountDir'] = self.mount_dir
        if self.server_addr is not None:
            result['serverAddr'] = self.server_addr
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enableTLS') is not None:
            self.enable_tls = m.get('enableTLS')
        if m.get('mountDir') is not None:
            self.mount_dir = m.get('mountDir')
        if m.get('serverAddr') is not None:
            self.server_addr = m.get('serverAddr')
        return self


class NASConfig(TeaModel):
    def __init__(
        self,
        group_id: int = None,
        mount_points: List[NASMountConfig] = None,
        user_id: int = None,
    ):
        self.group_id = group_id
        self.mount_points = mount_points
        self.user_id = user_id

    def validate(self):
        if self.mount_points:
            for k in self.mount_points:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['groupId'] = self.group_id
        result['mountPoints'] = []
        if self.mount_points is not None:
            for k in self.mount_points:
                result['mountPoints'].append(k.to_map() if k else None)
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')
        self.mount_points = []
        if m.get('mountPoints') is not None:
            for k in m.get('mountPoints'):
                temp_model = NASMountConfig()
                self.mount_points.append(temp_model.from_map(k))
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class OSSMountPoint(TeaModel):
    def __init__(
        self,
        bucket_name: str = None,
        bucket_path: str = None,
        endpoint: str = None,
        mount_dir: str = None,
        read_only: bool = None,
    ):
        self.bucket_name = bucket_name
        self.bucket_path = bucket_path
        self.endpoint = endpoint
        self.mount_dir = mount_dir
        self.read_only = read_only

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_name is not None:
            result['bucketName'] = self.bucket_name
        if self.bucket_path is not None:
            result['bucketPath'] = self.bucket_path
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint
        if self.mount_dir is not None:
            result['mountDir'] = self.mount_dir
        if self.read_only is not None:
            result['readOnly'] = self.read_only
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bucketName') is not None:
            self.bucket_name = m.get('bucketName')
        if m.get('bucketPath') is not None:
            self.bucket_path = m.get('bucketPath')
        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')
        if m.get('mountDir') is not None:
            self.mount_dir = m.get('mountDir')
        if m.get('readOnly') is not None:
            self.read_only = m.get('readOnly')
        return self


class OSSMountConfig(TeaModel):
    def __init__(
        self,
        mount_points: List[OSSMountPoint] = None,
    ):
        self.mount_points = mount_points

    def validate(self):
        if self.mount_points:
            for k in self.mount_points:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['mountPoints'] = []
        if self.mount_points is not None:
            for k in self.mount_points:
                result['mountPoints'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.mount_points = []
        if m.get('mountPoints') is not None:
            for k in m.get('mountPoints'):
                temp_model = OSSMountPoint()
                self.mount_points.append(temp_model.from_map(k))
        return self


class TracingConfig(TeaModel):
    def __init__(
        self,
        params: Dict[str, str] = None,
        type: str = None,
    ):
        self.params = params
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.params is not None:
            result['params'] = self.params
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('params') is not None:
            self.params = m.get('params')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class VPCConfig(TeaModel):
    def __init__(
        self,
        security_group_id: str = None,
        v_switch_ids: List[str] = None,
        vpc_id: str = None,
    ):
        self.security_group_id = security_group_id
        self.v_switch_ids = v_switch_ids
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_group_id is not None:
            result['securityGroupId'] = self.security_group_id
        if self.v_switch_ids is not None:
            result['vSwitchIds'] = self.v_switch_ids
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('securityGroupId') is not None:
            self.security_group_id = m.get('securityGroupId')
        if m.get('vSwitchIds') is not None:
            self.v_switch_ids = m.get('vSwitchIds')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        return self


class CreateFunctionInput(TeaModel):
    def __init__(
        self,
        code: InputCodeLocation = None,
        cpu: float = None,
        custom_container_config: CustomContainerConfig = None,
        custom_dns: CustomDNS = None,
        custom_runtime_config: CustomRuntimeConfig = None,
        description: str = None,
        disk_size: int = None,
        environment_variables: Dict[str, str] = None,
        function_name: str = None,
        gpu_config: GPUConfig = None,
        handler: str = None,
        instance_concurrency: int = None,
        instance_lifecycle_config: InstanceLifecycleConfig = None,
        internet_access: bool = None,
        layers: List[str] = None,
        log_config: LogConfig = None,
        memory_size: int = None,
        nas_config: NASConfig = None,
        oss_mount_config: OSSMountConfig = None,
        role: str = None,
        runtime: str = None,
        timeout: int = None,
        tracing_config: TracingConfig = None,
        vpc_config: VPCConfig = None,
    ):
        self.code = code
        self.cpu = cpu
        self.custom_container_config = custom_container_config
        self.custom_dns = custom_dns
        self.custom_runtime_config = custom_runtime_config
        self.description = description
        self.disk_size = disk_size
        self.environment_variables = environment_variables
        # This parameter is required.
        self.function_name = function_name
        self.gpu_config = gpu_config
        # This parameter is required.
        self.handler = handler
        self.instance_concurrency = instance_concurrency
        self.instance_lifecycle_config = instance_lifecycle_config
        self.internet_access = internet_access
        self.layers = layers
        self.log_config = log_config
        self.memory_size = memory_size
        self.nas_config = nas_config
        self.oss_mount_config = oss_mount_config
        self.role = role
        # This parameter is required.
        self.runtime = runtime
        self.timeout = timeout
        self.tracing_config = tracing_config
        self.vpc_config = vpc_config

    def validate(self):
        if self.code:
            self.code.validate()
        if self.custom_container_config:
            self.custom_container_config.validate()
        if self.custom_dns:
            self.custom_dns.validate()
        if self.custom_runtime_config:
            self.custom_runtime_config.validate()
        if self.gpu_config:
            self.gpu_config.validate()
        if self.instance_lifecycle_config:
            self.instance_lifecycle_config.validate()
        if self.log_config:
            self.log_config.validate()
        if self.nas_config:
            self.nas_config.validate()
        if self.oss_mount_config:
            self.oss_mount_config.validate()
        if self.tracing_config:
            self.tracing_config.validate()
        if self.vpc_config:
            self.vpc_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code.to_map()
        if self.cpu is not None:
            result['cpu'] = self.cpu
        if self.custom_container_config is not None:
            result['customContainerConfig'] = self.custom_container_config.to_map()
        if self.custom_dns is not None:
            result['customDNS'] = self.custom_dns.to_map()
        if self.custom_runtime_config is not None:
            result['customRuntimeConfig'] = self.custom_runtime_config.to_map()
        if self.description is not None:
            result['description'] = self.description
        if self.disk_size is not None:
            result['diskSize'] = self.disk_size
        if self.environment_variables is not None:
            result['environmentVariables'] = self.environment_variables
        if self.function_name is not None:
            result['functionName'] = self.function_name
        if self.gpu_config is not None:
            result['gpuConfig'] = self.gpu_config.to_map()
        if self.handler is not None:
            result['handler'] = self.handler
        if self.instance_concurrency is not None:
            result['instanceConcurrency'] = self.instance_concurrency
        if self.instance_lifecycle_config is not None:
            result['instanceLifecycleConfig'] = self.instance_lifecycle_config.to_map()
        if self.internet_access is not None:
            result['internetAccess'] = self.internet_access
        if self.layers is not None:
            result['layers'] = self.layers
        if self.log_config is not None:
            result['logConfig'] = self.log_config.to_map()
        if self.memory_size is not None:
            result['memorySize'] = self.memory_size
        if self.nas_config is not None:
            result['nasConfig'] = self.nas_config.to_map()
        if self.oss_mount_config is not None:
            result['ossMountConfig'] = self.oss_mount_config.to_map()
        if self.role is not None:
            result['role'] = self.role
        if self.runtime is not None:
            result['runtime'] = self.runtime
        if self.timeout is not None:
            result['timeout'] = self.timeout
        if self.tracing_config is not None:
            result['tracingConfig'] = self.tracing_config.to_map()
        if self.vpc_config is not None:
            result['vpcConfig'] = self.vpc_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            temp_model = InputCodeLocation()
            self.code = temp_model.from_map(m['code'])
        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')
        if m.get('customContainerConfig') is not None:
            temp_model = CustomContainerConfig()
            self.custom_container_config = temp_model.from_map(m['customContainerConfig'])
        if m.get('customDNS') is not None:
            temp_model = CustomDNS()
            self.custom_dns = temp_model.from_map(m['customDNS'])
        if m.get('customRuntimeConfig') is not None:
            temp_model = CustomRuntimeConfig()
            self.custom_runtime_config = temp_model.from_map(m['customRuntimeConfig'])
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('diskSize') is not None:
            self.disk_size = m.get('diskSize')
        if m.get('environmentVariables') is not None:
            self.environment_variables = m.get('environmentVariables')
        if m.get('functionName') is not None:
            self.function_name = m.get('functionName')
        if m.get('gpuConfig') is not None:
            temp_model = GPUConfig()
            self.gpu_config = temp_model.from_map(m['gpuConfig'])
        if m.get('handler') is not None:
            self.handler = m.get('handler')
        if m.get('instanceConcurrency') is not None:
            self.instance_concurrency = m.get('instanceConcurrency')
        if m.get('instanceLifecycleConfig') is not None:
            temp_model = InstanceLifecycleConfig()
            self.instance_lifecycle_config = temp_model.from_map(m['instanceLifecycleConfig'])
        if m.get('internetAccess') is not None:
            self.internet_access = m.get('internetAccess')
        if m.get('layers') is not None:
            self.layers = m.get('layers')
        if m.get('logConfig') is not None:
            temp_model = LogConfig()
            self.log_config = temp_model.from_map(m['logConfig'])
        if m.get('memorySize') is not None:
            self.memory_size = m.get('memorySize')
        if m.get('nasConfig') is not None:
            temp_model = NASConfig()
            self.nas_config = temp_model.from_map(m['nasConfig'])
        if m.get('ossMountConfig') is not None:
            temp_model = OSSMountConfig()
            self.oss_mount_config = temp_model.from_map(m['ossMountConfig'])
        if m.get('role') is not None:
            self.role = m.get('role')
        if m.get('runtime') is not None:
            self.runtime = m.get('runtime')
        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')
        if m.get('tracingConfig') is not None:
            temp_model = TracingConfig()
            self.tracing_config = temp_model.from_map(m['tracingConfig'])
        if m.get('vpcConfig') is not None:
            temp_model = VPCConfig()
            self.vpc_config = temp_model.from_map(m['vpcConfig'])
        return self


class CreateLayerVersionInput(TeaModel):
    def __init__(
        self,
        code: InputCodeLocation = None,
        compatible_runtime: List[str] = None,
        description: str = None,
        license: str = None,
    ):
        self.code = code
        self.compatible_runtime = compatible_runtime
        self.description = description
        self.license = license

    def validate(self):
        if self.code:
            self.code.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code.to_map()
        if self.compatible_runtime is not None:
            result['compatibleRuntime'] = self.compatible_runtime
        if self.description is not None:
            result['description'] = self.description
        if self.license is not None:
            result['license'] = self.license
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            temp_model = InputCodeLocation()
            self.code = temp_model.from_map(m['code'])
        if m.get('compatibleRuntime') is not None:
            self.compatible_runtime = m.get('compatibleRuntime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('license') is not None:
            self.license = m.get('license')
        return self


class CreateTriggerInput(TeaModel):
    def __init__(
        self,
        description: str = None,
        invocation_role: str = None,
        qualifier: str = None,
        source_arn: str = None,
        trigger_config: str = None,
        trigger_name: str = None,
        trigger_type: str = None,
    ):
        self.description = description
        self.invocation_role = invocation_role
        self.qualifier = qualifier
        self.source_arn = source_arn
        # This parameter is required.
        self.trigger_config = trigger_config
        # This parameter is required.
        self.trigger_name = trigger_name
        # This parameter is required.
        self.trigger_type = trigger_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.invocation_role is not None:
            result['invocationRole'] = self.invocation_role
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        if self.source_arn is not None:
            result['sourceArn'] = self.source_arn
        if self.trigger_config is not None:
            result['triggerConfig'] = self.trigger_config
        if self.trigger_name is not None:
            result['triggerName'] = self.trigger_name
        if self.trigger_type is not None:
            result['triggerType'] = self.trigger_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('invocationRole') is not None:
            self.invocation_role = m.get('invocationRole')
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        if m.get('sourceArn') is not None:
            self.source_arn = m.get('sourceArn')
        if m.get('triggerConfig') is not None:
            self.trigger_config = m.get('triggerConfig')
        if m.get('triggerName') is not None:
            self.trigger_name = m.get('triggerName')
        if m.get('triggerType') is not None:
            self.trigger_type = m.get('triggerType')
        return self


class CreateVpcBindingInput(TeaModel):
    def __init__(
        self,
        vpc_id: str = None,
    ):
        # This parameter is required.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        return self


class CustomDomain(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        api_version: str = None,
        auth_config: AuthConfig = None,
        cert_config: CertConfig = None,
        created_time: str = None,
        domain_name: str = None,
        last_modified_time: str = None,
        protocol: str = None,
        route_config: RouteConfig = None,
        subdomain_count: str = None,
        tls_config: TLSConfig = None,
        waf_config: WAFConfig = None,
    ):
        self.account_id = account_id
        self.api_version = api_version
        self.auth_config = auth_config
        self.cert_config = cert_config
        self.created_time = created_time
        self.domain_name = domain_name
        self.last_modified_time = last_modified_time
        self.protocol = protocol
        self.route_config = route_config
        self.subdomain_count = subdomain_count
        self.tls_config = tls_config
        self.waf_config = waf_config

    def validate(self):
        if self.auth_config:
            self.auth_config.validate()
        if self.cert_config:
            self.cert_config.validate()
        if self.route_config:
            self.route_config.validate()
        if self.tls_config:
            self.tls_config.validate()
        if self.waf_config:
            self.waf_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['accountId'] = self.account_id
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.auth_config is not None:
            result['authConfig'] = self.auth_config.to_map()
        if self.cert_config is not None:
            result['certConfig'] = self.cert_config.to_map()
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.domain_name is not None:
            result['domainName'] = self.domain_name
        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time
        if self.protocol is not None:
            result['protocol'] = self.protocol
        if self.route_config is not None:
            result['routeConfig'] = self.route_config.to_map()
        if self.subdomain_count is not None:
            result['subdomainCount'] = self.subdomain_count
        if self.tls_config is not None:
            result['tlsConfig'] = self.tls_config.to_map()
        if self.waf_config is not None:
            result['wafConfig'] = self.waf_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('authConfig') is not None:
            temp_model = AuthConfig()
            self.auth_config = temp_model.from_map(m['authConfig'])
        if m.get('certConfig') is not None:
            temp_model = CertConfig()
            self.cert_config = temp_model.from_map(m['certConfig'])
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('domainName') is not None:
            self.domain_name = m.get('domainName')
        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('routeConfig') is not None:
            temp_model = RouteConfig()
            self.route_config = temp_model.from_map(m['routeConfig'])
        if m.get('subdomainCount') is not None:
            self.subdomain_count = m.get('subdomainCount')
        if m.get('tlsConfig') is not None:
            temp_model = TLSConfig()
            self.tls_config = temp_model.from_map(m['tlsConfig'])
        if m.get('wafConfig') is not None:
            temp_model = WAFConfig()
            self.waf_config = temp_model.from_map(m['wafConfig'])
        return self


class DeadLetterQueue(TeaModel):
    def __init__(
        self,
        arn: str = None,
    ):
        self.arn = arn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        return self


class DeliveryOption(TeaModel):
    def __init__(
        self,
        concurrency: int = None,
        event_schema: str = None,
    ):
        self.concurrency = concurrency
        self.event_schema = event_schema

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.concurrency is not None:
            result['concurrency'] = self.concurrency
        if self.event_schema is not None:
            result['eventSchema'] = self.event_schema
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('concurrency') is not None:
            self.concurrency = m.get('concurrency')
        if m.get('eventSchema') is not None:
            self.event_schema = m.get('eventSchema')
        return self


class Error(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
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
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class EventSinkConfig(TeaModel):
    def __init__(
        self,
        delivery_option: DeliveryOption = None,
    ):
        self.delivery_option = delivery_option

    def validate(self):
        if self.delivery_option:
            self.delivery_option.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delivery_option is not None:
            result['deliveryOption'] = self.delivery_option.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deliveryOption') is not None:
            temp_model = DeliveryOption()
            self.delivery_option = temp_model.from_map(m['deliveryOption'])
        return self


class SourceDTSParameters(TeaModel):
    def __init__(
        self,
        broker_url: str = None,
        init_check_point: int = None,
        password: str = None,
        region_id: str = None,
        sid: str = None,
        task_id: str = None,
        topic: str = None,
        username: str = None,
    ):
        self.broker_url = broker_url
        self.init_check_point = init_check_point
        self.password = password
        self.region_id = region_id
        self.sid = sid
        self.task_id = task_id
        self.topic = topic
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.broker_url is not None:
            result['BrokerUrl'] = self.broker_url
        if self.init_check_point is not None:
            result['InitCheckPoint'] = self.init_check_point
        if self.password is not None:
            result['Password'] = self.password
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.sid is not None:
            result['Sid'] = self.sid
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BrokerUrl') is not None:
            self.broker_url = m.get('BrokerUrl')
        if m.get('InitCheckPoint') is not None:
            self.init_check_point = m.get('InitCheckPoint')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Sid') is not None:
            self.sid = m.get('Sid')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class SourceKafkaParameters(TeaModel):
    def __init__(
        self,
        consumer_group: str = None,
        instance_id: str = None,
        network: str = None,
        offset_reset: str = None,
        region_id: str = None,
        security_group_id: str = None,
        topic: str = None,
        v_switch_ids: str = None,
        vpc_id: str = None,
    ):
        self.consumer_group = consumer_group
        self.instance_id = instance_id
        self.network = network
        self.offset_reset = offset_reset
        self.region_id = region_id
        self.security_group_id = security_group_id
        self.topic = topic
        self.v_switch_ids = v_switch_ids
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consumer_group is not None:
            result['ConsumerGroup'] = self.consumer_group
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.network is not None:
            result['Network'] = self.network
        if self.offset_reset is not None:
            result['OffsetReset'] = self.offset_reset
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsumerGroup') is not None:
            self.consumer_group = m.get('ConsumerGroup')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Network') is not None:
            self.network = m.get('Network')
        if m.get('OffsetReset') is not None:
            self.offset_reset = m.get('OffsetReset')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class SourceMNSParameters(TeaModel):
    def __init__(
        self,
        is_base_64decode: bool = None,
        queue_name: str = None,
        region_id: str = None,
    ):
        self.is_base_64decode = is_base_64decode
        self.queue_name = queue_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_base_64decode is not None:
            result['IsBase64Decode'] = self.is_base_64decode
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsBase64Decode') is not None:
            self.is_base_64decode = m.get('IsBase64Decode')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class SourceMQTTParameters(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
        topic: str = None,
    ):
        self.instance_id = instance_id
        self.region_id = region_id
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class SourceRabbitMQParameters(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        queue_name: str = None,
        region_id: str = None,
        virtual_host_name: str = None,
    ):
        self.instance_id = instance_id
        self.queue_name = queue_name
        self.region_id = region_id
        self.virtual_host_name = virtual_host_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.virtual_host_name is not None:
            result['VirtualHostName'] = self.virtual_host_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VirtualHostName') is not None:
            self.virtual_host_name = m.get('VirtualHostName')
        return self


class SourceRocketMQParameters(TeaModel):
    def __init__(
        self,
        auth_type: str = None,
        filter_type: str = None,
        group_id: str = None,
        instance_endpoint: str = None,
        instance_id: str = None,
        instance_network: str = None,
        instance_password: str = None,
        instance_security_group_id: str = None,
        instance_type: str = None,
        instance_username: str = None,
        instance_vswitch_ids: str = None,
        instance_vpc_id: str = None,
        offset: str = None,
        region_id: str = None,
        tag: str = None,
        timestamp: int = None,
        topic: str = None,
    ):
        self.auth_type = auth_type
        self.filter_type = filter_type
        self.group_id = group_id
        self.instance_endpoint = instance_endpoint
        self.instance_id = instance_id
        self.instance_network = instance_network
        self.instance_password = instance_password
        self.instance_security_group_id = instance_security_group_id
        self.instance_type = instance_type
        self.instance_username = instance_username
        self.instance_vswitch_ids = instance_vswitch_ids
        self.instance_vpc_id = instance_vpc_id
        self.offset = offset
        self.region_id = region_id
        self.tag = tag
        self.timestamp = timestamp
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_type is not None:
            result['AuthType'] = self.auth_type
        if self.filter_type is not None:
            result['FilterType'] = self.filter_type
        if self.group_id is not None:
            result['GroupID'] = self.group_id
        if self.instance_endpoint is not None:
            result['InstanceEndpoint'] = self.instance_endpoint
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_network is not None:
            result['InstanceNetwork'] = self.instance_network
        if self.instance_password is not None:
            result['InstancePassword'] = self.instance_password
        if self.instance_security_group_id is not None:
            result['InstanceSecurityGroupId'] = self.instance_security_group_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.instance_username is not None:
            result['InstanceUsername'] = self.instance_username
        if self.instance_vswitch_ids is not None:
            result['InstanceVSwitchIds'] = self.instance_vswitch_ids
        if self.instance_vpc_id is not None:
            result['InstanceVpcId'] = self.instance_vpc_id
        if self.offset is not None:
            result['Offset'] = self.offset
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')
        if m.get('FilterType') is not None:
            self.filter_type = m.get('FilterType')
        if m.get('GroupID') is not None:
            self.group_id = m.get('GroupID')
        if m.get('InstanceEndpoint') is not None:
            self.instance_endpoint = m.get('InstanceEndpoint')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceNetwork') is not None:
            self.instance_network = m.get('InstanceNetwork')
        if m.get('InstancePassword') is not None:
            self.instance_password = m.get('InstancePassword')
        if m.get('InstanceSecurityGroupId') is not None:
            self.instance_security_group_id = m.get('InstanceSecurityGroupId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('InstanceUsername') is not None:
            self.instance_username = m.get('InstanceUsername')
        if m.get('InstanceVSwitchIds') is not None:
            self.instance_vswitch_ids = m.get('InstanceVSwitchIds')
        if m.get('InstanceVpcId') is not None:
            self.instance_vpc_id = m.get('InstanceVpcId')
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class EventSourceParameters(TeaModel):
    def __init__(
        self,
        source_dtsparameters: SourceDTSParameters = None,
        source_kafka_parameters: SourceKafkaParameters = None,
        source_mnsparameters: SourceMNSParameters = None,
        source_mqttparameters: SourceMQTTParameters = None,
        source_rabbit_mqparameters: SourceRabbitMQParameters = None,
        source_rocket_mqparameters: SourceRocketMQParameters = None,
    ):
        self.source_dtsparameters = source_dtsparameters
        self.source_kafka_parameters = source_kafka_parameters
        self.source_mnsparameters = source_mnsparameters
        self.source_mqttparameters = source_mqttparameters
        self.source_rabbit_mqparameters = source_rabbit_mqparameters
        self.source_rocket_mqparameters = source_rocket_mqparameters

    def validate(self):
        if self.source_dtsparameters:
            self.source_dtsparameters.validate()
        if self.source_kafka_parameters:
            self.source_kafka_parameters.validate()
        if self.source_mnsparameters:
            self.source_mnsparameters.validate()
        if self.source_mqttparameters:
            self.source_mqttparameters.validate()
        if self.source_rabbit_mqparameters:
            self.source_rabbit_mqparameters.validate()
        if self.source_rocket_mqparameters:
            self.source_rocket_mqparameters.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_dtsparameters is not None:
            result['sourceDTSParameters'] = self.source_dtsparameters.to_map()
        if self.source_kafka_parameters is not None:
            result['sourceKafkaParameters'] = self.source_kafka_parameters.to_map()
        if self.source_mnsparameters is not None:
            result['sourceMNSParameters'] = self.source_mnsparameters.to_map()
        if self.source_mqttparameters is not None:
            result['sourceMQTTParameters'] = self.source_mqttparameters.to_map()
        if self.source_rabbit_mqparameters is not None:
            result['sourceRabbitMQParameters'] = self.source_rabbit_mqparameters.to_map()
        if self.source_rocket_mqparameters is not None:
            result['sourceRocketMQParameters'] = self.source_rocket_mqparameters.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sourceDTSParameters') is not None:
            temp_model = SourceDTSParameters()
            self.source_dtsparameters = temp_model.from_map(m['sourceDTSParameters'])
        if m.get('sourceKafkaParameters') is not None:
            temp_model = SourceKafkaParameters()
            self.source_kafka_parameters = temp_model.from_map(m['sourceKafkaParameters'])
        if m.get('sourceMNSParameters') is not None:
            temp_model = SourceMNSParameters()
            self.source_mnsparameters = temp_model.from_map(m['sourceMNSParameters'])
        if m.get('sourceMQTTParameters') is not None:
            temp_model = SourceMQTTParameters()
            self.source_mqttparameters = temp_model.from_map(m['sourceMQTTParameters'])
        if m.get('sourceRabbitMQParameters') is not None:
            temp_model = SourceRabbitMQParameters()
            self.source_rabbit_mqparameters = temp_model.from_map(m['sourceRabbitMQParameters'])
        if m.get('sourceRocketMQParameters') is not None:
            temp_model = SourceRocketMQParameters()
            self.source_rocket_mqparameters = temp_model.from_map(m['sourceRocketMQParameters'])
        return self


class EventSourceConfig(TeaModel):
    def __init__(
        self,
        event_source_parameters: EventSourceParameters = None,
        event_source_type: str = None,
    ):
        self.event_source_parameters = event_source_parameters
        self.event_source_type = event_source_type

    def validate(self):
        if self.event_source_parameters:
            self.event_source_parameters.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_source_parameters is not None:
            result['eventSourceParameters'] = self.event_source_parameters.to_map()
        if self.event_source_type is not None:
            result['eventSourceType'] = self.event_source_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('eventSourceParameters') is not None:
            temp_model = EventSourceParameters()
            self.event_source_parameters = temp_model.from_map(m['eventSourceParameters'])
        if m.get('eventSourceType') is not None:
            self.event_source_type = m.get('eventSourceType')
        return self


class RetryStrategy(TeaModel):
    def __init__(
        self,
        push_retry_strategy: str = None,
    ):
        self.push_retry_strategy = push_retry_strategy

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.push_retry_strategy is not None:
            result['PushRetryStrategy'] = self.push_retry_strategy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PushRetryStrategy') is not None:
            self.push_retry_strategy = m.get('PushRetryStrategy')
        return self


class RunOptions(TeaModel):
    def __init__(
        self,
        batch_window: BatchWindow = None,
        dead_letter_queue: DeadLetterQueue = None,
        errors_tolerance: str = None,
        mode: str = None,
        retry_strategy: RetryStrategy = None,
    ):
        self.batch_window = batch_window
        self.dead_letter_queue = dead_letter_queue
        self.errors_tolerance = errors_tolerance
        self.mode = mode
        self.retry_strategy = retry_strategy

    def validate(self):
        if self.batch_window:
            self.batch_window.validate()
        if self.dead_letter_queue:
            self.dead_letter_queue.validate()
        if self.retry_strategy:
            self.retry_strategy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.batch_window is not None:
            result['batchWindow'] = self.batch_window.to_map()
        if self.dead_letter_queue is not None:
            result['deadLetterQueue'] = self.dead_letter_queue.to_map()
        if self.errors_tolerance is not None:
            result['errorsTolerance'] = self.errors_tolerance
        if self.mode is not None:
            result['mode'] = self.mode
        if self.retry_strategy is not None:
            result['retryStrategy'] = self.retry_strategy.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('batchWindow') is not None:
            temp_model = BatchWindow()
            self.batch_window = temp_model.from_map(m['batchWindow'])
        if m.get('deadLetterQueue') is not None:
            temp_model = DeadLetterQueue()
            self.dead_letter_queue = temp_model.from_map(m['deadLetterQueue'])
        if m.get('errorsTolerance') is not None:
            self.errors_tolerance = m.get('errorsTolerance')
        if m.get('mode') is not None:
            self.mode = m.get('mode')
        if m.get('retryStrategy') is not None:
            temp_model = RetryStrategy()
            self.retry_strategy = temp_model.from_map(m['retryStrategy'])
        return self


class EventBridgeTriggerConfig(TeaModel):
    def __init__(
        self,
        async_invocation_type: bool = None,
        event_rule_filter_pattern: str = None,
        event_sink_config: EventSinkConfig = None,
        event_source_config: EventSourceConfig = None,
        run_options: RunOptions = None,
        trigger_enable: bool = None,
    ):
        self.async_invocation_type = async_invocation_type
        self.event_rule_filter_pattern = event_rule_filter_pattern
        self.event_sink_config = event_sink_config
        self.event_source_config = event_source_config
        self.run_options = run_options
        self.trigger_enable = trigger_enable

    def validate(self):
        if self.event_sink_config:
            self.event_sink_config.validate()
        if self.event_source_config:
            self.event_source_config.validate()
        if self.run_options:
            self.run_options.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.async_invocation_type is not None:
            result['asyncInvocationType'] = self.async_invocation_type
        if self.event_rule_filter_pattern is not None:
            result['eventRuleFilterPattern'] = self.event_rule_filter_pattern
        if self.event_sink_config is not None:
            result['eventSinkConfig'] = self.event_sink_config.to_map()
        if self.event_source_config is not None:
            result['eventSourceConfig'] = self.event_source_config.to_map()
        if self.run_options is not None:
            result['runOptions'] = self.run_options.to_map()
        if self.trigger_enable is not None:
            result['triggerEnable'] = self.trigger_enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('asyncInvocationType') is not None:
            self.async_invocation_type = m.get('asyncInvocationType')
        if m.get('eventRuleFilterPattern') is not None:
            self.event_rule_filter_pattern = m.get('eventRuleFilterPattern')
        if m.get('eventSinkConfig') is not None:
            temp_model = EventSinkConfig()
            self.event_sink_config = temp_model.from_map(m['eventSinkConfig'])
        if m.get('eventSourceConfig') is not None:
            temp_model = EventSourceConfig()
            self.event_source_config = temp_model.from_map(m['eventSourceConfig'])
        if m.get('runOptions') is not None:
            temp_model = RunOptions()
            self.run_options = temp_model.from_map(m['runOptions'])
        if m.get('triggerEnable') is not None:
            self.trigger_enable = m.get('triggerEnable')
        return self


class Key(TeaModel):
    def __init__(
        self,
        prefix: str = None,
        suffix: str = None,
    ):
        self.prefix = prefix
        self.suffix = suffix

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.prefix is not None:
            result['prefix'] = self.prefix
        if self.suffix is not None:
            result['suffix'] = self.suffix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('prefix') is not None:
            self.prefix = m.get('prefix')
        if m.get('suffix') is not None:
            self.suffix = m.get('suffix')
        return self


class Filter(TeaModel):
    def __init__(
        self,
        key: Key = None,
    ):
        self.key = key

    def validate(self):
        if self.key:
            self.key.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            temp_model = Key()
            self.key = temp_model.from_map(m['key'])
        return self


class FunctionLayer(TeaModel):
    def __init__(
        self,
        arn: str = None,
        size: int = None,
    ):
        self.arn = arn
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['arn'] = self.arn
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('arn') is not None:
            self.arn = m.get('arn')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class Function(TeaModel):
    def __init__(
        self,
        code_checksum: str = None,
        code_size: int = None,
        cpu: float = None,
        created_time: str = None,
        custom_container_config: CustomContainerConfig = None,
        custom_dns: CustomDNS = None,
        custom_runtime_config: CustomRuntimeConfig = None,
        description: str = None,
        disk_size: int = None,
        environment_variables: Dict[str, str] = None,
        function_arn: str = None,
        function_id: str = None,
        function_name: str = None,
        gpu_config: GPUConfig = None,
        handler: str = None,
        instance_concurrency: int = None,
        instance_lifecycle_config: InstanceLifecycleConfig = None,
        internet_access: bool = None,
        last_modified_time: str = None,
        last_update_status: str = None,
        last_update_status_reason: str = None,
        last_update_status_reason_code: str = None,
        layers: List[FunctionLayer] = None,
        log_config: LogConfig = None,
        memory_size: int = None,
        nas_config: NASConfig = None,
        oss_mount_config: OSSMountConfig = None,
        role: str = None,
        runtime: str = None,
        state: str = None,
        state_reason: str = None,
        state_reason_code: str = None,
        timeout: int = None,
        tracing_config: TracingConfig = None,
        vpc_config: VPCConfig = None,
    ):
        self.code_checksum = code_checksum
        self.code_size = code_size
        self.cpu = cpu
        self.created_time = created_time
        self.custom_container_config = custom_container_config
        self.custom_dns = custom_dns
        self.custom_runtime_config = custom_runtime_config
        self.description = description
        self.disk_size = disk_size
        self.environment_variables = environment_variables
        self.function_arn = function_arn
        self.function_id = function_id
        self.function_name = function_name
        self.gpu_config = gpu_config
        self.handler = handler
        self.instance_concurrency = instance_concurrency
        self.instance_lifecycle_config = instance_lifecycle_config
        self.internet_access = internet_access
        self.last_modified_time = last_modified_time
        self.last_update_status = last_update_status
        self.last_update_status_reason = last_update_status_reason
        self.last_update_status_reason_code = last_update_status_reason_code
        self.layers = layers
        self.log_config = log_config
        self.memory_size = memory_size
        self.nas_config = nas_config
        self.oss_mount_config = oss_mount_config
        self.role = role
        self.runtime = runtime
        self.state = state
        self.state_reason = state_reason
        self.state_reason_code = state_reason_code
        self.timeout = timeout
        self.tracing_config = tracing_config
        self.vpc_config = vpc_config

    def validate(self):
        if self.custom_container_config:
            self.custom_container_config.validate()
        if self.custom_dns:
            self.custom_dns.validate()
        if self.custom_runtime_config:
            self.custom_runtime_config.validate()
        if self.gpu_config:
            self.gpu_config.validate()
        if self.instance_lifecycle_config:
            self.instance_lifecycle_config.validate()
        if self.layers:
            for k in self.layers:
                if k:
                    k.validate()
        if self.log_config:
            self.log_config.validate()
        if self.nas_config:
            self.nas_config.validate()
        if self.oss_mount_config:
            self.oss_mount_config.validate()
        if self.tracing_config:
            self.tracing_config.validate()
        if self.vpc_config:
            self.vpc_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code_checksum is not None:
            result['codeChecksum'] = self.code_checksum
        if self.code_size is not None:
            result['codeSize'] = self.code_size
        if self.cpu is not None:
            result['cpu'] = self.cpu
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.custom_container_config is not None:
            result['customContainerConfig'] = self.custom_container_config.to_map()
        if self.custom_dns is not None:
            result['customDNS'] = self.custom_dns.to_map()
        if self.custom_runtime_config is not None:
            result['customRuntimeConfig'] = self.custom_runtime_config.to_map()
        if self.description is not None:
            result['description'] = self.description
        if self.disk_size is not None:
            result['diskSize'] = self.disk_size
        if self.environment_variables is not None:
            result['environmentVariables'] = self.environment_variables
        if self.function_arn is not None:
            result['functionArn'] = self.function_arn
        if self.function_id is not None:
            result['functionId'] = self.function_id
        if self.function_name is not None:
            result['functionName'] = self.function_name
        if self.gpu_config is not None:
            result['gpuConfig'] = self.gpu_config.to_map()
        if self.handler is not None:
            result['handler'] = self.handler
        if self.instance_concurrency is not None:
            result['instanceConcurrency'] = self.instance_concurrency
        if self.instance_lifecycle_config is not None:
            result['instanceLifecycleConfig'] = self.instance_lifecycle_config.to_map()
        if self.internet_access is not None:
            result['internetAccess'] = self.internet_access
        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time
        if self.last_update_status is not None:
            result['lastUpdateStatus'] = self.last_update_status
        if self.last_update_status_reason is not None:
            result['lastUpdateStatusReason'] = self.last_update_status_reason
        if self.last_update_status_reason_code is not None:
            result['lastUpdateStatusReasonCode'] = self.last_update_status_reason_code
        result['layers'] = []
        if self.layers is not None:
            for k in self.layers:
                result['layers'].append(k.to_map() if k else None)
        if self.log_config is not None:
            result['logConfig'] = self.log_config.to_map()
        if self.memory_size is not None:
            result['memorySize'] = self.memory_size
        if self.nas_config is not None:
            result['nasConfig'] = self.nas_config.to_map()
        if self.oss_mount_config is not None:
            result['ossMountConfig'] = self.oss_mount_config.to_map()
        if self.role is not None:
            result['role'] = self.role
        if self.runtime is not None:
            result['runtime'] = self.runtime
        if self.state is not None:
            result['state'] = self.state
        if self.state_reason is not None:
            result['stateReason'] = self.state_reason
        if self.state_reason_code is not None:
            result['stateReasonCode'] = self.state_reason_code
        if self.timeout is not None:
            result['timeout'] = self.timeout
        if self.tracing_config is not None:
            result['tracingConfig'] = self.tracing_config.to_map()
        if self.vpc_config is not None:
            result['vpcConfig'] = self.vpc_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('codeChecksum') is not None:
            self.code_checksum = m.get('codeChecksum')
        if m.get('codeSize') is not None:
            self.code_size = m.get('codeSize')
        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('customContainerConfig') is not None:
            temp_model = CustomContainerConfig()
            self.custom_container_config = temp_model.from_map(m['customContainerConfig'])
        if m.get('customDNS') is not None:
            temp_model = CustomDNS()
            self.custom_dns = temp_model.from_map(m['customDNS'])
        if m.get('customRuntimeConfig') is not None:
            temp_model = CustomRuntimeConfig()
            self.custom_runtime_config = temp_model.from_map(m['customRuntimeConfig'])
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('diskSize') is not None:
            self.disk_size = m.get('diskSize')
        if m.get('environmentVariables') is not None:
            self.environment_variables = m.get('environmentVariables')
        if m.get('functionArn') is not None:
            self.function_arn = m.get('functionArn')
        if m.get('functionId') is not None:
            self.function_id = m.get('functionId')
        if m.get('functionName') is not None:
            self.function_name = m.get('functionName')
        if m.get('gpuConfig') is not None:
            temp_model = GPUConfig()
            self.gpu_config = temp_model.from_map(m['gpuConfig'])
        if m.get('handler') is not None:
            self.handler = m.get('handler')
        if m.get('instanceConcurrency') is not None:
            self.instance_concurrency = m.get('instanceConcurrency')
        if m.get('instanceLifecycleConfig') is not None:
            temp_model = InstanceLifecycleConfig()
            self.instance_lifecycle_config = temp_model.from_map(m['instanceLifecycleConfig'])
        if m.get('internetAccess') is not None:
            self.internet_access = m.get('internetAccess')
        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')
        if m.get('lastUpdateStatus') is not None:
            self.last_update_status = m.get('lastUpdateStatus')
        if m.get('lastUpdateStatusReason') is not None:
            self.last_update_status_reason = m.get('lastUpdateStatusReason')
        if m.get('lastUpdateStatusReasonCode') is not None:
            self.last_update_status_reason_code = m.get('lastUpdateStatusReasonCode')
        self.layers = []
        if m.get('layers') is not None:
            for k in m.get('layers'):
                temp_model = FunctionLayer()
                self.layers.append(temp_model.from_map(k))
        if m.get('logConfig') is not None:
            temp_model = LogConfig()
            self.log_config = temp_model.from_map(m['logConfig'])
        if m.get('memorySize') is not None:
            self.memory_size = m.get('memorySize')
        if m.get('nasConfig') is not None:
            temp_model = NASConfig()
            self.nas_config = temp_model.from_map(m['nasConfig'])
        if m.get('ossMountConfig') is not None:
            temp_model = OSSMountConfig()
            self.oss_mount_config = temp_model.from_map(m['ossMountConfig'])
        if m.get('role') is not None:
            self.role = m.get('role')
        if m.get('runtime') is not None:
            self.runtime = m.get('runtime')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('stateReason') is not None:
            self.state_reason = m.get('stateReason')
        if m.get('stateReasonCode') is not None:
            self.state_reason_code = m.get('stateReasonCode')
        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')
        if m.get('tracingConfig') is not None:
            temp_model = TracingConfig()
            self.tracing_config = temp_model.from_map(m['tracingConfig'])
        if m.get('vpcConfig') is not None:
            temp_model = VPCConfig()
            self.vpc_config = temp_model.from_map(m['vpcConfig'])
        return self


class GetResourceTagsOutput(TeaModel):
    def __init__(
        self,
        resouce_type: str = None,
        resource_arn: str = None,
        tags: Dict[str, str] = None,
    ):
        self.resouce_type = resouce_type
        self.resource_arn = resource_arn
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resouce_type is not None:
            result['resouceType'] = self.resouce_type
        if self.resource_arn is not None:
            result['resourceArn'] = self.resource_arn
        if self.tags is not None:
            result['tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resouceType') is not None:
            self.resouce_type = m.get('resouceType')
        if m.get('resourceArn') is not None:
            self.resource_arn = m.get('resourceArn')
        if m.get('tags') is not None:
            self.tags = m.get('tags')
        return self


class HTTPTrigger(TeaModel):
    def __init__(
        self,
        url_internet: str = None,
        url_intranet: str = None,
    ):
        self.url_internet = url_internet
        self.url_intranet = url_intranet

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url_internet is not None:
            result['urlInternet'] = self.url_internet
        if self.url_intranet is not None:
            result['urlIntranet'] = self.url_intranet
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('urlInternet') is not None:
            self.url_internet = m.get('urlInternet')
        if m.get('urlIntranet') is not None:
            self.url_intranet = m.get('urlIntranet')
        return self


class HTTPTriggerConfig(TeaModel):
    def __init__(
        self,
        auth_config: str = None,
        auth_type: str = None,
        disable_urlinternet: bool = None,
        methods: List[str] = None,
    ):
        self.auth_config = auth_config
        self.auth_type = auth_type
        self.disable_urlinternet = disable_urlinternet
        self.methods = methods

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_config is not None:
            result['authConfig'] = self.auth_config
        if self.auth_type is not None:
            result['authType'] = self.auth_type
        if self.disable_urlinternet is not None:
            result['disableURLInternet'] = self.disable_urlinternet
        if self.methods is not None:
            result['methods'] = self.methods
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authConfig') is not None:
            self.auth_config = m.get('authConfig')
        if m.get('authType') is not None:
            self.auth_type = m.get('authType')
        if m.get('disableURLInternet') is not None:
            self.disable_urlinternet = m.get('disableURLInternet')
        if m.get('methods') is not None:
            self.methods = m.get('methods')
        return self


class InstanceInfo(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        version_id: str = None,
    ):
        self.instance_id = instance_id
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.version_id is not None:
            result['versionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('versionId') is not None:
            self.version_id = m.get('versionId')
        return self


class JobConfig(TeaModel):
    def __init__(
        self,
        max_retry_time: int = None,
        trigger_interval: int = None,
    ):
        self.max_retry_time = max_retry_time
        self.trigger_interval = trigger_interval

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_retry_time is not None:
            result['maxRetryTime'] = self.max_retry_time
        if self.trigger_interval is not None:
            result['triggerInterval'] = self.trigger_interval
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxRetryTime') is not None:
            self.max_retry_time = m.get('maxRetryTime')
        if m.get('triggerInterval') is not None:
            self.trigger_interval = m.get('triggerInterval')
        return self


class OutputCodeLocation(TeaModel):
    def __init__(
        self,
        location: str = None,
        repository_type: str = None,
    ):
        self.location = location
        self.repository_type = repository_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.location is not None:
            result['location'] = self.location
        if self.repository_type is not None:
            result['repositoryType'] = self.repository_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('location') is not None:
            self.location = m.get('location')
        if m.get('repositoryType') is not None:
            self.repository_type = m.get('repositoryType')
        return self


class Layer(TeaModel):
    def __init__(
        self,
        acl: str = None,
        code: OutputCodeLocation = None,
        code_checksum: str = None,
        code_size: int = None,
        compatible_runtime: List[str] = None,
        create_time: str = None,
        description: str = None,
        layer_name: str = None,
        layer_version_arn: str = None,
        license: str = None,
        version: int = None,
    ):
        self.acl = acl
        self.code = code
        self.code_checksum = code_checksum
        self.code_size = code_size
        self.compatible_runtime = compatible_runtime
        self.create_time = create_time
        self.description = description
        # This parameter is required.
        self.layer_name = layer_name
        self.layer_version_arn = layer_version_arn
        self.license = license
        self.version = version

    def validate(self):
        if self.code:
            self.code.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl is not None:
            result['acl'] = self.acl
        if self.code is not None:
            result['code'] = self.code.to_map()
        if self.code_checksum is not None:
            result['codeChecksum'] = self.code_checksum
        if self.code_size is not None:
            result['codeSize'] = self.code_size
        if self.compatible_runtime is not None:
            result['compatibleRuntime'] = self.compatible_runtime
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.layer_name is not None:
            result['layerName'] = self.layer_name
        if self.layer_version_arn is not None:
            result['layerVersionArn'] = self.layer_version_arn
        if self.license is not None:
            result['license'] = self.license
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('acl') is not None:
            self.acl = m.get('acl')
        if m.get('code') is not None:
            temp_model = OutputCodeLocation()
            self.code = temp_model.from_map(m['code'])
        if m.get('codeChecksum') is not None:
            self.code_checksum = m.get('codeChecksum')
        if m.get('codeSize') is not None:
            self.code_size = m.get('codeSize')
        if m.get('compatibleRuntime') is not None:
            self.compatible_runtime = m.get('compatibleRuntime')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('layerName') is not None:
            self.layer_name = m.get('layerName')
        if m.get('layerVersionArn') is not None:
            self.layer_version_arn = m.get('layerVersionArn')
        if m.get('license') is not None:
            self.license = m.get('license')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class ListAliasesOutput(TeaModel):
    def __init__(
        self,
        aliases: List[Alias] = None,
        next_token: str = None,
    ):
        self.aliases = aliases
        self.next_token = next_token

    def validate(self):
        if self.aliases:
            for k in self.aliases:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['aliases'] = []
        if self.aliases is not None:
            for k in self.aliases:
                result['aliases'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.aliases = []
        if m.get('aliases') is not None:
            for k in m.get('aliases'):
                temp_model = Alias()
                self.aliases.append(temp_model.from_map(k))
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        return self


class ListAsyncInvokeConfigOutput(TeaModel):
    def __init__(
        self,
        configs: List[AsyncConfig] = None,
        next_token: str = None,
    ):
        self.configs = configs
        self.next_token = next_token

    def validate(self):
        if self.configs:
            for k in self.configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['configs'] = []
        if self.configs is not None:
            for k in self.configs:
                result['configs'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.configs = []
        if m.get('configs') is not None:
            for k in m.get('configs'):
                temp_model = AsyncConfig()
                self.configs.append(temp_model.from_map(k))
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        return self


class ListAsyncTaskOutput(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        tasks: List[AsyncTask] = None,
    ):
        self.next_token = next_token
        self.tasks = tasks

    def validate(self):
        if self.tasks:
            for k in self.tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        result['tasks'] = []
        if self.tasks is not None:
            for k in self.tasks:
                result['tasks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        self.tasks = []
        if m.get('tasks') is not None:
            for k in m.get('tasks'):
                temp_model = AsyncTask()
                self.tasks.append(temp_model.from_map(k))
        return self


class ListConcurrencyConfigsOutput(TeaModel):
    def __init__(
        self,
        configs: List[ConcurrencyConfig] = None,
        next_token: str = None,
    ):
        self.configs = configs
        self.next_token = next_token

    def validate(self):
        if self.configs:
            for k in self.configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['configs'] = []
        if self.configs is not None:
            for k in self.configs:
                result['configs'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.configs = []
        if m.get('configs') is not None:
            for k in m.get('configs'):
                temp_model = ConcurrencyConfig()
                self.configs.append(temp_model.from_map(k))
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        return self


class ListCustomDomainOutput(TeaModel):
    def __init__(
        self,
        custom_domains: List[CustomDomain] = None,
        next_token: str = None,
    ):
        self.custom_domains = custom_domains
        self.next_token = next_token

    def validate(self):
        if self.custom_domains:
            for k in self.custom_domains:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['customDomains'] = []
        if self.custom_domains is not None:
            for k in self.custom_domains:
                result['customDomains'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.custom_domains = []
        if m.get('customDomains') is not None:
            for k in m.get('customDomains'):
                temp_model = CustomDomain()
                self.custom_domains.append(temp_model.from_map(k))
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        return self


class ListFunctionsOutput(TeaModel):
    def __init__(
        self,
        functions: List[Function] = None,
        next_token: str = None,
    ):
        self.functions = functions
        self.next_token = next_token

    def validate(self):
        if self.functions:
            for k in self.functions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['functions'] = []
        if self.functions is not None:
            for k in self.functions:
                result['functions'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.functions = []
        if m.get('functions') is not None:
            for k in m.get('functions'):
                temp_model = Function()
                self.functions.append(temp_model.from_map(k))
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        return self


class ListInstancesOutput(TeaModel):
    def __init__(
        self,
        instances: List[InstanceInfo] = None,
    ):
        self.instances = instances

    def validate(self):
        if self.instances:
            for k in self.instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['instances'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instances = []
        if m.get('instances') is not None:
            for k in m.get('instances'):
                temp_model = InstanceInfo()
                self.instances.append(temp_model.from_map(k))
        return self


class ListLayerVersionOutput(TeaModel):
    def __init__(
        self,
        layers: List[Layer] = None,
        next_version: int = None,
    ):
        self.layers = layers
        self.next_version = next_version

    def validate(self):
        if self.layers:
            for k in self.layers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['layers'] = []
        if self.layers is not None:
            for k in self.layers:
                result['layers'].append(k.to_map() if k else None)
        if self.next_version is not None:
            result['nextVersion'] = self.next_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.layers = []
        if m.get('layers') is not None:
            for k in m.get('layers'):
                temp_model = Layer()
                self.layers.append(temp_model.from_map(k))
        if m.get('nextVersion') is not None:
            self.next_version = m.get('nextVersion')
        return self


class ListLayersOutput(TeaModel):
    def __init__(
        self,
        layers: List[Layer] = None,
        next_token: str = None,
    ):
        self.layers = layers
        self.next_token = next_token

    def validate(self):
        if self.layers:
            for k in self.layers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['layers'] = []
        if self.layers is not None:
            for k in self.layers:
                result['layers'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.layers = []
        if m.get('layers') is not None:
            for k in m.get('layers'):
                temp_model = Layer()
                self.layers.append(temp_model.from_map(k))
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        return self


class ScheduledAction(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        name: str = None,
        schedule_expression: str = None,
        start_time: str = None,
        target: int = None,
    ):
        self.end_time = end_time
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.schedule_expression = schedule_expression
        self.start_time = start_time
        # This parameter is required.
        self.target = target

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.name is not None:
            result['name'] = self.name
        if self.schedule_expression is not None:
            result['scheduleExpression'] = self.schedule_expression
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.target is not None:
            result['target'] = self.target
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('scheduleExpression') is not None:
            self.schedule_expression = m.get('scheduleExpression')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('target') is not None:
            self.target = m.get('target')
        return self


class TargetTrackingPolicy(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        max_capacity: int = None,
        metric_target: float = None,
        metric_type: str = None,
        min_capacity: int = None,
        name: str = None,
        start_time: str = None,
    ):
        self.end_time = end_time
        # This parameter is required.
        self.max_capacity = max_capacity
        # This parameter is required.
        self.metric_target = metric_target
        # This parameter is required.
        self.metric_type = metric_type
        # This parameter is required.
        self.min_capacity = min_capacity
        # This parameter is required.
        self.name = name
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.max_capacity is not None:
            result['maxCapacity'] = self.max_capacity
        if self.metric_target is not None:
            result['metricTarget'] = self.metric_target
        if self.metric_type is not None:
            result['metricType'] = self.metric_type
        if self.min_capacity is not None:
            result['minCapacity'] = self.min_capacity
        if self.name is not None:
            result['name'] = self.name
        if self.start_time is not None:
            result['startTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('maxCapacity') is not None:
            self.max_capacity = m.get('maxCapacity')
        if m.get('metricTarget') is not None:
            self.metric_target = m.get('metricTarget')
        if m.get('metricType') is not None:
            self.metric_type = m.get('metricType')
        if m.get('minCapacity') is not None:
            self.min_capacity = m.get('minCapacity')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        return self


class ProvisionConfig(TeaModel):
    def __init__(
        self,
        always_allocate_cpu: bool = None,
        current: int = None,
        current_error: str = None,
        function_arn: str = None,
        scheduled_actions: List[ScheduledAction] = None,
        target: int = None,
        target_tracking_policies: List[TargetTrackingPolicy] = None,
    ):
        self.always_allocate_cpu = always_allocate_cpu
        self.current = current
        self.current_error = current_error
        self.function_arn = function_arn
        self.scheduled_actions = scheduled_actions
        self.target = target
        self.target_tracking_policies = target_tracking_policies

    def validate(self):
        if self.scheduled_actions:
            for k in self.scheduled_actions:
                if k:
                    k.validate()
        if self.target_tracking_policies:
            for k in self.target_tracking_policies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.always_allocate_cpu is not None:
            result['alwaysAllocateCPU'] = self.always_allocate_cpu
        if self.current is not None:
            result['current'] = self.current
        if self.current_error is not None:
            result['currentError'] = self.current_error
        if self.function_arn is not None:
            result['functionArn'] = self.function_arn
        result['scheduledActions'] = []
        if self.scheduled_actions is not None:
            for k in self.scheduled_actions:
                result['scheduledActions'].append(k.to_map() if k else None)
        if self.target is not None:
            result['target'] = self.target
        result['targetTrackingPolicies'] = []
        if self.target_tracking_policies is not None:
            for k in self.target_tracking_policies:
                result['targetTrackingPolicies'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alwaysAllocateCPU') is not None:
            self.always_allocate_cpu = m.get('alwaysAllocateCPU')
        if m.get('current') is not None:
            self.current = m.get('current')
        if m.get('currentError') is not None:
            self.current_error = m.get('currentError')
        if m.get('functionArn') is not None:
            self.function_arn = m.get('functionArn')
        self.scheduled_actions = []
        if m.get('scheduledActions') is not None:
            for k in m.get('scheduledActions'):
                temp_model = ScheduledAction()
                self.scheduled_actions.append(temp_model.from_map(k))
        if m.get('target') is not None:
            self.target = m.get('target')
        self.target_tracking_policies = []
        if m.get('targetTrackingPolicies') is not None:
            for k in m.get('targetTrackingPolicies'):
                temp_model = TargetTrackingPolicy()
                self.target_tracking_policies.append(temp_model.from_map(k))
        return self


class ListProvisionConfigsOutput(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        provision_configs: List[ProvisionConfig] = None,
    ):
        self.next_token = next_token
        self.provision_configs = provision_configs

    def validate(self):
        if self.provision_configs:
            for k in self.provision_configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        result['provisionConfigs'] = []
        if self.provision_configs is not None:
            for k in self.provision_configs:
                result['provisionConfigs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        self.provision_configs = []
        if m.get('provisionConfigs') is not None:
            for k in m.get('provisionConfigs'):
                temp_model = ProvisionConfig()
                self.provision_configs.append(temp_model.from_map(k))
        return self


class TagResource(TeaModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_type: str = None,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class ListTagResourcesOutput(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        tag_resources: List[TagResource] = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.tag_resources = tag_resources

    def validate(self):
        if self.tag_resources:
            for k in self.tag_resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TagResources'] = []
        if self.tag_resources is not None:
            for k in self.tag_resources:
                result['TagResources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tag_resources = []
        if m.get('TagResources') is not None:
            for k in m.get('TagResources'):
                temp_model = TagResource()
                self.tag_resources.append(temp_model.from_map(k))
        return self


class Resource(TeaModel):
    def __init__(
        self,
        resouce_type: str = None,
        resource_arn: str = None,
        tags: Dict[str, str] = None,
    ):
        self.resouce_type = resouce_type
        self.resource_arn = resource_arn
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resouce_type is not None:
            result['resouceType'] = self.resouce_type
        if self.resource_arn is not None:
            result['resourceArn'] = self.resource_arn
        if self.tags is not None:
            result['tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resouceType') is not None:
            self.resouce_type = m.get('resouceType')
        if m.get('resourceArn') is not None:
            self.resource_arn = m.get('resourceArn')
        if m.get('tags') is not None:
            self.tags = m.get('tags')
        return self


class ListTaggedResourcesOutput(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        resources: List[Resource] = None,
    ):
        self.next_token = next_token
        self.resources = resources

    def validate(self):
        if self.resources:
            for k in self.resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        result['resources'] = []
        if self.resources is not None:
            for k in self.resources:
                result['resources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        self.resources = []
        if m.get('resources') is not None:
            for k in m.get('resources'):
                temp_model = Resource()
                self.resources.append(temp_model.from_map(k))
        return self


class Trigger(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        description: str = None,
        http_trigger: HTTPTrigger = None,
        invocation_role: str = None,
        last_modified_time: str = None,
        qualifier: str = None,
        source_arn: str = None,
        status: str = None,
        target_arn: str = None,
        trigger_config: str = None,
        trigger_id: str = None,
        trigger_name: str = None,
        trigger_type: str = None,
    ):
        self.created_time = created_time
        self.description = description
        self.http_trigger = http_trigger
        self.invocation_role = invocation_role
        self.last_modified_time = last_modified_time
        self.qualifier = qualifier
        self.source_arn = source_arn
        self.status = status
        self.target_arn = target_arn
        self.trigger_config = trigger_config
        self.trigger_id = trigger_id
        self.trigger_name = trigger_name
        self.trigger_type = trigger_type

    def validate(self):
        if self.http_trigger:
            self.http_trigger.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.description is not None:
            result['description'] = self.description
        if self.http_trigger is not None:
            result['httpTrigger'] = self.http_trigger.to_map()
        if self.invocation_role is not None:
            result['invocationRole'] = self.invocation_role
        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        if self.source_arn is not None:
            result['sourceArn'] = self.source_arn
        if self.status is not None:
            result['status'] = self.status
        if self.target_arn is not None:
            result['targetArn'] = self.target_arn
        if self.trigger_config is not None:
            result['triggerConfig'] = self.trigger_config
        if self.trigger_id is not None:
            result['triggerId'] = self.trigger_id
        if self.trigger_name is not None:
            result['triggerName'] = self.trigger_name
        if self.trigger_type is not None:
            result['triggerType'] = self.trigger_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('httpTrigger') is not None:
            temp_model = HTTPTrigger()
            self.http_trigger = temp_model.from_map(m['httpTrigger'])
        if m.get('invocationRole') is not None:
            self.invocation_role = m.get('invocationRole')
        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        if m.get('sourceArn') is not None:
            self.source_arn = m.get('sourceArn')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('targetArn') is not None:
            self.target_arn = m.get('targetArn')
        if m.get('triggerConfig') is not None:
            self.trigger_config = m.get('triggerConfig')
        if m.get('triggerId') is not None:
            self.trigger_id = m.get('triggerId')
        if m.get('triggerName') is not None:
            self.trigger_name = m.get('triggerName')
        if m.get('triggerType') is not None:
            self.trigger_type = m.get('triggerType')
        return self


class ListTriggersOutput(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        triggers: List[Trigger] = None,
    ):
        self.next_token = next_token
        self.triggers = triggers

    def validate(self):
        if self.triggers:
            for k in self.triggers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        result['triggers'] = []
        if self.triggers is not None:
            for k in self.triggers:
                result['triggers'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        self.triggers = []
        if m.get('triggers') is not None:
            for k in m.get('triggers'):
                temp_model = Trigger()
                self.triggers.append(temp_model.from_map(k))
        return self


class Version(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        description: str = None,
        last_modified_time: str = None,
        version_id: str = None,
    ):
        self.created_time = created_time
        self.description = description
        self.last_modified_time = last_modified_time
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.description is not None:
            result['description'] = self.description
        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time
        if self.version_id is not None:
            result['versionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')
        if m.get('versionId') is not None:
            self.version_id = m.get('versionId')
        return self


class ListVersionsOutput(TeaModel):
    def __init__(
        self,
        direction: str = None,
        next_token: str = None,
        versions: List[Version] = None,
    ):
        self.direction = direction
        self.next_token = next_token
        self.versions = versions

    def validate(self):
        if self.versions:
            for k in self.versions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.direction is not None:
            result['direction'] = self.direction
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        result['versions'] = []
        if self.versions is not None:
            for k in self.versions:
                result['versions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('direction') is not None:
            self.direction = m.get('direction')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        self.versions = []
        if m.get('versions') is not None:
            for k in m.get('versions'):
                temp_model = Version()
                self.versions.append(temp_model.from_map(k))
        return self


class ListVpcBindingsOutput(TeaModel):
    def __init__(
        self,
        vpc_ids: List[str] = None,
    ):
        self.vpc_ids = vpc_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vpc_ids is not None:
            result['vpcIds'] = self.vpc_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('vpcIds') is not None:
            self.vpc_ids = m.get('vpcIds')
        return self


class MNSTopicTriggerConfig(TeaModel):
    def __init__(
        self,
        filter_tag: str = None,
        notify_content_format: str = None,
        notify_strategy: str = None,
    ):
        self.filter_tag = filter_tag
        self.notify_content_format = notify_content_format
        self.notify_strategy = notify_strategy

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter_tag is not None:
            result['filterTag'] = self.filter_tag
        if self.notify_content_format is not None:
            result['notifyContentFormat'] = self.notify_content_format
        if self.notify_strategy is not None:
            result['notifyStrategy'] = self.notify_strategy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filterTag') is not None:
            self.filter_tag = m.get('filterTag')
        if m.get('notifyContentFormat') is not None:
            self.notify_content_format = m.get('notifyContentFormat')
        if m.get('notifyStrategy') is not None:
            self.notify_strategy = m.get('notifyStrategy')
        return self


class OSSTriggerConfig(TeaModel):
    def __init__(
        self,
        events: List[str] = None,
        filter: Filter = None,
    ):
        self.events = events
        self.filter = filter

    def validate(self):
        if self.filter:
            self.filter.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.events is not None:
            result['events'] = self.events
        if self.filter is not None:
            result['filter'] = self.filter.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('events') is not None:
            self.events = m.get('events')
        if m.get('filter') is not None:
            temp_model = Filter()
            self.filter = temp_model.from_map(m['filter'])
        return self


class OutputFuncCode(TeaModel):
    def __init__(
        self,
        checksum: str = None,
        url: str = None,
    ):
        self.checksum = checksum
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.checksum is not None:
            result['checksum'] = self.checksum
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('checksum') is not None:
            self.checksum = m.get('checksum')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class PublishVersionInput(TeaModel):
    def __init__(
        self,
        description: str = None,
    ):
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        return self


class PutAsyncInvokeConfigInput(TeaModel):
    def __init__(
        self,
        async_task: bool = None,
        destination_config: DestinationConfig = None,
        max_async_event_age_in_seconds: int = None,
        max_async_retry_attempts: int = None,
    ):
        self.async_task = async_task
        self.destination_config = destination_config
        self.max_async_event_age_in_seconds = max_async_event_age_in_seconds
        self.max_async_retry_attempts = max_async_retry_attempts

    def validate(self):
        if self.destination_config:
            self.destination_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.async_task is not None:
            result['asyncTask'] = self.async_task
        if self.destination_config is not None:
            result['destinationConfig'] = self.destination_config.to_map()
        if self.max_async_event_age_in_seconds is not None:
            result['maxAsyncEventAgeInSeconds'] = self.max_async_event_age_in_seconds
        if self.max_async_retry_attempts is not None:
            result['maxAsyncRetryAttempts'] = self.max_async_retry_attempts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('asyncTask') is not None:
            self.async_task = m.get('asyncTask')
        if m.get('destinationConfig') is not None:
            temp_model = DestinationConfig()
            self.destination_config = temp_model.from_map(m['destinationConfig'])
        if m.get('maxAsyncEventAgeInSeconds') is not None:
            self.max_async_event_age_in_seconds = m.get('maxAsyncEventAgeInSeconds')
        if m.get('maxAsyncRetryAttempts') is not None:
            self.max_async_retry_attempts = m.get('maxAsyncRetryAttempts')
        return self


class PutConcurrencyInput(TeaModel):
    def __init__(
        self,
        reserved_concurrency: int = None,
    ):
        # This parameter is required.
        self.reserved_concurrency = reserved_concurrency

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.reserved_concurrency is not None:
            result['reservedConcurrency'] = self.reserved_concurrency
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('reservedConcurrency') is not None:
            self.reserved_concurrency = m.get('reservedConcurrency')
        return self


class PutProvisionConfigInput(TeaModel):
    def __init__(
        self,
        always_allocate_cpu: bool = None,
        scheduled_actions: List[ScheduledAction] = None,
        target: int = None,
        target_tracking_policies: List[TargetTrackingPolicy] = None,
    ):
        self.always_allocate_cpu = always_allocate_cpu
        self.scheduled_actions = scheduled_actions
        # This parameter is required.
        self.target = target
        self.target_tracking_policies = target_tracking_policies

    def validate(self):
        if self.scheduled_actions:
            for k in self.scheduled_actions:
                if k:
                    k.validate()
        if self.target_tracking_policies:
            for k in self.target_tracking_policies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.always_allocate_cpu is not None:
            result['alwaysAllocateCPU'] = self.always_allocate_cpu
        result['scheduledActions'] = []
        if self.scheduled_actions is not None:
            for k in self.scheduled_actions:
                result['scheduledActions'].append(k.to_map() if k else None)
        if self.target is not None:
            result['target'] = self.target
        result['targetTrackingPolicies'] = []
        if self.target_tracking_policies is not None:
            for k in self.target_tracking_policies:
                result['targetTrackingPolicies'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alwaysAllocateCPU') is not None:
            self.always_allocate_cpu = m.get('alwaysAllocateCPU')
        self.scheduled_actions = []
        if m.get('scheduledActions') is not None:
            for k in m.get('scheduledActions'):
                temp_model = ScheduledAction()
                self.scheduled_actions.append(temp_model.from_map(k))
        if m.get('target') is not None:
            self.target = m.get('target')
        self.target_tracking_policies = []
        if m.get('targetTrackingPolicies') is not None:
            for k in m.get('targetTrackingPolicies'):
                temp_model = TargetTrackingPolicy()
                self.target_tracking_policies.append(temp_model.from_map(k))
        return self


class SLSTriggerLogConfig(TeaModel):
    def __init__(
        self,
        logstore: str = None,
        project: str = None,
    ):
        self.logstore = logstore
        self.project = project

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logstore is not None:
            result['logstore'] = self.logstore
        if self.project is not None:
            result['project'] = self.project
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('logstore') is not None:
            self.logstore = m.get('logstore')
        if m.get('project') is not None:
            self.project = m.get('project')
        return self


class SourceConfig(TeaModel):
    def __init__(
        self,
        logstore: str = None,
        start_time: int = None,
    ):
        self.logstore = logstore
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logstore is not None:
            result['logstore'] = self.logstore
        if self.start_time is not None:
            result['startTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('logstore') is not None:
            self.logstore = m.get('logstore')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        return self


class SLSTriggerConfig(TeaModel):
    def __init__(
        self,
        enable: bool = None,
        function_parameter: Dict[str, str] = None,
        job_config: JobConfig = None,
        log_config: SLSTriggerLogConfig = None,
        source_config: SourceConfig = None,
    ):
        self.enable = enable
        self.function_parameter = function_parameter
        self.job_config = job_config
        self.log_config = log_config
        self.source_config = source_config

    def validate(self):
        if self.job_config:
            self.job_config.validate()
        if self.log_config:
            self.log_config.validate()
        if self.source_config:
            self.source_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable is not None:
            result['enable'] = self.enable
        if self.function_parameter is not None:
            result['functionParameter'] = self.function_parameter
        if self.job_config is not None:
            result['jobConfig'] = self.job_config.to_map()
        if self.log_config is not None:
            result['logConfig'] = self.log_config.to_map()
        if self.source_config is not None:
            result['sourceConfig'] = self.source_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('functionParameter') is not None:
            self.function_parameter = m.get('functionParameter')
        if m.get('jobConfig') is not None:
            temp_model = JobConfig()
            self.job_config = temp_model.from_map(m['jobConfig'])
        if m.get('logConfig') is not None:
            temp_model = SLSTriggerLogConfig()
            self.log_config = temp_model.from_map(m['logConfig'])
        if m.get('sourceConfig') is not None:
            temp_model = SourceConfig()
            self.source_config = temp_model.from_map(m['sourceConfig'])
        return self


class Tag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class TagResourceInput(TeaModel):
    def __init__(
        self,
        resource_arn: str = None,
        tags: Dict[str, str] = None,
    ):
        # This parameter is required.
        self.resource_arn = resource_arn
        # This parameter is required.
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_arn is not None:
            result['resourceArn'] = self.resource_arn
        if self.tags is not None:
            result['tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resourceArn') is not None:
            self.resource_arn = m.get('resourceArn')
        if m.get('tags') is not None:
            self.tags = m.get('tags')
        return self


class TagResourcesInput(TeaModel):
    def __init__(
        self,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag: List[Tag] = None,
    ):
        # This parameter is required.
        self.resource_id = resource_id
        self.resource_type = resource_type
        # This parameter is required.
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = Tag()
                self.tag.append(temp_model.from_map(k))
        return self


class TimerTriggerConfig(TeaModel):
    def __init__(
        self,
        cron_expression: str = None,
        enable: bool = None,
        payload: str = None,
    ):
        self.cron_expression = cron_expression
        self.enable = enable
        self.payload = payload

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cron_expression is not None:
            result['cronExpression'] = self.cron_expression
        if self.enable is not None:
            result['enable'] = self.enable
        if self.payload is not None:
            result['payload'] = self.payload
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cronExpression') is not None:
            self.cron_expression = m.get('cronExpression')
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('payload') is not None:
            self.payload = m.get('payload')
        return self


class UpdateAliasInput(TeaModel):
    def __init__(
        self,
        additional_version_weight: Dict[str, float] = None,
        description: str = None,
        version_id: str = None,
    ):
        self.additional_version_weight = additional_version_weight
        self.description = description
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.additional_version_weight is not None:
            result['additionalVersionWeight'] = self.additional_version_weight
        if self.description is not None:
            result['description'] = self.description
        if self.version_id is not None:
            result['versionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('additionalVersionWeight') is not None:
            self.additional_version_weight = m.get('additionalVersionWeight')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('versionId') is not None:
            self.version_id = m.get('versionId')
        return self


class UpdateCustomDomainInput(TeaModel):
    def __init__(
        self,
        auth_config: AuthConfig = None,
        cert_config: CertConfig = None,
        protocol: str = None,
        route_config: RouteConfig = None,
        tls_config: TLSConfig = None,
        waf_config: WAFConfig = None,
    ):
        self.auth_config = auth_config
        self.cert_config = cert_config
        self.protocol = protocol
        self.route_config = route_config
        self.tls_config = tls_config
        self.waf_config = waf_config

    def validate(self):
        if self.auth_config:
            self.auth_config.validate()
        if self.cert_config:
            self.cert_config.validate()
        if self.route_config:
            self.route_config.validate()
        if self.tls_config:
            self.tls_config.validate()
        if self.waf_config:
            self.waf_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_config is not None:
            result['authConfig'] = self.auth_config.to_map()
        if self.cert_config is not None:
            result['certConfig'] = self.cert_config.to_map()
        if self.protocol is not None:
            result['protocol'] = self.protocol
        if self.route_config is not None:
            result['routeConfig'] = self.route_config.to_map()
        if self.tls_config is not None:
            result['tlsConfig'] = self.tls_config.to_map()
        if self.waf_config is not None:
            result['wafConfig'] = self.waf_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authConfig') is not None:
            temp_model = AuthConfig()
            self.auth_config = temp_model.from_map(m['authConfig'])
        if m.get('certConfig') is not None:
            temp_model = CertConfig()
            self.cert_config = temp_model.from_map(m['certConfig'])
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('routeConfig') is not None:
            temp_model = RouteConfig()
            self.route_config = temp_model.from_map(m['routeConfig'])
        if m.get('tlsConfig') is not None:
            temp_model = TLSConfig()
            self.tls_config = temp_model.from_map(m['tlsConfig'])
        if m.get('wafConfig') is not None:
            temp_model = WAFConfig()
            self.waf_config = temp_model.from_map(m['wafConfig'])
        return self


class UpdateFunctionInput(TeaModel):
    def __init__(
        self,
        code: InputCodeLocation = None,
        cpu: float = None,
        custom_container_config: CustomContainerConfig = None,
        custom_dns: CustomDNS = None,
        custom_runtime_config: CustomRuntimeConfig = None,
        description: str = None,
        disk_size: int = None,
        environment_variables: Dict[str, str] = None,
        gpu_config: GPUConfig = None,
        handler: str = None,
        instance_concurrency: int = None,
        instance_lifecycle_config: InstanceLifecycleConfig = None,
        internet_access: bool = None,
        layers: List[str] = None,
        log_config: LogConfig = None,
        memory_size: int = None,
        nas_config: NASConfig = None,
        oss_mount_config: OSSMountConfig = None,
        role: str = None,
        runtime: str = None,
        timeout: int = None,
        tracing_config: TracingConfig = None,
        vpc_config: VPCConfig = None,
    ):
        self.code = code
        self.cpu = cpu
        self.custom_container_config = custom_container_config
        self.custom_dns = custom_dns
        self.custom_runtime_config = custom_runtime_config
        self.description = description
        self.disk_size = disk_size
        self.environment_variables = environment_variables
        self.gpu_config = gpu_config
        self.handler = handler
        self.instance_concurrency = instance_concurrency
        self.instance_lifecycle_config = instance_lifecycle_config
        self.internet_access = internet_access
        self.layers = layers
        self.log_config = log_config
        self.memory_size = memory_size
        self.nas_config = nas_config
        self.oss_mount_config = oss_mount_config
        self.role = role
        self.runtime = runtime
        self.timeout = timeout
        self.tracing_config = tracing_config
        self.vpc_config = vpc_config

    def validate(self):
        if self.code:
            self.code.validate()
        if self.custom_container_config:
            self.custom_container_config.validate()
        if self.custom_dns:
            self.custom_dns.validate()
        if self.custom_runtime_config:
            self.custom_runtime_config.validate()
        if self.gpu_config:
            self.gpu_config.validate()
        if self.instance_lifecycle_config:
            self.instance_lifecycle_config.validate()
        if self.log_config:
            self.log_config.validate()
        if self.nas_config:
            self.nas_config.validate()
        if self.oss_mount_config:
            self.oss_mount_config.validate()
        if self.tracing_config:
            self.tracing_config.validate()
        if self.vpc_config:
            self.vpc_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code.to_map()
        if self.cpu is not None:
            result['cpu'] = self.cpu
        if self.custom_container_config is not None:
            result['customContainerConfig'] = self.custom_container_config.to_map()
        if self.custom_dns is not None:
            result['customDNS'] = self.custom_dns.to_map()
        if self.custom_runtime_config is not None:
            result['customRuntimeConfig'] = self.custom_runtime_config.to_map()
        if self.description is not None:
            result['description'] = self.description
        if self.disk_size is not None:
            result['diskSize'] = self.disk_size
        if self.environment_variables is not None:
            result['environmentVariables'] = self.environment_variables
        if self.gpu_config is not None:
            result['gpuConfig'] = self.gpu_config.to_map()
        if self.handler is not None:
            result['handler'] = self.handler
        if self.instance_concurrency is not None:
            result['instanceConcurrency'] = self.instance_concurrency
        if self.instance_lifecycle_config is not None:
            result['instanceLifecycleConfig'] = self.instance_lifecycle_config.to_map()
        if self.internet_access is not None:
            result['internetAccess'] = self.internet_access
        if self.layers is not None:
            result['layers'] = self.layers
        if self.log_config is not None:
            result['logConfig'] = self.log_config.to_map()
        if self.memory_size is not None:
            result['memorySize'] = self.memory_size
        if self.nas_config is not None:
            result['nasConfig'] = self.nas_config.to_map()
        if self.oss_mount_config is not None:
            result['ossMountConfig'] = self.oss_mount_config.to_map()
        if self.role is not None:
            result['role'] = self.role
        if self.runtime is not None:
            result['runtime'] = self.runtime
        if self.timeout is not None:
            result['timeout'] = self.timeout
        if self.tracing_config is not None:
            result['tracingConfig'] = self.tracing_config.to_map()
        if self.vpc_config is not None:
            result['vpcConfig'] = self.vpc_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            temp_model = InputCodeLocation()
            self.code = temp_model.from_map(m['code'])
        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')
        if m.get('customContainerConfig') is not None:
            temp_model = CustomContainerConfig()
            self.custom_container_config = temp_model.from_map(m['customContainerConfig'])
        if m.get('customDNS') is not None:
            temp_model = CustomDNS()
            self.custom_dns = temp_model.from_map(m['customDNS'])
        if m.get('customRuntimeConfig') is not None:
            temp_model = CustomRuntimeConfig()
            self.custom_runtime_config = temp_model.from_map(m['customRuntimeConfig'])
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('diskSize') is not None:
            self.disk_size = m.get('diskSize')
        if m.get('environmentVariables') is not None:
            self.environment_variables = m.get('environmentVariables')
        if m.get('gpuConfig') is not None:
            temp_model = GPUConfig()
            self.gpu_config = temp_model.from_map(m['gpuConfig'])
        if m.get('handler') is not None:
            self.handler = m.get('handler')
        if m.get('instanceConcurrency') is not None:
            self.instance_concurrency = m.get('instanceConcurrency')
        if m.get('instanceLifecycleConfig') is not None:
            temp_model = InstanceLifecycleConfig()
            self.instance_lifecycle_config = temp_model.from_map(m['instanceLifecycleConfig'])
        if m.get('internetAccess') is not None:
            self.internet_access = m.get('internetAccess')
        if m.get('layers') is not None:
            self.layers = m.get('layers')
        if m.get('logConfig') is not None:
            temp_model = LogConfig()
            self.log_config = temp_model.from_map(m['logConfig'])
        if m.get('memorySize') is not None:
            self.memory_size = m.get('memorySize')
        if m.get('nasConfig') is not None:
            temp_model = NASConfig()
            self.nas_config = temp_model.from_map(m['nasConfig'])
        if m.get('ossMountConfig') is not None:
            temp_model = OSSMountConfig()
            self.oss_mount_config = temp_model.from_map(m['ossMountConfig'])
        if m.get('role') is not None:
            self.role = m.get('role')
        if m.get('runtime') is not None:
            self.runtime = m.get('runtime')
        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')
        if m.get('tracingConfig') is not None:
            temp_model = TracingConfig()
            self.tracing_config = temp_model.from_map(m['tracingConfig'])
        if m.get('vpcConfig') is not None:
            temp_model = VPCConfig()
            self.vpc_config = temp_model.from_map(m['vpcConfig'])
        return self


class UpdateTriggerInput(TeaModel):
    def __init__(
        self,
        description: str = None,
        invocation_role: str = None,
        qualifier: str = None,
        trigger_config: str = None,
    ):
        self.description = description
        self.invocation_role = invocation_role
        self.qualifier = qualifier
        self.trigger_config = trigger_config

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.invocation_role is not None:
            result['invocationRole'] = self.invocation_role
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        if self.trigger_config is not None:
            result['triggerConfig'] = self.trigger_config
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('invocationRole') is not None:
            self.invocation_role = m.get('invocationRole')
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        if m.get('triggerConfig') is not None:
            self.trigger_config = m.get('triggerConfig')
        return self


class CreateAliasRequest(TeaModel):
    def __init__(
        self,
        body: CreateAliasInput = None,
    ):
        # The request parameters for creating an alias.
        # 
        # This parameter is required.
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = CreateAliasInput()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAliasResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Alias = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = Alias()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCustomDomainRequest(TeaModel):
    def __init__(
        self,
        body: CreateCustomDomainInput = None,
    ):
        # The information about the custom domain name.
        # 
        # This parameter is required.
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = CreateCustomDomainInput()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCustomDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CustomDomain = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = CustomDomain()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFunctionRequest(TeaModel):
    def __init__(
        self,
        body: CreateFunctionInput = None,
    ):
        # The information about function configurations.
        # 
        # This parameter is required.
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = CreateFunctionInput()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFunctionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Function = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = Function()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLayerVersionRequest(TeaModel):
    def __init__(
        self,
        body: CreateLayerVersionInput = None,
    ):
        # The information about layer configurations.
        # 
        # This parameter is required.
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = CreateLayerVersionInput()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLayerVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Layer = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = Layer()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTriggerRequest(TeaModel):
    def __init__(
        self,
        body: CreateTriggerInput = None,
    ):
        # The trigger configurations.
        # 
        # This parameter is required.
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = CreateTriggerInput()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTriggerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Trigger = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = Trigger()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateVpcBindingRequest(TeaModel):
    def __init__(
        self,
        body: CreateVpcBindingInput = None,
    ):
        # The configurations of the virtual private cloud (VPC) binding.
        # 
        # This parameter is required.
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = CreateVpcBindingInput()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateVpcBindingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeleteAliasResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeleteAsyncInvokeConfigRequest(TeaModel):
    def __init__(
        self,
        qualifier: str = None,
    ):
        # The version or alias of the function.
        self.qualifier = qualifier

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        return self


class DeleteAsyncInvokeConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeleteConcurrencyConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeleteCustomDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeleteFunctionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeleteFunctionVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeleteLayerVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeleteProvisionConfigRequest(TeaModel):
    def __init__(
        self,
        qualifier: str = None,
    ):
        # The function alias or LATEST.
        self.qualifier = qualifier

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        return self


class DeleteProvisionConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeleteTriggerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeleteVpcBindingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class GetAliasResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Alias = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = Alias()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAsyncInvokeConfigRequest(TeaModel):
    def __init__(
        self,
        qualifier: str = None,
    ):
        # The version or alias of the function.
        self.qualifier = qualifier

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        return self


class GetAsyncInvokeConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AsyncConfig = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = AsyncConfig()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAsyncTaskRequest(TeaModel):
    def __init__(
        self,
        qualifier: str = None,
    ):
        # The function version or alias.
        self.qualifier = qualifier

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        return self


class GetAsyncTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AsyncTask = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = AsyncTask()
            self.body = temp_model.from_map(m['body'])
        return self


class GetConcurrencyConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ConcurrencyConfig = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ConcurrencyConfig()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCustomDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CustomDomain = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = CustomDomain()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFunctionRequest(TeaModel):
    def __init__(
        self,
        qualifier: str = None,
    ):
        # The version or alias of the function.
        self.qualifier = qualifier

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        return self


class GetFunctionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Function = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = Function()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFunctionCodeRequest(TeaModel):
    def __init__(
        self,
        qualifier: str = None,
    ):
        # The version or alias of the function.
        self.qualifier = qualifier

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        return self


class GetFunctionCodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OutputFuncCode = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = OutputFuncCode()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLayerVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Layer = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = Layer()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLayerVersionByArnResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Layer = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = Layer()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProvisionConfigRequest(TeaModel):
    def __init__(
        self,
        qualifier: str = None,
    ):
        # The function alias or LATEST.
        self.qualifier = qualifier

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        return self


class GetProvisionConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ProvisionConfig = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ProvisionConfig()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTriggerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Trigger = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = Trigger()
            self.body = temp_model.from_map(m['body'])
        return self


class InvokeFunctionHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_async_task_id: str = None,
        x_fc_invocation_type: str = None,
        x_fc_log_type: str = None,
    ):
        self.common_headers = common_headers
        self.x_fc_async_task_id = x_fc_async_task_id
        # The type of function invocation. Valid values: Sync and Async.
        self.x_fc_invocation_type = x_fc_invocation_type
        # The log type of function invocation. Valid values: None and Tail.
        self.x_fc_log_type = x_fc_log_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_async_task_id is not None:
            result['x-fc-async-task-id'] = self.x_fc_async_task_id
        if self.x_fc_invocation_type is not None:
            result['x-fc-invocation-type'] = self.x_fc_invocation_type
        if self.x_fc_log_type is not None:
            result['x-fc-log-type'] = self.x_fc_log_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-fc-async-task-id') is not None:
            self.x_fc_async_task_id = m.get('x-fc-async-task-id')
        if m.get('x-fc-invocation-type') is not None:
            self.x_fc_invocation_type = m.get('x-fc-invocation-type')
        if m.get('x-fc-log-type') is not None:
            self.x_fc_log_type = m.get('x-fc-log-type')
        return self


class InvokeFunctionRequest(TeaModel):
    def __init__(
        self,
        body: BinaryIO = None,
        qualifier: str = None,
    ):
        # The request parameters of function invocation.
        self.body = body
        # The version or alias of the function.
        self.qualifier = qualifier

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        return self


class InvokeFunctionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BinaryIO = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        pass

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
            result['body'] = self.body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class ListAliasesRequest(TeaModel):
    def __init__(
        self,
        limit: int = None,
        next_token: str = None,
        prefix: str = None,
    ):
        # The number of aliases returned.
        self.limit = limit
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The alias prefix.
        self.prefix = prefix

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limit is not None:
            result['limit'] = self.limit
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.prefix is not None:
            result['prefix'] = self.prefix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('prefix') is not None:
            self.prefix = m.get('prefix')
        return self


class ListAliasesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAliasesOutput = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListAliasesOutput()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAsyncInvokeConfigsRequest(TeaModel):
    def __init__(
        self,
        function_name: str = None,
        limit: int = None,
        next_token: str = None,
    ):
        # The function name. If you do not configure this parameter, the asynchronous invocation configurations of all functions are displayed.
        self.function_name = function_name
        # The maximum number of entries to be returned.
        self.limit = limit
        # The paging information. This parameter specifies the start point of the query.
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.function_name is not None:
            result['functionName'] = self.function_name
        if self.limit is not None:
            result['limit'] = self.limit
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('functionName') is not None:
            self.function_name = m.get('functionName')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        return self


class ListAsyncInvokeConfigsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAsyncInvokeConfigOutput = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListAsyncInvokeConfigOutput()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAsyncTasksRequest(TeaModel):
    def __init__(
        self,
        include_payload: bool = None,
        limit: int = None,
        next_token: str = None,
        prefix: str = None,
        qualifier: str = None,
        sort_order_by_time: str = None,
        started_time_begin: int = None,
        started_time_end: int = None,
        status: str = None,
    ):
        # Specifies whether to return input parameters of the asynchronous tasks. Valid values:
        # 
        # *   true: returns the `invocationPayload` parameter in the response.
        # *   false: does not return the `invocationPayload` parameter in the response.
        # 
        # >  The `invocationPayload` parameter indicates the input parameters of an asynchronous task.
        self.include_payload = include_payload
        # The number of asynchronous tasks to return. Valid values: [1,100]. Default value: 50.
        self.limit = limit
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token
        # The ID prefix of asynchronous tasks. If this parameter is specified, a list of asynchronous tasks whose IDs match the prefix is returned.
        self.prefix = prefix
        # The function version or alias.
        self.qualifier = qualifier
        # The order in which the returned asynchronous tasks are sorted.
        # 
        # *   asc: in ascending order.
        # *   desc: in descending order.
        self.sort_order_by_time = sort_order_by_time
        # The start time of the period in which the asynchronous tasks are launched.
        self.started_time_begin = started_time_begin
        # The end time of the period in which the asynchronous tasks are launched.
        self.started_time_end = started_time_end
        # The state of asynchronous tasks. The following items list the states of an asynchronous task:
        # 
        # *   Enqueued: The asynchronous invocation is enqueued and is waiting to be executed.
        # *   Succeeded: The invocation is successful.
        # *   Failed: The invocation fails.
        # *   Running: The invocation is being executed.
        # *   Stopped: The invocation is terminated.
        # *   Stopping: The invocation is being terminated.
        # *   Invalid: The invocation is invalid and not executed due to specific reasons. For example, the function is deleted.
        # *   Expired: The maximum validity period of messages is specified for asynchronous invocation. The invocation is discarded and not executed because the specified maximum validity period has elapsed.
        # *   Retrying: The asynchronous invocation is being retried due to an execution error.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.include_payload is not None:
            result['includePayload'] = self.include_payload
        if self.limit is not None:
            result['limit'] = self.limit
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.prefix is not None:
            result['prefix'] = self.prefix
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        if self.sort_order_by_time is not None:
            result['sortOrderByTime'] = self.sort_order_by_time
        if self.started_time_begin is not None:
            result['startedTimeBegin'] = self.started_time_begin
        if self.started_time_end is not None:
            result['startedTimeEnd'] = self.started_time_end
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('includePayload') is not None:
            self.include_payload = m.get('includePayload')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('prefix') is not None:
            self.prefix = m.get('prefix')
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        if m.get('sortOrderByTime') is not None:
            self.sort_order_by_time = m.get('sortOrderByTime')
        if m.get('startedTimeBegin') is not None:
            self.started_time_begin = m.get('startedTimeBegin')
        if m.get('startedTimeEnd') is not None:
            self.started_time_end = m.get('startedTimeEnd')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ListAsyncTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAsyncTaskOutput = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListAsyncTaskOutput()
            self.body = temp_model.from_map(m['body'])
        return self


class ListConcurrencyConfigsRequest(TeaModel):
    def __init__(
        self,
        function_name: str = None,
        limit: int = None,
        next_token: str = None,
    ):
        # The function name. If you leave this parameter empty, the concurrency configurations of all functions are returned.
        self.function_name = function_name
        # The maximum number of entries returned.
        self.limit = limit
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.function_name is not None:
            result['functionName'] = self.function_name
        if self.limit is not None:
            result['limit'] = self.limit
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('functionName') is not None:
            self.function_name = m.get('functionName')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        return self


class ListConcurrencyConfigsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListConcurrencyConfigsOutput = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListConcurrencyConfigsOutput()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCustomDomainsRequest(TeaModel):
    def __init__(
        self,
        limit: int = None,
        next_token: str = None,
        prefix: str = None,
    ):
        # The number of custom domain names returned.
        self.limit = limit
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The domain name prefix.
        self.prefix = prefix

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limit is not None:
            result['limit'] = self.limit
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.prefix is not None:
            result['prefix'] = self.prefix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('prefix') is not None:
            self.prefix = m.get('prefix')
        return self


class ListCustomDomainsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListCustomDomainOutput = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListCustomDomainOutput()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFunctionVersionsRequest(TeaModel):
    def __init__(
        self,
        direction: str = None,
        limit: int = None,
        next_token: str = None,
    ):
        # The sorting mode of function versions. Valid values: BACKWARD and FORWARD.
        self.direction = direction
        # The number of function versions that are returned.
        self.limit = limit
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.direction is not None:
            result['direction'] = self.direction
        if self.limit is not None:
            result['limit'] = self.limit
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('direction') is not None:
            self.direction = m.get('direction')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        return self


class ListFunctionVersionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListVersionsOutput = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListVersionsOutput()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFunctionsRequest(TeaModel):
    def __init__(
        self,
        limit: int = None,
        next_token: str = None,
        prefix: str = None,
    ):
        # The number of functions to return. The minimum value is 1 and the maximum value is 100.
        self.limit = limit
        # The pagination token.
        self.next_token = next_token
        # The prefix of the function name.
        self.prefix = prefix

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limit is not None:
            result['limit'] = self.limit
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.prefix is not None:
            result['prefix'] = self.prefix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('prefix') is not None:
            self.prefix = m.get('prefix')
        return self


class ListFunctionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListFunctionsOutput = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListFunctionsOutput()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstancesRequest(TeaModel):
    def __init__(
        self,
        qualifier: str = None,
        with_all_active: bool = None,
    ):
        # The function version or alias.
        self.qualifier = qualifier
        # Specifies whether to list all instances. Valid values: true and false.
        self.with_all_active = with_all_active

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        if self.with_all_active is not None:
            result['withAllActive'] = self.with_all_active
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        if m.get('withAllActive') is not None:
            self.with_all_active = m.get('withAllActive')
        return self


class ListInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListInstancesOutput = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListInstancesOutput()
            self.body = temp_model.from_map(m['body'])
        return self


class ListLayerVersionsRequest(TeaModel):
    def __init__(
        self,
        limit: int = None,
        start_version: str = None,
    ):
        # The number of versions to be returned.
        self.limit = limit
        # The initial version of the layer.
        self.start_version = start_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limit is not None:
            result['limit'] = self.limit
        if self.start_version is not None:
            result['startVersion'] = self.start_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('startVersion') is not None:
            self.start_version = m.get('startVersion')
        return self


class ListLayerVersionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListLayerVersionOutput = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListLayerVersionOutput()
            self.body = temp_model.from_map(m['body'])
        return self


class ListLayersRequest(TeaModel):
    def __init__(
        self,
        limit: int = None,
        next_token: str = None,
        official: str = None,
        prefix: str = None,
        public: str = None,
    ):
        # The number of layers that are returned
        self.limit = limit
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # Specifies whether the layer is official. Valid values: true and false.
        self.official = official
        # The name prefix of the layer.
        self.prefix = prefix
        # Specifies whether the layer is public. Valid values: true and false.
        self.public = public

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limit is not None:
            result['limit'] = self.limit
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.official is not None:
            result['official'] = self.official
        if self.prefix is not None:
            result['prefix'] = self.prefix
        if self.public is not None:
            result['public'] = self.public
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('official') is not None:
            self.official = m.get('official')
        if m.get('prefix') is not None:
            self.prefix = m.get('prefix')
        if m.get('public') is not None:
            self.public = m.get('public')
        return self


class ListLayersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListLayersOutput = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListLayersOutput()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProvisionConfigsRequest(TeaModel):
    def __init__(
        self,
        function_name: str = None,
        limit: int = None,
        next_token: str = None,
    ):
        # The name of the function. If this parameter is not specified, the provisioned configurations of all functions are listed.
        self.function_name = function_name
        # Number of provisioned configurations to return.
        self.limit = limit
        # A pagination token.
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.function_name is not None:
            result['functionName'] = self.function_name
        if self.limit is not None:
            result['limit'] = self.limit
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('functionName') is not None:
            self.function_name = m.get('functionName')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        return self


class ListProvisionConfigsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListProvisionConfigsOutput = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListProvisionConfigsOutput()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        # 
        # The tag key can be up to 64 characters in length, and cannot contain `http://` or `https://`. The tag key cannot start with `aliyun` or `acs:`.
        self.key = key
        # The tag value.
        # 
        # The tag value can be up to 128 characters in length and can be an empty string.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListTagResourcesRequest(TeaModel):
    def __init__(
        self,
        limit: int = None,
        next_token: str = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag: List[ListTagResourcesRequestTag] = None,
    ):
        # The number of resources to return.
        self.limit = limit
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The resource IDs.
        self.resource_id = resource_id
        # The resource type.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The tags.
        # 
        # You can query up to 20 tags at a time.
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListTagResourcesShrinkRequest(TeaModel):
    def __init__(
        self,
        limit: int = None,
        next_token: str = None,
        resource_id_shrink: str = None,
        resource_type: str = None,
        tag_shrink: str = None,
    ):
        # The number of resources to return.
        self.limit = limit
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The resource IDs.
        self.resource_id_shrink = resource_id_shrink
        # The resource type.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The tags.
        # 
        # You can query up to 20 tags at a time.
        self.tag_shrink = tag_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.resource_id_shrink is not None:
            result['ResourceId'] = self.resource_id_shrink
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_shrink is not None:
            result['Tag'] = self.tag_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ResourceId') is not None:
            self.resource_id_shrink = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Tag') is not None:
            self.tag_shrink = m.get('Tag')
        return self


class ListTagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTagResourcesOutput = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListTagResourcesOutput()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTriggersRequest(TeaModel):
    def __init__(
        self,
        limit: int = None,
        next_token: str = None,
        prefix: str = None,
    ):
        # The number of triggers returned.
        self.limit = limit
        # The token for the next page.
        self.next_token = next_token
        # The trigger name prefix.
        self.prefix = prefix

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limit is not None:
            result['limit'] = self.limit
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.prefix is not None:
            result['prefix'] = self.prefix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('prefix') is not None:
            self.prefix = m.get('prefix')
        return self


class ListTriggersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTriggersOutput = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListTriggersOutput()
            self.body = temp_model.from_map(m['body'])
        return self


class ListVpcBindingsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListVpcBindingsOutput = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListVpcBindingsOutput()
            self.body = temp_model.from_map(m['body'])
        return self


class PublishFunctionVersionRequest(TeaModel):
    def __init__(
        self,
        body: PublishVersionInput = None,
    ):
        # The information about the function version.
        # 
        # This parameter is required.
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = PublishVersionInput()
            self.body = temp_model.from_map(m['body'])
        return self


class PublishFunctionVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Version = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = Version()
            self.body = temp_model.from_map(m['body'])
        return self


class PutAsyncInvokeConfigRequest(TeaModel):
    def __init__(
        self,
        body: PutAsyncInvokeConfigInput = None,
        qualifier: str = None,
    ):
        # The configurations of asynchronous function invocation.
        # 
        # This parameter is required.
        self.body = body
        # The version or alias of the function.
        self.qualifier = qualifier

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = PutAsyncInvokeConfigInput()
            self.body = temp_model.from_map(m['body'])
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        return self


class PutAsyncInvokeConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AsyncConfig = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = AsyncConfig()
            self.body = temp_model.from_map(m['body'])
        return self


class PutConcurrencyConfigRequest(TeaModel):
    def __init__(
        self,
        body: PutConcurrencyInput = None,
    ):
        # The concurrency configurations.
        # 
        # This parameter is required.
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = PutConcurrencyInput()
            self.body = temp_model.from_map(m['body'])
        return self


class PutConcurrencyConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ConcurrencyConfig = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ConcurrencyConfig()
            self.body = temp_model.from_map(m['body'])
        return self


class PutLayerACLRequest(TeaModel):
    def __init__(
        self,
        acl: str = None,
        public: str = None,
    ):
        self.acl = acl
        # Specifies whether the layer is a public layer. Valid values: true and false.
        self.public = public

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl is not None:
            result['acl'] = self.acl
        if self.public is not None:
            result['public'] = self.public
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('acl') is not None:
            self.acl = m.get('acl')
        if m.get('public') is not None:
            self.public = m.get('public')
        return self


class PutLayerACLResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class PutProvisionConfigRequest(TeaModel):
    def __init__(
        self,
        body: PutProvisionConfigInput = None,
        qualifier: str = None,
    ):
        # The information about the provisioned configuration.
        # 
        # This parameter is required.
        self.body = body
        # The function alias or LATEST.
        self.qualifier = qualifier

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = PutProvisionConfigInput()
            self.body = temp_model.from_map(m['body'])
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        return self


class PutProvisionConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ProvisionConfig = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ProvisionConfig()
            self.body = temp_model.from_map(m['body'])
        return self


class StopAsyncTaskRequest(TeaModel):
    def __init__(
        self,
        qualifier: str = None,
    ):
        # The function version or alias.
        self.qualifier = qualifier

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        return self


class StopAsyncTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class TagResourcesRequest(TeaModel):
    def __init__(
        self,
        body: TagResourcesInput = None,
    ):
        # The configuration of the resource tag.
        # 
        # This parameter is required.
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = TagResourcesInput()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(
        self,
        all: bool = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag_key: List[str] = None,
    ):
        # Specifies whether to delete all tags.
        self.all = all
        # The resource identifiers.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The resource type.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The tag to remove. You can specify a maximum of 50 tags.
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['All'] = self.all
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class UntagResourcesShrinkRequest(TeaModel):
    def __init__(
        self,
        all: bool = None,
        resource_id_shrink: str = None,
        resource_type: str = None,
        tag_key_shrink: str = None,
    ):
        # Specifies whether to delete all tags.
        self.all = all
        # The resource identifiers.
        # 
        # This parameter is required.
        self.resource_id_shrink = resource_id_shrink
        # The resource type.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The tag to remove. You can specify a maximum of 50 tags.
        self.tag_key_shrink = tag_key_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['All'] = self.all
        if self.resource_id_shrink is not None:
            result['ResourceId'] = self.resource_id_shrink
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key_shrink is not None:
            result['TagKey'] = self.tag_key_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('ResourceId') is not None:
            self.resource_id_shrink = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key_shrink = m.get('TagKey')
        return self


class UntagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class UpdateAliasRequest(TeaModel):
    def __init__(
        self,
        body: UpdateAliasInput = None,
    ):
        # The alias information to be updated.
        # 
        # This parameter is required.
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = UpdateAliasInput()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAliasResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Alias = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = Alias()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCustomDomainRequest(TeaModel):
    def __init__(
        self,
        body: UpdateCustomDomainInput = None,
    ):
        # The information about the custom domain name.
        # 
        # This parameter is required.
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = UpdateCustomDomainInput()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCustomDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CustomDomain = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = CustomDomain()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFunctionRequest(TeaModel):
    def __init__(
        self,
        body: UpdateFunctionInput = None,
    ):
        # The function information
        # 
        # This parameter is required.
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = UpdateFunctionInput()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFunctionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Function = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = Function()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTriggerRequest(TeaModel):
    def __init__(
        self,
        body: UpdateTriggerInput = None,
    ):
        # The trigger configurations.
        # 
        # This parameter is required.
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = UpdateTriggerInput()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTriggerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Trigger = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = Trigger()
            self.body = temp_model.from_map(m['body'])
        return self


