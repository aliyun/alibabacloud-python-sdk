# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


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


class AsyncConfigMeta(TeaModel):
    def __init__(
        self,
        function_name: str = None,
        qualifier: str = None,
        service_name: str = None,
    ):
        self.function_name = function_name
        self.qualifier = qualifier
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.function_name is not None:
            result['functionName'] = self.function_name
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('functionName') is not None:
            self.function_name = m.get('functionName')
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        return self


class AvailableAZ(TeaModel):
    def __init__(
        self,
        available_azs: str = None,
    ):
        self.available_azs = available_azs

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.available_azs is not None:
            result['availableAZs'] = self.available_azs
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('availableAZs') is not None:
            self.available_azs = m.get('availableAZs')
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


class CDNEventsTriggerConfig(TeaModel):
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
        self.cert_name = cert_name
        self.certificate = certificate
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


class Code(TeaModel):
    def __init__(
        self,
        oss_bucket_name: str = None,
        oss_object_name: str = None,
        zip_file: str = None,
    ):
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
        if self.oss_bucket_name is not None:
            result['ossBucketName'] = self.oss_bucket_name
        if self.oss_object_name is not None:
            result['ossObjectName'] = self.oss_object_name
        if self.zip_file is not None:
            result['zipFile'] = self.zip_file
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ossBucketName') is not None:
            self.oss_bucket_name = m.get('ossBucketName')
        if m.get('ossObjectName') is not None:
            self.oss_object_name = m.get('ossObjectName')
        if m.get('zipFile') is not None:
            self.zip_file = m.get('zipFile')
        return self


class CustomContainerConfig(TeaModel):
    def __init__(
        self,
        acceleration_type: str = None,
        args: str = None,
        command: str = None,
        image: str = None,
        instance_id: str = None,
        web_server_mode: bool = None,
    ):
        self.acceleration_type = acceleration_type
        self.args = args
        self.command = command
        self.image = image
        self.instance_id = instance_id
        self.web_server_mode = web_server_mode

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acceleration_type is not None:
            result['accelerationType'] = self.acceleration_type
        if self.args is not None:
            result['args'] = self.args
        if self.command is not None:
            result['command'] = self.command
        if self.image is not None:
            result['image'] = self.image
        if self.instance_id is not None:
            result['instanceID'] = self.instance_id
        if self.web_server_mode is not None:
            result['webServerMode'] = self.web_server_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accelerationType') is not None:
            self.acceleration_type = m.get('accelerationType')
        if m.get('args') is not None:
            self.args = m.get('args')
        if m.get('command') is not None:
            self.command = m.get('command')
        if m.get('image') is not None:
            self.image = m.get('image')
        if m.get('instanceID') is not None:
            self.instance_id = m.get('instanceID')
        if m.get('webServerMode') is not None:
            self.web_server_mode = m.get('webServerMode')
        return self


class CustomContainerConfigInfo(TeaModel):
    def __init__(
        self,
        acceleration_info: AccelerationInfo = None,
        acceleration_type: str = None,
        args: str = None,
        command: str = None,
        image: str = None,
        instance_id: str = None,
        web_server_mode: bool = None,
    ):
        self.acceleration_info = acceleration_info
        self.acceleration_type = acceleration_type
        self.args = args
        self.command = command
        self.image = image
        self.instance_id = instance_id
        self.web_server_mode = web_server_mode

    def validate(self):
        if self.acceleration_info:
            self.acceleration_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acceleration_info is not None:
            result['accelerationInfo'] = self.acceleration_info.to_map()
        if self.acceleration_type is not None:
            result['accelerationType'] = self.acceleration_type
        if self.args is not None:
            result['args'] = self.args
        if self.command is not None:
            result['command'] = self.command
        if self.image is not None:
            result['image'] = self.image
        if self.instance_id is not None:
            result['instanceID'] = self.instance_id
        if self.web_server_mode is not None:
            result['webServerMode'] = self.web_server_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accelerationInfo') is not None:
            temp_model = AccelerationInfo()
            self.acceleration_info = temp_model.from_map(m['accelerationInfo'])
        if m.get('accelerationType') is not None:
            self.acceleration_type = m.get('accelerationType')
        if m.get('args') is not None:
            self.args = m.get('args')
        if m.get('command') is not None:
            self.command = m.get('command')
        if m.get('image') is not None:
            self.image = m.get('image')
        if m.get('instanceID') is not None:
            self.instance_id = m.get('instanceID')
        if m.get('webServerMode') is not None:
            self.web_server_mode = m.get('webServerMode')
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


class CustomRuntimeConfig(TeaModel):
    def __init__(
        self,
        args: List[str] = None,
        command: List[str] = None,
    ):
        self.args = args
        self.command = command

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.args is not None:
            result['args'] = self.args
        if self.command is not None:
            result['command'] = self.command
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('args') is not None:
            self.args = m.get('args')
        if m.get('command') is not None:
            self.command = m.get('command')
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
        mode: str = None,
    ):
        self.concurrency = concurrency
        self.event_schema = event_schema
        self.mode = mode

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
        if self.mode is not None:
            result['mode'] = self.mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('concurrency') is not None:
            self.concurrency = m.get('concurrency')
        if m.get('eventSchema') is not None:
            self.event_schema = m.get('eventSchema')
        if m.get('mode') is not None:
            self.mode = m.get('mode')
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


class Error(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
    ):
        self.error_code = error_code
        self.error_message = error_message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        return self


class ErrorInfo(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        stack_trace: str = None,
    ):
        self.error_message = error_message
        self.stack_trace = stack_trace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.stack_trace is not None:
            result['stackTrace'] = self.stack_trace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('stackTrace') is not None:
            self.stack_trace = m.get('stackTrace')
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
        filter_sql: str = None,
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
        self.filter_sql = filter_sql
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
        if self.filter_sql is not None:
            result['FilterSql'] = self.filter_sql
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
        if m.get('FilterSql') is not None:
            self.filter_sql = m.get('FilterSql')
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
        maximum_event_age_in_seconds: int = None,
        maximum_retry_attempts: int = None,
        push_retry_strategy: str = None,
    ):
        self.maximum_event_age_in_seconds = maximum_event_age_in_seconds
        self.maximum_retry_attempts = maximum_retry_attempts
        self.push_retry_strategy = push_retry_strategy

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.maximum_event_age_in_seconds is not None:
            result['MaximumEventAgeInSeconds'] = self.maximum_event_age_in_seconds
        if self.maximum_retry_attempts is not None:
            result['MaximumRetryAttempts'] = self.maximum_retry_attempts
        if self.push_retry_strategy is not None:
            result['PushRetryStrategy'] = self.push_retry_strategy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaximumEventAgeInSeconds') is not None:
            self.maximum_event_age_in_seconds = m.get('MaximumEventAgeInSeconds')
        if m.get('MaximumRetryAttempts') is not None:
            self.maximum_retry_attempts = m.get('MaximumRetryAttempts')
        if m.get('PushRetryStrategy') is not None:
            self.push_retry_strategy = m.get('PushRetryStrategy')
        return self


class RunOptions(TeaModel):
    def __init__(
        self,
        batch_window: BatchWindow = None,
        dead_letter_queue: DeadLetterQueue = None,
        errors_tolerance: str = None,
        maximum_tasks: int = None,
        mode: str = None,
        retry_strategy: RetryStrategy = None,
    ):
        self.batch_window = batch_window
        self.dead_letter_queue = dead_letter_queue
        self.errors_tolerance = errors_tolerance
        self.maximum_tasks = maximum_tasks
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
        if self.maximum_tasks is not None:
            result['maximumTasks'] = self.maximum_tasks
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
        if m.get('maximumTasks') is not None:
            self.maximum_tasks = m.get('maximumTasks')
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
        # 禁用默认公网域名访问的开关，设置为true 时，访问函数默认提供的公网URL地址会返回403错误。设置为 false 则不会有任何影响。
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
        pre_freeze: LifecycleHook = None,
        pre_stop: LifecycleHook = None,
    ):
        self.pre_freeze = pre_freeze
        self.pre_stop = pre_stop

    def validate(self):
        if self.pre_freeze:
            self.pre_freeze.validate()
        if self.pre_stop:
            self.pre_stop.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pre_freeze is not None:
            result['preFreeze'] = self.pre_freeze.to_map()
        if self.pre_stop is not None:
            result['preStop'] = self.pre_stop.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('preFreeze') is not None:
            temp_model = LifecycleHook()
            self.pre_freeze = temp_model.from_map(m['preFreeze'])
        if m.get('preStop') is not None:
            temp_model = LifecycleHook()
            self.pre_stop = temp_model.from_map(m['preStop'])
        return self


class JWTAuthConfig(TeaModel):
    def __init__(
        self,
        black_list: str = None,
        claim_pass_by: List[str] = None,
        jwks: str = None,
        token_lookup: List[str] = None,
        white_list: List[str] = None,
    ):
        self.black_list = black_list
        self.claim_pass_by = claim_pass_by
        self.jwks = jwks
        self.token_lookup = token_lookup
        self.white_list = white_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.black_list is not None:
            result['blackList'] = self.black_list
        if self.claim_pass_by is not None:
            result['claimPassBy'] = self.claim_pass_by
        if self.jwks is not None:
            result['jwks'] = self.jwks
        if self.token_lookup is not None:
            result['tokenLookup'] = self.token_lookup
        if self.white_list is not None:
            result['whiteList'] = self.white_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('blackList') is not None:
            self.black_list = m.get('blackList')
        if m.get('claimPassBy') is not None:
            self.claim_pass_by = m.get('claimPassBy')
        if m.get('jwks') is not None:
            self.jwks = m.get('jwks')
        if m.get('tokenLookup') is not None:
            self.token_lookup = m.get('tokenLookup')
        if m.get('whiteList') is not None:
            self.white_list = m.get('whiteList')
        return self


class JaegerConfig(TeaModel):
    def __init__(
        self,
        endpoint: str = None,
    ):
        self.endpoint = endpoint

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')
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


class JobLogConfig(TeaModel):
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


class LayerCode(TeaModel):
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
        acl: int = None,
        arn: str = None,
        arn_v2: str = None,
        code: LayerCode = None,
        code_checksum: str = None,
        code_size: int = None,
        compatible_runtime: List[str] = None,
        create_time: str = None,
        description: str = None,
        layer_name: str = None,
        license: str = None,
        version: int = None,
    ):
        self.acl = acl
        self.arn = arn
        self.arn_v2 = arn_v2
        self.code = code
        self.code_checksum = code_checksum
        self.code_size = code_size
        self.compatible_runtime = compatible_runtime
        self.create_time = create_time
        self.description = description
        self.layer_name = layer_name
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
        if self.arn is not None:
            result['arn'] = self.arn
        if self.arn_v2 is not None:
            result['arnV2'] = self.arn_v2
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
        if self.license is not None:
            result['license'] = self.license
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('acl') is not None:
            self.acl = m.get('acl')
        if m.get('arn') is not None:
            self.arn = m.get('arn')
        if m.get('arnV2') is not None:
            self.arn_v2 = m.get('arnV2')
        if m.get('code') is not None:
            temp_model = LayerCode()
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
        if m.get('license') is not None:
            self.license = m.get('license')
        if m.get('version') is not None:
            self.version = m.get('version')
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


class SourceConfig(TeaModel):
    def __init__(
        self,
        logstore: str = None,
    ):
        self.logstore = logstore

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logstore is not None:
            result['logstore'] = self.logstore
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('logstore') is not None:
            self.logstore = m.get('logstore')
        return self


