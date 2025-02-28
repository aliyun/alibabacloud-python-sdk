# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class Detail(TeaModel):
    def __init__(
        self,
        app_conf: str = None,
        dbcluster_id: str = None,
        estimate_execution_cpu_time_in_seconds: int = None,
        last_attempt_id: str = None,
        last_updated_time_in_millis: int = None,
        log_root_path: str = None,
        resource_group_name: str = None,
        started_time_in_millis: int = None,
        submitted_time_in_millis: int = None,
        terminated_time_in_millis: int = None,
        web_ui_address: str = None,
    ):
        self.app_conf = app_conf
        self.dbcluster_id = dbcluster_id
        self.estimate_execution_cpu_time_in_seconds = estimate_execution_cpu_time_in_seconds
        self.last_attempt_id = last_attempt_id
        self.last_updated_time_in_millis = last_updated_time_in_millis
        self.log_root_path = log_root_path
        self.resource_group_name = resource_group_name
        self.started_time_in_millis = started_time_in_millis
        self.submitted_time_in_millis = submitted_time_in_millis
        self.terminated_time_in_millis = terminated_time_in_millis
        self.web_ui_address = web_ui_address

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_conf is not None:
            result['AppConf'] = self.app_conf
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.estimate_execution_cpu_time_in_seconds is not None:
            result['EstimateExecutionCpuTimeInSeconds'] = self.estimate_execution_cpu_time_in_seconds
        if self.last_attempt_id is not None:
            result['LastAttemptId'] = self.last_attempt_id
        if self.last_updated_time_in_millis is not None:
            result['LastUpdatedTimeInMillis'] = self.last_updated_time_in_millis
        if self.log_root_path is not None:
            result['LogRootPath'] = self.log_root_path
        if self.resource_group_name is not None:
            result['ResourceGroupName'] = self.resource_group_name
        if self.started_time_in_millis is not None:
            result['StartedTimeInMillis'] = self.started_time_in_millis
        if self.submitted_time_in_millis is not None:
            result['SubmittedTimeInMillis'] = self.submitted_time_in_millis
        if self.terminated_time_in_millis is not None:
            result['TerminatedTimeInMillis'] = self.terminated_time_in_millis
        if self.web_ui_address is not None:
            result['WebUiAddress'] = self.web_ui_address
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppConf') is not None:
            self.app_conf = m.get('AppConf')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('EstimateExecutionCpuTimeInSeconds') is not None:
            self.estimate_execution_cpu_time_in_seconds = m.get('EstimateExecutionCpuTimeInSeconds')
        if m.get('LastAttemptId') is not None:
            self.last_attempt_id = m.get('LastAttemptId')
        if m.get('LastUpdatedTimeInMillis') is not None:
            self.last_updated_time_in_millis = m.get('LastUpdatedTimeInMillis')
        if m.get('LogRootPath') is not None:
            self.log_root_path = m.get('LogRootPath')
        if m.get('ResourceGroupName') is not None:
            self.resource_group_name = m.get('ResourceGroupName')
        if m.get('StartedTimeInMillis') is not None:
            self.started_time_in_millis = m.get('StartedTimeInMillis')
        if m.get('SubmittedTimeInMillis') is not None:
            self.submitted_time_in_millis = m.get('SubmittedTimeInMillis')
        if m.get('TerminatedTimeInMillis') is not None:
            self.terminated_time_in_millis = m.get('TerminatedTimeInMillis')
        if m.get('WebUiAddress') is not None:
            self.web_ui_address = m.get('WebUiAddress')
        return self


class SparkAppInfo(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        detail: Detail = None,
        message: str = None,
        state: str = None,
    ):
        self.app_id = app_id
        self.app_name = app_name
        self.detail = detail
        self.message = message
        self.state = state

    def validate(self):
        if self.detail:
            self.detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.detail is not None:
            result['Detail'] = self.detail.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Detail') is not None:
            temp_model = Detail()
            self.detail = temp_model.from_map(m['Detail'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class AllocateClusterVpcConnectionRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        engine: str = None,
        ins_type: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        self.engine = engine
        self.ins_type = ins_type
        self.v_switch_id = v_switch_id
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.ins_type is not None:
            result['InsType'] = self.ins_type
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('InsType') is not None:
            self.ins_type = m.get('InsType')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class AllocateClusterVpcConnectionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AllocateClusterVpcConnectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AllocateClusterVpcConnectionResponseBody = None,
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
            temp_model = AllocateClusterVpcConnectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AuthorizeInstanceEgressRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        endpoint_id: str = None,
        ins_type: str = None,
    ):
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # This parameter is required.
        self.endpoint_id = endpoint_id
        # This parameter is required.
        self.ins_type = ins_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        if self.ins_type is not None:
            result['InsType'] = self.ins_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        if m.get('InsType') is not None:
            self.ins_type = m.get('InsType')
        return self


class AuthorizeInstanceEgressResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AuthorizeInstanceEgressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AuthorizeInstanceEgressResponseBody = None,
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
            temp_model = AuthorizeInstanceEgressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckOssObjectContentConsistencyRequest(TeaModel):
    def __init__(
        self,
        ak: str = None,
        encrypted_sk: str = None,
        prefix: str = None,
        region_id: str = None,
        source_bucket_name: str = None,
        source_db_cluster_id: str = None,
        source_endpoint: str = None,
        source_region_id: str = None,
        target_bucket_name: str = None,
        target_endpoint: str = None,
    ):
        self.ak = ak
        self.encrypted_sk = encrypted_sk
        self.prefix = prefix
        self.region_id = region_id
        self.source_bucket_name = source_bucket_name
        self.source_db_cluster_id = source_db_cluster_id
        self.source_endpoint = source_endpoint
        self.source_region_id = source_region_id
        self.target_bucket_name = target_bucket_name
        self.target_endpoint = target_endpoint

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ak is not None:
            result['Ak'] = self.ak
        if self.encrypted_sk is not None:
            result['EncryptedSk'] = self.encrypted_sk
        if self.prefix is not None:
            result['Prefix'] = self.prefix
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.source_bucket_name is not None:
            result['SourceBucketName'] = self.source_bucket_name
        if self.source_db_cluster_id is not None:
            result['SourceDbClusterId'] = self.source_db_cluster_id
        if self.source_endpoint is not None:
            result['SourceEndpoint'] = self.source_endpoint
        if self.source_region_id is not None:
            result['SourceRegionId'] = self.source_region_id
        if self.target_bucket_name is not None:
            result['TargetBucketName'] = self.target_bucket_name
        if self.target_endpoint is not None:
            result['TargetEndpoint'] = self.target_endpoint
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ak') is not None:
            self.ak = m.get('Ak')
        if m.get('EncryptedSk') is not None:
            self.encrypted_sk = m.get('EncryptedSk')
        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SourceBucketName') is not None:
            self.source_bucket_name = m.get('SourceBucketName')
        if m.get('SourceDbClusterId') is not None:
            self.source_db_cluster_id = m.get('SourceDbClusterId')
        if m.get('SourceEndpoint') is not None:
            self.source_endpoint = m.get('SourceEndpoint')
        if m.get('SourceRegionId') is not None:
            self.source_region_id = m.get('SourceRegionId')
        if m.get('TargetBucketName') is not None:
            self.target_bucket_name = m.get('TargetBucketName')
        if m.get('TargetEndpoint') is not None:
            self.target_endpoint = m.get('TargetEndpoint')
        return self


class CheckOssObjectContentConsistencyResponseBody(TeaModel):
    def __init__(
        self,
        is_consistent: bool = None,
        request_id: str = None,
        http_status_code: int = None,
        message: str = None,
        result_code: str = None,
        success: bool = None,
    ):
        self.is_consistent = is_consistent
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.message = message
        self.result_code = result_code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_consistent is not None:
            result['IsConsistent'] = self.is_consistent
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.result_code is not None:
            result['resultCode'] = self.result_code
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsConsistent') is not None:
            self.is_consistent = m.get('IsConsistent')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('resultCode') is not None:
            self.result_code = m.get('resultCode')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class CheckOssObjectContentConsistencyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckOssObjectContentConsistencyResponseBody = None,
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
            temp_model = CheckOssObjectContentConsistencyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateMajorCustomerRequest(TeaModel):
    def __init__(
        self,
        area: str = None,
        customer_id: int = None,
        customer_name: str = None,
        description: str = None,
        industry: str = None,
        pd: str = None,
        pdsa: str = None,
        ranking: int = None,
        rd: str = None,
        sa: str = None,
    ):
        self.area = area
        # This parameter is required.
        self.customer_id = customer_id
        # This parameter is required.
        self.customer_name = customer_name
        self.description = description
        self.industry = industry
        self.pd = pd
        self.pdsa = pdsa
        self.ranking = ranking
        self.rd = rd
        self.sa = sa

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.area is not None:
            result['Area'] = self.area
        if self.customer_id is not None:
            result['CustomerId'] = self.customer_id
        if self.customer_name is not None:
            result['CustomerName'] = self.customer_name
        if self.description is not None:
            result['Description'] = self.description
        if self.industry is not None:
            result['Industry'] = self.industry
        if self.pd is not None:
            result['Pd'] = self.pd
        if self.pdsa is not None:
            result['Pdsa'] = self.pdsa
        if self.ranking is not None:
            result['Ranking'] = self.ranking
        if self.rd is not None:
            result['Rd'] = self.rd
        if self.sa is not None:
            result['Sa'] = self.sa
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Area') is not None:
            self.area = m.get('Area')
        if m.get('CustomerId') is not None:
            self.customer_id = m.get('CustomerId')
        if m.get('CustomerName') is not None:
            self.customer_name = m.get('CustomerName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Industry') is not None:
            self.industry = m.get('Industry')
        if m.get('Pd') is not None:
            self.pd = m.get('Pd')
        if m.get('Pdsa') is not None:
            self.pdsa = m.get('Pdsa')
        if m.get('Ranking') is not None:
            self.ranking = m.get('Ranking')
        if m.get('Rd') is not None:
            self.rd = m.get('Rd')
        if m.get('Sa') is not None:
            self.sa = m.get('Sa')
        return self


class CreateMajorCustomerResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateMajorCustomerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateMajorCustomerResponseBody = None,
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
            temp_model = CreateMajorCustomerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteBucketReplicationRequest(TeaModel):
    def __init__(
        self,
        ak: str = None,
        encrypted_sk: str = None,
        endpoint: str = None,
        region_id: str = None,
        rule_id: str = None,
        source_bucket_name: str = None,
    ):
        self.ak = ak
        self.encrypted_sk = encrypted_sk
        self.endpoint = endpoint
        self.region_id = region_id
        self.rule_id = rule_id
        self.source_bucket_name = source_bucket_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ak is not None:
            result['Ak'] = self.ak
        if self.encrypted_sk is not None:
            result['EncryptedSk'] = self.encrypted_sk
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.source_bucket_name is not None:
            result['SourceBucketName'] = self.source_bucket_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ak') is not None:
            self.ak = m.get('Ak')
        if m.get('EncryptedSk') is not None:
            self.encrypted_sk = m.get('EncryptedSk')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('SourceBucketName') is not None:
            self.source_bucket_name = m.get('SourceBucketName')
        return self


class DeleteBucketReplicationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        http_status_code: int = None,
        message: str = None,
        result_code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.message = message
        self.result_code = result_code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.result_code is not None:
            result['resultCode'] = self.result_code
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('resultCode') is not None:
            self.result_code = m.get('resultCode')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class DeleteBucketReplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteBucketReplicationResponseBody = None,
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
            temp_model = DeleteBucketReplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDBClusterRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        force: bool = None,
    ):
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        self.force = force

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.force is not None:
            result['Force'] = self.force
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('Force') is not None:
            self.force = m.get('Force')
        return self


class DeleteDBClusterResponseBody(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        request_id: str = None,
        task_id: int = None,
    ):
        self.dbcluster_id = dbcluster_id
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DeleteDBClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDBClusterResponseBody = None,
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
            temp_model = DeleteDBClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteMajorCustomerRequest(TeaModel):
    def __init__(
        self,
        customer_id: int = None,
    ):
        # This parameter is required.
        self.customer_id = customer_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.customer_id is not None:
            result['CustomerId'] = self.customer_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomerId') is not None:
            self.customer_id = m.get('CustomerId')
        return self


class DeleteMajorCustomerResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteMajorCustomerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteMajorCustomerResponseBody = None,
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
            temp_model = DeleteMajorCustomerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAccountsRequest(TeaModel):
    def __init__(
        self,
        account_name: str = None,
        dbcluster_id: str = None,
        engine: str = None,
        owner_id: str = None,
    ):
        self.account_name = account_name
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        self.engine = engine
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeAccountsResponseBodyAccountListDBAccount(TeaModel):
    def __init__(
        self,
        account_description: str = None,
        account_name: str = None,
        account_status: str = None,
        account_type: str = None,
        engine: str = None,
        ram_users: str = None,
    ):
        self.account_description = account_description
        self.account_name = account_name
        self.account_status = account_status
        self.account_type = account_type
        self.engine = engine
        self.ram_users = ram_users

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_description is not None:
            result['AccountDescription'] = self.account_description
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.account_status is not None:
            result['AccountStatus'] = self.account_status
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.ram_users is not None:
            result['RamUsers'] = self.ram_users
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountDescription') is not None:
            self.account_description = m.get('AccountDescription')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountStatus') is not None:
            self.account_status = m.get('AccountStatus')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('RamUsers') is not None:
            self.ram_users = m.get('RamUsers')
        return self


