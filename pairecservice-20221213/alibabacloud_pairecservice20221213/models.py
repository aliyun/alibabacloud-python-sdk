# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class ExperimentReportValue(TeaModel):
    def __init__(
        self,
        baseline: bool = None,
        metric_results: Dict[str, dict] = None,
    ):
        self.baseline = baseline
        self.metric_results = metric_results

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.baseline is not None:
            result['Baseline'] = self.baseline
        if self.metric_results is not None:
            result['MetricResults'] = self.metric_results
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Baseline') is not None:
            self.baseline = m.get('Baseline')
        if m.get('MetricResults') is not None:
            self.metric_results = m.get('MetricResults')
        return self


class BackflowFeatureConsistencyCheckJobDataRequest(TeaModel):
    def __init__(
        self,
        feature_consistency_check_job_config_id: str = None,
        instance_id: str = None,
        item_features: str = None,
        log_item_id: str = None,
        log_request_id: str = None,
        log_request_time: int = None,
        log_user_id: str = None,
        scene_name: str = None,
        scores: str = None,
        user_features: str = None,
    ):
        # This parameter is required.
        self.feature_consistency_check_job_config_id = feature_consistency_check_job_config_id
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.item_features = item_features
        # This parameter is required.
        self.log_item_id = log_item_id
        # This parameter is required.
        self.log_request_id = log_request_id
        # This parameter is required.
        self.log_request_time = log_request_time
        # This parameter is required.
        self.log_user_id = log_user_id
        # This parameter is required.
        self.scene_name = scene_name
        # This parameter is required.
        self.scores = scores
        # This parameter is required.
        self.user_features = user_features

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.feature_consistency_check_job_config_id is not None:
            result['FeatureConsistencyCheckJobConfigId'] = self.feature_consistency_check_job_config_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.item_features is not None:
            result['ItemFeatures'] = self.item_features
        if self.log_item_id is not None:
            result['LogItemId'] = self.log_item_id
        if self.log_request_id is not None:
            result['LogRequestId'] = self.log_request_id
        if self.log_request_time is not None:
            result['LogRequestTime'] = self.log_request_time
        if self.log_user_id is not None:
            result['LogUserId'] = self.log_user_id
        if self.scene_name is not None:
            result['SceneName'] = self.scene_name
        if self.scores is not None:
            result['Scores'] = self.scores
        if self.user_features is not None:
            result['UserFeatures'] = self.user_features
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FeatureConsistencyCheckJobConfigId') is not None:
            self.feature_consistency_check_job_config_id = m.get('FeatureConsistencyCheckJobConfigId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ItemFeatures') is not None:
            self.item_features = m.get('ItemFeatures')
        if m.get('LogItemId') is not None:
            self.log_item_id = m.get('LogItemId')
        if m.get('LogRequestId') is not None:
            self.log_request_id = m.get('LogRequestId')
        if m.get('LogRequestTime') is not None:
            self.log_request_time = m.get('LogRequestTime')
        if m.get('LogUserId') is not None:
            self.log_user_id = m.get('LogUserId')
        if m.get('SceneName') is not None:
            self.scene_name = m.get('SceneName')
        if m.get('Scores') is not None:
            self.scores = m.get('Scores')
        if m.get('UserFeatures') is not None:
            self.user_features = m.get('UserFeatures')
        return self


class BackflowFeatureConsistencyCheckJobDataResponseBody(TeaModel):
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


class BackflowFeatureConsistencyCheckJobDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BackflowFeatureConsistencyCheckJobDataResponseBody = None,
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
            temp_model = BackflowFeatureConsistencyCheckJobDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckInstanceResourcesRequest(TeaModel):
    def __init__(
        self,
        type: str = None,
        uri: str = None,
    ):
        # This parameter is required.
        self.type = type
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.uri is not None:
            result['Uri'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        return self


class CheckInstanceResourcesResponseBodyResources(TeaModel):
    def __init__(
        self,
        status: str = None,
        type: str = None,
        uri: str = None,
    ):
        self.status = status
        self.type = type
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.uri is not None:
            result['Uri'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        return self


class CheckInstanceResourcesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resources: List[CheckInstanceResourcesResponseBodyResources] = None,
    ):
        self.request_id = request_id
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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Resources'] = []
        if self.resources is not None:
            for k in self.resources:
                result['Resources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.resources = []
        if m.get('Resources') is not None:
            for k in m.get('Resources'):
                temp_model = CheckInstanceResourcesResponseBodyResources()
                self.resources.append(temp_model.from_map(k))
        return self


class CheckInstanceResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckInstanceResourcesResponseBody = None,
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
            temp_model = CheckInstanceResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CloneExperimentRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class CloneExperimentResponseBody(TeaModel):
    def __init__(
        self,
        experiment_id: str = None,
        request_id: str = None,
    ):
        self.experiment_id = experiment_id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CloneExperimentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CloneExperimentResponseBody = None,
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
            temp_model = CloneExperimentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CloneExperimentGroupRequest(TeaModel):
    def __init__(
        self,
        environment: str = None,
        instance_id: str = None,
        layer_id: str = None,
    ):
        # This parameter is required.
        self.environment = environment
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.layer_id = layer_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.environment is not None:
            result['Environment'] = self.environment
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.layer_id is not None:
            result['LayerId'] = self.layer_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Environment') is not None:
            self.environment = m.get('Environment')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('LayerId') is not None:
            self.layer_id = m.get('LayerId')
        return self


class CloneExperimentGroupResponseBody(TeaModel):
    def __init__(
        self,
        experiment_group_id: str = None,
        request_id: str = None,
    ):
        self.experiment_group_id = experiment_group_id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.experiment_group_id is not None:
            result['ExperimentGroupId'] = self.experiment_group_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExperimentGroupId') is not None:
            self.experiment_group_id = m.get('ExperimentGroupId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CloneExperimentGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CloneExperimentGroupResponseBody = None,
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
            temp_model = CloneExperimentGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CloneFeatureConsistencyCheckJobConfigRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class CloneFeatureConsistencyCheckJobConfigResponseBody(TeaModel):
    def __init__(
        self,
        feature_consistency_check_id: str = None,
        request_id: str = None,
    ):
        self.feature_consistency_check_id = feature_consistency_check_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.feature_consistency_check_id is not None:
            result['FeatureConsistencyCheckId'] = self.feature_consistency_check_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FeatureConsistencyCheckId') is not None:
            self.feature_consistency_check_id = m.get('FeatureConsistencyCheckId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CloneFeatureConsistencyCheckJobConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CloneFeatureConsistencyCheckJobConfigResponseBody = None,
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
            temp_model = CloneFeatureConsistencyCheckJobConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CloneLaboratoryRequest(TeaModel):
    def __init__(
        self,
        clone_experiment_group: bool = None,
        environment: str = None,
        instance_id: str = None,
    ):
        # This parameter is required.
        self.clone_experiment_group = clone_experiment_group
        # This parameter is required.
        self.environment = environment
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.clone_experiment_group is not None:
            result['CloneExperimentGroup'] = self.clone_experiment_group
        if self.environment is not None:
            result['Environment'] = self.environment
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CloneExperimentGroup') is not None:
            self.clone_experiment_group = m.get('CloneExperimentGroup')
        if m.get('Environment') is not None:
            self.environment = m.get('Environment')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class CloneLaboratoryResponseBody(TeaModel):
    def __init__(
        self,
        laboratory_id: str = None,
        request_id: str = None,
    ):
        self.laboratory_id = laboratory_id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.laboratory_id is not None:
            result['LaboratoryId'] = self.laboratory_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LaboratoryId') is not None:
            self.laboratory_id = m.get('LaboratoryId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CloneLaboratoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CloneLaboratoryResponseBody = None,
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
            temp_model = CloneLaboratoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CloneTrafficControlTaskRequest(TeaModel):
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
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class CloneTrafficControlTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        traffic_control_task_id: str = None,
    ):
        self.request_id = request_id
        self.traffic_control_task_id = traffic_control_task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.traffic_control_task_id is not None:
            result['TrafficControlTaskId'] = self.traffic_control_task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TrafficControlTaskId') is not None:
            self.traffic_control_task_id = m.get('TrafficControlTaskId')
        return self


class CloneTrafficControlTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CloneTrafficControlTaskResponseBody = None,
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
            temp_model = CloneTrafficControlTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateABMetricRequest(TeaModel):
    def __init__(
        self,
        definition: str = None,
        description: str = None,
        instance_id: str = None,
        left_metric_id: str = None,
        name: str = None,
        operator: str = None,
        realtime: bool = None,
        result_resource_id: str = None,
        right_metric_id: str = None,
        scene_id: str = None,
        statistics_cycle: int = None,
        table_meta_id: str = None,
        type: str = None,
    ):
        # This parameter is required.
        self.definition = definition
        # This parameter is required.
        self.description = description
        # This parameter is required.
        self.instance_id = instance_id
        self.left_metric_id = left_metric_id
        # This parameter is required.
        self.name = name
        self.operator = operator
        # This parameter is required.
        self.realtime = realtime
        self.result_resource_id = result_resource_id
        self.right_metric_id = right_metric_id
        # This parameter is required.
        self.scene_id = scene_id
        self.statistics_cycle = statistics_cycle
        # This parameter is required.
        self.table_meta_id = table_meta_id
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.definition is not None:
            result['Definition'] = self.definition
        if self.description is not None:
            result['Description'] = self.description
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.left_metric_id is not None:
            result['LeftMetricId'] = self.left_metric_id
        if self.name is not None:
            result['Name'] = self.name
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.realtime is not None:
            result['Realtime'] = self.realtime
        if self.result_resource_id is not None:
            result['ResultResourceId'] = self.result_resource_id
        if self.right_metric_id is not None:
            result['RightMetricId'] = self.right_metric_id
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.statistics_cycle is not None:
            result['StatisticsCycle'] = self.statistics_cycle
        if self.table_meta_id is not None:
            result['TableMetaId'] = self.table_meta_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Definition') is not None:
            self.definition = m.get('Definition')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('LeftMetricId') is not None:
            self.left_metric_id = m.get('LeftMetricId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('Realtime') is not None:
            self.realtime = m.get('Realtime')
        if m.get('ResultResourceId') is not None:
            self.result_resource_id = m.get('ResultResourceId')
        if m.get('RightMetricId') is not None:
            self.right_metric_id = m.get('RightMetricId')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('StatisticsCycle') is not None:
            self.statistics_cycle = m.get('StatisticsCycle')
        if m.get('TableMetaId') is not None:
            self.table_meta_id = m.get('TableMetaId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateABMetricResponseBody(TeaModel):
    def __init__(
        self,
        abmetric_id: str = None,
        request_id: str = None,
    ):
        self.abmetric_id = abmetric_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.abmetric_id is not None:
            result['ABMetricId'] = self.abmetric_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ABMetricId') is not None:
            self.abmetric_id = m.get('ABMetricId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateABMetricResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateABMetricResponseBody = None,
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
            temp_model = CreateABMetricResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateABMetricGroupRequest(TeaModel):
    def __init__(
        self,
        abmetric_ids: str = None,
        description: str = None,
        instance_id: str = None,
        name: str = None,
        realtime: bool = None,
        scene_id: str = None,
    ):
        # This parameter is required.
        self.abmetric_ids = abmetric_ids
        # This parameter is required.
        self.description = description
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.realtime = realtime
        # This parameter is required.
        self.scene_id = scene_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.abmetric_ids is not None:
            result['ABMetricIds'] = self.abmetric_ids
        if self.description is not None:
            result['Description'] = self.description
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        if self.realtime is not None:
            result['Realtime'] = self.realtime
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ABMetricIds') is not None:
            self.abmetric_ids = m.get('ABMetricIds')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Realtime') is not None:
            self.realtime = m.get('Realtime')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        return self


class CreateABMetricGroupResponseBody(TeaModel):
    def __init__(
        self,
        abmetric_group_id: str = None,
        request_id: str = None,
    ):
        self.abmetric_group_id = abmetric_group_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.abmetric_group_id is not None:
            result['ABMetricGroupId'] = self.abmetric_group_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ABMetricGroupId') is not None:
            self.abmetric_group_id = m.get('ABMetricGroupId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateABMetricGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateABMetricGroupResponseBody = None,
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
            temp_model = CreateABMetricGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCalculationJobsRequest(TeaModel):
    def __init__(
        self,
        abmetric_ids: str = None,
        end_date: str = None,
        instance_id: str = None,
        start_date: str = None,
    ):
        # This parameter is required.
        self.abmetric_ids = abmetric_ids
        # This parameter is required.
        self.end_date = end_date
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.start_date = start_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.abmetric_ids is not None:
            result['ABMetricIds'] = self.abmetric_ids
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ABMetricIds') is not None:
            self.abmetric_ids = m.get('ABMetricIds')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        return self


class CreateCalculationJobsResponseBody(TeaModel):
    def __init__(
        self,
        calculation_job_ids: List[str] = None,
        request_id: str = None,
    ):
        self.calculation_job_ids = calculation_job_ids
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.calculation_job_ids is not None:
            result['CalculationJobIds'] = self.calculation_job_ids
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CalculationJobIds') is not None:
            self.calculation_job_ids = m.get('CalculationJobIds')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateCalculationJobsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateCalculationJobsResponseBody = None,
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
            temp_model = CreateCalculationJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCrowdRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        instance_id: str = None,
        label: str = None,
        name: str = None,
        source: str = None,
        users: str = None,
    ):
        # This parameter is required.
        self.description = description
        # This parameter is required.
        self.instance_id = instance_id
        self.label = label
        # This parameter is required.
        self.name = name
        self.source = source
        self.users = users

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.label is not None:
            result['Label'] = self.label
        if self.name is not None:
            result['Name'] = self.name
        if self.source is not None:
            result['Source'] = self.source
        if self.users is not None:
            result['Users'] = self.users
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Users') is not None:
            self.users = m.get('Users')
        return self


class CreateCrowdResponseBody(TeaModel):
    def __init__(
        self,
        crowd_id: str = None,
        request_id: str = None,
    ):
        self.crowd_id = crowd_id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.crowd_id is not None:
            result['CrowdId'] = self.crowd_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CrowdId') is not None:
            self.crowd_id = m.get('CrowdId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateCrowdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateCrowdResponseBody = None,
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
            temp_model = CreateCrowdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateExperimentRequest(TeaModel):
    def __init__(
        self,
        config: str = None,
        debug_crowd_id: str = None,
        debug_users: str = None,
        description: str = None,
        experiment_group_id: str = None,
        flow_percent: int = None,
        instance_id: str = None,
        name: str = None,
        type: str = None,
    ):
        self.config = config
        self.debug_crowd_id = debug_crowd_id
        self.debug_users = debug_users
        # This parameter is required.
        self.description = description
        # This parameter is required.
        self.experiment_group_id = experiment_group_id
        self.flow_percent = flow_percent
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.debug_crowd_id is not None:
            result['DebugCrowdId'] = self.debug_crowd_id
        if self.debug_users is not None:
            result['DebugUsers'] = self.debug_users
        if self.description is not None:
            result['Description'] = self.description
        if self.experiment_group_id is not None:
            result['ExperimentGroupId'] = self.experiment_group_id
        if self.flow_percent is not None:
            result['FlowPercent'] = self.flow_percent
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('DebugCrowdId') is not None:
            self.debug_crowd_id = m.get('DebugCrowdId')
        if m.get('DebugUsers') is not None:
            self.debug_users = m.get('DebugUsers')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExperimentGroupId') is not None:
            self.experiment_group_id = m.get('ExperimentGroupId')
        if m.get('FlowPercent') is not None:
            self.flow_percent = m.get('FlowPercent')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateExperimentResponseBody(TeaModel):
    def __init__(
        self,
        experiment_id: str = None,
        request_id: str = None,
    ):
        self.experiment_id = experiment_id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateExperimentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateExperimentResponseBody = None,
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
            temp_model = CreateExperimentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateExperimentGroupRequest(TeaModel):
    def __init__(
        self,
        config: str = None,
        crowd_id: str = None,
        crowd_target_type: str = None,
        debug_crowd_id: str = None,
        debug_users: str = None,
        description: str = None,
        distribution_time_duration: int = None,
        distribution_type: str = None,
        filter: str = None,
        instance_id: str = None,
        layer_id: str = None,
        name: str = None,
        need_aa: bool = None,
        random_flow: int = None,
        reserved_buckets: str = None,
    ):
        self.config = config
        self.crowd_id = crowd_id
        self.crowd_target_type = crowd_target_type
        self.debug_crowd_id = debug_crowd_id
        self.debug_users = debug_users
        self.description = description
        self.distribution_time_duration = distribution_time_duration
        self.distribution_type = distribution_type
        self.filter = filter
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.layer_id = layer_id
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.need_aa = need_aa
        self.random_flow = random_flow
        self.reserved_buckets = reserved_buckets

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.crowd_id is not None:
            result['CrowdId'] = self.crowd_id
        if self.crowd_target_type is not None:
            result['CrowdTargetType'] = self.crowd_target_type
        if self.debug_crowd_id is not None:
            result['DebugCrowdId'] = self.debug_crowd_id
        if self.debug_users is not None:
            result['DebugUsers'] = self.debug_users
        if self.description is not None:
            result['Description'] = self.description
        if self.distribution_time_duration is not None:
            result['DistributionTimeDuration'] = self.distribution_time_duration
        if self.distribution_type is not None:
            result['DistributionType'] = self.distribution_type
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.layer_id is not None:
            result['LayerId'] = self.layer_id
        if self.name is not None:
            result['Name'] = self.name
        if self.need_aa is not None:
            result['NeedAA'] = self.need_aa
        if self.random_flow is not None:
            result['RandomFlow'] = self.random_flow
        if self.reserved_buckets is not None:
            result['ReservedBuckets'] = self.reserved_buckets
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('CrowdId') is not None:
            self.crowd_id = m.get('CrowdId')
        if m.get('CrowdTargetType') is not None:
            self.crowd_target_type = m.get('CrowdTargetType')
        if m.get('DebugCrowdId') is not None:
            self.debug_crowd_id = m.get('DebugCrowdId')
        if m.get('DebugUsers') is not None:
            self.debug_users = m.get('DebugUsers')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DistributionTimeDuration') is not None:
            self.distribution_time_duration = m.get('DistributionTimeDuration')
        if m.get('DistributionType') is not None:
            self.distribution_type = m.get('DistributionType')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('LayerId') is not None:
            self.layer_id = m.get('LayerId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NeedAA') is not None:
            self.need_aa = m.get('NeedAA')
        if m.get('RandomFlow') is not None:
            self.random_flow = m.get('RandomFlow')
        if m.get('ReservedBuckets') is not None:
            self.reserved_buckets = m.get('ReservedBuckets')
        return self


class CreateExperimentGroupResponseBody(TeaModel):
    def __init__(
        self,
        experiment_group_id: str = None,
        request_id: str = None,
    ):
        self.experiment_group_id = experiment_group_id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.experiment_group_id is not None:
            result['ExperimentGroupId'] = self.experiment_group_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExperimentGroupId') is not None:
            self.experiment_group_id = m.get('ExperimentGroupId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateExperimentGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateExperimentGroupResponseBody = None,
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
            temp_model = CreateExperimentGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFeatureConsistencyCheckJobRequest(TeaModel):
    def __init__(
        self,
        environment: str = None,
        feature_consistency_check_job_config_id: str = None,
        instance_id: str = None,
        sampling_duration: int = None,
    ):
        # This parameter is required.
        self.environment = environment
        # This parameter is required.
        self.feature_consistency_check_job_config_id = feature_consistency_check_job_config_id
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.sampling_duration = sampling_duration

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.environment is not None:
            result['Environment'] = self.environment
        if self.feature_consistency_check_job_config_id is not None:
            result['FeatureConsistencyCheckJobConfigId'] = self.feature_consistency_check_job_config_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.sampling_duration is not None:
            result['SamplingDuration'] = self.sampling_duration
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Environment') is not None:
            self.environment = m.get('Environment')
        if m.get('FeatureConsistencyCheckJobConfigId') is not None:
            self.feature_consistency_check_job_config_id = m.get('FeatureConsistencyCheckJobConfigId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SamplingDuration') is not None:
            self.sampling_duration = m.get('SamplingDuration')
        return self


class CreateFeatureConsistencyCheckJobResponseBody(TeaModel):
    def __init__(
        self,
        feature_consistency_check_job_id: str = None,
        request_id: str = None,
    ):
        self.feature_consistency_check_job_id = feature_consistency_check_job_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.feature_consistency_check_job_id is not None:
            result['FeatureConsistencyCheckJobId'] = self.feature_consistency_check_job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FeatureConsistencyCheckJobId') is not None:
            self.feature_consistency_check_job_id = m.get('FeatureConsistencyCheckJobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateFeatureConsistencyCheckJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateFeatureConsistencyCheckJobResponseBody = None,
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
            temp_model = CreateFeatureConsistencyCheckJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFeatureConsistencyCheckJobConfigRequest(TeaModel):
    def __init__(
        self,
        compare_feature: bool = None,
        eas_service_name: str = None,
        easy_rec_package_path: str = None,
        easy_rec_version: str = None,
        feature_display_exclude: str = None,
        feature_landing_resource_id: str = None,
        feature_priority: str = None,
        feature_store_item_id: str = None,
        feature_store_model_id: str = None,
        feature_store_project_id: str = None,
        feature_store_project_name: str = None,
        feature_store_seq_feature_view: str = None,
        feature_store_user_id: str = None,
        fg_jar_version: str = None,
        fg_json_file_name: str = None,
        generate_zip: bool = None,
        instance_id: str = None,
        item_id_field: str = None,
        item_table: str = None,
        item_table_partition_field: str = None,
        item_table_partition_field_format: str = None,
        name: str = None,
        oss_resource_id: str = None,
        sample_rate: float = None,
        scene_id: str = None,
        service_id: str = None,
        use_feature_store: bool = None,
        user_id_field: str = None,
        user_table: str = None,
        user_table_partition_field: str = None,
        user_table_partition_field_format: str = None,
        workflow_name: str = None,
    ):
        # This parameter is required.
        self.compare_feature = compare_feature
        # This parameter is required.
        self.eas_service_name = eas_service_name
        self.easy_rec_package_path = easy_rec_package_path
        self.easy_rec_version = easy_rec_version
        self.feature_display_exclude = feature_display_exclude
        # This parameter is required.
        self.feature_landing_resource_id = feature_landing_resource_id
        self.feature_priority = feature_priority
        self.feature_store_item_id = feature_store_item_id
        self.feature_store_model_id = feature_store_model_id
        self.feature_store_project_id = feature_store_project_id
        self.feature_store_project_name = feature_store_project_name
        self.feature_store_seq_feature_view = feature_store_seq_feature_view
        self.feature_store_user_id = feature_store_user_id
        self.fg_jar_version = fg_jar_version
        # This parameter is required.
        self.fg_json_file_name = fg_json_file_name
        # This parameter is required.
        self.generate_zip = generate_zip
        # This parameter is required.
        self.instance_id = instance_id
        self.item_id_field = item_id_field
        self.item_table = item_table
        self.item_table_partition_field = item_table_partition_field
        self.item_table_partition_field_format = item_table_partition_field_format
        # This parameter is required.
        self.name = name
        self.oss_resource_id = oss_resource_id
        # This parameter is required.
        self.sample_rate = sample_rate
        # This parameter is required.
        self.scene_id = scene_id
        # This parameter is required.
        self.service_id = service_id
        # This parameter is required.
        self.use_feature_store = use_feature_store
        self.user_id_field = user_id_field
        self.user_table = user_table
        self.user_table_partition_field = user_table_partition_field
        self.user_table_partition_field_format = user_table_partition_field_format
        self.workflow_name = workflow_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compare_feature is not None:
            result['CompareFeature'] = self.compare_feature
        if self.eas_service_name is not None:
            result['EasServiceName'] = self.eas_service_name
        if self.easy_rec_package_path is not None:
            result['EasyRecPackagePath'] = self.easy_rec_package_path
        if self.easy_rec_version is not None:
            result['EasyRecVersion'] = self.easy_rec_version
        if self.feature_display_exclude is not None:
            result['FeatureDisplayExclude'] = self.feature_display_exclude
        if self.feature_landing_resource_id is not None:
            result['FeatureLandingResourceId'] = self.feature_landing_resource_id
        if self.feature_priority is not None:
            result['FeaturePriority'] = self.feature_priority
        if self.feature_store_item_id is not None:
            result['FeatureStoreItemId'] = self.feature_store_item_id
        if self.feature_store_model_id is not None:
            result['FeatureStoreModelId'] = self.feature_store_model_id
        if self.feature_store_project_id is not None:
            result['FeatureStoreProjectId'] = self.feature_store_project_id
        if self.feature_store_project_name is not None:
            result['FeatureStoreProjectName'] = self.feature_store_project_name
        if self.feature_store_seq_feature_view is not None:
            result['FeatureStoreSeqFeatureView'] = self.feature_store_seq_feature_view
        if self.feature_store_user_id is not None:
            result['FeatureStoreUserId'] = self.feature_store_user_id
        if self.fg_jar_version is not None:
            result['FgJarVersion'] = self.fg_jar_version
        if self.fg_json_file_name is not None:
            result['FgJsonFileName'] = self.fg_json_file_name
        if self.generate_zip is not None:
            result['GenerateZip'] = self.generate_zip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.item_id_field is not None:
            result['ItemIdField'] = self.item_id_field
        if self.item_table is not None:
            result['ItemTable'] = self.item_table
        if self.item_table_partition_field is not None:
            result['ItemTablePartitionField'] = self.item_table_partition_field
        if self.item_table_partition_field_format is not None:
            result['ItemTablePartitionFieldFormat'] = self.item_table_partition_field_format
        if self.name is not None:
            result['Name'] = self.name
        if self.oss_resource_id is not None:
            result['OssResourceId'] = self.oss_resource_id
        if self.sample_rate is not None:
            result['SampleRate'] = self.sample_rate
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.use_feature_store is not None:
            result['UseFeatureStore'] = self.use_feature_store
        if self.user_id_field is not None:
            result['UserIdField'] = self.user_id_field
        if self.user_table is not None:
            result['UserTable'] = self.user_table
        if self.user_table_partition_field is not None:
            result['UserTablePartitionField'] = self.user_table_partition_field
        if self.user_table_partition_field_format is not None:
            result['UserTablePartitionFieldFormat'] = self.user_table_partition_field_format
        if self.workflow_name is not None:
            result['WorkflowName'] = self.workflow_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompareFeature') is not None:
            self.compare_feature = m.get('CompareFeature')
        if m.get('EasServiceName') is not None:
            self.eas_service_name = m.get('EasServiceName')
        if m.get('EasyRecPackagePath') is not None:
            self.easy_rec_package_path = m.get('EasyRecPackagePath')
        if m.get('EasyRecVersion') is not None:
            self.easy_rec_version = m.get('EasyRecVersion')
        if m.get('FeatureDisplayExclude') is not None:
            self.feature_display_exclude = m.get('FeatureDisplayExclude')
        if m.get('FeatureLandingResourceId') is not None:
            self.feature_landing_resource_id = m.get('FeatureLandingResourceId')
        if m.get('FeaturePriority') is not None:
            self.feature_priority = m.get('FeaturePriority')
        if m.get('FeatureStoreItemId') is not None:
            self.feature_store_item_id = m.get('FeatureStoreItemId')
        if m.get('FeatureStoreModelId') is not None:
            self.feature_store_model_id = m.get('FeatureStoreModelId')
        if m.get('FeatureStoreProjectId') is not None:
            self.feature_store_project_id = m.get('FeatureStoreProjectId')
        if m.get('FeatureStoreProjectName') is not None:
            self.feature_store_project_name = m.get('FeatureStoreProjectName')
        if m.get('FeatureStoreSeqFeatureView') is not None:
            self.feature_store_seq_feature_view = m.get('FeatureStoreSeqFeatureView')
        if m.get('FeatureStoreUserId') is not None:
            self.feature_store_user_id = m.get('FeatureStoreUserId')
        if m.get('FgJarVersion') is not None:
            self.fg_jar_version = m.get('FgJarVersion')
        if m.get('FgJsonFileName') is not None:
            self.fg_json_file_name = m.get('FgJsonFileName')
        if m.get('GenerateZip') is not None:
            self.generate_zip = m.get('GenerateZip')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ItemIdField') is not None:
            self.item_id_field = m.get('ItemIdField')
        if m.get('ItemTable') is not None:
            self.item_table = m.get('ItemTable')
        if m.get('ItemTablePartitionField') is not None:
            self.item_table_partition_field = m.get('ItemTablePartitionField')
        if m.get('ItemTablePartitionFieldFormat') is not None:
            self.item_table_partition_field_format = m.get('ItemTablePartitionFieldFormat')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OssResourceId') is not None:
            self.oss_resource_id = m.get('OssResourceId')
        if m.get('SampleRate') is not None:
            self.sample_rate = m.get('SampleRate')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('UseFeatureStore') is not None:
            self.use_feature_store = m.get('UseFeatureStore')
        if m.get('UserIdField') is not None:
            self.user_id_field = m.get('UserIdField')
        if m.get('UserTable') is not None:
            self.user_table = m.get('UserTable')
        if m.get('UserTablePartitionField') is not None:
            self.user_table_partition_field = m.get('UserTablePartitionField')
        if m.get('UserTablePartitionFieldFormat') is not None:
            self.user_table_partition_field_format = m.get('UserTablePartitionFieldFormat')
        if m.get('WorkflowName') is not None:
            self.workflow_name = m.get('WorkflowName')
        return self


class CreateFeatureConsistencyCheckJobConfigResponseBody(TeaModel):
    def __init__(
        self,
        feature_consistency_check_job_config_id: str = None,
        request_id: str = None,
    ):
        self.feature_consistency_check_job_config_id = feature_consistency_check_job_config_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.feature_consistency_check_job_config_id is not None:
            result['FeatureConsistencyCheckJobConfigId'] = self.feature_consistency_check_job_config_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FeatureConsistencyCheckJobConfigId') is not None:
            self.feature_consistency_check_job_config_id = m.get('FeatureConsistencyCheckJobConfigId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateFeatureConsistencyCheckJobConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateFeatureConsistencyCheckJobConfigResponseBody = None,
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
            temp_model = CreateFeatureConsistencyCheckJobConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateInstanceResourceRequest(TeaModel):
    def __init__(
        self,
        category: str = None,
        group: str = None,
        type: str = None,
        uri: str = None,
    ):
        # This parameter is required.
        self.category = category
        # This parameter is required.
        self.group = group
        # This parameter is required.
        self.type = type
        # This parameter is required.
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.group is not None:
            result['Group'] = self.group
        if self.type is not None:
            result['Type'] = self.type
        if self.uri is not None:
            result['Uri'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        return self


class CreateInstanceResourceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resource_id: str = None,
    ):
        self.request_id = request_id
        self.resource_id = resource_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        return self


class CreateInstanceResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateInstanceResourceResponseBody = None,
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
            temp_model = CreateInstanceResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLaboratoryRequest(TeaModel):
    def __init__(
        self,
        bucket_count: int = None,
        bucket_type: str = None,
        buckets: str = None,
        debug_crowd_id: str = None,
        debug_users: str = None,
        description: str = None,
        environment: str = None,
        filter: str = None,
        instance_id: str = None,
        name: str = None,
        scene_id: str = None,
        type: str = None,
    ):
        self.bucket_count = bucket_count
        # This parameter is required.
        self.bucket_type = bucket_type
        self.buckets = buckets
        self.debug_crowd_id = debug_crowd_id
        self.debug_users = debug_users
        self.description = description
        # This parameter is required.
        self.environment = environment
        self.filter = filter
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.scene_id = scene_id
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_count is not None:
            result['BucketCount'] = self.bucket_count
        if self.bucket_type is not None:
            result['BucketType'] = self.bucket_type
        if self.buckets is not None:
            result['Buckets'] = self.buckets
        if self.debug_crowd_id is not None:
            result['DebugCrowdId'] = self.debug_crowd_id
        if self.debug_users is not None:
            result['DebugUsers'] = self.debug_users
        if self.description is not None:
            result['Description'] = self.description
        if self.environment is not None:
            result['Environment'] = self.environment
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketCount') is not None:
            self.bucket_count = m.get('BucketCount')
        if m.get('BucketType') is not None:
            self.bucket_type = m.get('BucketType')
        if m.get('Buckets') is not None:
            self.buckets = m.get('Buckets')
        if m.get('DebugCrowdId') is not None:
            self.debug_crowd_id = m.get('DebugCrowdId')
        if m.get('DebugUsers') is not None:
            self.debug_users = m.get('DebugUsers')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Environment') is not None:
            self.environment = m.get('Environment')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateLaboratoryResponseBody(TeaModel):
    def __init__(
        self,
        laboratory_id: str = None,
        request_id: str = None,
    ):
        self.laboratory_id = laboratory_id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.laboratory_id is not None:
            result['LaboratoryId'] = self.laboratory_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LaboratoryId') is not None:
            self.laboratory_id = m.get('LaboratoryId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateLaboratoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateLaboratoryResponseBody = None,
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
            temp_model = CreateLaboratoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLayerRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        instance_id: str = None,
        laboratory_id: str = None,
        name: str = None,
    ):
        # This parameter is required.
        self.description = description
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.laboratory_id = laboratory_id
        # This parameter is required.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.laboratory_id is not None:
            result['LaboratoryId'] = self.laboratory_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('LaboratoryId') is not None:
            self.laboratory_id = m.get('LaboratoryId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class CreateLayerResponseBody(TeaModel):
    def __init__(
        self,
        layer_id: str = None,
        request_id: str = None,
    ):
        self.layer_id = layer_id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.layer_id is not None:
            result['LayerId'] = self.layer_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LayerId') is not None:
            self.layer_id = m.get('LayerId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateLayerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateLayerResponseBody = None,
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
            temp_model = CreateLayerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateParamRequest(TeaModel):
    def __init__(
        self,
        environment: str = None,
        instance_id: str = None,
        name: str = None,
        scene_id: str = None,
        value: str = None,
    ):
        self.environment = environment
        self.instance_id = instance_id
        self.name = name
        self.scene_id = scene_id
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.environment is not None:
            result['Environment'] = self.environment
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Environment') is not None:
            self.environment = m.get('Environment')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateParamResponseBody(TeaModel):
    def __init__(
        self,
        param_id: int = None,
        request_id: str = None,
    ):
        self.param_id = param_id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.param_id is not None:
            result['ParamId'] = self.param_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParamId') is not None:
            self.param_id = m.get('ParamId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateParamResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateParamResponseBody = None,
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
            temp_model = CreateParamResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateResourceRuleRequestRuleItems(TeaModel):
    def __init__(
        self,
        description: str = None,
        max_value: float = None,
        min_value: float = None,
        name: str = None,
        value: float = None,
    ):
        self.description = description
        # This parameter is required.
        self.max_value = max_value
        # This parameter is required.
        self.min_value = min_value
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.max_value is not None:
            result['MaxValue'] = self.max_value
        if self.min_value is not None:
            result['MinValue'] = self.min_value
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('MaxValue') is not None:
            self.max_value = m.get('MaxValue')
        if m.get('MinValue') is not None:
            self.min_value = m.get('MinValue')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateResourceRuleRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        instance_id: str = None,
        metric_operation_type: str = None,
        metric_pull_info: str = None,
        metric_pull_period: str = None,
        name: str = None,
        rule_computing_definition: str = None,
        rule_items: List[CreateResourceRuleRequestRuleItems] = None,
    ):
        self.description = description
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.metric_operation_type = metric_operation_type
        self.metric_pull_info = metric_pull_info
        self.metric_pull_period = metric_pull_period
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.rule_computing_definition = rule_computing_definition
        # This parameter is required.
        self.rule_items = rule_items

    def validate(self):
        if self.rule_items:
            for k in self.rule_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.metric_operation_type is not None:
            result['MetricOperationType'] = self.metric_operation_type
        if self.metric_pull_info is not None:
            result['MetricPullInfo'] = self.metric_pull_info
        if self.metric_pull_period is not None:
            result['MetricPullPeriod'] = self.metric_pull_period
        if self.name is not None:
            result['Name'] = self.name
        if self.rule_computing_definition is not None:
            result['RuleComputingDefinition'] = self.rule_computing_definition
        result['RuleItems'] = []
        if self.rule_items is not None:
            for k in self.rule_items:
                result['RuleItems'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MetricOperationType') is not None:
            self.metric_operation_type = m.get('MetricOperationType')
        if m.get('MetricPullInfo') is not None:
            self.metric_pull_info = m.get('MetricPullInfo')
        if m.get('MetricPullPeriod') is not None:
            self.metric_pull_period = m.get('MetricPullPeriod')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RuleComputingDefinition') is not None:
            self.rule_computing_definition = m.get('RuleComputingDefinition')
        self.rule_items = []
        if m.get('RuleItems') is not None:
            for k in m.get('RuleItems'):
                temp_model = CreateResourceRuleRequestRuleItems()
                self.rule_items.append(temp_model.from_map(k))
        return self


class CreateResourceRuleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resource_rule_id: str = None,
    ):
        self.request_id = request_id
        self.resource_rule_id = resource_rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_rule_id is not None:
            result['ResourceRuleId'] = self.resource_rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceRuleId') is not None:
            self.resource_rule_id = m.get('ResourceRuleId')
        return self


class CreateResourceRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateResourceRuleResponseBody = None,
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
            temp_model = CreateResourceRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateResourceRuleItemRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        instance_id: str = None,
        max_value: float = None,
        min_value: float = None,
        name: str = None,
        value: float = None,
    ):
        self.description = description
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.max_value = max_value
        # This parameter is required.
        self.min_value = min_value
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.max_value is not None:
            result['MaxValue'] = self.max_value
        if self.min_value is not None:
            result['MinValue'] = self.min_value
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MaxValue') is not None:
            self.max_value = m.get('MaxValue')
        if m.get('MinValue') is not None:
            self.min_value = m.get('MinValue')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateResourceRuleItemResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resource_rule_item_id: str = None,
    ):
        self.request_id = request_id
        self.resource_rule_item_id = resource_rule_item_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_rule_item_id is not None:
            result['ResourceRuleItemId'] = self.resource_rule_item_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceRuleItemId') is not None:
            self.resource_rule_item_id = m.get('ResourceRuleItemId')
        return self


class CreateResourceRuleItemResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateResourceRuleItemResponseBody = None,
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
            temp_model = CreateResourceRuleItemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSceneRequestFlows(TeaModel):
    def __init__(
        self,
        flow_code: str = None,
        flow_name: str = None,
    ):
        self.flow_code = flow_code
        self.flow_name = flow_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_code is not None:
            result['FlowCode'] = self.flow_code
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowCode') is not None:
            self.flow_code = m.get('FlowCode')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        return self


class CreateSceneRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        flows: List[CreateSceneRequestFlows] = None,
        instance_id: str = None,
        name: str = None,
    ):
        self.description = description
        self.flows = flows
        self.instance_id = instance_id
        self.name = name

    def validate(self):
        if self.flows:
            for k in self.flows:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        result['Flows'] = []
        if self.flows is not None:
            for k in self.flows:
                result['Flows'].append(k.to_map() if k else None)
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        self.flows = []
        if m.get('Flows') is not None:
            for k in m.get('Flows'):
                temp_model = CreateSceneRequestFlows()
                self.flows.append(temp_model.from_map(k))
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class CreateSceneResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        scene_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.scene_id = scene_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        return self


class CreateSceneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateSceneResponseBody = None,
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
            temp_model = CreateSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSubCrowdRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        source: str = None,
        users: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.source = source
        # This parameter is required.
        self.users = users

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.source is not None:
            result['Source'] = self.source
        if self.users is not None:
            result['Users'] = self.users
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Users') is not None:
            self.users = m.get('Users')
        return self


class CreateSubCrowdResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        sub_crowd_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.sub_crowd_id = sub_crowd_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sub_crowd_id is not None:
            result['SubCrowdId'] = self.sub_crowd_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubCrowdId') is not None:
            self.sub_crowd_id = m.get('SubCrowdId')
        return self


class CreateSubCrowdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateSubCrowdResponseBody = None,
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
            temp_model = CreateSubCrowdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTableMetaRequestFields(TeaModel):
    def __init__(
        self,
        data_type: str = None,
        is_dimension_field: bool = None,
        is_partition_field: str = None,
        meaning: str = None,
        name: str = None,
        type: str = None,
    ):
        self.data_type = data_type
        # This parameter is required.
        self.is_dimension_field = is_dimension_field
        # This parameter is required.
        self.is_partition_field = is_partition_field
        # This parameter is required.
        self.meaning = meaning
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.is_dimension_field is not None:
            result['IsDimensionField'] = self.is_dimension_field
        if self.is_partition_field is not None:
            result['IsPartitionField'] = self.is_partition_field
        if self.meaning is not None:
            result['Meaning'] = self.meaning
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('IsDimensionField') is not None:
            self.is_dimension_field = m.get('IsDimensionField')
        if m.get('IsPartitionField') is not None:
            self.is_partition_field = m.get('IsPartitionField')
        if m.get('Meaning') is not None:
            self.meaning = m.get('Meaning')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateTableMetaRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        fields: List[CreateTableMetaRequestFields] = None,
        instance_id: str = None,
        module: str = None,
        name: str = None,
        resource_id: str = None,
        table_name: str = None,
    ):
        # This parameter is required.
        self.description = description
        # This parameter is required.
        self.fields = fields
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.module = module
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.resource_id = resource_id
        # This parameter is required.
        self.table_name = table_name

    def validate(self):
        if self.fields:
            for k in self.fields:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        result['Fields'] = []
        if self.fields is not None:
            for k in self.fields:
                result['Fields'].append(k.to_map() if k else None)
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.module is not None:
            result['Module'] = self.module
        if self.name is not None:
            result['Name'] = self.name
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        self.fields = []
        if m.get('Fields') is not None:
            for k in m.get('Fields'):
                temp_model = CreateTableMetaRequestFields()
                self.fields.append(temp_model.from_map(k))
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Module') is not None:
            self.module = m.get('Module')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class CreateTableMetaResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        table_meta_id: str = None,
    ):
        self.request_id = request_id
        self.table_meta_id = table_meta_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.table_meta_id is not None:
            result['TableMetaId'] = self.table_meta_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TableMetaId') is not None:
            self.table_meta_id = m.get('TableMetaId')
        return self


class CreateTableMetaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateTableMetaResponseBody = None,
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
            temp_model = CreateTableMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTrafficControlTargetRequest(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        event: str = None,
        item_condition_array: str = None,
        item_condition_express: str = None,
        item_condition_type: str = None,
        name: str = None,
        new_product_regulation: bool = None,
        recall_name: str = None,
        start_time: str = None,
        statis_period: str = None,
        status: str = None,
        tolerance_value: int = None,
        traffic_control_task_id: str = None,
        value: float = None,
    ):
        self.end_time = end_time
        self.event = event
        self.item_condition_array = item_condition_array
        self.item_condition_express = item_condition_express
        self.item_condition_type = item_condition_type
        self.name = name
        self.new_product_regulation = new_product_regulation
        self.recall_name = recall_name
        self.start_time = start_time
        self.statis_period = statis_period
        self.status = status
        self.tolerance_value = tolerance_value
        self.traffic_control_task_id = traffic_control_task_id
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.event is not None:
            result['Event'] = self.event
        if self.item_condition_array is not None:
            result['ItemConditionArray'] = self.item_condition_array
        if self.item_condition_express is not None:
            result['ItemConditionExpress'] = self.item_condition_express
        if self.item_condition_type is not None:
            result['ItemConditionType'] = self.item_condition_type
        if self.name is not None:
            result['Name'] = self.name
        if self.new_product_regulation is not None:
            result['NewProductRegulation'] = self.new_product_regulation
        if self.recall_name is not None:
            result['RecallName'] = self.recall_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.statis_period is not None:
            result['StatisPeriod'] = self.statis_period
        if self.status is not None:
            result['Status'] = self.status
        if self.tolerance_value is not None:
            result['ToleranceValue'] = self.tolerance_value
        if self.traffic_control_task_id is not None:
            result['TrafficControlTaskId'] = self.traffic_control_task_id
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Event') is not None:
            self.event = m.get('Event')
        if m.get('ItemConditionArray') is not None:
            self.item_condition_array = m.get('ItemConditionArray')
        if m.get('ItemConditionExpress') is not None:
            self.item_condition_express = m.get('ItemConditionExpress')
        if m.get('ItemConditionType') is not None:
            self.item_condition_type = m.get('ItemConditionType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NewProductRegulation') is not None:
            self.new_product_regulation = m.get('NewProductRegulation')
        if m.get('RecallName') is not None:
            self.recall_name = m.get('RecallName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StatisPeriod') is not None:
            self.statis_period = m.get('StatisPeriod')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ToleranceValue') is not None:
            self.tolerance_value = m.get('ToleranceValue')
        if m.get('TrafficControlTaskId') is not None:
            self.traffic_control_task_id = m.get('TrafficControlTaskId')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateTrafficControlTargetResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        traffic_control_target_id: str = None,
    ):
        self.request_id = request_id
        self.traffic_control_target_id = traffic_control_target_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.traffic_control_target_id is not None:
            result['TrafficControlTargetId'] = self.traffic_control_target_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TrafficControlTargetId') is not None:
            self.traffic_control_target_id = m.get('TrafficControlTargetId')
        return self


class CreateTrafficControlTargetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateTrafficControlTargetResponseBody = None,
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
            temp_model = CreateTrafficControlTargetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTrafficControlTaskRequestTrafficControlTargets(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        event: str = None,
        item_condition_array: str = None,
        item_condition_express: str = None,
        item_condition_type: str = None,
        name: str = None,
        new_product_regulation: bool = None,
        recall_name: str = None,
        start_time: str = None,
        statis_period: str = None,
        status: str = None,
        tolerance_value: int = None,
        value: float = None,
    ):
        self.end_time = end_time
        self.event = event
        self.item_condition_array = item_condition_array
        self.item_condition_express = item_condition_express
        self.item_condition_type = item_condition_type
        self.name = name
        self.new_product_regulation = new_product_regulation
        self.recall_name = recall_name
        self.start_time = start_time
        self.statis_period = statis_period
        self.status = status
        self.tolerance_value = tolerance_value
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.event is not None:
            result['Event'] = self.event
        if self.item_condition_array is not None:
            result['ItemConditionArray'] = self.item_condition_array
        if self.item_condition_express is not None:
            result['ItemConditionExpress'] = self.item_condition_express
        if self.item_condition_type is not None:
            result['ItemConditionType'] = self.item_condition_type
        if self.name is not None:
            result['Name'] = self.name
        if self.new_product_regulation is not None:
            result['NewProductRegulation'] = self.new_product_regulation
        if self.recall_name is not None:
            result['RecallName'] = self.recall_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.statis_period is not None:
            result['StatisPeriod'] = self.statis_period
        if self.status is not None:
            result['Status'] = self.status
        if self.tolerance_value is not None:
            result['ToleranceValue'] = self.tolerance_value
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Event') is not None:
            self.event = m.get('Event')
        if m.get('ItemConditionArray') is not None:
            self.item_condition_array = m.get('ItemConditionArray')
        if m.get('ItemConditionExpress') is not None:
            self.item_condition_express = m.get('ItemConditionExpress')
        if m.get('ItemConditionType') is not None:
            self.item_condition_type = m.get('ItemConditionType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NewProductRegulation') is not None:
            self.new_product_regulation = m.get('NewProductRegulation')
        if m.get('RecallName') is not None:
            self.recall_name = m.get('RecallName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StatisPeriod') is not None:
            self.statis_period = m.get('StatisPeriod')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ToleranceValue') is not None:
            self.tolerance_value = m.get('ToleranceValue')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateTrafficControlTaskRequest(TeaModel):
    def __init__(
        self,
        behavior_table_meta_id: str = None,
        control_granularity: str = None,
        control_logic: str = None,
        control_type: str = None,
        description: str = None,
        end_time: str = None,
        execution_time: str = None,
        instance_id: str = None,
        item_condition_array: str = None,
        item_condition_express: str = None,
        item_condition_type: str = None,
        item_table_meta_id: str = None,
        name: str = None,
        scene_id: str = None,
        start_time: str = None,
        statis_behavior_condition_array: str = None,
        statis_behavior_condition_express: str = None,
        statis_behavior_condition_type: str = None,
        traffic_control_targets: List[CreateTrafficControlTaskRequestTrafficControlTargets] = None,
        user_condition_array: str = None,
        user_condition_express: str = None,
        user_condition_type: str = None,
        user_table_meta_id: str = None,
    ):
        self.behavior_table_meta_id = behavior_table_meta_id
        self.control_granularity = control_granularity
        self.control_logic = control_logic
        self.control_type = control_type
        self.description = description
        self.end_time = end_time
        self.execution_time = execution_time
        self.instance_id = instance_id
        self.item_condition_array = item_condition_array
        self.item_condition_express = item_condition_express
        self.item_condition_type = item_condition_type
        self.item_table_meta_id = item_table_meta_id
        self.name = name
        self.scene_id = scene_id
        self.start_time = start_time
        self.statis_behavior_condition_array = statis_behavior_condition_array
        self.statis_behavior_condition_express = statis_behavior_condition_express
        self.statis_behavior_condition_type = statis_behavior_condition_type
        self.traffic_control_targets = traffic_control_targets
        self.user_condition_array = user_condition_array
        self.user_condition_express = user_condition_express
        self.user_condition_type = user_condition_type
        self.user_table_meta_id = user_table_meta_id

    def validate(self):
        if self.traffic_control_targets:
            for k in self.traffic_control_targets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.behavior_table_meta_id is not None:
            result['BehaviorTableMetaId'] = self.behavior_table_meta_id
        if self.control_granularity is not None:
            result['ControlGranularity'] = self.control_granularity
        if self.control_logic is not None:
            result['ControlLogic'] = self.control_logic
        if self.control_type is not None:
            result['ControlType'] = self.control_type
        if self.description is not None:
            result['Description'] = self.description
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.execution_time is not None:
            result['ExecutionTime'] = self.execution_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.item_condition_array is not None:
            result['ItemConditionArray'] = self.item_condition_array
        if self.item_condition_express is not None:
            result['ItemConditionExpress'] = self.item_condition_express
        if self.item_condition_type is not None:
            result['ItemConditionType'] = self.item_condition_type
        if self.item_table_meta_id is not None:
            result['ItemTableMetaId'] = self.item_table_meta_id
        if self.name is not None:
            result['Name'] = self.name
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.statis_behavior_condition_array is not None:
            result['StatisBehaviorConditionArray'] = self.statis_behavior_condition_array
        if self.statis_behavior_condition_express is not None:
            result['StatisBehaviorConditionExpress'] = self.statis_behavior_condition_express
        if self.statis_behavior_condition_type is not None:
            result['StatisBehaviorConditionType'] = self.statis_behavior_condition_type
        result['TrafficControlTargets'] = []
        if self.traffic_control_targets is not None:
            for k in self.traffic_control_targets:
                result['TrafficControlTargets'].append(k.to_map() if k else None)
        if self.user_condition_array is not None:
            result['UserConditionArray'] = self.user_condition_array
        if self.user_condition_express is not None:
            result['UserConditionExpress'] = self.user_condition_express
        if self.user_condition_type is not None:
            result['UserConditionType'] = self.user_condition_type
        if self.user_table_meta_id is not None:
            result['UserTableMetaId'] = self.user_table_meta_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BehaviorTableMetaId') is not None:
            self.behavior_table_meta_id = m.get('BehaviorTableMetaId')
        if m.get('ControlGranularity') is not None:
            self.control_granularity = m.get('ControlGranularity')
        if m.get('ControlLogic') is not None:
            self.control_logic = m.get('ControlLogic')
        if m.get('ControlType') is not None:
            self.control_type = m.get('ControlType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ExecutionTime') is not None:
            self.execution_time = m.get('ExecutionTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ItemConditionArray') is not None:
            self.item_condition_array = m.get('ItemConditionArray')
        if m.get('ItemConditionExpress') is not None:
            self.item_condition_express = m.get('ItemConditionExpress')
        if m.get('ItemConditionType') is not None:
            self.item_condition_type = m.get('ItemConditionType')
        if m.get('ItemTableMetaId') is not None:
            self.item_table_meta_id = m.get('ItemTableMetaId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StatisBehaviorConditionArray') is not None:
            self.statis_behavior_condition_array = m.get('StatisBehaviorConditionArray')
        if m.get('StatisBehaviorConditionExpress') is not None:
            self.statis_behavior_condition_express = m.get('StatisBehaviorConditionExpress')
        if m.get('StatisBehaviorConditionType') is not None:
            self.statis_behavior_condition_type = m.get('StatisBehaviorConditionType')
        self.traffic_control_targets = []
        if m.get('TrafficControlTargets') is not None:
            for k in m.get('TrafficControlTargets'):
                temp_model = CreateTrafficControlTaskRequestTrafficControlTargets()
                self.traffic_control_targets.append(temp_model.from_map(k))
        if m.get('UserConditionArray') is not None:
            self.user_condition_array = m.get('UserConditionArray')
        if m.get('UserConditionExpress') is not None:
            self.user_condition_express = m.get('UserConditionExpress')
        if m.get('UserConditionType') is not None:
            self.user_condition_type = m.get('UserConditionType')
        if m.get('UserTableMetaId') is not None:
            self.user_table_meta_id = m.get('UserTableMetaId')
        return self


class CreateTrafficControlTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        traffic_control_task_id: str = None,
    ):
        self.request_id = request_id
        self.traffic_control_task_id = traffic_control_task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.traffic_control_task_id is not None:
            result['TrafficControlTaskId'] = self.traffic_control_task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TrafficControlTaskId') is not None:
            self.traffic_control_task_id = m.get('TrafficControlTaskId')
        return self


class CreateTrafficControlTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateTrafficControlTaskResponseBody = None,
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
            temp_model = CreateTrafficControlTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DebugResourceRuleRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        metric_info: Dict[str, Any] = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.metric_info = metric_info
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.metric_info is not None:
            result['MetricInfo'] = self.metric_info
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MetricInfo') is not None:
            self.metric_info = m.get('MetricInfo')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DebugResourceRuleShrinkRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        metric_info_shrink: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.metric_info_shrink = metric_info_shrink
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.metric_info_shrink is not None:
            result['MetricInfo'] = self.metric_info_shrink
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MetricInfo') is not None:
            self.metric_info_shrink = m.get('MetricInfo')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DebugResourceRuleResponseBody(TeaModel):
    def __init__(
        self,
        current_values: Dict[str, Any] = None,
        output_values: Dict[str, Any] = None,
        request_id: str = None,
    ):
        self.current_values = current_values
        self.output_values = output_values
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_values is not None:
            result['CurrentValues'] = self.current_values
        if self.output_values is not None:
            result['OutputValues'] = self.output_values
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentValues') is not None:
            self.current_values = m.get('CurrentValues')
        if m.get('OutputValues') is not None:
            self.output_values = m.get('OutputValues')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DebugResourceRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DebugResourceRuleResponseBody = None,
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
            temp_model = DebugResourceRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteABMetricRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DeleteABMetricResponseBody(TeaModel):
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


class DeleteABMetricResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteABMetricResponseBody = None,
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
            temp_model = DeleteABMetricResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteABMetricGroupRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DeleteABMetricGroupResponseBody(TeaModel):
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


class DeleteABMetricGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteABMetricGroupResponseBody = None,
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
            temp_model = DeleteABMetricGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCrowdRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DeleteCrowdResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
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


class DeleteCrowdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteCrowdResponseBody = None,
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
            temp_model = DeleteCrowdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteExperimentRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DeleteExperimentResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
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


class DeleteExperimentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteExperimentResponseBody = None,
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
            temp_model = DeleteExperimentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteExperimentGroupRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DeleteExperimentGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
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


class DeleteExperimentGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteExperimentGroupResponseBody = None,
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
            temp_model = DeleteExperimentGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteInstanceResourceResponseBody(TeaModel):
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


class DeleteInstanceResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteInstanceResourceResponseBody = None,
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
            temp_model = DeleteInstanceResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteLaboratoryRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DeleteLaboratoryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
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


class DeleteLaboratoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteLaboratoryResponseBody = None,
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
            temp_model = DeleteLaboratoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteLayerRequest(TeaModel):
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
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DeleteLayerResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
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


class DeleteLayerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteLayerResponseBody = None,
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
            temp_model = DeleteLayerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteParamRequest(TeaModel):
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
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DeleteParamResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
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


class DeleteParamResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteParamResponseBody = None,
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
            temp_model = DeleteParamResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteResourceRuleRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DeleteResourceRuleResponseBody(TeaModel):
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


class DeleteResourceRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteResourceRuleResponseBody = None,
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
            temp_model = DeleteResourceRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteResourceRuleItemRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DeleteResourceRuleItemResponseBody(TeaModel):
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


class DeleteResourceRuleItemResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteResourceRuleItemResponseBody = None,
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
            temp_model = DeleteResourceRuleItemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSceneRequest(TeaModel):
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
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DeleteSceneResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
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


class DeleteSceneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteSceneResponseBody = None,
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
            temp_model = DeleteSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSubCrowdRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DeleteSubCrowdResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
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


class DeleteSubCrowdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteSubCrowdResponseBody = None,
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
            temp_model = DeleteSubCrowdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTableMetaRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DeleteTableMetaResponseBody(TeaModel):
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


class DeleteTableMetaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteTableMetaResponseBody = None,
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
            temp_model = DeleteTableMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTrafficControlTargetRequest(TeaModel):
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
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DeleteTrafficControlTargetResponseBody(TeaModel):
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


class DeleteTrafficControlTargetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteTrafficControlTargetResponseBody = None,
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
            temp_model = DeleteTrafficControlTargetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTrafficControlTaskRequest(TeaModel):
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
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DeleteTrafficControlTaskResponseBody(TeaModel):
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


class DeleteTrafficControlTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteTrafficControlTaskResponseBody = None,
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
            temp_model = DeleteTrafficControlTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateTrafficControlTaskCodeRequest(TeaModel):
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
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GenerateTrafficControlTaskCodeResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        request_id: str = None,
    ):
        self.code = code
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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GenerateTrafficControlTaskCodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GenerateTrafficControlTaskCodeResponseBody = None,
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
            temp_model = GenerateTrafficControlTaskCodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateTrafficControlTaskConfigRequest(TeaModel):
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
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GenerateTrafficControlTaskConfigResponseBody(TeaModel):
    def __init__(
        self,
        config: str = None,
        request_id: str = None,
    ):
        self.config = config
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GenerateTrafficControlTaskConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GenerateTrafficControlTaskConfigResponseBody = None,
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
            temp_model = GenerateTrafficControlTaskConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetABMetricRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetABMetricResponseBody(TeaModel):
    def __init__(
        self,
        definition: str = None,
        description: str = None,
        left_metric_id: str = None,
        name: str = None,
        operator: str = None,
        realtime: str = None,
        request_id: str = None,
        result_resource_id: str = None,
        result_table_meta_id: str = None,
        right_metric_id: str = None,
        scene_id: str = None,
        scene_name: str = None,
        statistics_cycle: int = None,
        table_meta_id: str = None,
        type: str = None,
    ):
        self.definition = definition
        self.description = description
        self.left_metric_id = left_metric_id
        self.name = name
        self.operator = operator
        self.realtime = realtime
        self.request_id = request_id
        self.result_resource_id = result_resource_id
        self.result_table_meta_id = result_table_meta_id
        self.right_metric_id = right_metric_id
        self.scene_id = scene_id
        self.scene_name = scene_name
        self.statistics_cycle = statistics_cycle
        self.table_meta_id = table_meta_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.definition is not None:
            result['Definition'] = self.definition
        if self.description is not None:
            result['Description'] = self.description
        if self.left_metric_id is not None:
            result['LeftMetricId'] = self.left_metric_id
        if self.name is not None:
            result['Name'] = self.name
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.realtime is not None:
            result['Realtime'] = self.realtime
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_resource_id is not None:
            result['ResultResourceId'] = self.result_resource_id
        if self.result_table_meta_id is not None:
            result['ResultTableMetaId'] = self.result_table_meta_id
        if self.right_metric_id is not None:
            result['RightMetricId'] = self.right_metric_id
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.scene_name is not None:
            result['SceneName'] = self.scene_name
        if self.statistics_cycle is not None:
            result['StatisticsCycle'] = self.statistics_cycle
        if self.table_meta_id is not None:
            result['TableMetaId'] = self.table_meta_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Definition') is not None:
            self.definition = m.get('Definition')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('LeftMetricId') is not None:
            self.left_metric_id = m.get('LeftMetricId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('Realtime') is not None:
            self.realtime = m.get('Realtime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultResourceId') is not None:
            self.result_resource_id = m.get('ResultResourceId')
        if m.get('ResultTableMetaId') is not None:
            self.result_table_meta_id = m.get('ResultTableMetaId')
        if m.get('RightMetricId') is not None:
            self.right_metric_id = m.get('RightMetricId')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('SceneName') is not None:
            self.scene_name = m.get('SceneName')
        if m.get('StatisticsCycle') is not None:
            self.statistics_cycle = m.get('StatisticsCycle')
        if m.get('TableMetaId') is not None:
            self.table_meta_id = m.get('TableMetaId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetABMetricResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetABMetricResponseBody = None,
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
            temp_model = GetABMetricResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetABMetricGroupRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetABMetricGroupResponseBody(TeaModel):
    def __init__(
        self,
        abmetric_ids: str = None,
        abmetric_names: str = None,
        description: str = None,
        name: str = None,
        owner: str = None,
        realtime: bool = None,
        request_id: str = None,
        scene_id: str = None,
    ):
        self.abmetric_ids = abmetric_ids
        self.abmetric_names = abmetric_names
        self.description = description
        self.name = name
        self.owner = owner
        self.realtime = realtime
        self.request_id = request_id
        self.scene_id = scene_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.abmetric_ids is not None:
            result['ABMetricIds'] = self.abmetric_ids
        if self.abmetric_names is not None:
            result['ABMetricNames'] = self.abmetric_names
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.realtime is not None:
            result['Realtime'] = self.realtime
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ABMetricIds') is not None:
            self.abmetric_ids = m.get('ABMetricIds')
        if m.get('ABMetricNames') is not None:
            self.abmetric_names = m.get('ABMetricNames')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('Realtime') is not None:
            self.realtime = m.get('Realtime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        return self


class GetABMetricGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetABMetricGroupResponseBody = None,
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
            temp_model = GetABMetricGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCalculationJobRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetCalculationJobResponseBody(TeaModel):
    def __init__(
        self,
        abmetric_id: str = None,
        abmetric_name: str = None,
        biz_date: str = None,
        config: str = None,
        gmt_ran_time: str = None,
        job_message: List[str] = None,
        job_source: str = None,
        request_id: str = None,
        status: str = None,
    ):
        self.abmetric_id = abmetric_id
        self.abmetric_name = abmetric_name
        self.biz_date = biz_date
        self.config = config
        self.gmt_ran_time = gmt_ran_time
        self.job_message = job_message
        self.job_source = job_source
        self.request_id = request_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.abmetric_id is not None:
            result['ABMetricId'] = self.abmetric_id
        if self.abmetric_name is not None:
            result['ABMetricName'] = self.abmetric_name
        if self.biz_date is not None:
            result['BizDate'] = self.biz_date
        if self.config is not None:
            result['Config'] = self.config
        if self.gmt_ran_time is not None:
            result['GmtRanTime'] = self.gmt_ran_time
        if self.job_message is not None:
            result['JobMessage'] = self.job_message
        if self.job_source is not None:
            result['JobSource'] = self.job_source
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ABMetricId') is not None:
            self.abmetric_id = m.get('ABMetricId')
        if m.get('ABMetricName') is not None:
            self.abmetric_name = m.get('ABMetricName')
        if m.get('BizDate') is not None:
            self.biz_date = m.get('BizDate')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('GmtRanTime') is not None:
            self.gmt_ran_time = m.get('GmtRanTime')
        if m.get('JobMessage') is not None:
            self.job_message = m.get('JobMessage')
        if m.get('JobSource') is not None:
            self.job_source = m.get('JobSource')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetCalculationJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetCalculationJobResponseBody = None,
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
            temp_model = GetCalculationJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetExperimentRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetExperimentResponseBody(TeaModel):
    def __init__(
        self,
        alias_experiment_id: str = None,
        buckets: str = None,
        config: str = None,
        debug_crowd_id: str = None,
        debug_users: str = None,
        description: str = None,
        experiment_group_id: str = None,
        flow_percent: int = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        laboratory_id: str = None,
        layer_id: str = None,
        name: str = None,
        request_id: str = None,
        scene_id: str = None,
        status: str = None,
        type: str = None,
    ):
        self.alias_experiment_id = alias_experiment_id
        self.buckets = buckets
        self.config = config
        self.debug_crowd_id = debug_crowd_id
        self.debug_users = debug_users
        self.description = description
        self.experiment_group_id = experiment_group_id
        self.flow_percent = flow_percent
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.laboratory_id = laboratory_id
        self.layer_id = layer_id
        self.name = name
        # Id of the request
        self.request_id = request_id
        self.scene_id = scene_id
        self.status = status
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias_experiment_id is not None:
            result['AliasExperimentId'] = self.alias_experiment_id
        if self.buckets is not None:
            result['Buckets'] = self.buckets
        if self.config is not None:
            result['Config'] = self.config
        if self.debug_crowd_id is not None:
            result['DebugCrowdId'] = self.debug_crowd_id
        if self.debug_users is not None:
            result['DebugUsers'] = self.debug_users
        if self.description is not None:
            result['Description'] = self.description
        if self.experiment_group_id is not None:
            result['ExperimentGroupId'] = self.experiment_group_id
        if self.flow_percent is not None:
            result['FlowPercent'] = self.flow_percent
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.laboratory_id is not None:
            result['LaboratoryId'] = self.laboratory_id
        if self.layer_id is not None:
            result['LayerId'] = self.layer_id
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliasExperimentId') is not None:
            self.alias_experiment_id = m.get('AliasExperimentId')
        if m.get('Buckets') is not None:
            self.buckets = m.get('Buckets')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('DebugCrowdId') is not None:
            self.debug_crowd_id = m.get('DebugCrowdId')
        if m.get('DebugUsers') is not None:
            self.debug_users = m.get('DebugUsers')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExperimentGroupId') is not None:
            self.experiment_group_id = m.get('ExperimentGroupId')
        if m.get('FlowPercent') is not None:
            self.flow_percent = m.get('FlowPercent')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('LaboratoryId') is not None:
            self.laboratory_id = m.get('LaboratoryId')
        if m.get('LayerId') is not None:
            self.layer_id = m.get('LayerId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetExperimentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetExperimentResponseBody = None,
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
            temp_model = GetExperimentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetExperimentGroupRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetExperimentGroupResponseBody(TeaModel):
    def __init__(
        self,
        config: str = None,
        crowd_id: str = None,
        crowd_target_type: str = None,
        debug_crowd_id: str = None,
        debug_users: str = None,
        description: str = None,
        distribution_time_duration: int = None,
        distribution_type: str = None,
        filter: str = None,
        holding_buckets: str = None,
        laboratory_id: str = None,
        layer_id: str = None,
        name: str = None,
        need_aa: bool = None,
        owner: str = None,
        random_flow: int = None,
        request_id: str = None,
        reserved_buckets: str = None,
        scene_id: str = None,
        status: str = None,
    ):
        self.config = config
        self.crowd_id = crowd_id
        self.crowd_target_type = crowd_target_type
        self.debug_crowd_id = debug_crowd_id
        self.debug_users = debug_users
        self.description = description
        self.distribution_time_duration = distribution_time_duration
        self.distribution_type = distribution_type
        self.filter = filter
        self.holding_buckets = holding_buckets
        self.laboratory_id = laboratory_id
        self.layer_id = layer_id
        self.name = name
        self.need_aa = need_aa
        self.owner = owner
        self.random_flow = random_flow
        # Id of the request
        self.request_id = request_id
        self.reserved_buckets = reserved_buckets
        self.scene_id = scene_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.crowd_id is not None:
            result['CrowdId'] = self.crowd_id
        if self.crowd_target_type is not None:
            result['CrowdTargetType'] = self.crowd_target_type
        if self.debug_crowd_id is not None:
            result['DebugCrowdId'] = self.debug_crowd_id
        if self.debug_users is not None:
            result['DebugUsers'] = self.debug_users
        if self.description is not None:
            result['Description'] = self.description
        if self.distribution_time_duration is not None:
            result['DistributionTimeDuration'] = self.distribution_time_duration
        if self.distribution_type is not None:
            result['DistributionType'] = self.distribution_type
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.holding_buckets is not None:
            result['HoldingBuckets'] = self.holding_buckets
        if self.laboratory_id is not None:
            result['LaboratoryId'] = self.laboratory_id
        if self.layer_id is not None:
            result['LayerId'] = self.layer_id
        if self.name is not None:
            result['Name'] = self.name
        if self.need_aa is not None:
            result['NeedAA'] = self.need_aa
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.random_flow is not None:
            result['RandomFlow'] = self.random_flow
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.reserved_buckets is not None:
            result['ReservedBuckets'] = self.reserved_buckets
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('CrowdId') is not None:
            self.crowd_id = m.get('CrowdId')
        if m.get('CrowdTargetType') is not None:
            self.crowd_target_type = m.get('CrowdTargetType')
        if m.get('DebugCrowdId') is not None:
            self.debug_crowd_id = m.get('DebugCrowdId')
        if m.get('DebugUsers') is not None:
            self.debug_users = m.get('DebugUsers')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DistributionTimeDuration') is not None:
            self.distribution_time_duration = m.get('DistributionTimeDuration')
        if m.get('DistributionType') is not None:
            self.distribution_type = m.get('DistributionType')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('HoldingBuckets') is not None:
            self.holding_buckets = m.get('HoldingBuckets')
        if m.get('LaboratoryId') is not None:
            self.laboratory_id = m.get('LaboratoryId')
        if m.get('LayerId') is not None:
            self.layer_id = m.get('LayerId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NeedAA') is not None:
            self.need_aa = m.get('NeedAA')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('RandomFlow') is not None:
            self.random_flow = m.get('RandomFlow')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ReservedBuckets') is not None:
            self.reserved_buckets = m.get('ReservedBuckets')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetExperimentGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetExperimentGroupResponseBody = None,
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
            temp_model = GetExperimentGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFeatureConsistencyCheckJobRequest(TeaModel):
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
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetFeatureConsistencyCheckJobResponseBody(TeaModel):
    def __init__(
        self,
        config: str = None,
        feature_consistency_check_job_config_id: str = None,
        feature_consistency_check_job_config_name: str = None,
        gmt_end_time: str = None,
        gmt_start_time: str = None,
        logs: List[str] = None,
        request_id: str = None,
        status: str = None,
    ):
        self.config = config
        self.feature_consistency_check_job_config_id = feature_consistency_check_job_config_id
        self.feature_consistency_check_job_config_name = feature_consistency_check_job_config_name
        self.gmt_end_time = gmt_end_time
        self.gmt_start_time = gmt_start_time
        self.logs = logs
        self.request_id = request_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.feature_consistency_check_job_config_id is not None:
            result['FeatureConsistencyCheckJobConfigId'] = self.feature_consistency_check_job_config_id
        if self.feature_consistency_check_job_config_name is not None:
            result['FeatureConsistencyCheckJobConfigName'] = self.feature_consistency_check_job_config_name
        if self.gmt_end_time is not None:
            result['GmtEndTime'] = self.gmt_end_time
        if self.gmt_start_time is not None:
            result['GmtStartTime'] = self.gmt_start_time
        if self.logs is not None:
            result['Logs'] = self.logs
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('FeatureConsistencyCheckJobConfigId') is not None:
            self.feature_consistency_check_job_config_id = m.get('FeatureConsistencyCheckJobConfigId')
        if m.get('FeatureConsistencyCheckJobConfigName') is not None:
            self.feature_consistency_check_job_config_name = m.get('FeatureConsistencyCheckJobConfigName')
        if m.get('GmtEndTime') is not None:
            self.gmt_end_time = m.get('GmtEndTime')
        if m.get('GmtStartTime') is not None:
            self.gmt_start_time = m.get('GmtStartTime')
        if m.get('Logs') is not None:
            self.logs = m.get('Logs')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetFeatureConsistencyCheckJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetFeatureConsistencyCheckJobResponseBody = None,
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
            temp_model = GetFeatureConsistencyCheckJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFeatureConsistencyCheckJobConfigRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetFeatureConsistencyCheckJobConfigResponseBody(TeaModel):
    def __init__(
        self,
        compare_feature: bool = None,
        eas_service_name: str = None,
        easy_rec_package_path: str = None,
        easy_rec_version: str = None,
        feature_display_exclude: str = None,
        feature_landing_resource_id: str = None,
        feature_landing_resource_uri: str = None,
        feature_priority: str = None,
        feature_store_item_id: str = None,
        feature_store_model_id: str = None,
        feature_store_project_id: str = None,
        feature_store_project_name: str = None,
        feature_store_seq_feature_view: str = None,
        feature_store_user_id: str = None,
        fg_jar_version: str = None,
        fg_json_file_name: str = None,
        generate_zip: bool = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        item_id_field: str = None,
        item_table: str = None,
        item_table_partition_field: str = None,
        item_table_partition_field_format: str = None,
        latest_job_gmt_sampling_end_time: str = None,
        latest_job_gmt_sampling_start_time: str = None,
        latest_job_id: str = None,
        name: str = None,
        oss_bucket: str = None,
        oss_resource_id: str = None,
        request_id: str = None,
        sample_rate: str = None,
        scene_id: str = None,
        scene_name: str = None,
        service_id: str = None,
        service_name: str = None,
        status: str = None,
        use_feature_store: bool = None,
        user_id_field: str = None,
        user_table: str = None,
        user_table_partition_field: str = None,
        user_table_partition_field_format: str = None,
        workflow_name: str = None,
    ):
        self.compare_feature = compare_feature
        self.eas_service_name = eas_service_name
        self.easy_rec_package_path = easy_rec_package_path
        self.easy_rec_version = easy_rec_version
        self.feature_display_exclude = feature_display_exclude
        self.feature_landing_resource_id = feature_landing_resource_id
        self.feature_landing_resource_uri = feature_landing_resource_uri
        self.feature_priority = feature_priority
        self.feature_store_item_id = feature_store_item_id
        self.feature_store_model_id = feature_store_model_id
        self.feature_store_project_id = feature_store_project_id
        self.feature_store_project_name = feature_store_project_name
        self.feature_store_seq_feature_view = feature_store_seq_feature_view
        self.feature_store_user_id = feature_store_user_id
        self.fg_jar_version = fg_jar_version
        self.fg_json_file_name = fg_json_file_name
        self.generate_zip = generate_zip
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.item_id_field = item_id_field
        self.item_table = item_table
        self.item_table_partition_field = item_table_partition_field
        self.item_table_partition_field_format = item_table_partition_field_format
        self.latest_job_gmt_sampling_end_time = latest_job_gmt_sampling_end_time
        self.latest_job_gmt_sampling_start_time = latest_job_gmt_sampling_start_time
        self.latest_job_id = latest_job_id
        self.name = name
        self.oss_bucket = oss_bucket
        self.oss_resource_id = oss_resource_id
        self.request_id = request_id
        self.sample_rate = sample_rate
        self.scene_id = scene_id
        self.scene_name = scene_name
        self.service_id = service_id
        self.service_name = service_name
        self.status = status
        self.use_feature_store = use_feature_store
        self.user_id_field = user_id_field
        self.user_table = user_table
        self.user_table_partition_field = user_table_partition_field
        self.user_table_partition_field_format = user_table_partition_field_format
        self.workflow_name = workflow_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compare_feature is not None:
            result['CompareFeature'] = self.compare_feature
        if self.eas_service_name is not None:
            result['EasServiceName'] = self.eas_service_name
        if self.easy_rec_package_path is not None:
            result['EasyRecPackagePath'] = self.easy_rec_package_path
        if self.easy_rec_version is not None:
            result['EasyRecVersion'] = self.easy_rec_version
        if self.feature_display_exclude is not None:
            result['FeatureDisplayExclude'] = self.feature_display_exclude
        if self.feature_landing_resource_id is not None:
            result['FeatureLandingResourceId'] = self.feature_landing_resource_id
        if self.feature_landing_resource_uri is not None:
            result['FeatureLandingResourceUri'] = self.feature_landing_resource_uri
        if self.feature_priority is not None:
            result['FeaturePriority'] = self.feature_priority
        if self.feature_store_item_id is not None:
            result['FeatureStoreItemId'] = self.feature_store_item_id
        if self.feature_store_model_id is not None:
            result['FeatureStoreModelId'] = self.feature_store_model_id
        if self.feature_store_project_id is not None:
            result['FeatureStoreProjectId'] = self.feature_store_project_id
        if self.feature_store_project_name is not None:
            result['FeatureStoreProjectName'] = self.feature_store_project_name
        if self.feature_store_seq_feature_view is not None:
            result['FeatureStoreSeqFeatureView'] = self.feature_store_seq_feature_view
        if self.feature_store_user_id is not None:
            result['FeatureStoreUserId'] = self.feature_store_user_id
        if self.fg_jar_version is not None:
            result['FgJarVersion'] = self.fg_jar_version
        if self.fg_json_file_name is not None:
            result['FgJsonFileName'] = self.fg_json_file_name
        if self.generate_zip is not None:
            result['GenerateZip'] = self.generate_zip
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.item_id_field is not None:
            result['ItemIdField'] = self.item_id_field
        if self.item_table is not None:
            result['ItemTable'] = self.item_table
        if self.item_table_partition_field is not None:
            result['ItemTablePartitionField'] = self.item_table_partition_field
        if self.item_table_partition_field_format is not None:
            result['ItemTablePartitionFieldFormat'] = self.item_table_partition_field_format
        if self.latest_job_gmt_sampling_end_time is not None:
            result['LatestJobGmtSamplingEndTime'] = self.latest_job_gmt_sampling_end_time
        if self.latest_job_gmt_sampling_start_time is not None:
            result['LatestJobGmtSamplingStartTime'] = self.latest_job_gmt_sampling_start_time
        if self.latest_job_id is not None:
            result['LatestJobId'] = self.latest_job_id
        if self.name is not None:
            result['Name'] = self.name
        if self.oss_bucket is not None:
            result['OssBucket'] = self.oss_bucket
        if self.oss_resource_id is not None:
            result['OssResourceId'] = self.oss_resource_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sample_rate is not None:
            result['SampleRate'] = self.sample_rate
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.scene_name is not None:
            result['SceneName'] = self.scene_name
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.status is not None:
            result['Status'] = self.status
        if self.use_feature_store is not None:
            result['UseFeatureStore'] = self.use_feature_store
        if self.user_id_field is not None:
            result['UserIdField'] = self.user_id_field
        if self.user_table is not None:
            result['UserTable'] = self.user_table
        if self.user_table_partition_field is not None:
            result['UserTablePartitionField'] = self.user_table_partition_field
        if self.user_table_partition_field_format is not None:
            result['UserTablePartitionFieldFormat'] = self.user_table_partition_field_format
        if self.workflow_name is not None:
            result['WorkflowName'] = self.workflow_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompareFeature') is not None:
            self.compare_feature = m.get('CompareFeature')
        if m.get('EasServiceName') is not None:
            self.eas_service_name = m.get('EasServiceName')
        if m.get('EasyRecPackagePath') is not None:
            self.easy_rec_package_path = m.get('EasyRecPackagePath')
        if m.get('EasyRecVersion') is not None:
            self.easy_rec_version = m.get('EasyRecVersion')
        if m.get('FeatureDisplayExclude') is not None:
            self.feature_display_exclude = m.get('FeatureDisplayExclude')
        if m.get('FeatureLandingResourceId') is not None:
            self.feature_landing_resource_id = m.get('FeatureLandingResourceId')
        if m.get('FeatureLandingResourceUri') is not None:
            self.feature_landing_resource_uri = m.get('FeatureLandingResourceUri')
        if m.get('FeaturePriority') is not None:
            self.feature_priority = m.get('FeaturePriority')
        if m.get('FeatureStoreItemId') is not None:
            self.feature_store_item_id = m.get('FeatureStoreItemId')
        if m.get('FeatureStoreModelId') is not None:
            self.feature_store_model_id = m.get('FeatureStoreModelId')
        if m.get('FeatureStoreProjectId') is not None:
            self.feature_store_project_id = m.get('FeatureStoreProjectId')
        if m.get('FeatureStoreProjectName') is not None:
            self.feature_store_project_name = m.get('FeatureStoreProjectName')
        if m.get('FeatureStoreSeqFeatureView') is not None:
            self.feature_store_seq_feature_view = m.get('FeatureStoreSeqFeatureView')
        if m.get('FeatureStoreUserId') is not None:
            self.feature_store_user_id = m.get('FeatureStoreUserId')
        if m.get('FgJarVersion') is not None:
            self.fg_jar_version = m.get('FgJarVersion')
        if m.get('FgJsonFileName') is not None:
            self.fg_json_file_name = m.get('FgJsonFileName')
        if m.get('GenerateZip') is not None:
            self.generate_zip = m.get('GenerateZip')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('ItemIdField') is not None:
            self.item_id_field = m.get('ItemIdField')
        if m.get('ItemTable') is not None:
            self.item_table = m.get('ItemTable')
        if m.get('ItemTablePartitionField') is not None:
            self.item_table_partition_field = m.get('ItemTablePartitionField')
        if m.get('ItemTablePartitionFieldFormat') is not None:
            self.item_table_partition_field_format = m.get('ItemTablePartitionFieldFormat')
        if m.get('LatestJobGmtSamplingEndTime') is not None:
            self.latest_job_gmt_sampling_end_time = m.get('LatestJobGmtSamplingEndTime')
        if m.get('LatestJobGmtSamplingStartTime') is not None:
            self.latest_job_gmt_sampling_start_time = m.get('LatestJobGmtSamplingStartTime')
        if m.get('LatestJobId') is not None:
            self.latest_job_id = m.get('LatestJobId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OssBucket') is not None:
            self.oss_bucket = m.get('OssBucket')
        if m.get('OssResourceId') is not None:
            self.oss_resource_id = m.get('OssResourceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SampleRate') is not None:
            self.sample_rate = m.get('SampleRate')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('SceneName') is not None:
            self.scene_name = m.get('SceneName')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UseFeatureStore') is not None:
            self.use_feature_store = m.get('UseFeatureStore')
        if m.get('UserIdField') is not None:
            self.user_id_field = m.get('UserIdField')
        if m.get('UserTable') is not None:
            self.user_table = m.get('UserTable')
        if m.get('UserTablePartitionField') is not None:
            self.user_table_partition_field = m.get('UserTablePartitionField')
        if m.get('UserTablePartitionFieldFormat') is not None:
            self.user_table_partition_field_format = m.get('UserTablePartitionFieldFormat')
        if m.get('WorkflowName') is not None:
            self.workflow_name = m.get('WorkflowName')
        return self


class GetFeatureConsistencyCheckJobConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetFeatureConsistencyCheckJobConfigResponseBody = None,
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
            temp_model = GetFeatureConsistencyCheckJobConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstanceResponseBodyConfigDataManagements(TeaModel):
    def __init__(
        self,
        component_code: str = None,
        meta: Dict[str, Any] = None,
        type: str = None,
    ):
        self.component_code = component_code
        self.meta = meta
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_code is not None:
            result['ComponentCode'] = self.component_code
        if self.meta is not None:
            result['Meta'] = self.meta
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComponentCode') is not None:
            self.component_code = m.get('ComponentCode')
        if m.get('Meta') is not None:
            self.meta = m.get('Meta')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetInstanceResponseBodyConfigEngines(TeaModel):
    def __init__(
        self,
        component_code: str = None,
        meta: Dict[str, Any] = None,
        type: str = None,
    ):
        self.component_code = component_code
        self.meta = meta
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_code is not None:
            result['ComponentCode'] = self.component_code
        if self.meta is not None:
            result['Meta'] = self.meta
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComponentCode') is not None:
            self.component_code = m.get('ComponentCode')
        if m.get('Meta') is not None:
            self.meta = m.get('Meta')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetInstanceResponseBodyConfigMonitors(TeaModel):
    def __init__(
        self,
        component_code: str = None,
        meta: Dict[str, Any] = None,
        type: str = None,
    ):
        self.component_code = component_code
        self.meta = meta
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_code is not None:
            result['ComponentCode'] = self.component_code
        if self.meta is not None:
            result['Meta'] = self.meta
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComponentCode') is not None:
            self.component_code = m.get('ComponentCode')
        if m.get('Meta') is not None:
            self.meta = m.get('Meta')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetInstanceResponseBodyConfig(TeaModel):
    def __init__(
        self,
        data_managements: List[GetInstanceResponseBodyConfigDataManagements] = None,
        engines: List[GetInstanceResponseBodyConfigEngines] = None,
        monitors: List[GetInstanceResponseBodyConfigMonitors] = None,
    ):
        self.data_managements = data_managements
        self.engines = engines
        self.monitors = monitors

    def validate(self):
        if self.data_managements:
            for k in self.data_managements:
                if k:
                    k.validate()
        if self.engines:
            for k in self.engines:
                if k:
                    k.validate()
        if self.monitors:
            for k in self.monitors:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataManagements'] = []
        if self.data_managements is not None:
            for k in self.data_managements:
                result['DataManagements'].append(k.to_map() if k else None)
        result['Engines'] = []
        if self.engines is not None:
            for k in self.engines:
                result['Engines'].append(k.to_map() if k else None)
        result['Monitors'] = []
        if self.monitors is not None:
            for k in self.monitors:
                result['Monitors'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_managements = []
        if m.get('DataManagements') is not None:
            for k in m.get('DataManagements'):
                temp_model = GetInstanceResponseBodyConfigDataManagements()
                self.data_managements.append(temp_model.from_map(k))
        self.engines = []
        if m.get('Engines') is not None:
            for k in m.get('Engines'):
                temp_model = GetInstanceResponseBodyConfigEngines()
                self.engines.append(temp_model.from_map(k))
        self.monitors = []
        if m.get('Monitors') is not None:
            for k in m.get('Monitors'):
                temp_model = GetInstanceResponseBodyConfigMonitors()
                self.monitors.append(temp_model.from_map(k))
        return self


class GetInstanceResponseBody(TeaModel):
    def __init__(
        self,
        charge_type: str = None,
        commodity_code: str = None,
        config: GetInstanceResponseBodyConfig = None,
        expired_time: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        instance_id: str = None,
        region_id: str = None,
        request_id: str = None,
        status: str = None,
        type: str = None,
    ):
        self.charge_type = charge_type
        self.commodity_code = commodity_code
        self.config = config
        self.expired_time = expired_time
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.instance_id = instance_id
        self.region_id = region_id
        self.request_id = request_id
        self.status = status
        self.type = type

    def validate(self):
        if self.config:
            self.config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.config is not None:
            result['Config'] = self.config.to_map()
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('Config') is not None:
            temp_model = GetInstanceResponseBodyConfig()
            self.config = temp_model.from_map(m['Config'])
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetInstanceResponseBody = None,
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
            temp_model = GetInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstanceResourceResponseBody(TeaModel):
    def __init__(
        self,
        category: str = None,
        config: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        group: str = None,
        request_id: str = None,
        resource_id: str = None,
        type: str = None,
        uri: str = None,
    ):
        self.category = category
        self.config = config
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.group = group
        self.request_id = request_id
        self.resource_id = resource_id
        self.type = type
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.config is not None:
            result['Config'] = self.config
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.group is not None:
            result['Group'] = self.group
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.type is not None:
            result['Type'] = self.type
        if self.uri is not None:
            result['Uri'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        return self


class GetInstanceResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetInstanceResourceResponseBody = None,
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
            temp_model = GetInstanceResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstanceResourceTableResponseBodyFields(TeaModel):
    def __init__(
        self,
        is_dimension_field: bool = None,
        is_partition_field: bool = None,
        meaning: str = None,
        name: str = None,
        type: str = None,
    ):
        self.is_dimension_field = is_dimension_field
        self.is_partition_field = is_partition_field
        self.meaning = meaning
        self.name = name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_dimension_field is not None:
            result['IsDimensionField'] = self.is_dimension_field
        if self.is_partition_field is not None:
            result['IsPartitionField'] = self.is_partition_field
        if self.meaning is not None:
            result['Meaning'] = self.meaning
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsDimensionField') is not None:
            self.is_dimension_field = m.get('IsDimensionField')
        if m.get('IsPartitionField') is not None:
            self.is_partition_field = m.get('IsPartitionField')
        if m.get('Meaning') is not None:
            self.meaning = m.get('Meaning')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetInstanceResourceTableResponseBody(TeaModel):
    def __init__(
        self,
        fields: List[GetInstanceResourceTableResponseBodyFields] = None,
        request_id: str = None,
        table_name: str = None,
    ):
        self.fields = fields
        self.request_id = request_id
        self.table_name = table_name

    def validate(self):
        if self.fields:
            for k in self.fields:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Fields'] = []
        if self.fields is not None:
            for k in self.fields:
                result['Fields'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.fields = []
        if m.get('Fields') is not None:
            for k in m.get('Fields'):
                temp_model = GetInstanceResourceTableResponseBodyFields()
                self.fields.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class GetInstanceResourceTableResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetInstanceResourceTableResponseBody = None,
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
            temp_model = GetInstanceResourceTableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLaboratoryRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetLaboratoryResponseBody(TeaModel):
    def __init__(
        self,
        bucket_count: int = None,
        bucket_type: str = None,
        buckets: str = None,
        crowd_id: str = None,
        debug_crowd_id: str = None,
        debug_users: str = None,
        description: str = None,
        environment: str = None,
        filter: str = None,
        name: str = None,
        request_id: str = None,
        scene_id: str = None,
        status: str = None,
        type: str = None,
    ):
        self.bucket_count = bucket_count
        self.bucket_type = bucket_type
        self.buckets = buckets
        self.crowd_id = crowd_id
        self.debug_crowd_id = debug_crowd_id
        self.debug_users = debug_users
        self.description = description
        self.environment = environment
        self.filter = filter
        self.name = name
        # Id of the request
        self.request_id = request_id
        self.scene_id = scene_id
        self.status = status
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_count is not None:
            result['BucketCount'] = self.bucket_count
        if self.bucket_type is not None:
            result['BucketType'] = self.bucket_type
        if self.buckets is not None:
            result['Buckets'] = self.buckets
        if self.crowd_id is not None:
            result['CrowdId'] = self.crowd_id
        if self.debug_crowd_id is not None:
            result['DebugCrowdId'] = self.debug_crowd_id
        if self.debug_users is not None:
            result['DebugUsers'] = self.debug_users
        if self.description is not None:
            result['Description'] = self.description
        if self.environment is not None:
            result['Environment'] = self.environment
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketCount') is not None:
            self.bucket_count = m.get('BucketCount')
        if m.get('BucketType') is not None:
            self.bucket_type = m.get('BucketType')
        if m.get('Buckets') is not None:
            self.buckets = m.get('Buckets')
        if m.get('CrowdId') is not None:
            self.crowd_id = m.get('CrowdId')
        if m.get('DebugCrowdId') is not None:
            self.debug_crowd_id = m.get('DebugCrowdId')
        if m.get('DebugUsers') is not None:
            self.debug_users = m.get('DebugUsers')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Environment') is not None:
            self.environment = m.get('Environment')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetLaboratoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetLaboratoryResponseBody = None,
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
            temp_model = GetLaboratoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLayerRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetLayerResponseBody(TeaModel):
    def __init__(
        self,
        description: str = None,
        gmt_create_time: str = None,
        laboratory_id: str = None,
        name: str = None,
        request_id: str = None,
        residual_flow: int = None,
        scene_id: str = None,
    ):
        self.description = description
        self.gmt_create_time = gmt_create_time
        self.laboratory_id = laboratory_id
        self.name = name
        # Id of the request
        self.request_id = request_id
        self.residual_flow = residual_flow
        self.scene_id = scene_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.laboratory_id is not None:
            result['LaboratoryId'] = self.laboratory_id
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.residual_flow is not None:
            result['ResidualFlow'] = self.residual_flow
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('LaboratoryId') is not None:
            self.laboratory_id = m.get('LaboratoryId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResidualFlow') is not None:
            self.residual_flow = m.get('ResidualFlow')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        return self


class GetLayerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetLayerResponseBody = None,
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
            temp_model = GetLayerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetResourceRuleRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetResourceRuleResponseBodyRuleItems(TeaModel):
    def __init__(
        self,
        description: str = None,
        max_value: str = None,
        min_value: str = None,
        name: str = None,
        value: str = None,
    ):
        self.description = description
        self.max_value = max_value
        self.min_value = min_value
        self.name = name
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.max_value is not None:
            result['MaxValue'] = self.max_value
        if self.min_value is not None:
            result['MinValue'] = self.min_value
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('MaxValue') is not None:
            self.max_value = m.get('MaxValue')
        if m.get('MinValue') is not None:
            self.min_value = m.get('MinValue')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetResourceRuleResponseBody(TeaModel):
    def __init__(
        self,
        description: str = None,
        metric_operation_type: str = None,
        metric_pull_info: str = None,
        metric_pull_period: str = None,
        name: str = None,
        request_id: str = None,
        resource_rule_id: str = None,
        rule_computing_definition: str = None,
        rule_items: List[GetResourceRuleResponseBodyRuleItems] = None,
    ):
        self.description = description
        self.metric_operation_type = metric_operation_type
        self.metric_pull_info = metric_pull_info
        self.metric_pull_period = metric_pull_period
        self.name = name
        self.request_id = request_id
        self.resource_rule_id = resource_rule_id
        self.rule_computing_definition = rule_computing_definition
        self.rule_items = rule_items

    def validate(self):
        if self.rule_items:
            for k in self.rule_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.metric_operation_type is not None:
            result['MetricOperationType'] = self.metric_operation_type
        if self.metric_pull_info is not None:
            result['MetricPullInfo'] = self.metric_pull_info
        if self.metric_pull_period is not None:
            result['MetricPullPeriod'] = self.metric_pull_period
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_rule_id is not None:
            result['ResourceRuleId'] = self.resource_rule_id
        if self.rule_computing_definition is not None:
            result['RuleComputingDefinition'] = self.rule_computing_definition
        result['RuleItems'] = []
        if self.rule_items is not None:
            for k in self.rule_items:
                result['RuleItems'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('MetricOperationType') is not None:
            self.metric_operation_type = m.get('MetricOperationType')
        if m.get('MetricPullInfo') is not None:
            self.metric_pull_info = m.get('MetricPullInfo')
        if m.get('MetricPullPeriod') is not None:
            self.metric_pull_period = m.get('MetricPullPeriod')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceRuleId') is not None:
            self.resource_rule_id = m.get('ResourceRuleId')
        if m.get('RuleComputingDefinition') is not None:
            self.rule_computing_definition = m.get('RuleComputingDefinition')
        self.rule_items = []
        if m.get('RuleItems') is not None:
            for k in m.get('RuleItems'):
                temp_model = GetResourceRuleResponseBodyRuleItems()
                self.rule_items.append(temp_model.from_map(k))
        return self


class GetResourceRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetResourceRuleResponseBody = None,
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
            temp_model = GetResourceRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSceneRequest(TeaModel):
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
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetSceneResponseBodyFlows(TeaModel):
    def __init__(
        self,
        flow_code: str = None,
        flow_name: str = None,
    ):
        self.flow_code = flow_code
        self.flow_name = flow_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_code is not None:
            result['FlowCode'] = self.flow_code
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowCode') is not None:
            self.flow_code = m.get('FlowCode')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        return self


class GetSceneResponseBody(TeaModel):
    def __init__(
        self,
        description: str = None,
        flows: List[GetSceneResponseBodyFlows] = None,
        name: str = None,
        request_id: str = None,
    ):
        self.description = description
        self.flows = flows
        self.name = name
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.flows:
            for k in self.flows:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        result['Flows'] = []
        if self.flows is not None:
            for k in self.flows:
                result['Flows'].append(k.to_map() if k else None)
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        self.flows = []
        if m.get('Flows') is not None:
            for k in m.get('Flows'):
                temp_model = GetSceneResponseBodyFlows()
                self.flows.append(temp_model.from_map(k))
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetSceneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSceneResponseBody = None,
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
            temp_model = GetSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSubCrowdRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetSubCrowdResponseBody(TeaModel):
    def __init__(
        self,
        gmt_create_time: str = None,
        quantity: str = None,
        request_id: str = None,
        source: str = None,
        users: str = None,
    ):
        self.gmt_create_time = gmt_create_time
        self.quantity = quantity
        # Id of the request
        self.request_id = request_id
        self.source = source
        self.users = users

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.source is not None:
            result['Source'] = self.source
        if self.users is not None:
            result['Users'] = self.users
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Users') is not None:
            self.users = m.get('Users')
        return self


class GetSubCrowdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSubCrowdResponseBody = None,
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
            temp_model = GetSubCrowdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTableMetaRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetTableMetaResponseBodyFields(TeaModel):
    def __init__(
        self,
        is_dimension_field: bool = None,
        meaning: str = None,
        name: str = None,
        type: str = None,
    ):
        self.is_dimension_field = is_dimension_field
        self.meaning = meaning
        self.name = name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_dimension_field is not None:
            result['IsDimensionField'] = self.is_dimension_field
        if self.meaning is not None:
            result['Meaning'] = self.meaning
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsDimensionField') is not None:
            self.is_dimension_field = m.get('IsDimensionField')
        if m.get('Meaning') is not None:
            self.meaning = m.get('Meaning')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetTableMetaResponseBody(TeaModel):
    def __init__(
        self,
        can_delete: bool = None,
        config: str = None,
        description: str = None,
        fields: List[GetTableMetaResponseBodyFields] = None,
        gmt_create_time: str = None,
        gmt_imported_time: str = None,
        gmt_modified_time: str = None,
        module: str = None,
        name: str = None,
        request_id: str = None,
        resource_id: str = None,
        table_meta_id: str = None,
        table_name: str = None,
        type: str = None,
        url: str = None,
    ):
        self.can_delete = can_delete
        self.config = config
        self.description = description
        self.fields = fields
        self.gmt_create_time = gmt_create_time
        self.gmt_imported_time = gmt_imported_time
        self.gmt_modified_time = gmt_modified_time
        self.module = module
        self.name = name
        self.request_id = request_id
        self.resource_id = resource_id
        self.table_meta_id = table_meta_id
        self.table_name = table_name
        self.type = type
        self.url = url

    def validate(self):
        if self.fields:
            for k in self.fields:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_delete is not None:
            result['CanDelete'] = self.can_delete
        if self.config is not None:
            result['Config'] = self.config
        if self.description is not None:
            result['Description'] = self.description
        result['Fields'] = []
        if self.fields is not None:
            for k in self.fields:
                result['Fields'].append(k.to_map() if k else None)
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_imported_time is not None:
            result['GmtImportedTime'] = self.gmt_imported_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.module is not None:
            result['Module'] = self.module
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.table_meta_id is not None:
            result['TableMetaId'] = self.table_meta_id
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.type is not None:
            result['Type'] = self.type
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanDelete') is not None:
            self.can_delete = m.get('CanDelete')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        self.fields = []
        if m.get('Fields') is not None:
            for k in m.get('Fields'):
                temp_model = GetTableMetaResponseBodyFields()
                self.fields.append(temp_model.from_map(k))
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtImportedTime') is not None:
            self.gmt_imported_time = m.get('GmtImportedTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('Module') is not None:
            self.module = m.get('Module')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('TableMetaId') is not None:
            self.table_meta_id = m.get('TableMetaId')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class GetTableMetaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTableMetaResponseBody = None,
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
            temp_model = GetTableMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTrafficControlTargetRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetTrafficControlTargetResponseBodySplitParts(TeaModel):
    def __init__(
        self,
        set_values: List[int] = None,
        time_points: List[int] = None,
    ):
        self.set_values = set_values
        self.time_points = time_points

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.set_values is not None:
            result['SetValues'] = self.set_values
        if self.time_points is not None:
            result['TimePoints'] = self.time_points
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SetValues') is not None:
            self.set_values = m.get('SetValues')
        if m.get('TimePoints') is not None:
            self.time_points = m.get('TimePoints')
        return self


class GetTrafficControlTargetResponseBody(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        event: str = None,
        gmt_create_time: str = None,
        item_condition_array: str = None,
        item_condition_express: str = None,
        item_condition_type: str = None,
        name: str = None,
        new_product_regulation: bool = None,
        recall_name: str = None,
        request_id: str = None,
        split_parts: GetTrafficControlTargetResponseBodySplitParts = None,
        start_time: str = None,
        statis_period: str = None,
        status: str = None,
        tolerance_value: int = None,
        traffic_control_target_id: str = None,
        value: float = None,
    ):
        self.end_time = end_time
        self.event = event
        self.gmt_create_time = gmt_create_time
        self.item_condition_array = item_condition_array
        self.item_condition_express = item_condition_express
        self.item_condition_type = item_condition_type
        self.name = name
        self.new_product_regulation = new_product_regulation
        self.recall_name = recall_name
        self.request_id = request_id
        self.split_parts = split_parts
        self.start_time = start_time
        self.statis_period = statis_period
        self.status = status
        self.tolerance_value = tolerance_value
        self.traffic_control_target_id = traffic_control_target_id
        self.value = value

    def validate(self):
        if self.split_parts:
            self.split_parts.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.event is not None:
            result['Event'] = self.event
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.item_condition_array is not None:
            result['ItemConditionArray'] = self.item_condition_array
        if self.item_condition_express is not None:
            result['ItemConditionExpress'] = self.item_condition_express
        if self.item_condition_type is not None:
            result['ItemConditionType'] = self.item_condition_type
        if self.name is not None:
            result['Name'] = self.name
        if self.new_product_regulation is not None:
            result['NewProductRegulation'] = self.new_product_regulation
        if self.recall_name is not None:
            result['RecallName'] = self.recall_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.split_parts is not None:
            result['SplitParts'] = self.split_parts.to_map()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.statis_period is not None:
            result['StatisPeriod'] = self.statis_period
        if self.status is not None:
            result['Status'] = self.status
        if self.tolerance_value is not None:
            result['ToleranceValue'] = self.tolerance_value
        if self.traffic_control_target_id is not None:
            result['TrafficControlTargetId'] = self.traffic_control_target_id
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Event') is not None:
            self.event = m.get('Event')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('ItemConditionArray') is not None:
            self.item_condition_array = m.get('ItemConditionArray')
        if m.get('ItemConditionExpress') is not None:
            self.item_condition_express = m.get('ItemConditionExpress')
        if m.get('ItemConditionType') is not None:
            self.item_condition_type = m.get('ItemConditionType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NewProductRegulation') is not None:
            self.new_product_regulation = m.get('NewProductRegulation')
        if m.get('RecallName') is not None:
            self.recall_name = m.get('RecallName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SplitParts') is not None:
            temp_model = GetTrafficControlTargetResponseBodySplitParts()
            self.split_parts = temp_model.from_map(m['SplitParts'])
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StatisPeriod') is not None:
            self.statis_period = m.get('StatisPeriod')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ToleranceValue') is not None:
            self.tolerance_value = m.get('ToleranceValue')
        if m.get('TrafficControlTargetId') is not None:
            self.traffic_control_target_id = m.get('TrafficControlTargetId')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetTrafficControlTargetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTrafficControlTargetResponseBody = None,
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
            temp_model = GetTrafficControlTargetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTrafficControlTaskRequest(TeaModel):
    def __init__(
        self,
        control_target_filter: str = None,
        environment: str = None,
        instance_id: str = None,
        region_id: str = None,
        version: str = None,
    ):
        self.control_target_filter = control_target_filter
        self.environment = environment
        self.instance_id = instance_id
        self.region_id = region_id
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.control_target_filter is not None:
            result['ControlTargetFilter'] = self.control_target_filter
        if self.environment is not None:
            result['Environment'] = self.environment
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ControlTargetFilter') is not None:
            self.control_target_filter = m.get('ControlTargetFilter')
        if m.get('Environment') is not None:
            self.environment = m.get('Environment')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class GetTrafficControlTaskResponseBodyTrafficControlTargetsSplitParts(TeaModel):
    def __init__(
        self,
        set_points: List[int] = None,
        time_points: List[int] = None,
    ):
        self.set_points = set_points
        self.time_points = time_points

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.set_points is not None:
            result['SetPoints'] = self.set_points
        if self.time_points is not None:
            result['TimePoints'] = self.time_points
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SetPoints') is not None:
            self.set_points = m.get('SetPoints')
        if m.get('TimePoints') is not None:
            self.time_points = m.get('TimePoints')
        return self


class GetTrafficControlTaskResponseBodyTrafficControlTargets(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        event: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        item_condition_array: str = None,
        item_condition_express: str = None,
        item_condition_type: str = None,
        name: str = None,
        new_product_regulation: bool = None,
        recall_name: str = None,
        split_parts: GetTrafficControlTaskResponseBodyTrafficControlTargetsSplitParts = None,
        start_time: str = None,
        statis_period: str = None,
        status: str = None,
        tolerance_value: int = None,
        traffic_control_target_id: str = None,
        value: float = None,
    ):
        self.end_time = end_time
        self.event = event
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.item_condition_array = item_condition_array
        self.item_condition_express = item_condition_express
        self.item_condition_type = item_condition_type
        self.name = name
        self.new_product_regulation = new_product_regulation
        self.recall_name = recall_name
        self.split_parts = split_parts
        self.start_time = start_time
        self.statis_period = statis_period
        self.status = status
        self.tolerance_value = tolerance_value
        self.traffic_control_target_id = traffic_control_target_id
        self.value = value

    def validate(self):
        if self.split_parts:
            self.split_parts.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.event is not None:
            result['Event'] = self.event
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.item_condition_array is not None:
            result['ItemConditionArray'] = self.item_condition_array
        if self.item_condition_express is not None:
            result['ItemConditionExpress'] = self.item_condition_express
        if self.item_condition_type is not None:
            result['ItemConditionType'] = self.item_condition_type
        if self.name is not None:
            result['Name'] = self.name
        if self.new_product_regulation is not None:
            result['NewProductRegulation'] = self.new_product_regulation
        if self.recall_name is not None:
            result['RecallName'] = self.recall_name
        if self.split_parts is not None:
            result['SplitParts'] = self.split_parts.to_map()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.statis_period is not None:
            result['StatisPeriod'] = self.statis_period
        if self.status is not None:
            result['Status'] = self.status
        if self.tolerance_value is not None:
            result['ToleranceValue'] = self.tolerance_value
        if self.traffic_control_target_id is not None:
            result['TrafficControlTargetId'] = self.traffic_control_target_id
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Event') is not None:
            self.event = m.get('Event')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('ItemConditionArray') is not None:
            self.item_condition_array = m.get('ItemConditionArray')
        if m.get('ItemConditionExpress') is not None:
            self.item_condition_express = m.get('ItemConditionExpress')
        if m.get('ItemConditionType') is not None:
            self.item_condition_type = m.get('ItemConditionType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NewProductRegulation') is not None:
            self.new_product_regulation = m.get('NewProductRegulation')
        if m.get('RecallName') is not None:
            self.recall_name = m.get('RecallName')
        if m.get('SplitParts') is not None:
            temp_model = GetTrafficControlTaskResponseBodyTrafficControlTargetsSplitParts()
            self.split_parts = temp_model.from_map(m['SplitParts'])
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StatisPeriod') is not None:
            self.statis_period = m.get('StatisPeriod')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ToleranceValue') is not None:
            self.tolerance_value = m.get('ToleranceValue')
        if m.get('TrafficControlTargetId') is not None:
            self.traffic_control_target_id = m.get('TrafficControlTargetId')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetTrafficControlTaskResponseBody(TeaModel):
    def __init__(
        self,
        behavior_table_meta_id: str = None,
        control_granularity: str = None,
        control_logic: str = None,
        control_type: str = None,
        description: str = None,
        end_time: str = None,
        ever_published: bool = None,
        execution_time: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        item_condition_array: str = None,
        item_condition_express: str = None,
        item_condition_type: str = None,
        item_table_meta_id: str = None,
        name: str = None,
        prepub_status: str = None,
        product_status: str = None,
        request_id: str = None,
        scene_id: str = None,
        scene_name: str = None,
        start_time: str = None,
        statis_behavior_condition_array: str = None,
        statis_behavior_condition_express: str = None,
        statis_behavior_condition_type: str = None,
        traffic_control_targets: List[GetTrafficControlTaskResponseBodyTrafficControlTargets] = None,
        traffic_control_task_id: str = None,
        user_condition_array: str = None,
        user_condition_express: str = None,
        user_condition_type: str = None,
        user_table_meta_id: str = None,
    ):
        self.behavior_table_meta_id = behavior_table_meta_id
        self.control_granularity = control_granularity
        self.control_logic = control_logic
        self.control_type = control_type
        self.description = description
        self.end_time = end_time
        self.ever_published = ever_published
        self.execution_time = execution_time
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.item_condition_array = item_condition_array
        self.item_condition_express = item_condition_express
        self.item_condition_type = item_condition_type
        self.item_table_meta_id = item_table_meta_id
        self.name = name
        self.prepub_status = prepub_status
        self.product_status = product_status
        self.request_id = request_id
        self.scene_id = scene_id
        self.scene_name = scene_name
        self.start_time = start_time
        self.statis_behavior_condition_array = statis_behavior_condition_array
        self.statis_behavior_condition_express = statis_behavior_condition_express
        self.statis_behavior_condition_type = statis_behavior_condition_type
        self.traffic_control_targets = traffic_control_targets
        self.traffic_control_task_id = traffic_control_task_id
        self.user_condition_array = user_condition_array
        self.user_condition_express = user_condition_express
        self.user_condition_type = user_condition_type
        self.user_table_meta_id = user_table_meta_id

    def validate(self):
        if self.traffic_control_targets:
            for k in self.traffic_control_targets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.behavior_table_meta_id is not None:
            result['BehaviorTableMetaId'] = self.behavior_table_meta_id
        if self.control_granularity is not None:
            result['ControlGranularity'] = self.control_granularity
        if self.control_logic is not None:
            result['ControlLogic'] = self.control_logic
        if self.control_type is not None:
            result['ControlType'] = self.control_type
        if self.description is not None:
            result['Description'] = self.description
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.ever_published is not None:
            result['EverPublished'] = self.ever_published
        if self.execution_time is not None:
            result['ExecutionTime'] = self.execution_time
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.item_condition_array is not None:
            result['ItemConditionArray'] = self.item_condition_array
        if self.item_condition_express is not None:
            result['ItemConditionExpress'] = self.item_condition_express
        if self.item_condition_type is not None:
            result['ItemConditionType'] = self.item_condition_type
        if self.item_table_meta_id is not None:
            result['ItemTableMetaId'] = self.item_table_meta_id
        if self.name is not None:
            result['Name'] = self.name
        if self.prepub_status is not None:
            result['PrepubStatus'] = self.prepub_status
        if self.product_status is not None:
            result['ProductStatus'] = self.product_status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.scene_name is not None:
            result['SceneName'] = self.scene_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.statis_behavior_condition_array is not None:
            result['StatisBehaviorConditionArray'] = self.statis_behavior_condition_array
        if self.statis_behavior_condition_express is not None:
            result['StatisBehaviorConditionExpress'] = self.statis_behavior_condition_express
        if self.statis_behavior_condition_type is not None:
            result['StatisBehaviorConditionType'] = self.statis_behavior_condition_type
        result['TrafficControlTargets'] = []
        if self.traffic_control_targets is not None:
            for k in self.traffic_control_targets:
                result['TrafficControlTargets'].append(k.to_map() if k else None)
        if self.traffic_control_task_id is not None:
            result['TrafficControlTaskId'] = self.traffic_control_task_id
        if self.user_condition_array is not None:
            result['UserConditionArray'] = self.user_condition_array
        if self.user_condition_express is not None:
            result['UserConditionExpress'] = self.user_condition_express
        if self.user_condition_type is not None:
            result['UserConditionType'] = self.user_condition_type
        if self.user_table_meta_id is not None:
            result['UserTableMetaId'] = self.user_table_meta_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BehaviorTableMetaId') is not None:
            self.behavior_table_meta_id = m.get('BehaviorTableMetaId')
        if m.get('ControlGranularity') is not None:
            self.control_granularity = m.get('ControlGranularity')
        if m.get('ControlLogic') is not None:
            self.control_logic = m.get('ControlLogic')
        if m.get('ControlType') is not None:
            self.control_type = m.get('ControlType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EverPublished') is not None:
            self.ever_published = m.get('EverPublished')
        if m.get('ExecutionTime') is not None:
            self.execution_time = m.get('ExecutionTime')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('ItemConditionArray') is not None:
            self.item_condition_array = m.get('ItemConditionArray')
        if m.get('ItemConditionExpress') is not None:
            self.item_condition_express = m.get('ItemConditionExpress')
        if m.get('ItemConditionType') is not None:
            self.item_condition_type = m.get('ItemConditionType')
        if m.get('ItemTableMetaId') is not None:
            self.item_table_meta_id = m.get('ItemTableMetaId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PrepubStatus') is not None:
            self.prepub_status = m.get('PrepubStatus')
        if m.get('ProductStatus') is not None:
            self.product_status = m.get('ProductStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('SceneName') is not None:
            self.scene_name = m.get('SceneName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StatisBehaviorConditionArray') is not None:
            self.statis_behavior_condition_array = m.get('StatisBehaviorConditionArray')
        if m.get('StatisBehaviorConditionExpress') is not None:
            self.statis_behavior_condition_express = m.get('StatisBehaviorConditionExpress')
        if m.get('StatisBehaviorConditionType') is not None:
            self.statis_behavior_condition_type = m.get('StatisBehaviorConditionType')
        self.traffic_control_targets = []
        if m.get('TrafficControlTargets') is not None:
            for k in m.get('TrafficControlTargets'):
                temp_model = GetTrafficControlTaskResponseBodyTrafficControlTargets()
                self.traffic_control_targets.append(temp_model.from_map(k))
        if m.get('TrafficControlTaskId') is not None:
            self.traffic_control_task_id = m.get('TrafficControlTaskId')
        if m.get('UserConditionArray') is not None:
            self.user_condition_array = m.get('UserConditionArray')
        if m.get('UserConditionExpress') is not None:
            self.user_condition_express = m.get('UserConditionExpress')
        if m.get('UserConditionType') is not None:
            self.user_condition_type = m.get('UserConditionType')
        if m.get('UserTableMetaId') is not None:
            self.user_table_meta_id = m.get('UserTableMetaId')
        return self


class GetTrafficControlTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTrafficControlTaskResponseBody = None,
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
            temp_model = GetTrafficControlTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTrafficControlTaskTrafficRequest(TeaModel):
    def __init__(
        self,
        environment: str = None,
        instance_id: str = None,
    ):
        self.environment = environment
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.environment is not None:
            result['Environment'] = self.environment
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Environment') is not None:
            self.environment = m.get('Environment')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetTrafficControlTaskTrafficResponseBodyTrafficControlTaskTrafficInfoTargetTraffics(TeaModel):
    def __init__(
        self,
        data: List[Dict[str, Any]] = None,
        traffic_contorl_target_id: str = None,
    ):
        self.data = data
        self.traffic_contorl_target_id = traffic_contorl_target_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.traffic_contorl_target_id is not None:
            result['TrafficContorlTargetId'] = self.traffic_contorl_target_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('TrafficContorlTargetId') is not None:
            self.traffic_contorl_target_id = m.get('TrafficContorlTargetId')
        return self


class GetTrafficControlTaskTrafficResponseBodyTrafficControlTaskTrafficInfo(TeaModel):
    def __init__(
        self,
        target_traffics: List[GetTrafficControlTaskTrafficResponseBodyTrafficControlTaskTrafficInfoTargetTraffics] = None,
        task_traffics: Dict[str, Any] = None,
    ):
        self.target_traffics = target_traffics
        self.task_traffics = task_traffics

    def validate(self):
        if self.target_traffics:
            for k in self.target_traffics:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TargetTraffics'] = []
        if self.target_traffics is not None:
            for k in self.target_traffics:
                result['TargetTraffics'].append(k.to_map() if k else None)
        if self.task_traffics is not None:
            result['TaskTraffics'] = self.task_traffics
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.target_traffics = []
        if m.get('TargetTraffics') is not None:
            for k in m.get('TargetTraffics'):
                temp_model = GetTrafficControlTaskTrafficResponseBodyTrafficControlTaskTrafficInfoTargetTraffics()
                self.target_traffics.append(temp_model.from_map(k))
        if m.get('TaskTraffics') is not None:
            self.task_traffics = m.get('TaskTraffics')
        return self


class GetTrafficControlTaskTrafficResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        traffic_control_task_traffic_info: GetTrafficControlTaskTrafficResponseBodyTrafficControlTaskTrafficInfo = None,
    ):
        self.request_id = request_id
        self.traffic_control_task_traffic_info = traffic_control_task_traffic_info

    def validate(self):
        if self.traffic_control_task_traffic_info:
            self.traffic_control_task_traffic_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.traffic_control_task_traffic_info is not None:
            result['TrafficControlTaskTrafficInfo'] = self.traffic_control_task_traffic_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TrafficControlTaskTrafficInfo') is not None:
            temp_model = GetTrafficControlTaskTrafficResponseBodyTrafficControlTaskTrafficInfo()
            self.traffic_control_task_traffic_info = temp_model.from_map(m['TrafficControlTaskTrafficInfo'])
        return self


class GetTrafficControlTaskTrafficResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTrafficControlTaskTrafficResponseBody = None,
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
            temp_model = GetTrafficControlTaskTrafficResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListABMetricGroupsRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        realtime: bool = None,
        scene_id: str = None,
        sort_by: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        self.order = order
        self.page_number = page_number
        self.page_size = page_size
        self.realtime = realtime
        self.scene_id = scene_id
        self.sort_by = sort_by

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.order is not None:
            result['Order'] = self.order
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.realtime is not None:
            result['Realtime'] = self.realtime
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Realtime') is not None:
            self.realtime = m.get('Realtime')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        return self


class ListABMetricGroupsResponseBodyABMetricGroups(TeaModel):
    def __init__(
        self,
        abmetric_group_id: str = None,
        abmetric_ids: str = None,
        abmetric_names: str = None,
        description: str = None,
        name: str = None,
        owner: str = None,
        realtime: bool = None,
        scene_id: str = None,
    ):
        self.abmetric_group_id = abmetric_group_id
        self.abmetric_ids = abmetric_ids
        self.abmetric_names = abmetric_names
        self.description = description
        self.name = name
        self.owner = owner
        self.realtime = realtime
        self.scene_id = scene_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.abmetric_group_id is not None:
            result['ABMetricGroupId'] = self.abmetric_group_id
        if self.abmetric_ids is not None:
            result['ABMetricIds'] = self.abmetric_ids
        if self.abmetric_names is not None:
            result['ABMetricNames'] = self.abmetric_names
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.realtime is not None:
            result['Realtime'] = self.realtime
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ABMetricGroupId') is not None:
            self.abmetric_group_id = m.get('ABMetricGroupId')
        if m.get('ABMetricIds') is not None:
            self.abmetric_ids = m.get('ABMetricIds')
        if m.get('ABMetricNames') is not None:
            self.abmetric_names = m.get('ABMetricNames')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('Realtime') is not None:
            self.realtime = m.get('Realtime')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        return self


class ListABMetricGroupsResponseBody(TeaModel):
    def __init__(
        self,
        abmetric_groups: List[ListABMetricGroupsResponseBodyABMetricGroups] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.abmetric_groups = abmetric_groups
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.abmetric_groups:
            for k in self.abmetric_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ABMetricGroups'] = []
        if self.abmetric_groups is not None:
            for k in self.abmetric_groups:
                result['ABMetricGroups'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.abmetric_groups = []
        if m.get('ABMetricGroups') is not None:
            for k in m.get('ABMetricGroups'):
                temp_model = ListABMetricGroupsResponseBodyABMetricGroups()
                self.abmetric_groups.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListABMetricGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListABMetricGroupsResponseBody = None,
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
            temp_model = ListABMetricGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListABMetricsRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        name: str = None,
        page_number: int = None,
        page_size: int = None,
        realtime: bool = None,
        scene_id: str = None,
        table_meta_id: str = None,
        type: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        self.name = name
        self.page_number = page_number
        self.page_size = page_size
        self.realtime = realtime
        self.scene_id = scene_id
        self.table_meta_id = table_meta_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.realtime is not None:
            result['Realtime'] = self.realtime
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.table_meta_id is not None:
            result['TableMetaId'] = self.table_meta_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Realtime') is not None:
            self.realtime = m.get('Realtime')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('TableMetaId') is not None:
            self.table_meta_id = m.get('TableMetaId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListABMetricsResponseBodyABMetrics(TeaModel):
    def __init__(
        self,
        abmetric_id: str = None,
        definition: str = None,
        description: str = None,
        left_metric_id: str = None,
        name: str = None,
        operator: str = None,
        realtime: str = None,
        result_resource_id: str = None,
        result_table_meta_id: str = None,
        right_metric_id: str = None,
        scene_id: str = None,
        scene_name: str = None,
        statistics_cycle: int = None,
        table_meta_id: str = None,
        type: str = None,
    ):
        self.abmetric_id = abmetric_id
        self.definition = definition
        self.description = description
        self.left_metric_id = left_metric_id
        self.name = name
        self.operator = operator
        self.realtime = realtime
        self.result_resource_id = result_resource_id
        self.result_table_meta_id = result_table_meta_id
        self.right_metric_id = right_metric_id
        self.scene_id = scene_id
        self.scene_name = scene_name
        self.statistics_cycle = statistics_cycle
        self.table_meta_id = table_meta_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.abmetric_id is not None:
            result['ABMetricId'] = self.abmetric_id
        if self.definition is not None:
            result['Definition'] = self.definition
        if self.description is not None:
            result['Description'] = self.description
        if self.left_metric_id is not None:
            result['LeftMetricId'] = self.left_metric_id
        if self.name is not None:
            result['Name'] = self.name
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.realtime is not None:
            result['Realtime'] = self.realtime
        if self.result_resource_id is not None:
            result['ResultResourceId'] = self.result_resource_id
        if self.result_table_meta_id is not None:
            result['ResultTableMetaId'] = self.result_table_meta_id
        if self.right_metric_id is not None:
            result['RightMetricId'] = self.right_metric_id
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.scene_name is not None:
            result['SceneName'] = self.scene_name
        if self.statistics_cycle is not None:
            result['StatisticsCycle'] = self.statistics_cycle
        if self.table_meta_id is not None:
            result['TableMetaId'] = self.table_meta_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ABMetricId') is not None:
            self.abmetric_id = m.get('ABMetricId')
        if m.get('Definition') is not None:
            self.definition = m.get('Definition')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('LeftMetricId') is not None:
            self.left_metric_id = m.get('LeftMetricId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('Realtime') is not None:
            self.realtime = m.get('Realtime')
        if m.get('ResultResourceId') is not None:
            self.result_resource_id = m.get('ResultResourceId')
        if m.get('ResultTableMetaId') is not None:
            self.result_table_meta_id = m.get('ResultTableMetaId')
        if m.get('RightMetricId') is not None:
            self.right_metric_id = m.get('RightMetricId')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('SceneName') is not None:
            self.scene_name = m.get('SceneName')
        if m.get('StatisticsCycle') is not None:
            self.statistics_cycle = m.get('StatisticsCycle')
        if m.get('TableMetaId') is not None:
            self.table_meta_id = m.get('TableMetaId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListABMetricsResponseBody(TeaModel):
    def __init__(
        self,
        abmetrics: List[ListABMetricsResponseBodyABMetrics] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.abmetrics = abmetrics
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.abmetrics:
            for k in self.abmetrics:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ABMetrics'] = []
        if self.abmetrics is not None:
            for k in self.abmetrics:
                result['ABMetrics'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.abmetrics = []
        if m.get('ABMetrics') is not None:
            for k in m.get('ABMetrics'):
                temp_model = ListABMetricsResponseBodyABMetrics()
                self.abmetrics.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListABMetricsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListABMetricsResponseBody = None,
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
            temp_model = ListABMetricsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCalculationJobsRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        page_number: int = None,
        page_size: int = None,
        scene_id: str = None,
        status: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        self.page_number = page_number
        self.page_size = page_size
        # This parameter is required.
        self.scene_id = scene_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListCalculationJobsResponseBodyCalculationJobs(TeaModel):
    def __init__(
        self,
        abmetric_name: str = None,
        biz_date: str = None,
        calculation_job_id: str = None,
        config: str = None,
        gmt_ran_time: str = None,
        job_message: List[str] = None,
        job_source: str = None,
        status: str = None,
    ):
        self.abmetric_name = abmetric_name
        self.biz_date = biz_date
        self.calculation_job_id = calculation_job_id
        self.config = config
        self.gmt_ran_time = gmt_ran_time
        self.job_message = job_message
        self.job_source = job_source
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.abmetric_name is not None:
            result['ABMetricName'] = self.abmetric_name
        if self.biz_date is not None:
            result['BizDate'] = self.biz_date
        if self.calculation_job_id is not None:
            result['CalculationJobId'] = self.calculation_job_id
        if self.config is not None:
            result['Config'] = self.config
        if self.gmt_ran_time is not None:
            result['GmtRanTime'] = self.gmt_ran_time
        if self.job_message is not None:
            result['JobMessage'] = self.job_message
        if self.job_source is not None:
            result['JobSource'] = self.job_source
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ABMetricName') is not None:
            self.abmetric_name = m.get('ABMetricName')
        if m.get('BizDate') is not None:
            self.biz_date = m.get('BizDate')
        if m.get('CalculationJobId') is not None:
            self.calculation_job_id = m.get('CalculationJobId')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('GmtRanTime') is not None:
            self.gmt_ran_time = m.get('GmtRanTime')
        if m.get('JobMessage') is not None:
            self.job_message = m.get('JobMessage')
        if m.get('JobSource') is not None:
            self.job_source = m.get('JobSource')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListCalculationJobsResponseBody(TeaModel):
    def __init__(
        self,
        calculation_jobs: List[ListCalculationJobsResponseBodyCalculationJobs] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.calculation_jobs = calculation_jobs
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.calculation_jobs:
            for k in self.calculation_jobs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CalculationJobs'] = []
        if self.calculation_jobs is not None:
            for k in self.calculation_jobs:
                result['CalculationJobs'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.calculation_jobs = []
        if m.get('CalculationJobs') is not None:
            for k in m.get('CalculationJobs'):
                temp_model = ListCalculationJobsResponseBodyCalculationJobs()
                self.calculation_jobs.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListCalculationJobsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListCalculationJobsResponseBody = None,
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
            temp_model = ListCalculationJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCrowdUsersRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ListCrowdUsersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: int = None,
        users: List[str] = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.total_count = total_count
        self.users = users

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.users is not None:
            result['Users'] = self.users
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Users') is not None:
            self.users = m.get('Users')
        return self


class ListCrowdUsersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListCrowdUsersResponseBody = None,
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
            temp_model = ListCrowdUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCrowdsRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ListCrowdsResponseBodyCrowds(TeaModel):
    def __init__(
        self,
        crowd_id: str = None,
        description: str = None,
        gmt_create_time: str = None,
        label: str = None,
        name: str = None,
        quantity: str = None,
        source: str = None,
        users: str = None,
    ):
        self.crowd_id = crowd_id
        self.description = description
        self.gmt_create_time = gmt_create_time
        self.label = label
        self.name = name
        self.quantity = quantity
        self.source = source
        self.users = users

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.crowd_id is not None:
            result['CrowdId'] = self.crowd_id
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.label is not None:
            result['Label'] = self.label
        if self.name is not None:
            result['Name'] = self.name
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        if self.source is not None:
            result['Source'] = self.source
        if self.users is not None:
            result['Users'] = self.users
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CrowdId') is not None:
            self.crowd_id = m.get('CrowdId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Users') is not None:
            self.users = m.get('Users')
        return self


class ListCrowdsResponseBody(TeaModel):
    def __init__(
        self,
        crowds: List[ListCrowdsResponseBodyCrowds] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.crowds = crowds
        # Id of the request
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.crowds:
            for k in self.crowds:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Crowds'] = []
        if self.crowds is not None:
            for k in self.crowds:
                result['Crowds'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.crowds = []
        if m.get('Crowds') is not None:
            for k in m.get('Crowds'):
                temp_model = ListCrowdsResponseBodyCrowds()
                self.crowds.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListCrowdsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListCrowdsResponseBody = None,
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
            temp_model = ListCrowdsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListExperimentGroupsRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        layer_id: str = None,
        region_id: str = None,
        status: str = None,
        time_range_end: str = None,
        time_range_start: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        self.layer_id = layer_id
        self.region_id = region_id
        self.status = status
        self.time_range_end = time_range_end
        self.time_range_start = time_range_start

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.layer_id is not None:
            result['LayerId'] = self.layer_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        if self.time_range_end is not None:
            result['TimeRangeEnd'] = self.time_range_end
        if self.time_range_start is not None:
            result['TimeRangeStart'] = self.time_range_start
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('LayerId') is not None:
            self.layer_id = m.get('LayerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TimeRangeEnd') is not None:
            self.time_range_end = m.get('TimeRangeEnd')
        if m.get('TimeRangeStart') is not None:
            self.time_range_start = m.get('TimeRangeStart')
        return self


class ListExperimentGroupsResponseBodyExperimentGroups(TeaModel):
    def __init__(
        self,
        config: str = None,
        crowd_id: str = None,
        crowd_target_type: str = None,
        debug_crowd_id: str = None,
        debug_users: str = None,
        description: str = None,
        distribution_time_duration: int = None,
        distribution_type: str = None,
        experiment_group_id: str = None,
        filter: str = None,
        holding_buckets: str = None,
        laboratory_id: str = None,
        layer_id: str = None,
        name: str = None,
        need_aa: bool = None,
        owner: str = None,
        random_flow: int = None,
        reserved_buckets: str = None,
        scene_id: str = None,
        status: str = None,
    ):
        self.config = config
        self.crowd_id = crowd_id
        self.crowd_target_type = crowd_target_type
        self.debug_crowd_id = debug_crowd_id
        self.debug_users = debug_users
        self.description = description
        self.distribution_time_duration = distribution_time_duration
        self.distribution_type = distribution_type
        self.experiment_group_id = experiment_group_id
        self.filter = filter
        self.holding_buckets = holding_buckets
        self.laboratory_id = laboratory_id
        self.layer_id = layer_id
        self.name = name
        self.need_aa = need_aa
        self.owner = owner
        self.random_flow = random_flow
        self.reserved_buckets = reserved_buckets
        self.scene_id = scene_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.crowd_id is not None:
            result['CrowdId'] = self.crowd_id
        if self.crowd_target_type is not None:
            result['CrowdTargetType'] = self.crowd_target_type
        if self.debug_crowd_id is not None:
            result['DebugCrowdId'] = self.debug_crowd_id
        if self.debug_users is not None:
            result['DebugUsers'] = self.debug_users
        if self.description is not None:
            result['Description'] = self.description
        if self.distribution_time_duration is not None:
            result['DistributionTimeDuration'] = self.distribution_time_duration
        if self.distribution_type is not None:
            result['DistributionType'] = self.distribution_type
        if self.experiment_group_id is not None:
            result['ExperimentGroupId'] = self.experiment_group_id
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.holding_buckets is not None:
            result['HoldingBuckets'] = self.holding_buckets
        if self.laboratory_id is not None:
            result['LaboratoryId'] = self.laboratory_id
        if self.layer_id is not None:
            result['LayerId'] = self.layer_id
        if self.name is not None:
            result['Name'] = self.name
        if self.need_aa is not None:
            result['NeedAA'] = self.need_aa
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.random_flow is not None:
            result['RandomFlow'] = self.random_flow
        if self.reserved_buckets is not None:
            result['ReservedBuckets'] = self.reserved_buckets
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('CrowdId') is not None:
            self.crowd_id = m.get('CrowdId')
        if m.get('CrowdTargetType') is not None:
            self.crowd_target_type = m.get('CrowdTargetType')
        if m.get('DebugCrowdId') is not None:
            self.debug_crowd_id = m.get('DebugCrowdId')
        if m.get('DebugUsers') is not None:
            self.debug_users = m.get('DebugUsers')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DistributionTimeDuration') is not None:
            self.distribution_time_duration = m.get('DistributionTimeDuration')
        if m.get('DistributionType') is not None:
            self.distribution_type = m.get('DistributionType')
        if m.get('ExperimentGroupId') is not None:
            self.experiment_group_id = m.get('ExperimentGroupId')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('HoldingBuckets') is not None:
            self.holding_buckets = m.get('HoldingBuckets')
        if m.get('LaboratoryId') is not None:
            self.laboratory_id = m.get('LaboratoryId')
        if m.get('LayerId') is not None:
            self.layer_id = m.get('LayerId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NeedAA') is not None:
            self.need_aa = m.get('NeedAA')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('RandomFlow') is not None:
            self.random_flow = m.get('RandomFlow')
        if m.get('ReservedBuckets') is not None:
            self.reserved_buckets = m.get('ReservedBuckets')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListExperimentGroupsResponseBody(TeaModel):
    def __init__(
        self,
        experiment_groups: List[ListExperimentGroupsResponseBodyExperimentGroups] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.experiment_groups = experiment_groups
        # Id of the request
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.experiment_groups:
            for k in self.experiment_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ExperimentGroups'] = []
        if self.experiment_groups is not None:
            for k in self.experiment_groups:
                result['ExperimentGroups'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.experiment_groups = []
        if m.get('ExperimentGroups') is not None:
            for k in m.get('ExperimentGroups'):
                temp_model = ListExperimentGroupsResponseBodyExperimentGroups()
                self.experiment_groups.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListExperimentGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListExperimentGroupsResponseBody = None,
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
            temp_model = ListExperimentGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListExperimentsRequest(TeaModel):
    def __init__(
        self,
        experiment_group_id: str = None,
        instance_id: str = None,
        query: str = None,
        status: str = None,
    ):
        self.experiment_group_id = experiment_group_id
        # This parameter is required.
        self.instance_id = instance_id
        self.query = query
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.experiment_group_id is not None:
            result['ExperimentGroupId'] = self.experiment_group_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.query is not None:
            result['Query'] = self.query
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExperimentGroupId') is not None:
            self.experiment_group_id = m.get('ExperimentGroupId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListExperimentsResponseBodyExperiments(TeaModel):
    def __init__(
        self,
        alias_experiment_id: str = None,
        buckets: str = None,
        config: str = None,
        debug_crowd_id: str = None,
        debug_users: str = None,
        description: str = None,
        experiment_group_id: str = None,
        experiment_id: str = None,
        flow_percent: int = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        laboratory_id: str = None,
        layer_id: str = None,
        name: str = None,
        scene_id: str = None,
        status: str = None,
        type: str = None,
    ):
        self.alias_experiment_id = alias_experiment_id
        self.buckets = buckets
        self.config = config
        self.debug_crowd_id = debug_crowd_id
        self.debug_users = debug_users
        self.description = description
        self.experiment_group_id = experiment_group_id
        self.experiment_id = experiment_id
        self.flow_percent = flow_percent
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.laboratory_id = laboratory_id
        self.layer_id = layer_id
        self.name = name
        self.scene_id = scene_id
        self.status = status
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias_experiment_id is not None:
            result['AliasExperimentId'] = self.alias_experiment_id
        if self.buckets is not None:
            result['Buckets'] = self.buckets
        if self.config is not None:
            result['Config'] = self.config
        if self.debug_crowd_id is not None:
            result['DebugCrowdId'] = self.debug_crowd_id
        if self.debug_users is not None:
            result['DebugUsers'] = self.debug_users
        if self.description is not None:
            result['Description'] = self.description
        if self.experiment_group_id is not None:
            result['ExperimentGroupId'] = self.experiment_group_id
        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id
        if self.flow_percent is not None:
            result['FlowPercent'] = self.flow_percent
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.laboratory_id is not None:
            result['LaboratoryId'] = self.laboratory_id
        if self.layer_id is not None:
            result['LayerId'] = self.layer_id
        if self.name is not None:
            result['Name'] = self.name
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliasExperimentId') is not None:
            self.alias_experiment_id = m.get('AliasExperimentId')
        if m.get('Buckets') is not None:
            self.buckets = m.get('Buckets')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('DebugCrowdId') is not None:
            self.debug_crowd_id = m.get('DebugCrowdId')
        if m.get('DebugUsers') is not None:
            self.debug_users = m.get('DebugUsers')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExperimentGroupId') is not None:
            self.experiment_group_id = m.get('ExperimentGroupId')
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')
        if m.get('FlowPercent') is not None:
            self.flow_percent = m.get('FlowPercent')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('LaboratoryId') is not None:
            self.laboratory_id = m.get('LaboratoryId')
        if m.get('LayerId') is not None:
            self.layer_id = m.get('LayerId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListExperimentsResponseBody(TeaModel):
    def __init__(
        self,
        experiments: List[ListExperimentsResponseBodyExperiments] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.experiments = experiments
        # Id of the request
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.experiments:
            for k in self.experiments:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Experiments'] = []
        if self.experiments is not None:
            for k in self.experiments:
                result['Experiments'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.experiments = []
        if m.get('Experiments') is not None:
            for k in m.get('Experiments'):
                temp_model = ListExperimentsResponseBodyExperiments()
                self.experiments.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListExperimentsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListExperimentsResponseBody = None,
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
            temp_model = ListExperimentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFeatureConsistencyCheckJobConfigsRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        order: str = None,
        page_number: str = None,
        page_size: str = None,
        sort_by: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        self.order = order
        self.page_number = page_number
        self.page_size = page_size
        self.sort_by = sort_by

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.order is not None:
            result['Order'] = self.order
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        return self


class ListFeatureConsistencyCheckJobConfigsResponseBodyFeatureConsistencyCheckConfigs(TeaModel):
    def __init__(
        self,
        compare_feature: bool = None,
        eas_service_name: str = None,
        easy_rec_package_path: str = None,
        easy_rec_version: str = None,
        feature_consistency_check_job_config_id: str = None,
        feature_display_exclude: str = None,
        feature_landing_resource_id: str = None,
        feature_landing_resource_uri: str = None,
        feature_priority: str = None,
        feature_store_item_id: str = None,
        feature_store_model_id: str = None,
        feature_store_project_id: str = None,
        feature_store_project_name: str = None,
        feature_store_seq_feature_view: str = None,
        feature_store_user_id: str = None,
        fg_jar_version: str = None,
        fg_json_file_name: str = None,
        generate_zip: bool = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        item_id_field: str = None,
        item_table: str = None,
        item_table_partition_field: str = None,
        item_table_partition_field_format: str = None,
        latest_job_gmt_sampling_end_time: str = None,
        latest_job_gmt_sampling_start_time: str = None,
        latest_job_id: str = None,
        name: str = None,
        oss_bucket: str = None,
        oss_resource_id: str = None,
        sample_rate: str = None,
        scene_id: str = None,
        scene_name: str = None,
        service_id: str = None,
        service_name: str = None,
        status: str = None,
        use_feature_store: str = None,
        user_id_field: str = None,
        user_table: str = None,
        user_table_partition_field: str = None,
        user_table_partition_field_format: str = None,
        workflow_name: str = None,
    ):
        self.compare_feature = compare_feature
        self.eas_service_name = eas_service_name
        self.easy_rec_package_path = easy_rec_package_path
        self.easy_rec_version = easy_rec_version
        self.feature_consistency_check_job_config_id = feature_consistency_check_job_config_id
        self.feature_display_exclude = feature_display_exclude
        self.feature_landing_resource_id = feature_landing_resource_id
        self.feature_landing_resource_uri = feature_landing_resource_uri
        self.feature_priority = feature_priority
        self.feature_store_item_id = feature_store_item_id
        self.feature_store_model_id = feature_store_model_id
        self.feature_store_project_id = feature_store_project_id
        self.feature_store_project_name = feature_store_project_name
        self.feature_store_seq_feature_view = feature_store_seq_feature_view
        self.feature_store_user_id = feature_store_user_id
        self.fg_jar_version = fg_jar_version
        self.fg_json_file_name = fg_json_file_name
        self.generate_zip = generate_zip
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.item_id_field = item_id_field
        self.item_table = item_table
        self.item_table_partition_field = item_table_partition_field
        self.item_table_partition_field_format = item_table_partition_field_format
        self.latest_job_gmt_sampling_end_time = latest_job_gmt_sampling_end_time
        self.latest_job_gmt_sampling_start_time = latest_job_gmt_sampling_start_time
        self.latest_job_id = latest_job_id
        self.name = name
        self.oss_bucket = oss_bucket
        self.oss_resource_id = oss_resource_id
        self.sample_rate = sample_rate
        self.scene_id = scene_id
        self.scene_name = scene_name
        self.service_id = service_id
        self.service_name = service_name
        self.status = status
        self.use_feature_store = use_feature_store
        self.user_id_field = user_id_field
        self.user_table = user_table
        self.user_table_partition_field = user_table_partition_field
        self.user_table_partition_field_format = user_table_partition_field_format
        self.workflow_name = workflow_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compare_feature is not None:
            result['CompareFeature'] = self.compare_feature
        if self.eas_service_name is not None:
            result['EasServiceName'] = self.eas_service_name
        if self.easy_rec_package_path is not None:
            result['EasyRecPackagePath'] = self.easy_rec_package_path
        if self.easy_rec_version is not None:
            result['EasyRecVersion'] = self.easy_rec_version
        if self.feature_consistency_check_job_config_id is not None:
            result['FeatureConsistencyCheckJobConfigId'] = self.feature_consistency_check_job_config_id
        if self.feature_display_exclude is not None:
            result['FeatureDisplayExclude'] = self.feature_display_exclude
        if self.feature_landing_resource_id is not None:
            result['FeatureLandingResourceId'] = self.feature_landing_resource_id
        if self.feature_landing_resource_uri is not None:
            result['FeatureLandingResourceUri'] = self.feature_landing_resource_uri
        if self.feature_priority is not None:
            result['FeaturePriority'] = self.feature_priority
        if self.feature_store_item_id is not None:
            result['FeatureStoreItemId'] = self.feature_store_item_id
        if self.feature_store_model_id is not None:
            result['FeatureStoreModelId'] = self.feature_store_model_id
        if self.feature_store_project_id is not None:
            result['FeatureStoreProjectId'] = self.feature_store_project_id
        if self.feature_store_project_name is not None:
            result['FeatureStoreProjectName'] = self.feature_store_project_name
        if self.feature_store_seq_feature_view is not None:
            result['FeatureStoreSeqFeatureView'] = self.feature_store_seq_feature_view
        if self.feature_store_user_id is not None:
            result['FeatureStoreUserId'] = self.feature_store_user_id
        if self.fg_jar_version is not None:
            result['FgJarVersion'] = self.fg_jar_version
        if self.fg_json_file_name is not None:
            result['FgJsonFileName'] = self.fg_json_file_name
        if self.generate_zip is not None:
            result['GenerateZip'] = self.generate_zip
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.item_id_field is not None:
            result['ItemIdField'] = self.item_id_field
        if self.item_table is not None:
            result['ItemTable'] = self.item_table
        if self.item_table_partition_field is not None:
            result['ItemTablePartitionField'] = self.item_table_partition_field
        if self.item_table_partition_field_format is not None:
            result['ItemTablePartitionFieldFormat'] = self.item_table_partition_field_format
        if self.latest_job_gmt_sampling_end_time is not None:
            result['LatestJobGmtSamplingEndTime'] = self.latest_job_gmt_sampling_end_time
        if self.latest_job_gmt_sampling_start_time is not None:
            result['LatestJobGmtSamplingStartTime'] = self.latest_job_gmt_sampling_start_time
        if self.latest_job_id is not None:
            result['LatestJobId'] = self.latest_job_id
        if self.name is not None:
            result['Name'] = self.name
        if self.oss_bucket is not None:
            result['OssBucket'] = self.oss_bucket
        if self.oss_resource_id is not None:
            result['OssResourceId'] = self.oss_resource_id
        if self.sample_rate is not None:
            result['SampleRate'] = self.sample_rate
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.scene_name is not None:
            result['SceneName'] = self.scene_name
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.status is not None:
            result['Status'] = self.status
        if self.use_feature_store is not None:
            result['UseFeatureStore'] = self.use_feature_store
        if self.user_id_field is not None:
            result['UserIdField'] = self.user_id_field
        if self.user_table is not None:
            result['UserTable'] = self.user_table
        if self.user_table_partition_field is not None:
            result['UserTablePartitionField'] = self.user_table_partition_field
        if self.user_table_partition_field_format is not None:
            result['UserTablePartitionFieldFormat'] = self.user_table_partition_field_format
        if self.workflow_name is not None:
            result['WorkflowName'] = self.workflow_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompareFeature') is not None:
            self.compare_feature = m.get('CompareFeature')
        if m.get('EasServiceName') is not None:
            self.eas_service_name = m.get('EasServiceName')
        if m.get('EasyRecPackagePath') is not None:
            self.easy_rec_package_path = m.get('EasyRecPackagePath')
        if m.get('EasyRecVersion') is not None:
            self.easy_rec_version = m.get('EasyRecVersion')
        if m.get('FeatureConsistencyCheckJobConfigId') is not None:
            self.feature_consistency_check_job_config_id = m.get('FeatureConsistencyCheckJobConfigId')
        if m.get('FeatureDisplayExclude') is not None:
            self.feature_display_exclude = m.get('FeatureDisplayExclude')
        if m.get('FeatureLandingResourceId') is not None:
            self.feature_landing_resource_id = m.get('FeatureLandingResourceId')
        if m.get('FeatureLandingResourceUri') is not None:
            self.feature_landing_resource_uri = m.get('FeatureLandingResourceUri')
        if m.get('FeaturePriority') is not None:
            self.feature_priority = m.get('FeaturePriority')
        if m.get('FeatureStoreItemId') is not None:
            self.feature_store_item_id = m.get('FeatureStoreItemId')
        if m.get('FeatureStoreModelId') is not None:
            self.feature_store_model_id = m.get('FeatureStoreModelId')
        if m.get('FeatureStoreProjectId') is not None:
            self.feature_store_project_id = m.get('FeatureStoreProjectId')
        if m.get('FeatureStoreProjectName') is not None:
            self.feature_store_project_name = m.get('FeatureStoreProjectName')
        if m.get('FeatureStoreSeqFeatureView') is not None:
            self.feature_store_seq_feature_view = m.get('FeatureStoreSeqFeatureView')
        if m.get('FeatureStoreUserId') is not None:
            self.feature_store_user_id = m.get('FeatureStoreUserId')
        if m.get('FgJarVersion') is not None:
            self.fg_jar_version = m.get('FgJarVersion')
        if m.get('FgJsonFileName') is not None:
            self.fg_json_file_name = m.get('FgJsonFileName')
        if m.get('GenerateZip') is not None:
            self.generate_zip = m.get('GenerateZip')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('ItemIdField') is not None:
            self.item_id_field = m.get('ItemIdField')
        if m.get('ItemTable') is not None:
            self.item_table = m.get('ItemTable')
        if m.get('ItemTablePartitionField') is not None:
            self.item_table_partition_field = m.get('ItemTablePartitionField')
        if m.get('ItemTablePartitionFieldFormat') is not None:
            self.item_table_partition_field_format = m.get('ItemTablePartitionFieldFormat')
        if m.get('LatestJobGmtSamplingEndTime') is not None:
            self.latest_job_gmt_sampling_end_time = m.get('LatestJobGmtSamplingEndTime')
        if m.get('LatestJobGmtSamplingStartTime') is not None:
            self.latest_job_gmt_sampling_start_time = m.get('LatestJobGmtSamplingStartTime')
        if m.get('LatestJobId') is not None:
            self.latest_job_id = m.get('LatestJobId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OssBucket') is not None:
            self.oss_bucket = m.get('OssBucket')
        if m.get('OssResourceId') is not None:
            self.oss_resource_id = m.get('OssResourceId')
        if m.get('SampleRate') is not None:
            self.sample_rate = m.get('SampleRate')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('SceneName') is not None:
            self.scene_name = m.get('SceneName')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UseFeatureStore') is not None:
            self.use_feature_store = m.get('UseFeatureStore')
        if m.get('UserIdField') is not None:
            self.user_id_field = m.get('UserIdField')
        if m.get('UserTable') is not None:
            self.user_table = m.get('UserTable')
        if m.get('UserTablePartitionField') is not None:
            self.user_table_partition_field = m.get('UserTablePartitionField')
        if m.get('UserTablePartitionFieldFormat') is not None:
            self.user_table_partition_field_format = m.get('UserTablePartitionFieldFormat')
        if m.get('WorkflowName') is not None:
            self.workflow_name = m.get('WorkflowName')
        return self


class ListFeatureConsistencyCheckJobConfigsResponseBody(TeaModel):
    def __init__(
        self,
        feature_consistency_check_configs: List[ListFeatureConsistencyCheckJobConfigsResponseBodyFeatureConsistencyCheckConfigs] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.feature_consistency_check_configs = feature_consistency_check_configs
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.feature_consistency_check_configs:
            for k in self.feature_consistency_check_configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FeatureConsistencyCheckConfigs'] = []
        if self.feature_consistency_check_configs is not None:
            for k in self.feature_consistency_check_configs:
                result['FeatureConsistencyCheckConfigs'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.feature_consistency_check_configs = []
        if m.get('FeatureConsistencyCheckConfigs') is not None:
            for k in m.get('FeatureConsistencyCheckConfigs'):
                temp_model = ListFeatureConsistencyCheckJobConfigsResponseBodyFeatureConsistencyCheckConfigs()
                self.feature_consistency_check_configs.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListFeatureConsistencyCheckJobConfigsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListFeatureConsistencyCheckJobConfigsResponseBody = None,
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
            temp_model = ListFeatureConsistencyCheckJobConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFeatureConsistencyCheckJobFeatureReportsRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        log_item_id: str = None,
        log_request_id: str = None,
        log_user_id: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.log_item_id = log_item_id
        # This parameter is required.
        self.log_request_id = log_request_id
        # This parameter is required.
        self.log_user_id = log_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.log_item_id is not None:
            result['LogItemId'] = self.log_item_id
        if self.log_request_id is not None:
            result['LogRequestId'] = self.log_request_id
        if self.log_user_id is not None:
            result['LogUserId'] = self.log_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('LogItemId') is not None:
            self.log_item_id = m.get('LogItemId')
        if m.get('LogRequestId') is not None:
            self.log_request_id = m.get('LogRequestId')
        if m.get('LogUserId') is not None:
            self.log_user_id = m.get('LogUserId')
        return self


class ListFeatureConsistencyCheckJobFeatureReportsResponseBodyReportsOfFeatureDiff(TeaModel):
    def __init__(
        self,
        feature_name: str = None,
        log_item_id: str = None,
        log_request_id: str = None,
        log_user_id: str = None,
        offline_value: str = None,
        online_value: str = None,
    ):
        self.feature_name = feature_name
        self.log_item_id = log_item_id
        self.log_request_id = log_request_id
        self.log_user_id = log_user_id
        self.offline_value = offline_value
        self.online_value = online_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.feature_name is not None:
            result['FeatureName'] = self.feature_name
        if self.log_item_id is not None:
            result['LogItemId'] = self.log_item_id
        if self.log_request_id is not None:
            result['LogRequestId'] = self.log_request_id
        if self.log_user_id is not None:
            result['LogUserId'] = self.log_user_id
        if self.offline_value is not None:
            result['OfflineValue'] = self.offline_value
        if self.online_value is not None:
            result['OnlineValue'] = self.online_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FeatureName') is not None:
            self.feature_name = m.get('FeatureName')
        if m.get('LogItemId') is not None:
            self.log_item_id = m.get('LogItemId')
        if m.get('LogRequestId') is not None:
            self.log_request_id = m.get('LogRequestId')
        if m.get('LogUserId') is not None:
            self.log_user_id = m.get('LogUserId')
        if m.get('OfflineValue') is not None:
            self.offline_value = m.get('OfflineValue')
        if m.get('OnlineValue') is not None:
            self.online_value = m.get('OnlineValue')
        return self


class ListFeatureConsistencyCheckJobFeatureReportsResponseBody(TeaModel):
    def __init__(
        self,
        data_path: str = None,
        oss_path: str = None,
        reports_of_feature_diff: List[ListFeatureConsistencyCheckJobFeatureReportsResponseBodyReportsOfFeatureDiff] = None,
        request_id: str = None,
    ):
        self.data_path = data_path
        self.oss_path = oss_path
        self.reports_of_feature_diff = reports_of_feature_diff
        self.request_id = request_id

    def validate(self):
        if self.reports_of_feature_diff:
            for k in self.reports_of_feature_diff:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_path is not None:
            result['DataPath'] = self.data_path
        if self.oss_path is not None:
            result['OssPath'] = self.oss_path
        result['ReportsOfFeatureDiff'] = []
        if self.reports_of_feature_diff is not None:
            for k in self.reports_of_feature_diff:
                result['ReportsOfFeatureDiff'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataPath') is not None:
            self.data_path = m.get('DataPath')
        if m.get('OssPath') is not None:
            self.oss_path = m.get('OssPath')
        self.reports_of_feature_diff = []
        if m.get('ReportsOfFeatureDiff') is not None:
            for k in m.get('ReportsOfFeatureDiff'):
                temp_model = ListFeatureConsistencyCheckJobFeatureReportsResponseBodyReportsOfFeatureDiff()
                self.reports_of_feature_diff.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListFeatureConsistencyCheckJobFeatureReportsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListFeatureConsistencyCheckJobFeatureReportsResponseBody = None,
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
            temp_model = ListFeatureConsistencyCheckJobFeatureReportsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFeatureConsistencyCheckJobScoreReportsRequest(TeaModel):
    def __init__(
        self,
        exclude_request_ids: List[str] = None,
        instance_id: str = None,
    ):
        self.exclude_request_ids = exclude_request_ids
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exclude_request_ids is not None:
            result['ExcludeRequestIds'] = self.exclude_request_ids
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExcludeRequestIds') is not None:
            self.exclude_request_ids = m.get('ExcludeRequestIds')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ListFeatureConsistencyCheckJobScoreReportsShrinkRequest(TeaModel):
    def __init__(
        self,
        exclude_request_ids_shrink: str = None,
        instance_id: str = None,
    ):
        self.exclude_request_ids_shrink = exclude_request_ids_shrink
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exclude_request_ids_shrink is not None:
            result['ExcludeRequestIds'] = self.exclude_request_ids_shrink
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExcludeRequestIds') is not None:
            self.exclude_request_ids_shrink = m.get('ExcludeRequestIds')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ListFeatureConsistencyCheckJobScoreReportsResponseBodyReportsOfScoreDiff(TeaModel):
    def __init__(
        self,
        log_item_id: str = None,
        log_request_id: str = None,
        log_user_id: str = None,
        score_diff: str = None,
        score_diff_detail: str = None,
    ):
        self.log_item_id = log_item_id
        self.log_request_id = log_request_id
        self.log_user_id = log_user_id
        self.score_diff = score_diff
        self.score_diff_detail = score_diff_detail

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_item_id is not None:
            result['LogItemId'] = self.log_item_id
        if self.log_request_id is not None:
            result['LogRequestId'] = self.log_request_id
        if self.log_user_id is not None:
            result['LogUserId'] = self.log_user_id
        if self.score_diff is not None:
            result['ScoreDiff'] = self.score_diff
        if self.score_diff_detail is not None:
            result['ScoreDiffDetail'] = self.score_diff_detail
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogItemId') is not None:
            self.log_item_id = m.get('LogItemId')
        if m.get('LogRequestId') is not None:
            self.log_request_id = m.get('LogRequestId')
        if m.get('LogUserId') is not None:
            self.log_user_id = m.get('LogUserId')
        if m.get('ScoreDiff') is not None:
            self.score_diff = m.get('ScoreDiff')
        if m.get('ScoreDiffDetail') is not None:
            self.score_diff_detail = m.get('ScoreDiffDetail')
        return self


class ListFeatureConsistencyCheckJobScoreReportsResponseBody(TeaModel):
    def __init__(
        self,
        data_path: str = None,
        oss_path: str = None,
        reports_of_score_diff: List[ListFeatureConsistencyCheckJobScoreReportsResponseBodyReportsOfScoreDiff] = None,
        request_id: str = None,
    ):
        self.data_path = data_path
        self.oss_path = oss_path
        self.reports_of_score_diff = reports_of_score_diff
        self.request_id = request_id

    def validate(self):
        if self.reports_of_score_diff:
            for k in self.reports_of_score_diff:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_path is not None:
            result['DataPath'] = self.data_path
        if self.oss_path is not None:
            result['OssPath'] = self.oss_path
        result['ReportsOfScoreDiff'] = []
        if self.reports_of_score_diff is not None:
            for k in self.reports_of_score_diff:
                result['ReportsOfScoreDiff'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataPath') is not None:
            self.data_path = m.get('DataPath')
        if m.get('OssPath') is not None:
            self.oss_path = m.get('OssPath')
        self.reports_of_score_diff = []
        if m.get('ReportsOfScoreDiff') is not None:
            for k in m.get('ReportsOfScoreDiff'):
                temp_model = ListFeatureConsistencyCheckJobScoreReportsResponseBodyReportsOfScoreDiff()
                self.reports_of_score_diff.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListFeatureConsistencyCheckJobScoreReportsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListFeatureConsistencyCheckJobScoreReportsResponseBody = None,
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
            temp_model = ListFeatureConsistencyCheckJobScoreReportsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFeatureConsistencyCheckJobsRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        order: str = None,
        page_number: str = None,
        page_size: str = None,
        sort_by: str = None,
        status: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        self.order = order
        self.page_number = page_number
        self.page_size = page_size
        self.sort_by = sort_by
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.order is not None:
            result['Order'] = self.order
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListFeatureConsistencyCheckJobsResponseBodyFeatureConsistencyCheckJobs(TeaModel):
    def __init__(
        self,
        config: str = None,
        feature_consistency_check_job_config_id: str = None,
        feature_consistency_check_job_config_name: str = None,
        feature_consistency_check_job_id: str = None,
        gmt_end_time: str = None,
        gmt_start_time: str = None,
        logs: List[str] = None,
        status: str = None,
    ):
        self.config = config
        self.feature_consistency_check_job_config_id = feature_consistency_check_job_config_id
        self.feature_consistency_check_job_config_name = feature_consistency_check_job_config_name
        self.feature_consistency_check_job_id = feature_consistency_check_job_id
        self.gmt_end_time = gmt_end_time
        self.gmt_start_time = gmt_start_time
        self.logs = logs
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.feature_consistency_check_job_config_id is not None:
            result['FeatureConsistencyCheckJobConfigId'] = self.feature_consistency_check_job_config_id
        if self.feature_consistency_check_job_config_name is not None:
            result['FeatureConsistencyCheckJobConfigName'] = self.feature_consistency_check_job_config_name
        if self.feature_consistency_check_job_id is not None:
            result['FeatureConsistencyCheckJobId'] = self.feature_consistency_check_job_id
        if self.gmt_end_time is not None:
            result['GmtEndTime'] = self.gmt_end_time
        if self.gmt_start_time is not None:
            result['GmtStartTime'] = self.gmt_start_time
        if self.logs is not None:
            result['Logs'] = self.logs
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('FeatureConsistencyCheckJobConfigId') is not None:
            self.feature_consistency_check_job_config_id = m.get('FeatureConsistencyCheckJobConfigId')
        if m.get('FeatureConsistencyCheckJobConfigName') is not None:
            self.feature_consistency_check_job_config_name = m.get('FeatureConsistencyCheckJobConfigName')
        if m.get('FeatureConsistencyCheckJobId') is not None:
            self.feature_consistency_check_job_id = m.get('FeatureConsistencyCheckJobId')
        if m.get('GmtEndTime') is not None:
            self.gmt_end_time = m.get('GmtEndTime')
        if m.get('GmtStartTime') is not None:
            self.gmt_start_time = m.get('GmtStartTime')
        if m.get('Logs') is not None:
            self.logs = m.get('Logs')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListFeatureConsistencyCheckJobsResponseBody(TeaModel):
    def __init__(
        self,
        feature_consistency_check_jobs: List[ListFeatureConsistencyCheckJobsResponseBodyFeatureConsistencyCheckJobs] = None,
        request_id: str = None,
        total_count: str = None,
    ):
        self.feature_consistency_check_jobs = feature_consistency_check_jobs
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.feature_consistency_check_jobs:
            for k in self.feature_consistency_check_jobs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FeatureConsistencyCheckJobs'] = []
        if self.feature_consistency_check_jobs is not None:
            for k in self.feature_consistency_check_jobs:
                result['FeatureConsistencyCheckJobs'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.feature_consistency_check_jobs = []
        if m.get('FeatureConsistencyCheckJobs') is not None:
            for k in m.get('FeatureConsistencyCheckJobs'):
                temp_model = ListFeatureConsistencyCheckJobsResponseBodyFeatureConsistencyCheckJobs()
                self.feature_consistency_check_jobs.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListFeatureConsistencyCheckJobsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListFeatureConsistencyCheckJobsResponseBody = None,
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
            temp_model = ListFeatureConsistencyCheckJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstanceResourcesRequest(TeaModel):
    def __init__(
        self,
        category: str = None,
        group: str = None,
        type: str = None,
    ):
        self.category = category
        self.group = group
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.group is not None:
            result['Group'] = self.group
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListInstanceResourcesResponseBodyResources(TeaModel):
    def __init__(
        self,
        category: str = None,
        config: str = None,
        gmt_create_at: str = None,
        gmt_modified_at: str = None,
        group: str = None,
        resource_id: str = None,
        type: str = None,
        uri: str = None,
    ):
        self.category = category
        self.config = config
        self.gmt_create_at = gmt_create_at
        self.gmt_modified_at = gmt_modified_at
        self.group = group
        self.resource_id = resource_id
        self.type = type
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.config is not None:
            result['Config'] = self.config
        if self.gmt_create_at is not None:
            result['GmtCreateAt'] = self.gmt_create_at
        if self.gmt_modified_at is not None:
            result['GmtModifiedAt'] = self.gmt_modified_at
        if self.group is not None:
            result['Group'] = self.group
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.type is not None:
            result['Type'] = self.type
        if self.uri is not None:
            result['Uri'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('GmtCreateAt') is not None:
            self.gmt_create_at = m.get('GmtCreateAt')
        if m.get('GmtModifiedAt') is not None:
            self.gmt_modified_at = m.get('GmtModifiedAt')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        return self


class ListInstanceResourcesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resources: List[ListInstanceResourcesResponseBodyResources] = None,
        total_count: int = None,
    ):
        self.request_id = request_id
        self.resources = resources
        self.total_count = total_count

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Resources'] = []
        if self.resources is not None:
            for k in self.resources:
                result['Resources'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.resources = []
        if m.get('Resources') is not None:
            for k in m.get('Resources'):
                temp_model = ListInstanceResourcesResponseBodyResources()
                self.resources.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListInstanceResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListInstanceResourcesResponseBody = None,
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
            temp_model = ListInstanceResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstancesRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        sort_by: str = None,
        type: str = None,
    ):
        self.instance_id = instance_id
        self.order = order
        self.page_number = page_number
        self.page_size = page_size
        self.sort_by = sort_by
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.order is not None:
            result['Order'] = self.order
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListInstancesResponseBodyInstancesConfigDataManagements(TeaModel):
    def __init__(
        self,
        component_code: str = None,
        meta: Dict[str, Any] = None,
        type: str = None,
    ):
        self.component_code = component_code
        self.meta = meta
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_code is not None:
            result['ComponentCode'] = self.component_code
        if self.meta is not None:
            result['Meta'] = self.meta
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComponentCode') is not None:
            self.component_code = m.get('ComponentCode')
        if m.get('Meta') is not None:
            self.meta = m.get('Meta')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListInstancesResponseBodyInstancesConfigEngines(TeaModel):
    def __init__(
        self,
        component_code: str = None,
        meta: Dict[str, Any] = None,
        type: str = None,
    ):
        self.component_code = component_code
        self.meta = meta
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_code is not None:
            result['ComponentCode'] = self.component_code
        if self.meta is not None:
            result['Meta'] = self.meta
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComponentCode') is not None:
            self.component_code = m.get('ComponentCode')
        if m.get('Meta') is not None:
            self.meta = m.get('Meta')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListInstancesResponseBodyInstancesConfigMonitors(TeaModel):
    def __init__(
        self,
        component_code: str = None,
        meta: Dict[str, Any] = None,
        type: str = None,
    ):
        self.component_code = component_code
        self.meta = meta
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_code is not None:
            result['ComponentCode'] = self.component_code
        if self.meta is not None:
            result['Meta'] = self.meta
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComponentCode') is not None:
            self.component_code = m.get('ComponentCode')
        if m.get('Meta') is not None:
            self.meta = m.get('Meta')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListInstancesResponseBodyInstancesConfig(TeaModel):
    def __init__(
        self,
        data_managements: List[ListInstancesResponseBodyInstancesConfigDataManagements] = None,
        engines: List[ListInstancesResponseBodyInstancesConfigEngines] = None,
        monitors: List[ListInstancesResponseBodyInstancesConfigMonitors] = None,
    ):
        self.data_managements = data_managements
        self.engines = engines
        self.monitors = monitors

    def validate(self):
        if self.data_managements:
            for k in self.data_managements:
                if k:
                    k.validate()
        if self.engines:
            for k in self.engines:
                if k:
                    k.validate()
        if self.monitors:
            for k in self.monitors:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataManagements'] = []
        if self.data_managements is not None:
            for k in self.data_managements:
                result['DataManagements'].append(k.to_map() if k else None)
        result['Engines'] = []
        if self.engines is not None:
            for k in self.engines:
                result['Engines'].append(k.to_map() if k else None)
        result['Monitors'] = []
        if self.monitors is not None:
            for k in self.monitors:
                result['Monitors'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_managements = []
        if m.get('DataManagements') is not None:
            for k in m.get('DataManagements'):
                temp_model = ListInstancesResponseBodyInstancesConfigDataManagements()
                self.data_managements.append(temp_model.from_map(k))
        self.engines = []
        if m.get('Engines') is not None:
            for k in m.get('Engines'):
                temp_model = ListInstancesResponseBodyInstancesConfigEngines()
                self.engines.append(temp_model.from_map(k))
        self.monitors = []
        if m.get('Monitors') is not None:
            for k in m.get('Monitors'):
                temp_model = ListInstancesResponseBodyInstancesConfigMonitors()
                self.monitors.append(temp_model.from_map(k))
        return self


class ListInstancesResponseBodyInstances(TeaModel):
    def __init__(
        self,
        charge_type: str = None,
        commodity_code: str = None,
        config: ListInstancesResponseBodyInstancesConfig = None,
        expired_time: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        instance_id: str = None,
        region_id: str = None,
        status: str = None,
        type: str = None,
    ):
        self.charge_type = charge_type
        self.commodity_code = commodity_code
        self.config = config
        self.expired_time = expired_time
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.instance_id = instance_id
        self.region_id = region_id
        self.status = status
        self.type = type

    def validate(self):
        if self.config:
            self.config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.config is not None:
            result['Config'] = self.config.to_map()
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('Config') is not None:
            temp_model = ListInstancesResponseBodyInstancesConfig()
            self.config = temp_model.from_map(m['Config'])
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListInstancesResponseBody(TeaModel):
    def __init__(
        self,
        instances: List[ListInstancesResponseBodyInstances] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.instances = instances
        self.request_id = request_id
        self.total_count = total_count

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
        result['Instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['Instances'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instances = []
        if m.get('Instances') is not None:
            for k in m.get('Instances'):
                temp_model = ListInstancesResponseBodyInstances()
                self.instances.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
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


class ListLaboratoriesRequest(TeaModel):
    def __init__(
        self,
        environment: str = None,
        instance_id: str = None,
        scene_id: str = None,
        status: str = None,
    ):
        self.environment = environment
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.scene_id = scene_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.environment is not None:
            result['Environment'] = self.environment
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Environment') is not None:
            self.environment = m.get('Environment')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListLaboratoriesResponseBodyLaboratories(TeaModel):
    def __init__(
        self,
        bucket_count: int = None,
        bucket_type: str = None,
        buckets: str = None,
        crowd_id: str = None,
        debug_crowd_id: str = None,
        debug_users: str = None,
        description: str = None,
        environment: str = None,
        filter: str = None,
        laboratory_id: str = None,
        name: str = None,
        scene_id: str = None,
        status: str = None,
        type: str = None,
    ):
        self.bucket_count = bucket_count
        self.bucket_type = bucket_type
        self.buckets = buckets
        self.crowd_id = crowd_id
        self.debug_crowd_id = debug_crowd_id
        self.debug_users = debug_users
        self.description = description
        self.environment = environment
        self.filter = filter
        self.laboratory_id = laboratory_id
        self.name = name
        self.scene_id = scene_id
        self.status = status
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_count is not None:
            result['BucketCount'] = self.bucket_count
        if self.bucket_type is not None:
            result['BucketType'] = self.bucket_type
        if self.buckets is not None:
            result['Buckets'] = self.buckets
        if self.crowd_id is not None:
            result['CrowdId'] = self.crowd_id
        if self.debug_crowd_id is not None:
            result['DebugCrowdId'] = self.debug_crowd_id
        if self.debug_users is not None:
            result['DebugUsers'] = self.debug_users
        if self.description is not None:
            result['Description'] = self.description
        if self.environment is not None:
            result['Environment'] = self.environment
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.laboratory_id is not None:
            result['LaboratoryId'] = self.laboratory_id
        if self.name is not None:
            result['Name'] = self.name
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketCount') is not None:
            self.bucket_count = m.get('BucketCount')
        if m.get('BucketType') is not None:
            self.bucket_type = m.get('BucketType')
        if m.get('Buckets') is not None:
            self.buckets = m.get('Buckets')
        if m.get('CrowdId') is not None:
            self.crowd_id = m.get('CrowdId')
        if m.get('DebugCrowdId') is not None:
            self.debug_crowd_id = m.get('DebugCrowdId')
        if m.get('DebugUsers') is not None:
            self.debug_users = m.get('DebugUsers')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Environment') is not None:
            self.environment = m.get('Environment')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('LaboratoryId') is not None:
            self.laboratory_id = m.get('LaboratoryId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListLaboratoriesResponseBody(TeaModel):
    def __init__(
        self,
        laboratories: List[ListLaboratoriesResponseBodyLaboratories] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.laboratories = laboratories
        # Id of the request
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.laboratories:
            for k in self.laboratories:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Laboratories'] = []
        if self.laboratories is not None:
            for k in self.laboratories:
                result['Laboratories'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.laboratories = []
        if m.get('Laboratories') is not None:
            for k in m.get('Laboratories'):
                temp_model = ListLaboratoriesResponseBodyLaboratories()
                self.laboratories.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListLaboratoriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListLaboratoriesResponseBody = None,
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
            temp_model = ListLaboratoriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListLayersRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        laboratory_id: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.laboratory_id = laboratory_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.laboratory_id is not None:
            result['LaboratoryId'] = self.laboratory_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('LaboratoryId') is not None:
            self.laboratory_id = m.get('LaboratoryId')
        return self


class ListLayersResponseBodyLayers(TeaModel):
    def __init__(
        self,
        description: str = None,
        gmt_create_time: str = None,
        laboratory_id: str = None,
        layer_id: str = None,
        name: str = None,
        residual_flow: int = None,
        scene_id: str = None,
    ):
        self.description = description
        self.gmt_create_time = gmt_create_time
        self.laboratory_id = laboratory_id
        self.layer_id = layer_id
        self.name = name
        self.residual_flow = residual_flow
        self.scene_id = scene_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.laboratory_id is not None:
            result['LaboratoryId'] = self.laboratory_id
        if self.layer_id is not None:
            result['LayerId'] = self.layer_id
        if self.name is not None:
            result['Name'] = self.name
        if self.residual_flow is not None:
            result['ResidualFlow'] = self.residual_flow
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('LaboratoryId') is not None:
            self.laboratory_id = m.get('LaboratoryId')
        if m.get('LayerId') is not None:
            self.layer_id = m.get('LayerId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ResidualFlow') is not None:
            self.residual_flow = m.get('ResidualFlow')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        return self


class ListLayersResponseBody(TeaModel):
    def __init__(
        self,
        layers: List[ListLayersResponseBodyLayers] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.layers = layers
        # Id of the request
        self.request_id = request_id
        self.total_count = total_count

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
        result['Layers'] = []
        if self.layers is not None:
            for k in self.layers:
                result['Layers'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.layers = []
        if m.get('Layers') is not None:
            for k in m.get('Layers'):
                temp_model = ListLayersResponseBodyLayers()
                self.layers.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
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


class ListParamsRequest(TeaModel):
    def __init__(
        self,
        environment: str = None,
        instance_id: str = None,
        name: str = None,
        page_number: int = None,
        page_size: int = None,
        scene_id: str = None,
    ):
        self.environment = environment
        # This parameter is required.
        self.instance_id = instance_id
        self.name = name
        self.page_number = page_number
        self.page_size = page_size
        # This parameter is required.
        self.scene_id = scene_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.environment is not None:
            result['Environment'] = self.environment
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Environment') is not None:
            self.environment = m.get('Environment')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        return self


class ListParamsResponseBodyParams(TeaModel):
    def __init__(
        self,
        environment: str = None,
        gmt_modified_time: str = None,
        name: str = None,
        param_id: str = None,
        value: str = None,
    ):
        self.environment = environment
        self.gmt_modified_time = gmt_modified_time
        self.name = name
        self.param_id = param_id
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.environment is not None:
            result['Environment'] = self.environment
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.name is not None:
            result['Name'] = self.name
        if self.param_id is not None:
            result['ParamId'] = self.param_id
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Environment') is not None:
            self.environment = m.get('Environment')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParamId') is not None:
            self.param_id = m.get('ParamId')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListParamsResponseBody(TeaModel):
    def __init__(
        self,
        params: List[ListParamsResponseBodyParams] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.params = params
        # Id of the request
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.params:
            for k in self.params:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Params'] = []
        if self.params is not None:
            for k in self.params:
                result['Params'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.params = []
        if m.get('Params') is not None:
            for k in m.get('Params'):
                temp_model = ListParamsResponseBodyParams()
                self.params.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListParamsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListParamsResponseBody = None,
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
            temp_model = ListParamsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListResourceRulesRequest(TeaModel):
    def __init__(
        self,
        all: bool = None,
        instance_id: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        resource_rule_id: str = None,
        resource_rule_name: str = None,
        sort_by: str = None,
    ):
        self.all = all
        # This parameter is required.
        self.instance_id = instance_id
        self.order = order
        self.page_number = page_number
        self.page_size = page_size
        self.resource_rule_id = resource_rule_id
        self.resource_rule_name = resource_rule_name
        self.sort_by = sort_by

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['All'] = self.all
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.order is not None:
            result['Order'] = self.order
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_rule_id is not None:
            result['ResourceRuleId'] = self.resource_rule_id
        if self.resource_rule_name is not None:
            result['ResourceRuleName'] = self.resource_rule_name
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceRuleId') is not None:
            self.resource_rule_id = m.get('ResourceRuleId')
        if m.get('ResourceRuleName') is not None:
            self.resource_rule_name = m.get('ResourceRuleName')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        return self


class ListResourceRulesResponseBodyResourceRulesRuleItems(TeaModel):
    def __init__(
        self,
        description: str = None,
        max_value: str = None,
        min_value: str = None,
        name: str = None,
        value: str = None,
    ):
        self.description = description
        self.max_value = max_value
        self.min_value = min_value
        self.name = name
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.max_value is not None:
            result['MaxValue'] = self.max_value
        if self.min_value is not None:
            result['MinValue'] = self.min_value
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('MaxValue') is not None:
            self.max_value = m.get('MaxValue')
        if m.get('MinValue') is not None:
            self.min_value = m.get('MinValue')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListResourceRulesResponseBodyResourceRules(TeaModel):
    def __init__(
        self,
        description: str = None,
        metric_operation_type: str = None,
        metric_pull_info: str = None,
        metric_pull_period: str = None,
        name: str = None,
        resource_rule_id: str = None,
        rule_computing_definition: str = None,
        rule_items: List[ListResourceRulesResponseBodyResourceRulesRuleItems] = None,
    ):
        self.description = description
        self.metric_operation_type = metric_operation_type
        self.metric_pull_info = metric_pull_info
        self.metric_pull_period = metric_pull_period
        self.name = name
        self.resource_rule_id = resource_rule_id
        self.rule_computing_definition = rule_computing_definition
        self.rule_items = rule_items

    def validate(self):
        if self.rule_items:
            for k in self.rule_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.metric_operation_type is not None:
            result['MetricOperationType'] = self.metric_operation_type
        if self.metric_pull_info is not None:
            result['MetricPullInfo'] = self.metric_pull_info
        if self.metric_pull_period is not None:
            result['MetricPullPeriod'] = self.metric_pull_period
        if self.name is not None:
            result['Name'] = self.name
        if self.resource_rule_id is not None:
            result['ResourceRuleId'] = self.resource_rule_id
        if self.rule_computing_definition is not None:
            result['RuleComputingDefinition'] = self.rule_computing_definition
        result['RuleItems'] = []
        if self.rule_items is not None:
            for k in self.rule_items:
                result['RuleItems'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('MetricOperationType') is not None:
            self.metric_operation_type = m.get('MetricOperationType')
        if m.get('MetricPullInfo') is not None:
            self.metric_pull_info = m.get('MetricPullInfo')
        if m.get('MetricPullPeriod') is not None:
            self.metric_pull_period = m.get('MetricPullPeriod')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ResourceRuleId') is not None:
            self.resource_rule_id = m.get('ResourceRuleId')
        if m.get('RuleComputingDefinition') is not None:
            self.rule_computing_definition = m.get('RuleComputingDefinition')
        self.rule_items = []
        if m.get('RuleItems') is not None:
            for k in m.get('RuleItems'):
                temp_model = ListResourceRulesResponseBodyResourceRulesRuleItems()
                self.rule_items.append(temp_model.from_map(k))
        return self


class ListResourceRulesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resource_rules: List[ListResourceRulesResponseBodyResourceRules] = None,
        total_count: int = None,
    ):
        self.request_id = request_id
        self.resource_rules = resource_rules
        self.total_count = total_count

    def validate(self):
        if self.resource_rules:
            for k in self.resource_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ResourceRules'] = []
        if self.resource_rules is not None:
            for k in self.resource_rules:
                result['ResourceRules'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.resource_rules = []
        if m.get('ResourceRules') is not None:
            for k in m.get('ResourceRules'):
                temp_model = ListResourceRulesResponseBodyResourceRules()
                self.resource_rules.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListResourceRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListResourceRulesResponseBody = None,
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
            temp_model = ListResourceRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListScenesRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        name: str = None,
    ):
        self.instance_id = instance_id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListScenesResponseBodyScenesFlows(TeaModel):
    def __init__(
        self,
        flow_code: str = None,
        flow_name: str = None,
    ):
        self.flow_code = flow_code
        self.flow_name = flow_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_code is not None:
            result['FlowCode'] = self.flow_code
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowCode') is not None:
            self.flow_code = m.get('FlowCode')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        return self


class ListScenesResponseBodyScenes(TeaModel):
    def __init__(
        self,
        description: str = None,
        flows: List[ListScenesResponseBodyScenesFlows] = None,
        name: str = None,
        scene_id: str = None,
    ):
        self.description = description
        self.flows = flows
        self.name = name
        self.scene_id = scene_id

    def validate(self):
        if self.flows:
            for k in self.flows:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        result['Flows'] = []
        if self.flows is not None:
            for k in self.flows:
                result['Flows'].append(k.to_map() if k else None)
        if self.name is not None:
            result['Name'] = self.name
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        self.flows = []
        if m.get('Flows') is not None:
            for k in m.get('Flows'):
                temp_model = ListScenesResponseBodyScenesFlows()
                self.flows.append(temp_model.from_map(k))
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        return self


class ListScenesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        scenes: List[ListScenesResponseBodyScenes] = None,
        total_count: int = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.scenes = scenes
        self.total_count = total_count

    def validate(self):
        if self.scenes:
            for k in self.scenes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Scenes'] = []
        if self.scenes is not None:
            for k in self.scenes:
                result['Scenes'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.scenes = []
        if m.get('Scenes') is not None:
            for k in m.get('Scenes'):
                temp_model = ListScenesResponseBodyScenes()
                self.scenes.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListScenesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListScenesResponseBody = None,
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
            temp_model = ListScenesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSubCrowdsRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ListSubCrowdsResponseBodySubCrowds(TeaModel):
    def __init__(
        self,
        gmt_create_time: str = None,
        quantity: int = None,
        source: str = None,
        sub_crowd_id: str = None,
        users: str = None,
    ):
        self.gmt_create_time = gmt_create_time
        self.quantity = quantity
        self.source = source
        self.sub_crowd_id = sub_crowd_id
        self.users = users

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        if self.source is not None:
            result['Source'] = self.source
        if self.sub_crowd_id is not None:
            result['SubCrowdId'] = self.sub_crowd_id
        if self.users is not None:
            result['Users'] = self.users
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SubCrowdId') is not None:
            self.sub_crowd_id = m.get('SubCrowdId')
        if m.get('Users') is not None:
            self.users = m.get('Users')
        return self


class ListSubCrowdsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        sub_crowds: List[ListSubCrowdsResponseBodySubCrowds] = None,
        total_count: int = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.sub_crowds = sub_crowds
        self.total_count = total_count

    def validate(self):
        if self.sub_crowds:
            for k in self.sub_crowds:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SubCrowds'] = []
        if self.sub_crowds is not None:
            for k in self.sub_crowds:
                result['SubCrowds'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.sub_crowds = []
        if m.get('SubCrowds') is not None:
            for k in m.get('SubCrowds'):
                temp_model = ListSubCrowdsResponseBodySubCrowds()
                self.sub_crowds.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListSubCrowdsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListSubCrowdsResponseBody = None,
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
            temp_model = ListSubCrowdsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTableMetasRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        module: str = None,
        name: str = None,
        page_number: int = None,
        page_size: int = None,
        type: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.module = module
        self.name = name
        self.page_number = page_number
        self.page_size = page_size
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.module is not None:
            result['Module'] = self.module
        if self.name is not None:
            result['Name'] = self.name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Module') is not None:
            self.module = m.get('Module')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListTableMetasResponseBodyTableMetasFields(TeaModel):
    def __init__(
        self,
        is_dimension_field: bool = None,
        meaning: str = None,
        name: str = None,
        type: str = None,
    ):
        self.is_dimension_field = is_dimension_field
        self.meaning = meaning
        self.name = name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_dimension_field is not None:
            result['IsDimensionField'] = self.is_dimension_field
        if self.meaning is not None:
            result['Meaning'] = self.meaning
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsDimensionField') is not None:
            self.is_dimension_field = m.get('IsDimensionField')
        if m.get('Meaning') is not None:
            self.meaning = m.get('Meaning')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListTableMetasResponseBodyTableMetas(TeaModel):
    def __init__(
        self,
        can_delete: bool = None,
        config: str = None,
        description: str = None,
        fields: List[ListTableMetasResponseBodyTableMetasFields] = None,
        gmt_create_time: str = None,
        gmt_imported_time: str = None,
        gmt_modified_time: str = None,
        module: str = None,
        name: str = None,
        resource_id: str = None,
        table_meta_id: str = None,
        table_name: str = None,
        type: str = None,
        url: str = None,
    ):
        self.can_delete = can_delete
        self.config = config
        self.description = description
        self.fields = fields
        self.gmt_create_time = gmt_create_time
        self.gmt_imported_time = gmt_imported_time
        self.gmt_modified_time = gmt_modified_time
        self.module = module
        self.name = name
        self.resource_id = resource_id
        self.table_meta_id = table_meta_id
        self.table_name = table_name
        self.type = type
        self.url = url

    def validate(self):
        if self.fields:
            for k in self.fields:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_delete is not None:
            result['CanDelete'] = self.can_delete
        if self.config is not None:
            result['Config'] = self.config
        if self.description is not None:
            result['Description'] = self.description
        result['Fields'] = []
        if self.fields is not None:
            for k in self.fields:
                result['Fields'].append(k.to_map() if k else None)
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_imported_time is not None:
            result['GmtImportedTime'] = self.gmt_imported_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.module is not None:
            result['Module'] = self.module
        if self.name is not None:
            result['Name'] = self.name
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.table_meta_id is not None:
            result['TableMetaId'] = self.table_meta_id
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.type is not None:
            result['Type'] = self.type
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanDelete') is not None:
            self.can_delete = m.get('CanDelete')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        self.fields = []
        if m.get('Fields') is not None:
            for k in m.get('Fields'):
                temp_model = ListTableMetasResponseBodyTableMetasFields()
                self.fields.append(temp_model.from_map(k))
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtImportedTime') is not None:
            self.gmt_imported_time = m.get('GmtImportedTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('Module') is not None:
            self.module = m.get('Module')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('TableMetaId') is not None:
            self.table_meta_id = m.get('TableMetaId')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class ListTableMetasResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        table_metas: List[ListTableMetasResponseBodyTableMetas] = None,
        total_count: int = None,
    ):
        self.request_id = request_id
        self.table_metas = table_metas
        self.total_count = total_count

    def validate(self):
        if self.table_metas:
            for k in self.table_metas:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TableMetas'] = []
        if self.table_metas is not None:
            for k in self.table_metas:
                result['TableMetas'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.table_metas = []
        if m.get('TableMetas') is not None:
            for k in m.get('TableMetas'):
                temp_model = ListTableMetasResponseBodyTableMetas()
                self.table_metas.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListTableMetasResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTableMetasResponseBody = None,
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
            temp_model = ListTableMetasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTrafficControlTargetTrafficHistoryRequest(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        environment: str = None,
        experiment_group_id: str = None,
        experiment_id: str = None,
        instance_id: str = None,
        item_id: str = None,
        start_time: str = None,
        threshold: str = None,
    ):
        self.end_time = end_time
        self.environment = environment
        self.experiment_group_id = experiment_group_id
        self.experiment_id = experiment_id
        self.instance_id = instance_id
        self.item_id = item_id
        self.start_time = start_time
        self.threshold = threshold

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.environment is not None:
            result['Environment'] = self.environment
        if self.experiment_group_id is not None:
            result['ExperimentGroupId'] = self.experiment_group_id
        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Environment') is not None:
            self.environment = m.get('Environment')
        if m.get('ExperimentGroupId') is not None:
            self.experiment_group_id = m.get('ExperimentGroupId')
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        return self


class ListTrafficControlTargetTrafficHistoryResponseBodyTrafficControlTaskTrafficHistories(TeaModel):
    def __init__(
        self,
        experiment_id: str = None,
        item_id: str = None,
        record_time: str = None,
        traffic_control_target_aim_traffic: str = None,
        traffic_control_target_traffic: str = None,
        traffic_control_task_traffic: str = None,
    ):
        self.experiment_id = experiment_id
        self.item_id = item_id
        self.record_time = record_time
        self.traffic_control_target_aim_traffic = traffic_control_target_aim_traffic
        self.traffic_control_target_traffic = traffic_control_target_traffic
        self.traffic_control_task_traffic = traffic_control_task_traffic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.record_time is not None:
            result['RecordTime'] = self.record_time
        if self.traffic_control_target_aim_traffic is not None:
            result['TrafficControlTargetAimTraffic'] = self.traffic_control_target_aim_traffic
        if self.traffic_control_target_traffic is not None:
            result['TrafficControlTargetTraffic'] = self.traffic_control_target_traffic
        if self.traffic_control_task_traffic is not None:
            result['TrafficControlTaskTraffic'] = self.traffic_control_task_traffic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('RecordTime') is not None:
            self.record_time = m.get('RecordTime')
        if m.get('TrafficControlTargetAimTraffic') is not None:
            self.traffic_control_target_aim_traffic = m.get('TrafficControlTargetAimTraffic')
        if m.get('TrafficControlTargetTraffic') is not None:
            self.traffic_control_target_traffic = m.get('TrafficControlTargetTraffic')
        if m.get('TrafficControlTaskTraffic') is not None:
            self.traffic_control_task_traffic = m.get('TrafficControlTaskTraffic')
        return self


class ListTrafficControlTargetTrafficHistoryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: str = None,
        traffic_control_task_traffic_histories: List[ListTrafficControlTargetTrafficHistoryResponseBodyTrafficControlTaskTrafficHistories] = None,
    ):
        self.request_id = request_id
        self.total_count = total_count
        self.traffic_control_task_traffic_histories = traffic_control_task_traffic_histories

    def validate(self):
        if self.traffic_control_task_traffic_histories:
            for k in self.traffic_control_task_traffic_histories:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['TrafficControlTaskTrafficHistories'] = []
        if self.traffic_control_task_traffic_histories is not None:
            for k in self.traffic_control_task_traffic_histories:
                result['TrafficControlTaskTrafficHistories'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.traffic_control_task_traffic_histories = []
        if m.get('TrafficControlTaskTrafficHistories') is not None:
            for k in m.get('TrafficControlTaskTrafficHistories'):
                temp_model = ListTrafficControlTargetTrafficHistoryResponseBodyTrafficControlTaskTrafficHistories()
                self.traffic_control_task_traffic_histories.append(temp_model.from_map(k))
        return self


class ListTrafficControlTargetTrafficHistoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTrafficControlTargetTrafficHistoryResponseBody = None,
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
            temp_model = ListTrafficControlTargetTrafficHistoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTrafficControlTasksRequest(TeaModel):
    def __init__(
        self,
        all: bool = None,
        control_target_filter: str = None,
        environment: str = None,
        instance_id: str = None,
        name: str = None,
        order: str = None,
        page_number: str = None,
        page_size: str = None,
        scene_id: str = None,
        sort_by: str = None,
        status: str = None,
        traffic_control_task_id: str = None,
        version: str = None,
    ):
        self.all = all
        self.control_target_filter = control_target_filter
        self.environment = environment
        self.instance_id = instance_id
        self.name = name
        self.order = order
        self.page_number = page_number
        self.page_size = page_size
        self.scene_id = scene_id
        self.sort_by = sort_by
        self.status = status
        self.traffic_control_task_id = traffic_control_task_id
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['All'] = self.all
        if self.control_target_filter is not None:
            result['ControlTargetFilter'] = self.control_target_filter
        if self.environment is not None:
            result['Environment'] = self.environment
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        if self.order is not None:
            result['Order'] = self.order
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.status is not None:
            result['Status'] = self.status
        if self.traffic_control_task_id is not None:
            result['TrafficControlTaskId'] = self.traffic_control_task_id
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('ControlTargetFilter') is not None:
            self.control_target_filter = m.get('ControlTargetFilter')
        if m.get('Environment') is not None:
            self.environment = m.get('Environment')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TrafficControlTaskId') is not None:
            self.traffic_control_task_id = m.get('TrafficControlTaskId')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class ListTrafficControlTasksResponseBodyTrafficControlTasksTrafficControlTargetsSplitParts(TeaModel):
    def __init__(
        self,
        set_values: List[int] = None,
        time_points: List[int] = None,
    ):
        self.set_values = set_values
        self.time_points = time_points

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.set_values is not None:
            result['SetValues'] = self.set_values
        if self.time_points is not None:
            result['TimePoints'] = self.time_points
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SetValues') is not None:
            self.set_values = m.get('SetValues')
        if m.get('TimePoints') is not None:
            self.time_points = m.get('TimePoints')
        return self


class ListTrafficControlTasksResponseBodyTrafficControlTasksTrafficControlTargets(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        event: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        item_condition_array: str = None,
        item_condition_express: str = None,
        item_condition_type: str = None,
        name: str = None,
        new_product_regulation: bool = None,
        recall_name: str = None,
        split_parts: ListTrafficControlTasksResponseBodyTrafficControlTasksTrafficControlTargetsSplitParts = None,
        start_time: str = None,
        statis_period: str = None,
        status: str = None,
        tolerance_value: int = None,
        traffic_control_target_id: str = None,
        value: float = None,
    ):
        self.end_time = end_time
        self.event = event
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.item_condition_array = item_condition_array
        self.item_condition_express = item_condition_express
        self.item_condition_type = item_condition_type
        self.name = name
        self.new_product_regulation = new_product_regulation
        self.recall_name = recall_name
        self.split_parts = split_parts
        self.start_time = start_time
        self.statis_period = statis_period
        self.status = status
        self.tolerance_value = tolerance_value
        self.traffic_control_target_id = traffic_control_target_id
        self.value = value

    def validate(self):
        if self.split_parts:
            self.split_parts.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.event is not None:
            result['Event'] = self.event
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.item_condition_array is not None:
            result['ItemConditionArray'] = self.item_condition_array
        if self.item_condition_express is not None:
            result['ItemConditionExpress'] = self.item_condition_express
        if self.item_condition_type is not None:
            result['ItemConditionType'] = self.item_condition_type
        if self.name is not None:
            result['Name'] = self.name
        if self.new_product_regulation is not None:
            result['NewProductRegulation'] = self.new_product_regulation
        if self.recall_name is not None:
            result['RecallName'] = self.recall_name
        if self.split_parts is not None:
            result['SplitParts'] = self.split_parts.to_map()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.statis_period is not None:
            result['StatisPeriod'] = self.statis_period
        if self.status is not None:
            result['Status'] = self.status
        if self.tolerance_value is not None:
            result['ToleranceValue'] = self.tolerance_value
        if self.traffic_control_target_id is not None:
            result['TrafficControlTargetId'] = self.traffic_control_target_id
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Event') is not None:
            self.event = m.get('Event')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('ItemConditionArray') is not None:
            self.item_condition_array = m.get('ItemConditionArray')
        if m.get('ItemConditionExpress') is not None:
            self.item_condition_express = m.get('ItemConditionExpress')
        if m.get('ItemConditionType') is not None:
            self.item_condition_type = m.get('ItemConditionType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NewProductRegulation') is not None:
            self.new_product_regulation = m.get('NewProductRegulation')
        if m.get('RecallName') is not None:
            self.recall_name = m.get('RecallName')
        if m.get('SplitParts') is not None:
            temp_model = ListTrafficControlTasksResponseBodyTrafficControlTasksTrafficControlTargetsSplitParts()
            self.split_parts = temp_model.from_map(m['SplitParts'])
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StatisPeriod') is not None:
            self.statis_period = m.get('StatisPeriod')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ToleranceValue') is not None:
            self.tolerance_value = m.get('ToleranceValue')
        if m.get('TrafficControlTargetId') is not None:
            self.traffic_control_target_id = m.get('TrafficControlTargetId')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListTrafficControlTasksResponseBodyTrafficControlTasks(TeaModel):
    def __init__(
        self,
        behavior_table_meta_id: str = None,
        control_granularity: str = None,
        control_logic: str = None,
        control_type: str = None,
        description: str = None,
        end_time: str = None,
        ever_published: bool = None,
        execution_time: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        item_condition_array: str = None,
        item_condition_express: str = None,
        item_condition_type: str = None,
        item_table_meta_id: str = None,
        name: str = None,
        prepub_status: str = None,
        product_status: str = None,
        scene_id: str = None,
        scene_name: str = None,
        start_time: str = None,
        statis_bahavior_condition_express: str = None,
        statis_behavior_condition_array: str = None,
        statis_behavior_condition_type: str = None,
        traffic_control_targets: List[ListTrafficControlTasksResponseBodyTrafficControlTasksTrafficControlTargets] = None,
        traffic_control_task_id: str = None,
        user_condition_array: str = None,
        user_condition_express: str = None,
        user_condition_type: str = None,
        user_table_meta_id: str = None,
    ):
        self.behavior_table_meta_id = behavior_table_meta_id
        self.control_granularity = control_granularity
        self.control_logic = control_logic
        self.control_type = control_type
        self.description = description
        self.end_time = end_time
        self.ever_published = ever_published
        self.execution_time = execution_time
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.item_condition_array = item_condition_array
        self.item_condition_express = item_condition_express
        self.item_condition_type = item_condition_type
        self.item_table_meta_id = item_table_meta_id
        self.name = name
        self.prepub_status = prepub_status
        self.product_status = product_status
        self.scene_id = scene_id
        self.scene_name = scene_name
        self.start_time = start_time
        self.statis_bahavior_condition_express = statis_bahavior_condition_express
        self.statis_behavior_condition_array = statis_behavior_condition_array
        self.statis_behavior_condition_type = statis_behavior_condition_type
        self.traffic_control_targets = traffic_control_targets
        self.traffic_control_task_id = traffic_control_task_id
        self.user_condition_array = user_condition_array
        self.user_condition_express = user_condition_express
        self.user_condition_type = user_condition_type
        self.user_table_meta_id = user_table_meta_id

    def validate(self):
        if self.traffic_control_targets:
            for k in self.traffic_control_targets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.behavior_table_meta_id is not None:
            result['BehaviorTableMetaId'] = self.behavior_table_meta_id
        if self.control_granularity is not None:
            result['ControlGranularity'] = self.control_granularity
        if self.control_logic is not None:
            result['ControlLogic'] = self.control_logic
        if self.control_type is not None:
            result['ControlType'] = self.control_type
        if self.description is not None:
            result['Description'] = self.description
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.ever_published is not None:
            result['EverPublished'] = self.ever_published
        if self.execution_time is not None:
            result['ExecutionTime'] = self.execution_time
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.item_condition_array is not None:
            result['ItemConditionArray'] = self.item_condition_array
        if self.item_condition_express is not None:
            result['ItemConditionExpress'] = self.item_condition_express
        if self.item_condition_type is not None:
            result['ItemConditionType'] = self.item_condition_type
        if self.item_table_meta_id is not None:
            result['ItemTableMetaId'] = self.item_table_meta_id
        if self.name is not None:
            result['Name'] = self.name
        if self.prepub_status is not None:
            result['PrepubStatus'] = self.prepub_status
        if self.product_status is not None:
            result['ProductStatus'] = self.product_status
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.scene_name is not None:
            result['SceneName'] = self.scene_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.statis_bahavior_condition_express is not None:
            result['StatisBahaviorConditionExpress'] = self.statis_bahavior_condition_express
        if self.statis_behavior_condition_array is not None:
            result['StatisBehaviorConditionArray'] = self.statis_behavior_condition_array
        if self.statis_behavior_condition_type is not None:
            result['StatisBehaviorConditionType'] = self.statis_behavior_condition_type
        result['TrafficControlTargets'] = []
        if self.traffic_control_targets is not None:
            for k in self.traffic_control_targets:
                result['TrafficControlTargets'].append(k.to_map() if k else None)
        if self.traffic_control_task_id is not None:
            result['TrafficControlTaskId'] = self.traffic_control_task_id
        if self.user_condition_array is not None:
            result['UserConditionArray'] = self.user_condition_array
        if self.user_condition_express is not None:
            result['UserConditionExpress'] = self.user_condition_express
        if self.user_condition_type is not None:
            result['UserConditionType'] = self.user_condition_type
        if self.user_table_meta_id is not None:
            result['UserTableMetaId'] = self.user_table_meta_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BehaviorTableMetaId') is not None:
            self.behavior_table_meta_id = m.get('BehaviorTableMetaId')
        if m.get('ControlGranularity') is not None:
            self.control_granularity = m.get('ControlGranularity')
        if m.get('ControlLogic') is not None:
            self.control_logic = m.get('ControlLogic')
        if m.get('ControlType') is not None:
            self.control_type = m.get('ControlType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EverPublished') is not None:
            self.ever_published = m.get('EverPublished')
        if m.get('ExecutionTime') is not None:
            self.execution_time = m.get('ExecutionTime')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('ItemConditionArray') is not None:
            self.item_condition_array = m.get('ItemConditionArray')
        if m.get('ItemConditionExpress') is not None:
            self.item_condition_express = m.get('ItemConditionExpress')
        if m.get('ItemConditionType') is not None:
            self.item_condition_type = m.get('ItemConditionType')
        if m.get('ItemTableMetaId') is not None:
            self.item_table_meta_id = m.get('ItemTableMetaId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PrepubStatus') is not None:
            self.prepub_status = m.get('PrepubStatus')
        if m.get('ProductStatus') is not None:
            self.product_status = m.get('ProductStatus')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('SceneName') is not None:
            self.scene_name = m.get('SceneName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StatisBahaviorConditionExpress') is not None:
            self.statis_bahavior_condition_express = m.get('StatisBahaviorConditionExpress')
        if m.get('StatisBehaviorConditionArray') is not None:
            self.statis_behavior_condition_array = m.get('StatisBehaviorConditionArray')
        if m.get('StatisBehaviorConditionType') is not None:
            self.statis_behavior_condition_type = m.get('StatisBehaviorConditionType')
        self.traffic_control_targets = []
        if m.get('TrafficControlTargets') is not None:
            for k in m.get('TrafficControlTargets'):
                temp_model = ListTrafficControlTasksResponseBodyTrafficControlTasksTrafficControlTargets()
                self.traffic_control_targets.append(temp_model.from_map(k))
        if m.get('TrafficControlTaskId') is not None:
            self.traffic_control_task_id = m.get('TrafficControlTaskId')
        if m.get('UserConditionArray') is not None:
            self.user_condition_array = m.get('UserConditionArray')
        if m.get('UserConditionExpress') is not None:
            self.user_condition_express = m.get('UserConditionExpress')
        if m.get('UserConditionType') is not None:
            self.user_condition_type = m.get('UserConditionType')
        if m.get('UserTableMetaId') is not None:
            self.user_table_meta_id = m.get('UserTableMetaId')
        return self


class ListTrafficControlTasksResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: str = None,
        traffic_control_tasks: List[ListTrafficControlTasksResponseBodyTrafficControlTasks] = None,
    ):
        self.request_id = request_id
        self.total_count = total_count
        self.traffic_control_tasks = traffic_control_tasks

    def validate(self):
        if self.traffic_control_tasks:
            for k in self.traffic_control_tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['TrafficControlTasks'] = []
        if self.traffic_control_tasks is not None:
            for k in self.traffic_control_tasks:
                result['TrafficControlTasks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.traffic_control_tasks = []
        if m.get('TrafficControlTasks') is not None:
            for k in m.get('TrafficControlTasks'):
                temp_model = ListTrafficControlTasksResponseBodyTrafficControlTasks()
                self.traffic_control_tasks.append(temp_model.from_map(k))
        return self


class ListTrafficControlTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTrafficControlTasksResponseBody = None,
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
            temp_model = ListTrafficControlTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OfflineExperimentRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class OfflineExperimentResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
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


class OfflineExperimentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OfflineExperimentResponseBody = None,
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
            temp_model = OfflineExperimentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OfflineExperimentGroupRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class OfflineExperimentGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
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


class OfflineExperimentGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OfflineExperimentGroupResponseBody = None,
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
            temp_model = OfflineExperimentGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OfflineLaboratoryRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class OfflineLaboratoryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
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


class OfflineLaboratoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OfflineLaboratoryResponseBody = None,
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
            temp_model = OfflineLaboratoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OnlineExperimentRequest(TeaModel):
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
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class OnlineExperimentResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
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


class OnlineExperimentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OnlineExperimentResponseBody = None,
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
            temp_model = OnlineExperimentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OnlineExperimentGroupRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class OnlineExperimentGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
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


class OnlineExperimentGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OnlineExperimentGroupResponseBody = None,
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
            temp_model = OnlineExperimentGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OnlineLaboratoryRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class OnlineLaboratoryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
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


class OnlineLaboratoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OnlineLaboratoryResponseBody = None,
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
            temp_model = OnlineLaboratoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PushAllExperimentRequest(TeaModel):
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
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class PushAllExperimentResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
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


class PushAllExperimentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PushAllExperimentResponseBody = None,
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
            temp_model = PushAllExperimentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PushResourceRuleRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        metric_info: Dict[str, Any] = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.metric_info = metric_info

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.metric_info is not None:
            result['MetricInfo'] = self.metric_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MetricInfo') is not None:
            self.metric_info = m.get('MetricInfo')
        return self


class PushResourceRuleShrinkRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        metric_info_shrink: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.metric_info_shrink = metric_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.metric_info_shrink is not None:
            result['MetricInfo'] = self.metric_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MetricInfo') is not None:
            self.metric_info_shrink = m.get('MetricInfo')
        return self


class PushResourceRuleResponseBodyRuleItems(TeaModel):
    def __init__(
        self,
        description: str = None,
        max_value: str = None,
        min_value: str = None,
        name: str = None,
        value: str = None,
    ):
        self.description = description
        self.max_value = max_value
        self.min_value = min_value
        self.name = name
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.max_value is not None:
            result['MaxValue'] = self.max_value
        if self.min_value is not None:
            result['MinValue'] = self.min_value
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('MaxValue') is not None:
            self.max_value = m.get('MaxValue')
        if m.get('MinValue') is not None:
            self.min_value = m.get('MinValue')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class PushResourceRuleResponseBody(TeaModel):
    def __init__(
        self,
        description: str = None,
        metric_operation_type: str = None,
        metric_pull_info: str = None,
        metric_pull_period: str = None,
        name: str = None,
        request_id: str = None,
        resource_rule_id: str = None,
        rule_computing_definition: str = None,
        rule_items: List[PushResourceRuleResponseBodyRuleItems] = None,
    ):
        self.description = description
        self.metric_operation_type = metric_operation_type
        self.metric_pull_info = metric_pull_info
        self.metric_pull_period = metric_pull_period
        self.name = name
        self.request_id = request_id
        self.resource_rule_id = resource_rule_id
        self.rule_computing_definition = rule_computing_definition
        self.rule_items = rule_items

    def validate(self):
        if self.rule_items:
            for k in self.rule_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.metric_operation_type is not None:
            result['MetricOperationType'] = self.metric_operation_type
        if self.metric_pull_info is not None:
            result['MetricPullInfo'] = self.metric_pull_info
        if self.metric_pull_period is not None:
            result['MetricPullPeriod'] = self.metric_pull_period
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_rule_id is not None:
            result['ResourceRuleId'] = self.resource_rule_id
        if self.rule_computing_definition is not None:
            result['RuleComputingDefinition'] = self.rule_computing_definition
        result['RuleItems'] = []
        if self.rule_items is not None:
            for k in self.rule_items:
                result['RuleItems'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('MetricOperationType') is not None:
            self.metric_operation_type = m.get('MetricOperationType')
        if m.get('MetricPullInfo') is not None:
            self.metric_pull_info = m.get('MetricPullInfo')
        if m.get('MetricPullPeriod') is not None:
            self.metric_pull_period = m.get('MetricPullPeriod')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceRuleId') is not None:
            self.resource_rule_id = m.get('ResourceRuleId')
        if m.get('RuleComputingDefinition') is not None:
            self.rule_computing_definition = m.get('RuleComputingDefinition')
        self.rule_items = []
        if m.get('RuleItems') is not None:
            for k in m.get('RuleItems'):
                temp_model = PushResourceRuleResponseBodyRuleItems()
                self.rule_items.append(temp_model.from_map(k))
        return self


class PushResourceRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PushResourceRuleResponseBody = None,
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
            temp_model = PushResourceRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReleaseTrafficControlTaskRequest(TeaModel):
    def __init__(
        self,
        environment: str = None,
        instance_id: str = None,
    ):
        self.environment = environment
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.environment is not None:
            result['Environment'] = self.environment
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Environment') is not None:
            self.environment = m.get('Environment')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ReleaseTrafficControlTaskResponseBody(TeaModel):
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


class ReleaseTrafficControlTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReleaseTrafficControlTaskResponseBody = None,
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
            temp_model = ReleaseTrafficControlTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReportABMetricGroupRequest(TeaModel):
    def __init__(
        self,
        base_experiment_id: str = None,
        dimension_fields: str = None,
        end_date: str = None,
        experiment_group_id: str = None,
        experiment_ids: str = None,
        instance_id: str = None,
        report_type: str = None,
        scene_id: str = None,
        start_date: str = None,
        time_statistics_method: str = None,
    ):
        # This parameter is required.
        self.base_experiment_id = base_experiment_id
        self.dimension_fields = dimension_fields
        self.end_date = end_date
        self.experiment_group_id = experiment_group_id
        # This parameter is required.
        self.experiment_ids = experiment_ids
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.report_type = report_type
        self.scene_id = scene_id
        self.start_date = start_date
        self.time_statistics_method = time_statistics_method

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_experiment_id is not None:
            result['BaseExperimentId'] = self.base_experiment_id
        if self.dimension_fields is not None:
            result['DimensionFields'] = self.dimension_fields
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.experiment_group_id is not None:
            result['ExperimentGroupId'] = self.experiment_group_id
        if self.experiment_ids is not None:
            result['ExperimentIds'] = self.experiment_ids
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.report_type is not None:
            result['ReportType'] = self.report_type
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.time_statistics_method is not None:
            result['TimeStatisticsMethod'] = self.time_statistics_method
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseExperimentId') is not None:
            self.base_experiment_id = m.get('BaseExperimentId')
        if m.get('DimensionFields') is not None:
            self.dimension_fields = m.get('DimensionFields')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('ExperimentGroupId') is not None:
            self.experiment_group_id = m.get('ExperimentGroupId')
        if m.get('ExperimentIds') is not None:
            self.experiment_ids = m.get('ExperimentIds')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ReportType') is not None:
            self.report_type = m.get('ReportType')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('TimeStatisticsMethod') is not None:
            self.time_statistics_method = m.get('TimeStatisticsMethod')
        return self


class ReportABMetricGroupResponseBody(TeaModel):
    def __init__(
        self,
        experiment_report: Dict[str, ExperimentReportValue] = None,
        group_dimension: List[str] = None,
        request_id: str = None,
    ):
        self.experiment_report = experiment_report
        self.group_dimension = group_dimension
        self.request_id = request_id

    def validate(self):
        if self.experiment_report:
            for v in self.experiment_report.values():
                if v:
                    v.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ExperimentReport'] = {}
        if self.experiment_report is not None:
            for k, v in self.experiment_report.items():
                result['ExperimentReport'][k] = v.to_map()
        if self.group_dimension is not None:
            result['GroupDimension'] = self.group_dimension
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.experiment_report = {}
        if m.get('ExperimentReport') is not None:
            for k, v in m.get('ExperimentReport').items():
                temp_model = ExperimentReportValue()
                self.experiment_report[k] = temp_model.from_map(v)
        if m.get('GroupDimension') is not None:
            self.group_dimension = m.get('GroupDimension')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ReportABMetricGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReportABMetricGroupResponseBody = None,
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
            temp_model = ReportABMetricGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SplitTrafficControlTargetRequest(TeaModel):
    def __init__(
        self,
        environment: str = None,
        instance_id: str = None,
        set_values: List[int] = None,
        time_points: List[int] = None,
    ):
        self.environment = environment
        self.instance_id = instance_id
        self.set_values = set_values
        self.time_points = time_points

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.environment is not None:
            result['Environment'] = self.environment
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.set_values is not None:
            result['SetValues'] = self.set_values
        if self.time_points is not None:
            result['TimePoints'] = self.time_points
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Environment') is not None:
            self.environment = m.get('Environment')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SetValues') is not None:
            self.set_values = m.get('SetValues')
        if m.get('TimePoints') is not None:
            self.time_points = m.get('TimePoints')
        return self


class SplitTrafficControlTargetResponseBody(TeaModel):
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


class SplitTrafficControlTargetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SplitTrafficControlTargetResponseBody = None,
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
            temp_model = SplitTrafficControlTargetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartTrafficControlTargetRequest(TeaModel):
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
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class StartTrafficControlTargetResponseBody(TeaModel):
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


class StartTrafficControlTargetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartTrafficControlTargetResponseBody = None,
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
            temp_model = StartTrafficControlTargetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartTrafficControlTaskRequest(TeaModel):
    def __init__(
        self,
        environment: str = None,
        instance_id: str = None,
    ):
        self.environment = environment
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.environment is not None:
            result['Environment'] = self.environment
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Environment') is not None:
            self.environment = m.get('Environment')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class StartTrafficControlTaskResponseBody(TeaModel):
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


class StartTrafficControlTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartTrafficControlTaskResponseBody = None,
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
            temp_model = StartTrafficControlTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopTrafficControlTargetRequest(TeaModel):
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
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class StopTrafficControlTargetResponseBody(TeaModel):
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


class StopTrafficControlTargetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopTrafficControlTargetResponseBody = None,
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
            temp_model = StopTrafficControlTargetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopTrafficControlTaskRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        environment: str = None,
        instance_id: str = None,
    ):
        self.region_id = region_id
        self.environment = environment
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.environment is not None:
            result['Environment'] = self.environment
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Environment') is not None:
            self.environment = m.get('Environment')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class StopTrafficControlTaskResponseBody(TeaModel):
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


class StopTrafficControlTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopTrafficControlTaskResponseBody = None,
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
            temp_model = StopTrafficControlTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SyncFeatureConsistencyCheckJobReplayLogRequest(TeaModel):
    def __init__(
        self,
        context_features: str = None,
        feature_consistency_check_job_config_id: str = None,
        generated_features: str = None,
        instance_id: str = None,
        log_item_id: str = None,
        log_request_id: str = None,
        log_request_time: int = None,
        log_user_id: str = None,
        raw_features: str = None,
        scene_name: str = None,
    ):
        # This parameter is required.
        self.context_features = context_features
        # This parameter is required.
        self.feature_consistency_check_job_config_id = feature_consistency_check_job_config_id
        # This parameter is required.
        self.generated_features = generated_features
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.log_item_id = log_item_id
        # This parameter is required.
        self.log_request_id = log_request_id
        # This parameter is required.
        self.log_request_time = log_request_time
        # This parameter is required.
        self.log_user_id = log_user_id
        # This parameter is required.
        self.raw_features = raw_features
        # This parameter is required.
        self.scene_name = scene_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.context_features is not None:
            result['ContextFeatures'] = self.context_features
        if self.feature_consistency_check_job_config_id is not None:
            result['FeatureConsistencyCheckJobConfigId'] = self.feature_consistency_check_job_config_id
        if self.generated_features is not None:
            result['GeneratedFeatures'] = self.generated_features
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.log_item_id is not None:
            result['LogItemId'] = self.log_item_id
        if self.log_request_id is not None:
            result['LogRequestId'] = self.log_request_id
        if self.log_request_time is not None:
            result['LogRequestTime'] = self.log_request_time
        if self.log_user_id is not None:
            result['LogUserId'] = self.log_user_id
        if self.raw_features is not None:
            result['RawFeatures'] = self.raw_features
        if self.scene_name is not None:
            result['SceneName'] = self.scene_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContextFeatures') is not None:
            self.context_features = m.get('ContextFeatures')
        if m.get('FeatureConsistencyCheckJobConfigId') is not None:
            self.feature_consistency_check_job_config_id = m.get('FeatureConsistencyCheckJobConfigId')
        if m.get('GeneratedFeatures') is not None:
            self.generated_features = m.get('GeneratedFeatures')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('LogItemId') is not None:
            self.log_item_id = m.get('LogItemId')
        if m.get('LogRequestId') is not None:
            self.log_request_id = m.get('LogRequestId')
        if m.get('LogRequestTime') is not None:
            self.log_request_time = m.get('LogRequestTime')
        if m.get('LogUserId') is not None:
            self.log_user_id = m.get('LogUserId')
        if m.get('RawFeatures') is not None:
            self.raw_features = m.get('RawFeatures')
        if m.get('SceneName') is not None:
            self.scene_name = m.get('SceneName')
        return self


class SyncFeatureConsistencyCheckJobReplayLogResponseBody(TeaModel):
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


class SyncFeatureConsistencyCheckJobReplayLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SyncFeatureConsistencyCheckJobReplayLogResponseBody = None,
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
            temp_model = SyncFeatureConsistencyCheckJobReplayLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TerminateFeatureConsistencyCheckJobRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class TerminateFeatureConsistencyCheckJobResponseBody(TeaModel):
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


class TerminateFeatureConsistencyCheckJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TerminateFeatureConsistencyCheckJobResponseBody = None,
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
            temp_model = TerminateFeatureConsistencyCheckJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateABMetricRequest(TeaModel):
    def __init__(
        self,
        definition: str = None,
        description: str = None,
        instance_id: str = None,
        left_metric_id: str = None,
        name: str = None,
        operator: str = None,
        realtime: bool = None,
        result_resource_id: str = None,
        right_metric_id: str = None,
        scene_id: str = None,
        statistics_cycle: int = None,
        table_meta_id: str = None,
        type: str = None,
    ):
        # This parameter is required.
        self.definition = definition
        # This parameter is required.
        self.description = description
        # This parameter is required.
        self.instance_id = instance_id
        self.left_metric_id = left_metric_id
        # This parameter is required.
        self.name = name
        self.operator = operator
        # This parameter is required.
        self.realtime = realtime
        self.result_resource_id = result_resource_id
        self.right_metric_id = right_metric_id
        # This parameter is required.
        self.scene_id = scene_id
        self.statistics_cycle = statistics_cycle
        # This parameter is required.
        self.table_meta_id = table_meta_id
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.definition is not None:
            result['Definition'] = self.definition
        if self.description is not None:
            result['Description'] = self.description
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.left_metric_id is not None:
            result['LeftMetricId'] = self.left_metric_id
        if self.name is not None:
            result['Name'] = self.name
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.realtime is not None:
            result['Realtime'] = self.realtime
        if self.result_resource_id is not None:
            result['ResultResourceId'] = self.result_resource_id
        if self.right_metric_id is not None:
            result['RightMetricId'] = self.right_metric_id
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.statistics_cycle is not None:
            result['StatisticsCycle'] = self.statistics_cycle
        if self.table_meta_id is not None:
            result['TableMetaId'] = self.table_meta_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Definition') is not None:
            self.definition = m.get('Definition')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('LeftMetricId') is not None:
            self.left_metric_id = m.get('LeftMetricId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('Realtime') is not None:
            self.realtime = m.get('Realtime')
        if m.get('ResultResourceId') is not None:
            self.result_resource_id = m.get('ResultResourceId')
        if m.get('RightMetricId') is not None:
            self.right_metric_id = m.get('RightMetricId')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('StatisticsCycle') is not None:
            self.statistics_cycle = m.get('StatisticsCycle')
        if m.get('TableMetaId') is not None:
            self.table_meta_id = m.get('TableMetaId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class UpdateABMetricResponseBody(TeaModel):
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


class UpdateABMetricResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateABMetricResponseBody = None,
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
            temp_model = UpdateABMetricResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateABMetricGroupRequest(TeaModel):
    def __init__(
        self,
        abmetric_ids: str = None,
        description: str = None,
        instance_id: str = None,
        name: str = None,
        realtime: bool = None,
        scene_id: str = None,
    ):
        # This parameter is required.
        self.abmetric_ids = abmetric_ids
        # This parameter is required.
        self.description = description
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.realtime = realtime
        # This parameter is required.
        self.scene_id = scene_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.abmetric_ids is not None:
            result['ABMetricIds'] = self.abmetric_ids
        if self.description is not None:
            result['Description'] = self.description
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        if self.realtime is not None:
            result['Realtime'] = self.realtime
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ABMetricIds') is not None:
            self.abmetric_ids = m.get('ABMetricIds')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Realtime') is not None:
            self.realtime = m.get('Realtime')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        return self


class UpdateABMetricGroupResponseBody(TeaModel):
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


class UpdateABMetricGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateABMetricGroupResponseBody = None,
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
            temp_model = UpdateABMetricGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCrowdRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        instance_id: str = None,
        name: str = None,
    ):
        # This parameter is required.
        self.description = description
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class UpdateCrowdResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
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


class UpdateCrowdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateCrowdResponseBody = None,
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
            temp_model = UpdateCrowdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateExperimentRequest(TeaModel):
    def __init__(
        self,
        config: str = None,
        debug_crowd_id: str = None,
        debug_users: str = None,
        description: str = None,
        flow_percent: int = None,
        instance_id: str = None,
        name: str = None,
        type: str = None,
    ):
        self.config = config
        self.debug_crowd_id = debug_crowd_id
        self.debug_users = debug_users
        # This parameter is required.
        self.description = description
        self.flow_percent = flow_percent
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.debug_crowd_id is not None:
            result['DebugCrowdId'] = self.debug_crowd_id
        if self.debug_users is not None:
            result['DebugUsers'] = self.debug_users
        if self.description is not None:
            result['Description'] = self.description
        if self.flow_percent is not None:
            result['FlowPercent'] = self.flow_percent
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('DebugCrowdId') is not None:
            self.debug_crowd_id = m.get('DebugCrowdId')
        if m.get('DebugUsers') is not None:
            self.debug_users = m.get('DebugUsers')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FlowPercent') is not None:
            self.flow_percent = m.get('FlowPercent')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class UpdateExperimentResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
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


class UpdateExperimentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateExperimentResponseBody = None,
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
            temp_model = UpdateExperimentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateExperimentGroupRequest(TeaModel):
    def __init__(
        self,
        config: str = None,
        crowd_id: str = None,
        crowd_target_type: str = None,
        debug_crowd_id: str = None,
        debug_users: str = None,
        description: str = None,
        distribution_time_duration: int = None,
        distribution_type: str = None,
        filter: str = None,
        instance_id: str = None,
        layer_id: str = None,
        name: str = None,
        need_aa: bool = None,
        random_flow: int = None,
        reservced_buckets: str = None,
    ):
        self.config = config
        self.crowd_id = crowd_id
        self.crowd_target_type = crowd_target_type
        self.debug_crowd_id = debug_crowd_id
        self.debug_users = debug_users
        # This parameter is required.
        self.description = description
        self.distribution_time_duration = distribution_time_duration
        self.distribution_type = distribution_type
        self.filter = filter
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.layer_id = layer_id
        # This parameter is required.
        self.name = name
        self.need_aa = need_aa
        self.random_flow = random_flow
        self.reservced_buckets = reservced_buckets

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.crowd_id is not None:
            result['CrowdId'] = self.crowd_id
        if self.crowd_target_type is not None:
            result['CrowdTargetType'] = self.crowd_target_type
        if self.debug_crowd_id is not None:
            result['DebugCrowdId'] = self.debug_crowd_id
        if self.debug_users is not None:
            result['DebugUsers'] = self.debug_users
        if self.description is not None:
            result['Description'] = self.description
        if self.distribution_time_duration is not None:
            result['DistributionTimeDuration'] = self.distribution_time_duration
        if self.distribution_type is not None:
            result['DistributionType'] = self.distribution_type
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.layer_id is not None:
            result['LayerId'] = self.layer_id
        if self.name is not None:
            result['Name'] = self.name
        if self.need_aa is not None:
            result['NeedAA'] = self.need_aa
        if self.random_flow is not None:
            result['RandomFlow'] = self.random_flow
        if self.reservced_buckets is not None:
            result['ReservcedBuckets'] = self.reservced_buckets
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('CrowdId') is not None:
            self.crowd_id = m.get('CrowdId')
        if m.get('CrowdTargetType') is not None:
            self.crowd_target_type = m.get('CrowdTargetType')
        if m.get('DebugCrowdId') is not None:
            self.debug_crowd_id = m.get('DebugCrowdId')
        if m.get('DebugUsers') is not None:
            self.debug_users = m.get('DebugUsers')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DistributionTimeDuration') is not None:
            self.distribution_time_duration = m.get('DistributionTimeDuration')
        if m.get('DistributionType') is not None:
            self.distribution_type = m.get('DistributionType')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('LayerId') is not None:
            self.layer_id = m.get('LayerId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NeedAA') is not None:
            self.need_aa = m.get('NeedAA')
        if m.get('RandomFlow') is not None:
            self.random_flow = m.get('RandomFlow')
        if m.get('ReservcedBuckets') is not None:
            self.reservced_buckets = m.get('ReservcedBuckets')
        return self


class UpdateExperimentGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
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


class UpdateExperimentGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateExperimentGroupResponseBody = None,
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
            temp_model = UpdateExperimentGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFeatureConsistencyCheckJobConfigRequest(TeaModel):
    def __init__(
        self,
        compare_feature: bool = None,
        eas_service_name: str = None,
        easy_rec_package_path: str = None,
        easy_rec_version: str = None,
        feature_display_exclude: str = None,
        feature_landing_resource_id: str = None,
        feature_priority: str = None,
        feature_store_item_id: str = None,
        feature_store_model_id: str = None,
        feature_store_project_id: str = None,
        feature_store_project_name: str = None,
        feature_store_seq_feature_view: str = None,
        feature_store_user_id: str = None,
        fg_jar_version: str = None,
        fg_json_file_name: str = None,
        generate_zip: bool = None,
        instance_id: str = None,
        is_use_feature_store: bool = None,
        item_id_field: str = None,
        item_table: str = None,
        item_table_partition_field: str = None,
        item_table_partition_field_format: str = None,
        name: str = None,
        oss_resource_id: str = None,
        sample_rate: float = None,
        scene_id: str = None,
        service_id: str = None,
        user_id_field: str = None,
        user_table: str = None,
        user_table_partition_field: str = None,
        user_table_partition_field_format: str = None,
        workflow_name: str = None,
    ):
        # This parameter is required.
        self.compare_feature = compare_feature
        # This parameter is required.
        self.eas_service_name = eas_service_name
        self.easy_rec_package_path = easy_rec_package_path
        self.easy_rec_version = easy_rec_version
        self.feature_display_exclude = feature_display_exclude
        # This parameter is required.
        self.feature_landing_resource_id = feature_landing_resource_id
        self.feature_priority = feature_priority
        self.feature_store_item_id = feature_store_item_id
        self.feature_store_model_id = feature_store_model_id
        self.feature_store_project_id = feature_store_project_id
        self.feature_store_project_name = feature_store_project_name
        self.feature_store_seq_feature_view = feature_store_seq_feature_view
        self.feature_store_user_id = feature_store_user_id
        self.fg_jar_version = fg_jar_version
        # This parameter is required.
        self.fg_json_file_name = fg_json_file_name
        # This parameter is required.
        self.generate_zip = generate_zip
        # This parameter is required.
        self.instance_id = instance_id
        self.is_use_feature_store = is_use_feature_store
        # This parameter is required.
        self.item_id_field = item_id_field
        # This parameter is required.
        self.item_table = item_table
        # This parameter is required.
        self.item_table_partition_field = item_table_partition_field
        # This parameter is required.
        self.item_table_partition_field_format = item_table_partition_field_format
        # This parameter is required.
        self.name = name
        self.oss_resource_id = oss_resource_id
        # This parameter is required.
        self.sample_rate = sample_rate
        # This parameter is required.
        self.scene_id = scene_id
        self.service_id = service_id
        # This parameter is required.
        self.user_id_field = user_id_field
        # This parameter is required.
        self.user_table = user_table
        # This parameter is required.
        self.user_table_partition_field = user_table_partition_field
        # This parameter is required.
        self.user_table_partition_field_format = user_table_partition_field_format
        self.workflow_name = workflow_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compare_feature is not None:
            result['CompareFeature'] = self.compare_feature
        if self.eas_service_name is not None:
            result['EasServiceName'] = self.eas_service_name
        if self.easy_rec_package_path is not None:
            result['EasyRecPackagePath'] = self.easy_rec_package_path
        if self.easy_rec_version is not None:
            result['EasyRecVersion'] = self.easy_rec_version
        if self.feature_display_exclude is not None:
            result['FeatureDisplayExclude'] = self.feature_display_exclude
        if self.feature_landing_resource_id is not None:
            result['FeatureLandingResourceId'] = self.feature_landing_resource_id
        if self.feature_priority is not None:
            result['FeaturePriority'] = self.feature_priority
        if self.feature_store_item_id is not None:
            result['FeatureStoreItemId'] = self.feature_store_item_id
        if self.feature_store_model_id is not None:
            result['FeatureStoreModelId'] = self.feature_store_model_id
        if self.feature_store_project_id is not None:
            result['FeatureStoreProjectId'] = self.feature_store_project_id
        if self.feature_store_project_name is not None:
            result['FeatureStoreProjectName'] = self.feature_store_project_name
        if self.feature_store_seq_feature_view is not None:
            result['FeatureStoreSeqFeatureView'] = self.feature_store_seq_feature_view
        if self.feature_store_user_id is not None:
            result['FeatureStoreUserId'] = self.feature_store_user_id
        if self.fg_jar_version is not None:
            result['FgJarVersion'] = self.fg_jar_version
        if self.fg_json_file_name is not None:
            result['FgJsonFileName'] = self.fg_json_file_name
        if self.generate_zip is not None:
            result['GenerateZip'] = self.generate_zip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.is_use_feature_store is not None:
            result['IsUseFeatureStore'] = self.is_use_feature_store
        if self.item_id_field is not None:
            result['ItemIdField'] = self.item_id_field
        if self.item_table is not None:
            result['ItemTable'] = self.item_table
        if self.item_table_partition_field is not None:
            result['ItemTablePartitionField'] = self.item_table_partition_field
        if self.item_table_partition_field_format is not None:
            result['ItemTablePartitionFieldFormat'] = self.item_table_partition_field_format
        if self.name is not None:
            result['Name'] = self.name
        if self.oss_resource_id is not None:
            result['OssResourceId'] = self.oss_resource_id
        if self.sample_rate is not None:
            result['SampleRate'] = self.sample_rate
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.user_id_field is not None:
            result['UserIdField'] = self.user_id_field
        if self.user_table is not None:
            result['UserTable'] = self.user_table
        if self.user_table_partition_field is not None:
            result['UserTablePartitionField'] = self.user_table_partition_field
        if self.user_table_partition_field_format is not None:
            result['UserTablePartitionFieldFormat'] = self.user_table_partition_field_format
        if self.workflow_name is not None:
            result['WorkflowName'] = self.workflow_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompareFeature') is not None:
            self.compare_feature = m.get('CompareFeature')
        if m.get('EasServiceName') is not None:
            self.eas_service_name = m.get('EasServiceName')
        if m.get('EasyRecPackagePath') is not None:
            self.easy_rec_package_path = m.get('EasyRecPackagePath')
        if m.get('EasyRecVersion') is not None:
            self.easy_rec_version = m.get('EasyRecVersion')
        if m.get('FeatureDisplayExclude') is not None:
            self.feature_display_exclude = m.get('FeatureDisplayExclude')
        if m.get('FeatureLandingResourceId') is not None:
            self.feature_landing_resource_id = m.get('FeatureLandingResourceId')
        if m.get('FeaturePriority') is not None:
            self.feature_priority = m.get('FeaturePriority')
        if m.get('FeatureStoreItemId') is not None:
            self.feature_store_item_id = m.get('FeatureStoreItemId')
        if m.get('FeatureStoreModelId') is not None:
            self.feature_store_model_id = m.get('FeatureStoreModelId')
        if m.get('FeatureStoreProjectId') is not None:
            self.feature_store_project_id = m.get('FeatureStoreProjectId')
        if m.get('FeatureStoreProjectName') is not None:
            self.feature_store_project_name = m.get('FeatureStoreProjectName')
        if m.get('FeatureStoreSeqFeatureView') is not None:
            self.feature_store_seq_feature_view = m.get('FeatureStoreSeqFeatureView')
        if m.get('FeatureStoreUserId') is not None:
            self.feature_store_user_id = m.get('FeatureStoreUserId')
        if m.get('FgJarVersion') is not None:
            self.fg_jar_version = m.get('FgJarVersion')
        if m.get('FgJsonFileName') is not None:
            self.fg_json_file_name = m.get('FgJsonFileName')
        if m.get('GenerateZip') is not None:
            self.generate_zip = m.get('GenerateZip')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IsUseFeatureStore') is not None:
            self.is_use_feature_store = m.get('IsUseFeatureStore')
        if m.get('ItemIdField') is not None:
            self.item_id_field = m.get('ItemIdField')
        if m.get('ItemTable') is not None:
            self.item_table = m.get('ItemTable')
        if m.get('ItemTablePartitionField') is not None:
            self.item_table_partition_field = m.get('ItemTablePartitionField')
        if m.get('ItemTablePartitionFieldFormat') is not None:
            self.item_table_partition_field_format = m.get('ItemTablePartitionFieldFormat')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OssResourceId') is not None:
            self.oss_resource_id = m.get('OssResourceId')
        if m.get('SampleRate') is not None:
            self.sample_rate = m.get('SampleRate')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('UserIdField') is not None:
            self.user_id_field = m.get('UserIdField')
        if m.get('UserTable') is not None:
            self.user_table = m.get('UserTable')
        if m.get('UserTablePartitionField') is not None:
            self.user_table_partition_field = m.get('UserTablePartitionField')
        if m.get('UserTablePartitionFieldFormat') is not None:
            self.user_table_partition_field_format = m.get('UserTablePartitionFieldFormat')
        if m.get('WorkflowName') is not None:
            self.workflow_name = m.get('WorkflowName')
        return self


class UpdateFeatureConsistencyCheckJobConfigResponseBody(TeaModel):
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


class UpdateFeatureConsistencyCheckJobConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateFeatureConsistencyCheckJobConfigResponseBody = None,
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
            temp_model = UpdateFeatureConsistencyCheckJobConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateInstanceResourceRequest(TeaModel):
    def __init__(
        self,
        config: str = None,
        uri: str = None,
    ):
        self.config = config
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.uri is not None:
            result['Uri'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        return self


class UpdateInstanceResourceResponseBody(TeaModel):
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


class UpdateInstanceResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateInstanceResourceResponseBody = None,
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
            temp_model = UpdateInstanceResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateLaboratoryRequest(TeaModel):
    def __init__(
        self,
        bucket_count: int = None,
        bucket_type: str = None,
        buckets: str = None,
        debug_crowd_id: str = None,
        debug_users: str = None,
        description: str = None,
        environment: str = None,
        filter: str = None,
        instance_id: str = None,
        name: str = None,
        type: str = None,
    ):
        self.bucket_count = bucket_count
        # This parameter is required.
        self.bucket_type = bucket_type
        self.buckets = buckets
        self.debug_crowd_id = debug_crowd_id
        self.debug_users = debug_users
        self.description = description
        self.environment = environment
        self.filter = filter
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_count is not None:
            result['BucketCount'] = self.bucket_count
        if self.bucket_type is not None:
            result['BucketType'] = self.bucket_type
        if self.buckets is not None:
            result['Buckets'] = self.buckets
        if self.debug_crowd_id is not None:
            result['DebugCrowdId'] = self.debug_crowd_id
        if self.debug_users is not None:
            result['DebugUsers'] = self.debug_users
        if self.description is not None:
            result['Description'] = self.description
        if self.environment is not None:
            result['Environment'] = self.environment
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketCount') is not None:
            self.bucket_count = m.get('BucketCount')
        if m.get('BucketType') is not None:
            self.bucket_type = m.get('BucketType')
        if m.get('Buckets') is not None:
            self.buckets = m.get('Buckets')
        if m.get('DebugCrowdId') is not None:
            self.debug_crowd_id = m.get('DebugCrowdId')
        if m.get('DebugUsers') is not None:
            self.debug_users = m.get('DebugUsers')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Environment') is not None:
            self.environment = m.get('Environment')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class UpdateLaboratoryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
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


class UpdateLaboratoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateLaboratoryResponseBody = None,
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
            temp_model = UpdateLaboratoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateLayerRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        instance_id: str = None,
        name: str = None,
    ):
        # This parameter is required.
        self.description = description
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class UpdateLayerResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
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


class UpdateLayerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateLayerResponseBody = None,
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
            temp_model = UpdateLayerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateParamRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        value: str = None,
    ):
        self.instance_id = instance_id
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateParamResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
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


class UpdateParamResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateParamResponseBody = None,
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
            temp_model = UpdateParamResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateResourceRuleRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        instance_id: str = None,
        metric_operation_type: str = None,
        metric_pull_info: str = None,
        metric_pull_period: str = None,
        name: str = None,
        rule_computing_definition: str = None,
    ):
        self.description = description
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.metric_operation_type = metric_operation_type
        self.metric_pull_info = metric_pull_info
        self.metric_pull_period = metric_pull_period
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.rule_computing_definition = rule_computing_definition

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.metric_operation_type is not None:
            result['MetricOperationType'] = self.metric_operation_type
        if self.metric_pull_info is not None:
            result['MetricPullInfo'] = self.metric_pull_info
        if self.metric_pull_period is not None:
            result['MetricPullPeriod'] = self.metric_pull_period
        if self.name is not None:
            result['Name'] = self.name
        if self.rule_computing_definition is not None:
            result['RuleComputingDefinition'] = self.rule_computing_definition
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MetricOperationType') is not None:
            self.metric_operation_type = m.get('MetricOperationType')
        if m.get('MetricPullInfo') is not None:
            self.metric_pull_info = m.get('MetricPullInfo')
        if m.get('MetricPullPeriod') is not None:
            self.metric_pull_period = m.get('MetricPullPeriod')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RuleComputingDefinition') is not None:
            self.rule_computing_definition = m.get('RuleComputingDefinition')
        return self


class UpdateResourceRuleResponseBody(TeaModel):
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


class UpdateResourceRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateResourceRuleResponseBody = None,
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
            temp_model = UpdateResourceRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateResourceRuleItemRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        instance_id: str = None,
        max_value: float = None,
        min_value: float = None,
        name: str = None,
        value: float = None,
    ):
        self.description = description
        # This parameter is required.
        self.instance_id = instance_id
        self.max_value = max_value
        self.min_value = min_value
        # This parameter is required.
        self.name = name
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.max_value is not None:
            result['MaxValue'] = self.max_value
        if self.min_value is not None:
            result['MinValue'] = self.min_value
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MaxValue') is not None:
            self.max_value = m.get('MaxValue')
        if m.get('MinValue') is not None:
            self.min_value = m.get('MinValue')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateResourceRuleItemResponseBody(TeaModel):
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


class UpdateResourceRuleItemResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateResourceRuleItemResponseBody = None,
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
            temp_model = UpdateResourceRuleItemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSceneRequestFlows(TeaModel):
    def __init__(
        self,
        flow_code: str = None,
        flow_name: str = None,
    ):
        self.flow_code = flow_code
        self.flow_name = flow_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_code is not None:
            result['FlowCode'] = self.flow_code
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowCode') is not None:
            self.flow_code = m.get('FlowCode')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        return self


class UpdateSceneRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        flows: List[UpdateSceneRequestFlows] = None,
        instance_id: str = None,
        name: str = None,
    ):
        self.description = description
        self.flows = flows
        self.instance_id = instance_id
        self.name = name

    def validate(self):
        if self.flows:
            for k in self.flows:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        result['Flows'] = []
        if self.flows is not None:
            for k in self.flows:
                result['Flows'].append(k.to_map() if k else None)
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        self.flows = []
        if m.get('Flows') is not None:
            for k in m.get('Flows'):
                temp_model = UpdateSceneRequestFlows()
                self.flows.append(temp_model.from_map(k))
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class UpdateSceneResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
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


class UpdateSceneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateSceneResponseBody = None,
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
            temp_model = UpdateSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTableMetaRequestFields(TeaModel):
    def __init__(
        self,
        data_type: str = None,
        is_dimension_field: bool = None,
        is_partition_field: str = None,
        meaning: str = None,
        name: str = None,
        type: str = None,
    ):
        self.data_type = data_type
        # This parameter is required.
        self.is_dimension_field = is_dimension_field
        # This parameter is required.
        self.is_partition_field = is_partition_field
        # This parameter is required.
        self.meaning = meaning
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.is_dimension_field is not None:
            result['IsDimensionField'] = self.is_dimension_field
        if self.is_partition_field is not None:
            result['IsPartitionField'] = self.is_partition_field
        if self.meaning is not None:
            result['Meaning'] = self.meaning
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('IsDimensionField') is not None:
            self.is_dimension_field = m.get('IsDimensionField')
        if m.get('IsPartitionField') is not None:
            self.is_partition_field = m.get('IsPartitionField')
        if m.get('Meaning') is not None:
            self.meaning = m.get('Meaning')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class UpdateTableMetaRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        fields: List[UpdateTableMetaRequestFields] = None,
        instance_id: str = None,
        module: str = None,
        name: str = None,
        resource_id: str = None,
        table_name: str = None,
    ):
        self.description = description
        # This parameter is required.
        self.fields = fields
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.module = module
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.resource_id = resource_id
        # This parameter is required.
        self.table_name = table_name

    def validate(self):
        if self.fields:
            for k in self.fields:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        result['Fields'] = []
        if self.fields is not None:
            for k in self.fields:
                result['Fields'].append(k.to_map() if k else None)
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.module is not None:
            result['Module'] = self.module
        if self.name is not None:
            result['Name'] = self.name
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        self.fields = []
        if m.get('Fields') is not None:
            for k in m.get('Fields'):
                temp_model = UpdateTableMetaRequestFields()
                self.fields.append(temp_model.from_map(k))
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Module') is not None:
            self.module = m.get('Module')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class UpdateTableMetaResponseBody(TeaModel):
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


class UpdateTableMetaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateTableMetaResponseBody = None,
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
            temp_model = UpdateTableMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTrafficControlTargetRequest(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        event: str = None,
        item_condition_array: str = None,
        item_condition_express: str = None,
        item_condition_type: str = None,
        name: str = None,
        new_product_regulation: bool = None,
        recall_name: str = None,
        start_time: str = None,
        statis_period: str = None,
        status: str = None,
        tolerance_value: int = None,
        value: float = None,
        new_param_3: str = None,
    ):
        self.end_time = end_time
        self.event = event
        self.item_condition_array = item_condition_array
        self.item_condition_express = item_condition_express
        self.item_condition_type = item_condition_type
        self.name = name
        self.new_product_regulation = new_product_regulation
        self.recall_name = recall_name
        self.start_time = start_time
        self.statis_period = statis_period
        self.status = status
        self.tolerance_value = tolerance_value
        self.value = value
        self.new_param_3 = new_param_3

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.event is not None:
            result['Event'] = self.event
        if self.item_condition_array is not None:
            result['ItemConditionArray'] = self.item_condition_array
        if self.item_condition_express is not None:
            result['ItemConditionExpress'] = self.item_condition_express
        if self.item_condition_type is not None:
            result['ItemConditionType'] = self.item_condition_type
        if self.name is not None:
            result['Name'] = self.name
        if self.new_product_regulation is not None:
            result['NewProductRegulation'] = self.new_product_regulation
        if self.recall_name is not None:
            result['RecallName'] = self.recall_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.statis_period is not None:
            result['StatisPeriod'] = self.statis_period
        if self.status is not None:
            result['Status'] = self.status
        if self.tolerance_value is not None:
            result['ToleranceValue'] = self.tolerance_value
        if self.value is not None:
            result['Value'] = self.value
        if self.new_param_3 is not None:
            result['new-param-3'] = self.new_param_3
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Event') is not None:
            self.event = m.get('Event')
        if m.get('ItemConditionArray') is not None:
            self.item_condition_array = m.get('ItemConditionArray')
        if m.get('ItemConditionExpress') is not None:
            self.item_condition_express = m.get('ItemConditionExpress')
        if m.get('ItemConditionType') is not None:
            self.item_condition_type = m.get('ItemConditionType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NewProductRegulation') is not None:
            self.new_product_regulation = m.get('NewProductRegulation')
        if m.get('RecallName') is not None:
            self.recall_name = m.get('RecallName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StatisPeriod') is not None:
            self.statis_period = m.get('StatisPeriod')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ToleranceValue') is not None:
            self.tolerance_value = m.get('ToleranceValue')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('new-param-3') is not None:
            self.new_param_3 = m.get('new-param-3')
        return self


class UpdateTrafficControlTargetResponseBody(TeaModel):
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


class UpdateTrafficControlTargetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateTrafficControlTargetResponseBody = None,
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
            temp_model = UpdateTrafficControlTargetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTrafficControlTaskRequestTrafficControlTargets(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        event: str = None,
        item_condition_array: str = None,
        item_condition_express: str = None,
        item_condition_type: str = None,
        name: str = None,
        new_product_regulation: bool = None,
        recall_name: str = None,
        start_time: str = None,
        statis_period: str = None,
        status: str = None,
        tolerance_value: int = None,
        value: float = None,
    ):
        self.end_time = end_time
        self.event = event
        self.item_condition_array = item_condition_array
        self.item_condition_express = item_condition_express
        self.item_condition_type = item_condition_type
        self.name = name
        self.new_product_regulation = new_product_regulation
        self.recall_name = recall_name
        self.start_time = start_time
        self.statis_period = statis_period
        self.status = status
        self.tolerance_value = tolerance_value
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.event is not None:
            result['Event'] = self.event
        if self.item_condition_array is not None:
            result['ItemConditionArray'] = self.item_condition_array
        if self.item_condition_express is not None:
            result['ItemConditionExpress'] = self.item_condition_express
        if self.item_condition_type is not None:
            result['ItemConditionType'] = self.item_condition_type
        if self.name is not None:
            result['Name'] = self.name
        if self.new_product_regulation is not None:
            result['NewProductRegulation'] = self.new_product_regulation
        if self.recall_name is not None:
            result['RecallName'] = self.recall_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.statis_period is not None:
            result['StatisPeriod'] = self.statis_period
        if self.status is not None:
            result['Status'] = self.status
        if self.tolerance_value is not None:
            result['ToleranceValue'] = self.tolerance_value
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Event') is not None:
            self.event = m.get('Event')
        if m.get('ItemConditionArray') is not None:
            self.item_condition_array = m.get('ItemConditionArray')
        if m.get('ItemConditionExpress') is not None:
            self.item_condition_express = m.get('ItemConditionExpress')
        if m.get('ItemConditionType') is not None:
            self.item_condition_type = m.get('ItemConditionType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NewProductRegulation') is not None:
            self.new_product_regulation = m.get('NewProductRegulation')
        if m.get('RecallName') is not None:
            self.recall_name = m.get('RecallName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StatisPeriod') is not None:
            self.statis_period = m.get('StatisPeriod')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ToleranceValue') is not None:
            self.tolerance_value = m.get('ToleranceValue')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateTrafficControlTaskRequest(TeaModel):
    def __init__(
        self,
        behavior_table_meta_id: str = None,
        control_granularity: str = None,
        control_logic: str = None,
        control_type: str = None,
        description: str = None,
        end_time: str = None,
        execution_time: str = None,
        instance_id: str = None,
        item_condition_array: str = None,
        item_condition_express: str = None,
        item_condition_type: str = None,
        item_table_meta_id: str = None,
        name: str = None,
        scene_id: str = None,
        start_time: str = None,
        statis_baeavior_condition_array: str = None,
        statis_behavior_condition_express: str = None,
        statis_behavior_condition_type: str = None,
        traffic_control_targets: List[UpdateTrafficControlTaskRequestTrafficControlTargets] = None,
        user_condition_array: str = None,
        user_condition_express: str = None,
        user_condition_type: str = None,
        user_table_meta_id: str = None,
    ):
        self.behavior_table_meta_id = behavior_table_meta_id
        self.control_granularity = control_granularity
        self.control_logic = control_logic
        self.control_type = control_type
        self.description = description
        self.end_time = end_time
        self.execution_time = execution_time
        self.instance_id = instance_id
        self.item_condition_array = item_condition_array
        self.item_condition_express = item_condition_express
        self.item_condition_type = item_condition_type
        self.item_table_meta_id = item_table_meta_id
        self.name = name
        self.scene_id = scene_id
        self.start_time = start_time
        self.statis_baeavior_condition_array = statis_baeavior_condition_array
        self.statis_behavior_condition_express = statis_behavior_condition_express
        self.statis_behavior_condition_type = statis_behavior_condition_type
        self.traffic_control_targets = traffic_control_targets
        self.user_condition_array = user_condition_array
        self.user_condition_express = user_condition_express
        self.user_condition_type = user_condition_type
        self.user_table_meta_id = user_table_meta_id

    def validate(self):
        if self.traffic_control_targets:
            for k in self.traffic_control_targets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.behavior_table_meta_id is not None:
            result['BehaviorTableMetaId'] = self.behavior_table_meta_id
        if self.control_granularity is not None:
            result['ControlGranularity'] = self.control_granularity
        if self.control_logic is not None:
            result['ControlLogic'] = self.control_logic
        if self.control_type is not None:
            result['ControlType'] = self.control_type
        if self.description is not None:
            result['Description'] = self.description
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.execution_time is not None:
            result['ExecutionTime'] = self.execution_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.item_condition_array is not None:
            result['ItemConditionArray'] = self.item_condition_array
        if self.item_condition_express is not None:
            result['ItemConditionExpress'] = self.item_condition_express
        if self.item_condition_type is not None:
            result['ItemConditionType'] = self.item_condition_type
        if self.item_table_meta_id is not None:
            result['ItemTableMetaId'] = self.item_table_meta_id
        if self.name is not None:
            result['Name'] = self.name
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.statis_baeavior_condition_array is not None:
            result['StatisBaeaviorConditionArray'] = self.statis_baeavior_condition_array
        if self.statis_behavior_condition_express is not None:
            result['StatisBehaviorConditionExpress'] = self.statis_behavior_condition_express
        if self.statis_behavior_condition_type is not None:
            result['StatisBehaviorConditionType'] = self.statis_behavior_condition_type
        result['TrafficControlTargets'] = []
        if self.traffic_control_targets is not None:
            for k in self.traffic_control_targets:
                result['TrafficControlTargets'].append(k.to_map() if k else None)
        if self.user_condition_array is not None:
            result['UserConditionArray'] = self.user_condition_array
        if self.user_condition_express is not None:
            result['UserConditionExpress'] = self.user_condition_express
        if self.user_condition_type is not None:
            result['UserConditionType'] = self.user_condition_type
        if self.user_table_meta_id is not None:
            result['UserTableMetaId'] = self.user_table_meta_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BehaviorTableMetaId') is not None:
            self.behavior_table_meta_id = m.get('BehaviorTableMetaId')
        if m.get('ControlGranularity') is not None:
            self.control_granularity = m.get('ControlGranularity')
        if m.get('ControlLogic') is not None:
            self.control_logic = m.get('ControlLogic')
        if m.get('ControlType') is not None:
            self.control_type = m.get('ControlType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ExecutionTime') is not None:
            self.execution_time = m.get('ExecutionTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ItemConditionArray') is not None:
            self.item_condition_array = m.get('ItemConditionArray')
        if m.get('ItemConditionExpress') is not None:
            self.item_condition_express = m.get('ItemConditionExpress')
        if m.get('ItemConditionType') is not None:
            self.item_condition_type = m.get('ItemConditionType')
        if m.get('ItemTableMetaId') is not None:
            self.item_table_meta_id = m.get('ItemTableMetaId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StatisBaeaviorConditionArray') is not None:
            self.statis_baeavior_condition_array = m.get('StatisBaeaviorConditionArray')
        if m.get('StatisBehaviorConditionExpress') is not None:
            self.statis_behavior_condition_express = m.get('StatisBehaviorConditionExpress')
        if m.get('StatisBehaviorConditionType') is not None:
            self.statis_behavior_condition_type = m.get('StatisBehaviorConditionType')
        self.traffic_control_targets = []
        if m.get('TrafficControlTargets') is not None:
            for k in m.get('TrafficControlTargets'):
                temp_model = UpdateTrafficControlTaskRequestTrafficControlTargets()
                self.traffic_control_targets.append(temp_model.from_map(k))
        if m.get('UserConditionArray') is not None:
            self.user_condition_array = m.get('UserConditionArray')
        if m.get('UserConditionExpress') is not None:
            self.user_condition_express = m.get('UserConditionExpress')
        if m.get('UserConditionType') is not None:
            self.user_condition_type = m.get('UserConditionType')
        if m.get('UserTableMetaId') is not None:
            self.user_table_meta_id = m.get('UserTableMetaId')
        return self


class UpdateTrafficControlTaskResponseBody(TeaModel):
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


class UpdateTrafficControlTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateTrafficControlTaskResponseBody = None,
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
            temp_model = UpdateTrafficControlTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTrafficControlTaskTrafficRequestTraffics(TeaModel):
    def __init__(
        self,
        item_or_experiment_id: str = None,
        record_time: str = None,
        traffic_control_target_aim_traffic: float = None,
        traffic_control_target_id: str = None,
        traffic_control_target_traffic: int = None,
        traffic_control_task_traffic: int = None,
    ):
        self.item_or_experiment_id = item_or_experiment_id
        self.record_time = record_time
        self.traffic_control_target_aim_traffic = traffic_control_target_aim_traffic
        self.traffic_control_target_id = traffic_control_target_id
        self.traffic_control_target_traffic = traffic_control_target_traffic
        self.traffic_control_task_traffic = traffic_control_task_traffic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.item_or_experiment_id is not None:
            result['ItemOrExperimentId'] = self.item_or_experiment_id
        if self.record_time is not None:
            result['RecordTime'] = self.record_time
        if self.traffic_control_target_aim_traffic is not None:
            result['TrafficControlTargetAimTraffic'] = self.traffic_control_target_aim_traffic
        if self.traffic_control_target_id is not None:
            result['TrafficControlTargetId'] = self.traffic_control_target_id
        if self.traffic_control_target_traffic is not None:
            result['TrafficControlTargetTraffic'] = self.traffic_control_target_traffic
        if self.traffic_control_task_traffic is not None:
            result['TrafficControlTaskTraffic'] = self.traffic_control_task_traffic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ItemOrExperimentId') is not None:
            self.item_or_experiment_id = m.get('ItemOrExperimentId')
        if m.get('RecordTime') is not None:
            self.record_time = m.get('RecordTime')
        if m.get('TrafficControlTargetAimTraffic') is not None:
            self.traffic_control_target_aim_traffic = m.get('TrafficControlTargetAimTraffic')
        if m.get('TrafficControlTargetId') is not None:
            self.traffic_control_target_id = m.get('TrafficControlTargetId')
        if m.get('TrafficControlTargetTraffic') is not None:
            self.traffic_control_target_traffic = m.get('TrafficControlTargetTraffic')
        if m.get('TrafficControlTaskTraffic') is not None:
            self.traffic_control_task_traffic = m.get('TrafficControlTaskTraffic')
        return self


class UpdateTrafficControlTaskTrafficRequest(TeaModel):
    def __init__(
        self,
        environment: str = None,
        instance_id: str = None,
        traffics: List[UpdateTrafficControlTaskTrafficRequestTraffics] = None,
        new_param_3: str = None,
    ):
        self.environment = environment
        self.instance_id = instance_id
        self.traffics = traffics
        self.new_param_3 = new_param_3

    def validate(self):
        if self.traffics:
            for k in self.traffics:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.environment is not None:
            result['Environment'] = self.environment
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        result['Traffics'] = []
        if self.traffics is not None:
            for k in self.traffics:
                result['Traffics'].append(k.to_map() if k else None)
        if self.new_param_3 is not None:
            result['new-param-3'] = self.new_param_3
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Environment') is not None:
            self.environment = m.get('Environment')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        self.traffics = []
        if m.get('Traffics') is not None:
            for k in m.get('Traffics'):
                temp_model = UpdateTrafficControlTaskTrafficRequestTraffics()
                self.traffics.append(temp_model.from_map(k))
        if m.get('new-param-3') is not None:
            self.new_param_3 = m.get('new-param-3')
        return self


class UpdateTrafficControlTaskTrafficResponseBody(TeaModel):
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


class UpdateTrafficControlTaskTrafficResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateTrafficControlTaskTrafficResponseBody = None,
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
            temp_model = UpdateTrafficControlTaskTrafficResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UploadRecommendationDataRequestContent(TeaModel):
    def __init__(
        self,
        fields: str = None,
        operation_type: str = None,
    ):
        self.fields = fields
        self.operation_type = operation_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fields is not None:
            result['Fields'] = self.fields
        if self.operation_type is not None:
            result['OperationType'] = self.operation_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Fields') is not None:
            self.fields = m.get('Fields')
        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')
        return self


class UploadRecommendationDataRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        content: List[UploadRecommendationDataRequestContent] = None,
        data_type: str = None,
    ):
        self.region_id = region_id
        self.content = content
        self.data_type = data_type

    def validate(self):
        if self.content:
            for k in self.content:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        result['Content'] = []
        if self.content is not None:
            for k in self.content:
                result['Content'].append(k.to_map() if k else None)
        if self.data_type is not None:
            result['DataType'] = self.data_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        self.content = []
        if m.get('Content') is not None:
            for k in m.get('Content'):
                temp_model = UploadRecommendationDataRequestContent()
                self.content.append(temp_model.from_map(k))
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        return self


class UploadRecommendationDataResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
    ):
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UploadRecommendationDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UploadRecommendationDataResponseBody = None,
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
            temp_model = UploadRecommendationDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