class LogTriggerConfig(TeaModel):
    def __init__(
        self,
        enable: bool = None,
        function_parameter: Dict[str, str] = None,
        job_config: JobConfig = None,
        log_config: JobLogConfig = None,
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
            temp_model = JobLogConfig()
            self.log_config = temp_model.from_map(m['logConfig'])
        if m.get('sourceConfig') is not None:
            temp_model = SourceConfig()
            self.source_config = temp_model.from_map(m['sourceConfig'])
        return self


class MeteringConfig(TeaModel):
    def __init__(
        self,
        log_config: LogConfig = None,
        payer_id: str = None,
        role: str = None,
    ):
        self.log_config = log_config
        self.payer_id = payer_id
        self.role = role

    def validate(self):
        if self.log_config:
            self.log_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_config is not None:
            result['logConfig'] = self.log_config.to_map()
        if self.payer_id is not None:
            result['payerId'] = self.payer_id
        if self.role is not None:
            result['role'] = self.role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('logConfig') is not None:
            temp_model = LogConfig()
            self.log_config = temp_model.from_map(m['logConfig'])
        if m.get('payerId') is not None:
            self.payer_id = m.get('payerId')
        if m.get('role') is not None:
            self.role = m.get('role')
        return self


class MnsTopicTriggerConfig(TeaModel):
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


class NASConfigMountPoints(TeaModel):
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
        mount_points: List[NASConfigMountPoints] = None,
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
                temp_model = NASConfigMountPoints()
                self.mount_points.append(temp_model.from_map(k))
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class OSSMountConfigMountPoints(TeaModel):
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
        mount_points: List[OSSMountConfigMountPoints] = None,
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
                temp_model = OSSMountConfigMountPoints()
                self.mount_points.append(temp_model.from_map(k))
        return self


class OSSTriggerKey(TeaModel):
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


class OSSTriggerFilter(TeaModel):
    def __init__(
        self,
        key: OSSTriggerKey = None,
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
            temp_model = OSSTriggerKey()
            self.key = temp_model.from_map(m['key'])
        return self


class OSSTriggerConfig(TeaModel):
    def __init__(
        self,
        events: List[str] = None,
        filter: OSSTriggerFilter = None,
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
            temp_model = OSSTriggerFilter()
            self.filter = temp_model.from_map(m['filter'])
        return self


class OnDemandConfig(TeaModel):
    def __init__(
        self,
        maximum_instance_count: int = None,
        resource: str = None,
    ):
        self.maximum_instance_count = maximum_instance_count
        self.resource = resource

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.maximum_instance_count is not None:
            result['maximumInstanceCount'] = self.maximum_instance_count
        if self.resource is not None:
            result['resource'] = self.resource
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maximumInstanceCount') is not None:
            self.maximum_instance_count = m.get('maximumInstanceCount')
        if m.get('resource') is not None:
            self.resource = m.get('resource')
        return self


class OpenReservedCapacity(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        cu: int = None,
        deadline: str = None,
        instance_id: str = None,
        is_refunded: str = None,
        last_modified_time: str = None,
    ):
        self.created_time = created_time
        self.cu = cu
        self.deadline = deadline
        self.instance_id = instance_id
        self.is_refunded = is_refunded
        self.last_modified_time = last_modified_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.cu is not None:
            result['cu'] = self.cu
        if self.deadline is not None:
            result['deadline'] = self.deadline
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.is_refunded is not None:
            result['isRefunded'] = self.is_refunded
        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('cu') is not None:
            self.cu = m.get('cu')
        if m.get('deadline') is not None:
            self.deadline = m.get('deadline')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('isRefunded') is not None:
            self.is_refunded = m.get('isRefunded')
        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')
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


class RewriteConfigEqualRules(TeaModel):
    def __init__(
        self,
        match: str = None,
        replacement: str = None,
    ):
        self.match = match
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


class RewriteConfigRegexRules(TeaModel):
    def __init__(
        self,
        match: str = None,
        replacement: str = None,
    ):
        self.match = match
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


class RewriteConfigWildcardRules(TeaModel):
    def __init__(
        self,
        match: str = None,
        replacement: str = None,
    ):
        self.match = match
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
        equal_rules: List[RewriteConfigEqualRules] = None,
        regex_rules: List[RewriteConfigRegexRules] = None,
        wildcard_rules: List[RewriteConfigWildcardRules] = None,
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
                temp_model = RewriteConfigEqualRules()
                self.equal_rules.append(temp_model.from_map(k))
        self.regex_rules = []
        if m.get('regexRules') is not None:
            for k in m.get('regexRules'):
                temp_model = RewriteConfigRegexRules()
                self.regex_rules.append(temp_model.from_map(k))
        self.wildcard_rules = []
        if m.get('wildcardRules') is not None:
            for k in m.get('wildcardRules'):
                temp_model = RewriteConfigWildcardRules()
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
        service_name: str = None,
    ):
        self.function_name = function_name
        self.methods = methods
        self.path = path
        self.qualifier = qualifier
        self.rewrite_config = rewrite_config
        self.service_name = service_name

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
        if self.service_name is not None:
            result['serviceName'] = self.service_name
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
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        return self


class PolicyItem(TeaModel):
    def __init__(
        self,
        key: str = None,
        operator: str = None,
        type: str = None,
        value: str = None,
    ):
        self.key = key
        self.operator = operator
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.operator is not None:
            result['operator'] = self.operator
        if self.type is not None:
            result['type'] = self.type
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class PreFreeze(TeaModel):
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


class PreStop(TeaModel):
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


class RdsTriggerConfig(TeaModel):
    def __init__(
        self,
        concurrency: int = None,
        event_format: str = None,
        retry: int = None,
        subscription_objects: List[str] = None,
    ):
        self.concurrency = concurrency
        self.event_format = event_format
        self.retry = retry
        self.subscription_objects = subscription_objects

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.concurrency is not None:
            result['concurrency'] = self.concurrency
        if self.event_format is not None:
            result['eventFormat'] = self.event_format
        if self.retry is not None:
            result['retry'] = self.retry
        if self.subscription_objects is not None:
            result['subscriptionObjects'] = self.subscription_objects
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('concurrency') is not None:
            self.concurrency = m.get('concurrency')
        if m.get('eventFormat') is not None:
            self.event_format = m.get('eventFormat')
        if m.get('retry') is not None:
            self.retry = m.get('retry')
        if m.get('subscriptionObjects') is not None:
            self.subscription_objects = m.get('subscriptionObjects')
        return self


class Resource(TeaModel):
    def __init__(
        self,
        resource_arn: str = None,
        tags: Dict[str, str] = None,
    ):
        self.resource_arn = resource_arn
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


class RoutePolicy(TeaModel):
    def __init__(
        self,
        condition: str = None,
        policy_items: List[PolicyItem] = None,
    ):
        self.condition = condition
        self.policy_items = policy_items

    def validate(self):
        if self.policy_items:
            for k in self.policy_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.condition is not None:
            result['condition'] = self.condition
        result['policyItems'] = []
        if self.policy_items is not None:
            for k in self.policy_items:
                result['policyItems'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('condition') is not None:
            self.condition = m.get('condition')
        self.policy_items = []
        if m.get('policyItems') is not None:
            for k in m.get('policyItems'):
                temp_model = PolicyItem()
                self.policy_items.append(temp_model.from_map(k))
        return self


class ScheduledActions(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        name: str = None,
        schedule_expression: str = None,
        start_time: str = None,
        target: int = None,
    ):
        self.end_time = end_time
        self.name = name
        self.schedule_expression = schedule_expression
        self.start_time = start_time
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


class StatefulAsyncInvocationEvent(TeaModel):
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


class StatefulAsyncInvocation(TeaModel):
    def __init__(
        self,
        already_retried_times: int = None,
        destination_status: str = None,
        duration_ms: int = None,
        end_time: int = None,
        events: List[StatefulAsyncInvocationEvent] = None,
        function_name: str = None,
        instance_id: str = None,
        invocation_error_message: str = None,
        invocation_id: str = None,
        invocation_payload: str = None,
        qualifier: str = None,
        request_id: str = None,
        return_payload: str = None,
        service_name: str = None,
        started_time: int = None,
        status: str = None,
    ):
        self.already_retried_times = already_retried_times
        self.destination_status = destination_status
        self.duration_ms = duration_ms
        self.end_time = end_time
        self.events = events
        self.function_name = function_name
        self.instance_id = instance_id
        self.invocation_error_message = invocation_error_message
        self.invocation_id = invocation_id
        self.invocation_payload = invocation_payload
        self.qualifier = qualifier
        self.request_id = request_id
        self.return_payload = return_payload
        self.service_name = service_name
        self.started_time = started_time
        self.status = status

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
        if self.function_name is not None:
            result['functionName'] = self.function_name
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.invocation_error_message is not None:
            result['invocationErrorMessage'] = self.invocation_error_message
        if self.invocation_id is not None:
            result['invocationId'] = self.invocation_id
        if self.invocation_payload is not None:
            result['invocationPayload'] = self.invocation_payload
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.return_payload is not None:
            result['returnPayload'] = self.return_payload
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        if self.started_time is not None:
            result['startedTime'] = self.started_time
        if self.status is not None:
            result['status'] = self.status
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
                temp_model = StatefulAsyncInvocationEvent()
                self.events.append(temp_model.from_map(k))
        if m.get('functionName') is not None:
            self.function_name = m.get('functionName')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('invocationErrorMessage') is not None:
            self.invocation_error_message = m.get('invocationErrorMessage')
        if m.get('invocationId') is not None:
            self.invocation_id = m.get('invocationId')
        if m.get('invocationPayload') is not None:
            self.invocation_payload = m.get('invocationPayload')
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('returnPayload') is not None:
            self.return_payload = m.get('returnPayload')
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        if m.get('startedTime') is not None:
            self.started_time = m.get('startedTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class TLSConfig(TeaModel):
    def __init__(
        self,
        cipher_suites: List[str] = None,
        max_version: str = None,
        min_version: str = None,
    ):
        self.cipher_suites = cipher_suites
        self.max_version = max_version
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


class TargetTrackingPolicies(TeaModel):
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
        self.max_capacity = max_capacity
        self.metric_target = metric_target
        self.metric_type = metric_type
        self.min_capacity = min_capacity
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


class TimeTriggerConfig(TeaModel):
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


class Trigger(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        domain_name: str = None,
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
        url_internet: str = None,
        url_intranet: str = None,
    ):
        self.created_time = created_time
        self.domain_name = domain_name
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
        self.url_internet = url_internet
        self.url_intranet = url_intranet

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.domain_name is not None:
            result['domainName'] = self.domain_name
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
        if self.url_internet is not None:
            result['urlInternet'] = self.url_internet
        if self.url_intranet is not None:
            result['urlIntranet'] = self.url_intranet
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('domainName') is not None:
            self.domain_name = m.get('domainName')
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
        if m.get('urlInternet') is not None:
            self.url_internet = m.get('urlInternet')
        if m.get('urlIntranet') is not None:
            self.url_intranet = m.get('urlIntranet')
        return self


class VPCConfig(TeaModel):
    def __init__(
        self,
        role: str = None,
        security_group_id: str = None,
        v_switch_ids: List[str] = None,
        vpc_id: str = None,
    ):
        self.role = role
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
        if self.role is not None:
            result['role'] = self.role
        if self.security_group_id is not None:
            result['securityGroupId'] = self.security_group_id
        if self.v_switch_ids is not None:
            result['vSwitchIds'] = self.v_switch_ids
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('role') is not None:
            self.role = m.get('role')
        if m.get('securityGroupId') is not None:
            self.security_group_id = m.get('securityGroupId')
        if m.get('vSwitchIds') is not None:
            self.v_switch_ids = m.get('vSwitchIds')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        return self


class VendorConfig(TeaModel):
    def __init__(
        self,
        metering_config: MeteringConfig = None,
    ):
        self.metering_config = metering_config

    def validate(self):
        if self.metering_config:
            self.metering_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.metering_config is not None:
            result['meteringConfig'] = self.metering_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('meteringConfig') is not None:
            temp_model = MeteringConfig()
            self.metering_config = temp_model.from_map(m['meteringConfig'])
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


class ClaimGPUInstanceHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id
        # The time on which the function is invoked. The format of the value is: **EEE,d MMM yyyy HH:mm:ss GMT**.
        self.x_fc_date = x_fc_date
        # The custom request ID.
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class ClaimGPUInstanceRequest(TeaModel):
    def __init__(
        self,
        disk_performance_level: str = None,
        disk_size_gigabytes: str = None,
        image_id: str = None,
        instance_type: str = None,
        internet_bandwidth_out: str = None,
        password: str = None,
        role: str = None,
        sg_id: str = None,
        source_cidr_ip: str = None,
        tcp_port_range: List[str] = None,
        udp_port_range: List[str] = None,
        vpc_id: str = None,
        vsw_id: str = None,
    ):
        # The disk performance level of the GPU rendering instance.
        self.disk_performance_level = disk_performance_level
        # The system disk space of the GPU rendering instance. Unit: GB.
        self.disk_size_gigabytes = disk_size_gigabytes
        # The image ID of the GPU rendering instance.
        self.image_id = image_id
        # The specifications of the GPU rendering instance.
        self.instance_type = instance_type
        # The outbound Internet bandwidth of the GPU rendering instance.
        self.internet_bandwidth_out = internet_bandwidth_out
        # The password of the GPU rendering instance.
        self.password = password
        # The user role.
        self.role = role
        # The security group ID.
        self.sg_id = sg_id
        # The source IPv4 CIDR block of the GPU rendering instance.
        self.source_cidr_ip = source_cidr_ip
        # The range of TCP ports that are open to the security group of the GPU rendering instance.
        self.tcp_port_range = tcp_port_range
        # The range of UDP ports that are open to the security group of the GPU rendering instance.
        self.udp_port_range = udp_port_range
        # The ID of the VPC in which the instance resides.
        self.vpc_id = vpc_id
        # The vSwitch ID of the instance.
        self.vsw_id = vsw_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disk_performance_level is not None:
            result['diskPerformanceLevel'] = self.disk_performance_level
        if self.disk_size_gigabytes is not None:
            result['diskSizeGigabytes'] = self.disk_size_gigabytes
        if self.image_id is not None:
            result['imageId'] = self.image_id
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        if self.internet_bandwidth_out is not None:
            result['internetBandwidthOut'] = self.internet_bandwidth_out
        if self.password is not None:
            result['password'] = self.password
        if self.role is not None:
            result['role'] = self.role
        if self.sg_id is not None:
            result['sgId'] = self.sg_id
        if self.source_cidr_ip is not None:
            result['sourceCidrIp'] = self.source_cidr_ip
        if self.tcp_port_range is not None:
            result['tcpPortRange'] = self.tcp_port_range
        if self.udp_port_range is not None:
            result['udpPortRange'] = self.udp_port_range
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.vsw_id is not None:
            result['vswId'] = self.vsw_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('diskPerformanceLevel') is not None:
            self.disk_performance_level = m.get('diskPerformanceLevel')
        if m.get('diskSizeGigabytes') is not None:
            self.disk_size_gigabytes = m.get('diskSizeGigabytes')
        if m.get('imageId') is not None:
            self.image_id = m.get('imageId')
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        if m.get('internetBandwidthOut') is not None:
            self.internet_bandwidth_out = m.get('internetBandwidthOut')
        if m.get('password') is not None:
            self.password = m.get('password')
        if m.get('role') is not None:
            self.role = m.get('role')
        if m.get('sgId') is not None:
            self.sg_id = m.get('sgId')
        if m.get('sourceCidrIp') is not None:
            self.source_cidr_ip = m.get('sourceCidrIp')
        if m.get('tcpPortRange') is not None:
            self.tcp_port_range = m.get('tcpPortRange')
        if m.get('udpPortRange') is not None:
            self.udp_port_range = m.get('udpPortRange')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('vswId') is not None:
            self.vsw_id = m.get('vswId')
        return self


class ClaimGPUInstanceResponseBody(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        instance_id: str = None,
        public_ip: str = None,
    ):
        # The time when the product instance is created.
        self.created_time = created_time
        # The ID of the instance that you query.
        self.instance_id = instance_id
        # The public IP address of the server.
        self.public_ip = public_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.public_ip is not None:
            result['publicIp'] = self.public_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('publicIp') is not None:
            self.public_ip = m.get('publicIp')
        return self


class ClaimGPUInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ClaimGPUInstanceResponseBody = None,
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
            temp_model = ClaimGPUInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAliasHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id
        # The time on which the function is invoked. The format of the value is: **EEE,d MMM yyyy HH:mm:ss GMT**.
        self.x_fc_date = x_fc_date
        # The trace ID of the invocation request of Function Compute.
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class CreateAliasRequest(TeaModel):
    def __init__(
        self,
        additional_version_weight: Dict[str, float] = None,
        alias_name: str = None,
        description: str = None,
        resolve_policy: str = None,
        route_policy: RoutePolicy = None,
        version_id: str = None,
    ):
        # The canary release version to which the alias points and the weight of the canary release version.
        # 
        # *   The canary release version takes effect only when the function is invoked.
        # *   The value consists of a version number and a specific weight. For example, 2:0.05 indicates that when a function is invoked, Version 2 is the canary release version, 5% of the traffic is distributed to the canary release version, and 95% of the traffic is distributed to the major version.
        self.additional_version_weight = additional_version_weight
        # The name of the alias. The name can contain letters, digits, underscores (\_), and hyphens (-) only. The name cannot start with a digit or a hyphen (-). The name must be 1 to 128 characters in length. The name cannot be set to **LATEST**\
        self.alias_name = alias_name
        # The description of the alias.
        self.description = description
        # The canary release mode. Default values: off. Valid values:
        # 
        # *   **Random**: random canary release.
        # *   **Content**: rule-based canary release. By default, this parameter is empty.
        self.resolve_policy = resolve_policy
        # The canary release rule. Traffic that meets the canary release rule is routed to the canary release instance.
        self.route_policy = route_policy
        # The ID of the version to which the alias points.
        self.version_id = version_id

    def validate(self):
        if self.route_policy:
            self.route_policy.validate()

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
        if self.resolve_policy is not None:
            result['resolvePolicy'] = self.resolve_policy
        if self.route_policy is not None:
            result['routePolicy'] = self.route_policy.to_map()
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
        if m.get('resolvePolicy') is not None:
            self.resolve_policy = m.get('resolvePolicy')
        if m.get('routePolicy') is not None:
            temp_model = RoutePolicy()
            self.route_policy = temp_model.from_map(m['routePolicy'])
        if m.get('versionId') is not None:
            self.version_id = m.get('versionId')
        return self


class CreateAliasResponseBody(TeaModel):
    def __init__(
        self,
        additional_version_weight: Dict[str, float] = None,
        alias_name: str = None,
        created_time: str = None,
        description: str = None,
        last_modified_time: str = None,
        resolve_policy: str = None,
        route_policy: RoutePolicy = None,
        version_id: str = None,
    ):
        # The additional version to which the alias points and the weight of the additional version.
        # 
        # *   The additional version takes effect only when the function is invoked.
        # *   The value consists of a version number and a specific weight. For example, 2:0.05 indicates that when a function is invoked, Version 2 is the canary release version, 5% of the traffic is distributed to the canary release version, and 95% of the traffic is distributed to the major version.
        self.additional_version_weight = additional_version_weight
        # The name of the alias.
        self.alias_name = alias_name
        # The time when the alias was created.
        self.created_time = created_time
        # The description of the alias.
        self.description = description
        # The time when the alias was last modified.
        self.last_modified_time = last_modified_time
        self.resolve_policy = resolve_policy
        self.route_policy = route_policy
        # The ID of the version to which the alias points.
        self.version_id = version_id

    def validate(self):
        if self.route_policy:
            self.route_policy.validate()

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
        if self.resolve_policy is not None:
            result['resolvePolicy'] = self.resolve_policy
        if self.route_policy is not None:
            result['routePolicy'] = self.route_policy.to_map()
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
        if m.get('resolvePolicy') is not None:
            self.resolve_policy = m.get('resolvePolicy')
        if m.get('routePolicy') is not None:
            temp_model = RoutePolicy()
            self.route_policy = temp_model.from_map(m['routePolicy'])
        if m.get('versionId') is not None:
            self.version_id = m.get('versionId')
        return self


class CreateAliasResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAliasResponseBody = None,
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
            temp_model = CreateAliasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCustomDomainHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id
        # The time when the operation is called. The format is: **EEE,d MMM yyyy HH:mm:ss GMT**.
        self.x_fc_date = x_fc_date
        # The custom request ID.
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class CreateCustomDomainRequest(TeaModel):
    def __init__(
        self,
        cert_config: CertConfig = None,
        domain_name: str = None,
        protocol: str = None,
        route_config: RouteConfig = None,
        tls_config: TLSConfig = None,
        waf_config: WAFConfig = None,
    ):
        # The configurations of the HTTPS certificate.
        self.cert_config = cert_config
        # The domain name. Enter a custom domain name that has obtained an ICP filing in the Alibaba Cloud ICP Filing system, or a custom domain name whose ICP filing information includes Alibaba Cloud as a service provider.
        self.domain_name = domain_name
        # The protocol types supported by the domain name. Valid values:
        # 
        # *   **HTTP**: Only HTTP is supported.
        # *   **HTTPS**: Only HTTPS is supported.
        # *   **HTTP,HTTPS**: HTTP and HTTPS are supported.
        self.protocol = protocol
        # The route table that maps the paths to functions when the functions are invoked by using the custom domain name.
        self.route_config = route_config
        # The Transport Layer Security (TLS) configuration.
        self.tls_config = tls_config
        # The Web Application Firewall (WAF) configuration.
        self.waf_config = waf_config

    def validate(self):
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


class CreateCustomDomainResponseBody(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        api_version: str = None,
        cert_config: CertConfig = None,
        created_time: str = None,
        domain_name: str = None,
        last_modified_time: str = None,
        protocol: str = None,
        route_config: RouteConfig = None,
        tls_config: TLSConfig = None,
        waf_config: WAFConfig = None,
    ):
        # The ID of your Alibaba Cloud account.
        self.account_id = account_id
        # The version of the API.
        self.api_version = api_version
        # The configurations of the HTTPS certificate.
        self.cert_config = cert_config
        # The time when the domain name was added.
        self.created_time = created_time
        # The domain name.
        self.domain_name = domain_name
        # The time when the domain name was last modified.
        self.last_modified_time = last_modified_time
        # The protocol types supported by the domain name. Valid values:
        # 
        # *   **HTTP**: Only HTTP is supported.
        # *   **HTTPS**: Only HTTPS is supported.
        # *   **HTTP,HTTPS**: HTTP and HTTPS are supported.
        self.protocol = protocol
        # The route table that maps the paths to functions when the functions are invoked by using the custom domain name.
        self.route_config = route_config
        # The Transport Layer Security (TLS) configuration.
        self.tls_config = tls_config
        # The Web Application Firewall (WAF) configuration.
        self.waf_config = waf_config

    def validate(self):
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
        if m.get('tlsConfig') is not None:
            temp_model = TLSConfig()
            self.tls_config = temp_model.from_map(m['tlsConfig'])
        if m.get('wafConfig') is not None:
            temp_model = WAFConfig()
            self.waf_config = temp_model.from_map(m['wafConfig'])
        return self


class CreateCustomDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateCustomDomainResponseBody = None,
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
            temp_model = CreateCustomDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFunctionHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_code_checksum: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id
        # The CRC-64 value of the function code package.
        self.x_fc_code_checksum = x_fc_code_checksum
        # The time on which the function is invoked. The format of the value is: **EEE,d MMM yyyy HH:mm:ss GMT**.
        self.x_fc_date = x_fc_date
        # The trace ID of the request. The value is the same as that of the requestId parameter in the response.
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_code_checksum is not None:
            result['X-Fc-Code-Checksum'] = self.x_fc_code_checksum
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Code-Checksum') is not None:
            self.x_fc_code_checksum = m.get('X-Fc-Code-Checksum')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class CreateFunctionRequest(TeaModel):
    def __init__(
        self,
        ca_port: int = None,
        code: Code = None,
        cpu: float = None,
        custom_container_config: CustomContainerConfig = None,
        custom_dns: CustomDNS = None,
        custom_health_check_config: CustomHealthCheckConfig = None,
        custom_runtime_config: CustomRuntimeConfig = None,
        description: str = None,
        disk_size: int = None,
        environment_variables: Dict[str, str] = None,
        function_name: str = None,
        gpu_memory_size: int = None,
        handler: str = None,
        initialization_timeout: int = None,
        initializer: str = None,
        instance_concurrency: int = None,
        instance_lifecycle_config: InstanceLifecycleConfig = None,
        instance_soft_concurrency: int = None,
        instance_type: str = None,
        layers: List[str] = None,
        memory_size: int = None,
        runtime: str = None,
        timeout: int = None,
    ):
        # The port on which the HTTP server listens for the custom runtime or custom container runtime.
        self.ca_port = ca_port
        # The code of the function. The code must be packaged into a ZIP file. Configure **code** or **customContainerConfig**.
        self.code = code
        # The number of vCPUs of the function. The value is a multiple of 0.05.
        self.cpu = cpu
        # The configurations of the Custom Container runtime. After you configure the Custom Container runtime, Function Compute can execute the function in a container created from a custom image. Configure **code** or **customContainerConfig**.
        self.custom_container_config = custom_container_config
        # The custom DNS configurations of the function.
        self.custom_dns = custom_dns
        # The custom health check configuration of the function. This parameter is applicable only to custom runtimes and custom containers.
        self.custom_health_check_config = custom_health_check_config
        # The configurations of the custom runtime.
        self.custom_runtime_config = custom_runtime_config
        # The description of the function.
        self.description = description
        # The disk size of the function. Unit: MB. Valid values: 512 and 10240.
        self.disk_size = disk_size
        # The environment variables that you configured for the function. You can obtain the values of the environment variables from the function. For more information, see [Environment variables](~~69777~~).
        self.environment_variables = environment_variables
        # The name of the function. The name can contain letters, digits, underscores (\_), and hyphens (-) only. The name cannot start with a digit or a hyphen (-). The name must be 1 to 64 characters in length.
        self.function_name = function_name
        # The GPU memory capacity for the function. Unit: MB. The value is a multiple of 1,024.
        self.gpu_memory_size = gpu_memory_size
        # The handler of the function. The format varies based on the programming language. For more information, see [Function handlers](~~157704~~).
        self.handler = handler
        # The timeout period for the execution of the Initializer hook. Unit: seconds. Default value: 3. Valid values: 1 to 300. When this period expires, the execution of the Initializer hook is terminated.
        self.initialization_timeout = initialization_timeout
        # The handler of the Initializer hook. For more information, see [Initializer hooks](~~157704~~).
        self.initializer = initializer
        # The number of requests that can be concurrently processed by a single instance.
        self.instance_concurrency = instance_concurrency
        # The lifecycle configurations of the instance.
        self.instance_lifecycle_config = instance_lifecycle_config
        # The soft concurrency of the instance. You can use this property to implement graceful scale-ups for instances. If the number of concurrent requests on an instance is greater than the soft concurrency value of the instance, an instance scale-up is triggered. For example, if your instance requires a long time to start, you can specify a suitable soft concurrency to start the instance in advance.
        # 
        # The value must be less than or equal to that of the **instanceConcurrency** parameter.
        self.instance_soft_concurrency = instance_soft_concurrency
        # The instance type of the function. Valid values:
        # 
        # *   **e1**: elastic instance
        # *   **c1**: performance instance
        # *   **fc.gpu.tesla.1**: GPU-accelerated instance (Tesla T4)
        # *   **fc.gpu.ampere.1**: GPU-accelerated instance (Ampere A10)
        # *   **g1**: same as **fc.gpu.tesla.1**\
        # 
        # Default value: e1
        self.instance_type = instance_type
        # An array that consists of the information of layers.
        # 
        # >  If multiple layers exist, the layers are merged based on the array subscripts in descending order. The content of a layer with a smaller subscript overwrites that of a larger subscript.
        self.layers = layers
        # The memory size of the function. Unit: MB. The value must be a multiple of 64. The memory size varies based on the function instance type. For more information, see the "Instance types" section of the [Instance types and usage modes](~~179379~~) topic.
        self.memory_size = memory_size
        # The runtime of the function. Valid values: **nodejs16**, **nodejs14**, **nodejs12**, **nodejs10**, **nodejs8**, **nodejs6**, **nodejs4.4**, **python3.10**, **python3.9**, **python3**, **python2.7**, **java11**, **java8**, **go1**, **php7.2**, **dotnetcore3.1**, **dotnetcore2.1**, **custom.debian10**, **custom**, and **custom-container**. For more information, see [Supported function runtime environments](~~73338~~).
        self.runtime = runtime
        # The timeout period for the execution of the function. Unit: seconds. Default value: 3. Minimum value: 1. When this period is elapsed, the function execution is terminated.
        self.timeout = timeout

    def validate(self):
        if self.code:
            self.code.validate()
        if self.custom_container_config:
            self.custom_container_config.validate()
        if self.custom_dns:
            self.custom_dns.validate()
        if self.custom_health_check_config:
            self.custom_health_check_config.validate()
        if self.custom_runtime_config:
            self.custom_runtime_config.validate()
        if self.instance_lifecycle_config:
            self.instance_lifecycle_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ca_port is not None:
            result['caPort'] = self.ca_port
        if self.code is not None:
            result['code'] = self.code.to_map()
        if self.cpu is not None:
            result['cpu'] = self.cpu
        if self.custom_container_config is not None:
            result['customContainerConfig'] = self.custom_container_config.to_map()
        if self.custom_dns is not None:
            result['customDNS'] = self.custom_dns.to_map()
        if self.custom_health_check_config is not None:
            result['customHealthCheckConfig'] = self.custom_health_check_config.to_map()
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
        if self.gpu_memory_size is not None:
            result['gpuMemorySize'] = self.gpu_memory_size
        if self.handler is not None:
            result['handler'] = self.handler
        if self.initialization_timeout is not None:
            result['initializationTimeout'] = self.initialization_timeout
        if self.initializer is not None:
            result['initializer'] = self.initializer
        if self.instance_concurrency is not None:
            result['instanceConcurrency'] = self.instance_concurrency
        if self.instance_lifecycle_config is not None:
            result['instanceLifecycleConfig'] = self.instance_lifecycle_config.to_map()
        if self.instance_soft_concurrency is not None:
            result['instanceSoftConcurrency'] = self.instance_soft_concurrency
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        if self.layers is not None:
            result['layers'] = self.layers
        if self.memory_size is not None:
            result['memorySize'] = self.memory_size
        if self.runtime is not None:
            result['runtime'] = self.runtime
        if self.timeout is not None:
            result['timeout'] = self.timeout
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('caPort') is not None:
            self.ca_port = m.get('caPort')
        if m.get('code') is not None:
            temp_model = Code()
            self.code = temp_model.from_map(m['code'])
        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')
        if m.get('customContainerConfig') is not None:
            temp_model = CustomContainerConfig()
            self.custom_container_config = temp_model.from_map(m['customContainerConfig'])
        if m.get('customDNS') is not None:
            temp_model = CustomDNS()
            self.custom_dns = temp_model.from_map(m['customDNS'])
        if m.get('customHealthCheckConfig') is not None:
            temp_model = CustomHealthCheckConfig()
            self.custom_health_check_config = temp_model.from_map(m['customHealthCheckConfig'])
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
        if m.get('gpuMemorySize') is not None:
            self.gpu_memory_size = m.get('gpuMemorySize')
        if m.get('handler') is not None:
            self.handler = m.get('handler')
        if m.get('initializationTimeout') is not None:
            self.initialization_timeout = m.get('initializationTimeout')
        if m.get('initializer') is not None:
            self.initializer = m.get('initializer')
        if m.get('instanceConcurrency') is not None:
            self.instance_concurrency = m.get('instanceConcurrency')
        if m.get('instanceLifecycleConfig') is not None:
            temp_model = InstanceLifecycleConfig()
            self.instance_lifecycle_config = temp_model.from_map(m['instanceLifecycleConfig'])
        if m.get('instanceSoftConcurrency') is not None:
            self.instance_soft_concurrency = m.get('instanceSoftConcurrency')
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        if m.get('layers') is not None:
            self.layers = m.get('layers')
        if m.get('memorySize') is not None:
            self.memory_size = m.get('memorySize')
        if m.get('runtime') is not None:
            self.runtime = m.get('runtime')
        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')
        return self


class CreateFunctionResponseBody(TeaModel):
    def __init__(
        self,
        ca_port: int = None,
        code_checksum: str = None,
        code_size: int = None,
        cpu: float = None,
        created_time: str = None,
        custom_container_config: CustomContainerConfig = None,
        custom_dns: CustomDNS = None,
        custom_health_check_config: CustomHealthCheckConfig = None,
        custom_runtime_config: CustomRuntimeConfig = None,
        description: str = None,
        disk_size: int = None,
        environment_variables: Dict[str, str] = None,
        function_id: str = None,
        function_name: str = None,
        gpu_memory_size: int = None,
        handler: str = None,
        initialization_timeout: int = None,
        initializer: str = None,
        instance_concurrency: int = None,
        instance_lifecycle_config: InstanceLifecycleConfig = None,
        instance_soft_concurrency: int = None,
        instance_type: str = None,
        last_modified_time: str = None,
        layers: List[str] = None,
        layers_arn_v2: List[str] = None,
        memory_size: int = None,
        runtime: str = None,
        timeout: int = None,
    ):
        # The port on which the HTTP server listens for the custom runtime or custom container runtime.
        self.ca_port = ca_port
        # The CRC-64 value of the function code package.
        self.code_checksum = code_checksum
        # The size of the function code package that is returned by the system. Unit: bytes.
        self.code_size = code_size
        # The number of vCPUs of the function. The value is a multiple of 0.05.
        self.cpu = cpu
        # The time when the function was created.
        self.created_time = created_time
        # The configurations of the custom container runtime. After you configure the custom container runtime, Function Compute can execute the function in a container created from a custom image.
        self.custom_container_config = custom_container_config
        # The custom DNS configurations of the function.
        self.custom_dns = custom_dns
        # The custom health check configuration of the function. This parameter is applicable only to custom runtimes and custom containers.
        self.custom_health_check_config = custom_health_check_config
        # The configurations of the custom runtime.
        self.custom_runtime_config = custom_runtime_config
        # The description of the function.
        self.description = description
        # The disk size of the function. Unit: MB. Valid values: 512 and 10240.
        self.disk_size = disk_size
        # The environment variables that are configured for the function. You can obtain the values of the environment variables from the function. For more information, see [Environment variables](~~69777~~).
        self.environment_variables = environment_variables
        # The unique ID that is generated by the system for the function.
        self.function_id = function_id
        # The name of the function.
        self.function_name = function_name
        # The GPU memory capacity for the function. Unit: MB. The value is a multiple of 1,024.
        self.gpu_memory_size = gpu_memory_size
        # The handler of the function.
        self.handler = handler
        # The timeout period for the execution of the Initializer hook. Unit: seconds. Default value: 3. Minimum value: 1. When the period ends, the execution of the Initializer hook is terminated.
        self.initialization_timeout = initialization_timeout
        # The handler of the Initializer hook. The format is determined by the programming language.
        self.initializer = initializer
        # The number of requests that can be concurrently processed by a single instance.
        self.instance_concurrency = instance_concurrency
        # The lifecycle configurations of the instance.
        self.instance_lifecycle_config = instance_lifecycle_config
        # The soft concurrency of the instance. You can use this parameter to implement graceful scale-up of instances. If the number of concurrent requests on an instance is greater than the value of soft concurrency, an instance scale-up is triggered. For example, if your instance requires a long time to start, you can specify a suitable soft concurrency to start the instance in advance.
        # 
        # The value must be less than or equal to that of the **instanceConcurrency** parameter.
        self.instance_soft_concurrency = instance_soft_concurrency
        # The instance type of the function. Valid values:
        # 
        # *   **e1**: elastic instance
        # *   **c1**: performance instance
        # *   **fc.gpu.tesla.1**: GPU-accelerated instance (Tesla T4)
        # *   **fc.gpu.ampere.1**: GPU-accelerated instance (Ampere A10)
        # *   **g1**: same as **fc.gpu.tesla.1**\
        self.instance_type = instance_type
        # The time when the function was last modified.
        self.last_modified_time = last_modified_time
        # An array that consists of the information of layers.
        # 
        # >  If multiple layers exist, the layers are merged based on the array subscripts in descending order. The content of a layer with a smaller subscript overwrites that of a larger subscript.
        self.layers = layers
        # ARN list of layers
        self.layers_arn_v2 = layers_arn_v2
        # The memory size that is configured for the function. Unit: MB.
        self.memory_size = memory_size
        # The runtime environment of the function. Valid values: **nodejs16**, **nodejs14**, **nodejs12**, **nodejs10**, **nodejs8**, **nodejs6**, **nodejs4.4**, **python3.10**, **python3.9**, **python3**, **python2.7**, **java11**, **java8**, **go1**, **php7.2**, **dotnetcore3.1**, **dotnetcore2.1**, **custom.debian10**, **custom**, and **custom-container**. For more information, see [Supported function runtime environments](~~73338~~).
        self.runtime = runtime
        # The timeout period for the execution of the function. Unit: seconds. Default value: 60. Valid values: 1 to 600. When this period expires, the execution of the function is terminated.
        self.timeout = timeout

    def validate(self):
        if self.custom_container_config:
            self.custom_container_config.validate()
        if self.custom_dns:
            self.custom_dns.validate()
        if self.custom_health_check_config:
            self.custom_health_check_config.validate()
        if self.custom_runtime_config:
            self.custom_runtime_config.validate()
        if self.instance_lifecycle_config:
            self.instance_lifecycle_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ca_port is not None:
            result['caPort'] = self.ca_port
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
        if self.custom_health_check_config is not None:
            result['customHealthCheckConfig'] = self.custom_health_check_config.to_map()
        if self.custom_runtime_config is not None:
            result['customRuntimeConfig'] = self.custom_runtime_config.to_map()
        if self.description is not None:
            result['description'] = self.description
        if self.disk_size is not None:
            result['diskSize'] = self.disk_size
        if self.environment_variables is not None:
            result['environmentVariables'] = self.environment_variables
        if self.function_id is not None:
            result['functionId'] = self.function_id
        if self.function_name is not None:
            result['functionName'] = self.function_name
        if self.gpu_memory_size is not None:
            result['gpuMemorySize'] = self.gpu_memory_size
        if self.handler is not None:
            result['handler'] = self.handler
        if self.initialization_timeout is not None:
            result['initializationTimeout'] = self.initialization_timeout
        if self.initializer is not None:
            result['initializer'] = self.initializer
        if self.instance_concurrency is not None:
            result['instanceConcurrency'] = self.instance_concurrency
        if self.instance_lifecycle_config is not None:
            result['instanceLifecycleConfig'] = self.instance_lifecycle_config.to_map()
        if self.instance_soft_concurrency is not None:
            result['instanceSoftConcurrency'] = self.instance_soft_concurrency
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time
        if self.layers is not None:
            result['layers'] = self.layers
        if self.layers_arn_v2 is not None:
            result['layersArnV2'] = self.layers_arn_v2
        if self.memory_size is not None:
            result['memorySize'] = self.memory_size
        if self.runtime is not None:
            result['runtime'] = self.runtime
        if self.timeout is not None:
            result['timeout'] = self.timeout
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('caPort') is not None:
            self.ca_port = m.get('caPort')
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
        if m.get('customHealthCheckConfig') is not None:
            temp_model = CustomHealthCheckConfig()
            self.custom_health_check_config = temp_model.from_map(m['customHealthCheckConfig'])
        if m.get('customRuntimeConfig') is not None:
            temp_model = CustomRuntimeConfig()
            self.custom_runtime_config = temp_model.from_map(m['customRuntimeConfig'])
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('diskSize') is not None:
            self.disk_size = m.get('diskSize')
        if m.get('environmentVariables') is not None:
            self.environment_variables = m.get('environmentVariables')
        if m.get('functionId') is not None:
            self.function_id = m.get('functionId')
        if m.get('functionName') is not None:
            self.function_name = m.get('functionName')
        if m.get('gpuMemorySize') is not None:
            self.gpu_memory_size = m.get('gpuMemorySize')
        if m.get('handler') is not None:
            self.handler = m.get('handler')
        if m.get('initializationTimeout') is not None:
            self.initialization_timeout = m.get('initializationTimeout')
        if m.get('initializer') is not None:
            self.initializer = m.get('initializer')
        if m.get('instanceConcurrency') is not None:
            self.instance_concurrency = m.get('instanceConcurrency')
        if m.get('instanceLifecycleConfig') is not None:
            temp_model = InstanceLifecycleConfig()
            self.instance_lifecycle_config = temp_model.from_map(m['instanceLifecycleConfig'])
        if m.get('instanceSoftConcurrency') is not None:
            self.instance_soft_concurrency = m.get('instanceSoftConcurrency')
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')
        if m.get('layers') is not None:
            self.layers = m.get('layers')
        if m.get('layersArnV2') is not None:
            self.layers_arn_v2 = m.get('layersArnV2')
        if m.get('memorySize') is not None:
            self.memory_size = m.get('memorySize')
        if m.get('runtime') is not None:
            self.runtime = m.get('runtime')
        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')
        return self


class CreateFunctionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateFunctionResponseBody = None,
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
            temp_model = CreateFunctionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLayerVersionHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id
        # The time when the function is invoked. The value is in the **EEE,d MMM yyyy HH:mm:ss GMT** format.
        self.x_fc_date = x_fc_date
        # The trace ID of the invocation request of Function Compute.
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class CreateLayerVersionRequest(TeaModel):
    def __init__(
        self,
        code: Code = None,
        compatible_runtime: List[str] = None,
        description: str = None,
    ):
        # The layer code.
        self.code = code
        # The runtimes that are supported by the layer.
        self.compatible_runtime = compatible_runtime
        # The layer description. The description can be up to 256 characters in length.
        self.description = description

    def validate(self):
        if self.code:
            self.code.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code.to_map()
        if self.compatible_runtime is not None:
            result['compatibleRuntime'] = self.compatible_runtime
        if self.description is not None:
            result['description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            temp_model = Code()
            self.code = temp_model.from_map(m['Code'])
        if m.get('compatibleRuntime') is not None:
            self.compatible_runtime = m.get('compatibleRuntime')
        if m.get('description') is not None:
            self.description = m.get('description')
        return self


class CreateLayerVersionResponseBody(TeaModel):
    def __init__(
        self,
        acl: int = None,
        arn: str = None,
        code: OutputCodeLocation = None,
        code_checksum: str = None,
        codesize: int = None,
        compatible_runtime: List[str] = None,
        create_time: str = None,
        description: str = None,
        layer_name: str = None,
        version: int = None,
    ):
        # The access mode of the layer. Digit 0 specifies that the layer is private and digit 1 specifies that the layer is public. By default, public layers are public. Custom layers can be set to private or public.
        self.acl = acl
        # The Alibaba Cloud Resource Name (ARN) of the layer.
        self.arn = arn
        # The information about the layer code package.
        self.code = code
        # The CRC-64 value of the layer code package. The value is calculated based on the **ECMA-182 **standard.
        self.code_checksum = code_checksum
        # The size of the layer code package. Unit: bytes.
        self.codesize = codesize
        # The runtimes that are supported by the layer.
        self.compatible_runtime = compatible_runtime
        # The time when the layer version was created. The time is in the yyyy-MM-ddTHH:mm:ssZ format.
        self.create_time = create_time
        # The description of the layer version.
        self.description = description
        # The layer name.
        self.layer_name = layer_name
        # The layer version.
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
        if self.arn is not None:
            result['arn'] = self.arn
        if self.code is not None:
            result['code'] = self.code.to_map()
        if self.code_checksum is not None:
            result['codeChecksum'] = self.code_checksum
        if self.codesize is not None:
            result['codesize'] = self.codesize
        if self.compatible_runtime is not None:
            result['compatibleRuntime'] = self.compatible_runtime
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.layer_name is not None:
            result['layerName'] = self.layer_name
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('acl') is not None:
            self.acl = m.get('acl')
        if m.get('arn') is not None:
            self.arn = m.get('arn')
        if m.get('code') is not None:
            temp_model = OutputCodeLocation()
            self.code = temp_model.from_map(m['code'])
        if m.get('codeChecksum') is not None:
            self.code_checksum = m.get('codeChecksum')
        if m.get('codesize') is not None:
            self.codesize = m.get('codesize')
        if m.get('compatibleRuntime') is not None:
            self.compatible_runtime = m.get('compatibleRuntime')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('layerName') is not None:
            self.layer_name = m.get('layerName')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class CreateLayerVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateLayerVersionResponseBody = None,
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
            temp_model = CreateLayerVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateServiceHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id
        # The time on which the function is invoked. The format of the value is: **EEE,d MMM yyyy HH:mm:ss GMT**.
        self.x_fc_date = x_fc_date
        # The custom request ID.
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class CreateServiceRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        internet_access: bool = None,
        log_config: LogConfig = None,
        nas_config: NASConfig = None,
        oss_mount_config: OSSMountConfig = None,
        role: str = None,
        service_name: str = None,
        tracing_config: TracingConfig = None,
        vpc_config: VPCConfig = None,
    ):
        # The description of the service.
        self.description = description
        # Specifies whether to allow functions to access the Internet. Valid values:
        # 
        # *   **true**: allows functions to access the Internet. This is the default value.
        # *   **false**: does not allow functions to access the Internet.
        self.internet_access = internet_access
        # The log configuration. Function Compute writes function execution logs to the specified Logstore.
        self.log_config = log_config
        # The configuration of the Apsara File Storage NAS (NAS) file system. The configurations allow functions in the specified service to access the NAS file system.
        self.nas_config = nas_config
        # The OSS mount configurations.
        self.oss_mount_config = oss_mount_config
        # The RAM role that is used to grant required permissions to Function Compute. The RAM role is used in the following scenarios:
        # 
        # *   Sends function execution logs to your Logstore.
        # *   Generates a token for a function to access other cloud resources during function execution.
        self.role = role
        # The name of the service. The name can contain only letters, digits, hyphens (-), and underscores (\_). It cannot start with a digit or hyphen (-). It must be 1 to 128 characters in length.
        self.service_name = service_name
        # The configuration of Tracing Analysis. After Function Compute is integrated with Tracing Analysis, you can record the duration of a request in Function Compute, view the cold start time of a function, and record the execution duration of a function. For more information, see [Tracing Analysis](~~189804~~).
        self.tracing_config = tracing_config
        # The VPC configurations. The configurations allow functions in the specified service to access the specified VPC.
        self.vpc_config = vpc_config

    def validate(self):
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
        if self.description is not None:
            result['description'] = self.description
        if self.internet_access is not None:
            result['internetAccess'] = self.internet_access
        if self.log_config is not None:
            result['logConfig'] = self.log_config.to_map()
        if self.nas_config is not None:
            result['nasConfig'] = self.nas_config.to_map()
        if self.oss_mount_config is not None:
            result['ossMountConfig'] = self.oss_mount_config.to_map()
        if self.role is not None:
            result['role'] = self.role
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        if self.tracing_config is not None:
            result['tracingConfig'] = self.tracing_config.to_map()
        if self.vpc_config is not None:
            result['vpcConfig'] = self.vpc_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('internetAccess') is not None:
            self.internet_access = m.get('internetAccess')
        if m.get('logConfig') is not None:
            temp_model = LogConfig()
            self.log_config = temp_model.from_map(m['logConfig'])
        if m.get('nasConfig') is not None:
            temp_model = NASConfig()
            self.nas_config = temp_model.from_map(m['nasConfig'])
        if m.get('ossMountConfig') is not None:
            temp_model = OSSMountConfig()
            self.oss_mount_config = temp_model.from_map(m['ossMountConfig'])
        if m.get('role') is not None:
            self.role = m.get('role')
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        if m.get('tracingConfig') is not None:
            temp_model = TracingConfig()
            self.tracing_config = temp_model.from_map(m['tracingConfig'])
        if m.get('vpcConfig') is not None:
            temp_model = VPCConfig()
            self.vpc_config = temp_model.from_map(m['vpcConfig'])
        return self


class CreateServiceResponseBody(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        description: str = None,
        internet_access: bool = None,
        last_modified_time: str = None,
        log_config: LogConfig = None,
        nas_config: NASConfig = None,
        oss_mount_config: OSSMountConfig = None,
        role: str = None,
        service_id: str = None,
        service_name: str = None,
        tracing_config: TracingConfig = None,
        use_slrauthentication: bool = None,
        vpc_config: VPCConfig = None,
    ):
        # The time when the service was created.
        self.created_time = created_time
        # The description of the service.
        self.description = description
        # Specifies whether to allow functions to access the Internet. Valid values:
        # 
        # *   **true**: allows functions in the specified service to access the Internet.
        # *   **false**: does not allow functions in the specified service to access the Internet.
        self.internet_access = internet_access
        # The time when the service was last modified.
        self.last_modified_time = last_modified_time
        # The log configuration. Function Compute writes function execution logs to the specified Logstore.
        self.log_config = log_config
        # The configuration of the NAS file system. The configurations allow functions in the specified service to access the NAS file system.
        self.nas_config = nas_config
        # The OSS mount configurations.
        self.oss_mount_config = oss_mount_config
        # The RAM role that is used to grant required permissions to Function Compute. The RAM role is used in the following scenarios:
        # 
        # *   Sends function execution logs to your Logstore.
        # *   Generates a token for a function to access other cloud resources during function execution.
        self.role = role
        # The unique ID generated by the system for the service.
        self.service_id = service_id
        # The name of the service.
        self.service_name = service_name
        # The configuration of Tracing Analysis. After Function Compute is integrated with Tracing Analysis, you can record the duration of a request in Function Compute, view the cold start time of a function, and record the execution duration of a function. For more information, see [Tracing Analysis](~~189804~~).
        self.tracing_config = tracing_config
        self.use_slrauthentication = use_slrauthentication
        # The VPC configurations. The configurations allow functions in the specified service to access the specified VPC.
        self.vpc_config = vpc_config

    def validate(self):
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
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.description is not None:
            result['description'] = self.description
        if self.internet_access is not None:
            result['internetAccess'] = self.internet_access
        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time
        if self.log_config is not None:
            result['logConfig'] = self.log_config.to_map()
        if self.nas_config is not None:
            result['nasConfig'] = self.nas_config.to_map()
        if self.oss_mount_config is not None:
            result['ossMountConfig'] = self.oss_mount_config.to_map()
        if self.role is not None:
            result['role'] = self.role
        if self.service_id is not None:
            result['serviceId'] = self.service_id
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        if self.tracing_config is not None:
            result['tracingConfig'] = self.tracing_config.to_map()
        if self.use_slrauthentication is not None:
            result['useSLRAuthentication'] = self.use_slrauthentication
        if self.vpc_config is not None:
            result['vpcConfig'] = self.vpc_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('internetAccess') is not None:
            self.internet_access = m.get('internetAccess')
        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')
        if m.get('logConfig') is not None:
            temp_model = LogConfig()
            self.log_config = temp_model.from_map(m['logConfig'])
        if m.get('nasConfig') is not None:
            temp_model = NASConfig()
            self.nas_config = temp_model.from_map(m['nasConfig'])
        if m.get('ossMountConfig') is not None:
            temp_model = OSSMountConfig()
            self.oss_mount_config = temp_model.from_map(m['ossMountConfig'])
        if m.get('role') is not None:
            self.role = m.get('role')
        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        if m.get('tracingConfig') is not None:
            temp_model = TracingConfig()
            self.tracing_config = temp_model.from_map(m['tracingConfig'])
        if m.get('useSLRAuthentication') is not None:
            self.use_slrauthentication = m.get('useSLRAuthentication')
        if m.get('vpcConfig') is not None:
            temp_model = VPCConfig()
            self.vpc_config = temp_model.from_map(m['vpcConfig'])
        return self


class CreateServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateServiceResponseBody = None,
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
            temp_model = CreateServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTriggerHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id
        # The time when the request is initiated on the client. The format of the value is: **EEE,d MMM yyyy HH:mm:ss GMT**.
        self.x_fc_date = x_fc_date
        # The custom request ID.
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class CreateTriggerRequest(TeaModel):
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
        # The description of the trigger.
        self.description = description
        # The role that is used by the event source such as Object Storage Service (OSS) to invoke the function. For more information, see [Overview](~~53102~~).
        self.invocation_role = invocation_role
        # The version or alias of the service.
        self.qualifier = qualifier
        # The Alibaba Cloud Resource Name (ARN) of the event source for the trigger.
        self.source_arn = source_arn
        # The configurations of the trigger. The configurations vary based on the trigger type. For more information about the format, see the following topics:
        # 
        # *   Object Storage Service (OSS) trigger: [OSSTriggerConfig](~~415697~~).
        # *   Simple Log Service trigger: [LogTriggerConfig](~~415694~~).
        # *   Time trigger: [TimeTriggerConfig](~~415712~~).
        # *   HTTP trigger: [HTTPTriggerConfig](~~415685~~).
        # *   Tablestore trigger: Specify the **SourceArn** parameter and leave this parameter empty.
        # *   Alibaba Cloud CDN event trigger: [CDNEventsTriggerConfig](~~415674~~).
        # *   Message Service (MNS) topic trigger: [MnsTopicTriggerConfig](~~415695~~).
        # *   EventBridge triggers: [EventBridgeTriggerConfig](~~2508622~~).
        self.trigger_config = trigger_config
        # The name of the trigger. The name contains only letters, digits, hyphens (-), and underscores (\_). The name must be 1 to 128 characters in length and cannot start with a digit or hyphen (-).
        self.trigger_name = trigger_name
        # The type of the trigger. Valid values:
        # 
        # *   **oss**: OSS event trigger. For more information, see [Overview](~~62922~~).
        # *   **log**: Simple Log Service trigger. For more information, see [Overview](~~84386~~).
        # *   **timer**: time trigger. For more information, see [Overview](~~68172~~).
        # *   **http**: HTTP trigger. For more information, see [Overview](~~71229~~).
        # *   **tablestore**: Tablestore trigger. For more information, see [Overview](~~100092~~).
        # *   **cdn_events**: CDN event trigger. For more information, see [Overview](~~73333~~).
        # *   **mns_topic**: MNS topic trigger. For more information, see [Overview](~~97032~~).
        # *   **eventbridge**: EventBridge triggers.
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


class CreateTriggerResponseBody(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        description: str = None,
        domain_name: str = None,
        invocation_role: str = None,
        last_modified_time: str = None,
        qualifier: str = None,
        source_arn: str = None,
        trigger_config: str = None,
        trigger_id: str = None,
        trigger_name: str = None,
        trigger_type: str = None,
        url_internet: str = None,
        url_intranet: str = None,
    ):
        # The time when the trigger was created.
        self.created_time = created_time
        # The description of the trigger.
        self.description = description
        # The domain name used to invoke the function by using HTTP. You can add this domain name as the prefix to the endpoint of Function Compute. This way, you can invoke the function that corresponds to the trigger by using HTTP. For example, `{domainName}.cn-shanghai.fc.aliyuncs.com`.
        self.domain_name = domain_name
        # The ARN of the RAM role that is used by the event source to invoke the function.
        self.invocation_role = invocation_role
        # The time when the trigger was last modified.
        self.last_modified_time = last_modified_time
        # The version of the service.
        self.qualifier = qualifier
        # The ARN of the event source.
        self.source_arn = source_arn
        # The configurations of the trigger. The configurations vary based on the trigger type.
        self.trigger_config = trigger_config
        # The unique ID of the trigger.
        self.trigger_id = trigger_id
        # The name of the trigger. The name contains only letters, digits, hyphens (-), and underscores (\_). The name must be 1 to 128 characters in length and cannot start with a digit or hyphen (-).
        self.trigger_name = trigger_name
        # The trigger type. Valid values: **oss**, **log**, **tablestore**, **timer**, **http**, **cdn_events**, **mns_topic**, and **eventbridge**.
        self.trigger_type = trigger_type
        # The public domain address. You can access HTTP triggers over the Internet by using HTTP or HTTPS.
        self.url_internet = url_internet
        # The private endpoint. In a VPC, you can access HTTP triggers by using HTTP or HTTPS.
        self.url_intranet = url_intranet

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
        if self.domain_name is not None:
            result['domainName'] = self.domain_name
        if self.invocation_role is not None:
            result['invocationRole'] = self.invocation_role
        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        if self.source_arn is not None:
            result['sourceArn'] = self.source_arn
        if self.trigger_config is not None:
            result['triggerConfig'] = self.trigger_config
        if self.trigger_id is not None:
            result['triggerId'] = self.trigger_id
        if self.trigger_name is not None:
            result['triggerName'] = self.trigger_name
        if self.trigger_type is not None:
            result['triggerType'] = self.trigger_type
        if self.url_internet is not None:
            result['urlInternet'] = self.url_internet
        if self.url_intranet is not None:
            result['urlIntranet'] = self.url_intranet
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domainName') is not None:
            self.domain_name = m.get('domainName')
        if m.get('invocationRole') is not None:
            self.invocation_role = m.get('invocationRole')
        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        if m.get('sourceArn') is not None:
            self.source_arn = m.get('sourceArn')
        if m.get('triggerConfig') is not None:
            self.trigger_config = m.get('triggerConfig')
        if m.get('triggerId') is not None:
            self.trigger_id = m.get('triggerId')
        if m.get('triggerName') is not None:
            self.trigger_name = m.get('triggerName')
        if m.get('triggerType') is not None:
            self.trigger_type = m.get('triggerType')
        if m.get('urlInternet') is not None:
            self.url_internet = m.get('urlInternet')
        if m.get('urlIntranet') is not None:
            self.url_intranet = m.get('urlIntranet')
        return self


class CreateTriggerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateTriggerResponseBody = None,
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
            temp_model = CreateTriggerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateVpcBindingHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id
        # The time when Function Compute API is called. Specify the time in the **EEE,d MMM yyyy HH:mm:ss GMT** format.
        self.x_fc_date = x_fc_date
        # The custom request ID.
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class CreateVpcBindingRequest(TeaModel):
    def __init__(
        self,
        vpc_id: str = None,
    ):
        # The ID of the VPC to be bound.
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


class CreateVpcBindingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

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


class DeleteAliasHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        if_match: str = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        # If the ETag specified in the request matches the ETag value of the object, OSS transmits the object and returns 200 OK. If the ETag specified in the request does not match the ETag value of the object, OSS returns 412 Precondition Failed. 
        # The ETag value of a resource is used to check whether the resource has changed. You can check data integrity by using the ETag value. 
        # Default value: null
        self.if_match = if_match
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id
        # The time when Function Compute API is called. Specify the time in the **EEE,d MMM yyyy HH:mm:ss GMT** format.
        self.x_fc_date = x_fc_date
        # The trace ID of the invocation request of Function Compute.
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.if_match is not None:
            result['If-Match'] = self.if_match
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('If-Match') is not None:
            self.if_match = m.get('If-Match')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

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


class DeleteCustomDomainHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id
        # The time when Function Compute API is called. Specify the time in the **EEE,d MMM yyyy HH:mm:ss GMT** format.
        self.x_fc_date = x_fc_date
        # The custom request ID.
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

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


class DeleteFunctionHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        if_match: str = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        # The ETag value of the resource. This value is used to ensure that the modified resource is consistent with the resource to be modified. The ETag value is returned in the responses of the CREATE, GET, and UPDATE operations.
        self.if_match = if_match
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id
        # The time when Function Compute API is called. Specify the time in the **EEE,d MMM yyyy HH:mm:ss GMT** format.
        self.x_fc_date = x_fc_date
        # The trace ID of the request for Function Compute API. The value is the same as that of the requestId parameter in the response.
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.if_match is not None:
            result['If-Match'] = self.if_match
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('If-Match') is not None:
            self.if_match = m.get('If-Match')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

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


class DeleteFunctionAsyncInvokeConfigHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id
        # The time when Function Compute API is called. Specify the time in the **EEE,d MMM yyyy HH:mm:ss GMT** format.
        self.x_fc_date = x_fc_date
        # The trace ID of the invocation request of Function Compute.
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class DeleteFunctionAsyncInvokeConfigRequest(TeaModel):
    def __init__(
        self,
        qualifier: str = None,
    ):
        # The qualifier.
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


class DeleteFunctionAsyncInvokeConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

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


class DeleteFunctionOnDemandConfigHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        if_match: str = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        # If the ETag specified in the request matches the ETag value of the OndemandConfig, FC returns 200 OK. If the ETag specified in the request does not match the ETag value of the object, FC returns 412 Precondition Failed.
        self.if_match = if_match
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id
        # The start time when the function is invoked. Specify the time in the **EEE,d MMM yyyy HH:mm:ss GMT** format.
        self.x_fc_date = x_fc_date
        # The trace ID of the request for Function Compute API, which is also the unique ID of the request.
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.if_match is not None:
            result['If-Match'] = self.if_match
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('If-Match') is not None:
            self.if_match = m.get('If-Match')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class DeleteFunctionOnDemandConfigRequest(TeaModel):
    def __init__(
        self,
        qualifier: str = None,
    ):
        # The alias of the service or LATEST.
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


class DeleteFunctionOnDemandConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

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


class DeleteLayerVersionHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id
        # The time when Function Compute API is called. Specify the time in the **EEE,d MMM yyyy HH:mm:ss GMT** format.
        self.x_fc_date = x_fc_date
        # The trace ID of the request for Function Compute API.
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

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


class DeleteServiceHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        if_match: str = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        # The ETag value of the service. This value is used to ensure that the modified service is consistent with the service to be modified. The ETag value is returned in the responses of the [CreateService](~~175256~~), [UpdateService](~~188167~~), and [GetService](~~189225~~) operations.
        self.if_match = if_match
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id
        # The time when Function Compute API is called. Specify the time in the **EEE,d MMM yyyy HH:mm:ss GMT** format.
        self.x_fc_date = x_fc_date
        # The custom request ID.
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.if_match is not None:
            result['If-Match'] = self.if_match
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('If-Match') is not None:
            self.if_match = m.get('If-Match')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class DeleteServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

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


class DeleteServiceVersionHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id
        # The time when Function Compute API is called. Specify the time in the **EEE,d MMM yyyy HH:mm:ss GMT** format.
        self.x_fc_date = x_fc_date
        # The trace ID of the invocation request of Function Compute.
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class DeleteServiceVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

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


class DeleteTriggerHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        if_match: str = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        # This parameter is used to ensure that the modified resource is consistent with the resource to be modified. You can obtain the parameter value from the responses of [CreateTrigger](~~415729~~), [GetTrigger](~~415732~~), and [UpdateTrigger](~~415731~~) operations.
        self.if_match = if_match
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id
        # The time when the request is initiated on the client. The format of the value is: **EEE,d MMM yyyy HH:mm:ss GMT**.
        self.x_fc_date = x_fc_date
        # The custom request ID.
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.if_match is not None:
            result['If-Match'] = self.if_match
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('If-Match') is not None:
            self.if_match = m.get('If-Match')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

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


class DeleteVpcBindingHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id
        # The time when Function Compute API is called. Specify the time in the **EEE,d MMM yyyy HH:mm:ss GMT** format.
        self.x_fc_date = x_fc_date
        # The custom request ID.
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

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


class DeregisterEventSourceHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id
        # The time when Function Compute API is called. Specify the time in the **EEE,d MMM yyyy HH:mm:ss GMT** format.
        self.x_fc_date = x_fc_date
        # The trace ID of the invocation request of Function Compute.
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class DeregisterEventSourceRequest(TeaModel):
    def __init__(
        self,
        qualifier: str = None,
    ):
        # The version or alias of the service.
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


class DeregisterEventSourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

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


class GetAccountSettingsHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id
        # The time when Function Compute API is called. Specify the time in the **EEE,d MMM yyyy HH:mm:ss GMT** format.
        self.x_fc_date = x_fc_date
        # The custom request ID.
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class GetAccountSettingsResponseBody(TeaModel):
    def __init__(
        self,
        available_azs: List[str] = None,
        default_role: str = None,
    ):
        # The list of zones.
        self.available_azs = available_azs
        # The default RAM role.
        self.default_role = default_role

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.available_azs is not None:
            result['availableAZs'] = self.available_azs
        if self.default_role is not None:
            result['defaultRole'] = self.default_role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('availableAZs') is not None:
            self.available_azs = m.get('availableAZs')
        if m.get('defaultRole') is not None:
            self.default_role = m.get('defaultRole')
        return self


class GetAccountSettingsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAccountSettingsResponseBody = None,
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
            temp_model = GetAccountSettingsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAliasHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id
        # The time on which the function is invoked. The format of the value is: **EEE,d MMM yyyy HH:mm:ss GMT**.
        self.x_fc_date = x_fc_date
        # The trace ID of the invocation request of Function Compute.
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class GetAliasResponseBody(TeaModel):
    def __init__(
        self,
        additional_version_weight: Dict[str, float] = None,
        alias_name: str = None,
        created_time: str = None,
        description: str = None,
        last_modified_time: str = None,
        resolve_policy: str = None,
        route_policy: RoutePolicy = None,
        version_id: str = None,
    ):
        # The additional version to which the alias points and the weight of the additional version.
        # 
        # *   The additional version takes effect only when the function is invoked.
        # *   The value consists of a version number and a specific weight. For example, 2:0.05 indicates that when a function is invoked, Version 2 is the canary release version, 5% of the traffic is distributed to the canary release version, and 95% of the traffic is distributed to the major version.
        self.additional_version_weight = additional_version_weight
        # The name of the alias.
        self.alias_name = alias_name
        # The time when the alias was created.
        self.created_time = created_time
        # The description of the alias.
        self.description = description
        # The time when the alias was last modified.
        self.last_modified_time = last_modified_time
        # The canary release mode. Valid values:
        # 
        # *   **Random**: random canary release. This is the default value.
        # *   **Content**: rule-based canary release.
        self.resolve_policy = resolve_policy
        # The canary release rule. Traffic that meets the canary release rule is routed to the canary release instance.
        self.route_policy = route_policy
        # The version to which the alias points.
        self.version_id = version_id

    def validate(self):
        if self.route_policy:
            self.route_policy.validate()

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
        if self.resolve_policy is not None:
            result['resolvePolicy'] = self.resolve_policy
        if self.route_policy is not None:
            result['routePolicy'] = self.route_policy.to_map()
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
        if m.get('resolvePolicy') is not None:
            self.resolve_policy = m.get('resolvePolicy')
        if m.get('routePolicy') is not None:
            temp_model = RoutePolicy()
            self.route_policy = temp_model.from_map(m['routePolicy'])
        if m.get('versionId') is not None:
            self.version_id = m.get('versionId')
        return self


class GetAliasResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAliasResponseBody = None,
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
            temp_model = GetAliasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCustomDomainHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id
        # The time when the operation is called. The format is: **EEE,d MMM yyyy HH:mm:ss GMT**.
        self.x_fc_date = x_fc_date
        # The custom request ID.
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class GetCustomDomainResponseBody(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        api_version: str = None,
        cert_config: CertConfig = None,
        created_time: str = None,
        domain_name: str = None,
        last_modified_time: str = None,
        protocol: str = None,
        route_config: RouteConfig = None,
        tls_config: TLSConfig = None,
        waf_config: WAFConfig = None,
    ):
        # The ID of your Alibaba Cloud account.
        self.account_id = account_id
        # The version of the API.
        self.api_version = api_version
        # The configurations of the HTTPS certificate.
        self.cert_config = cert_config
        # The time when the custom domain name was created.
        self.created_time = created_time
        # The domain name.
        self.domain_name = domain_name
        # The time when the domain name was last modified.
        self.last_modified_time = last_modified_time
        # The protocol types supported by the domain name. Valid values:
        # 
        # *   **HTTP**: Only HTTP is supported.
        # *   **HTTPS**: Only HTTPS is supported.
        # *   **HTTP,HTTPS**: HTTP and HTTPS are supported.
        self.protocol = protocol
        # The route table that maps the paths to functions when the functions are invoked by using the custom domain name.
        self.route_config = route_config
        # The Transport Layer Security (TLS) configuration.
        self.tls_config = tls_config
        # The Web Application Firewall (WAF) configuration.
        self.waf_config = waf_config

    def validate(self):
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
        if m.get('tlsConfig') is not None:
            temp_model = TLSConfig()
            self.tls_config = temp_model.from_map(m['tlsConfig'])
        if m.get('wafConfig') is not None:
            temp_model = WAFConfig()
            self.waf_config = temp_model.from_map(m['wafConfig'])
        return self


class GetCustomDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetCustomDomainResponseBody = None,
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
            temp_model = GetCustomDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFunctionHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id
        # The time on which the function is invoked. The format of the value is: **EEE,d MMM yyyy HH:mm:ss GMT**.
        self.x_fc_date = x_fc_date
        # The custom request ID.
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class GetFunctionRequest(TeaModel):
    def __init__(
        self,
        qualifier: str = None,
    ):
        # The version or alias of the service.
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


class GetFunctionResponseBody(TeaModel):
    def __init__(
        self,
        ca_port: int = None,
        code_checksum: str = None,
        code_size: int = None,
        cpu: float = None,
        created_time: str = None,
        custom_container_config: CustomContainerConfigInfo = None,
        custom_dns: CustomDNS = None,
        custom_health_check_config: CustomHealthCheckConfig = None,
        custom_runtime_config: CustomRuntimeConfig = None,
        description: str = None,
        disk_size: int = None,
        environment_variables: Dict[str, str] = None,
        function_id: str = None,
        function_name: str = None,
        gpu_memory_size: int = None,
        handler: str = None,
        initialization_timeout: int = None,
        initializer: str = None,
        instance_concurrency: int = None,
        instance_lifecycle_config: InstanceLifecycleConfig = None,
        instance_soft_concurrency: int = None,
        instance_type: str = None,
        last_modified_time: str = None,
        layers: List[str] = None,
        layers_arn_v2: List[str] = None,
        memory_size: int = None,
        runtime: str = None,
        timeout: int = None,
    ):
        # The port on which the HTTP server listens for the custom runtime or custom container runtime.
        self.ca_port = ca_port
        # The CRC-64 value of the function code package.
        self.code_checksum = code_checksum
        # The size of the function code package. Unit: byte.
        self.code_size = code_size
        # The number of vCPUs of the function. The value must be a multiple of 0.05.
        self.cpu = cpu
        # The time when the function was created.
        self.created_time = created_time
        # The configurations of the custom container runtime. After you configure the custom container runtime, Function Compute can execute the function in a container created from a custom image.
        self.custom_container_config = custom_container_config
        # The custom DNS configurations of the function.
        self.custom_dns = custom_dns
        # The custom health check configuration of the function. This parameter is applicable only to custom runtimes and custom containers.
        self.custom_health_check_config = custom_health_check_config
        # The configurations of the custom runtime.
        self.custom_runtime_config = custom_runtime_config
        # The description of the function.
        self.description = description
        # The disk size of the function. Unit: MB. Valid values: 512 and 10240.
        self.disk_size = disk_size
        # The environment variables that are configured for the function. You can obtain the values of the environment variables from the function. For more information, see [Environment variables](~~69777~~).
        self.environment_variables = environment_variables
        # The ID that is generated by the system for the function. Each function ID is unique in Function Compute.
        self.function_id = function_id
        # The name of the function.
        self.function_name = function_name
        # The GPU memory capacity for the function. Unit: MB. The value is a multiple of 1,024.
        self.gpu_memory_size = gpu_memory_size
        # The handler of the function. For more information, see [Function handler](~~157704~~).
        self.handler = handler
        # The timeout period for the execution of the Initializer hook. Unit: seconds. Default value: 3. Valid values: 1 to 300. When this period ends, the execution of the Initializer hook is terminated.
        self.initialization_timeout = initialization_timeout
        # The handler of the Initializer hook. The format of the value is determined by the programming language that you use. For more information, see [Initializer hook](~~157704~~).
        self.initializer = initializer
        # The number of requests that can be concurrently processed by a single instance.
        self.instance_concurrency = instance_concurrency
        # The lifecycle configurations of the instance.
        self.instance_lifecycle_config = instance_lifecycle_config
        # The soft concurrency of the instance. You can use this parameter to implement graceful scale-up of instances. If the number of concurrent requests on an instance is greater than the value of soft concurrency, an instance scale-up is triggered. For example, if your instance requires a long time to start, you can specify a suitable soft concurrency to start the instance in advance.
        # 
        # The value must be less than or equal to that of the **instanceConcurrency** parameter.
        self.instance_soft_concurrency = instance_soft_concurrency
        # The instance type of the function. Valid values:
        # 
        # *   **e1**: elastic instance
        # *   **c1**: performance instance
        # *   **fc.gpu.tesla.1**: GPU-accelerated instance (Tesla T4)
        # *   **fc.gpu.ampere.1**: GPU-accelerated instance (Ampere A10)
        # *   **g1**: same as fc.gpu.tesla.1
        self.instance_type = instance_type
        # The time when the function was last modified.
        self.last_modified_time = last_modified_time
        # The layers (ARN V1 version).
        # 
        # > Multiple layers are merged based on the order of array subscripts. The content of a layer with a smaller subscript overwrites the file that has the same name as a layer with a larger subscript.
        # 
        # **\
        # 
        # **Warning** This parameter is to be deprecated. Use layersArnV2.
        self.layers = layers
        # The list of layers (ARN V2 version).
        # 
        # > Multiple layers are merged based on the order of array subscripts. The content of a layer with a smaller subscript overwrites the file that has the same name as a layer with a larger subscript.
        self.layers_arn_v2 = layers_arn_v2
        # The memory size for the function. Unit: MB. The value must be a multiple of 64. The memory size varies based on the function instance type. For more information, see [Instance types](~~179379~~).
        self.memory_size = memory_size
        # The runtime environment of the function. Valid values: **nodejs16**, **nodejs14**, **nodejs12**, **nodejs10**, **nodejs8**, **nodejs6**, **nodejs4.4**, **python3.9**, **python3**, **python2.7**, **java11**, **java8**, **go1**, **php7.2**, **dotnetcore2.1**, **custom**, and **custom-container**.
        self.runtime = runtime
        # The timeout period for the execution of the function. Unit: seconds. Default value: 60. Valid values: 1 to 600. When this period expires, the execution of the function is terminated.
        self.timeout = timeout

    def validate(self):
        if self.custom_container_config:
            self.custom_container_config.validate()
        if self.custom_dns:
            self.custom_dns.validate()
        if self.custom_health_check_config:
            self.custom_health_check_config.validate()
        if self.custom_runtime_config:
            self.custom_runtime_config.validate()
        if self.instance_lifecycle_config:
            self.instance_lifecycle_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ca_port is not None:
            result['caPort'] = self.ca_port
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
        if self.custom_health_check_config is not None:
            result['customHealthCheckConfig'] = self.custom_health_check_config.to_map()
        if self.custom_runtime_config is not None:
            result['customRuntimeConfig'] = self.custom_runtime_config.to_map()
        if self.description is not None:
            result['description'] = self.description
        if self.disk_size is not None:
            result['diskSize'] = self.disk_size
        if self.environment_variables is not None:
            result['environmentVariables'] = self.environment_variables
        if self.function_id is not None:
            result['functionId'] = self.function_id
        if self.function_name is not None:
            result['functionName'] = self.function_name
        if self.gpu_memory_size is not None:
            result['gpuMemorySize'] = self.gpu_memory_size
        if self.handler is not None:
            result['handler'] = self.handler
        if self.initialization_timeout is not None:
            result['initializationTimeout'] = self.initialization_timeout
        if self.initializer is not None:
            result['initializer'] = self.initializer
        if self.instance_concurrency is not None:
            result['instanceConcurrency'] = self.instance_concurrency
        if self.instance_lifecycle_config is not None:
            result['instanceLifecycleConfig'] = self.instance_lifecycle_config.to_map()
        if self.instance_soft_concurrency is not None:
            result['instanceSoftConcurrency'] = self.instance_soft_concurrency
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time
        if self.layers is not None:
            result['layers'] = self.layers
        if self.layers_arn_v2 is not None:
            result['layersArnV2'] = self.layers_arn_v2
        if self.memory_size is not None:
            result['memorySize'] = self.memory_size
        if self.runtime is not None:
            result['runtime'] = self.runtime
        if self.timeout is not None:
            result['timeout'] = self.timeout
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('caPort') is not None:
            self.ca_port = m.get('caPort')
        if m.get('codeChecksum') is not None:
            self.code_checksum = m.get('codeChecksum')
        if m.get('codeSize') is not None:
            self.code_size = m.get('codeSize')
        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('customContainerConfig') is not None:
            temp_model = CustomContainerConfigInfo()
            self.custom_container_config = temp_model.from_map(m['customContainerConfig'])
        if m.get('customDNS') is not None:
            temp_model = CustomDNS()
            self.custom_dns = temp_model.from_map(m['customDNS'])
        if m.get('customHealthCheckConfig') is not None:
            temp_model = CustomHealthCheckConfig()
            self.custom_health_check_config = temp_model.from_map(m['customHealthCheckConfig'])
        if m.get('customRuntimeConfig') is not None:
            temp_model = CustomRuntimeConfig()
            self.custom_runtime_config = temp_model.from_map(m['customRuntimeConfig'])
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('diskSize') is not None:
            self.disk_size = m.get('diskSize')
        if m.get('environmentVariables') is not None:
            self.environment_variables = m.get('environmentVariables')
        if m.get('functionId') is not None:
            self.function_id = m.get('functionId')
        if m.get('functionName') is not None:
            self.function_name = m.get('functionName')
        if m.get('gpuMemorySize') is not None:
            self.gpu_memory_size = m.get('gpuMemorySize')
        if m.get('handler') is not None:
            self.handler = m.get('handler')
        if m.get('initializationTimeout') is not None:
            self.initialization_timeout = m.get('initializationTimeout')
        if m.get('initializer') is not None:
            self.initializer = m.get('initializer')
        if m.get('instanceConcurrency') is not None:
            self.instance_concurrency = m.get('instanceConcurrency')
        if m.get('instanceLifecycleConfig') is not None:
            temp_model = InstanceLifecycleConfig()
            self.instance_lifecycle_config = temp_model.from_map(m['instanceLifecycleConfig'])
        if m.get('instanceSoftConcurrency') is not None:
            self.instance_soft_concurrency = m.get('instanceSoftConcurrency')
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')
        if m.get('layers') is not None:
            self.layers = m.get('layers')
        if m.get('layersArnV2') is not None:
            self.layers_arn_v2 = m.get('layersArnV2')
        if m.get('memorySize') is not None:
            self.memory_size = m.get('memorySize')
        if m.get('runtime') is not None:
            self.runtime = m.get('runtime')
        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')
        return self


class GetFunctionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetFunctionResponseBody = None,
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
            temp_model = GetFunctionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFunctionAsyncInvokeConfigHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id
        # The time when the Function Compute is called. The format is **EEE,d MMM yyyy HH:mm:ss GMT**.
        self.x_fc_date = x_fc_date
        # The trace ID of the invocation request of Function Compute.
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class GetFunctionAsyncInvokeConfigRequest(TeaModel):
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


class GetFunctionAsyncInvokeConfigResponseBody(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        destination_config: DestinationConfig = None,
        function: str = None,
        last_modified_time: str = None,
        max_async_event_age_in_seconds: int = None,
        max_async_retry_attempts: int = None,
        qualifier: str = None,
        service: str = None,
        stateful_invocation: bool = None,
    ):
        # The time when the desktop group was created.
        self.created_time = created_time
        # The configuration struct of the destination for asynchronous invocations.
        self.destination_config = destination_config
        # The name of the function.
        self.function = function
        # The time when the configuration was last modified.
        self.last_modified_time = last_modified_time
        # The maximum validity period of a message.
        self.max_async_event_age_in_seconds = max_async_event_age_in_seconds
        # The maximum number of retries allowed after an asynchronous invocation fails.
        self.max_async_retry_attempts = max_async_retry_attempts
        # The version or alias of the service to which the function belongs.
        self.qualifier = qualifier
        # The name of the service.
        self.service = service
        # Indicates whether the asynchronous task feature is enabled.
        # 
        # *   **true**: The asynchronous task feature is enabled.
        # *   **false**: The asynchronous task feature is disabled.
        self.stateful_invocation = stateful_invocation

    def validate(self):
        if self.destination_config:
            self.destination_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.destination_config is not None:
            result['destinationConfig'] = self.destination_config.to_map()
        if self.function is not None:
            result['function'] = self.function
        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time
        if self.max_async_event_age_in_seconds is not None:
            result['maxAsyncEventAgeInSeconds'] = self.max_async_event_age_in_seconds
        if self.max_async_retry_attempts is not None:
            result['maxAsyncRetryAttempts'] = self.max_async_retry_attempts
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        if self.service is not None:
            result['service'] = self.service
        if self.stateful_invocation is not None:
            result['statefulInvocation'] = self.stateful_invocation
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('destinationConfig') is not None:
            temp_model = DestinationConfig()
            self.destination_config = temp_model.from_map(m['destinationConfig'])
        if m.get('function') is not None:
            self.function = m.get('function')
        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')
        if m.get('maxAsyncEventAgeInSeconds') is not None:
            self.max_async_event_age_in_seconds = m.get('maxAsyncEventAgeInSeconds')
        if m.get('maxAsyncRetryAttempts') is not None:
            self.max_async_retry_attempts = m.get('maxAsyncRetryAttempts')
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        if m.get('service') is not None:
            self.service = m.get('service')
        if m.get('statefulInvocation') is not None:
            self.stateful_invocation = m.get('statefulInvocation')
        return self


class GetFunctionAsyncInvokeConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetFunctionAsyncInvokeConfigResponseBody = None,
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
            temp_model = GetFunctionAsyncInvokeConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFunctionCodeHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id
        # The time on which the function is invoked. The format of the value is: **EEE,d MMM yyyy HH:mm:ss GMT**.
        self.x_fc_date = x_fc_date
        # The custom request ID.
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class GetFunctionCodeRequest(TeaModel):
    def __init__(
        self,
        qualifier: str = None,
    ):
        # The version or alias of the service.
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


class GetFunctionCodeResponseBody(TeaModel):
    def __init__(
        self,
        checksum: str = None,
        url: str = None,
    ):
        # The CRC-64 value of the function code package.
        self.checksum = checksum
        # The URL of the function code package.
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


class GetFunctionCodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetFunctionCodeResponseBody = None,
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
            temp_model = GetFunctionCodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFunctionOnDemandConfigHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id
        # The time on which the function is invoked. The format of the value is: **EEE,d MMM yyyy HH:mm:ss GMT**.
        self.x_fc_date = x_fc_date
        # The unique ID of the trace.
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class GetFunctionOnDemandConfigRequest(TeaModel):
    def __init__(
        self,
        qualifier: str = None,
    ):
        # Service alias or LATEST. Other versions are not supported.
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


class GetFunctionOnDemandConfigResponseBody(TeaModel):
    def __init__(
        self,
        maximum_instance_count: int = None,
        resource: str = None,
    ):
        # The maximum number of instances.
        self.maximum_instance_count = maximum_instance_count
        # The description of the resource.
        self.resource = resource

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.maximum_instance_count is not None:
            result['maximumInstanceCount'] = self.maximum_instance_count
        if self.resource is not None:
            result['resource'] = self.resource
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maximumInstanceCount') is not None:
            self.maximum_instance_count = m.get('maximumInstanceCount')
        if m.get('resource') is not None:
            self.resource = m.get('resource')
        return self


class GetFunctionOnDemandConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetFunctionOnDemandConfigResponseBody = None,
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
            temp_model = GetFunctionOnDemandConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLayerVersionHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        # This parameter is returned only when the information about a specific layer version is queried.
        self.x_fc_account_id = x_fc_account_id
        # The location of the layer code.
        self.x_fc_date = x_fc_date
        # The structure of the layer code.
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
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
            temp_model = Layer()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProvisionConfigHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id
        # The start time when the function is invoked. Specify the time in the **EEE,d MMM yyyy HH:mm:ss GMT** format.
        self.x_fc_date = x_fc_date
        # The trace ID of the invocation request of Function Compute.
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class GetProvisionConfigRequest(TeaModel):
    def __init__(
        self,
        qualifier: str = None,
    ):
        # The name of the alias.
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


class GetProvisionConfigResponseBody(TeaModel):
    def __init__(
        self,
        always_allocate_cpu: bool = None,
        current: int = None,
        current_error: str = None,
        resource: str = None,
        scheduled_actions: List[ScheduledActions] = None,
        target: int = None,
        target_tracking_policies: List[TargetTrackingPolicies] = None,
    ):
        # Specifies whether to always allocate CPU to a function instance.
        self.always_allocate_cpu = always_allocate_cpu
        # The actual number of provisioned instances.
        self.current = current
        # The error message returned if a provisioned instance fails to be created.
        self.current_error = current_error
        # The description of the resource.
        self.resource = resource
        # The configurations of scheduled auto scaling.
        self.scheduled_actions = scheduled_actions
        # The expected number of provisioned instances.
        self.target = target
        # The configurations of metric-based auto scaling.
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
        if self.resource is not None:
            result['resource'] = self.resource
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
        if m.get('resource') is not None:
            self.resource = m.get('resource')
        self.scheduled_actions = []
        if m.get('scheduledActions') is not None:
            for k in m.get('scheduledActions'):
                temp_model = ScheduledActions()
                self.scheduled_actions.append(temp_model.from_map(k))
        if m.get('target') is not None:
            self.target = m.get('target')
        self.target_tracking_policies = []
        if m.get('targetTrackingPolicies') is not None:
            for k in m.get('targetTrackingPolicies'):
                temp_model = TargetTrackingPolicies()
                self.target_tracking_policies.append(temp_model.from_map(k))
        return self


class GetProvisionConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetProvisionConfigResponseBody = None,
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
            temp_model = GetProvisionConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetResourceTagsHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id
        # The time when Function Compute API is called. Specify the time in the **EEE,d MMM yyyy HH:mm:ss GMT** format.
        self.x_fc_date = x_fc_date
        # The custom request ID.
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class GetResourceTagsRequest(TeaModel):
    def __init__(
        self,
        resource_arn: str = None,
    ):
        # The Alibaba Cloud Resource Name (ARN) of the resource. 
        # 
        # > You can use the value of this parameter to query the information about the resource, such as the account, service, and region information of the resource. You can manage tags only for services for top level resources.
        self.resource_arn = resource_arn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_arn is not None:
            result['resourceArn'] = self.resource_arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resourceArn') is not None:
            self.resource_arn = m.get('resourceArn')
        return self


class GetResourceTagsResponseBody(TeaModel):
    def __init__(
        self,
        resource_arn: str = None,
        tags: Dict[str, str] = None,
    ):
        # The ARN of the resource. 
        # 
        # > You can use the value of this parameter to query the information about the resource, such as the account, service, and region information of the resource.
        self.resource_arn = resource_arn
        # The tag dictionary.
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


class GetResourceTagsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetResourceTagsResponseBody = None,
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
            temp_model = GetResourceTagsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetServiceHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id
        # The time on which the function is invoked. The format of the value is: **EEE,d MMM yyyy HH:mm:ss GMT**.
        self.x_fc_date = x_fc_date
        # The custom request ID.
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class GetServiceRequest(TeaModel):
    def __init__(
        self,
        qualifier: str = None,
    ):
        # The version or alias of the service.
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


class GetServiceResponseBody(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        description: str = None,
        internet_access: bool = None,
        last_modified_time: str = None,
        log_config: LogConfig = None,
        nas_config: NASConfig = None,
        oss_mount_config: OSSMountConfig = None,
        role: str = None,
        service_id: str = None,
        service_name: str = None,
        tracing_config: TracingConfig = None,
        use_slrauthentication: bool = None,
        vpc_config: VPCConfig = None,
    ):
        # The time when the service was created.
        self.created_time = created_time
        # The description of the service.
        self.description = description
        # Specifies whether to allow functions to access the Internet. Valid values:
        # 
        # *   **true**: allows functions in the specified service to access the Internet.
        # *   **false**: does not allow functions to access the Internet.
        self.internet_access = internet_access
        # The time when the service was last modified.
        self.last_modified_time = last_modified_time
        # The log configuration, which specifies a Logstore to store function execution logs.
        self.log_config = log_config
        # The configurations of the NAS file system. The configuration allows functions in the specified service in Function Compute to access the NAS file system.
        self.nas_config = nas_config
        # The OSS mount configurations.
        self.oss_mount_config = oss_mount_config
        # The RAM role that is used to grant required permissions to Function Compute. Scenarios:
        # 
        # *   Sends function execution logs to your Logstore.
        # *   Generates a token for a function to access other cloud resources during function execution.
        self.role = role
        # The unique ID generated by the system for the service.
        self.service_id = service_id
        # The name of the service.
        self.service_name = service_name
        # The configuration of Tracing Analysis. After you configure Tracing Analysis for a service in Function Compute, you can record the execution duration of a request, view the amount of cold start time for a function, and record the execution duration of a function. For more information, see [Overview](~~189804~~).
        self.tracing_config = tracing_config
        self.use_slrauthentication = use_slrauthentication
        # The VPC configuration. The configuration allows a function to access the specified VPC.
        self.vpc_config = vpc_config

    def validate(self):
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
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.description is not None:
            result['description'] = self.description
        if self.internet_access is not None:
            result['internetAccess'] = self.internet_access
        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time
        if self.log_config is not None:
            result['logConfig'] = self.log_config.to_map()
        if self.nas_config is not None:
            result['nasConfig'] = self.nas_config.to_map()
        if self.oss_mount_config is not None:
            result['ossMountConfig'] = self.oss_mount_config.to_map()
        if self.role is not None:
            result['role'] = self.role
        if self.service_id is not None:
            result['serviceId'] = self.service_id
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        if self.tracing_config is not None:
            result['tracingConfig'] = self.tracing_config.to_map()
        if self.use_slrauthentication is not None:
            result['useSLRAuthentication'] = self.use_slrauthentication
        if self.vpc_config is not None:
            result['vpcConfig'] = self.vpc_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('internetAccess') is not None:
            self.internet_access = m.get('internetAccess')
        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')
        if m.get('logConfig') is not None:
            temp_model = LogConfig()
            self.log_config = temp_model.from_map(m['logConfig'])
        if m.get('nasConfig') is not None:
            temp_model = NASConfig()
            self.nas_config = temp_model.from_map(m['nasConfig'])
        if m.get('ossMountConfig') is not None:
            temp_model = OSSMountConfig()
            self.oss_mount_config = temp_model.from_map(m['ossMountConfig'])
        if m.get('role') is not None:
            self.role = m.get('role')
        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        if m.get('tracingConfig') is not None:
            temp_model = TracingConfig()
            self.tracing_config = temp_model.from_map(m['tracingConfig'])
        if m.get('useSLRAuthentication') is not None:
            self.use_slrauthentication = m.get('useSLRAuthentication')
        if m.get('vpcConfig') is not None:
            temp_model = VPCConfig()
            self.vpc_config = temp_model.from_map(m['vpcConfig'])
        return self


class GetServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetServiceResponseBody = None,
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
            temp_model = GetServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetStatefulAsyncInvocationHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_code_checksum: str = None,
        x_fc_date: str = None,
        x_fc_invocation_type: str = None,
        x_fc_log_type: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        # The list of events that trigger the asynchronous task.
        self.x_fc_account_id = x_fc_account_id
        # The structure of the asynchronous task.
        self.x_fc_code_checksum = x_fc_code_checksum
        # Alibaba Cloud provides SDKs for multiple programming languages to help you integrate Alibaba Cloud services by using APIs. We recommend that you use an SDK to call API operations. This frees you from manual signature verification.
        self.x_fc_date = x_fc_date
        # StatefulAsyncInvocation: asynchronous task. Asynchronous tasks allow you to manage the states on the basis of common asynchronous invocations, which is more suitable for task scenarios.
        self.x_fc_invocation_type = x_fc_invocation_type
        # The latest version of Function Compute API.
        self.x_fc_log_type = x_fc_log_type
        # You can search for API operations, call and debug API operations online, and dynamically generate executable sample code for SDKs.
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_code_checksum is not None:
            result['X-Fc-Code-Checksum'] = self.x_fc_code_checksum
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_invocation_type is not None:
            result['X-Fc-Invocation-Type'] = self.x_fc_invocation_type
        if self.x_fc_log_type is not None:
            result['X-Fc-Log-Type'] = self.x_fc_log_type
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Code-Checksum') is not None:
            self.x_fc_code_checksum = m.get('X-Fc-Code-Checksum')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Invocation-Type') is not None:
            self.x_fc_invocation_type = m.get('X-Fc-Invocation-Type')
        if m.get('X-Fc-Log-Type') is not None:
            self.x_fc_log_type = m.get('X-Fc-Log-Type')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class GetStatefulAsyncInvocationRequest(TeaModel):
    def __init__(
        self,
        qualifier: str = None,
    ):
        # The ID of the instance that is used to run the asynchronous task.
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


class GetStatefulAsyncInvocationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StatefulAsyncInvocation = None,
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
            temp_model = StatefulAsyncInvocation()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTriggerHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id
        # The time when the request is initiated on the client. The format of the value is: **EEE,d MMM yyyy HH:mm:ss GMT**.
        self.x_fc_date = x_fc_date
        # The custom request ID.
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class GetTriggerResponseBody(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        description: str = None,
        domain_name: str = None,
        invocation_role: str = None,
        last_modified_time: str = None,
        qualifier: str = None,
        source_arn: str = None,
        trigger_config: str = None,
        trigger_id: str = None,
        trigger_name: str = None,
        trigger_type: str = None,
        url_internet: str = None,
        url_intranet: str = None,
    ):
        # The time when the trigger was created.
        self.created_time = created_time
        # The description of the trigger.
        self.description = description
        # The domain name used to invoke the function by using HTTP. You can add this domain name as the prefix to the endpoint of Function Compute. This way, you can invoke the function that corresponds to the trigger by using HTTP. For example, `{domainName}.cn-shanghai.fc.aliyuncs.com`.
        self.domain_name = domain_name
        # The ARN of the RAM role that is used by the event source to invoke the function.
        self.invocation_role = invocation_role
        # The time when the trigger was last modified.
        self.last_modified_time = last_modified_time
        # The version or alias of the service.
        self.qualifier = qualifier
        # The ARN of the event source.
        self.source_arn = source_arn
        # The configurations of the trigger. The configurations vary based on the trigger type. For more information about the format, see the following topics:
        # 
        # *   Object Storage Service (OSS) trigger: [OSSTriggerConfig](~~415697~~).
        # *   Simple Log Service trigger: [LogTriggerConfig](~~415694~~).
        # *   Time trigger: [TimeTriggerConfig](~~415712~~).
        # *   HTTP trigger: [HTTPTriggerConfig](~~415685~~).
        # *   Tablestore trigger: Specify the **SourceArn** parameter and leave this parameter empty.
        # *   Alibaba Cloud CDN event trigger: [CDNEventsTriggerConfig](~~415674~~).
        # *   Message Service (MNS) topic trigger: [MnsTopicTriggerConfig](~~415695~~).
        # *   EventBridge triggers: [EventBridgeTriggerConfig](~~2508622~~).
        self.trigger_config = trigger_config
        # The unique ID of the trigger.
        self.trigger_id = trigger_id
        # The name of the trigger.
        self.trigger_name = trigger_name
        # The trigger type. Example values: **oss**, **log**, **tablestore**, **timer**, **http**, **cdn_events**, **mns_topic**, and **eventbridge**.
        self.trigger_type = trigger_type
        # The public domain address. You can access HTTP triggers over the Internet by using HTTP or HTTPS.
        self.url_internet = url_internet
        # The private endpoint. In a VPC, you can access HTTP triggers by using HTTP or HTTPS.
        self.url_intranet = url_intranet

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
        if self.domain_name is not None:
            result['domainName'] = self.domain_name
        if self.invocation_role is not None:
            result['invocationRole'] = self.invocation_role
        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        if self.source_arn is not None:
            result['sourceArn'] = self.source_arn
        if self.trigger_config is not None:
            result['triggerConfig'] = self.trigger_config
        if self.trigger_id is not None:
            result['triggerId'] = self.trigger_id
        if self.trigger_name is not None:
            result['triggerName'] = self.trigger_name
        if self.trigger_type is not None:
            result['triggerType'] = self.trigger_type
        if self.url_internet is not None:
            result['urlInternet'] = self.url_internet
        if self.url_intranet is not None:
            result['urlIntranet'] = self.url_intranet
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domainName') is not None:
            self.domain_name = m.get('domainName')
        if m.get('invocationRole') is not None:
            self.invocation_role = m.get('invocationRole')
        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        if m.get('sourceArn') is not None:
            self.source_arn = m.get('sourceArn')
        if m.get('triggerConfig') is not None:
            self.trigger_config = m.get('triggerConfig')
        if m.get('triggerId') is not None:
            self.trigger_id = m.get('triggerId')
        if m.get('triggerName') is not None:
            self.trigger_name = m.get('triggerName')
        if m.get('triggerType') is not None:
            self.trigger_type = m.get('triggerType')
        if m.get('urlInternet') is not None:
            self.url_internet = m.get('urlInternet')
        if m.get('urlIntranet') is not None:
            self.url_intranet = m.get('urlIntranet')
        return self


class GetTriggerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTriggerResponseBody = None,
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
            temp_model = GetTriggerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InvokeFunctionHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_invocation_type: str = None,
        x_fc_log_type: str = None,
        x_fc_stateful_async_invocation_enable: str = None,
        x_fc_stateful_async_invocation_id: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id
        # The time when the function is invoked. The format is **EEE,d MMM yyyy HH:mm:ss GMT**.
        self.x_fc_date = x_fc_date
        # The invocation method. Valid values:
        # 
        # *   **Sync**: synchronous invocations
        # *   **Async**: asynchronous invocations
        # 
        # Default value: Sync
        self.x_fc_invocation_type = x_fc_invocation_type
        # The method used to return logs. Valid values:
        # 
        # *   **Tail**: returns the last 4 KB of logs that are generated for the current request.
        # *   **None**: No logs are returned for the current request. Default value: None.
        self.x_fc_log_type = x_fc_log_type
        # Specifies whether to enable the asynchronous task mode for requests. Default value: false. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        # 
        # > 
        # 
        # *   This parameter takes effect only for asynchronous invocations. It does not take effect for synchronous invocations.
        self.x_fc_stateful_async_invocation_enable = x_fc_stateful_async_invocation_enable
        # The ID of the asynchronous task. You must enable the asynchronous task feature in advance.
        # 
        # > When you use an SDK to invoke a function, we recommend that you specify a business-related ID to facilitate subsequent operations. For example, you can use the video name as the invocation ID for a video-processing function. This way, you can use the ID to check whether the video is processed or terminate the processing of the video. The ID must start with a letter or an underscore (\_) and can contain letters, digits, underscores (\_), and hyphens (-). The ID can be up to 128 characters in length. If you do not specify the ID of the asynchronous invocation, Function Compute automatically generates an ID.
        self.x_fc_stateful_async_invocation_id = x_fc_stateful_async_invocation_id
        # The trace ID of the request for Function Compute API. The value is the same as that of the **requestId** parameter in the response.
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_invocation_type is not None:
            result['X-Fc-Invocation-Type'] = self.x_fc_invocation_type
        if self.x_fc_log_type is not None:
            result['X-Fc-Log-Type'] = self.x_fc_log_type
        if self.x_fc_stateful_async_invocation_enable is not None:
            result['X-Fc-Stateful-Async-Invocation-Enable'] = self.x_fc_stateful_async_invocation_enable
        if self.x_fc_stateful_async_invocation_id is not None:
            result['X-Fc-Stateful-Async-Invocation-Id'] = self.x_fc_stateful_async_invocation_id
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Invocation-Type') is not None:
            self.x_fc_invocation_type = m.get('X-Fc-Invocation-Type')
        if m.get('X-Fc-Log-Type') is not None:
            self.x_fc_log_type = m.get('X-Fc-Log-Type')
        if m.get('X-Fc-Stateful-Async-Invocation-Enable') is not None:
            self.x_fc_stateful_async_invocation_enable = m.get('X-Fc-Stateful-Async-Invocation-Enable')
        if m.get('X-Fc-Stateful-Async-Invocation-Id') is not None:
            self.x_fc_stateful_async_invocation_id = m.get('X-Fc-Stateful-Async-Invocation-Id')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class InvokeFunctionRequest(TeaModel):
    def __init__(
        self,
        body: bytes = None,
        qualifier: str = None,
    ):
        # The event to be processed by the function. Set this parameter to a binary string. Function Compute passes the event to the function for processing.
        self.body = body
        # The version or alias of the service.
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
        body: bytes = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')

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


class ListAliasesHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id
        # The time on which the function is invoked. The format of the value is: **EEE,d MMM yyyy HH:mm:ss GMT**.
        self.x_fc_date = x_fc_date
        # The trace ID of the invocation request of Function Compute.
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class ListAliasesRequest(TeaModel):
    def __init__(
        self,
        limit: int = None,
        next_token: str = None,
        prefix: str = None,
        start_key: str = None,
    ):
        # The maximum number of resources to return. Default value: 20. Maximum value: 100. The number of returned resources is less than or equal to the specified number.
        self.limit = limit
        # The token required to obtain more results. If the number of resources exceeds the limit, the nextToken parameter is returned. You can include the parameter in subsequent calls to obtain more results. You do not need to provide this parameter in the first call.
        self.next_token = next_token
        # The prefix that the names of returned resources must contain.
        self.prefix = prefix
        # The starting position of the result list. The returned resources are sorted in alphabetical order, and the resources that include and follow the resource specified by the startKey parameter are returned.
        self.start_key = start_key

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
        if self.start_key is not None:
            result['startKey'] = self.start_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('prefix') is not None:
            self.prefix = m.get('prefix')
        if m.get('startKey') is not None:
            self.start_key = m.get('startKey')
        return self


class ListAliasesResponseBodyAliases(TeaModel):
    def __init__(
        self,
        additional_version_weight: Dict[str, float] = None,
        alias_name: str = None,
        created_time: str = None,
        description: str = None,
        last_modified_time: str = None,
        resolve_policy: str = None,
        route_policy: RoutePolicy = None,
        version_id: str = None,
    ):
        # The additional version to which the alias points and the weight of the additional version.
        # 
        # *   The additional version takes effect only when the function is invoked.
        # *   The value consists of a version number and a specific weight. For example, 2:0.05 indicates that when a function is invoked, Version 2 is the canary release version, 5% of the traffic is distributed to the canary release version, and 95% of the traffic is distributed to the major version.
        self.additional_version_weight = additional_version_weight
        # The name of the alias.
        self.alias_name = alias_name
        # The time when the ConfigMaps were created.
        self.created_time = created_time
        # The description of the alias.
        self.description = description
        # The time at which the system parameter was last modified.
        self.last_modified_time = last_modified_time
        # The canary release mode. Valid values:
        # 
        # *   **Random**: random canary release. This is the default value.
        # *   **Content**: rule-based canary release.
        self.resolve_policy = resolve_policy
        # The canary release rule. Traffic that meets the canary release rule is routed to the canary release instance.
        self.route_policy = route_policy
        # The ID of the version.
        self.version_id = version_id

    def validate(self):
        if self.route_policy:
            self.route_policy.validate()

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
        if self.resolve_policy is not None:
            result['resolvePolicy'] = self.resolve_policy
        if self.route_policy is not None:
            result['routePolicy'] = self.route_policy.to_map()
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
        if m.get('resolvePolicy') is not None:
            self.resolve_policy = m.get('resolvePolicy')
        if m.get('routePolicy') is not None:
            temp_model = RoutePolicy()
            self.route_policy = temp_model.from_map(m['routePolicy'])
        if m.get('versionId') is not None:
            self.version_id = m.get('versionId')
        return self


class ListAliasesResponseBody(TeaModel):
    def __init__(
        self,
        aliases: List[ListAliasesResponseBodyAliases] = None,
        next_token: str = None,
    ):
        # The list of aliases.
        self.aliases = aliases
        # The token used to obtain more results.
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
                temp_model = ListAliasesResponseBodyAliases()
                self.aliases.append(temp_model.from_map(k))
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        return self


class ListAliasesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAliasesResponseBody = None,
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
            temp_model = ListAliasesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCustomDomainsHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id
        # The time when the operation is called. The format is: **EEE,d MMM yyyy HH:mm:ss GMT**.
        self.x_fc_date = x_fc_date
        # The custom request ID.
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class ListCustomDomainsRequest(TeaModel):
    def __init__(
        self,
        limit: int = None,
        next_token: str = None,
        prefix: str = None,
        start_key: str = None,
    ):
        # The maximum number of resources to return. Valid values: \[0,100]. Default value: 20. The number of returned results is less than or equal to the specified number.
        self.limit = limit
        # The pagination token to use to request the next page of results. If the number of resources exceeds the limit, the nextToken parameter is returned. You can include the parameter in subsequent calls to obtain more results. You do not need to provide this parameter in the first call.
        self.next_token = next_token
        # The prefix that the returned domain names must contain.
        self.prefix = prefix
        # The returned resources are sorted in alphabetical order, and the resources that include and follow the resource specified by the startKey parameter are returned.
        self.start_key = start_key

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
        if self.start_key is not None:
            result['startKey'] = self.start_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('prefix') is not None:
            self.prefix = m.get('prefix')
        if m.get('startKey') is not None:
            self.start_key = m.get('startKey')
        return self


class ListCustomDomainsResponseBodyCustomDomains(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        api_version: str = None,
        cert_config: CertConfig = None,
        created_time: str = None,
        domain_name: str = None,
        last_modified_time: str = None,
        protocol: str = None,
        route_config: RouteConfig = None,
        tls_config: TLSConfig = None,
        waf_config: WAFConfig = None,
    ):
        # The ID of your Alibaba Cloud account.
        self.account_id = account_id
        # The version of the API.
        self.api_version = api_version
        # The configurations of the HTTPS certificate.
        self.cert_config = cert_config
        # The time when the custom domain name was created.
        self.created_time = created_time
        # The domain name.
        self.domain_name = domain_name
        # The time when the domain name was last modified.
        self.last_modified_time = last_modified_time
        # The protocol type that is supported by the custom domain name.
        # 
        # *   **HTTP**: Only HTTP is supported.
        # *   **HTTPS**: Only HTTPS is supported.
        # *   **HTTP,HTTPS**: HTTP and HTTPS are supported.
        self.protocol = protocol
        # The route table that maps the paths to functions when the functions are invoked by using the custom domain name.
        self.route_config = route_config
        # The Transport Layer Security (TLS) configuration.
        self.tls_config = tls_config
        # The Web Application Firewall (WAF) configuration.
        self.waf_config = waf_config

    def validate(self):
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
        if m.get('tlsConfig') is not None:
            temp_model = TLSConfig()
            self.tls_config = temp_model.from_map(m['tlsConfig'])
        if m.get('wafConfig') is not None:
            temp_model = WAFConfig()
            self.waf_config = temp_model.from_map(m['wafConfig'])
        return self


class ListCustomDomainsResponseBody(TeaModel):
    def __init__(
        self,
        custom_domains: List[ListCustomDomainsResponseBodyCustomDomains] = None,
        next_token: str = None,
    ):
        # The information about custom domain names.
        self.custom_domains = custom_domains
        # The pagination token to use to request the next page of results. If the number of resources exceeds the limit, the nextToken parameter is returned. You can include the parameter in subsequent calls to obtain more results. You do not need to provide this parameter in the first call.
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
                temp_model = ListCustomDomainsResponseBodyCustomDomains()
                self.custom_domains.append(temp_model.from_map(k))
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        return self


class ListCustomDomainsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListCustomDomainsResponseBody = None,
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
            temp_model = ListCustomDomainsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEventSourcesHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id
        # The time when Function Compute API is called. Specify the time in the **EEE,d MMM yyyy HH:mm:ss GMT** format.
        self.x_fc_date = x_fc_date
        # The trace ID of the invocation request of Function Compute.
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class ListEventSourcesRequest(TeaModel):
    def __init__(
        self,
        qualifier: str = None,
    ):
        # The version or alias of the service.
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


class ListEventSourcesResponseBodyEventSources(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        source_arn: str = None,
    ):
        # The time when the event source was created.
        self.created_time = created_time
        # The ARN of the event source.
        self.source_arn = source_arn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.source_arn is not None:
            result['sourceArn'] = self.source_arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('sourceArn') is not None:
            self.source_arn = m.get('sourceArn')
        return self


class ListEventSourcesResponseBody(TeaModel):
    def __init__(
        self,
        event_sources: List[ListEventSourcesResponseBodyEventSources] = None,
    ):
        # The information about event sources.
        self.event_sources = event_sources

    def validate(self):
        if self.event_sources:
            for k in self.event_sources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['eventSources'] = []
        if self.event_sources is not None:
            for k in self.event_sources:
                result['eventSources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.event_sources = []
        if m.get('eventSources') is not None:
            for k in m.get('eventSources'):
                temp_model = ListEventSourcesResponseBodyEventSources()
                self.event_sources.append(temp_model.from_map(k))
        return self


class ListEventSourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListEventSourcesResponseBody = None,
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
            temp_model = ListEventSourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFunctionAsyncInvokeConfigsHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_code_checksum: str = None,
        x_fc_date: str = None,
        x_fc_invocation_type: str = None,
        x_fc_log_type: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id
        # The CRC-64 value of the function code package. This value is used to check data integrity. The value is automatically calculated by the tool.
        self.x_fc_code_checksum = x_fc_code_checksum
        # The time when the Function Compute is called. The format is **EEE,d MMM yyyy HH:mm:ss GMT**.
        self.x_fc_date = x_fc_date
        # The invocation method.
        # 
        # *   **Sync**: synchronous
        # *   **Async**: asynchronous
        self.x_fc_invocation_type = x_fc_invocation_type
        # The method used to return logs. Valid values:
        # 
        # *   **Tail**: returns the last 4 KB of logs that are generated for the current request.
        # *   **None**: No logs are returned for the current request. Default value: None.
        self.x_fc_log_type = x_fc_log_type
        # The trace ID of the invocation request of Function Compute.
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_code_checksum is not None:
            result['X-Fc-Code-Checksum'] = self.x_fc_code_checksum
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_invocation_type is not None:
            result['X-Fc-Invocation-Type'] = self.x_fc_invocation_type
        if self.x_fc_log_type is not None:
            result['X-Fc-Log-Type'] = self.x_fc_log_type
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Code-Checksum') is not None:
            self.x_fc_code_checksum = m.get('X-Fc-Code-Checksum')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Invocation-Type') is not None:
            self.x_fc_invocation_type = m.get('X-Fc-Invocation-Type')
        if m.get('X-Fc-Log-Type') is not None:
            self.x_fc_log_type = m.get('X-Fc-Log-Type')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class ListFunctionAsyncInvokeConfigsRequest(TeaModel):
    def __init__(
        self,
        limit: int = None,
        next_token: str = None,
    ):
        # The maximum number of resources to return. Default value: 20. The value cannot exceed 100. The number of returned configurations is less than or equal to the specified number.
        self.limit = limit
        # The token required to obtain more results. If the number of resources exceeds the limit, the nextToken parameter is returned. You can include the parameter in subsequent calls to obtain more results. You do not need to provide this parameter in the first call.
        self.next_token = next_token

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        return self


class ListFunctionAsyncInvokeConfigsResponseBodyConfigs(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        destination_config: DestinationConfig = None,
        function: str = None,
        last_modified_time: str = None,
        max_async_event_age_in_seconds: int = None,
        max_async_retry_attempts: int = None,
        qualifier: str = None,
        service: str = None,
        stateful_invocation: bool = None,
    ):
        # The time when the application was created.
        self.created_time = created_time
        # The configuration structure of the destination for the asynchronous invocation. If you have not configured this parameter, this parameter is null.
        self.destination_config = destination_config
        # The function name.
        self.function = function
        # The time when the configuration was last modified.
        self.last_modified_time = last_modified_time
        # The maximum validity period of messages. If you have not configured this parameter, this parameter is null.
        self.max_async_event_age_in_seconds = max_async_event_age_in_seconds
        # The maximum number of retries allowed after an asynchronous invocation fails. If you have not configured this parameter, this parameter is null.
        self.max_async_retry_attempts = max_async_retry_attempts
        # The version or alias of the service.
        self.qualifier = qualifier
        # The name of the service.
        self.service = service
        # Specifies whether to enable the asynchronous task feature.
        # 
        # *   **true**\
        # *   **false**\
        # 
        # If you have not configured this parameter, this parameter is null.
        self.stateful_invocation = stateful_invocation

    def validate(self):
        if self.destination_config:
            self.destination_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.destination_config is not None:
            result['destinationConfig'] = self.destination_config.to_map()
        if self.function is not None:
            result['function'] = self.function
        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time
        if self.max_async_event_age_in_seconds is not None:
            result['maxAsyncEventAgeInSeconds'] = self.max_async_event_age_in_seconds
        if self.max_async_retry_attempts is not None:
            result['maxAsyncRetryAttempts'] = self.max_async_retry_attempts
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        if self.service is not None:
            result['service'] = self.service
        if self.stateful_invocation is not None:
            result['statefulInvocation'] = self.stateful_invocation
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('destinationConfig') is not None:
            temp_model = DestinationConfig()
            self.destination_config = temp_model.from_map(m['destinationConfig'])
        if m.get('function') is not None:
            self.function = m.get('function')
        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')
        if m.get('maxAsyncEventAgeInSeconds') is not None:
            self.max_async_event_age_in_seconds = m.get('maxAsyncEventAgeInSeconds')
        if m.get('maxAsyncRetryAttempts') is not None:
            self.max_async_retry_attempts = m.get('maxAsyncRetryAttempts')
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        if m.get('service') is not None:
            self.service = m.get('service')
        if m.get('statefulInvocation') is not None:
            self.stateful_invocation = m.get('statefulInvocation')
        return self


class ListFunctionAsyncInvokeConfigsResponseBody(TeaModel):
    def __init__(
        self,
        configs: List[ListFunctionAsyncInvokeConfigsResponseBodyConfigs] = None,
        next_token: str = None,
    ):
        # The list of asynchronous invocation configurations.
        self.configs = configs
        # The token used to obtain more results.
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
                temp_model = ListFunctionAsyncInvokeConfigsResponseBodyConfigs()
                self.configs.append(temp_model.from_map(k))
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        return self


class ListFunctionAsyncInvokeConfigsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListFunctionAsyncInvokeConfigsResponseBody = None,
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
            temp_model = ListFunctionAsyncInvokeConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFunctionsHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id
        # The time when the function is invoked. The format is **EEE,d MMM yyyy HH:mm:ss GMT**.
        self.x_fc_date = x_fc_date
        # The custom request ID.
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class ListFunctionsRequest(TeaModel):
    def __init__(
        self,
        limit: int = None,
        next_token: str = None,
        prefix: str = None,
        qualifier: str = None,
        start_key: str = None,
    ):
        # The maximum number of resources to return. Default value: 20. Maximum value: 100. The number of returned resources is less than or equal to the specified number.
        self.limit = limit
        # The token required to obtain more results. If the number of resources exceeds the limit, the nextToken parameter is returned. You can include the parameter in subsequent calls to obtain more results. You do not need to provide this parameter in the first call.
        self.next_token = next_token
        # The prefix that the names of returned resources must contain.
        self.prefix = prefix
        # The version or alias of the service.
        self.qualifier = qualifier
        # The starting position of the result list. The returned resources are sorted in alphabetical order, and the resources that include and follow the resource specified by the startKey parameter are returned.
        self.start_key = start_key

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
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        if self.start_key is not None:
            result['startKey'] = self.start_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('prefix') is not None:
            self.prefix = m.get('prefix')
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        if m.get('startKey') is not None:
            self.start_key = m.get('startKey')
        return self


class ListFunctionsResponseBodyFunctions(TeaModel):
    def __init__(
        self,
        ca_port: int = None,
        code_checksum: str = None,
        code_size: int = None,
        cpu: float = None,
        created_time: str = None,
        custom_container_config: CustomContainerConfig = None,
        custom_dns: CustomDNS = None,
        custom_health_check_config: CustomHealthCheckConfig = None,
        custom_runtime_config: CustomRuntimeConfig = None,
        description: str = None,
        disk_size: int = None,
        environment_variables: Dict[str, str] = None,
        function_id: str = None,
        function_name: str = None,
        gpu_memory_size: int = None,
        handler: str = None,
        initialization_timeout: int = None,
        initializer: str = None,
        instance_concurrency: int = None,
        instance_lifecycle_config: InstanceLifecycleConfig = None,
        instance_soft_concurrency: int = None,
        instance_type: str = None,
        last_modified_time: str = None,
        layers: List[str] = None,
        layers_arn_v2: List[str] = None,
        memory_size: int = None,
        runtime: str = None,
        timeout: int = None,
    ):
        # The port on which the HTTP server listens for the custom runtime or custom container runtime.
        self.ca_port = ca_port
        # The CRC-64 value of the function code package.
        self.code_checksum = code_checksum
        # The size of the function code package that is returned by the system. Unit: bytes.
        self.code_size = code_size
        # The number of vCPUs of the function. The value must be a multiple of 0.05.
        self.cpu = cpu
        # The time when the function was created.
        self.created_time = created_time
        # The configurations of the custom container runtime.
        self.custom_container_config = custom_container_config
        self.custom_dns = custom_dns
        # The custom health check configuration of the function. This parameter is applicable only to custom runtimes and custom containers.
        self.custom_health_check_config = custom_health_check_config
        self.custom_runtime_config = custom_runtime_config
        # The description of the function.
        self.description = description
        # The disk size of the function. Unit: MB. Valid values: 512 and 10240.
        self.disk_size = disk_size
        # The environment variables that you configured for the function. You can obtain the values of the environment variables from the function.
        self.environment_variables = environment_variables
        # The unique ID that is generated by the system for the function.
        self.function_id = function_id
        # The name of the function.
        self.function_name = function_name
        # The GPU memory capacity for the function. Unit: MB. The value is a multiple of 1,024.
        self.gpu_memory_size = gpu_memory_size
        # The handler of the function.
        self.handler = handler
        # The timeout period for the execution of the Initializer hook. Unit: seconds. Default value: 3. Valid values: 1 to 300. When this period ends, the execution of the Initializer hook is terminated.
        self.initialization_timeout = initialization_timeout
        # The handler of the Initializer hook. The format of the value is determined by the programming language that you use. For more information, see [Initializer hook](~~157704~~).
        self.initializer = initializer
        # The number of requests that can be concurrently processed by a single instance.
        self.instance_concurrency = instance_concurrency
        # The lifecycle configurations of the instance.
        self.instance_lifecycle_config = instance_lifecycle_config
        # The soft concurrency of the instance. You can use this parameter to implement graceful scale-up of instances. If the number of concurrent requests on an instance is greater than the value of soft concurrency, an instance scale-up is triggered. For example, if your instance requires a long time to start, you can specify a suitable soft concurrency to start the instance in advance.
        # 
        # The value must be less than or equal to that of the **instanceConcurrency** parameter.
        self.instance_soft_concurrency = instance_soft_concurrency
        # The instance type of the function. Valid values:
        # 
        # *   **e1**: elastic instance
        # *   **c1**: performance instance
        # *   **fc.gpu.tesla.1**: GPU-accelerated instance (Tesla T4)
        # *   **fc.gpu.ampere.1**: GPU-accelerated instance (Ampere A10)
        # *   **g1**: same as fc.gpu.tesla.1
        self.instance_type = instance_type
        # The time when the function was last modified.
        self.last_modified_time = last_modified_time
        # The information about layers.
        # 
        # > Multiple layers are merged based on the order of array subscripts. The content of a layer with a smaller subscript overwrites the file that has the same name as a layer with a larger subscript.
        self.layers = layers
        self.layers_arn_v2 = layers_arn_v2
        # The memory size that is configured for the function. Unit: MB.
        self.memory_size = memory_size
        # The runtime environment of the function. Valid values: **nodejs16**, **nodejs14**, **nodejs12**, **nodejs10**, **nodejs8**, **nodejs6**, **nodejs4.4**, **python3.10**, **python3.9**, **python3**, **python2.7**, **java11**, **java8**, **go1**, **php7.2**, **dotnetcore3.1**, **dotnetcore2.1**, **custom.debian10**, **custom**, and **custom-container**. For more information, see [Supported function runtime environments](~~73338~~).
        self.runtime = runtime
        # The timeout period for the execution of the function. Unit: seconds. Default value: 60. Valid values: 1 to 600. When this period expires, the execution of the function is terminated.
        self.timeout = timeout

    def validate(self):
        if self.custom_container_config:
            self.custom_container_config.validate()
        if self.custom_dns:
            self.custom_dns.validate()
        if self.custom_health_check_config:
            self.custom_health_check_config.validate()
        if self.custom_runtime_config:
            self.custom_runtime_config.validate()
        if self.instance_lifecycle_config:
            self.instance_lifecycle_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ca_port is not None:
            result['caPort'] = self.ca_port
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
        if self.custom_health_check_config is not None:
            result['customHealthCheckConfig'] = self.custom_health_check_config.to_map()
        if self.custom_runtime_config is not None:
            result['customRuntimeConfig'] = self.custom_runtime_config.to_map()
        if self.description is not None:
            result['description'] = self.description
        if self.disk_size is not None:
            result['diskSize'] = self.disk_size
        if self.environment_variables is not None:
            result['environmentVariables'] = self.environment_variables
        if self.function_id is not None:
            result['functionId'] = self.function_id
        if self.function_name is not None:
            result['functionName'] = self.function_name
        if self.gpu_memory_size is not None:
            result['gpuMemorySize'] = self.gpu_memory_size
        if self.handler is not None:
            result['handler'] = self.handler
        if self.initialization_timeout is not None:
            result['initializationTimeout'] = self.initialization_timeout
        if self.initializer is not None:
            result['initializer'] = self.initializer
        if self.instance_concurrency is not None:
            result['instanceConcurrency'] = self.instance_concurrency
        if self.instance_lifecycle_config is not None:
            result['instanceLifecycleConfig'] = self.instance_lifecycle_config.to_map()
        if self.instance_soft_concurrency is not None:
            result['instanceSoftConcurrency'] = self.instance_soft_concurrency
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time
        if self.layers is not None:
            result['layers'] = self.layers
        if self.layers_arn_v2 is not None:
            result['layersArnV2'] = self.layers_arn_v2
        if self.memory_size is not None:
            result['memorySize'] = self.memory_size
        if self.runtime is not None:
            result['runtime'] = self.runtime
        if self.timeout is not None:
            result['timeout'] = self.timeout
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('caPort') is not None:
            self.ca_port = m.get('caPort')
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
        if m.get('customHealthCheckConfig') is not None:
            temp_model = CustomHealthCheckConfig()
            self.custom_health_check_config = temp_model.from_map(m['customHealthCheckConfig'])
        if m.get('customRuntimeConfig') is not None:
            temp_model = CustomRuntimeConfig()
            self.custom_runtime_config = temp_model.from_map(m['customRuntimeConfig'])
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('diskSize') is not None:
            self.disk_size = m.get('diskSize')
        if m.get('environmentVariables') is not None:
            self.environment_variables = m.get('environmentVariables')
        if m.get('functionId') is not None:
            self.function_id = m.get('functionId')
        if m.get('functionName') is not None:
            self.function_name = m.get('functionName')
        if m.get('gpuMemorySize') is not None:
            self.gpu_memory_size = m.get('gpuMemorySize')
        if m.get('handler') is not None:
            self.handler = m.get('handler')
        if m.get('initializationTimeout') is not None:
            self.initialization_timeout = m.get('initializationTimeout')
        if m.get('initializer') is not None:
            self.initializer = m.get('initializer')
        if m.get('instanceConcurrency') is not None:
            self.instance_concurrency = m.get('instanceConcurrency')
        if m.get('instanceLifecycleConfig') is not None:
            temp_model = InstanceLifecycleConfig()
            self.instance_lifecycle_config = temp_model.from_map(m['instanceLifecycleConfig'])
        if m.get('instanceSoftConcurrency') is not None:
            self.instance_soft_concurrency = m.get('instanceSoftConcurrency')
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')
        if m.get('layers') is not None:
            self.layers = m.get('layers')
        if m.get('layersArnV2') is not None:
            self.layers_arn_v2 = m.get('layersArnV2')
        if m.get('memorySize') is not None:
            self.memory_size = m.get('memorySize')
        if m.get('runtime') is not None:
            self.runtime = m.get('runtime')
        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')
        return self


class ListFunctionsResponseBody(TeaModel):
    def __init__(
        self,
        functions: List[ListFunctionsResponseBodyFunctions] = None,
        next_token: str = None,
    ):
        # The information about functions.
        self.functions = functions
        # The token used to obtain more results. If this parameter is not returned, all the layers are returned.
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
                temp_model = ListFunctionsResponseBodyFunctions()
                self.functions.append(temp_model.from_map(k))
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        return self


class ListFunctionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListFunctionsResponseBody = None,
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
            temp_model = ListFunctionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstancesHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
    ):
        self.common_headers = common_headers
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        return self


class ListInstancesRequest(TeaModel):
    def __init__(
        self,
        instance_ids: List[str] = None,
        limit: int = None,
        qualifier: str = None,
    ):
        # The IDs of the instance.
        self.instance_ids = instance_ids
        # The maximum number of resources to return. Valid values: \[0,1000].
        # 
        # The number of returned resources is less than or equal to the specified number.
        self.limit = limit
        # The version or alias.
        self.qualifier = qualifier

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_ids is not None:
            result['instanceIds'] = self.instance_ids
        if self.limit is not None:
            result['limit'] = self.limit
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instanceIds') is not None:
            self.instance_ids = m.get('instanceIds')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        return self


class ListInstancesResponseBodyInstances(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        version_id: str = None,
    ):
        # The ID of the instance.
        self.instance_id = instance_id
        # The version of the service to which the instance belongs. If the instance belongs to the LATEST alias, 0 is returned as the version.
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


class ListInstancesResponseBody(TeaModel):
    def __init__(
        self,
        instances: List[ListInstancesResponseBodyInstances] = None,
    ):
        # The information about instances.
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
                temp_model = ListInstancesResponseBodyInstances()
                self.instances.append(temp_model.from_map(k))
        return self


class ListInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListInstancesResponseBody = None,
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
            temp_model = ListInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListLayerVersionsHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id
        # The time when the operation is called. The format is: **EEE,d MMM yyyy HH:mm:ss GMT**.
        self.x_fc_date = x_fc_date
        # The trace ID of the request for Function Compute API.
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class ListLayerVersionsRequest(TeaModel):
    def __init__(
        self,
        limit: int = None,
        start_version: int = None,
    ):
        # The maximum number of resources to return. Default value: 20. The value cannot exceed 100. The number of returned configurations is less than or equal to the specified number.
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


class ListLayerVersionsResponseBody(TeaModel):
    def __init__(
        self,
        layers: List[Layer] = None,
        next_version: int = None,
    ):
        # The information about layer versions.
        self.layers = layers
        # The initial version of the layer for the next query.
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


class ListLayerVersionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListLayerVersionsResponseBody = None,
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
            temp_model = ListLayerVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListLayersHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id
        # The time when the function is invoked. The format is: **EEE,d MMM yyyy HH:mm:ss GMT**.
        self.x_fc_date = x_fc_date
        # The trace ID of the request for Function Compute API.
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class ListLayersRequest(TeaModel):
    def __init__(
        self,
        limit: int = None,
        next_token: str = None,
        official: bool = None,
        prefix: str = None,
        public: bool = None,
        start_key: str = None,
    ):
        # The maximum number of resources to return. Default value: 20. Maximum value: 100. The number of returned configurations is less than or equal to the specified number.
        self.limit = limit
        # The token required to obtain more results. If the number of resources exceeds the limit, the nextToken parameter is returned. You can include the parameter in subsequent calls to obtain more results. You do not need to provide this parameter in the first call.
        self.next_token = next_token
        # Specifies whether to obtain the official public layer. When the official parameter is set to true, the public field does not take effect. The default value is false.
        self.official = official
        # The name prefix of the layer. The names of returned resources must contain the prefix. If the name prefix is a, the names of returned resources must start with a.
        self.prefix = prefix
        # Specifies whether to obtain only the common layer. Default value: false.
        self.public = public
        # The name of the start layer. The returned layers are sorted in alphabetical order, and the layers that include and follow the layer specified by the startKey parameter are returned.
        self.start_key = start_key

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
        if self.start_key is not None:
            result['startKey'] = self.start_key
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
        if m.get('startKey') is not None:
            self.start_key = m.get('startKey')
        return self


class ListLayersResponseBody(TeaModel):
    def __init__(
        self,
        layers: List[Layer] = None,
        next_token: str = None,
    ):
        # The information about layers.
        self.layers = layers
        # The name of the start layer for the next query, which is also the token used to obtain more results.
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


class ListLayersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListLayersResponseBody = None,
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
            temp_model = ListLayersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOnDemandConfigsHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        # $.parameters[8].schema.description
        self.x_fc_account_id = x_fc_account_id
        # $.parameters[8].schema.example
        self.x_fc_date = x_fc_date
        # $.parameters[8].schema.enumValueTitles
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class ListOnDemandConfigsRequest(TeaModel):
    def __init__(
        self,
        limit: int = None,
        next_token: str = None,
        prefix: str = None,
        start_key: str = None,
    ):
        # The time when Function Compute API is called.
        self.limit = limit
        # The ID of your Alibaba Cloud account.
        self.next_token = next_token
        # The returned data.
        self.prefix = prefix
        # The maximum number of resources to return. Default value: 20. Maximum value: 100. The number of returned resources is less than or equal to the specified number.
        self.start_key = start_key

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
        if self.start_key is not None:
            result['startKey'] = self.start_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('prefix') is not None:
            self.prefix = m.get('prefix')
        if m.get('startKey') is not None:
            self.start_key = m.get('startKey')
        return self


class ListOnDemandConfigsResponseBody(TeaModel):
    def __init__(
        self,
        configs: List[OnDemandConfig] = None,
        next_token: str = None,
    ):
        # $.parameters[9].schema.enumValueTitles
        self.configs = configs
        # {"name":"ListOnDemandConfigs","product":"FC-Open","version":"2021-04-06","path":"/2021-04-06/on-demand-configs","deprecated":0,"method":"GET","protocol":"HTTP|HTTPS","hidden":0,"timeout":10000,"parameter_type":"Single","params":"[{\"name\":\"prefix\",\"position\":\"Query\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"The prefix that the names of returned resources must contain. If the name prefix is a, the names of returned resources must start with a. \",\"description\":\"The prefix that the names of returned resources must contain. If the name prefix is a, the names of returned resources must start with a. \",\"example\":\"prefix_text\"},{\"name\":\"startKey\",\"position\":\"Query\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"The returned resources are sorted in alphabetical order, and the resources that include and follow the resource specified by the startKey parameter are returned. \",\"description\":\"The returned resources are sorted in alphabetical order, and the resources that include and follow the resource specified by the startKey parameter are returned. \",\"example\":\"nextservice\"},{\"name\":\"nextToken\",\"position\":\"Query\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"The token used to obtain more results. If the number of resources exceeds the limit, the nextToken parameter is returned. You can include the parameter in subsequent calls to obtain more results. You do not need to provide this parameter in the first call. \",\"description\":\"The token used to obtain more results. If the number of resources exceeds the limit, the nextToken parameter is returned. You can include the parameter in subsequent calls to obtain more results. You do not need to provide this parameter in the first call. \",\"example\":\"8bj81uI8n****\"},{\"name\":\"limit\",\"position\":\"Query\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Integer\",\"title\":\"The maximum number of resources to return. Default value: 20. Maximum value: 100. The number of returned resources is less than or equal to the specified number. \",\"description\":\"The maximum number of resources to return. Default value: 20. Maximum value: 100. The number of returned resources is less than or equal to the specified number. \",\"example\":\"20\"},{\"name\":\"X-Fc-Account-Id\",\"position\":\"Header\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"description\":\"The ID of your Alibaba Cloud account. \",\"example\":\"188077086902****\"},{\"name\":\"X-Fc-Date\",\"position\":\"Header\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"description\":\"The time when Function Compute API is called. \",\"example\":\"2020-12-1210:00:00\"},{\"name\":\"X-Fc-Trace-Id\",\"position\":\"Header\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"description\":\"The trace ID of the invocation request of Function Compute. \",\"example\":\"rid281s******\"}]","response_headers":"[]","response":"{\"type\":\"Object\",\"children\":[{\"name\":\"configs\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Array\",\"subType\":\"Object\",\"example\":\"[{\"maximumInstanceCount\": 10, \"resource\": \"services/serviceName-bb7f36eb-7f1b-4c42-8f64-401b32ecbf31.aliasName/functions/functionName\"}]\",\"description\":\"The information about the on-demand configuration. \",\"children\":[{\"name\":\"resource\",\"required\":false,\"checkBlank\":false,\"visibility\":\"public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"The details of the function.\",\"description\":\"The description of the resource. \",\"example\":\"123#serviceName#alias#functionName\"},{\"name\":\"maximumInstanceCount\",\"required\":false,\"checkBlank\":false,\"visibility\":\"public\",\"deprecated\":false,\"type\":\"Long\",\"title\":\"todo\",\"description\":\"The maximum number of on-demand instances. \",\"example\":\"10\"}],\"title\":\"The information about the provisioned configuration.\"},{\"name\":\"nextToken\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"The token used to obtain more results. If this parameter is left empty, all the results are returned. \",\"description\":\"The token used to obtain more results. If this parameter is left empty, all the results are returned. \",\"example\":\"next_token\"}],\"title\":\"Schema of Response\",\"description\":\"The returned data. \"}","errors":"{}"}
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
                temp_model = OnDemandConfig()
                self.configs.append(temp_model.from_map(k))
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        return self


class ListOnDemandConfigsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListOnDemandConfigsResponseBody = None,
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
            temp_model = ListOnDemandConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProvisionConfigsHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id
        # The time when Function Compute API is called. Specify the time in the **EEE,d MMM yyyy HH:mm:ss GMT** format.
        self.x_fc_date = x_fc_date
        # The trace ID of the invocation request of Function Compute.
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class ListProvisionConfigsRequest(TeaModel):
    def __init__(
        self,
        limit: int = None,
        next_token: str = None,
        qualifier: str = None,
        service_name: str = None,
    ):
        # The maximum number of resources to return. Default value: 20. Maximum value: 100. The number of returned resources is less than or equal to the specified number.
        self.limit = limit
        # The token used to obtain more results. You do not need to provide this parameter in the first call. The tokens for subsequent queries are obtained from the returned results.
        self.next_token = next_token
        # The qualifier of the service to which resources belong. The qualifier must be aliasName and used together with the serviceName parameter.
        self.qualifier = qualifier
        # The name of the service to which resources belong.
        self.service_name = service_name

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
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        return self


class ListProvisionConfigsResponseBodyProvisionConfigs(TeaModel):
    def __init__(
        self,
        always_allocate_cpu: bool = None,
        current: int = None,
        current_error: str = None,
        resource: str = None,
        scheduled_actions: List[ScheduledActions] = None,
        target: int = None,
        target_tracking_policies: List[TargetTrackingPolicies] = None,
    ):
        # Specifies whether to always allocate CPU to a function instance.
        self.always_allocate_cpu = always_allocate_cpu
        # The actual number of provisioned instances.
        self.current = current
        # The error message returned if a provisioned instance fails to be created.
        self.current_error = current_error
        # The description of the resource.
        self.resource = resource
        # The configurations of scheduled auto scaling.
        self.scheduled_actions = scheduled_actions
        # The expected number of provisioned instances.
        self.target = target
        # The configurations of metric-based auto scaling.
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
        if self.resource is not None:
            result['resource'] = self.resource
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
        if m.get('resource') is not None:
            self.resource = m.get('resource')
        self.scheduled_actions = []
        if m.get('scheduledActions') is not None:
            for k in m.get('scheduledActions'):
                temp_model = ScheduledActions()
                self.scheduled_actions.append(temp_model.from_map(k))
        if m.get('target') is not None:
            self.target = m.get('target')
        self.target_tracking_policies = []
        if m.get('targetTrackingPolicies') is not None:
            for k in m.get('targetTrackingPolicies'):
                temp_model = TargetTrackingPolicies()
                self.target_tracking_policies.append(temp_model.from_map(k))
        return self


class ListProvisionConfigsResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        provision_configs: List[ListProvisionConfigsResponseBodyProvisionConfigs] = None,
    ):
        # The token used to obtain more results.
        self.next_token = next_token
        # The information about provisioned instances.
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
                temp_model = ListProvisionConfigsResponseBodyProvisionConfigs()
                self.provision_configs.append(temp_model.from_map(k))
        return self


class ListProvisionConfigsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListProvisionConfigsResponseBody = None,
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
            temp_model = ListProvisionConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListReservedCapacitiesHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id
        # The time when the Function Compute API is called. The format is **EEE,d MMM yyyy HH:mm:ss GMT**.
        self.x_fc_date = x_fc_date
        # The custom request ID.
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class ListReservedCapacitiesRequest(TeaModel):
    def __init__(
        self,
        limit: str = None,
        next_token: str = None,
    ):
        # The maximum number of resources to return. Valid values: 1 to 100.
        self.limit = limit
        # The token that determines the start point of the query.
        self.next_token = next_token

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        return self


class ListReservedCapacitiesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        reserved_capacities: List[OpenReservedCapacity] = None,
    ):
        # The token used to obtain more results.
        self.next_token = next_token
        # The information about subscription instances.
        self.reserved_capacities = reserved_capacities

    def validate(self):
        if self.reserved_capacities:
            for k in self.reserved_capacities:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        result['reservedCapacities'] = []
        if self.reserved_capacities is not None:
            for k in self.reserved_capacities:
                result['reservedCapacities'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        self.reserved_capacities = []
        if m.get('reservedCapacities') is not None:
            for k in m.get('reservedCapacities'):
                temp_model = OpenReservedCapacity()
                self.reserved_capacities.append(temp_model.from_map(k))
        return self


class ListReservedCapacitiesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListReservedCapacitiesResponseBody = None,
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
            temp_model = ListReservedCapacitiesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListServiceVersionsHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id
        # The time when Function Compute API is called. Specify the time in the **EEE,d MMM yyyy HH:mm:ss GMT** format.
        self.x_fc_date = x_fc_date
        # The trace ID of the invocation request of Function Compute.
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class ListServiceVersionsRequest(TeaModel):
    def __init__(
        self,
        direction: str = None,
        limit: int = None,
        next_token: str = None,
        start_key: str = None,
    ):
        # The order in which the returned versions are sorted. Valid values:
        #   - **FORWARD**: in ascending order. 
        #   - **BACKWARD**: in descending order. This is the default value.
        self.direction = direction
        # The maximum number of resources to return. Default value: 20. Maximum value: 100. The number of returned resources is less than or equal to the specified number.
        self.limit = limit
        # The token used to obtain more results. If the number of resources exceeds the limit, the nextToken parameter is returned. You can include the parameter in subsequent calls to obtain more results. You do not need to provide this parameter in the first call.
        self.next_token = next_token
        # The starting position of the result list. The returned resources are sorted based on the version number, and the resources that include and follow the resource specified by the startKey parameter are returned.
        self.start_key = start_key

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
        if self.start_key is not None:
            result['startKey'] = self.start_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('direction') is not None:
            self.direction = m.get('direction')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('startKey') is not None:
            self.start_key = m.get('startKey')
        return self


class ListServiceVersionsResponseBodyVersions(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        description: str = None,
        last_modified_time: str = None,
        version_id: str = None,
    ):
        # The time when the service version was created.
        self.created_time = created_time
        # The description of the service version.
        self.description = description
        # The time when the service version was last modified.
        self.last_modified_time = last_modified_time
        # The version of the service.
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


class ListServiceVersionsResponseBody(TeaModel):
    def __init__(
        self,
        direction: str = None,
        next_token: str = None,
        versions: List[ListServiceVersionsResponseBodyVersions] = None,
    ):
        # The order in which the returned versions are sorted. Valid values:
        #   - **FORWARD**: in ascending order. 
        #   - **BACKWARD**: in descending order. This is the default value.
        self.direction = direction
        # The token used to obtain more results. If the number of resources exceeds the limit, the nextToken parameter is returned. You can include the parameter in subsequent calls to obtain more results. You do not need to provide this parameter in the first call.
        self.next_token = next_token
        # The list of versions.
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
                temp_model = ListServiceVersionsResponseBodyVersions()
                self.versions.append(temp_model.from_map(k))
        return self


class ListServiceVersionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListServiceVersionsResponseBody = None,
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
            temp_model = ListServiceVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListServicesHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id
        # The time on which the function is invoked. The format of the value is: **EEE,d MMM yyyy HH:mm:ss GMT**.
        self.x_fc_date = x_fc_date
        # The custom request ID.
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class ListServicesRequest(TeaModel):
    def __init__(
        self,
        limit: int = None,
        next_token: str = None,
        prefix: str = None,
        start_key: str = None,
    ):
        # The maximum number of resources to return. Default value: 20. The value cannot exceed 100. The number of returned configurations is less than or equal to the specified number.
        self.limit = limit
        # The starting position of the query. If this parameter is left empty, the query starts from the beginning. You do not need to specify this parameter in the first query. If the number of asynchronous tasks exceeds the limit, the nextToken parameter is returned, the value of which can be used in subsequent calls to obtain more results.
        self.next_token = next_token
        # The prefix that the names of returned resources must contain. If the name prefix is a, the names of returned resources must start with a.
        self.prefix = prefix
        # The returned resources are sorted in alphabetical order, and the resources that include and follow the resource specified by the startKey parameter are returned.
        self.start_key = start_key

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
        if self.start_key is not None:
            result['startKey'] = self.start_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('prefix') is not None:
            self.prefix = m.get('prefix')
        if m.get('startKey') is not None:
            self.start_key = m.get('startKey')
        return self


class ListServicesResponseBodyServices(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        description: str = None,
        internet_access: bool = None,
        last_modified_time: str = None,
        log_config: LogConfig = None,
        nas_config: NASConfig = None,
        oss_mount_config: OSSMountConfig = None,
        role: str = None,
        service_id: str = None,
        service_name: str = None,
        tracing_config: TracingConfig = None,
        use_slrauthentication: bool = None,
        vpc_config: VPCConfig = None,
    ):
        # The time when the service was created.
        self.created_time = created_time
        # The description of the service.
        self.description = description
        # Specifies whether to allow functions to access the Internet. Valid values:
        # 
        # *   **true**: allows functions in the specified service to access the Internet.
        # *   **false**: does not allow functions to access the Internet.
        self.internet_access = internet_access
        # The time when the service was last modified.
        self.last_modified_time = last_modified_time
        # The log configuration, which specifies a Logstore to store function execution logs.
        self.log_config = log_config
        # The configurations of the NAS file system. The configuration allows functions in the specified service in Function Compute to access the NAS file system.
        self.nas_config = nas_config
        # The OSS mount configurations.
        self.oss_mount_config = oss_mount_config
        # The RAM role that is used to grant required permissions to Function Compute. The RAM role is used in the following scenarios:
        # 
        # *   Sends function execution logs to your Logstore.
        # *   Generates a token for a function to access other cloud resources during function execution.
        self.role = role
        # The unique ID generated by the system for the service.
        self.service_id = service_id
        # The name of the service.
        self.service_name = service_name
        # The configuration of Tracing Analysis. After you configure Tracing Analysis for a service in Function Compute, you can record the execution duration of a request, view the amount of cold start time for a function, and record the execution duration of a function. For more information, see [Overview](~~189804~~).
        self.tracing_config = tracing_config
        self.use_slrauthentication = use_slrauthentication
        # The VPC configuration. The configuration allows a function to access the specified VPC.
        self.vpc_config = vpc_config

    def validate(self):
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
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.description is not None:
            result['description'] = self.description
        if self.internet_access is not None:
            result['internetAccess'] = self.internet_access
        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time
        if self.log_config is not None:
            result['logConfig'] = self.log_config.to_map()
        if self.nas_config is not None:
            result['nasConfig'] = self.nas_config.to_map()
        if self.oss_mount_config is not None:
            result['ossMountConfig'] = self.oss_mount_config.to_map()
        if self.role is not None:
            result['role'] = self.role
        if self.service_id is not None:
            result['serviceId'] = self.service_id
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        if self.tracing_config is not None:
            result['tracingConfig'] = self.tracing_config.to_map()
        if self.use_slrauthentication is not None:
            result['useSLRAuthentication'] = self.use_slrauthentication
        if self.vpc_config is not None:
            result['vpcConfig'] = self.vpc_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('internetAccess') is not None:
            self.internet_access = m.get('internetAccess')
        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')
        if m.get('logConfig') is not None:
            temp_model = LogConfig()
            self.log_config = temp_model.from_map(m['logConfig'])
        if m.get('nasConfig') is not None:
            temp_model = NASConfig()
            self.nas_config = temp_model.from_map(m['nasConfig'])
        if m.get('ossMountConfig') is not None:
            temp_model = OSSMountConfig()
            self.oss_mount_config = temp_model.from_map(m['ossMountConfig'])
        if m.get('role') is not None:
            self.role = m.get('role')
        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        if m.get('tracingConfig') is not None:
            temp_model = TracingConfig()
            self.tracing_config = temp_model.from_map(m['tracingConfig'])
        if m.get('useSLRAuthentication') is not None:
            self.use_slrauthentication = m.get('useSLRAuthentication')
        if m.get('vpcConfig') is not None:
            temp_model = VPCConfig()
            self.vpc_config = temp_model.from_map(m['vpcConfig'])
        return self


class ListServicesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        services: List[ListServicesResponseBodyServices] = None,
    ):
        # The token used to obtain more results. If this parameter is left empty, all the results are returned.
        self.next_token = next_token
        # The information about a service.
        self.services = services

    def validate(self):
        if self.services:
            for k in self.services:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        result['services'] = []
        if self.services is not None:
            for k in self.services:
                result['services'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        self.services = []
        if m.get('services') is not None:
            for k in m.get('services'):
                temp_model = ListServicesResponseBodyServices()
                self.services.append(temp_model.from_map(k))
        return self


class ListServicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListServicesResponseBody = None,
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
            temp_model = ListServicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListStatefulAsyncInvocationFunctionsHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        # It is a tool used to manage and configure Alibaba Cloud resources. After simple installation and configuration, you can use Alibaba Cloud CLI to manage multiple Alibaba Cloud services and migrate your data and business to the cloud with ease.
        self.x_fc_account_id = x_fc_account_id
        # The token used to obtain more results. If this parameter is left empty, all the results are returned.
        self.x_fc_date = x_fc_date
        # The details of returned data.
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class ListStatefulAsyncInvocationFunctionsRequest(TeaModel):
    def __init__(
        self,
        limit: int = None,
        next_token: str = None,
    ):
        # The latest version of Function Compute API.
        self.limit = limit
        # Alibaba Cloud provides SDKs for multiple programming languages to help you integrate Alibaba Cloud services by using APIs. We recommend that you use an SDK to call API operations. This frees you from manual signature verification.
        self.next_token = next_token

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        return self


class ListStatefulAsyncInvocationFunctionsResponseBody(TeaModel):
    def __init__(
        self,
        data: List[AsyncConfigMeta] = None,
        next_token: str = None,
    ):
        # The trace ID of the request for Function Compute API.
        self.data = data
        # 2022-01-28 18:04:38
        self.next_token = next_token

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = AsyncConfigMeta()
                self.data.append(temp_model.from_map(k))
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        return self


class ListStatefulAsyncInvocationFunctionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListStatefulAsyncInvocationFunctionsResponseBody = None,
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
            temp_model = ListStatefulAsyncInvocationFunctionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListStatefulAsyncInvocationsHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_code_checksum: str = None,
        x_fc_date: str = None,
        x_fc_invocation_type: str = None,
        x_fc_log_type: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        # It is a tool used to manage and configure Alibaba Cloud resources. After simple installation and configuration, you can use Alibaba Cloud CLI to manage multiple Alibaba Cloud services and migrate your data and business to the cloud with ease.
        self.x_fc_account_id = x_fc_account_id
        # Alibaba Cloud CLI
        self.x_fc_code_checksum = x_fc_code_checksum
        # - **true**: returns the invocationPayload parameter in the response. 
        # - **false**: does not return the invocationPayload parameter in the response. 
        # 
        # > The `invocationPayload` parameter indicates the input parameters of an asynchronous task.
        self.x_fc_date = x_fc_date
        # The token used to obtain more results. If this parameter is left empty, all the results are returned.
        self.x_fc_invocation_type = x_fc_invocation_type
        # The time when Function Compute API is called.
        self.x_fc_log_type = x_fc_log_type
        # The CRC-64 value of the function code package. This value is used to check data integrity. The value is automatically calculated by the tool.
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_code_checksum is not None:
            result['X-Fc-Code-Checksum'] = self.x_fc_code_checksum
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_invocation_type is not None:
            result['X-Fc-Invocation-Type'] = self.x_fc_invocation_type
        if self.x_fc_log_type is not None:
            result['X-Fc-Log-Type'] = self.x_fc_log_type
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Code-Checksum') is not None:
            self.x_fc_code_checksum = m.get('X-Fc-Code-Checksum')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Invocation-Type') is not None:
            self.x_fc_invocation_type = m.get('X-Fc-Invocation-Type')
        if m.get('X-Fc-Log-Type') is not None:
            self.x_fc_log_type = m.get('X-Fc-Log-Type')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class ListStatefulAsyncInvocationsRequest(TeaModel):
    def __init__(
        self,
        include_payload: bool = None,
        invocation_id_prefix: str = None,
        limit: int = None,
        next_token: str = None,
        qualifier: str = None,
        sort_order_by_time: str = None,
        started_time_begin: int = None,
        started_time_end: int = None,
        status: str = None,
    ):
        # You can search for API operations, call and debug API operations online, and dynamically generate executable sample code for SDKs.
        self.include_payload = include_payload
        # Alibaba Cloud provides SDKs for multiple programming languages to help you integrate Alibaba Cloud services by using APIs. We recommend that you use an SDK to call API operations. This frees you from manual signature verification.
        self.invocation_id_prefix = invocation_id_prefix
        # The list of events that trigger the asynchronous task.
        self.limit = limit
        # The ID of the instance that is used to run the asynchronous task.
        self.next_token = next_token
        # The number of retries after the asynchronous task fails.
        self.qualifier = qualifier
        # StatefulAsyncInvocation: asynchronous task. Asynchronous tasks allow you to manage the states on the basis of common asynchronous invocations, which is more suitable for task scenarios.
        self.sort_order_by_time = sort_order_by_time
        # The structure of the asynchronous task.
        self.started_time_begin = started_time_begin
        # The latest version of Function Compute API.
        self.started_time_end = started_time_end
        # The request ID of the asynchronous task.
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
        if self.invocation_id_prefix is not None:
            result['invocationIdPrefix'] = self.invocation_id_prefix
        if self.limit is not None:
            result['limit'] = self.limit
        if self.next_token is not None:
            result['nextToken'] = self.next_token
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
        if m.get('invocationIdPrefix') is not None:
            self.invocation_id_prefix = m.get('invocationIdPrefix')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
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


class ListStatefulAsyncInvocationsResponseBody(TeaModel):
    def __init__(
        self,
        invocations: List[StatefulAsyncInvocation] = None,
        next_token: str = None,
    ):
        # The version or alias of the service to which the asynchronous task belongs.
        self.invocations = invocations
        # The returned data.
        self.next_token = next_token

    def validate(self):
        if self.invocations:
            for k in self.invocations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['invocations'] = []
        if self.invocations is not None:
            for k in self.invocations:
                result['invocations'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.invocations = []
        if m.get('invocations') is not None:
            for k in m.get('invocations'):
                temp_model = StatefulAsyncInvocation()
                self.invocations.append(temp_model.from_map(k))
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        return self


class ListStatefulAsyncInvocationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListStatefulAsyncInvocationsResponseBody = None,
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
            temp_model = ListStatefulAsyncInvocationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTaggedResourcesHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id
        # The time when Function Compute API is called. Specify the time in the **EEE,d MMM yyyy HH:mm:ss GMT** format.
        self.x_fc_date = x_fc_date
        # The custom request ID.
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class ListTaggedResourcesRequest(TeaModel):
    def __init__(
        self,
        limit: int = None,
        next_token: str = None,
    ):
        # The maximum number of resources to return. Default value: 20. Maximum value: 100. The number of returned resources is less than or equal to the specified number.
        self.limit = limit
        # The token used to obtain more results. You do not need to provide this parameter in the first call. The tokens for subsequent queries are obtained from the returned results.
        self.next_token = next_token

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        return self


class ListTaggedResourcesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        resources: List[Resource] = None,
    ):
        # The token used to obtain more results. You do not need to provide this parameter in the first call. The tokens for subsequent queries are obtained from the returned results.
        self.next_token = next_token
        # The information about tagged services.
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


class ListTaggedResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTaggedResourcesResponseBody = None,
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
            temp_model = ListTaggedResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTriggersHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id
        # The time when the request is initiated on the client. The format of the value is: **EEE,d MMM yyyy HH:mm:ss GMT**.
        self.x_fc_date = x_fc_date
        # The custom request ID.
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class ListTriggersRequest(TeaModel):
    def __init__(
        self,
        limit: int = None,
        next_token: str = None,
        prefix: str = None,
        start_key: str = None,
    ):
        # The maximum number of resources to return. Default value: 20. Maximum value: 100. The number of returned resources is less than or equal to the specified number.
        self.limit = limit
        # The token required to obtain more results. You do not need to provide this parameter in the first call. The tokens for subsequent queries are obtained from the returned results.
        self.next_token = next_token
        # The prefix that the names of returned resources must contain.
        self.prefix = prefix
        # The returned resources are sorted in alphabetical order, and the resources that include and follow the resource specified by the startKey parameter are returned.
        self.start_key = start_key

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
        if self.start_key is not None:
            result['startKey'] = self.start_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('prefix') is not None:
            self.prefix = m.get('prefix')
        if m.get('startKey') is not None:
            self.start_key = m.get('startKey')
        return self


class ListTriggersResponseBodyTriggers(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        description: str = None,
        domain_name: str = None,
        invocation_role: str = None,
        last_modified_time: str = None,
        qualifier: str = None,
        source_arn: str = None,
        trigger_config: str = None,
        trigger_id: str = None,
        trigger_name: str = None,
        trigger_type: str = None,
        url_internet: str = None,
        url_intranet: str = None,
    ):
        # The time when the trigger was created.
        self.created_time = created_time
        # The description of the trigger.
        self.description = description
        # The domain name used to invoke the function by using HTTP. You can add this domain name as the prefix to the endpoint of Function Compute. This way, you can invoke the function that corresponds to the trigger by using HTTP. Example: `{domainName}.cn-shanghai.fc.aliyuncs.com`.
        self.domain_name = domain_name
        # The Alibaba Cloud Resource Name (ARN) of the RAM role that is used by the event source to invoke the function.
        self.invocation_role = invocation_role
        # The time when the trigger was last modified.
        self.last_modified_time = last_modified_time
        # The version or alias of the service.
        self.qualifier = qualifier
        # The ARN of the event source.
        self.source_arn = source_arn
        # The configurations of the trigger. The configurations vary based on the trigger type. For more information about the format, see the following topics:
        # 
        # *   Object Storage Service (OSS) trigger: [OSSTriggerConfig](~~415697~~).
        # *   Simple Log Service trigger: [LogTriggerConfig](~~415694~~).
        # *   Time trigger: [TimeTriggerConfig](~~415712~~).
        # *   HTTP trigger: [HTTPTriggerConfig](~~415685~~).
        # *   Tablestore trigger: Specify the **SourceArn** parameter and leave this parameter empty.
        # *   Alibaba Cloud CDN event trigger: [CDNEventsTriggerConfig](javascript:void\(0\)).
        # *   MNS topic trigger: [MnsTopicTriggerConfig](~~415695~~).
        # *   EventBridge triggers: [EventBridgeTriggerConfig](javascript:void\(0\)).
        self.trigger_config = trigger_config
        # The unique ID of the trigger.
        self.trigger_id = trigger_id
        # The name of the trigger.
        self.trigger_name = trigger_name
        # The trigger type. Valid values: **oss**, **log**, **tablestore**, **timer**, **http**, **cdn_events**, **mns_topic**, and **eventbridge**.
        self.trigger_type = trigger_type
        # The public endpoint. You can access HTTP triggers over the Internet by using HTTP or HTTPS.
        self.url_internet = url_internet
        # The private endpoint. In a VPC, you can access HTTP triggers by using HTTP or HTTPS.
        self.url_intranet = url_intranet

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
        if self.domain_name is not None:
            result['domainName'] = self.domain_name
        if self.invocation_role is not None:
            result['invocationRole'] = self.invocation_role
        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        if self.source_arn is not None:
            result['sourceArn'] = self.source_arn
        if self.trigger_config is not None:
            result['triggerConfig'] = self.trigger_config
        if self.trigger_id is not None:
            result['triggerId'] = self.trigger_id
        if self.trigger_name is not None:
            result['triggerName'] = self.trigger_name
        if self.trigger_type is not None:
            result['triggerType'] = self.trigger_type
        if self.url_internet is not None:
            result['urlInternet'] = self.url_internet
        if self.url_intranet is not None:
            result['urlIntranet'] = self.url_intranet
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domainName') is not None:
            self.domain_name = m.get('domainName')
        if m.get('invocationRole') is not None:
            self.invocation_role = m.get('invocationRole')
        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        if m.get('sourceArn') is not None:
            self.source_arn = m.get('sourceArn')
        if m.get('triggerConfig') is not None:
            self.trigger_config = m.get('triggerConfig')
        if m.get('triggerId') is not None:
            self.trigger_id = m.get('triggerId')
        if m.get('triggerName') is not None:
            self.trigger_name = m.get('triggerName')
        if m.get('triggerType') is not None:
            self.trigger_type = m.get('triggerType')
        if m.get('urlInternet') is not None:
            self.url_internet = m.get('urlInternet')
        if m.get('urlIntranet') is not None:
            self.url_intranet = m.get('urlIntranet')
        return self


class ListTriggersResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        triggers: List[ListTriggersResponseBodyTriggers] = None,
    ):
        # The token used to obtain more results. If this parameter is left empty, all the results are returned.
        self.next_token = next_token
        # The information about triggers.
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
                temp_model = ListTriggersResponseBodyTriggers()
                self.triggers.append(temp_model.from_map(k))
        return self


class ListTriggersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTriggersResponseBody = None,
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
            temp_model = ListTriggersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListVpcBindingsHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id
        # The time when Function Compute API is called. Specify the time in the **EEE,d MMM yyyy HH:mm:ss GMT** format.
        self.x_fc_date = x_fc_date
        # The custom request ID.
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class ListVpcBindingsResponseBody(TeaModel):
    def __init__(
        self,
        vpc_ids: List[str] = None,
    ):
        # The IDs of bound VPCs.
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


class ListVpcBindingsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListVpcBindingsResponseBody = None,
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
            temp_model = ListVpcBindingsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PublishServiceVersionHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        if_match: str = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        # The ETag value of the service. This value is used to ensure that the modified service is consistent with the service to be modified. The ETag value is returned in the responses of the [CreateService](~~175256~~), [UpdateService](~~188167~~), and [GetService](~~189225~~) operations.
        self.if_match = if_match
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id
        # The start time when the function is invoked. Specify the time in the yyyy-mm-ddhh:mm:ss format.
        self.x_fc_date = x_fc_date
        # 2020-12-1210:00:00
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.if_match is not None:
            result['If-Match'] = self.if_match
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('If-Match') is not None:
            self.if_match = m.get('If-Match')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class PublishServiceVersionRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
    ):
        # The description of the service version.
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


class PublishServiceVersionResponseBody(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        description: str = None,
        last_modified_time: str = None,
        version_id: str = None,
    ):
        # The returned data.
        self.created_time = created_time
        # The creation time.
        self.description = description
        # The description of the service version.
        self.last_modified_time = last_modified_time
        # The last update time.
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


class PublishServiceVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PublishServiceVersionResponseBody = None,
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
            temp_model = PublishServiceVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PutFunctionAsyncInvokeConfigHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        # The name of the service.
        self.x_fc_account_id = x_fc_account_id
        # The creation time.
        self.x_fc_date = x_fc_date
        # The maximum number of retries allowed after an asynchronous invocation fails. Default value: 3. Valid values: 0 to 8.
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class PutFunctionAsyncInvokeConfigRequest(TeaModel):
    def __init__(
        self,
        destination_config: DestinationConfig = None,
        max_async_event_age_in_seconds: int = None,
        max_async_retry_attempts: int = None,
        stateful_invocation: bool = None,
        qualifier: str = None,
    ):
        # You can search for API operations, call and debug API operations online, and dynamically generate executable sample code for SDKs.
        self.destination_config = destination_config
        # Alibaba Cloud CLI
        self.max_async_event_age_in_seconds = max_async_event_age_in_seconds
        # The information about the asynchronous invocation configuration.
        self.max_async_retry_attempts = max_async_retry_attempts
        # The version or alias of the service.
        self.stateful_invocation = stateful_invocation
        # The latest version of Function Compute API.
        self.qualifier = qualifier

    def validate(self):
        if self.destination_config:
            self.destination_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_config is not None:
            result['destinationConfig'] = self.destination_config.to_map()
        if self.max_async_event_age_in_seconds is not None:
            result['maxAsyncEventAgeInSeconds'] = self.max_async_event_age_in_seconds
        if self.max_async_retry_attempts is not None:
            result['maxAsyncRetryAttempts'] = self.max_async_retry_attempts
        if self.stateful_invocation is not None:
            result['statefulInvocation'] = self.stateful_invocation
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('destinationConfig') is not None:
            temp_model = DestinationConfig()
            self.destination_config = temp_model.from_map(m['destinationConfig'])
        if m.get('maxAsyncEventAgeInSeconds') is not None:
            self.max_async_event_age_in_seconds = m.get('maxAsyncEventAgeInSeconds')
        if m.get('maxAsyncRetryAttempts') is not None:
            self.max_async_retry_attempts = m.get('maxAsyncRetryAttempts')
        if m.get('statefulInvocation') is not None:
            self.stateful_invocation = m.get('statefulInvocation')
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        return self


class PutFunctionAsyncInvokeConfigResponseBody(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        destination_config: DestinationConfig = None,
        function: str = None,
        last_modified_time: str = None,
        max_async_event_age_in_seconds: int = None,
        max_async_retry_attempts: int = None,
        qualifier: str = None,
        service: str = None,
        stateful_invocation: bool = None,
    ):
        # Sat, 14 Jul 2017 07:02:38 GMT
        self.created_time = created_time
        # The trace ID of the invocation request of Function Compute.
        self.destination_config = destination_config
        # The name of the function.
        self.function = function
        # The configuration structure of the destination for asynchronous invocation.
        self.last_modified_time = last_modified_time
        # Specifies whether to enable the asynchronous task feature. 
        # 
        # - **true**: enables the asynchronous task feature. 
        # - **false**: does not enable the asynchronous task feature.
        self.max_async_event_age_in_seconds = max_async_event_age_in_seconds
        # The ID of your Alibaba Cloud account.
        self.max_async_retry_attempts = max_async_retry_attempts
        # Specifies whether to enable the asynchronous task feature. 
        # 
        # - **true**: enables the asynchronous task feature. 
        # - **false**: does not enable the asynchronous task feature.
        self.qualifier = qualifier
        # Creates or modifies an asynchronous invocation configuration for a function.
        self.service = service
        # Jianyi
        self.stateful_invocation = stateful_invocation

    def validate(self):
        if self.destination_config:
            self.destination_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.destination_config is not None:
            result['destinationConfig'] = self.destination_config.to_map()
        if self.function is not None:
            result['function'] = self.function
        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time
        if self.max_async_event_age_in_seconds is not None:
            result['maxAsyncEventAgeInSeconds'] = self.max_async_event_age_in_seconds
        if self.max_async_retry_attempts is not None:
            result['maxAsyncRetryAttempts'] = self.max_async_retry_attempts
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        if self.service is not None:
            result['service'] = self.service
        if self.stateful_invocation is not None:
            result['statefulInvocation'] = self.stateful_invocation
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('destinationConfig') is not None:
            temp_model = DestinationConfig()
            self.destination_config = temp_model.from_map(m['destinationConfig'])
        if m.get('function') is not None:
            self.function = m.get('function')
        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')
        if m.get('maxAsyncEventAgeInSeconds') is not None:
            self.max_async_event_age_in_seconds = m.get('maxAsyncEventAgeInSeconds')
        if m.get('maxAsyncRetryAttempts') is not None:
            self.max_async_retry_attempts = m.get('maxAsyncRetryAttempts')
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        if m.get('service') is not None:
            self.service = m.get('service')
        if m.get('statefulInvocation') is not None:
            self.stateful_invocation = m.get('statefulInvocation')
        return self


class PutFunctionAsyncInvokeConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PutFunctionAsyncInvokeConfigResponseBody = None,
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
            temp_model = PutFunctionAsyncInvokeConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PutFunctionOnDemandConfigHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        if_match: str = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        # If the ETag specified in the request matches the ETag value of the object, the object and 200 OK are returned. Otherwise, 412 Precondition Failed is returned.
        self.if_match = if_match
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id
        # The time when the function is invoked. The value is in the **EEE,d MMM yyyy HH:mm:ss GMT** format.
        self.x_fc_date = x_fc_date
        # The unique ID of the trace.
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.if_match is not None:
            result['If-Match'] = self.if_match
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('If-Match') is not None:
            self.if_match = m.get('If-Match')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class PutFunctionOnDemandConfigRequest(TeaModel):
    def __init__(
        self,
        maximum_instance_count: int = None,
        qualifier: str = None,
    ):
        # The maximum number of on-demand instances. For more information, see [Configure provisioned instances and auto scaling rules](~~185038~~).
        self.maximum_instance_count = maximum_instance_count
        # The service alias or latest version. Other versions are not supported.
        self.qualifier = qualifier

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.maximum_instance_count is not None:
            result['maximumInstanceCount'] = self.maximum_instance_count
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maximumInstanceCount') is not None:
            self.maximum_instance_count = m.get('maximumInstanceCount')
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        return self


class PutFunctionOnDemandConfigResponseBody(TeaModel):
    def __init__(
        self,
        maximum_instance_count: int = None,
        resource: str = None,
    ):
        # The maximum number of instances.
        self.maximum_instance_count = maximum_instance_count
        # The description of the resource.
        self.resource = resource

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.maximum_instance_count is not None:
            result['maximumInstanceCount'] = self.maximum_instance_count
        if self.resource is not None:
            result['resource'] = self.resource
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maximumInstanceCount') is not None:
            self.maximum_instance_count = m.get('maximumInstanceCount')
        if m.get('resource') is not None:
            self.resource = m.get('resource')
        return self


class PutFunctionOnDemandConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PutFunctionOnDemandConfigResponseBody = None,
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
            temp_model = PutFunctionOnDemandConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PutLayerACLHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id
        # The time when the operation is called. The format is: **EEE,d MMM yyyy HH:mm:ss GMT**.
        self.x_fc_date = x_fc_date
        # The trace ID of the request for Function Compute API.
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class PutLayerACLRequest(TeaModel):
    def __init__(
        self,
        public: bool = None,
    ):
        # Specifies whether the layer is public.
        # 
        # *   **true**: Public.
        # *   **false**: Not public.
        self.public = public

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.public is not None:
            result['public'] = self.public
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

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


class PutProvisionConfigHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id
        # The time when the function is invoked. The value follows the **EEE,d MMM yyyy HH:mm:ss GMT** format.
        self.x_fc_date = x_fc_date
        # The trace ID of the invocation request of Function Compute.
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class PutProvisionConfigRequest(TeaModel):
    def __init__(
        self,
        always_allocate_cpu: bool = None,
        scheduled_actions: List[ScheduledActions] = None,
        target: int = None,
        target_tracking_policies: List[TargetTrackingPolicies] = None,
        qualifier: str = None,
    ):
        # Specifies whether to always allocate CPU resources. Default value: true.
        self.always_allocate_cpu = always_allocate_cpu
        # The configurations of scheduled auto scaling.
        self.scheduled_actions = scheduled_actions
        # The number of target provisioned instances. Valid values: \[0,10000].
        self.target = target
        # The configurations of metric-based auto scaling.
        self.target_tracking_policies = target_tracking_policies
        # The service alias or latest version. Other versions are not supported.
        self.qualifier = qualifier

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
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alwaysAllocateCPU') is not None:
            self.always_allocate_cpu = m.get('alwaysAllocateCPU')
        self.scheduled_actions = []
        if m.get('scheduledActions') is not None:
            for k in m.get('scheduledActions'):
                temp_model = ScheduledActions()
                self.scheduled_actions.append(temp_model.from_map(k))
        if m.get('target') is not None:
            self.target = m.get('target')
        self.target_tracking_policies = []
        if m.get('targetTrackingPolicies') is not None:
            for k in m.get('targetTrackingPolicies'):
                temp_model = TargetTrackingPolicies()
                self.target_tracking_policies.append(temp_model.from_map(k))
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        return self


class PutProvisionConfigResponseBody(TeaModel):
    def __init__(
        self,
        always_allocate_cpu: bool = None,
        current: int = None,
        resource: str = None,
        scheduled_actions: List[ScheduledActions] = None,
        target: int = None,
        target_tracking_policies: List[TargetTrackingPolicies] = None,
    ):
        # Specifies whether to always allocate CPU to a function instance.
        self.always_allocate_cpu = always_allocate_cpu
        # The actual number of provisioned instances.
        self.current = current
        # The description of the resource.
        self.resource = resource
        # The configurations of scheduled auto scaling.
        self.scheduled_actions = scheduled_actions
        # The number of target provisioned instances.
        self.target = target
        # The configurations of metric-based auto scaling.
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
        if self.resource is not None:
            result['resource'] = self.resource
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
        if m.get('resource') is not None:
            self.resource = m.get('resource')
        self.scheduled_actions = []
        if m.get('scheduledActions') is not None:
            for k in m.get('scheduledActions'):
                temp_model = ScheduledActions()
                self.scheduled_actions.append(temp_model.from_map(k))
        if m.get('target') is not None:
            self.target = m.get('target')
        self.target_tracking_policies = []
        if m.get('targetTrackingPolicies') is not None:
            for k in m.get('targetTrackingPolicies'):
                temp_model = TargetTrackingPolicies()
                self.target_tracking_policies.append(temp_model.from_map(k))
        return self


class PutProvisionConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PutProvisionConfigResponseBody = None,
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
            temp_model = PutProvisionConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RegisterEventSourceHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id
        # The time when Function Compute API is called. Specify the time in the **EEE,d MMM yyyy HH:mm:ss GMT** format.
        self.x_fc_date = x_fc_date
        # The trace ID of the invocation request of Function Compute.
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class RegisterEventSourceRequest(TeaModel):
    def __init__(
        self,
        source_arn: str = None,
        qualifier: str = None,
    ):
        # The Alibaba Cloud Resource Name (ARN) of the event source.
        self.source_arn = source_arn
        # The version or alias of the service.
        self.qualifier = qualifier

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_arn is not None:
            result['sourceArn'] = self.source_arn
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sourceArn') is not None:
            self.source_arn = m.get('sourceArn')
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        return self


class RegisterEventSourceResponseBody(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        source_arn: str = None,
    ):
        # The time when the event source was created.
        self.created_time = created_time
        # The ARN of the event source.
        self.source_arn = source_arn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.source_arn is not None:
            result['sourceArn'] = self.source_arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('sourceArn') is not None:
            self.source_arn = m.get('sourceArn')
        return self


class RegisterEventSourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RegisterEventSourceResponseBody = None,
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
            temp_model = RegisterEventSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReleaseGPUInstanceHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id
        # The time when the function is invoked. The format of the value is: EEE,d MMM yyyy HH:mm:ss GMT.
        self.x_fc_date = x_fc_date
        # The custom request ID.
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class ReleaseGPUInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

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


class StopStatefulAsyncInvocationHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id
        # The time when Function Compute API is called. Specify the time in the **EEE,d MMM yyyy HH:mm:ss GMT** format.
        self.x_fc_date = x_fc_date
        # The trace ID of the invocation request of Function Compute.
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class StopStatefulAsyncInvocationRequest(TeaModel):
    def __init__(
        self,
        qualifier: str = None,
    ):
        # The version or alias of the service to which the asynchronous task belongs.
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


class StopStatefulAsyncInvocationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

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


class TagResourceHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id
        # The time when the function is invoked. The format is **EEE,d MMM yyyy HH:mm:ss GMT**.
        self.x_fc_date = x_fc_date
        # The custom request ID.
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class TagResourceRequest(TeaModel):
    def __init__(
        self,
        resource_arn: str = None,
        tags: Dict[str, str] = None,
    ):
        # The ARN of the resource.
        # 
        # > You can use the value of this parameter to query the information about the resource, such as the account, service, and region information of the resource. You can manage tags only for services for top level resources.
        self.resource_arn = resource_arn
        # The tag dictionary.
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


class TagResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

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


class UntagResourceHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id
        # The time when the function is invoked. The value is in the **EEE,d MMM yyyy HH:mm:ss GMT** format.
        self.x_fc_date = x_fc_date
        # The custom request ID.
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class UntagResourceRequest(TeaModel):
    def __init__(
        self,
        all: bool = None,
        resource_arn: str = None,
        tag_keys: List[str] = None,
    ):
        # Specifies whether to remove all tags. This parameter takes effect only when no tag key is specified. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.all = all
        # The Alibaba Cloud Resource Name (ARN) of the resource.
        # 
        # > You can use the value of this parameter to query the information about the resource, such as the account, service, and region information of the resource. You can manage tags only for services for top level resources.
        self.resource_arn = resource_arn
        # The keys of the tags that you want to remove.
        self.tag_keys = tag_keys

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['all'] = self.all
        if self.resource_arn is not None:
            result['resourceArn'] = self.resource_arn
        if self.tag_keys is not None:
            result['tagKeys'] = self.tag_keys
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('all') is not None:
            self.all = m.get('all')
        if m.get('resourceArn') is not None:
            self.resource_arn = m.get('resourceArn')
        if m.get('tagKeys') is not None:
            self.tag_keys = m.get('tagKeys')
        return self


class UntagResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

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


class UpdateAliasHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        if_match: str = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        # If the ETag specified in the request matches the ETag value of the object, the object and 200 OK are returned. Otherwise, 412 Precondition Failed is returned.
        # 
        # The ETag value of an object is used to check data integrity of the object. This parameter is empty by default.
        self.if_match = if_match
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id
        # The time on which the function is invoked. The format of the value is: **EEE,d MMM yyyy HH:mm:ss GMT**.
        self.x_fc_date = x_fc_date
        # The trace ID of the invocation request of Function Compute.
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.if_match is not None:
            result['If-Match'] = self.if_match
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('If-Match') is not None:
            self.if_match = m.get('If-Match')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class UpdateAliasRequest(TeaModel):
    def __init__(
        self,
        additional_version_weight: Dict[str, float] = None,
        description: str = None,
        resolve_policy: str = None,
        route_policy: RoutePolicy = None,
        version_id: str = None,
    ):
        # The additional version to which the alias points and the weight of the additional version.
        # 
        # *   The additional version takes effect only when the function is invoked.
        # *   The value consists of a version number and a specific weight. For example, 2:0.05 indicates that when a function is invoked, Version 2 is the canary release version, 5% of the traffic is distributed to the canary release version, and 95% of the traffic is distributed to the major version.
        self.additional_version_weight = additional_version_weight
        # The description of the alias.
        self.description = description
        # The canary release mode. Valid values:
        # 
        # *   **Random**: random canary release. This is the default value.
        # *   **Content**: rule-based canary release.
        self.resolve_policy = resolve_policy
        # The canary release rule. Traffic that meets the canary release rule is routed to the canary release instance.
        self.route_policy = route_policy
        # The ID of the version to which the alias points.
        self.version_id = version_id

    def validate(self):
        if self.route_policy:
            self.route_policy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.additional_version_weight is not None:
            result['additionalVersionWeight'] = self.additional_version_weight
        if self.description is not None:
            result['description'] = self.description
        if self.resolve_policy is not None:
            result['resolvePolicy'] = self.resolve_policy
        if self.route_policy is not None:
            result['routePolicy'] = self.route_policy.to_map()
        if self.version_id is not None:
            result['versionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('additionalVersionWeight') is not None:
            self.additional_version_weight = m.get('additionalVersionWeight')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('resolvePolicy') is not None:
            self.resolve_policy = m.get('resolvePolicy')
        if m.get('routePolicy') is not None:
            temp_model = RoutePolicy()
            self.route_policy = temp_model.from_map(m['routePolicy'])
        if m.get('versionId') is not None:
            self.version_id = m.get('versionId')
        return self


class UpdateAliasResponseBody(TeaModel):
    def __init__(
        self,
        additional_version_weight: Dict[str, float] = None,
        alias_name: str = None,
        created_time: str = None,
        description: str = None,
        last_modified_time: str = None,
        resolve_policy: str = None,
        route_policy: RoutePolicy = None,
        version_id: str = None,
    ):
        # The additional version to which the alias points and the weight of the additional version.
        # 
        # *   The additional version takes effect only when the function is invoked.
        # *   The value consists of a version number and a specific weight. For example, 2:0.05 indicates that when a function is invoked, Version 2 is the canary release version, 5% of the traffic is distributed to the canary release version, and 95% of the traffic is distributed to the major version.
        self.additional_version_weight = additional_version_weight
        # The name of the alias.
        self.alias_name = alias_name
        # The time when the alias was created.
        self.created_time = created_time
        # The description of the alias.
        self.description = description
        # The time when the alias was last modified.
        self.last_modified_time = last_modified_time
        self.resolve_policy = resolve_policy
        self.route_policy = route_policy
        # The ID of the version to which the alias points.
        self.version_id = version_id

    def validate(self):
        if self.route_policy:
            self.route_policy.validate()

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
        if self.resolve_policy is not None:
            result['resolvePolicy'] = self.resolve_policy
        if self.route_policy is not None:
            result['routePolicy'] = self.route_policy.to_map()
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
        if m.get('resolvePolicy') is not None:
            self.resolve_policy = m.get('resolvePolicy')
        if m.get('routePolicy') is not None:
            temp_model = RoutePolicy()
            self.route_policy = temp_model.from_map(m['routePolicy'])
        if m.get('versionId') is not None:
            self.version_id = m.get('versionId')
        return self


class UpdateAliasResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateAliasResponseBody = None,
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
            temp_model = UpdateAliasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCustomDomainHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id
        # The time when the operation is called. The format is: **EEE,d MMM yyyy HH:mm:ss GMT**.
        self.x_fc_date = x_fc_date
        # The custom request ID.
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class UpdateCustomDomainRequest(TeaModel):
    def __init__(
        self,
        cert_config: CertConfig = None,
        protocol: str = None,
        route_config: RouteConfig = None,
        tls_config: TLSConfig = None,
        waf_config: WAFConfig = None,
    ):
        # The configurations of the HTTPS certificate.
        self.cert_config = cert_config
        # The protocol types supported by the domain name. Valid values:
        # 
        # *   **HTTP**: Only HTTP is supported.
        # *   **HTTPS**: Only HTTPS is supported.
        # *   **HTTP,HTTPS**: HTTP and HTTPS are supported.
        self.protocol = protocol
        # The route table that maps the paths to functions when the functions are invoked by using the custom domain name.
        self.route_config = route_config
        # The Transport Layer Security (TLS) configuration.
        self.tls_config = tls_config
        # The Web Application Firewall (WAF) configuration.
        self.waf_config = waf_config

    def validate(self):
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


class UpdateCustomDomainResponseBody(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        api_version: str = None,
        cert_config: CertConfig = None,
        created_time: str = None,
        domain_name: str = None,
        last_modified_time: str = None,
        protocol: str = None,
        route_config: RouteConfig = None,
        tls_config: TLSConfig = None,
        waf_config: WAFConfig = None,
    ):
        # The ID of your Alibaba Cloud account.
        self.account_id = account_id
        # The version of the API.
        self.api_version = api_version
        # The configurations of the HTTPS certificate.
        self.cert_config = cert_config
        # The time when the custom domain name was created.
        self.created_time = created_time
        # The domain name.
        self.domain_name = domain_name
        # The time when the domain name was last modified.
        self.last_modified_time = last_modified_time
        # The protocol type that is supported by the custom domain name.
        # 
        # *   **HTTP**: Only HTTP is supported.
        # *   **HTTPS**: Only HTTPS is supported.
        # *   **HTTP,HTTPS**: HTTP and HTTPS are supported.
        self.protocol = protocol
        # The route table that maps the paths to functions when the functions are invoked by using the custom domain name.
        self.route_config = route_config
        # The Transport Layer Security (TLS) configuration.
        self.tls_config = tls_config
        # The Web Application Firewall (WAF) configuration.
        self.waf_config = waf_config

    def validate(self):
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
        if m.get('tlsConfig') is not None:
            temp_model = TLSConfig()
            self.tls_config = temp_model.from_map(m['tlsConfig'])
        if m.get('wafConfig') is not None:
            temp_model = WAFConfig()
            self.waf_config = temp_model.from_map(m['wafConfig'])
        return self


class UpdateCustomDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateCustomDomainResponseBody = None,
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
            temp_model = UpdateCustomDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFunctionHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        if_match: str = None,
        x_fc_account_id: str = None,
        x_fc_code_checksum: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        self.if_match = if_match
        self.x_fc_account_id = x_fc_account_id
        self.x_fc_code_checksum = x_fc_code_checksum
        self.x_fc_date = x_fc_date
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.if_match is not None:
            result['If-Match'] = self.if_match
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_code_checksum is not None:
            result['X-Fc-Code-Checksum'] = self.x_fc_code_checksum
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('If-Match') is not None:
            self.if_match = m.get('If-Match')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Code-Checksum') is not None:
            self.x_fc_code_checksum = m.get('X-Fc-Code-Checksum')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class UpdateFunctionRequest(TeaModel):
    def __init__(
        self,
        instance_concurrency: int = None,
        ca_port: int = None,
        code: Code = None,
        cpu: float = None,
        custom_container_config: CustomContainerConfig = None,
        custom_dns: CustomDNS = None,
        custom_health_check_config: CustomHealthCheckConfig = None,
        custom_runtime_config: CustomRuntimeConfig = None,
        description: str = None,
        disk_size: int = None,
        environment_variables: Dict[str, str] = None,
        gpu_memory_size: int = None,
        handler: str = None,
        initialization_timeout: int = None,
        initializer: str = None,
        instance_lifecycle_config: InstanceLifecycleConfig = None,
        instance_soft_concurrency: int = None,
        instance_type: str = None,
        layers: List[str] = None,
        memory_size: int = None,
        runtime: str = None,
        timeout: int = None,
    ):
        # The number of requests that can be concurrently processed by a single instance.
        self.instance_concurrency = instance_concurrency
        # The port on which the HTTP server listens for the custom runtime or custom container runtime.
        self.ca_port = ca_port
        # The packaged code of the function. **Function code packages** can be provided with the following two methods. You must use only one of the methods in a request.
        # 
        # *   Specify the name of the Object Storage Service (OSS) bucket and object where the code package is stored. The names are specified in the **ossBucketName** and **ossObjectName** parameters.
        # *   Specify the Base64-encoded content of the ZIP file by using the **zipFile** parameter.
        self.code = code
        # The number of vCPUs of the function. The value is a multiple of 0.05.
        self.cpu = cpu
        # The configuration of the custom container. After you configure the custom container, Function Compute can execute the function in a container created from a custom image.
        self.custom_container_config = custom_container_config
        # The custom DNS configurations of the function.
        self.custom_dns = custom_dns
        # The custom health check configuration of the function. This parameter is applicable only to custom runtimes and custom containers.
        self.custom_health_check_config = custom_health_check_config
        # The configurations of the custom runtime for the function.
        self.custom_runtime_config = custom_runtime_config
        # The description of the function.
        self.description = description
        # The disk size of the function. Unit: MB. Valid values: 512 and 10240.
        self.disk_size = disk_size
        # The environment variables that are configured for the function. You can obtain the values of the environment variables from the function. For more information, see [Environment variables](~~69777~~).
        self.environment_variables = environment_variables
        # The GPU memory capacity for the function. Unit: MB. The value is a multiple of 1,024.
        self.gpu_memory_size = gpu_memory_size
        # The handler of the function. The format varies based on the programming language. For more information, see [Function handlers](~~157704~~).
        self.handler = handler
        # The timeout period for the execution of the Initializer hook. Unit: seconds. Default value: 3. Minimum value: 1. When the period ends, the execution of the Initializer hook is terminated.
        self.initialization_timeout = initialization_timeout
        # The handler of the Initializer hook. The format is determined by the programming language. For more information, see [Function handlers](~~157704~~).
        self.initializer = initializer
        # The lifecycle configurations of the instance.
        self.instance_lifecycle_config = instance_lifecycle_config
        # The soft concurrency of the instance. You can use this property to implement graceful scale-ups for instances. If the number of concurrent requests on an instance is greater than the soft concurrency value of the instance, an instance scale-up is triggered. For example, if your instance requires a long time to start, you can specify a suitable soft concurrency to start the instance in advance.
        # 
        # The value must be less than or equal to that of the **instanceConcurrency** parameter.
        self.instance_soft_concurrency = instance_soft_concurrency
        # The instance type of the function. Valid values:
        # 
        # *   **e1**: elastic instance
        # *   **c1**: performance instance
        # *   **fc.gpu.tesla.1**: GPU-accelerated instance (Tesla T4)
        # *   **fc.gpu.ampere.1**: GPU-accelerated instance (Ampere A10)
        # *   **g1**: same as **fc.gpu.tesla.1**\
        self.instance_type = instance_type
        # An array that consists of the information of layers.
        # 
        # > Multiple layers are merged based on the order of array subscripts. The content of a layer with a smaller subscript overwrites the file that has the same name as a layer with a larger subscript.
        self.layers = layers
        # The memory size for the function. Unit: MB. The value must be a multiple of 64. The memory size varies based on the function instance type. For more information, see [Instance types](~~179379~~).
        self.memory_size = memory_size
        # The runtime environment of the function. Valid values: **nodejs16**, **nodejs14**, **nodejs12**, **nodejs10**, **nodejs8**, **nodejs6**, **nodejs4.4**, **python3.10**, **python3.9**, **python3**, **python2.7**, **java11**, **java8**, **go1**, **php7.2**, **dotnetcore3.1**, **dotnetcore2.1**, **custom.debian10**, **custom**, and **custom-container**. For more information, see [Supported function runtime environments](~~73338~~).
        self.runtime = runtime
        # The timeout period for the execution of the function. Unit: seconds. Default value: 3. Minimum value: 1. When the period ends, the execution of the function is terminated.
        self.timeout = timeout

    def validate(self):
        if self.code:
            self.code.validate()
        if self.custom_container_config:
            self.custom_container_config.validate()
        if self.custom_dns:
            self.custom_dns.validate()
        if self.custom_health_check_config:
            self.custom_health_check_config.validate()
        if self.custom_runtime_config:
            self.custom_runtime_config.validate()
        if self.instance_lifecycle_config:
            self.instance_lifecycle_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_concurrency is not None:
            result['InstanceConcurrency'] = self.instance_concurrency
        if self.ca_port is not None:
            result['caPort'] = self.ca_port
        if self.code is not None:
            result['code'] = self.code.to_map()
        if self.cpu is not None:
            result['cpu'] = self.cpu
        if self.custom_container_config is not None:
            result['customContainerConfig'] = self.custom_container_config.to_map()
        if self.custom_dns is not None:
            result['customDNS'] = self.custom_dns.to_map()
        if self.custom_health_check_config is not None:
            result['customHealthCheckConfig'] = self.custom_health_check_config.to_map()
        if self.custom_runtime_config is not None:
            result['customRuntimeConfig'] = self.custom_runtime_config.to_map()
        if self.description is not None:
            result['description'] = self.description
        if self.disk_size is not None:
            result['diskSize'] = self.disk_size
        if self.environment_variables is not None:
            result['environmentVariables'] = self.environment_variables
        if self.gpu_memory_size is not None:
            result['gpuMemorySize'] = self.gpu_memory_size
        if self.handler is not None:
            result['handler'] = self.handler
        if self.initialization_timeout is not None:
            result['initializationTimeout'] = self.initialization_timeout
        if self.initializer is not None:
            result['initializer'] = self.initializer
        if self.instance_lifecycle_config is not None:
            result['instanceLifecycleConfig'] = self.instance_lifecycle_config.to_map()
        if self.instance_soft_concurrency is not None:
            result['instanceSoftConcurrency'] = self.instance_soft_concurrency
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        if self.layers is not None:
            result['layers'] = self.layers
        if self.memory_size is not None:
            result['memorySize'] = self.memory_size
        if self.runtime is not None:
            result['runtime'] = self.runtime
        if self.timeout is not None:
            result['timeout'] = self.timeout
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceConcurrency') is not None:
            self.instance_concurrency = m.get('InstanceConcurrency')
        if m.get('caPort') is not None:
            self.ca_port = m.get('caPort')
        if m.get('code') is not None:
            temp_model = Code()
            self.code = temp_model.from_map(m['code'])
        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')
        if m.get('customContainerConfig') is not None:
            temp_model = CustomContainerConfig()
            self.custom_container_config = temp_model.from_map(m['customContainerConfig'])
        if m.get('customDNS') is not None:
            temp_model = CustomDNS()
            self.custom_dns = temp_model.from_map(m['customDNS'])
        if m.get('customHealthCheckConfig') is not None:
            temp_model = CustomHealthCheckConfig()
            self.custom_health_check_config = temp_model.from_map(m['customHealthCheckConfig'])
        if m.get('customRuntimeConfig') is not None:
            temp_model = CustomRuntimeConfig()
            self.custom_runtime_config = temp_model.from_map(m['customRuntimeConfig'])
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('diskSize') is not None:
            self.disk_size = m.get('diskSize')
        if m.get('environmentVariables') is not None:
            self.environment_variables = m.get('environmentVariables')
        if m.get('gpuMemorySize') is not None:
            self.gpu_memory_size = m.get('gpuMemorySize')
        if m.get('handler') is not None:
            self.handler = m.get('handler')
        if m.get('initializationTimeout') is not None:
            self.initialization_timeout = m.get('initializationTimeout')
        if m.get('initializer') is not None:
            self.initializer = m.get('initializer')
        if m.get('instanceLifecycleConfig') is not None:
            temp_model = InstanceLifecycleConfig()
            self.instance_lifecycle_config = temp_model.from_map(m['instanceLifecycleConfig'])
        if m.get('instanceSoftConcurrency') is not None:
            self.instance_soft_concurrency = m.get('instanceSoftConcurrency')
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        if m.get('layers') is not None:
            self.layers = m.get('layers')
        if m.get('memorySize') is not None:
            self.memory_size = m.get('memorySize')
        if m.get('runtime') is not None:
            self.runtime = m.get('runtime')
        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')
        return self


class UpdateFunctionResponseBody(TeaModel):
    def __init__(
        self,
        ca_port: int = None,
        code_checksum: str = None,
        code_size: int = None,
        cpu: float = None,
        created_time: str = None,
        custom_container_config: CustomContainerConfig = None,
        custom_dns: CustomDNS = None,
        custom_health_check_config: CustomHealthCheckConfig = None,
        custom_runtime_config: CustomRuntimeConfig = None,
        description: str = None,
        disk_size: int = None,
        environment_variables: Dict[str, str] = None,
        function_id: str = None,
        function_name: str = None,
        gpu_memory_size: int = None,
        handler: str = None,
        initialization_timeout: int = None,
        initializer: str = None,
        instance_concurrency: int = None,
        instance_lifecycle_config: InstanceLifecycleConfig = None,
        instance_soft_concurrency: int = None,
        instance_type: str = None,
        last_modified_time: str = None,
        layers: List[str] = None,
        layers_arn_v2: List[str] = None,
        memory_size: int = None,
        runtime: str = None,
        timeout: int = None,
    ):
        self.ca_port = ca_port
        self.code_checksum = code_checksum
        self.code_size = code_size
        self.cpu = cpu
        self.created_time = created_time
        self.custom_container_config = custom_container_config
        self.custom_dns = custom_dns
        self.custom_health_check_config = custom_health_check_config
        self.custom_runtime_config = custom_runtime_config
        self.description = description
        self.disk_size = disk_size
        self.environment_variables = environment_variables
        self.function_id = function_id
        self.function_name = function_name
        self.gpu_memory_size = gpu_memory_size
        self.handler = handler
        self.initialization_timeout = initialization_timeout
        self.initializer = initializer
        self.instance_concurrency = instance_concurrency
        self.instance_lifecycle_config = instance_lifecycle_config
        self.instance_soft_concurrency = instance_soft_concurrency
        self.instance_type = instance_type
        self.last_modified_time = last_modified_time
        # An array that consists of the information of layers.
        # 
        # > Multiple layers are merged based on the order of array subscripts. The content of a layer with a smaller subscript overwrites the file that has the same name as a layer with a larger subscript.
        self.layers = layers
        # ARN list of layers
        self.layers_arn_v2 = layers_arn_v2
        self.memory_size = memory_size
        # The runtime environment of the function. Valid values: **nodejs16**, **nodejs14**, **nodejs12**, **nodejs10**, **nodejs8**, **nodejs6**, **nodejs4.4**, **python3.10**, **python3.9**, **python3**, **python2.7**, **java11**, **java8**, **go1**, **php7.2**, **dotnetcore3.1**, **dotnetcore2.1**, **custom.debian10**, **custom**, and **custom-container**. For more information, see [Supported function runtime environments](~~73338~~).
        self.runtime = runtime
        self.timeout = timeout

    def validate(self):
        if self.custom_container_config:
            self.custom_container_config.validate()
        if self.custom_dns:
            self.custom_dns.validate()
        if self.custom_health_check_config:
            self.custom_health_check_config.validate()
        if self.custom_runtime_config:
            self.custom_runtime_config.validate()
        if self.instance_lifecycle_config:
            self.instance_lifecycle_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ca_port is not None:
            result['caPort'] = self.ca_port
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
        if self.custom_health_check_config is not None:
            result['customHealthCheckConfig'] = self.custom_health_check_config.to_map()
        if self.custom_runtime_config is not None:
            result['customRuntimeConfig'] = self.custom_runtime_config.to_map()
        if self.description is not None:
            result['description'] = self.description
        if self.disk_size is not None:
            result['diskSize'] = self.disk_size
        if self.environment_variables is not None:
            result['environmentVariables'] = self.environment_variables
        if self.function_id is not None:
            result['functionId'] = self.function_id
        if self.function_name is not None:
            result['functionName'] = self.function_name
        if self.gpu_memory_size is not None:
            result['gpuMemorySize'] = self.gpu_memory_size
        if self.handler is not None:
            result['handler'] = self.handler
        if self.initialization_timeout is not None:
            result['initializationTimeout'] = self.initialization_timeout
        if self.initializer is not None:
            result['initializer'] = self.initializer
        if self.instance_concurrency is not None:
            result['instanceConcurrency'] = self.instance_concurrency
        if self.instance_lifecycle_config is not None:
            result['instanceLifecycleConfig'] = self.instance_lifecycle_config.to_map()
        if self.instance_soft_concurrency is not None:
            result['instanceSoftConcurrency'] = self.instance_soft_concurrency
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time
        if self.layers is not None:
            result['layers'] = self.layers
        if self.layers_arn_v2 is not None:
            result['layersArnV2'] = self.layers_arn_v2
        if self.memory_size is not None:
            result['memorySize'] = self.memory_size
        if self.runtime is not None:
            result['runtime'] = self.runtime
        if self.timeout is not None:
            result['timeout'] = self.timeout
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('caPort') is not None:
            self.ca_port = m.get('caPort')
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
        if m.get('customHealthCheckConfig') is not None:
            temp_model = CustomHealthCheckConfig()
            self.custom_health_check_config = temp_model.from_map(m['customHealthCheckConfig'])
        if m.get('customRuntimeConfig') is not None:
            temp_model = CustomRuntimeConfig()
            self.custom_runtime_config = temp_model.from_map(m['customRuntimeConfig'])
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('diskSize') is not None:
            self.disk_size = m.get('diskSize')
        if m.get('environmentVariables') is not None:
            self.environment_variables = m.get('environmentVariables')
        if m.get('functionId') is not None:
            self.function_id = m.get('functionId')
        if m.get('functionName') is not None:
            self.function_name = m.get('functionName')
        if m.get('gpuMemorySize') is not None:
            self.gpu_memory_size = m.get('gpuMemorySize')
        if m.get('handler') is not None:
            self.handler = m.get('handler')
        if m.get('initializationTimeout') is not None:
            self.initialization_timeout = m.get('initializationTimeout')
        if m.get('initializer') is not None:
            self.initializer = m.get('initializer')
        if m.get('instanceConcurrency') is not None:
            self.instance_concurrency = m.get('instanceConcurrency')
        if m.get('instanceLifecycleConfig') is not None:
            temp_model = InstanceLifecycleConfig()
            self.instance_lifecycle_config = temp_model.from_map(m['instanceLifecycleConfig'])
        if m.get('instanceSoftConcurrency') is not None:
            self.instance_soft_concurrency = m.get('instanceSoftConcurrency')
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')
        if m.get('layers') is not None:
            self.layers = m.get('layers')
        if m.get('layersArnV2') is not None:
            self.layers_arn_v2 = m.get('layersArnV2')
        if m.get('memorySize') is not None:
            self.memory_size = m.get('memorySize')
        if m.get('runtime') is not None:
            self.runtime = m.get('runtime')
        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')
        return self


class UpdateFunctionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateFunctionResponseBody = None,
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
            temp_model = UpdateFunctionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateServiceHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        if_match: str = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        # The value used to ensure that the modified service is consistent with the service to be modified. The value is obtained from the responses of the [CreateService](~~175256~~), [UpdateService](~~188167~~), and [GetService](~~189225~~) operations.
        self.if_match = if_match
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id
        # The time when the Function Compute API is called. The format is **EEE,d MMM yyyy HH:mm:ss GMT**.
        self.x_fc_date = x_fc_date
        # The custom request ID.
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.if_match is not None:
            result['If-Match'] = self.if_match
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('If-Match') is not None:
            self.if_match = m.get('If-Match')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class UpdateServiceRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        internet_access: bool = None,
        log_config: LogConfig = None,
        nas_config: NASConfig = None,
        oss_mount_config: OSSMountConfig = None,
        role: str = None,
        tracing_config: TracingConfig = None,
        vpc_config: VPCConfig = None,
    ):
        # The description of the service.
        self.description = description
        # Specifies whether to allow functions to access the Internet. Valid values:
        # 
        # *   **true**: allows functions in the specified service to access the Internet.
        # *   **false**: does not allow functions to access the Internet.
        self.internet_access = internet_access
        # The log configuration. Function Compute writes function execution logs to the specified Logstore.
        self.log_config = log_config
        # The configurations of the NAS file system. The configurations allow functions to access the specified NAS resources.
        self.nas_config = nas_config
        # The OSS mount configurations.
        self.oss_mount_config = oss_mount_config
        # The RAM role that is used to grant required permissions to Function Compute. The RAM role is used in the following scenarios:
        # 
        # *   Sends function execution logs to your Logstore.
        # *   Generates a token for a function to access other cloud resources during function execution.
        self.role = role
        # The configurations of Tracing Analysis. After you configure Tracing Analysis for a service in Function Compute, you can record the execution duration of a request, view the amount of cold start time for a function, and record the execution duration of a function. For more information, see [Overview](~~189804~~).
        self.tracing_config = tracing_config
        # The virtual private cloud (VPC) configuration, which allows functions in the specified service in Function Compute to access the specified VPC.
        self.vpc_config = vpc_config

    def validate(self):
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
        if self.description is not None:
            result['description'] = self.description
        if self.internet_access is not None:
            result['internetAccess'] = self.internet_access
        if self.log_config is not None:
            result['logConfig'] = self.log_config.to_map()
        if self.nas_config is not None:
            result['nasConfig'] = self.nas_config.to_map()
        if self.oss_mount_config is not None:
            result['ossMountConfig'] = self.oss_mount_config.to_map()
        if self.role is not None:
            result['role'] = self.role
        if self.tracing_config is not None:
            result['tracingConfig'] = self.tracing_config.to_map()
        if self.vpc_config is not None:
            result['vpcConfig'] = self.vpc_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('internetAccess') is not None:
            self.internet_access = m.get('internetAccess')
        if m.get('logConfig') is not None:
            temp_model = LogConfig()
            self.log_config = temp_model.from_map(m['logConfig'])
        if m.get('nasConfig') is not None:
            temp_model = NASConfig()
            self.nas_config = temp_model.from_map(m['nasConfig'])
        if m.get('ossMountConfig') is not None:
            temp_model = OSSMountConfig()
            self.oss_mount_config = temp_model.from_map(m['ossMountConfig'])
        if m.get('role') is not None:
            self.role = m.get('role')
        if m.get('tracingConfig') is not None:
            temp_model = TracingConfig()
            self.tracing_config = temp_model.from_map(m['tracingConfig'])
        if m.get('vpcConfig') is not None:
            temp_model = VPCConfig()
            self.vpc_config = temp_model.from_map(m['vpcConfig'])
        return self


class UpdateServiceResponseBody(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        description: str = None,
        internet_access: bool = None,
        last_modified_time: str = None,
        log_config: LogConfig = None,
        nas_config: NASConfig = None,
        oss_mount_config: OSSMountConfig = None,
        role: str = None,
        service_id: str = None,
        service_name: str = None,
        tracing_config: TracingConfig = None,
        use_slrauthentication: bool = None,
        vpc_config: VPCConfig = None,
    ):
        # The time when the service was created.
        self.created_time = created_time
        # The description of the service.
        self.description = description
        # Specifies whether to allow functions to access the Internet. Valid values:
        # 
        # *   **true**: allows functions in the specified service to access the Internet.
        # *   **false**: does not allow functions to access the Internet.
        self.internet_access = internet_access
        # The time when the service was last modified.
        self.last_modified_time = last_modified_time
        # The log configuration, which specifies a Logstore to store function execution logs.
        self.log_config = log_config
        # The configurations of the NAS file system. The configuration allows functions in the specified service in Function Compute to access the NAS file system.
        self.nas_config = nas_config
        # The OSS mount configurations.
        self.oss_mount_config = oss_mount_config
        # The RAM role that is used to grant required permissions to Function Compute. The RAM role is used in the following scenarios:
        # 
        # *   Sends function execution logs to your Logstore.
        # *   Generates a token for a function to access other cloud resources during function execution.
        self.role = role
        # The unique ID generated by the system for the service.
        self.service_id = service_id
        # The name of the service.
        self.service_name = service_name
        # The configuration of Tracing Analysis. After you configure Tracing Analysis for a service in Function Compute, you can record the execution duration of a request, view the amount of cold start time for a function, and record the execution duration of a function. For more information, see [Overview](~~189804~~).
        self.tracing_config = tracing_config
        self.use_slrauthentication = use_slrauthentication
        # The VPC configuration. The configuration allows a function to access the specified VPC.
        self.vpc_config = vpc_config

    def validate(self):
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
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.description is not None:
            result['description'] = self.description
        if self.internet_access is not None:
            result['internetAccess'] = self.internet_access
        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time
        if self.log_config is not None:
            result['logConfig'] = self.log_config.to_map()
        if self.nas_config is not None:
            result['nasConfig'] = self.nas_config.to_map()
        if self.oss_mount_config is not None:
            result['ossMountConfig'] = self.oss_mount_config.to_map()
        if self.role is not None:
            result['role'] = self.role
        if self.service_id is not None:
            result['serviceId'] = self.service_id
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        if self.tracing_config is not None:
            result['tracingConfig'] = self.tracing_config.to_map()
        if self.use_slrauthentication is not None:
            result['useSLRAuthentication'] = self.use_slrauthentication
        if self.vpc_config is not None:
            result['vpcConfig'] = self.vpc_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('internetAccess') is not None:
            self.internet_access = m.get('internetAccess')
        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')
        if m.get('logConfig') is not None:
            temp_model = LogConfig()
            self.log_config = temp_model.from_map(m['logConfig'])
        if m.get('nasConfig') is not None:
            temp_model = NASConfig()
            self.nas_config = temp_model.from_map(m['nasConfig'])
        if m.get('ossMountConfig') is not None:
            temp_model = OSSMountConfig()
            self.oss_mount_config = temp_model.from_map(m['ossMountConfig'])
        if m.get('role') is not None:
            self.role = m.get('role')
        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        if m.get('tracingConfig') is not None:
            temp_model = TracingConfig()
            self.tracing_config = temp_model.from_map(m['tracingConfig'])
        if m.get('useSLRAuthentication') is not None:
            self.use_slrauthentication = m.get('useSLRAuthentication')
        if m.get('vpcConfig') is not None:
            temp_model = VPCConfig()
            self.vpc_config = temp_model.from_map(m['vpcConfig'])
        return self


class UpdateServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateServiceResponseBody = None,
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
            temp_model = UpdateServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTriggerHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        if_match: str = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        # This parameter is used to ensure that the modified resource is consistent with the resource to be modified. You can obtain the parameter value from the responses of [CreateTrigger](~~190054~~), [GetTrigger](~~190056~~), and [UpdateTrigger](~~190055~~) operations.
        self.if_match = if_match
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id
        # The time when the request is initiated on the client. The format of the value is: **EEE,d MMM yyyy HH:mm:ss GMT**.
        self.x_fc_date = x_fc_date
        # The custom request ID.
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.if_match is not None:
            result['If-Match'] = self.if_match
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('If-Match') is not None:
            self.if_match = m.get('If-Match')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class UpdateTriggerRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        invocation_role: str = None,
        qualifier: str = None,
        trigger_config: str = None,
    ):
        # The description of the trigger.
        self.description = description
        # The role that is used by the event source such as Object Storage Service (OSS) to invoke the function. For more information, see [Overview](~~53102~~).
        self.invocation_role = invocation_role
        # The version or alias of the service.
        self.qualifier = qualifier
        # The configurations of the trigger. The configurations vary based on the trigger type. For more information about the format, see the following topics:
        # 
        # *   Object Storage Service (OSS) trigger: [OSSTriggerConfig](~~415697~~).
        # *   Simple Log Service trigger: [LogTriggerConfig](~~415694~~).
        # *   Time trigger: [TimeTriggerConfig](~~415712~~).
        # *   HTTP trigger: [HTTPTriggerConfig](~~415685~~).
        # *   Tablestore trigger: Specify the **SourceArn** parameter and leave this parameter empty.
        # *   Alibaba Cloud CDN event trigger: [CDNEventsTriggerConfig](~~415674~~).
        # *   MNS topic trigger: [MnsTopicTriggerConfig](~~415695~~).
        # *   EventBridge triggers: [EventBridgeTriggerConfig](~~2508622~~).
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