class DescribeAccountsResponseBodyAccountList(TeaModel):
    def __init__(
        self,
        dbaccount: List[DescribeAccountsResponseBodyAccountListDBAccount] = None,
    ):
        self.dbaccount = dbaccount

    def validate(self):
        if self.dbaccount:
            for k in self.dbaccount:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DBAccount'] = []
        if self.dbaccount is not None:
            for k in self.dbaccount:
                result['DBAccount'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dbaccount = []
        if m.get('DBAccount') is not None:
            for k in m.get('DBAccount'):
                temp_model = DescribeAccountsResponseBodyAccountListDBAccount()
                self.dbaccount.append(temp_model.from_map(k))
        return self


class DescribeAccountsResponseBody(TeaModel):
    def __init__(
        self,
        account_list: DescribeAccountsResponseBodyAccountList = None,
        request_id: str = None,
    ):
        self.account_list = account_list
        self.request_id = request_id

    def validate(self):
        if self.account_list:
            self.account_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_list is not None:
            result['AccountList'] = self.account_list.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountList') is not None:
            temp_model = DescribeAccountsResponseBodyAccountList()
            self.account_list = temp_model.from_map(m['AccountList'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeAccountsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAccountsResponseBody = None,
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
            temp_model = DescribeAccountsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAdbDutyRuleRequest(TeaModel):
    def __init__(
        self,
        rule_ids: str = None,
    ):
        self.rule_ids = rule_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_ids is not None:
            result['RuleIds'] = self.rule_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleIds') is not None:
            self.rule_ids = m.get('RuleIds')
        return self


class DescribeAdbDutyRuleResponseBodyItemsCurrentDutyStaff(TeaModel):
    def __init__(
        self,
        nick_name: str = None,
        worker_no: str = None,
    ):
        self.nick_name = nick_name
        self.worker_no = worker_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.nick_name is not None:
            result['NickName'] = self.nick_name
        if self.worker_no is not None:
            result['WorkerNo'] = self.worker_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')
        if m.get('WorkerNo') is not None:
            self.worker_no = m.get('WorkerNo')
        return self


class DescribeAdbDutyRuleResponseBodyItems(TeaModel):
    def __init__(
        self,
        current_duty_staff: List[DescribeAdbDutyRuleResponseBodyItemsCurrentDutyStaff] = None,
        rule_code: str = None,
        rule_id: str = None,
    ):
        self.current_duty_staff = current_duty_staff
        self.rule_code = rule_code
        self.rule_id = rule_id

    def validate(self):
        if self.current_duty_staff:
            for k in self.current_duty_staff:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CurrentDutyStaff'] = []
        if self.current_duty_staff is not None:
            for k in self.current_duty_staff:
                result['CurrentDutyStaff'].append(k.to_map() if k else None)
        if self.rule_code is not None:
            result['RuleCode'] = self.rule_code
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.current_duty_staff = []
        if m.get('CurrentDutyStaff') is not None:
            for k in m.get('CurrentDutyStaff'):
                temp_model = DescribeAdbDutyRuleResponseBodyItemsCurrentDutyStaff()
                self.current_duty_staff.append(temp_model.from_map(k))
        if m.get('RuleCode') is not None:
            self.rule_code = m.get('RuleCode')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class DescribeAdbDutyRuleResponseBody(TeaModel):
    def __init__(
        self,
        items: List[DescribeAdbDutyRuleResponseBodyItems] = None,
        request_id: str = None,
    ):
        self.items = items
        self.request_id = request_id

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeAdbDutyRuleResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeAdbDutyRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAdbDutyRuleResponseBody = None,
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
            temp_model = DescribeAdbDutyRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBackupPolicyRequest(TeaModel):
    def __init__(
        self,
        aliuid: int = None,
        dbcluster_id: str = None,
        region_id: str = None,
    ):
        self.aliuid = aliuid
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliuid is not None:
            result['Aliuid'] = self.aliuid
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.region_id is not None:
            result['regionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Aliuid') is not None:
            self.aliuid = m.get('Aliuid')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        return self


class DescribeBackupPolicyResponseBodyBackupPolicy(TeaModel):
    def __init__(
        self,
        backup_location_full: str = None,
        backup_location_log: str = None,
        backup_retention_period: int = None,
        cluster_id: int = None,
        enable_backup_log: bool = None,
        log_backup_retention_period: int = None,
        preferred_backup_period: str = None,
        preferred_backup_time: str = None,
    ):
        self.backup_location_full = backup_location_full
        self.backup_location_log = backup_location_log
        self.backup_retention_period = backup_retention_period
        self.cluster_id = cluster_id
        self.enable_backup_log = enable_backup_log
        self.log_backup_retention_period = log_backup_retention_period
        self.preferred_backup_period = preferred_backup_period
        self.preferred_backup_time = preferred_backup_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_location_full is not None:
            result['BackupLocationFull'] = self.backup_location_full
        if self.backup_location_log is not None:
            result['BackupLocationLog'] = self.backup_location_log
        if self.backup_retention_period is not None:
            result['BackupRetentionPeriod'] = self.backup_retention_period
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.enable_backup_log is not None:
            result['EnableBackupLog'] = self.enable_backup_log
        if self.log_backup_retention_period is not None:
            result['LogBackupRetentionPeriod'] = self.log_backup_retention_period
        if self.preferred_backup_period is not None:
            result['PreferredBackupPeriod'] = self.preferred_backup_period
        if self.preferred_backup_time is not None:
            result['PreferredBackupTime'] = self.preferred_backup_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupLocationFull') is not None:
            self.backup_location_full = m.get('BackupLocationFull')
        if m.get('BackupLocationLog') is not None:
            self.backup_location_log = m.get('BackupLocationLog')
        if m.get('BackupRetentionPeriod') is not None:
            self.backup_retention_period = m.get('BackupRetentionPeriod')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('EnableBackupLog') is not None:
            self.enable_backup_log = m.get('EnableBackupLog')
        if m.get('LogBackupRetentionPeriod') is not None:
            self.log_backup_retention_period = m.get('LogBackupRetentionPeriod')
        if m.get('PreferredBackupPeriod') is not None:
            self.preferred_backup_period = m.get('PreferredBackupPeriod')
        if m.get('PreferredBackupTime') is not None:
            self.preferred_backup_time = m.get('PreferredBackupTime')
        return self


class DescribeBackupPolicyResponseBody(TeaModel):
    def __init__(
        self,
        backup_policy: DescribeBackupPolicyResponseBodyBackupPolicy = None,
        request_id: str = None,
        http_status_code: int = None,
        message: str = None,
        result_code: str = None,
        success: bool = None,
    ):
        self.backup_policy = backup_policy
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.message = message
        self.result_code = result_code
        self.success = success

    def validate(self):
        if self.backup_policy:
            self.backup_policy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_policy is not None:
            result['BackupPolicy'] = self.backup_policy.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.result_code is not None:
            result['resultCode'] = self.result_code
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupPolicy') is not None:
            temp_model = DescribeBackupPolicyResponseBodyBackupPolicy()
            self.backup_policy = temp_model.from_map(m['BackupPolicy'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('resultCode') is not None:
            self.result_code = m.get('resultCode')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class DescribeBackupPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeBackupPolicyResponseBody = None,
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
            temp_model = DescribeBackupPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBackupsRequest(TeaModel):
    def __init__(
        self,
        ali_uid: str = None,
        backup_id: str = None,
        dbcluster_id: str = None,
        end_time: str = None,
        page_number: int = None,
        page_size: int = None,
        start_time: str = None,
        region_id: str = None,
    ):
        self.ali_uid = ali_uid
        self.backup_id = backup_id
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # This parameter is required.
        self.end_time = end_time
        self.page_number = page_number
        self.page_size = page_size
        # This parameter is required.
        self.start_time = start_time
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.backup_id is not None:
            result['BackupID'] = self.backup_id
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.region_id is not None:
            result['regionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('BackupID') is not None:
            self.backup_id = m.get('BackupID')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        return self


class DescribeBackupsResponseBodyBackupsList(TeaModel):
    def __init__(
        self,
        backup_end_time: str = None,
        backup_id: int = None,
        backup_method: str = None,
        backup_set_info: str = None,
        backup_size: int = None,
        backup_start_time: str = None,
        backup_type: str = None,
        db_cluster_id: str = None,
        policy_id: int = None,
    ):
        self.backup_end_time = backup_end_time
        self.backup_id = backup_id
        self.backup_method = backup_method
        self.backup_set_info = backup_set_info
        self.backup_size = backup_size
        self.backup_start_time = backup_start_time
        self.backup_type = backup_type
        self.db_cluster_id = db_cluster_id
        self.policy_id = policy_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_end_time is not None:
            result['BackupEndTime'] = self.backup_end_time
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
        if self.backup_method is not None:
            result['BackupMethod'] = self.backup_method
        if self.backup_set_info is not None:
            result['BackupSetInfo'] = self.backup_set_info
        if self.backup_size is not None:
            result['BackupSize'] = self.backup_size
        if self.backup_start_time is not None:
            result['BackupStartTime'] = self.backup_start_time
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type
        if self.db_cluster_id is not None:
            result['DbClusterId'] = self.db_cluster_id
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupEndTime') is not None:
            self.backup_end_time = m.get('BackupEndTime')
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        if m.get('BackupMethod') is not None:
            self.backup_method = m.get('BackupMethod')
        if m.get('BackupSetInfo') is not None:
            self.backup_set_info = m.get('BackupSetInfo')
        if m.get('BackupSize') is not None:
            self.backup_size = m.get('BackupSize')
        if m.get('BackupStartTime') is not None:
            self.backup_start_time = m.get('BackupStartTime')
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')
        if m.get('DbClusterId') is not None:
            self.db_cluster_id = m.get('DbClusterId')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        return self


class DescribeBackupsResponseBody(TeaModel):
    def __init__(
        self,
        backups_list: List[DescribeBackupsResponseBodyBackupsList] = None,
        http_status_code: int = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.backups_list = backups_list
        self.http_status_code = http_status_code
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.backups_list:
            for k in self.backups_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BackupsList'] = []
        if self.backups_list is not None:
            for k in self.backups_list:
                result['BackupsList'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.backups_list = []
        if m.get('BackupsList') is not None:
            for k in m.get('BackupsList'):
                temp_model = DescribeBackupsResponseBodyBackupsList()
                self.backups_list.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeBackupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeBackupsResponseBody = None,
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
            temp_model = DescribeBackupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeClusterInstanceRequest(TeaModel):
    def __init__(
        self,
        db_cluster_id: str = None,
        ins_type: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.db_cluster_id = db_cluster_id
        self.ins_type = ins_type
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_cluster_id is not None:
            result['DbClusterId'] = self.db_cluster_id
        if self.ins_type is not None:
            result['InsType'] = self.ins_type
        if self.region_id is not None:
            result['regionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbClusterId') is not None:
            self.db_cluster_id = m.get('DbClusterId')
        if m.get('InsType') is not None:
            self.ins_type = m.get('InsType')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        return self


class DescribeClusterInstanceResponseBodyClusterInstance(TeaModel):
    def __init__(
        self,
        cluster_id: int = None,
        cluster_id_str: str = None,
        db_cluster_id: str = None,
        instance_id: int = None,
        instance_id_str: str = None,
        instance_name: str = None,
        k_8s_service_account: str = None,
        namespace: str = None,
        parent_id: int = None,
        replica_id_list: List[int] = None,
        replica_id_str_list: List[str] = None,
        replicas: int = None,
        state: str = None,
        version: str = None,
        instance_type: str = None,
    ):
        self.cluster_id = cluster_id
        self.cluster_id_str = cluster_id_str
        self.db_cluster_id = db_cluster_id
        self.instance_id = instance_id
        self.instance_id_str = instance_id_str
        self.instance_name = instance_name
        self.k_8s_service_account = k_8s_service_account
        self.namespace = namespace
        self.parent_id = parent_id
        self.replica_id_list = replica_id_list
        self.replica_id_str_list = replica_id_str_list
        self.replicas = replicas
        self.state = state
        self.version = version
        self.instance_type = instance_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_id_str is not None:
            result['ClusterIdStr'] = self.cluster_id_str
        if self.db_cluster_id is not None:
            result['DbClusterId'] = self.db_cluster_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_id_str is not None:
            result['InstanceIdStr'] = self.instance_id_str
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.k_8s_service_account is not None:
            result['K8sServiceAccount'] = self.k_8s_service_account
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.replica_id_list is not None:
            result['ReplicaIdList'] = self.replica_id_list
        if self.replica_id_str_list is not None:
            result['ReplicaIdStrList'] = self.replica_id_str_list
        if self.replicas is not None:
            result['Replicas'] = self.replicas
        if self.state is not None:
            result['State'] = self.state
        if self.version is not None:
            result['Version'] = self.version
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterIdStr') is not None:
            self.cluster_id_str = m.get('ClusterIdStr')
        if m.get('DbClusterId') is not None:
            self.db_cluster_id = m.get('DbClusterId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceIdStr') is not None:
            self.instance_id_str = m.get('InstanceIdStr')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('K8sServiceAccount') is not None:
            self.k_8s_service_account = m.get('K8sServiceAccount')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('ReplicaIdList') is not None:
            self.replica_id_list = m.get('ReplicaIdList')
        if m.get('ReplicaIdStrList') is not None:
            self.replica_id_str_list = m.get('ReplicaIdStrList')
        if m.get('Replicas') is not None:
            self.replicas = m.get('Replicas')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        return self


class DescribeClusterInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        cluster_instance: DescribeClusterInstanceResponseBodyClusterInstance = None,
        http_status_code: int = None,
        message: str = None,
        result_code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.cluster_instance = cluster_instance
        self.http_status_code = http_status_code
        self.message = message
        self.result_code = result_code
        self.success = success

    def validate(self):
        if self.cluster_instance:
            self.cluster_instance.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.cluster_instance is not None:
            result['clusterInstance'] = self.cluster_instance.to_map()
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.result_code is not None:
            result['resultCode'] = self.result_code
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('clusterInstance') is not None:
            temp_model = DescribeClusterInstanceResponseBodyClusterInstance()
            self.cluster_instance = temp_model.from_map(m['clusterInstance'])
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('resultCode') is not None:
            self.result_code = m.get('resultCode')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class DescribeClusterInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeClusterInstanceResponseBody = None,
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
            temp_model = DescribeClusterInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeClusterNetInfoRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        engine: str = None,
        ins_type: str = None,
    ):
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        self.engine = engine
        self.ins_type = ins_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.ins_type is not None:
            result['InsType'] = self.ins_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('InsType') is not None:
            self.ins_type = m.get('InsType')
        return self


class DescribeClusterNetInfoResponseBodyItemsAddressPortsPorts(TeaModel):
    def __init__(
        self,
        port: str = None,
        protocol: str = None,
    ):
        self.port = port
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.port is not None:
            result['Port'] = self.port
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        return self


class DescribeClusterNetInfoResponseBodyItemsAddressPorts(TeaModel):
    def __init__(
        self,
        ports: List[DescribeClusterNetInfoResponseBodyItemsAddressPortsPorts] = None,
    ):
        self.ports = ports

    def validate(self):
        if self.ports:
            for k in self.ports:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ports'] = []
        if self.ports is not None:
            for k in self.ports:
                result['ports'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ports = []
        if m.get('ports') is not None:
            for k in m.get('ports'):
                temp_model = DescribeClusterNetInfoResponseBodyItemsAddressPortsPorts()
                self.ports.append(temp_model.from_map(k))
        return self


class DescribeClusterNetInfoResponseBodyItemsAddress(TeaModel):
    def __init__(
        self,
        connection_string: str = None,
        connection_string_prefix: str = None,
        ipaddress: str = None,
        net_type: str = None,
        port: str = None,
        ports: DescribeClusterNetInfoResponseBodyItemsAddressPorts = None,
        vpcid: str = None,
        v_switch_id: str = None,
    ):
        self.connection_string = connection_string
        self.connection_string_prefix = connection_string_prefix
        self.ipaddress = ipaddress
        self.net_type = net_type
        self.port = port
        self.ports = ports
        self.vpcid = vpcid
        self.v_switch_id = v_switch_id

    def validate(self):
        if self.ports:
            self.ports.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
        if self.connection_string_prefix is not None:
            result['ConnectionStringPrefix'] = self.connection_string_prefix
        if self.ipaddress is not None:
            result['IPAddress'] = self.ipaddress
        if self.net_type is not None:
            result['NetType'] = self.net_type
        if self.port is not None:
            result['Port'] = self.port
        if self.ports is not None:
            result['Ports'] = self.ports.to_map()
        if self.vpcid is not None:
            result['VPCId'] = self.vpcid
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
        if m.get('ConnectionStringPrefix') is not None:
            self.connection_string_prefix = m.get('ConnectionStringPrefix')
        if m.get('IPAddress') is not None:
            self.ipaddress = m.get('IPAddress')
        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Ports') is not None:
            temp_model = DescribeClusterNetInfoResponseBodyItemsAddressPorts()
            self.ports = temp_model.from_map(m['Ports'])
        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        return self


class DescribeClusterNetInfoResponseBodyItems(TeaModel):
    def __init__(
        self,
        address: List[DescribeClusterNetInfoResponseBodyItemsAddress] = None,
    ):
        self.address = address

    def validate(self):
        if self.address:
            for k in self.address:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Address'] = []
        if self.address is not None:
            for k in self.address:
                result['Address'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.address = []
        if m.get('Address') is not None:
            for k in m.get('Address'):
                temp_model = DescribeClusterNetInfoResponseBodyItemsAddress()
                self.address.append(temp_model.from_map(k))
        return self


class DescribeClusterNetInfoResponseBody(TeaModel):
    def __init__(
        self,
        cluster_network_type: str = None,
        items: DescribeClusterNetInfoResponseBodyItems = None,
        request_id: str = None,
    ):
        self.cluster_network_type = cluster_network_type
        self.items = items
        self.request_id = request_id

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_network_type is not None:
            result['ClusterNetworkType'] = self.cluster_network_type
        if self.items is not None:
            result['Items'] = self.items.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterNetworkType') is not None:
            self.cluster_network_type = m.get('ClusterNetworkType')
        if m.get('Items') is not None:
            temp_model = DescribeClusterNetInfoResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeClusterNetInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeClusterNetInfoResponseBody = None,
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
            temp_model = DescribeClusterNetInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCustomersRequest(TeaModel):
    def __init__(
        self,
        user_ids: str = None,
    ):
        # This parameter is required.
        self.user_ids = user_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_ids is not None:
            result['UserIds'] = self.user_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserIds') is not None:
            self.user_ids = m.get('UserIds')
        return self


class DescribeCustomersResponseBodyCustomers(TeaModel):
    def __init__(
        self,
        customer_id: str = None,
        customer_name: str = None,
        gc_level: str = None,
        is_major: int = None,
        user_id: str = None,
        user_name: str = None,
    ):
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.gc_level = gc_level
        self.is_major = is_major
        self.user_id = user_id
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.customer_id is not None:
            result['CustomerId'] = self.customer_id
        if self.customer_name is not None:
            result['CustomerName'] = self.customer_name
        if self.gc_level is not None:
            result['GcLevel'] = self.gc_level
        if self.is_major is not None:
            result['IsMajor'] = self.is_major
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomerId') is not None:
            self.customer_id = m.get('CustomerId')
        if m.get('CustomerName') is not None:
            self.customer_name = m.get('CustomerName')
        if m.get('GcLevel') is not None:
            self.gc_level = m.get('GcLevel')
        if m.get('IsMajor') is not None:
            self.is_major = m.get('IsMajor')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class DescribeCustomersResponseBody(TeaModel):
    def __init__(
        self,
        customers: List[DescribeCustomersResponseBodyCustomers] = None,
        request_id: str = None,
    ):
        self.customers = customers
        self.request_id = request_id

    def validate(self):
        if self.customers:
            for k in self.customers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Customers'] = []
        if self.customers is not None:
            for k in self.customers:
                result['Customers'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.customers = []
        if m.get('Customers') is not None:
            for k in m.get('Customers'):
                temp_model = DescribeCustomersResponseBodyCustomers()
                self.customers.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeCustomersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCustomersResponseBody = None,
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
            temp_model = DescribeCustomersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBClusterPerformanceRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        end_time: str = None,
        key: str = None,
        region_id: str = None,
        resource_pools: str = None,
        start_time: str = None,
    ):
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        self.end_time = end_time
        self.key = key
        # This parameter is required.
        self.region_id = region_id
        self.resource_pools = resource_pools
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.key is not None:
            result['Key'] = self.key
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_pools is not None:
            result['ResourcePools'] = self.resource_pools
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourcePools') is not None:
            self.resource_pools = m.get('ResourcePools')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDBClusterPerformanceResponseBodyPerformancesSeries(TeaModel):
    def __init__(
        self,
        name: str = None,
        tags: str = None,
        values: List[str] = None,
    ):
        self.name = name
        self.tags = tags
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class DescribeDBClusterPerformanceResponseBodyPerformances(TeaModel):
    def __init__(
        self,
        key: str = None,
        series: List[DescribeDBClusterPerformanceResponseBodyPerformancesSeries] = None,
        unit: str = None,
    ):
        self.key = key
        self.series = series
        self.unit = unit

    def validate(self):
        if self.series:
            for k in self.series:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        result['Series'] = []
        if self.series is not None:
            for k in self.series:
                result['Series'].append(k.to_map() if k else None)
        if self.unit is not None:
            result['Unit'] = self.unit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        self.series = []
        if m.get('Series') is not None:
            for k in m.get('Series'):
                temp_model = DescribeDBClusterPerformanceResponseBodyPerformancesSeries()
                self.series.append(temp_model.from_map(k))
        if m.get('Unit') is not None:
            self.unit = m.get('Unit')
        return self


class DescribeDBClusterPerformanceResponseBody(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        end_time: str = None,
        performances: List[DescribeDBClusterPerformanceResponseBodyPerformances] = None,
        request_id: str = None,
        start_time: str = None,
    ):
        self.dbcluster_id = dbcluster_id
        self.end_time = end_time
        self.performances = performances
        self.request_id = request_id
        self.start_time = start_time

    def validate(self):
        if self.performances:
            for k in self.performances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        result['Performances'] = []
        if self.performances is not None:
            for k in self.performances:
                result['Performances'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        self.performances = []
        if m.get('Performances') is not None:
            for k in m.get('Performances'):
                temp_model = DescribeDBClusterPerformanceResponseBodyPerformances()
                self.performances.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDBClusterPerformanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDBClusterPerformanceResponseBody = None,
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
            temp_model = DescribeDBClusterPerformanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBResourceGroupRequest(TeaModel):
    def __init__(
        self,
        customer_uid: int = None,
        dbcluster_id: str = None,
        exclude_ainode: bool = None,
        group_name: str = None,
        group_type: str = None,
        region_code: str = None,
    ):
        # This parameter is required.
        self.customer_uid = customer_uid
        self.dbcluster_id = dbcluster_id
        self.exclude_ainode = exclude_ainode
        self.group_name = group_name
        self.group_type = group_type
        # This parameter is required.
        self.region_code = region_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.customer_uid is not None:
            result['CustomerUid'] = self.customer_uid
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.exclude_ainode is not None:
            result['ExcludeAINode'] = self.exclude_ainode
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.group_type is not None:
            result['GroupType'] = self.group_type
        if self.region_code is not None:
            result['RegionCode'] = self.region_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomerUid') is not None:
            self.customer_uid = m.get('CustomerUid')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('ExcludeAINode') is not None:
            self.exclude_ainode = m.get('ExcludeAINode')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('GroupType') is not None:
            self.group_type = m.get('GroupType')
        if m.get('RegionCode') is not None:
            self.region_code = m.get('RegionCode')
        return self


class DescribeDBResourceGroupResponseBodyGroupsInfoGpuModelCpu(TeaModel):
    def __init__(
        self,
        value: int = None,
    ):
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class DescribeDBResourceGroupResponseBodyGroupsInfoGpuModelMemory(TeaModel):
    def __init__(
        self,
        value: int = None,
    ):
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class DescribeDBResourceGroupResponseBodyGroupsInfoGpuModel(TeaModel):
    def __init__(
        self,
        internal_gpumodel: str = None,
        allocate_unit: str = None,
        cpu: DescribeDBResourceGroupResponseBodyGroupsInfoGpuModelCpu = None,
        memory: DescribeDBResourceGroupResponseBodyGroupsInfoGpuModelMemory = None,
        name: str = None,
    ):
        self.internal_gpumodel = internal_gpumodel
        self.allocate_unit = allocate_unit
        self.cpu = cpu
        self.memory = memory
        self.name = name

    def validate(self):
        if self.cpu:
            self.cpu.validate()
        if self.memory:
            self.memory.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.internal_gpumodel is not None:
            result['InternalGPUModel'] = self.internal_gpumodel
        if self.allocate_unit is not None:
            result['allocateUnit'] = self.allocate_unit
        if self.cpu is not None:
            result['cpu'] = self.cpu.to_map()
        if self.memory is not None:
            result['memory'] = self.memory.to_map()
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InternalGPUModel') is not None:
            self.internal_gpumodel = m.get('InternalGPUModel')
        if m.get('allocateUnit') is not None:
            self.allocate_unit = m.get('allocateUnit')
        if m.get('cpu') is not None:
            temp_model = DescribeDBResourceGroupResponseBodyGroupsInfoGpuModelCpu()
            self.cpu = temp_model.from_map(m['cpu'])
        if m.get('memory') is not None:
            temp_model = DescribeDBResourceGroupResponseBodyGroupsInfoGpuModelMemory()
            self.memory = temp_model.from_map(m['memory'])
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class DescribeDBResourceGroupResponseBodyGroupsInfoRules(TeaModel):
    def __init__(
        self,
        group_name: str = None,
        query_time: str = None,
        target_group_name: str = None,
    ):
        self.group_name = group_name
        self.query_time = query_time
        self.target_group_name = target_group_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.query_time is not None:
            result['QueryTime'] = self.query_time
        if self.target_group_name is not None:
            result['TargetGroupName'] = self.target_group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('QueryTime') is not None:
            self.query_time = m.get('QueryTime')
        if m.get('TargetGroupName') is not None:
            self.target_group_name = m.get('TargetGroupName')
        return self


class DescribeDBResourceGroupResponseBodyGroupsInfo(TeaModel):
    def __init__(
        self,
        auto_stop_interval: str = None,
        cluster_mode: str = None,
        cluster_size_resource: str = None,
        create_timestamp: int = None,
        db_cluster_id: str = None,
        elastic_min_compute_resource: str = None,
        enable_spot: str = None,
        engine: str = None,
        engine_params: Dict[str, Any] = None,
        gpu_model: DescribeDBResourceGroupResponseBodyGroupsInfoGpuModel = None,
        group_name: str = None,
        group_type: str = None,
        group_users: str = None,
        max_cluster_count: int = None,
        max_compute_resource: str = None,
        max_gpu_quantity: int = None,
        message: str = None,
        min_cluster_count: int = None,
        min_compute_resource: str = None,
        min_gpu_quantity: int = None,
        rules: List[DescribeDBResourceGroupResponseBodyGroupsInfoRules] = None,
        running_cluster_count: int = None,
        spec_name: str = None,
        status: str = None,
        target_resource_group_name: str = None,
        update_timestamp: str = None,
        vpc_id: str = None,
    ):
        self.auto_stop_interval = auto_stop_interval
        self.cluster_mode = cluster_mode
        self.cluster_size_resource = cluster_size_resource
        self.create_timestamp = create_timestamp
        self.db_cluster_id = db_cluster_id
        self.elastic_min_compute_resource = elastic_min_compute_resource
        self.enable_spot = enable_spot
        self.engine = engine
        self.engine_params = engine_params
        self.gpu_model = gpu_model
        self.group_name = group_name
        self.group_type = group_type
        self.group_users = group_users
        self.max_cluster_count = max_cluster_count
        self.max_compute_resource = max_compute_resource
        self.max_gpu_quantity = max_gpu_quantity
        # This parameter is required.
        self.message = message
        self.min_cluster_count = min_cluster_count
        self.min_compute_resource = min_compute_resource
        self.min_gpu_quantity = min_gpu_quantity
        self.rules = rules
        self.running_cluster_count = running_cluster_count
        self.spec_name = spec_name
        self.status = status
        self.target_resource_group_name = target_resource_group_name
        self.update_timestamp = update_timestamp
        self.vpc_id = vpc_id

    def validate(self):
        if self.gpu_model:
            self.gpu_model.validate()
        if self.rules:
            for k in self.rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_stop_interval is not None:
            result['AutoStopInterval'] = self.auto_stop_interval
        if self.cluster_mode is not None:
            result['ClusterMode'] = self.cluster_mode
        if self.cluster_size_resource is not None:
            result['ClusterSizeResource'] = self.cluster_size_resource
        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp
        if self.db_cluster_id is not None:
            result['DbClusterId'] = self.db_cluster_id
        if self.elastic_min_compute_resource is not None:
            result['ElasticMinComputeResource'] = self.elastic_min_compute_resource
        if self.enable_spot is not None:
            result['EnableSpot'] = self.enable_spot
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.engine_params is not None:
            result['EngineParams'] = self.engine_params
        if self.gpu_model is not None:
            result['GpuModel'] = self.gpu_model.to_map()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.group_type is not None:
            result['GroupType'] = self.group_type
        if self.group_users is not None:
            result['GroupUsers'] = self.group_users
        if self.max_cluster_count is not None:
            result['MaxClusterCount'] = self.max_cluster_count
        if self.max_compute_resource is not None:
            result['MaxComputeResource'] = self.max_compute_resource
        if self.max_gpu_quantity is not None:
            result['MaxGpuQuantity'] = self.max_gpu_quantity
        if self.message is not None:
            result['Message'] = self.message
        if self.min_cluster_count is not None:
            result['MinClusterCount'] = self.min_cluster_count
        if self.min_compute_resource is not None:
            result['MinComputeResource'] = self.min_compute_resource
        if self.min_gpu_quantity is not None:
            result['MinGpuQuantity'] = self.min_gpu_quantity
        result['Rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['Rules'].append(k.to_map() if k else None)
        if self.running_cluster_count is not None:
            result['RunningClusterCount'] = self.running_cluster_count
        if self.spec_name is not None:
            result['SpecName'] = self.spec_name
        if self.status is not None:
            result['Status'] = self.status
        if self.target_resource_group_name is not None:
            result['TargetResourceGroupName'] = self.target_resource_group_name
        if self.update_timestamp is not None:
            result['UpdateTimestamp'] = self.update_timestamp
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoStopInterval') is not None:
            self.auto_stop_interval = m.get('AutoStopInterval')
        if m.get('ClusterMode') is not None:
            self.cluster_mode = m.get('ClusterMode')
        if m.get('ClusterSizeResource') is not None:
            self.cluster_size_resource = m.get('ClusterSizeResource')
        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')
        if m.get('DbClusterId') is not None:
            self.db_cluster_id = m.get('DbClusterId')
        if m.get('ElasticMinComputeResource') is not None:
            self.elastic_min_compute_resource = m.get('ElasticMinComputeResource')
        if m.get('EnableSpot') is not None:
            self.enable_spot = m.get('EnableSpot')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('EngineParams') is not None:
            self.engine_params = m.get('EngineParams')
        if m.get('GpuModel') is not None:
            temp_model = DescribeDBResourceGroupResponseBodyGroupsInfoGpuModel()
            self.gpu_model = temp_model.from_map(m['GpuModel'])
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('GroupType') is not None:
            self.group_type = m.get('GroupType')
        if m.get('GroupUsers') is not None:
            self.group_users = m.get('GroupUsers')
        if m.get('MaxClusterCount') is not None:
            self.max_cluster_count = m.get('MaxClusterCount')
        if m.get('MaxComputeResource') is not None:
            self.max_compute_resource = m.get('MaxComputeResource')
        if m.get('MaxGpuQuantity') is not None:
            self.max_gpu_quantity = m.get('MaxGpuQuantity')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('MinClusterCount') is not None:
            self.min_cluster_count = m.get('MinClusterCount')
        if m.get('MinComputeResource') is not None:
            self.min_compute_resource = m.get('MinComputeResource')
        if m.get('MinGpuQuantity') is not None:
            self.min_gpu_quantity = m.get('MinGpuQuantity')
        self.rules = []
        if m.get('Rules') is not None:
            for k in m.get('Rules'):
                temp_model = DescribeDBResourceGroupResponseBodyGroupsInfoRules()
                self.rules.append(temp_model.from_map(k))
        if m.get('RunningClusterCount') is not None:
            self.running_cluster_count = m.get('RunningClusterCount')
        if m.get('SpecName') is not None:
            self.spec_name = m.get('SpecName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TargetResourceGroupName') is not None:
            self.target_resource_group_name = m.get('TargetResourceGroupName')
        if m.get('UpdateTimestamp') is not None:
            self.update_timestamp = m.get('UpdateTimestamp')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class DescribeDBResourceGroupResponseBody(TeaModel):
    def __init__(
        self,
        groups_info: List[DescribeDBResourceGroupResponseBodyGroupsInfo] = None,
        request_id: str = None,
    ):
        self.groups_info = groups_info
        self.request_id = request_id

    def validate(self):
        if self.groups_info:
            for k in self.groups_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['GroupsInfo'] = []
        if self.groups_info is not None:
            for k in self.groups_info:
                result['GroupsInfo'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.groups_info = []
        if m.get('GroupsInfo') is not None:
            for k in m.get('GroupsInfo'):
                temp_model = DescribeDBResourceGroupResponseBodyGroupsInfo()
                self.groups_info.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDBResourceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDBResourceGroupResponseBody = None,
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
            temp_model = DescribeDBResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDbClusterRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        ali_uid: int = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # This parameter is required.
        self.ali_uid = ali_uid
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.ali_uid is not None:
            result['aliUid'] = self.ali_uid
        if self.region_id is not None:
            result['regionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('aliUid') is not None:
            self.ali_uid = m.get('aliUid')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        return self


class DescribeDbClusterResponseBodyDataDbClusterBillingDetails(TeaModel):
    def __init__(
        self,
        channel: str = None,
        commodity_code: str = None,
        expire_time: str = None,
        order_id: int = None,
        pay_type: str = None,
    ):
        self.channel = channel
        self.commodity_code = commodity_code
        self.expire_time = expire_time
        self.order_id = order_id
        self.pay_type = pay_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel is not None:
            result['Channel'] = self.channel
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        return self


class DescribeDbClusterResponseBodyDataDbClusterDeprecatedProperties(TeaModel):
    def __init__(
        self,
        db_cluster_type: str = None,
        engine: str = None,
        engine_version: str = None,
        instance_class_group: str = None,
        storage_category: str = None,
    ):
        self.db_cluster_type = db_cluster_type
        self.engine = engine
        self.engine_version = engine_version
        self.instance_class_group = instance_class_group
        self.storage_category = storage_category

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_cluster_type is not None:
            result['DbClusterType'] = self.db_cluster_type
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.instance_class_group is not None:
            result['InstanceClassGroup'] = self.instance_class_group
        if self.storage_category is not None:
            result['StorageCategory'] = self.storage_category
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbClusterType') is not None:
            self.db_cluster_type = m.get('DbClusterType')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('InstanceClassGroup') is not None:
            self.instance_class_group = m.get('InstanceClassGroup')
        if m.get('StorageCategory') is not None:
            self.storage_category = m.get('StorageCategory')
        return self


class DescribeDbClusterResponseBodyDataDbClusterLocation(TeaModel):
    def __init__(
        self,
        region_code: str = None,
        region_id: str = None,
        sub_domain: str = None,
        zone_id: str = None,
    ):
        self.region_code = region_code
        self.region_id = region_id
        self.sub_domain = sub_domain
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_code is not None:
            result['RegionCode'] = self.region_code
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.sub_domain is not None:
            result['SubDomain'] = self.sub_domain
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionCode') is not None:
            self.region_code = m.get('RegionCode')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SubDomain') is not None:
            self.sub_domain = m.get('SubDomain')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeDbClusterResponseBodyDataDbClusterNetwork(TeaModel):
    def __init__(
        self,
        cloud_instance_ip: str = None,
        cluster_network_type: str = None,
        connection_string: str = None,
        db_cluster_net_type: str = None,
        port: str = None,
        tunnel_id: str = None,
        v_switch_id: str = None,
        vpc_cloud_instance_id: str = None,
        vpc_id: str = None,
    ):
        self.cloud_instance_ip = cloud_instance_ip
        self.cluster_network_type = cluster_network_type
        self.connection_string = connection_string
        self.db_cluster_net_type = db_cluster_net_type
        self.port = port
        self.tunnel_id = tunnel_id
        self.v_switch_id = v_switch_id
        self.vpc_cloud_instance_id = vpc_cloud_instance_id
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cloud_instance_ip is not None:
            result['CloudInstanceIp'] = self.cloud_instance_ip
        if self.cluster_network_type is not None:
            result['ClusterNetworkType'] = self.cluster_network_type
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
        if self.db_cluster_net_type is not None:
            result['DbClusterNetType'] = self.db_cluster_net_type
        if self.port is not None:
            result['Port'] = self.port
        if self.tunnel_id is not None:
            result['TunnelId'] = self.tunnel_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_cloud_instance_id is not None:
            result['VpcCloudInstanceId'] = self.vpc_cloud_instance_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CloudInstanceIp') is not None:
            self.cloud_instance_ip = m.get('CloudInstanceIp')
        if m.get('ClusterNetworkType') is not None:
            self.cluster_network_type = m.get('ClusterNetworkType')
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
        if m.get('DbClusterNetType') is not None:
            self.db_cluster_net_type = m.get('DbClusterNetType')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('TunnelId') is not None:
            self.tunnel_id = m.get('TunnelId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcCloudInstanceId') is not None:
            self.vpc_cloud_instance_id = m.get('VpcCloudInstanceId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class DescribeDbClusterResponseBodyDataDbClusterOperationalStatus(TeaModel):
    def __init__(
        self,
        full_engine_version: str = None,
        is_non_standard: bool = None,
        lock_mode: str = None,
        lock_reason: str = None,
        sample_dataset_status: str = None,
    ):
        self.full_engine_version = full_engine_version
        self.is_non_standard = is_non_standard
        self.lock_mode = lock_mode
        self.lock_reason = lock_reason
        self.sample_dataset_status = sample_dataset_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.full_engine_version is not None:
            result['FullEngineVersion'] = self.full_engine_version
        if self.is_non_standard is not None:
            result['IsNonStandard'] = self.is_non_standard
        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode
        if self.lock_reason is not None:
            result['LockReason'] = self.lock_reason
        if self.sample_dataset_status is not None:
            result['SampleDatasetStatus'] = self.sample_dataset_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FullEngineVersion') is not None:
            self.full_engine_version = m.get('FullEngineVersion')
        if m.get('IsNonStandard') is not None:
            self.is_non_standard = m.get('IsNonStandard')
        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')
        if m.get('LockReason') is not None:
            self.lock_reason = m.get('LockReason')
        if m.get('SampleDatasetStatus') is not None:
            self.sample_dataset_status = m.get('SampleDatasetStatus')
        return self


class DescribeDbClusterResponseBodyDataDbClusterResourceAssociations(TeaModel):
    def __init__(
        self,
        db_logic_id: int = None,
        kms_id: str = None,
        rds_instance_id: str = None,
        resource_group_id: str = None,
        resource_mode: str = None,
        resource_order_id: str = None,
    ):
        self.db_logic_id = db_logic_id
        self.kms_id = kms_id
        self.rds_instance_id = rds_instance_id
        self.resource_group_id = resource_group_id
        self.resource_mode = resource_mode
        self.resource_order_id = resource_order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_logic_id is not None:
            result['DbLogicId'] = self.db_logic_id
        if self.kms_id is not None:
            result['KmsId'] = self.kms_id
        if self.rds_instance_id is not None:
            result['RdsInstanceId'] = self.rds_instance_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_mode is not None:
            result['ResourceMode'] = self.resource_mode
        if self.resource_order_id is not None:
            result['ResourceOrderId'] = self.resource_order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbLogicId') is not None:
            self.db_logic_id = m.get('DbLogicId')
        if m.get('KmsId') is not None:
            self.kms_id = m.get('KmsId')
        if m.get('RdsInstanceId') is not None:
            self.rds_instance_id = m.get('RdsInstanceId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceMode') is not None:
            self.resource_mode = m.get('ResourceMode')
        if m.get('ResourceOrderId') is not None:
            self.resource_order_id = m.get('ResourceOrderId')
        return self


class DescribeDbClusterResponseBodyDataDbClusterResourceSpec(TeaModel):
    def __init__(
        self,
        compute_resource: str = None,
        db_node_class: str = None,
        db_node_count: int = None,
        db_node_storage: int = None,
        db_node_storage_type: str = None,
        elastic_ioresource: int = None,
        elastic_ioresource_size: str = None,
        executor_count: int = None,
        reserve_acu: str = None,
        reserved_node_replica_count: int = None,
        reserved_node_size_acu: int = None,
        storage_resource: str = None,
    ):
        self.compute_resource = compute_resource
        self.db_node_class = db_node_class
        self.db_node_count = db_node_count
        self.db_node_storage = db_node_storage
        self.db_node_storage_type = db_node_storage_type
        self.elastic_ioresource = elastic_ioresource
        self.elastic_ioresource_size = elastic_ioresource_size
        self.executor_count = executor_count
        self.reserve_acu = reserve_acu
        self.reserved_node_replica_count = reserved_node_replica_count
        self.reserved_node_size_acu = reserved_node_size_acu
        self.storage_resource = storage_resource

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compute_resource is not None:
            result['ComputeResource'] = self.compute_resource
        if self.db_node_class is not None:
            result['DbNodeClass'] = self.db_node_class
        if self.db_node_count is not None:
            result['DbNodeCount'] = self.db_node_count
        if self.db_node_storage is not None:
            result['DbNodeStorage'] = self.db_node_storage
        if self.db_node_storage_type is not None:
            result['DbNodeStorageType'] = self.db_node_storage_type
        if self.elastic_ioresource is not None:
            result['ElasticIOResource'] = self.elastic_ioresource
        if self.elastic_ioresource_size is not None:
            result['ElasticIOResourceSize'] = self.elastic_ioresource_size
        if self.executor_count is not None:
            result['ExecutorCount'] = self.executor_count
        if self.reserve_acu is not None:
            result['ReserveAcu'] = self.reserve_acu
        if self.reserved_node_replica_count is not None:
            result['ReservedNodeReplicaCount'] = self.reserved_node_replica_count
        if self.reserved_node_size_acu is not None:
            result['ReservedNodeSizeAcu'] = self.reserved_node_size_acu
        if self.storage_resource is not None:
            result['StorageResource'] = self.storage_resource
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComputeResource') is not None:
            self.compute_resource = m.get('ComputeResource')
        if m.get('DbNodeClass') is not None:
            self.db_node_class = m.get('DbNodeClass')
        if m.get('DbNodeCount') is not None:
            self.db_node_count = m.get('DbNodeCount')
        if m.get('DbNodeStorage') is not None:
            self.db_node_storage = m.get('DbNodeStorage')
        if m.get('DbNodeStorageType') is not None:
            self.db_node_storage_type = m.get('DbNodeStorageType')
        if m.get('ElasticIOResource') is not None:
            self.elastic_ioresource = m.get('ElasticIOResource')
        if m.get('ElasticIOResourceSize') is not None:
            self.elastic_ioresource_size = m.get('ElasticIOResourceSize')
        if m.get('ExecutorCount') is not None:
            self.executor_count = m.get('ExecutorCount')
        if m.get('ReserveAcu') is not None:
            self.reserve_acu = m.get('ReserveAcu')
        if m.get('ReservedNodeReplicaCount') is not None:
            self.reserved_node_replica_count = m.get('ReservedNodeReplicaCount')
        if m.get('ReservedNodeSizeAcu') is not None:
            self.reserved_node_size_acu = m.get('ReservedNodeSizeAcu')
        if m.get('StorageResource') is not None:
            self.storage_resource = m.get('StorageResource')
        return self


class DescribeDbClusterResponseBodyDataDbClusterUser(TeaModel):
    def __init__(
        self,
        ali_uid: int = None,
        bid: str = None,
        customer_level: str = None,
        customer_name: str = None,
        is_enterprise_customer: bool = None,
        is_inner_customer: bool = None,
        is_test_cluster: bool = None,
    ):
        self.ali_uid = ali_uid
        self.bid = bid
        self.customer_level = customer_level
        self.customer_name = customer_name
        self.is_enterprise_customer = is_enterprise_customer
        self.is_inner_customer = is_inner_customer
        self.is_test_cluster = is_test_cluster

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.bid is not None:
            result['Bid'] = self.bid
        if self.customer_level is not None:
            result['CustomerLevel'] = self.customer_level
        if self.customer_name is not None:
            result['CustomerName'] = self.customer_name
        if self.is_enterprise_customer is not None:
            result['IsEnterpriseCustomer'] = self.is_enterprise_customer
        if self.is_inner_customer is not None:
            result['IsInnerCustomer'] = self.is_inner_customer
        if self.is_test_cluster is not None:
            result['IsTestCluster'] = self.is_test_cluster
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')
        if m.get('CustomerLevel') is not None:
            self.customer_level = m.get('CustomerLevel')
        if m.get('CustomerName') is not None:
            self.customer_name = m.get('CustomerName')
        if m.get('IsEnterpriseCustomer') is not None:
            self.is_enterprise_customer = m.get('IsEnterpriseCustomer')
        if m.get('IsInnerCustomer') is not None:
            self.is_inner_customer = m.get('IsInnerCustomer')
        if m.get('IsTestCluster') is not None:
            self.is_test_cluster = m.get('IsTestCluster')
        return self


class DescribeDbClusterResponseBodyDataDbCluster(TeaModel):
    def __init__(
        self,
        admin_remark: str = None,
        billing_details: DescribeDbClusterResponseBodyDataDbClusterBillingDetails = None,
        category: str = None,
        db_cluster_description: str = None,
        db_cluster_id: str = None,
        db_cluster_status: str = None,
        db_type: str = None,
        db_version: str = None,
        deprecated_properties: DescribeDbClusterResponseBodyDataDbClusterDeprecatedProperties = None,
        location: DescribeDbClusterResponseBodyDataDbClusterLocation = None,
        mode: str = None,
        network: DescribeDbClusterResponseBodyDataDbClusterNetwork = None,
        operational_status: DescribeDbClusterResponseBodyDataDbClusterOperationalStatus = None,
        platform: str = None,
        product_form: str = None,
        resource_associations: DescribeDbClusterResponseBodyDataDbClusterResourceAssociations = None,
        resource_spec: DescribeDbClusterResponseBodyDataDbClusterResourceSpec = None,
        user: DescribeDbClusterResponseBodyDataDbClusterUser = None,
    ):
        self.admin_remark = admin_remark
        self.billing_details = billing_details
        self.category = category
        self.db_cluster_description = db_cluster_description
        self.db_cluster_id = db_cluster_id
        self.db_cluster_status = db_cluster_status
        self.db_type = db_type
        self.db_version = db_version
        self.deprecated_properties = deprecated_properties
        self.location = location
        self.mode = mode
        self.network = network
        self.operational_status = operational_status
        self.platform = platform
        self.product_form = product_form
        self.resource_associations = resource_associations
        self.resource_spec = resource_spec
        self.user = user

    def validate(self):
        if self.billing_details:
            self.billing_details.validate()
        if self.deprecated_properties:
            self.deprecated_properties.validate()
        if self.location:
            self.location.validate()
        if self.network:
            self.network.validate()
        if self.operational_status:
            self.operational_status.validate()
        if self.resource_associations:
            self.resource_associations.validate()
        if self.resource_spec:
            self.resource_spec.validate()
        if self.user:
            self.user.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.admin_remark is not None:
            result['AdminRemark'] = self.admin_remark
        if self.billing_details is not None:
            result['BillingDetails'] = self.billing_details.to_map()
        if self.category is not None:
            result['Category'] = self.category
        if self.db_cluster_description is not None:
            result['DbClusterDescription'] = self.db_cluster_description
        if self.db_cluster_id is not None:
            result['DbClusterId'] = self.db_cluster_id
        if self.db_cluster_status is not None:
            result['DbClusterStatus'] = self.db_cluster_status
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.db_version is not None:
            result['DbVersion'] = self.db_version
        if self.deprecated_properties is not None:
            result['DeprecatedProperties'] = self.deprecated_properties.to_map()
        if self.location is not None:
            result['Location'] = self.location.to_map()
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.network is not None:
            result['Network'] = self.network.to_map()
        if self.operational_status is not None:
            result['OperationalStatus'] = self.operational_status.to_map()
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.product_form is not None:
            result['ProductForm'] = self.product_form
        if self.resource_associations is not None:
            result['ResourceAssociations'] = self.resource_associations.to_map()
        if self.resource_spec is not None:
            result['ResourceSpec'] = self.resource_spec.to_map()
        if self.user is not None:
            result['User'] = self.user.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdminRemark') is not None:
            self.admin_remark = m.get('AdminRemark')
        if m.get('BillingDetails') is not None:
            temp_model = DescribeDbClusterResponseBodyDataDbClusterBillingDetails()
            self.billing_details = temp_model.from_map(m['BillingDetails'])
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('DbClusterDescription') is not None:
            self.db_cluster_description = m.get('DbClusterDescription')
        if m.get('DbClusterId') is not None:
            self.db_cluster_id = m.get('DbClusterId')
        if m.get('DbClusterStatus') is not None:
            self.db_cluster_status = m.get('DbClusterStatus')
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('DbVersion') is not None:
            self.db_version = m.get('DbVersion')
        if m.get('DeprecatedProperties') is not None:
            temp_model = DescribeDbClusterResponseBodyDataDbClusterDeprecatedProperties()
            self.deprecated_properties = temp_model.from_map(m['DeprecatedProperties'])
        if m.get('Location') is not None:
            temp_model = DescribeDbClusterResponseBodyDataDbClusterLocation()
            self.location = temp_model.from_map(m['Location'])
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('Network') is not None:
            temp_model = DescribeDbClusterResponseBodyDataDbClusterNetwork()
            self.network = temp_model.from_map(m['Network'])
        if m.get('OperationalStatus') is not None:
            temp_model = DescribeDbClusterResponseBodyDataDbClusterOperationalStatus()
            self.operational_status = temp_model.from_map(m['OperationalStatus'])
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('ProductForm') is not None:
            self.product_form = m.get('ProductForm')
        if m.get('ResourceAssociations') is not None:
            temp_model = DescribeDbClusterResponseBodyDataDbClusterResourceAssociations()
            self.resource_associations = temp_model.from_map(m['ResourceAssociations'])
        if m.get('ResourceSpec') is not None:
            temp_model = DescribeDbClusterResponseBodyDataDbClusterResourceSpec()
            self.resource_spec = temp_model.from_map(m['ResourceSpec'])
        if m.get('User') is not None:
            temp_model = DescribeDbClusterResponseBodyDataDbClusterUser()
            self.user = temp_model.from_map(m['User'])
        return self


class DescribeDbClusterResponseBodyData(TeaModel):
    def __init__(
        self,
        db_cluster: DescribeDbClusterResponseBodyDataDbCluster = None,
    ):
        self.db_cluster = db_cluster

    def validate(self):
        if self.db_cluster:
            self.db_cluster.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_cluster is not None:
            result['dbCluster'] = self.db_cluster.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dbCluster') is not None:
            temp_model = DescribeDbClusterResponseBodyDataDbCluster()
            self.db_cluster = temp_model.from_map(m['dbCluster'])
        return self


class DescribeDbClusterResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: DescribeDbClusterResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        result_code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.result_code = result_code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.result_code is not None:
            result['resultCode'] = self.result_code
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('data') is not None:
            temp_model = DescribeDbClusterResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('resultCode') is not None:
            self.result_code = m.get('resultCode')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class DescribeDbClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDbClusterResponseBody = None,
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
            temp_model = DescribeDbClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDbClusterParamRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        param_name: str = None,
        ali_uid: int = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # This parameter is required.
        self.param_name = param_name
        self.ali_uid = ali_uid
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.param_name is not None:
            result['ParamName'] = self.param_name
        if self.ali_uid is not None:
            result['aliUid'] = self.ali_uid
        if self.region_id is not None:
            result['regionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('ParamName') is not None:
            self.param_name = m.get('ParamName')
        if m.get('aliUid') is not None:
            self.ali_uid = m.get('aliUid')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        return self


class DescribeDbClusterParamResponseBody(TeaModel):
    def __init__(
        self,
        param_json: str = None,
        request_id: str = None,
        http_status_code: int = None,
        message: str = None,
        result_code: str = None,
        success: bool = None,
    ):
        self.param_json = param_json
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.message = message
        self.result_code = result_code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.param_json is not None:
            result['ParamJson'] = self.param_json
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.result_code is not None:
            result['resultCode'] = self.result_code
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParamJson') is not None:
            self.param_json = m.get('ParamJson')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('resultCode') is not None:
            self.result_code = m.get('resultCode')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class DescribeDbClusterParamResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDbClusterParamResponseBody = None,
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
            temp_model = DescribeDbClusterParamResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDbClusterV5Request(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        ali_uid: int = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # This parameter is required.
        self.ali_uid = ali_uid
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.ali_uid is not None:
            result['aliUid'] = self.ali_uid
        if self.region_id is not None:
            result['regionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('aliUid') is not None:
            self.ali_uid = m.get('aliUid')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        return self


class DescribeDbClusterV5ResponseBodyDataDbClusterBillingDetails(TeaModel):
    def __init__(
        self,
        channel: str = None,
        commodity_code: str = None,
        expire_time: str = None,
        order_id: int = None,
        pay_type: str = None,
    ):
        self.channel = channel
        self.commodity_code = commodity_code
        self.expire_time = expire_time
        self.order_id = order_id
        self.pay_type = pay_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel is not None:
            result['Channel'] = self.channel
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        return self


class DescribeDbClusterV5ResponseBodyDataDbClusterDeprecatedProperties(TeaModel):
    def __init__(
        self,
        db_cluster_type: str = None,
        engine: str = None,
        engine_version: str = None,
        instance_class_group: str = None,
        storage_category: str = None,
    ):
        self.db_cluster_type = db_cluster_type
        self.engine = engine
        self.engine_version = engine_version
        self.instance_class_group = instance_class_group
        self.storage_category = storage_category

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_cluster_type is not None:
            result['DbClusterType'] = self.db_cluster_type
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.instance_class_group is not None:
            result['InstanceClassGroup'] = self.instance_class_group
        if self.storage_category is not None:
            result['StorageCategory'] = self.storage_category
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbClusterType') is not None:
            self.db_cluster_type = m.get('DbClusterType')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('InstanceClassGroup') is not None:
            self.instance_class_group = m.get('InstanceClassGroup')
        if m.get('StorageCategory') is not None:
            self.storage_category = m.get('StorageCategory')
        return self


class DescribeDbClusterV5ResponseBodyDataDbClusterLocation(TeaModel):
    def __init__(
        self,
        region_code: str = None,
        region_id: str = None,
        sub_domain: str = None,
        zone_id: str = None,
    ):
        self.region_code = region_code
        self.region_id = region_id
        self.sub_domain = sub_domain
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_code is not None:
            result['RegionCode'] = self.region_code
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.sub_domain is not None:
            result['SubDomain'] = self.sub_domain
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionCode') is not None:
            self.region_code = m.get('RegionCode')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SubDomain') is not None:
            self.sub_domain = m.get('SubDomain')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeDbClusterV5ResponseBodyDataDbClusterNetwork(TeaModel):
    def __init__(
        self,
        cloud_instance_ip: str = None,
        cluster_network_type: str = None,
        connection_string: str = None,
        db_cluster_net_type: str = None,
        port: str = None,
        tunnel_id: str = None,
        v_switch_id: str = None,
        vpc_cloud_instance_id: str = None,
        vpc_id: str = None,
    ):
        self.cloud_instance_ip = cloud_instance_ip
        self.cluster_network_type = cluster_network_type
        self.connection_string = connection_string
        self.db_cluster_net_type = db_cluster_net_type
        self.port = port
        self.tunnel_id = tunnel_id
        self.v_switch_id = v_switch_id
        self.vpc_cloud_instance_id = vpc_cloud_instance_id
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cloud_instance_ip is not None:
            result['CloudInstanceIp'] = self.cloud_instance_ip
        if self.cluster_network_type is not None:
            result['ClusterNetworkType'] = self.cluster_network_type
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
        if self.db_cluster_net_type is not None:
            result['DbClusterNetType'] = self.db_cluster_net_type
        if self.port is not None:
            result['Port'] = self.port
        if self.tunnel_id is not None:
            result['TunnelId'] = self.tunnel_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_cloud_instance_id is not None:
            result['VpcCloudInstanceId'] = self.vpc_cloud_instance_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CloudInstanceIp') is not None:
            self.cloud_instance_ip = m.get('CloudInstanceIp')
        if m.get('ClusterNetworkType') is not None:
            self.cluster_network_type = m.get('ClusterNetworkType')
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
        if m.get('DbClusterNetType') is not None:
            self.db_cluster_net_type = m.get('DbClusterNetType')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('TunnelId') is not None:
            self.tunnel_id = m.get('TunnelId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcCloudInstanceId') is not None:
            self.vpc_cloud_instance_id = m.get('VpcCloudInstanceId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class DescribeDbClusterV5ResponseBodyDataDbClusterOperationalStatus(TeaModel):
    def __init__(
        self,
        full_engine_version: str = None,
        is_non_standard: bool = None,
        lock_mode: str = None,
        lock_reason: str = None,
        sample_dataset_status: str = None,
    ):
        self.full_engine_version = full_engine_version
        self.is_non_standard = is_non_standard
        self.lock_mode = lock_mode
        self.lock_reason = lock_reason
        self.sample_dataset_status = sample_dataset_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.full_engine_version is not None:
            result['FullEngineVersion'] = self.full_engine_version
        if self.is_non_standard is not None:
            result['IsNonStandard'] = self.is_non_standard
        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode
        if self.lock_reason is not None:
            result['LockReason'] = self.lock_reason
        if self.sample_dataset_status is not None:
            result['SampleDatasetStatus'] = self.sample_dataset_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FullEngineVersion') is not None:
            self.full_engine_version = m.get('FullEngineVersion')
        if m.get('IsNonStandard') is not None:
            self.is_non_standard = m.get('IsNonStandard')
        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')
        if m.get('LockReason') is not None:
            self.lock_reason = m.get('LockReason')
        if m.get('SampleDatasetStatus') is not None:
            self.sample_dataset_status = m.get('SampleDatasetStatus')
        return self


class DescribeDbClusterV5ResponseBodyDataDbClusterResourceAssociations(TeaModel):
    def __init__(
        self,
        db_logic_id: int = None,
        kms_id: str = None,
        rds_instance_id: str = None,
        resource_group_id: str = None,
        resource_mode: str = None,
        resource_order_id: str = None,
    ):
        self.db_logic_id = db_logic_id
        self.kms_id = kms_id
        self.rds_instance_id = rds_instance_id
        self.resource_group_id = resource_group_id
        self.resource_mode = resource_mode
        self.resource_order_id = resource_order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_logic_id is not None:
            result['DbLogicId'] = self.db_logic_id
        if self.kms_id is not None:
            result['KmsId'] = self.kms_id
        if self.rds_instance_id is not None:
            result['RdsInstanceId'] = self.rds_instance_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_mode is not None:
            result['ResourceMode'] = self.resource_mode
        if self.resource_order_id is not None:
            result['ResourceOrderId'] = self.resource_order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbLogicId') is not None:
            self.db_logic_id = m.get('DbLogicId')
        if m.get('KmsId') is not None:
            self.kms_id = m.get('KmsId')
        if m.get('RdsInstanceId') is not None:
            self.rds_instance_id = m.get('RdsInstanceId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceMode') is not None:
            self.resource_mode = m.get('ResourceMode')
        if m.get('ResourceOrderId') is not None:
            self.resource_order_id = m.get('ResourceOrderId')
        return self


class DescribeDbClusterV5ResponseBodyDataDbClusterResourceSpec(TeaModel):
    def __init__(
        self,
        compute_resource: str = None,
        db_node_class: str = None,
        db_node_count: int = None,
        db_node_storage: int = None,
        db_node_storage_type: str = None,
        elastic_ioresource: int = None,
        elastic_ioresource_size: str = None,
        executor_count: int = None,
        reserve_acu: str = None,
        reserved_node_replica_count: int = None,
        reserved_node_size_acu: int = None,
        storage_resource: str = None,
    ):
        self.compute_resource = compute_resource
        self.db_node_class = db_node_class
        self.db_node_count = db_node_count
        self.db_node_storage = db_node_storage
        self.db_node_storage_type = db_node_storage_type
        self.elastic_ioresource = elastic_ioresource
        self.elastic_ioresource_size = elastic_ioresource_size
        self.executor_count = executor_count
        self.reserve_acu = reserve_acu
        self.reserved_node_replica_count = reserved_node_replica_count
        self.reserved_node_size_acu = reserved_node_size_acu
        self.storage_resource = storage_resource

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compute_resource is not None:
            result['ComputeResource'] = self.compute_resource
        if self.db_node_class is not None:
            result['DbNodeClass'] = self.db_node_class
        if self.db_node_count is not None:
            result['DbNodeCount'] = self.db_node_count
        if self.db_node_storage is not None:
            result['DbNodeStorage'] = self.db_node_storage
        if self.db_node_storage_type is not None:
            result['DbNodeStorageType'] = self.db_node_storage_type
        if self.elastic_ioresource is not None:
            result['ElasticIOResource'] = self.elastic_ioresource
        if self.elastic_ioresource_size is not None:
            result['ElasticIOResourceSize'] = self.elastic_ioresource_size
        if self.executor_count is not None:
            result['ExecutorCount'] = self.executor_count
        if self.reserve_acu is not None:
            result['ReserveAcu'] = self.reserve_acu
        if self.reserved_node_replica_count is not None:
            result['ReservedNodeReplicaCount'] = self.reserved_node_replica_count
        if self.reserved_node_size_acu is not None:
            result['ReservedNodeSizeAcu'] = self.reserved_node_size_acu
        if self.storage_resource is not None:
            result['StorageResource'] = self.storage_resource
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComputeResource') is not None:
            self.compute_resource = m.get('ComputeResource')
        if m.get('DbNodeClass') is not None:
            self.db_node_class = m.get('DbNodeClass')
        if m.get('DbNodeCount') is not None:
            self.db_node_count = m.get('DbNodeCount')
        if m.get('DbNodeStorage') is not None:
            self.db_node_storage = m.get('DbNodeStorage')
        if m.get('DbNodeStorageType') is not None:
            self.db_node_storage_type = m.get('DbNodeStorageType')
        if m.get('ElasticIOResource') is not None:
            self.elastic_ioresource = m.get('ElasticIOResource')
        if m.get('ElasticIOResourceSize') is not None:
            self.elastic_ioresource_size = m.get('ElasticIOResourceSize')
        if m.get('ExecutorCount') is not None:
            self.executor_count = m.get('ExecutorCount')
        if m.get('ReserveAcu') is not None:
            self.reserve_acu = m.get('ReserveAcu')
        if m.get('ReservedNodeReplicaCount') is not None:
            self.reserved_node_replica_count = m.get('ReservedNodeReplicaCount')
        if m.get('ReservedNodeSizeAcu') is not None:
            self.reserved_node_size_acu = m.get('ReservedNodeSizeAcu')
        if m.get('StorageResource') is not None:
            self.storage_resource = m.get('StorageResource')
        return self


class DescribeDbClusterV5ResponseBodyDataDbClusterUser(TeaModel):
    def __init__(
        self,
        ali_uid: int = None,
        bid: str = None,
        customer_level: str = None,
        customer_name: str = None,
        is_enterprise_customer: bool = None,
        is_inner_customer: bool = None,
        is_test_cluster: bool = None,
    ):
        self.ali_uid = ali_uid
        self.bid = bid
        self.customer_level = customer_level
        self.customer_name = customer_name
        self.is_enterprise_customer = is_enterprise_customer
        self.is_inner_customer = is_inner_customer
        self.is_test_cluster = is_test_cluster

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.bid is not None:
            result['Bid'] = self.bid
        if self.customer_level is not None:
            result['CustomerLevel'] = self.customer_level
        if self.customer_name is not None:
            result['CustomerName'] = self.customer_name
        if self.is_enterprise_customer is not None:
            result['IsEnterpriseCustomer'] = self.is_enterprise_customer
        if self.is_inner_customer is not None:
            result['IsInnerCustomer'] = self.is_inner_customer
        if self.is_test_cluster is not None:
            result['IsTestCluster'] = self.is_test_cluster
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')
        if m.get('CustomerLevel') is not None:
            self.customer_level = m.get('CustomerLevel')
        if m.get('CustomerName') is not None:
            self.customer_name = m.get('CustomerName')
        if m.get('IsEnterpriseCustomer') is not None:
            self.is_enterprise_customer = m.get('IsEnterpriseCustomer')
        if m.get('IsInnerCustomer') is not None:
            self.is_inner_customer = m.get('IsInnerCustomer')
        if m.get('IsTestCluster') is not None:
            self.is_test_cluster = m.get('IsTestCluster')
        return self


class DescribeDbClusterV5ResponseBodyDataDbCluster(TeaModel):
    def __init__(
        self,
        admin_remark: str = None,
        billing_details: DescribeDbClusterV5ResponseBodyDataDbClusterBillingDetails = None,
        category: str = None,
        db_cluster_description: str = None,
        db_cluster_id: str = None,
        db_cluster_status: str = None,
        db_type: str = None,
        db_version: str = None,
        deprecated_properties: DescribeDbClusterV5ResponseBodyDataDbClusterDeprecatedProperties = None,
        location: DescribeDbClusterV5ResponseBodyDataDbClusterLocation = None,
        mode: str = None,
        network: DescribeDbClusterV5ResponseBodyDataDbClusterNetwork = None,
        operational_status: DescribeDbClusterV5ResponseBodyDataDbClusterOperationalStatus = None,
        platform: str = None,
        product_form: str = None,
        resource_associations: DescribeDbClusterV5ResponseBodyDataDbClusterResourceAssociations = None,
        resource_spec: DescribeDbClusterV5ResponseBodyDataDbClusterResourceSpec = None,
        user: DescribeDbClusterV5ResponseBodyDataDbClusterUser = None,
    ):
        self.admin_remark = admin_remark
        self.billing_details = billing_details
        self.category = category
        self.db_cluster_description = db_cluster_description
        self.db_cluster_id = db_cluster_id
        self.db_cluster_status = db_cluster_status
        self.db_type = db_type
        self.db_version = db_version
        self.deprecated_properties = deprecated_properties
        self.location = location
        self.mode = mode
        self.network = network
        self.operational_status = operational_status
        self.platform = platform
        self.product_form = product_form
        self.resource_associations = resource_associations
        self.resource_spec = resource_spec
        self.user = user

    def validate(self):
        if self.billing_details:
            self.billing_details.validate()
        if self.deprecated_properties:
            self.deprecated_properties.validate()
        if self.location:
            self.location.validate()
        if self.network:
            self.network.validate()
        if self.operational_status:
            self.operational_status.validate()
        if self.resource_associations:
            self.resource_associations.validate()
        if self.resource_spec:
            self.resource_spec.validate()
        if self.user:
            self.user.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.admin_remark is not None:
            result['AdminRemark'] = self.admin_remark
        if self.billing_details is not None:
            result['BillingDetails'] = self.billing_details.to_map()
        if self.category is not None:
            result['Category'] = self.category
        if self.db_cluster_description is not None:
            result['DbClusterDescription'] = self.db_cluster_description
        if self.db_cluster_id is not None:
            result['DbClusterId'] = self.db_cluster_id
        if self.db_cluster_status is not None:
            result['DbClusterStatus'] = self.db_cluster_status
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.db_version is not None:
            result['DbVersion'] = self.db_version
        if self.deprecated_properties is not None:
            result['DeprecatedProperties'] = self.deprecated_properties.to_map()
        if self.location is not None:
            result['Location'] = self.location.to_map()
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.network is not None:
            result['Network'] = self.network.to_map()
        if self.operational_status is not None:
            result['OperationalStatus'] = self.operational_status.to_map()
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.product_form is not None:
            result['ProductForm'] = self.product_form
        if self.resource_associations is not None:
            result['ResourceAssociations'] = self.resource_associations.to_map()
        if self.resource_spec is not None:
            result['ResourceSpec'] = self.resource_spec.to_map()
        if self.user is not None:
            result['User'] = self.user.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdminRemark') is not None:
            self.admin_remark = m.get('AdminRemark')
        if m.get('BillingDetails') is not None:
            temp_model = DescribeDbClusterV5ResponseBodyDataDbClusterBillingDetails()
            self.billing_details = temp_model.from_map(m['BillingDetails'])
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('DbClusterDescription') is not None:
            self.db_cluster_description = m.get('DbClusterDescription')
        if m.get('DbClusterId') is not None:
            self.db_cluster_id = m.get('DbClusterId')
        if m.get('DbClusterStatus') is not None:
            self.db_cluster_status = m.get('DbClusterStatus')
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('DbVersion') is not None:
            self.db_version = m.get('DbVersion')
        if m.get('DeprecatedProperties') is not None:
            temp_model = DescribeDbClusterV5ResponseBodyDataDbClusterDeprecatedProperties()
            self.deprecated_properties = temp_model.from_map(m['DeprecatedProperties'])
        if m.get('Location') is not None:
            temp_model = DescribeDbClusterV5ResponseBodyDataDbClusterLocation()
            self.location = temp_model.from_map(m['Location'])
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('Network') is not None:
            temp_model = DescribeDbClusterV5ResponseBodyDataDbClusterNetwork()
            self.network = temp_model.from_map(m['Network'])
        if m.get('OperationalStatus') is not None:
            temp_model = DescribeDbClusterV5ResponseBodyDataDbClusterOperationalStatus()
            self.operational_status = temp_model.from_map(m['OperationalStatus'])
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('ProductForm') is not None:
            self.product_form = m.get('ProductForm')
        if m.get('ResourceAssociations') is not None:
            temp_model = DescribeDbClusterV5ResponseBodyDataDbClusterResourceAssociations()
            self.resource_associations = temp_model.from_map(m['ResourceAssociations'])
        if m.get('ResourceSpec') is not None:
            temp_model = DescribeDbClusterV5ResponseBodyDataDbClusterResourceSpec()
            self.resource_spec = temp_model.from_map(m['ResourceSpec'])
        if m.get('User') is not None:
            temp_model = DescribeDbClusterV5ResponseBodyDataDbClusterUser()
            self.user = temp_model.from_map(m['User'])
        return self


class DescribeDbClusterV5ResponseBodyData(TeaModel):
    def __init__(
        self,
        db_cluster: DescribeDbClusterV5ResponseBodyDataDbCluster = None,
    ):
        self.db_cluster = db_cluster

    def validate(self):
        if self.db_cluster:
            self.db_cluster.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_cluster is not None:
            result['dbCluster'] = self.db_cluster.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dbCluster') is not None:
            temp_model = DescribeDbClusterV5ResponseBodyDataDbCluster()
            self.db_cluster = temp_model.from_map(m['dbCluster'])
        return self


class DescribeDbClusterV5ResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: DescribeDbClusterV5ResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        result_code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.result_code = result_code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.result_code is not None:
            result['resultCode'] = self.result_code
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('data') is not None:
            temp_model = DescribeDbClusterV5ResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('resultCode') is not None:
            self.result_code = m.get('resultCode')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class DescribeDbClusterV5Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDbClusterV5ResponseBody = None,
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
            temp_model = DescribeDbClusterV5ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceReleaseRequest(TeaModel):
    def __init__(
        self,
        db_cluster_id: str = None,
        ins_type: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.db_cluster_id = db_cluster_id
        self.ins_type = ins_type
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_cluster_id is not None:
            result['DbClusterId'] = self.db_cluster_id
        if self.ins_type is not None:
            result['InsType'] = self.ins_type
        if self.region_id is not None:
            result['regionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbClusterId') is not None:
            self.db_cluster_id = m.get('DbClusterId')
        if m.get('InsType') is not None:
            self.ins_type = m.get('InsType')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        return self


class DescribeInstanceReleaseResponseBodyReleaseInfo(TeaModel):
    def __init__(
        self,
        compose_name: str = None,
        description: str = None,
        image: str = None,
        ins_type: str = None,
        major_version: str = None,
        minor_version: str = None,
    ):
        self.compose_name = compose_name
        self.description = description
        self.image = image
        self.ins_type = ins_type
        self.major_version = major_version
        self.minor_version = minor_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compose_name is not None:
            result['ComposeName'] = self.compose_name
        if self.description is not None:
            result['Description'] = self.description
        if self.image is not None:
            result['Image'] = self.image
        if self.ins_type is not None:
            result['InsType'] = self.ins_type
        if self.major_version is not None:
            result['MajorVersion'] = self.major_version
        if self.minor_version is not None:
            result['MinorVersion'] = self.minor_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComposeName') is not None:
            self.compose_name = m.get('ComposeName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('InsType') is not None:
            self.ins_type = m.get('InsType')
        if m.get('MajorVersion') is not None:
            self.major_version = m.get('MajorVersion')
        if m.get('MinorVersion') is not None:
            self.minor_version = m.get('MinorVersion')
        return self


class DescribeInstanceReleaseResponseBody(TeaModel):
    def __init__(
        self,
        release_info: DescribeInstanceReleaseResponseBodyReleaseInfo = None,
        request_id: str = None,
        http_status_code: int = None,
        message: str = None,
        result_code: str = None,
        success: bool = None,
    ):
        self.release_info = release_info
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.message = message
        self.result_code = result_code
        self.success = success

    def validate(self):
        if self.release_info:
            self.release_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.release_info is not None:
            result['ReleaseInfo'] = self.release_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.result_code is not None:
            result['resultCode'] = self.result_code
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReleaseInfo') is not None:
            temp_model = DescribeInstanceReleaseResponseBodyReleaseInfo()
            self.release_info = temp_model.from_map(m['ReleaseInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('resultCode') is not None:
            self.result_code = m.get('resultCode')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class DescribeInstanceReleaseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeInstanceReleaseResponseBody = None,
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
            temp_model = DescribeInstanceReleaseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMajorCustomerInstancesRequest(TeaModel):
    def __init__(
        self,
        customer_ids: str = None,
    ):
        # This parameter is required.
        self.customer_ids = customer_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.customer_ids is not None:
            result['CustomerIds'] = self.customer_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomerIds') is not None:
            self.customer_ids = m.get('CustomerIds')
        return self


class DescribeMajorCustomerInstancesResponseBodyMajorCustomerInstances(TeaModel):
    def __init__(
        self,
        customer_id: str = None,
        customer_name: str = None,
        db_version: str = None,
        engine_version: str = None,
        gc_level: str = None,
        gmt_created: str = None,
        gmt_modified: str = None,
        instance_id: str = None,
        ranking: int = None,
        region_id: str = None,
        status: str = None,
        user_id: str = None,
        user_name: str = None,
    ):
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.db_version = db_version
        self.engine_version = engine_version
        self.gc_level = gc_level
        self.gmt_created = gmt_created
        self.gmt_modified = gmt_modified
        self.instance_id = instance_id
        self.ranking = ranking
        self.region_id = region_id
        self.status = status
        self.user_id = user_id
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.customer_id is not None:
            result['CustomerId'] = self.customer_id
        if self.customer_name is not None:
            result['CustomerName'] = self.customer_name
        if self.db_version is not None:
            result['DbVersion'] = self.db_version
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.gc_level is not None:
            result['GcLevel'] = self.gc_level
        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ranking is not None:
            result['Ranking'] = self.ranking
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomerId') is not None:
            self.customer_id = m.get('CustomerId')
        if m.get('CustomerName') is not None:
            self.customer_name = m.get('CustomerName')
        if m.get('DbVersion') is not None:
            self.db_version = m.get('DbVersion')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('GcLevel') is not None:
            self.gc_level = m.get('GcLevel')
        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Ranking') is not None:
            self.ranking = m.get('Ranking')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class DescribeMajorCustomerInstancesResponseBody(TeaModel):
    def __init__(
        self,
        major_customer_instances: List[DescribeMajorCustomerInstancesResponseBodyMajorCustomerInstances] = None,
        request_id: str = None,
    ):
        self.major_customer_instances = major_customer_instances
        self.request_id = request_id

    def validate(self):
        if self.major_customer_instances:
            for k in self.major_customer_instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MajorCustomerInstances'] = []
        if self.major_customer_instances is not None:
            for k in self.major_customer_instances:
                result['MajorCustomerInstances'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.major_customer_instances = []
        if m.get('MajorCustomerInstances') is not None:
            for k in m.get('MajorCustomerInstances'):
                temp_model = DescribeMajorCustomerInstancesResponseBodyMajorCustomerInstances()
                self.major_customer_instances.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeMajorCustomerInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeMajorCustomerInstancesResponseBody = None,
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
            temp_model = DescribeMajorCustomerInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMajorCustomersResponseBodyMajorCustomers(TeaModel):
    def __init__(
        self,
        area: str = None,
        customer_id: str = None,
        customer_name: str = None,
        description: str = None,
        industry: str = None,
        pd: str = None,
        pdsa: str = None,
        ranking: int = None,
        rd: str = None,
        sa: str = None,
    ):
        self.area = area
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.description = description
        self.industry = industry
        self.pd = pd
        self.pdsa = pdsa
        self.ranking = ranking
        self.rd = rd
        self.sa = sa

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.area is not None:
            result['Area'] = self.area
        if self.customer_id is not None:
            result['CustomerId'] = self.customer_id
        if self.customer_name is not None:
            result['CustomerName'] = self.customer_name
        if self.description is not None:
            result['Description'] = self.description
        if self.industry is not None:
            result['Industry'] = self.industry
        if self.pd is not None:
            result['Pd'] = self.pd
        if self.pdsa is not None:
            result['Pdsa'] = self.pdsa
        if self.ranking is not None:
            result['Ranking'] = self.ranking
        if self.rd is not None:
            result['Rd'] = self.rd
        if self.sa is not None:
            result['Sa'] = self.sa
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Area') is not None:
            self.area = m.get('Area')
        if m.get('CustomerId') is not None:
            self.customer_id = m.get('CustomerId')
        if m.get('CustomerName') is not None:
            self.customer_name = m.get('CustomerName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Industry') is not None:
            self.industry = m.get('Industry')
        if m.get('Pd') is not None:
            self.pd = m.get('Pd')
        if m.get('Pdsa') is not None:
            self.pdsa = m.get('Pdsa')
        if m.get('Ranking') is not None:
            self.ranking = m.get('Ranking')
        if m.get('Rd') is not None:
            self.rd = m.get('Rd')
        if m.get('Sa') is not None:
            self.sa = m.get('Sa')
        return self


class DescribeMajorCustomersResponseBody(TeaModel):
    def __init__(
        self,
        major_customers: List[DescribeMajorCustomersResponseBodyMajorCustomers] = None,
        request_id: str = None,
    ):
        self.major_customers = major_customers
        self.request_id = request_id

    def validate(self):
        if self.major_customers:
            for k in self.major_customers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MajorCustomers'] = []
        if self.major_customers is not None:
            for k in self.major_customers:
                result['MajorCustomers'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.major_customers = []
        if m.get('MajorCustomers') is not None:
            for k in m.get('MajorCustomers'):
                temp_model = DescribeMajorCustomersResponseBodyMajorCustomers()
                self.major_customers.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeMajorCustomersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeMajorCustomersResponseBody = None,
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
            temp_model = DescribeMajorCustomersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeOssBucketReplicationProgressRequest(TeaModel):
    def __init__(
        self,
        ak: str = None,
        bucket_name: str = None,
        encrypted_sk: str = None,
        endpoint: str = None,
        region_id: str = None,
        rule_id: str = None,
    ):
        self.ak = ak
        self.bucket_name = bucket_name
        self.encrypted_sk = encrypted_sk
        self.endpoint = endpoint
        self.region_id = region_id
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ak is not None:
            result['Ak'] = self.ak
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.encrypted_sk is not None:
            result['EncryptedSk'] = self.encrypted_sk
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ak') is not None:
            self.ak = m.get('Ak')
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('EncryptedSk') is not None:
            self.encrypted_sk = m.get('EncryptedSk')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class DescribeOssBucketReplicationProgressResponseBodyProgress(TeaModel):
    def __init__(
        self,
        enable_historical_object_replication: bool = None,
        historical_object_progress: float = None,
        new_object_progress: int = None,
        replication_rule_id: str = None,
        replication_status: str = None,
        target_bucket_location: str = None,
        target_bucket_name: str = None,
        target_cloud: str = None,
        target_cloud_location: str = None,
    ):
        self.enable_historical_object_replication = enable_historical_object_replication
        self.historical_object_progress = historical_object_progress
        self.new_object_progress = new_object_progress
        self.replication_rule_id = replication_rule_id
        self.replication_status = replication_status
        self.target_bucket_location = target_bucket_location
        self.target_bucket_name = target_bucket_name
        self.target_cloud = target_cloud
        self.target_cloud_location = target_cloud_location

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_historical_object_replication is not None:
            result['enableHistoricalObjectReplication'] = self.enable_historical_object_replication
        if self.historical_object_progress is not None:
            result['historicalObjectProgress'] = self.historical_object_progress
        if self.new_object_progress is not None:
            result['newObjectProgress'] = self.new_object_progress
        if self.replication_rule_id is not None:
            result['replicationRuleId'] = self.replication_rule_id
        if self.replication_status is not None:
            result['replicationStatus'] = self.replication_status
        if self.target_bucket_location is not None:
            result['targetBucketLocation'] = self.target_bucket_location
        if self.target_bucket_name is not None:
            result['targetBucketName'] = self.target_bucket_name
        if self.target_cloud is not None:
            result['targetCloud'] = self.target_cloud
        if self.target_cloud_location is not None:
            result['targetCloudLocation'] = self.target_cloud_location
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enableHistoricalObjectReplication') is not None:
            self.enable_historical_object_replication = m.get('enableHistoricalObjectReplication')
        if m.get('historicalObjectProgress') is not None:
            self.historical_object_progress = m.get('historicalObjectProgress')
        if m.get('newObjectProgress') is not None:
            self.new_object_progress = m.get('newObjectProgress')
        if m.get('replicationRuleId') is not None:
            self.replication_rule_id = m.get('replicationRuleId')
        if m.get('replicationStatus') is not None:
            self.replication_status = m.get('replicationStatus')
        if m.get('targetBucketLocation') is not None:
            self.target_bucket_location = m.get('targetBucketLocation')
        if m.get('targetBucketName') is not None:
            self.target_bucket_name = m.get('targetBucketName')
        if m.get('targetCloud') is not None:
            self.target_cloud = m.get('targetCloud')
        if m.get('targetCloudLocation') is not None:
            self.target_cloud_location = m.get('targetCloudLocation')
        return self


class DescribeOssBucketReplicationProgressResponseBody(TeaModel):
    def __init__(
        self,
        progress: DescribeOssBucketReplicationProgressResponseBodyProgress = None,
        request_id: str = None,
        http_status_code: int = None,
        message: str = None,
        result_code: str = None,
        success: bool = None,
    ):
        self.progress = progress
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.message = message
        self.result_code = result_code
        self.success = success

    def validate(self):
        if self.progress:
            self.progress.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.progress is not None:
            result['Progress'] = self.progress.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.result_code is not None:
            result['resultCode'] = self.result_code
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Progress') is not None:
            temp_model = DescribeOssBucketReplicationProgressResponseBodyProgress()
            self.progress = temp_model.from_map(m['Progress'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('resultCode') is not None:
            self.result_code = m.get('resultCode')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class DescribeOssBucketReplicationProgressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeOssBucketReplicationProgressResponseBody = None,
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
            temp_model = DescribeOssBucketReplicationProgressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeOssBucketReplicationRulesRequest(TeaModel):
    def __init__(
        self,
        ak: str = None,
        bucket_name: str = None,
        encrypted_sk: str = None,
        endpoint: str = None,
        region_id: str = None,
    ):
        self.ak = ak
        self.bucket_name = bucket_name
        self.encrypted_sk = encrypted_sk
        self.endpoint = endpoint
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ak is not None:
            result['Ak'] = self.ak
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.encrypted_sk is not None:
            result['EncryptedSk'] = self.encrypted_sk
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ak') is not None:
            self.ak = m.get('Ak')
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('EncryptedSk') is not None:
            self.encrypted_sk = m.get('EncryptedSk')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeOssBucketReplicationRulesResponseBodyResultRules(TeaModel):
    def __init__(
        self,
        enable_historical_object_replication: bool = None,
        object_prefix_list: List[str] = None,
        replica_kms_key_id: str = None,
        replication_action_list: List[str] = None,
        replication_rule_id: str = None,
        replication_status: str = None,
        sse_kms_encrypted_objects_status: str = None,
        sync_role: str = None,
        target_bucket_location: str = None,
        target_bucket_name: str = None,
        target_cloud: str = None,
        target_cloud_location: str = None,
    ):
        self.enable_historical_object_replication = enable_historical_object_replication
        self.object_prefix_list = object_prefix_list
        self.replica_kms_key_id = replica_kms_key_id
        self.replication_action_list = replication_action_list
        self.replication_rule_id = replication_rule_id
        self.replication_status = replication_status
        self.sse_kms_encrypted_objects_status = sse_kms_encrypted_objects_status
        self.sync_role = sync_role
        self.target_bucket_location = target_bucket_location
        self.target_bucket_name = target_bucket_name
        self.target_cloud = target_cloud
        self.target_cloud_location = target_cloud_location

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_historical_object_replication is not None:
            result['enableHistoricalObjectReplication'] = self.enable_historical_object_replication
        if self.object_prefix_list is not None:
            result['objectPrefixList'] = self.object_prefix_list
        if self.replica_kms_key_id is not None:
            result['replicaKmsKeyID'] = self.replica_kms_key_id
        if self.replication_action_list is not None:
            result['replicationActionList'] = self.replication_action_list
        if self.replication_rule_id is not None:
            result['replicationRuleID'] = self.replication_rule_id
        if self.replication_status is not None:
            result['replicationStatus'] = self.replication_status
        if self.sse_kms_encrypted_objects_status is not None:
            result['sseKmsEncryptedObjectsStatus'] = self.sse_kms_encrypted_objects_status
        if self.sync_role is not None:
            result['syncRole'] = self.sync_role
        if self.target_bucket_location is not None:
            result['targetBucketLocation'] = self.target_bucket_location
        if self.target_bucket_name is not None:
            result['targetBucketName'] = self.target_bucket_name
        if self.target_cloud is not None:
            result['targetCloud'] = self.target_cloud
        if self.target_cloud_location is not None:
            result['targetCloudLocation'] = self.target_cloud_location
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enableHistoricalObjectReplication') is not None:
            self.enable_historical_object_replication = m.get('enableHistoricalObjectReplication')
        if m.get('objectPrefixList') is not None:
            self.object_prefix_list = m.get('objectPrefixList')
        if m.get('replicaKmsKeyID') is not None:
            self.replica_kms_key_id = m.get('replicaKmsKeyID')
        if m.get('replicationActionList') is not None:
            self.replication_action_list = m.get('replicationActionList')
        if m.get('replicationRuleID') is not None:
            self.replication_rule_id = m.get('replicationRuleID')
        if m.get('replicationStatus') is not None:
            self.replication_status = m.get('replicationStatus')
        if m.get('sseKmsEncryptedObjectsStatus') is not None:
            self.sse_kms_encrypted_objects_status = m.get('sseKmsEncryptedObjectsStatus')
        if m.get('syncRole') is not None:
            self.sync_role = m.get('syncRole')
        if m.get('targetBucketLocation') is not None:
            self.target_bucket_location = m.get('targetBucketLocation')
        if m.get('targetBucketName') is not None:
            self.target_bucket_name = m.get('targetBucketName')
        if m.get('targetCloud') is not None:
            self.target_cloud = m.get('targetCloud')
        if m.get('targetCloudLocation') is not None:
            self.target_cloud_location = m.get('targetCloudLocation')
        return self


class DescribeOssBucketReplicationRulesResponseBodyResult(TeaModel):
    def __init__(
        self,
        rules: List[DescribeOssBucketReplicationRulesResponseBodyResultRules] = None,
    ):
        self.rules = rules

    def validate(self):
        if self.rules:
            for k in self.rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['Rules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.rules = []
        if m.get('Rules') is not None:
            for k in m.get('Rules'):
                temp_model = DescribeOssBucketReplicationRulesResponseBodyResultRules()
                self.rules.append(temp_model.from_map(k))
        return self


class DescribeOssBucketReplicationRulesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: DescribeOssBucketReplicationRulesResponseBodyResult = None,
        http_status_code: int = None,
        message: str = None,
        result_code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.result = result
        self.http_status_code = http_status_code
        self.message = message
        self.result_code = result_code
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.result_code is not None:
            result['resultCode'] = self.result_code
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DescribeOssBucketReplicationRulesResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('resultCode') is not None:
            self.result_code = m.get('resultCode')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class DescribeOssBucketReplicationRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeOssBucketReplicationRulesResponseBody = None,
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
            temp_model = DescribeOssBucketReplicationRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeOssInfoRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        encrypted: bool = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        self.encrypted = encrypted
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.encrypted is not None:
            result['Encrypted'] = self.encrypted
        if self.region_id is not None:
            result['regionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('Encrypted') is not None:
            self.encrypted = m.get('Encrypted')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        return self


class DescribeOssInfoResponseBodyOssInfo(TeaModel):
    def __init__(
        self,
        access_id: str = None,
        access_secret: str = None,
        bucket: str = None,
        db_cluster_id: str = None,
        endpoint: str = None,
        keep_days: str = None,
        owner_id: str = None,
        policy_name: str = None,
        region: str = None,
        role_name: str = None,
        url: str = None,
        user_name: str = None,
    ):
        self.access_id = access_id
        self.access_secret = access_secret
        self.bucket = bucket
        self.db_cluster_id = db_cluster_id
        self.endpoint = endpoint
        self.keep_days = keep_days
        self.owner_id = owner_id
        self.policy_name = policy_name
        self.region = region
        self.role_name = role_name
        self.url = url
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_id is not None:
            result['accessId'] = self.access_id
        if self.access_secret is not None:
            result['accessSecret'] = self.access_secret
        if self.bucket is not None:
            result['bucket'] = self.bucket
        if self.db_cluster_id is not None:
            result['dbClusterId'] = self.db_cluster_id
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint
        if self.keep_days is not None:
            result['keepDays'] = self.keep_days
        if self.owner_id is not None:
            result['ownerId'] = self.owner_id
        if self.policy_name is not None:
            result['policyName'] = self.policy_name
        if self.region is not None:
            result['region'] = self.region
        if self.role_name is not None:
            result['roleName'] = self.role_name
        if self.url is not None:
            result['url'] = self.url
        if self.user_name is not None:
            result['userName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessId') is not None:
            self.access_id = m.get('accessId')
        if m.get('accessSecret') is not None:
            self.access_secret = m.get('accessSecret')
        if m.get('bucket') is not None:
            self.bucket = m.get('bucket')
        if m.get('dbClusterId') is not None:
            self.db_cluster_id = m.get('dbClusterId')
        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')
        if m.get('keepDays') is not None:
            self.keep_days = m.get('keepDays')
        if m.get('ownerId') is not None:
            self.owner_id = m.get('ownerId')
        if m.get('policyName') is not None:
            self.policy_name = m.get('policyName')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('roleName') is not None:
            self.role_name = m.get('roleName')
        if m.get('url') is not None:
            self.url = m.get('url')
        if m.get('userName') is not None:
            self.user_name = m.get('userName')
        return self


class DescribeOssInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        http_status_code: int = None,
        message: str = None,
        oss_info: DescribeOssInfoResponseBodyOssInfo = None,
        result_code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.message = message
        self.oss_info = oss_info
        self.result_code = result_code
        self.success = success

    def validate(self):
        if self.oss_info:
            self.oss_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.oss_info is not None:
            result['ossInfo'] = self.oss_info.to_map()
        if self.result_code is not None:
            result['resultCode'] = self.result_code
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('ossInfo') is not None:
            temp_model = DescribeOssInfoResponseBodyOssInfo()
            self.oss_info = temp_model.from_map(m['ossInfo'])
        if m.get('resultCode') is not None:
            self.result_code = m.get('resultCode')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class DescribeOssInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeOssInfoResponseBody = None,
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
            temp_model = DescribeOssInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeOssInfoV2Request(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        ali_uid: int = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        self.ali_uid = ali_uid
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.ali_uid is not None:
            result['aliUid'] = self.ali_uid
        if self.region_id is not None:
            result['regionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('aliUid') is not None:
            self.ali_uid = m.get('aliUid')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        return self


class DescribeOssInfoV2ResponseBodyOssInfo(TeaModel):
    def __init__(
        self,
        access_id: str = None,
        access_secret: str = None,
        bucket: str = None,
        endpoint: str = None,
        keep_days: str = None,
        owner_id: str = None,
        policy_name: str = None,
        region: str = None,
        role_name: str = None,
        user_name: str = None,
    ):
        self.access_id = access_id
        self.access_secret = access_secret
        self.bucket = bucket
        self.endpoint = endpoint
        self.keep_days = keep_days
        self.owner_id = owner_id
        self.policy_name = policy_name
        self.region = region
        self.role_name = role_name
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_id is not None:
            result['accessId'] = self.access_id
        if self.access_secret is not None:
            result['accessSecret'] = self.access_secret
        if self.bucket is not None:
            result['bucket'] = self.bucket
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint
        if self.keep_days is not None:
            result['keepDays'] = self.keep_days
        if self.owner_id is not None:
            result['ownerId'] = self.owner_id
        if self.policy_name is not None:
            result['policyName'] = self.policy_name
        if self.region is not None:
            result['region'] = self.region
        if self.role_name is not None:
            result['roleName'] = self.role_name
        if self.user_name is not None:
            result['userName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessId') is not None:
            self.access_id = m.get('accessId')
        if m.get('accessSecret') is not None:
            self.access_secret = m.get('accessSecret')
        if m.get('bucket') is not None:
            self.bucket = m.get('bucket')
        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')
        if m.get('keepDays') is not None:
            self.keep_days = m.get('keepDays')
        if m.get('ownerId') is not None:
            self.owner_id = m.get('ownerId')
        if m.get('policyName') is not None:
            self.policy_name = m.get('policyName')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('roleName') is not None:
            self.role_name = m.get('roleName')
        if m.get('userName') is not None:
            self.user_name = m.get('userName')
        return self


class DescribeOssInfoV2ResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        http_status_code: int = None,
        message: str = None,
        oss_info: DescribeOssInfoV2ResponseBodyOssInfo = None,
        result_code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.message = message
        self.oss_info = oss_info
        self.result_code = result_code
        self.success = success

    def validate(self):
        if self.oss_info:
            self.oss_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.oss_info is not None:
            result['ossInfo'] = self.oss_info.to_map()
        if self.result_code is not None:
            result['resultCode'] = self.result_code
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('ossInfo') is not None:
            temp_model = DescribeOssInfoV2ResponseBodyOssInfo()
            self.oss_info = temp_model.from_map(m['ossInfo'])
        if m.get('resultCode') is not None:
            self.result_code = m.get('resultCode')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class DescribeOssInfoV2Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeOssInfoV2ResponseBody = None,
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
            temp_model = DescribeOssInfoV2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTaskStatusRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        task_id: int = None,
    ):
        self.dbcluster_id = dbcluster_id
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribeTaskStatusResponseBodyTaskInfo(TeaModel):
    def __init__(
        self,
        status: str = None,
        task_id: int = None,
    ):
        self.status = status
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribeTaskStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_info: DescribeTaskStatusResponseBodyTaskInfo = None,
    ):
        self.request_id = request_id
        self.task_info = task_info

    def validate(self):
        if self.task_info:
            self.task_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_info is not None:
            result['TaskInfo'] = self.task_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskInfo') is not None:
            temp_model = DescribeTaskStatusResponseBodyTaskInfo()
            self.task_info = temp_model.from_map(m['TaskInfo'])
        return self


class DescribeTaskStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeTaskStatusResponseBody = None,
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
            temp_model = DescribeTaskStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateZeroEtlTokenRequest(TeaModel):
    def __init__(
        self,
        content: str = None,
        dbcluster_id: str = None,
        polar_dbinstance_id: str = None,
        region_id: str = None,
        uid: str = None,
    ):
        self.content = content
        self.dbcluster_id = dbcluster_id
        self.polar_dbinstance_id = polar_dbinstance_id
        self.region_id = region_id
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.polar_dbinstance_id is not None:
            result['PolarDBInstanceId'] = self.polar_dbinstance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.uid is not None:
            result['UID'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('PolarDBInstanceId') is not None:
            self.polar_dbinstance_id = m.get('PolarDBInstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UID') is not None:
            self.uid = m.get('UID')
        return self


class GenerateZeroEtlTokenResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        token: str = None,
    ):
        self.request_id = request_id
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class GenerateZeroEtlTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GenerateZeroEtlTokenResponseBody = None,
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
            temp_model = GenerateZeroEtlTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAATOssInfoForADBRequest(TeaModel):
    def __init__(
        self,
        ali_uid: str = None,
        polar_dbinstance_id: str = None,
        region_id: str = None,
    ):
        self.ali_uid = ali_uid
        self.polar_dbinstance_id = polar_dbinstance_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.polar_dbinstance_id is not None:
            result['PolarDBInstanceId'] = self.polar_dbinstance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('PolarDBInstanceId') is not None:
            self.polar_dbinstance_id = m.get('PolarDBInstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetAATOssInfoForADBResponseBodyOssInfo(TeaModel):
    def __init__(
        self,
        access_key_id: str = None,
        access_key_secret: str = None,
        oss_bucket: str = None,
        oss_endpoint: str = None,
        path: str = None,
        security_token: str = None,
    ):
        self.access_key_id = access_key_id
        self.access_key_secret = access_key_secret
        self.oss_bucket = oss_bucket
        self.oss_endpoint = oss_endpoint
        self.path = path
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id
        if self.access_key_secret is not None:
            result['AccessKeySecret'] = self.access_key_secret
        if self.oss_bucket is not None:
            result['OssBucket'] = self.oss_bucket
        if self.oss_endpoint is not None:
            result['OssEndpoint'] = self.oss_endpoint
        if self.path is not None:
            result['Path'] = self.path
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')
        if m.get('AccessKeySecret') is not None:
            self.access_key_secret = m.get('AccessKeySecret')
        if m.get('OssBucket') is not None:
            self.oss_bucket = m.get('OssBucket')
        if m.get('OssEndpoint') is not None:
            self.oss_endpoint = m.get('OssEndpoint')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class GetAATOssInfoForADBResponseBody(TeaModel):
    def __init__(
        self,
        oss_info: GetAATOssInfoForADBResponseBodyOssInfo = None,
        request_id: str = None,
    ):
        self.oss_info = oss_info
        self.request_id = request_id

    def validate(self):
        if self.oss_info:
            self.oss_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oss_info is not None:
            result['OssInfo'] = self.oss_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OssInfo') is not None:
            temp_model = GetAATOssInfoForADBResponseBodyOssInfo()
            self.oss_info = temp_model.from_map(m['OssInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAATOssInfoForADBResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAATOssInfoForADBResponseBody = None,
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
            temp_model = GetAATOssInfoForADBResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetBucketTransferAccelerationRequest(TeaModel):
    def __init__(
        self,
        ak: str = None,
        bucket_name: str = None,
        encrypted_sk: str = None,
        endpoint: str = None,
        region_id: str = None,
    ):
        self.ak = ak
        self.bucket_name = bucket_name
        self.encrypted_sk = encrypted_sk
        self.endpoint = endpoint
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ak is not None:
            result['Ak'] = self.ak
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.encrypted_sk is not None:
            result['EncryptedSk'] = self.encrypted_sk
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ak') is not None:
            self.ak = m.get('Ak')
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('EncryptedSk') is not None:
            self.encrypted_sk = m.get('EncryptedSk')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetBucketTransferAccelerationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: bool = None,
        http_status_code: int = None,
        message: str = None,
        result_code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.result_code = result_code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['data'] = self.data
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.result_code is not None:
            result['resultCode'] = self.result_code
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('resultCode') is not None:
            self.result_code = m.get('resultCode')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetBucketTransferAccelerationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetBucketTransferAccelerationResponseBody = None,
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
            temp_model = GetBucketTransferAccelerationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDBResourceGroupRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        group_name: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        self.group_name = group_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.region_id is not None:
            result['regionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        return self


class GetDBResourceGroupResponseBodyGroupsInfoRules(TeaModel):
    def __init__(
        self,
        group_name: str = None,
        query_time: str = None,
        target_group_name: str = None,
    ):
        self.group_name = group_name
        self.query_time = query_time
        self.target_group_name = target_group_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.query_time is not None:
            result['QueryTime'] = self.query_time
        if self.target_group_name is not None:
            result['TargetGroupName'] = self.target_group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('QueryTime') is not None:
            self.query_time = m.get('QueryTime')
        if m.get('TargetGroupName') is not None:
            self.target_group_name = m.get('TargetGroupName')
        return self


class GetDBResourceGroupResponseBodyGroupsInfo(TeaModel):
    def __init__(
        self,
        auto_stop_interval: str = None,
        cluster_mode: str = None,
        cluster_size_resource: str = None,
        create_time: str = None,
        elastic_min_compute_resource: str = None,
        enable_spot: str = None,
        engine: str = None,
        engine_params: Dict[str, Any] = None,
        group_name: str = None,
        group_type: str = None,
        group_user_list: List[str] = None,
        group_users: str = None,
        max_cluster_count: int = None,
        max_compute_resource: str = None,
        max_gpu_quantity: int = None,
        message: str = None,
        min_cluster_count: int = None,
        min_compute_resource: str = None,
        min_gpu_quantity: int = None,
        node_num: int = None,
        rules: List[GetDBResourceGroupResponseBodyGroupsInfoRules] = None,
        running_cluster_count: int = None,
        spec_name: str = None,
        status: str = None,
        target_resource_group_name: str = None,
        update_time: str = None,
    ):
        self.auto_stop_interval = auto_stop_interval
        self.cluster_mode = cluster_mode
        self.cluster_size_resource = cluster_size_resource
        self.create_time = create_time
        self.elastic_min_compute_resource = elastic_min_compute_resource
        self.enable_spot = enable_spot
        self.engine = engine
        self.engine_params = engine_params
        self.group_name = group_name
        self.group_type = group_type
        self.group_user_list = group_user_list
        self.group_users = group_users
        self.max_cluster_count = max_cluster_count
        self.max_compute_resource = max_compute_resource
        self.max_gpu_quantity = max_gpu_quantity
        # This parameter is required.
        self.message = message
        self.min_cluster_count = min_cluster_count
        self.min_compute_resource = min_compute_resource
        self.min_gpu_quantity = min_gpu_quantity
        self.node_num = node_num
        self.rules = rules
        self.running_cluster_count = running_cluster_count
        self.spec_name = spec_name
        self.status = status
        self.target_resource_group_name = target_resource_group_name
        self.update_time = update_time

    def validate(self):
        if self.rules:
            for k in self.rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_stop_interval is not None:
            result['AutoStopInterval'] = self.auto_stop_interval
        if self.cluster_mode is not None:
            result['ClusterMode'] = self.cluster_mode
        if self.cluster_size_resource is not None:
            result['ClusterSizeResource'] = self.cluster_size_resource
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.elastic_min_compute_resource is not None:
            result['ElasticMinComputeResource'] = self.elastic_min_compute_resource
        if self.enable_spot is not None:
            result['EnableSpot'] = self.enable_spot
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.engine_params is not None:
            result['EngineParams'] = self.engine_params
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.group_type is not None:
            result['GroupType'] = self.group_type
        if self.group_user_list is not None:
            result['GroupUserList'] = self.group_user_list
        if self.group_users is not None:
            result['GroupUsers'] = self.group_users
        if self.max_cluster_count is not None:
            result['MaxClusterCount'] = self.max_cluster_count
        if self.max_compute_resource is not None:
            result['MaxComputeResource'] = self.max_compute_resource
        if self.max_gpu_quantity is not None:
            result['MaxGpuQuantity'] = self.max_gpu_quantity
        if self.message is not None:
            result['Message'] = self.message
        if self.min_cluster_count is not None:
            result['MinClusterCount'] = self.min_cluster_count
        if self.min_compute_resource is not None:
            result['MinComputeResource'] = self.min_compute_resource
        if self.min_gpu_quantity is not None:
            result['MinGpuQuantity'] = self.min_gpu_quantity
        if self.node_num is not None:
            result['NodeNum'] = self.node_num
        result['Rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['Rules'].append(k.to_map() if k else None)
        if self.running_cluster_count is not None:
            result['RunningClusterCount'] = self.running_cluster_count
        if self.spec_name is not None:
            result['SpecName'] = self.spec_name
        if self.status is not None:
            result['Status'] = self.status
        if self.target_resource_group_name is not None:
            result['TargetResourceGroupName'] = self.target_resource_group_name
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoStopInterval') is not None:
            self.auto_stop_interval = m.get('AutoStopInterval')
        if m.get('ClusterMode') is not None:
            self.cluster_mode = m.get('ClusterMode')
        if m.get('ClusterSizeResource') is not None:
            self.cluster_size_resource = m.get('ClusterSizeResource')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ElasticMinComputeResource') is not None:
            self.elastic_min_compute_resource = m.get('ElasticMinComputeResource')
        if m.get('EnableSpot') is not None:
            self.enable_spot = m.get('EnableSpot')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('EngineParams') is not None:
            self.engine_params = m.get('EngineParams')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('GroupType') is not None:
            self.group_type = m.get('GroupType')
        if m.get('GroupUserList') is not None:
            self.group_user_list = m.get('GroupUserList')
        if m.get('GroupUsers') is not None:
            self.group_users = m.get('GroupUsers')
        if m.get('MaxClusterCount') is not None:
            self.max_cluster_count = m.get('MaxClusterCount')
        if m.get('MaxComputeResource') is not None:
            self.max_compute_resource = m.get('MaxComputeResource')
        if m.get('MaxGpuQuantity') is not None:
            self.max_gpu_quantity = m.get('MaxGpuQuantity')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('MinClusterCount') is not None:
            self.min_cluster_count = m.get('MinClusterCount')
        if m.get('MinComputeResource') is not None:
            self.min_compute_resource = m.get('MinComputeResource')
        if m.get('MinGpuQuantity') is not None:
            self.min_gpu_quantity = m.get('MinGpuQuantity')
        if m.get('NodeNum') is not None:
            self.node_num = m.get('NodeNum')
        self.rules = []
        if m.get('Rules') is not None:
            for k in m.get('Rules'):
                temp_model = GetDBResourceGroupResponseBodyGroupsInfoRules()
                self.rules.append(temp_model.from_map(k))
        if m.get('RunningClusterCount') is not None:
            self.running_cluster_count = m.get('RunningClusterCount')
        if m.get('SpecName') is not None:
            self.spec_name = m.get('SpecName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TargetResourceGroupName') is not None:
            self.target_resource_group_name = m.get('TargetResourceGroupName')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class GetDBResourceGroupResponseBody(TeaModel):
    def __init__(
        self,
        groups_info: List[GetDBResourceGroupResponseBodyGroupsInfo] = None,
        request_id: str = None,
    ):
        self.groups_info = groups_info
        self.request_id = request_id

    def validate(self):
        if self.groups_info:
            for k in self.groups_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['GroupsInfo'] = []
        if self.groups_info is not None:
            for k in self.groups_info:
                result['GroupsInfo'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.groups_info = []
        if m.get('GroupsInfo') is not None:
            for k in m.get('GroupsInfo'):
                temp_model = GetDBResourceGroupResponseBodyGroupsInfo()
                self.groups_info.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDBResourceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDBResourceGroupResponseBody = None,
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
            temp_model = GetDBResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInitDmsAIServiceK8sEnvInfoRequest(TeaModel):
    def __init__(
        self,
        ali_uid: str = None,
        dbcluster_id: str = None,
        resource_group_name: str = None,
    ):
        # This parameter is required.
        self.ali_uid = ali_uid
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        self.resource_group_name = resource_group_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.resource_group_name is not None:
            result['ResourceGroupName'] = self.resource_group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('ResourceGroupName') is not None:
            self.resource_group_name = m.get('ResourceGroupName')
        return self


class GetInitDmsAIServiceK8sEnvInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        annotations: Dict[str, str] = None,
        api_server_proxy_pvl_address: str = None,
        asi_cluster_id: str = None,
        db_cluster_id: str = None,
        engine_params: Dict[str, str] = None,
        k_8s_namespace: str = None,
        k_8s_service_account: str = None,
        labels: Dict[str, str] = None,
        max_compute_resource: str = None,
        min_compute_resource: str = None,
        pool_engine: str = None,
        pool_name: str = None,
        pool_type: str = None,
        priority_class_name: str = None,
        ready: bool = None,
        runtime_class_name: str = None,
        service_account_token: str = None,
        volumes_json: str = None,
    ):
        self.annotations = annotations
        self.api_server_proxy_pvl_address = api_server_proxy_pvl_address
        self.asi_cluster_id = asi_cluster_id
        self.db_cluster_id = db_cluster_id
        self.engine_params = engine_params
        self.k_8s_namespace = k_8s_namespace
        self.k_8s_service_account = k_8s_service_account
        self.labels = labels
        self.max_compute_resource = max_compute_resource
        self.min_compute_resource = min_compute_resource
        self.pool_engine = pool_engine
        self.pool_name = pool_name
        self.pool_type = pool_type
        self.priority_class_name = priority_class_name
        self.ready = ready
        self.runtime_class_name = runtime_class_name
        self.service_account_token = service_account_token
        self.volumes_json = volumes_json

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.annotations is not None:
            result['Annotations'] = self.annotations
        if self.api_server_proxy_pvl_address is not None:
            result['ApiServerProxyPvlAddress'] = self.api_server_proxy_pvl_address
        if self.asi_cluster_id is not None:
            result['AsiClusterId'] = self.asi_cluster_id
        if self.db_cluster_id is not None:
            result['DbClusterId'] = self.db_cluster_id
        if self.engine_params is not None:
            result['EngineParams'] = self.engine_params
        if self.k_8s_namespace is not None:
            result['K8sNamespace'] = self.k_8s_namespace
        if self.k_8s_service_account is not None:
            result['K8sServiceAccount'] = self.k_8s_service_account
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.max_compute_resource is not None:
            result['MaxComputeResource'] = self.max_compute_resource
        if self.min_compute_resource is not None:
            result['MinComputeResource'] = self.min_compute_resource
        if self.pool_engine is not None:
            result['PoolEngine'] = self.pool_engine
        if self.pool_name is not None:
            result['PoolName'] = self.pool_name
        if self.pool_type is not None:
            result['PoolType'] = self.pool_type
        if self.priority_class_name is not None:
            result['PriorityClassName'] = self.priority_class_name
        if self.ready is not None:
            result['Ready'] = self.ready
        if self.runtime_class_name is not None:
            result['RuntimeClassName'] = self.runtime_class_name
        if self.service_account_token is not None:
            result['ServiceAccountToken'] = self.service_account_token
        if self.volumes_json is not None:
            result['VolumesJson'] = self.volumes_json
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Annotations') is not None:
            self.annotations = m.get('Annotations')
        if m.get('ApiServerProxyPvlAddress') is not None:
            self.api_server_proxy_pvl_address = m.get('ApiServerProxyPvlAddress')
        if m.get('AsiClusterId') is not None:
            self.asi_cluster_id = m.get('AsiClusterId')
        if m.get('DbClusterId') is not None:
            self.db_cluster_id = m.get('DbClusterId')
        if m.get('EngineParams') is not None:
            self.engine_params = m.get('EngineParams')
        if m.get('K8sNamespace') is not None:
            self.k_8s_namespace = m.get('K8sNamespace')
        if m.get('K8sServiceAccount') is not None:
            self.k_8s_service_account = m.get('K8sServiceAccount')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('MaxComputeResource') is not None:
            self.max_compute_resource = m.get('MaxComputeResource')
        if m.get('MinComputeResource') is not None:
            self.min_compute_resource = m.get('MinComputeResource')
        if m.get('PoolEngine') is not None:
            self.pool_engine = m.get('PoolEngine')
        if m.get('PoolName') is not None:
            self.pool_name = m.get('PoolName')
        if m.get('PoolType') is not None:
            self.pool_type = m.get('PoolType')
        if m.get('PriorityClassName') is not None:
            self.priority_class_name = m.get('PriorityClassName')
        if m.get('Ready') is not None:
            self.ready = m.get('Ready')
        if m.get('RuntimeClassName') is not None:
            self.runtime_class_name = m.get('RuntimeClassName')
        if m.get('ServiceAccountToken') is not None:
            self.service_account_token = m.get('ServiceAccountToken')
        if m.get('VolumesJson') is not None:
            self.volumes_json = m.get('VolumesJson')
        return self


class GetInitDmsAIServiceK8sEnvInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        success: bool = None,
        data: GetInitDmsAIServiceK8sEnvInfoResponseBodyData = None,
    ):
        self.code = code
        self.message = message
        self.success = success
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        if self.data is not None:
            result['data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('data') is not None:
            temp_model = GetInitDmsAIServiceK8sEnvInfoResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        return self


class GetInitDmsAIServiceK8sEnvInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetInitDmsAIServiceK8sEnvInfoResponseBody = None,
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
            temp_model = GetInitDmsAIServiceK8sEnvInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSparkAppMetricsRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class GetSparkAppMetricsResponseBodyDataScanMetrics(TeaModel):
    def __init__(
        self,
        output_rows_count: int = None,
        total_read_file_size_in_byte: int = None,
    ):
        self.output_rows_count = output_rows_count
        self.total_read_file_size_in_byte = total_read_file_size_in_byte

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.output_rows_count is not None:
            result['OutputRowsCount'] = self.output_rows_count
        if self.total_read_file_size_in_byte is not None:
            result['TotalReadFileSizeInByte'] = self.total_read_file_size_in_byte
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OutputRowsCount') is not None:
            self.output_rows_count = m.get('OutputRowsCount')
        if m.get('TotalReadFileSizeInByte') is not None:
            self.total_read_file_size_in_byte = m.get('TotalReadFileSizeInByte')
        return self


class GetSparkAppMetricsResponseBodyData(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        attempt_id: str = None,
        event_log_path: str = None,
        finished: bool = None,
        scan_metrics: GetSparkAppMetricsResponseBodyDataScanMetrics = None,
    ):
        self.app_id = app_id
        self.attempt_id = attempt_id
        self.event_log_path = event_log_path
        self.finished = finished
        self.scan_metrics = scan_metrics

    def validate(self):
        if self.scan_metrics:
            self.scan_metrics.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.attempt_id is not None:
            result['AttemptId'] = self.attempt_id
        if self.event_log_path is not None:
            result['EventLogPath'] = self.event_log_path
        if self.finished is not None:
            result['Finished'] = self.finished
        if self.scan_metrics is not None:
            result['ScanMetrics'] = self.scan_metrics.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AttemptId') is not None:
            self.attempt_id = m.get('AttemptId')
        if m.get('EventLogPath') is not None:
            self.event_log_path = m.get('EventLogPath')
        if m.get('Finished') is not None:
            self.finished = m.get('Finished')
        if m.get('ScanMetrics') is not None:
            temp_model = GetSparkAppMetricsResponseBodyDataScanMetrics()
            self.scan_metrics = temp_model.from_map(m['ScanMetrics'])
        return self


class GetSparkAppMetricsResponseBody(TeaModel):
    def __init__(
        self,
        data: GetSparkAppMetricsResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetSparkAppMetricsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetSparkAppMetricsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSparkAppMetricsResponseBody = None,
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
            temp_model = GetSparkAppMetricsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSparkSubmitInfoRequest(TeaModel):
    def __init__(
        self,
        conf: str = None,
        dbcluster_id: str = None,
        resource_group_name: str = None,
        trusted_caller_parent_id: int = None,
        trusted_caller_type: str = None,
        trusted_caller_uid: int = None,
    ):
        self.conf = conf
        self.dbcluster_id = dbcluster_id
        self.resource_group_name = resource_group_name
        self.trusted_caller_parent_id = trusted_caller_parent_id
        self.trusted_caller_type = trusted_caller_type
        self.trusted_caller_uid = trusted_caller_uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conf is not None:
            result['Conf'] = self.conf
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.resource_group_name is not None:
            result['ResourceGroupName'] = self.resource_group_name
        if self.trusted_caller_parent_id is not None:
            result['TrustedCallerParentId'] = self.trusted_caller_parent_id
        if self.trusted_caller_type is not None:
            result['TrustedCallerType'] = self.trusted_caller_type
        if self.trusted_caller_uid is not None:
            result['TrustedCallerUid'] = self.trusted_caller_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Conf') is not None:
            self.conf = m.get('Conf')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('ResourceGroupName') is not None:
            self.resource_group_name = m.get('ResourceGroupName')
        if m.get('TrustedCallerParentId') is not None:
            self.trusted_caller_parent_id = m.get('TrustedCallerParentId')
        if m.get('TrustedCallerType') is not None:
            self.trusted_caller_type = m.get('TrustedCallerType')
        if m.get('TrustedCallerUid') is not None:
            self.trusted_caller_uid = m.get('TrustedCallerUid')
        return self


class GetSparkSubmitInfoResponseBody(TeaModel):
    def __init__(
        self,
        data: Dict[str, Any] = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetSparkSubmitInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSparkSubmitInfoResponseBody = None,
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
            temp_model = GetSparkSubmitInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InitDmsAIServiceK8sEnvRequest(TeaModel):
    def __init__(
        self,
        ali_uid: str = None,
        dbcluster_id: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        # This parameter is required.
        self.ali_uid = ali_uid
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # This parameter is required.
        self.v_switch_id = v_switch_id
        # This parameter is required.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class InitDmsAIServiceK8sEnvResponseBody(TeaModel):
    def __init__(
        self,
        task_id: int = None,
    ):
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class InitDmsAIServiceK8sEnvResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: InitDmsAIServiceK8sEnvResponseBody = None,
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
            temp_model = InitDmsAIServiceK8sEnvResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InnerGetSparkAppInfoRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        trusted_caller_parent_id: int = None,
        trusted_caller_type: str = None,
        trusted_caller_uid: int = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        # This parameter is required.
        self.trusted_caller_parent_id = trusted_caller_parent_id
        # This parameter is required.
        self.trusted_caller_type = trusted_caller_type
        # This parameter is required.
        self.trusted_caller_uid = trusted_caller_uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.trusted_caller_parent_id is not None:
            result['TrustedCallerParentId'] = self.trusted_caller_parent_id
        if self.trusted_caller_type is not None:
            result['TrustedCallerType'] = self.trusted_caller_type
        if self.trusted_caller_uid is not None:
            result['TrustedCallerUid'] = self.trusted_caller_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('TrustedCallerParentId') is not None:
            self.trusted_caller_parent_id = m.get('TrustedCallerParentId')
        if m.get('TrustedCallerType') is not None:
            self.trusted_caller_type = m.get('TrustedCallerType')
        if m.get('TrustedCallerUid') is not None:
            self.trusted_caller_uid = m.get('TrustedCallerUid')
        return self


class InnerGetSparkAppInfoResponseBody(TeaModel):
    def __init__(
        self,
        data: SparkAppInfo = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = SparkAppInfo()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class InnerGetSparkAppInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: InnerGetSparkAppInfoResponseBody = None,
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
            temp_model = InnerGetSparkAppInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InnerGetSparkAppLogRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        log_length: int = None,
        trusted_caller_parent_id: int = None,
        trusted_caller_type: str = None,
        trusted_caller_uid: int = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        self.log_length = log_length
        # This parameter is required.
        self.trusted_caller_parent_id = trusted_caller_parent_id
        # This parameter is required.
        self.trusted_caller_type = trusted_caller_type
        # This parameter is required.
        self.trusted_caller_uid = trusted_caller_uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.log_length is not None:
            result['LogLength'] = self.log_length
        if self.trusted_caller_parent_id is not None:
            result['TrustedCallerParentId'] = self.trusted_caller_parent_id
        if self.trusted_caller_type is not None:
            result['TrustedCallerType'] = self.trusted_caller_type
        if self.trusted_caller_uid is not None:
            result['TrustedCallerUid'] = self.trusted_caller_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('LogLength') is not None:
            self.log_length = m.get('LogLength')
        if m.get('TrustedCallerParentId') is not None:
            self.trusted_caller_parent_id = m.get('TrustedCallerParentId')
        if m.get('TrustedCallerType') is not None:
            self.trusted_caller_type = m.get('TrustedCallerType')
        if m.get('TrustedCallerUid') is not None:
            self.trusted_caller_uid = m.get('TrustedCallerUid')
        return self


class InnerGetSparkAppLogResponseBodyData(TeaModel):
    def __init__(
        self,
        log_content: str = None,
        message: str = None,
    ):
        self.log_content = log_content
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_content is not None:
            result['LogContent'] = self.log_content
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogContent') is not None:
            self.log_content = m.get('LogContent')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class InnerGetSparkAppLogResponseBody(TeaModel):
    def __init__(
        self,
        data: InnerGetSparkAppLogResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = InnerGetSparkAppLogResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class InnerGetSparkAppLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: InnerGetSparkAppLogResponseBody = None,
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
            temp_model = InnerGetSparkAppLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InnerGetSparkAppStateRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        trusted_caller_parent_id: int = None,
        trusted_caller_type: str = None,
        trusted_caller_uid: int = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        # This parameter is required.
        self.trusted_caller_parent_id = trusted_caller_parent_id
        # This parameter is required.
        self.trusted_caller_type = trusted_caller_type
        # This parameter is required.
        self.trusted_caller_uid = trusted_caller_uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.trusted_caller_parent_id is not None:
            result['TrustedCallerParentId'] = self.trusted_caller_parent_id
        if self.trusted_caller_type is not None:
            result['TrustedCallerType'] = self.trusted_caller_type
        if self.trusted_caller_uid is not None:
            result['TrustedCallerUid'] = self.trusted_caller_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('TrustedCallerParentId') is not None:
            self.trusted_caller_parent_id = m.get('TrustedCallerParentId')
        if m.get('TrustedCallerType') is not None:
            self.trusted_caller_type = m.get('TrustedCallerType')
        if m.get('TrustedCallerUid') is not None:
            self.trusted_caller_uid = m.get('TrustedCallerUid')
        return self


class InnerGetSparkAppStateResponseBodyData(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        message: str = None,
        state: str = None,
    ):
        self.app_id = app_id
        self.app_name = app_name
        self.message = message
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.message is not None:
            result['Message'] = self.message
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class InnerGetSparkAppStateResponseBody(TeaModel):
    def __init__(
        self,
        data: InnerGetSparkAppStateResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = InnerGetSparkAppStateResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class InnerGetSparkAppStateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: InnerGetSparkAppStateResponseBody = None,
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
            temp_model = InnerGetSparkAppStateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InnerGetSparkAppWebUiAddressRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        trusted_caller_parent_id: int = None,
        trusted_caller_type: str = None,
        trusted_caller_uid: int = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        # This parameter is required.
        self.trusted_caller_parent_id = trusted_caller_parent_id
        # This parameter is required.
        self.trusted_caller_type = trusted_caller_type
        # This parameter is required.
        self.trusted_caller_uid = trusted_caller_uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.trusted_caller_parent_id is not None:
            result['TrustedCallerParentId'] = self.trusted_caller_parent_id
        if self.trusted_caller_type is not None:
            result['TrustedCallerType'] = self.trusted_caller_type
        if self.trusted_caller_uid is not None:
            result['TrustedCallerUid'] = self.trusted_caller_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('TrustedCallerParentId') is not None:
            self.trusted_caller_parent_id = m.get('TrustedCallerParentId')
        if m.get('TrustedCallerType') is not None:
            self.trusted_caller_type = m.get('TrustedCallerType')
        if m.get('TrustedCallerUid') is not None:
            self.trusted_caller_uid = m.get('TrustedCallerUid')
        return self


class InnerGetSparkAppWebUiAddressResponseBodyData(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        expiration_time_in_millis: int = None,
        web_ui_address: str = None,
    ):
        self.app_id = app_id
        self.expiration_time_in_millis = expiration_time_in_millis
        self.web_ui_address = web_ui_address

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.expiration_time_in_millis is not None:
            result['ExpirationTimeInMillis'] = self.expiration_time_in_millis
        if self.web_ui_address is not None:
            result['WebUiAddress'] = self.web_ui_address
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ExpirationTimeInMillis') is not None:
            self.expiration_time_in_millis = m.get('ExpirationTimeInMillis')
        if m.get('WebUiAddress') is not None:
            self.web_ui_address = m.get('WebUiAddress')
        return self


class InnerGetSparkAppWebUiAddressResponseBody(TeaModel):
    def __init__(
        self,
        data: InnerGetSparkAppWebUiAddressResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = InnerGetSparkAppWebUiAddressResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class InnerGetSparkAppWebUiAddressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: InnerGetSparkAppWebUiAddressResponseBody = None,
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
            temp_model = InnerGetSparkAppWebUiAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InnerKillSparkAppRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        trusted_caller_parent_id: int = None,
        trusted_caller_type: str = None,
        trusted_caller_uid: int = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        # This parameter is required.
        self.trusted_caller_parent_id = trusted_caller_parent_id
        # This parameter is required.
        self.trusted_caller_type = trusted_caller_type
        # This parameter is required.
        self.trusted_caller_uid = trusted_caller_uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.trusted_caller_parent_id is not None:
            result['TrustedCallerParentId'] = self.trusted_caller_parent_id
        if self.trusted_caller_type is not None:
            result['TrustedCallerType'] = self.trusted_caller_type
        if self.trusted_caller_uid is not None:
            result['TrustedCallerUid'] = self.trusted_caller_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('TrustedCallerParentId') is not None:
            self.trusted_caller_parent_id = m.get('TrustedCallerParentId')
        if m.get('TrustedCallerType') is not None:
            self.trusted_caller_type = m.get('TrustedCallerType')
        if m.get('TrustedCallerUid') is not None:
            self.trusted_caller_uid = m.get('TrustedCallerUid')
        return self


class InnerKillSparkAppResponseBodyData(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        message: str = None,
        state: str = None,
    ):
        self.app_id = app_id
        self.app_name = app_name
        self.message = message
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.message is not None:
            result['Message'] = self.message
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class InnerKillSparkAppResponseBody(TeaModel):
    def __init__(
        self,
        data: InnerKillSparkAppResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = InnerKillSparkAppResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class InnerKillSparkAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: InnerKillSparkAppResponseBody = None,
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
            temp_model = InnerKillSparkAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InnerSubmitSparkAppRequest(TeaModel):
    def __init__(
        self,
        agent_source: str = None,
        agent_version: str = None,
        app_name: str = None,
        app_type: str = None,
        dbcluster_id: str = None,
        data: str = None,
        resource_group_name: str = None,
        template_file_id: int = None,
        trusted_caller_parent_id: int = None,
        trusted_caller_type: str = None,
        trusted_caller_uid: int = None,
    ):
        self.agent_source = agent_source
        self.agent_version = agent_version
        self.app_name = app_name
        # This parameter is required.
        self.app_type = app_type
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # This parameter is required.
        self.data = data
        self.resource_group_name = resource_group_name
        self.template_file_id = template_file_id
        # This parameter is required.
        self.trusted_caller_parent_id = trusted_caller_parent_id
        # This parameter is required.
        self.trusted_caller_type = trusted_caller_type
        # This parameter is required.
        self.trusted_caller_uid = trusted_caller_uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_source is not None:
            result['AgentSource'] = self.agent_source
        if self.agent_version is not None:
            result['AgentVersion'] = self.agent_version
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.data is not None:
            result['Data'] = self.data
        if self.resource_group_name is not None:
            result['ResourceGroupName'] = self.resource_group_name
        if self.template_file_id is not None:
            result['TemplateFileId'] = self.template_file_id
        if self.trusted_caller_parent_id is not None:
            result['TrustedCallerParentId'] = self.trusted_caller_parent_id
        if self.trusted_caller_type is not None:
            result['TrustedCallerType'] = self.trusted_caller_type
        if self.trusted_caller_uid is not None:
            result['TrustedCallerUid'] = self.trusted_caller_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentSource') is not None:
            self.agent_source = m.get('AgentSource')
        if m.get('AgentVersion') is not None:
            self.agent_version = m.get('AgentVersion')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ResourceGroupName') is not None:
            self.resource_group_name = m.get('ResourceGroupName')
        if m.get('TemplateFileId') is not None:
            self.template_file_id = m.get('TemplateFileId')
        if m.get('TrustedCallerParentId') is not None:
            self.trusted_caller_parent_id = m.get('TrustedCallerParentId')
        if m.get('TrustedCallerType') is not None:
            self.trusted_caller_type = m.get('TrustedCallerType')
        if m.get('TrustedCallerUid') is not None:
            self.trusted_caller_uid = m.get('TrustedCallerUid')
        return self


class InnerSubmitSparkAppResponseBodyData(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        message: str = None,
        state: str = None,
    ):
        self.app_id = app_id
        self.app_name = app_name
        self.message = message
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.message is not None:
            result['Message'] = self.message
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class InnerSubmitSparkAppResponseBody(TeaModel):
    def __init__(
        self,
        data: InnerSubmitSparkAppResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = InnerSubmitSparkAppResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class InnerSubmitSparkAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: InnerSubmitSparkAppResponseBody = None,
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
            temp_model = InnerSubmitSparkAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListServiceQuotasRequest(TeaModel):
    def __init__(
        self,
        aliyun_uid: str = None,
        bid: str = None,
        category_enum: str = None,
        dimension_group_key: str = None,
        dimensions: str = None,
        keyword: str = None,
        max_results: int = None,
        next_token: str = None,
        product_code: str = None,
        quota_action_code: str = None,
        sort_field: str = None,
        sort_order: str = None,
        use_cache: bool = None,
    ):
        self.aliyun_uid = aliyun_uid
        self.bid = bid
        self.category_enum = category_enum
        self.dimension_group_key = dimension_group_key
        self.dimensions = dimensions
        self.keyword = keyword
        self.max_results = max_results
        self.next_token = next_token
        self.product_code = product_code
        self.quota_action_code = quota_action_code
        self.sort_field = sort_field
        self.sort_order = sort_order
        self.use_cache = use_cache

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyun_uid is not None:
            result['AliyunUid'] = self.aliyun_uid
        if self.bid is not None:
            result['Bid'] = self.bid
        if self.category_enum is not None:
            result['CategoryEnum'] = self.category_enum
        if self.dimension_group_key is not None:
            result['DimensionGroupKey'] = self.dimension_group_key
        if self.dimensions is not None:
            result['Dimensions'] = self.dimensions
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.quota_action_code is not None:
            result['QuotaActionCode'] = self.quota_action_code
        if self.sort_field is not None:
            result['SortField'] = self.sort_field
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        if self.use_cache is not None:
            result['UseCache'] = self.use_cache
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunUid') is not None:
            self.aliyun_uid = m.get('AliyunUid')
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')
        if m.get('CategoryEnum') is not None:
            self.category_enum = m.get('CategoryEnum')
        if m.get('DimensionGroupKey') is not None:
            self.dimension_group_key = m.get('DimensionGroupKey')
        if m.get('Dimensions') is not None:
            self.dimensions = m.get('Dimensions')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('QuotaActionCode') is not None:
            self.quota_action_code = m.get('QuotaActionCode')
        if m.get('SortField') is not None:
            self.sort_field = m.get('SortField')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        if m.get('UseCache') is not None:
            self.use_cache = m.get('UseCache')
        return self


class ListServiceQuotasResponseBodyQuotas(TeaModel):
    def __init__(
        self,
        adjustable: bool = None,
        applicable: str = None,
        applicable_type: str = None,
        dimensions: str = None,
        expire_time: str = None,
        quota_action_code: str = None,
        total_quota: float = None,
        total_usage: float = None,
        unadjustable_detail: str = None,
        unit: str = None,
    ):
        self.adjustable = adjustable
        self.applicable = applicable
        self.applicable_type = applicable_type
        self.dimensions = dimensions
        self.expire_time = expire_time
        self.quota_action_code = quota_action_code
        self.total_quota = total_quota
        self.total_usage = total_usage
        self.unadjustable_detail = unadjustable_detail
        self.unit = unit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adjustable is not None:
            result['Adjustable'] = self.adjustable
        if self.applicable is not None:
            result['Applicable'] = self.applicable
        if self.applicable_type is not None:
            result['ApplicableType'] = self.applicable_type
        if self.dimensions is not None:
            result['Dimensions'] = self.dimensions
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.quota_action_code is not None:
            result['QuotaActionCode'] = self.quota_action_code
        if self.total_quota is not None:
            result['TotalQuota'] = self.total_quota
        if self.total_usage is not None:
            result['TotalUsage'] = self.total_usage
        if self.unadjustable_detail is not None:
            result['UnadjustableDetail'] = self.unadjustable_detail
        if self.unit is not None:
            result['Unit'] = self.unit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Adjustable') is not None:
            self.adjustable = m.get('Adjustable')
        if m.get('Applicable') is not None:
            self.applicable = m.get('Applicable')
        if m.get('ApplicableType') is not None:
            self.applicable_type = m.get('ApplicableType')
        if m.get('Dimensions') is not None:
            self.dimensions = m.get('Dimensions')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('QuotaActionCode') is not None:
            self.quota_action_code = m.get('QuotaActionCode')
        if m.get('TotalQuota') is not None:
            self.total_quota = m.get('TotalQuota')
        if m.get('TotalUsage') is not None:
            self.total_usage = m.get('TotalUsage')
        if m.get('UnadjustableDetail') is not None:
            self.unadjustable_detail = m.get('UnadjustableDetail')
        if m.get('Unit') is not None:
            self.unit = m.get('Unit')
        return self


class ListServiceQuotasResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        quotas: List[ListServiceQuotasResponseBodyQuotas] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.quotas = quotas
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.quotas:
            for k in self.quotas:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['Quotas'] = []
        if self.quotas is not None:
            for k in self.quotas:
                result['Quotas'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.quotas = []
        if m.get('Quotas') is not None:
            for k in m.get('Quotas'):
                temp_model = ListServiceQuotasResponseBodyQuotas()
                self.quotas.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListServiceQuotasResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListServiceQuotasResponseBody = None,
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
            temp_model = ListServiceQuotasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MigrateDBClusterRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        dry_run: bool = None,
        link_switch_mode: str = None,
        new_shard_number: int = None,
        switch_time: str = None,
        switch_time_mode: int = None,
    ):
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        self.dry_run = dry_run
        self.link_switch_mode = link_switch_mode
        self.new_shard_number = new_shard_number
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ssZ
        self.switch_time = switch_time
        self.switch_time_mode = switch_time_mode

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.link_switch_mode is not None:
            result['LinkSwitchMode'] = self.link_switch_mode
        if self.new_shard_number is not None:
            result['NewShardNumber'] = self.new_shard_number
        if self.switch_time is not None:
            result['SwitchTime'] = self.switch_time
        if self.switch_time_mode is not None:
            result['SwitchTimeMode'] = self.switch_time_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('LinkSwitchMode') is not None:
            self.link_switch_mode = m.get('LinkSwitchMode')
        if m.get('NewShardNumber') is not None:
            self.new_shard_number = m.get('NewShardNumber')
        if m.get('SwitchTime') is not None:
            self.switch_time = m.get('SwitchTime')
        if m.get('SwitchTimeMode') is not None:
            self.switch_time_mode = m.get('SwitchTimeMode')
        return self


class MigrateDBClusterResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class MigrateDBClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: MigrateDBClusterResponseBody = None,
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
            temp_model = MigrateDBClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDBClusterConfigRequestConfigs(TeaModel):
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


class ModifyDBClusterConfigRequest(TeaModel):
    def __init__(
        self,
        configs: List[ModifyDBClusterConfigRequestConfigs] = None,
        dbcluster_id: str = None,
    ):
        self.configs = configs
        # This parameter is required.
        self.dbcluster_id = dbcluster_id

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
        result['Configs'] = []
        if self.configs is not None:
            for k in self.configs:
                result['Configs'].append(k.to_map() if k else None)
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.configs = []
        if m.get('Configs') is not None:
            for k in m.get('Configs'):
                temp_model = ModifyDBClusterConfigRequestConfigs()
                self.configs.append(temp_model.from_map(k))
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        return self


class ModifyDBClusterConfigShrinkRequest(TeaModel):
    def __init__(
        self,
        configs_shrink: str = None,
        dbcluster_id: str = None,
    ):
        self.configs_shrink = configs_shrink
        # This parameter is required.
        self.dbcluster_id = dbcluster_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.configs_shrink is not None:
            result['Configs'] = self.configs_shrink
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Configs') is not None:
            self.configs_shrink = m.get('Configs')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        return self


class ModifyDBClusterConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyDBClusterConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyDBClusterConfigResponseBody = None,
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
            temp_model = ModifyDBClusterConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyMajorCustomerRequest(TeaModel):
    def __init__(
        self,
        area: str = None,
        customer_id: int = None,
        customer_name: str = None,
        description: str = None,
        industry: str = None,
        pd: str = None,
        pdsa: str = None,
        ranking: int = None,
        rd: str = None,
        sa: str = None,
    ):
        self.area = area
        # This parameter is required.
        self.customer_id = customer_id
        # This parameter is required.
        self.customer_name = customer_name
        self.description = description
        self.industry = industry
        self.pd = pd
        self.pdsa = pdsa
        self.ranking = ranking
        self.rd = rd
        self.sa = sa

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.area is not None:
            result['Area'] = self.area
        if self.customer_id is not None:
            result['CustomerId'] = self.customer_id
        if self.customer_name is not None:
            result['CustomerName'] = self.customer_name
        if self.description is not None:
            result['Description'] = self.description
        if self.industry is not None:
            result['Industry'] = self.industry
        if self.pd is not None:
            result['Pd'] = self.pd
        if self.pdsa is not None:
            result['Pdsa'] = self.pdsa
        if self.ranking is not None:
            result['Ranking'] = self.ranking
        if self.rd is not None:
            result['Rd'] = self.rd
        if self.sa is not None:
            result['Sa'] = self.sa
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Area') is not None:
            self.area = m.get('Area')
        if m.get('CustomerId') is not None:
            self.customer_id = m.get('CustomerId')
        if m.get('CustomerName') is not None:
            self.customer_name = m.get('CustomerName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Industry') is not None:
            self.industry = m.get('Industry')
        if m.get('Pd') is not None:
            self.pd = m.get('Pd')
        if m.get('Pdsa') is not None:
            self.pdsa = m.get('Pdsa')
        if m.get('Ranking') is not None:
            self.ranking = m.get('Ranking')
        if m.get('Rd') is not None:
            self.rd = m.get('Rd')
        if m.get('Sa') is not None:
            self.sa = m.get('Sa')
        return self


class ModifyMajorCustomerResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyMajorCustomerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyMajorCustomerResponseBody = None,
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
            temp_model = ModifyMajorCustomerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyServiceQuotaRequest(TeaModel):
    def __init__(
        self,
        aliyun_uid: str = None,
        application_id: str = None,
        dimensions: Dict[str, Any] = None,
        product_code: str = None,
        quota_action_code: str = None,
        quota_category: str = None,
        reason: str = None,
        region_id: str = None,
        value: str = None,
    ):
        self.aliyun_uid = aliyun_uid
        self.application_id = application_id
        self.dimensions = dimensions
        self.product_code = product_code
        self.quota_action_code = quota_action_code
        self.quota_category = quota_category
        self.reason = reason
        self.region_id = region_id
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyun_uid is not None:
            result['AliyunUid'] = self.aliyun_uid
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.dimensions is not None:
            result['Dimensions'] = self.dimensions
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.quota_action_code is not None:
            result['QuotaActionCode'] = self.quota_action_code
        if self.quota_category is not None:
            result['QuotaCategory'] = self.quota_category
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunUid') is not None:
            self.aliyun_uid = m.get('AliyunUid')
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('Dimensions') is not None:
            self.dimensions = m.get('Dimensions')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('QuotaActionCode') is not None:
            self.quota_action_code = m.get('QuotaActionCode')
        if m.get('QuotaCategory') is not None:
            self.quota_category = m.get('QuotaCategory')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ModifyServiceQuotaShrinkRequest(TeaModel):
    def __init__(
        self,
        aliyun_uid: str = None,
        application_id: str = None,
        dimensions_shrink: str = None,
        product_code: str = None,
        quota_action_code: str = None,
        quota_category: str = None,
        reason: str = None,
        region_id: str = None,
        value: str = None,
    ):
        self.aliyun_uid = aliyun_uid
        self.application_id = application_id
        self.dimensions_shrink = dimensions_shrink
        self.product_code = product_code
        self.quota_action_code = quota_action_code
        self.quota_category = quota_category
        self.reason = reason
        self.region_id = region_id
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyun_uid is not None:
            result['AliyunUid'] = self.aliyun_uid
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.dimensions_shrink is not None:
            result['Dimensions'] = self.dimensions_shrink
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.quota_action_code is not None:
            result['QuotaActionCode'] = self.quota_action_code
        if self.quota_category is not None:
            result['QuotaCategory'] = self.quota_category
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunUid') is not None:
            self.aliyun_uid = m.get('AliyunUid')
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('Dimensions') is not None:
            self.dimensions_shrink = m.get('Dimensions')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('QuotaActionCode') is not None:
            self.quota_action_code = m.get('QuotaActionCode')
        if m.get('QuotaCategory') is not None:
            self.quota_category = m.get('QuotaCategory')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ModifyServiceQuotaResponseBody(TeaModel):
    def __init__(
        self,
        dimensions: Dict[str, str] = None,
        expire_time: str = None,
        quota_action_code: str = None,
        request_id: str = None,
        total_quota: int = None,
        total_usage: int = None,
    ):
        self.dimensions = dimensions
        self.expire_time = expire_time
        self.quota_action_code = quota_action_code
        self.request_id = request_id
        self.total_quota = total_quota
        self.total_usage = total_usage

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dimensions is not None:
            result['Dimensions'] = self.dimensions
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.quota_action_code is not None:
            result['QuotaActionCode'] = self.quota_action_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_quota is not None:
            result['TotalQuota'] = self.total_quota
        if self.total_usage is not None:
            result['TotalUsage'] = self.total_usage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Dimensions') is not None:
            self.dimensions = m.get('Dimensions')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('QuotaActionCode') is not None:
            self.quota_action_code = m.get('QuotaActionCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalQuota') is not None:
            self.total_quota = m.get('TotalQuota')
        if m.get('TotalUsage') is not None:
            self.total_usage = m.get('TotalUsage')
        return self


class ModifyServiceQuotaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyServiceQuotaResponseBody = None,
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
            temp_model = ModifyServiceQuotaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PreloadSparkAppMetricsRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class PreloadSparkAppMetricsResponseBodyDataScanMetrics(TeaModel):
    def __init__(
        self,
        output_rows_count: int = None,
        total_read_file_size_in_byte: int = None,
    ):
        self.output_rows_count = output_rows_count
        self.total_read_file_size_in_byte = total_read_file_size_in_byte

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.output_rows_count is not None:
            result['OutputRowsCount'] = self.output_rows_count
        if self.total_read_file_size_in_byte is not None:
            result['TotalReadFileSizeInByte'] = self.total_read_file_size_in_byte
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OutputRowsCount') is not None:
            self.output_rows_count = m.get('OutputRowsCount')
        if m.get('TotalReadFileSizeInByte') is not None:
            self.total_read_file_size_in_byte = m.get('TotalReadFileSizeInByte')
        return self


class PreloadSparkAppMetricsResponseBodyData(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        attempt_id: str = None,
        event_log_path: str = None,
        finished: bool = None,
        scan_metrics: PreloadSparkAppMetricsResponseBodyDataScanMetrics = None,
    ):
        self.app_id = app_id
        self.attempt_id = attempt_id
        self.event_log_path = event_log_path
        self.finished = finished
        self.scan_metrics = scan_metrics

    def validate(self):
        if self.scan_metrics:
            self.scan_metrics.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.attempt_id is not None:
            result['AttemptId'] = self.attempt_id
        if self.event_log_path is not None:
            result['EventLogPath'] = self.event_log_path
        if self.finished is not None:
            result['Finished'] = self.finished
        if self.scan_metrics is not None:
            result['ScanMetrics'] = self.scan_metrics.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AttemptId') is not None:
            self.attempt_id = m.get('AttemptId')
        if m.get('EventLogPath') is not None:
            self.event_log_path = m.get('EventLogPath')
        if m.get('Finished') is not None:
            self.finished = m.get('Finished')
        if m.get('ScanMetrics') is not None:
            temp_model = PreloadSparkAppMetricsResponseBodyDataScanMetrics()
            self.scan_metrics = temp_model.from_map(m['ScanMetrics'])
        return self


class PreloadSparkAppMetricsResponseBody(TeaModel):
    def __init__(
        self,
        data: PreloadSparkAppMetricsResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = PreloadSparkAppMetricsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class PreloadSparkAppMetricsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PreloadSparkAppMetricsResponseBody = None,
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
            temp_model = PreloadSparkAppMetricsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReleaseClusterVpcConnectionRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        engine: str = None,
        ins_type: str = None,
    ):
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        self.engine = engine
        self.ins_type = ins_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.ins_type is not None:
            result['InsType'] = self.ins_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('InsType') is not None:
            self.ins_type = m.get('InsType')
        return self


class ReleaseClusterVpcConnectionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ReleaseClusterVpcConnectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReleaseClusterVpcConnectionResponseBody = None,
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
            temp_model = ReleaseClusterVpcConnectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RestartDBClusterRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
    ):
        # This parameter is required.
        self.dbcluster_id = dbcluster_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        return self


class RestartDBClusterResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_id: str = None,
    ):
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class RestartDBClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RestartDBClusterResponseBody = None,
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
            temp_model = RestartDBClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RevokeInstanceEgressRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        endpoint_id: str = None,
        ins_type: str = None,
    ):
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # This parameter is required.
        self.endpoint_id = endpoint_id
        # This parameter is required.
        self.ins_type = ins_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        if self.ins_type is not None:
            result['InsType'] = self.ins_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        if m.get('InsType') is not None:
            self.ins_type = m.get('InsType')
        return self


class RevokeInstanceEgressResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RevokeInstanceEgressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RevokeInstanceEgressResponseBody = None,
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
            temp_model = RevokeInstanceEgressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetBucketTransferAccelerationRequest(TeaModel):
    def __init__(
        self,
        acceleration_enabled: bool = None,
        ak: str = None,
        bucket_name: str = None,
        encrypted_sk: str = None,
        endpoint: str = None,
        region_id: str = None,
    ):
        self.acceleration_enabled = acceleration_enabled
        self.ak = ak
        self.bucket_name = bucket_name
        self.encrypted_sk = encrypted_sk
        self.endpoint = endpoint
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acceleration_enabled is not None:
            result['AccelerationEnabled'] = self.acceleration_enabled
        if self.ak is not None:
            result['Ak'] = self.ak
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.encrypted_sk is not None:
            result['EncryptedSk'] = self.encrypted_sk
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccelerationEnabled') is not None:
            self.acceleration_enabled = m.get('AccelerationEnabled')
        if m.get('Ak') is not None:
            self.ak = m.get('Ak')
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('EncryptedSk') is not None:
            self.encrypted_sk = m.get('EncryptedSk')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class SetBucketTransferAccelerationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: bool = None,
        http_status_code: int = None,
        message: str = None,
        result_code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.result_code = result_code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['data'] = self.data
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.result_code is not None:
            result['resultCode'] = self.result_code
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('resultCode') is not None:
            self.result_code = m.get('resultCode')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class SetBucketTransferAccelerationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetBucketTransferAccelerationResponseBody = None,
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
            temp_model = SetBucketTransferAccelerationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartOssBucketReplicationRequest(TeaModel):
    def __init__(
        self,
        ak: str = None,
        encrypted_sk: str = None,
        endpoint: str = None,
        prefix_list: List[str] = None,
        region_id: str = None,
        replica_kms_key_id: str = None,
        role_name: str = None,
        source_bucket_name: str = None,
        sse_kms_encrypted_objects_status: str = None,
        target_bucket_name: str = None,
        target_region_code: str = None,
    ):
        self.ak = ak
        self.encrypted_sk = encrypted_sk
        self.endpoint = endpoint
        self.prefix_list = prefix_list
        self.region_id = region_id
        self.replica_kms_key_id = replica_kms_key_id
        self.role_name = role_name
        self.source_bucket_name = source_bucket_name
        self.sse_kms_encrypted_objects_status = sse_kms_encrypted_objects_status
        self.target_bucket_name = target_bucket_name
        self.target_region_code = target_region_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ak is not None:
            result['Ak'] = self.ak
        if self.encrypted_sk is not None:
            result['EncryptedSk'] = self.encrypted_sk
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.prefix_list is not None:
            result['PrefixList'] = self.prefix_list
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.replica_kms_key_id is not None:
            result['ReplicaKmsKeyId'] = self.replica_kms_key_id
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        if self.source_bucket_name is not None:
            result['SourceBucketName'] = self.source_bucket_name
        if self.sse_kms_encrypted_objects_status is not None:
            result['SseKmsEncryptedObjectsStatus'] = self.sse_kms_encrypted_objects_status
        if self.target_bucket_name is not None:
            result['TargetBucketName'] = self.target_bucket_name
        if self.target_region_code is not None:
            result['TargetRegionCode'] = self.target_region_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ak') is not None:
            self.ak = m.get('Ak')
        if m.get('EncryptedSk') is not None:
            self.encrypted_sk = m.get('EncryptedSk')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('PrefixList') is not None:
            self.prefix_list = m.get('PrefixList')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ReplicaKmsKeyId') is not None:
            self.replica_kms_key_id = m.get('ReplicaKmsKeyId')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        if m.get('SourceBucketName') is not None:
            self.source_bucket_name = m.get('SourceBucketName')
        if m.get('SseKmsEncryptedObjectsStatus') is not None:
            self.sse_kms_encrypted_objects_status = m.get('SseKmsEncryptedObjectsStatus')
        if m.get('TargetBucketName') is not None:
            self.target_bucket_name = m.get('TargetBucketName')
        if m.get('TargetRegionCode') is not None:
            self.target_region_code = m.get('TargetRegionCode')
        return self


class StartOssBucketReplicationShrinkRequest(TeaModel):
    def __init__(
        self,
        ak: str = None,
        encrypted_sk: str = None,
        endpoint: str = None,
        prefix_list_shrink: str = None,
        region_id: str = None,
        replica_kms_key_id: str = None,
        role_name: str = None,
        source_bucket_name: str = None,
        sse_kms_encrypted_objects_status: str = None,
        target_bucket_name: str = None,
        target_region_code: str = None,
    ):
        self.ak = ak
        self.encrypted_sk = encrypted_sk
        self.endpoint = endpoint
        self.prefix_list_shrink = prefix_list_shrink
        self.region_id = region_id
        self.replica_kms_key_id = replica_kms_key_id
        self.role_name = role_name
        self.source_bucket_name = source_bucket_name
        self.sse_kms_encrypted_objects_status = sse_kms_encrypted_objects_status
        self.target_bucket_name = target_bucket_name
        self.target_region_code = target_region_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ak is not None:
            result['Ak'] = self.ak
        if self.encrypted_sk is not None:
            result['EncryptedSk'] = self.encrypted_sk
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.prefix_list_shrink is not None:
            result['PrefixList'] = self.prefix_list_shrink
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.replica_kms_key_id is not None:
            result['ReplicaKmsKeyId'] = self.replica_kms_key_id
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        if self.source_bucket_name is not None:
            result['SourceBucketName'] = self.source_bucket_name
        if self.sse_kms_encrypted_objects_status is not None:
            result['SseKmsEncryptedObjectsStatus'] = self.sse_kms_encrypted_objects_status
        if self.target_bucket_name is not None:
            result['TargetBucketName'] = self.target_bucket_name
        if self.target_region_code is not None:
            result['TargetRegionCode'] = self.target_region_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ak') is not None:
            self.ak = m.get('Ak')
        if m.get('EncryptedSk') is not None:
            self.encrypted_sk = m.get('EncryptedSk')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('PrefixList') is not None:
            self.prefix_list_shrink = m.get('PrefixList')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ReplicaKmsKeyId') is not None:
            self.replica_kms_key_id = m.get('ReplicaKmsKeyId')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        if m.get('SourceBucketName') is not None:
            self.source_bucket_name = m.get('SourceBucketName')
        if m.get('SseKmsEncryptedObjectsStatus') is not None:
            self.sse_kms_encrypted_objects_status = m.get('SseKmsEncryptedObjectsStatus')
        if m.get('TargetBucketName') is not None:
            self.target_bucket_name = m.get('TargetBucketName')
        if m.get('TargetRegionCode') is not None:
            self.target_region_code = m.get('TargetRegionCode')
        return self


class StartOssBucketReplicationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        http_status_code: int = None,
        message: str = None,
        result_code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.message = message
        self.result_code = result_code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.result_code is not None:
            result['resultCode'] = self.result_code
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('resultCode') is not None:
            self.result_code = m.get('resultCode')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class StartOssBucketReplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartOssBucketReplicationResponseBody = None,
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
            temp_model = StartOssBucketReplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