class UpdateTriggerResponseBody(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        description: str = None,
        domain_name: str = None,
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
        url_internet: str = None,
        url_intranet: str = None,
    ):
        # The time when the audio or video file was created.
        self.created_time = created_time
        # The description of the trigger.
        self.description = description
        # The domain name used to invoke the function by using HTTP. You can add this domain name as the prefix to the endpoint of Function Compute. This way, you can invoke the function that corresponds to the trigger by using HTTP. For example, `{domainName}.cn-shanghai.fc.aliyuncs.com`.
        self.domain_name = domain_name
        # The ARN of the RAM role that is used by the event source to invoke the function.
        self.invocation_role = invocation_role
        # The last modification time.
        self.last_modified_time = last_modified_time
        # The version or alias of the service.
        self.qualifier = qualifier
        # The ARN of the event source.
        self.source_arn = source_arn
        self.status = status
        self.target_arn = target_arn
        # The configurations of the trigger. The configurations vary based on the trigger type.
        self.trigger_config = trigger_config
        # The unique ID of the trigger.
        self.trigger_id = trigger_id
        # The name of the trigger.
        self.trigger_name = trigger_name
        # The trigger type. Example values: **oss**, **log**, **tablestore**, **timer**, **http**, **cdn_events**, **mns_topic**, and **eventbridge**.
        self.trigger_type = trigger_type
        # The public domain address. You can access HTTP triggers over the Internet by using HTTP or HTTPS.
        self.url_internet = url_internet
        # The private endpoint. In a VPC, you can access HTTP triggers by using HTTP or HTTPS.
        self.url_intranet = url_intranet

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
        if self.domain_name is not None:
            result['domainName'] = self.domain_name
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
        if self.url_internet is not None:
            result['urlInternet'] = self.url_internet
        if self.url_intranet is not None:
            result['urlIntranet'] = self.url_intranet
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domainName') is not None:
            self.domain_name = m.get('domainName')
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
        if m.get('urlInternet') is not None:
            self.url_internet = m.get('urlInternet')
        if m.get('urlIntranet') is not None:
            self.url_intranet = m.get('urlIntranet')
        return self


class UpdateTriggerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateTriggerResponseBody = None,
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
            temp_model = UpdateTriggerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


